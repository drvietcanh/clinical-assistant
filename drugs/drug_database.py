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
        "pregnancy": "C"
    },
    
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
        "pregnancy": "C"
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
        "pregnancy": "C"
    },
    
    "Isosorbide mononitrate": {
        "group": "Cardiovascular - Nitrate",
        "vietnamese_name": "Isosorbide mononitrate, Imdur",
        "administration": ["PO"],
        "indications": [
            "Đau thắt ngực (phòng ngừa)",
            "Suy tim (giảm tiền gánh)",
            "Đau thắt ngực ổn định"
        ],
        "contraindications": [
            "Dị ứng nitrate",
            "Hạ huyết áp nặng",
            "Shock",
            "Dùng sildenafil/tadalafil/vardenafil (trong 24-48h)",
            "Tăng áp lực nội sọ",
            "Thiếu máu nặng"
        ],
        "dosage": {
            "adult_angina_immediate": "10-20mg x 2-3 lần/ngày",
            "adult_angina_extended": "30-120mg x 1 lần/ngày (buổi sáng)",
            "adult_heart_failure": "10-40mg x 2-3 lần/ngày",
            "notes": "Tolerance với nitrate nếu dùng liên tục. Cần khoảng nghỉ nitrate-free 10-14h mỗi ngày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nhức đầu (thường gặp, giảm sau vài ngày)",
            "Hạ huyết áp",
            "Chóng mặt",
            "Đỏ mặt",
            "Nhịp tim nhanh phản ứng",
            "Ngất (hiếm)"
        ],
        "interactions": [
            "Sildenafil/Tadalafil/Vardenafil: hạ huyết áp nguy hiểm - chống chỉ định",
            "Rượu: tăng tác dụng hạ huyết áp",
            "Thuốc hạ huyết áp khác: tăng tác dụng"
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
    
    "Empagliflozin": {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Empagliflozin, Jardiance",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Suy tim với phân suất tống máu giảm (HFrEF)",
            "Bệnh thận mạn tính (CKD) ở bệnh nhân đái tháo đường",
            "Giảm nguy cơ tim mạch"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton do đái tháo đường",
            "Suy thận nặng (eGFR <20)",
            "Đang lọc máu",
            "Nhiễm trùng đường tiết niệu tái phát"
        ],
        "dosage": {
            "adult_type2_dm": "10-25mg x 1 lần/ngày",
            "adult_heart_failure": "10mg x 1 lần/ngày",
            "adult_ckd": "10mg x 1 lần/ngày (eGFR ≥20)",
            "notes": "Uống bất kỳ lúc nào, không cần ăn. Giảm đường huyết nhẹ"
        },
        "renal_adjustment": {
            "normal": "10-25mg/ngày",
            "30_60": "10mg/ngày (eGFR ≥30)",
            "under_30": "Không dùng nếu eGFR <20"
        },
        "side_effects": [
            "Nhiễm trùng đường tiết niệu",
            "Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu)",
            "Mất nước, hạ huyết áp",
            "Nhiễm toan ceton (hiếm)",
            "Gãy xương tăng nhẹ",
            "Hoại thư Fournier (hiếm nhưng nguy hiểm)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết",
            "Diuretics: tăng nguy cơ mất nước",
            "Digoxin: tăng nhẹ nồng độ digoxin"
        ],
        "pregnancy": "C"
    },
    
    "Dapagliflozin": {
        "group": "Diabetes - SGLT2 Inhibitor",
        "vietnamese_name": "Dapagliflozin, Forxiga",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2",
            "Suy tim với phân suất tống máu giảm (HFrEF)",
            "Bệnh thận mạn tính (CKD) ở bệnh nhân đái tháo đường"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Suy thận nặng (eGFR <25)",
            "Đang lọc máu",
            "Nhiễm trùng đường tiết niệu tái phát"
        ],
        "dosage": {
            "adult_type2_dm": "5-10mg x 1 lần/ngày",
            "adult_heart_failure": "10mg x 1 lần/ngày",
            "adult_ckd": "10mg x 1 lần/ngày (eGFR ≥25)",
            "notes": "Uống bất kỳ lúc nào"
        },
        "renal_adjustment": {
            "normal": "5-10mg/ngày",
            "30_60": "10mg/ngày (eGFR ≥25)",
            "under_30": "Không dùng nếu eGFR <25"
        },
        "side_effects": [
            "Nhiễm trùng đường tiết niệu",
            "Nhiễm trùng đường sinh dục",
            "Mất nước",
            "Nhiễm toan ceton (hiếm)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết",
            "Diuretics: mất nước"
        ],
        "pregnancy": "C"
    },
    
    "Sitagliptin": {
        "group": "Diabetes - DPP-4 Inhibitor",
        "vietnamese_name": "Sitagliptin, Januvia",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Dị ứng sitagliptin",
            "Suy thận nặng (CrCl <30)"
        ],
        "dosage": {
            "adult_normal_renal": "100mg x 1 lần/ngày",
            "adult_moderate_renal": "50mg x 1 lần/ngày (CrCl 30-50)",
            "adult_severe_renal": "25mg x 1 lần/ngày (CrCl <30)",
            "notes": "Uống bất kỳ lúc nào. Ít gây hạ đường huyết"
        },
        "renal_adjustment": {
            "normal": "100mg/ngày",
            "30_60": "50mg/ngày (CrCl 30-50)",
            "under_30": "25mg/ngày (CrCl <30)"
        },
        "side_effects": [
            "Nhức đầu",
            "Nhiễm trùng đường hô hấp trên",
            "Viêm tụy cấp (hiếm nhưng nguy hiểm)",
            "Đau khớp nghiêm trọng (hiếm)",
            "Suy tim (tăng nhẹ nguy cơ)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết",
            "Digoxin: tăng nhẹ nồng độ digoxin"
        ],
        "pregnancy": "B"
    },
    
    "Vildagliptin": {
        "group": "Diabetes - DPP-4 Inhibitor",
        "vietnamese_name": "Vildagliptin, Galvus",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Nhiễm toan ceton",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "50mg x 2 lần/ngày (sáng và tối)",
            "adult_metformin_combination": "50mg x 2 lần/ngày",
            "notes": "Uống với bữa ăn. Ít gây hạ đường huyết"
        },
        "renal_adjustment": {
            "normal": "50mg x 2 lần/ngày",
            "30_60": "50mg x 2 lần/ngày",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Nhức đầu",
            "Chóng mặt",
            "Nhiễm trùng đường hô hấp",
            "Viêm tụy cấp (hiếm)",
            "Đau khớp (hiếm)"
        ],
        "interactions": [
            "Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết"
        ],
        "pregnancy": "C"
    },
    
    "Pioglitazone": {
        "group": "Diabetes - Thiazolidinedione (TZD)",
        "vietnamese_name": "Pioglitazone, Actos",
        "administration": ["PO"],
        "indications": [
            "Đái tháo đường type 2"
        ],
        "contraindications": [
            "Đái tháo đường type 1",
            "Suy tim (NYHA class III-IV)",
            "Bệnh gan nặng",
            "Ung thư bàng quang",
            "Gãy xương (phụ nữ có nguy cơ)"
        ],
        "dosage": {
            "adult_start": "15-30mg x 1 lần/ngày",
            "adult_usual": "15-45mg x 1 lần/ngày",
            "adult_max": "45mg/ngày",
            "notes": "Uống bất kỳ lúc nào. Tác dụng chậm (2-4 tuần). Gây giữ nước"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Giữ nước, phù (tăng nguy cơ suy tim)",
            "Tăng cân",
            "Gãy xương (phụ nữ có nguy cơ tăng)",
            "Thiếu máu",
            "Tăng LDL cholesterol",
            "Ung thư bàng quang (tăng nhẹ nguy cơ)"
        ],
        "interactions": [
            "Insulin: tăng nguy cơ suy tim, phù",
            "Digoxin: có thể tăng nồng độ digoxin"
        ],
        "pregnancy": "C"
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
    
    "Domperidone": {
        "group": "Gastrointestinal - Prokinetic, Antiemetic",
        "vietnamese_name": "Domperidone, Motilium",
        "administration": ["PO"],
        "indications": [
            "Buồn nôn, nôn",
            "Liệt dạ dày (gastroparesis)",
            "Ợ nóng",
            "Trào ngược dạ dày thực quản"
        ],
        "contraindications": [
            "Dị ứng domperidone",
            "Chảy máu dạ dày",
            "Tắc ruột cơ học",
            "Prolactinoma",
            "Dùng với các thuốc QT kéo dài"
        ],
        "dosage": {
            "adult_nausea": "10-20mg x 3-4 lần/ngày, uống trước bữa ăn",
            "adult_gastroparesis": "10mg x 3-4 lần/ngày trước bữa ăn",
            "adult_max": "80mg/ngày",
            "notes": "Không qua hàng rào máu-não nên ít tác dụng phụ thần kinh hơn metoclopramide"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Thận trọng, giảm liều 50%"
        },
        "side_effects": [
            "Rối loạn kinh nguyệt",
            "Tăng prolactin",
            "Đau vú",
            "Chảy sữa (galactorrhea)",
            "QT kéo dài (liều cao)",
            "Nhức đầu"
        ],
        "interactions": [
            "QT kéo dài: tránh dùng với thuốc QT kéo dài (amiodarone, quinolone)",
            "Ketoconazole: tăng nồng độ domperidone",
            "Erythromycin: tăng nồng độ domperidone"
        ],
        "pregnancy": "C"
    },
    
    "Ondansetron": {
        "group": "Gastrointestinal - Antiemetic (5-HT3 Antagonist)",
        "vietnamese_name": "Ondansetron, Zofran",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Buồn nôn, nôn sau hóa trị",
            "Buồn nôn, nôn sau phẫu thuật",
            "Buồn nôn, nôn do xạ trị",
            "Buồn nôn, nôn do nhiều nguyên nhân"
        ],
        "contraindications": [
            "Dị ứng ondansetron",
            "QT kéo dài",
            "Dùng với apomorphine"
        ],
        "dosage": {
            "adult_po": "8mg x 2-3 lần/ngày",
            "adult_iv_im": "4-8mg x 2-3 lần/ngày",
            "adult_chemotherapy": "8mg IV trước hóa trị, sau đó 8mg PO x 2 lần/ngày x 3 ngày",
            "adult_surgery": "4mg IV trước khi gây mê",
            "notes": "Rất hiệu quả cho buồn nôn do hóa trị và phẫu thuật"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "QT kéo dài",
            "Nhức đầu",
            "Chóng mặt",
            "Táo bón",
            "Mệt mỏi"
        ],
        "interactions": [
            "Apomorphine: chống chỉ định",
            "Thuốc QT kéo dài: tăng nguy cơ loạn nhịp",
            "CYP2D6 inhibitors: tăng nồng độ ondansetron"
        ],
        "pregnancy": "B"
    },
    
    "Lansoprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor (PPI)",
        "vietnamese_name": "Lansoprazole, Prevacid",
        "administration": ["PO"],
        "indications": [
            "Loét dạ dày tá tràng",
            "Trào ngược dạ dày thực quản (GERD)",
            "Hội chứng Zollinger-Ellison",
            "Tiệt trừ H. pylori (kết hợp)"
        ],
        "contraindications": [
            "Dị ứng lansoprazole/PPI"
        ],
        "dosage": {
            "adult_ulcer": "15-30mg x 1 lần/ngày",
            "adult_gerd": "15-30mg x 1 lần/ngày",
            "adult_h_pylori": "30mg x 2 lần/ngày (với amoxicillin + clarithromycin)",
            "notes": "Uống trước bữa ăn 30 phút. Viên tan trong miệng không cần nước"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau đầu",
            "Tiêu chảy",
            "Đau bụng",
            "Tăng nguy cơ nhiễm trùng (Clostridium difficile)",
            "Loãng xương (dùng lâu dài)",
            "Thiếu vitamin B12 (dùng lâu dài)",
            "Thiếu magie (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nhẹ nguy cơ chảy máu",
            "Digoxin: tăng nhẹ nồng độ digoxin",
            "Ketoconazole/Itraconazole: giảm hấp thu (giảm acid dạ dày)",
            "Methotrexate: tăng nồng độ methotrexate"
        ],
        "pregnancy": "B"
    },
    
    "Esomeprazole": {
        "group": "Gastrointestinal - Proton Pump Inhibitor (PPI)",
        "vietnamese_name": "Esomeprazole, Nexium",
        "administration": ["PO", "IV"],
        "indications": [
            "Loét dạ dày tá tràng",
            "Trào ngược dạ dày thực quản (GERD)",
            "Hội chứng Zollinger-Ellison",
            "Tiệt trừ H. pylori (kết hợp)",
            "Loét do NSAID (dự phòng)"
        ],
        "contraindications": [
            "Dị ứng esomeprazole/PPI"
        ],
        "dosage": {
            "adult_po": "20-40mg x 1 lần/ngày",
            "adult_iv": "20-40mg x 1 lần/ngày",
            "adult_h_pylori": "20mg x 2 lần/ngày (với amoxicillin + clarithromycin)",
            "adult_gerd_healing": "40mg x 1 lần/ngày x 4-8 tuần",
            "notes": "Enantiomer của omeprazole (S-omeprazole). Uống trước bữa ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau đầu",
            "Tiêu chảy",
            "Đau bụng",
            "Tăng nguy cơ nhiễm trùng (C. difficile)",
            "Loãng xương (dùng lâu dài)",
            "Thiếu vitamin B12 (dùng lâu dài)",
            "Thiếu magie (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nhẹ nguy cơ chảy máu",
            "Ketoconazole/Itraconazole: giảm hấp thu",
            "Clopidogrel: có thể giảm hiệu quả (controversial)",
            "Methotrexate: tăng nồng độ methotrexate"
        ],
        "pregnancy": "B"
    },
    
    "Sucralfate": {
        "group": "Gastrointestinal - Mucosal Protectant",
        "vietnamese_name": "Sucralfate, Carafate",
        "administration": ["PO"],
        "indications": [
            "Loét dạ dày tá tràng",
            "Viêm dạ dày",
            "Trào ngược dạ dày thực quản",
            "Loét do stress"
        ],
        "contraindications": [
            "Dị ứng sucralfate",
            "Suy thận nặng (tăng nguy cơ tích tụ nhôm)"
        ],
        "dosage": {
            "adult_ulcer": "1g x 4 lần/ngày (trước bữa ăn và trước khi ngủ) hoặc 2g x 2 lần/ngày",
            "adult_maintenance": "1g x 2 lần/ngày",
            "notes": "Uống khi bụng đói (1 giờ trước bữa ăn). Không dùng với PPI, H2 blocker, antacid (cách 2 giờ)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Tránh dùng (tích tụ nhôm)"
        },
        "side_effects": [
            "Táo bón",
            "Khô miệng",
            "Buồn nôn",
            "Đầy hơi",
            "Tích tụ nhôm (suy thận)"
        ],
        "interactions": [
            "PPI/H2 blocker/Antacid: giảm hiệu quả - cách 2 giờ",
            "Warfarin: có thể tăng tác dụng chống đông",
            "Phenytoin: giảm hấp thu phenytoin",
            "Digoxin: giảm hấp thu digoxin",
            "Quinolone: giảm hấp thu quinolone",
            "Thyroxine: giảm hấp thu thyroxine"
        ],
        "pregnancy": "B"
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
        "pregnancy": "C - D trong 3 tháng cuối"
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
        "pregnancy": "C - D trong 3 tháng cuối"
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
        "pregnancy": "C - D trong 3 tháng cuối (gây hội chứng cai ở trẻ sơ sinh)"
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
            "notes": "Prodrug của morphine, cần CYP2D6 để chuyển hóa. Một số người không có enzyme → không hiệu quả"
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
        "pregnancy": "C"
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
    
    "Salmeterol": {
        "group": "Respiratory - Long-acting Beta-2 Agonist (LABA)",
        "vietnamese_name": "Salmeterol, Serevent",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (phòng ngừa, phải dùng với ICS)",
            "COPD (phòng ngừa)",
            "Co thắt phế quản ban đêm",
            "Dự phòng co thắt do vận động"
        ],
        "contraindications": [
            "Dị ứng",
            "Nhịp tim nhanh nặng",
            "Hen phế quản cấp (không dùng đơn độc)"
        ],
        "dosage": {
            "adult_inhalation": "50mcg x 2 lần/ngày (sáng và tối)",
            "notes": "PHẢI dùng kết hợp với ICS. Không dùng đơn độc cho hen. Tác dụng kéo dài 12 giờ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tim đập nhanh",
            "Run cơ",
            "Đau đầu",
            "Co thắt phế quản nghịch lý (hiếm)",
            "Loạn nhịp tim (hiếm)"
        ],
        "interactions": [
            "Beta-blocker: đối kháng tác dụng",
            "Theophylline: tăng tác dụng phụ"
        ],
        "pregnancy": "C"
    },
    
    "Ipratropium": {
        "group": "Respiratory - Anticholinergic (Short-acting)",
        "vietnamese_name": "Ipratropium, Atrovent",
        "administration": ["Inhalation", "Nebulizer"],
        "indications": [
            "COPD (cắt cơn và phòng ngừa)",
            "Hen phế quản (kết hợp với SABA)",
            "Co thắt phế quản",
            "Chảy nước mũi (dạng xịt mũi)"
        ],
        "contraindications": [
            "Dị ứng atropine/ipratropium",
            "Glaucoma góc đóng",
            "Tăng nhãn áp"
        ],
        "dosage": {
            "adult_inhalation": "1-2 puffs (20-40mcg) mỗi 6-8 giờ",
            "adult_nebulizer": "250-500mcg mỗi 6-8 giờ",
            "adult_max": "12 puffs/ngày hoặc 3 lần nebulizer/ngày",
            "notes": "Tác dụng sau 15-30 phút, kéo dài 4-6 giờ. An toàn hơn beta-agonist cho bệnh nhân tim mạch"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Khô miệng",
            "Đắng miệng",
            "Ho",
            "Kích ứng mắt (nếu vào mắt)",
            "Tăng nhãn áp (nếu vào mắt)",
            "Bí tiểu (hiếm)"
        ],
        "interactions": [
            "Anticholinergic khác: tăng tác dụng phụ",
            "Beta-agonist: hiệp đồng tốt"
        ],
        "pregnancy": "B"
    },
    
    "Tiotropium": {
        "group": "Respiratory - Anticholinergic (Long-acting)",
        "vietnamese_name": "Tiotropium, Spiriva",
        "administration": ["Inhalation (HandiHaler hoặc Respimat)"],
        "indications": [
            "COPD (phòng ngừa)",
            "Hen phế quản (kết hợp với ICS, nếu không kiểm soát)"
        ],
        "contraindications": [
            "Dị ứng atropine/tiotropium",
            "Glaucoma góc đóng",
            "Tăng nhãn áp",
            "Phì đại tuyến tiền liệt nặng"
        ],
        "dosage": {
            "adult_handihaler": "18mcg x 1 lần/ngày",
            "adult_respimat": "5mcg x 2 lần/ngày (sáng và tối)",
            "notes": "Tác dụng kéo dài 24 giờ. Dùng 1 lần/ngày với HandiHaler"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Tránh dùng (thải qua thận)"
        },
        "side_effects": [
            "Khô miệng (thường gặp)",
            "Ho",
            "Nhiễm trùng đường hô hấp trên",
            "Táo bón",
            "Bí tiểu",
            "Kích ứng mắt (nếu vào mắt)"
        ],
        "interactions": [
            "Anticholinergic khác: tăng tác dụng phụ",
            "Beta-agonist: hiệp đồng"
        ],
        "pregnancy": "C"
    },
    
    "Budesonide inhaled": {
        "group": "Respiratory - Inhaled Corticosteroid (ICS)",
        "vietnamese_name": "Budesonide, Pulmicort",
        "administration": ["Inhalation", "Nebulizer"],
        "indications": [
            "Hen phế quản (kiểm soát, phòng ngừa)",
            "COPD (nếu có nhiều đợt cấp)",
            "Viêm phế quản co thắt"
        ],
        "contraindications": [
            "Nhiễm trùng đường hô hấp nặng chưa điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_inhalation_low": "200-400mcg x 2 lần/ngày",
            "adult_inhalation_medium": "400-800mcg x 2 lần/ngày",
            "adult_inhalation_high": "800-1600mcg x 2 lần/ngày",
            "adult_nebulizer": "0.5-1mg x 2 lần/ngày",
            "notes": "Súc miệng sau khi dùng để tránh nấm miệng. Không dùng cho cắt cơn cấp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nấm miệng (candidiasis)",
            "Khàn tiếng",
            "Ho",
            "Khô miệng",
            "Tác dụng toàn thân (liều cao)",
            "Ức chế trục hạ đồi-tuyến yên-thượng thận (liều cao)"
        ],
        "interactions": [
            "Ritonavir: tăng nồng độ budesonide (tránh dùng)",
            "Ketoconazole/Itraconazole: tăng nồng độ"
        ],
        "pregnancy": "C"
    },
    
    "Fluticasone inhaled": {
        "group": "Respiratory - Inhaled Corticosteroid (ICS)",
        "vietnamese_name": "Fluticasone, Flixotide",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (kiểm soát, phòng ngừa)",
            "COPD (kết hợp với LABA nếu nhiều đợt cấp)"
        ],
        "contraindications": [
            "Nhiễm trùng đường hô hấp nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_inhalation_low": "100-250mcg x 2 lần/ngày",
            "adult_inhalation_medium": "250-500mcg x 2 lần/ngày",
            "adult_inhalation_high": "500-1000mcg x 2 lần/ngày",
            "notes": "Súc miệng sau khi dùng. Thường dùng kết hợp với LABA (Salmeterol)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nấm miệng",
            "Khàn tiếng",
            "Ho",
            "Kích ứng cổ họng",
            "Tác dụng toàn thân (liều cao)",
            "Chậm phát triển ở trẻ em (liều cao)"
        ],
        "interactions": [
            "Ritonavir: tăng đáng kể nồng độ fluticasone - tránh dùng",
            "Ketoconazole: tăng nồng độ"
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
    
    # ========== ANTIFUNGALS ==========
    
    "Fluconazole": {
        "group": "Infectious Disease - Antifungal (Azole)",
        "vietnamese_name": "Fluconazole, Diflucan",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm nấm Candida (oral, esophageal, vaginal, systemic)",
            "Nhiễm nấm Cryptococcus",
            "Nhiễm nấm Coccidioidomycosis",
            "Dự phòng nhiễm nấm ở bệnh nhân suy giảm miễn dịch"
        ],
        "contraindications": [
            "Dị ứng fluconazole/azole",
            "Có thai (3 tháng đầu)",
            "Dùng terfenadine/astemizole với liều fluconazole ≥400mg/ngày"
        ],
        "dosage": {
            "adult_candidiasis_oral": "150mg x 1 lần (đơn liều) hoặc 50-100mg x 1 lần/ngày x 7-14 ngày",
            "adult_candidiasis_esophageal": "100-200mg x 1 lần/ngày x 14-21 ngày",
            "adult_candidiasis_vaginal": "150mg x 1 lần (đơn liều)",
            "adult_cryptococcal_meningitis": "400mg ngày đầu, sau đó 200-400mg x 1 lần/ngày",
            "adult_prophylaxis": "50-400mg x 1 lần/ngày",
            "notes": "Thải qua thận, cần điều chỉnh liều khi suy thận"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Nhức đầu",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Ban da",
            "Tăng men gan",
            "Rụng tóc",
            "QT kéo dài (liều cao)"
        ],
        "interactions": [
            "Warfarin: tăng tác dụng chống đông",
            "Phenytoin: tăng nồng độ phenytoin",
            "Cyclosporine: tăng nồng độ cyclosporine",
            "Sulfonylurea: tăng nguy cơ hạ đường huyết",
            "Rifampin: giảm nồng độ fluconazole"
        ],
        "pregnancy": "C - D trong 3 tháng đầu"
    },
    
    "Itraconazole": {
        "group": "Infectious Disease - Antifungal (Azole)",
        "vietnamese_name": "Itraconazole, Sporanox",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm nấm Aspergillosis",
            "Nhiễm nấm Blastomycosis",
            "Nhiễm nấm Histoplasmosis",
            "Nhiễm nấm Candidiasis (oral, esophageal)",
            "Onychomycosis (nấm móng)"
        ],
        "contraindications": [
            "Dị ứng itraconazole/azole",
            "Có thai",
            "Suy tim sung huyết",
            "Dùng với thuốc chuyển hóa CYP3A4 (xem interactions)"
        ],
        "dosage": {
            "adult_systemic": "200mg x 1-2 lần/ngày (PO)",
            "adult_aspergillosis": "200mg x 3 lần/ngày x 3 ngày, sau đó 200mg x 1-2 lần/ngày",
            "adult_onychomycosis": "200mg x 2 lần/ngày x 1 tuần mỗi tháng (x 3-4 tháng)",
            "adult_vaginal_candidiasis": "200mg x 2 lần/ngày x 1 ngày",
            "notes": "Uống với thức ăn để tăng hấp thu. Capsule cần acid dạ dày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng (IV không dùng nếu CrCl <30)",
            "under_30": "Tránh dùng IV"
        },
        "side_effects": [
            "Nhức đầu",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Tăng men gan (hiếm suy gan)",
            "Phù, suy tim",
            "Rụng tóc",
            "Ban da"
        ],
        "interactions": [
            "CYP3A4 substrates: tăng đáng kể nồng độ (simvastatin, lovastatin, midazolam, triazolam, quinidine)",
            "Rifampin: giảm nồng độ itraconazole",
            "Warfarin: tăng tác dụng chống đông",
            "Digoxin: tăng nồng độ digoxin",
            "Phenytoin: tăng nồng độ phenytoin"
        ],
        "pregnancy": "C - D (chống chỉ định)"
    },
    
    "Voriconazole": {
        "group": "Infectious Disease - Antifungal (Azole, 2nd generation)",
        "vietnamese_name": "Voriconazole, Vfend",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm nấm Aspergillosis invasive",
            "Nhiễm nấm Candida (invasive, kháng fluconazole)",
            "Nhiễm nấm Fusarium",
            "Nhiễm nấm Scedosporium",
            "Nhiễm nấm Seedosporium"
        ],
        "contraindications": [
            "Dị ứng voriconazole",
            "Có thai",
            "Dùng rifampin, rifabutin, carbamazepine, phenobarbital, ergotamine"
        ],
        "dosage": {
            "adult_po_loading": "400mg x 2 lần/ngày x 2 ngày đầu",
            "adult_po_maintenance": "200mg x 2 lần/ngày",
            "adult_iv_loading": "6mg/kg x 2 lần/ngày x 2 ngày đầu",
            "adult_iv_maintenance": "4mg/kg x 2 lần/ngày",
            "notes": "Theo dõi nồng độ trong máu. Nguy cơ cao với rối loạn chuyển hóa CYP2C19"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "IV: thay đổi chất pha (không dùng cyclodextrin)",
            "under_30": "IV: thay đổi chất pha. PO: không đổi"
        },
        "side_effects": [
            "Rối loạn thị giác (nhìn mờ, nhạy cảm ánh sáng - thường thoáng qua)",
            "Ban da (phản ứng quang hóa)",
            "Tăng men gan, suy gan",
            "Hallucination",
            "QT kéo dài",
            "Nhức đầu",
            "Buồn nôn"
        ],
        "interactions": [
            "Rifampin/Rifabutin: giảm nồng độ voriconazole - tránh dùng",
            "Carbamazepine/Phenobarbital: giảm nồng độ voriconazole - tránh dùng",
            "Warfarin: tăng tác dụng chống đông",
            "Cyclosporine/Tacrolimus: tăng nồng độ",
            "Phenytoin: giảm nồng độ voriconazole",
            "Omeprazole: tăng nồng độ omeprazole"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Nystatin": {
        "group": "Infectious Disease - Antifungal (Polyene)",
        "vietnamese_name": "Nystatin, Mycostatin",
        "administration": ["PO (suspension, tablet)", "Topical"],
        "indications": [
            "Nhiễm nấm Candida miệng (oral candidiasis/thrush)",
            "Nhiễm nấm Candida thực quản",
            "Nhiễm nấm Candida da (topical)",
            "Nhiễm nấm Candida âm đạo (topical)"
        ],
        "contraindications": [
            "Dị ứng nystatin"
        ],
        "dosage": {
            "adult_oral_suspension": "400,000-600,000 đơn vị x 4 lần/ngày",
            "adult_oral_tablet": "500,000-1,000,000 đơn vị x 4 lần/ngày",
            "adult_topical": "Bôi 2-3 lần/ngày",
            "notes": "Không hấp thu qua đường tiêu hóa. Chỉ tác dụng tại chỗ. Súc miệng và nuốt (suspension)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn (hiếm, PO)",
            "Tiêu chảy (hiếm, PO)",
            "Kích ứng da (hiếm, topical)",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Rất ít tương tác (không hấp thu hệ thống)"
        ],
        "pregnancy": "C - An toàn (không hấp thu)"
    },
    
    # ========== ANTIBIOTICS (COMMON) ==========
    
    "Azithromycin": {
        "group": "Infectious Disease - Macrolide Antibiotic",
        "vietnamese_name": "Azithromycin, Zithromax",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường hô hấp trên (viêm họng, viêm xoang)",
            "Nhiễm trùng đường hô hấp dưới (viêm phổi, viêm phế quản)",
            "Nhiễm trùng da và mô mềm",
            "Chlamydia",
            "Nhiễm trùng đường tiết niệu không biến chứng"
        ],
        "contraindications": [
            "Dị ứng azithromycin/macrolide",
            "QT kéo dài",
            "Rối loạn nhịp tim"
        ],
        "dosage": {
            "adult_respiratory": "500mg x 1 lần/ngày x 3 ngày hoặc 500mg ngày đầu, sau đó 250mg x 1 lần/ngày x 4 ngày",
            "adult_chlamydia": "1g x 1 lần (đơn liều)",
            "adult_iv": "500mg x 1 lần/ngày IV",
            "notes": "Tác dụng kéo dài, uống ít lần hơn erythromycin"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy",
            "Đau bụng",
            "QT kéo dài",
            "Loạn nhịp tim (torsades de pointes)",
            "Rối loạn thính giác (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Digoxin: tăng nồng độ digoxin",
            "Cyclosporine: tăng nồng độ cyclosporine",
            "Thuốc QT kéo dài: tăng nguy cơ loạn nhịp"
        ],
        "pregnancy": "B"
    },
    
    "Clarithromycin": {
        "group": "Infectious Disease - Macrolide Antibiotic",
        "vietnamese_name": "Clarithromycin, Klacid",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường hô hấp (viêm phổi, viêm phế quản)",
            "Nhiễm trùng da và mô mềm",
            "Tiệt trừ H. pylori (kết hợp)",
            "Mycobacterium avium complex (MAC)"
        ],
        "contraindications": [
            "Dị ứng clarithromycin/macrolide",
            "QT kéo dài",
            "Dùng pimozide, terfenadine, astemizole"
        ],
        "dosage": {
            "adult_respiratory": "250-500mg x 2 lần/ngày x 7-14 ngày",
            "adult_h_pylori": "500mg x 2 lần/ngày (với amoxicillin + PPI)",
            "adult_mac": "500mg x 2 lần/ngày",
            "notes": "Mạnh hơn azithromycin nhưng nhiều tương tác hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Vị kim loại trong miệng",
            "QT kéo dài",
            "Rối loạn thính giác (hiếm)"
        ],
        "interactions": [
            "CYP3A4 substrates: tăng đáng kể nồng độ (simvastatin, lovastatin, midazolam)",
            "Warfarin: tăng tác dụng chống đông",
            "Digoxin: tăng nồng độ digoxin",
            "Theophylline: tăng nồng độ theophylline"
        ],
        "pregnancy": "C"
    },
    
    "Ciprofloxacin": {
        "group": "Infectious Disease - Fluoroquinolone Antibiotic",
        "vietnamese_name": "Ciprofloxacin, Cipro",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường tiết niệu (UTI)",
            "Nhiễm trùng đường hô hấp",
            "Nhiễm trùng da và mô mềm",
            "Nhiễm trùng xương và khớp",
            "Nhiễm trùng ổ bụng",
            "Tiêu chảy do vi khuẩn"
        ],
        "contraindications": [
            "Dị ứng ciprofloxacin/quinolone",
            "Có thai",
            "Trẻ em <18 tuổi (trừ chỉ định đặc biệt)",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_uti": "250-500mg x 2 lần/ngày x 3-7 ngày",
            "adult_respiratory": "500-750mg x 2 lần/ngày",
            "adult_complicated": "400mg IV x 2 lần/ngày",
            "notes": "Tránh dùng với antacid, sắt, sucralfate (cách 2 giờ)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Đứt gân Achilles (hiếm nhưng nguy hiểm)",
            "QT kéo dài",
            "Rối loạn thần kinh (co giật, lú lẫn)",
            "Phản ứng quang hóa",
            "Viêm khớp (trẻ em)"
        ],
        "interactions": [
            "Antacid/Sắt/Sucralfate: giảm hấp thu - cách 2 giờ",
            "Warfarin: tăng tác dụng chống đông",
            "Theophylline: tăng nồng độ theophylline",
            "Cyclosporine: tăng nồng độ cyclosporine"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Doxycycline": {
        "group": "Infectious Disease - Tetracycline Antibiotic",
        "vietnamese_name": "Doxycycline, Vibramycin",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường hô hấp",
            "Nhiễm trùng da (mụn trứng cá)",
            "Chlamydia",
            "Lyme disease",
            "Sốt rét phòng ngừa",
            "Rickettsia",
            "Mycoplasma"
        ],
        "contraindications": [
            "Dị ứng doxycycline/tetracycline",
            "Có thai (3 tháng cuối)",
            "Trẻ em <8 tuổi (gây vàng răng)"
        ],
        "dosage": {
            "adult_respiratory": "100mg x 2 lần/ngày x 7-14 ngày",
            "adult_chlamydia": "100mg x 2 lần/ngày x 7 ngày",
            "adult_acne": "50-100mg x 1-2 lần/ngày",
            "adult_malaria_prophylaxis": "100mg x 1 lần/ngày",
            "notes": "Uống với nhiều nước, tránh nằm ngay sau khi uống. Tránh nắng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Loét thực quản (nếu không uống đủ nước)",
            "Phản ứng quang hóa (nhạy cảm ánh sáng)",
            "Vàng răng (trẻ em, có thai)",
            "Tăng áp lực nội sọ (hiếm)",
            "Độc gan (liều cao)"
        ],
        "interactions": [
            "Antacid/Sắt/Calcium: giảm hấp thu - cách 2 giờ",
            "Warfarin: tăng tác dụng chống đông",
            "Digoxin: tăng nồng độ digoxin",
            "Phenytoin/Carbamazepine: giảm nồng độ doxycycline"
        ],
        "pregnancy": "D - Chống chỉ định trong 3 tháng cuối"
    },
    
    "Metronidazole": {
        "group": "Infectious Disease - Nitroimidazole Antibiotic",
        "vietnamese_name": "Metronidazole, Flagyl",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn kỵ khí",
            "Giardia",
            "Trichomonas",
            "Amebiasis",
            "Bacterial vaginosis",
            "H. pylori (kết hợp)",
            "C. difficile colitis"
        ],
        "contraindications": [
            "Dị ứng metronidazole",
            "Có thai (3 tháng đầu)",
            "Dùng disulfiram trong 14 ngày"
        ],
        "dosage": {
            "adult_anaerobic": "500mg x 3 lần/ngày PO hoặc 500mg mỗi 6-8 giờ IV",
            "adult_giardia": "250mg x 3 lần/ngày x 7 ngày",
            "adult_trichomonas": "2g x 1 lần hoặc 500mg x 2 lần/ngày x 7 ngày",
            "adult_c_diff": "500mg x 3 lần/ngày x 10-14 ngày",
            "adult_h_pylori": "500mg x 2 lần/ngày (với amoxicillin + PPI)",
            "notes": "TRÁNH RƯỢU (phản ứng disulfiram-like). Uống với thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Vị kim loại trong miệng",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Phản ứng với rượu (nôn, đỏ mặt, nhịp tim nhanh)",
            "Co giật (liều cao)",
            "Bệnh thần kinh ngoại biên (dùng lâu dài)",
            "Ban da"
        ],
        "interactions": [
            "Rượu: phản ứng disulfiram-like (nôn, đỏ mặt) - TRÁNH",
            "Warfarin: tăng tác dụng chống đông",
            "Lithium: tăng nồng độ lithium",
            "Phenytoin: tăng nồng độ phenytoin",
            "Disulfiram: chống chỉ định"
        ],
        "pregnancy": "B - D trong 3 tháng đầu"
    },
    
    # ========== VITAMINS/SUPPLEMENTS ==========
    
    "Vitamin D": {
        "group": "Vitamins/Supplements - Vitamin D",
        "vietnamese_name": "Vitamin D, Cholecalciferol (D3), Ergocalciferol (D2)",
        "administration": ["PO"],
        "indications": [
            "Thiếu vitamin D",
            "Còi xương",
            "Loãng xương (kết hợp với calcium)",
            "Dự phòng thiếu vitamin D",
            "Suy giảm chức năng thận (cần dạng hoạt hóa)"
        ],
        "contraindications": [
            "Tăng calci máu",
            "Tăng calci niệu",
            "Sỏi thận calci",
            "Quá liều vitamin D"
        ],
        "dosage": {
            "adult_deficiency": "1,000-2,000 IU x 1 lần/ngày hoặc 50,000 IU x 1 lần/tuần x 8 tuần",
            "adult_maintenance": "600-800 IU x 1 lần/ngày",
            "adult_deficiency_severe": "50,000 IU x 1 lần/tuần x 8 tuần, sau đó 1,500-2,000 IU/ngày",
            "adult_osteoporosis": "800-1,200 IU/ngày (kết hợp với calcium)",
            "notes": "D3 (cholecalciferol) hiệu quả hơn D2. Theo dõi nồng độ 25(OH)D trong máu"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Có thể cần dạng hoạt hóa (calcitriol)",
            "under_30": "Dùng calcitriol (dạng hoạt hóa) thay vì vitamin D thường"
        },
        "side_effects": [
            "Tăng calci máu (quá liều)",
            "Tăng calci niệu",
            "Sỏi thận",
            "Buồn nôn, nôn (liều cao)",
            "Táo bón"
        ],
        "interactions": [
            "Calcium: tăng hấp thu calcium",
            "Thiazide diuretics: tăng nguy cơ tăng calci máu",
            "Corticosteroid: giảm hấp thu vitamin D",
            "Cholestyramine: giảm hấp thu vitamin D"
        ],
        "pregnancy": "A - An toàn, cần thiết cho thai kỳ"
    },
    
    "Vitamin B12": {
        "group": "Vitamins/Supplements - Vitamin B12",
        "vietnamese_name": "Vitamin B12, Cyanocobalamin, Methylcobalamin",
        "administration": ["PO", "IM", "SC"],
        "indications": [
            "Thiếu vitamin B12",
            "Thiếu máu hồng cầu to",
            "Bệnh thần kinh do thiếu B12",
            "Dự phòng thiếu B12",
            "Sau phẫu thuật cắt dạ dày"
        ],
        "contraindications": [
            "Dị ứng vitamin B12/cobalt",
            "Leber's disease (thoái hóa thần kinh thị giác di truyền)"
        ],
        "dosage": {
            "adult_po": "1,000-2,000mcg x 1 lần/ngày",
            "adult_im_loading": "1,000mcg IM mỗi ngày x 1 tuần, sau đó mỗi tuần x 4 tuần",
            "adult_im_maintenance": "1,000mcg IM mỗi tháng",
            "adult_deficiency_severe": "1,000mcg IM mỗi ngày x 1-2 tuần, sau đó mỗi tuần x 4 tuần",
            "notes": "IM cho thiếu máu nặng. PO cho thiếu nhẹ hoặc dự phòng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (IM)",
            "Ban da (hiếm)",
            "Phản ứng dị ứng (hiếm)",
            "Tăng đông máu (liều rất cao)"
        ],
        "interactions": [
            "Acid folic: che dấu thiếu B12",
            "Chloramphenicol: giảm đáp ứng với B12",
            "Metformin: giảm nồng độ B12 (dùng lâu dài)",
            "PPI/H2 blocker: giảm hấp thu B12"
        ],
        "pregnancy": "A - An toàn, cần thiết"
    },
    
    "Folic acid": {
        "group": "Vitamins/Supplements - Folate",
        "vietnamese_name": "Folic acid, Folate, Vitamin B9",
        "administration": ["PO"],
        "indications": [
            "Thiếu acid folic",
            "Thiếu máu hồng cầu to do thiếu folate",
            "Dự phòng dị tật ống thần kinh (có thai)",
            "Dự phòng thiếu máu",
            "Điều trị methotrexate độc tính"
        ],
        "contraindications": [
            "Dị ứng acid folic",
            "Ung thư (trừ khi điều trị thiếu máu do hóa trị)"
        ],
        "dosage": {
            "adult_deficiency": "1-5mg x 1 lần/ngày",
            "adult_pregnancy": "400-800mcg x 1 lần/ngày (bắt đầu trước khi có thai)",
            "adult_maintenance": "400mcg x 1 lần/ngày",
            "adult_methotrexate": "1-5mg x 1 lần/ngày (sau khi dùng methotrexate)",
            "notes": "Uống trước khi có thai ít nhất 1 tháng để dự phòng dị tật ống thần kinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Rất ít tác dụng phụ",
            "Ban da (hiếm)",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Methotrexate: giảm hiệu quả methotrexate (trừ khi dùng để điều trị độc tính)",
            "Phenytoin: giảm nồng độ phenytoin",
            "Chloramphenicol: giảm đáp ứng với acid folic",
            "Sulfasalazine: giảm hấp thu acid folic"
        ],
        "pregnancy": "A - An toàn, cần thiết (dự phòng dị tật ống thần kinh)"
    },
    
    "Iron": {
        "group": "Vitamins/Supplements - Iron",
        "vietnamese_name": "Iron, Ferrous sulfate, Ferrous fumarate, Ferrous gluconate",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Thiếu máu thiếu sắt",
            "Dự phòng thiếu sắt",
            "Có thai (dự phòng)",
            "Chảy máu mạn tính",
            "Sau phẫu thuật"
        ],
        "contraindications": [
            "Thừa sắt (hemochromatosis)",
            "Thiếu máu không do thiếu sắt",
            "Viêm loét dạ dày tá tràng nặng",
            "Viêm ruột"
        ],
        "dosage": {
            "adult_po_ferrous_sulfate": "325mg (65mg sắt nguyên tố) x 1-3 lần/ngày",
            "adult_po_ferrous_fumarate": "200mg (66mg sắt nguyên tố) x 2-3 lần/ngày",
            "adult_po_ferrous_gluconate": "300mg (35mg sắt nguyên tố) x 3 lần/ngày",
            "adult_pregnancy": "30-60mg sắt nguyên tố/ngày",
            "adult_iv": "100-200mg IV mỗi ngày hoặc theo phác đồ",
            "notes": "Uống khi bụng đói (1 giờ trước bữa ăn) để tăng hấp thu. Uống với vitamin C"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng (tăng nguy cơ tích tụ sắt)"
        },
        "side_effects": [
            "Táo bón",
            "Phân đen (không nguy hiểm)",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Kích ứng dạ dày",
            "Phản ứng dị ứng (IV)",
            "Quá tải sắt (dùng lâu dài, liều cao)"
        ],
        "interactions": [
            "Antacid/PPI/H2 blocker: giảm hấp thu sắt",
            "Tetracycline/Quinolone: giảm hấp thu cả hai",
            "Thyroxine: giảm hấp thu thyroxine",
            "Chloramphenicol: giảm đáp ứng với sắt",
            "Vitamin C: tăng hấp thu sắt"
        ],
        "pregnancy": "A - An toàn, cần thiết"
    },
    
    "Calcium": {
        "group": "Vitamins/Supplements - Calcium",
        "vietnamese_name": "Calcium, Calcium carbonate, Calcium citrate",
        "administration": ["PO"],
        "indications": [
            "Thiếu calci",
            "Loãng xương (kết hợp với vitamin D)",
            "Hạ calci máu",
            "Dự phòng loãng xương",
            "Có thai, cho con bú"
        ],
        "contraindications": [
            "Tăng calci máu",
            "Tăng calci niệu",
            "Sỏi thận calci",
            "Suy thận nặng",
            "Suy tim (calcium carbonate)"
        ],
        "dosage": {
            "adult_daily_requirement": "1,000-1,200mg nguyên tố calci/ngày",
            "adult_calcium_carbonate": "500-1,000mg x 2-3 lần/ngày (40% nguyên tố calci)",
            "adult_calcium_citrate": "500-1,000mg x 2-3 lần/ngày (21% nguyên tố calci)",
            "adult_hypocalcemia": "1-2g nguyên tố calci/ngày chia 2-3 lần",
            "adult_osteoporosis": "1,000-1,200mg nguyên tố calci/ngày (với vitamin D)",
            "notes": "Calcium citrate hấp thu tốt hơn, không cần acid dạ dày. Uống với thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng hoặc giảm liều (tăng nguy cơ tăng calci máu)"
        },
        "side_effects": [
            "Táo bón",
            "Đầy hơi",
            "Buồn nôn",
            "Tăng calci máu (quá liều)",
            "Sỏi thận (quá liều)",
            "Giảm hấp thu sắt, kẽm"
        ],
        "interactions": [
            "Sắt: giảm hấp thu sắt - cách 2 giờ",
            "Tetracycline/Quinolone: giảm hấp thu kháng sinh - cách 2 giờ",
            "Thyroxine: giảm hấp thu thyroxine - cách 4 giờ",
            "Digoxin: tăng nguy cơ loạn nhịp",
            "Thiazide diuretics: tăng nguy cơ tăng calci máu",
            "Vitamin D: tăng hấp thu calci"
        ],
        "pregnancy": "A - An toàn, cần thiết"
    },
    
    # ========== ANTI-INFECTIVES (OTHER) ==========
    
    "Chloroquine": {
        "group": "Infectious Disease - Antimalarial",
        "vietnamese_name": "Chloroquine, Aralen",
        "administration": ["PO"],
        "indications": [
            "Sốt rét (phòng ngừa và điều trị)",
            "Amebiasis ngoài gan",
            "Lupus ban đỏ hệ thống",
            "Viêm khớp dạng thấp"
        ],
        "contraindications": [
            "Dị ứng chloroquine/4-aminoquinoline",
            "Bệnh võng mạc",
            "Bệnh gan nặng",
            "Bệnh thận nặng",
            "Rối loạn tạo máu"
        ],
        "dosage": {
            "adult_malaria_treatment": "600mg base (1g phosphate) ngày đầu, sau đó 300mg base (500mg phosphate) sau 6-8 giờ, sau đó 300mg base/ngày x 2 ngày",
            "adult_malaria_prophylaxis": "300mg base (500mg phosphate) x 1 lần/tuần, bắt đầu 1-2 tuần trước khi đi, tiếp tục trong khi ở và 4 tuần sau khi về",
            "adult_lupus": "200-400mg base/ngày",
            "notes": "Rất độc cho võng mạc nếu dùng lâu dài. Theo dõi mắt định kỳ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Tránh dùng"
        },
        "side_effects": [
            "Độc võng mạc (dùng lâu dài, không hồi phục)",
            "Rối loạn thị giác",
            "Ban da, rụng tóc",
            "Rối loạn tạo máu",
            "Rối loạn tim mạc (liều cao)",
            "Co giật (quá liều)",
            "Độc gan"
        ],
        "interactions": [
            "Digoxin: tăng nồng độ digoxin",
            "Cimetidine: tăng nồng độ chloroquine",
            "Ampicillin: giảm hấp thu ampicillin",
            "Kaolin: giảm hấp thu chloroquine"
        ],
        "pregnancy": "C - Thận trọng, nhưng có thể dùng cho sốt rét"
    },
    
    "Artesunate": {
        "group": "Infectious Disease - Antimalarial (Artemisinin)",
        "vietnamese_name": "Artesunate",
        "administration": ["PO", "IV", "IM", "Rectal"],
        "indications": [
            "Sốt rét nặng (severe malaria)",
            "Sốt rét kháng chloroquine",
            "Sốt rét sốt rét P. falciparum",
            "Điều trị kết hợp sốt rét (ACT)"
        ],
        "contraindications": [
            "Dị ứng artesunate/artemisinin",
            "3 tháng đầu thai kỳ (trừ sốt rét nặng)",
            "Dùng đơn độc (phải dùng kết hợp)"
        ],
        "dosage": {
            "adult_severe_iv": "2.4mg/kg IV ngay, sau đó 1.2mg/kg sau 12 và 24 giờ, sau đó mỗi ngày",
            "adult_po": "200mg ngày đầu, sau đó 100mg x 1 lần/ngày x 5 ngày (với artemether-lumefantrine)",
            "adult_act": "Theo phác đồ ACT (artesunate + amodiaquine/ mefloquine/piperaquine)",
            "notes": "PHẢI dùng kết hợp với thuốc sốt rét khác (ACT). Không dùng đơn độc"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Nhức đầu",
            "Chóng mặt",
            "Buồn nôn",
            "Rối loạn tiêu hóa",
            "Nhịp tim chậm (hiếm)",
            "Độc tính thần kinh (dùng lâu dài, liều cao - hiếm)"
        ],
        "interactions": [
            "Thuốc sốt rét khác: dùng kết hợp (ACT protocol)",
            "Warfarin: có thể tăng tác dụng chống đông",
            "CYP2A6 substrates: có thể tăng nồng độ"
        ],
        "pregnancy": "D - Tránh trong 3 tháng đầu (trừ sốt rét nặng)"
    },
    
    "Albendazole": {
        "group": "Infectious Disease - Anthelmintic",
        "vietnamese_name": "Albendazole, Albenza",
        "administration": ["PO"],
        "indications": [
            "Giun sán (giun đũa, giun móc, giun tóc, giun kim)",
            "Sán dây",
            "Sán lá gan",
            "Hydatid disease (Echinococcus)",
            "Neurocysticercosis"
        ],
        "contraindications": [
            "Dị ứng albendazole/benzimidazole",
            "Có thai",
            "Suy gan nặng",
            "Giảm bạch cầu"
        ],
        "dosage": {
            "adult_intestinal_worms": "400mg x 1 lần (đơn liều) hoặc 400mg x 2 lần/ngày x 3 ngày",
            "adult_echinococcus": "400mg x 2 lần/ngày x 28 ngày (có thể lặp lại)",
            "adult_neurocysticercosis": "400mg x 2 lần/ngày x 8-30 ngày",
            "adult_hydatid": "10-15mg/kg/ngày x 28 ngày",
            "notes": "Uống với thức ăn béo để tăng hấp thu. Uống kèm corticosteroid cho neurocysticercosis"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Đau đầu",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Giảm bạch cầu",
            "Tăng men gan",
            "Ban da",
            "Rụng tóc (dùng lâu dài)"
        ],
        "interactions": [
            "Dexamethasone: tăng nồng độ albendazole",
            "Praziquantel: tăng nồng độ albendazole",
            "Cimetidine: tăng nồng độ albendazole",
            "Phenytoin/Carbamazepine: giảm nồng độ albendazole"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Mebendazole": {
        "group": "Infectious Disease - Anthelmintic",
        "vietnamese_name": "Mebendazole, Vermox",
        "administration": ["PO"],
        "indications": [
            "Giun sán (giun đũa, giun móc, giun tóc, giun kim)",
            "Sán dây",
            "Trichinosis"
        ],
        "contraindications": [
            "Dị ứng mebendazole/benzimidazole",
            "Có thai",
            "Trẻ em <1 tuổi"
        ],
        "dosage": {
            "adult_intestinal_worms": "100mg x 2 lần/ngày x 3 ngày",
            "adult_pinworm": "100mg x 1 lần (đơn liều), lặp lại sau 2-3 tuần",
            "adult_whipworm": "100mg x 2 lần/ngày x 3 ngày",
            "adult_tapeworm": "100mg x 2 lần/ngày x 3 ngày",
            "notes": "Uống với thức ăn hoặc không đều được. Không hấp thu tốt nên ít tác dụng phụ hệ thống"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau bụng",
            "Tiêu chảy",
            "Buồn nôn",
            "Ban da",
            "Giảm bạch cầu (dùng lâu dài, liều cao)",
            "Độc gan (hiếm)"
        ],
        "interactions": [
            "Cimetidine: có thể tăng nồng độ mebendazole",
            "Carbamazepine/Phenytoin: có thể giảm nồng độ mebendazole"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    # ========== ENDOCRINOLOGY ==========
    
    "Levothyroxine": {
        "group": "Endocrinology - Thyroid Hormone",
        "vietnamese_name": "Levothyroxine, Synthroid, Euthyrox, Thyroxine",
        "administration": ["PO", "IV"],
        "indications": [
            "Suy giáp (hypothyroidism)",
            "Suy giáp bẩm sinh",
            "Bướu cổ (goiter)",
            "Myxedema coma (IV)",
            "Ức chế TSH sau điều trị ung thư tuyến giáp"
        ],
        "contraindications": [
            "Cường giáp không điều trị",
            "Nhồi máu cơ tim cấp",
            "Viêm cơ tim cấp",
            "Dị ứng levothyroxine"
        ],
        "dosage": {
            "adult_start": "25-50mcg x 1 lần/ngày (sáng đói, trước ăn 30-60 phút)",
            "adult_usual": "75-150mcg x 1 lần/ngày",
            "adult_elderly": "Bắt đầu 12.5-25mcg/ngày, tăng dần",
            "adult_cardiac": "Bắt đầu 12.5-25mcg/ngày",
            "adult_myxedema_coma": "200-500mcg IV x 1 lần, sau đó 50-100mcg/ngày",
            "notes": "Uống sáng đói, cách xa thức ăn, thuốc khác ít nhất 30-60 phút"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Dấu hiệu cường giáp (quá liều): tim đập nhanh, lo âu, mất ngủ, đổ mồ hôi",
            "Đau ngực",
            "Nhức đầu",
            "Rối loạn kinh nguyệt",
            "Rụng tóc (tạm thời)",
            "Loạn nhịp tim (quá liều)"
        ],
        "interactions": [
            "Calcium/Sắt/Antacid: giảm hấp thu - cách 4 giờ",
            "Cholestyramine: giảm hấp thu - cách 4 giờ",
            "Warfarin: tăng tác dụng chống đông (điều chỉnh liều warfarin)",
            "Digoxin: có thể cần tăng liều digoxin",
            "Insulin/Oral hypoglycemics: có thể cần điều chỉnh liều",
            "Estrogen: có thể cần tăng liều levothyroxine"
        ],
        "pregnancy": "A - An toàn, cần thiết cho thai kỳ"
    },
    
    "Methimazole": {
        "group": "Endocrinology - Antithyroid (Thionamide)",
        "vietnamese_name": "Methimazole, Tapazole",
        "administration": ["PO"],
        "indications": [
            "Cường giáp (hyperthyroidism)",
            "Bệnh Graves",
            "Bướu cổ độc (toxic goiter)",
            "Chuẩn bị trước phẫu thuật tuyến giáp",
            "Điều trị cường giáp trước phóng xạ iod"
        ],
        "contraindications": [
            "Dị ứng methimazole",
            "Có thai (3 tháng đầu - dùng PTU)",
            "Đang cho con bú (ưu tiên PTU)",
            "Giảm bạch cầu nặng"
        ],
        "dosage": {
            "adult_mild": "15-30mg/ngày chia 1-3 lần",
            "adult_moderate": "30-45mg/ngày chia 2-3 lần",
            "adult_severe": "40-60mg/ngày chia 2-3 lần",
            "adult_maintenance": "5-15mg/ngày chia 1-2 lần",
            "notes": "Khởi đầu với liều cao, giảm dần khi đạt bình giáp. Điều trị 12-18 tháng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Giảm bạch cầu, giảm tiểu cầu (nguy hiểm - theo dõi công thức máu)",
            "Phát ban",
            "Ngứa",
            "Đau khớp",
            "Rối loạn vị giác",
            "Độc gan (hiếm nhưng nguy hiểm)",
            "Agranulocytosis (mất bạch cầu - hiếm nhưng nguy hiểm)"
        ],
        "interactions": [
            "Warfarin: có thể cần giảm liều warfarin (khi đạt bình giáp)",
            "Digoxin: có thể cần giảm liều digoxin"
        ],
        "pregnancy": "D - Tránh trong 3 tháng đầu (dùng PTU). Thận trọng sau đó"
    },
    
    "Propylthiouracil": {
        "group": "Endocrinology - Antithyroid (Thionamide)",
        "vietnamese_name": "Propylthiouracil, PTU",
        "administration": ["PO"],
        "indications": [
            "Cường giáp (hyperthyroidism)",
            "Bệnh Graves",
            "Bướu cổ độc",
            "Có thai (3 tháng đầu - ưu tiên hơn methimazole)",
            "Cường giáp cấp (thyroid storm)"
        ],
        "contraindications": [
            "Dị ứng propylthiouracil",
            "Giảm bạch cầu nặng",
            "Đang cho con bú (có thể dùng)"
        ],
        "dosage": {
            "adult_mild": "100-150mg x 3 lần/ngày",
            "adult_moderate": "150-200mg x 3 lần/ngày",
            "adult_severe": "200-300mg x 3-4 lần/ngày",
            "adult_storm": "200-300mg x 4 lần/ngày",
            "adult_maintenance": "50-150mg/ngày chia 1-3 lần",
            "notes": "Ưu tiên hơn methimazole trong 3 tháng đầu thai kỳ. Nhiều tác dụng phụ gan hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Độc gan (cao hơn methimazole, có thể suy gan cấp)",
            "Giảm bạch cầu, agranulocytosis",
            "Phát ban",
            "Ngứa",
            "Đau khớp",
            "Vasculitis (hiếm)",
            "Lupus-like syndrome (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể cần giảm liều warfarin",
            "Digoxin: có thể cần giảm liều digoxin"
        ],
        "pregnancy": "D - An toàn hơn methimazole trong 3 tháng đầu, nhưng vẫn thận trọng"
    },
    
    "Prednisone": {
        "group": "Endocrinology - Corticosteroid (Glucocorticoid)",
        "vietnamese_name": "Prednisone, Deltasone",
        "administration": ["PO"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản nặng",
            "COPD đợt cấp",
            "Lupus ban đỏ hệ thống",
            "Viêm mạch máu",
            "Bệnh viêm ruột",
            "Dị ứng nặng",
            "Ung thư (kết hợp hóa trị)",
            "Ức chế miễn dịch",
            "Suy thượng thận"
        ],
        "contraindications": [
            "Nhiễm trùng nặng chưa điều trị",
            "Nhiễm nấm hệ thống",
            "Loét dạ dày tá tràng đang hoạt động",
            "Suy tim nặng",
            "Tăng huyết áp không kiểm soát"
        ],
        "dosage": {
            "adult_antiinflammatory": "5-60mg/ngày chia 1-4 lần",
            "adult_immunosuppression": "1-2mg/kg/ngày",
            "adult_asthma_exacerbation": "40-60mg/ngày x 5-7 ngày",
            "adult_copd_exacerbation": "30-40mg/ngày x 10-14 ngày",
            "adult_rheumatoid": "5-10mg/ngày",
            "adult_adrenal_insufficiency": "5-7.5mg/ngày",
            "notes": "Giảm liều dần dần khi ngừng (tránh suy thượng thận). Uống với thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Hoại tử xương",
            "Loét dạ dày",
            "Tăng cân",
            "Giữ nước",
            "Yếu cơ",
            "Ức chế miễn dịch (tăng nguy cơ nhiễm trùng)",
            "Ức chế trục hạ đồi-tuyến yên-thượng thận",
            "Đục thủy tinh thể",
            "Tăng nhãn áp"
        ],
        "interactions": [
            "Warfarin: tăng/giảm tác dụng chống đông (thay đổi)",
            "Insulin/Oral hypoglycemics: tăng đường huyết - cần điều chỉnh",
            "Thuốc hạ huyết áp: giảm hiệu quả",
            "Diuretics: tăng mất kali",
            "NSAID: tăng nguy cơ loét dạ dày",
            "Vaccine sống: chống chỉ định",
            "Rifampin: giảm nồng độ prednisone"
        ],
        "pregnancy": "C - Thận trọng"
    },
    
    # ========== ONCOLOGY ==========
    
    "Cisplatin": {
        "group": "Oncology - Platinum Compound",
        "vietnamese_name": "Cisplatin, Platinol",
        "administration": ["IV"],
        "indications": [
            "Ung thư phổi (NSCLC, SCLC)",
            "Ung thư đầu cổ",
            "Ung thư tinh hoàn",
            "Ung thư buồng trứng",
            "Ung thư bàng quang",
            "Ung thư cổ tử cung"
        ],
        "contraindications": [
            "Dị ứng cisplatin",
            "Suy thận nặng (CrCl <60)",
            "Giảm thính lực",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_standard": "50-100mg/m² IV mỗi 3-4 tuần",
            "adult_weekly": "20-30mg/m² IV mỗi tuần",
            "adult_daily": "15-20mg/m² IV x 5 ngày (mỗi 3-4 tuần)",
            "notes": "Truyền với nước muối sinh lý (NaCl 0.9%), cần pre-hydration và post-hydration"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Không dùng hoặc giảm liều 50-75%"
        },
        "side_effects": [
            "Độc thận (phổ biến và nghiêm trọng - cần hydration)",
            "Nôn mửa nặng (thường xảy ra)",
            "Giảm thính lực (có thể vĩnh viễn)",
            "Độc thần kinh ngoại biên (tê bì, dị cảm)",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Rụng tóc",
            "Hạ magne máu (phổ biến)",
            "Độc tim (hiếm)"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Furosemide: tăng độc thận",
            "Phenytoin: giảm nồng độ phenytoin",
            "Thuốc độc thận khác: tránh dùng đồng thời"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Carboplatin": {
        "group": "Oncology - Platinum Compound",
        "vietnamese_name": "Carboplatin, Paraplatin",
        "administration": ["IV"],
        "indications": [
            "Ung thư buồng trứng",
            "Ung thư phổi (NSCLC)",
            "Ung thư đầu cổ",
            "Ung thư cổ tử cung",
            "Ung thư tinh hoàn"
        ],
        "contraindications": [
            "Dị ứng carboplatin hoặc platinum compounds",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_calvert": "AUC 4-6 mg/mL x min IV (tính theo GFR)",
            "adult_fixed": "300-400mg/m² IV mỗi 4 tuần",
            "adult_weekly": "100mg/m² IV mỗi tuần",
            "notes": "Dùng công thức Calvert: Dose (mg) = AUC x (GFR + 25). Ít độc thận hơn cisplatin"
        },
        "renal_adjustment": {
            "normal": "Tính theo GFR trong công thức Calvert",
            "30_60": "Giảm AUC hoặc liều 25-50%",
            "under_30": "Thận trọng, giảm liều đáng kể"
        },
        "side_effects": [
            "Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến hơn cisplatin)",
            "Nôn mửa (ít hơn cisplatin)",
            "Độc thận (ít hơn cisplatin nhưng vẫn có)",
            "Rụng tóc (ít)",
            "Độc thần kinh (ít hơn cisplatin)",
            "Phản ứng dị ứng (hiếm)",
            "Hạ magne máu"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Thuốc độc thận: tránh dùng đồng thời",
            "Phenytoin: giảm nồng độ phenytoin"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Oxaliplatin": {
        "group": "Oncology - Platinum Compound",
        "vietnamese_name": "Oxaliplatin, Eloxatin",
        "administration": ["IV"],
        "indications": [
            "Ung thư đại trực tràng (adjuvant và metastatic)",
            "Ung thư dạ dày",
            "Ung thư tụy"
        ],
        "contraindications": [
            "Dị ứng oxaliplatin hoặc platinum compounds",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Suy thận nặng (CrCl <30)",
            "Suy gan nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_folfox": "85mg/m² IV mỗi 2 tuần (phối hợp với 5-FU và leucovorin)",
            "adult_single": "85-130mg/m² IV mỗi 2-3 tuần",
            "notes": "Truyền 2-6 giờ. Tránh lạnh (độc lạnh - cold-induced neuropathy)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Thận trọng, giảm liều 25-50%"
        },
        "side_effects": [
            "Độc lạnh (cold-induced neuropathy - tê, cảm giác như bị điện giật khi tiếp xúc lạnh)",
            "Độc thần kinh ngoại biên (tê bì, mất cảm giác)",
            "Nôn mửa",
            "Tiêu chảy",
            "Giảm bạch cầu, tiểu cầu",
            "Phản ứng dị ứng (hiếm)",
            "Độc gan (tăng transaminase)"
        ],
        "interactions": [
            "Thuốc độc thận: thận trọng",
            "Phenytoin: có thể giảm nồng độ phenytoin"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "5-Fluorouracil": {
        "group": "Oncology - Antimetabolite",
        "vietnamese_name": "5-Fluorouracil, 5-FU, Fluorouracil",
        "administration": ["IV"],
        "indications": [
            "Ung thư đại trực tràng (adjuvant và metastatic)",
            "Ung thư dạ dày",
            "Ung thư đầu cổ",
            "Ung thư tụy",
            "Ung thư vú",
            "Ung thư da (topical)"
        ],
        "contraindications": [
            "Dị ứng 5-FU",
            "Thiếu hụt DPD (dihydropyrimidine dehydrogenase)",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_bolus": "400-600mg/m² IV bolus ngày 1, sau đó 400-600mg/m²/ngày x 4 ngày (mỗi 4 tuần)",
            "adult_infusion": "1000mg/m²/ngày IV infusion x 4-5 ngày (mỗi 4 tuần)",
            "adult_weekly": "500-600mg/m² IV mỗi tuần",
            "adult_topical": "5% cream bôi 2 lần/ngày",
            "notes": "Phối hợp với leucovorin để tăng hiệu quả. Cần test DPD nếu có thể"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều 25%",
            "under_30": "Thận trọng, giảm liều 25-50%"
        },
        "side_effects": [
            "Loét miệng (stomatitis - phổ biến)",
            "Tiêu chảy (phổ biến, có thể nặng)",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Ban da",
            "Rụng tóc",
            "Độc tim (hiếm nhưng nguy hiểm)",
            "Rối loạn thần kinh (hiếm)",
            "Tăng bilirubin"
        ],
        "interactions": [
            "Leucovorin: tăng hiệu quả và độc tính",
            "Methotrexate: tăng độc tính",
            "Warfarin: tăng nguy cơ chảy máu",
            "Phenytoin: tăng nồng độ phenytoin"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Methotrexate": {
        "group": "Oncology - Antimetabolite (Antifolate)",
        "vietnamese_name": "Methotrexate, MTX, Amethopterin",
        "administration": ["PO", "IV", "IM", "SC", "IT"],
        "indications": [
            "Bệnh bạch cầu cấp (leukemia)",
            "U lympho (lymphoma)",
            "U nguyên bào nuôi (choriocarcinoma)",
            "Ung thư đầu cổ",
            "Ung thư phổi",
            "Viêm khớp dạng thấp (liều thấp)",
            "Vẩy nến (liều thấp)"
        ],
        "contraindications": [
            "Dị ứng methotrexate",
            "Suy thận nặng",
            "Suy gan nặng",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Loét dạ dày tá tràng hoạt động",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_cancer_high": "50-250mg/m² IV (cần folinic acid rescue)",
            "adult_cancer_moderate": "10-50mg/m² IV/IM/PO",
            "adult_ra_psoriasis": "7.5-25mg PO x 1 lần/tuần",
            "adult_it": "12-15mg IT (theo dõi chặt chẽ)",
            "notes": "Liều cao (>50mg/m²) cần folinic acid rescue sau 24 giờ. Uống nhiều nước"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Không dùng hoặc giảm liều đáng kể, theo dõi sát"
        },
        "side_effects": [
            "Giảm bạch cầu, tiểu cầu, thiếu máu (myelosuppression - nghiêm trọng)",
            "Loét miệng (stomatitis)",
            "Tiêu chảy",
            "Độc gan (tăng transaminase, xơ gan)",
            "Độc phổi (viêm phổi kẽ - hiếm nhưng nguy hiểm)",
            "Độc thận (với liều cao)",
            "Rụng tóc",
            "Phát ban"
        ],
        "interactions": [
            "Probenecid: tăng độc tính methotrexate",
            "NSAID: tăng độc tính",
            "Penicillin: tăng độc tính",
            "Trimethoprim-Sulfamethoxazole: tăng độc tính",
            "Folinic acid: giải độc (rescue therapy)"
        ],
        "pregnancy": "X - Chống chỉ định tuyệt đối"
    },
    
    "Cyclophosphamide": {
        "group": "Oncology - Alkylating Agent",
        "vietnamese_name": "Cyclophosphamide, Endoxan, Cytoxan",
        "administration": ["PO", "IV"],
        "indications": [
            "U lympho (lymphoma)",
            "Bệnh bạch cầu",
            "Ung thư vú",
            "Ung thư buồng trứng",
            "Bệnh tự miễn (lupus, vasculitis, liều thấp)"
        ],
        "contraindications": [
            "Dị ứng cyclophosphamide",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Suy thận nặng",
            "Suy gan nặng",
            "Viêm bàng quang chảy máu",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_cancer_high": "500-1000mg/m² IV mỗi 3-4 tuần",
            "adult_cancer_moderate": "50-200mg/m² PO/IV mỗi ngày",
            "adult_autoimmune": "1-2mg/kg PO mỗi ngày hoặc 500-750mg/m² IV mỗi tháng",
            "notes": "Uống nhiều nước (2-3L/ngày) để phòng viêm bàng quang. Có thể dùng mesna để bảo vệ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Thận trọng, giảm liều đáng kể"
        },
        "side_effects": [
            "Viêm bàng quang chảy máu (hemorrhagic cystitis - phổ biến, nguy hiểm)",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Buồn nôn, nôn",
            "Rụng tóc",
            "Vô sinh (nam và nữ)",
            "Ung thư thứ phát (hiếm)",
            "Độc tim (với liều cao)",
            "Hội chứng lysis khối u"
        ],
        "interactions": [
            "Allopurinol: tăng độc tính",
            "Phenobarbital: tăng chuyển hóa",
            "Succinylcholine: kéo dài tác dụng",
            "Mesna: bảo vệ chống viêm bàng quang"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Ifosfamide": {
        "group": "Oncology - Alkylating Agent",
        "vietnamese_name": "Ifosfamide, Ifex",
        "administration": ["IV"],
        "indications": [
            "Ung thư tinh hoàn",
            "U lympho",
            "Sarcoma mô mềm",
            "Ung thư xương",
            "Ung thư phổi (một số loại)"
        ],
        "contraindications": [
            "Dị ứng ifosfamide",
            "Suy thận nặng",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Viêm bàng quang chảy máu",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_standard": "1200-2000mg/m² IV x 3-5 ngày (mỗi 3-4 tuần)",
            "adult_high": "3000-5000mg/m² IV x 1-3 ngày (với mesna)",
            "notes": "Luôn dùng kèm mesna để bảo vệ bàng quang. Uống nhiều nước"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều 25-50%",
            "under_30": "Thận trọng, giảm liều đáng kể"
        },
        "side_effects": [
            "Viêm bàng quang chảy máu (nguy hiểm - cần mesna)",
            "Độc thần kinh trung ương (lú lẫn, co giật - với liều cao)",
            "Giảm bạch cầu, tiểu cầu",
            "Buồn nôn, nôn",
            "Rụng tóc",
            "Độc thận",
            "Vô sinh"
        ],
        "interactions": [
            "Mesna: bảo vệ chống viêm bàng quang (bắt buộc)",
            "Phenobarbital: tăng chuyển hóa",
            "Cisplatin: tăng độc thận"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Doxorubicin": {
        "group": "Oncology - Anthracycline",
        "vietnamese_name": "Doxorubicin, Adriamycin",
        "administration": ["IV"],
        "indications": [
            "Ung thư vú",
            "U lympho",
            "Bệnh bạch cầu",
            "Sarcoma mô mềm",
            "Ung thư buồng trứng",
            "Ung thư phổi (SCLC)"
        ],
        "contraindications": [
            "Dị ứng doxorubicin",
            "Suy tim nặng",
            "Bệnh tim tiềm ẩn",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_standard": "60-75mg/m² IV mỗi 3 tuần",
            "adult_weekly": "20-30mg/m² IV mỗi tuần",
            "adult_cardiac_risk": "Giảm liều hoặc dùng liposomal doxorubicin",
            "notes": "Tổng liều tích lũy tối đa: 450-550mg/m² (nguy cơ độc tim). Dùng phác đồ 3 tuần"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Thận trọng, giảm liều"
        },
        "side_effects": [
            "Độc tim (suy tim, rối loạn nhịp - tích lũy, không hồi phục)",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Rụng tóc (phổ biến)",
            "Buồn nôn, nôn",
            "Loét miệng",
            "Da đỏ, đau khi truyền (extravasation - nguy hiểm)",
            "Nước tiểu đỏ (bình thường, không phải máu)",
            "Vô sinh"
        ],
        "interactions": [
            "Cyclophosphamide: tăng độc tim",
            "Trastuzumab: tăng độc tim",
            "Paclitaxel: có thể tăng độc tính",
            "Các anthracyclines khác: tăng độc tim"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Granisetron": {
        "group": "Oncology - Anti-emetic (5-HT3 Antagonist)",
        "vietnamese_name": "Granisetron, Kytril",
        "administration": ["PO", "IV"],
        "indications": [
            "Phòng và điều trị nôn do hóa trị",
            "Phòng nôn sau phẫu thuật",
            "Nôn do xạ trị"
        ],
        "contraindications": [
            "Dị ứng granisetron hoặc 5-HT3 antagonists"
        ],
        "dosage": {
            "adult_iv": "1mg IV x 1 lần trước hóa trị hoặc 0.01mg/kg IV",
            "adult_po": "1-2mg PO x 1 lần trước hóa trị, có thể lặp lại sau 12 giờ",
            "adult_prevention": "1-2mg PO x 1-2 lần/ngày",
            "notes": "Có thể dùng 30 phút - 1 giờ trước hóa trị"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau đầu (phổ biến)",
            "Táo bón",
            "Chóng mặt",
            "Mệt mỏi",
            "Tăng transaminase (hiếm)",
            "QT kéo dài (hiếm)"
        ],
        "interactions": [
            "Apomorphine: chống chỉ định (tăng tác dụng)",
            "Các 5-HT3 antagonists khác: không nên dùng đồng thời"
        ],
        "pregnancy": "B - Thận trọng"
    },
    
    "Palonosetron": {
        "group": "Oncology - Anti-emetic (5-HT3 Antagonist)",
        "vietnamese_name": "Palonosetron, Aloxi",
        "administration": ["IV"],
        "indications": [
            "Phòng nôn do hóa trị (ngắn và trung hạn)",
            "Phòng nôn sau phẫu thuật"
        ],
        "contraindications": [
            "Dị ứng palonosetron hoặc 5-HT3 antagonists"
        ],
        "dosage": {
            "adult_chemotherapy": "0.25mg IV x 1 lần trước hóa trị",
            "adult_surgery": "0.075mg IV x 1 lần trước gây mê",
            "notes": "Tác dụng dài (48-72 giờ), chỉ cần 1 liều"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau đầu",
            "Táo bón",
            "Chóng mặt",
            "Mệt mỏi",
            "QT kéo dài (hiếm)"
        ],
        "interactions": [
            "Apomorphine: chống chỉ định"
        ],
        "pregnancy": "B - Thận trọng"
    },
    
    # ========== PEDIATRIC-SPECIFIC ==========
    
    "Amoxicillin-clavulanate": {
        "group": "Antibiotic - Beta-lactam (Penicillin + Beta-lactamase inhibitor)",
        "vietnamese_name": "Amoxicillin-clavulanate, Augmentin, Amoclav",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp trên/dưới",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da mô mềm",
            "Nhiễm khuẩn răng miệng",
            "Nhiễm khuẩn tai mũi họng (trẻ em)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Viêm gan do amoxicillin-clavulanate trước đây",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "adult_po": "875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày",
            "pediatric_po_suspension": "20-40mg amoxicillin/kg/ngày chia 2-3 lần (tối đa 875mg/125mg)",
            "pediatric_po_tablet": "25-45mg amoxicillin/kg/ngày chia 2 lần (trên 40kg: dùng liều người lớn)",
            "adult_iv": "1000/200mg IV mỗi 8 giờ",
            "pediatric_iv": "90mg amoxicillin/kg/ngày chia 3 lần (tối đa 1000/200mg mỗi 8 giờ)",
            "notes": "Có dạng suspension cho trẻ em. Uống với thức ăn để giảm tiêu chảy"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều hoặc tăng khoảng cách",
            "under_30": "Liều thấp hơn, khoảng cách dài hơn"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn",
            "Phát ban",
            "Viêm gan (hiếm nhưng nguy hiểm)",
            "Nhiễm trùng nấm Candida"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Methotrexate: tăng độc tính methotrexate",
            "Allopurinol: tăng nguy cơ phát ban",
            "Thuốc tránh thai: có thể giảm hiệu quả"
        ],
        "pregnancy": "B - An toàn"
    },
    
    "Paracetamol": {
        "group": "Analgesic/Antipyretic",
        "vietnamese_name": "Paracetamol, Acetaminophen, Tylenol, Efferalgan",
        "administration": ["PO", "IV", "PR"],
        "indications": [
            "Sốt",
            "Đau nhẹ đến trung bình",
            "Đau đầu",
            "Đau cơ",
            "Đau răng"
        ],
        "contraindications": [
            "Dị ứng paracetamol",
            "Suy gan nặng",
            "Bệnh gan tiến triển"
        ],
        "dosage": {
            "adult_po": "500-1000mg x 3-4 lần/ngày (tối đa 4g/ngày)",
            "adult_iv": "1000mg IV mỗi 6 giờ (tối đa 4g/ngày)",
            "pediatric_po": "10-15mg/kg x 3-4 lần/ngày (tối đa 60mg/kg/ngày)",
            "pediatric_iv": "15mg/kg IV mỗi 6 giờ (tối đa 60mg/kg/ngày)",
            "pediatric_pr": "15-20mg/kg PR mỗi 6 giờ (khi không uống được)",
            "notes": "Liều tối đa: Người lớn 4g/ngày, Trẻ em 60mg/kg/ngày. Quá liều gây độc gan nghiêm trọng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Khoảng cách 6-8 giờ"
        },
        "side_effects": [
            "Hiếm khi có tác dụng phụ ở liều điều trị",
            "Độc gan (với liều quá cao - >150mg/kg)",
            "Phát ban (hiếm)",
            "Giảm bạch cầu (rất hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu (với liều cao kéo dài)",
            "Isoniazid: tăng nguy cơ độc gan",
            "Alcohol: tăng nguy cơ độc gan",
            "Phenytoin/Carbamazepine: tăng nguy cơ độc gan"
        ],
        "pregnancy": "C - An toàn (dùng được trong thai kỳ)"
    },
    
    "Ibuprofen": {
        "group": "Analgesic/Antipyretic/NSAID",
        "vietnamese_name": "Ibuprofen, Brufen, Advil",
        "administration": ["PO", "IV"],
        "indications": [
            "Sốt",
            "Đau nhẹ đến trung bình",
            "Viêm khớp",
            "Đau bụng kinh",
            "Đau đầu"
        ],
        "contraindications": [
            "Dị ứng NSAID",
            "Loét dạ dày tá tràng hoạt động",
            "Suy thận nặng",
            "Suy tim nặng",
            "Có thai (3 tháng cuối)",
            "Trẻ em <6 tháng"
        ],
        "dosage": {
            "adult_po": "200-400mg x 3-4 lần/ngày (tối đa 2.4g/ngày)",
            "adult_iv": "400-800mg IV mỗi 6 giờ",
            "pediatric_po": "5-10mg/kg x 3-4 lần/ngày (tối đa 40mg/kg/ngày)",
            "pediatric_suspension": "Có dạng suspension 100mg/5ml cho trẻ em",
            "notes": "Uống với thức ăn để giảm kích ứng dạ dày. Không dùng quá 10 ngày không có chỉ định"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Không dùng hoặc giảm liều đáng kể"
        },
        "side_effects": [
            "Kích ứng dạ dày",
            "Đau đầu",
            "Chóng mặt",
            "Tăng nguy cơ tim mạch (với dùng lâu dài)",
            "Suy thận cấp (hiếm)",
            "Phát ban"
        ],
        "interactions": [
            "Aspirin: có thể giảm hiệu quả aspirin",
            "Warfarin: tăng nguy cơ chảy máu",
            "Lithium: tăng nồng độ lithium",
            "Methotrexate: tăng độc tính",
            "ACE inhibitors: giảm hiệu quả"
        ],
        "pregnancy": "C - Tránh dùng trong 3 tháng cuối (D)"
    },
    
    "Salbutamol": {
        "group": "Respiratory - Beta-2 Agonist (Short-acting)",
        "vietnamese_name": "Salbutamol, Albuterol, Ventolin, Salbutamol",
        "administration": ["INH", "IV", "PO", "NEB"],
        "indications": [
            "Hen phế quản",
            "COPD",
            "Co thắt phế quản",
            "Phòng co thắt phế quản do gắng sức",
            "Cấp cứu hen (nebulizer/IV)"
        ],
        "contraindications": [
            "Dị ứng salbutamol",
            "Nhịp tim nhanh nặng",
            "Rối loạn nhịp tim nặng",
            "Cường giáp"
        ],
        "dosage": {
            "adult_inh": "1-2 puff (100-200mcg) x 4 lần/ngày hoặc khi cần (tối đa 8-12 puff/ngày)",
            "adult_neb": "2.5-5mg nebulizer mỗi 4-6 giờ",
            "adult_iv": "5mcg/kg IV bolus, sau đó 0.5-5mcg/kg/phút",
            "pediatric_inh": "1-2 puff (100-200mcg) x 4 lần/ngày (trên 4 tuổi)",
            "pediatric_neb": "0.15mg/kg (tối thiểu 1.25mg) nebulizer mỗi 4-6 giờ",
            "pediatric_po_syrup": "0.1-0.15mg/kg x 3 lần/ngày (tối đa 2-4mg x 3 lần/ngày)",
            "notes": "Có dạng syrup và nebulizer cho trẻ em. Dùng khi cần cho cơn cấp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Run tay (phổ biến)",
            "Tim đập nhanh",
            "Đánh trống ngực",
            "Đau đầu",
            "Chóng mặt",
            "Hạ kali máu (với liều cao)",
            "Kích động"
        ],
        "interactions": [
            "Beta-blockers: đối kháng tác dụng",
            "Digoxin: có thể tăng nguy cơ loạn nhịp",
            "Diuretics: tăng nguy cơ hạ kali máu",
            "MAOIs: thận trọng"
        ],
        "pregnancy": "C - An toàn"
    },
    
    "Budesonide": {
        "group": "Respiratory - Corticosteroid (Inhaled)",
        "vietnamese_name": "Budesonide inhaled, Pulmicort",
        "administration": ["INH", "NEB"],
        "indications": [
            "Hen phế quản (duy trì)",
            "COPD",
            "Viêm mũi dị ứng",
            "Hen phế quản (trẻ em)"
        ],
        "contraindications": [
            "Dị ứng budesonide",
            "Nhiễm trùng đường hô hấp không điều trị"
        ],
        "dosage": {
            "adult_inh": "200-800mcg x 2 lần/ngày",
            "adult_neb": "0.5-1mg nebulizer x 2 lần/ngày",
            "pediatric_inh": "100-400mcg x 2 lần/ngày (theo tuổi)",
            "pediatric_neb": "0.25-0.5mg nebulizer x 2 lần/ngày",
            "notes": "Súc miệng sau khi dùng để tránh nấm miệng. Có dạng nebulizer cho trẻ em"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nấm miệng (candida - phổ biến nếu không súc miệng)",
            "Khàn tiếng",
            "Ho",
            "Kích ứng họng",
            "Tác dụng toàn thân (hiếm với liều thường)"
        ],
        "interactions": [
            "Ketoconazole/Itraconazole: tăng nồng độ budesonide",
            "Ritonavir: tăng nồng độ budesonide"
        ],
        "pregnancy": "C - An toàn"
    },
    
    "Amoxicillin suspension": {
        "group": "Antibiotic - Beta-lactam (Penicillin)",
        "vietnamese_name": "Amoxicillin suspension, Amoxicillin sirô",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn tai mũi họng",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da mô mềm",
            "Helicobacter pylori (phối hợp)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "pediatric_otitis": "80-90mg/kg/ngày chia 2 lần (10 ngày)",
            "pediatric_pneumonia": "80-100mg/kg/ngày chia 3-4 lần",
            "pediatric_uti": "25-50mg/kg/ngày chia 3 lần",
            "pediatric_suspension_common": "20-40mg/kg/ngày chia 2-3 lần",
            "notes": "Có dạng suspension 125mg/5ml, 250mg/5ml cho trẻ em. Uống với hoặc không thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều hoặc tăng khoảng cách",
            "under_30": "Liều thấp hơn, khoảng cách dài hơn"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn",
            "Phát ban",
            "Nhiễm trùng nấm Candida",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Methotrexate: tăng độc tính",
            "Allopurinol: tăng nguy cơ phát ban",
            "Thuốc tránh thai: có thể giảm hiệu quả"
        ],
        "pregnancy": "B - An toàn"
    },
    
    # ========== EMERGENCY / ACLS ==========
    
    "Epinephrine": {
        "group": "Emergency - Catecholamine (Alpha & Beta Agonist)",
        "vietnamese_name": "Epinephrine, Adrenaline",
        "administration": ["IV", "IM", "SC", "INH", "IT"],
        "indications": [
            "Ngừng tim (cardiac arrest)",
            "Sốc phản vệ (anaphylaxis)",
            "Sốc (shock)",
            "Cơn hen nặng (IV/nebulizer)",
            "Co thắt thanh quản"
        ],
        "contraindications": [
            "Không có trong cấp cứu ngừng tim",
            "Sốc phản vệ: không có chống chỉ định tuyệt đối"
        ],
        "dosage": {
            "adult_cardiac_arrest_iv": "1mg IV mỗi 3-5 phút (hoặc 0.1mg/kg)",
            "adult_cardiac_arrest_it": "2-2.5mg IT",
            "adult_anaphylaxis_im": "0.3-0.5mg IM (0.3-0.5ml 1:1000) ở đùi ngoài",
            "adult_anaphylaxis_iv": "0.1-0.25mg IV bolus (pha 1mg trong 10ml = 0.1mg/ml)",
            "adult_shock": "0.1-2mcg/kg/phút IV infusion",
            "pediatric_cardiac_arrest": "0.01mg/kg (0.1ml/kg 1:10000) IV/IT mỗi 3-5 phút",
            "pediatric_anaphylaxis_im": "0.01mg/kg IM (0.01ml/kg 1:1000) ở đùi ngoài (tối đa 0.5mg)",
            "notes": "1:1000 = 1mg/ml (dùng IM/SC), 1:10000 = 0.1mg/ml (dùng IV). Đùi ngoài cho anaphylaxis"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tim đập nhanh",
            "Tăng huyết áp",
            "Lo lắng, run tay",
            "Đau đầu",
            "Nhồi máu cơ tim (với liều cao)",
            "Rối loạn nhịp tim",
            "Hoại tử (nếu tiêm ngoài mạch)"
        ],
        "interactions": [
            "Beta-blockers: đối kháng tác dụng",
            "MAOIs: tăng tác dụng",
            "Tricyclic antidepressants: tăng tác dụng",
            "Digoxin: tăng nguy cơ loạn nhịp"
        ],
        "pregnancy": "C - An toàn trong cấp cứu"
    },
    
    "Atropine": {
        "group": "Emergency - Anticholinergic",
        "vietnamese_name": "Atropine",
        "administration": ["IV", "IM", "IO", "IT"],
        "indications": [
            "Nhịp tim chậm có triệu chứng",
            "Block nhĩ thất",
            "Quá liều organophosphate",
            "Chuẩn bị phẫu thuật (giảm tiết)",
            "Ngừng tim với nhịp chậm/PEA"
        ],
        "contraindications": [
            "Glaucoma góc đóng",
            "Tắc nghẽn đường tiểu",
            "Nhịp tim nhanh",
            "Sốt"
        ],
        "dosage": {
            "adult_bradycardia": "0.5-1mg IV mỗi 3-5 phút (tối đa 3mg)",
            "adult_cardiac_arrest": "1mg IV/IT, lặp lại mỗi 3-5 phút",
            "adult_organophosphate": "2-5mg IV, lặp lại đến khi đạt tác dụng",
            "pediatric_bradycardia": "0.02mg/kg IV (tối thiểu 0.1mg, tối đa 0.5mg)",
            "pediatric_cardiac_arrest": "0.02mg/kg IV/IT (tối thiểu 0.1mg)",
            "notes": "Liều tối thiểu người lớn 0.5mg để tránh nhịp tim chậm nghịch lý"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nhịp tim nhanh",
            "Khô miệng",
            "Giãn đồng tử",
            "Táo bón",
            "Bí tiểu",
            "Lú lẫn (người già)",
            "Tăng nhãn áp"
        ],
        "interactions": [
            "Các anticholinergics khác: tăng tác dụng",
            "Digoxin: có thể tăng nồng độ digoxin"
        ],
        "pregnancy": "C - An toàn"
    },
    
    "Amiodarone": {
        "group": "Emergency - Antiarrhythmic (Class III)",
        "vietnamese_name": "Amiodarone, Cordarone",
        "administration": ["IV", "PO"],
        "indications": [
            "Rung thất / Nhịp nhanh thất không có mạch (cardiac arrest)",
            "Rối loạn nhịp thất",
            "Rung nhĩ / Cuồng nhĩ",
            "Nhịp nhanh trên thất"
        ],
        "contraindications": [
            "Dị ứng amiodarone",
            "Block nhĩ thất độ 2-3 (không có máy tạo nhịp)",
            "Nhịp tim chậm nặng",
            "Cường giáp",
            "Bệnh phổi nặng",
            "Có thai (3 tháng đầu)"
        ],
        "dosage": {
            "adult_cardiac_arrest_vfvt": "300mg IV bolus, sau đó 150mg IV, có thể lặp lại",
            "adult_vt_with_pulse": "150mg IV trong 10 phút, sau đó 1mg/phút x 6 giờ, sau đó 0.5mg/phút",
            "adult_po_loading": "800-1600mg/ngày chia 2 lần x 1-2 tuần",
            "adult_po_maintenance": "200-400mg/ngày x 1 lần",
            "pediatric_arrest": "5mg/kg IV bolus",
            "notes": "Tác dụng kéo dài. Theo dõi chức năng phổi, gan, tuyến giáp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Độc phổi (viêm phổi kẽ - nghiêm trọng)",
            "Độc gan (tăng transaminase)",
            "Rối loạn chức năng tuyến giáp (cường/ức chế)",
            "Rối loạn nhịp tim (hiếm)",
            "Độc thần kinh (viêm dây thần kinh)",
            "Phát ban (nhạy cảm ánh sáng)",
            "Tăng transaminase"
        ],
        "interactions": [
            "Digoxin: tăng nồng độ digoxin",
            "Warfarin: tăng INR",
            "Phenytoin: tăng nồng độ phenytoin",
            "Beta-blockers: tăng nguy cơ nhịp chậm",
            "Statins: tăng nguy cơ độc cơ"
        ],
        "pregnancy": "D - Tránh dùng"
    },
    
    "Lidocaine": {
        "group": "Emergency - Local Anesthetic / Antiarrhythmic (Class IB)",
        "vietnamese_name": "Lidocaine, Xylocaine",
        "administration": ["IV", "IO", "IT"],
        "indications": [
            "Rung thất / Nhịp nhanh thất không có mạch (khi không có amiodarone)",
            "Rối loạn nhịp thất",
            "Gây tê tại chỗ",
            "Gây tê vùng"
        ],
        "contraindications": [
            "Dị ứng lidocaine",
            "Block nhĩ thất độ 2-3 (không có máy tạo nhịp)",
            "Hội chứng Adams-Stokes",
            "Rối loạn nhịp nặng"
        ],
        "dosage": {
            "adult_cardiac_arrest": "1-1.5mg/kg IV bolus, lặp lại 0.5-0.75mg/kg mỗi 5-10 phút (tối đa 3mg/kg)",
            "adult_vt_with_pulse": "1-1.5mg/kg IV bolus, sau đó 1-4mg/phút IV infusion",
            "pediatric_arrest": "1mg/kg IV/IO bolus",
            "pediatric_infusion": "20-50mcg/kg/phút IV",
            "notes": "Giảm liều ở suy tim, suy gan, người già. Theo dõi co giật, độc thần kinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Độc thần kinh trung ương (co giật, lú lẫn, ngừng thở - với liều cao)",
            "Rối loạn nhịp tim",
            "Hạ huyết áp",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Beta-blockers: giảm chuyển hóa lidocaine",
            "Cimetidine: tăng nồng độ lidocaine",
            "Phenytoin: tăng độc tính"
        ],
        "pregnancy": "B - An toàn"
    },
    
    "Adenosine": {
        "group": "Emergency - Antiarrhythmic",
        "vietnamese_name": "Adenosine",
        "administration": ["IV", "IO"],
        "indications": [
            "Nhịp nhanh trên thất (SVT) - cấp cứu",
            "Chẩn đoán rối loạn nhịp",
            "Cuồng nhĩ"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3 (không có máy tạo nhịp)",
            "Hội chứng sick sinus",
            "Hen phế quản nặng",
            "Dị ứng adenosine"
        ],
        "dosage": {
            "adult_svt_first": "6mg IV bolus nhanh (1-2 giây) + flush nhanh 20ml NS",
            "adult_svt_second": "12mg IV nếu không đáp ứng (có thể lặp lại 1 lần)",
            "adult_max": "12mg (tối đa)",
            "pediatric_svt_first": "0.1mg/kg IV (tối đa 6mg)",
            "pediatric_svt_second": "0.2mg/kg IV nếu không đáp ứng (tối đa 12mg)",
            "notes": "Phải tiêm bolus nhanh (1-2 giây) và flush ngay 20ml. Có thể gây ngừng tim tạm thời"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Ngừng tim tạm thời (thường <10 giây - bình thường)",
            "Cảm giác khó chịu ở ngực",
            "Khó thở",
            "Đỏ mặt",
            "Chóng mặt",
            "Loạn nhịp (thoáng qua)"
        ],
        "interactions": [
            "Theophylline/Caffeine: đối kháng tác dụng",
            "Dipyridamole: tăng tác dụng",
            "Carbamazepine: tăng tác dụng"
        ],
        "pregnancy": "C - An toàn"
    },
    
    "Naloxone": {
        "group": "Emergency - Opioid Antagonist",
        "vietnamese_name": "Naloxone, Narcan",
        "administration": ["IV", "IM", "SC", "INH", "IO"],
        "indications": [
            "Quá liều opioid (nghiện)",
            "Ngộ độc opioid",
            "Đảo ngược tác dụng opioid sau phẫu thuật",
            "Đảo ngược tác dụng opioid trong ICU"
        ],
        "contraindications": [
            "Dị ứng naloxone"
        ],
        "dosage": {
            "adult_overdose": "0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút đến khi đáp ứng",
            "adult_reversal": "0.04-0.4mg IV titrate đến khi đáp ứng",
            "adult_infusion": "0.25-6.25mcg/kg/giờ IV (nếu cần duy trì)",
            "pediatric_overdose": "0.01mg/kg IV/IM/IO, lặp lại đến khi đáp ứng",
            "pediatric_infusion": "2.5-10mcg/kg/giờ IV",
            "notes": "Tác dụng ngắn (20-90 phút), có thể cần lặp lại hoặc infusion. Theo dõi hội chứng cai"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Hội chứng cai opioid (nếu bệnh nhân nghiện)",
            "Hạ huyết áp",
            "Rối loạn nhịp tim",
            "Co giật (hiếm)",
            "Phù phổi (hiếm)"
        ],
        "interactions": [
            "Opioids: đảo ngược tác dụng"
        ],
        "pregnancy": "C - An toàn"
    },
    
    "Flumazenil": {
        "group": "Emergency - Benzodiazepine Antagonist",
        "vietnamese_name": "Flumazenil, Anexate",
        "administration": ["IV"],
        "indications": [
            "Quá liều benzodiazepine",
            "Đảo ngược tác dụng benzodiazepine sau phẫu thuật",
            "Quá liều zolpidem/zopiclone"
        ],
        "contraindications": [
            "Dị ứng flumazenil",
            "Động kinh (đang điều trị với benzodiazepine)",
            "Quá liều tricyclic antidepressants",
            "Phụ thuộc benzodiazepine lâu dài"
        ],
        "dosage": {
            "adult_overdose": "0.2mg IV, lặp lại 0.2mg mỗi 1 phút đến khi đáp ứng (tối đa 1mg)",
            "adult_reversal": "0.1-0.2mg IV titrate đến khi đáp ứng",
            "pediatric": "0.01mg/kg IV (tối đa 0.2mg), lặp lại đến khi đáp ứng",
            "notes": "Tác dụng ngắn (30-60 phút), có thể cần lặp lại. Nguy cơ co giật ở bệnh nhân động kinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Co giật (nguy hiểm ở bệnh nhân động kinh)",
            "Hội chứng cai benzodiazepine",
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Lo lắng",
            "Rối loạn nhịp tim"
        ],
        "interactions": [
            "Benzodiazepines: đảo ngược tác dụng",
            "Tricyclic antidepressants: tăng nguy cơ co giật"
        ],
        "pregnancy": "C - Thận trọng"
    },
    
    # ========== GAP FILLING ==========
    
    "Rosuvastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Rosuvastatin, Crestor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Phòng ngừa biến cố tim mạch",
            "Hội chứng chuyển hóa"
        ],
        "contraindications": [
            "Dị ứng rosuvastatin",
            "Bệnh gan hoạt động",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_start": "5-10mg x 1 lần/ngày (tối)",
            "adult_usual": "10-20mg x 1 lần/ngày",
            "adult_max": "40mg x 1 lần/ngày",
            "notes": "Uống với hoặc không thức ăn. Mạnh hơn atorvastatin ở liều tương đương"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Bắt đầu với 5mg/ngày"
        },
        "side_effects": [
            "Đau cơ, yếu cơ",
            "Tăng transaminase",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Đau đầu",
            "Táo bón",
            "Đái tháo đường (nguy cơ tăng nhẹ)"
        ],
        "interactions": [
            "Cyclosporine: tăng nguy cơ độc tính",
            "Gemfibrozil: tăng nguy cơ độc cơ",
            "Warfarin: tăng INR",
            "Rifampin: giảm nồng độ rosuvastatin"
        ],
        "pregnancy": "X - Chống chỉ định"
    },
    
    "Enalaprilat": {
        "group": "Cardiovascular - ACE Inhibitor (IV)",
        "vietnamese_name": "Enalaprilat, Enalapril IV",
        "administration": ["IV"],
        "indications": [
            "Tăng huyết áp cấp cứu",
            "Suy tim cấp",
            "Khi không uống được"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "0.625-1.25mg IV mỗi 6 giờ",
            "adult_heart_failure": "0.625mg IV mỗi 6 giờ, tăng dần đến 1.25mg mỗi 6 giờ",
            "notes": "Khởi đầu với liều thấp, theo dõi huyết áp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Thận trọng, giảm liều 50%"
        },
        "side_effects": [
            "Hạ huyết áp (phổ biến)",
            "Ho khan",
            "Tăng kali máu",
            "Phù mạch",
            "Suy thận cấp"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "Diuretics: tăng nguy cơ hạ huyết áp",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D - Chống chỉ định"
    },
    
    "Ceftriaxone": {
        "group": "Antibiotic - Cephalosporin (3rd Generation)",
        "vietnamese_name": "Ceftriaxone, Rocephin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn nặng",
            "Viêm màng não",
            "Nhiễm khuẩn bệnh viện",
            "Nhiễm khuẩn đường tiết niệu",
            "Viêm phổi"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Trẻ sơ sinh <28 ngày với Ca IV"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM mỗi 24 giờ",
            "adult_severe": "2-4g IV mỗi 24 giờ",
            "adult_meningitis": "2g IV mỗi 12 giờ",
            "pediatric_standard": "50-75mg/kg IV/IM mỗi 24 giờ (tối đa 2g)",
            "pediatric_meningitis": "80-100mg/kg IV mỗi 12-24 giờ (tối đa 4g/ngày)",
            "notes": "Thời gian bán hủy dài, dùng 1 lần/ngày. Có thể gây kết tủa với Ca ở trẻ sơ sinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua mật)",
            "under_30": "Giảm liều nếu CrCl <10 và suy gan"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Tăng transaminase",
            "Viêm túi mật (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Sỏi mật (với liều cao dài ngày)"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Calcium IV: kết tủa (trẻ sơ sinh)",
            "Probenecid: tăng nồng độ ceftriaxone"
        ],
        "pregnancy": "B - An toàn"
    },
    
    "Ciprofloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Ciprofloxacin, Cipro",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường tiêu hóa",
            "Nhiễm khuẩn da mô mềm",
            "Nhiễm khuẩn xương khớp",
            "Viêm phổi (một số loại)"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Có thai",
            "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_uti": "250-500mg PO x 2 lần/ngày",
            "adult_uti_complicated": "500-750mg PO x 2 lần/ngày",
            "adult_iv": "200-400mg IV mỗi 12 giờ",
            "adult_severe": "400mg IV mỗi 8 giờ",
            "notes": "Uống cách xa antacid 2 giờ. Không dùng với sữa"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Đau gân, viêm gân (có thể đứt gân)",
            "QT kéo dài",
            "Co giật (hiếm)",
            "Nhạy cảm ánh sáng",
            "Rối loạn tâm thần (hiếm)"
        ],
        "interactions": [
            "Antacid: giảm hấp thu",
            "Warfarin: tăng INR",
            "Theophylline: tăng nồng độ theophylline",
            "Probenecid: tăng nồng độ ciprofloxacin"
        ],
        "pregnancy": "C - Tránh dùng"
    },
    
    "Metoclopramide": {
        "group": "Gastrointestinal - Prokinetic / Anti-emetic",
        "vietnamese_name": "Metoclopramide, Primperan, Reglan",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Buồn nôn, nôn",
            "Liệt dạ dày (gastroparesis)",
            "Trào ngược dạ dày thực quản",
            "Chậm làm rỗng dạ dày"
        ],
        "contraindications": [
            "Dị ứng metoclopramide",
            "Xuất huyết tiêu hóa",
            "Tắc ruột",
            "Pheochromocytoma",
            "Động kinh"
        ],
        "dosage": {
            "adult_po": "10mg x 3-4 lần/ngày (trước ăn 30 phút)",
            "adult_iv_im": "10mg IV/IM x 3-4 lần/ngày",
            "adult_severe": "10-20mg IV mỗi 6-8 giờ",
            "pediatric": "0.1-0.15mg/kg PO/IV x 3-4 lần/ngày",
            "notes": "Không dùng >12 tuần. Nguy cơ rối loạn vận động ngoại tháp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Rối loạn vận động ngoại tháp (dystonia, akathisia - phổ biến)",
            "Buồn ngủ",
            "Chóng mặt",
            "Rối loạn vận động muộn (tardive dyskinesia - hiếm nhưng không hồi phục)",
            "Tăng prolactin",
            "Rối loạn nhịp tim"
        ],
        "interactions": [
            "Phenothiazines: tăng nguy cơ rối loạn vận động",
            "Anticholinergics: đối kháng tác dụng",
            "Dopamine antagonists: tăng tác dụng"
        ],
        "pregnancy": "B - An toàn (tránh dùng trong 3 tháng đầu)"
    },
}

# Drug groups for filtering
DRUG_GROUPS = {
    "Cardiovascular": [
        "Captopril", "Enalapril", "Enalaprilat", "Lisinopril", "Losartan",
        "Metoprolol", "Propranolol", "Amlodipine", "Nifedipine", "Diltiazem", "Verapamil",
        "Furosemide", "Hydrochlorothiazide",
        "Amiodarone", "Digoxin",
        "Warfarin", "Aspirin", "Clopidogrel", "Ticagrelor", "Prasugrel", "Ticlopidine", "Dipyridamole",
        "Atorvastatin", "Simvastatin", "Rosuvastatin",
        "Isosorbide mononitrate"
    ],
    "Diabetes": [
        "Metformin", "Glibenclamide", "Gliclazide", "Insulin",
        "Empagliflozin", "Dapagliflozin", "Sitagliptin", "Vildagliptin", "Pioglitazone"
    ],
    "Gastrointestinal": [
        "Omeprazole", "Pantoprazole", "Ranitidine",
        "Metoclopramide", "Loperamide",
        "Domperidone", "Ondansetron", "Lansoprazole", "Esomeprazole", "Sucralfate"
    ],
    "Oncology": [
        "Cisplatin", "Carboplatin", "Oxaliplatin",
        "5-Fluorouracil", "Methotrexate",
        "Cyclophosphamide", "Ifosfamide",
        "Doxorubicin",
        "Granisetron", "Palonosetron"
    ],
    "Emergency": [
        "Epinephrine", "Atropine",
        "Amiodarone", "Lidocaine", "Adenosine",
        "Naloxone", "Flumazenil"
    ],
    "Antibiotics": [
        "Amoxicillin-clavulanate", "Amoxicillin suspension",
        "Ceftriaxone", "Ciprofloxacin"
    ],
    "Pediatric": [
        "Amoxicillin-clavulanate", "Amoxicillin suspension",
        "Paracetamol", "Ibuprofen",
        "Salbutamol", "Budesonide"
    ],
    "Analgesics": [
        "Paracetamol", "Ibuprofen", "Tramadol",
        "Naproxen", "Diclofenac", "Morphine", "Codeine", "Sumatriptan"
    ],
    "Respiratory": [
        "Salbutamol", "Salmeterol", "Ipratropium", "Tiotropium",
        "Budesonide inhaled", "Fluticasone inhaled"
    ],
    "Neurology/Psychiatry": [
        "Carbamazepine", "Fluoxetine", "Sertraline", "Citalopram", "Escitalopram", "Venlafaxine", "Amitriptyline",
        "Phenytoin", "Valproate", "Levetiracetam", "Lamotrigine", "Gabapentin", "Pregabalin"
    ],
    "Allergy": [
        "Loratadine", "Cetirizine", "Fexofenadine", "Desloratadine", "Levocetirizine"
    ],
    "Vitamins/Supplements": [
        "Vitamin D", "Vitamin B12", "Folic acid", "Iron", "Calcium"
    ],
    "Anti-infectives": [
        "Chloroquine", "Artesunate", "Albendazole", "Mebendazole"
    ],
    "Endocrinology": [
        "Levothyroxine", "Methimazole", "Propylthiouracil", "Prednisone"
    ],
    "Other": [
        "Allopurinol", "Prednisolone"
    ]
}

# Total count
TOTAL_DRUGS = len(DRUG_DATABASE)

