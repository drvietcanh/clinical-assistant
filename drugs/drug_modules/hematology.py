"""
Hematology and Anticoagulant Medications
Contains antiplatelet medications
"""

HEMATOLOGY_DRUGS = {
    "Alteplase": {
        "group": "Hematology - Thrombolytic (tPA)",
        "vietnamese_name": "Alteplase, rt-PA",
        "administration": ["IV"],
        "indications": [
            "Đột quỵ thiếu máu não cấp (AIS) trong cửa sổ 3–4.5 giờ",
            "Nhồi máu cơ tim cấp (STEMI) khi không thể PCI kịp thời",
            "Thuyên tắc phổi (PE) nguy kịch/huyết động không ổn định"
        ],
        "contraindications": [
            "Bất kỳ chảy máu nội sọ hoặc xuất huyết nội sọ trước đây",
            "Đột quỵ xuất huyết hoặc nhồi máu não gần đây (thường <3 tháng, tùy chỉ định)",
            "Phẫu thuật lớn, chấn thương nặng gần đây",
            "Huyết áp rất cao không kiểm soát",
            "Rối loạn đông máu nặng, giảm tiểu cầu rõ"
        ],
        "dosage": {
            "stroke_adult": "0.9 mg/kg (tối đa 90mg): 10% bolus IV trong 1 phút, 90% truyền trong 60 phút",
            "stemi_adult": "15mg bolus IV, sau đó 0.75mg/kg (tối đa 50mg) trong 30 phút, tiếp theo 0.5mg/kg (tối đa 35mg) trong 60 phút",
            "pe_adult": "100mg truyền IV trong 2 giờ (hoặc protocol tại bệnh viện)",
            "notes": "TUÂN THỦ chặt chẽ protocol từng chỉ định (AIS/STEMI/PE) và kiểm tra checklist chống chỉ định trước khi dùng."
        },
        "side_effects": [
            "Chảy máu lớn (xuất huyết nội sọ, xuất huyết tiêu hóa)",
            "Chảy máu tại vị trí chọc kim, catheter",
            "Hạ huyết áp thoáng qua",
            "Phản vệ (hiếm)"
        ],
        "interactions": [
            "Heparin, enoxaparin, DOACs, warfarin: tăng mạnh nguy cơ chảy máu",
            "Thuốc kháng tiểu cầu (aspirin, clopidogrel): tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C - Cân nhắc rất thận trọng, chỉ dùng khi lợi ích vượt xa nguy cơ",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": True,
            "bleeding_risk": "Very High",
            "organ_toxicity": []
        },
        "guideline_tags": [
            "AHA/ASA AIS tPA (0.9 mg/kg)",
            "ESC STEMI thrombolysis",
            "CHEST PE thrombolysis"
        ],
        "mechanism_of_action": "Alteplase là tissue plasminogen activator (tPA) tái tổ hợp. Gắn vào fibrin trong cục huyết khối và chuyển plasminogen thành plasmin, từ đó phân giải fibrin và làm tan cục máu đông. Tác dụng mạnh nhất trên huyết khối mới hình thành.",
        "monitoring": [
            "Dấu hiệu thần kinh mỗi 15 phút trong và sau truyền (AIS)",
            "Dấu hiệu chảy máu (da, niêm mạc, tiêu hóa, tiểu máu)",
            "Huyết áp, mạch, SpO2 liên tục trong quá trình truyền",
            "aPTT, INR, tiểu cầu (nếu dùng kèm hoặc sau heparin/kháng đông khác)"
        ],
        "precautions": [
            "TUYỆT ĐỐI tuân thủ checklist chống chỉ định cho AIS/STEMI/PE theo guideline.",
            "Không chọc kim, đặt catheter không cần thiết trong và 24 giờ sau truyền nếu có thể tránh.",
            "Kiểm soát huyết áp trước và trong khi truyền (đặc biệt AIS).",
            "Ngừng heparin/kháng đông khác trước truyền theo khuyến cáo.",
            "Nếu nghi ngờ xuất huyết nội sọ: ngừng truyền ngay, chụp CT, xử trí cấp cứu."
        ],
        "pharmacokinetics": {
            "half_life": "4-5 phút (nhanh, do bị ức chế bởi PAI-1 và α2-antiplasmin)",
            "onset": "Ngay lập tức sau khi bắt đầu truyền",
            "duration": "Tác dụng kéo dài sau khi ngừng truyền do plasmin đã được tạo ra",
            "protein_binding": "Gắn với fibrin trong cục máu đông",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Bị ức chế bởi PAI-1 và α2-antiplasmin trong huyết tương."
        },
        "storage": "Bảo quản bột đông khô trong tủ lạnh (2–8°C). Sau khi pha, dùng trong thời gian theo khuyến cáo của nhà sản xuất (thường ≤8 giờ), tránh lắc mạnh.",
        "black_box_warnings": "Nguy cơ xuất huyết nội sọ nghiêm trọng, có thể tử vong. TUYỆT ĐỐI tuân thủ checklist chống chỉ định. Không dùng ở bệnh nhân có xuất huyết nội sọ, đột quỵ xuất huyết, hoặc chống chỉ định khác.",
        "references": {
            "primary_sources": [
                "AHA/ASA Guidelines for the Early Management of Patients With Acute Ischemic Stroke",
                "ESC STEMI Guidelines",
                "CHEST Guidelines for VTE",
                "FDA Drug Label - Alteplase"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A"
        },
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - Cân nhắc rất thận trọng, chỉ dùng khi lợi ích vượt xa nguy cơ",
            "pregnancy_details": "Category C - Cân nhắc rất thận trọng, chỉ dùng khi lợi ích vượt xa nguy cơ - cần xem xét dữ liệu an toàn thai kỳ.",
            "lactation": {
            "safety": "Compatible with monitoring",
            "details": "Cần xem xét dữ liệu an toàn khi cho con bú.",
            "recommendation": "Thận trọng khi cho con bú.",
        },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Cần xem xét chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": [
            "Cần xem xét triệu chứng quá liều",
        ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
            "Ngừng ngay thuốc",
            "Hỗ trợ và điều trị triệu chứng",
            "Theo dõi dấu hiệu sinh tồn",
        ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu lâm sàng",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "iv": {
            "reconstitution": "Cần xem xét cách pha",
            "infusion_rate": "Cần xem xét tốc độ truyền",
            "compatibility": [
            "Cần xem xét",
        ],
            "incompatibility": [
            "Cần xem xét",
        ],
            "notes": "Cần xem xét hướng dẫn cụ thể",
        },
        },
    },
    
    "Andexanet alfa": {
        "group": "Hematology - DOAC Reversal Agent (Factor Xa Inhibitors)",
        "vietnamese_name": "Andexanet alfa, Andexxa",
        "administration": ["IV"],
        "indications": [
            "Đảo ngược tác dụng chống đông của apixaban hoặc rivaroxaban trong trường hợp chảy máu đe dọa tính mạng",
            "Đảo ngược tác dụng apixaban/rivaroxaban trước phẫu thuật khẩn cấp hoặc thủ thuật xâm lấn",
            "Quá liều apixaban/rivaroxaban có triệu chứng"
        ],
        "contraindications": [
            "Dị ứng với andexanet alfa hoặc các thành phần",
            "Không có chỉ định đảo ngược factor Xa inhibitor"
        ],
        "dosage": {
            "adult_low_dose": "400mg IV bolus, sau đó truyền 4mg/phút x 2 giờ (cho apixaban ≤5mg hoặc rivaroxaban ≤10mg, hoặc không biết liều)",
            "adult_high_dose": "800mg IV bolus, sau đó truyền 8mg/phút x 2 giờ (cho apixaban >5mg hoặc rivaroxaban >10mg)",
            "notes": "Liều dựa trên liều DOAC cuối cùng và thời gian từ liều cuối. Tác dụng đảo ngược trong vài phút."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
            "hemodialysis": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng dị ứng/phản vệ (hiếm)",
            "Huyết khối tái phát (sau khi đảo ngược) - nguy cơ cao hơn idarucizumab",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Không có tương tác thuốc đáng kể",
            "Sau khi đảo ngược: có thể dùng lại DOAC sau 24 giờ nếu cần"
        ],
        "pregnancy": "C - Dữ liệu hạn chế; chỉ dùng khi lợi ích vượt nguy cơ",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hepatic": True},
            "icu_critical_care_only": True,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ISTH 2020 DOAC Reversal Guidelines",
            "ACC/AHA/HRS AF Guidelines",
            "FDA Drug Label - Andexxa"
        ],
        "mechanism_of_action": (
            "Andexanet alfa là protein tái tổ hợp (modified factor Xa) gắn với các direct factor Xa inhibitors "
            "(apixaban, rivaroxaban, edoxaban, betrixaban) với ái lực cao, tạo phức hợp không hoạt tính. "
            "Andexanet alfa không có hoạt tính procoagulant do thiếu vị trí hoạt hóa. Đảo ngược tác dụng "
            "chống đông trong vài phút, có thể đo được bằng anti-factor Xa activity."
        ),
        "monitoring": [
            "Anti-factor Xa activity (apixaban/rivaroxaban-specific) trước và sau khi dùng",
            "Dấu hiệu chảy máu (nếu dùng cho chảy máu)",
            "Dấu hiệu huyết khối tái phát sau đảo ngược (nguy cơ cao hơn idarucizumab)",
            "Men gan (ALT/AST) nếu dùng kéo dài hoặc có bệnh gan nền",
            "Huyết áp, mạch trong quá trình truyền"
        ],
        "precautions": [
            "Chỉ dùng khi thật sự cần đảo ngược factor Xa inhibitor (chảy máu đe dọa tính mạng hoặc phẫu thuật khẩn cấp)",
            "Sau đảo ngược: nguy cơ huyết khối tái phát cao hơn idarucizumab - cân nhắc dùng lại chống đông sau 24 giờ",
            "Có thể dùng lại DOAC sau 24 giờ nếu cần",
            "Chuẩn bị sẵn phương tiện hồi sức cho phản ứng dị ứng",
            "Theo dõi men gan nếu có bệnh gan nền"
        ],
        "pharmacokinetics": {
            "half_life": "~1 giờ (ngắn)",
            "onset": "Vài phút sau khi bắt đầu bolus",
            "duration": "Đảo ngược trong vài phút, kéo dài trong thời gian truyền (2 giờ)",
            "protein_binding": "Gắn với factor Xa inhibitors",
            "clearance": "Chuyển hóa qua gan và thải trừ qua thận"
        },
        "storage": "Bảo quản lạnh 2-8°C, tránh đông lạnh. Sau khi pha, dùng trong 8 giờ ở nhiệt độ phòng hoặc 24 giờ ở 2-8°C.",
        "black_box_warnings": (
            "Sau khi đảo ngược factor Xa inhibitor, nguy cơ huyết khối tái phát tăng lên đáng kể. "
            "Cân nhắc dùng lại chống đông sau khi đảo ngược nếu bệnh nhân vẫn có chỉ định chống đông. "
            "Theo dõi sát dấu hiệu huyết khối trong 24-48 giờ sau đảo ngược."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với andexanet alfa hoặc các thành phần"
            ],
            "tương_đối": [
                "Không có chỉ định đảo ngược factor Xa inhibitor rõ ràng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế; chỉ dùng khi lợi ích vượt nguy cơ (chảy máu đe dọa tính mạng hoặc phẫu thuật khẩn cấp).",
            "lactation": {
                "safety": "Caution",
                "details": "Không rõ bài tiết sữa; phân tử lớn, hấp thu đường tiêu hóa kém ở trẻ.",
                "recommendation": "Có thể tiếp tục cho bú; theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều; theo dõi men gan",
            "severe": "Thận trọng; theo dõi men gan",
            "notes": "Andexanet alfa chuyển hóa qua gan; suy gan có thể ảnh hưởng đến thanh thải nhưng không cần điều chỉnh liều."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng dị ứng/phản vệ (hiếm)",
                "Huyết khối tái phát (nếu đã đảo ngược quá mức)",
                "Tăng men gan (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Xử trí phản ứng dị ứng: epinephrine, diphenhydramine, hydrocortisone nếu cần",
                "Nếu huyết khối tái phát: cân nhắc dùng lại chống đông (DOAC hoặc thuốc khác) sau 24 giờ",
                "Theo dõi men gan nếu có tăng men gan"
            ],
            "monitoring": "Huyết động, dấu hiệu dị ứng, dấu hiệu huyết khối, men gan trong 24-48 giờ"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha bột theo hướng dẫn chế phẩm với NS hoặc D5W",
                "infusion_rate": "Bolus: 400mg hoặc 800mg trong 15-30 phút, sau đó truyền liên tục 4mg/phút (low-dose) hoặc 8mg/phút (high-dose) x 2 giờ",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Liều dựa trên liều DOAC cuối cùng. Low-dose: 400mg bolus + 4mg/phút x 2h. High-dose: 800mg bolus + 8mg/phút x 2h."
            }
        },
        "references": {
            "primary_sources": [
                "ISTH 2020 Guidelines for DOAC Reversal",
                "ACC/AHA/HRS AF Guidelines",
                "FDA Drug Label - Andexxa (Andexanet alfa)",
                "ANNEXA-4 Study"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, guideline-supported"
        }
    },
    "Apixaban": {
        "group": "Hematology - Anticoagulant (Direct Factor Xa Inhibitor, DOAC)",
        "vietnamese_name": "Apixaban, Eliquis",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
            "Điều trị DVT/PE",
            "Phòng ngừa DVT sau phẫu thuật thay khớp háng/gối",
            "Phòng ngừa huyết khối sau hội chứng mạch vành cấp (với aspirin)"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Suy thận nặng (CrCl <15)",
            "Có thai",
            "Dị ứng apixaban"
        ],
        "dosage": {
            "adult_afib": "5mg x 2 lần/ngày (2.5mg nếu ≥2 trong: tuổi ≥80, cân nặng ≤60kg, creatinine ≥1.5mg/dL)",
            "adult_dvt_pe": "10mg x 2 lần/ngày x 7 ngày, sau đó 5mg x 2 lần/ngày",
            "adult_prophylaxis": "2.5mg x 2 lần/ngày",
            "adult_acs": "5mg x 2 lần/ngày (với aspirin)",
            "notes": "Điều chỉnh liều theo chức năng thận và các yếu tố khác. Không cần theo dõi INR/aPTT thường xuyên"
        },
        "side_effects": [
            "Chảy máu (phổ biến)",
            "Rối loạn tiêu hóa",
            "Nhức đầu"
        ],
        "interactions": [
            "CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir): tăng nồng độ (tránh dùng)",
            "CYP3A4 và P-gp inducers (rifampin): giảm nồng độ",
            "Aspirin/NSAID: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C - Tránh dùng",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": "High",
            "icu_critical_care_only": False
        },
        "guideline_tags": [
            "AHA/ACC/HRS AF stroke prevention",
            "ESC AF guidelines",
            "ISTH VTE treatment/prophylaxis"
        ],
        "mechanism_of_action": "Apixaban là direct factor Xa inhibitor, ức chế trực tiếp yếu tố Xa mà không cần antithrombin III. Apixaban gắn trực tiếp với Xa, ngăn chặn chuyển đổi prothrombin thành thrombin, ức chế hình thành cục máu đông. Thuốc là DOAC (direct oral anticoagulant), không cần theo dõi INR/aPTT thường xuyên như warfarin. Apixaban được thải trừ một phần qua thận (25%) và một phần qua gan (75%), nên cần điều chỉnh liều ở suy thận nặng. Có antidote đặc hiệu: andexanet alfa (Andexxa).",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
            "Chức năng thận (CrCl) - mỗi 3-6 tháng (apixaban thải trừ một phần qua thận)",
            "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
            "Dấu hiệu rối loạn tiêu hóa"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận (CrCl) và các yếu tố khác (tuổi, cân nặng) - mỗi 3-6 tháng",
            "Suy thận nặng (CrCl <15) - chống chỉ định",
            "Giảm liều xuống 2.5mg x 2 lần/ngày nếu ≥2 trong: tuổi ≥80, cân nặng ≤60kg, creatinine ≥1.5mg/dL",
            "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
            "Có antidote đặc hiệu: andexanet alfa (Andexxa) - đảo ngược tác dụng",
            "Tránh dùng với CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir) - tăng nồng độ",
            "Ngừng 1-2 ngày trước phẫu thuật lớn (tùy chức năng thận)",
            "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ (bình thường), 15-18 giờ (suy thận)",
            "onset": "3-4 giờ",
            "duration": "12-24 giờ",
            "protein_binding": "87%",
            "clearance": "Gan (75% - chuyển hóa qua CYP3A4). Thận (25% - thải trừ nguyên dạng). Cần điều chỉnh liều ở suy thận nặng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Suy thận nặng (CrCl <15) - chống chỉ định. Không ngừng đột ngột (tăng nguy cơ đột quỵ trong rung nhĩ).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)",
                    "mechanism": "Ức chế CYP3A4 và P-gp, tăng nồng độ apixaban",
                    "effect": "Tăng nồng độ apixaban, tăng nguy cơ chảy máu",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng CYP3A4 và P-gp inhibitors mạnh."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "CYP3A4 và P-gp inducers (rifampin)",
                    "mechanism": "Cảm ứng CYP3A4 và P-gp, giảm nồng độ apixaban",
                    "effect": "Giảm nồng độ apixaban, giảm hiệu quả",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <15) - chống chỉ định",
                "Dị ứng apixaban",
                "Dùng CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 15-30) - thận trọng, có thể cần giảm liều",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Có thai - tránh dùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ. Apixaban có thể gây chảy máu ở mẹ và thai nhi. Chỉ dùng nếu lợi ích > nguy cơ rõ ràng.",
            "lactation": {
                "safety": "Caution",
                "details": "Apixaban có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Apixaban chuyển hóa chủ yếu qua gan (CYP3A4 - 75%). Không cần điều chỉnh liều ở suy gan nhẹ. Thận trọng ở suy gan trung bình. Chống chỉ định ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
            ],
            "antidote": "Andexanet alfa (Andexxa) - antidote đặc hiệu",
            "treatment": [
                "Ngừng apixaban ngay lập tức",
                "Andexanet alfa (Andexxa): 400-800mg IV bolus, sau đó 4-8mg/phút x 2 giờ - đảo ngược tác dụng",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Rửa dạ dày nếu uống trong vòng 2 giờ",
                "Than hoạt tính",
                "Nếu không có andexanet: PCC 4 yếu tố (50 IU/kg) + than hoạt sớm",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                "Theo dõi ít nhất 24 giờ (do half-life 12 giờ)"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Andexanet alfa (Andexxa)",
                    "indication": "Đảo ngược tác dụng apixaban, rivaroxaban (chảy máu nặng hoặc phẫu thuật cấp cứu)",
                    "dose": "400-800mg IV bolus, sau đó 4-8mg/phút x 2 giờ",
                    "notes": "Antidote đặc hiệu cho apixaban và rivaroxaban. Đảo ngược tác dụng nhanh chóng."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 2 lần/ngày (sáng và tối), cách nhau 12 giờ. AFib: 5mg x 2 lần/ngày (2.5mg nếu ≥2 trong: tuổi ≥80, cân nặng ≤60kg, creatinine ≥1.5mg/dL). DVT/PE: 10mg x 2 lần/ngày x 7 ngày, sau đó 5mg x 2 lần/ngày."
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Eliquis (apixaban)",
                "ARISTOTLE Study - New England Journal of Medicine",
                "UpToDate - Apixaban: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High (FDA-approved, large RCT - ARISTOTLE study)"
        }
    },
    
    "Dabigatran": {
        "group": "Hematology - Anticoagulant (Direct Thrombin Inhibitor, DOAC)",
        "vietnamese_name": "Dabigatran, Pradaxa",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
            "Điều trị DVT/PE",
            "Phòng ngừa DVT sau phẫu thuật thay khớp háng/gối"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Suy thận nặng (CrCl <30)",
            "Có thai",
            "Dị ứng dabigatran"
        ],
        "dosage": {
            "adult_afib": "150mg x 2 lần/ngày (110mg x 2 lần/ngày nếu ≥75 tuổi hoặc CrCl 30-50)",
            "adult_dvt_pe": "150mg x 2 lần/ngày",
            "adult_prophylaxis": "220mg x 1 lần/ngày (110mg nếu CrCl 30-50)",
            "notes": "Điều chỉnh liều theo chức năng thận. Không cần theo dõi INR/aPTT thường xuyên"
        },
        "side_effects": [
            "Chảy máu (phổ biến)",
            "Khó tiêu, đau bụng",
            "Rối loạn tiêu hóa"
        ],
        "interactions": [
            "P-gp inhibitors (ketoconazole, dronedarone): tăng nồng độ (tránh dùng)",
            "P-gp inducers (rifampin): giảm nồng độ",
            "Aspirin/NSAID: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C - Tránh dùng",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "High",
            "organ_toxicity": []
        },
        "guideline_tags": [
            "AHA/ACC/HRS AF stroke prevention",
            "ISTH VTE treatment/prophylaxis",
            "ESC AF guidelines"
        ],
        "mechanism_of_action": "Dabigatran là direct thrombin inhibitor (DTI), ức chế trực tiếp thrombin (yếu tố IIa) mà không cần antithrombin III. Dabigatran gắn trực tiếp với thrombin, ngăn chặn chuyển đổi fibrinogen thành fibrin, ức chế hình thành cục máu đông. Thuốc là DOAC (direct oral anticoagulant), không cần theo dõi INR/aPTT thường xuyên như warfarin. Dabigatran được thải trừ chủ yếu qua thận (80%), nên cần điều chỉnh liều ở suy thận. Có antidote đặc hiệu: idarucizumab (Praxbind).",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
            "Chức năng thận (CrCl) - mỗi 3-6 tháng (dabigatran thải trừ qua thận)",
            "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
            "Dấu hiệu rối loạn tiêu hóa (khó tiêu, đau bụng)"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận (CrCl) - mỗi 3-6 tháng",
            "Suy thận nặng (CrCl <30) - chống chỉ định",
            "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
            "Có antidote đặc hiệu: idarucizumab (Praxbind) - đảo ngược tác dụng",
            "Tránh dùng với P-gp inhibitors mạnh (ketoconazole, dronedarone) - tăng nồng độ",
            "Ngừng 1-2 ngày trước phẫu thuật lớn (tùy chức năng thận)",
            "Uống với thức ăn để giảm rối loạn tiêu hóa",
            "Không mở viên nang (tăng hấp thu, tăng nguy cơ chảy máu)"
        ],
        "pharmacokinetics": {
            "half_life": "12-17 giờ (bình thường), 18-27 giờ (suy thận)",
            "onset": "1-2 giờ",
            "duration": "12-24 giờ",
            "protein_binding": "35%",
            "clearance": "Thận (80% - thải trừ nguyên dạng). Gan (20% - chuyển hóa). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Giữ trong bao bì gốc. Không mở viên nang.",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Suy thận nặng (CrCl <30) - chống chỉ định. Không ngừng đột ngột (tăng nguy cơ đột quỵ trong rung nhĩ).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "P-gp inhibitors mạnh (ketoconazole, dronedarone)",
                    "mechanism": "Ức chế P-gp, tăng nồng độ dabigatran",
                    "effect": "Tăng nồng độ dabigatran, tăng nguy cơ chảy máu",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng P-gp inhibitors mạnh."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "P-gp inducers (rifampin)",
                    "mechanism": "Cảm ứng P-gp, giảm nồng độ dabigatran",
                    "effect": "Giảm nồng độ dabigatran, giảm hiệu quả",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <30) - chống chỉ định",
                "Dị ứng dabigatran",
                "Dùng P-gp inhibitors mạnh (ketoconazole, dronedarone)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-50) - giảm liều (110mg x 2 lần/ngày)",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Có thai - tránh dùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ. Dabigatran có thể gây chảy máu ở mẹ và thai nhi. Chỉ dùng nếu lợi ích > nguy cơ rõ ràng.",
            "lactation": {
                "safety": "Caution",
                "details": "Dabigatran có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng",
            "notes": "Dabigatran chuyển hóa một phần qua gan (20%). Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
            ],
            "antidote": "Idarucizumab (Praxbind) - antidote đặc hiệu",
            "treatment": [
                "Ngừng dabigatran ngay lập tức",
                "Idarucizumab (Praxbind): 5g IV (2.5g x 2 lần, cách nhau 15 phút) - đảo ngược tác dụng",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Rửa dạ dày nếu uống trong vòng 2 giờ",
                "Than hoạt tính",
                "Nếu không có idarucizumab: PCC 4 yếu tố (≈50 IU/kg) ± than hoạt; lọc máu có thể giúp do thải qua thận",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                "Theo dõi ít nhất 24 giờ (do half-life 12-17 giờ)"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Idarucizumab (Praxbind)",
                    "indication": "Đảo ngược tác dụng dabigatran (chảy máu nặng hoặc phẫu thuật cấp cứu)",
                    "dose": "5g IV (2.5g x 2 lần, cách nhau 15 phút)",
                    "notes": "Antidote đặc hiệu cho dabigatran. Đảo ngược tác dụng nhanh chóng."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Uống với thức ăn để giảm rối loạn tiêu hóa.",
                "timing": "Uống 2 lần/ngày (sáng và tối), cách nhau 12 giờ. AFib: 150mg x 2 lần/ngày (110mg nếu ≥75 tuổi hoặc CrCl 30-50). DVT/PE: 150mg x 2 lần/ngày. KHÔNG MỞ VIÊN NANG.",
                "notes": "KHÔNG MỞ VIÊN NANG - tăng hấp thu, tăng nguy cơ chảy máu. Uống với thức ăn để giảm rối loạn tiêu hóa."
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pradaxa (dabigatran)",
                "RE-LY Study - New England Journal of Medicine",
                "UpToDate - Dabigatran: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High (FDA-approved, large RCT - RE-LY study)"
        }
    },
    
    "Dipyridamole": {
        "group": "Cardiovascular - Antiplatelet",
        "vietnamese_name": "Dipyridamole, Persantine",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ/TIA (kết hợp với aspirin)",
            "Phòng ngừa huyết khối sau phẫu thuật van tim"
        ],
        "contraindications": [
            "Nhồi máu cơ tim cấp",
            "Co thắt mạch vành (vasospasm)"
        ],
        "dosage": {
            "adult_standard": "200mg x 2 lần/ngày (với aspirin)",
            "adult_modified_release": "200mg x 2 lần/ngày",
            "notes": "Thường dùng kết hợp với aspirin 25mg x 2 lần/ngày"
        },
        "side_effects": [
            "Nhức đầu (phổ biến)",
            "Chóng mặt",
            "Đau bụng",
            "Chảy máu",
            "Tim đập nhanh"
        ],
        "interactions": [
            "Aspirin: dùng kèm để tăng hiệu quả",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Medium",
            "organ_toxicity": ["vasodilation_headache"]
        },
        "guideline_tags": [
            "AHA/ASA stroke secondary prevention",
            "ESC antiplatelet (secondary prevention)"
        ],
        "mechanism_of_action": "Dipyridamole ức chế phosphodiesterase và adenosine deaminase, làm tăng nồng độ cAMP và adenosine trong tiểu cầu, ức chế aggregation tiểu cầu. Thuốc cũng ức chế tái hấp thu adenosine, làm giãn mạch vành. Dipyridamole thường dùng kết hợp với aspirin để phòng ngừa đột quỵ/TIA sau stroke hoặc TIA. Thuốc có tác dụng chống đông và giãn mạch, nhưng có thể gây nhức đầu do giãn mạch. Thường dùng dạng modified-release để giảm tác dụng phụ.",
        "monitoring": [
            "Dấu hiệu chảy máu (xuất huyết, chảy máu chân răng, chảy máu cam)",
            "Nhức đầu (tác dụng phụ phổ biến, có thể giảm khi dùng liều thấp hơn)",
            "Huyết áp (có thể giảm nhẹ do giãn mạch)",
            "Nhịp tim (có thể tăng nhẹ)",
            "Đáp ứng điều trị (giảm nguy cơ đột quỵ/TIA)"
        ],
        "precautions": [
            "Thường dùng kết hợp với aspirin 25mg x 2 lần/ngày để tăng hiệu quả",
            "Nhức đầu là tác dụng phụ phổ biến (có thể giảm khi dùng liều thấp hơn hoặc dạng modified-release)",
            "Tránh dùng trong nhồi máu cơ tim cấp (có thể làm nặng thêm)",
            "Thận trọng ở bệnh nhân co thắt mạch vành (vasospasm)",
            "Tránh dùng với warfarin (tăng nguy cơ chảy máu)",
            "Có thể gây chóng mặt, đau bụng",
            "Ngừng 5-7 ngày trước phẫu thuật lớn",
            "Thận trọng ở bệnh nhân hạ huyết áp"
        ],
        "pharmacokinetics": {
            "half_life": "10-12 giờ",
            "onset": "2-4 giờ",
            "duration": "12-24 giờ",
            "protein_binding": "91-99%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Cần xem xét black box warnings",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - cần xem xét dữ liệu an toàn thai kỳ.",
            "lactation": {
            "safety": "Compatible with monitoring",
            "details": "Cần xem xét dữ liệu an toàn khi cho con bú.",
            "recommendation": "Thận trọng khi cho con bú.",
        },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Cần xem xét chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": [
            "Cần xem xét triệu chứng quá liều",
        ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
            "Ngừng ngay thuốc",
            "Hỗ trợ và điều trị triệu chứng",
            "Theo dõi dấu hiệu sinh tồn",
        ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu lâm sàng",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
            "with_food": "Cần xem xét uống với hoặc không có thức ăn",
            "timing": "Cần xem xét thời điểm dùng",
            "notes": "Cần xem xét hướng dẫn cụ thể",
        },
        },
        "references": {
            "primary_sources": [
            "FDA Drug Label - Dipyridamole, Persantine",
            "UpToDate - Drug information",
        ],
            "last_updated": "2025-02-05",
            "evidence_level": "A",
        },
    },
    
    "Edoxaban": {
        "group": "Hematology - Anticoagulant (Direct Factor Xa Inhibitor, DOAC)",
        "vietnamese_name": "Edoxaban, Lixiana, Savaysa",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
            "Điều trị DVT/PE"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Suy thận nặng (CrCl <15)",
            "Có thai",
            "Dị ứng edoxaban"
        ],
        "dosage": {
            "adult_afib": "60mg x 1 lần/ngày (30mg nếu CrCl 15-50, cân nặng ≤60kg, hoặc dùng P-gp inhibitors)",
            "adult_dvt_pe": "60mg x 1 lần/ngày (30mg nếu CrCl 15-50, cân nặng ≤60kg, hoặc dùng P-gp inhibitors)",
            "notes": "Điều chỉnh liều theo chức năng thận, cân nặng, và tương tác thuốc. Không cần theo dõi INR/aPTT thường xuyên"
        },
        "side_effects": [
            "Chảy máu (phổ biến)",
            "Rối loạn tiêu hóa",
            "Nhức đầu"
        ],
        "interactions": [
            "P-gp inhibitors mạnh (ketoconazole, dronedarone): tăng nồng độ (giảm liều xuống 30mg)",
            "P-gp inducers (rifampin): giảm nồng độ",
            "Aspirin/NSAID: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C - Tránh dùng",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": "High",
            "icu_critical_care_only": False
        },
        "guideline_tags": [
            "AHA/ACC/HRS AF stroke prevention",
            "ISTH VTE treatment/prophylaxis",
            "ESC AF guidelines"
        ],
        "mechanism_of_action": "Edoxaban là direct factor Xa inhibitor, ức chế trực tiếp yếu tố Xa mà không cần antithrombin III. Edoxaban gắn trực tiếp với Xa, ngăn chặn chuyển đổi prothrombin thành thrombin, ức chế hình thành cục máu đông. Thuốc là DOAC (direct oral anticoagulant), không cần theo dõi INR/aPTT thường xuyên như warfarin. Edoxaban được thải trừ chủ yếu qua thận (50%) và một phần qua gan (50%), nên cần điều chỉnh liều ở suy thận. Không có antidote đặc hiệu (khác apixaban, rivaroxaban).",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
            "Chức năng thận (CrCl) - mỗi 3-6 tháng (edoxaban thải trừ một phần qua thận)",
            "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
            "Dấu hiệu rối loạn tiêu hóa"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận (CrCl), cân nặng, và tương tác thuốc - mỗi 3-6 tháng",
            "Suy thận nặng (CrCl <15) - chống chỉ định",
            "Giảm liều xuống 30mg x 1 lần/ngày nếu CrCl 15-50, cân nặng ≤60kg, hoặc dùng P-gp inhibitors mạnh",
            "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
            "Không có antidote đặc hiệu (khác apixaban, rivaroxaban) - điều trị hỗ trợ nếu chảy máu",
            "Tránh dùng với P-gp inhibitors mạnh (ketoconazole, dronedarone) - giảm liều xuống 30mg nếu phải dùng",
            "Ngừng 1-2 ngày trước phẫu thuật lớn (tùy chức năng thận)",
            "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
        ],
        "pharmacokinetics": {
            "half_life": "10-14 giờ (bình thường), 15-20 giờ (suy thận)",
            "onset": "1-2 giờ",
            "duration": "12-24 giờ",
            "protein_binding": "55%",
            "clearance": "Thận (50% - thải trừ nguyên dạng). Gan (50% - chuyển hóa). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Suy thận nặng (CrCl <15) - chống chỉ định. Không ngừng đột ngột (tăng nguy cơ đột quỵ trong rung nhĩ).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "P-gp inhibitors mạnh (ketoconazole, dronedarone)",
                    "mechanism": "Ức chế P-gp, tăng nồng độ edoxaban",
                    "effect": "Tăng nồng độ edoxaban, tăng nguy cơ chảy máu",
                    "management": "Giảm liều xuống 30mg x 1 lần/ngày khi dùng với P-gp inhibitors mạnh. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "P-gp inducers (rifampin)",
                    "mechanism": "Cảm ứng P-gp, giảm nồng độ edoxaban",
                    "effect": "Giảm nồng độ edoxaban, giảm hiệu quả",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <15) - chống chỉ định",
                "Dị ứng edoxaban"
            ],
            "tương_đối": [
                "Suy thận (CrCl 15-50) - giảm liều xuống 30mg x 1 lần/ngày",
                "Cân nặng ≤60kg - giảm liều xuống 30mg x 1 lần/ngày",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Có thai - tránh dùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ. Edoxaban có thể gây chảy máu ở mẹ và thai nhi. Chỉ dùng nếu lợi ích > nguy cơ rõ ràng.",
            "lactation": {
                "safety": "Caution",
                "details": "Edoxaban có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Edoxaban chuyển hóa một phần qua gan (50%). Không cần điều chỉnh liều ở suy gan nhẹ. Thận trọng ở suy gan trung bình. Chống chỉ định ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng edoxaban ngay lập tức",
                "Nếu không có andexanet: PCC 4 yếu tố (≈50 IU/kg) + than hoạt sớm nếu mới uống",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Rửa dạ dày nếu uống trong vòng 2 giờ",
                "Than hoạt tính",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                "Theo dõi ít nhất 24 giờ (do half-life 10-14 giờ)"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày. AFib/DVT/PE: 60mg x 1 lần/ngày (30mg nếu CrCl 15-50, cân nặng ≤60kg, hoặc dùng P-gp inhibitors mạnh)."
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Savaysa (edoxaban)",
                "ENGAGE AF-TIMI 48 Study - New England Journal of Medicine",
                "UpToDate - Edoxaban: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High (FDA-approved, large RCT - ENGAGE AF-TIMI 48 study)"
        }
    },
    
    "Eltrombopag": {
        "group": "Hematology - TPO Receptor Agonist",
        "vietnamese_name": "Eltrombopag, Promacta",
        "administration": ["PO"],
        "indications": [
            "Thiếu máu giảm tiểu cầu miễn dịch (ITP) - chronic",
            "Thiếu máu giảm tiểu cầu ở bệnh nhân viêm gan C",
            "Thiếu máu giảm tiểu cầu ở bệnh nhân suy tủy xương nặng (severe aplastic anemia)",
            "Thiếu máu giảm tiểu cầu ở bệnh nhân ung thư hóa trị liệu"
        ],
        "contraindications": [
            "Dị ứng eltrombopag hoặc bất kỳ thành phần nào",
            "Bệnh gan nặng (Child-Pugh class C)"
        ],
        "dosage": {
            "adult_itp": "50mg PO mỗi ngày (có thể tăng đến 75mg/ngày nếu cần)",
            "adult_hepatitis_c": "25mg PO mỗi ngày (có thể tăng đến 100mg/ngày nếu cần)",
            "adult_aplastic_anemia": "150mg PO mỗi ngày (có thể tăng đến 300mg/ngày nếu cần)",
            "notes": "Uống khi đói (ít nhất 1 giờ trước hoặc 2 giờ sau bữa ăn). Không uống với sữa, canxi, hoặc antacids. Điều chỉnh liều theo số lượng tiểu cầu."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Nhức đầu - phổ biến",
            "Mệt mỏi",
            "Buồn nôn",
            "Tiêu chảy",
            "Tăng men gan (ALT, AST) - phổ biến, có thể nghiêm trọng",
            "Tăng bilirubin - có thể nghiêm trọng",
            "Tăng nguy cơ huyết khối (thrombosis) - do tăng số lượng tiểu cầu",
            "Tăng nguy cơ xơ tủy xương (bone marrow fibrosis) - với dùng dài ngày",
            "Đục thủy tinh thể (cataract) - với dùng dài ngày"
        ],
        "interactions": [
            "Sữa, canxi, antacids, sắt: giảm hấp thu (uống cách xa ít nhất 2 giờ)",
            "Cholestyramine: giảm hấp thu",
            "Thuốc chống đông/kháng tiểu cầu: tăng nguy cơ huyết khối do tăng số lượng tiểu cầu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Eltrombopag là chất chủ vận thụ thể thrombopoietin (TPO receptor agonist, non-peptide). "
            "Thrombopoietin là hormone tự nhiên kích thích sản xuất tiểu cầu từ megakaryocytes trong tủy xương. "
            "Trong ITP và các tình trạng giảm tiểu cầu khác, có sự thiếu hụt hoặc giảm đáp ứng với TPO. "
            "Eltrombopag gắn với thụ thể TPO trên megakaryocytes → kích thích tăng sinh và biệt hóa megakaryocytes → "
            "tăng sản xuất tiểu cầu từ tủy xương. "
            "Dẫn đến: tăng số lượng tiểu cầu trong máu, giảm nguy cơ chảy máu. "
            "Eltrombopag được dùng để điều trị giảm tiểu cầu trong ITP, viêm gan C, suy tủy xương, và ung thư hóa trị liệu. "
            "Khác với romiplostim (peptide TPO mimetic), eltrombopag là non-peptide, dùng đường uống, "
            "và có tương tác với thức ăn (giảm hấp thu với sữa, canxi, antacids)."
        ),
        "monitoring": [
            "Số lượng tiểu cầu - theo dõi thường xuyên (hàng tuần khi bắt đầu, sau đó định kỳ)",
            "Chức năng gan (ALT, AST, bilirubin) - theo dõi định kỳ, tăng men gan phổ biến",
            "Dấu hiệu huyết khối (đau ngực, khó thở, đau chân, sưng chân) - do tăng số lượng tiểu cầu",
            "Dấu hiệu xơ tủy xương (bone marrow fibrosis) - với dùng dài ngày",
            "Khám mắt định kỳ - theo dõi đục thủy tinh thể với dùng dài ngày"
        ],
        "precautions": [
            "TĂNG MEN GAN - phổ biến và có thể nghiêm trọng, cần theo dõi chức năng gan định kỳ",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh gan nặng (Child-Pugh class C)",
            "NGUY CƠ HUYẾT KHỐI - do tăng số lượng tiểu cầu, đặc biệt khi số lượng tiểu cầu >400,000/μL",
            "Uống khi đói (ít nhất 1 giờ trước hoặc 2 giờ sau bữa ăn) - quan trọng để tăng hấp thu",
            "Không uống với sữa, canxi, antacids, sắt - giảm hấp thu, uống cách xa ít nhất 2 giờ",
            "Điều chỉnh liều theo số lượng tiểu cầu - giảm liều nếu số lượng tiểu cầu >400,000/μL",
            "Thận trọng khi dùng với thuốc chống đông/kháng tiểu cầu - tăng nguy cơ huyết khối",
            "Ngừng thuốc nếu tăng men gan nặng hoặc tăng bilirubin"
        ],
        "pharmacokinetics": {
            "half_life": "~26-35 giờ (dài)",
            "onset": "1-2 tuần (tác dụng chậm)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": ">99%",
            "metabolism": "Gan (chuyển hóa qua CYP1A2, CYP2C8, UGT1A1, UGT1A3)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Cần điều chỉnh liều ở suy gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": (
            "NGUY CƠ TĂNG MEN GAN - có thể nghiêm trọng. Cần theo dõi chức năng gan (ALT, AST, bilirubin) định kỳ. "
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh gan nặng (Child-Pugh class C). "
            "Ngừng thuốc nếu tăng men gan nặng hoặc tăng bilirubin. "
            "NGUY CƠ HUYẾT KHỐI - do tăng số lượng tiểu cầu, đặc biệt khi số lượng tiểu cầu >400,000/μL. "
            "Điều chỉnh liều để tránh số lượng tiểu cầu quá cao."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Sữa, canxi, antacids, sắt",
                    "mechanism": "Giảm hấp thu eltrombopag",
                    "effect": "Giảm hiệu quả eltrombopag",
                    "management": "Uống cách xa ít nhất 2 giờ. Uống eltrombopag khi đói (ít nhất 1 giờ trước hoặc 2 giờ sau bữa ăn)."
                },
                {
                    "drug": "Cholestyramine",
                    "mechanism": "Giảm hấp thu eltrombopag",
                    "effect": "Giảm hiệu quả eltrombopag",
                    "management": "Uống cách xa ít nhất 4 giờ."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc chống đông/kháng tiểu cầu (warfarin, aspirin, clopidogrel)",
                    "mechanism": "Tăng số lượng tiểu cầu + chống đông/kháng tiểu cầu",
                    "effect": "Tăng nguy cơ huyết khối",
                    "management": "Thận trọng. Theo dõi số lượng tiểu cầu và dấu hiệu huyết khối."
                },
                {
                    "drug": "CYP1A2 inhibitors (fluvoxamine, ciprofloxacin)",
                    "mechanism": "Ức chế chuyển hóa eltrombopag",
                    "effect": "Tăng nồng độ eltrombopag, tăng tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều eltrombopag."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng eltrombopag hoặc bất kỳ thành phần nào",
                "Bệnh gan nặng (Child-Pugh class C)"
            ],
            "tương_đối": [
                "Bệnh gan (Child-Pugh class A-B) - tăng nguy cơ tăng men gan",
                "Tiền sử huyết khối - tăng nguy cơ huyết khối do tăng số lượng tiểu cầu",
                "Đang dùng thuốc chống đông/kháng tiểu cầu - tăng nguy cơ huyết khối"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Giảm liều 50%. Theo dõi chức năng gan chặt chẽ",
            "severe": "CHỐNG CHỈ ĐỊNH (Child-Pugh class C)",
            "notes": "Eltrombopag chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tăng men gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng số lượng tiểu cầu quá cao (>400,000/μL) - tăng nguy cơ huyết khối",
                "Tăng men gan nặng",
                "Tăng bilirubin nặng",
                "Nhức đầu, mệt mỏi, buồn nôn nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc ngay",
                "Theo dõi số lượng tiểu cầu - có thể cần phlebotomy nếu quá cao",
                "Theo dõi chức năng gan chặt chẽ",
                "Xử trí huyết khối nếu có (anticoagulation nếu cần)",
                "Điều trị hỗ trợ triệu chứng"
            ],
            "monitoring": "Số lượng tiểu cầu, chức năng gan (ALT, AST, bilirubin), dấu hiệu huyết khối"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi đói (ít nhất 1 giờ trước hoặc 2 giờ sau bữa ăn) - QUAN TRỌNG để tăng hấp thu",
                "timing": "Uống 1 lần/ngày khi đói. Không uống với sữa, canxi, antacids, sắt (uống cách xa ít nhất 2 giờ).",
                "notes": "Uống khi đói để tăng hấp thu. Không uống với sữa, canxi, antacids, sắt. Điều chỉnh liều theo số lượng tiểu cầu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Eltrombopag (Promacta)",
                "UpToDate - Eltrombopag: Drug information",
                "Lexicomp - Eltrombopag monograph",
                "ASH Guidelines - ITP"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in ITP"
        }
    },

    "Emicizumab": {
        "group": "Hematology - Bispecific Monoclonal Antibody",
        "vietnamese_name": "Emicizumab, Hemlibra",
        "administration": ["SC"],
        "indications": [
            "Hemophilia A (với hoặc không có chất ức chế factor VIII)",
            "Phòng ngừa chảy máu ở bệnh nhân hemophilia A"
        ],
        "contraindications": [
            "Dị ứng emicizumab hoặc bất kỳ thành phần nào",
            "Đang có huyết khối đang hoạt động"
        ],
        "dosage": {
            "adult_loading": "3mg/kg SC tuần 1, 2, 4",
            "adult_maintenance": "1.5mg/kg SC mỗi tuần, hoặc 3mg/kg SC mỗi 2 tuần, hoặc 6mg/kg SC mỗi 4 tuần",
            "notes": "Tiêm dưới da (SC) ở vùng bụng, đùi, hoặc cánh tay. Có thể tự tiêm sau khi được hướng dẫn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, ngứa) - phổ biến",
            "Nhức đầu",
            "Mệt mỏi",
            "Buồn nôn",
            "Tăng nguy cơ huyết khối (thrombosis) - hiếm nhưng nghiêm trọng, đặc biệt khi dùng với activated prothrombin complex concentrate (aPCC)",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Activated prothrombin complex concentrate (aPCC): tăng nguy cơ huyết khối nghiêm trọng",
            "Recombinant factor VIIa: có thể tăng nguy cơ huyết khối"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Emicizumab là bispecific monoclonal antibody (humanized) gắn đồng thời với factor IXa và factor X. "
            "Trong hemophilia A, thiếu factor VIII dẫn đến không thể hình thành phức hợp tenase (factor VIIIa/factor IXa) "
            "cần thiết để kích hoạt factor X thành factor Xa, dẫn đến rối loạn đông máu và chảy máu. "
            "Emicizumab bắt chước chức năng của factor VIIIa bằng cách gắn với factor IXa và factor X, "
            "tạo thành phức hợp tương tự tenase mà không cần factor VIII. "
            "Dẫn đến: kích hoạt factor X thành factor Xa, hình thành thrombin, và đông máu bình thường. "
            "Emicizumab được dùng để phòng ngừa chảy máu ở bệnh nhân hemophilia A, "
            "đặc biệt hiệu quả ở bệnh nhân có chất ức chế factor VIII (kháng thể kháng factor VIII) "
            "vì các thuốc thay thế factor VIII truyền thống không hiệu quả ở những bệnh nhân này. "
            "Emicizumab có half-life dài, cho phép dùng 1-4 tuần một lần (tùy phác đồ)."
        ),
        "monitoring": [
            "Tần suất và mức độ nghiêm trọng của chảy máu (theo dõi nhật ký chảy máu)",
            "Phản ứng tại chỗ tiêm",
            "Dấu hiệu huyết khối (đau ngực, khó thở, đau chân, sưng chân) - đặc biệt khi dùng với aPCC",
            "Dấu hiệu dị ứng (phát ban, khó thở, phù mạch)",
            "Chức năng gan (ALT, AST) - theo dõi định kỳ"
        ],
        "precautions": [
            "NGUY CƠ HUYẾT KHỐI - đặc biệt khi dùng với activated prothrombin complex concentrate (aPCC), "
            "cần theo dõi chặt chẽ dấu hiệu huyết khối",
            "Tránh dùng aPCC với emicizumab nếu có thể - nếu cần dùng, dùng liều thấp nhất và theo dõi chặt chẽ",
            "Có thể tự tiêm sau khi được hướng dẫn đúng cách",
            "Không dùng để điều trị cấp tính chảy máu nặng (cần dùng factor VIII hoặc bypassing agents)",
            "Thận trọng ở bệnh nhân có tiền sử huyết khối",
            "Có thể mất vài tuần để đạt hiệu quả đầy đủ"
        ],
        "pharmacokinetics": {
            "half_life": "~4-5 tuần (rất dài, cho phép dùng 1-4 tuần một lần)",
            "onset": "Vài tuần (tác dụng chậm)",
            "duration": "Dài (do half-life rất dài)",
            "protein_binding": "IgG4 bispecific monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 7 ngày. Không làm nóng hoặc lắc mạnh.",
        "black_box_warnings": (
            "NGUY CƠ HUYẾT KHỐI - đặc biệt khi dùng với activated prothrombin complex concentrate (aPCC). "
            "Có báo cáo huyết khối tĩnh mạch sâu (DVT), thuyên tắc phổi (PE), và huyết khối động mạch. "
            "Tránh dùng aPCC với emicizumab nếu có thể. Nếu cần dùng, dùng liều thấp nhất và theo dõi chặt chẽ dấu hiệu huyết khối."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Activated prothrombin complex concentrate (aPCC, FEIBA)",
                    "mechanism": "Tăng nguy cơ huyết khối khi dùng với emicizumab",
                    "effect": "Tăng nguy cơ huyết khối nghiêm trọng (DVT, PE, huyết khối động mạch)",
                    "management": "Tránh dùng nếu có thể. Nếu cần dùng, dùng liều thấp nhất (≤50 U/kg/24h) và theo dõi chặt chẽ dấu hiệu huyết khối."
                },
                {
                    "drug": "Recombinant factor VIIa (rFVIIa)",
                    "mechanism": "Có thể tăng nguy cơ huyết khối",
                    "effect": "Tăng nguy cơ huyết khối",
                    "management": "Thận trọng. Theo dõi chặt chẽ dấu hiệu huyết khối."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng emicizumab hoặc bất kỳ thành phần nào",
                "Đang có huyết khối đang hoạt động"
            ],
            "tương_đối": [
                "Tiền sử huyết khối - tăng nguy cơ huyết khối",
                "Đang dùng aPCC - tăng nguy cơ huyết khối nghiêm trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Emicizumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ huyết khối",
                "Phản ứng tại chỗ tiêm nặng hơn",
                "Dị ứng (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Theo dõi dấu hiệu huyết khối chặt chẽ",
                "Xử trí huyết khối nếu có (anticoagulation, thrombectomy nếu cần)",
                "Xử trí phản ứng dị ứng nếu có (antihistamine, corticosteroid, epinephrine nếu cần)"
            ],
            "monitoring": "Dấu hiệu huyết khối, phản ứng tại chỗ tiêm, dấu hiệu dị ứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dùng trực tiếp từ bút tiêm hoặc ống tiêm đã pha sẵn.",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                "notes": "Có thể tự tiêm sau khi được hướng dẫn. Lưu trữ trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm. Phác đồ: 3mg/kg tuần 1, 2, 4 (loading), sau đó 1.5mg/kg/tuần, 3mg/kg/2 tuần, hoặc 6mg/kg/4 tuần (maintenance)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Emicizumab (Hemlibra)",
                "UpToDate - Emicizumab: Drug information",
                "Lexicomp - Emicizumab monograph",
                "ASH Guidelines - Hemophilia A"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in hemophilia A prevention"
        }
    },

    "Enoxaparin": {
        "group": "Hematology - Anticoagulant (Low Molecular Weight Heparin)",
        "vietnamese_name": "Enoxaparin, Lovenox, Clexane",
        "administration": ["SC", "IV"],
        "indications": [
            "Phòng ngừa huyết khối tĩnh mạch sâu (DVT) sau phẫu thuật",
            "Điều trị DVT/PE",
            "Hội chứng mạch vành cấp (với aspirin)",
            "Phòng ngừa DVT ở bệnh nhân nằm viện"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Giảm tiểu cầu do heparin (HIT)",
            "Dị ứng heparin/enoxaparin",
            "Suy thận nặng (CrCl <30) - thận trọng"
        ],
        "dosage": {
            "adult_prophylaxis": "40mg SC x 1 lần/ngày hoặc 30mg SC x 2 lần/ngày",
            "adult_treatment": "1mg/kg SC x 2 lần/ngày hoặc 1.5mg/kg SC x 1 lần/ngày",
            "adult_acs": "1mg/kg SC x 2 lần/ngày (với aspirin)",
            "notes": "Điều chỉnh liều theo cân nặng. Theo dõi anti-Xa nếu cần"
        },
        "side_effects": [
            "Chảy máu (phổ biến)",
            "Giảm tiểu cầu do heparin (HIT) - hiếm nhưng nguy hiểm",
            "Phản ứng tại chỗ tiêm (đau, ban đỏ)",
            "Tăng transaminase (hiếm)",
            "Loãng xương (với điều trị dài ngày)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Aspirin/NSAID: tăng nguy cơ chảy máu",
            "Thrombolytics: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B - Tương đối an toàn",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hematologic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ACCP/Antithrombotic Therapy Guidelines",
            "ESC VTE Guidelines",
            "AHA/ACC ACS Guidelines",
            "ISTH HIT Guidelines"
        ],
        "mechanism_of_action": "Enoxaparin là low molecular weight heparin (LMWH), ức chế yếu tố Xa và yếu tố IIa (thrombin) thông qua antithrombin III. Enoxaparin có tỷ lệ anti-Xa/anti-IIa cao hơn heparin không phân đoạn (UFH), nên ức chế Xa mạnh hơn. Enoxaparin có thời gian bán thải dài hơn, dự đoán được hơn, và ít gây HIT hơn UFH. Thuốc được thải trừ chủ yếu qua thận, nên cần điều chỉnh liều ở suy thận. Enoxaparin không cần theo dõi aPTT thường xuyên như UFH, nhưng có thể theo dõi anti-Xa nếu cần.",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
            "Công thức máu (tiểu cầu) - theo dõi HIT (giảm tiểu cầu >50% hoặc <150,000/μL)",
            "Anti-Xa nếu cần (điều trị dài ngày, suy thận, béo phì)",
            "Chức năng thận (CrCl) - enoxaparin thải trừ qua thận",
            "Dấu hiệu HIT (giảm tiểu cầu, huyết khối mới) - cấp cứu"
        ],
        "precautions": [
            "Điều chỉnh liều theo cân nặng (1mg/kg cho điều trị)",
            "Giảm tiểu cầu do heparin (HIT) - hiếm nhưng nguy hiểm, ngừng ngay nếu nghi ngờ",
            "Suy thận (CrCl <30) - giảm liều hoặc dùng UFH thay thế",
            "Không cần theo dõi aPTT thường xuyên (khác UFH)",
            "Theo dõi anti-Xa nếu cần (điều trị dài ngày, suy thận, béo phì)",
            "Ngừng 12-24 giờ trước phẫu thuật lớn (tùy liều)",
            "Protamine có thể đảo ngược một phần (không hoàn toàn như UFH)",
            "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
        ],
        "pharmacokinetics": {
            "half_life": "4-5 giờ (SC), 2-3 giờ (IV)",
            "onset": "1-2 giờ (SC)",
            "duration": "12-24 giờ",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (thải trừ chủ yếu - 40% nguyên dạng). Gan (một phần). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Không rung lắc.",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Nguy cơ giảm tiểu cầu do heparin (HIT) - ngừng ngay nếu nghi ngờ. Suy thận nặng tăng nguy cơ chảy máu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR, dấu hiệu chảy máu. Dùng đồng thời trong quá trình khởi đầu warfarin."
                },
                {
                    "drug": "Thrombolytics (alteplase, streptokinase)",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Giảm tiểu cầu do heparin (HIT) đang hoạt động hoặc tiền sử",
                "Dị ứng heparin/enoxaparin"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều hoặc dùng UFH thay thế",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Có thai - tương đối an toàn nhưng thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Tương đối an toàn trong thai kỳ. Enoxaparin không qua nhau thai do kích thước phân tử lớn. Có thể dùng trong thai kỳ nếu cần chống đông. Theo dõi chặt chẽ dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Enoxaparin không bài tiết vào sữa mẹ do kích thước phân tử lớn. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng",
            "notes": "Enoxaparin chuyển hóa một phần qua gan. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
            ],
            "antidote": "Protamine sulfate - đảo ngược một phần (không hoàn toàn như UFH)",
            "treatment": [
                "Ngừng enoxaparin ngay lập tức",
                "Protamine sulfate: 1mg IV cho mỗi 1mg enoxaparin (nếu <8 giờ sau liều cuối). Nếu >8 giờ: 0.5mg protamine cho mỗi 1mg enoxaparin.",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                "Theo dõi ít nhất 24 giờ (do half-life 4-5 giờ)"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, anti-Xa nếu có"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Protamine sulfate",
                    "indication": "Đảo ngược tác dụng enoxaparin (chảy máu nặng)",
                    "dose": "1mg IV cho mỗi 1mg enoxaparin (nếu <8 giờ sau liều cuối). Nếu >8 giờ: 0.5mg protamine cho mỗi 1mg enoxaparin. Tối đa 50mg.",
                    "notes": "Đảo ngược một phần (không hoàn toàn như UFH). Có thể gây phản ứng quá mẫn."
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "sc": {
                "reconstitution": "Dùng trực tiếp, không cần pha",
                "injection_site": "Vùng bụng (tránh rốn 5cm), đùi ngoài, hoặc cánh tay",
                "technique": "Tiêm SC sâu, không xoa bóp sau tiêm",
                "notes": "Tiêm SC sâu. Không xoa bóp sau tiêm. Xoay vị trí tiêm. Prophylaxis: 40mg SC x 1 lần/ngày hoặc 30mg SC x 2 lần/ngày. Treatment: 1mg/kg SC x 2 lần/ngày hoặc 1.5mg/kg SC x 1 lần/ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W",
                "infusion_rate": "Truyền IV bolus hoặc infusion",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Có thể dùng IV nhưng thường dùng SC. IV thường dùng trong cấp cứu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lovenox (enoxaparin)",
                "UpToDate - Enoxaparin: Drug information",
                "American College of Chest Physicians (ACCP) guidelines"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },
    
    "Epoetin alfa": {
        "group": "Hematology - Erythropoiesis-Stimulating Agent (ESA)",
        "vietnamese_name": "Epoetin alfa, Erythropoietin",
        "administration": ["IV", "SC"],
        "indications": [
            "Thiếu máu do suy thận mạn",
            "Thiếu máu do hóa trị ung thư (chọn lọc bệnh nhân)",
            "Giảm nhu cầu truyền máu trong một số phẫu thuật chọn lọc"
        ],
        "contraindications": [
            "Tăng huyết áp không kiểm soát",
            "Phản vệ với epoetin hoặc albumin người",
            "Tiền sử pure red cell aplasia do ESA"
        ],
        "dosage": {
            "ckd_hd_adult": "50–100 units/kg IV hoặc SC, 3 lần/tuần; chỉnh liều theo đáp ứng Hb",
            "ckd_nd_adult": "75 units/kg SC/tuần hoặc chia 2–3 lần/tuần",
            "notes": "Mục tiêu Hb thường 10–11.5 g/dL; tránh Hb >12 g/dL do tăng nguy cơ huyết khối, đột quỵ, nhồi máu cơ tim."
        },
        "side_effects": [
            "Tăng huyết áp hoặc nặng lên tăng huyết áp có sẵn",
            "Huyết khối (DVT, PE, biến cố tim mạch) nếu Hb tăng nhanh/quá cao",
            "Đau đầu, đau cơ, triệu chứng giống cúm",
            "Pure red cell aplasia (rất hiếm)"
        ],
        "interactions": [
            "Thuốc làm tăng nguy cơ huyết khối (estrogen, thuốc tránh thai, thalidomide, lenalidomide)",
            "Thiếu sắt, folate, B12: làm giảm đáp ứng với epoetin (cần bổ sung khi thiếu)"
        ],
        "pregnancy": "C - Có thể dùng nếu cần thiết trong CKD sau khi cân nhắc lợi ích/nguy cơ",
        "mechanism_of_action": "Epoetin alfa là dạng tái tổ hợp của erythropoietin, kích thích tủy xương tăng sinh và biệt hóa dòng hồng cầu. Tăng số lượng hồng cầu, cải thiện vận chuyển oxy nhưng đồng thời làm tăng độ nhớt máu và nguy cơ huyết khối nếu Hb tăng quá cao.",
        "monitoring": [
            "Hemoglobin mỗi 1–2 tuần khi khởi trị, sau đó mỗi 1–3 tháng",
            "Huyết áp thường xuyên (nguy cơ tăng huyết áp)",
            "Ferritin, TSAT (dự trữ sắt) – bổ sung sắt nếu thiếu",
            "Dấu hiệu huyết khối (đau ngực, khó thở, đau/sưng chân)"
        ],
        "precautions": [
            "Không đẩy Hb >12 g/dL. Tăng liều từng bước nhỏ, không tăng dồn dập.",
            "Điều chỉnh hoặc ngừng thuốc nếu Hb tăng >1 g/dL trong 2 tuần.",
            "Đảm bảo dự trữ sắt, folate, B12 đủ trước và trong khi điều trị.",
            "Thận trọng ở bệnh nhân có tiền sử huyết khối, bệnh mạch vành, suy tim."
        ],
        "pharmacokinetics": {
            "half_life": "IV: 4-13 giờ; SC: 24-48 giờ (dài hơn do hấp thu chậm)",
            "onset": "Tăng reticulocyte sau 7-10 ngày, tăng Hb sau 2-4 tuần",
            "duration": "Tác dụng kéo dài sau khi ngừng thuốc",
            "protein_binding": "Không gắn protein đáng kể",
            "clearance": "Thận (chủ yếu), gan (một phần). Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình."
        },
        "storage": "Bảo quản trong tủ lạnh 2–8°C, không đông lạnh, không lắc mạnh. Tránh ánh sáng trực tiếp.",
        "black_box_warnings": "Nguy cơ tăng huyết áp, huyết khối, đột quỵ, nhồi máu cơ tim, và tử vong nếu Hb tăng quá cao (>12 g/dL) hoặc tăng quá nhanh. Không đẩy Hb >12 g/dL. Điều chỉnh hoặc ngừng thuốc nếu Hb tăng >1 g/dL trong 2 tuần.",
        "references": {
            "primary_sources": [
                "KDIGO Anemia in CKD Guidelines",
                "FDA Drug Label - Epoetin alfa",
                "ASCO/ASH Guidelines for ESA use in cancer"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Thromboembolism (DVT, PE, cardiovascular events)", "Hypertension"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Hemoglobin - CRITICAL (target 10-11.5 g/dL, avoid >12 g/dL)", "Blood pressure - CRITICAL (hypertension common)", "Ferritin, TSAT (iron stores)", "Signs of thrombosis (chest pain, dyspnea, leg pain/swelling)"]
        },
        "guideline_tags": [
            "KDIGO Guidelines - Anemia in CKD",
            "ASCO/ASH Guidelines - ESA Use in Cancer",
            "FDA Black Box Warning - Epoetin alfa and Thrombosis/Cardiovascular Events",
            "FDA Black Box Warning - Epoetin alfa and Hypertension"
        ],
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C - Có thể dùng nếu cần thiết trong CKD sau khi cân nhắc lợi ích/nguy cơ",
            "pregnancy_details": "Category C - Có thể dùng nếu cần thiết trong CKD sau khi cân nhắc lợi ích/nguy cơ - cần xem xét dữ liệu an toàn thai kỳ.",
            "lactation": {
            "safety": "Compatible with monitoring",
            "details": "Cần xem xét dữ liệu an toàn khi cho con bú.",
            "recommendation": "Thận trọng khi cho con bú.",
        },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Cần xem xét chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": [
            "Cần xem xét triệu chứng quá liều",
        ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
            "Ngừng ngay thuốc",
            "Hỗ trợ và điều trị triệu chứng",
            "Theo dõi dấu hiệu sinh tồn",
        ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu lâm sàng",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "iv": {
            "reconstitution": "Cần xem xét cách pha",
            "infusion_rate": "Cần xem xét tốc độ truyền",
            "compatibility": [
            "Cần xem xét",
        ],
            "incompatibility": [
            "Cần xem xét",
        ],
            "notes": "Cần xem xét hướng dẫn cụ thể",
        },
        },
    },
    
    "Filgrastim": {
        "group": "Hematology - G-CSF (Granulocyte Colony-Stimulating Factor)",
        "vietnamese_name": "Filgrastim, G-CSF, Neupogen",
        "administration": ["SC", "IV"],
        "indications": [
            "Giảm bạch cầu trung tính do hóa trị (ngăn ngừa nhiễm trùng)",
            "Suy tủy/truyền ghép tủy/xương (bone marrow transplantation)",
            "Huy động tế bào gốc ngoại vi"
        ],
        "contraindications": [
            "Quá mẫn với filgrastim hoặc protein nguồn E. coli",
            "Hội chứng suy hô hấp cấp (ARDS) đang tiến triển – thận trọng/ngừng nếu xấu đi"
        ],
        "dosage": {
            "chemo_neutropenia_adult": "5 mcg/kg/ngày SC hoặc IV, bắt đầu 24–72 giờ sau hóa trị, tiếp tục đến khi ANC >10.000/mm³",
            "stem_cell_mobilization": "10 mcg/kg/ngày SC, vài ngày trước thu thập tế bào gốc",
            "notes": "Liều và thời gian tùy protocol ung bướu/tủy xương cụ thể."
        },
        "side_effects": [
            "Đau xương (rất phổ biến)",
            "Đau cơ, đau đầu, mệt mỏi",
            "Tăng bạch cầu, lách to (hiếm: vỡ lách)",
            "Tăng nhẹ men gan",
            "Hội chứng suy hô hấp cấp (ARDS) hiếm gặp"
        ],
        "interactions": [
            "Không có tương tác thuốc-được biết rõ ràng, nhưng nên tránh dùng quá gần thời điểm hóa trị gây ức chế tủy (theo khuyến cáo từng regimen)."
        ],
        "pregnancy": "C - Dữ liệu hạn chế; cân nhắc nếu lợi ích > nguy cơ",
        "mechanism_of_action": "Filgrastim là dạng tái tổ hợp của yếu tố kích thích cụm bạch cầu hạt (G-CSF). Kích thích tủy xương tăng sinh, biệt hóa và giải phóng bạch cầu trung tính ra máu ngoại vi, rút ngắn thời gian giảm bạch cầu và giảm nguy cơ nhiễm trùng.",
        "monitoring": [
            "Công thức máu (đặc biệt ANC) thường xuyên trong khi điều trị",
            "Kích thước lách (đau bụng trái trên, siêu âm nếu nghi ngờ)",
            "Dấu hiệu nhiễm trùng (sốt, ớn lạnh)",
            "Triệu chứng hô hấp (khó thở, ho, thâm nhiễm phổi – nguy cơ ARDS hiếm)"
        ],
        "precautions": [
            "Thông báo cho bệnh nhân về đau xương – có thể kiểm soát bằng paracetamol hoặc NSAID nếu không chống chỉ định.",
            "Thận trọng ở bệnh nhân có bệnh lý tủy xương ác tính (có thể kích thích tế bào ác tính).",
            "Ngừng thuốc nếu nghi ngờ vỡ lách (đau bụng trái trên, tụt HA).",
            "Theo dõi triệu chứng hô hấp, ngừng nếu nghi ngờ ARDS."
        ],
        "pharmacokinetics": {
            "half_life": "3.5 giờ (IV), 3-4 giờ (SC)",
            "onset": "Tăng ANC sau 1-2 ngày, đạt đỉnh sau 5-7 ngày",
            "duration": "Tác dụng kéo dài trong thời gian điều trị",
            "protein_binding": "Không gắn protein đáng kể",
            "clearance": "Thận (chủ yếu), gan (một phần). Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình."
        },
        "storage": "Bảo quản trong tủ lạnh 2–8°C, không đông lạnh, không lắc mạnh. Có thể để ở nhiệt độ phòng trong thời gian ngắn tùy chế phẩm.",
        "black_box_warnings": None,
        "references": {
            "primary_sources": [
                "ASCO Guidelines for G-CSF use",
                "FDA Drug Label - Filgrastim",
                "UpToDate - Filgrastim: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Splenic rupture (rare)", "ARDS (rare)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (ANC) - CRITICAL (frequent during treatment)", "Spleen size (left upper quadrant pain, ultrasound if suspected)", "Signs of infection", "Respiratory symptoms (dyspnea, cough, pulmonary infiltrates - ARDS risk)"]
        },
        "guideline_tags": [
            "ASCO Guidelines - G-CSF Use",
            "FDA Drug Information - Filgrastim",
            "NCCN Guidelines - Myeloid Growth Factors",
            "UpToDate - Filgrastim Drug Information"
        ],
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Quá mẫn với filgrastim hoặc protein nguồn E. coli"
            ],
            "tương_đối": [
                "Hội chứng suy hô hấp cấp (ARDS) đang tiến triển - thận trọng/ngừng nếu xấu đi"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - dữ liệu hạn chế, cân nhắc nếu lợi ích > nguy cơ. Filgrastim là protein tái tổ hợp, dữ liệu an toàn thai kỳ hạn chế.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Filgrastim bài tiết vào sữa mẹ ở nồng độ thấp. Dữ liệu hạn chế.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc lợi ích và nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Filgrastim thải trừ chủ yếu qua thận, một phần qua gan. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng",
            "dialysis": "Thận trọng",
            "notes": "Filgrastim thải trừ chủ yếu qua thận. Suy thận nặng có thể làm chậm thải trừ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng bạch cầu nặng",
                "Đau xương nặng",
                "Lách to, nguy cơ vỡ lách",
                "Hội chứng suy hô hấp cấp (ARDS)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay filgrastim",
                "Theo dõi công thức máu",
                "Nếu vỡ lách: điều trị cấp cứu (truyền máu, phẫu thuật nếu cần)",
                "Nếu ARDS: hỗ trợ hô hấp, điều trị triệu chứng",
                "Theo dõi dấu hiệu sinh tồn"
            ],
            "monitoring": "Công thức máu, kích thước lách, dấu hiệu sinh tồn, triệu chứng hô hấp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "technique": "Tiêm dưới da, thường ở bụng, đùi, hoặc cánh tay",
                "timing": "Bắt đầu 24-72 giờ sau hóa trị, tiếp tục đến khi ANC >10.000/mm³",
                "notes": "Theo protocol ung bướu/tủy xương cụ thể. Lưu ý: đau xương là tác dụng phụ phổ biến."
            },
            "iv": {
                "reconstitution": "Pha trong Normal saline hoặc D5W theo hướng dẫn",
                "infusion_rate": "Truyền trong 15-30 phút",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [],
                "notes": "Có thể truyền IV, nhưng SC phổ biến hơn. Theo protocol cụ thể."
            }
        }
    },

    "Fondaparinux": {
        "group": "Hematology - Anticoagulant (Synthetic Factor Xa Inhibitor)",
        "vietnamese_name": "Fondaparinux, Arixtra",
        "administration": ["SC"],
        "indications": [
            "Phòng ngừa DVT sau phẫu thuật hông/gối",
            "Điều trị DVT/PE cấp",
            "Hội chứng mạch vành cấp (với aspirin)"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Giảm tiểu cầu nặng (<100,000/μL)",
            "Dị ứng fondaparinux",
            "Suy thận nặng (CrCl <30) - chống chỉ định"
        ],
        "dosage": {
            "adult_prophylaxis": "2.5mg SC x 1 lần/ngày",
            "adult_treatment_dvt_pe": "5mg SC x 1 lần/ngày (<50kg: 5mg; 50-100kg: 7.5mg; >100kg: 10mg)",
            "adult_acs": "2.5mg SC x 1 lần/ngày (với aspirin)",
            "notes": "Liều cố định cho prophylaxis; điều chỉnh theo cân nặng cho điều trị DVT/PE. Không cần theo dõi anti-Xa thường xuyên."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng; cân nhắc giảm liều",
            "under_30": "CHỐNG CHỈ ĐỊNH - không dùng",
            "hemodialysis": "CHỐNG CHỈ ĐỊNH"
        },
        "side_effects": [
            "Chảy máu (phổ biến)",
            "Phản ứng tại chỗ tiêm (đau, ban đỏ)",
            "Giảm tiểu cầu (hiếm, ít hơn heparin)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Aspirin/NSAID: tăng nguy cơ chảy máu",
            "Thrombolytics: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B - Tương đối an toàn",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"hematologic": True, "renal": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ACCP/Antithrombotic Therapy Guidelines",
            "ESC VTE Guidelines",
            "AHA/ACC ACS Guidelines"
        ],
        "mechanism_of_action": (
            "Fondaparinux là synthetic pentasaccharide, ức chế chọn lọc yếu tố Xa thông qua antithrombin III. "
            "Khác với heparin/LMWH, fondaparinux chỉ ức chế Xa (không ức chế IIa/thrombin). "
            "Thuốc có thời gian bán thải dài (~17 giờ), dự đoán được, và không gây HIT (heparin-induced thrombocytopenia). "
            "Thải trừ chủ yếu qua thận (100%), nên CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30)."
        ),
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
            "Công thức máu (tiểu cầu) - ít gây HIT hơn heparin",
            "Chức năng thận (CrCl) - CHỐNG CHỈ ĐỊNH nếu CrCl <30",
            "Anti-Xa (fondaparinux-specific) nếu cần (hiếm khi cần)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30) - tích lũy và tăng nguy cơ chảy máu",
            "Không có antidote đặc hiệu (khác với heparin có protamine)",
            "Thời gian bán thải dài (~17 giờ) - tác dụng kéo dài",
            "Không cần theo dõi anti-Xa thường xuyên (khác heparin)",
            "Ngừng 24-36 giờ trước phẫu thuật lớn (do half-life dài)",
            "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
        ],
        "pharmacokinetics": {
            "half_life": "~17 giờ (dài hơn LMWH)",
            "onset": "2-3 giờ (SC)",
            "duration": "24 giờ",
            "protein_binding": ">94% (gắn với antithrombin III)",
            "clearance": "Thận (100% - thải trừ nguyên dạng). CHỐNG CHỈ ĐỊNH ở suy thận nặng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Không rung lắc.",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30) - tích lũy và tăng nguy cơ chảy máu. Không có antidote đặc hiệu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR, dấu hiệu chảy máu. Dùng đồng thời trong quá trình khởi đầu warfarin."
                },
                {
                    "drug": "Thrombolytics (alteplase, tenecteplase)",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <30 mL/phút) - CHỐNG CHỈ ĐỊNH",
                "Giảm tiểu cầu nặng (<100,000/μL)",
                "Dị ứng fondaparinux"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-50) - thận trọng, cân nhắc giảm liều",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng 24-36 giờ trước phẫu thuật",
                "Có thai - tương đối an toàn nhưng thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Tương đối an toàn trong thai kỳ. Fondaparinux không qua nhau thai do kích thước phân tử lớn. Có thể dùng trong thai kỳ nếu cần chống đông. Theo dõi chặt chẽ dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Fondaparinux không bài tiết vào sữa mẹ do kích thước phân tử lớn. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng (không chuyển hóa qua gan nhưng có thể ảnh hưởng đến đông máu)",
            "notes": "Fondaparinux không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan. Thận trọng ở suy gan nặng do có thể ảnh hưởng đến đông máu."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
            ],
            "antidote": "KHÔNG CÓ ANTIDOTE ĐẶC HIỆU (khác với heparin có protamine)",
            "treatment": [
                "Ngừng fondaparinux ngay lập tức",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                "Cân nhắc recombinant factor VIIa (rFVIIa) trong chảy máu đe dọa tính mạng (off-label)",
                "Theo dõi ít nhất 48 giờ (do half-life ~17 giờ)"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, anti-Xa (fondaparinux-specific) nếu có"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "KHÔNG CÓ ANTIDOTE ĐẶC HIỆU. Protamine không đảo ngược fondaparinux. Cân nhắc rFVIIa trong chảy máu đe dọa tính mạng (off-label)."
        },
        "administration_instructions": {
            "oral": None,
            "sc": {
                "reconstitution": "Dùng trực tiếp, không cần pha",
                "injection_site": "Vùng bụng (tránh rốn 5cm), đùi ngoài, hoặc cánh tay",
                "technique": "Tiêm SC sâu, không xoa bóp sau tiêm",
                "notes": "Tiêm SC sâu. Không xoa bóp sau tiêm. Xoay vị trí tiêm. Prophylaxis: 2.5mg SC x 1 lần/ngày. Treatment DVT/PE: 5mg SC (<50kg), 7.5mg SC (50-100kg), 10mg SC (>100kg) x 1 lần/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Arixtra (Fondaparinux)",
                "ACCP/Antithrombotic Therapy Guidelines",
                "ESC VTE Guidelines",
                "UpToDate - Fondaparinux: Drug information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },
    
    "Heparin": {
        "group": "Hematology - Anticoagulant (Unfractionated Heparin)",
        "vietnamese_name": "Heparin, Unfractionated Heparin, UFH",
        "administration": ["IV", "SC"],
        "indications": [
            "Điều trị DVT/PE",
            "Hội chứng mạch vành cấp",
            "Phòng ngừa huyết khối trong phẫu thuật",
            "Phòng ngừa huyết khối trong lọc máu/thẩm phân phúc mạc",
            "Phòng ngừa huyết khối trong ECMO"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Giảm tiểu cầu do heparin (HIT)",
            "Dị ứng heparin",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_loading": "80 units/kg IV bolus, sau đó 18 units/kg/giờ IV",
            "adult_prophylaxis": "5000 units SC x 2-3 lần/ngày",
            "adult_treatment": "80 units/kg IV bolus, sau đó 18 units/kg/giờ IV (điều chỉnh theo aPTT)",
            "notes": "Điều chỉnh liều theo aPTT (target: 1.5-2.5 x baseline). Theo dõi aPTT mỗi 6 giờ"
        },
        "side_effects": [
            "Chảy máu (phổ biến)",
            "Giảm tiểu cầu do heparin (HIT) - 1-5%",
            "Loãng xương (với điều trị dài ngày)",
            "Tăng transaminase (hiếm)",
            "Phản ứng quá mẫn (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Aspirin/NSAID: tăng nguy cơ chảy máu",
            "Thrombolytics: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C - Tương đối an toàn",
        "mechanism_of_action": "Heparin là glycosaminoglycan, tăng cường hoạt động của antithrombin III (ATIII), ức chế yếu tố Xa và yếu tố IIa (thrombin). Heparin gắn với ATIII, làm thay đổi cấu trúc ATIII, tăng khả năng ức chế Xa và IIa. Heparin có tác dụng nhanh, có thể đảo ngược bằng protamine. Thuốc cần theo dõi aPTT thường xuyên do dự đoán kém. Heparin có thể gây HIT (heparin-induced thrombocytopenia) do tạo kháng thể chống heparin-PF4 complex.",
        "monitoring": [
            "aPTT (activated partial thromboplastin time) - mỗi 6 giờ cho đến khi ổn định, sau đó mỗi 24 giờ (target: 1.5-2.5 x baseline)",
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
            "Công thức máu (tiểu cầu) - theo dõi HIT (giảm tiểu cầu >50% hoặc <150,000/μL) - mỗi 2-3 ngày",
            "Dấu hiệu HIT (giảm tiểu cầu, huyết khối mới) - cấp cứu",
            "Chức năng gan nếu có triệu chứng"
        ],
        "precautions": [
            "Cần theo dõi aPTT thường xuyên (mỗi 6 giờ cho đến khi ổn định) - dự đoán kém",
            "Giảm tiểu cầu do heparin (HIT) - 1-5%, ngừng ngay nếu nghi ngờ",
            "Điều chỉnh liều theo aPTT (target: 1.5-2.5 x baseline)",
            "Protamine có thể đảo ngược hoàn toàn (khác LMWH)",
            "Ngừng ngay nếu có HIT - chuyển sang thuốc chống đông không chứa heparin (argatroban, bivalirudin)",
            "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao",
            "Có thể gây loãng xương với điều trị dài ngày",
            "Ngừng 4-6 giờ trước phẫu thuật lớn"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (IV), 2-4 giờ (SC)",
            "onset": "Ngay lập tức (IV), 1-2 giờ (SC)",
            "duration": "4-6 giờ",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan (một phần), thận (một phần), hệ thống reticuloendothelial. Dự đoán kém, cần theo dõi aPTT."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu.",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Nguy cơ giảm tiểu cầu do heparin (HIT) - 1-5%, ngừng ngay nếu nghi ngờ. Cần theo dõi aPTT thường xuyên.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR, aPTT, dấu hiệu chảy máu. Dùng đồng thời trong quá trình khởi đầu warfarin."
                },
                {
                    "drug": "Thrombolytics (alteplase, streptokinase)",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Giảm tiểu cầu do heparin (HIT) đang hoạt động hoặc tiền sử",
                "Dị ứng heparin"
            ],
            "tương_đối": [
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Suy gan nặng - thận trọng",
                "Có thai - tương đối an toàn nhưng thận trọng"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Giảm tiểu cầu do heparin (HIT) đang hoạt động hoặc tiền sử",
                "Dị ứng heparin"
            ],
            "tương_đối": [
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Suy gan nặng - thận trọng",
                "Có thai - tương đối an toàn nhưng thận trọng"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ một phần qua thận)",
            "dialysis": "Thận trọng, giảm liều. Heparin không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Heparin thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy."
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tương đối an toàn trong thai kỳ. Heparin không qua nhau thai do kích thước phân tử lớn. Có thể dùng trong thai kỳ nếu cần chống đông. Theo dõi chặt chẽ dấu hiệu chảy máu và aPTT.",
            "lactation": {
                "safety": "Compatible",
                "details": "Heparin không bài tiết vào sữa mẹ do kích thước phân tử lớn. An toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Heparin chuyển hóa một phần qua gan. Thận trọng ở suy gan. Theo dõi aPTT chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
            ],
            "antidote": "Protamine sulfate - đảo ngược hoàn toàn",
            "treatment": [
                "Ngừng heparin ngay lập tức",
                "Protamine sulfate: 1mg IV cho mỗi 100 units heparin (nếu <30 phút sau liều cuối). Nếu 30-60 phút: 0.5-0.75mg protamine cho mỗi 100 units heparin. Nếu >60 phút: 0.25-0.375mg protamine cho mỗi 100 units heparin. Tối đa 50mg.",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, aPTT, công thức máu, dấu hiệu chảy máu",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                "Theo dõi ít nhất 4-6 giờ (do half-life 1-2 giờ)"
            ],
            "monitoring": "Dấu hiệu sống, aPTT, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Protamine sulfate",
                    "indication": "Đảo ngược tác dụng heparin (chảy máu nặng)",
                    "dose": "1mg IV cho mỗi 100 units heparin (nếu <30 phút sau liều cuối). Tối đa 50mg.",
                    "notes": "Đảo ngược hoàn toàn. Có thể gây phản ứng quá mẫn, hạ huyết áp."
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "sc": {
                "reconstitution": "Dùng trực tiếp, không cần pha",
                "injection_site": "Vùng bụng (tránh rốn 5cm), đùi ngoài",
                "technique": "Tiêm SC sâu, không xoa bóp sau tiêm",
                "notes": "Prophylaxis: 5000 units SC x 2-3 lần/ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W",
                "infusion_rate": "Loading: 80 units/kg IV bolus. Maintenance: 18 units/kg/giờ IV (điều chỉnh theo aPTT).",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Theo dõi aPTT mỗi 6 giờ. Điều chỉnh liều theo aPTT (target: 1.5-2.5 x baseline)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Heparin",
                "UpToDate - Heparin: Drug information",
                "American College of Chest Physicians (ACCP) guidelines"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },
    
    "Idarucizumab": {
        "group": "Hematology - DOAC Reversal Agent (Dabigatran)",
        "vietnamese_name": "Idarucizumab, Praxbind",
        "administration": ["IV"],
        "indications": [
            "Đảo ngược tác dụng chống đông của dabigatran trong trường hợp chảy máu đe dọa tính mạng",
            "Đảo ngược tác dụng dabigatran trước phẫu thuật khẩn cấp hoặc thủ thuật xâm lấn",
            "Quá liều dabigatran có triệu chứng"
        ],
        "contraindications": [
            "Dị ứng với idarucizumab hoặc các thành phần",
            "Không có chỉ định đảo ngược dabigatran"
        ],
        "dosage": {
            "adult_standard": "5g IV (2 lọ 2.5g), tiêm nhanh liên tiếp hoặc truyền trong 5-10 phút",
            "notes": "Liều cố định, không cần điều chỉnh theo tuổi, cân nặng, hoặc chức năng thận/gan. Tác dụng ngay lập tức."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
            "hemodialysis": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng dị ứng/phản vệ (hiếm)",
            "Huyết khối tái phát (sau khi đảo ngược)",
            "Hạ kali máu nhẹ (hiếm)"
        ],
        "interactions": [
            "Không có tương tác thuốc đáng kể",
            "Sau khi đảo ngược: có thể dùng lại dabigatran sau 24 giờ nếu cần"
        ],
        "pregnancy": "C - Dữ liệu hạn chế; chỉ dùng khi lợi ích vượt nguy cơ",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": True,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "ISTH 2020 DOAC Reversal Guidelines",
            "ACC/AHA/HRS AF Guidelines",
            "FDA Drug Label - Praxbind"
        ],
        "mechanism_of_action": (
            "Idarucizumab là kháng thể đơn dòng humanized (Fab fragment) gắn đặc hiệu và với ái lực cao "
            "với dabigatran và các chất chuyển hóa của nó. Gắn với dabigatran tạo phức hợp không hoạt tính, "
            "đảo ngược tác dụng chống đông ngay lập tức. Tác dụng đảo ngược hoàn toàn và có thể đo được "
            "bằng aPTT và dTT (dilute thrombin time)."
        ),
        "monitoring": [
            "aPTT, dTT (dilute thrombin time) trước và sau khi dùng để xác nhận đảo ngược",
            "Dấu hiệu chảy máu (nếu dùng cho chảy máu)",
            "Dấu hiệu huyết khối tái phát sau đảo ngược (đặc biệt nếu đã ngừng dabigatran)",
            "Huyết áp, mạch trong quá trình tiêm"
        ],
        "precautions": [
            "Chỉ dùng khi thật sự cần đảo ngược dabigatran (chảy máu đe dọa tính mạng hoặc phẫu thuật khẩn cấp)",
            "Sau đảo ngược: nguy cơ huyết khối tái phát nếu bệnh nhân vẫn cần chống đông",
            "Có thể dùng lại dabigatran sau 24 giờ nếu cần",
            "Chuẩn bị sẵn phương tiện hồi sức cho phản ứng dị ứng (hiếm)"
        ],
        "pharmacokinetics": {
            "half_life": "~10 giờ (Fab fragment)",
            "onset": "Ngay lập tức sau khi tiêm",
            "duration": "Đảo ngược hoàn toàn trong vài phút, kéo dài vài giờ",
            "protein_binding": "Gắn với dabigatran",
            "clearance": "Thải trừ qua thận (không chuyển hóa)"
        },
        "storage": "Bảo quản lạnh 2-8°C, tránh đông lạnh. Sau khi pha, dùng trong 1 giờ ở nhiệt độ phòng hoặc 24 giờ ở 2-8°C.",
        "black_box_warnings": (
            "Sau khi đảo ngược dabigatran, nguy cơ huyết khối tái phát tăng lên. "
            "Cân nhắc dùng lại chống đông sau khi đảo ngược nếu bệnh nhân vẫn có chỉ định chống đông."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với idarucizumab hoặc các thành phần"
            ],
            "tương_đối": [
                "Không có chỉ định đảo ngược dabigatran rõ ràng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế; chỉ dùng khi lợi ích vượt nguy cơ (chảy máu đe dọa tính mạng hoặc phẫu thuật khẩn cấp).",
            "lactation": {
                "safety": "Caution",
                "details": "Không rõ bài tiết sữa; phân tử lớn, hấp thu đường tiêu hóa kém ở trẻ.",
                "recommendation": "Có thể tiếp tục cho bú; theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Idarucizumab không chuyển hóa qua gan; không cần điều chỉnh liều."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng dị ứng/phản vệ (hiếm)",
                "Huyết khối tái phát (nếu đã đảo ngược quá mức)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Xử trí phản ứng dị ứng: epinephrine, diphenhydramine, hydrocortisone nếu cần",
                "Nếu huyết khối tái phát: cân nhắc dùng lại chống đông (dabigatran hoặc thuốc khác) sau 24 giờ"
            ],
            "monitoring": "Huyết động, dấu hiệu dị ứng, dấu hiệu huyết khối trong 24-48 giờ"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha mỗi lọ 2.5g với 50ml NS hoặc D5W (tổng 100ml cho 2 lọ)",
                "infusion_rate": "Tiêm nhanh liên tiếp hoặc truyền trong 5-10 phút",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Liều cố định 5g (2 lọ 2.5g). Không cần điều chỉnh liều. Tác dụng ngay lập tức."
            }
        },
        "references": {
            "primary_sources": [
                "ISTH 2020 Guidelines for DOAC Reversal",
                "ACC/AHA/HRS AF Guidelines",
                "FDA Drug Label - Praxbind (Idarucizumab)",
                "RE-VERSE AD Study"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, guideline-supported"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
    },

    "Prasugrel": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Prasugrel, Effient",
        "administration": ["PO"],
        "indications": [
            "Hội chứng mạch vành cấp cần PCI",
            "Sau đặt stent"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Tiền sử TIA/đột quỵ",
            "Tuổi ≥75 (trừ nguy cơ cao)",
            "Cân nặng <60kg (trừ nguy cơ cao)"
        ],
        "dosage": {
            "adult_loading": "60mg x 1 lần",
            "adult_maintenance": "10mg x 1 lần/ngày (5mg nếu <60kg hoặc ≥75 tuổi)",
            "notes": "Mạnh hơn clopidogrel, nguy cơ chảy máu cao hơn"
        },
        "side_effects": [
            "Chảy máu (nhiều hơn clopidogrel)",
            "Chảy máu lớn (hiếm nhưng nguy hiểm)",
            "Thrombotic thrombocytopenic purpura (TTP) - hiếm"
        ],
        "interactions": [
            "Aspirin: dùng kèm (dual antiplatelet therapy)",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "High",
            "organ_toxicity": []
        },
        "guideline_tags": [
            "ACC/AHA ACS DAPT (PCI)",
            "ESC ACS DAPT (PCI)"
        ],
        "mechanism_of_action": "Prasugrel là chất ức chế P2Y12 receptor, đối kháng không thể đảo ngược (irreversible) với P2Y12 receptor trên tiểu cầu. P2Y12 receptor là một thụ thể adenosine diphosphate (ADP) quan trọng trong quá trình hoạt hóa và kết tập tiểu cầu. Prasugrel là một prodrug, được chuyển hóa nhanh chóng qua CYP3A4 và CYP2B6 thành metabolite hoạt động. Metabolite hoạt động gắn không thể đảo ngược với P2Y12 receptor, ức chế kết tập tiểu cầu do ADP. Prasugrel mạnh hơn và có tác dụng nhanh hơn clopidogrel, với ít biến thể di truyền (genetic variation) hơn. Prasugrel giảm nguy cơ huyết khối trong hội chứng mạch vành cấp cần can thiệp mạch vành (PCI), nhưng tăng nguy cơ chảy máu lớn so với clopidogrel, đặc biệt ở bệnh nhân có tiền sử TIA/đột quỵ hoặc tuổi ≥75.",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu tại vị trí tiêm)",
            "Chảy máu lớn (xuất huyết tiêu hóa, xuất huyết nội sọ, chảy máu sau phẫu thuật) - nguy cơ cao hơn clopidogrel",
            "Thrombotic thrombocytopenic purpura (TTP) - hiếm nhưng nguy hiểm (sốt, thiếu máu, giảm tiểu cầu, rối loạn thần kinh)",
            "Chức năng gan nếu có triệu chứng (hiếm)",
            "Công thức máu (tiểu cầu) nếu có dấu hiệu chảy máu"
        ],
        "precautions": [
            "Dùng kèm với aspirin 75-100mg/ngày (dual antiplatelet therapy - DAPT)",
            "Không dùng ở bệnh nhân có tiền sử TIA hoặc đột quỵ - tăng nguy cơ chảy máu nội sọ",
            "Thận trọng ở bệnh nhân ≥75 tuổi - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
            "Thận trọng ở bệnh nhân <60kg - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
            "Nguy cơ chảy máu cao hơn clopidogrel - không dùng nếu có chảy máu đang hoạt động",
            "Không ngừng đột ngột (tăng nguy cơ huyết khối)",
            "Không dùng ở bệnh nhân có nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây)",
            "Thời gian DAPT thường 12 tháng sau ACS với PCI, có thể kéo dài ở một số bệnh nhân nguy cơ cao",
            "Mạnh hơn clopidogrel - giảm nguy cơ huyết khối nhưng tăng nguy cơ chảy máu",
            "Liều khởi đầu: 60mg loading dose, sau đó 10mg/ngày (5mg nếu <60kg hoặc ≥75 tuổi)"
        ],
        "pharmacokinetics": {
            "half_life": "7 giờ",
            "onset": "30 phút - 1 giờ (nhanh hơn clopidogrel)",
            "duration": "7-10 ngày (do irreversible binding - tiểu cầu mới không bị ảnh hưởng)",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan: chuyển hóa nhanh qua CYP3A4 và CYP2B6 thành metabolite hoạt động (không cần chuyển hóa qua CYP2C19 như clopidogrel). Thận: bài tiết một phần. Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Không dùng ở bệnh nhân có tiền sử TIA hoặc đột quỵ - tăng nguy cơ chảy máu nội sọ. Không dùng ở bệnh nhân có chảy máu đang hoạt động. Thận trọng ở bệnh nhân ≥75 tuổi, <60kg, hoặc có nguy cơ chảy máu cao.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi INR, dấu hiệu chảy máu. Thường tránh dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin",
                    "mechanism": "Dùng kèm trong dual antiplatelet therapy",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Dùng kèm aspirin 75-100mg/ngày. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "Tác dụng hiệp đồng chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Tránh dùng nếu có thể."
                }
            ],
            "minor": [
                {
                    "drug": "CYP inducers/inhibitors",
                    "mechanism": "Prasugrel chuyển hóa qua CYP3A4, CYP2B6, nhưng ít bị ảnh hưởng bởi CYP inhibitors/inducers hơn clopidogrel",
                    "effect": "Tương tác tối thiểu",
                    "management": "Không cần điều chỉnh liều"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Tiền sử TIA hoặc đột quỵ",
                "Dị ứng prasugrel"
            ],
            "tương_đối": [
                "Tuổi ≥75 (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
                "Cân nặng <60kg (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Không có bằng chứng về nguy cơ gây dị tật thai nhi ở động vật. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Nguy cơ chảy máu ở mẹ và thai nhi. Cân nhắc nguy cơ huyết khối vs nguy cơ chảy máu. Theo dõi chặt chẽ dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Caution",
                "details": "Prasugrel và metabolite có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ về dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng",
            "notes": "Prasugrel chuyển hóa ở gan qua CYP3A4 và CYP2B6. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu lớn có thể nghiêm trọng và đe dọa tính mạng",
                "Thrombotic thrombocytopenic purpura (TTP) - hiếm nhưng nguy hiểm"
            ],
            "antidote": "Không có antidote đặc hiệu. Truyền tiểu cầu nếu cần (hiệu quả hạn chế do irreversible binding)",
            "treatment": [
                "Ngừng prasugrel ngay lập tức",
                "Truyền tiểu cầu nếu chảy máu nghiêm trọng (hiệu quả hạn chế do irreversible binding - cần tiểu cầu mới)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi ít nhất 7-10 ngày (do irreversible binding - tiểu cầu mới không bị ảnh hưởng)",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                "Nếu có TTP: điều trị với plasma exchange"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, dấu hiệu TTP"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Uống 1 lần/ngày. Loading dose: 60mg x 1 lần. Maintenance: 10mg x 1 lần/ngày (5mg nếu <60kg hoặc ≥75 tuổi). Dùng kèm aspirin 75-100mg/ngày."
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
                "FDA Drug Label - Effient (prasugrel)",
                "TRITON-TIMI 38 Study - New England Journal of Medicine",
                "UpToDate - Prasugrel: Drug information",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Large RCT (TRITON-TIMI 38 study)"
        }
    },
    
    "Protamine": {
        "group": "Hematology - Anticoagulant Reversal Agent",
        "vietnamese_name": "Protamine sulfate",
        "administration": ["IV"],
        "indications": [
            "Đảo ngược heparin (unfractionated heparin)",
            "Đảo ngược LMWH (một phần, không hoàn toàn)",
            "Chảy máu do heparin",
            "Sau phẫu thuật tim mạch (đảo ngược heparin)"
        ],
        "contraindications": [
            "Dị ứng protamine (đặc biệt bệnh nhân dị ứng cá)",
            "Đã dùng protamine trước đó (tăng nguy cơ phản ứng)",
            "Không dùng để đảo ngược LMWH (không hiệu quả)"
        ],
        "dosage": {
            "adult_heparin_reversal": "1mg protamine cho mỗi 100 units heparin (tối đa 50mg)",
            "adult_lmwh_reversal": "1mg protamine cho mỗi 1mg enoxaparin (không hoàn toàn)",
            "notes": "Tiêm IV chậm (trong 10 phút). Theo dõi aPTT sau 5-15 phút."
        },
        "side_effects": [
            "Hạ huyết áp (phổ biến)",
            "Phản ứng dị ứng (hiếm nhưng nguy hiểm)",
            "Suy hô hấp",
            "Bradycardia",
            "Đông máu (nếu quá liều)"
        ],
        "interactions": [
            "Heparin: đảo ngược tác dụng",
            "LMWH: đảo ngược một phần (không hoàn toàn)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Protamine là protein có nguồn gốc từ tinh trùng cá hồi, có điện tích dương mạnh. Protamine gắn với heparin (có điện tích âm) tạo thành phức hợp không hoạt động, đảo ngược tác dụng chống đông của heparin. Protamine gắn với heparin theo tỷ lệ 1:1 (1mg protamine cho 100 units heparin). Protamine đảo ngược hoàn toàn unfractionated heparin (UFH) nhưng chỉ đảo ngược một phần low molecular weight heparin (LMWH) do LMWH có chuỗi ngắn hơn. Protamine có thể gây phản ứng dị ứng, đặc biệt ở bệnh nhân dị ứng cá hoặc đã dùng protamine trước đó.",
        "monitoring": [
            "Huyết áp (có thể hạ huyết áp)",
            "aPTT (sau 5-15 phút để xác nhận đảo ngược)",
            "Dấu hiệu phản ứng dị ứng (phát ban, khó thở, sốc phản vệ)",
            "Nhịp tim (có thể bradycardia)",
            "Dấu hiệu chảy máu (xem có còn chảy máu sau đảo ngược)"
        ],
        "precautions": [
            "Tiêm IV CHẬM (trong 10 phút) - tiêm nhanh có thể gây hạ huyết áp nghiêm trọng",
            "Thận trọng với bệnh nhân dị ứng cá - tăng nguy cơ phản ứng dị ứng",
            "Thận trọng với bệnh nhân đã dùng protamine trước đó - tăng nguy cơ phản ứng",
            "Theo dõi huyết áp trong khi tiêm",
            "Đảo ngược hoàn toàn UFH, nhưng chỉ đảo ngược một phần LMWH",
            "Không dùng quá liều (có thể gây đông máu)",
            "Theo dõi aPTT sau 5-15 phút để xác nhận đảo ngược",
            "Có thể cần truyền máu nếu chảy máu nặng"
        ],
        "pharmacokinetics": {
            "half_life": "5-7 phút",
            "onset": "Ngay lập tức",
            "duration": "Phụ thuộc vào liều heparin",
            "protein_binding": "Gắn với heparin",
            "clearance": "Chuyển hóa nhanh, thải trừ qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng, dùng trong 24 giờ.",
        "black_box_warnings": "Phản ứng dị ứng nghiêm trọng, có thể gây sốc phản vệ và tử vong. Đặc biệt nguy hiểm ở bệnh nhân dị ứng cá hoặc đã dùng protamine trước đó. Tiêm IV chậm và theo dõi sát.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng protamine",
                "Dị ứng cá (tăng nguy cơ phản ứng dị ứng)"
            ],
            "tương_đối": [
                "Đã dùng protamine trước đó - tăng nguy cơ phản ứng",
                "Bệnh nhân có tiền sử phản ứng dị ứng nặng - thận trọng"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng protamine",
                "Dị ứng cá (tăng nguy cơ phản ứng dị ứng)"
            ],
            "tương_đối": [
                "Đã dùng protamine trước đó - tăng nguy cơ phản ứng",
                "Bệnh nhân có tiền sử phản ứng dị ứng nặng - thận trọng"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, có thể cần giảm liều",
            "dialysis": "Thận trọng, giảm liều. Protamine thải trừ qua thận.",
            "notes": "Protamine thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy."
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần thiết. Protamine được dùng để đảo ngược heparin trong phẫu thuật tim mạch ở phụ nữ có thai.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không rõ protamine có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng.",
                "recommendation": "Thận trọng khi dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Protamine không chuyển hóa ở gan. Suy gan không ảnh hưởng đến protamine."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nghiêm trọng",
                "Suy hô hấp",
                "Bradycardia",
                "Đông máu (nếu quá liều)",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng protamine ngay lập tức",
                "Hỗ trợ hô hấp (intubation nếu cần)",
                "Truyền dịch, vasopressors nếu hạ huyết áp",
                "Điều trị phản ứng dị ứng (epinephrine, corticosteroid, antihistamine)",
                "Theo dõi aPTT, dấu hiệu chảy máu hoặc đông máu"
            ],
            "monitoring": "Huyết áp, nhịp tim, hô hấp, aPTT, dấu hiệu dị ứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W (10mg/ml)",
                "infusion_rate": "Tiêm IV CHẬM trong 10 phút (không quá 5mg/phút)",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Tiêm IV chậm trong 10 phút. Theo dõi huyết áp trong khi tiêm. Liều: 1mg protamine cho mỗi 100 units heparin (tối đa 50mg)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Protamine sulfate",
                "UpToDate - Protamine: Drug information",
                "ACCP Guidelines - Anticoagulant reversal"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, widely used in clinical practice"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Severe allergic reactions (anaphylaxis) - CRITICAL", "Hypotension", "Respiratory depression"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood pressure - CRITICAL (during and after injection)", "aPTT (after 5-15 minutes to confirm reversal)", "Signs of allergic reaction (rash, dyspnea, anaphylaxis) - CRITICAL", "Heart rate (bradycardia)", "Signs of bleeding (check if bleeding persists after reversal)"]
        },
        "guideline_tags": [
            "ACCP Guidelines - Anticoagulant Reversal",
            "AHA/ACC Guidelines - Anticoagulant Reversal",
            "FDA Black Box Warning - Protamine and Anaphylaxis",
            "FDA Drug Information - Protamine"
        ]
    },
    
    "Rivaroxaban": {
        "group": "Hematology - Anticoagulant (Direct Factor Xa Inhibitor, DOAC)",
        "vietnamese_name": "Rivaroxaban, Xarelto",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
            "Điều trị DVT/PE",
            "Phòng ngừa DVT sau phẫu thuật thay khớp háng/gối",
            "Phòng ngừa huyết khối sau hội chứng mạch vành cấp (với aspirin)"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Suy thận nặng (CrCl <15)",
            "Có thai",
            "Dị ứng rivaroxaban"
        ],
        "dosage": {
            "adult_afib": "20mg x 1 lần/ngày (15mg nếu CrCl 15-50)",
            "adult_dvt_pe": "15mg x 2 lần/ngày x 21 ngày, sau đó 20mg x 1 lần/ngày",
            "adult_prophylaxis": "10mg x 1 lần/ngày",
            "adult_acs": "2.5mg x 2 lần/ngày (với aspirin)",
            "notes": "Điều chỉnh liều theo chức năng thận. Uống với thức ăn (liều ≥15mg)"
        },
        "side_effects": [
            "Chảy máu (phổ biến)",
            "Rối loạn tiêu hóa",
            "Nhức đầu"
        ],
        "interactions": [
            "CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir): tăng nồng độ (tránh dùng)",
            "CYP3A4 và P-gp inducers (rifampin): giảm nồng độ",
            "Aspirin/NSAID: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C - Tránh dùng",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "High",
            "organ_toxicity": []
        },
        "guideline_tags": [
            "AHA/ACC/HRS AF stroke prevention",
            "ISTH VTE treatment/prophylaxis",
            "ESC AF guidelines"
        ],
        "mechanism_of_action": "Rivaroxaban là direct factor Xa inhibitor, ức chế trực tiếp yếu tố Xa mà không cần antithrombin III. Rivaroxaban gắn trực tiếp với Xa, ngăn chặn chuyển đổi prothrombin thành thrombin, ức chế hình thành cục máu đông. Thuốc là DOAC (direct oral anticoagulant), không cần theo dõi INR/aPTT thường xuyên như warfarin. Rivaroxaban được thải trừ một phần qua thận (33%) và một phần qua gan (66%), nên cần điều chỉnh liều ở suy thận. Có antidote đặc hiệu: andexanet alfa (Andexxa).",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu)",
            "Chức năng thận (CrCl) - mỗi 3-6 tháng (rivaroxaban thải trừ một phần qua thận)",
            "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
            "Dấu hiệu rối loạn tiêu hóa"
        ],
        "precautions": [
            "Điều chỉnh liều theo chức năng thận (CrCl) - mỗi 3-6 tháng",
            "Suy thận nặng (CrCl <15) - chống chỉ định",
            "Uống với thức ăn (liều ≥15mg) - tăng hấp thu",
            "Không cần theo dõi INR/aPTT thường xuyên (khác warfarin)",
            "Có antidote đặc hiệu: andexanet alfa (Andexxa) - đảo ngược tác dụng",
            "Tránh dùng với CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir) - tăng nồng độ",
            "Ngừng 1-2 ngày trước phẫu thuật lớn (tùy chức năng thận)",
            "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao"
        ],
        "pharmacokinetics": {
            "half_life": "5-9 giờ (bình thường), 9-13 giờ (suy thận)",
            "onset": "2-4 giờ",
            "duration": "12-24 giờ",
            "protein_binding": "92-95%",
            "clearance": "Gan (66% - chuyển hóa qua CYP3A4). Thận (33% - thải trừ nguyên dạng). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Suy thận nặng (CrCl <15) - chống chỉ định. Không ngừng đột ngột (tăng nguy cơ đột quỵ trong rung nhĩ).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)",
                    "mechanism": "Ức chế CYP3A4 và P-gp, tăng nồng độ rivaroxaban",
                    "effect": "Tăng nồng độ rivaroxaban, tăng nguy cơ chảy máu",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng CYP3A4 và P-gp inhibitors mạnh."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "CYP3A4 và P-gp inducers (rifampin)",
                    "mechanism": "Cảm ứng CYP3A4 và P-gp, giảm nồng độ rivaroxaban",
                    "effect": "Giảm nồng độ rivaroxaban, giảm hiệu quả",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <15) - chống chỉ định",
                "Dị ứng rivaroxaban",
                "Dùng CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 15-50) - giảm liều (15mg x 1 lần/ngày cho AFib)",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Có thai - tránh dùng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ. Rivaroxaban có thể gây chảy máu ở mẹ và thai nhi. Chỉ dùng nếu lợi ích > nguy cơ rõ ràng.",
            "lactation": {
                "safety": "Caution",
                "details": "Rivaroxaban có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Rivaroxaban chuyển hóa chủ yếu qua gan (CYP3A4 - 66%). Không cần điều chỉnh liều ở suy gan nhẹ. Thận trọng ở suy gan trung bình. Chống chỉ định ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
            ],
            "antidote": "Andexanet alfa (Andexxa) - antidote đặc hiệu",
            "treatment": [
                "Ngừng rivaroxaban ngay lập tức",
                "Andexanet alfa (Andexxa): 400-800mg IV bolus, sau đó 4-8mg/phút x 2 giờ - đảo ngược tác dụng",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Rửa dạ dày nếu uống trong vòng 2 giờ",
                "Than hoạt tính",
                "Nếu không có andexanet: PCC 4 yếu tố (≈50 IU/kg) + than hoạt sớm",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                "Theo dõi ít nhất 24 giờ (do half-life 5-9 giờ)"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Andexanet alfa (Andexxa)",
                    "indication": "Đảo ngược tác dụng rivaroxaban, apixaban (chảy máu nặng hoặc phẫu thuật cấp cứu)",
                    "dose": "400-800mg IV bolus, sau đó 4-8mg/phút x 2 giờ",
                    "notes": "Antidote đặc hiệu cho rivaroxaban và apixaban. Đảo ngược tác dụng nhanh chóng."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn (liều ≥15mg) - tăng hấp thu. Liều <15mg có thể uống không cần thức ăn.",
                "timing": "AFib: 20mg x 1 lần/ngày (15mg nếu CrCl 15-50), uống với thức ăn. DVT/PE: 15mg x 2 lần/ngày x 21 ngày, sau đó 20mg x 1 lần/ngày, uống với thức ăn. Prophylaxis: 10mg x 1 lần/ngày, có thể uống không cần thức ăn.",
                "notes": "Uống với thức ăn (liều ≥15mg) - tăng hấp thu. Liều <15mg có thể uống không cần thức ăn."
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Xarelto (rivaroxaban)",
                "ROCKET-AF Study - New England Journal of Medicine",
                "UpToDate - Rivaroxaban: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High (FDA-approved, large RCT - ROCKET-AF study)"
        }
    },
    
    "Romiplostim": {
        "group": "Hematology - TPO Mimetic",
        "vietnamese_name": "Romiplostim, Nplate",
        "administration": ["SC"],
        "indications": [
            "Thiếu máu giảm tiểu cầu miễn dịch (ITP) - chronic",
            "Thiếu máu giảm tiểu cầu ở bệnh nhân ung thư hóa trị liệu"
        ],
        "contraindications": [
            "Dị ứng romiplostim hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_itp": "1mcg/kg SC mỗi tuần (có thể tăng đến 10mcg/kg/tuần nếu cần)",
            "adult_chemotherapy": "Liều tùy theo phác đồ hóa trị",
            "notes": "Tiêm dưới da (SC) ở vùng bụng, đùi, hoặc cánh tay. Điều chỉnh liều theo số lượng tiểu cầu. Cần được thực hiện bởi nhân viên y tế."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Nhức đầu - phổ biến",
            "Mệt mỏi",
            "Chóng mặt",
            "Đau khớp",
            "Đau cơ",
            "Phản ứng tại chỗ tiêm (đau, đỏ, ngứa)",
            "Tăng nguy cơ huyết khối (thrombosis) - do tăng số lượng tiểu cầu",
            "Tăng nguy cơ xơ tủy xương (bone marrow fibrosis) - với dùng dài ngày",
            "Tăng nguy cơ tăng sinh tế bào tủy xương (myeloproliferative disorders) - với dùng dài ngày"
        ],
        "interactions": [
            "Thuốc chống đông/kháng tiểu cầu: tăng nguy cơ huyết khối do tăng số lượng tiểu cầu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Romiplostim là TPO mimetic (thrombopoietin mimetic peptide) - một protein tái tổ hợp có cấu trúc tương tự thrombopoietin. "
            "Thrombopoietin là hormone tự nhiên kích thích sản xuất tiểu cầu từ megakaryocytes trong tủy xương. "
            "Trong ITP và các tình trạng giảm tiểu cầu khác, có sự thiếu hụt hoặc giảm đáp ứng với TPO. "
            "Romiplostim gắn với thụ thể TPO trên megakaryocytes → kích thích tăng sinh và biệt hóa megakaryocytes → "
            "tăng sản xuất tiểu cầu từ tủy xương. "
            "Dẫn đến: tăng số lượng tiểu cầu trong máu, giảm nguy cơ chảy máu. "
            "Romiplostim được dùng để điều trị giảm tiểu cầu trong ITP và ung thư hóa trị liệu. "
            "Khác với eltrombopag (non-peptide, đường uống), romiplostim là peptide, dùng đường tiêm dưới da (SC), "
            "và không có tương tác với thức ăn. "
            "Romiplostim có cấu trúc Fc fusion protein, cho phép half-life dài hơn."
        ),
        "monitoring": [
            "Số lượng tiểu cầu - theo dõi thường xuyên (hàng tuần khi bắt đầu, sau đó định kỳ)",
            "Dấu hiệu huyết khối (đau ngực, khó thở, đau chân, sưng chân) - do tăng số lượng tiểu cầu",
            "Dấu hiệu xơ tủy xương (bone marrow fibrosis) - với dùng dài ngày",
            "Dấu hiệu tăng sinh tế bào tủy xương (myeloproliferative disorders) - với dùng dài ngày",
            "Phản ứng tại chỗ tiêm"
        ],
        "precautions": [
            "NGUY CƠ HUYẾT KHỐI - do tăng số lượng tiểu cầu, đặc biệt khi số lượng tiểu cầu >400,000/μL",
            "Điều chỉnh liều theo số lượng tiểu cầu - giảm liều nếu số lượng tiểu cầu >400,000/μL",
            "Thận trọng khi dùng với thuốc chống đông/kháng tiểu cầu - tăng nguy cơ huyết khối",
            "NGUY CƠ XƠ TỦY XƯƠNG - với dùng dài ngày, cần theo dõi tủy xương định kỳ",
            "NGUY CƠ TĂNG SINH TẾ BÀO TỦY XƯƠNG - với dùng dài ngày, cần theo dõi",
            "Cần được thực hiện bởi nhân viên y tế (không tự tiêm như eltrombopag)",
            "Ngừng thuốc nếu số lượng tiểu cầu >400,000/μL hoặc có dấu hiệu xơ tủy xương"
        ],
        "pharmacokinetics": {
            "half_life": "~1-2 tuần (dài, do Fc fusion protein)",
            "onset": "1-2 tuần (tác dụng chậm)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "Fc fusion protein",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không làm nóng hoặc lắc mạnh. Dung dịch pha loãng: dùng trong 24 giờ ở 2-8°C.",
        "black_box_warnings": (
            "NGUY CƠ HUYẾT KHỐI - do tăng số lượng tiểu cầu, đặc biệt khi số lượng tiểu cầu >400,000/μL. "
            "Điều chỉnh liều để tránh số lượng tiểu cầu quá cao. "
            "NGUY CƠ XƠ TỦY XƯƠNG - với dùng dài ngày, có thể dẫn đến xơ tủy xương và suy tủy xương. "
            "Cần theo dõi tủy xương định kỳ. "
            "NGUY CƠ TĂNG SINH TẾ BÀO TỦY XƯƠNG - với dùng dài ngày, có thể dẫn đến myeloproliferative disorders."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc chống đông/kháng tiểu cầu (warfarin, aspirin, clopidogrel)",
                    "mechanism": "Tăng số lượng tiểu cầu + chống đông/kháng tiểu cầu",
                    "effect": "Tăng nguy cơ huyết khối",
                    "management": "Thận trọng. Theo dõi số lượng tiểu cầu và dấu hiệu huyết khối."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng romiplostim hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tiền sử huyết khối - tăng nguy cơ huyết khối do tăng số lượng tiểu cầu",
                "Đang dùng thuốc chống đông/kháng tiểu cầu - tăng nguy cơ huyết khối",
                "Tiền sử xơ tủy xương hoặc myeloproliferative disorders - tăng nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Protein lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Romiplostim chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng số lượng tiểu cầu quá cao (>400,000/μL) - tăng nguy cơ huyết khối",
                "Nhức đầu, mệt mỏi, chóng mặt nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc ngay",
                "Theo dõi số lượng tiểu cầu - có thể cần phlebotomy nếu quá cao",
                "Xử trí huyết khối nếu có (anticoagulation nếu cần)",
                "Điều trị hỗ trợ triệu chứng"
            ],
            "monitoring": "Số lượng tiểu cầu, dấu hiệu huyết khối"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Pha loãng trong nước cất vô trùng theo hướng dẫn hãng.",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                "notes": "Cần được thực hiện bởi nhân viên y tế. Lưu trữ trong tủ lạnh. Điều chỉnh liều theo số lượng tiểu cầu (bắt đầu 1mcg/kg/tuần, có thể tăng đến 10mcg/kg/tuần)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Romiplostim (Nplate)",
                "UpToDate - Romiplostim: Drug information",
                "Lexicomp - Romiplostim monograph",
                "ASH Guidelines - ITP"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in ITP"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Thrombosis (due to increased platelet count) - CRITICAL", "Bone marrow fibrosis (with long-term use) - CRITICAL", "Myeloproliferative disorders (with long-term use)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Platelet count - CRITICAL (frequently when starting, then periodically)", "Signs of thrombosis (chest pain, dyspnea, leg pain, leg swelling) - CRITICAL (due to increased platelet count)", "Signs of bone marrow fibrosis (with long-term use) - CRITICAL", "Signs of myeloproliferative disorders (with long-term use)", "Injection site reactions"]
        },
        "guideline_tags": [
            "ASH Guidelines - Immune Thrombocytopenia",
            "FDA Black Box Warning - Romiplostim and Thrombosis",
            "FDA Black Box Warning - Romiplostim and Bone Marrow Fibrosis",
            "FDA Drug Information - Romiplostim"
        ]
    },
    
    "Tenecteplase": {
        "group": "Hematology - Fibrin-specific thrombolytic (tPA variant)",
        "vietnamese_name": "Tenecteplase, TNK-tPA",
        "administration": ["IV"],
        "indications": [
            "Đột quỵ thiếu máu não cấp (AIS) trong cửa sổ 4.5 giờ – thay thế alteplase ở một số trung tâm",
            "Nhồi máu cơ tim cấp (STEMI) khi không thể PCI kịp thời",
            "Thuyên tắc phổi nguy kịch/huyết động không ổn định (off-label tại nhiều nơi)"
        ],
        "contraindications": [
            "Tiền sử hoặc bằng chứng xuất huyết nội sọ",
            "Đột quỵ xuất huyết hoặc nhồi máu não gần đây (thường <3 tháng, tùy chỉ định)",
            "Phẫu thuật lớn hoặc chấn thương nặng gần đây",
            "Huyết áp rất cao không kiểm soát",
            "Rối loạn đông máu nặng, giảm tiểu cầu rõ",
        ],
        "dosage": {
            "stroke_adult": "0.25 mg/kg IV bolus (tối đa 25mg) một lần duy nhất trong AIS; không khuyến cáo liều 0.4 mg/kg do nguy cơ xuất huyết cao hơn",
            "stemi_adult": "Bolus IV duy nhất: <60kg: 30mg; 60-69kg: 35mg; 70-79kg: 40mg; 80-89kg: 45mg; ≥90kg: 50mg",
            "pe_adult": "0.5 mg/kg IV bolus (tối đa 50mg) – off-label, tùy protocol bệnh viện",
            "notes": "Đảm bảo đáp ứng checklist chống chỉ định trước dùng. Không pha chung với heparin/kháng đông khác trong cùng đường truyền.",
        },
        "side_effects": [
            "Xuất huyết nội sọ (nguy cơ thấp nhưng nghiêm trọng)",
            "Chảy máu tiêu hóa, chảy máu chỗ chọc kim",
            "Hạ huyết áp thoáng qua",
            "Phản vệ (rất hiếm)",
        ],
        "interactions": [
            "Heparin, enoxaparin, DOACs, warfarin: tăng nguy cơ chảy máu",
            "Thuốc kháng tiểu cầu (aspirin, clopidogrel): tăng nguy cơ chảy máu",
        ],
        "pregnancy": "C - Cân nhắc thận trọng, chỉ dùng khi lợi ích vượt trội nguy cơ",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": True,
            "bleeding_risk": "Very High",
            "organ_toxicity": []
        },
        "guideline_tags": [
            "AHA/ASA AIS thrombolysis (0.25 mg/kg bolus centers)",
            "ESC STEMI thrombolysis",
            "CHEST/PE off-label (institutional protocols)"
        ],
        "mechanism_of_action": (
            "Tenecteplase là biến thể tái tổ hợp của tPA với ái lực fibrin cao hơn và kháng PAI-1, "
            "chuyển plasminogen thành plasmin tại cục huyết khối, phân giải fibrin và làm tan huyết khối."
        ),
        "monitoring": [
            "Dấu hiệu thần kinh và NIHSS (AIS) mỗi 15 phút trong và sau bolus, sau đó thưa dần",
            "Huyết áp, mạch, SpO2 liên tục trong 24 giờ đầu",
            "Dấu hiệu chảy máu (da, niêm mạc, tiêu hóa, tiểu máu)",
            "aPTT/INR/tiểu cầu nếu dùng hoặc dự định dùng kháng đông khác",
        ],
        "precautions": [
            "Tuân thủ checklist chống chỉ định tương tự alteplase cho AIS/STEMI.",
            "Tránh chọc kim/đặt catheter không cần thiết trong 24 giờ sau dùng.",
            "Kiểm soát huyết áp trước và sau tiêm (AIS: mục tiêu <185/110 mmHg trước dùng).",
            "Nếu nghi ngờ xuất huyết nội sọ: dừng ngay, chụp CT, xử trí cấp cứu.",
        ],
        "pharmacokinetics": {
            "half_life": "Pha alpha ~20 phút; pha beta ~90-130 phút (dài hơn alteplase)",
            "onset": "Ngay sau bolus",
            "duration": "Hiệu ứng tiêu sợi huyết kéo dài vài giờ",
            "protein_binding": "Gắn fibrin tại huyết khối",
            "clearance": "Gan (chuyển hóa), thận thải trừ một phần",
        },
        "storage": "Bảo quản bột đông khô ở 2–8°C. Sau pha theo hướng dẫn chế phẩm, dùng trong thời gian khuyến cáo; tránh lắc mạnh.",
        "black_box_warnings": "Nguy cơ xuất huyết nội sọ và chảy máu lớn. Chỉ dùng khi đáp ứng tiêu chuẩn lựa chọn và không có chống chỉ định.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Heparin/Enoxaparin/DOACs/Warfarin",
                    "mechanism": "Tăng hiệu ứng chống đông trên nền tiêu sợi huyết",
                    "effect": "Tăng mạnh nguy cơ chảy máu",
                    "management": "Tránh chồng lấp không cần thiết. Nếu phải dùng, theo dõi sát chảy máu và xét nghiệm đông máu.",
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, Clopidogrel, Ticagrelor",
                    "mechanism": "Cộng hưởng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng; giám sát chảy máu. Thường vẫn dùng sau tái tưới máu theo guideline nhưng cần kiểm soát nguy cơ.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Xuất huyết nội sọ hoặc xuất huyết hoạt động",
                "Đột quỵ xuất huyết/nhồi máu não trong 3 tháng (trừ AIS hiện tại)",
                "Phẫu thuật lớn hoặc chấn thương nặng trong 3 tuần gần đây",
                "U não, dị dạng mạch não, phình mạch chưa xử trí",
                "Tiểu cầu <100.000/mm³, INR >1.7 (không do dùng thuốc), aPTT kéo dài không rõ nguyên nhân",
            ],
            "tương_đối": [
                "HA >185/110 mmHg (AIS) hoặc >180/110 (STEMI) chưa kiểm soát",
                "Đái tháo đường kèm đột quỵ cũ (tùy guideline AIS)",
                "Mang thai hoặc hậu sản <10 ngày",
                "Viêm nội tâm mạc nhiễm khuẩn nghi ngờ",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu rất hạn chế; cân nhắc nếu lợi ích cứu mạng vượt nguy cơ chảy máu cho mẹ/thai.",
            "lactation": {
                "safety": "Caution",
                "details": "Không rõ bài tiết sữa; phân tử lớn, hấp thu đường tiêu hóa kém ở trẻ.",
                "recommendation": "Có thể tiếp tục cho bú sau 24 giờ nếu mẹ ổn định; theo dõi chảy máu ở trẻ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh",
            "moderate": "Không cần chỉnh nhưng thận trọng",
            "severe": "Tránh nếu có rối loạn đông máu nặng do suy gan",
        },
        "overdose_management": {
            "symptoms": ["Chảy máu lớn, xuất huyết nội sọ, tụt huyết áp"],
            "antidote": "Không có antidote đặc hiệu; có thể dùng các sản phẩm máu/thuốc chống tiêu sợi huyết",
            "treatment": [
                "Ngừng thuốc, ép chặt vị trí chảy máu nếu có",
                "Truyền cryoprecipitate hoặc fibrinogen concentrate nếu giảm fibrinogen",
                "Truyền tiểu cầu nếu giảm tiểu cầu hoặc dùng kháng tiểu cầu gần đây",
                "Cân nhắc tranexamic acid hoặc aminocaproic acid trong xuất huyết nặng",
                "Hồi sức tích cực, kiểm soát huyết áp, chụp CT nếu nghi xuất huyết nội sọ",
            ],
            "monitoring": "Huyết động, Hb/Hct, tiểu cầu, fibrinogen, aPTT/INR, đánh giá thần kinh lặp lại",
        },
        "reversal_agents": {
            "available": False,
            "agents": ["Tranexamic acid (supportive)", "Cryoprecipitate/fibrinogen concentrate"],
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha bột theo hướng dẫn chế phẩm; thường pha với nước pha tiêm rồi pha loãng nếu cần",
                "infusion_rate": "Tiêm IV bolus chậm trong 5–10 giây (AIS/STEMI)",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không truyền chung heparin/kháng đông cùng đường IV"],
                "notes": "Chuẩn bị sẵn bộ hồi sức và phương án xử trí xuất huyết.",
            }
        },
        "references": {
            "primary_sources": [
                "AHA/ASA 2023–2024 updates on Tenecteplase for AIS (0.25 mg/kg bolus)",
                "ESC STEMI Guidelines (tenecteplase bolus)",
                "CHEST/Institutional protocols for PE thrombolysis (off-label)",
                "FDA Drug Label - Tenecteplase (STEMI)",
            ],
            "last_updated": "2025-03-02",
            "evidence_level": "A (STEMI), B (AIS – trung tâm chọn lọc)",
        },
    },
    
    "Ticagrelor": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Ticagrelor, Brilinta",
        "administration": ["PO"],
        "indications": [
            "Hội chứng mạch vành cấp",
            "Sau đặt stent",
            "Sau nhồi máu cơ tim",
            "Phòng ngừa đột quỵ/TIA"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Xuất huyết nội sọ",
            "Suy gan nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_loading": "180mg x 1 lần",
            "adult_maintenance": "90mg x 2 lần/ngày",
            "notes": "Dùng kèm aspirin 75-100mg/ngày (dual antiplatelet therapy). Dùng với thức ăn để giảm dyspnea"
        },
        "side_effects": [
            "Chảy máu",
            "Khó thở (dyspnea) - phổ biến nhưng thường nhẹ",
            "Chóng mặt",
            "Nhức đầu"
        ],
        "interactions": [
            "Aspirin: dùng kèm (nhưng liều aspirin >100mg/ngày có thể giảm hiệu quả)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Strong CYP3A4 inhibitors: tăng nồng độ (tránh dùng)"
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "High",
            "organ_toxicity": ["bradycardia_dyspnea"]
        },
        "guideline_tags": [
            "ACC/AHA ACS DAPT",
            "ESC ACS DAPT"
        ],
        "mechanism_of_action": "Ticagrelor là chất ức chế P2Y12 receptor chọn lọc, đối kháng có thể đảo ngược (reversible) với P2Y12 receptor trên tiểu cầu. P2Y12 receptor là một thụ thể adenosine diphosphate (ADP) quan trọng trong quá trình hoạt hóa và kết tập tiểu cầu. Khác với clopidogrel và prasugrel (irreversible inhibitors), ticagrelor gắn trực tiếp với P2Y12 receptor mà không cần chuyển hóa thành metabolite hoạt động, và có thể đảo ngược (reversible). Ticagrelor ức chế kết tập tiểu cầu do ADP, giảm nguy cơ huyết khối trong hội chứng mạch vành cấp và sau can thiệp mạch vành. Ticagrelor cũng ức chế tái hấp thu adenosine (adenosine reuptake inhibitor), làm tăng nồng độ adenosine ngoại bào, có thể gây khó thở (dyspnea) và bradycardia. Tác dụng khởi phát nhanh hơn clopidogrel và hiệu quả hơn trong một số nghiên cứu.",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu tại vị trí tiêm)",
            "Chảy máu lớn (xuất huyết tiêu hóa, xuất huyết nội sọ, chảy máu sau phẫu thuật)",
            "Khó thở (dyspnea) - phổ biến (10-20%) nhưng thường nhẹ, có thể do ức chế tái hấp thu adenosine",
            "Nhịp tim chậm (bradycardia) - do tăng adenosine",
            "Chức năng gan nếu có triệu chứng (hiếm)",
            "Tương tác với strong CYP3A4 inhibitors (ketoconazole, clarithromycin) - tăng nồng độ"
        ],
        "precautions": [
            "Dùng kèm với aspirin 75-100mg/ngày (dual antiplatelet therapy - DAPT) - không dùng aspirin >100mg/ngày (có thể giảm hiệu quả)",
            "Không ngừng đột ngột (tăng nguy cơ huyết khối)",
            "Khó thở (dyspnea) - phổ biến nhưng thường nhẹ, có thể giảm khi dùng với thức ăn, thường tự khỏi",
            "Nguy cơ chảy máu cao - không dùng nếu có chảy máu đang hoạt động, xuất huyết nội sọ",
            "Tránh dùng với strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir) - tăng nồng độ",
            "Tránh dùng với strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin) - giảm nồng độ",
            "Dùng với thức ăn để giảm dyspnea và tăng hấp thu",
            "Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình",
            "Thận trọng ở bệnh nhân có tiền sử nhịp tim chậm hoặc block nhĩ thất",
            "Thời gian DAPT thường 12 tháng sau ACS hoặc đặt stent, có thể kéo dài ở một số bệnh nhân nguy cơ cao"
        ],
        "pharmacokinetics": {
            "half_life": "7-9 giờ (ticagrelor), 8-12 giờ (metabolite hoạt động)",
            "onset": "30 phút - 2 giờ (nhanh hơn clopidogrel)",
            "duration": "12 giờ (cần dùng 2 lần/ngày do reversible binding)",
            "protein_binding": ">99%",
            "clearance": "Gan: chuyển hóa qua CYP3A4 thành metabolite hoạt động. Thận: bài tiết một phần. Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Không dùng ở bệnh nhân có xuất huyết nội sọ đang hoạt động, chảy máu đang hoạt động. Không dùng aspirin >100mg/ngày vì có thể giảm hiệu quả của ticagrelor.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa ticagrelor, tăng nồng độ",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng strong CYP3A4 inhibitors."
                },
                {
                    "drug": "Aspirin >100mg/ngày",
                    "mechanism": "Có thể giảm hiệu quả của ticagrelor",
                    "effect": "Giảm hiệu quả chống kết tập tiểu cầu",
                    "management": "Dùng aspirin 75-100mg/ngày. Không dùng aspirin >100mg/ngày."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi INR, dấu hiệu chảy máu. Thường tránh dùng cùng."
                },
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa ticagrelor, giảm nồng độ",
                    "effect": "Giảm hiệu quả ticagrelor",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": [
                {
                    "drug": "Moderate CYP3A4 inhibitors (diltiazem, verapamil)",
                    "mechanism": "Có thể tăng nhẹ nồng độ ticagrelor",
                    "effect": "Tăng nhẹ nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Xuất huyết nội sọ đang hoạt động",
                "Dị ứng ticagrelor",
                "Dùng strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)"
            ],
            "tương_đối": [
                "Suy gan nặng - chống chỉ định",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Tiền sử nhịp tim chậm hoặc block nhĩ thất - tăng nguy cơ bradycardia",
                "Suy thận nặng - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Nguy cơ chảy máu ở mẹ và thai nhi. Cân nhắc nguy cơ huyết khối vs nguy cơ chảy máu. Theo dõi chặt chẽ dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Caution",
                "details": "Ticagrelor và metabolite có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ về dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Ticagrelor chuyển hóa ở gan qua CYP3A4. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Chống chỉ định ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Khó thở (dyspnea) - do tăng adenosine",
                "Nhịp tim chậm (bradycardia)",
                "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
            ],
            "antidote": "Không có antidote đặc hiệu. Truyền tiểu cầu nếu cần",
            "treatment": [
                "Ngừng ticagrelor ngay lập tức",
                "Truyền tiểu cầu nếu chảy máu nghiêm trọng (hiệu quả hạn chế do ticagrelor reversible)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi ít nhất 24-48 giờ (do half-life metabolite 8-12 giờ)",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, ECG (bradycardia)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên dùng với thức ăn để giảm dyspnea và tăng hấp thu",
                "timing": "Uống 2 lần/ngày (sáng và tối), cách nhau 12 giờ. Loading dose: 180mg x 1 lần. Maintenance: 90mg x 2 lần/ngày. Dùng kèm aspirin 75-100mg/ngày."
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
                "FDA Drug Label - Brilinta (ticagrelor)",
                "PLATO Study - New England Journal of Medicine",
                "UpToDate - Ticagrelor: Drug information",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Large RCT (PLATO study)"
        }
    },
    
    "Ticlopidine": {
        "group": "Cardiovascular - Antiplatelet",
        "vietnamese_name": "Ticlopidine, Ticlid",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ sau TIA",
            "Phòng ngừa huyết khối sau stent (ít dùng, thay bằng clopidogrel)"
        ],
        "contraindications": [
            "Giảm bạch cầu/giảm tiểu cầu",
            "Chảy máu đang hoạt động",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "250mg x 2 lần/ngày",
            "notes": "Ít dùng do nguy cơ giảm bạch cầu/tiểu cầu. Clopidogrel thay thế tốt hơn"
        },
        "side_effects": [
            "Giảm bạch cầu (nguy hiểm - cần theo dõi)",
            "Giảm tiểu cầu",
            "Ban xuất huyết giảm tiểu cầu huyết khối (TTP)",
            "Chảy máu",
            "Rối loạn tiêu hóa"
        ],
        "interactions": [
            "Aspirin: tăng nguy cơ chảy máu",
            "Warfarin: tăng nguy cơ chảy máu",
            "Antacids: giảm hấp thu"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ticlopidine là thienopyridine, ức chế P2Y12 receptor trên tiểu cầu, ngăn chặn kích hoạt tiểu cầu bởi ADP. Thuốc ức chế aggregation tiểu cầu và giải phóng các chất tiểu cầu, làm giảm hình thành huyết khối. Ticlopidine là prodrug, chuyển hóa trong gan thành chất hoạt động. Thuốc ức chế mạnh hơn clopidogrel nhưng có nhiều tác dụng phụ nghiêm trọng, đặc biệt giảm bạch cầu và giảm tiểu cầu, nên ít dùng, thay bằng clopidogrel. Thường dùng để phòng ngừa đột quỵ sau TIA, nhưng hiện tại clopidogrel là lựa chọn ưu tiên.",
        "monitoring": [
            "Công thức máu (CBC) - mỗi 2 tuần trong 3 tháng đầu (nguy cơ giảm bạch cầu cao nhất)",
            "Bạch cầu (WBC) - nếu <3500/μL: ngừng ngay",
            "Tiểu cầu - nếu <100,000/μL: ngừng ngay",
            "Dấu hiệu nhiễm trùng (sốt, đau họng) - dấu hiệu giảm bạch cầu",
            "Dấu hiệu chảy máu (xuất huyết, chảy máu chân răng)",
            "Dấu hiệu TTP (sốt, thiếu máu, giảm tiểu cầu, rối loạn thần kinh) - cấp cứu"
        ],
        "precautions": [
            "Ít dùng do nguy cơ giảm bạch cầu/tiểu cầu cao - clopidogrel thay thế tốt hơn",
            "Theo dõi sát công thức máu mỗi 2 tuần trong 3 tháng đầu (nguy cơ cao nhất)",
            "Ngừng ngay nếu giảm bạch cầu <3500/μL hoặc giảm tiểu cầu <100,000/μL",
            "Nguy cơ TTP (thrombotic thrombocytopenic purpura) - cấp cứu, có thể tử vong",
            "Thận trọng ở bệnh nhân suy gan (giảm chuyển hóa)",
            "Tránh dùng với aspirin và warfarin (tăng nguy cơ chảy máu)",
            "Có thể gây rối loạn tiêu hóa (buồn nôn, tiêu chảy)",
            "Ngừng 10-14 ngày trước phẫu thuật lớn"
        ],
        "pharmacokinetics": {
            "half_life": "4-5 ngày (rất dài)",
            "onset": "3-5 ngày (tác dụng tích tụ)",
            "duration": "7-10 ngày sau khi ngừng (do half-life dài)",
            "protein_binding": "98%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ giảm bạch cầu và giảm tiểu cầu nghiêm trọng, đe dọa tính mạng. Nguy cơ TTP (thrombotic thrombocytopenic purpura) có thể tử vong. Cần theo dõi công thức máu thường xuyên",
        "contraindications_detail": {
            "tuyệt_đối": [
                "Giảm bạch cầu/giảm tiểu cầu",
                "Chảy máu đang hoạt động",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Suy thận nặng - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Dùng với aspirin/warfarin - tăng nguy cơ chảy máu"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Ticlopidine không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Ticlopidine thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy."
        },
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - cần xem xét dữ liệu an toàn thai kỳ.",
            "lactation": {
            "safety": "Compatible with monitoring",
            "details": "Cần xem xét dữ liệu an toàn khi cho con bú.",
            "recommendation": "Thận trọng khi cho con bú.",
        },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Cần xem xét chuyển hóa qua gan.",
        },
        "overdose_management": {
            "symptoms": [
            "Cần xem xét triệu chứng quá liều",
        ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
            "Ngừng ngay thuốc",
            "Hỗ trợ và điều trị triệu chứng",
            "Theo dõi dấu hiệu sinh tồn",
        ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu lâm sàng",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
            "with_food": "Cần xem xét uống với hoặc không có thức ăn",
            "timing": "Cần xem xét thời điểm dùng",
            "notes": "Cần xem xét hướng dẫn cụ thể",
        },
        },
        "references": {
            "primary_sources": [
            "FDA Drug Label - Ticlopidine, Ticlid",
            "UpToDate - Drug information",
        ],
            "last_updated": "2025-02-05",
            "evidence_level": "A",
        },
    },
    
    "Tranexamic acid": {
        "group": "Hematology - Antifibrinolytic Agent",
        "vietnamese_name": "Tranexamic acid, Acid tranexamic",
        "administration": ["PO", "IV"],
        "indications": [
            "Chảy máu nặng (trauma, phẫu thuật)",
            "Chảy máu kinh nguyệt nặng",
            "Chảy máu do rối loạn đông máu",
            "Chảy máu do thuốc chống đông",
            "Phẫu thuật tim mạch (giảm chảy máu)",
            "Chảy máu do fibrinogen thấp"
        ],
        "contraindications": [
            "Huyết khối đang hoạt động",
            "Tiền sử huyết khối",
            "Suy thận nặng (CrCl <30) - thận trọng",
            "Dị ứng tranexamic acid"
        ],
        "dosage": {
            "adult_iv_loading": "1g IV trong 10 phút",
            "adult_iv_maintenance": "1g IV mỗi 8 giờ",
            "adult_po": "1-1.5g PO x 3-4 lần/ngày",
            "adult_menorrhagia": "1g PO x 3 lần/ngày trong 3-5 ngày",
            "pediatric": "10mg/kg IV mỗi 8 giờ",
            "notes": "Điều chỉnh liều theo suy thận. Tối đa 4g/ngày."
        },
        "side_effects": [
            "Huyết khối (nguy cơ cao)",
            "Co giật (liều cao IV)",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Nhìn mờ (hiếm)",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Thuốc chống đông: tăng nguy cơ huyết khối",
            "Estrogen: tăng nguy cơ huyết khối",
            "Factor IX concentrates: tăng nguy cơ huyết khối"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Tranexamic acid là chất ức chế plasmin (antifibrinolytic), ngăn chặn quá trình tiêu sợi huyết (fibrinolysis). Tranexamic acid gắn với plasminogen và plasmin, ngăn chặn plasmin gắn với fibrin, do đó ức chế sự phân hủy fibrin và cục máu đông. Tranexamic acid được sử dụng để giảm chảy máu trong các tình huống chảy máu nặng, đặc biệt khi có tăng tiêu sợi huyết (hyperfibrinolysis). Thuốc có hiệu quả trong chảy máu kinh nguyệt nặng, chảy máu do trauma, và chảy máu trong phẫu thuật. Tuy nhiên, tranexamic acid làm tăng nguy cơ huyết khối do ức chế tiêu sợi huyết, nên không dùng ở bệnh nhân có nguy cơ huyết khối.",
        "monitoring": [
            "Dấu hiệu chảy máu (xem có giảm chảy máu)",
            "Dấu hiệu huyết khối (đau ngực, khó thở, đau chân, sưng chân) - NGUY CƠ CAO",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều ở suy thận",
            "Dấu hiệu co giật (với liều cao IV)",
            "Thị lực (nhìn mờ, hiếm)"
        ],
        "precautions": [
            "NGUY CƠ HUYẾT KHỐI CAO - không dùng ở bệnh nhân có huyết khối đang hoạt động hoặc tiền sử huyết khối",
            "Điều chỉnh liều ở suy thận: CrCl 30-60 → giảm liều 50%, CrCl <30 → giảm liều 75%",
            "Thận trọng với bệnh nhân có nguy cơ huyết khối (ung thư, bất động, suy tim)",
            "Liều cao IV có thể gây co giật - không vượt quá 4g/ngày",
            "Không dùng quá 5 ngày liên tục (tăng nguy cơ huyết khối)",
            "Theo dõi sát dấu hiệu huyết khối",
            "Có thể dùng trong thai kỳ nếu cần thiết (category B)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "Ngay lập tức (IV), 1-2 giờ (PO)",
            "duration": "6-8 giờ",
            "protein_binding": "3%",
            "clearance": "Thận: bài tiết chủ yếu qua thận (90% nguyên dạng). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch IV: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
        "black_box_warnings": "Nguy cơ huyết khối nghiêm trọng, có thể gây tử vong. Không dùng ở bệnh nhân có huyết khối đang hoạt động hoặc tiền sử huyết khối. Theo dõi sát dấu hiệu huyết khối.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc chống đông (warfarin, heparin, DOACs)",
                    "mechanism": "Tác dụng đối kháng - tranexamic acid ức chế tiêu sợi huyết, làm tăng nguy cơ huyết khối",
                    "effect": "Tăng nguy cơ huyết khối nghiêm trọng",
                    "management": "Thận trọng. Thường tránh dùng cùng. Nếu cần thiết, theo dõi sát dấu hiệu huyết khối."
                },
                {
                    "drug": "Estrogen, Combined oral contraceptives",
                    "mechanism": "Cả hai đều tăng nguy cơ huyết khối",
                    "effect": "Tăng nguy cơ huyết khối nghiêm trọng",
                    "management": "Thận trọng. Thường tránh dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Factor IX concentrates",
                    "mechanism": "Tăng nguy cơ huyết khối",
                    "effect": "Tăng nguy cơ huyết khối",
                    "management": "Thận trọng. Theo dõi sát."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Huyết khối đang hoạt động",
                "Tiền sử huyết khối",
                "Dị ứng tranexamic acid"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng, giảm liều 75%",
                "Bệnh nhân có nguy cơ huyết khối (ung thư, bất động, suy tim) - thận trọng",
                "Liều cao IV - tăng nguy cơ co giật"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Huyết khối đang hoạt động",
                "Tiền sử huyết khối",
                "Dị ứng tranexamic acid"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng, giảm liều 75%",
                "Bệnh nhân có nguy cơ huyết khối (ung thư, bất động, suy tim) - thận trọng",
                "Liều cao IV - tăng nguy cơ co giật"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 75%",
            "dialysis": "Giảm liều 75%. Tranexamic acid được lọc sạch qua thẩm phân máu, bổ sung liều sau lọc.",
            "notes": "Tranexamic acid thải trừ chủ yếu qua thận (90% nguyên dạng). Suy thận cần điều chỉnh liều rõ ràng."
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần thiết. Tranexamic acid được sử dụng để điều trị chảy máu nặng trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Tranexamic acid bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Tranexamic acid không chuyển hóa ở gan. Suy gan không ảnh hưởng đến tranexamic acid."
        },
        "overdose_management": {
            "symptoms": [
                "Co giật (liều cao IV)",
                "Huyết khối (nguy cơ cao)",
                "Buồn nôn, nôn nặng",
                "Nhìn mờ"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng tranexamic acid ngay lập tức",
                "Điều trị co giật nếu có (benzodiazepines)",
                "Theo dõi dấu hiệu huyết khối",
                "Điều trị huyết khối nếu có",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Dấu hiệu huyết khối, co giật, thị lực"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Dùng 3-4 lần/ngày. Tối đa 4g/ngày. Không dùng quá 5 ngày liên tục."
            },
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W (10mg/ml)",
                "infusion_rate": "Tiêm IV trong 10 phút (loading), sau đó truyền chậm (maintenance)",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Loading: 1g IV trong 10 phút. Maintenance: 1g IV mỗi 8 giờ. Tối đa 4g/ngày. Điều chỉnh liều ở suy thận."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tranexamic acid",
                "UpToDate - Tranexamic acid: Drug information",
                "CRASH-2 Trial - Lancet (trauma bleeding)",
                "WHO Guidelines - Postpartum hemorrhage"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, large RCTs (CRASH-2, WOMAN trial)"
        }
    },
    
    "Vitamin K": {
        "group": "Hematology - Anticoagulant Reversal Agent / Vitamin",
        "vietnamese_name": "Vitamin K, Phytomenadione, Phytonadione",
        "administration": ["PO", "IV", "SC", "IM"],
        "indications": [
            "Đảo ngược warfarin (quá liều hoặc chảy máu)",
            "Thiếu vitamin K (thiếu máu, chảy máu)",
            "Dự phòng chảy máu ở trẻ sơ sinh",
            "Bệnh nhân kém hấp thu chất béo",
            "Đang dùng kháng sinh dài ngày"
        ],
        "contraindications": [
            "Dị ứng vitamin K",
            "Không dùng IV nhanh (có thể gây sốc phản vệ)"
        ],
        "dosage": {
            "adult_warfarin_reversal_minor": "1-2.5mg PO x 1 lần",
            "adult_warfarin_reversal_major": "5-10mg IV chậm",
            "adult_deficiency": "10mg SC/IM x 1 lần/ngày x 3 ngày",
            "pediatric_newborn": "0.5-1mg IM x 1 lần (dự phòng)",
            "notes": "IV phải tiêm chậm (không quá 1mg/phút). PO tác dụng chậm hơn (6-12 giờ)."
        },
        "side_effects": [
            "Phản ứng dị ứng (IV nhanh)",
            "Đỏ da tại chỗ tiêm (IV)",
            "Huyết khối (IV nhanh, hiếm)",
            "Tăng bilirubin (trẻ sơ sinh, liều cao)"
        ],
        "interactions": [
            "Warfarin: đảo ngược tác dụng",
            "Cholestyramine: giảm hấp thu vitamin K",
            "Antibiotics: có thể giảm vitamin K (do giảm vi khuẩn đường ruột)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Vitamin K là vitamin tan trong chất béo, cần thiết cho tổng hợp các yếu tố đông máu phụ thuộc vitamin K (II, VII, IX, X) và các protein chống đông (protein C, protein S). Vitamin K hoạt động như cofactor cho enzyme gamma-glutamyl carboxylase, tham gia vào quá trình carboxyl hóa các yếu tố đông máu. Warfarin ức chế vitamin K epoxide reductase, ngăn chặn tái chế vitamin K, dẫn đến giảm tổng hợp các yếu tố đông máu. Bổ sung vitamin K đảo ngược tác dụng của warfarin bằng cách cung cấp vitamin K để tổng hợp lại các yếu tố đông máu. Vitamin K có thể dùng đường uống (tác dụng chậm, 6-12 giờ), tiêm dưới da, tiêm bắp, hoặc tiêm tĩnh mạch (tác dụng nhanh hơn nhưng nguy hiểm hơn).",
        "monitoring": [
            "INR (sau 6-12 giờ với PO, sau 2-4 giờ với IV) - theo dõi đảo ngược warfarin",
            "Dấu hiệu chảy máu (xem có còn chảy máu sau đảo ngược)",
            "Dấu hiệu phản ứng dị ứng (đặc biệt với IV)",
            "Huyết áp, nhịp tim (với IV)",
            "Bilirubin (trẻ sơ sinh, liều cao)"
        ],
        "precautions": [
            "IV phải tiêm CHẬM (không quá 1mg/phút) - tiêm nhanh có thể gây sốc phản vệ",
            "PO tác dụng chậm hơn (6-12 giờ) - phù hợp cho đảo ngược nhẹ",
            "IV tác dụng nhanh hơn (2-4 giờ) - phù hợp cho chảy máu nặng",
            "Có thể cần FFP hoặc PCC nếu chảy máu nặng (vitamin K tác dụng chậm)",
            "Thận trọng với trẻ sơ sinh (liều cao có thể gây tăng bilirubin)",
            "Cần chất béo để hấp thu tốt (đường uống)",
            "Không dùng IV nhanh - nguy cơ sốc phản vệ"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (vitamin K1)",
            "onset": "2-4 giờ (IV), 6-12 giờ (PO)",
            "duration": "24-48 giờ",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan: chuyển hóa. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch IV: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
        "black_box_warnings": "Tiêm IV nhanh có thể gây sốc phản vệ và tử vong. Phải tiêm IV chậm (không quá 1mg/phút).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Vitamin K đảo ngược tác dụng warfarin",
                    "effect": "Giảm hiệu quả warfarin, giảm INR",
                    "management": "Dùng để đảo ngược warfarin khi quá liều hoặc chảy máu. Sau đó cần điều chỉnh lại liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Cholestyramine",
                    "mechanism": "Giảm hấp thu vitamin K",
                    "effect": "Giảm hiệu quả vitamin K",
                    "management": "Cách xa ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng vitamin K",
                "Tiêm IV nhanh - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Trẻ sơ sinh - thận trọng với liều cao (tăng bilirubin)"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng vitamin K",
                "Tiêm IV nhanh - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Trẻ sơ sinh - thận trọng với liều cao (tăng bilirubin)"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều",
            "dialysis": "Không cần chỉnh liều",
            "notes": "Vitamin K chủ yếu chuyển hóa ở gan, không cần điều chỉnh liều ở suy thận."
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần thiết. Vitamin K an toàn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Vitamin K bài tiết vào sữa mẹ. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng",
            "notes": "Vitamin K chuyển hóa ở gan. Suy gan nặng có thể ảnh hưởng đến chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng dị ứng (đặc biệt với IV)",
                "Huyết khối (IV nhanh, hiếm)",
                "Tăng bilirubin (trẻ sơ sinh, liều cao)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng vitamin K nếu có phản ứng",
                "Điều trị phản ứng dị ứng nếu có",
                "Theo dõi INR (có thể quá đảo ngược)",
                "Theo dõi bilirubin (trẻ sơ sinh)"
            ],
            "monitoring": "INR, dấu hiệu dị ứng, bilirubin (trẻ sơ sinh)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên dùng với thức ăn có chất béo để tăng hấp thu",
                "timing": "Dùng 1 lần. Tác dụng chậm (6-12 giờ). Phù hợp cho đảo ngược warfarin nhẹ."
            },
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W (1mg/ml)",
                "infusion_rate": "Tiêm IV CHẬM (không quá 1mg/phút)",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Tiêm IV chậm (không quá 1mg/phút). Theo dõi huyết áp, dấu hiệu dị ứng. Tác dụng nhanh (2-4 giờ). Phù hợp cho chảy máu nặng."
            },
            "sc_im": {
                "reconstitution": "Dùng trực tiếp từ lọ",
                "injection_site": "Tiêm dưới da hoặc tiêm bắp",
                "notes": "Tác dụng trung bình (4-6 giờ). Phù hợp cho thiếu vitamin K."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vitamin K (Phytonadione)",
                "UpToDate - Vitamin K: Drug information",
                "ACCP Guidelines - Warfarin reversal"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, widely used in clinical practice"
        }
    },
    
}

__all__ = ['HEMATOLOGY_DRUGS']

