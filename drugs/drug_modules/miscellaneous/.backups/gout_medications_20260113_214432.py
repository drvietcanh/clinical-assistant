"""Miscellaneous Drugs - Gout Medications
Colchicine, Probenecid, Febuxostat"""

GOUT_MEDICATIONS_DRUGS = {
    "Colchicine": {
        "group": "Metabolism - Gout Medication (Anti-inflammatory)",
        "vietnamese_name": "Colchicine",
        "administration": ["PO", "IV"],
        "indications": [
            "Gout cấp tính",
            "Dự phòng cơn gout cấp (khi bắt đầu allopurinol/febuxostat)",
            "Bệnh Behçet",
            "Viêm màng ngoài tim",
            "Sốt Địa Trung Hải gia đình (FMF)"
        ],
        "contraindications": [
            "Dị ứng colchicine",
            "Suy thận nặng (CrCl <30)",
            "Suy gan nặng",
            "Đang dùng strong CYP3A4 inhibitors hoặc P-gp inhibitors"
        ],
        "dosage": {
            "adult_gout_acute": "1.2mg x 1 lần, sau đó 0.6mg sau 1 giờ (tối đa 1.8mg trong 1 giờ đầu)",
            "adult_gout_prophylaxis": "0.6mg x 1-2 lần/ngày",
            "adult_iv": "1-2mg IV (hiếm dùng, chỉ khi không thể uống)",
            "pediatric": "Không khuyến nghị <18 tuổi",
            "notes": "Liều cao có thể gây độc tính nghiêm trọng. Không vượt quá 2.4mg/ngày."
        },
        "side_effects": [
            "Tiêu chảy, nôn (phổ biến, dấu hiệu độc tính)",
            "Độc tính tủy xương (giảm bạch cầu, giảm tiểu cầu)",
            "Độc tính cơ (yếu cơ, tiêu cơ vân)",
            "Độc tính thần kinh (tê, yếu)",
            "Độc tính gan",
            "Rụng tóc"
        ],
        "interactions": [
            "Strong CYP3A4 inhibitors (ketoconazole, clarithromycin): tăng độc tính nghiêm trọng",
            "P-gp inhibitors (cyclosporine): tăng độc tính",
            "Statins: tăng nguy cơ tiêu cơ vân",
            "Fibrates: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "D - Có bằng chứng về nguy cơ. Tránh trong thai kỳ""mechanism_of_action": "Colchicine là alkaloid có nguồn gốc từ cây colchicum, có tác dụng chống viêm mạnh trong gout cấp. Colchicine gắn với tubulin, ngăn chặn sự polymer hóa microtubule, ức chế sự di chuyển của bạch cầu đến vị trí viêm và ức chế thực bào các tinh thể urate. Colchicine cũng ức chế giải phóng các chất trung gian gây viêm từ bạch cầu. Colchicine không làm giảm nồng độ acid uric máu, chỉ có tác dụng chống viêm trong cơn gout cấp. Colchicine có phạm vi điều trị hẹp (narrow therapeutic window), dễ gây độc tính nếu quá liều.",
        "monitoring": [
            "Dấu hiệu độc tính: tiêu chảy, nôn (dấu hiệu sớm - NGỪNG NGAY)",
            "Công thức máu (CBC) - theo dõi giảm bạch cầu, giảm tiểu cầu",
            "CK (creatine kinase) - theo dõi tiêu cơ vân",
            "Chức năng gan (ALT, AST)",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều ở suy thận",
            "Dấu hiệu độc tính thần kinh (tê, yếu)"
        ],
        "precautions": [
            "PHẠM VI ĐIỀU TRỊ HẸP - dễ gây độc tính nếu quá liều",
            "NGỪNG NGAY nếu có tiêu chảy hoặc nôn - đây là dấu hiệu độc tính sớm",
            "Không vượt quá 2.4mg/ngày (nguy cơ độc tính cao)",
            "Điều chỉnh liều ở suy thận: CrCl 30-60 → giảm liều 50%, CrCl <30 → tránh dùng",
            "CHỐNG CHỈ ĐỊNH với strong CYP3A4 inhibitors (ketoconazole, clarithromycin, itraconazole) - tăng độc tính nghiêm trọng",
            "Thận trọng với statins và fibrates (tăng nguy cơ tiêu cơ vân)",
            "Không dùng trong thai kỳ (category D)",
            "Dùng để dự phòng cơn gout cấp khi bắt đầu allopurinol/febuxostat (1-2 tháng đầu)"
        ],
        "pharmacokinetics": {
            "half_life": "20-40 giờ",
            "onset": "12-24 giờ (gout cấp)",
            "duration": "24-48 giờ",
            "protein_binding": "30-50%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần. Cần điều chỉnh liều ở suy thận và suy gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Độc tính nghiêm trọng, có thể gây tử vong nếu quá liều. Phạm vi điều trị hẹp. Ngừng ngay nếu có tiêu chảy hoặc nôn. Chống chỉ định với strong CYP3A4 inhibitors và P-gp inhibitors. Điều chỉnh liều ở suy thận và suy gan.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, clarithromycin, itraconazole, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa colchicine, tăng nồng độ",
                    "effect": "Tăng độc tính nghiêm trọng, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng strong CYP3A4 inhibitors."
                },
                {
                    "drug": "P-gp inhibitors (cyclosporine, verapamil, diltiazem)",
                    "mechanism": "Ức chế P-gp, tăng hấp thu colchicine",
                    "effect": "Tăng độc tính",
                    "management": "CHỐNG CHỈ ĐỊNH hoặc giảm liều colchicine 50-75%."
                }
            ],
            "moderate": [
                {
                    "drug": "Statins (atorvastatin, simvastatin, lovastatin)",
                    "mechanism": "Cả hai đều có thể gây tiêu cơ vân",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Theo dõi CK. Cân nhắc tạm ngừng statin khi dùng colchicine."
                },
                {
                    "drug": "Fibrates (gemfibrozil, fenofibrate)",
                    "mechanism": "Cả hai đều có thể gây tiêu cơ vân",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Theo dõi CK."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng colchicine",
                "Suy thận nặng (CrCl <30)",
                "Suy gan nặng",
                "Đang dùng strong CYP3A4 inhibitors",
                "Đang dùng P-gp inhibitors mạnh",
                "Có thai (category D)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-60) - giảm liều 50%",
                "Suy gan nhẹ-trung bình - thận trọng",
                "Đang dùng statins hoặc fibrates - tăng nguy cơ tiêu cơ vân",
                "Người cao tuổi - tăng nguy cơ độc tính"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng colchicine",
                "Suy thận nặng (CrCl <30)",
                "Suy gan nặng",
                "Đang dùng strong CYP3A4 inhibitors",
                "Đang dùng P-gp inhibitors mạnh",
                "Có thai (category D)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-60) - giảm liều 50%",
                "Suy gan nhẹ-trung bình - thận trọng",
                "Đang dùng statins hoặc fibrates - tăng nguy cơ tiêu cơ vân",
                "Người cao tuổi - tăng nguy cơ độc tính"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, giảm liều 50%",
            "under_30": "CHỐNG CHỈ ĐỊNH hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "dialysis": "CHỐNG CHỈ ĐỊNH hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ. Colchicine không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Colchicine thải trừ một phần qua thận. Suy thận làm tăng nguy cơ tích lũy và độc tính nghiêm trọng. Phạm vi điều trị hẹp, cần điều chỉnh liều chặt chẽ ở suy thận."
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Colchicine có thể gây dị tật thai nhi. Chỉ dùng trong trường hợp đe dọa tính mạng nếu không có lựa chọn thay thế.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Colchicine bài tiết vào sữa mẹ. Không nên dùng khi cho con bú.",
                "recommendation": "KHÔNG dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Colchicine chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy, nôn (dấu hiệu sớm)",
                "Độc tính tủy xương (giảm bạch cầu, giảm tiểu cầu)",
                "Tiêu cơ vân (yếu cơ, tăng CK)",
                "Độc tính thần kinh (tê, yếu)",
                "Suy đa tạng",
                "Tử vong (nếu quá liều nặng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng colchicine ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi công thức máu, CK, chức năng gan, thận",
                "Điều trị hỗ trợ: truyền dịch, hỗ trợ hô hấp nếu cần",
                "Theo dõi tại ICU nếu độc tính nặng",
                "Theo dõi ít nhất 7 ngày (do half-life dài 20-40 giờ)"
            ],
            "monitoring": "Công thức máu, CK, chức năng gan, thận, dấu hiệu sống, dấu hiệu độc tính thần kinh"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Gout cấp: 1.2mg x 1 lần, sau đó 0.6mg sau 1 giờ (tối đa 1.8mg trong 1 giờ đầu). Dự phòng: 0.6mg x 1-2 lần/ngày. KHÔNG vượt quá 2.4mg/ngày."
            },
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W",
                "infusion_rate": "Tiêm IV chậm (1-2mg trong 10-20 phút)",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Hiếm dùng IV, chỉ khi không thể uống. Thận trọng với độc tính."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Colchicine",
                "American College of Rheumatology Guidelines - Gout Management",
                "UpToDate - Colchicine: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, ACR guidelines"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "hematologic": "Bone marrow suppression (leukopenia, thrombocytopenia) - CRITICAL",
                "muscular": "Rhabdomyolysis (muscle weakness, elevated CK) - CRITICAL",
                "neurological": "Neurotoxicity (numbness, weakness) - CRITICAL",
                "hepatic": "Hepatotoxicity",
                "gastrointestinal": "Diarrhea, vomiting (early signs of toxicity - STOP IMMEDIATELY)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - Diarrhea, vomiting (early signs of toxicity - STOP IMMEDIATELY) - CRITICAL",
                "Black Box Warning - CBC (leukopenia, thrombocytopenia - bone marrow suppression) - CRITICAL",
                "Black Box Warning - CK (creatine kinase - rhabdomyolysis risk) - CRITICAL",
                "Black Box Warning - Neurological symptoms (numbness, weakness) - CRITICAL",
                "Black Box Warning - Strong CYP3A4 inhibitors interaction (ketoconazole, clarithromycin - CONTRAINDICATED) - CRITICAL",
                "Black Box Warning - P-gp inhibitors interaction (cyclosporine - CONTRAINDICATED) - CRITICAL",
                "Renal function (creatinine, eGFR - dose adjustment required, contraindicated if CrCl <30)",
                "Hepatic function (ALT, AST)",
                "Statins/fibrates interaction (increased rhabdomyolysis risk)"
            ],
            "look_alike_sound_alike": ["Colchicine", "Colchicum"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Severe Toxicity (can be fatal if overdose)",
            "FDA Black Box Warning - Narrow Therapeutic Window",
            "FDA Black Box Warning - Strong CYP3A4 Inhibitors Interaction (contraindicated)",
            "FDA Black Box Warning - P-gp Inhibitors Interaction (contraindicated)",
            "ACR Guidelines - Gout Management",
            "EULAR Guidelines - Gout Management",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    
    "Febuxostat": {
        "group": "Metabolism - Gout Medication (Xanthine Oxidase Inhibitor)",
        "vietnamese_name": "Febuxostat, Uloric",
        "administration": ["PO"],
        "indications": [
            "Gout mạn tính",
            "Tăng acid uric máu",
            "Phòng ngừa sỏi thận uric acid",
            "Hóa trị (phòng ngừa tăng acid uric)"
        ],
        "contraindications": [
            "Dị ứng febuxostat",
            "Đang dùng azathioprine hoặc 6-mercaptopurine",
            "Có thai"
        ],
        "dosage": {
            "adult_standard": "40mg x 1 lần/ngày",
            "adult_severe": "80mg x 1 lần/ngày",
            "notes": "Khởi đầu với 40mg/ngày. Tăng lên 80mg/ngày nếu acid uric >6 mg/dL sau 2 tuần. Dùng kèm colchicine khi bắt đầu để tránh cơn gout cấp."
        },
        "side_effects": [
            "Tăng men gan (phổ biến)",
            "Buồn nôn",
            "Đau khớp",
            "Phát ban",
            "Tăng nguy cơ tim mạch (so với allopurinol)",
            "Ban da (hiếm, có thể SJS/TEN)"
        ],
        "interactions": [
            "Azathioprine/6-mercaptopurine: tăng độc tính (chống chỉ định)",
            "Theophylline: tăng nồng độ theophylline"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Febuxostat là xanthine oxidase inhibitor không purine, ức chế enzyme xanthine oxidase (cả dạng oxy hóa và khử), ngăn chặn sự chuyển đổi hypoxanthine thành xanthine và xanthine thành acid uric. Khác với allopurinol (purine analog), febuxostat không phải purine analog nên ít tương tác với các enzyme khác. Febuxostat có hiệu quả mạnh hơn allopurinol trong việc giảm acid uric máu và có thể dùng ở bệnh nhân suy thận mà không cần điều chỉnh liều. Tuy nhiên, febuxostat có thể tăng nguy cơ tim mạch so với allopurinol.",
        "monitoring": [
            "Nồng độ acid uric máu (mục tiêu <6 mg/dL)",
            "Chức năng gan (ALT, AST) - tăng men gan phổ biến",
            "Dấu hiệu tim mạch (đau ngực, khó thở) - tăng nguy cơ so với allopurinol",
            "Dấu hiệu ban da (hiếm, có thể SJS/TEN)",
            "Triệu chứng gout cấp (có thể xảy ra khi bắt đầu - cần dùng colchicine dự phòng)"
        ],
        "precautions": [
            "Tăng nguy cơ tim mạch so với allopurinol - cân nhắc dùng allopurinol nếu có bệnh tim mạch",
            "Khởi đầu với 40mg/ngày, tăng lên 80mg/ngày nếu cần",
            "Dùng kèm colchicine hoặc NSAID khi bắt đầu để dự phòng cơn gout cấp (1-2 tháng đầu)",
            "CHỐNG CHỈ ĐỊNH với azathioprine/6-mercaptopurine (tăng độc tính)",
            "Theo dõi chức năng gan (tăng men gan phổ biến)",
            "Không cần điều chỉnh liều ở suy thận (khác với allopurinol)",
            "Thận trọng ở bệnh nhân có bệnh tim mạch"
        ],
        "pharmacokinetics": {
            "half_life": "5-8 giờ",
            "onset": "1-2 tuần (giảm acid uric máu)",
            "duration": "24 giờ",
            "protein_binding": "99%",
            "clearance": "Gan: chuyển hóa qua UGT (uridine diphosphate glucuronosyltransferase). Thận: bài tiết một phần. Không cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Tăng nguy cơ tử vong do tim mạch so với allopurinol. Cân nhắc dùng allopurinol nếu có bệnh tim mạch. Chống chỉ định với azathioprine và 6-mercaptopurine.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Azathioprine, 6-Mercaptopurine",
                    "mechanism": "Febuxostat ức chế xanthine oxidase, enzyme chuyển hóa azathioprine và 6-mercaptopurine",
                    "effect": "Tăng nồng độ azathioprine/6-mercaptopurine, tăng độc tính nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng azathioprine hoặc 6-mercaptopurine."
                }
            ],
            "moderate": [
                {
                    "drug": "Theophylline",
                    "mechanism": "Febuxostat có thể ức chế chuyển hóa theophylline",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính",
                    "management": "Thận trọng. Theo dõi nồng độ theophylline và điều chỉnh liều nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng febuxostat",
                "Đang dùng azathioprine hoặc 6-mercaptopurine",
                "Có thai (category C)"
            ],
            "tương_đối": [
                "Bệnh tim mạch - cân nhắc dùng allopurinol thay vì febuxostat",
                "Suy gan nặng - thận trọng"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng febuxostat",
                "Đang dùng azathioprine hoặc 6-mercaptopurine",
                "Có thai (category C)"
            ],
            "tương_đối": [
                "Bệnh tim mạch - cân nhắc dùng allopurinol thay vì febuxostat",
                "Suy gan nặng - thận trọng"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều (khác với allopurinol)",
            "under_30": "Không cần chỉnh liều (khác với allopurinol)",
            "dialysis": "Không cần chỉnh liều. Febuxostat không được lọc sạch hiệu quả qua thẩm phân máu nhưng không cần điều chỉnh liều.",
            "notes": "Febuxostat chuyển hóa chủ yếu qua gan (UGT), không cần điều chỉnh liều ở suy thận (khác với allopurinol)."
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Không có dữ liệu đầy đủ về an toàn trong thai kỳ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không rõ febuxostat có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng.",
                "recommendation": "Thận trọng khi dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Febuxostat chuyển hóa ở gan qua UGT. Suy gan có thể ảnh hưởng đến chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng men gan",
                "Buồn nôn, nôn",
                "Phát ban",
                "Tăng nguy cơ tim mạch"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng febuxostat",
                "Theo dõi chức năng gan",
                "Theo dõi dấu hiệu tim mạch",
                "Điều trị hỗ trợ"
            ],
            "monitoring": "Chức năng gan, dấu hiệu tim mạch, dấu hiệu ban da"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày. Khởi đầu: 40mg/ngày. Tăng lên 80mg/ngày nếu acid uric >6 mg/dL sau 2 tuần. Dùng kèm colchicine khi bắt đầu để dự phòng cơn gout cấp."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Uloric (febuxostat)",
                "American College of Rheumatology Guidelines - Gout Management",
                "CARES Trial - New England Journal of Medicine",
                "UpToDate - Febuxostat: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, large RCT (CARES trial), ACR guidelines"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"cardiovascular": "Black Box Warning - Increased cardiovascular death risk vs allopurinol", "hepatic": "Hepatotoxicity (common elevation)", "dermatologic": "Severe cutaneous adverse reactions (SJS/TEN - rare)"},
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Cardiovascular symptoms (chest pain, dyspnea - increased risk vs allopurinol)", "Serum uric acid (target <6 mg/dL)", "Hepatic function (ALT, AST - common elevation)", "Skin reactions (SJS/TEN risk - rare)", "Acute gout attacks (may occur at initiation - use colchicine prophylaxis)", "Azathioprine/6-mercaptopurine interaction (contraindicated - severe myelosuppression)"],
            "look_alike_sound_alike": ["Febuxostat", "Allopurinol"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Cardiovascular Death Risk (vs allopurinol)",
            "FDA Black Box Warning - Azathioprine/6-Mercaptopurine Interaction (contraindicated)",
            "ACR Guidelines - Gout Management",
            "EULAR Guidelines - Gout Management",
            "CARES Trial - Cardiovascular Risk",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    "Probenecid": {
        "group": "Metabolism - Gout Medication (Uricosuric Agent)",
        "vietnamese_name": "Probenecid",
        "administration": ["PO"],
        "indications": [
            "Gout mạn tính (tăng bài tiết acid uric)",
            "Tăng acid uric máu",
            "Tăng nồng độ penicillin/cephalosporin (dùng kèm để tăng nồng độ kháng sinh)"
        ],
        "contraindications": [
            "Dị ứng probenecid",
            "Sỏi thận uric acid",
            "Suy thận nặng (CrCl <30)",
            "Đang dùng salicylates liều cao"
        ],
        "dosage": {
            "adult_standard": "250mg x 2 lần/ngày x 1 tuần, sau đó 500mg x 2 lần/ngày",
            "adult_max": "2g/ngày",
            "notes": "Uống với nhiều nước (2-3L/ngày) để tránh sỏi thận. Khởi đầu với liều thấp."
        },
        "side_effects": [
            "Sỏi thận uric acid (nếu không uống đủ nước)",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Phát ban",
            "Tăng men gan"
        ],
        "interactions": [
            "Penicillin/Cephalosporin: tăng nồng độ kháng sinh",
            "Salicylates liều cao: giảm hiệu quả probenecid",
            "Methotrexate: tăng nồng độ methotrexate",
            "NSAIDs: tăng nồng độ NSAIDs"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Probenecid là uricosuric agent, ức chế tái hấp thu acid uric ở ống thận gần, làm tăng bài tiết acid uric qua nước tiểu và giảm nồng độ acid uric trong máu. Probenecid cũng ức chế bài tiết các acid hữu cơ khác ở ống thận, bao gồm penicillin và cephalosporin, làm tăng nồng độ các kháng sinh này trong máu. Probenecid được sử dụng để điều trị gout mạn tính bằng cách tăng bài tiết acid uric, nhưng cần uống nhiều nước để tránh sỏi thận uric acid. Probenecid cũng được dùng để tăng nồng độ penicillin/cephalosporin khi cần thiết.",
        "monitoring": [
            "Nồng độ acid uric máu (mục tiêu <6 mg/dL)",
            "Chức năng thận (creatinine, eGFR)",
            "Dấu hiệu sỏi thận (đau lưng, đau bụng, tiểu máu)",
            "Nồng độ penicillin/cephalosporin nếu dùng kèm",
            "Chức năng gan (ALT, AST)"
        ],
        "precautions": [
            "UỐNG NHIỀU NƯỚC (2-3L/ngày) để tránh sỏi thận uric acid",
            "Khởi đầu với liều thấp (250mg x 2 lần/ngày) để tránh cơn gout cấp",
            "Không dùng nếu có sỏi thận uric acid",
            "Thận trọng ở suy thận (CrCl <30 - chống chỉ định)",
            "Tránh dùng với salicylates liều cao (giảm hiệu quả)",
            "Có thể tăng nồng độ penicillin/cephalosporin - thận trọng với độc tính",
            "Có thể tăng nồng độ methotrexate - thận trọng"
        ],
        "pharmacokinetics": {
            "half_life": "4-12 giờ",
            "onset": "Vài ngày đến vài tuần",
            "duration": "12 giờ",
            "protein_binding": "85-95%",
            "clearance": "Thận: bài tiết qua nước tiểu. Gan: chuyển hóa một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Methotrexate",
                    "mechanism": "Probenecid ức chế bài tiết methotrexate ở ống thận, tăng nồng độ",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính",
                    "management": "Thận trọng. Giảm liều methotrexate hoặc tránh dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Penicillin, Cephalosporin",
                    "mechanism": "Probenecid ức chế bài tiết kháng sinh ở ống thận, tăng nồng độ",
                    "effect": "Tăng nồng độ kháng sinh, có thể tăng độc tính",
                    "management": "Thận trọng. Có thể dùng để tăng nồng độ kháng sinh nếu cần, nhưng theo dõi độc tính."
                },
                {
                    "drug": "Salicylates liều cao (>3g/ngày)",
                    "mechanism": "Salicylates ức chế tác dụng uricosuric của probenecid",
                    "effect": "Giảm hiệu quả probenecid",
                    "management": "Tránh dùng salicylates liều cao khi dùng probenecid."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng probenecid",
                "Sỏi thận uric acid",
                "Suy thận nặng (CrCl <30)"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-60) - thận trọng",
                "Đang dùng methotrexate - tăng nồng độ",
                "Đang dùng salicylates liều cao - giảm hiệu quả"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần thiết. Không có bằng chứng về dị tật thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Probenecid bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Probenecid chuyển hóa một phần ở gan. Suy gan có thể ảnh hưởng đến chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau đầu",
                "Sỏi thận uric acid",
                "Phát ban"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng probenecid",
                "Uống nhiều nước để tăng bài tiết",
                "Điều trị sỏi thận nếu có",
                "Điều trị hỗ trợ"
            ],
            "monitoring": "Chức năng thận, dấu hiệu sỏi thận"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Khởi đầu: 250mg x 2 lần/ngày x 1 tuần. Sau đó: 500mg x 2 lần/ngày. UỐNG NHIỀU NƯỚC (2-3L/ngày) để tránh sỏi thận."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Probenecid",
                "American College of Rheumatology Guidelines - Gout Management",
                "UpToDate - Probenecid: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, ACR guidelines"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"renal": "Uric acid kidney stones (if inadequate hydration - critical)", "hepatic": "Hepatotoxicity (rare)"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["Serum uric acid (target <6 mg/dL)", "Renal function (creatinine, eGFR - contraindicated if CrCl <30)", "Kidney stones signs (back pain, abdominal pain, hematuria - critical, maintain adequate hydration 2-3L/day)", "Penicillin/cephalosporin levels (if co-administered - increases levels)", "Methotrexate levels (if co-administered - increases levels)", "Hepatic function (ALT, AST - hepatotoxicity risk)"],
            "look_alike_sound_alike": ["Probenecid", "Probenecid"]
        },
        "guideline_tags": [
            "ACR Guidelines - Gout Management",
            "EULAR Guidelines - Gout Management",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "black_box_warnings": None,
},
    
}

__all__ = ['GOUT_MEDICATIONS_DRUGS']

























