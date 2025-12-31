"""
Non-dihydropyridine Calcium Channel Blockers
Diltiazem and Verapamil for hypertension, angina, and arrhythmias
"""

NON_DIHYDROPYRIDINE_CCB = {
    "Diltiazem": {
        "group": "Cardiovascular - Calcium Channel Blocker (Non-dihydropyridine)",
        "vietnamese_name": "Diltiazem, Cardizem",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Rối loạn nhịp tim trên thất (SVT)",
            "Rung nhĩ",
            "Nhịp nhanh trên thất"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3",
            "Suy tim nặng",
            "Sick sinus syndrome",
            "Hạ huyết áp nặng",
            "Hội chứng Wolff-Parkinson-White với rung nhĩ"
        ],
        "dosage": {
            "adult_htn": "120-360mg/ngày chia 1-3 lần",
            "adult_htn_extended": "180-360mg x 1 lần/ngày (CD/XR)",
            "adult_angina": "120-360mg/ngày chia 1-3 lần",
            "adult_svt_iv": "0.25mg/kg IV bolus, có thể lặp 0.35mg/kg sau 15 phút",
            "adult_svt_iv_continuous": "5-15mg/giờ truyền liên tục",
            "notes": "Non-dihydropyridine, có tác dụng ức chế dẫn truyền nhĩ thất"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều 50%",
            "under_30": "Thận trọng, giảm liều 50%"
        },
        "side_effects": [
            "Nhịp tim chậm",
            "Block nhĩ thất",
            "Chóng mặt",
            "Mệt mỏi",
            "Phù chân (ít hơn dihydropyridine)",
            "Táo bón"
        ],
        "interactions": [
            "Beta-blocker: tăng nguy cơ block nhĩ thất, nhịp chậm",
            "Digoxin: tăng nồng độ digoxin",
            "Simvastatin: tăng nồng độ simvastatin",
            "Cyclosporine: tăng nồng độ cyclosporine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Non-dihydropyridine calcium channel blocker (benzothiazepine). Ức chế kênh calci L-type trong cả màng tế bào cơ trơn mạch máu và màng tế bào cơ tim. Giãn mạch ngoại vi → giảm huyết áp. Ức chế dẫn truyền nhĩ thất và làm chậm nhịp tim → giảm nhịp tim. Giảm co bóp cơ tim nhẹ. Giãn mạch vành → tăng tưới máu vành. Được dùng trong tăng huyết áp, đau thắt ngực, rối loạn nhịp trên thất (như rung nhĩ), và kiểm soát nhịp tim.",
        "monitoring": [
            "Huyết áp và nhịp tim",
            "ECG (theo dõi block nhĩ thất, nhịp tim chậm)",
            "Dấu hiệu block nhĩ thất (nhịp tim chậm, chóng mặt, ngất) - đặc biệt quan trọng",
            "Dấu hiệu suy tim (khó thở, phù) - có thể làm nặng suy tim",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu quá liều (block nhĩ thất nặng, nhịp tim chậm nặng, hạ huyết áp)"
        ],
        "precautions": [
            "KHÔNG dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp)",
            "KHÔNG dùng ở suy tim nặng (có thể làm nặng suy tim do giảm co bóp)",
            "Thận trọng ở suy gan (giảm chuyển hóa → tích lũy)",
            "Tương tác với nhiều thuốc: tăng nồng độ với CYP3A4 inhibitors, giảm với inducers",
            "Tránh bưởi chùm (grapefruit) - ức chế CYP3A4 → tăng nồng độ",
            "Tương tác với beta-blockers → tăng nguy cơ block nhĩ thất, nhịp tim chậm",
            "Tương tác với digoxin → tăng nồng độ digoxin (theo dõi nồng độ digoxin)",
            "Giảm liều ở suy gan",
            "Dạng extended-release: không nghiền, không nhai",
            "Uống với thức ăn hoặc không (tùy dạng)"
        ],
        "pharmacokinetics": {
            "half_life": "3-4.5 giờ (immediate-release), 5-10 giờ (extended-release)",
            "onset": "30-60 phút (PO)",
            "duration": "6-8 giờ (immediate-release), 12-24 giờ (extended-release)",
            "protein_binding": "70-80%",
            "metabolism": "Gan (CYP3A4, CYP2D6) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén extended-release: không nghiền, không nhai.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, block nhĩ thất và nhịp tim chậm có thể nặng, đặc biệt khi dùng với beta-blockers. Suy tim có thể nặng lên. Không dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (atenolol, metoprolol, propranolol, bisoprolol, carvedilol)",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất, giảm nhịp tim, giảm co bóp",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng, suy tim",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp sát. Tránh dùng cùng nếu có thể. Nếu cần dùng cùng: giảm liều cả hai, theo dõi sát."
                },
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa diltiazem",
                    "effect": "Tăng nồng độ diltiazem đáng kể, tăng tác dụng phụ",
                    "management": "TRÁNH hoàn toàn bưởi chùm và nước ép bưởi chùm khi dùng diltiazem."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa diltiazem qua CYP3A4",
                    "effect": "Tăng nồng độ diltiazem đáng kể, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều diltiazem. Theo dõi ECG, nhịp tim, huyết áp sát. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Diltiazem giảm thải trừ digoxin qua thận, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin 20-50%, tăng nguy cơ ngộ độc digoxin",
                    "management": "Theo dõi nồng độ digoxin. Giảm liều digoxin 25-50% khi bắt đầu diltiazem."
                },
                {
                    "drug": "Simvastatin, Lovastatin",
                    "mechanism": "Diltiazem ức chế CYP3A4, tăng nồng độ statin",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều simvastatin/lovastatin. Hoặc đổi sang statin không chuyển hóa qua CYP3A4 (pravastatin, rosuvastatin)."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Diltiazem ức chế CYP3A4, tăng nồng độ immunosuppressant",
                    "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ cyclosporine/tacrolimus. Giảm liều nếu cần."
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin, carbamazepine)",
                    "mechanism": "Tăng chuyển hóa diltiazem qua CYP3A4",
                    "effect": "Giảm nồng độ diltiazem, giảm hiệu quả",
                    "management": "Có thể cần tăng liều diltiazem. Theo dõi huyết áp, nhịp tim."
                }
            ],
            "minor": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Có thể ức chế nhẹ chuyển hóa",
                    "effect": "Tăng nhẹ nồng độ diltiazem",
                    "management": "Theo dõi nhịp tim, huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Sick sinus syndrome không có máy tạo nhịp",
                "Suy tim nặng (EF <30%)",
                "Hạ huyết áp nặng",
                "Hội chứng Wolff-Parkinson-White với rung nhĩ",
                "Dị ứng diltiazem"
            ],
            "tương_đối": [
                "Suy tim trung bình - thận trọng (EF 30-40%, có thể làm nặng suy tim)",
                "Suy gan nặng - giảm liều 50%, thận trọng (chuyển hóa qua CYP3A4)",
                "Suy thận nặng - giảm liều 50%, thận trọng",
                "Dùng với beta-blockers - tăng nguy cơ block AV đáng kể",
                "Dùng với digoxin - tăng nồng độ digoxin",
                "Dùng với CYP3A4 inhibitors mạnh - tăng nồng độ diltiazem"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong tăng huyết áp thai kỳ hoặc rối loạn nhịp nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Diltiazem bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50% (chuyển hóa qua CYP3A4, CYP2D6)",
            "severe": "Thận trọng, giảm liều 50% hoặc tránh dùng (chuyển hóa qua CYP3A4, CYP2D6)",
            "notes": "Diltiazem chuyển hóa mạnh qua gan (CYP3A4, CYP2D6). Suy gan làm giảm chuyển hóa, tăng nồng độ diltiazem, tích lũy. Cần giảm liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Block nhĩ thất độ 2-3",
                "Nhịp tim chậm nặng (<40 bpm)",
                "Hạ huyết áp nặng",
                "Suy tim cấp",
                "Sick sinus syndrome",
                "Chóng mặt, ngất",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (có thể đảo ngược tác dụng calcium channel blocker), Atropine (cho nhịp tim chậm, block AV)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị block nhĩ thất/nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Calcium gluconate 1-3g IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Calcium gluconate 1-3g IV, nếu cần: dopamine, norepinephrine",
                "Theo dõi ECG liên tục",
                "Theo dõi huyết áp, nhịp tim, ý thức",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life 3-4.5 giờ với immediate-release, 5-10 giờ với extended-release)"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu block AV, dấu hiệu suy tim, dấu hiệu suy hô hấp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate / Calcium chloride",
                    "mechanism": "Tăng nồng độ calci trong máu, đảo ngược tác dụng calcium channel blocker",
                    "dose": "Calcium gluconate 1-3g IV hoặc Calcium chloride 1g IV",
                    "indication": "Hạ huyết áp, block AV, rối loạn nhịp do quá liều calcium channel blocker"
                },
                {
                    "name": "Atropine",
                    "mechanism": "Chẹn muscarinic, tăng nhịp tim, cải thiện dẫn truyền AV",
                    "dose": "0.5-1mg IV, có thể lặp lại",
                    "indication": "Nhịp tim chậm, block AV do quá liều diltiazem"
                },
                {
                    "name": "Isoproterenol",
                    "mechanism": "Beta-agonist, tăng nhịp tim, cải thiện dẫn truyền AV",
                    "dose": "Theo protocol",
                    "indication": "Block AV, nhịp tim chậm không đáp ứng với atropine và calcium"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Dạng extended-release: có thể uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "Dạng immediate-release: uống 3-4 lần/ngày. Dạng extended-release: uống 1-2 lần/ngày vào cùng một giờ mỗi ngày. KHÔNG nghiền, KHÔNG nhai viên extended-release."
            },
            "iv": {
                "reconstitution": "Diltiazem IV: Pha với D5W hoặc normal saline. Nồng độ: 1mg/ml",
                "infusion_rate": "Bolus: 0.25mg/kg trong 2 phút. Có thể lặp lại 0.35mg/kg sau 15 phút nếu cần. Continuous infusion: 5-15mg/giờ, điều chỉnh theo đáp ứng.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Diltiazem IV dùng cho cấp cứu rối loạn nhịp trên thất (SVT). Theo dõi ECG liên tục. Theo dõi huyết áp, nhịp tim sát. Chống chỉ định trong block AV độ 2-3, sick sinus syndrome."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cardizem (diltiazem)",
                "UpToDate - Diltiazem: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Atrial fibrillation rate control",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Extensive clinical experience and multiple RCTs in atrial fibrillation rate control and hypertension"
        }
    },

    "Verapamil": {
        "group": "Cardiovascular - Calcium Channel Blocker (Non-dihydropyridine)",
        "vietnamese_name": "Verapamil, Isoptin",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Rối loạn nhịp tim trên thất",
            "Rung nhĩ",
            "Nhịp nhanh trên thất",
            "Migraine phòng ngừa"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3",
            "Suy tim nặng",
            "Sick sinus syndrome",
            "Hạ huyết áp nặng",
            "Hội chứng Wolff-Parkinson-White với rung nhĩ"
        ],
        "dosage": {
            "adult_htn": "80-320mg x 2-3 lần/ngày",
            "adult_htn_extended": "120-480mg x 1 lần/ngày (SR)",
            "adult_angina": "80-160mg x 3 lần/ngày",
            "adult_migraine": "80-160mg x 3 lần/ngày",
            "adult_svt_iv": "2.5-5mg IV bolus, có thể lặp 5-10mg sau 15-30 phút",
            "notes": "Mạnh hơn diltiazem trong ức chế dẫn truyền nhĩ thất"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Nhịp tim chậm",
            "Block nhĩ thất",
            "Táo bón (thường gặp)",
            "Chóng mặt",
            "Mệt mỏi",
            "Phù chân (ít)"
        ],
        "interactions": [
            "Beta-blocker: tăng nguy cơ block nhĩ thất, suy tim",
            "Digoxin: tăng nồng độ digoxin đáng kể",
            "Simvastatin: tăng nồng độ simvastatin",
            "Theophylline: tăng nồng độ theophylline",
            "Carbamazepine: tăng nồng độ carbamazepine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Non-dihydropyridine calcium channel blocker (phenylalkylamine). Ức chế kênh calci L-type trong cả màng tế bào cơ trơn mạch máu và màng tế bào cơ tim. Giãn mạch ngoại vi → giảm huyết áp. Ức chế dẫn truyền nhĩ thất và làm chậm nhịp tim → giảm nhịp tim. Giảm co bóp cơ tim. Giãn mạch vành → tăng tưới máu vành. Được dùng trong tăng huyết áp, đau thắt ngực, rối loạn nhịp trên thất (như rung nhĩ), và migraine. Tương tự diltiazem nhưng mạnh hơn về ức chế co bóp.",
        "monitoring": [
            "Huyết áp và nhịp tim",
            "ECG (theo dõi block nhĩ thất, nhịp tim chậm)",
            "Dấu hiệu block nhĩ thất (nhịp tim chậm, chóng mặt, ngất) - đặc biệt quan trọng",
            "Dấu hiệu suy tim (khó thở, phù) - có thể làm nặng suy tim",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu quá liều (block nhĩ thất nặng, nhịp tim chậm nặng, hạ huyết áp)"
        ],
        "precautions": [
            "KHÔNG dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp)",
            "KHÔNG dùng ở suy tim nặng (có thể làm nặng suy tim do giảm co bóp)",
            "Thận trọng ở suy gan (giảm chuyển hóa → tích lũy)",
            "Tương tác với nhiều thuốc: tăng nồng độ với CYP3A4 inhibitors, giảm với inducers",
            "Tránh bưởi chùm (grapefruit) - ức chế CYP3A4 → tăng nồng độ",
            "Tương tác với beta-blockers → tăng nguy cơ block nhĩ thất, nhịp tim chậm",
            "Tương tác với digoxin → tăng nồng độ digoxin (theo dõi nồng độ digoxin)",
            "Tương tác với statin → tăng nguy cơ tiêu cơ vân",
            "Giảm liều ở suy gan",
            "Dạng extended-release: không nghiền, không nhai",
            "Uống với thức ăn hoặc không (tùy dạng)"
        ],
        "pharmacokinetics": {
            "half_life": "2-7 giờ (immediate-release), 12 giờ (extended-release)",
            "onset": "1-2 giờ (PO)",
            "duration": "6-8 giờ (immediate-release), 24 giờ (extended-release)",
            "protein_binding": "90%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén extended-release: không nghiền, không nhai.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, block nhĩ thất và nhịp tim chậm có thể nặng, đặc biệt khi dùng với beta-blockers. Suy tim có thể nặng lên. Không dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (atenolol, metoprolol, propranolol, bisoprolol, carvedilol)",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất, giảm nhịp tim, giảm co bóp",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng, suy tim",
                    "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp sát. Tránh dùng cùng nếu có thể. Nếu cần dùng cùng: giảm liều cả hai, theo dõi sát."
                },
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa verapamil",
                    "effect": "Tăng nồng độ verapamil đáng kể, tăng tác dụng phụ",
                    "management": "TRÁNH hoàn toàn bưởi chùm và nước ép bưởi chùm khi dùng verapamil."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa verapamil qua CYP3A4",
                    "effect": "Tăng nồng độ verapamil đáng kể, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều verapamil. Theo dõi ECG, nhịp tim, huyết áp sát. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Verapamil giảm thải trừ digoxin qua thận và tăng hấp thu, tăng nồng độ digoxin",
                    "effect": "Tăng nồng độ digoxin 50-75%, tăng nguy cơ ngộ độc digoxin đáng kể",
                    "management": "Theo dõi nồng độ digoxin. Giảm liều digoxin 50% khi bắt đầu verapamil."
                },
                {
                    "drug": "Simvastatin, Lovastatin",
                    "mechanism": "Verapamil ức chế CYP3A4, tăng nồng độ statin",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều simvastatin/lovastatin. Hoặc đổi sang statin không chuyển hóa qua CYP3A4 (pravastatin, rosuvastatin)."
                },
                {
                    "drug": "Carbamazepine, Theophylline",
                    "mechanism": "Verapamil ức chế chuyển hóa, tăng nồng độ",
                    "effect": "Tăng nồng độ carbamazepine/theophylline, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ. Giảm liều nếu cần."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Verapamil ức chế CYP3A4, tăng nồng độ immunosuppressant",
                    "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ cyclosporine/tacrolimus. Giảm liều nếu cần."
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, phenytoin)",
                    "mechanism": "Tăng chuyển hóa verapamil qua CYP3A4",
                    "effect": "Giảm nồng độ verapamil, giảm hiệu quả",
                    "management": "Có thể cần tăng liều verapamil. Theo dõi huyết áp, nhịp tim."
                }
            ],
            "minor": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Có thể ức chế nhẹ chuyển hóa",
                    "effect": "Tăng nhẹ nồng độ verapamil",
                    "management": "Theo dõi nhịp tim, huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                "Sick sinus syndrome không có máy tạo nhịp",
                "Suy tim nặng (EF <30%)",
                "Hạ huyết áp nặng",
                "Hội chứng Wolff-Parkinson-White với rung nhĩ",
                "Dị ứng verapamil"
            ],
            "tương_đối": [
                "Suy tim trung bình - thận trọng (EF 30-40%, có thể làm nặng suy tim - verapamil mạnh hơn diltiazem về giảm co bóp)",
                "Suy gan nặng - giảm liều 50%, thận trọng (chuyển hóa qua CYP3A4)",
                "Suy thận nặng - giảm liều 50%, thận trọng",
                "Dùng với beta-blockers - tăng nguy cơ block AV đáng kể",
                "Dùng với digoxin - tăng nồng độ digoxin đáng kể (50-75%)",
                "Dùng với CYP3A4 inhibitors mạnh - tăng nồng độ verapamil"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được trong tăng huyết áp thai kỳ hoặc rối loạn nhịp nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Verapamil bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50% (chuyển hóa qua CYP3A4)",
            "severe": "Thận trọng, giảm liều 50% hoặc tránh dùng (chuyển hóa qua CYP3A4)",
            "notes": "Verapamil chuyển hóa mạnh qua gan (CYP3A4). Suy gan làm giảm chuyển hóa, tăng nồng độ verapamil, tích lũy. Cần giảm liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Block nhĩ thất độ 2-3",
                "Nhịp tim chậm nặng (<40 bpm)",
                "Hạ huyết áp nặng",
                "Suy tim cấp",
                "Sick sinus syndrome",
                "Chóng mặt, ngất",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (có thể đảo ngược tác dụng calcium channel blocker), Atropine (cho nhịp tim chậm, block AV)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị block nhĩ thất/nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Calcium gluconate 1-3g IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Calcium gluconate 1-3g IV, nếu cần: dopamine, norepinephrine",
                "Theo dõi ECG liên tục",
                "Theo dõi huyết áp, nhịp tim, ý thức",
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life 2-7 giờ với immediate-release, 12 giờ với extended-release)"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu block AV, dấu hiệu suy tim, dấu hiệu suy hô hấp"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate / Calcium chloride",
                    "mechanism": "Tăng nồng độ calci trong máu, đảo ngược tác dụng calcium channel blocker",
                    "dose": "Calcium gluconate 1-3g IV hoặc Calcium chloride 1g IV",
                    "indication": "Hạ huyết áp, block AV, rối loạn nhịp do quá liều calcium channel blocker"
                },
                {
                    "name": "Atropine",
                    "mechanism": "Chẹn muscarinic, tăng nhịp tim, cải thiện dẫn truyền AV",
                    "dose": "0.5-1mg IV, có thể lặp lại",
                    "indication": "Nhịp tim chậm, block AV do quá liều verapamil"
                },
                {
                    "name": "Isoproterenol",
                    "mechanism": "Beta-agonist, tăng nhịp tim, cải thiện dẫn truyền AV",
                    "dose": "Theo protocol",
                    "indication": "Block AV, nhịp tim chậm không đáp ứng với atropine và calcium"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Dạng extended-release: có thể uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "Dạng immediate-release: uống 2-3 lần/ngày. Dạng extended-release: uống 1 lần/ngày vào cùng một giờ mỗi ngày. KHÔNG nghiền, KHÔNG nhai viên extended-release."
            },
            "iv": {
                "reconstitution": "Verapamil IV: Pha với D5W hoặc normal saline. Nồng độ: 0.25mg/ml",
                "infusion_rate": "Bolus: 2.5-5mg trong 2 phút. Có thể lặp lại 5-10mg sau 15-30 phút nếu cần. Tối đa 20mg.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Verapamil IV dùng cho cấp cứu rối loạn nhịp trên thất (SVT). Theo dõi ECG liên tục. Theo dõi huyết áp, nhịp tim sát. Chống chỉ định trong block AV độ 2-3, sick sinus syndrome. Verapamil mạnh hơn diltiazem về ức chế dẫn truyền AV."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Calan (verapamil)",
                "UpToDate - Verapamil: Drug information",
                "American Heart Association/American College of Cardiology guidelines - Atrial fibrillation rate control",
                "American Heart Association/American College of Cardiology guidelines - Hypertension"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Extensive clinical experience and multiple RCTs in atrial fibrillation rate control and hypertension"
        }
    },
}

__all__ = ['NON_DIHYDROPYRIDINE_CCB']
