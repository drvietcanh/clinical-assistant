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
        "last_updated": "2025-02-18"
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
        "last_updated": "2025-02-18"
    }
}

__all__ = ['NON_DIHYDROPYRIDINE_CCB']
