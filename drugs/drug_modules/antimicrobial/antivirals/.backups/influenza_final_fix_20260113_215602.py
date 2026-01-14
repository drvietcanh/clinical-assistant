"""
Influenza Antivirals
Neuraminidase inhibitors for influenza treatment
"""

INFLUENZA_ANTIVIRALS = {
    "Favipiravir": {
        "group": "Infectious Disease - Antiviral (RNA polymerase inhibitor)",
        "vietnamese_name": "Favipiravir, Avigan",
        "administration": ["PO"],
        "indications": [
            "Cúm A và B (khi không đáp ứng hoặc không dùng được neuraminidase inhibitor)",
            "Cúm do chủng kháng oseltamivir/zanamivir",
            "COVID-19 (off-label tùy hướng dẫn địa phương)"
        ],
        "contraindications": [
            "Có thai hoặc dự định mang thai",
            "Cho con bú",
            "Bệnh gan tiến triển (ALT/AST >5x ULN)",
            "Gút tiến triển hoặc tăng acid uric không kiểm soát",
            "Dị ứng favipiravir"
        ],
        "dosage": {
            "adult_influenza": "1600mg x 2 lần (ngày 1), sau đó 600mg x 2 lần/ngày (ngày 2-5)",
            "adult_covid_off_label": "1800mg x 2 lần (ngày 1), sau đó 800mg x 2 lần/ngày (ngày 2-10) - theo phác đồ địa phương",
            "max_duration": "5 ngày cho cúm; 10 ngày cho COVID-19 (off-label)",
            "notes": "Uống sau ăn. Không dùng đơn trị kéo dài vì nguy cơ kháng thuốc và độc tính phôi thai."
        },
        "renal_adjustment": {
            "normal": "Không cần điều chỉnh",
            "30_60": "Thận trọng, có thể giữ nguyên liều nhưng theo dõi chặt chẽ men gan/acid uric",
            "under_30": "Dữ liệu hạn chế; tránh nếu có lựa chọn khác, hoặc giảm liều 50% và theo dõi sát"
        },
        "side_effects": [
            "Tăng acid uric, cơn gút",
            "Tăng men gan (ALT/AST)",
            "Buồn nôn, nôn, tiêu chảy",
            "Giảm bạch cầu trung tính nhẹ",
            "Kéo dài QT (hiếm)"
        ],
        "interactions": [
            "Thuốc tăng acid uric (thiazide, ciclosporin): tăng nguy cơ cơn gút",
            "Thuốc kéo dài QT (amiodarone, fluoroquinolone): tăng nguy cơ loạn nhịp",
            "Warfarin: có thể tăng INR, cần theo dõi"
        ],
        "pregnancy": "X - Chống chỉ định (gây quái thai)",
        "mechanism_of_action": "Favipiravir là tiền thuốc, được ribosyl hóa và phosphoryl hóa nội bào thành favipiravir-RTP, ức chế RNA-dependent RNA polymerase (RdRp) của virus RNA, gây ngừng kéo dài chuỗi và đột biến thảm họa, làm ngừng nhân lên virus.",
        "monitoring": [
            "Men gan (ALT/AST) trước và mỗi 2-3 ngày trong quá trình dùng",
            "Acid uric huyết thanh (nguy cơ cơn gút)",
            "Triệu chứng tim mạch nếu phối hợp thuốc kéo dài QT",
            "Công thức máu nếu dùng >5-10 ngày",
            "Test thai (nữ) và tư vấn tránh thai cho cả nam và nữ trong và sau điều trị (ít nhất 7 ngày)"
        ],
        "precautions": [
            "Gây quái thai: chống chỉ định tuyệt đối ở phụ nữ có thai; nam và nữ phải tránh thai hiệu quả",
            "Theo dõi men gan; ngừng nếu ALT/AST >5x ULN hoặc có triệu chứng viêm gan",
            "Thận trọng ở bệnh nhân gút hoặc tăng acid uric; cân nhắc allopurinol dự phòng nếu cần",
            "Uống sau ăn để giảm buồn nôn",
            "Không dùng đơn trị liệu cho COVID-19 ngoài phác đồ được phê duyệt"
        ],
        "pharmacokinetics": {
            "half_life": "2-5 giờ (tăng theo liều do ức chế aldehyde oxidase)",
            "onset": "Nồng độ đỉnh sau 2 giờ",
            "duration": "Liên quan phơi nhiễm AUC; dùng chia 2 lần/ngày sau liều tải",
            "protein_binding": "54%",
            "clearance": "Chuyển hóa chủ yếu qua aldehyde oxidase, một phần xanthine oxidase; thải qua thận dạng không hoạt tính"
        },
        "storage": "Bảo quản nhiệt độ phòng, tránh ẩm và ánh sáng.",
        "black_box_warnings": "GÂY QUÁI THAI - chống chỉ định tuyệt đối ở thai kỳ; yêu cầu tránh thai cho cả nam và nữ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, sotalol, levofloxacin)",
                    "mechanism": "Nguy cơ cộng dồn kéo dài QT",
                    "effect": "Tăng nguy cơ xoắn đỉnh",
                    "management": "Tránh nếu có thể; nếu bắt buộc, theo dõi ECG và điện giải."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể ức chế nhẹ chuyển hóa warfarin",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR và chỉnh liều warfarin khi bắt đầu/ngừng favipiravir."
                },
                {
                    "drug": "Allopurinol hoặc febuxostat",
                    "mechanism": "Tác động lên chuyển hóa purine/acid uric, có thể thay đổi nồng độ favipiravir",
                    "effect": "Biến thiên nồng độ thuốc và acid uric",
                    "management": "Theo dõi acid uric, lâm sàng; điều chỉnh nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Có thai hoặc dự định mang thai",
                "Cho con bú",
                "Dị ứng với favipiravir",
                "ALT/AST >5x ULN"
            ],
            "tương_đối": [
                "Tăng acid uric/gút không kiểm soát",
                "Suy gan vừa-nặng",
                "Phối hợp thuốc kéo dài QT",
                "CrCl <30 ml/phút (dữ liệu hạn chế)"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Có thai hoặc dự định mang thai",
                "Cho con bú",
                "Dị ứng với favipiravir",
                "ALT/AST >5x ULN"
            ],
            "tương_đối": [
                "Tăng acid uric/gút không kiểm soát",
                "Suy gan vừa-nặng",
                "Phối hợp thuốc kéo dài QT",
                "CrCl <30 ml/phút (dữ liệu hạn chế)"
            ]
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ."
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định tuyệt đối do gây quái thai trên động vật và cảnh báo của nhà sản xuất. Cả nam và nữ phải tránh thai hiệu quả trong điều trị và 7 ngày sau liều cuối.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Chưa rõ bài tiết vào sữa mẹ; nguy cơ độc tính phôi thai/nhũ nhi.",
                "recommendation": "Ngừng cho con bú hoặc chọn thuốc khác."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh nhưng theo dõi men gan",
            "moderate": "Thận trọng, cân nhắc giảm 25-50% nếu ALT/AST tăng nền",
            "severe": "Tránh dùng nếu ALT/AST >5x ULN hoặc Child-Pugh C",
            "notes": "Favipiravir chuyển hóa qua gan; suy gan làm tăng phơi nhiễm."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Tăng mạnh acid uric",
                "Tăng men gan",
                "Kéo dài QT (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc, điều trị hỗ trợ",
                "Theo dõi ECG, điện giải nếu nghi kéo dài QT",
                "Hydrat và dùng thuốc hạ acid uric nếu cần",
                "Theo dõi men gan"
            ],
            "monitoring": "ECG, men gan, acid uric, triệu chứng lâm sàng"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống sau ăn để giảm kích ứng tiêu hóa",
                "timing": "Liều tải ngày 1, sau đó chia 2 lần/ngày. Uống cách đều 12 giờ."
            },
            "iv": None
        },
        "references": {
            "primary_sources": [
                "PMDA Japan - Favipiravir Prescribing Information",
                "WHO COVID-19 Therapeutics (off-label use)",
                "UpToDate - Favipiravir",
                "IDSA influenza guidance (kháng neuraminidase)"
            ],
            "last_updated": "2025-02-17",
            "evidence_level": "B - Dữ liệu cấp phép tại Nhật và nghiên cứu quan sát; sử dụng off-label cần cân nhắc lợi ích/nguy cơ"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Teratogenicity (category X) - CRITICAL", "Hepatotoxicity", "Hyperuricemia/gout attacks", "QT prolongation (rare)"],
            "qt_prolongation": True,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Hepatic function (ALT, AST) - CRITICAL (before and every 2-3 days)", "Uric acid levels - CRITICAL (gout risk)", "ECG if co-administered with QT-prolonging drugs", "Pregnancy test (women) and contraception counseling (both sexes) - CRITICAL", "CBC if used >5-10 days"]
        },
        "guideline_tags": [
            "WHO Guidelines - Influenza Antiviral Treatment",
            "FDA Black Box Warning - Favipiravir and Teratogenicity",
            "FDA Black Box Warning - Favipiravir and Pregnancy (Category X)",
            "IDSA Guidelines - Influenza Treatment"
        ]
    },
    "Oseltamivir": {
        "group": "Infectious Disease - Antiviral (Neuraminidase Inhibitor)",
        "vietnamese_name": "Oseltamivir, Tamiflu",
        "administration": ["PO"],
        "indications": [
            "Cúm A và B (treatment)",
            "Phòng ngừa cúm",
            "Cúm ở người suy giảm miễn dịch"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng (thận trọng)"
        ],
        "dosage": {
            "adult_treatment": "75mg x 2 lần/ngày x 5 ngày",
            "adult_prophylaxis": "75mg x 1 lần/ngày x 10 ngày (sau tiếp xúc) hoặc x 6 tuần (mùa cúm)",
            "adult_max": "150mg x 2 lần/ngày (suy giảm miễn dịch)",
            "notes": "Bắt đầu trong 48 giờ đầu triệu chứng. Hiệu quả nhất trong 24 giờ đầu"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "75mg x 1 lần/ngày (treatment), 75mg cách ngày (prophylaxis)",
            "under_30": "75mg x 1 lần/ngày (treatment), 75mg cách 2 ngày (prophylaxis)"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Đau đầu",
            "Tiêu chảy",
            "Rối loạn tâm thần (hiếm, ở trẻ em)",
            "Co giật (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ oseltamivir",
            "Ít tương tác khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Oseltamivir là thuốc kháng virus cúm, thuộc nhóm chất ức chế neuraminidase. Oseltamivir phosphate là tiền thuốc (prodrug), được chuyển hóa trong gan thành oseltamivir carboxylate (chất hoạt động). Oseltamivir carboxylate ức chế enzyme neuraminidase của virus cúm A và B, enzyme này có vai trò quan trọng trong việc giải phóng các hạt virus mới từ tế bào chủ và lan truyền virus trong đường hô hấp. Bằng cách ức chế neuraminidase, oseltamivir ngăn chặn sự giải phóng virus, làm giảm lan truyền virus và giảm thời gian bệnh. Oseltamivir hiệu quả với cả cúm A và cúm B, nhưng hiệu quả nhất khi bắt đầu điều trị trong vòng 48 giờ đầu (tốt nhất là 24 giờ đầu) sau khi xuất hiện triệu chứng.",
        "monitoring": [
            "Triệu chứng cúm (sốt, ho, đau họng, đau cơ) - đánh giá đáp ứng điều trị",
            "Dấu hiệu biến chứng (viêm phổi, suy hô hấp, nhiễm trùng thứ phát)",
            "Tác dụng phụ (buồn nôn, nôn, đau đầu, tiêu chảy) - thường nhẹ",
            "Rối loạn tâm thần ở trẻ em (kích động, lú lẫn, hành vi bất thường) - hiếm nhưng cần theo dõi",
            "Co giật - hiếm, đặc biệt ở trẻ em",
            "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
            "Tương tác với probenecid (tăng nồng độ oseltamivir)"
        ],
        "precautions": [
            "Bắt đầu điều trị càng sớm càng tốt - hiệu quả nhất trong vòng 48 giờ đầu (tốt nhất là 24 giờ đầu) sau khi xuất hiện triệu chứng",
            "Điều chỉnh liều ở suy thận: CrCl 30-60: 75mg x 1 lần/ngày (treatment), 75mg cách ngày (prophylaxis); CrCl <30: 75mg x 1 lần/ngày (treatment), 75mg cách 2 ngày (prophylaxis)",
            "Uống với thức ăn để giảm buồn nôn, nôn",
            "Rối loạn tâm thần ở trẻ em - hiếm nhưng có thể nghiêm trọng, cần theo dõi chặt chẽ",
            "Thận trọng ở bệnh nhân suy thận nặng - cần điều chỉnh liều",
            "Probenecid tăng nồng độ oseltamivir - có thể cần điều chỉnh liều",
            "Hiệu quả phòng ngừa: dùng 75mg x 1 lần/ngày x 10 ngày sau tiếp xúc hoặc x 6 tuần trong mùa cúm",
            "Liều cao hơn (150mg x 2 lần/ngày) có thể cần ở bệnh nhân suy giảm miễn dịch",
            "Không thay thế vaccine cúm - vaccine vẫn là biện pháp phòng ngừa chính",
            "Kháng thuốc có thể xảy ra - theo dõi đáp ứng điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "1-3 giờ (oseltamivir), 6-10 giờ (oseltamivir carboxylate - chất hoạt động)",
            "onset": "24-48 giờ (giảm triệu chứng)",
            "duration": "5 ngày (treatment), 10 ngày - 6 tuần (prophylaxis)",
            "protein_binding": "3% (oseltamivir carboxylate)",
            "clearance": "Gan: chuyển hóa oseltamivir thành oseltamivir carboxylate (chất hoạt động) qua esterase. Thận: bài tiết chủ yếu qua thận (oseltamivir carboxylate bài tiết nguyên dạng). Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 10 ngày sau khi pha hoặc 17 ngày nếu bảo quản trong tủ lạnh.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết oseltamivir carboxylate qua thận, tăng nồng độ oseltamivir.",
                    "effect": "Tăng nồng độ oseltamivir carboxylate, tăng tác dụng và tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều oseltamivir khi dùng với probenecid. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng oseltamivir hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều nghiêm ngặt",
                "Có thai - category C, thận trọng",
                "Trẻ em <1 tuổi - không khuyến cáo"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng oseltamivir hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều nghiêm ngặt",
                "Có thai - category C, thận trọng",
                "Trẻ em <1 tuổi - không khuyến cáo"
            ]
        },
        "black_box_warnings": None,
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Oseltamivir là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Cúm trong thai kỳ có thể gây biến chứng nghiêm trọng (viêm phổi, suy hô hấp, tử vong). Oseltamivir được khuyến cáo để điều trị cúm trong thai kỳ nếu có chỉ định.",
            "lactation": {
                "safety": "Compatible",
                "details": "Oseltamivir và oseltamivir carboxylate bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh nếu có dấu hiệu bất thường (hiếm)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Oseltamivir chuyển hóa ở gan thành oseltamivir carboxylate, nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi tác dụng phụ. Chuyển hóa có thể giảm nhẹ ở suy gan trung bình.",
            "severe": "Thận trọng, theo dõi tác dụng phụ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thường không cần điều chỉnh liều.",
            "notes": "Oseltamivir chuyển hóa ở gan thành oseltamivir carboxylate (chất hoạt động) qua esterase. Suy gan có thể làm giảm chuyển hóa, nhưng thường không ảnh hưởng đáng kể đến nồng độ oseltamivir carboxylate."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn (tăng so với liều điều trị)",
                "Đau đầu",
                "Tiêu chảy",
                "Rối loạn tâm thần (hiếm)",
                "Co giật (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng oseltamivir nếu có thể",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị hỗ trợ: truyền dịch nếu cần, điều trị triệu chứng",
                "Theo dõi ít nhất 4-6 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu rối loạn tâm thần, co giật"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm buồn nôn, nôn. Có thể uống với hoặc không thức ăn, nhưng uống với thức ăn giúp giảm tác dụng phụ.",
                "timing": "Uống 2 lần/ngày (treatment) hoặc 1 lần/ngày (prophylaxis). Uống cùng thời điểm mỗi ngày để dễ nhớ. Điều chỉnh liều ở suy thận: CrCl 30-60: 75mg x 1 lần/ngày (treatment), 75mg cách ngày (prophylaxis); CrCl <30: 75mg x 1 lần/ngày (treatment), 75mg cách 2 ngày (prophylaxis)."
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
                "FDA Drug Label - Oseltamivir (Tamiflu)",
                "CDC Guidelines - Influenza Antiviral Medications",
                "WHO Guidelines - Antiviral Treatment for Influenza",
                "UpToDate - Oseltamivir: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels, CDC/WHO guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Neuropsychiatric events (rare, especially in children)", "Serious skin reactions (SJS/TEN) - rare"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Renal function (CrCl) - for dose adjustment", "Neuropsychiatric signs (hallucinations, delirium) - especially in children", "Skin reactions"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Influenza Treatment",
            "CDC Guidelines - Influenza Antiviral Medications",
            "FDA Drug Safety Communication - Neuropsychiatric Events"
        ]
    },

    "Remdesivir": {
        "group": "Infectious Disease - Antiviral (RNA Polymerase Inhibitor)",
        "vietnamese_name": "Remdesivir, Veklury",
        "administration": ["IV"],
        "indications": [
            "COVID-19 (bệnh nhân nhập viện, cần oxy nhưng chưa cần thở máy)",
            "COVID-19 (bệnh nhân nhập viện, không cần oxy nhưng có nguy cơ tiến triển nặng)"
        ],
        "contraindications": [
            "Dị ứng remdesivir",
            "Suy thận nặng (eGFR <30 mL/min/1.73m²)",
            "Suy gan nặng (ALT >5x ULN)"
        ],
        "dosage": {
            "adult_loading": "200mg IV x 1 lần (ngày 1)",
            "adult_maintenance": "100mg IV x 1 lần/ngày (ngày 2-5 hoặc 2-10)",
            "adult_duration": "5 ngày (bệnh nhân không cần oxy) hoặc 10 ngày (bệnh nhân cần oxy)",
            "notes": "Truyền IV trong 30-120 phút. Bắt đầu càng sớm càng tốt sau khi chẩn đoán COVID-19."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "CHỐNG CHỈ ĐỊNH (eGFR <30)"
        },
        "side_effects": [
            "Tăng men gan (ALT, AST) - thường gặp",
            "Buồn nôn",
            "Phản ứng truyền dịch (phản vệ, sốc phản vệ)",
            "Nhịp tim chậm",
            "Hạ huyết áp"
        ],
        "interactions": [
            "Chloroquine/Hydroxychloroquine: giảm hiệu quả remdesivir",
            "CYP3A4 inhibitors: có thể tăng nồng độ remdesivir"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Remdesivir là nucleotide analog (adenosine), ức chế RNA-dependent RNA polymerase (RdRp) của virus SARS-CoV-2. Remdesivir được phosphoryl hóa trong tế bào thành remdesivir triphosphate (chất hoạt động), ức chế RdRp, ngăn chặn sao chép RNA của virus, dẫn đến giảm tải lượng virus. Remdesivir có tác dụng phổ rộng trên nhiều virus RNA, bao gồm SARS-CoV-2, MERS-CoV, Ebola virus. Remdesivir hiệu quả nhất khi bắt đầu điều trị sớm (trong vòng 7-10 ngày sau khi xuất hiện triệu chứng), đặc biệt ở bệnh nhân nhập viện cần oxy nhưng chưa cần thở máy.",
        "monitoring": [
            "Men gan (ALT, AST) - trước khi bắt đầu và định kỳ (mỗi 2-3 ngày)",
            "Chức năng thận (creatinine, eGFR) - trước khi bắt đầu và định kỳ",
            "Dấu hiệu phản ứng truyền dịch (phản vệ, sốc phản vệ) - trong và sau khi truyền",
            "Dấu hiệu sinh tồn (huyết áp, nhịp tim) - trong và sau khi truyền",
            "Triệu chứng COVID-19 - đánh giá đáp ứng điều trị",
            "Tải lượng virus (nếu có) - theo dõi đáp ứng điều trị"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (eGFR <30) - nguy cơ tích tụ remdesivir",
            "Thận trọng ở suy gan (ALT >5x ULN) - nguy cơ độc tính gan",
            "Bắt đầu điều trị càng sớm càng tốt - hiệu quả nhất trong vòng 7-10 ngày sau khi xuất hiện triệu chứng",
            "Theo dõi men gan chặt chẽ - tăng men gan thường gặp, có thể cần ngừng nếu ALT >5x ULN",
            "Theo dõi phản ứng truyền dịch - có thể gây phản vệ, sốc phản vệ",
            "Truyền IV trong 30-120 phút - không truyền nhanh hơn",
            "Không dùng với chloroquine/hydroxychloroquine - giảm hiệu quả remdesivir",
            "Thận trọng ở bệnh nhân có tiền sử bệnh gan - tăng nguy cơ độc tính gan",
            "Dùng 5 ngày cho bệnh nhân không cần oxy, 10 ngày cho bệnh nhân cần oxy"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (remdesivir), 27 giờ (chất chuyển hóa hoạt động)",
            "onset": "1-2 ngày (giảm triệu chứng)",
            "duration": "5-10 ngày (tùy chỉ định)",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan (chuyển hóa) và thận (bài tiết)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C) hoặc tủ lạnh (2-8°C). Lọ bột: bảo quản trong bao bì kín. Sau khi pha: bảo quản ở nhiệt độ phòng hoặc tủ lạnh, dùng trong vòng 24 giờ.",
        "black_box_warnings": "Có thể gây phản ứng truyền dịch nghiêm trọng (phản vệ, sốc phản vệ). Ngừng ngay nếu có phản ứng dị ứng. Có thể gây tăng men gan (ALT, AST) - theo dõi chặt chẽ, ngừng nếu ALT >5x ULN.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Chloroquine, Hydroxychloroquine",
                    "mechanism": "Chloroquine/hydroxychloroquine ức chế hoạt động của remdesivir",
                    "effect": "Giảm hiệu quả remdesivir, giảm khả năng điều trị COVID-19",
                    "management": "KHÔNG DÙNG CÙNG. Tránh dùng chloroquine/hydroxychloroquine khi đang dùng remdesivir."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Có thể ức chế chuyển hóa remdesivir",
                    "effect": "Tăng nồng độ remdesivir, tăng nguy cơ độc tính",
                    "management": "Thận trọng. Theo dõi men gan, chức năng thận chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng remdesivir hoặc các thành phần khác",
                "Suy thận nặng (eGFR <30 mL/min/1.73m²) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Suy gan nặng (ALT >5x ULN) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI"
            ],
            "tương_đối": [
                "Suy thận trung bình (eGFR 30-60) - thận trọng, có thể cần giảm liều",
                "Suy gan trung bình (ALT 2-5x ULN) - thận trọng, theo dõi chặt chẽ",
                "Có thai - category B, thận trọng",
                "Dùng với chloroquine/hydroxychloroquine - giảm hiệu quả"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Remdesivir là category B. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. COVID-19 trong thai kỳ có thể gây biến chứng nghiêm trọng. Remdesivir có thể được dùng trong thai kỳ nếu có chỉ định.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết remdesivir có bài tiết vào sữa mẹ hay không. Không khuyến cáo dùng khi cho con bú trừ khi lợi ích vượt trội nguy cơ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, theo dõi men gan chặt chẽ (ALT 2-5x ULN)",
            "severe": "CHỐNG CHỈ ĐỊNH (ALT >5x ULN)",
            "notes": "Remdesivir chuyển hóa qua gan. Suy gan có thể làm tăng nồng độ và độc tính gan. CHỐNG CHỈ ĐỊNH ở suy gan nặng (ALT >5x ULN)."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng men gan nặng (ALT >5x ULN)",
                "Suy thận cấp",
                "Phản ứng truyền dịch (phản vệ, sốc phản vệ)",
                "Hạ huyết áp nặng",
                "Nhịp tim chậm nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay remdesivir",
                "Điều trị phản ứng truyền dịch: Epinephrine, diphenhydramine, methylprednisolone",
                "Theo dõi men gan, chức năng thận",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Men gan, chức năng thận, dấu hiệu sinh tồn, dấu hiệu phản ứng dị ứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 100mg remdesivir với 20ml nước cất hoặc normal saline. Lắc nhẹ để hòa tan. Pha loãng thêm trong 250ml normal saline hoặc D5W.",
                "infusion_rate": "Truyền trong 30-120 phút. KHÔNG truyền nhanh hơn. Theo dõi phản ứng truyền dịch trong và sau khi truyền.",
                "compatibility": ["Normal saline", "D5W"],
                "incompatibility": ["Chloroquine", "Hydroxychloroquine"],
                "notes": "Loading dose: 200mg IV x 1 lần (ngày 1). Maintenance: 100mg IV x 1 lần/ngày (ngày 2-5 hoặc 2-10). Truyền trong 30-120 phút. Theo dõi phản ứng truyền dịch."
            },
            "oral": {
                "with_food": "Không áp dụng",
                "timing": "Không áp dụng",
                "notes": "Remdesivir chỉ có dạng IV, không có dạng uống."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <12 tuổi hoặc <40kg (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <12 tuổi hoặc <40kg (dữ liệu hạn chế)",
            "children": "12-17 tuổi, ≥40kg: Liều người lớn. <40kg: 5mg/kg IV x 1 lần (loading), sau đó 2.5mg/kg IV x 1 lần/ngày (maintenance).",
            "adolescents": "Liều người lớn nếu ≥40kg",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng khi thực sự cần thiết và có chỉ định đặc biệt. Theo dõi men gan, chức năng thận chặt chẽ."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (tăng men gan, suy thận). Suy thận và suy gan phổ biến hơn.",
            "dose_adjustment": "Không cần điều chỉnh liều thường quy. Điều chỉnh theo chức năng thận nếu cần.",
            "monitoring": "Theo dõi men gan, chức năng thận sát hơn. Theo dõi phản ứng truyền dịch chặt chẽ."
        },
        "brand_names": {
            "vietnam": ["Veklury", "Remdesivir"],
            "common": ["Veklury", "Remdesivir"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "10,000,000 - 30,000,000 VND/liệu trình (tùy thương hiệu và nhà thuốc)",
            "note": "Giá rất cao do là thuốc mới. Giá thay đổi theo thương hiệu và nhà thuốc."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Remdesivir (Veklury)",
                "WHO Guidelines - COVID-19 Treatment",
                "NIH Guidelines - COVID-19 Treatment",
                "UpToDate - Remdesivir: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, WHO/NIH guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Hepatotoxicity (ALT, AST elevation - common) - CRITICAL", "Infusion reactions (anaphylaxis, anaphylactic shock) - CRITICAL"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Hepatic function (ALT, AST) - CRITICAL (baseline and every 2-3 days)", "Renal function (creatinine, eGFR) - CRITICAL (baseline and periodically)", "Infusion reactions (anaphylaxis, anaphylactic shock) - CRITICAL (during and after infusion)", "Vital signs (blood pressure, heart rate) - during and after infusion", "COVID-19 symptoms - assess treatment response", "Viral load (if available) - monitor treatment response"]
        },
        "guideline_tags": [
            "WHO Guidelines - COVID-19 Treatment",
            "NIH Guidelines - COVID-19 Treatment",
            "FDA Black Box Warning - Remdesivir and Infusion Reactions",
            "FDA Black Box Warning - Remdesivir and Hepatotoxicity",
            "FDA Drug Information - Remdesivir"
        ]
    },

    "Zanamivir": {
        "group": "Infectious Disease - Antiviral (Neuraminidase Inhibitor)",
        "vietnamese_name": "Zanamivir, Relenza",
        "administration": ["Inhalation"],
        "indications": [
            "Cúm A và B (treatment)",
            "Phòng ngừa cúm"
        ],
        "contraindications": [
            "Dị ứng zanamivir",
            "Bệnh phổi tắc nghẽn mạn tính (COPD)",
            "Hen phế quản",
            "Suy hô hấp"
        ],
        "dosage": {
            "adult_treatment": "10mg (2 lần hít) x 2 lần/ngày x 5 ngày",
            "adult_prophylaxis": "10mg (2 lần hít) x 1 lần/ngày x 10 ngày (sau tiếp xúc) hoặc x 28 ngày (mùa cúm)",
            "notes": "Dạng hít. Bắt đầu trong 48 giờ đầu triệu chứng. Hiệu quả nhất trong 24 giờ đầu"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Co thắt phế quản (nguy hiểm ở bệnh nhân COPD/hen)",
            "Khó thở",
            "Ho",
            "Đau đầu",
            "Buồn nôn",
            "Chóng mặt"
        ],
        "interactions": [
            "Ít tương tác (hấp thu toàn thân thấp)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Zanamivir là thuốc kháng virus cúm, thuộc nhóm chất ức chế neuraminidase. Zanamivir ức chế trực tiếp enzyme neuraminidase của virus cúm A và B, enzyme này có vai trò quan trọng trong việc giải phóng các hạt virus mới từ tế bào chủ và lan truyền virus trong đường hô hấp. Bằng cách ức chế neuraminidase, zanamivir ngăn chặn sự giải phóng virus, làm giảm lan truyền virus và giảm thời gian bệnh. Zanamivir được dùng dạng hít, tác dụng trực tiếp tại đường hô hấp, nơi virus cúm nhân lên. Zanamivir hiệu quả với cả cúm A và cúm B, nhưng hiệu quả nhất khi bắt đầu điều trị trong vòng 48 giờ đầu (tốt nhất là 24 giờ đầu) sau khi xuất hiện triệu chứng.",
        "monitoring": [
            "Triệu chứng cúm (sốt, ho, đau họng, đau cơ) - đánh giá đáp ứng điều trị",
            "Dấu hiệu biến chứng (viêm phổi, suy hô hấp, nhiễm trùng thứ phát)",
            "Chức năng hô hấp - đặc biệt ở bệnh nhân COPD/hen (nguy cơ co thắt phế quản)",
            "Tác dụng phụ hô hấp (co thắt phế quản, khó thở, ho) - nguy hiểm ở bệnh nhân COPD/hen",
            "Tác dụng phụ khác (đau đầu, buồn nôn, chóng mặt) - thường nhẹ"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân COPD hoặc hen phế quản - nguy cơ co thắt phế quản nghiêm trọng, có thể đe dọa tính mạng",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân suy hô hấp",
            "Bắt đầu điều trị càng sớm càng tốt - hiệu quả nhất trong vòng 48 giờ đầu (tốt nhất là 24 giờ đầu) sau khi xuất hiện triệu chứng",
            "Dạng hít - cần hướng dẫn bệnh nhân cách sử dụng đúng",
            "Ngừng ngay nếu có co thắt phế quản hoặc khó thở nặng",
            "Có thể cần dùng thuốc giãn phế quản trước khi dùng zanamivir ở bệnh nhân có nguy cơ",
            "Hiệu quả phòng ngừa: dùng 10mg x 1 lần/ngày x 10 ngày sau tiếp xúc hoặc x 28 ngày trong mùa cúm",
            "Không thay thế vaccine cúm - vaccine vẫn là biện pháp phòng ngừa chính",
            "Kháng thuốc có thể xảy ra - theo dõi đáp ứng điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "2.5-5 giờ",
            "onset": "24-48 giờ (giảm triệu chứng)",
            "duration": "5 ngày (treatment), 10-28 ngày (prophylaxis)",
            "protein_binding": "<10%",
            "clearance": "Thận (bài tiết nguyên dạng). Hấp thu toàn thân thấp (4-17%) do dùng dạng hít"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Đĩa Rotadisk: bảo quản trong bao bì kín. Không bảo quản trong tủ lạnh.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở bệnh nhân COPD hoặc hen phế quản - có thể gây co thắt phế quản nghiêm trọng, suy hô hấp, và tử vong. Ngừng ngay nếu có co thắt phế quản hoặc khó thở nặng.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng zanamivir hoặc các thành phần khác",
                "COPD - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Hen phế quản - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Suy hô hấp - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI"
            ],
            "tương_đối": [
                "Bệnh phổi mạn tính khác - thận trọng, có thể gây co thắt phế quản",
                "Có thai - category C, thận trọng",
                "Trẻ em <5 tuổi - không khuyến cáo (khó sử dụng dạng hít)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Zanamivir là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Cúm trong thai kỳ có thể gây biến chứng nghiêm trọng. Zanamivir có thể được dùng trong thai kỳ nếu có chỉ định, nhưng ưu tiên oseltamivir (dạng uống, dễ dùng hơn).",
            "lactation": {
                "safety": "Compatible",
                "details": "Zanamivir hấp thu toàn thân thấp (4-17%) do dùng dạng hít. Nồng độ trong sữa mẹ rất thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh nếu có dấu hiệu bất thường (hiếm)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều",
            "notes": "Zanamivir hấp thu toàn thân thấp và thải trừ chủ yếu qua thận. Suy gan không ảnh hưởng đáng kể đến dược động học của zanamivir."
        },
        "overdose_management": {
            "symptoms": [
                "Co thắt phế quản (nguy hiểm)",
                "Khó thở nặng",
                "Ho",
                "Đau đầu",
                "Buồn nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Thuốc giãn phế quản (albuterol) cho co thắt phế quản.",
            "treatment": [
                "Ngừng zanamivir ngay nếu có co thắt phế quản hoặc khó thở nặng",
                "Điều trị co thắt phế quản: Albuterol, ipratropium (thuốc giãn phế quản)",
                "Hỗ trợ hô hấp nếu cần (oxy, thở máy)",
                "Theo dõi dấu hiệu sinh tồn",
                "Theo dõi ít nhất 4-6 giờ"
            ],
            "monitoring": "Chức năng hô hấp, dấu hiệu co thắt phế quản, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "inhalation": {
                "instructions": "Dùng với thiết bị Diskhaler. Mỗi liều: 2 lần hít (mỗi lần hít 5mg). Hướng dẫn bệnh nhân cách sử dụng đúng. Đặt đĩa Rotadisk vào Diskhaler, đóng nắp, bấm để đâm thủng đĩa, hít sâu và giữ hơi thở 10 giây. Lặp lại lần hít thứ hai.",
                "timing": "Hít 2 lần/ngày (treatment) hoặc 1 lần/ngày (prophylaxis). Hít cùng thời điểm mỗi ngày để dễ nhớ.",
                "notes": "CHỐNG CHỈ ĐỊNH ở bệnh nhân COPD/hen - nguy cơ co thắt phế quản nghiêm trọng. Có thể cần dùng thuốc giãn phế quản trước khi dùng zanamivir ở bệnh nhân có nguy cơ."
            },
            "oral": {
                "with_food": "Không áp dụng",
                "timing": "Không áp dụng",
                "notes": "Zanamivir chỉ có dạng hít, không có dạng uống."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <5 tuổi (khó sử dụng dạng hít)",
            "infants": "Không khuyến cáo cho trẻ <5 tuổi (khó sử dụng dạng hít)",
            "children": "5-12 tuổi: 10mg (2 lần hít) x 2 lần/ngày x 5 ngày (treatment), 10mg x 1 lần/ngày x 10 ngày (prophylaxis). Cần hướng dẫn cách sử dụng đúng.",
            "adolescents": "Liều người lớn: 10mg (2 lần hít) x 2 lần/ngày x 5 ngày (treatment), 10mg x 1 lần/ngày x 10 ngày (prophylaxis)",
            "notes": "Không khuyến cáo cho trẻ <5 tuổi do khó sử dụng dạng hít. Cần hướng dẫn cách sử dụng đúng. CHỐNG CHỈ ĐỊNH ở trẻ có COPD/hen."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể khó sử dụng dạng hít. Có thể ưu tiên oseltamivir (dạng uống) nếu có thể.",
            "dose_adjustment": "Không cần điều chỉnh liều. Liều người lớn.",
            "monitoring": "Theo dõi chức năng hô hấp sát hơn. Đảm bảo bệnh nhân sử dụng đúng cách."
        },
        "brand_names": {
            "vietnam": ["Relenza", "Zanamivir"],
            "common": ["Relenza", "Zanamivir"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "200,000 - 500,000 VND/hộp (tùy thương hiệu và nhà thuốc)",
            "note": "Giá cao hơn oseltamivir. Giá thay đổi theo thương hiệu và nhà thuốc."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zanamivir (Relenza)",
                "CDC Guidelines - Influenza Antiviral Medications",
                "WHO Guidelines - Antiviral Treatment for Influenza",
                "UpToDate - Zanamivir: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, CDC/WHO guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Bronchospasm (CRITICAL in asthma/COPD)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory status (bronchospasm) - CRITICAL", "Signs of allergic reaction"]
        },
        "guideline_tags": [
            "IDSA Guidelines - Influenza Treatment",
            "CDC Guidelines - Influenza Antiviral Medications",
            "FDA Warning - Zanamivir and Bronchospasm"
        ]
    },

}

__all__ = ['INFLUENZA_ANTIVIRALS']
