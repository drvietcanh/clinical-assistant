"""
Immunosuppressants (Thuốc ức chế miễn dịch)
"""

IMMUNOSUPPRESSANTS_DRUGS = {
    "Tacrolimus": {
        "group": "Immunology - Calcineurin Inhibitor",
        "vietnamese_name": "Tacrolimus, FK506",
        "brand_names": {
            "common": ["Prograf", "Advagraf"],
            "vietnam": ["Prograf", "Tacrolimus", "Advagraf (tác dụng kéo dài)"]
        },
        "administration": ["PO", "IV", "Topical"],
        "indications": [
            "Dự phòng thải ghép (gan, thận, tim, phổi)",
            "Viêm da cơ địa (Topical - Protopic)",
            "Bệnh tự miễn kháng trị (Lupus, Viêm khớp dạng thấp - off-label)"
        ],
        "dosage": {
            "transplant_maintenance": "0.03-0.05 mg/kg/ngày chia 2 lần (Prograf) hoặc 1 lần (Advagraf). Điều chỉnh theo nồng độ đáy (Trough level).",
            "atopic_dermatitis": "Bôi 0.03-0.1% x 1-2 lần/ngày.",
            "notes": "Khoảng điều trị hẹp (Narrow therapeutic index). Cần theo dõi nồng độ thuốc trong máu (TDM) nghiêm ngặt."
        },
        "side_effects": [
            "Độc tính thận (Nephrotoxicity) - Phổ biến, phụ thuộc liều",
            "Độc tính thần kinh (Run tay, co giật, đau đầu)",
            "Tăng đường huyết (Đái tháo đường sau ghép - NODAT)",
            "Tăng huyết áp",
            "Tăng Kali máu"
        ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Macrolides, Azole antifungals, Nước bưởi) -> Tăng nồng độ Tacrolimus mạnh -> Ngộ độc.",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin) -> Giảm nồng độ Tacrolimus -> Thải ghép."
        ],
        "mechanism_of_action": "Tacrolimus là calcineurin inhibitor. Gắn với FKBP-12 trong tế bào T, phức hợp này ức chế calcineurin phosphatase, ngăn khử phosphoryl hóa NFAT và giảm sản xuất IL-2 cùng các cytokine khác, từ đó ức chế hoạt hóa và tăng sinh tế bào T.",
        "monitoring": ["Nồng độ Tacrolimus máu (Trough)", "Chức năng thận", "Đường huyết", "Kali máu"],
        "precautions": [
            "Khoảng điều trị hẹp, bắt buộc theo dõi TDM.",
            "Nguy cơ độc tính thận và thần kinh, cần theo dõi creatinine và triệu chứng thần kinh.",
            "Tăng nguy cơ nhiễm trùng và ung thư, cần giáo dục bệnh nhân nhận biết dấu hiệu.",
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 12 giờ (biến thiên rộng theo cá thể).",
            "onset": "Vài ngày đến vài tuần để đạt hiệu quả tối ưu.",
            "duration": "24 giờ với dạng dùng 2 lần/ngày hoặc 1 lần/ngày (tác dụng phụ thuộc nồng độ đáy).",
            "protein_binding": "≈ 99%.",
            "metabolism": "Chuyển hóa mạnh qua gan bởi CYP3A4.",
            "clearance": "Chủ yếu qua mật/phân; thải trừ qua thận rất ít dưới dạng không đổi."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm và ánh sáng. Không để đông lạnh dung dịch truyền.",
        "black_box_warnings": "Nguy cơ độc tính thận và thần kinh nặng, tăng nguy cơ nhiễm trùng nghiêm trọng và ác tính (lymphoma, các ung thư khác). Chỉ sử dụng bởi bác sĩ có kinh nghiệm trong ghép tạng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Azole antifungals, Macrolides, Nước bưởi",
                    "mechanism": "Ức chế CYP3A4 → giảm chuyển hóa tacrolimus.",
                    "effect": "Tăng mạnh nồng độ tacrolimus, nguy cơ độc tính thận/thần kinh.",
                    "management": "Giảm liều tacrolimus và theo dõi TDM sát hoặc tránh phối hợp nếu có thể."
                },
                {
                    "drug": "Rifampin, Carbamazepine, Phenytoin",
                    "mechanism": "Cảm ứng CYP3A4 → tăng chuyển hóa tacrolimus.",
                    "effect": "Giảm nồng độ tacrolimus, nguy cơ thải ghép.",
                    "management": "Tránh phối hợp nếu có thể; nếu bắt buộc, tăng liều tacrolimus theo TDM."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn với tacrolimus hoặc bất kỳ tá dược nào."
            ],
            "tương_đối": [
                "Suy thận nặng trước ghép.",
                "Suy gan trung bình–nặng.",
                "Nhiễm trùng không kiểm soát.",
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ khi lợi ích vượt nguy cơ, thường trong bệnh nhân ghép tạng; cần theo dõi sát mẹ và thai.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Bài tiết một phần vào sữa; cân nhắc lợi ích–nguy cơ và theo dõi trẻ.",
                "recommendation": "Dùng được nếu cần thiết, ưu tiên liều thấp nhất có hiệu quả, theo dõi tác dụng phụ ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Cân nhắc giảm liều và theo dõi TDM.",
            "moderate": "Giảm liều rõ rệt; theo dõi TDM sát.",
            "severe": "Thận trọng tối đa; chỉ dùng khi không có lựa chọn khác, theo dõi sát.",
            "notes": "Tacrolimus chuyển hóa gần như hoàn toàn qua gan (CYP3A4); suy gan làm tăng đáng kể nồng độ thuốc."
        },
        "renal_adjustment": {
            "normal": "Không chỉnh liều theo eGFR nhưng theo dõi sát độc tính thận.",
            "30_60": "Thận trọng; cân nhắc giảm mục tiêu nồng độ đáy nếu độc tính thận.",
            "under_30": "Thận trọng cao; giảm liều và cân nhắc chuyển phác đồ nếu độc tính thận kéo dài.",
            "dialysis": "Tacrolimus không loại đáng kể qua lọc máu; chỉnh liều theo TDM và lâm sàng.",
            "notes": "Độc tính thận chủ yếu do cơ chế co mạch thận hơn là tích lũy do giảm thải trừ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng creatinine, thiểu niệu.",
                "Run, co giật, lơ mơ.",
                "Tăng huyết áp, loạn nhịp.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng hoặc giảm mạnh liều tacrolimus.",
                "Điều trị hỗ trợ (hạ áp, kiểm soát co giật, bù dịch thận trọng).",
                "Cân nhắc dùng than hoạt nếu uống quá liều mới xảy ra.",
                "Theo dõi nồng độ thuốc, chức năng thận, điện giải."
            ],
            "monitoring": "Nồng độ tacrolimus máu, creatinine/eGFR, huyết áp, điện giải, tình trạng thần kinh."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; điều trị chủ yếu là giảm/hủy liều và hỗ trợ."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống thống nhất trước hoặc sau ăn; tránh thay đổi kiểu dùng đột ngột.",
                "timing": "Uống cùng thời điểm mỗi ngày (ví dụ sáng–tối cho dạng chia liều)."
            },
            "iv": {
                "notes": "Chỉ dùng khi không uống được; chuyển sang đường uống sớm nhất có thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tacrolimus (Prograf, Advagraf)",
                "UpToDate - Tacrolimus: Drug information",
                "KDIGO Guidelines - Kidney Transplant",
                "AST Guidelines - Solid Organ Transplant"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"renal": "Black Box Warning - Nephrotoxicity (may be irreversible)", "neurological": "Black Box Warning - Neurotoxicity (seizures, encephalopathy)", "metabolic": "Black Box Warning - Post-transplant diabetes mellitus (NODAT)", "oncologic": "Black Box Warning - Increased risk of infection and malignancy", "cardiovascular": "Hypertension, hyperkalemia"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["TDM required (trough levels - Black Box Warning, narrow therapeutic index)", "Renal function (creatinine, eGFR - Black Box Warning for nephrotoxicity)", "Neurological status (seizures, encephalopathy - Black Box Warning)", "Blood glucose (Black Box Warning - post-transplant diabetes)", "Blood pressure (hypertension)", "Serum potassium (hyperkalemia)", "Infection signs (Black Box Warning - increased risk)", "Malignancy screening (Black Box Warning - increased risk)", "CYP3A4 interactions (grapefruit juice, macrolides, azole antifungals)"],
            "look_alike_sound_alike": ["Tacrolimus", "Pimecrolimus"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Nephrotoxicity (may be irreversible)",
            "FDA Black Box Warning - Neurotoxicity (seizures, encephalopathy)",
            "FDA Black Box Warning - Post-transplant Diabetes Mellitus",
            "FDA Black Box Warning - Increased Risk of Infection and Malignancy",
            "KDIGO Guidelines - Kidney Transplant",
            "AST Guidelines - Solid Organ Transplant",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Cyclosporine": {
        "group": "Immunology - Calcineurin Inhibitor",
        "vietnamese_name": "Cyclosporine, Cyclosporin A",
        "brand_names": {
            "common": ["Neoral", "Sandimmune"],
            "vietnam": ["Neoral (vi nhũ tương)", "Sandimmun"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Dự phòng thải ghép tạng",
            "Viêm khớp dạng thấp",
            "Vảy nến nặng",
            "Hội chứng thận hư"
        ],
        "dosage": {
            "transplant": "Khởi đầu 8-12 mg/kg/ngày, giảm dần. Điều chỉnh theo nồng độ đáy.",
            "ra_psoriasis": "2.5-4 mg/kg/ngày chia 2 lần.",
            "notes": "Dạng Neoral (Modified) và Sandimmune (Non-modified) KHÔNG tương đương nhau."
        },
        "side_effects": [
            "Độc tính thận (Nephrotoxicity)",
            "Tăng huyết áp",
            "Phì đại lợi (Gingival hyperplasia)",
            "Rậm lông (Hirsutism)",
            "Tăng lipid máu"
        ],
        "features": {
             "comparison_tacrolimus": "Cyclosporine gây phì đại lợi và rậm lông, Tacrolimus gây rụng tóc và đái tháo đường nhiều hơn."
        },
        "mechanism_of_action": "Cyclosporine là calcineurin inhibitor. Gắn với cyclophilin trong tế bào T, phức hợp này ức chế calcineurin phosphatase, làm giảm hoạt hóa NFAT, giảm sản xuất IL-2 và các cytokine khác, ức chế hoạt hóa và tăng sinh tế bào T.",
        "monitoring": ["Nồng độ Cyclosporine máu", "Chức năng thận", "Huyết áp"],
        "black_box_warnings": "Nephrotoxicity có thể không hồi phục, tăng nguy cơ nhiễm trùng và ác tính, tăng huyết áp. Chỉ dùng bởi bác sĩ có kinh nghiệm trong ghép tạng và bệnh tự miễn nặng.",
        "precautions": [
            "Khoảng điều trị hẹp, bắt buộc theo dõi TDM.",
            "Nguy cơ độc tính thận và tăng huyết áp cao, cần theo dõi creatinine và huyết áp.",
            "Có nhiều tương tác qua CYP3A4 và P-gp; cần rà soát thuốc kỹ.",
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 8–20 giờ (biến thiên rộng).",
            "onset": "Vài ngày đến vài tuần.",
            "duration": "24 giờ (dùng chia 2 lần/ngày).",
            "protein_binding": "≈ 90%.",
            "metabolism": "Chuyển hóa mạnh qua gan (CYP3A4) và P-gp.",
            "clearance": "Chủ yếu qua mật/phân; thải trừ qua thận rất ít."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn với cyclosporine hoặc tá dược.",
            ],
            "tương_đối": [
                "Suy thận nặng chưa ổn định.",
                "Tăng huyết áp không kiểm soát.",
                "Tiền sử ác tính chưa điều trị ổn định.",
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ ở bệnh nhân ghép tạng khi lợi ích vượt nguy cơ; cần theo dõi sát mẹ và thai.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Bài tiết vào sữa ở mức thấp–trung bình; cần theo dõi chức năng thận và huyết áp ở trẻ.",
                "recommendation": "Dùng được nếu cần thiết, sau khi cân nhắc kỹ lợi ích–nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Giảm liều theo TDM.",
            "moderate": "Giảm liều đáng kể, theo dõi TDM sát.",
            "severe": "Thận trọng tối đa hoặc tránh dùng nếu có lựa chọn khác.",
            "notes": "Chuyển hóa mạnh qua gan; suy gan làm tăng nồng độ và độc tính."
        },
        "renal_adjustment": {
            "normal": "Không chỉnh liều theo eGFR, nhưng theo dõi sát độc tính thận.",
            "30_60": "Giảm liều nếu creatinine tăng kéo dài.",
            "under_30": "Thận trọng cao; cân nhắc phác đồ khác nếu độc tính thận tiến triển.",
            "dialysis": "Không loại đáng kể qua lọc máu; chỉnh liều theo TDM và lâm sàng.",
            "notes": "Độc tính thận chủ yếu do co mạch thận hơn là giảm thải trừ."
        },
        "overdose_management": {
            "symptoms": [
                "Suy thận cấp, tăng creatinine.",
                "Tăng huyết áp nặng.",
                "Run, nhức đầu, rối loạn thần kinh.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng hoặc giảm mạnh liều cyclosporine.",
                "Điều trị hỗ trợ: kiểm soát huyết áp, bù dịch thận trọng.",
                "Cân nhắc than hoạt nếu uống quá liều mới xảy ra.",
                "Theo dõi TDM, chức năng thận, huyết áp."
            ],
            "monitoring": "Nồng độ cyclosporine, creatinine/eGFR, huyết áp, triệu chứng thần kinh."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu; xử trí chủ yếu bằng giảm/hủy liều và hỗ trợ."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống nhất quán trước hoặc sau ăn; tránh thay đổi kiểu dùng vì ảnh hưởng hấp thu.",
                "timing": "Chia 2 lần/ngày, uống cùng thời điểm mỗi ngày."
            },
            "iv": {
                "notes": "Chỉ dùng khi không uống được; chuyển sang đường uống sớm nhất có thể."
            }
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "bleeding_risk": False,
            "organ_toxicity": ["renal", "cardiovascular", "oncologic"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["TDM required (trough levels - narrow therapeutic index)", "Renal function (creatinine, eGFR - Black Box Warning for nephrotoxicity)", "Blood pressure (hypertension)", "Lipid profile (hyperlipidemia)", "Infection signs (Black Box Warning - increased risk)", "Malignancy screening (Black Box Warning - increased risk)", "CYP3A4 interactions (grapefruit juice, macrolides, azole antifungals)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Nephrotoxicity (may be irreversible)",
            "FDA Black Box Warning - Increased Risk of Infection and Malignancy",
            "KDIGO Guidelines - Kidney Transplant",
            "AST Guidelines - Solid Organ Transplant",
            "WHO Essential Medicines List"
        ]
    },

    "Mycophenolate": {
        "group": "Immunology - Antimetabolite",

        "pregnancy": "D - Có bằng chứng về nguy cơ dị tật bẩm sinh. Chống chỉ định trong thai kỳ",
        "vietnamese_name": "Mycophenolate Mofetil (MMF), CellCept",
        "brand_names": {
            "common": ["CellCept", "Myfortic"],
            "vietnam": ["CellCept 250/500mg", "Myfortic (Mycophenolate Sodium)"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Dự phòng thải ghép (kết hợp Tacrolimus/Cyclosporine + Corticoid)",
            "Viêm thận Lupus (Lupus Nephritis)"
        ],
        "contraindications": [
            "Phụ nữ mang thai (Gây quái thai nghiêm trọng - REMS program)"
        ],
        "dosage": {
            "transplant_adult": "1000 mg (CellCept) hoặc 720 mg (Myfortic) x 2 lần/ngày.",
            "lupus_nephritis": "500-1500 mg x 2 lần/ngày.",
            "notes": "Myfortic là dạng bao tan trong ruột, giảm kích ứng dạ dày hơn CellCept."
        },
        "side_effects": [
            "Rối loạn tiêu hóa (Tiêu chảy, nôn) - Rất phổ biến, giới hạn liều dùng",
            "Suy tủy (Giảm bạch cầu, thiếu máu)",
            "Tăng nguy cơ nhiễm trùng (CMV, BK virus)"
        ],
        "mechanism_of_action": "Ức chế IMPDH, ức chế tổng hợp Purine de novo, ức chế chọn lọc tăng sinh tế bào Lympho T và B.",
        "monitoring": ["Công thức máu (CBC)", "Dấu hiệu nhiễm trùng"],
        "precautions": [
            "Teratogenic mạnh; bắt buộc chương trình REMS và tránh thai hiệu quả.",
            "Tăng nguy cơ nhiễm trùng nặng (CMV, BK virus).",
            "Rối loạn tiêu hóa giới hạn liều, cần theo dõi mất nước.",
        ],
        "pharmacokinetics": {
            "half_life": "≈ 16–18 giờ (MMF).",
            "onset": "Vài ngày đến vài tuần.",
            "duration": "24 giờ (dùng chia 2 lần/ngày).",
            "protein_binding": "≈ 97%.",
            "metabolism": "Chuyển hóa ở gan thành MPA và các glucuronid.",
            "clearance": "Thải trừ chủ yếu qua mật/phân, một phần qua thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ dị tật bẩm sinh và sẩy thai (teratogenic mạnh), nguy cơ nhiễm trùng nghiêm trọng và ác tính, suy tủy (giảm bạch cầu, thiếu máu, giảm tiểu cầu).",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Phụ nữ mang thai hoặc đang chuẩn bị mang thai.",
                "Quá mẫn với mycophenolate hoặc tá dược."
            ],
            "tương_đối": [
                "Suy tủy nặng (bạch cầu, tiểu cầu thấp).",
                "Nhiễm trùng nặng đang tiến triển.",
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D/X (ở một số hướng dẫn, xem là chống chỉ định trong thai kỳ)",
            "pregnancy_details": "Gây dị tật bẩm sinh nghiêm trọng và sẩy thai; chống chỉ định trừ khi không có lựa chọn khác và lợi ích vượt xa nguy cơ.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Bài tiết vào sữa; nguy cơ ức chế miễn dịch và suy tủy ở trẻ.",
                "recommendation": "Không nên cho con bú khi đang dùng mycophenolate."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều đáng kể, theo dõi lâm sàng.",
            "moderate": "Thận trọng; theo dõi độc tính và cân nhắc giảm liều.",
            "severe": "Thận trọng cao; cân nhắc liệu pháp thay thế.",
            "notes": "Chuyển hóa chủ yếu qua gan; dữ liệu cụ thể hạn chế, điều chỉnh chủ yếu dựa trên lâm sàng và độc tính."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều ở ghép tạng có chức năng thận ổn định.",
            "30_60": "Thận trọng; theo dõi MPA nếu có, chức năng thận và tác dụng phụ.",
            "under_30": "Thận trọng; cân nhắc giảm liều nếu tích lũy hoặc độc tính tăng.",
            "dialysis": "Không loại đáng kể qua lọc máu; chỉnh liều theo lâm sàng.",
            "notes": "Mycophenolate và các chất chuyển hóa được thải trừ một phần qua thận; suy thận có thể làm tăng phơi nhiễm."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng, nôn, mất nước.",
                "Nhiễm trùng nặng, sốt cao.",
                "Giảm bạch cầu, giảm tiểu cầu rõ."
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng hoặc giảm liều mycophenolate.",
                "Bù dịch và điện giải.",
                "Điều trị nhiễm trùng theo kháng sinh đồ.",
                "Hỗ trợ huyết học (truyền máu, G-CSF nếu cần)."
            ],
            "monitoring": "CBC, chức năng thận, điện giải, dấu hiệu nhiễm trùng và mất nước."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc; xử trí bằng giảm liều/ngừng thuốc và hỗ trợ tích cực."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn; ưu tiên uống nhất quán để giảm dao động hấp thu.",
                "timing": "Chia 2 lần/ngày; nuốt nguyên viên, không nghiền bẻ (đặc biệt với Myfortic)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Mycophenolate (CellCept, Myfortic)",
                "UpToDate - Mycophenolate: Drug information",
                "KDIGO Guidelines - Kidney Transplant",
                "ACR Guidelines - Lupus Nephritis"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"teratogenic": "Black Box Warning - Teratogenicity (severe birth defects, REMS program)", "hematologic": "Black Box Warning - Myelosuppression (neutropenia, anemia, thrombocytopenia)", "oncologic": "Black Box Warning - Increased risk of infection and malignancy", "gastrointestinal": "Severe diarrhea, nausea, vomiting (dose-limiting)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Pregnancy test (REMS program, teratogenicity)", "CBC (Black Box Warning - myelosuppression)", "Infection signs (Black Box Warning - increased risk, CMV, BK virus)", "Malignancy screening (Black Box Warning - increased risk)", "GI symptoms (severe diarrhea, nausea, vomiting - dose-limiting)"],
            "look_alike_sound_alike": ["Mycophenolate", "Mycophenolate mofetil"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Teratogenicity (severe birth defects, REMS program)",
            "FDA Black Box Warning - Myelosuppression (neutropenia, anemia, thrombocytopenia)",
            "FDA Black Box Warning - Increased Risk of Infection and Malignancy",
            "KDIGO Guidelines - Kidney Transplant",
            "ACR Guidelines - Lupus Nephritis",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Sirolimus": {
        "group": "Immunology - mTOR Inhibitor",
        "vietnamese_name": "Sirolimus, Rapamycin",
        "brand_names": {
            "common": ["Rapamune"],
            "vietnam": ["Rapamune", "Sirolimus"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Dự phòng thải ghép thận (kết hợp cyclosporine hoặc thay thế)",
            "Lymphangioleiomyomatosis (LAM)",
            "Bệnh tự miễn kháng trị (off-label)"
        ],
        "contraindications": [
            "Dị ứng sirolimus",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "transplant_loading": "6mg PO x 1 lần, sau đó 2mg/ngày",
            "transplant_maintenance": "2-5mg/ngày PO, điều chỉnh theo nồng độ đáy (trough level 4-12 ng/ml)",
            "notes": "Khoảng điều trị hẹp (Narrow therapeutic index). Cần theo dõi nồng độ thuốc trong máu (TDM) nghiêm ngặt. Uống cùng thời điểm mỗi ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Tăng lipid máu (cholesterol, triglyceride) - Phổ biến",
            "Tăng huyết áp",
            "Giảm tiểu cầu, giảm bạch cầu",
            "Viêm phổi (pneumonitis) - Hiếm nhưng nghiêm trọng",
            "Phù ngoại biên",
            "Loét miệng (stomatitis)",
            "Tăng nguy cơ nhiễm trùng và ung thư",
            "Độc tính thận (khi dùng với cyclosporine)",
            "Rối loạn vết thương (wound healing)"
        ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Ketoconazole, Voriconazole, Clarithromycin, Diltiazem) -> Tăng nồng độ Sirolimus mạnh -> Ngộ độc",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin) -> Giảm nồng độ Sirolimus -> Thải ghép",
            "Cyclosporine: Tăng độc tính thận (tránh dùng cùng nếu có thể)",
            "Grapefruit juice: Tăng nồng độ Sirolimus"
        ],
        "pregnancy": "C - D (với thải ghép)",
        "mechanism_of_action": "Sirolimus là mTOR (mammalian target of rapamycin) inhibitor, ức chế tín hiệu mTOR, ngăn chặn sự tăng sinh và hoạt hóa tế bào T và B. Khác với calcineurin inhibitors (tacrolimus, cyclosporine), sirolimus không gây độc tính thận trực tiếp nhưng có thể tăng độc tính thận khi dùng với cyclosporine. Sirolimus có tác dụng chống tăng sinh mạnh, ức chế sự phát triển của tế bào ung thư và tế bào miễn dịch.",
        "monitoring": [
            "Nồng độ Sirolimus máu (Trough level) - Mục tiêu 4-12 ng/ml",
            "Chức năng thận (creatinine, eGFR)",
            "Lipid máu (cholesterol, triglyceride) - Tăng lipid phổ biến",
            "Công thức máu (CBC) - Giảm tiểu cầu, bạch cầu",
            "Dấu hiệu viêm phổi (ho, khó thở, sốt) - Pneumonitis hiếm nhưng nghiêm trọng",
            "Dấu hiệu nhiễm trùng",
            "Dấu hiệu ung thư (sàng lọc định kỳ)",
            "Huyết áp"
        ],
        "precautions": [
            "Khoảng điều trị hẹp - Cần theo dõi nồng độ máu nghiêm ngặt (TDM)",
            "Uống cùng thời điểm mỗi ngày (quan trọng cho TDM)",
            "Tránh dùng với cyclosporine nếu có thể (tăng độc tính thận)",
            "Nhiều tương tác thuốc do chuyển hóa qua CYP3A4",
            "Tăng lipid máu phổ biến - Cần điều trị statin nếu cần",
            "Viêm phổi (pneumonitis) - Ngừng ngay nếu có dấu hiệu",
            "Rối loạn vết thương - Thận trọng sau phẫu thuật",
            "Tránh dùng trong thai kỳ (gây dị tật thai nhi)"
        ],
        "pharmacokinetics": {
            "half_life": "57-63 giờ (rất dài)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "24 giờ (uống 1 lần/ngày)",
            "protein_binding": "92%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần. Hấp thu tốt qua đường uống nhưng bị ảnh hưởng bởi thức ăn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng solution: bảo quản trong tủ lạnh (2-8°C) sau khi mở.",
        "black_box_warnings": "Tăng nguy cơ nhiễm trùng và ung thư. Có thể gây viêm phổi (pneumonitis) nghiêm trọng. Tăng lipid máu phổ biến. Rối loạn vết thương sau phẫu thuật. Chống chỉ định trong thai kỳ.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sirolimus (Rapamune)",
                "UpToDate - Sirolimus: Drug information",
                "KDIGO Guidelines - Kidney Transplant",
                "AST Guidelines - Solid Organ Transplant"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "High (thrombocytopenia)",
            "organ_toxicity": {"pulmonary": "Pneumonitis (rare but serious)", "hematologic": "Bone marrow suppression (thrombocytopenia, leukopenia)", "metabolic": "Hyperlipidemia (common)", "oncologic": "Black Box Warning - Increased risk of infection and malignancy", "renal": "Nephrotoxicity (when used with cyclosporine)", "wound_healing": "Impaired wound healing"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["TDM required (trough levels 4-12 ng/ml - Black Box Warning, narrow therapeutic index)", "Pulmonary symptoms (pneumonitis signs - Black Box Warning, rare but serious)", "CBC (Black Box Warning - bone marrow suppression, thrombocytopenia, leukopenia)", "Lipid profile (hyperlipidemia - common)", "Renal function (nephrotoxicity risk, especially with cyclosporine)", "Infection signs (Black Box Warning - increased risk)", "Malignancy screening (Black Box Warning - increased risk)", "Wound healing (impaired wound healing risk)", "CYP3A4 interactions (grapefruit juice, macrolides, azole antifungals)"],
            "look_alike_sound_alike": ["Sirolimus", "Tacrolimus"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Risk of Infection and Malignancy",
            "FDA Black Box Warning - Pneumonitis (rare but serious)",
            "KDIGO Guidelines - Kidney Transplant",
            "AST Guidelines - Solid Organ Transplant",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Everolimus": {
        "group": "Immunology - mTOR Inhibitor",
        "vietnamese_name": "Everolimus, Afinitor",
        "brand_names": {
            "common": ["Afinitor", "Zortress"],
            "vietnam": ["Afinitor", "Everolimus", "Zortress"]
        },
        "administration": ["PO"],
        "indications": [
            "Dự phòng thải ghép thận (Zortress)",
            "Ung thư thận tiến triển (Afinitor)",
            "Ung thư vú hormone receptor dương tính (Afinitor)",
            "Ung thư tụy thần kinh nội tiết (Afinitor)",
            "U xơ cứng củ (Tuberous Sclerosis Complex - Afinitor)"
        ],
        "contraindications": [
            "Dị ứng everolimus",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "transplant_maintenance": "0.75mg PO x 2 lần/ngày (Zortress), điều chỉnh theo nồng độ đáy (trough level 3-8 ng/ml)",
            "oncology": "10mg PO x 1 lần/ngày (Afinitor)",
            "notes": "Khoảng điều trị hẹp (Narrow therapeutic index). Cần theo dõi nồng độ thuốc trong máu (TDM) nghiêm ngặt. Uống cùng thời điểm mỗi ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều"
        },
        "side_effects": [
            "Tăng lipid máu (cholesterol, triglyceride) - Phổ biến",
            "Tăng đường huyết",
            "Giảm tiểu cầu, giảm bạch cầu",
            "Viêm phổi (pneumonitis) - Hiếm nhưng nghiêm trọng",
            "Loét miệng (stomatitis)",
            "Phát ban",
            "Tăng nguy cơ nhiễm trùng và ung thư",
            "Rối loạn vết thương (wound healing)"
        ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Ketoconazole, Voriconazole, Clarithromycin, Diltiazem) -> Tăng nồng độ Everolimus mạnh -> Ngộ độc",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin) -> Giảm nồng độ Everolimus -> Thải ghép hoặc giảm hiệu quả",
            "Grapefruit juice: Tăng nồng độ Everolimus"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Everolimus là mTOR (mammalian target of rapamycin) inhibitor, tương tự sirolimus nhưng có thời gian bán thải ngắn hơn. Ức chế tín hiệu mTOR, ngăn chặn sự tăng sinh và hoạt hóa tế bào T và B. Trong ung thư, everolimus ức chế sự phát triển của tế bào ung thư và tạo mạch máu. Everolimus được sử dụng cả trong ghép tạng (Zortress) và điều trị ung thư (Afinitor).",
        "monitoring": [
            "Nồng độ Everolimus máu (Trough level) - Mục tiêu 3-8 ng/ml (transplant)",
            "Chức năng thận (creatinine, eGFR)",
            "Lipid máu (cholesterol, triglyceride) - Tăng lipid phổ biến",
            "Đường huyết - Tăng đường huyết",
            "Công thức máu (CBC) - Giảm tiểu cầu, bạch cầu",
            "Dấu hiệu viêm phổi (ho, khó thở, sốt) - Pneumonitis hiếm nhưng nghiêm trọng",
            "Dấu hiệu nhiễm trùng",
            "Dấu hiệu ung thư (sàng lọc định kỳ)",
            "Huyết áp"
        ],
        "precautions": [
            "Khoảng điều trị hẹp - Cần theo dõi nồng độ máu nghiêm ngặt (TDM)",
            "Uống cùng thời điểm mỗi ngày (quan trọng cho TDM)",
            "Nhiều tương tác thuốc do chuyển hóa qua CYP3A4",
            "Tăng lipid máu phổ biến - Cần điều trị statin nếu cần",
            "Tăng đường huyết - Theo dõi và điều trị nếu cần",
            "Viêm phổi (pneumonitis) - Ngừng ngay nếu có dấu hiệu",
            "Rối loạn vết thương - Thận trọng sau phẫu thuật",
            "Tránh dùng trong thai kỳ (gây dị tật thai nhi - Category D)"
        ],
        "pharmacokinetics": {
            "half_life": "30 giờ (ngắn hơn sirolimus)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "12 giờ (uống 2 lần/ngày cho transplant)",
            "protein_binding": "74%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần. Hấp thu tốt qua đường uống."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Tăng nguy cơ nhiễm trùng và ung thư. Có thể gây viêm phổi (pneumonitis) nghiêm trọng. Tăng lipid máu và tăng đường huyết phổ biến. Rối loạn vết thương sau phẫu thuật. Chống chỉ định trong thai kỳ (Category D).",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Everolimus (Afinitor, Zortress)",
                "UpToDate - Everolimus: Drug information",
                "KDIGO Guidelines - Kidney Transplant",
                "NCCN Guidelines - Renal Cell Carcinoma",
                "NCCN Guidelines - Breast Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "High (thrombocytopenia)",
            "organ_toxicity": {"pulmonary": "Pneumonitis (rare but serious)", "hematologic": "Bone marrow suppression (thrombocytopenia, leukopenia)", "metabolic": "Hyperlipidemia (common), hyperglycemia (common)", "oncologic": "Black Box Warning - Increased risk of infection and malignancy", "wound_healing": "Impaired wound healing"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["TDM required (trough levels 3-8 ng/ml - Black Box Warning, narrow therapeutic index)", "Pulmonary symptoms (pneumonitis signs - Black Box Warning, rare but serious)", "CBC (Black Box Warning - bone marrow suppression, thrombocytopenia, leukopenia)", "Lipid profile (hyperlipidemia - common)", "Blood glucose (hyperglycemia - common)", "Renal function (nephrotoxicity risk)", "Infection signs (Black Box Warning - increased risk)", "Malignancy screening (Black Box Warning - increased risk)", "Wound healing (impaired wound healing risk)", "CYP3A4 interactions (grapefruit juice, macrolides, azole antifungals)"],
            "look_alike_sound_alike": ["Everolimus", "Sirolimus"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Risk of Infection and Malignancy",
            "FDA Black Box Warning - Pneumonitis (rare but serious)",
            "KDIGO Guidelines - Kidney Transplant",
            "NCCN Guidelines - Renal Cell Carcinoma",
            "NCCN Guidelines - Breast Cancer",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    }
}
