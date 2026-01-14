"""
Urology Drugs - Bph Alpha Blockers
"""
from typing import Dict, Any


BPH_ALPHA_BLOCKERS_DRUGS: Dict[str, Dict[str, Any]] = {
        "Alfuzosin": {
            "group": "Urology - Alpha-1 Adrenergic Blocker (BPH)",
            "vietnamese_name": "Alfuzosin, Uroxatral",
            "administration": ["PO"],
            "indications": [
                "Phì đại tuyến tiền liệt lành tính (BPH) - giảm triệu chứng",
                "Rối loạn tiểu tiện do BPH (tiểu khó, tiểu yếu, tiểu đêm, tiểu gấp)"
            ],
            "contraindications": [
                "Dị ứng alfuzosin",
                "Hạ huyết áp nặng",
                "Suy gan nặng",
                "Dùng với các thuốc ức chế CYP3A4 mạnh (ketoconazole, itraconazole, ritonavir)"
            ],
            "dosage": {
                "adult_bph": "10mg PO x 1 lần/ngày (sau bữa ăn)",
                "notes": "Uống sau bữa ăn để giảm nguy cơ hạ huyết áp. Alfuzosin là alpha-1 blocker không chọn lọc, ít chọn lọc hơn tamsulosin."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Không cần điều chỉnh đáng kể"
            },
            "side_effects": [
                "Hạ huyết áp tư thế (orthostatic hypotension) - phổ biến",
                "Chóng mặt",
                "Ngất (syncope) - hiếm nhưng nguy hiểm",
                "Rối loạn xuất tinh (retrograde ejaculation) - phổ biến",
                "Nhức đầu",
                "Mệt mỏi",
                "Nghẹt mũi"
            ],
            "interactions": [
                "Thuốc hạ huyết áp: tăng nguy cơ hạ huyết áp",
                "PDE-5 inhibitors (sildenafil, tadalafil): tăng nguy cơ hạ huyết áp",
                "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir): tăng nồng độ alfuzosin - CHỐNG CHỈ ĐỊNH"
            ],
        "pregnancy": "Không áp dụng (chỉ dùng cho nam giới)",
            "mechanism_of_action": "Alfuzosin là alpha-1 adrenergic blocker không chọn lọc. Ức chế alpha-1 receptors trên cơ trơn tuyến tiền liệt và cổ bàng quang, gây giãn cơ, giảm sức cản đường tiểu, và cải thiện dòng nước tiểu. Khác với tamsulosin (chọn lọc alpha-1A), alfuzosin ít chọn lọc hơn, có thể ảnh hưởng nhiều hơn đến alpha-1B receptors ở mạch máu, do đó có thể gây hạ huyết áp nhiều hơn. ĐẶC ĐIỂM: (1) Không chọn lọc (ít chọn lọc hơn tamsulosin), (2) Cải thiện triệu chứng BPH nhanh (1-2 tuần), (3) Nguy cơ hạ huyết áp tư thế và rối loạn xuất tinh, (4) Uống sau bữa ăn để giảm nguy cơ hạ huyết áp, (5) CHỐNG CHỈ ĐỊNH với CYP3A4 inhibitors mạnh.",
            "monitoring": [
                "Huyết áp (đặc biệt hạ huyết áp tư thế) - QUAN TRỌNG",
                "Triệu chứng BPH (tiểu khó, tiểu yếu, tiểu đêm, tiểu gấp)",
                "Dấu hiệu ngất (syncope)",
                "Dấu hiệu rối loạn xuất tinh (retrograde ejaculation)"
            ],
            "precautions": [
                "Hạ huyết áp tư thế - phổ biến, cần cảnh báo bệnh nhân",
                "Nguy cơ ngất (syncope) - đặc biệt khi đứng dậy đột ngột",
                "Uống sau bữa ăn để giảm nguy cơ hạ huyết áp",
                "CHỐNG CHỈ ĐỊNH với CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, ritonavir)",
                "Thận trọng ở bệnh nhân hạ huyết áp nền",
                "Thận trọng khi dùng với thuốc hạ huyết áp khác",
                "Thận trọng khi dùng với PDE-5 inhibitors (sildenafil, tadalafil)",
                "Rối loạn xuất tinh - tư vấn bệnh nhân trước khi dùng"
            ],
            "pharmacokinetics": {
                "half_life": "10 giờ",
                "onset": "1-2 tuần",
                "duration": "Dài (cần dùng liên tục)",
                "protein_binding": "82-90%",
                "metabolism": "Gan (CYP3A4)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ alfuzosin",
                        "effect": "Tăng nồng độ alfuzosin đáng kể, tăng nguy cơ hạ huyết áp nặng, ngất",
                        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. KHÔNG được dùng đồng thời."
                    },
                    {
                        "drug": "PDE-5 Inhibitors (Sildenafil, Tadalafil, Vardenafil)",
                        "mechanism": "Cả hai đều gây giãn mạch, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất, đột quỵ, nhồi máu cơ tim",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, dùng liều thấp nhất và theo dõi huyết áp sát. Cách xa ít nhất 4-6 giờ."
                    },
                    {
                        "drug": "Thuốc hạ huyết áp (ACE inhibitors, ARBs, Beta-blockers, Diuretics)",
                        "mechanism": "Tác dụng hạ huyết áp cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất",
                        "management": "Thận trọng. Theo dõi huyết áp sát. Có thể cần giảm liều thuốc hạ huyết áp khác."
                    }
                ],
                "moderate": [],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng alfuzosin",
                    "Hạ huyết áp nặng - CHỐNG CHỈ ĐỊNH",
                    "Dùng với CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, ritonavir) - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                    "Bệnh nhân cao tuổi - tăng nhạy cảm với hạ huyết áp",
                    "Dùng với thuốc hạ huyết áp - tăng nguy cơ hạ huyết áp",
                    "Dùng với PDE-5 inhibitors - tăng nguy cơ hạ huyết áp nặng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Không áp dụng",
                "pregnancy_details": "Alfuzosin chỉ dùng cho nam giới. Không áp dụng cho phụ nữ có thai.",
                "lactation": {
                    "safety": "Không áp dụng",
                    "details": "Alfuzosin chỉ dùng cho nam giới. Không áp dụng cho phụ nữ cho con bú.",
                    "recommendation": "Không áp dụng."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ alfuzosin. Theo dõi tác dụng phụ.",
                "severe": "Thận trọng. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ alfuzosin và nguy cơ tác dụng phụ. Giảm liều, theo dõi sát.",
                "notes": "Alfuzosin chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Cần thận trọng và giảm liều ở suy gan trung bình đến nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng, ngất",
                    "Chóng mặt nặng",
                    "Nhịp tim nhanh phản xạ"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng ngay alfuzosin",
                    "Nếu hạ huyết áp nặng:",
                    "  - Nằm đầu thấp, nâng chân",
                    "  - Truyền dịch (NS, LR) nếu cần",
                    "  - Thuốc vận mạch (norepinephrine, phenylephrine) nếu cần",
                    "Theo dõi: Huyết áp, nhịp tim liên tục"
                ],
                "monitoring": "Theo dõi huyết áp, nhịp tim liên tục cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống sau bữa ăn (QUAN TRỌNG) để giảm nguy cơ hạ huyết áp.",
                    "timing": "10mg PO x 1 lần/ngày sau bữa ăn. Uống đều đặn cùng một thời điểm mỗi ngày.",
                    "notes": "QUAN TRỌNG: 1) Uống sau bữa ăn, 2) Cảnh báo bệnh nhân về nguy cơ hạ huyết áp tư thế và ngất, 3) Đứng dậy từ từ, 4) Rối loạn xuất tinh có thể xảy ra, 5) CHỐNG CHỈ ĐỊNH với CYP3A4 inhibitors mạnh."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Alfuzosin (Uroxatral)",
                    "AUA Guidelines - Benign Prostatic Hyperplasia",
                    "UpToDate - Alfuzosin: Drug Information",
                    "Medscape - Alfuzosin Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Blood pressure (orthostatic hypotension) - CRITICAL", "Signs of syncope", "BPH symptoms improvement"]
            },
            "guideline_tags": [
                "AUA Guidelines - Benign Prostatic Hyperplasia",
                "EAU Guidelines - Lower Urinary Tract Symptoms",
                "FDA Drug Safety Communication - Alpha-blockers and Orthostatic Hypotension"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Silodosin": {
            "group": "Urology - Alpha-1 Adrenergic Blocker (BPH, Selective)",
            "vietnamese_name": "Silodosin, Rapaflo",
            "administration": ["PO"],
            "indications": [
                "Phì đại tuyến tiền liệt lành tính (BPH) - giảm triệu chứng",
                "Rối loạn tiểu tiện do BPH (tiểu khó, tiểu yếu, tiểu đêm, tiểu gấp)"
            ],
            "contraindications": [
                "Dị ứng silodosin",
                "Hạ huyết áp nặng",
                "Suy gan nặng",
                "Suy thận nặng (CrCl <30 mL/min)"
            ],
            "dosage": {
                "adult_bph": "8mg PO x 1 lần/ngày (sau bữa ăn)",
                "notes": "Silodosin là alpha-1 blocker chọn lọc cao nhất (ưu tiên alpha-1A receptors). Chọn lọc hơn tamsulosin, ít hạ huyết áp hơn. Uống sau bữa ăn để giảm nguy cơ hạ huyết áp."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Thận trọng, giảm liều 4mg nếu cần",
                "under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30 mL/min)"
            },
            "side_effects": [
                "Rối loạn xuất tinh (retrograde ejaculation) - phổ biến hơn tamsulosin",
                "Hạ huyết áp tư thế (orthostatic hypotension) - ít hơn tamsulosin",
                "Chóng mặt",
                "Ngất (syncope) - hiếm",
                "Nhức đầu",
                "Nghẹt mũi"
            ],
            "interactions": [
                "Thuốc hạ huyết áp: tăng nguy cơ hạ huyết áp",
                "PDE-5 inhibitors (sildenafil, tadalafil): tăng nguy cơ hạ huyết áp",
                "CYP3A4 inhibitors (ketoconazole, clarithromycin): tăng nồng độ silodosin"
            ],
        "pregnancy": "Không áp dụng (chỉ dùng cho nam giới)",
            "mechanism_of_action": "Silodosin là alpha-1 adrenergic blocker chọn lọc cao nhất (ưu tiên alpha-1A receptors ở tuyến tiền liệt và cổ bàng quang). Ức chế alpha-1A receptors trên cơ trơn tuyến tiền liệt và cổ bàng quang, gây giãn cơ, giảm sức cản đường tiểu, và cải thiện dòng nước tiểu. Silodosin chọn lọc hơn tamsulosin, ít ảnh hưởng đến alpha-1B receptors ở mạch máu, do đó ít gây hạ huyết áp hơn. ĐẶC ĐIỂM: (1) Chọn lọc alpha-1A cao nhất (ít hạ huyết áp nhất), (2) Rối loạn xuất tinh phổ biến hơn tamsulosin, (3) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 mL/min), (4) Uống sau bữa ăn để giảm nguy cơ hạ huyết áp.",
            "monitoring": [
                "Huyết áp (đặc biệt hạ huyết áp tư thế)",
                "Triệu chứng BPH (tiểu khó, tiểu yếu, tiểu đêm, tiểu gấp)",
                "Dấu hiệu ngất (syncope)",
                "Dấu hiệu rối loạn xuất tinh (retrograde ejaculation)",
                "Chức năng thận (CrCl)"
            ],
            "precautions": [
                "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 mL/min)",
                "Rối loạn xuất tinh - phổ biến hơn tamsulosin, cần tư vấn bệnh nhân",
                "Hạ huyết áp tư thế - ít hơn tamsulosin nhưng vẫn cần cảnh báo",
                "Uống sau bữa ăn để giảm nguy cơ hạ huyết áp",
                "Thận trọng ở bệnh nhân hạ huyết áp nền",
                "Thận trọng khi dùng với thuốc hạ huyết áp khác",
                "Thận trọng khi dùng với PDE-5 inhibitors"
            ],
            "pharmacokinetics": {
                "half_life": "13 giờ",
                "onset": "1-2 tuần",
                "duration": "Dài (cần dùng liên tục)",
                "protein_binding": "97%",
                "metabolism": "Gan (CYP3A4, UGT2B7)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "PDE-5 Inhibitors (Sildenafil, Tadalafil, Vardenafil)",
                        "mechanism": "Cả hai đều gây giãn mạch, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, dùng liều thấp nhất và theo dõi huyết áp sát."
                    },
                    {
                        "drug": "CYP3A4 Inhibitors (Ketoconazole, Clarithromycin, Itraconazole)",
                        "mechanism": "Ức chế CYP3A4, tăng nồng độ silodosin",
                        "effect": "Tăng nồng độ silodosin, tăng nguy cơ tác dụng phụ",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, giảm liều silodosin."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Thuốc hạ huyết áp (ACE inhibitors, ARBs, Beta-blockers, Diuretics)",
                        "mechanism": "Tác dụng hạ huyết áp cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất",
                        "management": "Thận trọng. Theo dõi huyết áp sát."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng silodosin",
                    "Hạ huyết áp nặng - CHỐNG CHỈ ĐỊNH",
                    "Suy thận nặng (CrCl <30 mL/min) - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                    "Suy thận trung bình (CrCl 30-60 mL/min) - thận trọng, giảm liều"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Không áp dụng",
                "pregnancy_details": "Silodosin chỉ dùng cho nam giới. Không áp dụng cho phụ nữ có thai.",
                "lactation": {
                    "safety": "Not Applicable",
                    "details": "Silodosin chỉ dùng cho nam giới. Không áp dụng cho phụ nữ cho con bú.",
                    "recommendation": "Không áp dụng."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ silodosin.",
                "severe": "Thận trọng. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ silodosin và nguy cơ tác dụng phụ. Giảm liều, theo dõi sát.",
                "notes": "Silodosin chuyển hóa qua gan (CYP3A4, UGT2B7). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ."
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng",
                    "Ngất (syncope)",
                    "Chóng mặt, mệt mỏi"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng ngay silodosin",
                    "Nếu hạ huyết áp nặng:",
                    "  - Nằm ngửa, nâng chân",
                    "  - Truyền dịch nếu cần",
                    "  - Theo dõi huyết áp liên tục",
                    "Theo dõi: Huyết áp, nhịp tim, dấu hiệu sinh tồn"
                ],
                "monitoring": "Theo dõi huyết áp, nhịp tim, dấu hiệu sinh tồn cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống sau bữa ăn để giảm nguy cơ hạ huyết áp.",
                    "timing": "8mg PO x 1 lần/ngày (sau bữa ăn).",
                    "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30 mL/min), 2) Uống sau bữa ăn, 3) Rối loạn xuất tinh phổ biến hơn tamsulosin, 4) Thận trọng khi dùng với thuốc hạ huyết áp hoặc PDE-5 inhibitors."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Silodosin (Rapaflo)",
                    "AUA Guidelines - Management of Benign Prostatic Hyperplasia",
                    "UpToDate - Silodosin: Drug Information",
                    "Medscape - Silodosin Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Orthostatic hypotension", "Syncope (rare)", "Retrograde ejaculation (more common than tamsulosin)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Blood pressure (especially orthostatic hypotension)", "BPH symptoms (difficulty urinating, weak stream, nocturia, urgency)", "Signs of syncope", "Signs of retrograde ejaculation", "Renal function (CrCl) - CONTRAINDICATED if CrCl <30 mL/min"]
            },
            "guideline_tags": [
                "AUA Guidelines - Benign Prostatic Hyperplasia",
                "FDA Drug Information - Silodosin"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

        "Tamsulosin": {
            "group": "Urology - Alpha-1 Adrenergic Blocker (BPH)",
            "vietnamese_name": "Tamsulosin, Flomax",
            "administration": ["PO"],
            "indications": [
                "Phì đại tuyến tiền liệt lành tính (BPH) - giảm triệu chứng",
                "Rối loạn tiểu tiện do BPH (tiểu khó, tiểu yếu, tiểu đêm, tiểu gấp)"
            ],
            "contraindications": [
                "Dị ứng tamsulosin",
                "Hạ huyết áp nặng",
                "Suy gan nặng"
            ],
            "dosage": {
                "adult_bph": "0.4mg PO x 1 lần/ngày (sau bữa ăn)",
                "adult_bph_max": "0.8mg PO x 1 lần/ngày nếu cần",
                "notes": "Uống sau bữa ăn để giảm nguy cơ hạ huyết áp. Không nhai hoặc nghiền viên nang (phóng thích có kiểm soát)."
            },
            "renal_adjustment": {
                "normal": "Không đổi",
                "30_60": "Không cần điều chỉnh đáng kể",
                "under_30": "Không cần điều chỉnh đáng kể"
            },
            "side_effects": [
                "Hạ huyết áp tư thế (orthostatic hypotension) - phổ biến",
                "Chóng mặt",
                "Ngất (syncope) - hiếm nhưng nguy hiểm",
                "Rối loạn xuất tinh (retrograde ejaculation) - phổ biến",
                "Nhức đầu",
                "Mệt mỏi",
                "Nghẹt mũi"
            ],
            "interactions": [
                "Thuốc hạ huyết áp: tăng nguy cơ hạ huyết áp",
                "PDE-5 inhibitors (sildenafil, tadalafil): tăng nguy cơ hạ huyết áp",
                "Cimetidine: tăng nồng độ tamsulosin"
            ],
        "pregnancy": "Không áp dụng (chỉ dùng cho nam giới)",
            "mechanism_of_action": "Tamsulosin là alpha-1 adrenergic blocker chọn lọc (ưu tiên alpha-1A receptors ở tuyến tiền liệt và cổ bàng quang). Ức chế alpha-1 receptors trên cơ trơn tuyến tiền liệt và cổ bàng quang, gây giãn cơ, giảm sức cản đường tiểu, và cải thiện dòng nước tiểu. Khác với các alpha-blocker không chọn lọc (prazosin, terazosin), tamsulosin ít ảnh hưởng đến alpha-1B receptors ở mạch máu, do đó ít gây hạ huyết áp hơn. ĐẶC ĐIỂM: (1) Chọn lọc alpha-1A (ít hạ huyết áp hơn), (2) Cải thiện triệu chứng BPH nhanh (1-2 tuần), (3) Nguy cơ hạ huyết áp tư thế và rối loạn xuất tinh, (4) Uống sau bữa ăn để giảm nguy cơ hạ huyết áp.",
            "monitoring": [
                "Huyết áp (đặc biệt hạ huyết áp tư thế) - QUAN TRỌNG",
                "Triệu chứng BPH (tiểu khó, tiểu yếu, tiểu đêm, tiểu gấp)",
                "Dấu hiệu ngất (syncope)",
                "Dấu hiệu rối loạn xuất tinh (retrograde ejaculation)"
            ],
            "precautions": [
                "Hạ huyết áp tư thế - phổ biến, cần cảnh báo bệnh nhân",
                "Nguy cơ ngất (syncope) - đặc biệt khi đứng dậy đột ngột",
                "Uống sau bữa ăn để giảm nguy cơ hạ huyết áp",
                "KHÔNG nhai hoặc nghiền viên nang (phóng thích có kiểm soát)",
                "Thận trọng ở bệnh nhân hạ huyết áp nền",
                "Thận trọng khi dùng với thuốc hạ huyết áp khác",
                "Thận trọng khi dùng với PDE-5 inhibitors (sildenafil, tadalafil)",
                "Rối loạn xuất tinh - tư vấn bệnh nhân trước khi dùng"
            ],
            "pharmacokinetics": {
                "half_life": "9-13 giờ",
                "onset": "1-2 tuần",
                "duration": "Dài (cần dùng liên tục)",
                "protein_binding": "94-99%",
                "metabolism": "Gan (CYP3A4, CYP2D6)",
                "clearance": "Gan, thận (bài tiết qua nước tiểu)"
            },
            "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [
                    {
                        "drug": "PDE-5 Inhibitors (Sildenafil, Tadalafil, Vardenafil)",
                        "mechanism": "Cả hai đều gây giãn mạch, tác dụng cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất, đột quỵ, nhồi máu cơ tim",
                        "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc, dùng liều thấp nhất và theo dõi huyết áp sát. Cách xa ít nhất 4-6 giờ."
                    },
                    {
                        "drug": "Thuốc hạ huyết áp (ACE inhibitors, ARBs, Beta-blockers, Diuretics)",
                        "mechanism": "Tác dụng hạ huyết áp cộng dồn",
                        "effect": "Tăng nguy cơ hạ huyết áp nặng, ngất",
                        "management": "Thận trọng. Theo dõi huyết áp sát. Có thể cần giảm liều thuốc hạ huyết áp khác."
                    }
                ],
                "moderate": [
                    {
                        "drug": "Cimetidine",
                        "mechanism": "Ức chế CYP3A4 và CYP2D6, tăng nồng độ tamsulosin",
                        "effect": "Tăng nồng độ tamsulosin, tăng nguy cơ tác dụng phụ",
                        "management": "Thận trọng. Có thể cần giảm liều tamsulosin."
                    }
                ],
                "minor": []
            },
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng tamsulosin",
                    "Hạ huyết áp nặng - CHỐNG CHỈ ĐỊNH"
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                    "Bệnh nhân cao tuổi - tăng nhạy cảm với hạ huyết áp",
                    "Dùng với thuốc hạ huyết áp - tăng nguy cơ hạ huyết áp",
                    "Dùng với PDE-5 inhibitors - tăng nguy cơ hạ huyết áp nặng"
                ]
            },
            "pregnancy_lactation": {
                "fda_category": "Không áp dụng",
                "pregnancy_details": "Tamsulosin chỉ dùng cho nam giới. Không áp dụng cho phụ nữ có thai.",
                "lactation": {
                    "safety": "Không áp dụng",
                    "details": "Tamsulosin chỉ dùng cho nam giới. Không áp dụng cho phụ nữ cho con bú.",
                    "recommendation": "Không áp dụng."
                }
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều",
                "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ tamsulosin. Theo dõi tác dụng phụ.",
                "severe": "Thận trọng. Chuyển hóa qua gan giảm đáng kể, tăng nồng độ tamsulosin và nguy cơ tác dụng phụ. Giảm liều, theo dõi sát.",
                "notes": "Tamsulosin chuyển hóa qua gan (CYP3A4, CYP2D6). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ tác dụng phụ. Cần thận trọng và giảm liều ở suy gan trung bình đến nặng."
            },
            "overdose_management": {
                "symptoms": [
                    "Hạ huyết áp nặng, ngất",
                    "Chóng mặt nặng",
                    "Nhịp tim nhanh phản xạ"
                ],
                "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
                "treatment": [
                    "Ngừng ngay tamsulosin",
                    "Nếu hạ huyết áp nặng:",
                    "  - Nằm đầu thấp, nâng chân",
                    "  - Truyền dịch (NS, LR) nếu cần",
                    "  - Thuốc vận mạch (norepinephrine, phenylephrine) nếu cần",
                    "Theo dõi: Huyết áp, nhịp tim liên tục"
                ],
                "monitoring": "Theo dõi huyết áp, nhịp tim liên tục cho đến khi hồi phục."
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống sau bữa ăn (QUAN TRỌNG) để giảm nguy cơ hạ huyết áp.",
                    "timing": "0.4mg PO x 1 lần/ngày sau bữa ăn. Có thể tăng đến 0.8mg/ngày nếu cần. Uống đều đặn cùng một thời điểm mỗi ngày.",
                    "notes": "QUAN TRỌNG: 1) Uống sau bữa ăn, 2) KHÔNG nhai hoặc nghiền viên nang (phóng thích có kiểm soát), 3) Cảnh báo bệnh nhân về nguy cơ hạ huyết áp tư thế và ngất, 4) Đứng dậy từ từ, 5) Rối loạn xuất tinh có thể xảy ra."
                }
            },
            "references": {
                "primary_sources": [
                    "FDA Drug Label - Tamsulosin (Flomax)",
                    "AUA Guidelines - Benign Prostatic Hyperplasia",
                    "UpToDate - Tamsulosin: Drug Information",
                    "Medscape - Tamsulosin Drug Reference"
                ],
                "last_updated": "2025-02-18",
                "evidence_level": "A - Dựa trên FDA drug labels, AUA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["Orthostatic hypotension", "Syncope (rare but dangerous)"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Blood pressure (especially orthostatic hypotension) - CRITICAL", "BPH symptoms (difficulty urinating, weak stream, nocturia, urgency)", "Signs of syncope", "Signs of retrograde ejaculation"]
            },
            "guideline_tags": [
                "AUA Guidelines - Benign Prostatic Hyperplasia",
                "FDA Drug Information - Tamsulosin"
            ],
            "black_box_warnings": "Cần xem xét black box warnings",
            "reversal_agents": {
                "available": False,
                "agents": [],
            },
        },

}

__all__ = ['BPH_ALPHA_BLOCKERS_DRUGS']
