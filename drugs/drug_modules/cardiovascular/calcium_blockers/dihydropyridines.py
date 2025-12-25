"""
Dihydropyridine Calcium Channel Blockers
Amlodipine and Nifedipine for hypertension and angina
"""

DIHYDROPYRIDINE_CCB = {
    "Amlodipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Amlodipine, Norvasc",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực"
        ],
        "contraindications": [
            "Dị ứng",
            "Sốc tim"
        ],
        "dosage": {
            "adult_htn": "2.5-10mg x 1 lần/ngày",
            "adult_angina": "5-10mg x 1 lần/ngày",
            "notes": "Tác dụng dài, uống 1 lần/ngày"
        },
        "side_effects": [
            "Phù chân",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)"
        ],
        "interactions": [
            "Simvastatin: tăng nồng độ simvastatin",
            "Grapefruit juice: tăng nồng độ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế dòng calci vào tế bào cơ trơn mạch máu, gây giãn mạch, giảm kháng lực mạch máu ngoại biên",
        "monitoring": [
            "Huyết áp mỗi lần khám",
            "Nhịp tim (có thể tăng nhẹ phản ứng)",
            "Phù chân (dấu hiệu tác dụng phụ)",
            "Chức năng gan định kỳ"
        ],
        "precautions": [
            "Phù chân thường gặp, thường không nghiêm trọng nhưng có thể khó chịu",
            "Tránh grapefruit juice (tăng nồng độ)",
            "Có thể dùng với thức ăn hoặc không",
            "Tác dụng chậm, đạt đỉnh sau 6-12 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "30-50 giờ (rất dài)",
            "onset": "2-4 giờ",
            "duration": "24 giờ",
            "protein_binding": ">93%",
            "clearance": "Gan (CYP3A4)"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Không có black box warning cụ thể. Thận trọng với bệnh nhân suy tim mất bù, hẹp van động mạch chủ nặng. Phù ngoại biên có thể xảy ra và thường không phản ánh suy tim",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Simvastatin, Lovastatin",
                    "mechanism": "Ức chế CYP3A4 chung, tăng nồng độ statin",
                    "effect": "Tăng nguy cơ tiêu cơ vân, tăng men gan",
                    "management": "Giảm liều simvastatin/lovastatin. Theo dõi CK, men gan. Có thể dùng atorvastatin hoặc rosuvastatin thay thế."
                }
            ],
            "moderate": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4",
                    "effect": "Tăng nồng độ amlodipine, tăng tác dụng phụ",
                    "management": "Tránh uống grapefruit juice. Có thể dùng nước cam thay thế."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, erythromycin, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa amlodipine",
                    "effect": "Tăng nồng độ amlodipine, tăng tác dụng phụ",
                    "management": "Thận trọng. Theo dõi huyết áp, phù chân. Có thể cần giảm liều amlodipine."
                }
            ],
            "minor": [
                {
                    "drug": "Sildenafil, Tadalafil",
                    "mechanism": "Tác dụng hiệp đồng hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp. Không phải chống chỉ định."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng amlodipine hoặc dihydropyridine calcium channel blockers",
                "Sốc tim",
                "Suy tim mất bù nặng (NYHA class IV)"
            ],
            "tương_đối": [
                "Hẹp van động mạch chủ nặng - có thể gây suy tim",
                "Suy gan - giảm chuyển hóa, tăng nồng độ",
                "Suy tim nhẹ đến trung bình - thận trọng",
                "Phù ngoại biên - tác dụng phụ thường gặp nhưng không nguy hiểm"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Ưu tiên dùng trong 3 tháng cuối nếu có thể. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Amlodipine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều (chuyển hóa qua gan)",
            "severe": "Giảm liều 50% (chuyển hóa qua gan CYP3A4)",
            "notes": "Amlodipine chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ. Giảm liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh phản xạ",
                "Phù ngoại biên",
                "Chóng mặt, ngất",
                "Sốc tim (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Calcium (cho block calci)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Calcium gluconate hoặc calcium chloride IV (đối kháng với calcium channel blocker)",
                "Atropine nếu có nhịp tim chậm",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life rất dài: 30-50 giờ)"
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, dấu hiệu sống, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate hoặc Calcium chloride",
                    "mechanism": "Đối kháng với calcium channel blocker bằng cách tăng nồng độ calci ngoại bào",
                    "indication": "Hạ huyết áp nặng, block calci",
                    "dose": "Calcium gluconate 10%: 10-30ml IV, hoặc Calcium chloride 10%: 5-10ml IV"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày (do half-life rất dài: 30-50 giờ). Uống cùng giờ mỗi ngày. Tác dụng chậm, đạt đỉnh sau 6-12 giờ."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <6 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <6 tuổi (dữ liệu hạn chế)",
            "children": "6-17 tuổi: 2.5-5mg x 1 lần/ngày (tối đa 5mg/ngày). Chỉ dùng cho tăng huyết áp. Theo dõi huyết áp, phù chân",
            "adolescents": "2.5-5mg x 1 lần/ngày, tăng dần đến 5-10mg/ngày nếu cần. Liều người lớn",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng huyết áp ở trẻ ≥6 tuổi. Khởi đầu với liều thấp, tăng dần. Theo dõi huyết áp, phù chân"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (phù chân, hạ huyết áp). Half-life dài hơn (30-50 giờ) nên tích lũy dễ hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (2.5mg x 1 lần/ngày). Tăng dần chậm hơn. Có thể cần liều thấp hơn do tích lũy",
            "monitoring": "Theo dõi huyết áp sát hơn. Theo dõi phù chân (tác dụng phụ thường gặp). Cảnh báo về tương tác với grapefruit juice"
        },
        "brand_names": {
            "vietnam": ["Norvasc", "Amlodipine Stada", "Amlodipine", "Amlor"],
            "common": ["Norvasc", "Amlodipine"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "8,000 - 25,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Amlodipine generic thường rẻ hơn (8,000-15,000 VND/viên 5mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Norvasc (amlodipine)",
                "UpToDate - Amlodipine: Drug information",
                "ALLHAT Study - JAMA",
                "ASCOT Study - The Lancet",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (ALLHAT, ASCOT) and extensive clinical experience"
        }
    },

    "Nifedipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Nifedipine, Adalat",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Raynaud's phenomenon",
            "Co thắt mạch vành"
        ],
        "contraindications": [
            "Dị ứng",
            "Sốc tim",
            "Suy tim nặng",
            "Hẹp van động mạch chủ nặng"
        ],
        "dosage": {
            "adult_htn_immediate": "10-20mg x 3 lần/ngày",
            "adult_htn_extended": "30-90mg x 1 lần/ngày (XL/retard)",
            "adult_angina": "10-20mg x 3 lần/ngày",
            "notes": "Tránh dùng immediate-release cho tăng huyết áp (nguy cơ hạ HA đột ngột). Ưu tiên extended-release"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Phù chân",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)",
            "Hạ huyết áp đột ngột (immediate-release)"
        ],
        "interactions": [
            "Grapefruit juice: tăng nồng độ",
            "Beta-blocker: có thể gây block nhĩ thất",
            "Digoxin: tăng nồng độ digoxin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dihydropyridine calcium channel blocker. Ức chế kênh calci L-type voltage-gated trong màng tế bào cơ trơn mạch máu, ngăn cản dòng calci vào trong tế bào, dẫn đến giãn mạch. Giãn mạch ngoại vi → giảm sức cản mạch máu hệ thống → giảm huyết áp. Giãn mạch vành → tăng tưới máu vành. Ít ảnh hưởng đến tim (không giảm co bóp, không làm chậm nhịp như verapamil/diltiazem). Được dùng trong tăng huyết áp, đau thắt ngực, và co thắt mạch vành.",
        "monitoring": [
            "Huyết áp (theo dõi chặt chẽ khi bắt đầu điều trị)",
            "Nhịp tim (có thể tăng phản xạ do giãn mạch)",
            "Dấu hiệu phù ngoại vi (mắt cá chân, cẳng chân) - tác dụng phụ thường gặp",
            "Đau thắt ngực (nếu dùng cho đau thắt ngực)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu quá liều (hạ huyết áp nặng, nhịp tim nhanh)",
            "Dấu hiệu thiếu máu cục bộ (đau chân khi đi bộ) - hiếm"
        ],
        "precautions": [
            "Dạng tác dụng nhanh (immediate-release) KHÔNG được dùng để điều trị tăng huyết áp hoặc đau thắt ngực (nguy cơ nhồi máu cơ tim, đột quỵ) - chỉ dùng extended-release",
            "Dạng extended-release: không nghiền, không nhai (phá hủy lớp bọc)",
            "Nguy cơ phù ngoại vi (mắt cá chân, cẳng chân) - thường gặp, không nguy hiểm nhưng khó chịu",
            "Có thể gây nhịp tim nhanh phản xạ (do giãn mạch) - thận trọng ở bệnh nhân đau thắt ngực",
            "Hạ huyết áp tư thế đứng - đứng dậy chậm",
            "Thận trọng ở suy gan (giảm chuyển hóa)",
            "Tương tác với nhiều thuốc: tăng nồng độ với CYP3A4 inhibitors (ketoconazole, erythromycin), giảm với inducers",
            "Tránh bưởi chùm (grapefruit) - ức chế CYP3A4 → tăng nồng độ",
            "Không dùng trong hẹp van động mạch chủ nặng (có thể gây suy tim)",
            "Uống với thức ăn hoặc không (tùy dạng)"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ (immediate-release), 17 giờ (extended-release)",
            "onset": "20 phút (immediate-release), 2-6 giờ (extended-release)",
            "duration": "6-8 giờ (immediate-release), 24 giờ (extended-release)",
            "protein_binding": "92-98%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén extended-release: không nghiền, không nhai.",
        "black_box_warnings": "Dạng immediate-release KHÔNG được dùng để điều trị tăng huyết áp hoặc đau thắt ngực - có thể làm tăng nguy cơ nhồi máu cơ tim và tử vong. Chỉ dùng dạng extended-release cho các chỉ định này.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa nifedipine",
                    "effect": "Tăng nồng độ nifedipine đáng kể (có thể tăng 2-3 lần), tăng tác dụng phụ (hạ huyết áp, nhức đầu, phù)",
                    "management": "TRÁNH hoàn toàn bưởi chùm và nước ép bưởi chùm khi dùng nifedipine."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa nifedipine qua CYP3A4",
                    "effect": "Tăng nồng độ nifedipine đáng kể, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều nifedipine. Theo dõi huyết áp, nhịp tim sát. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Tác dụng hiệp đồng giảm nhịp tim, giảm co bóp",
                    "effect": "Tăng nguy cơ block nhĩ thất, suy tim, nhịp tim chậm",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim. Thường dùng được nhưng cần theo dõi sát."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Nifedipine có thể tăng nồng độ digoxin",
                    "effect": "Tăng nguy cơ ngộ độc digoxin",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin, carbamazepine)",
                    "mechanism": "Tăng chuyển hóa nifedipine qua CYP3A4",
                    "effect": "Giảm nồng độ nifedipine, giảm hiệu quả",
                    "management": "Có thể cần tăng liều nifedipine. Theo dõi huyết áp."
                }
            ],
            "minor": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Có thể ức chế nhẹ chuyển hóa",
                    "effect": "Tăng nhẹ nồng độ nifedipine",
                    "management": "Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nifedipine hoặc dihydropyridine calcium channel blockers",
                "Sốc tim",
                "Suy tim nặng (EF <30%)",
                "Hẹp van động mạch chủ nặng",
                "Dạng immediate-release cho tăng huyết áp hoặc đau thắt ngực"
            ],
            "tương_đối": [
                "Suy tim trung bình - thận trọng (EF 30-40%)",
                "Suy gan nặng - giảm liều, thận trọng (chuyển hóa qua CYP3A4)",
                "Hẹp van động mạch chủ trung bình - thận trọng",
                "Dùng với beta-blockers - tăng nguy cơ block AV",
                "Dùng với CYP3A4 inhibitors mạnh - tăng nồng độ nifedipine"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim nhanh ở thai nhi. Có thể gây chậm phát triển thai nhi. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong tăng huyết áp thai kỳ nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Nifedipine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50% (chuyển hóa qua CYP3A4)",
            "severe": "Thận trọng, giảm liều 50-75% hoặc tránh dùng (chuyển hóa qua CYP3A4)",
            "notes": "Nifedipine chuyển hóa mạnh qua gan (CYP3A4). Suy gan làm giảm chuyển hóa, tăng nồng độ nifedipine. Cần giảm liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh phản xạ",
                "Chóng mặt, ngất",
                "Suy tim cấp",
                "Phù phổi",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (có thể đảo ngược tác dụng calcium channel blocker)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Calcium gluconate 1-3g IV hoặc calcium chloride 1g IV (có thể đảo ngược tác dụng)",
                "Theo dõi ECG liên tục",
                "Theo dõi huyết áp, nhịp tim, ý thức",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life dài với extended-release: 17 giờ)"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu suy hô hấp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate / Calcium chloride",
                    "mechanism": "Tăng nồng độ calci trong máu, đảo ngược tác dụng calcium channel blocker",
                    "dose": "Calcium gluconate 1-3g IV hoặc Calcium chloride 1g IV",
                    "indication": "Hạ huyết áp, rối loạn nhịp do quá liều calcium channel blocker"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Dạng extended-release: có thể uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "Dạng extended-release: uống 1 lần/ngày vào cùng một giờ mỗi ngày. KHÔNG nghiền, KHÔNG nhai viên extended-release (phá hủy lớp bọc, gây phóng thích nhanh nguy hiểm). Dạng immediate-release: KHÔNG dùng cho tăng huyết áp hoặc đau thắt ngực."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Nifedipine chỉ có dạng uống (PO)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Procardia (nifedipine)",
                "UpToDate - Nifedipine: Drug information",
                "ACCORD Study - New England Journal of Medicine (2010) - Intensive blood pressure control",
                "SPRINT Study - New England Journal of Medicine (2015) - Blood pressure targets",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs and extensive clinical experience. Strong warning against immediate-release formulation."
        }
    },

    "Felodipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Felodipine, Plendil",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực"
        ],
        "contraindications": [
            "Dị ứng felodipine hoặc dihydropyridine calcium channel blockers",
            "Sốc tim",
            "Suy tim mất bù nặng"
        ],
        "dosage": {
            "adult_htn": "5-10mg x 1 lần/ngày, tăng đến 20mg x 1 lần/ngày nếu cần",
            "adult_angina": "5-10mg x 1 lần/ngày",
            "elderly": "Khởi đầu 2.5mg x 1 lần/ngày",
            "notes": "Tác dụng dài, uống 1 lần/ngày. Extended-release formulation."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Phù chân",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)",
            "Hạ huyết áp tư thế đứng"
        ],
        "interactions": [
            "Grapefruit juice: tăng nồng độ đáng kể",
            "CYP3A4 inhibitors: tăng nồng độ",
            "CYP3A4 inducers: giảm nồng độ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dihydropyridine calcium channel blocker. Ức chế kênh calci L-type trong màng tế bào cơ trơn mạch máu, ngăn cản dòng calci vào trong tế bào, dẫn đến giãn mạch. Giãn mạch ngoại vi → giảm sức cản mạch máu hệ thống → giảm huyết áp. Ít ảnh hưởng đến tim (không giảm co bóp, không làm chậm nhịp như verapamil/diltiazem). Chuyển hóa qua CYP3A4.",
        "monitoring": [
            "Huyết áp mỗi lần khám",
            "Nhịp tim (có thể tăng nhẹ phản ứng)",
            "Phù chân (dấu hiệu tác dụng phụ)",
            "Chức năng gan định kỳ (chuyển hóa qua gan)"
        ],
        "precautions": [
            "Phù chân thường gặp, thường không nghiêm trọng nhưng có thể khó chịu",
            "TRÁNH grapefruit juice (tăng nồng độ đáng kể, có thể tăng 2-3 lần)",
            "Có thể dùng với thức ăn hoặc không",
            "Tác dụng chậm, đạt đỉnh sau 2.5-5 giờ",
            "Thận trọng ở suy gan (giảm chuyển hóa)"
        ],
        "pharmacokinetics": {
            "half_life": "11-16 giờ (extended-release)",
            "onset": "2-5 giờ",
            "duration": "24 giờ",
            "protein_binding": ">99%",
            "clearance": "Gan (CYP3A4)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén extended-release: không nghiền, không nhai.",
        "black_box_warnings": "Không có black box warning cụ thể. Thận trọng với bệnh nhân suy tim mất bù, hẹp van động mạch chủ nặng. Phù ngoại biên có thể xảy ra và thường không phản ánh suy tim.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa felodipine",
                    "effect": "Tăng nồng độ felodipine đáng kể (có thể tăng 2-3 lần), tăng tác dụng phụ (hạ huyết áp, nhức đầu, phù)",
                    "management": "TRÁNH hoàn toàn bưởi chùm và nước ép bưởi chùm khi dùng felodipine."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa felodipine qua CYP3A4",
                    "effect": "Tăng nồng độ felodipine đáng kể, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều felodipine. Theo dõi huyết áp, nhịp tim sát. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin, carbamazepine)",
                    "mechanism": "Tăng chuyển hóa felodipine qua CYP3A4",
                    "effect": "Giảm nồng độ felodipine, giảm hiệu quả",
                    "management": "Có thể cần tăng liều felodipine. Theo dõi huyết áp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng felodipine hoặc dihydropyridine calcium channel blockers",
                "Sốc tim",
                "Suy tim mất bù nặng (NYHA class IV)"
            ],
            "tương_đối": [
                "Hẹp van động mạch chủ nặng - có thể gây suy tim",
                "Suy gan - giảm chuyển hóa, tăng nồng độ",
                "Suy tim nhẹ đến trung bình - thận trọng",
                "Phù ngoại biên - tác dụng phụ thường gặp nhưng không nguy hiểm"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Ưu tiên dùng trong 3 tháng cuối nếu có thể. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Felodipine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều (chuyển hóa qua gan)",
            "severe": "Giảm liều 50% (chuyển hóa qua gan CYP3A4)",
            "notes": "Felodipine chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ. Giảm liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh phản xạ",
                "Phù ngoại biên",
                "Chóng mặt, ngất",
                "Sốc tim (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Calcium (cho block calci)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Calcium gluconate hoặc calcium chloride IV (đối kháng với calcium channel blocker)",
                "Atropine nếu có nhịp tim chậm",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life 11-16 giờ)"
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, dấu hiệu sống, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate hoặc Calcium chloride",
                    "mechanism": "Đối kháng với calcium channel blocker bằng cách tăng nồng độ calci ngoại bào",
                    "indication": "Hạ huyết áp nặng, block calci",
                    "dose": "Calcium gluconate 10%: 10-30ml IV, hoặc Calcium chloride 10%: 5-10ml IV"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày (do half-life 11-16 giờ). Uống cùng giờ mỗi ngày. KHÔNG nghiền, KHÔNG nhai viên extended-release (phá hủy lớp bọc, gây phóng thích nhanh nguy hiểm)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "adolescents": "2.5-5mg x 1 lần/ngày, tăng dần đến 5-10mg/ngày nếu cần. Liều người lớn",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng huyết áp ở trẻ ≥18 tuổi. Khởi đầu với liều thấp, tăng dần. Theo dõi huyết áp, phù chân"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (phù chân, hạ huyết áp). Suy gan phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (2.5mg x 1 lần/ngày). Tăng dần chậm hơn. Có thể cần liều thấp hơn do tích lũy",
            "monitoring": "Theo dõi huyết áp sát hơn. Theo dõi phù chân (tác dụng phụ thường gặp). Cảnh báo về tương tác với grapefruit juice"
        },
        "brand_names": {
            "vietnam": ["Plendil", "Felodipine Stada", "Felodipine"],
            "common": ["Plendil", "Felodipine"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "10,000 - 30,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Felodipine generic thường rẻ hơn (10,000-20,000 VND/viên 5mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Plendil (felodipine)",
                "UpToDate - Felodipine: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Extensive clinical experience"
        }
    },

    "Isradipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Isradipine, Dynacirc",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực"
        ],
        "contraindications": [
            "Dị ứng isradipine hoặc dihydropyridine calcium channel blockers",
            "Sốc tim",
            "Suy tim mất bù nặng"
        ],
        "dosage": {
            "adult_htn": "2.5mg x 2 lần/ngày, tăng đến 5mg x 2 lần/ngày nếu cần (tối đa 20mg/ngày)",
            "adult_angina": "2.5-5mg x 2 lần/ngày",
            "elderly": "Khởi đầu 1.25mg x 2 lần/ngày",
            "notes": "Uống 2 lần/ngày. Có dạng immediate-release và extended-release."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Phù chân",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)",
            "Hạ huyết áp tư thế đứng",
            "Mệt mỏi"
        ],
        "interactions": [
            "Grapefruit juice: tăng nồng độ",
            "CYP3A4 inhibitors: tăng nồng độ",
            "CYP3A4 inducers: giảm nồng độ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dihydropyridine calcium channel blocker. Ức chế kênh calci L-type trong màng tế bào cơ trơn mạch máu, ngăn cản dòng calci vào trong tế bào, dẫn đến giãn mạch. Giãn mạch ngoại vi → giảm sức cản mạch máu hệ thống → giảm huyết áp. Ít ảnh hưởng đến tim (không giảm co bóp, không làm chậm nhịp như verapamil/diltiazem). Chuyển hóa qua CYP3A4.",
        "monitoring": [
            "Huyết áp mỗi lần khám",
            "Nhịp tim (có thể tăng nhẹ phản ứng)",
            "Phù chân (dấu hiệu tác dụng phụ)",
            "Chức năng gan định kỳ (chuyển hóa qua gan)"
        ],
        "precautions": [
            "Phù chân thường gặp, thường không nghiêm trọng nhưng có thể khó chịu",
            "TRÁNH grapefruit juice (tăng nồng độ)",
            "Có thể dùng với thức ăn hoặc không",
            "Tác dụng nhanh hơn amlodipine (half-life ngắn hơn)",
            "Thận trọng ở suy gan (giảm chuyển hóa)"
        ],
        "pharmacokinetics": {
            "half_life": "8 giờ (immediate-release), 13 giờ (extended-release)",
            "onset": "2 giờ",
            "duration": "12 giờ (immediate-release), 24 giờ (extended-release)",
            "protein_binding": "95%",
            "clearance": "Gan (CYP3A4)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén extended-release: không nghiền, không nhai.",
        "black_box_warnings": "Không có black box warning cụ thể. Thận trọng với bệnh nhân suy tim mất bù, hẹp van động mạch chủ nặng. Phù ngoại biên có thể xảy ra và thường không phản ánh suy tim.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa isradipine",
                    "effect": "Tăng nồng độ isradipine, tăng tác dụng phụ",
                    "management": "TRÁNH hoàn toàn bưởi chùm và nước ép bưởi chùm khi dùng isradipine."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa isradipine qua CYP3A4",
                    "effect": "Tăng nồng độ isradipine, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều isradipine. Theo dõi huyết áp, nhịp tim sát."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin, carbamazepine)",
                    "mechanism": "Tăng chuyển hóa isradipine qua CYP3A4",
                    "effect": "Giảm nồng độ isradipine, giảm hiệu quả",
                    "management": "Có thể cần tăng liều isradipine. Theo dõi huyết áp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng isradipine hoặc dihydropyridine calcium channel blockers",
                "Sốc tim",
                "Suy tim mất bù nặng (NYHA class IV)"
            ],
            "tương_đối": [
                "Hẹp van động mạch chủ nặng - có thể gây suy tim",
                "Suy gan - giảm chuyển hóa, tăng nồng độ",
                "Suy tim nhẹ đến trung bình - thận trọng",
                "Phù ngoại biên - tác dụng phụ thường gặp nhưng không nguy hiểm"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Ưu tiên dùng trong 3 tháng cuối nếu có thể. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Isradipine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều (chuyển hóa qua gan)",
            "severe": "Giảm liều 50% (chuyển hóa qua gan CYP3A4)",
            "notes": "Isradipine chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ. Giảm liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh phản xạ",
                "Phù ngoại biên",
                "Chóng mặt, ngất",
                "Sốc tim (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Calcium (cho block calci)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Calcium gluconate hoặc calcium chloride IV (đối kháng với calcium channel blocker)",
                "Atropine nếu có nhịp tim chậm",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life 8-13 giờ)"
            ],
            "monitoring": "Huyết áp, nhịp tim, ECG, dấu hiệu sống, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate hoặc Calcium chloride",
                    "mechanism": "Đối kháng với calcium channel blocker bằng cách tăng nồng độ calci ngoại bào",
                    "indication": "Hạ huyết áp nặng, block calci",
                    "dose": "Calcium gluconate 10%: 10-30ml IV, hoặc Calcium chloride 10%: 5-10ml IV"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 2 lần/ngày (sáng và tối) vào cùng giờ mỗi ngày. Dạng extended-release: uống 1 lần/ngày. KHÔNG nghiền, KHÔNG nhai viên extended-release."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "adolescents": "1.25-2.5mg x 2 lần/ngày, tăng dần đến 5mg x 2 lần/ngày nếu cần. Liều người lớn",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng huyết áp ở trẻ ≥18 tuổi. Khởi đầu với liều thấp, tăng dần. Theo dõi huyết áp, phù chân"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (phù chân, hạ huyết áp). Suy gan phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (1.25mg x 2 lần/ngày). Tăng dần chậm hơn. Có thể cần liều thấp hơn",
            "monitoring": "Theo dõi huyết áp sát hơn. Theo dõi phù chân (tác dụng phụ thường gặp). Cảnh báo về tương tác với grapefruit juice"
        },
        "brand_names": {
            "vietnam": ["Dynacirc", "Isradipine Stada", "Isradipine"],
            "common": ["Dynacirc", "Isradipine"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "10,000 - 30,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Isradipine generic thường rẻ hơn (10,000-20,000 VND/viên 2.5mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dynacirc (isradipine)",
                "UpToDate - Isradipine: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Extensive clinical experience"
        }
    },
    
    "Felodipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Felodipine, Plendil",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực"
        ],
        "contraindications": [
            "Dị ứng felodipine hoặc dihydropyridine",
            "Sốc tim",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_htn": "5-10mg x 1 lần/ngày, tăng đến 20mg/ngày nếu cần",
            "adult_angina": "5-10mg x 1 lần/ngày",
            "adult_max": "20mg/ngày",
            "notes": "Dihydropyridine CCB. Uống với thức ăn để tăng hấp thu. Tránh grapefruit juice (tăng nồng độ)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Phù chân (phổ biến)",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)",
            "Chảy máu nướu (hiếm, do tăng sản nướu)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Grapefruit juice: tăng nồng độ felodipine đáng kể",
            "CYP3A4 inhibitors: tăng nồng độ felodipine",
            "CYP3A4 inducers: giảm nồng độ felodipine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dihydropyridine calcium channel blocker. Ức chế dòng calci vào tế bào cơ trơn mạch máu qua kênh calci L-type, gây giãn mạch ngoại biên, giảm kháng lực mạch máu ngoại biên, giảm huyết áp. Tác dụng chủ yếu trên mạch máu, ít ảnh hưởng đến tim (khác với non-dihydropyridine CCB như verapamil, diltiazem). Được dùng để điều trị tăng huyết áp và đau thắt ngực. Đặc điểm: hấp thu tốt hơn với thức ăn, tương tác mạnh với grapefruit juice (ức chế CYP3A4).",
        "monitoring": [
            "Huyết áp mỗi lần khám",
            "Nhịp tim (có thể tăng nhẹ phản ứng)",
            "Phù chân (dấu hiệu tác dụng phụ phổ biến)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu chảy máu nướu, tăng sản nướu (hiếm)"
        ],
        "precautions": [
            "Uống với thức ăn để tăng hấp thu",
            "TRÁNH grapefruit juice (tăng nồng độ felodipine đáng kể, tăng tác dụng phụ)",
            "Phù chân phổ biến - thường không nghiêm trọng nhưng có thể khó chịu",
            "Có thể gây nhức đầu, chóng mặt - thận trọng khi lái xe",
            "Thận trọng ở suy gan nặng (chống chỉ định)",
            "Tương tác với CYP3A4 inhibitors (tăng nồng độ) và inducers (giảm nồng độ)",
            "Nguy cơ chảy máu nướu, tăng sản nướu (hiếm) - vệ sinh răng miệng tốt"
        ],
        "pharmacokinetics": {
            "half_life": "11-16 giờ (dài)",
            "onset": "2-5 giờ",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "99% (rất cao)",
            "metabolism": "Gan (chuyển hóa chủ yếu qua CYP3A4)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Không cần điều chỉnh thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "TRÁNH grapefruit juice - tăng nồng độ felodipine đáng kể, tăng tác dụng phụ (phù chân, hạ huyết áp, nhức đầu).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4 trong ruột và gan, giảm chuyển hóa felodipine",
                    "effect": "Tăng nồng độ felodipine đáng kể (có thể tăng 2-3 lần), tăng tác dụng phụ (phù chân, hạ huyết áp, nhức đầu)",
                    "management": "TRÁNH TUYỆT ĐỐI grapefruit juice khi dùng felodipine. Tư vấn bệnh nhân về nguy cơ này."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa felodipine qua CYP3A4",
                    "effect": "Tăng nồng độ felodipine, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều felodipine. Theo dõi huyết áp, phù chân."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (carbamazepine, phenytoin, rifampin)",
                    "mechanism": "Cảm ứng enzyme CYP3A4, tăng chuyển hóa felodipine",
                    "effect": "Giảm nồng độ felodipine, giảm hiệu quả",
                    "management": "Tăng liều felodipine nếu cần. Theo dõi huyết áp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng felodipine hoặc dihydropyridine",
                "Sốc tim",
                "Suy gan nặng (Child-Pugh C)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, có thể giảm liều",
                "Dùng với grapefruit juice - tăng nồng độ đáng kể",
                "Dùng với CYP3A4 inhibitors - tăng nồng độ",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Felodipine là category C. Có thể dùng khi cần thiết. Có thể gây hạ huyết áp thai nhi. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Felodipine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (hạ huyết áp, nhịp tim nhanh).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu hạ huyết áp, nhịp tim nhanh ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa chủ yếu qua gan)",
            "notes": "Felodipine chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh (phản ứng)",
                "Phù chân nặng",
                "Nhức đầu nặng",
                "Chóng mặt, ngất",
                "Rối loạn nhịp tim (hiếm)"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (đảo ngược một phần tác dụng)",
            "treatment": [
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Calcium gluconate 1-3g IV hoặc calcium chloride 1g IV (đảo ngược một phần tác dụng)",
                "Theo dõi liên tục: huyết áp, nhịp tim, ECG",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần"
            ],
            "monitoring": "Theo dõi liên tục huyết áp, nhịp tim, ECG trong ít nhất 12-24 giờ"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate hoặc calcium chloride",
                    "mechanism": "Đảo ngược một phần tác dụng ức chế kênh calci",
                    "indication": "Hạ huyết áp nặng do quá liều CCB",
                    "dose": "Calcium gluconate 1-3g IV hoặc calcium chloride 1g IV"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu. Không uống khi bụng đói.",
                "timing": "Uống 1 lần/ngày (do half-life dài 11-16 giờ). Uống cùng thời điểm mỗi ngày. QUAN TRỌNG: TRÁNH grapefruit juice - tăng nồng độ đáng kể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Plendil (felodipine)",
                "UpToDate - Felodipine: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Nicardipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Nicardipine, Cardene",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Tăng huyết áp cấp cứu (IV)",
            "Kiểm soát huyết áp trong phẫu thuật (IV)"
        ],
        "contraindications": [
            "Dị ứng nicardipine hoặc dihydropyridine",
            "Sốc tim",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_htn_po": "20-40mg x 3 lần/ngày",
            "adult_htn_po_sr": "30-60mg x 2 lần/ngày (sustained release)",
            "adult_hypertensive_emergency_iv": "5mg/giờ, tăng 2.5mg/giờ mỗi 15 phút đến 15mg/giờ",
            "adult_iv_maintenance": "3-5mg/giờ",
            "notes": "Dihydropyridine CCB. Có dạng uống và IV. Dạng IV dùng cho tăng huyết áp cấp cứu và kiểm soát huyết áp trong phẫu thuật. Tránh grapefruit juice."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Phù chân (phổ biến)",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)",
            "Hạ huyết áp (đặc biệt với dạng IV)"
        ],
        "interactions": [
            "Grapefruit juice: tăng nồng độ nicardipine",
            "CYP3A4 inhibitors: tăng nồng độ nicardipine",
            "CYP3A4 inducers: giảm nồng độ nicardipine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dihydropyridine calcium channel blocker. Ức chế dòng calci vào tế bào cơ trơn mạch máu qua kênh calci L-type, gây giãn mạch ngoại biên, giảm kháng lực mạch máu ngoại biên, giảm huyết áp. Tác dụng chủ yếu trên mạch máu, ít ảnh hưởng đến tim (khác với non-dihydropyridine CCB như verapamil, diltiazem). Được dùng để điều trị tăng huyết áp và đau thắt ngực. Dạng IV dùng cho tăng huyết áp cấp cứu và kiểm soát huyết áp trong phẫu thuật. Đặc điểm: tương tác mạnh với grapefruit juice (ức chế CYP3A4).",
        "monitoring": [
            "Huyết áp mỗi lần khám (đặc biệt quan trọng với dạng IV)",
            "Nhịp tim (có thể tăng nhẹ phản ứng)",
            "Phù chân (dấu hiệu tác dụng phụ phổ biến)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan"
        ],
        "precautions": [
            "TRÁNH grapefruit juice (tăng nồng độ nicardipine đáng kể, tăng tác dụng phụ)",
            "Phù chân phổ biến - thường không nghiêm trọng nhưng có thể khó chịu",
            "Dạng IV: Theo dõi huyết áp sát (nguy cơ hạ huyết áp)",
            "Có thể gây nhức đầu, chóng mặt - thận trọng khi lái xe",
            "Thận trọng ở suy gan nặng (chống chỉ định)",
            "Tương tác với CYP3A4 inhibitors (tăng nồng độ) và inducers (giảm nồng độ)",
            "Dạng IV: Truyền liên tục, điều chỉnh tốc độ theo huyết áp"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ (ngắn)",
            "onset": "20 phút (PO), ngay lập tức (IV)",
            "duration": "8 giờ (PO), liên tục (IV)",
            "protein_binding": "95% (rất cao)",
            "metabolism": "Gan (chuyển hóa chủ yếu qua CYP3A4)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Không cần điều chỉnh thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng IV: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
        "black_box_warnings": "TRÁNH grapefruit juice - tăng nồng độ nicardipine đáng kể, tăng tác dụng phụ (phù chân, hạ huyết áp, nhức đầu).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4 trong ruột và gan, giảm chuyển hóa nicardipine",
                    "effect": "Tăng nồng độ nicardipine đáng kể (có thể tăng 2-3 lần), tăng tác dụng phụ (phù chân, hạ huyết áp, nhức đầu)",
                    "management": "TRÁNH TUYỆT ĐỐI grapefruit juice khi dùng nicardipine. Tư vấn bệnh nhân về nguy cơ này."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa nicardipine qua CYP3A4",
                    "effect": "Tăng nồng độ nicardipine, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều nicardipine. Theo dõi huyết áp, phù chân."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (carbamazepine, phenytoin, rifampin)",
                    "mechanism": "Cảm ứng enzyme CYP3A4, tăng chuyển hóa nicardipine",
                    "effect": "Giảm nồng độ nicardipine, giảm hiệu quả",
                    "management": "Tăng liều nicardipine nếu cần. Theo dõi huyết áp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nicardipine hoặc dihydropyridine",
                "Sốc tim",
                "Suy gan nặng (Child-Pugh C)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, có thể giảm liều",
                "Dùng với grapefruit juice - tăng nồng độ đáng kể",
                "Dùng với CYP3A4 inhibitors - tăng nồng độ",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Nicardipine là category C. Có thể dùng khi cần thiết. Có thể gây hạ huyết áp thai nhi. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Nicardipine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (hạ huyết áp, nhịp tim nhanh).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu hạ huyết áp, nhịp tim nhanh ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa chủ yếu qua gan)",
            "notes": "Nicardipine chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh (phản ứng)",
                "Phù chân nặng",
                "Nhức đầu nặng",
                "Chóng mặt, ngất",
                "Rối loạn nhịp tim (hiếm)"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (đảo ngược một phần tác dụng)",
            "treatment": [
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (PO)",
                "Ngừng truyền IV ngay lập tức",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ (PO)",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Calcium gluconate 1-3g IV hoặc calcium chloride 1g IV (đảo ngược một phần tác dụng)",
                "Theo dõi liên tục: huyết áp, nhịp tim, ECG",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần"
            ],
            "monitoring": "Theo dõi liên tục huyết áp, nhịp tim, ECG trong ít nhất 12-24 giờ"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate hoặc calcium chloride",
                    "mechanism": "Đảo ngược một phần tác dụng ức chế kênh calci",
                    "indication": "Hạ huyết áp nặng do quá liều CCB",
                    "dose": "Calcium gluconate 1-3g IV hoặc calcium chloride 1g IV"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu. Không uống khi bụng đói.",
                "timing": "Uống 3 lần/ngày (do half-life ngắn 2-4 giờ). Dạng SR: 2 lần/ngày. Uống cùng thời điểm mỗi ngày. QUAN TRỌNG: TRÁNH grapefruit juice - tăng nồng độ đáng kể."
            },
            "iv": {
                "reconstitution": "Pha trong D5W hoặc normal saline. Nồng độ: 0.1mg/ml. Pha 25mg trong 250ml = 0.1mg/ml.",
                "infusion_rate": "Khởi đầu: 5mg/giờ. Tăng 2.5mg/giờ mỗi 15 phút đến 15mg/giờ tối đa. Điều chỉnh theo huyết áp.",
                "compatibility": ["D5W", "0.9% NaCl"],
                "incompatibility": [],
                "notes": "QUAN TRỌNG: 1) Truyền liên tục, điều chỉnh tốc độ theo huyết áp, 2) Theo dõi huyết áp sát (nguy cơ hạ huyết áp), 3) Khởi đầu 5mg/giờ, tăng dần đến 15mg/giờ tối đa, 4) Dùng cho tăng huyết áp cấp cứu và kiểm soát huyết áp trong phẫu thuật."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cardene (nicardipine)",
                "UpToDate - Nicardipine: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Nisoldipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Nisoldipine, Sular",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực"
        ],
        "contraindications": [
            "Dị ứng nisoldipine hoặc dihydropyridine",
            "Sốc tim",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_htn": "20-40mg x 1 lần/ngày",
            "adult_max": "60mg/ngày",
            "notes": "Dihydropyridine CCB. Dạng extended release, dùng 1 lần/ngày. Tránh grapefruit juice."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Phù chân (phổ biến)",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)",
            "Hạ huyết áp"
        ],
        "interactions": [
            "Grapefruit juice: tăng nồng độ nisoldipine đáng kể",
            "CYP3A4 inhibitors: tăng nồng độ nisoldipine",
            "CYP3A4 inducers: giảm nồng độ nisoldipine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dihydropyridine calcium channel blocker. Ức chế dòng calci vào tế bào cơ trơn mạch máu qua kênh calci L-type, gây giãn mạch ngoại biên, giảm kháng lực mạch máu ngoại biên, giảm huyết áp. Tác dụng chủ yếu trên mạch máu, ít ảnh hưởng đến tim (khác với non-dihydropyridine CCB như verapamil, diltiazem). Được dùng để điều trị tăng huyết áp và đau thắt ngực. Dạng extended release, dùng 1 lần/ngày. Đặc điểm: tương tác mạnh với grapefruit juice (ức chế CYP3A4).",
        "monitoring": [
            "Huyết áp mỗi lần khám",
            "Nhịp tim (có thể tăng nhẹ phản ứng)",
            "Phù chân (dấu hiệu tác dụng phụ phổ biến)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan"
        ],
        "precautions": [
            "TRÁNH grapefruit juice (tăng nồng độ nisoldipine đáng kể, tăng tác dụng phụ)",
            "Phù chân phổ biến - thường không nghiêm trọng nhưng có thể khó chịu",
            "Có thể gây nhức đầu, chóng mặt - thận trọng khi lái xe",
            "Thận trọng ở suy gan nặng (chống chỉ định)",
            "Tương tác với CYP3A4 inhibitors (tăng nồng độ) và inducers (giảm nồng độ)",
            "Dạng extended release - nuốt nguyên viên, không nghiền hoặc nhai"
        ],
        "pharmacokinetics": {
            "half_life": "7-12 giờ",
            "onset": "2-4 giờ",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": ">99% (rất cao)",
            "metabolism": "Gan (chuyển hóa chủ yếu qua CYP3A4)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Không cần điều chỉnh thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "TRÁNH grapefruit juice - tăng nồng độ nisoldipine đáng kể, tăng tác dụng phụ (phù chân, hạ huyết áp, nhức đầu).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4 trong ruột và gan, giảm chuyển hóa nisoldipine",
                    "effect": "Tăng nồng độ nisoldipine đáng kể (có thể tăng 2-3 lần), tăng tác dụng phụ (phù chân, hạ huyết áp, nhức đầu)",
                    "management": "TRÁNH TUYỆT ĐỐI grapefruit juice khi dùng nisoldipine. Tư vấn bệnh nhân về nguy cơ này."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa nisoldipine qua CYP3A4",
                    "effect": "Tăng nồng độ nisoldipine, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều nisoldipine. Theo dõi huyết áp, phù chân."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (carbamazepine, phenytoin, rifampin)",
                    "mechanism": "Cảm ứng enzyme CYP3A4, tăng chuyển hóa nisoldipine",
                    "effect": "Giảm nồng độ nisoldipine, giảm hiệu quả",
                    "management": "Tăng liều nisoldipine nếu cần. Theo dõi huyết áp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nisoldipine hoặc dihydropyridine",
                "Sốc tim",
                "Suy gan nặng (Child-Pugh C)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, có thể giảm liều",
                "Dùng với grapefruit juice - tăng nồng độ đáng kể",
                "Dùng với CYP3A4 inhibitors - tăng nồng độ",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Nisoldipine là category C. Có thể dùng khi cần thiết. Có thể gây hạ huyết áp thai nhi. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Nisoldipine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (hạ huyết áp, nhịp tim nhanh).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu hạ huyết áp, nhịp tim nhanh ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa chủ yếu qua gan)",
            "notes": "Nisoldipine chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh (phản ứng)",
                "Phù chân nặng",
                "Nhức đầu nặng",
                "Chóng mặt, ngất",
                "Rối loạn nhịp tim (hiếm)"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (đảo ngược một phần tác dụng)",
            "treatment": [
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Calcium gluconate 1-3g IV hoặc calcium chloride 1g IV (đảo ngược một phần tác dụng)",
                "Theo dõi liên tục: huyết áp, nhịp tim, ECG",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần"
            ],
            "monitoring": "Theo dõi liên tục huyết áp, nhịp tim, ECG trong ít nhất 12-24 giờ"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate hoặc calcium chloride",
                    "mechanism": "Đảo ngược một phần tác dụng ức chế kênh calci",
                    "indication": "Hạ huyết áp nặng do quá liều CCB",
                    "dose": "Calcium gluconate 1-3g IV hoặc calcium chloride 1g IV"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Uống 1 lần/ngày (do half-life 7-12 giờ và dạng extended release). Uống cùng thời điểm mỗi ngày. QUAN TRỌNG: TRÁNH grapefruit juice - tăng nồng độ đáng kể. Nuốt nguyên viên, không nghiền hoặc nhai."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sular (nisoldipine)",
                "UpToDate - Nisoldipine: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },

    "Lacidipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine)",
        "vietnamese_name": "Lacidipine, Motens",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp"
        ],
        "contraindications": [
            "Dị ứng",
            "Sốc tim",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_initial": "2-4mg x 1 lần/ngày",
            "adult_maintenance": "4-6mg x 1 lần/ngày",
            "adult_max": "6mg/ngày",
            "notes": "Dihydropyridine CCB, tác dụng dài, dùng 1 lần/ngày. Ít dùng hơn amlodipine, nifedipine."
        },
        "side_effects": [
            "Phù chân",
            "Đỏ mặt",
            "Nhức đầu",
            "Chóng mặt",
            "Tim đập nhanh (phản ứng)",
            "Ít tác dụng phụ hơn một số CCB khác"
        ],
        "interactions": [
            "Grapefruit juice: tăng nồng độ lacidipine",
            "CYP3A4 inhibitors: tăng nồng độ"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế dòng calci vào tế bào cơ trơn mạch máu, gây giãn mạch, giảm kháng lực mạch máu ngoại biên. Dihydropyridine CCB, tác dụng chủ yếu trên mạch máu ngoại biên, ít tác dụng trên tim. Tác dụng dài, dùng 1 lần/ngày. Ít dùng hơn amlodipine, nifedipine nhưng có hiệu quả tương tự.",
        "monitoring": [
            "Huyết áp mỗi lần khám",
            "Nhịp tim (có thể tăng nhẹ phản ứng)",
            "Phù chân (dấu hiệu tác dụng phụ)",
            "Chức năng gan định kỳ"
        ],
        "precautions": [
            "Phù chân thường gặp, thường không nghiêm trọng nhưng có thể khó chịu",
            "Tránh grapefruit juice (tăng nồng độ)",
            "Có thể dùng với thức ăn hoặc không",
            "Tác dụng chậm, đạt đỉnh sau 1-2 giờ",
            "Ít dùng hơn amlodipine, nifedipine nhưng có hiệu quả tương tự"
        ],
        "pharmacokinetics": {
            "half_life": "13-19 giờ (dài)",
            "onset": "1-2 giờ",
            "duration": "24 giờ (dài, dùng 1 lần/ngày)",
            "protein_binding": ">95%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ lacidipine",
                    "effect": "Tăng tác dụng phụ",
                    "management": "Tránh grapefruit juice."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa lacidipine",
                    "effect": "Tăng nồng độ lacidipine",
                    "management": "Thận trọng, có thể cần giảm liều."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng lacidipine",
                "Sốc tim",
                "Suy tim nặng"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng khi cần thiết.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, giảm liều",
            "notes": "Chuyển hóa qua gan (CYP3A4). Suy gan có thể ảnh hưởng chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Nhịp tim nhanh",
                "Chóng mặt, ngất"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (đối kháng tác dụng chẹn kênh calci)",
            "treatment": [
                "Hỗ trợ huyết áp: truyền dịch, nâng chân",
                "Calcium gluconate hoặc calcium chloride IV nếu hạ huyết áp nặng",
                "Theo dõi huyết áp, nhịp tim liên tục"
            ],
            "monitoring": "Theo dõi liên tục huyết áp, nhịp tim trong ít nhất 6-12 giờ"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Calcium gluconate hoặc calcium chloride",
                    "mechanism": "Đối kháng tác dụng chẹn kênh calci",
                    "indication": "Quá liều gây hạ huyết áp nặng",
                    "dose": "Calcium gluconate: 1-3g IV. Calcium chloride: 1g IV.",
                    "caution": "Truyền chậm, theo dõi ECG."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không.",
                "timing": "Dùng 1 lần/ngày (tiện lợi). Uống cùng thời điểm mỗi ngày."
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
                "FDA Drug Label - Motens (Lacidipine)",
                "UpToDate - Lacidipine: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved"
        }
    },
    
    "Clevidipine": {
        "group": "Cardiovascular - Calcium Channel Blocker (Dihydropyridine, IV)",
        "vietnamese_name": "Clevidipine, Cleviprex",
        "administration": ["IV"],
        "indications": [
            "Cơn tăng huyết áp (hypertensive emergency) - cấp cứu",
            "Tăng huyết áp trong phẫu thuật",
            "Tăng huyết áp trong ICU"
        ],
        "contraindications": [
            "Dị ứng clevidipine hoặc đậu nành (soy)",
            "Dị ứng trứng (egg)",
            "Dị ứng lipid (lipid emulsion)",
            "Rối loạn chuyển hóa lipid nặng",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_initial": "1-2 mg/giờ IV infusion",
            "adult_maintenance": "4-6 mg/giờ IV infusion (tối đa 16 mg/giờ)",
            "notes": "Truyền liên tục. Chỉnh liều theo huyết áp mục tiêu. Tác dụng nhanh, thời gian tác dụng ngắn (half-life 1-15 phút)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể",
            "hemodialysis": "Không cần điều chỉnh đáng kể"
        },
        "side_effects": [
            "Hạ huyết áp (phổ biến, có thể nặng)",
            "Nhịp tim nhanh phản xạ",
            "Đau đầu",
            "Chóng mặt",
            "Buồn nôn",
            "Viêm tĩnh mạch tại chỗ tiêm"
        ],
        "interactions": [
            "Thuốc hạ huyết áp khác: tăng nguy cơ hạ huyết áp",
            "Thuốc gây mê: tăng nguy cơ hạ huyết áp"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "mechanism_of_action": "Clevidipine là dihydropyridine calcium channel blocker dạng IV, tác dụng nhanh. Ức chế dòng calci vào tế bào cơ trơn mạch máu (L-type calcium channels), gây giãn mạch động mạch, giảm sức cản mạch hệ thống (SVR) và huyết áp. Không có tác dụng đáng kể trên cơ tim hoặc dẫn truyền AV (chọn lọc mạch máu). ĐẶC ĐIỂM: (1) Tác dụng cực nhanh (khởi phát trong 2-4 phút), (2) Thời gian tác dụng ngắn (half-life 1-15 phút, do chuyển hóa nhanh bởi esterase trong huyết tương), (3) Không tích lũy, (4) Không cần điều chỉnh liều ở suy thận (chuyển hóa bởi esterase, không phụ thuộc gan/thận), (5) Dạng lipid emulsion (chứa đậu nành và trứng) - CHỐNG CHỈ ĐỊNH nếu dị ứng đậu nành, trứng, hoặc lipid.",
        "monitoring": [
            "Huyết áp liên tục (arterial line nếu có thể) - QUAN TRỌNG",
            "Nhịp tim và ECG",
            "Dấu hiệu hạ huyết áp nặng",
            "Dấu hiệu phản ứng dị ứng (đậu nành, trứng, lipid)"
        ],
        "precautions": [
            "Hạ huyết áp - phổ biến, cần theo dõi sát",
            "CHỐNG CHỈ ĐỊNH nếu dị ứng đậu nành, trứng, hoặc lipid",
            "CHỐNG CHỈ ĐỊNH ở rối loạn chuyển hóa lipid nặng",
            "Thận trọng ở suy gan nặng (chuyển hóa một phần qua gan)",
            "Bù dịch đầy đủ trước khi dùng (trừ sốc tim)",
            "Giảm liều hoặc ngừng nếu hạ huyết áp nặng",
            "Dùng đường truyền riêng, không trộn với các thuốc khác"
        ],
        "pharmacokinetics": {
            "half_life": "1-15 phút (rất ngắn, do chuyển hóa nhanh bởi esterase trong huyết tương)",
            "onset": "2-4 phút",
            "duration": "Ngắn (cần truyền liên tục)",
            "protein_binding": ">99%",
            "metabolism": "Chuyển hóa nhanh bởi esterase trong huyết tương (không phụ thuộc CYP450), một phần qua gan",
            "clearance": "Chuyển hóa bởi esterase trong huyết tương, không phụ thuộc gan/thận"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Sau khi mở: dùng trong 12 giờ. Dạng lipid emulsion - bảo vệ khỏi ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc hạ huyết áp khác (ACE inhibitors, ARBs, Nitroglycerin, Hydralazine)",
                    "mechanism": "Tác dụng hạ huyết áp cộng dồn",
                    "effect": "Tăng nguy cơ hạ huyết áp nặng, sốc",
                    "management": "Theo dõi huyết áp sát. Giảm liều các thuốc hạ huyết áp khác nếu cần."
                }
            ],
            "moderate": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng clevidipine hoặc đậu nành (soy) - CHỐNG CHỈ ĐỊNH",
                "Dị ứng trứng (egg) - CHỐNG CHỈ ĐỊNH",
                "Dị ứng lipid (lipid emulsion) - CHỐNG CHỈ ĐỊNH",
                "Rối loạn chuyển hóa lipid nặng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng (chuyển hóa một phần qua gan)",
                "Bệnh nhân cao tuổi - tăng nhạy cảm với hạ huyết áp",
                "Dùng với thuốc hạ huyết áp khác - tăng nguy cơ hạ huyết áp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Clevidipine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong cơn tăng huyết áp đe dọa tính mạng.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết clevidipine có bài tiết vào sữa mẹ hay không. Thời gian bán thải rất ngắn (1-15 phút).",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa một phần qua gan, nhưng chủ yếu qua esterase trong huyết tương.",
            "severe": "Thận trọng. Suy gan nặng có thể ảnh hưởng chuyển hóa. Theo dõi sát.",
            "notes": "Clevidipine chuyển hóa chủ yếu bởi esterase trong huyết tương (không phụ thuộc CYP450), một phần qua gan. Suy gan nhẹ đến trung bình thường không ảnh hưởng đáng kể. Suy gan nặng có thể ảnh hưởng chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng, sốc",
                "Nhịp tim nhanh",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay clevidipine nếu đang truyền",
                "Hỗ trợ huyết động: Truyền dịch bolus (NS, LR), thuốc vận mạch (norepinephrine, dopamine) nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG liên tục",
                "Hỗ trợ hô hấp nếu cần"
            ],
            "monitoring": "Theo dõi huyết áp, nhịp tim, ECG liên tục cho đến khi hồi phục. Thời gian bán thải ngắn (1-15 phút), hồi phục nhanh sau khi ngừng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dung dịch sẵn dùng (0.5 mg/ml). Dạng lipid emulsion (chứa đậu nành và trứng). Bảo vệ khỏi ánh sáng.",
                "infusion_rate": "Khởi đầu: 1-2 mg/giờ IV infusion. Chỉnh liều theo huyết áp mục tiêu. Tối đa: 16 mg/giờ. Tác dụng nhanh, chỉnh liều mỗi 90 giây nếu cần.",
                "compatibility": ["D5W (5% Dextrose)", "NS (0.9% NaCl)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) CHỐNG CHỈ ĐỊNH nếu dị ứng đậu nành, trứng, hoặc lipid, 2) Theo dõi huyết áp sát, 3) Tác dụng nhanh, chỉnh liều mỗi 90 giây nếu cần, 4) Bảo vệ khỏi ánh sáng, 5) Dùng trong 12 giờ sau khi mở."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Clevidipine (Cleviprex)",
                "ACC/AHA Guidelines for Hypertension",
                "UpToDate - Clevidipine: Drug Information",
                "Medscape - Clevidipine Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACC/AHA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    }
}

__all__ = ['DIHYDROPYRIDINE_CCB']
