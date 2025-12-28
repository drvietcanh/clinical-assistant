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
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị triệu chứng: ngừng thuốc, điều trị đau đầu, kích thích, mất ngủ, rối loạn tiêu hóa."
        },
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
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là ngừng thuốc và điều trị hỗ trợ. Nếu có chảy máu: điều trị chảy máu (truyền máu, vitamin K nếu cần, ngừng các thuốc chống đông/kháng tiểu cầu)."
        },
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
    
    "Cerebrolysin": {
        "group": "Neurology - Neuropeptide preparation (Stroke adjunct / Neurorecovery, controversial evidence)",
        "vietnamese_name": "Cerebrolysin",
        "administration": ["IV"],
        "indications": [
            "Đột quỵ thiếu máu não giai đoạn bán cấp – điều trị hỗ trợ hồi phục chức năng (off-label tại nhiều guideline)",
            "Chấn thương sọ não (TBI) – hỗ trợ phục hồi",
            "Một số rối loạn nhận thức/sa sút trí tuệ (bằng chứng hạn chế)",
        ],
        "contraindications": [
            "Động kinh chưa kiểm soát",
            "Trạng thái động kinh",
            "Suy thận cấp nặng",
            "Dị ứng với protein nguồn gốc lợn",
        ],
        "dosage": {
            "adult_stroke_iv": "10–50ml/ngày pha trong 100ml NaCl 0.9%, truyền tĩnh mạch chậm trong 30–60 phút, 10–20 ngày",
            "adult_tbi_iv": "10–50ml/ngày x 10–20 ngày",
            "course_repeat": "Có thể lặp lại sau 1–2 tháng tùy đáp ứng lâm sàng",
            "notes": "Không tiêm bolus trực tiếp nhanh. Luôn pha loãng và truyền chậm. Là thuốc hỗ trợ, KHÔNG thay thế điều trị chuẩn đột quỵ (tái tưới máu, chống kết tập tiểu cầu/chống đông, statin, kiểm soát HA, phục hồi chức năng).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh",
            "30_60": "Thận trọng, theo dõi thể tích dịch",
            "under_30": "Thận trọng cao, cân nhắc tránh dùng do dữ liệu hạn chế",
        },
        "side_effects": [
            "Đỏ bừng, nóng mặt trong khi truyền",
            "Nhức đầu",
            "Kích thích, bứt rứt, mất ngủ (ít gặp)",
            "Buồn nôn, nôn",
            "Co giật ở bệnh nhân có ngưỡng co giật thấp (hiếm)",
            "Phản ứng quá mẫn (phát ban, khó thở – rất hiếm)",
        ],
        "interactions": [
            "Thuốc hướng thần kinh (SSRI, SNRI, TCA, antipsychotic): có thể tăng kích thích nhẹ – theo dõi lâm sàng",
            "Không có tương tác dược động học lớn được chứng minh rõ; chủ yếu thận trọng khi phối hợp nhiều thuốc hướng thần kinh.",
        ],
        "pregnancy": "C – dữ liệu hạn chế, tránh dùng nếu không thực sự cần",
        "mechanism_of_action": (
            "Cerebrolysin là hỗn hợp peptide trọng lượng phân tử thấp và acid amin từ não lợn đã qua xử lý, "
            "được cho là có hoạt tính giống yếu tố dinh dưỡng thần kinh (neurotrophic-like), "
            "chống độc glutamate, giảm độc tính kích thích, tăng sống sót tế bào thần kinh và hỗ trợ tái tổ chức synapse. "
            "Một số RCT nhỏ cho thấy cải thiện điểm số chức năng sau đột quỵ/TBI, nhưng kết quả không đồng nhất "
            "và hiện chưa được coi là điều trị chuẩn trong đa số guideline đột quỵ châu Âu/US."
        ),
        "monitoring": [
            "Huyết áp, mạch, nhịp thở trong khi truyền",
            "Triệu chứng thần kinh (tri giác, thang điểm NIHSS, chức năng vận động)",
            "Dấu hiệu kích thích, mất ngủ",
            "Dấu hiệu phản vệ/ quá mẫn trong lần truyền đầu",
        ],
        "precautions": [
            "Luôn kết hợp với điều trị chuẩn đột quỵ, KHÔNG trì hoãn tái tưới máu hoặc can thiệp mạch vì dùng Cerebrolysin.",
            "Thận trọng ở bệnh nhân có tiền sử động kinh hoặc co giật.",
            "Thận trọng ở bệnh nhân suy thận nặng (tích lũy peptide, dữ liệu hạn chế).",
        ],
        "pharmacokinetics": {
            "half_life": "Các peptide thành phần có half-life ngắn; tác dụng được cho là kéo dài qua điều hòa quá trình sửa chữa thần kinh.",
            "onset": "Vài ngày đến vài tuần (đánh giá qua phục hồi chức năng)",
            "duration": "Hiệu ứng kéo dài sau khi kết thúc đợt điều trị do tác động lên quá trình sửa chữa thần kinh.",
            "protein_binding": "Không xác định (hỗn hợp peptide)",
            "clearance": "Chuyển hóa bởi peptidase, thải trừ qua thận.",
        },
        "storage": "Bảo quản ở 2–8°C, tránh ánh sáng. Không đông lạnh. Dùng ngay sau khi pha.",
        "black_box_warnings": None,
        "drug_interactions_detail": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Động kinh chưa kiểm soát",
                "Trạng thái động kinh",
                "Dị ứng với Cerebrolysin hoặc protein nguồn gốc lợn",
            ],
            "tương_đối": [
                "Suy thận nặng",
                "Tiền sử co giật",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Thiếu dữ liệu an toàn trên người; tránh dùng thường quy trong thai kỳ, chỉ cân nhắc nếu lợi ích vượt trội nguy cơ trong bối cảnh đột quỵ nặng.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ; là peptide nên nếu hấp thu đường tiêu hóa của trẻ thường rất thấp, nhưng vẫn nên thận trọng.",
                "recommendation": "Nếu cần dùng cho mẹ cho con bú, cân nhắc tạm ngưng cho bú trong những ngày điều trị hoặc theo dõi sát trẻ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Thận trọng, dữ liệu hạn chế",
            "severe": "Thận trọng, cân nhắc tránh dùng nếu không cần thiết",
            "notes": "Chuyển hóa chủ yếu qua peptidase toàn thân; suy gan có thể ít ảnh hưởng hơn suy thận.",
        },
        "overdose_management": {
            "symptoms": [
                "Kích thích, mất ngủ",
                "Đỏ bừng, nhức đầu",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng truyền thuốc",
                "Điều trị triệu chứng, theo dõi sinh hiệu và thần kinh",
            ],
            "monitoring": "Theo dõi huyết áp, mạch, tri giác; điều chỉnh tốc độ hoặc ngừng truyền nếu cần.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp từ ống/lọ, pha loãng trong NaCl 0.9% (thường 100ml) trước khi truyền.",
                "infusion_rate": "Truyền tĩnh mạch chậm trong 30–60 phút; KHÔNG tiêm bolus nhanh.",
                "compatibility": ["NaCl 0.9%"],
                "incompatibility": [
                    "Dung dịch chứa amino acid liều cao khác (tương kỵ về vật lý/hóa học có thể xảy ra)",
                ],
                "notes": "Không trộn với thuốc khác trong cùng dây truyền. Quan sát bệnh nhân trong lần truyền đầu để phát hiện phản ứng quá mẫn.",
            },
        },
        "references": {
            "primary_sources": [
                "Một số RCT về Cerebrolysin trong đột quỵ và TBI (kết quả không đồng nhất)",
                "ESO/AHA-ASA stroke guidelines: Cerebrolysin không phải điều trị chuẩn, có thể được xem là thử nghiệm/adjunct ở một số trung tâm.",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "Low–Moderate (thuốc hỗ trợ, không thay thế điều trị chuẩn)",
        },
    },
    
    "Nicergoline": {
        "group": "Neurology - Ergot-derived cerebral vasodilator",
        "vietnamese_name": "Nicergoline",
        "administration": ["PO"],
        "indications": [
            "Rối loạn tuần hoàn não mạn (chóng mặt, suy giảm nhận thức nhẹ) – bằng chứng hạn chế",
            "Rối loạn tuần hoàn ngoại vi (Raynaud, bệnh mạch ngoại vi) – hỗ trợ",
        ],
        "contraindications": [
            "Nhồi máu cơ tim cấp, xuất huyết cấp",
            "Tụt huyết áp nặng",
            "Dị ứng ergot derivatives",
        ],
        "dosage": {
            "adult_po": "5–10mg x 3 lần/ngày, uống sau ăn",
            "notes": "Tăng liều dần; đánh giá sau 4–8 tuần.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh",
            "30_60": "Thận trọng",
            "under_30": "Tránh hoặc giảm liều (dữ liệu hạn chế)",
        },
        "side_effects": [
            "Đỏ mặt, tụt huyết áp tư thế",
            "Rối loạn tiêu hóa",
            "Tăng acid uric (hiếm, do chuyển hóa) – thận trọng ở gout",
            "Xơ hóa sau phúc mạc (rất hiếm, nguy cơ class ergot khi dùng kéo dài liều cao)",
        ],
        "interactions": [
            "Thuốc hạ huyết áp: tăng nguy cơ tụt huyết áp",
            "Chống đông/kháng tiểu cầu: lý thuyết tăng chảy máu (hiếm)",
        ],
        "pregnancy": "C – tránh dùng thường quy",
        "mechanism_of_action": "Dẫn xuất ergot, gây giãn mạch não và cải thiện vi tuần hoàn, có thêm tác dụng đối kháng alpha-adrenergic nhẹ.",
        "monitoring": [
            "Huyết áp (tụt HA tư thế)",
            "Acid uric nếu có tiền sử gout",
        ],
        "precautions": [
            "Không dùng kéo dài liều cao; thận trọng nguy cơ xơ hóa (rất hiếm).",
            "Đánh giá đáp ứng sau 1–2 tháng; ngừng nếu không cải thiện.",
        ],
        "pharmacokinetics": {
            "half_life": "8–12 giờ (metabolites lâu hơn)",
            "onset": "vài ngày–tuần",
            "duration": "Liên quan T1/2 và tích lũy chuyển hóa",
            "protein_binding": "Cao",
            "clearance": "Gan (chuyển hóa), thận (thải trừ metabolites)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ẩm và ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions_detail": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc hạ huyết áp",
                    "mechanism": "Tác dụng giãn mạch cộng hưởng",
                    "effect": "Tụt huyết áp tư thế",
                    "management": "Theo dõi HA, giảm liều nếu cần.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["NMCT cấp", "Xuất huyết cấp", "Dị ứng ergot"],
            "tương_đối": ["Hạ HA tư thế", "Gout hoặc tăng acid uric"],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế; tránh dùng thường quy.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết sữa; tránh dùng nếu có thể.",
                "recommendation": "Ưu tiên thuốc khác an toàn hơn.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Thận trọng",
            "severe": "Tránh hoặc giảm liều (dữ liệu hạn chế)",
        },
        "overdose_management": {
            "symptoms": ["Tụt HA, chóng mặt, buồn nôn"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Nâng HA, bù dịch, điều trị triệu chứng"],
            "monitoring": "HA, mạch, ý thức",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống sau ăn để giảm kích ứng dạ dày",
                "timing": "Chia 2–3 lần/ngày; tránh dùng cùng rượu.",
            }
        },
        "references": {
            "primary_sources": [
                "Drug monographs nicergoline",
                "Thực hành lâm sàng tại EU/Asia (bằng chứng hạn chế)",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "Low–Moderate (bằng chứng hạn chế, không phải chuẩn guideline)",
        },
    },
    
    "Edaravone": {
        "group": "Neurology - Free-radical scavenger (AIS adjunct, Japan guideline)",
        "vietnamese_name": "Edaravone",
        "administration": ["IV"],
        "indications": [
            "Đột quỵ thiếu máu não cấp (AIS) trong 24 giờ đầu – thuốc hỗ trợ, không thay thế tái tưới máu",
            "Bệnh nhân đột quỵ có chống chỉ định tái tưới máu hoặc đang chờ can thiệp",
        ],
        "contraindications": [
            "Quá mẫn với edaravone hoặc sulfite",
            "Tiền sử phản vệ với edaravone",
            "Suy thận nặng (nguy cơ tích lũy)",
        ],
        "dosage": {
            "adult_ais_iv": "30mg IV truyền trong 30 phút, mỗi 12 giờ, liên tục 14 ngày (bắt đầu càng sớm càng tốt trong 24 giờ đầu)",
            "notes": "Pha 30mg vào 100ml NaCl 0.9%, truyền 30 phút; không pha chung với thuốc khác.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh",
            "30_60": "Thận trọng, theo dõi creatinine",
            "under_30": "Tránh/không khuyến cáo do nguy cơ tích lũy",
        },
        "side_effects": [
            "Tăng men gan, tăng creatinine hoặc tổn thương thận cấp",
            "Phản vệ, phù mạch (hiếm nhưng nghiêm trọng)",
            "Phát ban, mẩn đỏ",
            "Buồn nôn, nôn",
            "Chóng mặt, nhức đầu",
        ],
        "interactions": [
            "Thuốc chống kết tập tiểu cầu/kháng đông: lý thuyết tăng nguy cơ chảy máu khi phối hợp trong AIS",
            "Thuốc độc thận (aminoglycoside, amphotericin B, NSAID liều cao): có thể tăng nguy cơ tổn thương thận",
        ],
        "pregnancy": "C – dữ liệu hạn chế; chỉ dùng nếu lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Edaravone là chất quét gốc tự do (free-radical scavenger), giảm stress oxy hóa, "
            "ức chế peroxid hóa lipid màng tế bào thần kinh sau thiếu máu, bảo vệ nội mô và hàng rào máu não. "
            "Mục tiêu là hạn chế tiến triển vùng penumbra trong AIS."
        ),
        "monitoring": [
            "Chức năng thận (creatinine, BUN)",
            "Men gan",
            "Dấu hiệu phản vệ trong và sau truyền (mạch, HA, khó thở, phát ban)",
            "Triệu chứng thần kinh (NIHSS, ý thức)",
        ],
        "precautions": [
            "KHÔNG trì hoãn tái tưới máu (alteplase/tenecteplase, EVT) vì edaravone.",
            "Ngừng ngay nếu có dấu hiệu phản vệ hoặc tăng creatinine nhanh.",
            "Thận trọng khi phối hợp nhiều thuốc độc thận.",
        ],
        "pharmacokinetics": {
            "half_life": "0.5–1.5 giờ",
            "onset": "Trong ngày đầu điều trị (tác dụng bảo vệ tế bào thần kinh lý thuyết)",
            "duration": "Ngắn, nhưng có thể tích lũy nếu suy thận",
            "protein_binding": "Edaravone ~92% gắn protein",
            "clearance": "Gan và thận; chuyển hóa thành sulfate/glucuronide thải qua thận",
        },
        "storage": "Bảo quản 20–25°C, tránh ánh sáng. Dùng ngay sau khi pha loãng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc độc thận (aminoglycoside, amphotericin B, NSAID liều cao)",
                    "mechanism": "Cộng hưởng gây tổn thương thận",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Theo dõi creatinine; tránh phối hợp nếu có thể.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn với edaravone hoặc sulfite",
                "Tiền sử phản vệ với edaravone",
                "Suy thận nặng (CrCl <30 ml/phút) hoặc đang lọc máu",
            ],
            "tương_đối": [
                "Suy gan trung bình-nặng",
                "Đang dùng nhiều thuốc độc thận",
                "Tiền sử dị ứng nhiều thuốc",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu người rất hạn chế; chỉ cân nhắc nếu lợi ích rõ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa; ưu tiên tránh hoặc theo dõi trẻ nếu phải dùng.",
                "recommendation": "Tránh nếu không bắt buộc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều, theo dõi men gan",
            "moderate": "Thận trọng, theo dõi sát men gan",
            "severe": "Tránh do dữ liệu hạn chế",
        },
        "overdose_management": {
            "symptoms": ["Tụt huyết áp, buồn nôn, phản vệ, tăng creatinine"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng truyền ngay",
                "Hỗ trợ hô hấp, tuần hoàn nếu phản vệ",
                "Bù dịch, theo dõi creatinine; lọc máu nếu suy thận nặng",
            ],
            "monitoring": "HA, mạch, SpO2, chức năng thận, men gan",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là ngừng truyền ngay, hỗ trợ hô hấp và tuần hoàn nếu phản vệ, bù dịch, theo dõi creatinine. Lọc máu nếu suy thận nặng."
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 30mg vào 100ml NaCl 0.9%",
                "infusion_rate": "Truyền tĩnh mạch trong 30 phút, mỗi 12 giờ",
                "compatibility": ["NS"],
                "incompatibility": ["Không pha chung với thuốc khác trong cùng đường truyền"],
                "notes": "Bắt đầu càng sớm càng tốt trong 24 giờ đầu AIS; duy trì đủ 14 ngày nếu dung nạp.",
            }
        },
        "references": {
            "primary_sources": [
                "Japan Stroke Society Guidelines on edaravone (AIS adjunct)",
                "Nghiên cứu MPSS/edaravone AIS tại Nhật (giảm tiến triển NIHSS ở một số phân tích)",
                "UpToDate/Drug monograph - Edaravone",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "Moderate (nhật có khuyến cáo, chưa phải chuẩn toàn cầu)",
        },
    },
    
    "Cerebroprotein hydrolysate (khác)": {
        "group": "Neurology - Neuropeptide/cerebroprotein hydrolysate (adjunct, evidence limited)",
        "vietnamese_name": "Cerebroprotein hydrolysate (khác Cerebrolysin)",
        "administration": ["IV"],
        "indications": [
            "Đột quỵ thiếu máu não giai đoạn bán cấp/phục hồi chức năng – thuốc hỗ trợ",
            "Chấn thương sọ não (TBI) – hỗ trợ phục hồi",
        ],
        "contraindications": [
            "Động kinh chưa kiểm soát hoặc trạng thái động kinh",
            "Suy thận nặng",
            "Dị ứng với chế phẩm protein/peptide nguồn gốc động vật",
        ],
        "dosage": {
            "adult_iv": "10–30ml/ngày pha 100ml NaCl 0.9% truyền 30–60 phút x 10–20 ngày; có thể lặp lại đợt sau 1–2 tháng",
            "notes": "Không tiêm bolus. Là thuốc hỗ trợ, KHÔNG thay thế tái tưới máu, chống kết tập tiểu cầu/chống đông hoặc statin liều cao.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh",
            "30_60": "Thận trọng, theo dõi creatinine, thể tích dịch",
            "under_30": "Tránh hoặc cân nhắc kỹ do nguy cơ tích lũy peptide",
        },
        "side_effects": [
            "Đỏ bừng, nhức đầu trong lúc truyền",
            "Buồn nôn, nôn",
            "Kích thích, mất ngủ nhẹ",
            "Phát ban, phản ứng quá mẫn (hiếm)",
            "Co giật ở người có ngưỡng thấp (hiếm)",
        ],
        "interactions": [
            "Thuốc hướng thần (antidepressant/antipsychotic): có thể tăng kích thích nhẹ",
            "Không ghi nhận tương tác dược động học rõ; chủ yếu thận trọng khi phối hợp nhiều thuốc tác động CNS.",
        ],
        "pregnancy": "C – dữ liệu hạn chế, tránh dùng nếu không thật cần",
        "mechanism_of_action": (
            "Hỗn hợp peptide/amino acid trọng lượng phân tử thấp, được cho là có hoạt tính giống yếu tố dinh dưỡng thần kinh, "
            "cải thiện chuyển hóa năng lượng neuron và giảm độc tính glutamate. Bằng chứng lâm sàng còn hạn chế và không đồng nhất."
        ),
        "monitoring": [
            "Huyết áp, mạch trong khi truyền",
            "Triệu chứng thần kinh (chức năng vận động, thang điểm NIHSS/modified Rankin khi theo dõi phục hồi)",
            "Dấu hiệu phản vệ hoặc kích thích thần kinh",
        ],
        "precautions": [
            "Không trì hoãn hoặc thay thế điều trị chuẩn đột quỵ.",
            "Thận trọng ở bệnh nhân tiền sử co giật hoặc suy thận nặng.",
            "Ngừng nếu có phản ứng quá mẫn hoặc co giật.",
        ],
        "pharmacokinetics": {
            "half_life": "Không xác định (hỗn hợp peptide), giả định thải trừ nhanh",
            "onset": "Vài ngày đến vài tuần (đánh giá qua phục hồi chức năng)",
            "duration": "Hiệu ứng phục hồi có thể kéo dài sau đợt điều trị",
            "protein_binding": "Không xác định",
            "clearance": "Chuyển hóa bởi peptidase, thải trừ thận",
        },
        "storage": "Giữ 2–8°C, tránh ánh sáng. Dùng ngay sau pha loãng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Động kinh chưa kiểm soát",
                "Suy thận nặng",
                "Dị ứng với chế phẩm protein/peptide nguồn gốc động vật",
            ],
            "tương_đối": [
                "Tiền sử co giật",
                "Bệnh thận mức độ trung bình",
                "Đang dùng nhiều thuốc tác động thần kinh trung ương",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Thiếu dữ liệu; tránh dùng trong thai kỳ nếu không thật cần.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết sữa; cân nhắc ngừng cho bú hoặc chọn thuốc khác.",
                "recommendation": "Tránh nếu có lựa chọn an toàn hơn.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Thận trọng do dữ liệu hạn chế",
            "severe": "Tránh nếu có thể",
        },
        "overdose_management": {
            "symptoms": ["Kích thích, nhức đầu, nôn, phản ứng quá mẫn"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Ngừng truyền, điều trị triệu chứng, xử trí phản vệ nếu có"],
            "monitoring": "HA, mạch, hô hấp, dấu hiệu dị ứng",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: ngừng truyền ngay, điều trị triệu chứng (kích thích, nhức đầu, nôn), xử trí phản vệ nếu có (epinephrine, corticosteroids, antihistamines), theo dõi dấu hiệu sinh tồn."
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 10–30ml vào 100ml NaCl 0.9%",
                "infusion_rate": "Truyền 30–60 phút, 1 lần/ngày",
                "compatibility": ["NS"],
                "incompatibility": ["Không trộn chung với thuốc khác trong cùng chai/truyền"],
                "notes": "Theo dõi phản ứng trong 10–15 phút đầu mỗi lần truyền.",
            }
        },
        "references": {
            "primary_sources": [
                "Một số RCT/observational nhỏ về cerebroprotein hydrolysate trong AIS/TBI (kết quả không đồng nhất)",
                "UpToDate/Drug monograph - Cerebroprotein hydrolysate",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "Low–Moderate (bằng chứng hạn chế, không phải chuẩn guideline)",
        },
    },
    
    "Nimodipine": {
        "group": "Neurology - Calcium channel blocker (cerebral vasospasm prophylaxis)",
        "vietnamese_name": "Nimodipine",
        "administration": ["PO", "NG"],
        "indications": [
            "Phòng ngừa thiếu máu não chậm do co thắt mạch sau xuất huyết dưới nhện (aSAH) – điều trị chuẩn",
        ],
        "contraindications": [
            "Hạ huyết áp nặng",
            "Sốc, suy tim mất bù",
            "Dị ứng dihydropyridine CCB",
        ],
        "dosage": {
            "adult_sah": "60mg PO/NG mỗi 4 giờ x 21 ngày (có thể 30mg mỗi 2 giờ nếu tụt HA)",
            "notes": "Dùng sớm sau chẩn đoán aSAH. Không dùng dạng IV (nguy cơ tụt HA nghiêm trọng, từng có cảnh báo).",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh",
            "30_60": "Không cần chỉnh",
            "under_30": "Thận trọng, theo dõi HA",
        },
        "side_effects": [
            "Tụt huyết áp",
            "Đỏ bừng, nhức đầu",
            "Chóng mặt",
        ],
        "interactions": [
            "CYP3A4 inhibitors (azole, macrolide, protease inhibitor): tăng nồng độ nimodipine",
            "CYP3A4 inducers (phenytoin, carbamazepine, rifampin): giảm nồng độ",
            "Thuốc hạ huyết áp khác: cộng hưởng tụt HA",
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Chẹn kênh Ca2+ typ L (dihydropyridine) ưu thế trên mạch não, giảm co thắt mạch sau xuất huyết dưới nhện, cải thiện tưới máu não.",
        "monitoring": [
            "Huyết áp, mạch",
            "Triệu chứng thiếu máu não chậm (nhức đầu, rối loạn ý thức, khu trú)",
        ],
        "precautions": [
            "Không dùng đường IV; chỉ uống/NG. Theo dõi HA sát.",
            "Giảm liều hoặc kéo dài khoảng cách nếu tụt HA.",
        ],
        "pharmacokinetics": {
            "half_life": "8–9 giờ",
            "onset": "Trong ngày đầu",
            "duration": "Dùng đều mỗi 4 giờ",
            "protein_binding": ">95%",
            "clearance": "Gan (CYP3A4); thải trừ qua mật và phân",
        },
        "storage": "Viên nang bảo quản nhiệt độ phòng, tránh ánh sáng. Nếu cho qua sonde, rút dung dịch từ viên và dùng ngay.",
        "black_box_warnings": None,
        "drug_interactions_detail": {
            "major": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, clarithromycin, ritonavir)",
                    "mechanism": "Tăng nồng độ nimodipine",
                    "effect": "Tụt HA nghiêm trọng",
                    "management": "Tránh phối hợp hoặc giảm liều, theo dõi HA.",
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Giảm nồng độ nimodipine",
                    "effect": "Giảm hiệu quả phòng co thắt mạch",
                    "management": "Tránh hoặc tăng liều/giám sát sát nếu bắt buộc.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": ["Hạ HA nặng", "Sốc", "Dị ứng dihydropyridine"],
            "tương_đối": ["Suy gan (cần giảm liều/thận trọng)"],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế; chỉ dùng nếu lợi ích vượt nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết sữa; thận trọng khi cho con bú.",
                "recommendation": "Cân nhắc tạm ngừng cho bú hoặc theo dõi trẻ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Giảm liều/giãn cách liều",
            "severe": "Tránh nếu có thể (nguy cơ tích lũy, tụt HA)",
        },
        "overdose_management": {
            "symptoms": ["Tụt HA nặng, nhịp nhanh phản xạ"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Truyền dịch, vận mạch nếu cần, than hoạt nếu uống quá liều sớm"],
            "monitoring": "HA, mạch, ECG",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Tốt nhất uống xa bữa để hấp thu tối đa",
                "timing": "60mg mỗi 4 giờ; nếu HA thấp có thể 30mg mỗi 2 giờ",
            },
            "ng": {
                "with_food": "Pha dung dịch từ viên nang, bơm qua sonde, tráng sonde sau bơm",
                "timing": "Như đường uống",
            },
        },
        "references": {
            "primary_sources": [
                "AHA/ASA guidelines for aneurysmal SAH – nimodipine là chuẩn phòng co thắt mạch",
                "ESO guidelines on SAH",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "High (điều trị chuẩn trong aSAH)",
        },
    },
}

__all__ = ["CEREBRAL_CIRCULATION_DRUGS"]