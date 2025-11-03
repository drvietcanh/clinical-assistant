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
    
    # ========== ANTIPLATELETS (ADDITIONAL) ==========
    
    "Ticagrelor": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Ticagrelor, Brilinta",
        "administration": ["PO"],
        "indications": [
            "Hội chứng mạch vành cấp",
            "Sau đặt stent",
            "Sau nhồi máu cơ tim",
            "Phòng ngừa đột quỵ/TIA"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Xuất huyết nội sọ",
            "Suy gan nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_loading": "180mg x 1 lần",
            "adult_maintenance": "90mg x 2 lần/ngày",
            "notes": "Dùng kèm aspirin 75-100mg/ngày (dual antiplatelet therapy). Dùng với thức ăn để giảm dyspnea"
        },
        "side_effects": [
            "Chảy máu",
            "Khó thở (dyspnea) - phổ biến nhưng thường nhẹ",
            "Chóng mặt",
            "Nhức đầu"
        ],
        "interactions": [
            "Aspirin: dùng kèm (nhưng liều aspirin >100mg/ngày có thể giảm hiệu quả)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Strong CYP3A4 inhibitors: tăng nồng độ (tránh dùng)"
        ],
        "pregnancy": "C"
    },
    
    "Prasugrel": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Prasugrel, Effient",
        "administration": ["PO"],
        "indications": [
            "Hội chứng mạch vành cấp cần PCI",
            "Sau đặt stent"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Tiền sử TIA/đột quỵ",
            "Tuổi ≥75 (trừ nguy cơ cao)",
            "Cân nặng <60kg (trừ nguy cơ cao)"
        ],
        "dosage": {
            "adult_loading": "60mg x 1 lần",
            "adult_maintenance": "10mg x 1 lần/ngày (5mg nếu <60kg hoặc ≥75 tuổi)",
            "notes": "Mạnh hơn clopidogrel, nguy cơ chảy máu cao hơn"
        },
        "side_effects": [
            "Chảy máu (nhiều hơn clopidogrel)",
            "Chảy máu lớn (hiếm nhưng nguy hiểm)",
            "Thrombotic thrombocytopenic purpura (TTP) - hiếm"
        ],
        "interactions": [
            "Aspirin: dùng kèm (dual antiplatelet therapy)",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B"
    },
    
    "Ticlopidine": {
        "group": "Cardiovascular - Antiplatelet",
        "vietnamese_name": "Ticlopidine, Ticlid",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ sau TIA",
            "Phòng ngừa huyết khối sau stent (ít dùng, thay bằng clopidogrel)"
        ],
        "contraindications": [
            "Giảm bạch cầu/giảm tiểu cầu",
            "Chảy máu đang hoạt động",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "250mg x 2 lần/ngày",
            "notes": "Ít dùng do nguy cơ giảm bạch cầu/tiểu cầu. Clopidogrel thay thế tốt hơn"
        },
        "side_effects": [
            "Giảm bạch cầu (nguy hiểm - cần theo dõi)",
            "Giảm tiểu cầu",
            "Ban xuất huyết giảm tiểu cầu huyết khối (TTP)",
            "Chảy máu",
            "Rối loạn tiêu hóa"
        ],
        "interactions": [
            "Aspirin: tăng nguy cơ chảy máu",
            "Warfarin: tăng nguy cơ chảy máu",
            "Antacids: giảm hấp thu"
        ],
        "pregnancy": "B"
    },
    
    "Dipyridamole": {
        "group": "Cardiovascular - Antiplatelet",
        "vietnamese_name": "Dipyridamole, Persantine",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ/TIA (kết hợp với aspirin)",
            "Phòng ngừa huyết khối sau phẫu thuật van tim"
        ],
        "contraindications": [
            "Nhồi máu cơ tim cấp",
            "Co thắt mạch vành (vasospasm)"
        ],
        "dosage": {
            "adult_standard": "200mg x 2 lần/ngày (với aspirin)",
            "adult_modified_release": "200mg x 2 lần/ngày",
            "notes": "Thường dùng kết hợp với aspirin 25mg x 2 lần/ngày"
        },
        "side_effects": [
            "Nhức đầu (phổ biến)",
            "Chóng mặt",
            "Đau bụng",
            "Chảy máu",
            "Tim đập nhanh"
        ],
        "interactions": [
            "Aspirin: dùng kèm để tăng hiệu quả",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B"
    },
    
    # ========== ANTIDEPRESSANTS (ADDITIONAL) ==========
    
    "Sertraline": {
        "group": "Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)",
        "vietnamese_name": "Sertraline, Zoloft",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu",
            "Rối loạn ám ảnh cưỡng chế (OCD)",
            "Rối loạn stress sau sang chấn (PTSD)",
            "Rối loạn hoảng sợ"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng"
        ],
        "dosage": {
            "adult_depression": "50mg x 1 lần/ngày, tăng đến 50-200mg/ngày",
            "adult_ocd": "50-200mg/ngày",
            "adult_max": "200mg/ngày",
            "notes": "Khởi đầu 25-50mg/ngày, tăng dần. Uống buổi sáng hoặc tối"
        },
        "side_effects": [
            "Buồn nôn",
            "Tiêu chảy",
            "Mất ngủ",
            "Giảm ham muốn tình dục",
            "Nhức đầu",
            "Khô miệng",
            "Hội chứng serotonin (với thuốc khác)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng chống đông",
            "Tramadol: tăng nguy cơ co giật",
            "Triptans: tăng nguy cơ hội chứng serotonin"
        ],
        "pregnancy": "C"
    },
    
    "Citalopram": {
        "group": "Psychiatry - SSRI",
        "vietnamese_name": "Citalopram, Celexa",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "QT prolongation",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "20mg x 1 lần/ngày, tăng đến 20-40mg/ngày",
            "adult_max": "40mg/ngày (20mg nếu >60 tuổi)",
            "notes": "Giới hạn 40mg/ngày do nguy cơ QT prolongation. Người già: max 20mg/ngày"
        },
        "side_effects": [
            "Buồn nôn",
            "Mất ngủ",
            "Nhức đầu",
            "QT prolongation (liều cao)",
            "Giảm ham muốn tình dục"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "Warfarin: có thể tăng tác dụng"
        ],
        "pregnancy": "C"
    },
    
    "Escitalopram": {
        "group": "Psychiatry - SSRI",
        "vietnamese_name": "Escitalopram, Lexapro",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu tổng quát (GAD)",
            "Rối loạn hoảng sợ"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "10mg x 1 lần/ngày, tăng đến 10-20mg/ngày",
            "adult_max": "20mg/ngày",
            "notes": "Là S-enantiomer của citalopram, ít tác dụng phụ hơn"
        },
        "side_effects": [
            "Buồn nôn",
            "Mất ngủ",
            "Nhức đầu",
            "Giảm ham muốn tình dục",
            "Ít tác dụng phụ hơn citalopram"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng",
            "Tramadol: tăng nguy cơ co giật"
        ],
        "pregnancy": "C"
    },
    
    "Venlafaxine": {
        "group": "Psychiatry - SNRI (Serotonin-Norepinephrine Reuptake Inhibitor)",
        "vietnamese_name": "Venlafaxine, Effexor",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu tổng quát (GAD)",
            "Rối loạn hoảng sợ",
            "Rối loạn lo âu xã hội"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Tăng huyết áp không kiểm soát",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "37.5-75mg x 2 lần/ngày (immediate) hoặc 75-150mg x 1 lần/ngày (extended release)",
            "adult_max": "225mg/ngày (immediate) hoặc 225mg/ngày (extended release)",
            "notes": "Extended release: uống 1 lần/ngày, thuận tiện hơn"
        },
        "side_effects": [
            "Buồn nôn",
            "Tăng huyết áp (liều cao)",
            "Mất ngủ",
            "Chóng mặt",
            "Giảm ham muốn tình dục",
            "Tăng nhịp tim",
            "Khó chịu khi ngừng (withdrawal)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng",
            "Tramadol: tăng nguy cơ co giật và hội chứng serotonin"
        ],
        "pregnancy": "C"
    },
    
    "Amitriptyline": {
        "group": "Psychiatry - Tricyclic Antidepressant (TCA)",
        "vietnamese_name": "Amitriptyline, Elavil",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Đau thần kinh (neuropathic pain)",
            "Migraine phòng ngừa",
            "Rối loạn giấc ngủ",
            "Đau cơ xơ hóa"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Nhồi máu cơ tim gần đây",
            "Block nhĩ thất độ 2-3",
            "Rối loạn nhịp tim",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_depression": "25-75mg x 1 lần/ngày buổi tối, tăng đến 50-150mg/ngày",
            "adult_neuropathic": "10-25mg buổi tối, tăng đến 25-100mg/ngày",
            "adult_max": "150-300mg/ngày",
            "notes": "Dùng buổi tối để tránh buồn ngủ ban ngày. Nguy cơ quá liều cao"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Khô miệng",
            "Táo bón",
            "Rối loạn nhịp tim",
            "Hạ huyết áp tư thế",
            "Nhìn mờ",
            "Tăng cân",
            "Nguy cơ quá liều (cardiotoxic)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định (nguy hiểm)",
            "Quinidine: tăng nồng độ amitriptyline",
            "Cimetidine: tăng nồng độ",
            "Alcohol: tăng tác dụng an thần",
            "Sympathomimetics: tăng nguy cơ tăng huyết áp"
        ],
        "pregnancy": "C - D trong 3 tháng đầu"
    },
    
    # ========== ANTICONVULSANTS ==========
    
    "Phenytoin": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Phenytoin, Dilantin",
        "administration": ["PO", "IV"],
        "indications": [
            "Động kinh (tổng quát, cục bộ)",
            "Status epilepticus",
            "Đau dây thần kinh sinh ba",
            "Rối loạn nhịp tim (hiếm)"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy gan nặng",
            "Block nhĩ thất",
            "Hội chứng bệnh lympho"
        ],
        "dosage": {
            "adult_po": "100mg x 3 lần/ngày, tăng đến 200-400mg/ngày",
            "adult_iv_loading": "15-20mg/kg IV (tối đa 1.5g)",
            "adult_iv_maintenance": "100mg IV mỗi 6-8 giờ sau loading",
            "status_epilepticus": "15-20mg/kg IV x 1 lần",
            "notes": "Theo dõi nồng độ trong máu (mục tiêu 10-20 mcg/mL). Non-linear kinetics"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Nystagmus (liều cao)",
            "Ataxia (liều cao)",
            "Ban da (có thể nặng - SJS/TEN)",
            "Hạ bạch cầu",
            "Tăng men gan",
            "Loãng xương (dùng lâu dài)",
            "Tăng acid uric",
            "Rối loạn chức năng nhận thức"
        ],
        "interactions": [
            "Warfarin: giảm tác dụng warfarin (cảm ứng enzyme)",
            "Oral contraceptives: giảm hiệu quả",
            "Folic acid: giảm nồng độ phenytoin",
            "Many drugs: cảm ứng CYP450, giảm nồng độ nhiều thuốc"
        ],
        "pregnancy": "D - Nguy cơ dị tật thai nhi"
    },
    
    "Valproate": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Valproate, Valproic Acid, Depakote",
        "administration": ["PO", "IV"],
        "indications": [
            "Động kinh (nhiều loại)",
            "Rối loạn lưỡng cực",
            "Migraine phòng ngừa",
            "Status epilepticus"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Rối loạn chuyển hóa chu trình urea",
            "Suy gan nặng",
            "Có thai (cho rối loạn lưỡng cực)"
        ],
        "dosage": {
            "adult_po": "250-500mg x 2-3 lần/ngày, tăng đến 1000-3000mg/ngày",
            "adult_iv": "15-20mg/kg IV x 1 lần, sau đó 5-10mg/kg mỗi 6 giờ",
            "adult_max": "60mg/kg/ngày (không quá 3000mg/ngày)",
            "notes": "Theo dõi nồng độ (mục tiêu 50-100 mcg/mL), chức năng gan, tiểu cầu"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tăng cân",
            "Rụng tóc",
            "Tăng men gan",
            "Viêm tụy (hiếm nhưng nguy hiểm)",
            "Thiếu tiểu cầu",
            "Dị tật thai nhi (neural tube defects)",
            "Loãng xương (dùng lâu dài)",
            "Tăng ammonia máu"
        ],
        "interactions": [
            "Phenytoin/Carbamazepine: giảm nồng độ valproate",
            "Lamotrigine: tăng nồng độ lamotrigine",
            "Aspirin: tăng nồng độ valproate",
            "Warfarin: có thể tăng tác dụng"
        ],
        "pregnancy": "D - Nguy cơ dị tật thai nhi cao (neural tube defects)"
    },
    
    "Levetiracetam": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Levetiracetam, Keppra",
        "administration": ["PO", "IV"],
        "indications": [
            "Động kinh cục bộ",
            "Động kinh tổng quát",
            "Status epilepticus (IV)"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "500-1000mg x 2 lần/ngày, tăng đến 1000-3000mg/ngày",
            "adult_iv": "500-1000mg IV mỗi 12 giờ",
            "adult_max": "3000mg/ngày",
            "notes": "Ít tương tác thuốc, an toàn cho trẻ em và người già"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "50_80": "Giảm liều 25%",
            "30_50": "Giảm liều 50%",
            "under_30": "Giảm liều 75%"
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Kích động, hành vi bất thường",
            "Nhức đầu",
            "Mệt mỏi",
            "Ít tác dụng phụ hơn các anticonvulsants khác"
        ],
        "interactions": [
            "Ít tương tác - không cảm ứng hoặc ức chế CYP450"
        ],
        "pregnancy": "C"
    },
    
    "Lamotrigine": {
        "group": "Neurology - Anticonvulsant",
        "vietnamese_name": "Lamotrigine, Lamictal",
        "administration": ["PO"],
        "indications": [
            "Động kinh cục bộ",
            "Động kinh tổng quát",
            "Rối loạn lưỡng cực (phòng ngừa tái phát trầm cảm)"
        ],
        "contraindications": [
            "Dị ứng",
            "Ban da nặng trước đây (SJS/TEN)"
        ],
        "dosage": {
            "adult_epilepsy": "25mg x 2 lần/ngày x 2 tuần, tăng đến 100-200mg x 2 lần/ngày",
            "adult_bipolar": "25mg/ngày, tăng chậm đến 100-200mg/ngày",
            "adult_max": "400mg/ngày",
            "notes": "Tăng liều rất chậm để tránh ban da. Nếu dùng với valproate: giảm liều 50%"
        },
        "side_effects": [
            "Ban da (có thể nặng - SJS/TEN, đặc biệt khi tăng liều nhanh)",
            "Nhức đầu",
            "Chóng mặt",
            "Buồn nôn",
            "Mất ngủ",
            "Rối loạn thị giác"
        ],
        "interactions": [
            "Valproate: tăng nồng độ lamotrigine (giảm liều lamotrigine 50%)",
            "Carbamazepine: giảm nồng độ lamotrigine",
            "Oral contraceptives: giảm nồng độ lamotrigine (tăng liều)"
        ],
        "pregnancy": "C"
    },
    
    "Gabapentin": {
        "group": "Neurology - Anticonvulsant (Alpha-2-delta ligand)",
        "vietnamese_name": "Gabapentin, Neurontin",
        "administration": ["PO"],
        "indications": [
            "Động kinh cục bộ",
            "Đau thần kinh (postherpetic neuralgia, diabetic neuropathy)",
            "Rối loạn lo âu",
            "Hội chứng chân không yên"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_epilepsy": "300mg x 3 lần/ngày, tăng đến 900-1800mg/ngày",
            "adult_neuropathic": "300mg x 3 lần/ngày, tăng đến 1800-3600mg/ngày",
            "adult_max": "3600mg/ngày (chia 3 lần)",
            "notes": "Hấp thu giảm khi tăng liều. Uống cách xa antacids 2 giờ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "300mg x 2 lần/ngày",
            "15_30": "300mg x 1 lần/ngày",
            "under_15": "300mg cách ngày"
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Mệt mỏi",
            "Phù ngoại biên",
            "Tăng cân",
            "Nhìn mờ",
            "Suy giảm trí nhớ"
        ],
        "interactions": [
            "Antacids: giảm hấp thu (cách xa 2 giờ)",
            "Morphine: tăng tác dụng an thần",
            "Ít tương tác khác"
        ],
        "pregnancy": "C"
    },
    
    "Pregabalin": {
        "group": "Neurology - Anticonvulsant (Alpha-2-delta ligand)",
        "vietnamese_name": "Pregabalin, Lyrica",
        "administration": ["PO"],
        "indications": [
            "Đau thần kinh (postherpetic neuralgia, diabetic neuropathy)",
            "Đau cơ xơ hóa",
            "Động kinh cục bộ",
            "Rối loạn lo âu tổng quát"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_neuropathic": "75mg x 2 lần/ngày, tăng đến 150-300mg x 2 lần/ngày",
            "adult_epilepsy": "75mg x 2 lần/ngày, tăng đến 150-600mg/ngày",
            "adult_max": "600mg/ngày",
            "notes": "Mạnh hơn gabapentin, hấp thu tốt hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "Giảm liều 75%",
            "under_15": "Giảm liều 90%"
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Phù ngoại biên",
            "Tăng cân",
            "Nhìn mờ",
            "Suy giảm trí nhớ",
            "Nguy cơ lạm dụng (controlled substance)"
        ],
        "interactions": [
            "Morphine: tăng tác dụng an thần",
            "Alcohol: tăng tác dụng an thần",
            "Ít tương tác khác"
        ],
        "pregnancy": "C"
    },
    
    # ========== ANTIHISTAMINES ==========
    
    "Loratadine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Loratadine, Clarityne",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng thức ăn",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "10mg x 1 lần/ngày",
            "adult_max": "10mg x 2 lần/ngày",
            "pediatric": "5mg x 1 lần/ngày (2-12 tuổi)",
            "notes": "Non-sedating, ít tác dụng phụ"
        },
        "side_effects": [
            "Buồn ngủ (ít hơn 1st generation)",
            "Khô miệng (hiếm)",
            "Nhức đầu (hiếm)",
            "Ít tác dụng phụ hơn antihistamine 1st generation"
        ],
        "interactions": [
            "Ít tương tác",
            "Erythromycin/Ketoconazole: tăng nồng độ (nhưng thường không cần điều chỉnh)"
        ],
        "pregnancy": "B"
    },
    
    "Cetirizine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Cetirizine, Zyrtec",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng mắt",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_standard": "10mg x 1 lần/ngày",
            "adult_max": "10mg x 2 lần/ngày",
            "pediatric": "5mg x 1 lần/ngày (2-6 tuổi), 10mg/ngày (6-12 tuổi)",
            "notes": "Non-sedating, an toàn cho trẻ em"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "5mg x 1 lần/ngày",
            "under_30": "5mg cách ngày"
        },
        "side_effects": [
            "Buồn ngủ (ít, 10-15% người)",
            "Khô miệng",
            "Nhức đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Ít tương tác",
            "Alcohol: có thể tăng buồn ngủ"
        ],
        "pregnancy": "B"
    },
    
    "Fexofenadine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Fexofenadine, Allegra",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "180mg x 1 lần/ngày hoặc 60mg x 2 lần/ngày",
            "adult_max": "180mg x 2 lần/ngày",
            "pediatric": "30mg x 2 lần/ngày (6-11 tuổi)",
            "notes": "Non-sedating, ít buồn ngủ nhất"
        },
        "side_effects": [
            "Rất ít tác dụng phụ",
            "Buồn ngủ rất hiếm",
            "Nhức đầu (hiếm)",
            "Mệt mỏi (hiếm)"
        ],
        "interactions": [
            "Fruit juices (apple, orange, grapefruit): giảm hấp thu (cách xa 1-2 giờ)",
            "Antacids: giảm hấp thu (cách xa 2 giờ)"
        ],
        "pregnancy": "C"
    },
    
    "Desloratadine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Desloratadine, Aerius",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "5mg x 1 lần/ngày",
            "adult_max": "5mg x 2 lần/ngày",
            "pediatric": "2.5mg x 1 lần/ngày (6-11 tuổi)",
            "notes": "Là metabolite của loratadine, mạnh hơn và tác dụng dài hơn"
        },
        "side_effects": [
            "Buồn ngủ (rất hiếm)",
            "Khô miệng",
            "Nhức đầu",
            "Ít tác dụng phụ"
        ],
        "interactions": [
            "Ít tương tác"
        ],
        "pregnancy": "C"
    },
    
    "Levocetirizine": {
        "group": "Allergy - Antihistamine (H1 Antagonist, 2nd generation)",
        "vietnamese_name": "Levocetirizine, Xyzal",
        "administration": ["PO"],
        "indications": [
            "Dị ứng (allergic rhinitis)",
            "Mề đay (urticaria)",
            "Dị ứng da"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_standard": "5mg x 1 lần/ngày buổi tối",
            "adult_max": "5mg x 2 lần/ngày",
            "pediatric": "2.5mg x 1 lần/ngày (6-12 tuổi)",
            "notes": "Là R-enantiomer của cetirizine, mạnh hơn cetirizine"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "5mg cách ngày",
            "under_30": "5mg mỗi 3 ngày"
        },
        "side_effects": [
            "Buồn ngủ (ít hơn cetirizine)",
            "Nhức đầu",
            "Mệt mỏi",
            "Khô miệng"
        ],
        "interactions": [
            "Ít tương tác",
            "Alcohol: có thể tăng buồn ngủ"
        ],
        "pregnancy": "B"
    },
    
    # ========== CORTICOSTEROIDS (ADDITIONAL) ==========
    
    "Dexamethasone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Dexamethasone, Decadron",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản",
            "Phù não",
            "Nôn do hóa trị",
            "Chấn thương tủy sống",
            "Viêm màng não do vi khuẩn (kết hợp kháng sinh)",
            "COVID-19 (nặng)"
        ],
        "contraindications": [
            "Nhiễm nấm hệ thống không điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_antiinflammatory": "0.75-9mg/ngày chia 2-4 lần",
            "adult_edema": "10mg IV x 1 lần, sau đó 4mg IV mỗi 6 giờ",
            "adult_chemotherapy_nausea": "8-20mg x 1 lần trước hóa trị",
            "adult_covid19": "6mg x 1 lần/ngày (IV hoặc PO) x 10 ngày",
            "notes": "Tác dụng dài, ức chế mạnh. Không dùng cho nhiễm nấm không điều trị"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Ức chế miễn dịch",
            "Tăng cân",
            "Loét dạ dày",
            "Rối loạn tâm thần",
            "Phù",
            "Khó ngủ"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày",
            "Insulin/OAD: tăng đường huyết",
            "Vaccines: giảm hiệu quả vaccine"
        ],
        "pregnancy": "C"
    },
    
    "Methylprednisolone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Methylprednisolone, Medrol",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản",
            "Bệnh tự miễn",
            "Sốc phản vệ (kết hợp)",
            "Chấn thương tủy sống",
            "Đợt cấp bệnh đa xơ cứng"
        ],
        "contraindications": [
            "Nhiễm nấm hệ thống không điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "4-48mg/ngày chia 1-4 lần",
            "adult_iv_pulse": "250-1000mg IV x 1 lần/ngày x 3-5 ngày",
            "adult_iv_standard": "40-125mg IV mỗi 6-12 giờ",
            "spinal_cord_injury": "30mg/kg IV x 1 lần, sau đó 5.4mg/kg/giờ x 23 giờ",
            "notes": "IV pulse therapy cho bệnh nặng. Giảm dần liều khi ngừng"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Ức chế miễn dịch",
            "Tăng cân",
            "Loét dạ dày",
            "Rối loạn tâm thần"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày",
            "Ketoconazole: tăng nồng độ methylprednisolone"
        ],
        "pregnancy": "C"
    },
    
    "Hydrocortisone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Hydrocortisone, Cortef",
        "administration": ["PO", "IV", "IM", "Topical"],
        "indications": [
            "Suy thượng thận",
            "Phản ứng dị ứng nặng",
            "Sốc phản vệ (kết hợp)",
            "Viêm khớp",
            "Bệnh Addison",
            "Phù não"
        ],
        "contraindications": [
            "Nhiễm nấm hệ thống không điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_replacement": "15-25mg/ngày (20mg buổi sáng, 10mg buổi tối)",
            "adult_stress": "50-100mg IV mỗi 6-8 giờ",
            "adult_shock": "100mg IV x 1 lần, sau đó 50-100mg mỗi 6 giờ",
            "adult_antiinflammatory": "20-240mg/ngày",
            "notes": "Glucocorticoid tự nhiên, tác dụng ngắn"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Giữ natri, phù",
            "Loét dạ dày",
            "Ức chế miễn dịch"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày"
        ],
        "pregnancy": "C"
    },
    
    "Betamethasone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Betamethasone, Celestone",
        "administration": ["PO", "IV", "IM", "Topical"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản",
            "Bệnh tự miễn",
            "Viêm da",
            "Thúc đẩy trưởng thành phổi thai nhi (IM)"
        ],
        "contraindications": [
            "Nhiễm nấm hệ thống không điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "0.6-7.2mg/ngày chia 1-4 lần",
            "adult_im": "0.5-9mg IM",
            "fetal_lung_maturation": "12mg IM x 2 lần cách 24 giờ (cho mẹ)",
            "notes": "Tác dụng dài, ức chế mạnh"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Ức chế miễn dịch",
            "Tăng cân",
            "Loét dạ dày"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày"
        ],
        "pregnancy": "C"
    },
    
    # ========== ANTIVIRALS ==========
    
    "Acyclovir": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Acyclovir, Zovirax",
        "administration": ["PO", "IV", "Topical"],
        "indications": [
            "Herpes simplex (HSV)",
            "Herpes zoster (shingles)",
            "Viêm não do HSV",
            "Nhiễm HSV ở người suy giảm miễn dịch"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng (IV)"
        ],
        "dosage": {
            "adult_herpes_simplex": "200mg x 5 lần/ngày x 7-10 ngày",
            "adult_shingles": "800mg x 5 lần/ngày x 7-10 ngày",
            "adult_iv": "5-10mg/kg IV mỗi 8 giờ",
            "adult_encephalitis": "10mg/kg IV mỗi 8 giờ x 14-21 ngày",
            "notes": "Uống nhiều nước. Truyền IV chậm (1 giờ) để tránh độc thận"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 75%"
        },
        "side_effects": [
            "Buồn nôn",
            "Đau đầu",
            "Độc thận (IV, liều cao)",
            "Rối loạn thần kinh (IV)",
            "Viêm tĩnh mạch (IV)",
            "Ban da"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ acyclovir",
            "Nephrotoxic drugs: tăng nguy cơ độc thận"
        ],
        "pregnancy": "B"
    },
    
    "Valacyclovir": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Valacyclovir, Valtrex",
        "administration": ["PO"],
        "indications": [
            "Herpes simplex (HSV)",
            "Herpes zoster (shingles)",
            "Phòng ngừa tái phát HSV",
            "Phòng ngừa CMV sau ghép tạng"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_herpes_simplex": "500mg x 2 lần/ngày x 7-10 ngày",
            "adult_shingles": "1g x 3 lần/ngày x 7 ngày",
            "adult_prophylaxis": "500mg-1g x 1 lần/ngày",
            "adult_max": "3g/ngày",
            "notes": "Prodrug của acyclovir, hấp thu tốt hơn, uống ít lần hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 75%"
        },
        "side_effects": [
            "Buồn nôn",
            "Đau đầu",
            "Độc thận (liều cao)",
            "Ít tác dụng phụ hơn acyclovir"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Cimetidine: tăng nồng độ"
        ],
        "pregnancy": "B"
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
        "pregnancy": "C"
    },
    
    "Ganciclovir": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Ganciclovir, Cytovene",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm CMV ở người suy giảm miễn dịch",
            "Phòng ngừa CMV sau ghép tạng",
            "Viêm võng mạc do CMV",
            "CMV bẩm sinh"
        ],
        "contraindications": [
            "Dị ứng",
            "Suy thận nặng",
            "Có thai",
            "Giảm bạch cầu <500",
            "Giảm tiểu cầu <25,000"
        ],
        "dosage": {
            "adult_iv_induction": "5mg/kg IV mỗi 12 giờ x 14-21 ngày",
            "adult_iv_maintenance": "5mg/kg IV x 1 lần/ngày hoặc 6mg/kg x 5 lần/tuần",
            "adult_po": "1g x 3 lần/ngày (sau IV induction)",
            "notes": "Theo dõi bạch cầu, tiểu cầu, chức năng thận. Rất độc với tủy xương"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "50_80": "Giảm liều 50%",
            "25_50": "Giảm liều 75%",
            "under_25": "Giảm liều 90%"
        },
        "side_effects": [
            "Giảm bạch cầu (phổ biến, nặng)",
            "Giảm tiểu cầu",
            "Giảm hồng cầu",
            "Độc thận",
            "Độc thần kinh",
            "Sốt",
            "Ban da",
            "Rất độc - chỉ dùng khi cần thiết"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ ganciclovir",
            "Zidovudine: tăng độc tính tủy xương",
            "Mycophenolate: tăng nồng độ ganciclovir"
        ],
        "pregnancy": "C - D (với CMV)"
    },
    
    "Ribavirin": {
        "group": "Infectious Disease - Antiviral",
        "vietnamese_name": "Ribavirin, Rebetol",
        "administration": ["PO", "IV", "Inhalation"],
        "indications": [
            "Viêm gan C (kết hợp với interferon)",
            "Viêm gan C (kết hợp với sofosbuvir)",
            "Sốt Lassa (IV)",
            "RSV ở trẻ sơ sinh (inhalation)"
        ],
        "contraindications": [
            "Có thai (nam và nữ)",
            "Suy thận nặng",
            "Bệnh tim nặng",
            "Thiếu máu nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_hcv": "800-1200mg/ngày chia 2 lần (tùy genotype và trọng lượng)",
            "adult_hcv_sofosbuvir": "1000mg/ngày (nếu >75kg) hoặc 800mg/ngày (<75kg)",
            "adult_iv": "30-35mg/kg x 1 lần (loading), sau đó 15-20mg/kg mỗi 6 giờ",
            "notes": "Rất độc. Nam và nữ phải dùng biện pháp tránh thai 6 tháng sau khi ngừng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Không dùng"
        },
        "side_effects": [
            "Thiếu máu (phổ biến, có thể nặng)",
            "Giảm bạch cầu",
            "Dị tật thai nhi (nam và nữ - chống chỉ định tuyệt đối nếu có thai)",
            "Rối loạn tâm thần",
            "Rối loạn hô hấp (inhalation)",
            "Rất độc"
        ],
        "interactions": [
            "Zidovudine: tăng độc tính",
            "Didanosine: tăng độc tính",
            "Azathioprine: tăng độc tính"
        ],
        "pregnancy": "X - Chống chỉ định tuyệt đối"
    },
}

# Drug groups for filtering
DRUG_GROUPS = {
    "Cardiovascular": [
        "Captopril", "Enalapril", "Lisinopril", "Losartan",
        "Metoprolol", "Propranolol", "Amlodipine",
        "Furosemide", "Hydrochlorothiazide",
        "Amiodarone", "Digoxin",
        "Warfarin", "Aspirin", "Clopidogrel", "Ticagrelor", "Prasugrel", "Ticlopidine", "Dipyridamole",
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
        "Carbamazepine", "Fluoxetine", "Sertraline", "Citalopram", "Escitalopram", "Venlafaxine", "Amitriptyline",
        "Phenytoin", "Valproate", "Levetiracetam", "Lamotrigine", "Gabapentin", "Pregabalin"
    ],
    "Allergy": [
        "Loratadine", "Cetirizine", "Fexofenadine", "Desloratadine", "Levocetirizine"
    ],
    "Other": [
        "Allopurinol", "Prednisolone", "Folic Acid"
    ]
}

# Total count
TOTAL_DRUGS = len(DRUG_DATABASE)

