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
            "adult_start": "120mg x 2 lần/ngày (immediate-release) hoặc 180mg x 1 lần/ngày (extended-release)",
            "adult_usual": "180-240mg x 2 lần/ngày (immediate-release) hoặc 240-360mg x 1 lần/ngày (extended-release)",
            "adult_max": "360mg/ngày",
            "elderly": "Khởi đầu 60-120mg x 2 lần/ngày, tăng dần. Người cao tuổi nhạy cảm hơn với tác dụng phụ.",
            "renal_adjustment_dosage": {
                "normal": "120-360mg/ngày chia 1-3 lần",
                "30_60": "60-180mg/ngày chia 1-2 lần (giảm liều 50%)",
                "under_30": "60-120mg/ngày chia 1-2 lần (giảm liều 50%)",
                "dialysis": "Không có dữ liệu cụ thể"
            },
            "hepatic_adjustment_dosage": {
                "mild": "120-360mg/ngày",
                "moderate": "Giảm liều, thận trọng",
                "severe": "Giảm liều đáng kể, thận trọng"
            },
            "administration_route": "PO, IV",
            "frequency": "1-3 lần/ngày (PO), bolus hoặc truyền liên tục (IV)",
            "with_food": "Có thể uống với hoặc không thức ăn",
            "notes": "Non-dihydropyridine, có tác dụng ức chế dẫn truyền nhĩ thất. Chuyển hóa qua gan (CYP3A4), cần điều chỉnh liều ở suy gan. Tránh grapefruit juice."
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
        "mechanism_of_action": "Diltiazem là non-dihydropyridine calcium channel blocker thuộc nhóm benzothiazepine. Cơ chế tác dụng: (1) Ức chế chọn lọc kênh calci L-type voltage-gated trên cả màng tế bào cơ trơn mạch máu và màng tế bào cơ tim. Ngăn cản dòng calci vào trong tế bào, dẫn đến giảm nồng độ calci nội bào. (2) Tác dụng trên mạch máu: Giãn mạch ngoại vi (arterioles), giảm sức cản mạch máu hệ thống (SVR), giảm huyết áp. Giãn mạch vành, tăng tưới máu cơ tim, giảm nhu cầu oxy cơ tim (dùng trong đau thắt ngực). (3) Tác dụng trên tim: Ức chế dẫn truyền nhĩ thất (AV node), làm chậm nhịp tim, giảm co bóp cơ tim nhẹ. Điều này làm cho diltiazem hiệu quả trong điều trị rối loạn nhịp trên thất (SVT, rung nhĩ) và kiểm soát nhịp tim. (4) Khác với dihydropyridine CCB (như amlodipine): Diltiazem có tác dụng đáng kể trên tim (ức chế AV node, giảm co bóp), không chỉ trên mạch máu. Diltiazem chuyển hóa qua gan (CYP3A4, CYP2D6), thải trừ chủ yếu qua gan, cần điều chỉnh liều ở suy gan.",
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
        "black_box_warnings": "Không có black box warning. Tuy nhiên, block nhĩ thất và nhịp tim chậm có thể nặng.",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"cardiovascular": "AV block, bradycardia, heart failure exacerbation", "hepatic": "Hepatotoxicity (rare)"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (AV block - Black Box Warning)", "Heart rate (bradycardia)", "Blood pressure", "Hepatic function (hepatotoxicity risk)", "CYP3A4 interactions (grapefruit juice)"],
            "look_alike_sound_alike": ["Diltiazem", "Diltiazem"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Heart Failure (contraindicated in severe HF)",
            "ACC/AHA Guidelines - Atrial Fibrillation",
            "ACC/AHA Guidelines - Hypertension",
            "ESC Guidelines - Atrial Fibrillation",
            "WHO Essential Medicines List"
        ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Có thể gây nhịp tim chậm thai nhi, hạ huyết áp. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Diltiazem bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu nhịp tim chậm hoặc hạ huyết áp."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều (chuyển hóa qua gan CYP3A4)",
            "severe": "Giảm liều đáng kể, thận trọng (chuyển hóa qua gan)",
            "notes": "Diltiazem chuyển hóa qua gan (CYP3A4, CYP2D6). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ (block AV, nhịp tim chậm). Cần giảm liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Block nhĩ thất độ 2-3 (nghiêm trọng)",
                "Nhịp tim chậm nặng (<40 bpm)",
                "Hạ huyết áp nặng",
                "Suy tim cấp (do giảm co bóp)",
                "Chóng mặt, ngất",
                "Sốc tim"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride IV (đối kháng với calcium channel blocker)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị block AV/nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Isoproterenol, hoặc máy tạo nhịp tạm thời",
                "Calcium gluconate 10%: 10-30ml IV hoặc Calcium chloride 10%: 5-10ml IV (đối kháng với calcium channel blocker)",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Theo dõi ECG liên tục",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life 3-4.5 giờ cho immediate-release, 5-10 giờ cho extended-release)"
            ],
            "monitoring": "ECG liên tục (block AV, rối loạn nhịp), huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu sống"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate hoặc Calcium chloride",
                    "mechanism": "Đối kháng với calcium channel blocker bằng cách tăng nồng độ calci ngoại bào",
                    "indication": "Block AV, nhịp tim chậm, hạ huyết áp do quá liều calcium channel blocker",
                    "dose": "Calcium gluconate 10%: 10-30ml IV, hoặc Calcium chloride 10%: 5-10ml IV"
                },
                {
                    "name": "Atropine",
                    "mechanism": "Ức chế phó giao cảm, tăng nhịp tim",
                    "indication": "Nhịp tim chậm, block AV",
                    "dose": "0.5-1mg IV, có thể lặp lại"
                }
            ],
            "notes": "Calcium là antidote chính cho quá liều calcium channel blocker. Có thể cần máy tạo nhịp tạm thời nếu block AV nặng."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng đáng kể bởi thức ăn.",
                "timing": "Uống 1-3 lần/ngày tùy dạng (immediate-release: 2-3 lần/ngày, extended-release: 1 lần/ngày). Uống cùng giờ mỗi ngày. Dạng extended-release: KHÔNG nghiền, KHÔNG nhai viên nén.",
                "notes": "Tránh grapefruit juice (ức chế CYP3A4, tăng nồng độ). Uống đều đặn hàng ngày. Nếu quên liều, uống ngay khi nhớ ra, nhưng nếu gần đến liều tiếp theo thì bỏ qua liều đã quên và tiếp tục lịch trình bình thường."
            },
            "iv": {
                "reconstitution": "Diltiazem IV: Pha loãng trong 50-100ml D5W hoặc normal saline",
                "infusion_rate": "Bolus: 0.25mg/kg IV trong 2 phút, có thể lặp lại 0.35mg/kg sau 15 phút nếu cần. Truyền liên tục: 5-15mg/giờ, điều chỉnh theo đáp ứng.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": [],
                "notes": "Dạng IV dùng cho cấp cứu rối loạn nhịp trên thất (SVT). Theo dõi ECG liên tục, huyết áp, nhịp tim. Ngừng ngay nếu có block AV độ 2-3 hoặc nhịp tim chậm <50 bpm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cardizem (diltiazem), Cardizem IV",
                "UpToDate - Diltiazem: Drug information",
                "Micromedex - Diltiazem",
                "Lexicomp - Diltiazem"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "A - Dựa trên FDA labeling, UpToDate, và các guidelines chính thức (ACC/AHA, ESC)"
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
            "adult_start": "80mg x 3 lần/ngày (immediate-release) hoặc 120mg x 1 lần/ngày (extended-release)",
            "adult_usual": "120-240mg x 3 lần/ngày (immediate-release) hoặc 240-480mg x 1 lần/ngày (extended-release)",
            "adult_max": "480mg/ngày",
            "elderly": "Khởi đầu 40mg x 3 lần/ngày, tăng dần. Người cao tuổi nhạy cảm hơn với tác dụng phụ.",
            "renal_adjustment_dosage": {
                "normal": "80-320mg x 2-3 lần/ngày",
                "30_60": "40-160mg x 2-3 lần/ngày (giảm liều 25-50%)",
                "under_30": "40-80mg x 2-3 lần/ngày (giảm liều 50%)",
                "dialysis": "Không có dữ liệu cụ thể"
            },
            "hepatic_adjustment_dosage": {
                "mild": "80-320mg x 2-3 lần/ngày",
                "moderate": "Giảm liều, thận trọng",
                "severe": "Giảm liều đáng kể, thận trọng"
            },
            "administration_route": "PO, IV",
            "frequency": "2-3 lần/ngày (PO immediate-release), 1 lần/ngày (PO extended-release), bolus (IV)",
            "with_food": "Có thể uống với hoặc không thức ăn",
            "notes": "Mạnh hơn diltiazem trong ức chế dẫn truyền nhĩ thất. Chuyển hóa qua gan (CYP3A4), cần điều chỉnh liều ở suy gan. Tránh grapefruit juice."
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
        "mechanism_of_action": "Verapamil là non-dihydropyridine calcium channel blocker thuộc nhóm phenylalkylamine. Cơ chế tác dụng: (1) Ức chế chọn lọc kênh calci L-type voltage-gated trên cả màng tế bào cơ trơn mạch máu và màng tế bào cơ tim. Ngăn cản dòng calci vào trong tế bào, dẫn đến giảm nồng độ calci nội bào. (2) Tác dụng trên mạch máu: Giãn mạch ngoại vi (arterioles), giảm sức cản mạch máu hệ thống (SVR), giảm huyết áp. Giãn mạch vành, tăng tưới máu cơ tim, giảm nhu cầu oxy cơ tim (dùng trong đau thắt ngực). (3) Tác dụng trên tim: Ức chế mạnh dẫn truyền nhĩ thất (AV node), làm chậm nhịp tim, giảm co bóp cơ tim đáng kể (mạnh hơn diltiazem). Điều này làm cho verapamil rất hiệu quả trong điều trị rối loạn nhịp trên thất (SVT, rung nhĩ) nhưng cũng làm tăng nguy cơ block AV và suy tim. (4) Khác với dihydropyridine CCB: Verapamil có tác dụng mạnh trên tim (ức chế AV node, giảm co bóp), không chỉ trên mạch máu. Verapamil mạnh hơn diltiazem trong ức chế co bóp cơ tim. (5) Tác dụng trên migraine: Cơ chế chưa rõ hoàn toàn, có thể liên quan đến giảm co mạch não và giảm giải phóng chất dẫn truyền thần kinh. Verapamil chuyển hóa qua gan (CYP3A4), thải trừ chủ yếu qua gan, cần điều chỉnh liều ở suy gan.",
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
        "black_box_warnings": "Không có black box warning. Tuy nhiên, block nhĩ thất và nhịp tim chậm có thể nặng.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"cardiovascular": "Severe AV block, bradycardia, heart failure exacerbation - Black Box Warning", "hepatic": "Hepatotoxicity (rare)"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (AV block - Black Box Warning)", "Heart rate (bradycardia)", "Blood pressure", "Hepatic function (hepatotoxicity risk)", "CYP3A4 interactions (grapefruit juice)", "Digoxin levels (increases digoxin)"],
            "look_alike_sound_alike": ["Verapamil", "Verapamil"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Heart Failure (contraindicated in severe HF)",
            "ACC/AHA Guidelines - Atrial Fibrillation",
            "ACC/AHA Guidelines - Hypertension",
            "ESC Guidelines - Atrial Fibrillation",
            "WHO Essential Medicines List"
        ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Nghiên cứu trên động vật cho thấy có thể gây hại cho thai nhi. Không có nghiên cứu đầy đủ trên người. Có thể gây nhịp tim chậm thai nhi, hạ huyết áp. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Verapamil bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu nhịp tim chậm hoặc hạ huyết áp."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều (chuyển hóa qua gan CYP3A4)",
            "severe": "Giảm liều đáng kể, thận trọng (chuyển hóa qua gan)",
            "notes": "Verapamil chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ (block AV, nhịp tim chậm, suy tim). Cần giảm liều đáng kể ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Block nhĩ thất độ 2-3 (nghiêm trọng, có thể gây tử vong)",
                "Nhịp tim chậm nặng (<40 bpm)",
                "Hạ huyết áp nặng",
                "Suy tim cấp (do giảm co bóp mạnh)",
                "Chóng mặt, ngất",
                "Sốc tim",
                "Táo bón nặng (do giảm nhu động ruột)"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride IV (đối kháng với calcium channel blocker)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị block AV/nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Isoproterenol, hoặc máy tạo nhịp tạm thời (QUAN TRỌNG)",
                "Calcium gluconate 10%: 10-30ml IV hoặc Calcium chloride 10%: 5-10ml IV (đối kháng với calcium channel blocker)",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Điều trị suy tim: Inotropes (dobutamine, milrinone) nếu cần",
                "Theo dõi ECG liên tục",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 24-48 giờ (do half-life 2-7 giờ cho immediate-release, 12 giờ cho extended-release)"
            ],
            "monitoring": "ECG liên tục (block AV, rối loạn nhịp), huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu sống, chức năng thận (do hạ huyết áp)"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate hoặc Calcium chloride",
                    "mechanism": "Đối kháng với calcium channel blocker bằng cách tăng nồng độ calci ngoại bào",
                    "indication": "Block AV, nhịp tim chậm, hạ huyết áp, suy tim do quá liều calcium channel blocker",
                    "dose": "Calcium gluconate 10%: 10-30ml IV, hoặc Calcium chloride 10%: 5-10ml IV"
                },
                {
                    "name": "Atropine",
                    "mechanism": "Ức chế phó giao cảm, tăng nhịp tim",
                    "indication": "Nhịp tim chậm, block AV",
                    "dose": "0.5-1mg IV, có thể lặp lại"
                }
            ],
            "notes": "Calcium là antidote chính cho quá liều calcium channel blocker. Máy tạo nhịp tạm thời có thể cần thiết nếu block AV nặng không đáp ứng với calcium và atropine."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng đáng kể bởi thức ăn.",
                "timing": "Uống 2-3 lần/ngày (immediate-release) hoặc 1 lần/ngày (extended-release). Uống cùng giờ mỗi ngày. Dạng extended-release: KHÔNG nghiền, KHÔNG nhai viên nén.",
                "notes": "Tránh grapefruit juice (ức chế CYP3A4, tăng nồng độ). Uống đều đặn hàng ngày. Nếu quên liều, uống ngay khi nhớ ra, nhưng nếu gần đến liều tiếp theo thì bỏ qua liều đã quên và tiếp tục lịch trình bình thường. Táo bón là tác dụng phụ thường gặp."
            },
            "iv": {
                "reconstitution": "Verapamil IV: Pha loãng trong 50-100ml D5W hoặc normal saline",
                "infusion_rate": "Bolus: 2.5-5mg IV trong 2 phút, có thể lặp lại 5-10mg sau 15-30 phút nếu cần. Tối đa 20mg cho liều đầu tiên.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": [],
                "notes": "Dạng IV dùng cho cấp cứu rối loạn nhịp trên thất (SVT). Theo dõi ECG liên tục, huyết áp, nhịp tim. Ngừng ngay nếu có block AV độ 2-3 hoặc nhịp tim chậm <50 bpm. CHỐNG CHỈ ĐỊNH trong WPW với rung nhĩ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Isoptin (verapamil), Verapamil IV",
                "UpToDate - Verapamil: Drug information",
                "Micromedex - Verapamil",
                "Lexicomp - Verapamil"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "A - Dựa trên FDA labeling, UpToDate, và các guidelines chính thức (ACC/AHA, ESC)"
        }
    }
}

__all__ = ['NON_DIHYDROPYRIDINE_CCB']
