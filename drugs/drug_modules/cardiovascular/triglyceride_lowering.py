"""
Triglyceride Lowering Drugs
Các thuốc điều trị tăng triglyceride máu
"""

TRIGLYCERIDE_LOWERING_DRUGS = {
    "Icosapent ethyl": {
        "group": "Cardiovascular - Omega-3 Fatty Acid (EPA Ethyl Ester)",
        "vietnamese_name": "Icosapent ethyl, Vascepa",
        "administration": ["PO"],
        "indications": [
            "Tăng triglyceride máu nặng (≥500 mg/dL)",
            "Dự phòng biến cố tim mạch ở bệnh nhân có tăng triglyceride (150-499 mg/dL) và bệnh tim mạch do xơ vữa hoặc đái tháo đường với ≥2 yếu tố nguy cơ",
            "Giảm nguy cơ nhồi máu cơ tim, đột quỵ, tái thông mạch vành, đau thắt ngực không ổn định ở bệnh nhân có tăng triglyceride"
        ],
        "contraindications": [
            "Dị ứng icosapent ethyl hoặc bất kỳ thành phần nào",
            "Dị ứng cá hoặc động vật có vỏ"
        ],
        "dosage": {
            "adult_hypertriglyceridemia": "2g x 2 lần/ngày (tổng 4g/ngày), uống với thức ăn",
            "adult_cv_prevention": "2g x 2 lần/ngày (tổng 4g/ngày), uống với thức ăn",
            "notes": "Uống với thức ăn để tăng hấp thu. Không dùng quá 4g/ngày. Có bằng chứng giảm biến cố tim mạch (REDUCE-IT trial)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Đau khớp (thường gặp)",
            "Rối loạn tiêu hóa (buồn nôn, tiêu chảy)",
            "Tăng nguy cơ rung nhĩ (tăng nhẹ)",
            "Chảy máu (tăng nguy cơ nhẹ)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Thuốc chống đông (warfarin, apixaban, rivaroxaban): tăng nguy cơ chảy máu",
            "Aspirin: tăng nguy cơ chảy máu",
            "Thuốc chống kết tập tiểu cầu: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Icosapent ethyl là dạng ethyl ester của axit eicosapentaenoic (EPA), một axit béo omega-3 tinh khiết. EPA ức chế tổng hợp triglyceride ở gan bằng cách giảm sản xuất VLDL và tăng phân hủy triglyceride. EPA cũng có tác dụng chống viêm, chống huyết khối, và ổn định mảng xơ vữa. Khác với omega-3 hỗn hợp (EPA/DHA), icosapent ethyl chỉ chứa EPA tinh khiết, có bằng chứng mạnh giảm biến cố tim mạch (REDUCE-IT trial: giảm 25% nguy cơ biến cố tim mạch chính).",
        "monitoring": [
            "Lipid profile (triglyceride, LDL, HDL, total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "ALT/AST (theo dõi tăng men gan)",
            "Dấu hiệu chảy máu (nếu dùng với thuốc chống đông)",
            "ECG (theo dõi rung nhĩ - tăng nguy cơ nhẹ)",
            "Triệu chứng rối loạn tiêu hóa"
        ],
        "precautions": [
            "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ tiêu hóa",
            "Thận trọng khi dùng với thuốc chống đông hoặc thuốc chống kết tập tiểu cầu (tăng nguy cơ chảy máu)",
            "Theo dõi dấu hiệu chảy máu (chảy máu cam, chảy máu nướu, vết bầm tím)",
            "Theo dõi rung nhĩ (tăng nguy cơ nhẹ trong REDUCE-IT trial)",
            "Không dùng quá 4g/ngày",
            "Có bằng chứng mạnh giảm biến cố tim mạch ở bệnh nhân có tăng triglyceride và bệnh tim mạch do xơ vữa hoặc đái tháo đường"
        ],
        "pharmacokinetics": {
            "half_life": "EPA: 89 giờ (sau khi chuyển hóa)",
            "onset": "4-8 tuần để thấy hiệu quả giảm triglyceride",
            "duration": "Dài (do tích lũy trong mô)",
            "protein_binding": "Cao (gắn với albumin)",
            "metabolism": "Gan (beta-oxidation, omega-oxidation)",
            "clearance": "Gan và thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nang: ổn định.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, tăng nguy cơ rung nhĩ và chảy máu (nhẹ) đã được báo cáo trong REDUCE-IT trial.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, các thuốc chống đông (apixaban, rivaroxaban, dabigatran)",
                    "mechanism": "Omega-3 có thể ức chế kết tập tiểu cầu và kéo dài thời gian chảy máu",
                    "effect": "Tăng nguy cơ chảy máu (chảy máu cam, chảy máu nướu, chảy máu đường tiêu hóa)",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu. Có thể cần điều chỉnh liều thuốc chống đông. Theo dõi INR nếu dùng warfarin."
                },
                {
                    "drug": "Aspirin, clopidogrel, các thuốc chống kết tập tiểu cầu",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu. Cân nhắc lợi ích/nguy cơ."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng icosapent ethyl hoặc bất kỳ thành phần nào",
                "Dị ứng cá hoặc động vật có vỏ"
            ],
            "tương_đối": [
                "Dùng với thuốc chống đông - tăng nguy cơ chảy máu",
                "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                "Suy thận nặng - thận trọng, dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Không có dữ liệu đầy đủ trên phụ nữ có thai. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết icosapent ethyl có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (chuyển hóa qua gan)",
            "severe": "Thận trọng, có thể giảm liều (chuyển hóa qua gan)",
            "notes": "Icosapent ethyl chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vascepa (icosapent ethyl)",
                "UpToDate - Icosapent ethyl: Drug information",
                "REDUCE-IT Study - New England Journal of Medicine (2019) - Icosapent ethyl giảm biến cố tim mạch",
                "American Heart Association/American College of Cardiology guidelines - Hypertriglyceridemia"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Large RCT (REDUCE-IT) showing 25% reduction in cardiovascular events"
        }
    },

    "Pemafibrate": {
        "group": "Cardiovascular - Selective PPAR-alpha Modulator (Fibrate)",
        "vietnamese_name": "Pemafibrate, K-877",
        "administration": ["PO"],
        "indications": [
            "Tăng triglyceride máu (≥150 mg/dL)",
            "Rối loạn lipid máu hỗn hợp với tăng triglyceride",
            "Bệnh nhân không dung nạp hoặc không đáp ứng với fibrate truyền thống"
        ],
        "contraindications": [
            "Dị ứng pemafibrate hoặc bất kỳ thành phần nào",
            "Bệnh gan hoạt động",
            "Suy thận nặng (eGFR <30 mL/min/1.73m²)",
            "Bệnh túi mật",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "adult_standard": "0.2mg x 2 lần/ngày, uống với thức ăn",
            "adult_max": "0.4mg x 2 lần/ngày (tối đa 0.8mg/ngày)",
            "notes": "Uống với thức ăn để tăng hấp thu. Pemafibrate là fibrate thế hệ mới, chọn lọc PPAR-alpha hơn, ít tác dụng phụ hơn fibrate truyền thống."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "CHỐNG CHỈ ĐỊNH (eGFR <30)"
        },
        "side_effects": [
            "Rối loạn tiêu hóa (buồn nôn, tiêu chảy, đau bụng) - ít hơn fibrate truyền thống",
            "Tăng men gan (hiếm, ít hơn fibrate truyền thống)",
            "Sỏi mật (hiếm, ít hơn fibrate truyền thống)",
            "Đau cơ (hiếm, ít hơn fibrate truyền thống)",
            "Tăng creatine kinase (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng tác dụng chống đông (theo dõi INR)",
            "Statins: thận trọng (tăng nguy cơ tiêu cơ vân nhẹ, nhưng ít hơn fibrate truyền thống)",
            "Cyclosporine: tăng nguy cơ độc tính thận"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Pemafibrate là chất điều hòa thụ thể PPAR-alpha (Peroxisome Proliferator-Activated Receptor-alpha) chọn lọc. Kích thích PPAR-alpha → tăng biểu hiện gen liên quan đến beta-oxidation của axit béo, tăng hoạt động lipoprotein lipase, giảm sản xuất apolipoprotein C-III. Kết quả: giảm tổng hợp triglyceride ở gan, tăng phân hủy triglyceride, giảm VLDL, tăng HDL. Pemafibrate chọn lọc PPAR-alpha hơn fibrate truyền thống (fenofibrate, gemfibrozil) → ít tác dụng phụ hơn (ít tăng men gan, ít sỏi mật, ít đau cơ).",
        "monitoring": [
            "Lipid profile (triglyceride, LDL, HDL, total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "ALT/AST (theo dõi tăng men gan) - ít hơn fibrate truyền thống",
            "Creatine kinase (CK) nếu có đau cơ",
            "Creatinine, eGFR (theo dõi suy thận)",
            "Dấu hiệu sỏi mật (đau bụng phải trên) - ít hơn fibrate truyền thống",
            "INR nếu dùng với warfarin"
        ],
        "precautions": [
            "Uống với thức ăn để tăng hấp thu",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (eGFR <30)",
            "CHỐNG CHỈ ĐỊNH ở bệnh gan hoạt động",
            "Thận trọng khi dùng với statins (tăng nguy cơ tiêu cơ vân nhẹ, nhưng ít hơn fibrate truyền thống)",
            "Theo dõi dấu hiệu sỏi mật (đau bụng phải trên) - ít hơn fibrate truyền thống",
            "Theo dõi CK nếu có đau cơ hoặc yếu cơ",
            "Theo dõi INR nếu dùng với warfarin",
            "Pemafibrate ít tác dụng phụ hơn fibrate truyền thống (fenofibrate, gemfibrozil)"
        ],
        "pharmacokinetics": {
            "half_life": "15-20 giờ",
            "onset": "4-8 tuần để thấy hiệu quả giảm triglyceride",
            "duration": "Dài (do half-life dài)",
            "protein_binding": ">99%",
            "metabolism": "Gan (glucuronidation, một phần qua CYP2C8, CYP2C9)",
            "clearance": "Gan (chủ yếu) và thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: ổn định.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ - có thể gây hại cho thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Pemafibrate có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR chặt chẽ khi bắt đầu pemafibrate. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Statins (atorvastatin, simvastatin, rosuvastatin)",
                    "mechanism": "Tác dụng hiệp đồng trên cơ, tăng nguy cơ tiêu cơ vân",
                    "effect": "Tăng nguy cơ tiêu cơ vân (nhưng ít hơn fibrate truyền thống)",
                    "management": "Thận trọng. Theo dõi CK nếu có đau cơ. Có thể dùng cùng nhưng theo dõi sát. Ngừng nếu CK >10 lần ULN."
                }
            ],
            "moderate": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Có thể tăng độc tính thận",
                    "effect": "Tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, eGFR. Có thể cần giảm liều pemafibrate."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng pemafibrate hoặc bất kỳ thành phần nào",
                "Bệnh gan hoạt động",
                "Suy thận nặng (eGFR <30 mL/min/1.73m²)",
                "Bệnh túi mật",
                "Có thai - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Cho con bú"
            ],
            "tương_đối": [
                "Suy thận trung bình (eGFR 30-60) - thận trọng",
                "Dùng với statins - tăng nguy cơ tiêu cơ vân nhẹ",
                "Dùng với warfarin - tăng tác dụng chống đông"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây hại cho thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả. Ngừng ngay nếu có thai.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Không khuyến cáo dùng khi cho con bú. Pemafibrate có thể bài tiết vào sữa mẹ.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng (chuyển hóa qua gan)",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH nếu bệnh gan hoạt động",
            "notes": "Pemafibrate chuyển hóa qua gan. CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh gan hoạt động. Theo dõi ALT/AST định kỳ."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pemafibrate (K-877)",
                "UpToDate - Pemafibrate: Drug information",
                "Pemafibrate clinical trials - Selective PPAR-alpha modulator",
                "American Heart Association/American College of Cardiology guidelines - Hypertriglyceridemia"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "Moderate - Newer drug with selective PPAR-alpha activity, less side effects than traditional fibrates"
        }
    },

    "Omega-3 acid ethyl esters": {
        "group": "Cardiovascular - Omega-3 Fatty Acids (EPA/DHA)",
        "vietnamese_name": "Omega-3 acid ethyl esters, Lovaza, Omacor",
        "administration": ["PO"],
        "indications": [
            "Tăng triglyceride máu nặng (≥500 mg/dL)",
            "Rối loạn lipid máu hỗn hợp với tăng triglyceride",
            "Dự phòng biến cố tim mạch (một số chế phẩm)"
        ],
        "contraindications": [
            "Dị ứng omega-3 acid ethyl esters hoặc bất kỳ thành phần nào",
            "Dị ứng cá hoặc động vật có vỏ"
        ],
        "dosage": {
            "adult_hypertriglyceridemia": "2g x 2 lần/ngày hoặc 4g x 1 lần/ngày (tổng 4g/ngày), uống với thức ăn",
            "adult_cv_prevention": "1g x 1-2 lần/ngày (tùy chế phẩm), uống với thức ăn",
            "notes": "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ tiêu hóa. Liều điều trị tăng triglyceride: 4g/ngày. Liều dự phòng tim mạch: 1-2g/ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Rối loạn tiêu hóa (ợ hơi, buồn nôn, tiêu chảy, đau bụng) - thường gặp",
            "Vị tanh (sau khi uống)",
            "Tăng nguy cơ rung nhĩ (một số nghiên cứu)",
            "Chảy máu (tăng nguy cơ nhẹ)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Thuốc chống đông (warfarin, apixaban, rivaroxaban): tăng nguy cơ chảy máu",
            "Aspirin: tăng nguy cơ chảy máu",
            "Thuốc chống kết tập tiểu cầu: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Omega-3 acid ethyl esters chứa hỗn hợp EPA (eicosapentaenoic acid) và DHA (docosahexaenoic acid), các axit béo omega-3 chuỗi dài. EPA và DHA ức chế tổng hợp triglyceride ở gan bằng cách giảm sản xuất VLDL, tăng hoạt động lipoprotein lipase, và tăng beta-oxidation của axit béo. EPA và DHA cũng có tác dụng chống viêm, chống huyết khối, và ổn định mảng xơ vữa. Khác với icosapent ethyl (chỉ EPA), omega-3 acid ethyl esters chứa cả EPA và DHA. Hiệu quả giảm triglyceride: 20-50%. Hiệu quả dự phòng tim mạch: còn tranh cãi (một số nghiên cứu dương tính, một số âm tính).",
        "monitoring": [
            "Lipid profile (triglyceride, LDL, HDL, total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "ALT/AST (theo dõi tăng men gan)",
            "Dấu hiệu chảy máu (nếu dùng với thuốc chống đông)",
            "ECG (theo dõi rung nhĩ - một số nghiên cứu báo cáo tăng nguy cơ)",
            "Triệu chứng rối loạn tiêu hóa"
        ],
        "precautions": [
            "Uống với thức ăn để tăng hấp thu và giảm tác dụng phụ tiêu hóa (ợ hơi, vị tanh)",
            "Thận trọng khi dùng với thuốc chống đông hoặc thuốc chống kết tập tiểu cầu (tăng nguy cơ chảy máu)",
            "Theo dõi dấu hiệu chảy máu (chảy máu cam, chảy máu nướu, vết bầm tím)",
            "Theo dõi rung nhĩ (một số nghiên cứu báo cáo tăng nguy cơ)",
            "Vị tanh sau khi uống là bình thường",
            "Hiệu quả dự phòng tim mạch: còn tranh cãi (một số nghiên cứu dương tính, một số âm tính)"
        ],
        "pharmacokinetics": {
            "half_life": "EPA: 89 giờ, DHA: 89 giờ (sau khi chuyển hóa)",
            "onset": "4-8 tuần để thấy hiệu quả giảm triglyceride",
            "duration": "Dài (do tích lũy trong mô)",
            "protein_binding": "Cao (gắn với albumin)",
            "metabolism": "Gan (beta-oxidation, omega-oxidation)",
            "clearance": "Gan và thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nang: ổn định. Bảo quản trong tủ lạnh có thể giảm vị tanh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, một số nghiên cứu báo cáo tăng nguy cơ rung nhĩ và chảy máu (nhẹ).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, các thuốc chống đông (apixaban, rivaroxaban, dabigatran)",
                    "mechanism": "Omega-3 có thể ức chế kết tập tiểu cầu và kéo dài thời gian chảy máu",
                    "effect": "Tăng nguy cơ chảy máu (chảy máu cam, chảy máu nướu, chảy máu đường tiêu hóa)",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu. Có thể cần điều chỉnh liều thuốc chống đông. Theo dõi INR nếu dùng warfarin."
                },
                {
                    "drug": "Aspirin, clopidogrel, các thuốc chống kết tập tiểu cầu",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu. Cân nhắc lợi ích/nguy cơ."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng omega-3 acid ethyl esters hoặc bất kỳ thành phần nào",
                "Dị ứng cá hoặc động vật có vỏ"
            ],
            "tương_đối": [
                "Dùng với thuốc chống đông - tăng nguy cơ chảy máu",
                "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                "Suy thận nặng - thận trọng, dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Không có dữ liệu đầy đủ trên phụ nữ có thai. Omega-3 (DHA) được khuyến cáo trong thai kỳ cho sự phát triển não bộ thai nhi, nhưng liều điều trị (4g/ngày) cao hơn liều bổ sung. Thận trọng.",
            "lactation": {
                "safety": "Compatible",
                "details": "Omega-3 bài tiết vào sữa mẹ. DHA trong sữa mẹ có lợi cho sự phát triển não bộ trẻ sơ sinh. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu rối loạn tiêu hóa."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (chuyển hóa qua gan)",
            "severe": "Thận trọng, có thể giảm liều (chuyển hóa qua gan)",
            "notes": "Omega-3 acid ethyl esters chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lovaza (omega-3 acid ethyl esters), Omacor (omega-3 acid ethyl esters)",
                "UpToDate - Omega-3 fatty acids: Drug information",
                "STRENGTH Trial - JAMA (2020) - Omega-3 trong dự phòng tim mạch",
                "American Heart Association/American College of Cardiology guidelines - Hypertriglyceridemia"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "Moderate - Effective for hypertriglyceridemia, but cardiovascular benefit is controversial"
        }
    }
}

__all__ = ['TRIGLYCERIDE_LOWERING_DRUGS']

