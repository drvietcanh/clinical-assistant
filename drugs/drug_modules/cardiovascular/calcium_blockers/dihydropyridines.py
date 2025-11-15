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
    }
}

__all__ = ['DIHYDROPYRIDINE_CCB']
