"""Immunosuppressant Medications - Used in organ transplantation and autoimmune diseases"""

IMMUNOSUPPRESSANTS_DRUGS = {
    "Azathioprine": {
        "group": "Immunosuppressant - Antimetabolite",
        "vietnamese_name": "Azathioprine, Imuran",
        "administration": ["PO", "IV"],
        "indications": [
            "Ghép tạng (thận, gan, tim) - phòng ngừa thải ghép",
            "Bệnh tự miễn (lupus ban đỏ hệ thống, viêm khớp dạng thấp, viêm đa cơ)",
            "Bệnh thận IgA",
            "Hội chứng thận hư",
            "Bệnh viêm ruột (Crohn, viêm loét đại tràng)"
        ],
        "contraindications": [
            "Dị ứng azathioprine",
            "Thiếu hụt TPMT (thiopurine methyltransferase) nặng",
            "Có thai (thận trọng)",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_transplant_po": "1-3mg/kg/ngày chia 1-2 lần",
            "adult_transplant_iv": "1-3mg/kg/ngày",
            "adult_autoimmune": "1-2.5mg/kg/ngày chia 1-2 lần",
            "adult_ibd": "2-2.5mg/kg/ngày chia 1-2 lần",
            "notes": "Điều chỉnh liều theo đáp ứng và tác dụng phụ. Test TPMT trước khi dùng nếu có thể."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, theo dõi sát"
        },
        "side_effects": [
            "Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến, đặc biệt nếu thiếu TPMT)",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Tăng nguy cơ nhiễm trùng",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da, ung thư máu)",
            "Độc gan (tăng men gan, viêm gan)",
            "Viêm tụy (hiếm)",
            "Dị ứng (phát ban, sốt)"
        ],
        "interactions": [
            "Allopurinol: tăng độc tính azathioprine (chống chỉ định hoặc giảm liều azathioprine 75%)",
            "Warfarin: giảm tác dụng warfarin",
            "ACE inhibitor: tăng nguy cơ giảm bạch cầu"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Azathioprine là prodrug, được chuyển hóa thành 6-mercaptopurine (6-MP), chất hoạt động. 6-MP được chuyển hóa thành các nucleotide thiopurine (6-thioguanine nucleotides, 6-TGN), tích hợp vào DNA và RNA, gây tổn thương DNA và ức chế tổng hợp DNA/RNA. Dẫn đến: ức chế sự phát triển và phân chia tế bào, đặc biệt tế bào lympho B và T. Ức chế miễn dịch qua trung gian tế bào lympho, giảm đáp ứng miễn dịch với kháng nguyên lạ (ghép tạng), và giảm đáp ứng tự miễn. Azathioprine được dùng để phòng ngừa thải ghép tạng và điều trị các bệnh tự miễn. Chuyển hóa phụ thuộc enzyme TPMT (thiopurine methyltransferase). Thiếu hụt TPMT → tích lũy 6-TGN → tăng độc tính (giảm bạch cầu nặng).",
        "monitoring": [
            "Công thức máu (WBC, platelet, hemoglobin) - giảm bạch cầu, giảm tiểu cầu, thiếu máu - QUAN TRỌNG, đặc biệt trong 3 tháng đầu",
            "Test TPMT trước khi dùng nếu có thể (thiếu hụt TPMT → tăng độc tính)",
            "Chức năng gan (ALT, AST, bilirubin) - độc gan",
            "Dấu hiệu nhiễm trùng - tăng nguy cơ nhiễm trùng",
            "Dấu hiệu ung thư (lymphoma, ung thư da, ung thư máu) - tăng nguy cơ",
            "Dấu hiệu viêm tụy (đau bụng, tăng amylase) - hiếm",
            "Dấu hiệu dị ứng (phát ban, sốt)",
            "Tương tác với allopurinol (tăng độc tính - chống chỉ định hoặc giảm liều azathioprine 75%)"
        ],
        "precautions": [
            "Test TPMT trước khi dùng nếu có thể (thiếu hụt TPMT → tăng độc tính, giảm bạch cầu nặng)",
            "Giảm bạch cầu, giảm tiểu cầu phổ biến - theo dõi công thức máu mỗi 1-4 tuần, đặc biệt trong 3 tháng đầu",
            "CHỐNG CHỈ ĐỊNH hoặc giảm liều azathioprine 75% nếu dùng với allopurinol (tăng độc tính nghiêm trọng)",
            "Tăng nguy cơ nhiễm trùng - cần phòng ngừa nhiễm trùng",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da, ung thư máu) - cần theo dõi",
            "Độc gan - theo dõi chức năng gan định kỳ",
            "Viêm tụy hiếm - ngừng ngay nếu có dấu hiệu",
            "Dị ứng - ngừng ngay nếu có phát ban, sốt",
            "Thận trọng trong thai kỳ (category D) - có thể gây dị tật bẩm sinh",
            "Điều chỉnh liều ở suy thận (giảm liều 25-75%)"
        ],
        "pharmacokinetics": {
            "half_life": "3-5 giờ (azathioprine), 1-2 giờ (6-MP)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "30%",
            "metabolism": "Gan: azathioprine chuyển hóa thành 6-MP (chất hoạt động). 6-MP chuyển hóa qua TPMT và xanthine oxidase thành các metabolites. Thiếu hụt TPMT → tích lũy 6-TGN → tăng độc tính.",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Chuyển hóa phụ thuộc TPMT và xanthine oxidase."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Giảm bạch cầu, giảm tiểu cầu phổ biến, đặc biệt nếu thiếu hụt TPMT. CHỐNG CHỈ ĐỊNH hoặc giảm liều azathioprine 75% nếu dùng với allopurinol (tăng độc tính nghiêm trọng). Tăng nguy cơ nhiễm trùng và ung thư (lymphoma, ung thư da, ung thư máu). Test TPMT trước khi dùng nếu có thể.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Allopurinol ức chế xanthine oxidase, làm giảm chuyển hóa 6-MP, tăng tích lũy 6-TGN, tăng độc tính azathioprine",
                    "effect": "Tăng độc tính azathioprine nghiêm trọng, tăng nguy cơ giảm bạch cầu nặng, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng hoặc giảm liều azathioprine 75% nếu phải dùng cùng. Theo dõi công thức máu chặt chẽ."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Azathioprine có thể cảm ứng enzyme chuyển hóa warfarin",
                    "effect": "Giảm tác dụng warfarin, giảm INR, tăng nguy cơ huyết khối",
                    "management": "Theo dõi INR chặt chẽ. Có thể cần tăng liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "ACE inhibitors (captopril, enalapril, lisinopril)",
                    "mechanism": "Cả hai đều có thể gây giảm bạch cầu, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ giảm bạch cầu nặng",
                    "management": "Thận trọng. Theo dõi công thức máu chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng azathioprine",
                "Thiếu hụt TPMT nặng - CHỐNG CHỈ ĐỊNH (tăng độc tính nghiêm trọng)",
                "Dùng với allopurinol - CHỐNG CHỈ ĐỊNH hoặc giảm liều azathioprine 75%"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều 50-75%",
                "Suy gan nặng - thận trọng, giảm liều",
                "Giảm bạch cầu, giảm tiểu cầu nặng - có thể cần ngừng",
                "Có thai (category D) - thận trọng, có thể gây dị tật bẩm sinh",
                "Dùng với ACE inhibitor - tăng nguy cơ giảm bạch cầu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Azathioprine là FDA category D. Có thể gây dị tật bẩm sinh, nhưng có thể dùng trong thai kỳ khi cần thiết (ghép tạng, bệnh tự miễn nặng). Cần theo dõi chặt chẽ. Dùng liều thấp nhất hiệu quả.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Azathioprine bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ",
            "severe": "Thận trọng, giảm liều. Azathioprine chuyển hóa ở gan, suy gan có thể tăng độc tính.",
            "notes": "Azathioprine chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa, tăng độc tính. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu, giảm tiểu cầu nặng (myelosuppression)",
                "Nhiễm trùng nặng (do giảm bạch cầu)",
                "Chảy máu (do giảm tiểu cầu)",
                "Độc gan nặng (tăng men gan, vàng da)",
                "Viêm tụy"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng azathioprine",
                "Theo dõi công thức máu chặt chẽ",
                "Điều trị giảm bạch cầu: G-CSF nếu cần",
                "Điều trị giảm tiểu cầu: truyền tiểu cầu nếu cần",
                "Điều trị nhiễm trùng: kháng sinh nếu có",
                "Điều trị độc gan: hỗ trợ gan",
                "Điều trị viêm tụy: hỗ trợ, nhịn ăn nếu cần",
                "Theo dõi dấu hiệu nhiễm trùng, chảy máu, độc gan chặt chẽ"
            ],
            "monitoring": "Công thức máu, chức năng gan, dấu hiệu nhiễm trùng, dấu hiệu chảy máu trong ít nhất 1-2 tuần."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Chia 1-2 lần/ngày. Uống cùng thời điểm mỗi ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha đậm đặc: 10mg/ml, sau đó pha loãng để truyền.",
                "infusion_rate": "Truyền trong 30-60 phút. Không truyền nhanh.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Azathioprine (Imuran)",
                "UpToDate - Azathioprine: Drug information",
                "Lexicomp - Azathioprine monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used in transplantation and autoimmune diseases"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Bone marrow suppression (myelosuppression) - common", "Hepatotoxicity", "Pancreatitis (rare)", "Malignancy (lymphoma, skin cancer, blood cancer)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (WBC, platelet, hemoglobin) - CRITICAL, especially first 3 months", "TPMT testing before treatment if possible", "Hepatic function (ALT, AST, bilirubin)", "Signs of infection", "Signs of malignancy"]
        },
        "guideline_tags": [
            "AST Guidelines - Organ Transplantation",
            "ACR Guidelines - Autoimmune Diseases",
            "FDA Black Box Warning - Azathioprine and Myelosuppression",
            "FDA Black Box Warning - Azathioprine and Allopurinol Interaction",
            "ECCO Guidelines - Inflammatory Bowel Disease"
        ]
    },
    "Cyclosporine": {
        "group": "Immunosuppressant - Calcineurin Inhibitor",
        "vietnamese_name": "Cyclosporine, Cyclosporin A, Sandimmune, Neoral",
        "administration": ["PO", "IV"],
        "indications": [
            "Ghép tạng (thận, gan, tim, phổi)",
            "Bệnh tự miễn (viêm khớp dạng thấp, vảy nến, viêm da cơ địa)",
            "Bệnh thận IgA",
            "Hội chứng thận hư"
        ],
        "contraindications": [
            "Dị ứng cyclosporine",
            "Ung thư (trừ một số trường hợp)",
            "Nhiễm trùng nặng chưa điều trị",
            "Tăng huyết áp không kiểm soát",
            "Suy thận nặng (trừ ghép thận)"
        ],
        "dosage": {
            "adult_transplant_po": "5-15mg/kg/ngày chia 2 lần (tùy loại ghép)",
            "adult_transplant_iv": "3-5mg/kg/ngày truyền liên tục",
            "adult_autoimmune": "2.5-5mg/kg/ngày chia 2 lần",
            "adult_ra": "2.5-4mg/kg/ngày chia 2 lần",
            "notes": "Điều chỉnh liều theo nồng độ trong máu (trough level). Mục tiêu: 100-200 ng/mL (tùy chỉ định)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, theo dõi sát"
        },
        "side_effects": [
            "Độc thận (phổ biến, có thể vĩnh viễn)",
            "Tăng huyết áp",
            "Tăng cholesterol, triglyceride",
            "Rậm lông (hirsutism)",
            "Phì đại nướu (gingival hyperplasia)",
            "Run tay",
            "Đau đầu",
            "Buồn nôn, nôn",
            "Tăng nguy cơ nhiễm trùng",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
            "Độc gan (hiếm)"
        ],
        "interactions": [
            "Nhiều thuốc: ức chế hoặc cảm ứng CYP3A4",
            "Ketoconazole, Itraconazole: tăng nồng độ cyclosporine",
            "Rifampin, Phenytoin: giảm nồng độ cyclosporine",
            "NSAID: tăng độc thận",
            "Digoxin: tăng nồng độ digoxin",
            "Statins: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Cyclosporine là calcineurin inhibitor, ức chế calcineurin (một phosphatase phụ thuộc calci). Calcineurin kích hoạt nuclear factor of activated T-cells (NFAT), dẫn đến sản xuất interleukin-2 (IL-2) và các cytokine khác. Cyclosporine ức chế calcineurin, ngăn chặn kích hoạt NFAT, giảm sản xuất IL-2, và ức chế hoạt hóa tế bào T. Dẫn đến: ức chế miễn dịch qua trung gian tế bào T, giảm đáp ứng miễn dịch với kháng nguyên lạ (ghép tạng), và giảm đáp ứng tự miễn. Cyclosporine được dùng để phòng ngừa thải ghép tạng và điều trị các bệnh tự miễn. Cần theo dõi nồng độ trong máu (therapeutic drug monitoring, TDM) để đảm bảo hiệu quả và giảm độc tính.",
        "monitoring": [
            "Nồng độ cyclosporine trong máu (trough level, pre-dose) - QUAN TRỌNG: mục tiêu 100-200 ng/mL (tùy chỉ định và thời gian sau ghép)",
            "Chức năng thận (creatinine, eGFR) - độc thận phổ biến, có thể vĩnh viễn",
            "Huyết áp - tăng huyết áp phổ biến",
            "Lipid máu (cholesterol, triglyceride) - tăng lipid",
            "Chức năng gan (ALT, AST, bilirubin) - độc gan hiếm",
            "Công thức máu (CBC) - giảm bạch cầu, tiểu cầu (hiếm)",
            "Dấu hiệu nhiễm trùng - tăng nguy cơ nhiễm trùng",
            "Dấu hiệu ung thư (lymphoma, ung thư da) - tăng nguy cơ",
            "Tương tác với nhiều thuốc (CYP3A4 inhibitors/inducers)"
        ],
        "precautions": [
            "Độc thận phổ biến và có thể vĩnh viễn - theo dõi chức năng thận chặt chẽ",
            "Tăng huyết áp phổ biến - cần điều trị tăng huyết áp",
            "Tăng lipid máu - có thể cần statin (thận trọng với nguy cơ tiêu cơ vân)",
            "NHIỀU TƯƠNG TÁC THUỐC - kiểm tra tất cả thuốc đang dùng",
            "Theo dõi nồng độ trong máu (TDM) - điều chỉnh liều theo nồng độ",
            "Tránh dùng với NSAID (tăng độc thận)",
            "Tránh dùng với CYP3A4 inducers (rifampin, phenytoin) - giảm nồng độ",
            "Thận trọng với CYP3A4 inhibitors (ketoconazole, itraconazole) - tăng nồng độ",
            "Tăng nguy cơ nhiễm trùng - cần phòng ngừa nhiễm trùng",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da) - cần theo dõi",
            "Rậm lông, phì đại nướu - tác dụng phụ thẩm mỹ",
            "Uống với thức ăn để giảm buồn nôn"
        ],
        "pharmacokinetics": {
            "half_life": "19 giờ (dao động 10-27 giờ)",
            "onset": "Vài giờ đến vài ngày",
            "duration": "12-24 giờ (dùng 2 lần/ngày)",
            "protein_binding": "90-98%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa thành nhiều metabolites",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Chuyển hóa phụ thuộc CYP3A4, nhiều tương tác thuốc."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng lỏng: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi dùng. Không đông lạnh.",
        "black_box_warnings": "Độc thận có thể vĩnh viễn, đặc biệt với liều cao hoặc dùng kéo dài. Tăng nguy cơ nhiễm trùng và ung thư (lymphoma, ung thư da). Tăng huyết áp phổ biến. Nhiều tương tác thuốc nghiêm trọng. Cần theo dõi nồng độ trong máu (TDM) và chức năng thận chặt chẽ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, voriconazole, ritonavir, clarithromycin, erythromycin)",
                    "mechanism": "Ức chế chuyển hóa cyclosporine qua CYP3A4, tăng nồng độ cyclosporine",
                    "effect": "Tăng nồng độ cyclosporine, tăng độc tính (độc thận, tăng huyết áp)",
                    "management": "Giảm liều cyclosporine 50-75%. Theo dõi nồng độ cyclosporine và chức năng thận chặt chẽ."
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin, carbamazepine, phenobarbital)",
                    "mechanism": "Cảm ứng chuyển hóa cyclosporine qua CYP3A4, giảm nồng độ cyclosporine",
                    "effect": "Giảm nồng độ cyclosporine, giảm hiệu quả, tăng nguy cơ thải ghép",
                    "management": "Tăng liều cyclosporine 2-3 lần. Theo dõi nồng độ cyclosporine chặt chẽ. Cân nhắc thuốc thay thế."
                },
                {
                    "drug": "NSAID (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Cả hai đều có thể gây độc thận, tác dụng cộng dồn",
                    "effect": "Tăng độc thận, tăng nguy cơ suy thận cấp",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, theo dõi chức năng thận chặt chẽ."
                },
                {
                    "drug": "Statins (atorvastatin, simvastatin, lovastatin)",
                    "mechanism": "Cyclosporine ức chế chuyển hóa statin qua CYP3A4, tăng nồng độ statin",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân (rhabdomyolysis)",
                    "management": "Giảm liều statin hoặc dùng statin không phụ thuộc CYP3A4 (pravastatin, rosuvastatin). Theo dõi CK, dấu hiệu tiêu cơ vân."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Cyclosporine ức chế P-glycoprotein, tăng hấp thu digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng độc tính digoxin",
                    "management": "Giảm liều digoxin 25-50%. Theo dõi nồng độ digoxin và dấu hiệu độc tính."
                },
                {
                    "drug": "Potassium-sparing diuretics (spironolactone, amiloride)",
                    "mechanism": "Cả hai đều có thể gây tăng kali máu",
                    "effect": "Tăng nguy cơ tăng kali máu",
                    "management": "Theo dõi kali máu. Tránh dùng đồng thời nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cyclosporine",
                "Ung thư (trừ một số trường hợp đặc biệt)",
                "Nhiễm trùng nặng chưa điều trị",
                "Tăng huyết áp không kiểm soát",
                "Suy thận nặng (trừ ghép thận)"
            ],
            "tương_đối": [
                "Suy thận - tăng nguy cơ độc thận",
                "Suy gan - giảm chuyển hóa, tăng nồng độ",
                "Tăng huyết áp - có thể làm nặng",
                "Dùng với NSAID - tăng độc thận",
                "Dùng với CYP3A4 inducers - giảm nồng độ",
                "Dùng với CYP3A4 inhibitors - tăng nồng độ",
                "Dùng với statins - tăng nguy cơ tiêu cơ vân"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Cyclosporine là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (ghép tạng, bệnh tự miễn nặng). Một số nghiên cứu cho thấy tăng nguy cơ sinh non và nhẹ cân, nhưng không tăng nguy cơ dị tật bẩm sinh. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Cyclosporine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 25-50%, theo dõi nồng độ",
            "severe": "Giảm liều 50-75%, theo dõi nồng độ chặt chẽ",
            "notes": "Cyclosporine chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Cần giảm liều và theo dõi nồng độ chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Độc thận nặng (suy thận cấp)",
                "Tăng huyết áp nặng",
                "Độc gan (tăng men gan, vàng da)",
                "Co giật (hiếm)",
                "Buồn nôn, nôn nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng cyclosporine",
                "Theo dõi nồng độ cyclosporine trong máu",
                "Điều trị độc thận: hỗ trợ, có thể cần lọc máu",
                "Điều trị tăng huyết áp: thuốc hạ huyết áp",
                "Điều trị độc gan: hỗ trợ gan",
                "Theo dõi chức năng thận, gan, huyết áp chặt chẽ"
            ],
            "monitoring": "Nồng độ cyclosporine, chức năng thận, gan, huyết áp, dấu hiệu nhiễm trùng trong ít nhất 48-72 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm buồn nôn và tăng hấp thu",
                "timing": "Chia 2 lần/ngày (sáng và tối), cách đều 12 giờ. Uống cùng thời điểm mỗi ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha đậm đặc: 50mg/ml, sau đó pha loãng để truyền.",
                "infusion_rate": "Truyền liên tục trong 24 giờ. Không truyền nhanh (nguy cơ độc tính).",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể. Theo dõi nồng độ trong máu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cyclosporine (Sandimmune, Neoral)",
                "UpToDate - Cyclosporine: Drug information",
                "Lexicomp - Cyclosporine monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used in transplantation"
        }
    },
    
    "Mycophenolate": {
        "group": "Immunosuppressant - Antimetabolite",
        "vietnamese_name": "Mycophenolate mofetil, Mycophenolic acid, CellCept, Myfortic",
        "administration": ["PO", "IV"],
        "indications": [
            "Ghép tạng (thận, gan, tim, phổi) - phòng ngừa thải ghép",
            "Bệnh tự miễn (lupus ban đỏ hệ thống, viêm thận lupus)",
            "Bệnh thận IgA",
            "Hội chứng thận hư"
        ],
        "contraindications": [
            "Dị ứng mycophenolate",
            "Có thai (chống chỉ định tuyệt đối)",
            "Đang cho con bú",
            "Loét dạ dày tá tràng hoạt động"
        ],
        "dosage": {
            "adult_transplant_po": "1-1.5g x 2 lần/ngày (CellCept) hoặc 720mg x 2 lần/ngày (Myfortic)",
            "adult_transplant_iv": "1g x 2 lần/ngày",
            "adult_autoimmune": "1-1.5g x 2 lần/ngày",
            "notes": "Điều chỉnh liều theo đáp ứng và tác dụng phụ. Không cần TDM thường quy."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, theo dõi sát"
        },
        "side_effects": [
            "Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến)",
            "Tiêu chảy (phổ biến)",
            "Buồn nôn, nôn",
            "Loét dạ dày tá tràng",
            "Tăng nguy cơ nhiễm trùng",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
            "Dị tật bẩm sinh (nếu dùng trong thai kỳ - chống chỉ định tuyệt đối)"
        ],
        "interactions": [
            "Cholestyramine: giảm hấp thu mycophenolate",
            "Antacids: giảm hấp thu mycophenolate",
            "Acyclovir, Ganciclovir: tăng nguy cơ độc tính",
            "Probenecid: tăng nồng độ mycophenolate"
        ],
        "pregnancy": "X - Chống chỉ định tuyệt đối",
        "mechanism_of_action": "Mycophenolate mofetil (MMF) được chuyển hóa thành mycophenolic acid (MPA), chất hoạt động. MPA ức chế enzyme inosine monophosphate dehydrogenase (IMPDH), ngăn cản tổng hợp guanosine monophosphate (GMP) từ inosine monophosphate (IMP). GMP cần thiết cho tổng hợp DNA và RNA. Ức chế tổng hợp DNA và RNA → ức chế sự phát triển và phân chia tế bào, đặc biệt tế bào lympho B và T. Dẫn đến: ức chế miễn dịch qua trung gian tế bào lympho, giảm đáp ứng miễn dịch với kháng nguyên lạ (ghép tạng), và giảm đáp ứng tự miễn. Mycophenolate được dùng để phòng ngừa thải ghép tạng và điều trị các bệnh tự miễn. Thường dùng kết hợp với calcineurin inhibitor (cyclosporine, tacrolimus) và corticosteroid.",
        "monitoring": [
            "Công thức máu (WBC, platelet, hemoglobin) - giảm bạch cầu, giảm tiểu cầu, thiếu máu - QUAN TRỌNG",
            "Dấu hiệu tiêu chảy - phổ biến, có thể nặng",
            "Dấu hiệu loét dạ dày tá tràng (đau bụng, nôn ra máu, phân đen)",
            "Dấu hiệu nhiễm trùng - tăng nguy cơ nhiễm trùng",
            "Dấu hiệu ung thư (lymphoma, ung thư da) - tăng nguy cơ",
            "Chức năng thận (creatinine, eGFR) - cần điều chỉnh liều ở suy thận",
            "Tương tác với cholestyramine, antacids (giảm hấp thu)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ - gây dị tật bẩm sinh nghiêm trọng",
            "Phụ nữ trong độ tuổi sinh đẻ: phải dùng 2 biện pháp tránh thai hiệu quả",
            "Giảm bạch cầu, giảm tiểu cầu phổ biến - theo dõi công thức máu mỗi 1-4 tuần",
            "Tiêu chảy phổ biến - có thể cần giảm liều hoặc ngừng",
            "Loét dạ dày tá tràng - có thể cần PPI hoặc H2 blocker",
            "Tăng nguy cơ nhiễm trùng - cần phòng ngừa nhiễm trùng",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da) - cần theo dõi",
            "Uống cách xa cholestyramine, antacids ít nhất 2 giờ (giảm hấp thu)",
            "Thận trọng với acyclovir, ganciclovir (tăng nguy cơ độc tính)",
            "Điều chỉnh liều ở suy thận (giảm liều 25-75%)"
        ],
        "pharmacokinetics": {
            "half_life": "17 giờ (MPA)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "97% (MPA)",
            "metabolism": "Gan: MMF chuyển hóa thành MPA (chất hoạt động). MPA chuyển hóa qua glucuronidation.",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng lỏng: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi dùng. Không đông lạnh.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ - gây dị tật bẩm sinh nghiêm trọng (dị tật tai, dị tật tim, dị tật hệ thần kinh). Phụ nữ trong độ tuổi sinh đẻ: phải dùng 2 biện pháp tránh thai hiệu quả. Tăng nguy cơ nhiễm trùng và ung thư (lymphoma, ung thư da). Giảm bạch cầu, giảm tiểu cầu phổ biến.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cholestyramine, Colestipol",
                    "mechanism": "Gắn với mycophenolate trong ruột, giảm hấp thu",
                    "effect": "Giảm hấp thu mycophenolate, giảm hiệu quả",
                    "management": "Uống mycophenolate cách xa cholestyramine ít nhất 2 giờ."
                },
                {
                    "drug": "Antacids (aluminum, magnesium)",
                    "mechanism": "Gắn với mycophenolate trong ruột, giảm hấp thu",
                    "effect": "Giảm hấp thu mycophenolate, giảm hiệu quả",
                    "management": "Uống mycophenolate cách xa antacids ít nhất 2 giờ."
                }
            ],
            "moderate": [
                {
                    "drug": "Acyclovir, Ganciclovir, Valacyclovir",
                    "mechanism": "Cả hai đều có thể gây giảm bạch cầu, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ giảm bạch cầu nặng, tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Theo dõi công thức máu chặt chẽ. Có thể cần giảm liều một trong hai thuốc."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Ức chế bài tiết MPA qua thận, tăng nồng độ MPA",
                    "effect": "Tăng nồng độ mycophenolate, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều mycophenolate."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng mycophenolate",
                "Có thai - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (gây dị tật bẩm sinh nghiêm trọng)",
                "Đang cho con bú",
                "Loét dạ dày tá tràng hoạt động"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều 50-75%",
                "Giảm bạch cầu, giảm tiểu cầu nặng - có thể cần ngừng",
                "Tiêu chảy nặng - có thể cần giảm liều hoặc ngừng",
                "Dùng với acyclovir, ganciclovir - tăng nguy cơ giảm bạch cầu",
                "Phụ nữ trong độ tuổi sinh đẻ - phải dùng 2 biện pháp tránh thai"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Mycophenolate là FDA category X - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ. Gây dị tật bẩm sinh nghiêm trọng (dị tật tai, dị tật tim, dị tật hệ thần kinh). Nguy cơ dị tật bẩm sinh khoảng 20-25% (so với 2-3% ở dân số chung). Phụ nữ trong độ tuổi sinh đẻ: phải dùng 2 biện pháp tránh thai hiệu quả trước, trong, và sau khi dùng mycophenolate.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Mycophenolate bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, có thể cần giảm liều nhẹ",
            "notes": "Mycophenolate chuyển hóa ở gan nhưng không tích lũy đáng kể ở suy gan. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu, giảm tiểu cầu nặng (myelosuppression)",
                "Tiêu chảy nặng",
                "Loét dạ dày tá tràng",
                "Nhiễm trùng nặng (do giảm bạch cầu)",
                "Chảy máu (do giảm tiểu cầu)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng mycophenolate",
                "Theo dõi công thức máu chặt chẽ",
                "Điều trị giảm bạch cầu: G-CSF nếu cần",
                "Điều trị giảm tiểu cầu: truyền tiểu cầu nếu cần",
                "Điều trị tiêu chảy: loperamide, bù dịch",
                "Điều trị loét dạ dày: PPI, H2 blocker",
                "Điều trị nhiễm trùng: kháng sinh nếu có",
                "Theo dõi dấu hiệu nhiễm trùng, chảy máu chặt chẽ"
            ],
            "monitoring": "Công thức máu, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu loét dạ dày trong ít nhất 1-2 tuần."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Chia 2 lần/ngày (sáng và tối), cách đều 12 giờ. Uống cách xa cholestyramine, antacids ít nhất 2 giờ."
            },
            "iv": {
                "reconstitution": "Pha với D5W. Pha đậm đặc: 6mg/ml, sau đó pha loãng để truyền.",
                "infusion_rate": "Truyền trong 2 giờ. Không truyền nhanh.",
                "compatibility": ["D5W"],
                "incompatibility": ["NS (không ổn định)"],
                "notes": "Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mycophenolate (CellCept, Myfortic)",
                "UpToDate - Mycophenolate: Drug information",
                "Lexicomp - Mycophenolate monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used in transplantation"
        }
    },
    
    "Tacrolimus": {
        "group": "Immunosuppressant - Calcineurin Inhibitor",
        "vietnamese_name": "Tacrolimus, FK506, Prograf, Advagraf",
        "administration": ["PO", "IV"],
        "indications": [
            "Ghép tạng (thận, gan, tim, phổi)",
            "Bệnh tự miễn (viêm khớp dạng thấp, vảy nến, viêm da cơ địa)",
            "Bệnh thận IgA",
            "Hội chứng thận hư"
        ],
        "contraindications": [
            "Dị ứng tacrolimus",
            "Ung thư (trừ một số trường hợp)",
            "Nhiễm trùng nặng chưa điều trị",
            "Tăng huyết áp không kiểm soát",
            "Suy thận nặng (trừ ghép thận)"
        ],
        "dosage": {
            "adult_transplant_po": "0.1-0.2mg/kg/ngày chia 2 lần (tùy loại ghép)",
            "adult_transplant_iv": "0.03-0.05mg/kg/ngày truyền liên tục",
            "adult_autoimmune": "0.05-0.1mg/kg/ngày chia 2 lần",
            "notes": "Điều chỉnh liều theo nồng độ trong máu (trough level). Mục tiêu: 5-15 ng/mL (tùy chỉ định)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, theo dõi sát"
        },
        "side_effects": [
            "Độc thận (phổ biến, có thể vĩnh viễn)",
            "Tăng huyết áp",
            "Tăng cholesterol, triglyceride",
            "Tăng đường huyết (đái tháo đường sau ghép)",
            "Run tay (phổ biến)",
            "Đau đầu",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Tăng nguy cơ nhiễm trùng",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
            "Độc gan (hiếm)",
            "Độc thần kinh (co giật, lú lẫn - hiếm)"
        ],
        "interactions": [
            "Nhiều thuốc: ức chế hoặc cảm ứng CYP3A4",
            "Ketoconazole, Itraconazole: tăng nồng độ tacrolimus",
            "Rifampin, Phenytoin: giảm nồng độ tacrolimus",
            "NSAID: tăng độc thận",
            "Statins: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Tacrolimus là calcineurin inhibitor, tương tự cyclosporine nhưng mạnh hơn 10-100 lần. Ức chế calcineurin, ngăn chặn kích hoạt NFAT, giảm sản xuất IL-2, và ức chế hoạt hóa tế bào T. Dẫn đến: ức chế miễn dịch qua trung gian tế bào T, giảm đáp ứng miễn dịch với kháng nguyên lạ (ghép tạng), và giảm đáp ứng tự miễn. Tacrolimus được dùng để phòng ngừa thải ghép tạng và điều trị các bệnh tự miễn. Cần theo dõi nồng độ trong máu (TDM) để đảm bảo hiệu quả và giảm độc tính. Tacrolimus có ít tác dụng phụ thẩm mỹ hơn cyclosporine (không gây rậm lông, phì đại nướu).",
        "monitoring": [
            "Nồng độ tacrolimus trong máu (trough level, pre-dose) - QUAN TRỌNG: mục tiêu 5-15 ng/mL (tùy chỉ định và thời gian sau ghép)",
            "Chức năng thận (creatinine, eGFR) - độc thận phổ biến, có thể vĩnh viễn",
            "Huyết áp - tăng huyết áp phổ biến",
            "Đường huyết - tăng đường huyết, đái tháo đường sau ghép",
            "Lipid máu (cholesterol, triglyceride) - tăng lipid",
            "Chức năng gan (ALT, AST, bilirubin) - độc gan hiếm",
            "Công thức máu (CBC) - giảm bạch cầu, tiểu cầu (hiếm)",
            "Dấu hiệu nhiễm trùng - tăng nguy cơ nhiễm trùng",
            "Dấu hiệu ung thư (lymphoma, ung thư da) - tăng nguy cơ",
            "Dấu hiệu độc thần kinh (co giật, lú lẫn) - hiếm",
            "Tương tác với nhiều thuốc (CYP3A4 inhibitors/inducers)"
        ],
        "precautions": [
            "Độc thận phổ biến và có thể vĩnh viễn - theo dõi chức năng thận chặt chẽ",
            "Tăng huyết áp phổ biến - cần điều trị tăng huyết áp",
            "Tăng đường huyết, đái tháo đường sau ghép - theo dõi đường huyết",
            "Tăng lipid máu - có thể cần statin (thận trọng với nguy cơ tiêu cơ vân)",
            "NHIỀU TƯƠNG TÁC THUỐC - kiểm tra tất cả thuốc đang dùng",
            "Theo dõi nồng độ trong máu (TDM) - điều chỉnh liều theo nồng độ",
            "Tránh dùng với NSAID (tăng độc thận)",
            "Tránh dùng với CYP3A4 inducers (rifampin, phenytoin) - giảm nồng độ",
            "Thận trọng với CYP3A4 inhibitors (ketoconazole, itraconazole) - tăng nồng độ",
            "Tăng nguy cơ nhiễm trùng - cần phòng ngừa nhiễm trùng",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da) - cần theo dõi",
            "Run tay phổ biến - có thể giảm liều nếu nặng",
            "Uống với thức ăn hoặc không thức ăn (tùy sản phẩm)"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ (dao động 8-16 giờ)",
            "onset": "Vài giờ đến vài ngày",
            "duration": "12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "99%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa thành nhiều metabolites",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Chuyển hóa phụ thuộc CYP3A4, nhiều tương tác thuốc."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng lỏng: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi dùng. Không đông lạnh.",
        "black_box_warnings": "Độc thận có thể vĩnh viễn, đặc biệt với liều cao hoặc dùng kéo dài. Tăng nguy cơ nhiễm trùng và ung thư (lymphoma, ung thư da). Tăng huyết áp và đái tháo đường phổ biến. Nhiều tương tác thuốc nghiêm trọng. Cần theo dõi nồng độ trong máu (TDM) và chức năng thận chặt chẽ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, voriconazole, ritonavir, clarithromycin, erythromycin)",
                    "mechanism": "Ức chế chuyển hóa tacrolimus qua CYP3A4, tăng nồng độ tacrolimus",
                    "effect": "Tăng nồng độ tacrolimus, tăng độc tính (độc thận, tăng huyết áp)",
                    "management": "Giảm liều tacrolimus 50-75%. Theo dõi nồng độ tacrolimus và chức năng thận chặt chẽ."
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin, carbamazepine, phenobarbital)",
                    "mechanism": "Cảm ứng chuyển hóa tacrolimus qua CYP3A4, giảm nồng độ tacrolimus",
                    "effect": "Giảm nồng độ tacrolimus, giảm hiệu quả, tăng nguy cơ thải ghép",
                    "management": "Tăng liều tacrolimus 2-3 lần. Theo dõi nồng độ tacrolimus chặt chẽ. Cân nhắc thuốc thay thế."
                },
                {
                    "drug": "NSAID (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "Cả hai đều có thể gây độc thận, tác dụng cộng dồn",
                    "effect": "Tăng độc thận, tăng nguy cơ suy thận cấp",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, theo dõi chức năng thận chặt chẽ."
                },
                {
                    "drug": "Statins (atorvastatin, simvastatin, lovastatin)",
                    "mechanism": "Tacrolimus ức chế chuyển hóa statin qua CYP3A4, tăng nồng độ statin",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân (rhabdomyolysis)",
                    "management": "Giảm liều statin hoặc dùng statin không phụ thuộc CYP3A4 (pravastatin, rosuvastatin). Theo dõi CK, dấu hiệu tiêu cơ vân."
                }
            ],
            "moderate": [
                {
                    "drug": "Potassium-sparing diuretics (spironolactone, amiloride)",
                    "mechanism": "Cả hai đều có thể gây tăng kali máu",
                    "effect": "Tăng nguy cơ tăng kali máu",
                    "management": "Theo dõi kali máu. Tránh dùng đồng thời nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tacrolimus",
                "Ung thư (trừ một số trường hợp đặc biệt)",
                "Nhiễm trùng nặng chưa điều trị",
                "Tăng huyết áp không kiểm soát",
                "Suy thận nặng (trừ ghép thận)"
            ],
            "tương_đối": [
                "Suy thận - tăng nguy cơ độc thận",
                "Suy gan - giảm chuyển hóa, tăng nồng độ",
                "Tăng huyết áp - có thể làm nặng",
                "Đái tháo đường - có thể làm nặng",
                "Dùng với NSAID - tăng độc thận",
                "Dùng với CYP3A4 inducers - giảm nồng độ",
                "Dùng với CYP3A4 inhibitors - tăng nồng độ",
                "Dùng với statins - tăng nguy cơ tiêu cơ vân"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tacrolimus là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (ghép tạng, bệnh tự miễn nặng). Một số nghiên cứu cho thấy tăng nguy cơ sinh non và nhẹ cân, nhưng không tăng nguy cơ dị tật bẩm sinh. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Tacrolimus bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 25-50%, theo dõi nồng độ",
            "severe": "Giảm liều 50-75%, theo dõi nồng độ chặt chẽ",
            "notes": "Tacrolimus chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Cần giảm liều và theo dõi nồng độ chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Độc thận nặng (suy thận cấp)",
                "Tăng huyết áp nặng",
                "Tăng đường huyết nặng",
                "Độc gan (tăng men gan, vàng da)",
                "Độc thần kinh (co giật, lú lẫn)",
                "Buồn nôn, nôn nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng tacrolimus",
                "Theo dõi nồng độ tacrolimus trong máu",
                "Điều trị độc thận: hỗ trợ, có thể cần lọc máu",
                "Điều trị tăng huyết áp: thuốc hạ huyết áp",
                "Điều trị tăng đường huyết: insulin nếu cần",
                "Điều trị độc gan: hỗ trợ gan",
                "Điều trị độc thần kinh: hỗ trợ, chống co giật nếu cần",
                "Theo dõi chức năng thận, gan, huyết áp, đường huyết chặt chẽ"
            ],
            "monitoring": "Nồng độ tacrolimus, chức năng thận, gan, huyết áp, đường huyết, dấu hiệu nhiễm trùng, dấu hiệu độc thần kinh trong ít nhất 48-72 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Tùy sản phẩm: một số uống với thức ăn, một số không. Kiểm tra hướng dẫn sử dụng.",
                "timing": "Chia 2 lần/ngày (sáng và tối), cách đều 12 giờ. Uống cùng thời điểm mỗi ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha đậm đặc: 0.5mg/ml, sau đó pha loãng để truyền.",
                "infusion_rate": "Truyền liên tục trong 24 giờ. Không truyền nhanh (nguy cơ độc tính).",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể. Theo dõi nồng độ trong máu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tacrolimus (Prograf, Advagraf)",
                "UpToDate - Tacrolimus: Drug information",
                "Lexicomp - Tacrolimus monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used in transplantation"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": False,
            "organ_toxicity": ["Nephrotoxicity (common, can be permanent) - CRITICAL", "Hypertension", "Post-transplant diabetes", "Hyperlipidemia", "Neurotoxicity (seizures, confusion - rare)", "Hepatotoxicity (rare)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["Tacrolimus trough levels (target 5-15 ng/mL depending on indication and time post-transplant) - CRITICAL", "Renal function (creatinine, eGFR) - CRITICAL (nephrotoxicity common, can be permanent)", "Blood pressure - hypertension common", "Blood glucose - post-transplant diabetes", "Lipid panel (cholesterol, triglycerides)", "Hepatic function (ALT, AST, bilirubin) - hepatotoxicity rare", "CBC (leukocytes, platelets) - rare", "Signs of infection - increased risk", "Signs of malignancy (lymphoma, skin cancer) - increased risk", "Signs of neurotoxicity (seizures, confusion) - rare", "Drug interactions - CRITICAL (many CYP3A4 inhibitors/inducers)"]
        },
        "guideline_tags": [
            "AST Guidelines - Organ Transplantation",
            "KDIGO Guidelines - Kidney Transplantation",
            "FDA Black Box Warning - Tacrolimus and Nephrotoxicity",
            "FDA Black Box Warning - Tacrolimus and Post-transplant Diabetes",
            "FDA Black Box Warning - Tacrolimus and Drug Interactions (CYP3A4)"
        ]
    },
    
}

__all__ = ['IMMUNOSUPPRESSANTS_DRUGS']
