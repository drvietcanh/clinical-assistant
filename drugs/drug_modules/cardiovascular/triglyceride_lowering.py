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
        },
        "overdose_management": {
             "symptoms": [
                 "Cần tra cứu thêm thông tin về triệu chứng quá liều"
             ],
             "antidote": "Không có antidote đặc hiệu",
             "treatment": [
                 "Ngừng ngay thuốc",
                 "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                 "Than hoạt tính",
                 "Điều trị hỗ trợ và điều trị triệu chứng",
                 "Theo dõi dấu hiệu sinh tồn"
             ],
             "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
         },
         "reversal_agents": {
             "available": False,
             "agents": []
         },
         "administration_instructions": {
             "oral": {
                 "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                 "timing": "Theo chỉ định của bác sĩ",
                 "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
             }
         },
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
        },
        "overdose_management": {
              "symptoms": [
                  "Cần tra cứu thêm thông tin về triệu chứng quá liều"
              ],
              "antidote": "Không có antidote đặc hiệu",
              "treatment": [
                  "Ngừng ngay thuốc",
                  "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                  "Than hoạt tính",
                  "Điều trị hỗ trợ và điều trị triệu chứng",
                  "Theo dõi dấu hiệu sinh tồn"
              ],
              "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
          },
          "reversal_agents": {
              "available": False,
              "agents": []
          },
          "administration_instructions": {
              "oral": {
                  "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                  "timing": "Theo chỉ định của bác sĩ",
                  "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
              }
          },
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
        },
        "overdose_management": {
              "symptoms": [
                  "Cần tra cứu thêm thông tin về triệu chứng quá liều"
              ],
              "antidote": "Không có antidote đặc hiệu",
              "treatment": [
                  "Ngừng ngay thuốc",
                  "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                  "Than hoạt tính",
                  "Điều trị hỗ trợ và điều trị triệu chứng",
                  "Theo dõi dấu hiệu sinh tồn"
              ],
              "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
          },
          "reversal_agents": {
              "available": False,
              "agents": []
          },
          "administration_instructions": {
              "oral": {
                  "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                  "timing": "Theo chỉ định của bác sĩ",
                  "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
              }
          },
},

    "Niacin": {
        "group": "Cardiovascular - Vitamin B3 / Lipid-lowering Agent",
        "vietnamese_name": "Niacin, Nicotinic Acid, Vitamin B3",
        "administration": ["PO", "ER"],
        "indications": [
            "Tăng cholesterol máu (hypercholesterolemia)",
            "Tăng triglyceride máu (hypertriglyceridemia)",
            "Tăng HDL-C (high-density lipoprotein cholesterol)",
            "Rối loạn lipid máu hỗn hợp",
            "Bệnh nhân không dung nạp statin (dùng đơn trị hoặc kết hợp)"
        ],
        "contraindications": [
            "Dị ứng niacin hoặc bất kỳ thành phần nào",
            "Bệnh gan hoạt động",
            "Loét dạ dày tá tràng đang hoạt động",
            "Xuất huyết động mạch",
            "Có thai (khi dùng liều cao)"
        ],
        "dosage": {
            "adult_immediate_release": "100-500mg x 2-3 lần/ngày, tăng dần đến 1.5-3g/ngày (chia 2-3 lần)",
            "adult_extended_release": "500mg-2g x 1 lần/ngày (tối đa 2g/ngày)",
            "adult_sustained_release": "250-500mg x 2 lần/ngày, tăng dần đến 1-2g/ngày",
            "notes": "Bắt đầu với liều thấp và tăng dần để giảm tác dụng phụ (đỏ bừng). Uống với thức ăn hoặc aspirin để giảm đỏ bừng. Extended-release ít đỏ bừng hơn immediate-release nhưng tăng nguy cơ độc tính gan."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Thận trọng, giảm liều, dữ liệu hạn chế"
        },
        "side_effects": [
            "Đỏ bừng (flushing) - RẤT PHỔ BIẾN, đặc biệt với immediate-release",
            "Ngứa, nóng rát da",
            "Đau đầu",
            "Rối loạn tiêu hóa (buồn nôn, nôn, tiêu chảy, đau bụng)",
            "Tăng men gan (ALT, AST) - đặc biệt với sustained-release",
            "Độc tính gan (hiếm nhưng nghiêm trọng) - đặc biệt với sustained-release",
            "Tăng glucose máu (có thể làm nặng đái tháo đường)",
            "Tăng acid uric máu (có thể gây bệnh gút)",
            "Rối loạn nhịp tim (hiếm)",
            "Giảm huyết áp (hiếm)"
        ],
        "interactions": [
            "Aspirin: giảm đỏ bừng (dùng trước niacin 30 phút)",
            "Statins: tăng nguy cơ tiêu cơ vân (đặc biệt với simvastatin)",
            "Warfarin: có thể tăng tác dụng chống đông (theo dõi INR)",
            "Thuốc hạ huyết áp: tăng tác dụng hạ huyết áp",
            "Thuốc đái tháo đường: có thể tăng glucose máu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Niacin (nicotinic acid) là vitamin B3, có tác dụng hạ lipid máu qua nhiều cơ chế: (1) Ức chế lipolysis ở mô mỡ: niacin gắn với thụ thể GPR109A trên tế bào mỡ → ức chế hormone-sensitive lipase → giảm giải phóng axit béo tự do từ mô mỡ → giảm cung cấp axit béo cho gan → giảm tổng hợp VLDL và triglyceride. (2) Giảm tổng hợp triglyceride ở gan: giảm sản xuất VLDL. (3) Tăng HDL-C: niacin làm giảm catabolism của HDL (giảm chuyển cholesterol từ HDL về gan) và tăng tổng hợp HDL. (4) Giảm LDL-C: giảm sản xuất VLDL → giảm LDL (VLDL là tiền chất của LDL). Kết quả: giảm triglyceride 20-50%, giảm LDL-C 10-25%, tăng HDL-C 15-35%. ĐẶC ĐIỂM: (1) Thuốc cổ điển, ít dùng hiện nay do tác dụng phụ (đỏ bừng) và thiếu bằng chứng lợi ích tim mạch bổ sung khi kết hợp với statin, (2) Đỏ bừng là tác dụng phụ phổ biến nhất (do giải phóng prostaglandin D2), (3) Extended-release ít đỏ bừng hơn nhưng tăng nguy cơ độc tính gan, (4) Không khuyến cáo kết hợp với statin do thiếu bằng chứng lợi ích bổ sung.",
        "monitoring": [
            "Lipid profile (triglyceride, LDL, HDL, total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "ALT/AST (theo dõi độc tính gan) - QUAN TRỌNG, đặc biệt với sustained-release, mỗi 3-6 tháng",
            "Glucose máu (nếu có đái tháo đường hoặc tiền đái tháo đường) - niacin có thể tăng glucose máu",
            "Acid uric máu (nếu có tiền sử gút) - niacin có thể tăng acid uric",
            "Dấu hiệu đỏ bừng (flushing) - phổ biến, đặc biệt với immediate-release",
            "Dấu hiệu độc tính gan (vàng da, mệt mỏi, đau bụng) - ngừng ngay nếu có",
            "INR nếu dùng với warfarin",
            "CK nếu dùng với statin (tăng nguy cơ tiêu cơ vân)"
        ],
        "precautions": [
            "ĐỎ BỪNG (flushing) - RẤT PHỔ BIẾN, đặc biệt với immediate-release. Dùng aspirin 325mg trước niacin 30 phút để giảm đỏ bừng. Bắt đầu với liều thấp và tăng dần.",
            "ĐỘC TÍNH GAN - đặc biệt với sustained-release. Theo dõi ALT/AST mỗi 3-6 tháng. Ngừng ngay nếu ALT/AST >3x ULN hoặc có dấu hiệu vàng da.",
            "Tăng glucose máu - niacin có thể làm nặng đái tháo đường. Theo dõi glucose máu nếu có đái tháo đường.",
            "Tăng acid uric máu - niacin có thể gây bệnh gút. Theo dõi acid uric nếu có tiền sử gút.",
            "KHÔNG KHUYẾN CÁO kết hợp với statin do thiếu bằng chứng lợi ích tim mạch bổ sung (AIM-HIGH, HPS2-THRIVE trials âm tính).",
            "Tăng nguy cơ tiêu cơ vân khi dùng với statin - đặc biệt với simvastatin. Theo dõi CK nếu có đau cơ.",
            "Uống với thức ăn để giảm tác dụng phụ tiêu hóa.",
            "Extended-release ít đỏ bừng hơn immediate-release nhưng tăng nguy cơ độc tính gan.",
            "Ít dùng hiện nay do tác dụng phụ và thiếu bằng chứng lợi ích tim mạch bổ sung."
        ],
        "pharmacokinetics": {
            "half_life": "20-45 phút (immediate-release), 4-5 giờ (extended-release)",
            "onset": "2-4 tuần để thấy hiệu quả giảm lipid",
            "duration": "Ngắn (immediate-release), dài (extended-release)",
            "protein_binding": "Thấp (<20%)",
            "metabolism": "Gan (conjugation với glycine → nicotinuric acid, một phần methylated)",
            "clearance": "Thận (chủ yếu), một phần qua phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén/nang: ổn định.",
        "black_box_warnings": "ĐỘC TÍNH GAN - đặc biệt với sustained-release. Có thể gây suy gan, viêm gan. Theo dõi ALT/AST mỗi 3-6 tháng. Ngừng ngay nếu ALT/AST >3x ULN hoặc có dấu hiệu vàng da.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Statins (đặc biệt simvastatin)",
                    "mechanism": "Tác dụng hiệp đồng trên cơ, tăng nguy cơ tiêu cơ vân",
                    "effect": "Tăng nguy cơ tiêu cơ vân, tăng CK",
                    "management": "KHÔNG KHUYẾN CÁO kết hợp với statin do thiếu bằng chứng lợi ích tim mạch bổ sung. Nếu bắt buộc, theo dõi CK chặt chẽ. Ngừng nếu CK >10x ULN hoặc có đau cơ nặng."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Niacin có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR chặt chẽ khi bắt đầu niacin. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin",
                    "mechanism": "Aspirin ức chế prostaglandin D2, giảm đỏ bừng do niacin",
                    "effect": "Giảm đỏ bừng (tác dụng có lợi)",
                    "management": "Dùng aspirin 325mg trước niacin 30 phút để giảm đỏ bừng. Đây là cách sử dụng thường quy."
                },
                {
                    "drug": "Thuốc hạ huyết áp",
                    "mechanism": "Niacin có thể gây giãn mạch, hạ huyết áp",
                    "effect": "Tăng tác dụng hạ huyết áp, có thể gây hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp. Có thể cần giảm liều thuốc hạ huyết áp."
                },
                {
                    "drug": "Thuốc đái tháo đường (insulin, metformin, sulfonylurea)",
                    "mechanism": "Niacin có thể tăng glucose máu",
                    "effect": "Giảm hiệu quả thuốc đái tháo đường, tăng glucose máu",
                    "management": "Thận trọng. Theo dõi glucose máu chặt chẽ. Có thể cần tăng liều thuốc đái tháo đường."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng niacin hoặc bất kỳ thành phần nào",
                "Bệnh gan hoạt động",
                "Loét dạ dày tá tràng đang hoạt động",
                "Xuất huyết động mạch"
            ],
            "tương_đối": [
                "Đái tháo đường - niacin có thể tăng glucose máu",
                "Bệnh gút - niacin có thể tăng acid uric máu",
                "Suy thận nặng - thận trọng, dữ liệu hạn chế",
                "Suy gan - CHỐNG CHỈ ĐỊNH nếu bệnh gan hoạt động",
                "Có thai (liều cao) - thận trọng, category C"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Niacin phân loại C - thận trọng trong thai kỳ. Liều bổ sung vitamin B3 (niacin) thường an toàn trong thai kỳ, nhưng liều điều trị lipid (1-3g/ngày) chưa có dữ liệu đầy đủ. Không khuyến cáo dùng liều cao trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Niacin bài tiết vào sữa mẹ ở nồng độ thấp. Liều bổ sung vitamin B3 an toàn khi cho con bú. Liều điều trị lipid (1-3g/ngày) chưa có dữ liệu đầy đủ.",
                "recommendation": "Có thể dùng liều bổ sung khi cho con bú. Thận trọng với liều điều trị lipid. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng (chuyển hóa qua gan)",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH nếu bệnh gan hoạt động",
            "notes": "Niacin chuyển hóa qua gan. CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh gan hoạt động. Độc tính gan đặc biệt phổ biến với sustained-release. Theo dõi ALT/AST mỗi 3-6 tháng."
        },
        "overdose_management": {
            "symptoms": [
                "Đỏ bừng nặng",
                "Buồn nôn, nôn",
                "Đau bụng",
                "Tăng men gan (ALT, AST)",
                "Vàng da (nếu có độc tính gan)",
                "Hạ huyết áp",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng niacin ngay",
                "Rửa dạ dày nếu mới uống <1 giờ",
                "Than hoạt tính",
                "Điều trị đỏ bừng: aspirin, antihistamine, corticosteroid nếu cần",
                "Điều trị độc tính gan: hỗ trợ gan, ngừng niacin",
                "Hỗ trợ huyết áp nếu hạ huyết áp",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, ALT/AST, bilirubin, glucose máu, acid uric máu trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm tác dụng phụ tiêu hóa và đỏ bừng.",
                "timing": "Bắt đầu với liều thấp (100-250mg) và tăng dần mỗi 1-2 tuần. Dùng aspirin 325mg trước niacin 30 phút để giảm đỏ bừng. Immediate-release: chia 2-3 lần/ngày. Extended-release: 1 lần/ngày (tối đa 2g/ngày)."
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
                "FDA Drug Label - Niacin (Niacor, Niaspan)",
                "UpToDate - Niacin: Drug information",
                "AIM-HIGH Study - New England Journal of Medicine (2011) - Niacin + Statin trong CVD",
                "HPS2-THRIVE Study - New England Journal of Medicine (2014) - Niacin + Statin trong CVD",
                "ACC/AHA Guidelines - Cholesterol Management (2018)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate - Effective for lipid lowering, but no additional cardiovascular benefit when combined with statin (AIM-HIGH, HPS2-THRIVE negative)"
        }
    },

    "Evinacumab": {
        "group": "Cardiovascular - ANGPTL3 Inhibitor (Monoclonal Antibody)",
        "vietnamese_name": "Evinacumab, Evkeeza",
        "administration": ["IV"],
        "indications": [
            "Tăng cholesterol máu gia đình đồng hợp tử (HoFH - Homozygous Familial Hypercholesterolemia)",
            "Bệnh nhân HoFH không đạt mục tiêu LDL-C với statin tối đa và các thuốc khác",
            "Giảm LDL-C, HDL-C, và triglyceride ở bệnh nhân HoFH"
        ],
        "contraindications": [
            "Dị ứng evinacumab hoặc bất kỳ thành phần nào",
            "Dị ứng protein tái tổ hợp"
        ],
        "dosage": {
            "adult_iv": "15mg/kg IV mỗi 4 tuần",
            "notes": "Truyền IV trong 60 phút. Evinacumab là kháng thể đơn dòng, được FDA phê duyệt 2021 cho HoFH. Điều trị lâu dài, mỗi 4 tuần."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion reaction) - phổ biến",
            "Nhiễm trùng đường hô hấp trên",
            "Cúm",
            "Buồn nôn",
            "Phản ứng dị ứng (hiếm)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Có thể dùng cùng với statin",
            "Có thể dùng cùng với ezetimibe",
            "Có thể dùng cùng với PCSK9 inhibitors",
            "Không có tương tác với CYP450"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Evinacumab là kháng thể đơn dòng kháng ANGPTL3 (Angiopoietin-like protein 3, fully human monoclonal antibody). ANGPTL3 là protein được sản xuất ở gan, ức chế lipoprotein lipase (LPL) và endothelial lipase (EL). LPL và EL là enzyme quan trọng trong chuyển hóa triglyceride và HDL. Bằng cách ức chế ANGPTL3, evinacumab giải phóng ức chế LPL và EL → tăng hoạt động LPL và EL → tăng phân hủy triglyceride và HDL → giảm triglyceride, LDL-C, và HDL-C. ĐẶC ĐIỂM: (1) FDA phê duyệt 2021 cho HoFH (rất hiếm, 1/250,000-1/1,000,000), (2) Giảm cả LDL-C, HDL-C, và triglyceride (khác với các thuốc khác thường tăng HDL-C), (3) Hiệu quả cao: giảm LDL-C 47-49% ở bệnh nhân HoFH, (4) Chỉ định đặc biệt cho HoFH (không dùng cho các bệnh nhân khác), (5) Truyền IV mỗi 4 tuần, (6) Đắt tiền (orphan drug).",
        "monitoring": [
            "Lipid profile (LDL-C, HDL-C, TG, Total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "LFT (AST, ALT) trước điều trị và mỗi 6-12 tháng",
            "Dấu hiệu phản ứng truyền (infusion reaction) - trong và sau truyền",
            "Dấu hiệu phản ứng dị ứng",
            "Đánh giá đáp ứng: Mục tiêu LDL-C <100 mg/dL (hoặc <70 mg/dL nếu có bệnh tim mạch) ở HoFH"
        ],
        "precautions": [
            "PHẢN ỨNG TRUYỀN - phổ biến, cần theo dõi trong và sau truyền",
            "Chỉ định đặc biệt cho HoFH - không dùng cho các bệnh nhân khác",
            "Giảm cả HDL-C (khác với các thuốc khác) - cần theo dõi",
            "Có thể dùng cùng với statin, ezetimibe, PCSK9 inhibitors để tăng hiệu quả",
            "Đắt tiền (orphan drug) - cần cân nhắc chi phí",
            "Truyền IV mỗi 4 tuần - cần đến bệnh viện hoặc trung tâm điều trị",
            "Theo dõi lipid profile định kỳ để đánh giá đáp ứng"
        ],
        "pharmacokinetics": {
            "half_life": "17-19 ngày",
            "onset": "4-8 tuần để thấy hiệu quả giảm LDL-C",
            "duration": "4 tuần (liều mỗi 4 tuần)",
            "protein_binding": "IgG4 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES), tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, chỉ định đặc biệt cho HoFH - không dùng cho các bệnh nhân khác.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [
                {
                    "drug": "Statin, Ezetimibe, PCSK9 inhibitors",
                    "mechanism": "Tác dụng hiệp đồng giảm LDL-C",
                    "effect": "Tăng hiệu quả giảm LDL-C",
                    "management": "Có thể dùng cùng để tăng hiệu quả. Theo dõi lipid profile."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng evinacumab hoặc bất kỳ thành phần nào",
                "Dị ứng protein tái tổ hợp"
            ],
            "tương_đối": [
                "Không phải HoFH - chỉ định đặc biệt cho HoFH",
                "Suy thận nặng - thận trọng, không cần điều chỉnh liều",
                "Suy gan nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Evinacumab phân loại C - thận trọng trong thai kỳ. Không có dữ liệu đầy đủ trên phụ nữ có thai. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết evinacumab có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Evinacumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chức năng gan."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng",
                "Phản ứng dị ứng nặng",
                "Hạ huyết áp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị phản ứng truyền.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Hỗ trợ huyết áp nếu hạ huyết áp",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu phản ứng truyền, phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 1-10mg/ml. Không lọc.",
                "infusion_rate": "Truyền IV trong 60 phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Truyền IV trong 60 phút. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi phản ứng truyền. Liều: 15mg/kg mỗi 4 tuần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Evinacumab (Evkeeza)",
                "UpToDate - Evinacumab: Drug information",
                "ELIPSE HoFH Study - New England Journal of Medicine (2020) - Evinacumab trong HoFH",
                "ACC/AHA Guidelines - Cholesterol Management (2024)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved (2021), large RCT (ELIPSE HoFH) showing 47-49% LDL-C reduction in HoFH"
        }
    },

    "Plozasiran": {
        "group": "Cardiovascular - Apo C-III Inhibitor (RNA Interference)",
        "vietnamese_name": "Plozasiran, ARO-APOC3",
        "administration": ["SC"],
        "indications": [
            "Tăng triglyceride máu nghiêm trọng (severe hypertriglyceridemia, ≥500 mg/dL)",
            "Hội chứng Chylomicronemia gia đình (FCS - Familial Chylomicronemia Syndrome)",
            "Tăng triglyceride máu do thiếu lipoprotein lipase (LPL deficiency)",
            "Bệnh nhân không đáp ứng với các thuốc hạ triglyceride khác"
        ],
        "contraindications": [
            "Dị ứng plozasiran hoặc bất kỳ thành phần nào",
            "Dị ứng với RNA interference therapeutics"
        ],
        "dosage": {
            "adult_sc": "225mg SC mỗi 3 tháng (liều đầu tiên), sau đó 225mg SC mỗi 6 tháng",
            "adult_sc_alternative": "225mg SC: liều đầu, sau 3 tháng, sau đó mỗi 6 tháng",
            "notes": "Tiêm dưới da (bụng, đùi, hoặc cánh tay). Plozasiran là RNA interference (siRNA) therapeutic, FDA breakthrough therapy designation. Liều mỗi 6 tháng sau liều đầu tiên (tiện lợi hơn các thuốc khác)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, không cần điều chỉnh liều",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhiễm trùng đường hô hấp trên",
            "Cúm",
            "Đau đầu",
            "Mệt mỏi",
            "Phản ứng dị ứng (hiếm)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Có thể dùng cùng với statin",
            "Có thể dùng cùng với fibrate",
            "Có thể dùng cùng với omega-3",
            "Không có tương tác với CYP450"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Plozasiran là RNA interference (siRNA) therapeutic, ức chế sản xuất apolipoprotein C-III (Apo C-III) ở mức RNA. Apo C-III là protein được sản xuất ở gan, ức chế lipoprotein lipase (LPL) và chuyển hóa triglyceride. Apo C-III cũng ức chế clearance của triglyceride-rich lipoproteins (chylomicrons, VLDL). Bằng cách ức chế sản xuất Apo C-III, plozasiran giải phóng ức chế LPL → tăng hoạt động LPL → tăng phân hủy triglyceride → giảm triglyceride đáng kể. ĐẶC ĐIỂM: (1) FDA breakthrough therapy designation (2024), (2) RNA interference (siRNA) - ức chế ở mức RNA, tác dụng kéo dài, (3) Liều mỗi 6 tháng sau liều đầu tiên (tiện lợi hơn các thuốc khác), (4) Hiệu quả cao: giảm triglyceride 70-90% trong các nghiên cứu lâm sàng, (5) Chỉ định đặc biệt cho tăng triglyceride nghiêm trọng và FCS, (6) Đang trong giai đoạn nghiên cứu Phase 3 (dự kiến hoàn thành 2026), (7) Tương tự Olezarsen (thuốc khác cùng cơ chế, đã được FDA phê duyệt 2024 cho FCS).",
        "monitoring": [
            "Lipid profile (triglyceride, LDL, HDL, total cholesterol) sau 3-6 tháng, sau đó mỗi 6 tháng",
            "LFT (AST, ALT) trước điều trị và mỗi 6-12 tháng",
            "Dấu hiệu phản ứng tại chỗ tiêm",
            "Dấu hiệu phản ứng dị ứng",
            "Đánh giá đáp ứng: Mục tiêu triglyceride <500 mg/dL (hoặc <150 mg/dL nếu có thể)"
        ],
        "precautions": [
            "PHẢN ỨNG TẠI CHỖ TIÊM - phổ biến, thường nhẹ",
            "Chỉ định đặc biệt cho tăng triglyceride nghiêm trọng và FCS - không dùng cho các bệnh nhân khác",
            "Đang trong giai đoạn nghiên cứu Phase 3 - cần theo dõi kết quả nghiên cứu",
            "FDA breakthrough therapy designation - thuốc mới, cần theo dõi dữ liệu lâm sàng",
            "Có thể dùng cùng với statin, fibrate, omega-3 để tăng hiệu quả",
            "Liều mỗi 6 tháng - tiện lợi hơn các thuốc khác",
            "Theo dõi lipid profile định kỳ để đánh giá đáp ứng",
            "Tương tự Olezarsen (đã được FDA phê duyệt 2024 cho FCS)"
        ],
        "pharmacokinetics": {
            "half_life": "Dài (do RNA interference, tác dụng kéo dài)",
            "onset": "3-6 tháng để thấy hiệu quả giảm triglyceride",
            "duration": "6 tháng (liều mỗi 6 tháng)",
            "protein_binding": "siRNA therapeutic",
            "metabolism": "Chuyển hóa qua hệ thống nội bào, tương tự các siRNA therapeutics khác",
            "clearance": "Chuyển hóa qua hệ thống nội bào, thải trừ qua thận một phần. Tác dụng kéo dài do cơ chế RNA interference."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch: ổn định trong tủ lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, đang trong giai đoạn nghiên cứu Phase 3 - cần theo dõi kết quả nghiên cứu.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [
                {
                    "drug": "Statin, Fibrate, Omega-3",
                    "mechanism": "Tác dụng hiệp đồng giảm triglyceride",
                    "effect": "Tăng hiệu quả giảm triglyceride",
                    "management": "Có thể dùng cùng để tăng hiệu quả. Theo dõi lipid profile."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng plozasiran hoặc bất kỳ thành phần nào",
                "Dị ứng với RNA interference therapeutics"
            ],
            "tương_đối": [
                "Không phải tăng triglyceride nghiêm trọng hoặc FCS - chỉ định đặc biệt",
                "Suy thận nặng - thận trọng, không cần điều chỉnh liều",
                "Suy gan nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Plozasiran phân loại C - thận trọng trong thai kỳ. Không có dữ liệu đầy đủ trên phụ nữ có thai. Không khuyến cáo dùng trong thai kỳ trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết plozasiran có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Plozasiran không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chức năng gan."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng tại chỗ tiêm nặng",
                "Phản ứng dị ứng nặng",
                "Tăng men gan"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị phản ứng.",
            "treatment": [
                "Ngừng tiêm ngay",
                "Điều trị phản ứng tại chỗ: chườm lạnh, corticosteroid tại chỗ nếu cần",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine, epinephrine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu phản ứng tại chỗ, phản ứng dị ứng, chức năng gan trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dung dịch sẵn sàng sử dụng. Không cần pha loãng.",
                "injection_site": "Tiêm dưới da ở bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "injection_technique": "Tiêm dưới da, không tiêm vào cơ hoặc mạch máu.",
                "notes": "Liều: 225mg SC mỗi 3 tháng (liều đầu), sau đó 225mg SC mỗi 6 tháng. Có thể tự tiêm sau khi được hướng dẫn. Theo dõi phản ứng tại chỗ tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Breakthrough Therapy Designation - Plozasiran (ARO-APOC3)",
                "UpToDate - Plozasiran: Drug information",
                "Plozasiran Phase 2/3 Clinical Trials - Arrowhead Pharmaceuticals",
                "ACC/AHA Guidelines - Hypertriglyceridemia (2024)"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "Moderate - FDA breakthrough therapy designation (2024), Phase 2/3 clinical trials showing 70-90% triglyceride reduction, Phase 3 expected completion 2026"
        }
    },

    "Fenofibrate": {
        "group": "Cardiovascular - Fibrate (PPAR-alpha Agonist)",
        "vietnamese_name": "Fenofibrate, Tricor, Lipofen",
        "administration": ["PO"],
        "indications": [
            "Tăng triglyceride máu (≥150 mg/dL)",
            "Rối loạn lipid máu hỗn hợp với tăng triglyceride",
            "Tăng cholesterol máu (kết hợp với statin)",
            "Bệnh nhân không dung nạp statin (dùng đơn trị)"
        ],
        "contraindications": [
            "Dị ứng fenofibrate hoặc bất kỳ thành phần nào",
            "Bệnh gan hoạt động",
            "Suy thận nặng (eGFR <30 mL/min/1.73m²)",
            "Bệnh túi mật",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "adult_standard": "48-145mg PO x 1 lần/ngày (tùy chế phẩm)",
            "adult_tricor": "48-145mg PO x 1 lần/ngày",
            "adult_lipofen": "50-150mg PO x 1 lần/ngày",
            "adult_max": "145mg/ngày (tricor), 150mg/ngày (lipofen)",
            "notes": "Uống với thức ăn để tăng hấp thu. Điều chỉnh liều theo eGFR. Fenofibrate là fibrate thường dùng nhất, an toàn hơn gemfibrozil khi dùng với statin."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50% (eGFR 30-60)",
            "under_30": "CHỐNG CHỈ ĐỊNH (eGFR <30)"
        },
        "side_effects": [
            "Rối loạn tiêu hóa (buồn nôn, tiêu chảy, đau bụng)",
            "Tăng men gan (ALT, AST)",
            "Sỏi mật (tăng nguy cơ)",
            "Đau cơ, tăng CK (khi dùng với statin)",
            "Tăng creatinine (do ức chế creatinine transporter, không phải suy thận thực sự)",
            "Phản ứng dị ứng (ban da, sốt)",
            "Viêm cơ (myositis) - hiếm"
        ],
        "interactions": [
            "Statins: tăng nguy cơ tiêu cơ vân (ít hơn gemfibrozil)",
            "Warfarin: tăng tác dụng chống đông (theo dõi INR)",
            "Cyclosporine: tăng nguy cơ độc tính thận",
            "Cholestyramine: giảm hấp thu fenofibrate - dùng cách xa ít nhất 2 giờ"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Fenofibrate là chất điều hòa thụ thể PPAR-alpha (Peroxisome Proliferator-Activated Receptor-alpha). Kích thích PPAR-alpha → tăng biểu hiện gen liên quan đến beta-oxidation của axit béo, tăng hoạt động lipoprotein lipase, giảm sản xuất apolipoprotein C-III. Kết quả: giảm tổng hợp triglyceride ở gan, tăng phân hủy triglyceride, giảm VLDL, tăng HDL. Fenofibrate giảm triglyceride 30-50%, tăng HDL 10-20%, giảm LDL 10-20%. ĐẶC ĐIỂM: (1) Fibrate thường dùng nhất, (2) An toàn hơn gemfibrozil khi dùng với statin (ít nguy cơ tiêu cơ vân hơn), (3) Tăng creatinine (do ức chế creatinine transporter, không phải suy thận thực sự), (4) Điều chỉnh liều theo eGFR, (5) CHỐNG CHỈ ĐỊNH ở eGFR <30.",
        "monitoring": [
            "Lipid profile (triglyceride, LDL, HDL, total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "ALT/AST (theo dõi tăng men gan) - trước và trong điều trị, mỗi 3-6 tháng",
            "Creatinine, eGFR (theo dõi suy thận) - tăng creatinine có thể xảy ra (không phải suy thận thực sự)",
            "Creatine kinase (CK) nếu có đau cơ (đặc biệt khi dùng với statin)",
            "Dấu hiệu sỏi mật (đau bụng phải trên)",
            "INR nếu dùng với warfarin"
        ],
        "precautions": [
            "Uống với thức ăn để tăng hấp thu",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (eGFR <30)",
            "CHỐNG CHỈ ĐỊNH ở bệnh gan hoạt động",
            "Điều chỉnh liều theo eGFR - QUAN TRỌNG: giảm liều 50% nếu eGFR 30-60",
            "Tăng creatinine - do ức chế creatinine transporter, không phải suy thận thực sự, không cần điều chỉnh liều",
            "Thận trọng khi dùng với statins (tăng nguy cơ tiêu cơ vân, nhưng ít hơn gemfibrozil)",
            "Theo dõi dấu hiệu sỏi mật (đau bụng phải trên)",
            "Theo dõi CK nếu có đau cơ hoặc yếu cơ",
            "Theo dõi INR nếu dùng với warfarin",
            "Dùng cách xa cholestyramine ít nhất 2 giờ (giảm hấp thu fenofibrate)",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ và cho con bú (category X)"
        ],
        "pharmacokinetics": {
            "half_life": "20 giờ",
            "onset": "4-8 tuần để thấy hiệu quả giảm triglyceride",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "99%",
            "metabolism": "Gan (glucuronidation, một phần qua CYP2C8, CYP2C9)",
            "clearance": "Gan (chủ yếu) và thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén/nang: ổn định.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ - có thể gây hại cho thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả. Tăng nguy cơ tiêu cơ vân khi dùng với statin (nhưng ít hơn gemfibrozil).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Statins (Atorvastatin, Simvastatin, Rosuvastatin)",
                    "mechanism": "Tác dụng hiệp đồng trên cơ, tăng nguy cơ tiêu cơ vân",
                    "effect": "Tăng nguy cơ tiêu cơ vân (nhưng ít hơn gemfibrozil)",
                    "management": "Thận trọng. Theo dõi CK nếu có đau cơ. Có thể dùng cùng nhưng theo dõi sát. Ngừng nếu CK >10 lần ULN hoặc có đau cơ nặng."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Fenofibrate có thể ức chế chuyển hóa warfarin (CYP2C9)",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR chặt chẽ khi bắt đầu fenofibrate. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Có thể tăng độc tính thận",
                    "effect": "Tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, eGFR. Có thể cần giảm liều fenofibrate."
                },
                {
                    "drug": "Cholestyramine, Colestipol",
                    "mechanism": "Cholestyramine giảm hấp thu fenofibrate",
                    "effect": "Giảm nồng độ fenofibrate, giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 2 giờ. Dùng fenofibrate trước hoặc sau cholestyramine ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fenofibrate hoặc bất kỳ thành phần nào",
                "Bệnh gan hoạt động",
                "Suy thận nặng (eGFR <30 mL/min/1.73m²)",
                "Bệnh túi mật",
                "Có thai - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Cho con bú"
            ],
            "tương_đối": [
                "Suy thận trung bình (eGFR 30-60) - giảm liều 50%",
                "Dùng với statins - tăng nguy cơ tiêu cơ vân",
                "Dùng với warfarin - tăng tác dụng chống đông"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây hại cho thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả. Ngừng ngay nếu có thai.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Không khuyến cáo dùng khi cho con bú. Fenofibrate có thể bài tiết vào sữa mẹ.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng (chuyển hóa qua gan)",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH nếu bệnh gan hoạt động",
            "notes": "Fenofibrate chuyển hóa qua gan. CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh gan hoạt động. Theo dõi ALT/AST định kỳ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng men gan",
                "Đau cơ (nếu dùng với statin)",
                "Rối loạn tiêu hóa nặng",
                "Sỏi mật"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng fenofibrate nếu cần",
                "Theo dõi men gan, CK",
                "Điều trị sỏi mật nếu có",
                "Điều trị hỗ trợ"
            ],
            "monitoring": "Men gan, CK, creatinine, eGFR, lipid profile, triệu chứng lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để tăng hấp thu.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Dùng cách xa cholestyramine ít nhất 2 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fenofibrate (Tricor, Lipofen)",
                "UpToDate - Fenofibrate: Drug information",
                "ACCORD Lipid Study - New England Journal of Medicine (2010) - Fenofibrate + Statin",
                "American Heart Association/American College of Cardiology guidelines - Hypertriglyceridemia"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, multiple RCTs, clinical guidelines"
        }
    },

    "Gemfibrozil": {
        "group": "Cardiovascular - Fibrate (PPAR-alpha Agonist)",
        "vietnamese_name": "Gemfibrozil, Lopid",
        "administration": ["PO"],
        "indications": [
            "Tăng triglyceride máu (≥150 mg/dL)",
            "Rối loạn lipid máu hỗn hợp với tăng triglyceride",
            "Bệnh nhân không dung nạp statin (dùng đơn trị)"
        ],
        "contraindications": [
            "Dị ứng gemfibrozil hoặc bất kỳ thành phần nào",
            "Bệnh gan hoạt động",
            "Suy thận nặng (CrCl <30 ml/min)",
            "Bệnh túi mật",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "adult_standard": "600mg PO x 2 lần/ngày (sáng và tối, trước bữa ăn)",
            "adult_max": "1200mg/ngày",
            "notes": "Uống 30 phút trước bữa ăn để tăng hấp thu. Gemfibrozil có nguy cơ tiêu cơ vân cao hơn fenofibrate khi dùng với statin - TRÁNH dùng với statin nếu có thể."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30)"
        },
        "side_effects": [
            "Rối loạn tiêu hóa (buồn nôn, tiêu chảy, đau bụng) - phổ biến",
            "Tăng men gan (ALT, AST)",
            "Sỏi mật (tăng nguy cơ)",
            "Đau cơ, tăng CK (khi dùng với statin) - NGUY CƠ CAO",
            "Tiêu cơ vân (khi dùng với statin) - NGUY CƠ CAO",
            "Phản ứng dị ứng (ban da, sốt)",
            "Viêm cơ (myositis) - hiếm"
        ],
        "interactions": [
            "Statins: TĂNG NGUY CƠ TIÊU CƠ VÂN NGHIÊM TRỌNG - TRÁNH DÙNG CHUNG",
            "Warfarin: tăng tác dụng chống đông (theo dõi INR)",
            "Cyclosporine: tăng nguy cơ độc tính thận",
            "Repaglinide: tăng nồng độ repaglinide"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Gemfibrozil là chất điều hòa thụ thể PPAR-alpha (Peroxisome Proliferator-Activated Receptor-alpha). Kích thích PPAR-alpha → tăng biểu hiện gen liên quan đến beta-oxidation của axit béo, tăng hoạt động lipoprotein lipase, giảm sản xuất apolipoprotein C-III. Kết quả: giảm tổng hợp triglyceride ở gan, tăng phân hủy triglyceride, giảm VLDL, tăng HDL. Gemfibrozil giảm triglyceride 30-50%, tăng HDL 10-20%, giảm LDL 10-20%. ĐẶC ĐIỂM: (1) Fibrate cổ điển, (2) NGUY CƠ TIÊU CƠ VÂN CAO khi dùng với statin (cao hơn fenofibrate) - TRÁNH DÙNG CHUNG, (3) Điều chỉnh liều theo CrCl, (4) CHỐNG CHỈ ĐỊNH ở CrCl <30, (5) Ít dùng hiện nay do nguy cơ tiêu cơ vân cao với statin.",
        "monitoring": [
            "Lipid profile (triglyceride, LDL, HDL, total cholesterol) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "ALT/AST (theo dõi tăng men gan) - trước và trong điều trị, mỗi 3-6 tháng",
            "Creatinine, CrCl (theo dõi suy thận)",
            "Creatine kinase (CK) nếu có đau cơ (ĐẶC BIỆT khi dùng với statin) - QUAN TRỌNG",
            "Dấu hiệu sỏi mật (đau bụng phải trên)",
            "INR nếu dùng với warfarin",
            "Dấu hiệu tiêu cơ vân (đau cơ nặng, yếu cơ, nước tiểu sẫm màu) - NGUY HIỂM"
        ],
        "precautions": [
            "Uống 30 phút trước bữa ăn để tăng hấp thu",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30)",
            "CHỐNG CHỈ ĐỊNH ở bệnh gan hoạt động",
            "TRÁNH DÙNG VỚI STATINS - NGUY CƠ TIÊU CƠ VÂN NGHIÊM TRỌNG, cao hơn fenofibrate",
            "Nếu bắt buộc dùng với statin: dùng liều statin thấp nhất, theo dõi CK chặt chẽ, ngừng ngay nếu có đau cơ",
            "Theo dõi dấu hiệu sỏi mật (đau bụng phải trên)",
            "Theo dõi CK nếu có đau cơ hoặc yếu cơ - QUAN TRỌNG",
            "Theo dõi INR nếu dùng với warfarin",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ và cho con bú (category X)",
            "Ít dùng hiện nay do nguy cơ tiêu cơ vân cao với statin - ưu tiên fenofibrate"
        ],
        "pharmacokinetics": {
            "half_life": "1.5 giờ",
            "onset": "4-8 tuần để thấy hiệu quả giảm triglyceride",
            "duration": "Ngắn (do half-life ngắn, cần dùng 2 lần/ngày)",
            "protein_binding": ">95%",
            "metabolism": "Gan (glucuronidation, một phần qua CYP2C8, CYP2C9)",
            "clearance": "Gan (chủ yếu) và thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: ổn định.",
        "black_box_warnings": "TĂNG NGUY CƠ TIÊU CƠ VÂN NGHIÊM TRỌNG khi dùng với statin, có thể gây suy thận cấp và tử vong. TRÁNH DÙNG CHUNG với statin. CHỐNG CHỈ ĐỊNH trong thai kỳ - có thể gây hại cho thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Statins (Atorvastatin, Simvastatin, Rosuvastatin, Lovastatin)",
                    "mechanism": "Gemfibrozil ức chế OATP1B1 và glucuronidation của statin, tăng nồng độ statin đáng kể. Tác dụng hiệp đồng trên cơ.",
                    "effect": "TĂNG NGUY CƠ TIÊU CƠ VÂN NGHIÊM TRỌNG, có thể gây suy thận cấp và tử vong",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: dùng liều statin thấp nhất, theo dõi CK chặt chẽ, ngừng ngay nếu có đau cơ hoặc CK >10 lần ULN. Ưu tiên fenofibrate nếu cần dùng fibrate với statin."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Gemfibrozil có thể ức chế chuyển hóa warfarin (CYP2C9)",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR chặt chẽ khi bắt đầu gemfibrozil. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Có thể tăng độc tính thận",
                    "effect": "Tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi creatinine, CrCl. Có thể cần giảm liều gemfibrozil."
                },
                {
                    "drug": "Repaglinide",
                    "mechanism": "Gemfibrozil ức chế chuyển hóa repaglinide, tăng nồng độ repaglinide",
                    "effect": "Tăng nồng độ repaglinide, tăng nguy cơ hạ đường huyết",
                    "management": "Thận trọng. Theo dõi đường huyết. Có thể cần giảm liều repaglinide."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng gemfibrozil hoặc bất kỳ thành phần nào",
                "Bệnh gan hoạt động",
                "Suy thận nặng (CrCl <30 ml/min)",
                "Bệnh túi mật",
                "Có thai - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Cho con bú",
                "Dùng với statin - TRÁNH DÙNG CHUNG (nguy cơ tiêu cơ vân nghiêm trọng)"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng",
                "Dùng với warfarin - tăng tác dụng chống đông",
                "Dùng với repaglinide - tăng nồng độ repaglinide"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Có thể gây hại cho thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải sử dụng biện pháp tránh thai hiệu quả. Ngừng ngay nếu có thai.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Không khuyến cáo dùng khi cho con bú. Gemfibrozil có thể bài tiết vào sữa mẹ.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng (chuyển hóa qua gan)",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH nếu bệnh gan hoạt động",
            "notes": "Gemfibrozil chuyển hóa qua gan. CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh gan hoạt động. Theo dõi ALT/AST định kỳ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng men gan",
                "Đau cơ nặng, tiêu cơ vân (nếu dùng với statin)",
                "Rối loạn tiêu hóa nặng",
                "Sỏi mật"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng gemfibrozil ngay",
                "Nếu có tiêu cơ vân:",
                "  - Truyền dịch tích cực (normal saline 1-2L/giờ)",
                "  - Kiềm hóa nước tiểu (sodium bicarbonate)",
                "  - Theo dõi chức năng thận",
                "  - Hemodialysis nếu suy thận cấp",
                "Theo dõi men gan, CK",
                "Điều trị sỏi mật nếu có",
                "Điều trị hỗ trợ"
            ],
            "monitoring": "Men gan, CK, creatinine, CrCl, lipid profile, triệu chứng lâm sàng, dấu hiệu tiêu cơ vân"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống 30 phút trước bữa ăn để tăng hấp thu.",
                "timing": "Uống 2 lần/ngày (sáng và tối), 30 phút trước bữa ăn. Uống cùng giờ mỗi ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Gemfibrozil (Lopid)",
                "UpToDate - Gemfibrozil: Drug information",
                "Helsinki Heart Study - JAMA (1987) - Gemfibrozil trong dự phòng tim mạch",
                "VA-HIT Study - JAMA (1999) - Gemfibrozil trong dự phòng tim mạch",
                "American Heart Association/American College of Cardiology guidelines - Hypertriglyceridemia"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, multiple RCTs (Helsinki Heart Study, VA-HIT), clinical guidelines"
        }
    }
}

__all__ = ['TRIGLYCERIDE_LOWERING_DRUGS']

