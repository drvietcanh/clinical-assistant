"""
Analgesic and Pain Medications
Active module - contains all analgesic drug data
"""

ANALGESICS_DRUGS = {
"Ibuprofen": {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Ibuprofen, Brufen",
        "administration": ["PO"],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp",
            "Sốt",
            "Đau bụng kinh"
        ],
        "contraindications": [
            "Loét dạ dày tá tràng đang hoạt động",
            "Suy thận nặng",
            "Suy gan nặng",
            "Có thai (3 tháng cuối)",
            "Dị ứng NSAID/aspirin"
        ],
        "dosage": {
            "adult_pain": "200-400mg mỗi 4-6 giờ (tối đa 2.4g/ngày)",
            "adult_arthritis": "400-800mg x 3-4 lần/ngày (tối đa 3.2g/ngày)",
            "notes": "Uống với thức ăn để giảm kích ứng dạ dày"
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Ban da"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Aspirin: tăng nguy cơ chảy máu dạ dày",
            "Methotrexate: tăng độc tính methotrexate"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Prostaglandin tham gia vào quá trình đau, viêm, sốt, bảo vệ niêm mạc dạ dày, và điều hòa thận",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng)",
            "Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ",
            "Huyết áp (NSAID có thể tăng huyết áp)",
            "Chức năng gan (transaminase) nếu dùng lâu dài",
            "Dấu hiệu suy tim (giữ nước, phù)"
        ],
        "precautions": [
            "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
            "Cân nhắc dùng PPI hoặc misoprostol nếu có nguy cơ loét dạ dày",
            "Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp",
            "Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)",
            "Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "30-60 phút",
            "duration": "4-6 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa qua CYP2C9, CYP2C8), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ"
    },
    "Tramadol": {
        "group": "Analgesic - Opioid Agonist",
        "vietnamese_name": "Tramadol, Tramal",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Đau trung bình đến nặng",
            "Đau sau phẫu thuật",
            "Đau mạn tính"
        ],
        "contraindications": [
            "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
            "Dùng MAO inhibitor trong 14 ngày",
            "Co giật không kiểm soát",
            "Suy hô hấp nặng"
        ],
        "dosage": {
            "adult_po": "50-100mg mỗi 4-6 giờ (tối đa 400mg/ngày)",
            "adult_iv_im": "50-100mg mỗi 4-6 giờ",
            "elderly": "Liều thấp hơn (25-50mg)",
            "notes": "Nguy cơ co giật, đặc biệt với SSRI"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Buồn ngủ",
            "Co giật (đặc biệt với SSRI)",
            "Hội chứng serotonin (với SSRI)",
            "Táo bón",
            "Nguy cơ nghiện (thấp hơn opioid mạnh)"
        ],
        "interactions": [
            "SSRI/SNRI: tăng nguy cơ co giật và hội chứng serotonin",
            "MAO inhibitor: chống chỉ định",
            "Thuốc an thần: tăng tác dụng an thần",
            "Quinidine: tăng nồng độ tramadol"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Opioid tổng hợp, tác dụng kép. Vừa là opioid mu-receptor agonist (yếu hơn morphine) vừa ức chế tái hấp thu serotonin và norepinephrine. Giảm đau thông qua cả hai cơ chế. Độc tính opioid thấp hơn morphine nhưng vẫn có nguy cơ ức chế hô hấp và nghiện. Được dùng trong đau vừa đến nặng. Có nguy cơ co giật, đặc biệt khi dùng liều cao hoặc với các thuốc làm giảm ngưỡng co giật.",
        "monitoring": [
            "Mức độ đau (thang điểm đau)",
            "Nhịp thở và độ bão hòa oxy (SpO2) - nguy cơ ức chế hô hấp",
            "Mức độ ý thức",
            "Co giật (nguy cơ tăng ở liều cao, dùng với SSRI/SNRI, hoặc bệnh nhân có tiền sử co giật)",
            "Hội chứng serotonin (khi dùng với SSRI/SNRI: kích động, sốt, run, cứng cơ)",
            "Dấu hiệu nghiện/lệ thuộc",
            "Chức năng thận (điều chỉnh liều ở suy thận nặng)",
            "Chức năng gan (giảm liều ở suy gan nặng)"
        ],
        "precautions": [
            "Nguy cơ co giật - tăng ở: liều cao (>400mg/ngày), dùng với SSRI/SNRI, MAOI, tricyclic antidepressant, bệnh nhân có tiền sử co giật",
            "KHÔNG dùng với MAOI (nguy cơ hội chứng serotonin nặng, có thể tử vong)",
            "Thận trọng với SSRI/SNRI (nguy cơ hội chứng serotonin và co giật)",
            "Nguy cơ ức chế hô hấp - thấp hơn morphine nhưng vẫn có",
            "Không dùng với rượu, benzodiazepine, thuốc an thần (tăng nguy cơ ức chế hô hấp)",
            "Nguy cơ nghiện/lệ thuộc - chỉ dùng khi thực sự cần thiết, không dùng kéo dài",
            "Giảm liều ở suy thận nặng (CrCl < 30)",
            "Giảm liều ở suy gan nặng (giảm chuyển hóa)",
            "Liều tối đa: 400mg/ngày (để giảm nguy cơ co giật)",
            "Người cao tuổi: giảm liều (tăng nhạy cảm)",
            "Không dùng cho trẻ em < 12 tuổi (nguy cơ ức chế hô hấp)"
        ],
        "pharmacokinetics": {
            "half_life": "6 giờ (tramadol), 7 giờ (active metabolite O-desmethyltramadol)",
            "onset": "1 giờ (PO)",
            "duration": "4-6 giờ",
            "protein_binding": "20%",
            "metabolism": "Gan (CYP2D6, CYP3A4) → active metabolite O-desmethyltramadol",
            "clearance": "Chủ yếu qua thận, cần điều chỉnh ở suy thận nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Viên nén: tránh ẩm, để xa tầm tay trẻ em.",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt khi dùng với benzodiazepine, rượu, hoặc thuốc an thần khác. Nguy cơ co giật tăng ở liều cao và khi dùng với SSRI/SNRI. Nguy cơ hội chứng serotonin khi dùng với MAOI hoặc SSRI/SNRI, có thể tử vong.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa serotonin, tăng nguy cơ hội chứng serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng, có thể tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAOI ít nhất 14 ngày trước khi dùng tramadol"
                },
                {
                    "drug": "SSRI/SNRI (fluoxetine, sertraline, venlafaxine, duloxetine)",
                    "mechanism": "Tăng nồng độ serotonin, giảm ngưỡng co giật",
                    "effect": "Tăng nguy cơ co giật và hội chứng serotonin",
                    "management": "Tránh dùng hoặc dùng với thận trọng. Giảm liều tramadol. Theo dõi dấu hiệu co giật và hội chứng serotonin"
                }
            ],
            "moderate": [
                {
                    "drug": "Benzodiazepine, rượu, thuốc an thần",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, giảm liều và theo dõi hô hấp chặt chẽ"
                },
                {
                    "drug": "Quinidine, fluoxetine, paroxetine",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa tramadol thành O-desmethyltramadol",
                    "effect": "Giảm hiệu quả giảm đau (do giảm active metabolite)",
                    "management": "Cân nhắc dùng opioid khác không phụ thuộc CYP2D6 nếu cần"
                }
            ],
            "minor": [
                {
                    "drug": "Carbamazepine, phenytoin",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa tramadol",
                    "effect": "Giảm hiệu quả tramadol",
                    "management": "Có thể cần tăng liều tramadol"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor trong vòng 14 ngày",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Co giật không kiểm soát",
                "Suy hô hấp nặng hoặc suy hô hấp cấp tính",
                "Dị ứng tramadol"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều 50%",
                "Suy gan nặng - giảm liều 50%",
                "Dùng SSRI/SNRI - tăng nguy cơ co giật và hội chứng serotonin",
                "Tiền sử co giật - tăng nguy cơ",
                "Trẻ em <12 tuổi - nguy cơ ức chế hô hấp",
                "Người cao tuổi - giảm liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng nếu lợi ích > nguy cơ. Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng kéo dài trong thai kỳ. Tránh dùng trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Tramadol và O-desmethyltramadol bài tiết vào sữa mẹ. Nồng độ trong sữa mẹ tương đương khoảng 0.1% liều mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi cho con bú. Nếu dùng, theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ). Tránh dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 25-50%",
            "severe": "Giảm liều 50% hoặc tránh dùng",
            "notes": "Tramadol chuyển hóa ở gan qua CYP2D6 và CYP3A4 thành O-desmethyltramadol (active metabolite). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co giật (đặc biệt ở liều cao hoặc với SSRI/SNRI)",
                "Hội chứng serotonin (nếu dùng với SSRI/SNRI: kích động, sốt, run, cứng cơ)",
                "Hạ huyết áp",
                "Nhịp tim chậm",
                "Táo bón nặng"
            ],
            "antidote": "Naloxone (opioid antagonist) - có thể đảo ngược một phần tác dụng opioid nhưng không đảo ngược co giật hoặc hội chứng serotonin",
            "treatment": [
                "Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần)",
                "Naloxone: 0.4-2mg IV, có thể lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)",
                "Nếu co giật: benzodiazepine (diazepam, lorazepam) hoặc phenobarbital",
                "Nếu hội chứng serotonin: cyproheptadine, dantrolene nếu cần",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ (nhưng cần cẩn thận về nguy cơ hôn mê)",
                "Truyền dịch, hỗ trợ huyết động nếu hạ huyết áp",
                "Theo dõi liên tục: hô hấp, ý thức, ECG"
            ],
            "monitoring": "Nhịp thở, SpO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Theo dõi ít nhất 24 giờ do half-life dài của active metabolite (7 giờ)"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "indication": "Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức)",
                    "dose": "0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). Có thể dùng IM/SC nếu không có IV",
                    "notes": "Naloxone chỉ đảo ngược tác dụng opioid, KHÔNG đảo ngược co giật hoặc hội chứng serotonin. Half-life ngắn (1 giờ) nên có thể cần truyền liên tục nếu quá liều nặng."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn",
                "timing": "Mỗi 4-6 giờ khi cần. Liều tối đa: 400mg/ngày"
            },
            "iv": {
                "reconstitution": "Pha với 50-100ml NS hoặc D5W",
                "infusion_rate": "Truyền trong 15-30 phút. Hoặc tiêm trực tiếp IV chậm (2-3 phút)",
                "compatibility": ["NS", "D5W", "Ringer's Lactate"],
                "incompatibility": [],
                "notes": "Theo dõi hô hấp chặt chẽ khi dùng IV. Có thể gây co giật ở liều cao."
            },
            "im": {
                "notes": "Tiêm bắp sâu. Có thể gây đau tại chỗ tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ultram (tramadol)",
                "UpToDate - Tramadol: Drug information",
                "Lexicomp - Tramadol monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-06",
            "evidence_level": "High - FDA-approved, extensive clinical data"
        }
    },
    "Naproxen": {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Naproxen, Naprosyn",
        "administration": ["PO"],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Viêm cột sống dính khớp",
            "Đau bụng kinh",
            "Đau đầu do căng thẳng",
            "Gout cấp"
        ],
        "contraindications": [
            "Loét dạ dày tá tràng đang hoạt động",
            "Suy thận nặng",
            "Suy gan nặng",
            "Có thai (3 tháng cuối)",
            "Dị ứng NSAID/aspirin",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_pain": "250-500mg x 2 lần/ngày (tối đa 1.25g/ngày)",
            "adult_arthritis": "250-500mg x 2 lần/ngày (tối đa 1.5g/ngày)",
            "adult_dysmenorrhea": "500mg ngay khi có triệu chứng, sau đó 250mg mỗi 6-8 giờ",
            "adult_gout": "750mg ngay, sau đó 250mg mỗi 8 giờ",
            "notes": "Tác dụng kéo dài hơn ibuprofen. Uống với thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng"
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Đau đầu",
            "Ban da",
            "Nhạy cảm với ánh sáng"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Aspirin: giảm hiệu quả naproxen",
            "Lithium: tăng nồng độ lithium",
            "Methotrexate: tăng độc tính methotrexate"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Prostaglandin tham gia vào quá trình đau, viêm, sốt, bảo vệ niêm mạc dạ dày, và điều hòa thận. Tác dụng kháng viêm và giảm đau mạnh hơn ibuprofen. Thời gian bán thải dài hơn ibuprofen (12-17 giờ) → tác dụng kéo dài hơn, có thể dùng 2 lần/ngày.",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng)",
            "Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ",
            "Huyết áp (NSAID có thể tăng huyết áp)",
            "Chức năng gan (transaminase) nếu dùng lâu dài",
            "Dấu hiệu suy tim (giữ nước, phù)",
            "Lithium máu nếu dùng với lithium",
            "Nhạy cảm với ánh sáng (ban da khi tiếp xúc ánh nắng)"
        ],
        "precautions": [
            "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
            "Cân nhắc dùng PPI hoặc misoprostol nếu có nguy cơ loét dạ dày",
            "Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp",
            "Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)",
            "Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể",
            "Tránh tiếp xúc ánh nắng quá nhiều (nhạy cảm với ánh sáng)",
            "Thời gian bán thải dài → tích lũy ở bệnh nhân suy thận, suy gan"
        ],
        "pharmacokinetics": {
            "half_life": "12-17 giờ (dài hơn ibuprofen)",
            "onset": "30-60 phút",
            "duration": "8-12 giờ",
            "protein_binding": "99%",
            "clearance": "Gan (chuyển hóa qua CYP2C9, CYP1A2), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp",
        "black_box_warnings": "Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần"
                }
            ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận"
                },
                {
                    "drug": "Aspirin (liều thấp)",
                    "mechanism": "Naproxen có thể ức chế tác dụng chống kết tập tiểu cầu của aspirin",
                    "effect": "Giảm hiệu quả phòng ngừa nhồi máu cơ tim của aspirin",
                    "management": "Dùng aspirin ít nhất 2 giờ trước naproxen, hoặc cân nhắc NSAID khác"
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Giảm thải trừ lithium qua thận",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính",
                    "management": "Theo dõi lithium máu thường xuyên. Có thể cần giảm liều lithium"
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Giảm thải trừ methotrexate qua thận",
                    "effect": "Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ"
                }
            ],
            "minor": [
                {
                    "drug": "Corticosteroid",
                    "mechanism": "Tăng nguy cơ loét dạ dày",
                    "effect": "Tăng nguy cơ chảy máu dạ dày",
                    "management": "Cân nhắc dùng PPI hoặc misoprostol để bảo vệ dạ dày"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng naproxen hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều",
                "Suy gan nặng - thận trọng, giảm liều",
                "Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn",
                "Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch",
                "Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp",
                "Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.",
            "lactation": {
                "safety": "Compatible",
                "details": "Naproxen bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <1% liều mẹ. Half-life dài (12-17 giờ) nhưng nồng độ trong sữa mẹ thấp nên ít ảnh hưởng đến trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với liều ngắn hạn. Theo dõi trẻ về dấu hiệu bất thường (hiếm)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50%",
            "severe": "Tránh dùng hoặc giảm liều mạnh",
            "notes": "Naproxen chuyển hóa ở gan qua CYP2C9 và CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, naproxen ít gây độc gan hơn một số NSAID khác (như diclofenac)."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, đau bụng",
                "Chóng mặt, nhức đầu",
                "Lú lẫn, buồn ngủ",
                "Ức chế hô hấp (hiếm, ở liều rất cao)",
                "Hạ huyết áp",
                "Suy thận cấp",
                "Chảy máu dạ dày",
                "Co giật (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi chức năng thận (creatinine, BUN), điện giải",
                "Theo dõi huyết áp, nhịp tim",
                "Hỗ trợ hô hấp nếu có ức chế hô hấp (hiếm)",
                "Truyền dịch nếu hạ huyết áp, suy thận",
                "Theo dõi dấu hiệu chảy máu dạ dày",
                "Điều trị hỗ trợ triệu chứng"
            ],
            "monitoring": "Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 12-24 giờ do half-life dài (12-17 giờ)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
                "timing": "Mỗi 8-12 giờ (do half-life dài). Có thể dùng 2 lần/ngày. Dùng với bữa ăn để giảm tác dụng phụ dạ dày."
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
                "FDA Drug Label - Naprosyn (naproxen)",
                "UpToDate - Naproxen: Drug information",
                "Lexicomp - Naproxen monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-06",
            "evidence_level": "High - FDA-approved, extensive clinical data"
        }
    },
    "Diclofenac": {
        "group": "Analgesic - NSAID",
        "vietnamese_name": "Diclofenac, Voltaren",
        "administration": ["PO", "IM", "Topical"],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Viêm khớp dạng thấp",
            "Viêm khớp xương khớp",
            "Đau sau phẫu thuật",
            "Đau do chấn thương",
            "Viêm gân (topical)"
        ],
        "contraindications": [
            "Loét dạ dày tá tràng đang hoạt động",
            "Suy thận nặng",
            "Suy gan nặng",
            "Có thai (3 tháng cuối)",
            "Dị ứng NSAID/aspirin",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_po": "50mg x 2-3 lần/ngày hoặc 75-100mg x 1 lần/ngày (extended release)",
            "adult_im": "75mg IM x 1-2 lần/ngày (tối đa 3 ngày)",
            "adult_topical": "Bôi 2-4g x 3-4 lần/ngày",
            "notes": "Hiệu quả cao nhưng nguy cơ tác dụng phụ cao"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng"
        },
        "side_effects": [
            "Chảy máu dạ dày (cao hơn các NSAID khác)",
            "Suy thận",
            "Tăng huyết áp",
            "Phù",
            "Tăng men gan",
            "Đau đầu",
            "Ban da"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận",
            "Digoxin: tăng nồng độ digoxin",
            "Methotrexate: tăng độc tính methotrexate"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), ưu tiên COX-2 hơn một số NSAID khác. Giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Prostaglandin tham gia vào quá trình đau, viêm, sốt, bảo vệ niêm mạc dạ dày, và điều hòa thận. Tác dụng kháng viêm và giảm đau mạnh. Có nhiều dạng: uống, tiêm bắp, bôi tại chỗ. Dạng bôi tại chỗ có ít tác dụng phụ hệ thống hơn.",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng) - nguy cơ cao hơn các NSAID khác",
            "Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ",
            "Huyết áp (NSAID có thể tăng huyết áp)",
            "Chức năng gan (ALT, AST) - diclofenac có nguy cơ tăng men gan cao hơn",
            "Dấu hiệu suy tim (giữ nước, phù)",
            "Lithium máu nếu dùng với lithium",
            "Cyclosporine levels nếu dùng với cyclosporine"
        ],
        "precautions": [
            "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
            "Cân nhắc dùng PPI hoặc misoprostol nếu có nguy cơ loét dạ dày (nguy cơ cao)",
            "Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp",
            "Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)",
            "Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể",
            "Dạng bôi tại chỗ: ít tác dụng phụ hệ thống, phù hợp cho đau cục bộ",
            "IM: chỉ dùng tối đa 3 ngày, không dùng lâu dài",
            "Theo dõi chức năng gan chặt chẽ (nguy cơ tăng men gan)"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (ngắn), nhưng tác dụng kéo dài do tích lũy trong dịch khớp",
            "onset": "30-60 phút (PO), 10-15 phút (IM)",
            "duration": "8-12 giờ",
            "protein_binding": "99.7%",
            "clearance": "Gan (chuyển hóa qua CYP2C9, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng bôi: bảo quản ở nhiệt độ phòng, không làm lạnh.",
        "black_box_warnings": "Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao. Diclofenac có nguy cơ tăng men gan và chảy máu dạ dày cao hơn một số NSAID khác.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin, các thuốc chống đông khác",
                    "mechanism": "Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu nặng, tăng INR",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần"
                }
            ],
            "moderate": [
                {
                    "drug": "ACE inhibitor, ARB",
                    "mechanism": "Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận"
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Giảm thải trừ digoxin qua thận",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính (nhịp tim chậm, block nhĩ thất)",
                    "management": "Theo dõi digoxin máu thường xuyên. Có thể cần giảm liều digoxin"
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Giảm thải trừ methotrexate qua thận",
                    "effect": "Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ"
                },
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Tăng nguy cơ độc tính thận",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Theo dõi creatinine, BUN chặt chẽ. Cân nhắc NSAID khác hoặc giảm liều cyclosporine"
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng diclofenac hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)",
                "Loét dạ dày tá tràng đang hoạt động",
                "Tam cá nguyệt 3 thai kỳ (3 tháng cuối)",
                "Suy gan nặng (do nguy cơ tăng men gan cao)",
                "Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều",
                "Suy gan trung bình - thận trọng, theo dõi men gan chặt chẽ",
                "Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn",
                "Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch",
                "Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp",
                "Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, đặc biệt chảy máu dạ dày"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.",
            "lactation": {
                "safety": "Compatible",
                "details": "Diclofenac bài tiết vào sữa mẹ ở nồng độ rất thấp (<0.1% liều mẹ). An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Dạng bôi tại chỗ: ít ảnh hưởng hệ thống, an toàn hơn."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi nhưng theo dõi men gan",
            "moderate": "Thận trọng, giảm liều 25-50%, theo dõi men gan chặt chẽ",
            "severe": "TRÁNH DÙNG (chống chỉ định)",
            "notes": "Diclofenac chuyển hóa ở gan qua CYP2C9 và CYP3A4. Có nguy cơ tăng men gan cao hơn các NSAID khác. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, đau bụng",
                "Chóng mặt, nhức đầu",
                "Lú lẫn, buồn ngủ",
                "Hạ huyết áp",
                "Suy thận cấp",
                "Chảy máu dạ dày",
                "Tăng men gan (ALT, AST)",
                "Co giật (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi chức năng thận (creatinine, BUN), điện giải",
                "Theo dõi chức năng gan (ALT, AST) - diclofenac có nguy cơ cao",
                "Theo dõi huyết áp, nhịp tim",
                "Truyền dịch nếu hạ huyết áp, suy thận",
                "Theo dõi dấu hiệu chảy máu dạ dày",
                "Điều trị hỗ trợ triệu chứng"
            ],
            "monitoring": "Huyết áp, nhịp tim, ý thức, creatinine, BUN, ALT/AST, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 12-24 giờ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày (quan trọng với diclofenac do nguy cơ cao)",
                "timing": "Mỗi 8-12 giờ. Dùng với bữa ăn để giảm tác dụng phụ dạ dày."
            },
            "im": {
                "notes": "Tiêm bắp sâu. Chỉ dùng tối đa 3 ngày, không dùng lâu dài. Có thể gây đau tại chỗ tiêm."
            },
            "topical": {
                "notes": "Dạng bôi tại chỗ: Bôi 2-4g x 3-4 lần/ngày lên vùng đau. Ít tác dụng phụ hệ thống hơn dạng uống. Không bôi trên vùng da bị tổn thương hoặc niêm mạc."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Voltaren (diclofenac)",
                "UpToDate - Diclofenac: Drug information",
                "Lexicomp - Diclofenac monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-06",
            "evidence_level": "High - FDA-approved, extensive clinical data"
        }
    },
    "Morphine": {
        "group": "Analgesic - Opioid Agonist (Strong)",
        "vietnamese_name": "Morphine",
        "administration": ["PO", "IV", "IM", "SC"],
        "indications": [
            "Đau nặng (ung thư, sau phẫu thuật)",
            "Đau cấp tính nặng",
            "Đau mạn tính nặng",
            "Khó thở do suy tim",
            "Cơn đau do hồi sức"
        ],
        "contraindications": [
            "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
            "Suy hô hấp nặng",
            "Hen phế quản nặng",
            "Tắc ruột cơ học",
            "Tăng áp lực nội sọ",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_po_immediate": "10-30mg mỗi 4 giờ khi cần",
            "adult_po_extended": "15-30mg x 2 lần/ngày (MS Contin)",
            "adult_iv": "2.5-5mg IV mỗi 3-4 giờ hoặc 0.8-10mg/giờ truyền liên tục",
            "adult_im_sc": "5-15mg mỗi 4 giờ",
            "elderly": "Giảm liều 25-50%",
            "notes": "Thuốc chuẩn vàng cho đau nặng. Theo dõi hô hấp chặt chẽ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, tăng khoảng cách liều"
        },
        "side_effects": [
            "Ức chế hô hấp (nguy hiểm)",
            "Buồn nôn, nôn",
            "Táo bón (rất thường gặp)",
            "Ngứa",
            "Buồn ngủ, lú lẫn",
            "Co đồng tử (miosis)",
            "Hạ huyết áp",
            "Ức chế tiết ADH (SIADH)",
            "Nguy cơ nghiện, lệ thuộc"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Rượu: tăng nguy cơ ức chế hô hấp",
            "Cimetidine: tăng nồng độ morphine"
        ],
        "pregnancy": "C - D trong 3 tháng cuối (gây hội chứng cai ở trẻ sơ sinh)",
        "mechanism_of_action": "Opioid mu-receptor agonist mạnh. Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. Tăng ngưỡng đau, giảm đáp ứng cảm xúc với đau. Tác động lên brainstem → giảm trung tâm hô hấp. Tác động lên đường tiêu hóa → giảm nhu động ruột, tăng trương lực cơ thắt.",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - quan trọng nhất",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim (có thể gây hạ huyết áp, nhịp tim chậm)",
            "Co đồng tử (miosis) - dấu hiệu đặc trưng của opioid",
            "Dấu hiệu táo bón (rất thường gặp, cần dự phòng)",
            "Dấu hiệu nghiện/lệ thuộc (nếu dùng kéo dài)",
            "Chức năng thận (tích lũy ở suy thận do tích tụ active metabolite)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt ở liều đầu tiên, người cao tuổi, suy thận, suy gan",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, rượu, thuốc an thần (tăng nguy cơ ức chế hô hấp nặng)",
            "Dự phòng táo bón từ đầu (dùng thuốc nhuận tràng)",
            "Thận trọng ở suy thận (tích lũy active metabolite morphine-6-glucuronide - có thể gây ức chế hô hấp kéo dài)",
            "Thận trọng ở suy gan (giảm chuyển hóa)",
            "Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài - cần đánh giá định kỳ",
            "Không dùng trong tăng áp lực nội sọ (tăng CO2 → tăng áp lực nội sọ)",
            "Không dùng trong tắc ruột cơ học (tăng trương lực cơ thắt)"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "IV: 5-10 phút; IM: 15-30 phút; PO: 30-60 phút",
            "duration": "3-7 giờ (IV), 4-7 giờ (IM), 3-6 giờ (PO)",
            "protein_binding": "20-35%",
            "clearance": "Chủ yếu qua thận (morphine-6-glucuronide tích lũy ở suy thận)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em (nguy cơ quá liều).",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt khi dùng với benzodiazepine hoặc rượu. Morphine có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương, đặc biệt trung tâm hô hấp",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều morphine, theo dõi hô hấp liên tục, có naloxone sẵn sàng"
                },
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng tương tác nghiêm trọng",
                    "effect": "Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng morphine"
                }
            ],
            "moderate": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế chuyển hóa morphine qua gan",
                    "effect": "Tăng nồng độ morphine, tăng nguy cơ ức chế hô hấp",
                    "management": "Giảm liều morphine 25-50%. Theo dõi hô hấp chặt chẽ"
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng enzyme chuyển hóa morphine",
                    "effect": "Giảm hiệu quả morphine",
                    "management": "Có thể cần tăng liều morphine"
                },
                {
                    "drug": "Phenothiazine, haloperidol",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ ức chế hô hấp, hạ huyết áp",
                    "management": "Thận trọng. Giảm liều morphine, theo dõi hô hấp"
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng morphine hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng hoặc suy hô hấp cấp tính",
                "Hen phế quản nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ (do tăng CO2)",
                "Dùng MAO inhibitor trong vòng 14 ngày"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều 50-75%, tăng khoảng cách liều (tích lũy morphine-6-glucuronide)",
                "Suy gan nặng - giảm liều 25-50% (giảm chuyển hóa)",
                "Người cao tuổi - giảm liều 25-50% (tăng nhạy cảm)",
                "Trẻ em <12 tuổi - nguy cơ ức chế hô hấp",
                "Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện",
                "Suy tim - tăng nguy cơ ức chế hô hấp",
                "Bệnh phổi tắc nghẽn mạn tính (COPD) - tăng nguy cơ ức chế hô hấp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ cho điều trị đau nặng. Tam cá nguyệt 3: Nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng kéo dài. Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Morphine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ tương đương khoảng 0.8-3% liều mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ, đặc biệt ở trẻ sơ sinh.",
                "recommendation": "Thận trọng khi cho con bú. Nếu dùng, theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ, bú kém). Tránh dùng liều cao hoặc kéo dài. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 25-50%",
            "severe": "Giảm liều 50% hoặc tránh dùng",
            "notes": "Morphine chuyển hóa ở gan qua glucuronidation thành morphine-6-glucuronide (active, mạnh hơn morphine) và morphine-3-glucuronide (inactive). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm <12 lần/phút, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis) - dấu hiệu đặc trưng",
                "Hạ huyết áp",
                "Nhịp tim chậm",
                "Táo bón nặng",
                "Co giật (hiếm, ở trẻ em hoặc liều rất cao)"
            ],
            "antidote": "Naloxone (opioid antagonist) - đảo ngược tác dụng opioid",
            "treatment": [
                "Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần) - QUAN TRỌNG NHẤT",
                "Naloxone: 0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)",
                "Nếu không có IV: 0.4-2mg IM/SC, có thể lặp lại",
                "Nếu quá liều nặng: có thể cần truyền naloxone liên tục (0.4-0.8mg/giờ) do half-life ngắn (1 giờ) so với morphine (2-4 giờ)",
                "Theo dõi hô hấp liên tục ít nhất 24 giờ (do half-life dài của morphine-6-glucuronide)",
                "Hỗ trợ huyết động: truyền dịch, vasopressor nếu hạ huyết áp",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ (nhưng cần cẩn thận về nguy cơ hôn mê)",
                "Theo dõi ECG, huyết áp, nhịp tim liên tục"
            ],
            "monitoring": "Nhịp thở, SpO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Theo dõi ít nhất 24 giờ do half-life dài của active metabolite morphine-6-glucuronide"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "indication": "Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức, hạ huyết áp)",
                    "dose": "0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). IM/SC: 0.4-2mg nếu không có IV. Truyền liên tục: 0.4-0.8mg/giờ nếu quá liều nặng",
                    "notes": "Naloxone có half-life ngắn (1 giờ) so với morphine (2-4 giờ) và morphine-6-glucuronide (dài hơn). Có thể cần truyền liên tục hoặc lặp lại liều để tránh tái phát ức chế hô hấp."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn",
                "timing": "Mỗi 4 giờ khi cần (immediate release) hoặc 2 lần/ngày (extended release MS Contin)"
            },
            "iv": {
                "reconstitution": "Pha với 50-100ml NS hoặc D5W cho truyền liên tục. Hoặc tiêm trực tiếp IV",
                "infusion_rate": "Tiêm IV chậm trong 2-5 phút. Truyền liên tục: 0.8-10mg/giờ (tùy liều)",
                "compatibility": ["NS", "D5W", "Ringer's Lactate"],
                "incompatibility": ["Alkaline solutions"],
                "notes": "Theo dõi hô hấp chặt chẽ khi dùng IV. Cần có naloxone sẵn sàng. Khởi đầu với liều thấp, tăng dần."
            },
            "im": {
                "notes": "Tiêm bắp sâu. Có thể gây đau tại chỗ tiêm. Tác dụng bắt đầu 15-30 phút."
            },
            "sc": {
                "notes": "Tiêm dưới da. Có thể gây kích ứng tại chỗ. Tác dụng bắt đầu 15-30 phút."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Morphine sulfate",
                "UpToDate - Morphine: Drug information",
                "Lexicomp - Morphine monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-06",
            "evidence_level": "High - FDA-approved, extensive clinical data, gold standard for severe pain"
        }
    },
    "Codeine": {
        "group": "Analgesic - Opioid Agonist (Weak)",
        "vietnamese_name": "Codeine",
        "administration": ["PO"],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Ho không hiệu quả (chỉ định hạn chế)",
            "Đau sau phẫu thuật nhỏ"
        ],
        "contraindications": [
            "Ngộ độc cấp tính opioid",
            "Suy hô hấp nặng",
            "Hen phế quản nặng",
            "Tắc ruột cơ học",
            "Trẻ em <12 tuổi (ho)",
            "Trẻ em <18 tuổi sau cắt amidan/VA"
        ],
        "dosage": {
            "adult_pain": "15-60mg mỗi 4-6 giờ (tối đa 360mg/ngày)",
            "adult_cough": "10-20mg mỗi 4-6 giờ (tối đa 120mg/ngày)",
            "notes": "Prodrug của morphine, cần CYP2D6 để chuyển hóa. Một số người không có enzyme (poor metabolizers) → không hiệu quả. Ultra-rapid metabolizers → nguy cơ quá liều"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng hoặc giảm liều 50%"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Táo bón",
            "Buồn ngủ",
            "Chóng mặt",
            "Ức chế hô hấp (liều cao)",
            "Ngứa",
            "Nguy cơ nghiện"
        ],
        "interactions": [
            "Thuốc an thần: tăng tác dụng an thần",
            "Rượu: tăng nguy cơ ức chế hô hấp",
            "CYP2D6 inhibitors: giảm hiệu quả",
            "Quinidine: giảm chuyển hóa thành morphine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Prodrug của morphine. Codeine tự thân không có tác dụng giảm đau, cần chuyển hóa qua enzyme CYP2D6 ở gan để tạo thành morphine (active metabolite). Morphine gắn với mu-opioid receptors, ức chế dẫn truyền đau, tăng ngưỡng đau, giảm đáp ứng với kích thích đau. Tác dụng yếu hơn morphine trực tiếp. Có tác dụng chống ho do ức chế trung tâm ho. Hiệu quả phụ thuộc vào genotype CYP2D6 (poor metabolizers → không hiệu quả, ultra-rapid metabolizers → nguy cơ quá liều).",
        "monitoring": [
            "Mức độ đau (thang điểm đau) - đánh giá hiệu quả",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm) - đặc biệt ở ultra-rapid metabolizers",
            "Huyết áp và nhịp tim (có thể gây hạ huyết áp, nhịp tim chậm)",
            "Dấu hiệu táo bón (rất thường gặp, cần dự phòng)",
            "Dấu hiệu nghiện/lệ thuộc (nếu dùng kéo dài)",
            "Chức năng thận (tích lũy ở suy thận)",
            "Đáp ứng với thuốc (nếu không hiệu quả có thể do poor metabolizer)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp - đặc biệt ở ultra-rapid metabolizers (tạo nhiều morphine) hoặc dùng liều cao",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Tránh dùng với benzodiazepine, rượu, thuốc an thần (tăng nguy cơ ức chế hô hấp)",
            "Dự phòng táo bón từ đầu (dùng thuốc nhuận tràng)",
            "Thận trọng ở suy thận (tích lũy)",
            "Thận trọng ở suy gan (giảm chuyển hóa)",
            "Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài - cần đánh giá định kỳ",
            "Không dùng trong tăng áp lực nội sọ",
            "Không dùng trong tắc ruột cơ học",
            "Nếu không hiệu quả → có thể do poor CYP2D6 metabolizer, cân nhắc dùng opioid khác",
            "Trẻ em <12 tuổi: không dùng cho ho (nguy cơ ức chế hô hấp)",
            "Trẻ em <18 tuổi sau cắt amidan/VA: chống chỉ định (nguy cơ ức chế hô hấp nghiêm trọng)"
        ],
        "pharmacokinetics": {
            "half_life": "2.5-4 giờ",
            "onset": "30-60 phút",
            "duration": "4-6 giờ",
            "protein_binding": "7-25%",
            "metabolism": "Gan: chuyển hóa qua CYP2D6 thành morphine (10% codeine → morphine), CYP3A4 thành norcodeine (không hoạt động)",
            "clearance": "Chủ yếu qua thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em (nguy cơ quá liều).",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt ở ultra-rapid metabolizers (tạo nhiều morphine) hoặc khi dùng với benzodiazepine/rượu. Trẻ em <12 tuổi: không dùng cho ho. Trẻ em <18 tuổi sau cắt amidan/VA: chống chỉ định (nguy cơ ức chế hô hấp nghiêm trọng, có thể tử vong).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương, đặc biệt trung tâm hô hấp",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều codeine, theo dõi hô hấp liên tục, có naloxone sẵn sàng"
                }
            ],
            "moderate": [
                {
                    "drug": "CYP2D6 inhibitors (quinidine, fluoxetine, paroxetine)",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa codeine thành morphine",
                    "effect": "Giảm hiệu quả giảm đau (do giảm active metabolite morphine)",
                    "management": "Cân nhắc dùng opioid khác không phụ thuộc CYP2D6 (như morphine, oxycodone)"
                },
                {
                    "drug": "CYP2D6 inducers (rifampin)",
                    "mechanism": "Cảm ứng CYP2D6, tăng chuyển hóa codeine thành morphine",
                    "effect": "Tăng nguy cơ quá liều (tạo nhiều morphine)",
                    "management": "Thận trọng. Giảm liều codeine. Theo dõi dấu hiệu quá liều"
                },
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng tương tác nghiêm trọng",
                    "effect": "Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng",
                    "management": "Thận trọng. Ngừng MAOI ít nhất 14 ngày trước khi dùng codeine"
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng codeine hoặc opioid",
                "Ngộ độc cấp tính opioid",
                "Suy hô hấp nặng hoặc suy hô hấp cấp tính",
                "Hen phế quản nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Trẻ em <12 tuổi (khi dùng cho ho)",
                "Trẻ em <18 tuổi sau cắt amidan/VA (chống chỉ định tuyệt đối)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - tránh dùng hoặc giảm liều 50%",
                "Suy gan nặng - giảm liều (giảm chuyển hóa)",
                "Người cao tuổi - giảm liều (tăng nhạy cảm)",
                "Ultra-rapid CYP2D6 metabolizers - tăng nguy cơ quá liều (tạo nhiều morphine)",
                "Poor CYP2D6 metabolizers - không hiệu quả (không tạo đủ morphine)",
                "Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện",
                "Tăng áp lực nội sọ - tăng nguy cơ ức chế hô hấp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng nếu lợi ích > nguy cơ. Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng kéo dài trong thai kỳ. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Codeine và morphine (metabolite) bài tiết vào sữa mẹ. Nồng độ trong sữa mẹ tương đương khoảng 0.5-2% liều mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ, đặc biệt ở trẻ sơ sinh hoặc mẹ là ultra-rapid metabolizer (tạo nhiều morphine).",
                "recommendation": "Thận trọng khi cho con bú. Nếu dùng, theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ, bú kém). Tránh dùng liều cao hoặc kéo dài. Dùng liều thấp nhất hiệu quả. Nếu mẹ là ultra-rapid metabolizer, tránh dùng codeine khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "Tránh dùng hoặc giảm liều mạnh",
            "notes": "Codeine chuyển hóa ở gan qua CYP2D6 thành morphine (active metabolite) và CYP3A4 thành norcodeine (inactive). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Ultra-rapid metabolizers có nguy cơ quá liều cao hơn."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm, ngừng thở) - đặc biệt ở ultra-rapid metabolizers",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis) - dấu hiệu đặc trưng",
                "Hạ huyết áp",
                "Nhịp tim chậm",
                "Táo bón nặng",
                "Co giật (hiếm, ở trẻ em hoặc liều rất cao)"
            ],
            "antidote": "Naloxone (opioid antagonist) - đảo ngược tác dụng opioid",
            "treatment": [
                "Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần) - QUAN TRỌNG NHẤT",
                "Naloxone: 0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)",
                "Nếu không có IV: 0.4-2mg IM/SC, có thể lặp lại",
                "Nếu quá liều nặng: có thể cần truyền naloxone liên tục do half-life ngắn (1 giờ)",
                "Theo dõi hô hấp liên tục ít nhất 12-24 giờ",
                "Hỗ trợ huyết động: truyền dịch, vasopressor nếu hạ huyết áp",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ (nhưng cần cẩn thận về nguy cơ hôn mê)",
                "Theo dõi ECG, huyết áp, nhịp tim liên tục"
            ],
            "monitoring": "Nhịp thở, SpO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Theo dõi ít nhất 12-24 giờ. Đặc biệt chú ý ở ultra-rapid metabolizers (tạo nhiều morphine)"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "indication": "Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức, hạ huyết áp)",
                    "dose": "0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). IM/SC: 0.4-2mg nếu không có IV. Truyền liên tục: 0.4-0.8mg/giờ nếu quá liều nặng",
                    "notes": "Naloxone có half-life ngắn (1 giờ). Có thể cần truyền liên tục hoặc lặp lại liều để tránh tái phát ức chế hô hấp, đặc biệt ở ultra-rapid metabolizers."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn",
                "timing": "Mỗi 4-6 giờ khi cần. Liều tối đa: 360mg/ngày (đau), 120mg/ngày (ho)"
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
                "FDA Drug Label - Codeine sulfate",
                "UpToDate - Codeine: Drug information",
                "Lexicomp - Codeine monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-06",
            "evidence_level": "High - FDA-approved, extensive clinical data. Note: efficacy depends on CYP2D6 genotype"
        }
    },
    "Sumatriptan": {
        "group": "Analgesic - Antimigraine (5-HT1 Receptor Agonist)",
        "vietnamese_name": "Sumatriptan, Imitrex",
        "administration": ["PO", "SC", "Nasal"],
        "indications": [
            "Migraine có tiền triệu (aura) hoặc không",
            "Cluster headache"
        ],
        "contraindications": [
            "Bệnh mạch vành",
            "Nhồi máu cơ tim",
            "Đau thắt ngực không ổn định",
            "Đột quỵ, TIA",
            "Bệnh mạch máu ngoại biên",
            "Tăng huyết áp không kiểm soát",
            "Dùng MAO inhibitor trong 14 ngày",
            "Dùng ergotamine trong 24 giờ"
        ],
        "dosage": {
            "adult_po": "25-100mg, có thể lặp sau 2 giờ (tối đa 200mg/ngày)",
            "adult_sc": "6mg SC, có thể lặp sau 1 giờ (tối đa 12mg/ngày)",
            "adult_nasal": "5-20mg xịt mũi, có thể lặp sau 2 giờ (tối đa 40mg/ngày)",
            "notes": "Dùng ngay khi có triệu chứng migraine. Không dùng để phòng ngừa"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Cảm giác nóng, đỏ, ngứa (SC injection)",
            "Đau ngực, khó thở (tương tự đau thắt ngực)",
            "Nhức đầu",
            "Chóng mặt",
            "Buồn nôn",
            "Co thắt cơ",
            "Yếu, mệt mỏi",
            "Nguy cơ đau tim (hiếm nhưng nguy hiểm)"
        ],
        "interactions": [
            "Ergotamine/Dihydroergotamine: chống chỉ định (trong 24 giờ)",
            "MAO inhibitor: chống chỉ định (trong 14 ngày)",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin",
            "Thuốc ức chế CYP2D6: tăng nồng độ sumatriptan"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "5-HT1B/1D receptor agonist (selective serotonin receptor agonist, triptan). Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine). Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua cả hai cơ chế: co mạch và ức chế viêm thần kinh. Tác dụng nhanh (10-30 phút SC, 30-60 phút PO).",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)",
            "Dấu hiệu co mạch: đau ngực, khó thở, đau cổ, hàm (có thể giống đau thắt ngực)",
            "Dấu hiệu bệnh mạch vành: đau ngực, khó thở, đau lan (nguy hiểm)",
            "Huyết áp (có thể tăng nhẹ)",
            "Dấu hiệu hội chứng serotonin: kích động, tăng thân nhiệt, tăng phản xạ (nếu dùng với SSRI/SNRI)",
            "Dấu hiệu quá liều: co mạch nặng, thiếu máu cục bộ"
        ],
        "precautions": [
            "Dùng ngay khi có triệu chứng migraine (không chờ đến khi đau nặng)",
            "Không dùng để phòng ngừa - chỉ dùng để cắt cơn",
            "CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên",
            "CHỐNG CHỈ ĐỊNH trong tăng huyết áp không kiểm soát",
            "Không dùng với ergotamine/dihydroergotamine trong 24 giờ - tăng nguy cơ co mạch nặng",
            "Không dùng với MAO inhibitor trong 14 ngày - tăng nguy cơ tác dụng phụ",
            "Thận trọng khi dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin",
            "Nếu đau ngực, khó thở → ngừng ngay và đánh giá",
            "Không vượt quá liều tối đa (200mg/ngày PO, 12mg/ngày SC, 40mg/ngày nasal)",
            "Nếu không đáp ứng sau 2 liều → không dùng thêm, đánh giá lại chẩn đoán"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ",
            "onset": "SC: 10-15 phút; PO: 30-60 phút; Nasal: 15-30 phút",
            "duration": "2-4 giờ",
            "protein_binding": "14-21%",
            "metabolism": "Gan (chuyển hóa qua MAO-A, một phần qua CYP2D6)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng SC: bảo quản trong tủ lạnh, để ở nhiệt độ phòng trước khi dùng.",
        "black_box_warnings": "Nguy cơ co mạch nghiêm trọng, có thể gây nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ, có thể tử vong. CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên, tăng huyết áp không kiểm soát. Không dùng với ergotamine trong 24 giờ. Nếu có đau ngực, khó thở → ngừng ngay và đánh giá.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ergotamine, Dihydroergotamine",
                    "mechanism": "Cả hai đều gây co mạch, tăng nguy cơ co mạch nghiêm trọng",
                    "effect": "Tăng nguy cơ co mạch nghiêm trọng, nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ."
                },
                {
                    "drug": "MAO Inhibitors (Phenelzine, Tranylcypromine)",
                    "mechanism": "Ức chế MAO-A (chuyển hóa sumatriptan), tăng nồng độ sumatriptan",
                    "effect": "Tăng nguy cơ tác dụng phụ, co mạch nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với MAO inhibitor trong 14 ngày."
                }
            ],
            "moderate": [
                {
                    "drug": "SSRI/SNRI (Fluoxetine, Sertraline, Venlafaxine)",
                    "mechanism": "Cả hai đều tăng serotonin, tăng nguy cơ hội chứng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin (kích động, tăng thân nhiệt, tăng phản xạ)",
                    "management": "Thận trọng, theo dõi dấu hiệu hội chứng serotonin. Có thể cần tránh dùng cùng."
                },
                {
                    "drug": "Thuốc ức chế CYP2D6",
                    "mechanism": "Giảm chuyển hóa sumatriptan, tăng nồng độ",
                    "effect": "Tăng tác dụng phụ, tăng nguy cơ co mạch",
                    "management": "Thận trọng, theo dõi tác dụng phụ. Có thể cần giảm liều sumatriptan."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với sumatriptan hoặc các thành phần khác",
                "Bệnh mạch vành (CAD)",
                "Nhồi máu cơ tim",
                "Đau thắt ngực không ổn định",
                "Đột quỵ, TIA",
                "Bệnh mạch máu ngoại biên",
                "Tăng huyết áp không kiểm soát",
                "Dùng MAO inhibitor trong 14 ngày",
                "Dùng ergotamine/dihydroergotamine trong 24 giờ"
            ],
            "tương_đối": [
                "Bệnh tim mạch khác (suy tim, loạn nhịp) - thận trọng, đánh giá tim mạch trước",
                "Tăng huyết áp đã kiểm soát - thận trọng",
                "Tiền sử đau thắt ngực - thận trọng",
                "Dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin",
                "Suy thận nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Sumatriptan là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Sumatriptan được sử dụng trong thai kỳ để điều trị migraine và có vẻ an toàn. Tuy nhiên, có nguy cơ co mạch có thể ảnh hưởng đến thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng thận trọng.",
            "lactation": {
                "safety": "Compatible",
                "details": "Sumatriptan bài tiết vào sữa mẹ với nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng - sumatriptan chuyển hóa qua gan (MAO-A, CYP2D6), có thể tích lũy",
            "severe": "Thận trọng - có thể tích lũy, tăng tác dụng phụ",
            "notes": "Sumatriptan chuyển hóa qua gan (MAO-A, một phần CYP2D6). Ở suy gan, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ tác dụng phụ. Có thể cần giảm liều."
        },
        "overdose_management": {
            "symptoms": [
                "Co mạch nghiêm trọng",
                "Nhồi máu cơ tim",
                "Đột quỵ",
                "Thiếu máu cục bộ",
                "Đau ngực nặng",
                "Khó thở nặng",
                "Tăng huyết áp nghiêm trọng",
                "Hội chứng serotonin (nếu dùng với SSRI/SNRI)",
                "Kích động, lú lẫn"
            ],
            "antidote": "Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch, nhưng thận trọng.",
            "treatment": [
                "Ngừng ngay sumatriptan",
                "Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)",
                "Theo dõi tim mạch liên tục (ECG, huyết áp, SpO2)",
                "Điều trị nhồi máu cơ tim nếu có (theo protocol)",
                "Điều trị đột quỵ nếu có (theo protocol)",
                "Nitroglycerin để giãn mạch (thận trọng, có thể gây hạ huyết áp)",
                "Điều trị hội chứng serotonin nếu có (dantrolene, benzodiazepine)",
                "Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)",
                "Theo dõi và điều trị triệu chứng"
            ],
            "monitoring": "Theo dõi liên tục: ECG, huyết áp, SpO2, dấu hiệu co mạch, dấu hiệu nhồi máu cơ tim, dấu hiệu đột quỵ, dấu hiệu hội chứng serotonin. Theo dõi ít nhất 24 giờ do thời gian bán thải (2 giờ) và nguy cơ biến chứng."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Nitroglycerin",
                    "mechanism": "Giãn mạch, đối kháng tác dụng co mạch",
                    "indication": "Quá liều gây co mạch nghiêm trọng, đau ngực",
                    "caution": "Thận trọng, có thể gây hạ huyết áp. Chỉ dùng khi có co mạch nghiêm trọng."
                }
            ],
            "notes": "Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch trong trường hợp quá liều nghiêm trọng, nhưng thận trọng. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Dùng ngay khi có triệu chứng migraine. Không dùng để phòng ngừa. Có thể lặp sau 2 giờ nếu cần (tối đa 200mg/ngày)."
            },
            "iv": None,
            "sc": {
                "technique": "Dạng SC: Tiêm dưới da, thường ở đùi hoặc cánh tay. Liều: 6mg SC.",
                "timing": "Dùng ngay khi có triệu chứng migraine. Có thể lặp sau 1 giờ nếu cần (tối đa 12mg/ngày).",
                "notes": "Tác dụng nhanh nhất (10-15 phút). Bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi dùng."
            },
            "nasal": {
                "technique": "Dạng xịt mũi: Xịt vào một bên mũi, nhắm mắt và miệng khi xịt.",
                "timing": "Dùng ngay khi có triệu chứng migraine. Có thể lặp sau 2 giờ nếu cần (tối đa 40mg/ngày).",
                "notes": "Tác dụng nhanh (15-30 phút). Có thể gây vị đắng trong miệng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Imitrex (Sumatriptan)",
                "UpToDate: Triptans for acute migraine",
                "American Headache Society Guidelines",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Micromedex: Sumatriptan"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "High - FDA approved, multiple RCTs, clinical guidelines"
        }
    },
}

__all__ = ['ANALGESICS_DRUGS']
