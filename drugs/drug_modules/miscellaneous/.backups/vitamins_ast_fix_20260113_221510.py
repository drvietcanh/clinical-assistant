"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology"""

# Vitamins

VITAMINS_DRUGS = {
    "Calcium (elemental)": {
        "group": "Vitamins/Supplements - Calcium",
        "vietnamese_name": "Calci bổ sung (calcium carbonate/citrate)",
        "administration": ["PO"],
        "indications": [
            "Thiếu calci, co cứng cơ do hạ calci máu nhẹ",
            "Hỗ trợ điều trị loãng xương (kết hợp vitamin D và thuốc chống loãng xương)",
            "Phụ nữ mang thai, cho con bú, người cao tuổi có nguy cơ thiếu calci",
        ],
        "contraindications": [
            "Tăng calci máu",
            "Sỏi thận calci hoạt động",
            "Tăng calci niệu nặng",
        ],
        "dosage": {
            "adult_osteoporosis_support": "Tổng lượng calci nguyên tố từ chế độ ăn + thuốc ~1000–1200mg/ngày (tùy tuổi và giới), chia 1–2 lần",
            "notes": "Ưu tiên calci từ thức ăn; chỉ bổ sung lượng thiếu. Calcium carbonate nên dùng cùng bữa ăn, calcium citrate có thể dùng xa bữa ăn.",
        },
        "side_effects": [
            "Táo bón, đầy bụng",
            "Tăng calci máu nếu dùng liều cao kéo dài (đặc biệt kèm vitamin D liều cao)",
            "Sỏi thận calci (nguy cơ tăng nhẹ nếu dùng liều cao lâu dài)",
        ],
        "interactions": [
            "Bisphosphonates đường uống, levothyroxine, tetracyclines, fluoroquinolones, sắt: giảm hấp thu khi dùng cùng lúc",
            "Thiazide: tăng nguy cơ tăng calci máu",
        ],
        "pregnancy": "A/B – an toàn nếu dùng trong giới hạn khuyến cáo",
        "mechanism_of_action": (
            "Cung cấp calci nguyên tố cần thiết cho khoáng hóa xương, co cơ, dẫn truyền thần kinh và đông máu. "
            "Trong loãng xương, bổ sung calci (kèm vitamin D) giúp tối ưu hiệu quả thuốc chống loãng xương và hạn chế mất xương."
        ),
        "monitoring": [
            "Calci máu và chức năng thận nếu dùng liều cao hoặc ở bệnh nhân nguy cơ cao",
            "Tiền sử và triệu chứng sỏi thận",
        ],
        "precautions": [
            "Không vượt quá tổng calci nguyên tố 1500mg/ngày (từ tất cả nguồn) trừ khi có chỉ định đặc biệt",
            "Tránh dùng đồng thời với thuốc dễ tạo phức; cách ít nhất 2 giờ trước hoặc 4 giờ sau",
            "Bổ sung nước đầy đủ để giảm nguy cơ sỏi thận",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (ion sinh lý)",
            "onset": "Vài ngày–tuần để cải thiện thiếu hụt",
            "duration": "Phụ thuộc dự trữ xương và chế độ ăn",
            "protein_binding": "N/A",
            "clearance": "Thải qua thận và đường tiêu hóa",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ẩm.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Bisphosphonates, levothyroxine, tetracyclines, fluoroquinolones, sắt",
                    "mechanism": "Tạo phức, giảm hấp thu thuốc",
                    "effect": "Giảm hiệu quả điều trị",
                    "management": "Dùng thuốc kia ít nhất 2 giờ trước hoặc 4 giờ sau calcium.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tăng calci máu",
                "Sỏi thận calci hoạt động",
            ],
            "tương_đối": [
                "Tiền sử sỏi thận calci",
                "Tăng calci niệu",
                "Dùng đồng thời nhiều nguồn calci, vitamin D liều cao, hoặc thiazide",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "A/B",
            "pregnancy_details": "Khuyến nghị bổ sung calci vừa phải trong thai kỳ (thường 1000–1300mg/ngày tổng cộng).",
            "lactation": {
                "safety": "Compatible",
                "details": "Calci là khoáng chất thiết yếu; an toàn trong giới hạn khuyến cáo.",
                "recommendation": "Có thể dùng an toàn.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Không phụ thuộc chuyển hóa gan.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, theo dõi calci máu và chức năng thận",
            "under_30": "Thận trọng, giảm liều nếu cần. Theo dõi calci máu và chức năng thận chặt chẽ",
            "hemodialysis": "Thận trọng, có thể cần giảm liều. Theo dõi calci máu và chức năng thận chặt chẽ",
            "notes": "Calcium thải trừ qua thận. Suy thận có thể làm giảm thải trừ calci, tăng nguy cơ tăng calci máu. Theo dõi calci máu và chức năng thận chặt chẽ ở bệnh nhân suy thận."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu: buồn nôn, nôn, táo bón, đa niệu, khát nhiều, lú lẫn",
                "Sỏi thận, vôi hóa mô mềm (dùng liều rất cao kéo dài)",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng tất cả nguồn calci và vitamin D",
                "Bù dịch, lợi tiểu quai (furosemide) sau khi đủ dịch để tăng thải calci",
            ],
            "monitoring": "Calci máu, creatinin, tình trạng nước–điện giải.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc và điều chỉnh calci máu nếu tăng calci máu."},
        "administration_instructions": {
            "oral": {
                "with_food": "Calcium carbonate nên dùng cùng thức ăn; calcium citrate có thể dùng cùng hoặc xa bữa ăn.",
                "timing": "Chia 1–2 lần/ngày, ưu tiên dùng buổi tối nếu chỉ uống 1 lần.",
            }
        },
        "references": {
            "primary_sources": [
                "NOF Guidelines 2024 – Calcium and vitamin D",
                "UpToDate – Calcium supplementation",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – guideline-based",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "None",
            "organ_toxicity": {
                "renal": "Moderate (calcium kidney stones with high doses, especially with inadequate hydration)",
                "metabolic": "Moderate (hypercalcemia with high doses, especially with vitamin D or thiazides)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Serum calcium (if high doses or at-risk patients)",
                "Renal function (creatinine, eGFR) if high doses",
                "History and symptoms of kidney stones",
                "Signs of hypercalcemia (nausea, vomiting, constipation, polyuria, polydipsia, confusion)"
            ],
            "look_alike_sound_alike": ["Calcium", "Calcitriol", "Calcium carbonate", "Calcium citrate"]
        },
        "guideline_tags": [
            "NOF Guidelines - Calcium and Vitamin D Supplementation",
            "IOM Guidelines - Dietary Reference Intakes for Calcium",
            "WHO Guidelines - Calcium Supplementation",
            "FDA Drug Information - Calcium Supplements"
        ],
        "black_box_warnings": None,
},
    "Folic Acid":     {
        "group": "Hematology - Vitamin",
        "vietnamese_name": "Acid Folic",
        "administration": [
            "PO"
    ],
        "indications": [
            "Thiếu máu do thiếu folate",
            "Dự phòng dị tật ống thần kinh trong thai kỳ",
            "Bệnh hồng cầu hình liềm",
            "Đang dùng methotrexate"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng folic acid"
    ],
            "tương_đối": [
                "Ung thư - thận trọng (folic acid có thể kích thích tế bào ung thư)",
                "Thiếu vitamin B12 chưa được điều trị - thận trọng (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)"
    ],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng folic acid"
            ],
            "tương_đối": [
                "Ung thư - thận trọng (folic acid có thể kích thích tế bào ung thư)",
                "Thiếu vitamin B12 chưa được điều trị - thận trọng (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)"
            ]
        },
        "dosage": {
            "adult_deficiency": "1-5mg x 1 lần/ngày",
            "pregnancy": "0.4-0.8mg x 1 lần/ngày",
            "methotrexate": "5-10mg/tuần (24h sau methotrexate)",
            "notes": "Dùng kèm vitamin B12 khi thiếu máu",
        },
        "side_effects": [
            "Hiếm khi có tác dụng phụ",
            "Phản ứng dị ứng (hiếm)"
    ],
        "interactions": [
            "Methotrexate: giảm hiệu quả methotrexate (nhưng dùng để giảm độc tính)",
            "Phenytoin: giảm nồng độ phenytoin"
    ],
        "pregnancy": "A - Khuyến nghị dùng trong thai kỳ",
        "mechanism_of_action": """Folic acid (folate, vitamin B9) là coenzyme cần thiết cho tổng hợp DNA và RNA, đặc biệt quan trọng trong quá trình phân chia tế bào. Folic acid được chuyển đổi thành tetrahydrofolate (THF), tham gia vào các phản ứng methyl transfer, tổng hợp purine và pyrimidine (các nucleotide của DNA/RNA). Folic acid cần thiết cho sự phát triển bình thường của ống thần kinh trong thai kỳ (tuần 3-4), giúp ngăn ngừa dị tật ống thần kinh (spina bifida, anencephaly). Thiếu folic acid gây thiếu máu hồng cầu to do giảm tổng hợp DNA, dẫn đến tế bào hồng cầu chưa trưởng thành. Folic acid cũng được dùng để giảm độc tính của methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate).""",
        "monitoring": [
            "Hemoglobin, MCV (mean corpuscular volume) - theo dõi đáp ứng điều trị thiếu máu",
            "Nồng độ folate trong máu (nếu cần)",
            "Nồng độ vitamin B12 (thiếu B12 có thể che dấu bởi folic acid)",
            "Đáp ứng điều trị (giảm triệu chứng thiếu máu)",
            "Dấu hiệu dị ứng (hiếm)"
    ],
        "precautions": [
            "Dùng kèm vitamin B12 khi thiếu máu (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)",
            "Với thiếu máu: luôn kiểm tra B12 trước khi dùng folic acid",
            "Dự phòng dị tật ống thần kinh: bắt đầu trước khi có thai 1 tháng, tiếp tục trong 3 tháng đầu",
            "Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)",
            "Liều cao (>1mg/ngày) có thể che dấu thiếu B12",
            "An toàn trong thai kỳ và cho con bú",
            "Hiếm khi có tác dụng phụ",
            "Thận trọng ở bệnh nhân ung thư (folic acid có thể kích thích tế bào ung thư)"
    ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (vitamin)",
            "onset": "Vài ngày đến vài tuần (tác dụng tích tụ)",
            "duration": "Phụ thuộc vào dự trữ trong cơ thể",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (thải trừ qua nước tiểu), một phần dự trữ trong gan",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "Methotrexate",
                    "mechanism": """Folic acid giảm hiệu quả methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate)""",
                    "effect": "Giảm hiệu quả methotrexate (nhưng dùng để giảm độc tính methotrexate)",
                    "management": """Dùng folic acid 24 giờ sau methotrexate (không dùng cùng lúc). Theo dõi đáp ứng điều trị methotrexate""",
                },
    {
                    "drug": "Phenytoin",
                    "mechanism": "Folic acid giảm nồng độ phenytoin (cơ chế chưa rõ)",
                    "effect": "Giảm nồng độ phenytoin, giảm hiệu quả chống co giật",
                    "management": "Theo dõi nồng độ phenytoin, có thể cần tăng liều phenytoin",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": """Khuyến nghị dùng trong thai kỳ. Folic acid rất quan trọng cho sự phát triển bình thường của ống thần kinh trong thai kỳ (tuần 3-4), giúp ngăn ngừa dị tật ống thần kinh (spina bifida, anencephaly). Nên bắt đầu trước khi có thai 1 tháng và tiếp tục trong 3 tháng đầu thai kỳ. Liều dự phòng: 0.4-0.8mg/ngày. Liều điều trị thiếu máu: 1-5mg/ngày.""",
            "lactation": {
                "safety": "Compatible",
                "details": """Folic acid bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Folic acid trong sữa mẹ có lợi cho trẻ.""",
                "recommendation": "Có thể dùng an toàn khi cho con bú. Liều thường dùng (0.4-5mg/ngày) an toàn cho trẻ bú mẹ",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều",
            "moderate": "Không đổi liều",
            "severe": "Không đổi liều",
            "notes": "Folic acid là vitamin, không chuyển hóa ở gan. Suy gan không ảnh hưởng đến folic acid",
        },
        "overdose_management": {
            "symptoms": [
                "Hiếm khi có triệu chứng (folic acid ít độc)",
                "Phản ứng dị ứng (hiếm)",
                "Có thể che dấu thiếu B12 nếu dùng liều cao (>1mg/ngày)"
    ],
            "antidote": "Không có thuốc giải độc đặc hiệu",
            "treatment": [
                "Ngừng thuốc nếu có phản ứng dị ứng",
                "Điều trị hỗ trợ: Truyền dịch nếu cần",
                "Kiểm tra nồng độ vitamin B12 nếu dùng liều cao lâu dài",
                "Điều trị dị ứng nếu có (antihistamine, corticosteroid)"
    ],
            "monitoring": "Triệu chứng lâm sàng, dấu hiệu dị ứng, nồng độ vitamin B12 (nếu dùng liều cao lâu dài)",
        },
        "reversal_agents": {
            "available": False,
            "agents": None,
            "notes": "Không có thuốc giải độc đặc hiệu. Folic acid ít độc, hiếm khi cần điều trị đặc biệt",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ (nếu có)",
                "timing": """Với thiếu máu: 1-5mg x 1 lần/ngày. Với dự phòng dị tật ống thần kinh: 0.4-0.8mg x 1 lần/ngày (bắt đầu trước khi có thai 1 tháng, tiếp tục trong 3 tháng đầu). Với methotrexate: 5-10mg/tuần (dùng 24 giờ sau methotrexate, không dùng cùng lúc)""",
                "notes": """Dùng kèm vitamin B12 khi thiếu máu (folic acid có thể che dấu thiếu B12). Với thiếu máu: luôn kiểm tra B12 trước khi dùng folic acid. Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)""",
            },
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Hemoglobin, MCV (mean corpuscular volume) - to monitor treatment response for anemia",
                "Vitamin B12 levels - CRITICAL (folic acid can mask B12 deficiency, leading to neurological damage)",
                "Serum folate levels (if needed)",
                "Treatment response (reduced anemia symptoms)",
                "Signs of allergy (rare)"
            ],
            "look_alike_sound_alike": ["Folic Acid", "Folinic Acid", "Folinic acid"]
        },
        "guideline_tags": [
            "CDC Guidelines - Folic Acid Supplementation in Pregnancy",
            "WHO Guidelines - Folic Acid Supplementation",
            "ACOG Guidelines - Neural Tube Defect Prevention",
            "WHO Essential Medicines List"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Folic Acid",
                "UpToDate - Folic acid drug information",
                "CDC Guidelines for folic acid supplementation in pregnancy",
                "WHO Guidelines for folic acid supplementation",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics"
    ],
            "last_updated": "2025-02-04",
            "evidence_level": "High - Guidelines dựa trên chứng cứ từ CDC, WHO và FDA",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [
                "May mask vitamin B12 deficiency (high doses >1mg/day)"
    ],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Hemoglobin, MCV (for anemia treatment)",
                "Vitamin B12 levels - CRITICAL (to avoid masking B12 deficiency)",
                "Folate levels (if needed)",
                "Clinical response"
    ],
        },
        "guideline_tags": [
            "CDC Guidelines - Folic Acid Supplementation in Pregnancy",
            "WHO Guidelines - Folic Acid Supplementation",
            "ACOG Guidelines - Neural Tube Defect Prevention",
            "FDA Drug Information - Folic Acid"
    ],
    },
    "Vitamin C":     {
        "group": "Vitamins/Supplements - Vitamin C",
        "vietnamese_name": "Vitamin C, Ascorbic Acid",
        "administration": [
            "PO",
            "IV"
    ],
        "indications": [
            "Thiếu vitamin C (scurvy)",
            "Dự phòng thiếu vitamin C",
            "Hỗ trợ miễn dịch",
            "Vết thương chậm lành",
            "Bệnh nhân lọc máu (thiếu vitamin C)",
            "Nhiễm trùng (hỗ trợ)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng vitamin C",
                "Bệnh thận oxalate nặng"
    ],
            "tương_đối": [
                "Bệnh nhân có tiền sử sỏi thận oxalate - thận trọng (tăng nguy cơ)",
                "Hemochromatosis - thận trọng (tăng hấp thu sắt)"
    ],
        },
        "dosage": {
            "adult_deficiency": "100-200mg x 2-3 lần/ngày (PO)",
            "adult_maintenance": "60-100mg x 1 lần/ngày",
            "adult_iv": "200-500mg IV (bệnh nhân lọc máu)",
            "pediatric": "30-50mg x 1 lần/ngày",
            "notes": "Liều cao (>1g/ngày) có thể gây tiêu chảy",
        },
        "side_effects": [
            "Tiêu chảy (liều cao >1g/ngày)",
            "Buồn nôn",
            "Sỏi thận oxalate (liều cao lâu dài)",
            "Tăng hấp thu sắt (có thể gây quá tải sắt)"
    ],
        "interactions": [
            "Sắt: tăng hấp thu sắt",
            "Warfarin: có thể giảm hiệu quả warfarin (liều cao)",
            "Aspirin: tăng bài tiết vitamin C"
    ],
        "pregnancy": "A - An toàn",
        "mechanism_of_action": """Vitamin C (ascorbic acid) là vitamin tan trong nước, đóng vai trò quan trọng như một chất chống oxy hóa và cofactor cho nhiều enzyme. Vitamin C cần thiết cho tổng hợp collagen (protein chính của mô liên kết, xương, sụn, mạch máu), giúp vết thương lành nhanh. Vitamin C cũng tham gia vào tổng hợp catecholamines (dopamine, norepinephrine), carnitine, và chuyển hóa cholesterol. Vitamin C hoạt động như chất chống oxy hóa, bảo vệ tế bào khỏi tổn thương do gốc tự do, và tái tạo vitamin E (tocopherol) từ dạng oxy hóa. Vitamin C cũng tăng cường chức năng miễn dịch (tăng hoạt động của bạch cầu, tăng sản xuất interferon). Thiếu vitamin C gây scurvy (chảy máu nướu, vết thương chậm lành, yếu mệt).""",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng thiếu vitamin C)",
            "Dấu hiệu tiêu chảy (nếu dùng liều cao >1g/ngày)",
            "Nồng độ oxalate trong nước tiểu (nếu dùng liều cao lâu dài)",
            "Chức năng thận (nếu có nguy cơ sỏi thận)"
    ],
        "precautions": [
            "Liều cao (>1g/ngày) có thể gây tiêu chảy - giảm liều nếu có",
            "Thận trọng với bệnh nhân có tiền sử sỏi thận oxalate (tăng nguy cơ)",
            "Tăng hấp thu sắt - thận trọng với bệnh nhân quá tải sắt (hemochromatosis)",
            "An toàn trong thai kỳ và cho con bú",
            "Hấp thu tốt từ thức ăn (trái cây, rau quả)",
            "Không cần bổ sung nếu ăn đủ trái cây và rau quả"
    ],
        "pharmacokinetics": {
            "half_life": "10-20 ngày (dự trữ trong cơ thể)",
            "onset": "Vài ngày đến vài tuần (tác dụng tích tụ)",
            "duration": "Phụ thuộc vào dự trữ trong cơ thể",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận: bài tiết qua nước tiểu (liều cao), dự trữ trong mô (liều bình thường)",
        },
        "storage": """Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Vitamin C dễ bị oxy hóa khi tiếp xúc với không khí, ánh sáng, nhiệt độ cao.""",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "Sắt",
                    "mechanism": "Vitamin C tăng hấp thu sắt (chuyển Fe3+ thành Fe2+)",
                    "effect": "Tăng hấp thu sắt, có thể gây quá tải sắt",
                    "management": """Thận trọng với bệnh nhân hemochromatosis. Có thể dùng cùng để tăng hấp thu sắt khi thiếu máu thiếu sắt.""",
                },
    {
                    "drug": "Warfarin",
                    "mechanism": "Vitamin C liều cao có thể giảm hiệu quả warfarin (cơ chế chưa rõ)",
                    "effect": "Giảm hiệu quả warfarin",
                    "management": "Thận trọng. Theo dõi INR nếu dùng liều cao vitamin C.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": """An toàn trong thai kỳ. Vitamin C cần thiết cho sự phát triển bình thường của thai nhi. Liều khuyến nghị: 85mg/ngày trong thai kỳ.""",
            "lactation": {
                "safety": "Compatible",
                "details": "Vitamin C bài tiết vào sữa mẹ. An toàn cho trẻ bú mẹ. Liều khuyến nghị: 120mg/ngày khi cho con bú.",
                "recommendation": "Có thể dùng an toàn khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Vitamin C là vitamin, không chuyển hóa ở gan. Suy gan không ảnh hưởng đến vitamin C.",
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy (liều cao >1g/ngày)",
                "Buồn nôn, nôn",
                "Sỏi thận oxalate (liều cao lâu dài)",
                "Tăng hấp thu sắt (có thể gây quá tải sắt)"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc nếu có triệu chứng",
                "Giảm liều nếu tiêu chảy",
                "Điều trị hỗ trợ: truyền dịch nếu cần",
                "Theo dõi chức năng thận nếu có nguy cơ sỏi thận"
    ],
            "monitoring": "Triệu chứng lâm sàng, chức năng thận",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ.",
                "timing": "Dùng 1-3 lần/ngày tùy liều. Liều cao nên chia nhỏ để tránh tiêu chảy.",
            },
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W",
                "infusion_rate": "Truyền chậm (200-500mg trong 30-60 phút)",
                "compatibility": [
                    "NS",
                    "D5W"
    ],
                "incompatibility": [],
                "notes": "Dùng cho bệnh nhân lọc máu hoặc không thể uống.",
            },
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "renal": "Moderate (oxalate kidney stones with high doses long-term)",
                "metabolic": "Moderate (increased iron absorption - can cause iron overload in hemochromatosis)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": [
                "Clinical response (symptoms of vitamin C deficiency)",
                "Signs of diarrhea (if high doses >1g/day)",
                "Urine oxalate levels (if high doses long-term)",
                "Renal function (if history of kidney stones)",
                "Iron levels (if hemochromatosis - increased iron absorption)"
            ],
            "look_alike_sound_alike": ["Vitamin C", "Ascorbic Acid", "Ascorbate"]
        },
        "guideline_tags": [
            "WHO Guidelines - Vitamin C Supplementation",
            "FDA Drug Information - Vitamin C (Ascorbic Acid)",
            "IOM Guidelines - Dietary Reference Intakes for Vitamin C",
            "WHO Essential Medicines List"
        ],
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vitamin C (Ascorbic Acid)",
                "UpToDate - Vitamin C drug information",
                "WHO Guidelines for vitamin C supplementation"
    ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Guidelines dựa trên chứng cứ từ WHO và FDA",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "None",
            "organ_toxicity": {
                "renal": "Moderate (oxalate kidney stones with high doses >1g/day long-term)",
                "gastrointestinal": "Low (diarrhea with high doses >1g/day)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Clinical response (symptoms of vitamin C deficiency)",
                "Signs of diarrhea (if high doses >1g/day)",
                "Urine oxalate levels (if high doses long-term)",
                "Renal function (if history of kidney stones)"
            ],
            "look_alike_sound_alike": ["Vitamin C", "Ascorbic acid", "Ascorbate"]
        },
        "guideline_tags": [
            "WHO Guidelines - Vitamin C Supplementation",
            "FDA Drug Information - Vitamin C (Ascorbic Acid)",
            "IOM Guidelines - Dietary Reference Intakes for Vitamin C"
        ]
    },
    "Vitamin D3 (Cholecalciferol)": {
        "group": "Vitamins/Supplements - Vitamin D",
        "vietnamese_name": "Vitamin D3, Cholecalciferol",
        "administration": ["PO"],
        "indications": [
            "Thiếu vitamin D, còi xương ở trẻ em",
            "Hỗ trợ điều trị loãng xương, người cao tuổi",
            "Phòng ngừa thiếu vitamin D ở người ít tiếp xúc ánh nắng, bệnh nhân mạn tính",
        ],
        "contraindications": [
            "Tăng calci máu",
            "Sỏi thận calci tái phát",
            "Nhiễm độc vitamin D trước đó",
        ],
        "dosage": {
            "adult_deficiency": "800–2000 IU/ngày, có thể dùng liều nạp 50.000 IU/tuần trong 6–8 tuần theo phác đồ chuyên khoa",
            "adult_osteoporosis_support": "800–1000 IU/ngày kết hợp calcium",
            "pediatric": "400–1000 IU/ngày tùy tuổi và tình trạng thiếu hụt",
            "notes": "Điều chỉnh liều theo nồng độ 25(OH)D huyết thanh, mục tiêu thường 30–50 ng/mL.",
        },
        "side_effects": [
            "Thường dung nạp tốt ở liều sinh lý",
            "Quá liều kéo dài: tăng calci máu, buồn nôn, nôn, khát nhiều, tiểu nhiều, sỏi thận",
        ],
        "interactions": [
            "Thiazide: tăng nguy cơ tăng calci máu khi dùng kèm vitamin D liều cao và calcium",
            "Digitalis (digoxin): tăng nguy cơ loạn nhịp nếu tăng calci máu",
        ],
        "pregnancy": "A - Không có nguy cơ trong các nghiên cứu có đối chứng",
        '"mechanism_of_action": (
            "Vitamin D3 được chuyển hóa ở gan thành 25-hydroxyvitamin D [25(OH)D], sau đó ở thận thành dạng hoạt động "
            "1,25-dihydroxyvitamin D [1,25(OH)2D]. Dạng hoạt động tăng hấp thu calci và phospho tại ruột, "
            "tăng tái hấp thu calci tại thận và điều hòa chuyển hóa xương, giúp duy trì nồng độ calci, phospho và sức khỏe xương."
        ),
        "monitoring": [
            "Nồng độ 25(OH)D huyết thanh nếu điều trị thiếu hụt nặng hoặc dùng liều cao",
            "Calci máu, creatinin (đặc biệt nếu dùng cùng calcium và thiazide)",
        ],
        "precautions": [
            "Tránh lạm dụng liều rất cao kéo dài (ví dụ >4000 IU/ngày mà không theo dõi)",
            "Thận trọng ở bệnh nhân có sỏi thận calci, tăng calci máu, cường cận giáp",
        ],
        "pharmacokinetics": {
            "half_life": "25(OH)D có t1/2 khoảng 2–3 tuần",
            "onset": "Vài tuần để điều chỉnh nồng độ 25(OH)D",
            "duration": "Hiệu quả kéo dài vài tuần–tháng do dự trữ trong mô mỡ",
            "protein_binding": "Gắn với vitamin D–binding protein trong huyết tương",
            "clearance": "Chuyển hóa ở gan, thận; thải qua mật/phân",
        },
        "storage": "Bảo quản nơi khô mát, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thiazide diuretics",
                    "mechanism": "Giảm thải calci qua thận + tăng hấp thu calci do vitamin D",
                    "effect": "Tăng nguy cơ tăng calci máu",
                    "management": "Theo dõi calci máu nếu dùng chung với liều vitamin D và calcium cao.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tăng calci máu",
                "Nhiễm độc vitamin D trước đó",
            ],
            "tương_đối": [
                "Sỏi thận calci tái phát",
                "Cường cận giáp, sarcoidosis (tăng sản xuất vitamin D nội sinh)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "A/B",
            "pregnancy_details": "Liều sinh lý (400–2000 IU/ngày) an toàn và được khuyến nghị trong thai kỳ nếu thiếu hụt.",
            "lactation": {
                "safety": "Compatible",
                "details": "Vitamin D vào sữa mẹ ở nồng độ thấp; thường cần bổ sung riêng cho trẻ.",
                "recommendation": "Có thể dùng an toàn ở liều sinh lý.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng, điều chỉnh theo nồng độ 25(OH)D",
            "notes": "Chuyển hóa ở gan; suy gan nặng có thể giảm hoạt hóa vitamin D.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Có thể cần dạng hoạt hóa (calcitriol) nếu suy thận nặng",
            "under_30": "Dùng calcitriol (dạng hoạt hóa) thay vì vitamin D3 thường",
            "hemodialysis": "Dùng calcitriol (dạng hoạt hóa) thay vì vitamin D3 thường",
            "notes": "Vitamin D3 được chuyển hóa ở thận thành dạng hoạt động 1,25(OH)2D (calcitriol). Suy thận nặng làm giảm chuyển hóa này, nên cần dùng calcitriol (dạng hoạt hóa) thay vì vitamin D3 thường. Theo dõi nồng độ 25(OH)D và calci máu."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu (buồn nôn, nôn, khát, tiểu nhiều, lú lẫn)",
                "Sỏi thận, vôi hóa mô mềm (dùng liều rất cao kéo dài)",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng vitamin D và calcium",
                "Bù dịch, lợi tiểu, corticosteroid hoặc bisphosphonate nếu tăng calci máu nặng",
            ],
            "monitoring": "Calci, phospho, creatinin huyết thanh.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc và điều chỉnh calci máu nếu cần."},
        "administration_instructions": {
            "oral": {
                "with_food": "Nên dùng với bữa ăn có chất béo nhẹ để tăng hấp thu.",
                "timing": "1 lần/ngày hoặc 1 lần/tuần/tháng tùy dạng chế phẩm và phác đồ.",
            }
        },
        "references": {
            "primary_sources": [
                "Endocrine Society guideline on vitamin D deficiency",
                "UpToDate – Vitamin D supplementation",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "High – guideline-based",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "None",
            "organ_toxicity": {
                "metabolic": "Moderate (hypercalcemia with overdose, especially with calcium or thiazides)",
                "renal": "Moderate (calcium kidney stones with overdose)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Serum 25(OH)D levels (if treating deficiency or using high doses)",
                "Serum calcium, creatinine (especially if co-administered with calcium or thiazides)",
                "Signs of hypercalcemia (nausea, vomiting, polydipsia, polyuria, confusion)"
            ],
            "look_alike_sound_alike": ["Vitamin D3", "Cholecalciferol", "Calcitriol", "Ergocalciferol"]
        },
        "guideline_tags": [
            "Endocrine Society Guidelines - Vitamin D Deficiency",
            "NOF Guidelines - Calcium and Vitamin D Supplementation",
            "IOM Guidelines - Dietary Reference Intakes for Vitamin D",
            "FDA Drug Information - Vitamin D"
        ]
    },

    "Vitamin E": {
        'group': 'Vitamins/Supplements - Vitamin E',
        'vietnamese_name': 'Vitamin E, Alpha-tocopherol',
        'administration': ['PO'],
        'indications': [
            'Thiếu vitamin E (hiếm)',
            'Dự phòng thiếu vitamin E',
            'Chống oxy hóa',
            'Bệnh nhân kém hấp thu chất béo',
            'Thiếu máu tan máu ở trẻ sinh non'
        ],
        'contraindications': [
            'Dị ứng vitamin E',
            'Đang dùng warfarin (tăng nguy cơ chảy máu)'
        ],
        'dosage': {
            'adult_standard': '15-30mg (22-33 IU) x 1 lần/ngày',
            'adult_max': '1000mg/ngày',
            'pediatric': '5-10mg/ngày',
            'notes': 'Liều cao (>400 IU/ngày) có thể tăng nguy cơ chảy máu'
        },
        'side_effects': [
            'Chảy máu (liều cao >400 IU/ngày)',
            'Buồn nôn',
            'Tiêu chảy',
            'Mệt mỏi',
            'Tăng nguy cơ đột quỵ xuất huyết (liều cao)'
        ],
        'interactions': [
            'Warfarin: tăng nguy cơ chảy máu',
            'Aspirin: tăng nguy cơ chảy máu',
            'Chất béo: tăng hấp thu vitamin E'
        ],pregnancy': 'A - An toàn',
        'mechanism_of_action': 'Vitamin E (alpha-tocopherol) là vitamin tan trong chất béo, hoạt động chủ yếu như một chất chống oxy hóa mạnh. Vitamin E bảo vệ màng tế bào khỏi tổn thương do gốc tự do (lipid peroxidation), đặc biệt quan trọng cho tế bào thần kinh, tế bào cơ, và tế bào hồng cầu. Vitamin E ức chế quá trình oxy hóa LDL cholesterol, giúp ngăn ngừa xơ vữa động mạch. Vitamin E cũng có vai trò trong chức năng miễn dịch, tổng hợp DNA, và điều hòa biểu hiện gen. Vitamin E được tái tạo từ dạng oxy hóa bởi vitamin C. Thiếu vitamin E (hiếm) gây thiếu máu tan máu, bệnh thần kinh ngoại biên, và yếu cơ. Vitamin E cần chất béo để hấp thu tốt.',
        'monitoring': [
            'Đáp ứng điều trị (giảm triệu chứng thiếu vitamin E)',
            'Dấu hiệu chảy máu (nếu dùng liều cao >400 IU/ngày)',
            'INR (nếu dùng với warfarin)',
            'Chức năng gan (nếu dùng liều cao lâu dài)'
        ],
        'precautions': [
            'Liều cao (>400 IU/ngày) có thể tăng nguy cơ chảy máu - thận trọng',
            'KHÔNG dùng với warfarin (tăng nguy cơ chảy máu nghiêm trọng)',
            'Thận trọng với aspirin và các thuốc chống đông khác',
            'Cần chất béo để hấp thu tốt - nên dùng với thức ăn có chất béo',
            'An toàn trong thai kỳ và cho con bú (liều bình thường)',
            'Liều cao có thể tăng nguy cơ đột quỵ xuất huyết',
            'Không cần bổ sung nếu ăn đủ thực phẩm giàu vitamin E (dầu thực vật, hạt, rau xanh)'
        ],
        'pharmacokinetics': {
            'half_life': 'Vài ngày đến vài tuần (dự trữ trong mô mỡ)',
            'onset': 'Vài ngày đến vài tuần (tác dụng tích tụ)',
            'duration': 'Phụ thuộc vào dự trữ trong cơ thể',
            'protein_binding': 'Không đáng kể',
            'clearance': 'Gan: chuyển hóa, bài tiết qua mật. Dự trữ trong mô mỡ và gan.'
        },storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Vitamin E dễ bị oxy hóa khi tiếp xúc với không khí, ánh sáng.',
        'black_box_warnings': None,
        'drug_interactions': {
            'major': [
                {
                    'drug': 'Warfarin',
                    'mechanism': 'Vitamin E ức chế vitamin K-dependent clotting factors, tăng tác dụng warfarin',
                    'effect': 'Tăng nguy cơ chảy máu nghiêm trọng',
                    'management': 'CHỐNG CHỈ ĐỊNH dùng với warfarin. Nếu cần dùng, theo dõi INR chặt chẽ và giảm liều warfarin.'
                }
            ],moderate': [
                {
                    'drug': 'Aspirin, NSAIDs, Clopidogrel',
                    'mechanism': 'Cả hai đều ảnh hưởng đến đông máu',
                    'effect': 'Tăng nguy cơ chảy máu',
                    'management': 'Thận trọng. Theo dõi dấu hiệu chảy máu.'
                }
            ],minor': []
        },contraindications': {
            'tuyệt_đối': [
                'Dị ứng vitamin E',
                'Đang dùng warfarin - CHỐNG CHỈ ĐỊNH'
            ],
        'tương_đối': [
                'Đang dùng aspirin, NSAIDs, clopidogrel - thận trọng (tăng nguy cơ chảy máu)',
                'Bệnh nhân có nguy cơ chảy máu - thận trọng',
                'Liều cao >400 IU/ngày - tăng nguy cơ đột quỵ xuất huyết'
            ]
        },pregnancy_lactation': {
            'fda_category': 'A',
            'pregnancy_details': 'An toàn trong thai kỳ với liều bình thường (15-30mg/ngày). Liều cao (>400 IU/ngày) không khuyến nghị trong thai kỳ do tăng nguy cơ chảy máu.',
            'lactation': {
                'safety': 'Compatible',
                'details': 'Vitamin E bài tiết vào sữa mẹ. An toàn cho trẻ bú mẹ với liều bình thường.',
                'recommendation': 'Có thể dùng an toàn khi cho con bú với liều bình thường.'
            }
        },hepatic_adjustment': {
            'mild': 'Không đổi',
            'moderate': 'Không đổi',
            'severe': 'Thận trọng, có thể giảm liều',
            'notes': 'Vitamin E chuyển hóa ở gan và bài tiết qua mật. Suy gan nặng có thể ảnh hưởng đến chuyển hóa.'
        },overdose_management': {
            'symptoms': [
                'Chảy máu (liều cao >400 IU/ngày)',
                'Buồn nôn, nôn',
                'Tiêu chảy',
                'Mệt mỏi',
                'Tăng nguy cơ đột quỵ xuất huyết'
            ],antidote': 'Không có antidote đặc hiệu',
            'treatment': [
                'Ngừng thuốc nếu có triệu chứng chảy máu',
                'Điều trị chảy máu nếu có (vitamin K, FFP nếu cần)',
                'Theo dõi INR nếu dùng với warfarin',
                'Điều trị hỗ trợ: truyền dịch nếu cần'
            ],
        'monitoring': 'Dấu hiệu chảy máu, INR, huyết áp, dấu hiệu đột quỵ'
        },reversal_agents': {
            'available': False,
            'agents': []
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Moderate",
            "organ_toxicity": {
                "hematologic": "Moderate (increased bleeding risk with high doses >400 IU/day)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Clinical response (symptoms of vitamin E deficiency)",
                "Signs of bleeding (if high doses >400 IU/day or co-administered with warfarin/anticoagulants) - CRITICAL",
                "INR (if co-administered with warfarin) - CRITICAL",
                "Hepatic function (if high doses long-term)"
            ],
            "look_alike_sound_alike": ["Vitamin E", "Alpha-tocopherol", "Tocopherol"]
        },
        "guideline_tags": [
            "IOM Guidelines - Dietary Reference Intakes for Vitamin E",
            "FDA Drug Information - Vitamin E",
            "FDA Warning - Vitamin E and Bleeding Risk with Warfarin"
        ],administration_instructions': {
            'oral': {
                'with_food': 'NÊN dùng với thức ăn có chất béo để tăng hấp thu. Vitamin E tan trong chất béo, hấp thu tốt hơn khi có chất béo.',
                'timing': 'Dùng 1 lần/ngày với thức ăn. Tránh dùng liều cao >400 IU/ngày.'
            },iv': {
                'reconstitution': 'Không có dạng IV thường dùng',
                'infusion_rate': 'N/A',
                'compatibility': [],incompatibility': [],notes': 'Vitamin E chủ yếu dùng đường uống.'
            }
        },references': {
            'primary_sources': [
                'FDA Drug Label - Vitamin E (Alpha-tocopherol)',
                'UpToDate - Vitamin E drug information',
                'WHO Guidelines for vitamin E supplementation'
            ],last_updated': '2025-02-05',
            'evidence_level': 'High - Guidelines dựa trên chứng cứ từ WHO và FDA'
        },
        "black_box_warnings": None,
},

}

__all__ = ["VITAMINS_DRUGS"]
