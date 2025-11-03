"""
Drug Database - Common Medications in Vietnam
Database 100-200 thuốc phổ biến tại Việt Nam
Ưu tiên thuốc thường dùng trong lâm sàng
"""

DRUG_DATABASE = {
    # ========== CARDIOVASCULAR ==========
    
    # ACE Inhibitors
    "Captopril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Captopril, Capoten",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Bảo vệ thận trong đái tháo đường",
            "Sau nhồi máu cơ tim"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên",
            "Phù mạch trước đây với ACE inhibitor"
        ],
        "dosage": {
            "adult_htn": "12.5-50mg x 2-3 lần/ngày",
            "adult_heart_failure": "6.25mg x 3 lần/ngày, tăng dần đến 50mg x 3 lần/ngày",
            "adult_post_mi": "6.25mg x 3 lần/ngày, tăng đến 50mg x 3 lần/ngày",
            "notes": "Khởi đầu với liều thấp, tăng dần. Uống 1 giờ trước bữa ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Không dùng nếu CrCl <10"
        },
        "side_effects": [
            "Ho khan (phổ biến)",
            "Tăng kali máu",
            "Hạ huyết áp",
            "Phù mạch (hiếm nhưng nguy hiểm)",
            "Suy thận cấp (hẹp ĐM thận)"
        ],
        "interactions": [
            "Kali bổ sung: tăng nguy cơ tăng kali máu",
            "Spironolactone: tăng kali máu",
            "NSAID: giảm hiệu quả, tăng nguy cơ suy thận",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "D - Chống chỉ định trong thai kỳ"
    },
    
    "Enalapril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Enalapril, Renitec",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Bảo vệ thận trong đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "5-40mg x 1-2 lần/ngày",
            "adult_heart_failure": "2.5mg x 2 lần/ngày, tăng dần đến 10-20mg x 2 lần/ngày",
            "notes": "Khởi đầu với liều thấp, tăng dần"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 2.5mg/ngày",
            "under_30": "Liều khởi đầu 2.5mg/ngày, theo dõi sát"
        },
        "side_effects": [
            "Ho khan",
            "Tăng kali máu",
            "Hạ huyết áp",
            "Phù mạch"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "Diuretics: tăng nguy cơ hạ huyết áp",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D"
    },
    
    "Lisinopril": {
        "group": "Cardiovascular - ACE Inhibitor",
        "vietnamese_name": "Lisinopril, Zestril",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Sau nhồi máu cơ tim"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "10-40mg x 1 lần/ngày",
            "adult_heart_failure": "5mg x 1 lần/ngày, tăng đến 20-40mg x 1 lần/ngày",
            "notes": "Liều hàng ngày 1 lần"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 5-10mg/ngày",
            "under_30": "Liều khởi đầu 2.5-5mg/ngày"
        },
        "side_effects": [
            "Ho khan",
            "Tăng kali máu",
            "Hạ huyết áp"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D"
    },
    
    # ARBs
    "Losartan": {
        "group": "Cardiovascular - ARB (Angiotensin Receptor Blocker)",
        "vietnamese_name": "Losartan, Cozaar",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim (không dung nạp ACE inhibitor)",
            "Bảo vệ thận trong đái tháo đường"
        ],
        "contraindications": [
            "Dị ứng ARB",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "50-100mg x 1-2 lần/ngày",
            "adult_heart_failure": "25-50mg x 1 lần/ngày, tăng đến 50-100mg x 1 lần/ngày",
            "notes": "Ít gây ho hơn ACE inhibitor"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Liều khởi đầu 25mg/ngày",
            "under_30": "Thận trọng, theo dõi sát"
        },
        "side_effects": [
            "Ít tác dụng phụ hơn ACE inhibitor",
            "Ho ít hơn ACE inhibitor",
            "Tăng kali máu (ít hơn ACE)",
            "Hạ huyết áp"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D"
    },
    
    # Beta-blockers
    "Metoprolol": {
        "group": "Cardiovascular - Beta-blocker",
        "vietnamese_name": "Metoprolol, Betaloc",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Rối loạn nhịp tim",
            "Sau nhồi máu cơ tim",
            "Đau thắt ngực"
        ],
        "contraindications": [
            "Hen phế quản nặng",
            "Block nhĩ thất độ 2-3",
            "Suy tim cấp không bù",
            "Nhịp tim chậm nặng"
        ],
        "dosage": {
            "adult_po": "25-200mg x 2 lần/ngày (tartrate) hoặc 50-200mg x 1 lần/ngày (succinate)",
            "adult_iv": "2.5-5mg IV mỗi 5 phút x 3 lần (tối đa 15mg)",
            "heart_failure": "12.5-25mg x 2 lần/ngày, tăng dần đến 200mg x 2 lần/ngày",
            "notes": "Tartrate: ngắn tác dụng, Succinate: dài tác dụng"
        },
        "side_effects": [
            "Mệt mỏi",
            "Lạnh tay chân",
            "Nhịp tim chậm",
            "Rối loạn giấc ngủ",
            "Khó thở ở bệnh nhân hen/COPD"
        ],
        "interactions": [
            "Verapamil/Diltiazem: tăng nguy cơ block nhĩ thất",
            "Insulin: che dấu triệu chứng hạ đường huyết",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "C"
    },
    
    "Propranolol": {
        "group": "Cardiovascular - Beta-blocker (non-selective)",
        "vietnamese_name": "Propranolol, Inderal",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Đau thắt ngực",
            "Rối loạn nhịp tim",
            "Migraine phòng ngừa",
            "Run cơ",
            "Lo âu"
        ],
        "contraindications": [
            "Hen phế quản",
            "Suy tim cấp",
            "Block nhĩ thất độ 2-3",
            "Nhịp tim chậm nặng"
        ],
        "dosage": {
            "adult_htn": "40-160mg x 2 lần/ngày",
            "adult_angina": "80-320mg x 2-3 lần/ngày",
            "adult_migraine": "20-40mg x 2-3 lần/ngày",
            "notes": "Non-selective, ức chế cả beta1 và beta2"
        },
        "side_effects": [
            "Mệt mỏi",
            "Lạnh tay chân",
            "Nhịp tim chậm",
            "Co thắt phế quản",
            "Giảm libido"
        ],
        "interactions": [
            "Verapamil: tăng nguy cơ block nhĩ thất",
            "Insulin: che dấu triệu chứng hạ đường huyết"
        ],
        "pregnancy": "C"
    },
    
    # Calcium Channel Blockers
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
        "pregnancy": "C"
    },
    
    # Diuretics
    "Furosemide": {
        "group": "Cardiovascular - Loop Diuretic",
        "vietnamese_name": "Furosemide, Lasix",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Phù (suy tim, xơ gan, suy thận)",
            "Tăng huyết áp",
            "Suy tim cấp",
            "Tăng kali máu"
        ],
        "contraindications": [
            "Vô niệu",
            "Mất nước nặng",
            "Hạ kali máu nặng",
            "Dị ứng sulfonamide"
        ],
        "dosage": {
            "adult_po": "20-80mg x 1-2 lần/ngày",
            "adult_iv": "20-80mg IV (có thể lặp lại)",
            "adult_iv_continuous": "5-40mg/giờ truyền liên tục",
            "heart_failure_acute": "20-40mg IV, có thể lặp lại",
            "notes": "Theo dõi cân bằng dịch, điện giải"
        },
        "side_effects": [
            "Hạ kali máu",
            "Hạ natri máu",
            "Mất nước",
            "Tăng acid uric",
            "Điếc tạm thời (IV liều cao)",
            "Tăng đường huyết"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ ngộ độc digoxin (hạ kali)",
            "Aminoglycosides: tăng độc tính thính giác",
            "NSAID: giảm hiệu quả",
            "Lithium: tăng nồng độ lithium"
        ],
        "pregnancy": "C"
    },
    
    "Hydrochlorothiazide": {
        "group": "Cardiovascular - Thiazide Diuretic",
        "vietnamese_name": "Hydrochlorothiazide, HCTZ",
        "administration": ["PO"],
        "indications": [
            "Tăng huyết áp",
            "Phù (suy tim nhẹ)",
            "Sỏi thận canxi"
        ],
        "contraindications": [
            "Dị ứng sulfonamide",
            "Vô niệu",
            "Hạ kali máu nặng"
        ],
        "dosage": {
            "adult_htn": "12.5-50mg x 1 lần/ngày",
            "adult_edema": "25-100mg x 1-2 lần/ngày",
            "notes": "Liều thấp (12.5-25mg) đủ cho tăng huyết áp"
        },
        "side_effects": [
            "Hạ kali máu",
            "Hạ natri máu",
            "Tăng đường huyết",
            "Tăng acid uric",
            "Tăng cholesterol"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ ngộ độc digoxin",
            "Lithium: tăng nồng độ lithium",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "C"
    },
    
    # Antiarrhythmics
    "Amiodarone": {
        "group": "Cardiovascular - Antiarrhythmic (Class III)",
        "vietnamese_name": "Amiodarone, Cordarone",
        "administration": ["PO", "IV"],
        "indications": [
            "Rối loạn nhịp thất",
            "Rung nhĩ",
            "Nhịp nhanh trên thất",
            "Rối loạn nhịp kháng trị"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
            "Rối loạn chức năng tuyến giáp",
            "Bệnh phổi mạn tính",
            "Bệnh gan nặng"
        ],
        "dosage": {
            "adult_po_loading": "800-1600mg/ngày chia 2 lần x 1-2 tuần",
            "adult_po_maintenance": "200-400mg x 1 lần/ngày",
            "adult_iv_loading": "150mg IV trong 10 phút, sau đó 1mg/phút x 6 giờ, 0.5mg/phút x 18 giờ",
            "notes": "Theo dõi chức năng gan, phổi, tuyến giáp định kỳ"
        },
        "side_effects": [
            "Bệnh phổi do amiodarone (nguy hiểm)",
            "Rối loạn chức năng tuyến giáp",
            "Bệnh gan",
            "Tích tụ ở da (màu xanh xám)",
            "Nhạy cảm với ánh sáng",
            "Corneal deposits",
            "Block nhĩ thất"
        ],
        "interactions": [
            "Digoxin: tăng nồng độ digoxin (giảm liều digoxin 50%)",
            "Warfarin: tăng tác dụng chống đông",
            "Statins: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "D"
    },
    
    "Digoxin": {
        "group": "Cardiovascular - Cardiac Glycoside",
        "vietnamese_name": "Digoxin, Lanoxin",
        "administration": ["PO", "IV"],
        "indications": [
            "Suy tim với rung nhĩ",
            "Rung nhĩ kiểm soát tần số",
            "Suy tim không rung nhĩ (ít dùng)"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3",
            "Nhịp tim chậm nặng",
            "Hội chứng Wolff-Parkinson-White",
            "Ngộ độc digoxin"
        ],
        "dosage": {
            "adult_po_loading": "0.5-1mg chia 2-3 lần/ngày x 1 ngày",
            "adult_po_maintenance": "0.125-0.25mg x 1 lần/ngày",
            "adult_iv": "0.25-0.5mg IV x 1 lần",
            "elderly": "Liều thấp hơn (0.0625-0.125mg/ngày)",
            "notes": "Theo dõi nồng độ digoxin (mục tiêu 0.8-2 ng/mL)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%",
            "hemodialysis": "Bổ sung sau lọc máu"
        },
        "side_effects": [
            "Ngộ độc digoxin (buồn nôn, rối loạn nhịp, rối loạn thị giác)",
            "Nhịp tim chậm",
            "Block nhĩ thất",
            "Rối loạn nhịp (ngoại tâm thu, nhịp nhanh thất)"
        ],
        "interactions": [
            "Amiodarone: tăng nồng độ digoxin (giảm liều 50%)",
            "Furosemide: tăng nguy cơ ngộ độc (hạ kali)",
            "Verapamil: tăng nồng độ digoxin",
            "Quinine: tăng nồng độ digoxin"
        ],
        "pregnancy": "C"
    },
    
    # Anticoagulants
    "Warfarin": {
        "group": "Cardiovascular - Anticoagulant (Vitamin K Antagonist)",
        "vietnamese_name": "Warfarin, Coumadin",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ",
            "Huyết khối tĩnh mạch sâu (DVT)",
            "Thuyên tắc phổi (PE)",
            "Sau phẫu thuật tim mạch",
            "Thay van tim cơ học"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Có thai (3 tháng đầu và cuối)",
            "Bệnh gan nặng",
            "Không tuân thủ điều trị"
        ],
        "dosage": {
            "adult_loading": "5-10mg x 1 lần/ngày x 2-3 ngày",
            "adult_maintenance": "2-10mg x 1 lần/ngày (theo INR)",
            "target_inr": "2.0-3.0 (hầu hết), 2.5-3.5 (van tim cơ học)",
            "notes": "Theo dõi INR thường xuyên, điều chỉnh liều theo INR"
        },
        "side_effects": [
            "Chảy máu (nặng có thể tử vong)",
            "Hoại tử da (hiếm, ngày 3-10)",
            "Dị tật thai nhi",
            "Tăng nguy cơ loãng xương"
        ],
        "interactions": [
            "Aspirin/NSAID: tăng nguy cơ chảy máu",
            "Metronidazole: tăng tác dụng warfarin",
            "Vitamin K: giảm tác dụng",
            "Nhiều thuốc khác (xem interaction checker)"
        ],
        "pregnancy": "X - Chống chỉ định (trừ trường hợp đặc biệt)"
    },
    
    # Antiplatelets
    "Aspirin": {
        "group": "Cardiovascular - Antiplatelet",
        "vietnamese_name": "Aspirin, Acetylsalicylic acid",
        "administration": ["PO"],
        "indications": [
            "Dự phòng nhồi máu cơ tim",
            "Dự phòng đột quỵ",
            "Sau đặt stent",
            "Đau, sốt, viêm",
            "Viêm khớp dạng thấp"
        ],
        "contraindications": [
            "Loét dạ dày tá tràng đang hoạt động",
            "Chảy máu đang hoạt động",
            "Dị ứng aspirin",
            "Trẻ em <12 tuổi (hội chứng Reye)"
        ],
        "dosage": {
            "adult_cardioprotective": "75-100mg x 1 lần/ngày",
            "adult_pain": "325-650mg mỗi 4-6 giờ",
            "adult_arthritis": "325-650mg x 4 lần/ngày",
            "notes": "Liều thấp (75-100mg) cho dự phòng tim mạch"
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Loét dạ dày tá tràng",
            "Chảy máu nói chung",
            "Ù tai (liều cao)",
            "Co thắt phế quản (ở bệnh nhân hen)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "NSAID khác: tăng nguy cơ chảy máu dạ dày",
            "ACE inhibitor: giảm hiệu quả hạ huyết áp"
        ],
        "pregnancy": "C - D trong 3 tháng cuối"
    },
    
    "Clopidogrel": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Clopidogrel, Plavix",
        "administration": ["PO"],
        "indications": [
            "Sau nhồi máu cơ tim",
            "Sau đặt stent",
            "Hội chứng mạch vành cấp",
            "Đột quỵ/TIA",
            "Bệnh động mạch ngoại biên"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Loét dạ dày tá tràng nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_loading": "300-600mg x 1 lần",
            "adult_maintenance": "75mg x 1 lần/ngày",
            "notes": "Dùng kèm aspirin sau ACS/stent (dual antiplatelet therapy)"
        },
        "side_effects": [
            "Chảy máu",
            "Giảm tiểu cầu",
            "Tăng nguy cơ xuất huyết",
            "Ban xuất huyết giảm tiểu cầu huyết khối (TTP) - hiếm"
        ],
        "interactions": [
            "Omeprazole: giảm hiệu quả clopidogrel",
            "Aspirin: tăng nguy cơ chảy máu (nhưng có chỉ định)",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B"
    },
    
    # Statins
    "Atorvastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Atorvastatin, Lipitor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch",
            "Sau nhồi máu cơ tim",
            "Bệnh động mạch vành"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú",
            "Tiêu cơ vân đang hoạt động"
        ],
        "dosage": {
            "adult_standard": "10-80mg x 1 lần/ngày",
            "adult_high_intensity": "40-80mg x 1 lần/ngày",
            "notes": "Uống bất kỳ lúc nào trong ngày, có thể uống với thức ăn"
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Tăng men gan",
            "Tăng đường huyết",
            "Suy giảm trí nhớ (hiếm)"
        ],
        "interactions": [
            "Clarithromycin/Erythromycin: tăng nguy cơ tiêu cơ vân",
            "Grapefruit juice: tăng nồng độ (với liều cao)",
            "Cyclosporine: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "X"
    },
    
    "Simvastatin": {
        "group": "Cardiovascular - Statin",
        "vietnamese_name": "Simvastatin, Zocor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "adult_standard": "10-40mg x 1 lần/ngày",
            "adult_max": "80mg x 1 lần/ngày (hiếm dùng)",
            "notes": "Uống buổi tối, tránh grapefruit juice"
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân",
            "Tăng men gan"
        ],
        "interactions": [
            "Amiodarone: giảm liều simvastatin xuống tối đa 20mg/ngày",
            "Verapamil: giảm liều simvastatin",
            "Grapefruit juice: tăng nồng độ"
        ],
        "pregnancy": "X"
    },
    
    # ========== DIABETES ==========
    
    "Metformin": {
        "group": "Diabetes - Biguanide",
        "vietnamese_name": "Metformin, Glucophage",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Hội chứng buồng trứng đa nang (PCOS)",
            "Dự phòng đái tháo đường"
        ],
        "contraindications": [
            "Suy thận (CrCl <30 hoặc eGFR <30)",
            "Toan chuyển hóa",
            "Nhiễm toan lactic",
            "Suy gan nặng",
            "Suy tim nặng",
            "Dùng thuốc cản quang (tạm ngừng)"
        ],
        "dosage": {
            "adult_start": "500mg x 2 lần/ngày với bữa ăn",
            "adult_usual": "500-1000mg x 2-3 lần/ngày",
            "adult_max": "1000mg x 2 lần/ngày (2000mg/ngày)",
            "extended_release": "500-2000mg x 1 lần/ngày với bữa ăn tối",
            "notes": "Khởi đầu với liều thấp, tăng dần. Tạm ngừng khi dùng thuốc cản quang"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Chống chỉ định"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Đau bụng",
            "Nhiễm toan lactic (hiếm nhưng nguy hiểm)",
            "Hạ đường huyết (ít khi)",
            "Thiếu vitamin B12 (dùng lâu dài)"
        ],
        "interactions": [
            "Thuốc cản quang: tăng nguy cơ nhiễm toan lactic - ngừng 48h trước và sau",
            "Rượu: tăng nguy cơ nhiễm toan lactic",
            "Furosemide: có thể tăng nồng độ metformin"
        ],
        "pregnancy": "B"
    },
    
    "Glibenclamide": {
        "group": "Diabetes - Sulfonylurea",
        "vietnamese_name": "Glibenclamide, Daonil",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton do đái tháo đường",
            "Suy thận nặng",
            "Suy gan nặng",
            "Có thai"
        ],
        "dosage": {
            "adult_start": "2.5-5mg x 1 lần/ngày trước bữa sáng",
            "adult_usual": "5-15mg/ngày chia 1-2 lần",
            "adult_max": "20mg/ngày",
            "notes": "Nguy cơ hạ đường huyết cao, đặc biệt ở người già, suy thận"
        },
        "side_effects": [
            "Hạ đường huyết (thường gặp, có thể nặng)",
            "Tăng cân",
            "Ban da",
            "Rối loạn tiêu hóa"
        ],
        "interactions": [
            "Warfarin: có thể tăng tác dụng chống đông",
            "Rượu: tăng nguy cơ hạ đường huyết",
            "Beta-blocker: che dấu triệu chứng hạ đường huyết"
        ],
        "pregnancy": "C - Tránh dùng trong thai kỳ"
    },
    
    "Gliclazide": {
        "group": "Diabetes - Sulfonylurea",
        "vietnamese_name": "Gliclazide, Diamicron",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_standard": "80-320mg/ngày chia 1-2 lần",
            "adult_modified_release": "30-120mg x 1 lần/ngày",
            "notes": "Ít nguy cơ hạ đường huyết hơn glibenclamide"
        },
        "side_effects": [
            "Hạ đường huyết",
            "Tăng cân",
            "Ban da"
        ],
        "interactions": [
            "Tương tự sulfonylurea khác"
        ],
        "pregnancy": "C"
    },
    
    "Insulin": {
        "group": "Diabetes - Insulin",
        "vietnamese_name": "Insulin",
        "administration": ["SC", "IV"],
        "indications": [
            "Đái tháo đường type 1",
            "Đái tháo đường type 2 (khi không kiểm soát bằng thuốc uống)",
            "Nhiễm toan ceton do đái tháo đường",
            "Tăng đường huyết tăng áp lực thẩm thấu",
            "Tăng đường huyết trong bệnh viện"
        ],
        "contraindications": [
            "Hạ đường huyết",
            "Dị ứng insulin"
        ],
        "dosage": {
            "type1_basal": "0.2-0.4 đơn vị/kg/ngày (NPH hoặc insulin dài)",
            "type1_bolus": "0.5-1 đơn vị/kg/ngày chia trước bữa ăn",
            "dka_iv": "0.1 đơn vị/kg/giờ IV truyền liên tục",
            "hospital_hyperglycemia": "0.05-0.1 đơn vị/kg/giờ",
            "notes": "Nhiều loại: rapid-acting, short-acting, intermediate, long-acting. Điều chỉnh theo đường huyết"
        },
        "side_effects": [
            "Hạ đường huyết (nguy hiểm)",
            "Tăng cân",
            "Phản ứng tại chỗ tiêm",
            "Kháng insulin (hiếm)"
        ],
        "interactions": [
            "Beta-blocker: che dấu triệu chứng hạ đường huyết",
            "Corticosteroid: tăng đường huyết",
            "Rượu: tăng nguy cơ hạ đường huyết"
        ],
        "pregnancy": "B - An toàn, điều chỉnh liều theo thai kỳ"
    },
    
    # ========== GASTROINTESTINAL ==========
    
    "Omeprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor (PPI)",
        "vietnamese_name": "Omeprazole, Losec",
        "administration": ["PO", "IV"],
        "indications": [
            "Loét dạ dày tá tràng",
            "Trào ngược dạ dày thực quản (GERD)",
            "Hội chứng Zollinger-Ellison",
            "Phòng ngừa loét do stress",
            "Eradication H. pylori (kết hợp với kháng sinh)"
        ],
        "contraindications": [
            "Dị ứng",
            "Dùng cùng atazanavir"
        ],
        "dosage": {
            "adult_po": "20-40mg x 1-2 lần/ngày",
            "adult_iv": "40mg x 1-2 lần/ngày",
            "h_pylori": "20mg x 2 lần/ngày (với amoxicillin + clarithromycin)",
            "notes": "Uống 30 phút trước bữa ăn, không nhai/cắn viên"
        },
        "side_effects": [
            "Nhức đầu",
            "Tiêu chảy",
            "Đau bụng",
            "Tăng nguy cơ nhiễm C. difficile",
            "Gãy xương (dùng lâu dài, liều cao)",
            "Thiếu vitamin B12 (dùng lâu dài)",
            "Thiếu magnesium (dùng lâu dài)"
        ],
        "interactions": [
            "Clopidogrel: giảm hiệu quả clopidogrel",
            "Warfarin: có thể tăng tác dụng",
            "Phenytoin: tăng nồng độ phenytoin",
            "Methotrexate: tăng nồng độ methotrexate"
        ],
        "pregnancy": "C"
    },
    
    "Pantoprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor",
        "vietnamese_name": "Pantoprazole, Pantoloc",
        "administration": ["PO", "IV"],
        "indications": [
            "Loét dạ dày tá tràng",
            "GERD",
            "Phòng ngừa loét do stress"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "40mg x 1-2 lần/ngày",
            "adult_iv": "40mg x 1-2 lần/ngày",
            "notes": "Ít tương tác hơn omeprazole với clopidogrel"
        },
        "side_effects": [
            "Nhức đầu",
            "Tiêu chảy",
            "Tương tự omeprazole"
        ],
        "interactions": [
            "Ít tương tác hơn omeprazole"
        ],
        "pregnancy": "B"
    },
    
    "Ranitidine": {
        "group": "Gastrointestinal - H2 Receptor Antagonist",
        "vietnamese_name": "Ranitidine, Zantac",
        "administration": ["PO", "IV"],
        "indications": [
            "Loét dạ dày tá tràng",
            "GERD",
            "Phòng ngừa loét do stress"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "150mg x 2 lần/ngày hoặc 300mg x 1 lần/ngày",
            "adult_iv": "50mg x 3 lần/ngày hoặc 150mg truyền liên tục/24h",
            "notes": "Yếu hơn PPI, nhưng rẻ hơn. Một số sản phẩm đã bị thu hồi do NDMA"
        },
        "side_effects": [
            "Nhức đầu",
            "Rối loạn tiêu hóa",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng tác dụng (ít hơn cimetidine)"
        ],
        "pregnancy": "B"
    },
    
    "Metoclopramide": {
        "group": "Gastrointestinal - Prokinetic, Antiemetic",
        "vietnamese_name": "Metoclopramide, Primperan",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Buồn nôn, nôn",
            "Liệt dạ dày",
            "Trào ngược dạ dày thực quản",
            "Đau nửa đầu (kết hợp)"
        ],
        "contraindications": [
            "Tắc ruột",
            "Xuất huyết tiêu hóa",
            "Rối loạn vận động (Parkinson, dystonia)",
            "Epilepsy"
        ],
        "dosage": {
            "adult_po": "10mg x 3-4 lần/ngày",
            "adult_iv_im": "10mg IV/IM mỗi 6-8 giờ",
            "adult_max": "60mg/ngày",
            "notes": "Không dùng quá 12 tuần (rối loạn vận động muộn)"
        },
        "side_effects": [
            "Rối loạn vận động (dystonia, parkinsonism)",
            "Buồn ngủ",
            "Hội chứng serotonin (với SSRI)",
            "Rối loạn vận động muộn (dùng lâu dài)"
        ],
        "interactions": [
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin",
            "Antipsychotics: tăng nguy cơ rối loạn vận động"
        ],
        "pregnancy": "B"
    },
    
    "Loperamide": {
        "group": "Gastrointestinal - Antidiarrheal",
        "vietnamese_name": "Loperamide, Imodium",
        "administration": ["PO"],
        "indications": [
            "Tiêu chảy cấp",
            "Tiêu chảy mạn tính"
        ],
        "contraindications": [
            "Tiêu chảy do nhiễm khuẩn (nặng)",
            "Viêm đại tràng giả mạc",
            "Tắc ruột",
            "Trẻ em <2 tuổi"
        ],
        "dosage": {
            "adult_loading": "4mg x 1 lần",
            "adult_maintenance": "2mg sau mỗi lần đi ngoài (tối đa 16mg/ngày)",
            "notes": "Không dùng quá 48 giờ nếu không cải thiện"
        },
        "side_effects": [
            "Táo bón",
            "Buồn nôn",
            "Đau bụng",
            "Buồn ngủ"
        ],
        "interactions": [
            "Opioids: tăng tác dụng (ít dùng chung)"
        ],
        "pregnancy": "C"
    },
    
    # ========== ANALGESICS ==========
    
    "Paracetamol": {
        "group": "Analgesic - Acetaminophen",
        "vietnamese_name": "Paracetamol, Acetaminophen, Panadol",
        "administration": ["PO", "IV", "Rectal"],
        "indications": [
            "Đau nhẹ đến trung bình",
            "Sốt",
            "Đau sau phẫu thuật"
        ],
        "contraindications": [
            "Suy gan nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "500-1000mg mỗi 4-6 giờ (tối đa 4g/ngày)",
            "adult_iv": "1000mg mỗi 4-6 giờ (tối đa 4g/ngày)",
            "adult_rectal": "500mg mỗi 4-6 giờ",
            "notes": "Không vượt quá 4g/ngày để tránh độc tính gan"
        },
        "side_effects": [
            "Hiếm khi có tác dụng phụ (nếu dùng đúng liều)",
            "Độc tính gan (quá liều)",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng nguy cơ chảy máu (liều cao, dùng lâu)",
            "Rượu: tăng nguy cơ độc tính gan"
        ],
        "pregnancy": "B - An toàn trong thai kỳ"
    },
    
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
        "pregnancy": "C - D trong 3 tháng cuối"
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
        "pregnancy": "C"
    },
    
    # ========== RESPIRATORY ==========
    
    "Salbutamol": {
        "group": "Respiratory - Short-acting Beta-2 Agonist (SABA)",
        "vietnamese_name": "Salbutamol, Ventolin",
        "administration": ["Inhalation", "IV", "PO"],
        "indications": [
            "Hen phế quản (cắt cơn)",
            "COPD (cắt cơn)",
            "Co thắt phế quản cấp",
            "Dự phòng co thắt do vận động"
        ],
        "contraindications": [
            "Dị ứng",
            "Nhịp tim nhanh nặng"
        ],
        "dosage": {
            "adult_inhalation": "1-2 puffs (100-200mcg) mỗi 4-6 giờ khi cần",
            "adult_nebulizer": "2.5-5mg mỗi 4-6 giờ",
            "adult_iv": "0.5mg IV, sau đó 5-20mcg/phút truyền liên tục",
            "notes": "Dùng khi cần (PRN) cho cắt cơn, không dùng thường xuyên"
        },
        "side_effects": [
            "Tim đập nhanh",
            "Run cơ",
            "Đau đầu",
            "Hạ kali máu (liều cao)",
            "Loạn nhịp tim (hiếm)"
        ],
        "interactions": [
            "Beta-blocker: đối kháng tác dụng (tránh dùng)"
        ],
        "pregnancy": "C"
    },
    
    # ========== NEUROLOGY/PSYCHIATRY ==========
    
    "Carbamazepine": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Carbamazepine, Tegretol",
        "administration": ["PO"],
        "indications": [
            "Động kinh",
            "Đau dây thần kinh sinh ba",
            "Rối loạn lưỡng cực",
            "Rối loạn nhân cách"
        ],
        "contraindications": [
            "Block nhĩ thất",
            "Bệnh gan nặng",
            "Porphyria",
            "Dùng MAO inhibitor",
            "Giảm bạch cầu/giảm tiểu cầu"
        ],
        "dosage": {
            "adult_epilepsy": "200-400mg x 2-3 lần/ngày, tăng dần đến 800-1600mg/ngày",
            "adult_neuralgia": "100-200mg x 2 lần/ngày, tăng đến 200-400mg x 3-4 lần/ngày",
            "notes": "Theo dõi nồng độ trong máu, công thức máu, chức năng gan"
        },
        "side_effects": [
            "Chóng mặt",
            "Buồn nôn",
            "Giảm bạch cầu",
            "Ban da (nặng có thể SJS/TEN)",
            "Rối loạn chức năng gan",
            "Hạ natri máu"
        ],
        "interactions": [
            "Nhiều thuốc: cảm ứng enzyme CYP450, giảm nồng độ nhiều thuốc",
            "Warfarin: giảm tác dụng warfarin",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "pregnancy": "D"
    },
    
    "Fluoxetine": {
        "group": "Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)",
        "vietnamese_name": "Fluoxetine, Prozac",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu",
            "Rối loạn ám ảnh cưỡng chế (OCD)",
            "Bulimia"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng"
        ],
        "dosage": {
            "adult_depression": "20mg x 1 lần/ngày, tăng đến 20-80mg/ngày",
            "adult_ocd": "20-60mg/ngày",
            "notes": "Tác dụng kéo dài (half-life dài), ngừng 5 tuần trước MAO inhibitor"
        },
        "side_effects": [
            "Buồn nôn",
            "Mất ngủ hoặc buồn ngủ",
            "Giảm ham muốn tình dục",
            "Nhức đầu",
            "Hội chứng serotonin (với thuốc khác)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định (nguy cơ hội chứng serotonin)",
            "Tramadol: tăng nguy cơ co giật và hội chứng serotonin",
            "Warfarin: tăng tác dụng chống đông",
            "Triptans: tăng nguy cơ hội chứng serotonin"
        ],
        "pregnancy": "C"
    },
    
    # ========== ADDITIONAL COMMON DRUGS ==========
    
    "Allopurinol": {
        "group": "Metabolism - Xanthine Oxidase Inhibitor",
        "vietnamese_name": "Allopurinol, Zyloric",
        "administration": ["PO"],
        "indications": [
            "Gout",
            "Tăng acid uric máu",
            "Phòng ngừa sỏi thận uric acid",
            "Hóa trị (phòng ngừa tăng acid uric)"
        ],
        "contraindications": [
            "Dị ứng",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "adult_standard": "100-300mg x 1 lần/ngày",
            "adult_severe": "400-600mg/ngày chia 2-3 lần",
            "notes": "Khởi đầu với liều thấp (100mg), tăng dần. Dùng kèm colchicine khi bắt đầu để tránh cơn gout cấp"
        },
        "side_effects": [
            "Ban da (nặng có thể SJS/TEN - nguy hiểm)",
            "Buồn nôn",
            "Đau đầu",
            "Tăng men gan"
        ],
        "interactions": [
            "Azathioprine/6-mercaptopurine: tăng độc tính (giảm liều azathioprine 75%)",
            "Ampicillin/Amoxicillin: tăng nguy cơ ban da",
            "Warfarin: tăng tác dụng chống đông"
        ],
        "pregnancy": "C"
    },
    
    "Prednisolone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Prednisolone",
        "administration": ["PO"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản",
            "Bệnh tự miễn",
            "Suy thượng thận",
            "Dị ứng nặng"
        ],
        "contraindications": [
            "Nhiễm khuẩn hệ thống không điều trị",
            "Loét dạ dày tá tràng đang hoạt động",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "5-60mg/ngày tùy chỉ định",
            "adult_high": "1-2mg/kg/ngày cho bệnh nặng",
            "notes": "Giảm dần liều khi ngừng, không ngừng đột ngột. Uống buổi sáng với thức ăn"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Ức chế miễn dịch",
            "Tăng cân",
            "Loét dạ dày",
            "Rối loạn tâm thần",
            "Ức chế trục HPA (khi ngừng)"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày",
            "Insulin/OAD: tăng đường huyết",
            "Vaccines: giảm hiệu quả vaccine"
        ],
        "pregnancy": "C"
    },
    
    "Folic Acid": {
        "group": "Hematology - Vitamin",
        "vietnamese_name": "Acid Folic",
        "administration": ["PO"],
        "indications": [
            "Thiếu máu do thiếu folate",
            "Dự phòng dị tật ống thần kinh trong thai kỳ",
            "Bệnh hồng cầu hình liềm",
            "Đang dùng methotrexate"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_deficiency": "1-5mg x 1 lần/ngày",
            "pregnancy": "0.4-0.8mg x 1 lần/ngày",
            "methotrexate": "5-10mg/tuần (24h sau methotrexate)",
            "notes": "Dùng kèm vitamin B12 khi thiếu máu"
        },
        "side_effects": [
            "Hiếm khi có tác dụng phụ",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Methotrexate: giảm hiệu quả methotrexate (nhưng dùng để giảm độc tính)",
            "Phenytoin: giảm nồng độ phenytoin"
        ],
        "pregnancy": "A - Khuyến nghị dùng trong thai kỳ"
    },
}

# Drug groups for filtering
DRUG_GROUPS = {
    "Cardiovascular": [
        "Captopril", "Enalapril", "Lisinopril", "Losartan",
        "Metoprolol", "Propranolol", "Amlodipine",
        "Furosemide", "Hydrochlorothiazide",
        "Amiodarone", "Digoxin",
        "Warfarin", "Aspirin", "Clopidogrel",
        "Atorvastatin", "Simvastatin"
    ],
    "Diabetes": [
        "Metformin", "Glibenclamide", "Gliclazide", "Insulin"
    ],
    "Gastrointestinal": [
        "Omeprazole", "Pantoprazole", "Ranitidine",
        "Metoclopramide", "Loperamide"
    ],
    "Analgesics": [
        "Paracetamol", "Ibuprofen", "Tramadol"
    ],
    "Respiratory": [
        "Salbutamol"
    ],
    "Neurology/Psychiatry": [
        "Carbamazepine", "Fluoxetine"
    ],
    "Other": [
        "Allopurinol", "Prednisolone", "Folic Acid"
    ]
}

# Total count
TOTAL_DRUGS = len(DRUG_DATABASE)

