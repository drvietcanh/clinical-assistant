"""
DMARDs - Disease-Modifying Antirheumatic Drugs
Thuốc điều trị bệnh thấp khớp, Lupus, bệnh tự miễn.
"""

DMARDS_DRUGS = {
    "Methotrexate":     {
        "group": "Rheumatology - DMARD (Immunosuppressant)",
        "vietnamese_name": "Methotrexate",
        "brand_names": {
            "common": [
                "Trexall",
                "Rheumatrex"
            ],
            "vietnam": [
                "Methotrexate 2.5mg",
                "Methotrexate 5mg",
                "Methotrexate 10mg",
                "Trexall",
                "Rheumatrex"
            ],
        },
        "manufacturer": {
            "primary": "Teva Pharmaceuticals (Trexall), Pfizer (Rheumatrex)",
            "vietnam": [
                "Teva Pharmaceuticals",
                "Pfizer",
                "Các công ty dược phẩm Việt Nam (generic - Methotrexate)"
            ],
            "notes": "Teva Pharmaceuticals là nhà sản xuất gốc của Trexall (methotrexate). Có nhiều sản phẩm generic tại Việt Nam."
        },
        "administration": [
            "PO",
            "SC",
            "IM"
    ],
        "indications": [
            "Viêm khớp dạng thấp (Rheumatoid Arthritis) - Thuốc đầu tay",
            "Viêm khớp vảy nến (Psoriatic Arthritis)",
            "Lupus ban đỏ hệ thống (SLE)",
            "Viêm da vảy nến (Psoriasis)",
            "Ung thư (Leukemia, Lymphoma) - Liều cao"
    ],
        "contraindications": [
            "Có thai (CHỐNG CHỈ ĐỊNH - gây quái thai nghiêm trọng - Black Box Warning)",
            "Cho con bú",
            "Suy gan nặng",
            "Suy thận nặng (CrCl <30 ml/min)",
            "Suy tủy xương",
            "Nghiện rượu",
            "Dị ứng với methotrexate"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Có thai (CHỐNG CHỈ ĐỊNH - gây quái thai nghiêm trọng - Black Box Warning)",
                "Cho con bú",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30 ml/min)",
                "Suy tủy xương",
                "Dị ứng với methotrexate"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60 ml/min) - thận trọng, có thể cần giảm liều",
                "Suy gan trung bình - thận trọng, theo dõi men gan chặt chẽ",
                "Nghiện rượu - tăng nguy cơ độc gan",
                "Nhiễm trùng nặng - ngừng thuốc",
                "Phụ nữ có kế hoạch mang thai - tránh thai ≥3 tháng sau ngừng thuốc"
            ]
        },
        "dosage": {
            "adult_ra_initial": "7.5-10mg PO/SC/IM x 1 lần/tuần",
            "adult_ra_maintenance": "7.5-25mg PO/SC/IM x 1 lần/tuần (thường 15-20mg/tuần)",
            "adult_ra_max": "25mg/tuần (có thể tăng đến 30mg/tuần nếu cần)",
            "adult_psoriasis": "10-25mg PO/SC/IM x 1 lần/tuần",
            "adult_sle": "10-15mg PO/SC/IM x 1 lần/tuần",
            "adult_renal_crcl_30_60": "Giảm liều 50% (CrCl 30-60 ml/min)",
            "adult_renal_crcl_under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30 ml/min)",
            "adult_hepatic_impairment": "Thận trọng, giảm liều hoặc tránh dùng",
            "notes": "QUAN TRỌNG: Uống 1 lần/TUẦN, không phải mỗi ngày (sai lầm phổ biến → ngộ độc)! Bổ sung Folic Acid 1mg/ngày (trừ ngày uống MTX) để giảm tác dụng phụ. Điều chỉnh liều theo chức năng thận."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "30_60": "Giảm liều 50% (CrCl 30-60 ml/min)",
            "under_30": "CHỐNG CHỈ ĐỊNH - không dùng (CrCl <30 ml/min)",
            "dialysis": "CHỐNG CHỈ ĐỊNH",
            "notes": "Methotrexate thải trừ chủ yếu qua thận. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 ml/min). Cần giảm liều ở suy thận trung bình. Nguy cơ tích lũy và độc tính tăng ở suy thận."
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến)",
            "Loét miệng (Stomatitis)",
            "Suy tủy xương (Giảm bạch cầu, tiểu cầu, hồng cầu)",
            "Độc gan (Xơ gan nếu dùng lâu dài)",
            "Viêm phổi do Methotrexate (MTX pneumonitis) - Hiếm nhưng nguy hiểm",
            "Rụng tóc",
            "Nhiễm trùng (do ức chế miễn dịch)"
    ],
        "interactions": [
            "NSAIDs (liều cao): tăng độc tính MTX (giảm thải trừ qua thận) - thận trọng, theo dõi chức năng thận",
            "Trimethoprim/Sulfamethoxazole: tăng độc tính MTX (cộng gộp ức chế folate) - thận trọng",
            "PPI (Omeprazole, Pantoprazole): tăng nồng độ MTX - thận trọng",
            "Rượu: tăng nguy cơ độc gan - tránh rượu",
            "Penicillin: tăng nồng độ MTX - thận trọng",
            "Probenecid: tăng nồng độ MTX - thận trọng",
            "Aspirin: tăng độc tính MTX - thận trọng"
        ],
        "mechanism_of_action": """Chất đối kháng Folic Acid, ức chế dihydrofolate reductase (DHFR) → Ức chế tổng hợp DNA → Ức chế tế bào phân chia nhanh (lymphocyte, tế bào ung thư). Liều thấp (RA): Chống viêm, ức chế miễn dịch.""",
        "monitoring": [
            "Công thức máu (CBC) - Mỗi 2-4 tuần khi bắt đầu, sau đó mỗi 8-12 tuần",
            "Men gan (ALT, AST) - Mỗi 2-4 tuần khi bắt đầu, sau đó mỗi 8-12 tuần",
            "Chức năng thận (Creatinine, eGFR)",
            "Dấu hiệu nhiễm trùng",
            "Dấu hiệu viêm phổi (ho, khó thở)"
    ],
        "precautions": [
            "TUYỆT ĐỐI TRÁNH THAI - Gây quái thai nghiêm trọng (tránh thai ≥3 tháng sau ngừng thuốc)",
            "Uống 1 lần/TUẦN, không phải mỗi ngày (sai lầm phổ biến → ngộ độc)",
            "Bổ sung Folic Acid 1mg/ngày (trừ ngày uống MTX) để giảm tác dụng phụ",
            "Tránh rượu (tăng nguy cơ độc gan)",
            "Ngừng thuốc nếu nhiễm trùng nặng",
            "Theo dõi men gan, công thức máu định kỳ"
    ],
        "black_box_warnings": """Gây quái thai nghiêm trọng. Độc tủy xương, độc gan, độc phổi có thể gây tử vong. Chỉ dùng cho bệnh nhân có thể tuân thủ theo dõi chặt chẽ.""",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "High (thrombocytopenia)",
            "organ_toxicity": {"teratogenic": "Black Box Warning - Teratogenicity (severe birth defects)", "hematologic": "Black Box Warning - Bone marrow suppression (may be fatal)", "hepatic": "Black Box Warning - Hepatotoxicity (cirrhosis with long-term use)", "pulmonary": "Black Box Warning - Pneumonitis (rare but fatal)", "renal": "Nephrotoxicity (rare)", "gastrointestinal": "Mucositis, stomatitis"},
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": "Rare",
            "requires_monitoring": ["Black Box Warning - Pregnancy test (teratogenicity)", "CBC (Black Box Warning - bone marrow suppression, every 2-4 weeks initially, then every 8-12 weeks)", "Hepatic function (ALT, AST - Black Box Warning for hepatotoxicity, every 2-4 weeks initially, then every 8-12 weeks)", "Renal function (creatinine, eGFR - nephrotoxicity risk)", "Pulmonary symptoms (Black Box Warning - pneumonitis signs: cough, dyspnea)", "Folic acid supplementation (1mg/day except MTX day - reduces side effects)", "Weekly dosing (NOT daily - common error leads to overdose)", "NSAID/trimethoprim-sulfamethoxazole interactions (increase MTX toxicity)"],
            "look_alike_sound_alike": ["Methotrexate", "Metformin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Teratogenicity (severe birth defects)",
            "FDA Black Box Warning - Bone Marrow Suppression (may be fatal)",
            "FDA Black Box Warning - Hepatotoxicity (cirrhosis with long-term use)",
            "FDA Black Box Warning - Pneumonitis (rare but fatal)",
            "ACR Guidelines - Rheumatoid Arthritis",
            "ACR Guidelines - Psoriatic Arthritis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH trong thai kỳ",
        "pharmacokinetics": {
            "half_life": "3-10 giờ (liều thấp), 8-15 giờ (liều cao)",
            "onset": "Tác dụng trong 4-8 tuần",
            "duration": "1 tuần (do dùng 1 lần/tuần)",
            "protein_binding": "50-60%",
            "clearance": "Thận (thải trừ chủ yếu qua thận, 80-90%). Một phần được chuyển hóa qua gan. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 ml/min).",
            "metabolism": "Chuyển hóa một phần qua gan thành polyglutamate (hoạt động lâu dài). Thải trừ chủ yếu qua thận (80-90%)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "NSAIDs (liều cao - ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs giảm thải trừ methotrexate qua thận, tăng nồng độ methotrexate",
                    "effect": "Tăng độc tính methotrexate (ức chế tủy xương, độc gan, độc thận)",
                    "management": "Thận trọng. Theo dõi chức năng thận và CBC. Có thể cần giảm liều methotrexate hoặc tránh NSAIDs liều cao."
                },
                {
                    "drug": "Trimethoprim/Sulfamethoxazole (Bactrim, Septra)",
                    "mechanism": "Cộng gộp ức chế folate (cả hai đều ức chế DHFR)",
                    "effect": "Tăng độc tính methotrexate (ức chế tủy xương nghiêm trọng)",
                    "management": "Thận trọng. Theo dõi CBC chặt chẽ. Có thể cần giảm liều methotrexate hoặc tránh dùng chung."
                }
            ],
            "moderate": [
                {
                    "drug": "PPI (Omeprazole, Pantoprazole)",
                    "mechanism": "PPI có thể ức chế thải trừ methotrexate",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính",
                    "management": "Thận trọng. Theo dõi tác dụng phụ. Có thể cần giảm liều methotrexate."
                },
                {
                    "drug": "Penicillin",
                    "mechanism": "Penicillin có thể giảm thải trừ methotrexate",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết methotrexate qua thận",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính",
                    "management": "Thận trọng. Theo dõi tác dụng phụ. Có thể cần giảm liều methotrexate."
                },
                {
                    "drug": "Aspirin",
                    "mechanism": "Aspirin có thể giảm thải trừ methotrexate",
                    "effect": "Tăng độc tính methotrexate",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                }
            ],
            "minor": [
                {
                    "drug": "Rượu",
                    "mechanism": "Cộng gộp độc tính gan",
                    "effect": "Tăng nguy cơ độc gan",
                    "management": "Tránh rượu hoàn toàn."
                }
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Methotrexate gây quái thai nghiêm trọng ở người và động vật. Phụ nữ có kế hoạch mang thai phải tránh thai ≥3 tháng sau ngừng thuốc.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Methotrexate bài tiết vào sữa mẹ. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc."
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi men gan chặt chẽ",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH - không dùng",
            "notes": "Methotrexate chuyển hóa một phần qua gan. Suy gan có thể tăng nguy cơ độc tính (viêm gan, xơ gan). CHỐNG CHỈ ĐỊNH ở suy gan nặng. Theo dõi men gan chặt chẽ ở tất cả bệnh nhân."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế tủy xương (giảm bạch cầu, giảm tiểu cầu, thiếu máu) - có thể nghiêm trọng",
                "Độc gan (tăng men gan, viêm gan, suy gan)",
                "Viêm phổi kẽ (ho, khó thở) - hiếm nhưng nguy hiểm",
                "Loét miệng, buồn nôn, nôn nặng",
                "Suy thận cấp",
                "Có thể tử vong nếu không điều trị"
            ],
            "antidote": "Leucovorin (folinic acid) - antidote đặc hiệu",
            "treatment": [
                "Ngừng methotrexate ngay lập tức",
                "Leucovorin (folinic acid) IV/PO: 10-15mg/m² mỗi 6 giờ cho đến khi nồng độ methotrexate <0.01 micromol/L (antidote đặc hiệu)",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ: truyền dịch, theo dõi dấu hiệu sống",
                "Điều trị ức chế tủy xương: truyền máu, tiểu cầu, G-CSF nếu cần",
                "Điều trị độc gan: hỗ trợ gan, theo dõi men gan",
                "Điều trị viêm phổi kẽ: corticosteroid, hỗ trợ hô hấp nếu cần",
                "Theo dõi nồng độ methotrexate trong máu",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu, men gan, chức năng thận, nồng độ methotrexate trong máu, dấu hiệu viêm phổi"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Leucovorin (Folinic Acid)",
                    "dosage": "10-15mg/m² IV/PO mỗi 6 giờ cho đến khi nồng độ methotrexate <0.01 micromol/L",
                    "mechanism": "Leucovorin là dạng hoạt động của folic acid, bỏ qua bước ức chế DHFR, cung cấp folate cho tế bào bình thường",
                    "notes": "Antidote đặc hiệu cho methotrexate. Phải bắt đầu càng sớm càng tốt sau quá liều."
                }
            ],
            "notes": "Leucovorin (folinic acid) là antidote đặc hiệu cho methotrexate. Phải bắt đầu càng sớm càng tốt sau quá liều."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Uống 1 lần/TUẦN (không phải mỗi ngày!). RA: 7.5-25mg/tuần. Psoriasis: 10-25mg/tuần.",
                "notes": "QUAN TRỌNG: Uống 1 lần/TUẦN, không phải mỗi ngày (sai lầm phổ biến → ngộ độc)! Bổ sung Folic Acid 1mg/ngày (trừ ngày uống MTX) để giảm tác dụng phụ."
            },
            "sc": {
                "reconstitution": "Pha trong nước cất hoặc NaCl 0,9%",
                "injection_site": "Dưới da bụng hoặc đùi",
                "notes": "Có thể dùng SC thay vì PO nếu không dung nạp đường uống hoặc để tăng hấp thu."
            },
            "im": {
                "reconstitution": "Pha trong nước cất hoặc NaCl 0,9%",
                "injection_site": "Tiêm bắp",
                "notes": "Có thể dùng IM thay vì PO nếu không dung nạp đường uống hoặc để tăng hấp thu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Trexall (methotrexate)",
                "ACR Guidelines - Rheumatoid Arthritis",
                "ACR Guidelines - Psoriatic Arthritis",
                "UpToDate - Methotrexate: Drug Information",
                "EULAR Recommendations - Rheumatoid Arthritis"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High - FDA approved, ACR guidelines, extensive clinical data"
        },
    },
    "Hydroxychloroquine":     {
        "group": "Rheumatology - DMARD (Antimalarial)",
        "vietnamese_name": "Hydroxychloroquine, Plaquenil",
        "brand_names": {
            "common": [
                "Plaquenil"
            ],
            "vietnam": [
                "Plaquenil 200mg",
                "Hydroxychloroquine 200mg",
                "Hydroxychloroquine"
            ],
        },
        "manufacturer": {
            "primary": "Sanofi-Aventis (Plaquenil)",
            "vietnam": [
                "Sanofi-Aventis",
                "Các công ty dược phẩm Việt Nam (generic)"
            ],
            "notes": "Sanofi-Aventis là nhà sản xuất gốc của Plaquenil (hydroxychloroquine). Có nhiều sản phẩm generic tại Việt Nam."
        },
        "administration": [
            "PO"
        ],
        "indications": [
            "Lupus ban đỏ hệ thống (SLE) - Thuốc nền, điều trị triệu chứng da và khớp",
            "Viêm khớp dạng thấp (RA) - Nhẹ đến trung bình",
            "Sốt rét (Malaria) - Dự phòng và điều trị",
            "Viêm khớp vảy nến (Psoriatic Arthritis)"
        ],
        "contraindications": [
            "Dị ứng với hydroxychloroquine hoặc chloroquine",
            "Bệnh võng mạc (retinopathy) do hydroxychloroquine",
            "Thiếu G6PD (nguy cơ tan máu)",
            "Rối loạn nhịp tim nặng (QT prolongation nặng)"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hydroxychloroquine hoặc chloroquine",
                "Bệnh võng mạc (retinopathy) do hydroxychloroquine",
                "Thiếu G6PD (nguy cơ tan máu)",
                "Rối loạn nhịp tim nặng (QT prolongation nặng)"
            ],
            "tương_đối": [
                "Bệnh võng mạc khác - tăng nguy cơ độc võng mạc",
                "Bệnh gan nặng - thận trọng",
                "Bệnh thận nặng - thận trọng",
                "Rối loạn nhịp tim - tăng nguy cơ QT prolongation"
            ]
        },
        "dosage": {
            "adult_sle_ra_initial": "400-600mg/ngày (chia 1-2 lần) trong vài tuần đầu",
            "adult_sle_ra_maintenance": "200-400mg/ngày (chia 1-2 lần), không quá 5mg/kg/ngày dựa trên cân nặng lý tưởng",
            "adult_sle_ra_max": "≤5mg/kg/ngày dựa trên cân nặng lý tưởng (để giảm nguy cơ độc võng mạc)",
            "adult_malaria_prophylaxis": "400mg uống 1 lần/tuần, bắt đầu 2 tuần trước khi tiếp xúc, tiếp tục trong 4-8 tuần sau khi rời khỏi vùng dịch",
            "adult_malaria_treatment": "800mg uống 1 lần, sau đó 400mg sau 6-8 giờ, sau đó 400mg/ngày x 2 ngày",
            "adult_hepatic_impairment": "Thận trọng, có thể cần giảm liều",
            "adult_renal_impairment": "Thận trọng, có thể cần giảm liều",
            "notes": "QUAN TRỌNG: Liều ≤5mg/kg/ngày dựa trên cân nặng lý tưởng để giảm nguy cơ độc võng mạc. Uống với thức ăn để giảm buồn nôn. Tác dụng chậm (2-6 tháng) - cần kiên nhẫn. Khám mắt định kỳ mỗi năm để phát hiện độc võng mạc."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "30_60": "Thận trọng, có thể cần giảm liều (CrCl 30-60 ml/min)",
            "under_30": "Thận trọng, giảm liều hoặc tránh dùng (CrCl <30 ml/min)",
            "dialysis": "Thận trọng, giảm liều hoặc tránh dùng",
            "notes": "Hydroxychloroquine thải trừ một phần qua thận. Thận trọng ở suy thận. Có thể cần giảm liều ở suy thận."
        },
        "side_effects": [
            "Buồn nôn, tiêu chảy (phổ biến, nhẹ)",
            "Độc võng mạc (retinopathy) - hiếm nhưng nghiêm trọng, không hồi phục (nguy cơ tăng với liều cao và dùng lâu dài)",
            "Phát ban da (thường gặp)",
            "Đau đầu, chóng mặt (thường gặp)",
            "Rối loạn nhịp tim (QT prolongation) - hiếm",
            "Tan máu (ở bệnh nhân thiếu G6PD) - CHỐNG CHỈ ĐỊNH",
            "Rối loạn thị giác (mờ mắt, nhìn đôi) - có thể là dấu hiệu độc võng mạc",
            "Rối loạn tâm thần (hiếm)",
            "Giảm thính lực, ù tai (hiếm)"
        ],
        "mechanism_of_action": "Hydroxychloroquine tích tụ trong lysosome tế bào miễn dịch, tăng pH nội lysosome, ức chế hoạt động của lysosome. Hydroxychloroquine ức chế Toll-like receptors (TLR), đặc biệt TLR7 và TLR9, giảm sản xuất cytokine (TNF-α, IL-1, IL-6), ức chế hoạt động của tế bào T và B, dẫn đến ức chế miễn dịch và chống viêm. Hydroxychloroquine cũng ức chế sự trình diện kháng nguyên và hoạt động của tế bào dendritic. An toàn hơn methotrexate và leflunomide.",
        "monitoring": [
            "Khám mắt (Ophthalmology) - trước điều trị (baseline), sau đó mỗi năm (phát hiện độc võng mạc - hiếm nhưng nghiêm trọng)",
            "Thị lực, thị trường, fundoscopy - mỗi năm",
            "ECG - nếu có nguy cơ QT prolongation hoặc dùng với thuốc kéo dài QT",
            "Không cần theo dõi xét nghiệm máu thường xuyên (khác methotrexate)",
            "Dấu hiệu rối loạn thị giác (mờ mắt, nhìn đôi) - có thể là dấu hiệu độc võng mạc"
        ],
        "interactions": [
            "Thuốc kéo dài QT (Azithromycin, Amiodarone, Quinolones): tăng nguy cơ rối loạn nhịp tim (QT prolongation) - thận trọng",
            "Digoxin: hydroxychloroquine tăng nồng độ digoxin - theo dõi nồng độ digoxin",
            "Insulin, Sulfonylurea: hydroxychloroquine tăng nguy cơ hạ đường huyết - theo dõi đường huyết",
            "Thuốc kháng acid, thuốc trị tiêu chảy: giảm hấp thu hydroxychloroquine - dùng cách xa ít nhất 4 giờ",
            "Cimetidine: tăng nồng độ hydroxychloroquine - thận trọng"
        ],
        "pregnancy": "C - Có thể dùng nếu cần thiết, an toàn hơn methotrexate",
        "precautions": [
            "QUAN TRỌNG: Nguy cơ độc võng mạc - khám mắt định kỳ mỗi năm (hiếm nhưng nghiêm trọng, không hồi phục)",
            "Liều ≤5mg/kg/ngày dựa trên cân nặng lý tưởng để giảm nguy cơ độc võng mạc",
            "Tác dụng chậm (2-6 tháng) - cần kiên nhẫn",
            "An toàn hơn Methotrexate và Leflunomide - ít tác dụng phụ",
            "Có thể dùng trong thai kỳ (Category C, an toàn hơn MTX)",
            "Uống với thức ăn để giảm buồn nôn",
            "Thận trọng khi dùng với thuốc kéo dài QT - tăng nguy cơ rối loạn nhịp tim",
            "Theo dõi dấu hiệu rối loạn thị giác - có thể là dấu hiệu độc võng mạc"
        ],
        "pharmacokinetics": {
            "half_life": "40-50 ngày (rất dài, do tích tụ trong mô)",
            "onset": "Tác dụng trong 2-6 tháng (chậm)",
            "duration": "Nhiều tuần đến nhiều tháng sau khi ngừng (do half-life dài)",
            "protein_binding": "~45%",
            "clearance": "Gan (chuyển hóa một phần) và thận (thải trừ một phần). Tích tụ trong mô (đặc biệt là mắt, da, gan, thận) do half-life rất dài.",
            "metabolism": "Chuyển hóa một phần qua gan. Tích tụ trong mô do half-life rất dài (40-50 ngày)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kéo dài QT (Azithromycin, Amiodarone, Quinolones)",
                    "mechanism": "Cộng gộp kéo dài QT",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim (QT prolongation, torsades de pointes)",
                    "management": "Thận trọng. Theo dõi ECG. Tránh dùng với thuốc kéo dài QT mạnh nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Hydroxychloroquine có thể ức chế P-gp, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ digoxin. Giảm liều digoxin nếu cần."
                },
                {
                    "drug": "Insulin, Sulfonylurea",
                    "mechanism": "Hydroxychloroquine có thể tăng nhạy cảm với insulin",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết. Có thể cần giảm liều insulin/sulfonylurea."
                },
                {
                    "drug": "Thuốc kháng acid, Thuốc trị tiêu chảy",
                    "mechanism": "Giảm hấp thu hydroxychloroquine",
                    "effect": "Giảm hấp thu hydroxychloroquine, giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 4 giờ."
                }
            ],
            "minor": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Cimetidine có thể ức chế chuyển hóa hydroxychloroquine",
                    "effect": "Tăng nồng độ hydroxychloroquine, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                }
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần thiết. Hydroxychloroquine đã được sử dụng an toàn trong thai kỳ cho SLE và RA. An toàn hơn methotrexate và leflunomide trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Hydroxychloroquine bài tiết vào sữa mẹ ở nồng độ thấp. Đã được sử dụng an toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú nếu lợi ích vượt trội. Theo dõi trẻ sơ sinh."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều hoặc tránh dùng",
            "notes": "Hydroxychloroquine chuyển hóa một phần qua gan. Suy gan có thể tăng nguy cơ tích tụ và độc tính. Thận trọng ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Độc võng mạc (mờ mắt, nhìn đôi, mất thị lực)",
                "Rối loạn nhịp tim (QT prolongation, torsades de pointes)",
                "Hạ đường huyết",
                "Tan máu (ở bệnh nhân thiếu G6PD)",
                "Co giật, hôn mê (liều rất cao)",
                "Suy tim, suy hô hấp (liều rất cao)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng hydroxychloroquine ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ: truyền dịch, theo dõi dấu hiệu sống",
                "Điều trị rối loạn nhịp tim: theo dõi ECG, điều chỉnh điện giải, điều trị nếu cần",
                "Điều trị hạ đường huyết: truyền glucose nếu cần",
                "Điều trị tan máu: truyền máu nếu cần",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài)"
            ],
            "monitoring": "Dấu hiệu sống, ECG, đường huyết, hemoglobin, thị lực, dấu hiệu độc võng mạc"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm buồn nôn",
                "timing": "Uống 1-2 lần/ngày tùy liều. SLE/RA: 200-400mg/ngày (khởi đầu 400-600mg/ngày). Malaria prophylaxis: 400mg x 1 lần/tuần.",
                "notes": "Uống với thức ăn để giảm buồn nôn. Liều ≤5mg/kg/ngày dựa trên cân nặng lý tưởng để giảm nguy cơ độc võng mạc. Dùng cách xa thuốc kháng acid và thuốc trị tiêu chảy ít nhất 4 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Plaquenil (hydroxychloroquine)",
                "ACR Guidelines - Rheumatoid Arthritis",
                "ACR Guidelines - Systemic Lupus Erythematosus",
                "UpToDate - Hydroxychloroquine: Drug Information",
                "EULAR Recommendations - Rheumatoid Arthritis",
                "EULAR Recommendations - Systemic Lupus Erythematosus"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High - FDA approved, ACR guidelines, extensive clinical data"
        },
    },
    "Sulfasalazine":     {
        "group": "Rheumatology - DMARD (Sulfonamide)",
        "vietnamese_name": "Sulfasalazine, Azulfidine",
        "brand_names": {
            "common": [
                "Azulfidine",
                "Salazopyrin"
            ],
            "vietnam": [
                "Sulfasalazine 500mg",
                "Azulfidine",
                "Sulfasalazine"
            ],
        },
        "manufacturer": {
            "primary": "Pfizer (Azulfidine), Pharmacia (Salazopyrin)",
            "vietnam": [
                "Pfizer",
                "Pharmacia",
                "Các công ty dược phẩm Việt Nam (generic)"
            ],
            "notes": "Pfizer là nhà sản xuất gốc của Azulfidine (sulfasalazine). Có nhiều sản phẩm generic tại Việt Nam."
        },
        "administration": [
            "PO"
        ],
        "indications": [
            "Viêm khớp dạng thấp (Rheumatoid Arthritis - RA)",
            "Viêm khớp cột sống dính khớp (Ankylosing Spondylitis)",
            "Bệnh viêm ruột (IBD - Ulcerative Colitis)",
            "Bệnh Crohn (Crohn's Disease)"
        ],
        "contraindications": [
            "Dị ứng với sulfonamide (sulfa) - CHỐNG CHỈ ĐỊNH",
            "Dị ứng với salicylate",
            "Suy thận nặng",
            "Suy gan nặng",
            "Thiếu G6PD (nguy cơ tan máu)",
            "Trẻ sơ sinh dưới 2 tuổi"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với sulfonamide (sulfa) - CHỐNG CHỈ ĐỊNH",
                "Dị ứng với salicylate",
                "Suy thận nặng",
                "Suy gan nặng",
                "Thiếu G6PD (nguy cơ tan máu)",
                "Trẻ sơ sinh dưới 2 tuổi"
            ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng, có thể cần giảm liều",
                "Suy gan trung bình - thận trọng",
                "Phụ nữ có thai - thận trọng, có thể dùng nếu cần thiết",
                "Nam giới có kế hoạch có con - giảm số lượng tinh trùng (hồi phục sau ngừng thuốc)"
            ]
        },
        "dosage": {
            "adult_ra_initial": "500mg uống 2 lần/ngày trong tuần đầu",
            "adult_ra_maintenance": "Tăng dần mỗi tuần 500mg đến 1000mg x 2 lần/ngày (2g/ngày), có thể tăng đến 3g/ngày nếu cần",
            "adult_ra_max": "3g/ngày (chia 2-4 lần)",
            "adult_ibd_acute": "1-2g uống 4 lần/ngày cho đến khi thuyên giảm",
            "adult_ibd_maintenance": "500mg uống 4 lần/ngày",
            "adult_renal_impairment": "Thận trọng, có thể cần giảm liều",
            "notes": "Uống với thức ăn để giảm buồn nôn. Tăng liều từ từ (mỗi tuần 500mg) để giảm tác dụng phụ. Bổ sung folic acid (1mg/ngày) vì sulfasalazine làm giảm hấp thu folate."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "30_60": "Thận trọng, có thể cần giảm liều (CrCl 30-60 ml/min)",
            "under_30": "Thận trọng, giảm liều hoặc tránh dùng (CrCl <30 ml/min)",
            "dialysis": "Thận trọng, giảm liều hoặc tránh dùng",
            "notes": "Sulfasalazine và các metabolite thải trừ qua thận. Thận trọng ở suy thận. Có thể cần giảm liều ở suy thận."
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến, thường giảm sau vài tuần)",
            "Đau đầu (thường gặp)",
            "Phát ban da, dị ứng (thường gặp)",
            "Giảm số lượng tinh trùng (oligospermia) - hồi phục sau ngừng thuốc",
            "Suy tủy xương (giảm bạch cầu, giảm tiểu cầu, thiếu máu) - hiếm nhưng nghiêm trọng",
            "Độc gan (tăng men gan, viêm gan) - hiếm",
            "Tan máu (ở bệnh nhân thiếu G6PD) - CHỐNG CHỈ ĐỊNH",
            "Thiếu folate (do giảm hấp thu folate)",
            "Đau bụng, tiêu chảy"
        ],
        "mechanism_of_action": "Sulfasalazine là prodrug, được chuyển hóa bởi vi khuẩn đường ruột thành sulfapyridine (kháng khuẩn) và 5-aminosalicylic acid (5-ASA, mesalamine - chống viêm). 5-ASA ức chế cyclooxygenase và lipoxygenase, giảm sản xuất prostaglandin và leukotriene, dẫn đến chống viêm. Cơ chế chống viêm ở RA chưa rõ hoàn toàn, có thể liên quan đến ức chế cytokine và tế bào miễn dịch.",
        "monitoring": [
            "Công thức máu (CBC) - mỗi 2-4 tuần khi bắt đầu, sau đó mỗi 2-3 tháng (suy tủy xương hiếm nhưng nghiêm trọng)",
            "Men gan (ALT, AST) - định kỳ (độc gan hiếm)",
            "Dấu hiệu dị ứng (phát ban, sốt) - thường gặp",
            "Folate máu - bổ sung folic acid 1mg/ngày vì sulfasalazine làm giảm hấp thu folate",
            "Chức năng thận - định kỳ",
            "Số lượng tinh trùng (ở nam giới có kế hoạch có con) - giảm số lượng tinh trùng, hồi phục sau ngừng thuốc"
        ],
        "interactions": [
            "Methotrexate: tăng nguy cơ ức chế tủy xương và độc gan - thận trọng, theo dõi CBC và men gan",
            "Mercaptopurine, Azathioprine: tăng nguy cơ ức chế tủy xương - thận trọng",
            "Warfarin: sulfasalazine có thể tăng tác dụng chống đông - theo dõi INR",
            "Digoxin: sulfasalazine có thể giảm hấp thu digoxin - theo dõi nồng độ digoxin",
            "Folate: sulfasalazine làm giảm hấp thu folate - bổ sung folic acid 1mg/ngày"
        ],
        "pregnancy": "B - Tương đối an toàn, có thể dùng nếu cần thiết",
        "precautions": [
            "Dị ứng Sulfa - CHỐNG CHỈ ĐỊNH (kiểm tra tiền sử dị ứng sulfa trước khi dùng)",
            "Uống với thức ăn để giảm buồn nôn",
            "Tăng liều từ từ (mỗi tuần 500mg) để giảm tác dụng phụ",
            "Bổ sung folic acid 1mg/ngày vì sulfasalazine làm giảm hấp thu folate",
            "Giảm số lượng tinh trùng ở nam giới - thông báo cho bệnh nhân, hồi phục sau ngừng thuốc",
            "Theo dõi CBC định kỳ (suy tủy xương hiếm nhưng nghiêm trọng)",
            "Theo dõi men gan định kỳ (độc gan hiếm)",
            "Thận trọng khi dùng với methotrexate - tăng nguy cơ ức chế tủy xương"
        ],
        "pharmacokinetics": {
            "half_life": "Sulfasalazine: 5-10 giờ; Sulfapyridine: 6-17 giờ; 5-ASA: 0.5-1.5 giờ",
            "onset": "Tác dụng trong 4-12 tuần",
            "duration": "12-24 giờ",
            "protein_binding": "Sulfapyridine: 50-70%",
            "clearance": "Thận (thải trừ chủ yếu qua thận). Một phần được chuyển hóa bởi vi khuẩn đường ruột.",
            "metabolism": "Chuyển hóa bởi vi khuẩn đường ruột thành sulfapyridine (kháng khuẩn) và 5-ASA (chống viêm). Sulfapyridine được hấp thu và chuyển hóa qua gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Methotrexate",
                    "mechanism": "Cộng gộp ức chế tủy xương và độc gan",
                    "effect": "Tăng nguy cơ ức chế tủy xương và độc gan",
                    "management": "Thận trọng. Theo dõi CBC và men gan chặt chẽ. Giảm liều nếu cần."
                },
                {
                    "drug": "Mercaptopurine, Azathioprine",
                    "mechanism": "Cộng gộp ức chế tủy xương",
                    "effect": "Tăng nguy cơ ức chế tủy xương",
                    "management": "Thận trọng. Theo dõi CBC chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Sulfasalazine có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu/ngừng sulfasalazine. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Sulfasalazine có thể giảm hấp thu digoxin",
                    "effect": "Giảm nồng độ digoxin, giảm hiệu quả",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần tăng liều digoxin."
                }
            ],
            "minor": [
                {
                    "drug": "Folate",
                    "mechanism": "Sulfasalazine làm giảm hấp thu folate",
                    "effect": "Thiếu folate",
                    "management": "Bổ sung folic acid 1mg/ngày."
                }
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Tương đối an toàn trong thai kỳ, có thể dùng nếu cần thiết. Sulfasalazine đã được sử dụng an toàn trong thai kỳ cho bệnh viêm ruột. Tuy nhiên, nên bổ sung folic acid để tránh thiếu folate.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Sulfasalazine và các metabolite bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây vàng da ở trẻ sơ sinh nếu thiếu G6PD.",
                "recommendation": "Có thể dùng khi cho con bú nếu lợi ích vượt trội. Theo dõi trẻ sơ sinh, đặc biệt nếu thiếu G6PD."
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH - không dùng",
            "notes": "Sulfasalazine và sulfapyridine chuyển hóa một phần qua gan. Suy gan có thể tăng nguy cơ độc tính (viêm gan). CHỐNG CHỈ ĐỊNH ở suy gan nặng. Thận trọng ở suy gan trung bình."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Ức chế tủy xương (giảm bạch cầu, giảm tiểu cầu, thiếu máu)",
                "Độc gan (tăng men gan, viêm gan)",
                "Tan máu (ở bệnh nhân thiếu G6PD)",
                "Phản ứng dị ứng nghiêm trọng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng sulfasalazine ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ: truyền dịch, theo dõi dấu hiệu sống",
                "Điều trị ức chế tủy xương: truyền máu, tiểu cầu, G-CSF nếu cần",
                "Điều trị độc gan: hỗ trợ gan, theo dõi men gan",
                "Điều trị tan máu: truyền máu nếu cần, theo dõi hemoglobin",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu, men gan, hemoglobin, dấu hiệu dị ứng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm buồn nôn",
                "timing": "Uống 2-4 lần/ngày tùy liều. RA: khởi đầu 500mg x 2 lần/ngày, tăng dần đến 1000mg x 2 lần/ngày. IBD: 1-2g x 4 lần/ngày (cấp), 500mg x 4 lần/ngày (duy trì).",
                "notes": "Uống với thức ăn để giảm buồn nôn. Tăng liều từ từ (mỗi tuần 500mg) để giảm tác dụng phụ. Bổ sung folic acid 1mg/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Azulfidine (sulfasalazine)",
                "ACR Guidelines - Rheumatoid Arthritis",
                "ACR Guidelines - Ankylosing Spondylitis",
                "UpToDate - Sulfasalazine: Drug Information",
                "EULAR Recommendations - Rheumatoid Arthritis"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High - FDA approved, ACR guidelines, extensive clinical data"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hematologic", "hepatic", "reproductive"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (bone marrow suppression - rare)", "Liver function (ALT, AST - hepatotoxicity rare)", "Allergic reactions (sulfa allergy - contraindicated)", "Sperm count (oligospermia - reversible)"]
        },
        "guideline_tags": [
            "ACR Guidelines - Rheumatoid Arthritis",
            "ACR Guidelines - Ankylosing Spondylitis",
            "WHO Essential Medicines List"
        ],
    },
    "Leflunomide":     {
        "group": "Rheumatology - DMARD (Immunosuppressant)",
        "vietnamese_name": "Leflunomide, Arava",
        "brand_names": {
            "common": [
                "Arava"
            ],
            "vietnam": [
                "Arava 10mg",
                "Arava 20mg",
                "Schuster 20mg",
                "Osbifin 20mg",
                "Leflunomide"
            ],
        },
        "manufacturer": {
            "primary": "Sanofi-Aventis (Arava)",
            "vietnam": [
                "Sanofi-Aventis",
                "Davipharm (Schuster)",
                "Delorbis Pharmaceuticals (Osbifin)",
                "Các công ty dược phẩm Việt Nam (generic)"
            ],
            "notes": "Sanofi-Aventis là nhà sản xuất gốc của Arava (leflunomide). Có các sản phẩm generic tại Việt Nam."
        },
        "administration": [
            "PO"
        ],
        "indications": [
            "Viêm khớp dạng thấp (Rheumatoid Arthritis - RA)",
            "Viêm khớp vảy nến (Psoriatic Arthritis)"
        ],
        "contraindications": [
            "Phụ nữ có thai (CHỐNG CHỈ ĐỊNH - gây quái thai nghiêm trọng - Black Box Warning)",
            "Phụ nữ có kế hoạch mang thai (phải làm washout trước)",
            "Suy gan nặng",
            "Suy thận nặng",
            "Dị ứng với leflunomide",
            "Nhiễm trùng nặng"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Phụ nữ có thai (CHỐNG CHỈ ĐỊNH - gây quái thai nghiêm trọng - Black Box Warning)",
                "Phụ nữ có kế hoạch mang thai (phải làm washout với cholestyramine trước)",
                "Suy gan nặng",
                "Suy thận nặng",
                "Dị ứng với leflunomide",
                "Nhiễm trùng nặng"
            ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng, theo dõi men gan chặt chẽ",
                "Suy thận trung bình - thận trọng",
                "Tiền sử bệnh gan - tăng nguy cơ độc gan",
                "Tăng huyết áp - theo dõi huyết áp",
                "Nam giới có kế hoạch có con - thận trọng"
            ]
        },
        "dosage": {
            "adult_ra_loading": "100mg uống 1 lần/ngày x 3 ngày đầu (tùy chọn, để đạt nồng độ ổn định nhanh hơn)",
            "adult_ra_maintenance": "10-20mg uống 1 lần/ngày (thường 20mg/ngày)",
            "adult_psoriatic_arthritis": "20mg uống 1 lần/ngày",
            "adult_hepatic_impairment": "Giảm liều hoặc tránh dùng",
            "adult_renal_impairment": "Không cần chỉnh liều ở suy thận nhẹ-trung bình, thận trọng ở suy thận nặng",
            "notes": "QUAN TRỌNG: TUYỆT ĐỐI TRÁNH THAI - gây quái thai nghiêm trọng (Black Box Warning). Thải trừ rất chậm (có thể còn trong cơ thể đến 2 năm). Nếu cần mang thai: phải làm washout với cholestyramine 8g x 3 lần/ngày x 11 ngày. Theo dõi men gan chặt chẽ (mỗi tháng trong 6 tháng đầu)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều (CrCl >60 ml/min)",
            "30_60": "Không cần chỉnh liều (CrCl 30-60 ml/min)",
            "under_30": "Thận trọng, có thể cần giảm liều (CrCl <30 ml/min)",
            "dialysis": "Thận trọng, có thể cần giảm liều",
            "notes": "Leflunomide và teriflunomide (metabolite) thải trừ chủ yếu qua gan và thận. Không cần điều chỉnh liều ở suy thận nhẹ-trung bình. Thận trọng ở suy thận nặng."
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Tăng huyết áp (phổ biến)",
            "Rụng tóc (thường gặp)",
            "Độc gan (tăng men gan, viêm gan) - Black Box Warning",
            "Gây quái thai (quái thai nghiêm trọng) - Black Box Warning",
            "Nhiễm trùng (do ức chế miễn dịch)",
            "Ức chế tủy xương (giảm bạch cầu, giảm tiểu cầu) - hiếm",
            "Viêm phổi kẽ (interstitial pneumonitis) - hiếm",
            "Đau đầu, chóng mặt",
            "Phát ban"
        ],
        "mechanism_of_action": "Leflunomide là tiền chất, chuyển hóa thành A77 1726 (teriflunomide), chất hoạt động. Teriflunomide ức chế dihydroorotate dehydrogenase (DHODH), enzyme cần thiết cho tổng hợp pyrimidine. Bằng cách ức chế DHODH, leflunomide ức chế tổng hợp pyrimidine, ức chế sự tăng sinh và hoạt động của tế bào T và B, dẫn đến ức chế miễn dịch và chống viêm. Leflunomide có tác dụng tương tự methotrexate nhưng cơ chế khác.",
        "monitoring": [
            "Men gan (ALT, AST) - mỗi tháng trong 6 tháng đầu, sau đó mỗi 2-3 tháng (Black Box Warning - độc gan nghiêm trọng)",
            "Huyết áp - định kỳ (tăng huyết áp phổ biến)",
            "Công thức máu (CBC) - định kỳ (ức chế tủy xương hiếm)",
            "Chức năng thận - định kỳ",
            "Dấu hiệu nhiễm trùng",
            "Dấu hiệu viêm phổi kẽ (ho, khó thở) - hiếm",
            "Test thai kỳ trước khi bắt đầu điều trị (Black Box Warning - gây quái thai)"
        ],
        "interactions": [
            "Methotrexate: tăng nguy cơ độc gan và viêm phổi kẽ - thận trọng, theo dõi men gan chặt chẽ",
            "Thuốc gây độc gan (azathioprine, sulfasalazine, rượu, thuốc gây độc tế bào, retinoids): tăng nguy cơ độc gan - thận trọng",
            "Warfarin: leflunomide có thể tăng tác dụng chống đông - theo dõi INR",
            "Rifampin: giảm nồng độ teriflunomide - có thể cần tăng liều leflunomide",
            "Cholestyramine, than hoạt tính: giảm nồng độ teriflunomide (dùng để washout)"
        ],
        "pregnancy": "X - CHỐNG CHỈ ĐỊNH trong thai kỳ",
        "precautions": [
            "QUAN TRỌNG: TUYỆT ĐỐI TRÁNH THAI - gây quái thai nghiêm trọng (Black Box Warning)",
            "Test thai kỳ trước khi bắt đầu điều trị",
            "Thải trừ rất chậm (có thể còn trong cơ thể đến 2 năm) - teriflunomide có half-life rất dài",
            "Nếu cần mang thai: phải làm washout với cholestyramine 8g x 3 lần/ngày x 11 ngày hoặc than hoạt tính 50g x 4 lần/ngày x 11 ngày",
            "Theo dõi men gan chặt chẽ (mỗi tháng trong 6 tháng đầu) - Black Box Warning",
            "Theo dõi huyết áp (tăng huyết áp phổ biến)",
            "Thận trọng khi dùng với methotrexate - tăng nguy cơ độc gan",
            "Thận trọng khi dùng với thuốc gây độc gan",
            "Ngừng thuốc nếu nhiễm trùng nặng"
        ],
        "pharmacokinetics": {
            "half_life": "Leflunomide: ~1 ngày; Teriflunomide (metabolite hoạt động): ~2 tuần (rất dài)",
            "onset": "Tác dụng trong 4-8 tuần (nhanh hơn nếu dùng loading dose)",
            "duration": "2-3 tuần sau khi ngừng (do teriflunomide có half-life dài)",
            "protein_binding": "Teriflunomide: >99%",
            "clearance": "Gan (chuyển hóa chủ yếu) và thận (thải trừ một phần). Thải trừ rất chậm do teriflunomide có half-life dài (~2 tuần).",
            "metabolism": "Chuyển hóa thành teriflunomide (A77 1726) - chất hoạt động. Teriflunomide có half-life rất dài (~2 tuần), có thể còn trong cơ thể đến 2 năm."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Gây quái thai nghiêm trọng: leflunomide gây quái thai nghiêm trọng ở người và động vật. CHỐNG CHỈ ĐỊNH trong thai kỳ. Phụ nữ có kế hoạch mang thai phải làm washout với cholestyramine trước. Độc gan nghiêm trọng: có thể gây viêm gan, suy gan, thậm chí tử vong. Theo dõi men gan chặt chẽ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Methotrexate",
                    "mechanism": "Cộng gộp độc tính gan và phổi",
                    "effect": "Tăng nguy cơ độc gan và viêm phổi kẽ",
                    "management": "Thận trọng. Theo dõi men gan chặt chẽ (mỗi tháng). Ngừng nếu có dấu hiệu độc gan hoặc viêm phổi kẽ."
                },
                {
                    "drug": "Thuốc gây độc gan (azathioprine, sulfasalazine, rượu, thuốc gây độc tế bào, retinoids)",
                    "mechanism": "Cộng gộp độc tính gan",
                    "effect": "Tăng nguy cơ độc gan",
                    "management": "Thận trọng. Tránh rượu. Theo dõi men gan chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Leflunomide có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu/ngừng leflunomide. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng chuyển hóa, giảm nồng độ teriflunomide",
                    "effect": "Giảm nồng độ teriflunomide, giảm hiệu quả",
                    "management": "Có thể cần tăng liều leflunomide. Theo dõi đáp ứng điều trị."
                }
            ],
            "minor": [
                {
                    "drug": "Cholestyramine, Than hoạt tính",
                    "mechanism": "Giảm hấp thu và tăng thải trừ teriflunomide",
                    "effect": "Giảm nồng độ teriflunomide (dùng để washout)",
                    "management": "Dùng để washout leflunomide: cholestyramine 8g x 3 lần/ngày x 11 ngày hoặc than hoạt tính 50g x 4 lần/ngày x 11 ngày."
                }
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Leflunomide gây quái thai nghiêm trọng ở người và động vật. Phụ nữ có kế hoạch mang thai phải làm washout với cholestyramine 8g x 3 lần/ngày x 11 ngày hoặc than hoạt tính 50g x 4 lần/ngày x 11 ngày trước khi mang thai.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Leflunomide và teriflunomide bài tiết vào sữa mẹ. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc."
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi men gan chặt chẽ",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH - không dùng",
            "notes": "Leflunomide chuyển hóa chủ yếu qua gan. Suy gan có thể tăng nguy cơ độc tính (viêm gan, suy gan). CHỐNG CHỈ ĐỊNH ở suy gan nặng. Theo dõi men gan chặt chẽ ở tất cả bệnh nhân."
        },
        "overdose_management": {
            "symptoms": [
                "Độc gan (tăng men gan, viêm gan, suy gan)",
                "Ức chế tủy xương (giảm bạch cầu, giảm tiểu cầu, thiếu máu)",
                "Tiêu chảy, buồn nôn, nôn",
                "Tăng huyết áp",
                "Nhiễm trùng"
            ],
            "antidote": "Cholestyramine hoặc than hoạt tính (để tăng thải trừ teriflunomide)",
            "treatment": [
                "Ngừng leflunomide ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Washout với cholestyramine 8g x 3 lần/ngày x 11 ngày hoặc than hoạt tính 50g x 4 lần/ngày x 11 ngày để tăng thải trừ teriflunomide",
                "Điều trị hỗ trợ: truyền dịch, theo dõi dấu hiệu sống",
                "Điều trị độc gan: hỗ trợ gan, theo dõi men gan",
                "Điều trị ức chế tủy xương: truyền máu, tiểu cầu, G-CSF nếu cần",
                "Theo dõi ít nhất 2-3 tuần (do teriflunomide có half-life dài)"
            ],
            "monitoring": "Dấu hiệu sống, men gan, công thức máu, chức năng thận, dấu hiệu nhiễm trùng"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Cholestyramine",
                    "dosage": "8g x 3 lần/ngày x 11 ngày",
                    "mechanism": "Tăng thải trừ teriflunomide qua đường tiêu hóa",
                    "notes": "Dùng để washout leflunomide khi cần mang thai hoặc trong trường hợp quá liều"
                },
                {
                    "agent": "Than hoạt tính",
                    "dosage": "50g x 4 lần/ngày x 11 ngày",
                    "mechanism": "Tăng thải trừ teriflunomide qua đường tiêu hóa",
                    "notes": "Dùng để washout leflunomide khi cần mang thai hoặc trong trường hợp quá liều"
                }
            ],
            "notes": "Cholestyramine hoặc than hoạt tính có thể được dùng để tăng thải trừ teriflunomide (washout)."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Uống 1 lần/ngày. Loading dose (tùy chọn): 100mg x 3 ngày đầu. Maintenance: 10-20mg/ngày (thường 20mg/ngày).",
                "notes": "Có thể uống với hoặc không có thức ăn. Loading dose (100mg x 3 ngày) giúp đạt nồng độ ổn định nhanh hơn nhưng tùy chọn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Arava (leflunomide)",
                "ACR Guidelines - Rheumatoid Arthritis",
                "UpToDate - Leflunomide: Drug Information",
                "EULAR Recommendations - Rheumatoid Arthritis"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "High - FDA approved, ACR guidelines, large RCTs"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "teratogenic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Pregnancy test (teratogenicity)", "Liver function (ALT, AST - Black Box Warning for hepatotoxicity, monthly for first 6 months)", "Blood pressure (hypertension)", "CBC (bone marrow suppression rare)", "Washout with cholestyramine if pregnancy needed (very slow elimination - up to 2 years)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Teratogenicity (severe birth defects)",
            "FDA Black Box Warning - Hepatotoxicity (severe)",
            "ACR Guidelines - Rheumatoid Arthritis",
            "ACR Guidelines - Psoriatic Arthritis"
        ],
    },
}
