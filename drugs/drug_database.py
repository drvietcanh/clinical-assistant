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
        "pregnancy": "D - Chống chỉ định trong thai kỳ",
        "mechanism_of_action": "Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp, tăng dần",
            "Uống 1 giờ trước bữa ăn (giảm hấp thu nếu dùng với thức ăn)",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)",
            "Ho khan có thể kéo dài, thường tự hết khi ngừng thuốc"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ (ngắn)",
            "onset": "15-30 phút",
            "duration": "6-12 giờ",
            "protein_binding": "25-30%",
            "clearance": "Thận (50-75%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng"
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
        "pregnancy": "D",
        "mechanism_of_action": "Enalapril là prodrug, chuyển hóa thành enalaprilat (hoạt chất) trong gan. Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (2.5-5mg), tăng dần",
            "Có thể dùng 1-2 lần/ngày (khác với captopril 2-3 lần/ngày)",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)",
            "Ít tác dụng phụ hơn captopril, nhưng vẫn có thể gây ho khan"
        ],
        "pharmacokinetics": {
            "half_life": "Enalapril: 11 giờ; Enalaprilat: 30-35 giờ (dài)",
            "onset": "1 giờ (PO), 15 phút (enalaprilat IV)",
            "duration": "12-24 giờ",
            "protein_binding": "50-60%",
            "clearance": "Thận (60%), một phần qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng"
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
        "pregnancy": "D",
        "mechanism_of_action": "Ức chế angiotensin converting enzyme (ACE), giảm chuyển angiotensin I thành angiotensin II, giảm aldosterone, gây giãn mạch và giảm huyết áp. Không phải prodrug (khác với enalapril), tác dụng trực tiếp",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ",
            "Huyết áp",
            "Ho khan (tác dụng phụ thường gặp)",
            "Dấu hiệu phù mạch (sưng mặt, lưỡi, họng - cấp cứu)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (5-10mg), tăng dần",
            "Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn)",
            "Không phải prodrug nên tác dụng nhanh hơn enalapril",
            "Theo dõi sát creatinine khi bắt đầu (có thể tăng nhẹ)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (có thể nguy hiểm tính mạng)"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ (dài)",
            "onset": "1 giờ",
            "duration": "24 giờ (dài nhất trong các ACE inhibitor)",
            "protein_binding": "25%",
            "clearance": "Thận (100%), không chuyển hóa qua gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Phù mạch có thể đe dọa tính mạng"
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
        "pregnancy": "D",
        "mechanism_of_action": "Losartan là prodrug, chuyển hóa thành EXP-3174 (hoạt chất) trong gan. Ức chế thụ thể angiotensin II type 1 (AT1), ngăn chặn tác dụng của angiotensin II (giãn mạch, giảm aldosterone). Ít gây ho hơn ACE inhibitor vì không ảnh hưởng đến bradykinin",
        "monitoring": [
            "Creatinine, BUN sau 1-2 tuần khi bắt đầu",
            "Kali máu định kỳ (ít hơn ACE inhibitor)",
            "Huyết áp",
            "Ít phải theo dõi ho khan (không gây ho như ACE inhibitor)"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (25-50mg), tăng dần",
            "Ưu điểm: ít gây ho hơn ACE inhibitor (thay thế tốt cho bệnh nhân không dung nạp ACE inhibitor)",
            "Vẫn có thể gây tăng kali máu và suy thận cấp (nhưng ít hơn ACE inhibitor)",
            "Theo dõi sát creatinine khi bắt đầu",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Ngừng ngay nếu có phù mạch (hiếm hơn ACE inhibitor nhưng vẫn có thể xảy ra)"
        ],
        "pharmacokinetics": {
            "half_life": "Losartan: 2 giờ; EXP-3174 (active): 6-9 giờ",
            "onset": "1 giờ",
            "duration": "24 giờ",
            "protein_binding": "98.7%",
            "clearance": "Gan (chuyển hóa), thận (EXP-3174)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi"
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
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế thụ thể beta-1 chọn lọc, giảm nhịp tim, lực co bóp cơ tim, và dẫn truyền nhĩ thất",
        "monitoring": [
            "Huyết áp, nhịp tim mỗi lần khám",
            "ECG nếu có triệu chứng block nhĩ thất",
            "Đường huyết ở bệnh nhân đái tháo đường (che dấu triệu chứng hạ đường huyết)",
            "Chức năng gan, thận định kỳ"
        ],
        "precautions": [
            "Không ngừng đột ngột (có thể gây cơn tăng huyết áp phản hồi)",
            "Giảm liều từ từ khi ngừng",
            "Thận trọng với bệnh nhân hen/COPD (có thể gây co thắt phế quản)",
            "Theo dõi suy tim mới xuất hiện"
        ],
        "pharmacokinetics": {
            "half_life": "3-7 giờ (tartrate), 3-4 giờ (succinate)",
            "onset": "1-2 giờ (PO), 15 phút (IV)",
            "duration": "6-12 giờ (tartrate), 24 giờ (succinate)",
            "protein_binding": "12%",
            "clearance": "Gan (CYP2D6)"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Không ngừng đột ngột - có thể gây tăng huyết áp phản hồi, đau thắt ngực, nhồi máu cơ tim. Giảm liều từ từ trong 1-2 tuần. Suy tim cấp có thể xảy ra nếu dùng ở bệnh nhân suy tim không bù trừ"
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
          "pregnancy": "C",
          "mechanism_of_action": "Non-selective beta-adrenergic receptor blocker (beta1 và beta2). Ức chế tác dụng của catecholamines (epinephrine, norepinephrine), giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp, giảm nhu cầu oxy cơ tim. Ức chế renin-angiotensin system. Có tác dụng chống loạn nhịp (class II antiarrhythmic).",
          "monitoring": [
              "Nhịp tim và huyết áp (trước và sau khi bắt đầu)",
              "Dấu hiệu suy tim (khó thở, phù, tăng cân)",
              "Chức năng phổi (nếu có bệnh phổi tắc nghẽn)",
              "Đường huyết (đặc biệt ở bệnh nhân đái tháo đường - che dấu triệu chứng hạ đường huyết)",
              "Triệu chứng mệt mỏi, lạnh tay chân, rối loạn cương dương"
          ],
          "precautions": [
              "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng, nhồi máu cơ tim). Phải giảm liều dần trong 1-2 tuần",
              "Thận trọng ở bệnh nhân hen phế quản/COPD (có thể gây co thắt phế quản nặng)",
              "Tránh dùng trong suy tim cấp, block AV độ 2-3, nhịp tim chậm <50 bpm",
              "Thận trọng ở bệnh nhân đái tháo đường (che dấu triệu chứng hạ đường huyết)",
              "Có thể gây mệt mỏi, giảm khả năng tập luyện",
              "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)"
          ],
          "pharmacokinetics": {
              "half_life": "3-5 giờ (ngắn), nhưng tác dụng kéo dài hơn do tác dụng trên receptor",
              "onset": "1-2 giờ (PO)",
              "duration": "6-12 giờ",
              "protein_binding": "90-95%",
              "clearance": "Gan (extensive first-pass metabolism), CYP2D6, CYP1A2"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, rối loạn nhịp tim nặng. Phải giảm liều dần dần trong 1-2 tuần"
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
        "black_box_warnings": "Không có black box warning cụ thể. Thận trọng với bệnh nhân suy tim mất bù, hẹp van động mạch chủ nặng. Phù ngoại biên có thể xảy ra và thường không phản ánh suy tim"
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
        "black_box_warnings": "Dạng immediate-release KHÔNG được dùng để điều trị tăng huyết áp hoặc đau thắt ngực - có thể làm tăng nguy cơ nhồi máu cơ tim và tử vong. Chỉ dùng dạng extended-release cho các chỉ định này."

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
        "black_box_warnings": "Không có black box warning. Tuy nhiên, block nhĩ thất và nhịp tim chậm có thể nặng, đặc biệt khi dùng với beta-blockers. Suy tim có thể nặng lên. Không dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp)."

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
        "black_box_warnings": "Không có black box warning. Tuy nhiên, block nhĩ thất và nhịp tim chậm có thể nặng, đặc biệt khi dùng với beta-blockers. Suy tim có thể nặng lên. Không dùng ở block nhĩ thất độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp)."

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
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế đồng vận chuyển Na-K-2Cl ở quai Henle, tăng thải natri, kali, clo, và nước",
        "monitoring": [
            "Điện giải (K, Na, Cl) trước điều trị và định kỳ",
            "Cân bằng dịch vào-ra, cân nặng",
            "Creatinine, BUN",
            "Acid uric nếu dùng lâu dài",
            "Thính giác nếu IV liều cao hoặc suy thận"
        ],
        "precautions": [
            "Theo dõi sát điện giải, đặc biệt kali",
            "Bù kali nếu cần",
            "Tránh dùng quá liều (gây mất nước, suy thận)",
            "Thận trọng với bệnh nhân suy thận (có thể cần liều cao hơn)",
            "Tránh dùng IV liều cao ở bệnh nhân suy thận (nguy cơ điếc)"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ (PO), 1 giờ (IV)",
            "onset": "30-60 phút (PO), 5 phút (IV)",
            "duration": "6-8 giờ",
            "protein_binding": ">98%",
            "clearance": "Thận (50%) và gan"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Có thể gây mất nước và rối loạn điện giải nghiêm trọng. Điếc có thể xảy ra với liều IV cao hoặc dùng nhanh. Hạ kali máu có thể làm tăng nguy cơ ngộ độc digoxin và rối loạn nhịp tim"
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
          "pregnancy": "C",
          "mechanism_of_action": "Thiazide diuretic. Ức chế Na+/Cl- cotransporter ở đoạn xa của ống thận (distal convoluted tubule), tăng bài tiết Na+, Cl-, và nước, gây lợi tiểu. Giảm thể tích máu và giảm huyết áp. Tăng bài tiết K+, Mg2+, nhưng giữ lại Ca2+ (khác với loop diuretics).",
          "monitoring": [
              "Kali máu (mỗi 1-3 tháng, đặc biệt khi bắt đầu) - HCTZ gây hạ kali máu",
              "Natri máu - có thể gây hạ natri máu, đặc biệt ở người già",
              "Creatinine, BUN - có thể tăng nhẹ (không phải suy thận thật)",
              "Đường huyết - có thể tăng đường huyết, đặc biệt ở bệnh nhân đái tháo đường",
              "Acid uric - HCTZ gây tăng acid uric, có thể gây gout",
              "Lipid máu - có thể tăng cholesterol, triglycerides nhẹ",
              "Canxi máu - HCTZ có thể gây tăng canxi máu nhẹ (do giữ lại Ca2+)"
          ],
          "precautions": [
              "Liều thấp (12.5-25mg/ngày) đủ cho tăng huyết áp, ít tác dụng phụ hơn liều cao",
              "Thường cần bổ sung kali hoặc dùng với kali-sparing diuretic (spironolactone, amiloride)",
              "Thận trọng ở người già (tăng nguy cơ hạ natri máu)",
              "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
              "Thận trọng ở bệnh nhân gout (tăng acid uric)",
              "Tránh dùng với lithium (tăng nguy cơ độc tính lithium)",
              "Dị ứng sulfonamide - không dùng nếu dị ứng"
          ],
          "pharmacokinetics": {
              "half_life": "6-15 giờ",
              "onset": "2 giờ (PO)",
              "duration": "6-12 giờ",
              "protein_binding": "40-70%",
              "clearance": "Thận (không chuyển hóa, thải nguyên dạng)"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": ""
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
        "pregnancy": "D",
        "mechanism_of_action": "Class III antiarrhythmic (chủ yếu) với tác dụng bổ sung class I, II, IV. Chủ yếu ức chế kênh K+ (delayed rectifier), kéo dài phase 3 của action potential, kéo dài QT interval. Cũng có tác dụng ức chế Na+ channels (class I), chẹn beta (class II), và chẹn Ca2+ (class IV). Rất hiệu quả cho rối loạn nhịp nhưng có nhiều tác dụng phụ.",
        "monitoring": [
            "ECG: QT interval (kéo dài QT là bình thường, nhưng QT >500ms hoặc tăng >60ms nguy hiểm)",
            "Chức năng phổi: X-quang phổi, PFT (6 tháng/lần), đặc biệt chú ý dấu hiệu viêm phổi mô kẽ",
            "Chức năng gan: ALT, AST, bilirubin (mỗi 3-6 tháng)",
            "Chức năng tuyến giáp: TSH, FT4, FT3 (mỗi 6 tháng) - có thể gây cường giáp hoặc suy giáp",
            "Khám mắt: Soi đáy mắt (mỗi 6-12 tháng) - có thể gây viêm giác mạc, đục thủy tinh thể",
            "Da: Dấu hiệu nhạy cảm ánh sáng, xám da (blue-gray discoloration)",
            "Electrolytes: K+, Mg2+ (phải đảm bảo bình thường trước khi dùng)"
        ],
        "precautions": [
            "CẦN LOADING DOSE (thường 800-1600mg/ngày trong 1-2 tuần) trước khi dùng liều duy trì",
            "Tác dụng phụ nhiều và nghiêm trọng - chỉ dùng cho rối loạn nhịp đe dọa tính mạng hoặc không đáp ứng với thuốc khác",
            "Bắt buộc monitor chức năng phổi, gan, tuyến giáp, mắt định kỳ",
            "Tương tác thuốc rất nhiều - kiểm tra kỹ trước khi dùng",
            "Tránh dùng ở phụ nữ có thai (category D)",
            "Thời gian bán hủy rất dài (50-60 ngày) - tác dụng phụ có thể kéo dài sau khi ngừng",
            "Phải đảm bảo K+ và Mg2+ bình thường (giảm K+/Mg2+ tăng nguy cơ torsades de pointes)",
            "Tránh ánh nắng mặt trời (nhạy cảm ánh sáng nặng)"
        ],
        "pharmacokinetics": {
            "half_life": "50-60 ngày (RẤT DÀI - do tích lũy trong mô mỡ)",
            "onset": "1-3 tuần (do loading period)",
            "duration": "Rất lâu sau khi ngừng (do half-life dài)",
            "protein_binding": "96%",
            "clearance": "Gan (CYP3A4, CYP2C8), thải qua phân và nước tiểu (chậm)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây tử vong do viêm phổi mô kẽ, suy gan, rối loạn nhịp tim nặng. Chỉ dùng cho rối loạn nhịp đe dọa tính mạng không đáp ứng với thuốc khác. Phải monitor chức năng phổi, gan, tuyến giáp định kỳ. Chống chỉ định trong thai kỳ"
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
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế Na+/K+-ATPase ở màng tế bào cơ tim, tăng nồng độ Na+ nội bào, kích thích Na+/Ca2+ exchanger, tăng Ca2+ nội bào → tăng lực co bóp cơ tim (inotropy dương). Ở nút AV: tăng trương lực phế vị, giảm dẫn truyền AV (làm chậm tần số thất trong AF)",
        "monitoring": [
            "Nồng độ digoxin trong máu (BẮT BUỘC): Mục tiêu 0.8-2 ng/mL (1.0-2.6 nmol/L)",
            "Đo nồng độ ít nhất 6-8 giờ sau liều (sau khi phân bố)",
            "Điện giải: K+, Mg2+ (quan trọng - hạ K+, hạ Mg2+ → tăng nguy cơ ngộ độc)",
            "Creatinine, eGFR (digoxin thải qua thận)",
            "ECG: nhịp tim, block AV, rối loạn nhịp",
            "Triệu chứng ngộ độc: buồn nôn, nôn, rối loạn thị giác (nhìn vàng xanh), rối loạn nhịp"
        ],
        "precautions": [
            "LUÔN theo dõi nồng độ trong máu (therapeutic window hẹp)",
            "Hạ K+ và hạ Mg2+ làm tăng nguy cơ ngộ độc mạnh → phải bù điện giải trước",
            "Giảm liều ở suy thận (half-life tăng từ 36h lên 4-6 ngày)",
            "Ở người già: dùng liều thấp hơn (0.0625-0.125mg/ngày)",
            "Tránh loading dose nhanh ở suy thận (nguy cơ ngộ độc)",
            "Nhiều thuốc tương tác làm tăng nồng độ: amiodarone, verapamil, diltiazem, quinidine, macrolides, cyclosporine",
            "Ngộ độc digoxin có thể đe dọa tính mạng → cần điều trị ngay (Digibind/digoxin immune fab)"
        ],
        "pharmacokinetics": {
            "half_life": "36-48 giờ (bình thường), 4-6 ngày (suy thận)",
            "onset": "1-2 giờ (PO), 5-30 phút (IV)",
            "duration": "3-4 ngày (vì half-life dài)",
            "protein_binding": "20-25%",
            "clearance": "Thận (75-80%), không chuyển hóa"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: ổn định",
        "black_box_warnings": "Không dùng trong WPW với AF (có thể gây nhịp nhanh thất nguy hiểm). Ngộ độc digoxin có thể gây rối loạn nhịp đe dọa tính mạng và tử vong"
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
        "pregnancy": "X - Chống chỉ định (trừ trường hợp đặc biệt)",
        "mechanism_of_action": "Ức chế enzyme vitamin K epoxide reductase, giảm tổng hợp các yếu tố đông máu phụ thuộc vitamin K (II, VII, IX, X)",
        "monitoring": [
            "INR mỗi 1-4 tuần khi ổn định, thường xuyên hơn khi mới bắt đầu hoặc thay đổi liều",
            "INR mỗi 2-3 ngày trong tuần đầu",
            "Công thức máu (Hct, Hb) nếu nghi ngờ chảy máu",
            "Theo dõi dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím)"
        ],
        "precautions": [
            "Uống cùng thời điểm mỗi ngày",
            "Tránh thay đổi đột ngột chế độ ăn (vitamin K)",
            "Giữ chế độ ăn ổn định vitamin K",
            "Tránh rượu (tăng nguy cơ chảy máu)",
            "Thông báo bác sĩ trước khi phẫu thuật",
            "Theo dõi hoại tử da (ngày 3-10, thường ở bệnh nhân thiếu protein C)"
        ],
        "pharmacokinetics": {
            "half_life": "40 giờ (dài)",
            "onset": "24-72 giờ",
            "duration": "2-5 ngày sau khi ngừng",
            "protein_binding": "99%",
            "clearance": "Gan (CYP2C9, CYP1A2)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Chảy máu nặng có thể dẫn đến tử vong. Cần theo dõi INR chặt chẽ. Hoại tử da hiếm nhưng nguy hiểm"
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
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Ức chế không hồi phục enzyme cyclooxygenase (COX-1), ức chế kết tập tiểu cầu và tổng hợp prostaglandin. Với liều cao: giảm đau, hạ sốt, kháng viêm",
        "monitoring": [
            "Dấu hiệu chảy máu (phân đen, nôn ra máu, chảy máu chân răng)",
            "Hemoglobin nếu nghi ngờ chảy máu",
            "Chức năng thận nếu dùng lâu dài",
            "Ù tai nếu dùng liều cao (dấu hiệu độc tính)"
        ],
        "precautions": [
            "Dùng với thức ăn hoặc sau ăn để giảm kích ứng dạ dày",
            "Cân nhắc dùng PPI nếu có nguy cơ loét dạ dày",
            "Ngừng 5-7 ngày trước phẫu thuật lớn (nếu có thể)",
            "Không dùng cho trẻ <12 tuổi (hội chứng Reye)",
            "Không dùng với rượu (tăng nguy cơ chảy máu dạ dày)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (liều thấp), 15-20 giờ (liều cao)",
            "onset": "30 phút",
            "duration": "7-10 ngày (tiểu cầu, liều thấp), 4-6 giờ (giảm đau)",
            "protein_binding": "50-80%",
            "clearance": "Gan (thủy phân) và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ chảy máu, đặc biệt chảy máu dạ dày ruột. Nguy cơ tăng ở người già và dùng chung với thuốc khác"
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
        "pregnancy": "B",
        "mechanism_of_action": "Clopidogrel là prodrug, chuyển hóa thành chất chuyển hóa hoạt tính bởi CYP2C19 (và các CYP khác). Ức chế không hồi phục thụ thể P2Y12 trên tiểu cầu, ngăn chặn kích hoạt tiểu cầu bởi ADP, giảm kết tập tiểu cầu",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu)",
            "Công thức máu nếu nghi ngờ giảm tiểu cầu",
            "Xét nghiệm chức năng tiểu cầu (nếu cần - để đánh giá hiệu quả)",
            "Lưu ý: Một số bệnh nhân có thể kháng clopidogrel do đa hình CYP2C19"
        ],
        "precautions": [
            "Tránh dùng với PPIs mạnh (omeprazole, esomeprazole) - giảm hiệu quả do ức chế CYP2C19",
            "Có thể dùng với pantoprazole, lansoprazole (ít ức chế CYP2C19 hơn)",
            "Dùng kèm aspirin sau ACS/stent: DAPT 12 tháng (hoặc theo hướng dẫn)",
            "Ngừng 5-7 ngày trước phẫu thuật lớn (nếu có thể)",
            "Không ngừng đột ngột sau stent (nguy cơ huyết khối stent)",
            "Một số bệnh nhân kháng clopidogrel: xem xét thay bằng ticagrelor hoặc prasugrel"
        ],
        "pharmacokinetics": {
            "half_life": "Clopidogrel: 6 giờ; Metabolite hoạt tính: 30 phút (nhưng tác dụng kéo dài do ức chế không hồi phục)",
            "onset": "2-8 giờ (sau loading dose 300-600mg)",
            "duration": "5-10 ngày (cho đến khi tiểu cầu mới được tạo ra)",
            "protein_binding": "98%",
            "clearance": "Gan (chuyển hóa qua CYP2C19, CYP3A4, CYP2B6, CYP1A2)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Không ngừng clopidogrel sớm sau đặt stent (đặc biệt drug-eluting stent) - nguy cơ huyết khối stent và tử vong do tim. Chảy máu có thể đe dọa tính mạng"
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
        "pregnancy": "X",
        "mechanism_of_action": "Ức chế HMG-CoA reductase, enzyme chính trong tổng hợp cholesterol, dẫn đến giảm LDL-cholesterol và tăng HDL-cholesterol",
        "monitoring": [
            "Lipid profile (LDL, HDL, TG) sau 6-8 tuần, sau đó mỗi 3-6 tháng",
            "AST/ALT trước điều trị, sau 12 tuần, sau đó mỗi 6-12 tháng",
            "CK nếu có đau cơ, yếu cơ",
            "HbA1c/đường huyết (statin có thể tăng đường huyết)"
        ],
        "precautions": [
            "Kiểm tra CK nếu đau cơ hoặc yếu cơ (ngừng nếu CK >10 lần ULN)",
            "Ngừng nếu ALT >3 lần ULN",
            "Thận trọng với bệnh nhân đái tháo đường (có thể tăng đường huyết)",
            "Tránh grapefruit juice với liều cao"
        ],
        "pharmacokinetics": {
            "half_life": "14 giờ",
            "onset": "1-2 tuần",
            "duration": "24 giờ",
            "protein_binding": ">98%",
            "clearance": "Gan (CYP3A4)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tiêu cơ vân - có thể gây suy thận cấp và tử vong. Nguy cơ tăng khi dùng chung với thuốc khác hoặc liều cao"
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
          "pregnancy": "X",
          "mechanism_of_action": "HMG-CoA reductase inhibitor (statin). Ức chế enzyme HMG-CoA reductase - enzyme quan trọng trong tổng hợp cholesterol ở gan. Giảm sản xuất cholesterol nội sinh, tăng biểu hiện LDL receptor ở gan, giảm LDL cholesterol. Cũng có tác dụng chống viêm, ổn định mảng xơ vữa (pleiotropic effects).",
          "monitoring": [
              "Lipid panel: Cholesterol toàn phần, LDL, HDL, triglycerides (sau 4-8 tuần, sau đó mỗi 3-6 tháng)",
              "Chức năng gan: ALT, AST (trước khi bắt đầu, sau 12 tuần, sau đó mỗi 6-12 tháng hoặc khi có triệu chứng)",
              "CK (creatine kinase) - nếu có đau cơ, yếu cơ (để phát hiện tiêu cơ vân)",
              "Glucose/HbA1c - statins có thể tăng đường huyết nhẹ",
              "Dấu hiệu đau cơ, yếu cơ, nước tiểu sẫm màu (dấu hiệu tiêu cơ vân)"
          ],
          "precautions": [
              "Uống buổi tối (cholesterol được tổng hợp nhiều vào ban đêm)",
              "TRÁNH grapefruit juice (ức chế CYP3A4, tăng nồng độ, tăng nguy cơ tác dụng phụ)",
              "Kiểm tra CK nếu có đau cơ/yếu cơ - ngừng ngay nếu CK >10x ULN hoặc có dấu hiệu tiêu cơ vân",
              "Thận trọng với liều cao (>40mg/ngày) - tăng nguy cơ tiêu cơ vân",
              "Giảm liều khi dùng với amiodarone, verapamil, diltiazem, macrolides, azole antifungals (tương tác CYP3A4)",
              "CHỐNG CHỈ ĐỊNH trong thai kỳ và cho con bú (category X)",
              "Thận trọng ở bệnh nhân có bệnh gan - kiểm tra ALT/AST trước khi bắt đầu",
              "Có thể tăng đường huyết nhẹ (đặc biệt ở bệnh nhân đái tháo đường)"
          ],
          "pharmacokinetics": {
              "half_life": "2-3 giờ (ngắn), nhưng tác dụng kéo dài do ức chế enzyme)",
              "onset": "1-2 tuần (giảm LDL)",
              "duration": "Kéo dài sau khi ngừng",
              "protein_binding": "95%",
              "clearance": "Gan (CYP3A4) - extensive first-pass metabolism"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ - có thể gây dị tật thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả. Tiêu cơ vân có thể gây suy thận cấp và tử vong - ngừng ngay nếu có đau cơ, yếu cơ, nước tiểu sẫm màu"
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
        "pregnancy": "B",
        "mechanism_of_action": "Ức chế sản xuất glucose ở gan, tăng nhạy cảm với insulin ở mô ngoại vi, giảm hấp thu glucose ở ruột",
        "monitoring": [
            "HbA1c mỗi 3 tháng",
            "Đường huyết đói và sau ăn",
            "Creatinine, eGFR mỗi 3-6 tháng",
            "Vitamin B12 mỗi 1-2 năm",
            "Lactate nếu nghi ngờ nhiễm toan lactic (đau cơ, khó thở, đau bụng)"
        ],
        "precautions": [
            "Ngừng 48h trước và sau khi dùng thuốc cản quang",
            "Theo dõi nhiễm toan lactic ở bệnh nhân suy tim, suy gan, suy thận",
            "Bổ sung vitamin B12 nếu dùng lâu dài",
            "Tránh rượu (tăng nguy cơ nhiễm toan lactic)"
        ],
        "pharmacokinetics": {
            "half_life": "6.2 giờ",
            "onset": "1-2 giờ",
            "duration": "10-12 giờ",
            "protein_binding": "Minimal",
            "clearance": "Thận (chủ yếu)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nhiễm toan lactic - có thể tử vong. Nguy cơ cao ở suy thận, suy tim, suy gan, nhiễm trùng nặng"
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
          "pregnancy": "C",
          "mechanism_of_action": "Sulfonylurea thế hệ 2. Kích thích tế bào beta tuyến tụy tiết insulin bằng cách đóng kênh KATP (ATP-sensitive K+ channel), làm khử cực màng tế bào, mở kênh Ca2+, và giải phóng insulin. Chỉ hoạt động khi còn chức năng tế bào beta. Gliclazide ưu điểm: thời gian bán hủy ngắn hơn, ít nguy cơ hạ đường huyết hơn glibenclamide.",
          "monitoring": [
              "Đường huyết: HbA1c (mỗi 3 tháng), đường huyết đói, đường huyết sau ăn",
              "Dấu hiệu hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, lú lẫn, co giật",
              "Cân nặng - sulfonylureas có thể gây tăng cân",
              "Chức năng thận: creatinine, eGFR (suy thận tăng nguy cơ hạ đường huyết)",
              "Chức năng gan: ALT, AST (nếu có bệnh gan)"
          ],
          "precautions": [
              "Uống với thức ăn hoặc trước bữa ăn để tránh hạ đường huyết",
              "KHÔNG dùng ở đái tháo đường type 1 hoặc nhiễm toan ceton",
              "Thận trọng ở bệnh nhân suy thận - tăng nguy cơ hạ đường huyết (có thể cần giảm liều hoặc tránh dùng)",
              "Thận trọng ở bệnh nhân suy gan - tăng nguy cơ hạ đường huyết",
              "Hạ đường huyết là tác dụng phụ phổ biến nhất - bệnh nhân cần biết dấu hiệu và cách xử trí",
              "Tránh bỏ bữa - tăng nguy cơ hạ đường huyết",
              "Tránh rượu - tăng nguy cơ hạ đường huyết",
              "Có thể tăng cân - cần tư vấn chế độ ăn và tập luyện",
              "Gliclazide ưu điểm: thời gian bán hủy ngắn hơn, ít hạ đường huyết hơn glibenclamide"
          ],
          "pharmacokinetics": {
              "half_life": "10-12 giờ (ngắn hơn glibenclamide)",
              "onset": "30-60 phút (PO)",
              "duration": "12-24 giờ",
              "protein_binding": "85-95%",
              "clearance": "Gan (CYP2C9), thận (metabolites)"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "Hạ đường huyết có thể gây nguy hiểm tính mạng, đặc biệt ở bệnh nhân suy thận, suy gan, người già. Bệnh nhân cần biết dấu hiệu và cách xử trí hạ đường huyết"
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
        "pregnancy": "B - An toàn, điều chỉnh liều theo thai kỳ",
        "mechanism_of_action": "Insulin là hormone tự nhiên được tiết ra từ tế bào beta tuyến tụy. Gắn với thụ thể insulin, kích hoạt các tín hiệu nội bào, tăng vận chuyển glucose vào tế bào, kích thích tổng hợp glycogen, protein, lipid, và ức chế sản xuất glucose ở gan. Giảm đường huyết bằng cách tăng sử dụng glucose và giảm sản xuất glucose",
        "monitoring": [
            "Đường huyết (glucose) thường xuyên: Trước bữa ăn, 2 giờ sau bữa ăn, trước khi ngủ",
            "HbA1c mỗi 3 tháng (mục tiêu <7% hoặc theo cá thể hóa)",
            "Dấu hiệu hạ đường huyết: Run rẩy, đổ mồ hôi, nhịp tim nhanh, đói, nhầm lẫn, co giật, hôn mê",
            "Dấu hiệu tăng đường huyết: Khát nhiều, tiểu nhiều, mệt mỏi, mờ mắt",
            "Cân nặng (insulin có thể gây tăng cân)",
            "Chức năng thận (giảm clearance insulin ở suy thận)",
            "Kiểm tra vị trí tiêm (tránh lipodystrophy)"
        ],
        "precautions": [
            "LUÔN có glucagon và glucose sẵn để điều trị hạ đường huyết",
            "Điều chỉnh liều theo đường huyết, bữa ăn, hoạt động thể chất",
            "Xoay vị trí tiêm (bụng, đùi, cánh tay, mông)",
            "Bảo quản đúng cách: Insulin đang dùng có thể để ở nhiệt độ phòng, chưa mở phải để tủ lạnh",
            "Không được làm đông lạnh insulin",
            "Giảm liều ở suy thận (giảm clearance)",
            "Tăng liều trong bệnh nặng, stress, nhiễm trùng",
            "Dạy bệnh nhân nhận biết và xử trí hạ đường huyết",
            "Trong thai kỳ: tăng nhu cầu insulin, điều chỉnh thường xuyên"
        ],
        "pharmacokinetics": {
            "half_life": "Rapid-acting (lispro, aspart): 1 giờ; Short-acting (regular): 2-4 giờ; Intermediate (NPH): 8-12 giờ; Long-acting (glargine, detemir): 12-24 giờ; Ultra-long (degludec): 42 giờ",
            "onset": "Rapid: 15 phút; Short: 30-60 phút; Intermediate: 1-3 giờ; Long: 1-2 giờ",
            "duration": "Rapid: 3-5 giờ; Short: 6-8 giờ; Intermediate: 12-16 giờ; Long: 18-24 giờ; Ultra-long: >42 giờ",
            "protein_binding": "Không (peptide hormone)",
            "clearance": "Gan (50-60%), thận (30-40%), một phần bị phân hủy bởi insulinase"
        },
        "storage": "Chưa mở: Tủ lạnh (2-8°C), không đông lạnh. Đang dùng: Nhiệt độ phòng (<30°C), tránh ánh sáng, tránh nhiệt độ cao. Dùng trong vòng 28-30 ngày sau khi mở",
        "black_box_warnings": "Hạ đường huyết có thể đe dọa tính mạng. Cần theo dõi đường huyết thường xuyên và có sẵn glucose/glucagon để điều trị hạ đường huyết. Không được dùng chung ống tiêm insulin"
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
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế không hồi phục H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày",
        "monitoring": [
            "Triệu chứng cải thiện (đau dạ dày, ợ chua)",
            "Vitamin B12 mỗi 1-2 năm nếu dùng lâu dài",
            "Magnesium nếu có triệu chứng (chuột rút, yếu cơ) hoặc dùng lâu dài",
            "Mật độ xương nếu dùng lâu dài, liều cao (phụ nữ >50 tuổi)",
            "Theo dõi nhiễm C. difficile nếu có tiêu chảy"
        ],
        "precautions": [
            "Uống 30 phút trước bữa ăn (để tối đa hóa hiệu quả)",
            "Không nhai/cắn viên bao tan trong ruột",
            "Dùng liều thấp nhất có hiệu quả, thời gian ngắn nhất",
            "Cân nhắc giảm liều hoặc ngừng sau 4-8 tuần nếu có thể",
            "Bổ sung vitamin B12 nếu dùng lâu dài",
            "Bổ sung magnesium nếu thiếu"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ (ngắn), nhưng tác dụng kéo dài do ức chế không hồi phục",
            "onset": "1-3 giờ",
            "duration": "24 giờ (một liều)",
            "protein_binding": "95%",
            "clearance": "Gan (CYP2C19, CYP3A4)"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Giảm hiệu quả clopidogrel khi dùng đồng thời. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài"
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
          "pregnancy": "B",
          "mechanism_of_action": "Proton pump inhibitor (PPI). Ức chế H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày mạnh và kéo dài. Khác với H2 blockers, PPI ức chế bước cuối cùng của quá trình tiết acid, nên hiệu quả hơn. Pantoprazole ít tương tác với CYP450 hơn omeprazole.",
          "monitoring": [
              "Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng",
              "Mg2+ máu (nếu dùng kéo dài >3 tháng) - PPI có thể gây hạ magie máu",
              "Vitamin B12 (nếu dùng kéo dài >2 năm) - PPI giảm hấp thu B12",
              "Dấu hiệu nhiễm trùng: PPI tăng nguy cơ viêm phổi, C. difficile colitis",
              "Loãng xương: PPI dùng kéo dài có thể tăng nguy cơ gãy xương (cần monitor nếu >1 năm)"
          ],
          "precautions": [
              "Uống 30-60 phút TRƯỚC bữa ăn (để PPI hoạt động khi proton pump được kích hoạt)",
              "KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated)",
              "Pantoprazole ưu điểm: ít tương tác với CYP450 hơn omeprazole, ít ảnh hưởng đến clopidogrel hơn",
              "Dùng ngắn hạn khi có thể - tránh dùng kéo dài không cần thiết",
              "Thận trọng ở bệnh nhân loãng xương (PPI dùng kéo dài có thể tăng nguy cơ gãy xương)",
              "Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều nhưng monitor)",
              "Tăng nguy cơ viêm phổi, C. difficile colitis (đặc biệt ở người già, suy giảm miễn dịch)"
          ],
          "pharmacokinetics": {
              "half_life": "1 giờ (ngắn), nhưng tác dụng kéo dài 24h do ức chế không thuận nghịch proton pump",
              "onset": "1-3 ngày (tác dụng đầy đủ)",
              "duration": "24 giờ (mặc dù half-life ngắn)",
              "protein_binding": "98%",
              "clearance": "Gan (CYP2C19, CYP3A4) - ít tương tác hơn omeprazole"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": ""
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
        "pregnancy": "B",
        "mechanism_of_action": "H2 (histamine-2) receptor antagonist. Ức chế histamine tại H2 receptors ở tế bào thành dạ dày, giảm tiết acid dạ dày (giảm acid kích thích và một phần acid cơ bản). Yếu hơn PPI (proton pump inhibitor) nhưng rẻ hơn. Tác dụng ngắn hơn PPI (cần dùng 2 lần/ngày). Ức chế nhẹ một số enzyme CYP450 (ít hơn cimetidine).",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau, triệu chứng GERD)",
            "Chức năng gan (transaminase) - có thể tăng men gan (hiếm)",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy nặng, đau bụng) - tăng nguy cơ nhẹ",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu nhẹ)"
        ],
        "precautions": [
            "Uống với thức ăn hoặc trước bữa ăn (tăng hiệu quả)",
            "Yếu hơn PPI - cân nhắc dùng PPI nếu không đáp ứng",
            "Thận trọng ở suy thận (giảm liều)",
            "Thận trọng ở suy gan (giảm liều)",
            "Cân nhắc ngừng sau 4-8 tuần nếu không cần thiết (giảm nguy cơ tác dụng phụ)",
            "Một số sản phẩm đã bị thu hồi do NDMA (chất gây ung thư) - kiểm tra nguồn gốc sản phẩm",
            "Không dùng với các thuốc cần acid để hấp thu (ketoconazole, itraconazole, iron salts) - cách 2 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "1-3 giờ",
            "duration": "8-12 giờ",
            "protein_binding": "15%",
            "metabolism": "Gan (chuyển hóa qua CYP450, một phần), thận (thải trừ)",
            "clearance": "Gan (chuyển hóa), thận (30-50% thải nguyên dạng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Kiểm tra nguồn gốc sản phẩm (một số sản phẩm đã bị thu hồi do NDMA).",
        "black_box_warnings": "Một số sản phẩm ranitidine đã bị thu hồi do chứa NDMA (N-nitrosodimethylamine) - chất gây ung thư. NDMA có thể tích lũy trong sản phẩm theo thời gian, đặc biệt ở nhiệt độ cao. Kiểm tra nguồn gốc sản phẩm và cân nhắc dùng thuốc khác (PPI, famotidine) nếu có thể."
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
        "pregnancy": "B",
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%"
        },
        "mechanism_of_action": "Dopamine D2 receptor antagonist và 5-HT3 receptor antagonist. Ức chế dopamine ở chemoreceptor trigger zone (CTZ), giảm buồn nôn, nôn. Tăng co bóp dạ dày, tăng trương lực cơ thắt môn vị, tăng nhu động ruột (prokinetic effect). Cũng ức chế 5-HT3 receptor (giống ondansetron).",
        "monitoring": [
            "Dấu hiệu rối loạn vận động: dystonia, parkinsonism, akathisia (xuất hiện sớm, có thể điều trị)",
            "Rối loạn vận động muộn (tardive dyskinesia) - nếu dùng >12 tuần (có thể không hồi phục)",
            "Dấu hiệu hội chứng serotonin: kích động, tăng thân nhiệt, tăng phản xạ (nếu dùng với SSRI/SNRI)",
            "Đáp ứng lâm sàng: giảm buồn nôn, nôn; tăng nhu động dạ dày"
        ],
        "precautions": [
            "KHÔNG dùng quá 12 tuần - tăng nguy cơ rối loạn vận động muộn (tardive dyskinesia) có thể không hồi phục",
            "Thận trọng ở trẻ em và thanh niên - tăng nguy cơ rối loạn vận động (dystonia, parkinsonism)",
            "Tránh dùng ở bệnh nhân Parkinson, dystonia - làm nặng triệu chứng",
            "Thận trọng khi dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin",
            "Thận trọng khi dùng với antipsychotics - tăng nguy cơ rối loạn vận động",
            "Tránh dùng với anticholinergics - đối kháng tác dụng prokinetic",
            "CHỐNG CHỈ ĐỊNH trong tắc ruột, xuất huyết tiêu hóa",
            "Có thể gây buồn ngủ - tránh lái xe, vận hành máy móc"
        ],
        "pharmacokinetics": {
            "half_life": "5-6 giờ",
            "onset": "1-3 phút (IV), 30-60 phút (PO)",
            "duration": "1-2 giờ",
            "protein_binding": "30%",
            "clearance": "Gan (CYP2D6), thận (30% thải nguyên dạng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Rối loạn vận động muộn (tardive dyskinesia) có thể phát triển và trở thành không hồi phục. Nguy cơ tăng với thời gian điều trị và tổng liều. Ngừng ngay nếu có dấu hiệu rối loạn vận động. KHÔNG dùng quá 12 tuần"
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
        "pregnancy": "C",
        "mechanism_of_action": "Opioid mu-receptor agonist ở ruột (peripheral opioid). Ức chế acetylcholine và prostaglandin ở cơ trơn ruột, giảm nhu động ruột, tăng trương lực cơ thắt hậu môn, tăng hấp thu nước từ phân. Tác dụng chống tiêu chảy. Không qua hàng rào máu-não đáng kể ở liều điều trị → ít tác dụng phụ thần kinh và ít nguy cơ nghiện hơn opioid hệ thống. Tuy nhiên, liều cao có thể qua hàng rào máu-não và gây tác dụng opioid hệ thống.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm tần suất đi ngoài, cải thiện tính chất phân)",
            "Dấu hiệu quá liều: ức chế hô hấp, giảm ý thức, co đồng tử (miosis)",
            "Dấu hiệu táo bón nặng (có thể gây tắc ruột giả)",
            "Dấu hiệu nhiễm khuẩn (nếu giữ vi khuẩn trong ruột quá lâu)",
            "Dấu hiệu viêm đại tràng giả mạc (tiêu chảy nặng, đau bụng, sốt) - nguy cơ nếu dùng với kháng sinh"
        ],
        "precautions": [
            "Chỉ dùng cho tiêu chảy không nhiễm khuẩn hoặc đã điều trị nhiễm khuẩn",
            "Không dùng quá 48 giờ nếu không cải thiện (cần đánh giá lại nguyên nhân)",
            "Không dùng cho tiêu chảy nhiễm khuẩn nặng (có thể giữ vi khuẩn trong ruột)",
            "Không dùng cho viêm đại tràng giả mạc (có thể làm nặng thêm)",
            "Không dùng cho trẻ em <2 tuổi (nguy cơ ức chế hô hấp)",
            "Không vượt quá 16mg/ngày (tăng nguy cơ tác dụng phụ hệ thống)",
            "Ngừng ngay nếu có dấu hiệu quá liều (ức chế hô hấp, giảm ý thức)",
            "Thận trọng ở bệnh nhân suy gan (giảm chuyển hóa)",
            "Thận trọng ở bệnh nhân suy thận (tích lũy)",
            "Nếu dùng với kháng sinh → tăng nguy cơ viêm đại tràng giả mạc"
        ],
        "pharmacokinetics": {
            "half_life": "7-14 giờ",
            "onset": "1-2 giờ",
            "duration": "4-6 giờ",
            "protein_binding": "97%",
            "metabolism": "Gan (chuyển hóa qua CYP3A4, CYP2C8)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em (nguy cơ quá liều).",
        "black_box_warnings": "Liều cao có thể gây ức chế hô hấp nặng, có thể tử vong, đặc biệt ở trẻ em. Không dùng quá liều khuyến cáo (16mg/ngày). Không dùng cho trẻ em <2 tuổi. Không dùng cho tiêu chảy nhiễm khuẩn nặng - có thể giữ vi khuẩn trong ruột và làm nặng bệnh. Ngừng ngay nếu có dấu hiệu quá liều."
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
        "pregnancy": "C",
        "mechanism_of_action": "Dopamine D2 receptor antagonist ở ngoại vi (ruột và chemoreceptor trigger zone). Ức chế dopamine → tăng nhu động dạ dày và ruột, tăng trương lực cơ thắt dưới thực quản, tăng tốc độ làm rỗng dạ dày. Có tác dụng chống nôn do ức chế dopamine ở chemoreceptor trigger zone. KHÔNG qua hàng rào máu-não (do bị P-glycoprotein đẩy ra) → ít tác dụng phụ thần kinh hơn metoclopramide (không gây mê sảng, parkinsonism). Tăng prolactin do ức chế dopamine ở tuyến yên (dopamine ức chế tiết prolactin).",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm buồn nôn, nôn, cải thiện làm rỗng dạ dày)",
            "ECG nếu dùng liều cao hoặc kéo dài (nguy cơ QT kéo dài)",
            "Dấu hiệu tăng prolactin: rối loạn kinh nguyệt, chảy sữa, đau vú",
            "Dấu hiệu QT kéo dài: loạn nhịp tim, chóng mặt, ngất",
            "Dấu hiệu tác dụng phụ thần kinh (hiếm nhưng có thể xảy ra nếu tích lũy)"
        ],
        "precautions": [
            "Uống trước bữa ăn 15-30 phút (tăng hiệu quả)",
            "Không vượt quá 80mg/ngày (tăng nguy cơ QT kéo dài)",
            "Tránh dùng với các thuốc kéo dài QT (amiodarone, quinolone, macrolide) - tăng nguy cơ loạn nhịp",
            "Thận trọng ở suy thận (giảm liều)",
            "Thận trọng ở suy gan (giảm liều)",
            "Theo dõi dấu hiệu tăng prolactin (rối loạn kinh nguyệt, chảy sữa)",
            "Ngừng nếu có dấu hiệu QT kéo dài hoặc loạn nhịp",
            "Ít tác dụng phụ thần kinh hơn metoclopramide (không qua hàng rào máu-não)",
            "Không dùng trong prolactinoma (tăng prolactin có thể làm tăng kích thước u)"
        ],
        "pharmacokinetics": {
            "half_life": "7-9 giờ",
            "onset": "30-60 phút",
            "duration": "4-8 giờ",
            "protein_binding": "91-93%",
            "metabolism": "Gan (chuyển hóa qua CYP3A4), CYP1A2",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ QT kéo dài và loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Nguy cơ tăng ở liều cao (>80mg/ngày), suy thận, suy gan, hoặc dùng với các thuốc kéo dài QT. Không vượt quá 80mg/ngày. Tránh dùng với các thuốc kéo dài QT."
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
        "pregnancy": "B",
        "mechanism_of_action": "5-HT3 (serotonin) receptor antagonist. Ức chế chọn lọc receptor 5-HT3 ở ngoại vi (dây thần kinh phế vị) và trung ương (chemoreceptor trigger zone trong area postrema). Ngăn cản tác dụng của serotonin, dẫn đến giảm nôn và buồn nôn. Được dùng trong dự phòng và điều trị nôn do hóa trị, xạ trị, và sau phẫu thuật. Hiệu quả hơn metoclopramide và không gây tác dụng phụ ngoại tháp như metoclopramide.",
        "monitoring": [
            "Tần suất nôn và buồn nôn",
            "ECG (QT kéo dài - nguy cơ rối loạn nhịp tim, đặc biệt ở liều cao)",
            "Điện giải (kali, magie) - hạ kali, hạ magie tăng nguy cơ QT kéo dài",
            "Dấu hiệu tắc ruột (ondansetron có thể che dấu triệu chứng)",
            "Chức năng gan (ALT, AST) - hiếm tăng men gan"
        ],
        "precautions": [
            "QT kéo dài → không dùng ở bệnh nhân có QT kéo dài, rối loạn nhịp tim, hoặc dùng các thuốc kéo dài QT khác",
            "Nguy cơ tăng ở liều cao (> 16mg đơn liều), hạ kali, hạ magie, suy gan",
            "Có thể che dấu triệu chứng tắc ruột - thận trọng ở bệnh nhân có nguy cơ",
            "Giảm liều ở suy gan nặng (giảm chuyển hóa)",
            "Liều thường: 4-8mg (PO/IV), có thể lặp lại mỗi 8 giờ",
            "Liều tối đa: 32mg/ngày (để giảm nguy cơ QT kéo dài)",
            "Có thể dùng trước hóa trị/xạ trị để dự phòng",
            "An toàn trong thai kỳ (category B)"
        ],
        "pharmacokinetics": {
            "half_life": "3-6 giờ (bình thường), kéo dài ở suy gan",
            "onset": "30 phút (PO), ngay lập tức (IV)",
            "duration": "4-8 giờ",
            "protein_binding": "70-76%",
            "metabolism": "Gan (CYP1A2, CYP2D6, CYP3A4) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Dung dịch tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ QT kéo dài, có thể gây rối loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Nguy cơ tăng ở liều cao, hạ kali, hạ magie, suy gan, hoặc dùng với các thuốc kéo dài QT khác. Không dùng vượt quá liều khuyến cáo."

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
        "pregnancy": "B",
        "mechanism_of_action": "Ức chế không hồi phục enzyme H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, ức chế bước cuối cùng trong quá trình tiết acid dạ dày. Ức chế cả acid kích thích và acid cơ bản. Cần chuyển hóa ở gan thành dạng hoạt động (sulfenamide). Tác dụng mạnh hơn H2 blocker. Thời gian bán thải ngắn nhưng tác dụng kéo dài do ức chế không hồi phục enzyme.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau, triệu chứng GERD)",
            "Magie máu nếu dùng lâu dài (>1 năm) - có thể giảm magie",
            "Vitamin B12 nếu dùng lâu dài (>2 năm) - có thể thiếu B12",
            "Mật độ xương (DEXA scan) nếu dùng lâu dài và có nguy cơ loãng xương",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy nặng, đau bụng) - tăng nguy cơ",
            "Chức năng thận (nếu dùng lâu dài với nguy cơ suy thận)"
        ],
        "precautions": [
            "Uống trước bữa ăn 30 phút (tăng hiệu quả)",
            "Viên tan trong miệng: đặt trên lưỡi, để tan tự nhiên, không cần nước",
            "Không nghiền hoặc nhai viên (bao tan trong ruột)",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể",
            "Cân nhắc ngừng sau 4-8 tuần nếu không cần thiết (giảm nguy cơ tác dụng phụ)",
            "Cân nhắc dùng liều cách ngày hoặc ngắt quãng nếu dùng lâu dài",
            "Thận trọng ở bệnh nhân suy gan nặng (giảm liều)",
            "Không dùng với các thuốc cần acid để hấp thu (ketoconazole, itraconazole, iron salts)"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (ngắn, nhưng tác dụng kéo dài do ức chế không hồi phục)",
            "onset": "1-3 giờ",
            "duration": "24 giờ (một lần/ngày)",
            "protein_binding": "97%",
            "clearance": "Gan (chuyển hóa qua CYP2C19, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên tan trong miệng: bảo quản trong bao bì gốc, tránh ẩm.",
        "black_box_warnings": "Dùng lâu dài (>1 năm) có thể tăng nguy cơ loãng xương, gãy xương hông, cổ tay, cột sống. Dùng lâu dài có thể tăng nguy cơ thiếu vitamin B12. Tăng nguy cơ nhiễm C. difficile."
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
        "pregnancy": "B",
        "mechanism_of_action": "Enantiomer S của omeprazole. Ức chế không hồi phục enzyme H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, ức chế bước cuối cùng trong quá trình tiết acid dạ dày. Chuyển hóa qua CYP2C19 ít hơn omeprazole (racemic) → hiệu quả tốt hơn và ổn định hơn. Ức chế cả acid kích thích và acid cơ bản. Tác dụng mạnh hơn và ổn định hơn omeprazole do ít chuyển hóa qua CYP2C19.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau, triệu chứng GERD)",
            "Magie máu nếu dùng lâu dài (>1 năm) - có thể giảm magie",
            "Vitamin B12 nếu dùng lâu dài (>2 năm) - có thể thiếu B12",
            "Mật độ xương (DEXA scan) nếu dùng lâu dài và có nguy cơ loãng xương",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy nặng, đau bụng) - tăng nguy cơ",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Chức năng thận (nếu dùng lâu dài với nguy cơ suy thận)"
        ],
        "precautions": [
            "Uống trước bữa ăn 30 phút (tăng hiệu quả)",
            "Không nghiền hoặc nhai viên (bao tan trong ruột)",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể",
            "Cân nhắc ngừng sau 4-8 tuần nếu không cần thiết (giảm nguy cơ tác dụng phụ)",
            "Cân nhắc dùng liều cách ngày hoặc ngắt quãng nếu dùng lâu dài",
            "Thận trọng ở bệnh nhân suy gan nặng (giảm liều)",
            "Không dùng với các thuốc cần acid để hấp thu (ketoconazole, itraconazole, iron salts)",
            "Cân nhắc tương tác với clopidogrel (có thể giảm hiệu quả - controversial, cân nhắc dùng PPI khác)"
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ (ngắn, nhưng tác dụng kéo dài do ức chế không hồi phục)",
            "onset": "1-3 giờ",
            "duration": "24 giờ (một lần/ngày)",
            "protein_binding": "97%",
            "clearance": "Gan (chuyển hóa qua CYP2C19 ít hơn omeprazole, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên bao tan trong ruột: không nghiền hoặc nhai.",
        "black_box_warnings": "Dùng lâu dài (>1 năm) có thể tăng nguy cơ loãng xương, gãy xương hông, cổ tay, cột sống. Dùng lâu dài có thể tăng nguy cơ thiếu vitamin B12. Tăng nguy cơ nhiễm C. difficile."
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
        "pregnancy": "B",
        "mechanism_of_action": "Phức hợp sucrose-aluminum. Tạo lớp phủ bảo vệ trên vết loét dạ dày tá tràng. Phản ứng với acid dạ dày tạo thành gel dính, bám chặt vào vết loét, tạo hàng rào bảo vệ khỏi acid, pepsin, và muối mật. Kích thích tổng hợp prostaglandin, tăng tiết chất nhầy, tăng tái tạo niêm mạc. Cũng có thể hấp phụ pepsin và muối mật. Không giảm tiết acid như PPI/H2 blocker mà bảo vệ niêm mạc trực tiếp.",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau, lành vết loét)",
            "Dấu hiệu tích tụ nhôm: rối loạn thần kinh, xương yếu (nếu dùng lâu dài ở suy thận)",
            "Chức năng thận (creatinine, BUN) - đặc biệt nếu dùng lâu dài",
            "INR nếu dùng với warfarin (có thể tăng tác dụng chống đông)",
            "Dấu hiệu táo bón nặng (tác dụng phụ thường gặp)"
        ],
        "precautions": [
            "Uống khi bụng đói (1 giờ trước bữa ăn) - cần acid dạ dày để tạo gel",
            "Không dùng với PPI, H2 blocker, antacid - cách 2 giờ (chúng làm giảm acid → giảm hiệu quả sucralfate)",
            "Không dùng với các thuốc khác - cách 2 giờ (sucralfate có thể giảm hấp thu)",
            "Thận trọng ở suy thận (CrCl 30-60) - giảm liều",
            "Tránh dùng ở suy thận nặng (CrCl <30) - tích tụ nhôm có thể gây độc",
            "Có thể gây táo bón - dùng thuốc nhuận tràng nếu cần",
            "Không nghiền hoặc nhai viên (giảm hiệu quả)",
            "Dùng đủ 4-8 tuần để lành vết loét hoàn toàn"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (tác dụng tại chỗ, không hấp thu)",
            "onset": "1-2 giờ",
            "duration": "6 giờ (lớp phủ bảo vệ)",
            "protein_binding": "Không áp dụng (không hấp thu)",
            "clearance": "Không hấp thu đáng kể, thải qua phân. Nhôm có thể tích tụ ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tránh dùng ở suy thận nặng (CrCl <30) - tích tụ nhôm có thể gây độc thần kinh, xương yếu, thiếu máu. Không dùng với PPI/H2 blocker/antacid đồng thời - cách 2 giờ để đảm bảo hiệu quả."
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
        "pregnancy": "B - An toàn trong thai kỳ",
        "mechanism_of_action": "Ức chế cyclooxygenase ở hệ thần kinh trung ương, giảm tổng hợp prostaglandin, từ đó giảm đau và hạ sốt. Ít tác dụng kháng viêm so với NSAID",
        "monitoring": [
            "ALT/AST nếu nghi ngờ quá liều hoặc bệnh nhân có nguy cơ",
            "INR nếu dùng với warfarin liều cao kéo dài",
            "Dấu hiệu độc tính gan: buồn nôn, nôn, đau bụng, vàng da (xuất hiện sau 24-48h)"
        ],
        "precautions": [
            "Không vượt quá 4g/ngày ở người lớn",
            "Giảm liều ở bệnh nhân suy gan",
            "Tránh rượu khi dùng (tăng nguy cơ độc tính gan)",
            "Kiểm tra các thuốc khác có chứa paracetamol (tránh quá liều)",
            "Nếu quá liều, điều trị ngay với N-acetylcysteine"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "30 phút (PO), 15 phút (IV)",
            "duration": "4-6 giờ",
            "protein_binding": "20-30%",
            "clearance": "Gan (chủ yếu qua glucuronidation và sulfation, một phần qua CYP2E1 tạo NAPQI - chất độc)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Quá liều có thể gây độc tính gan nghiêm trọng, suy gan, tử vong. Liều >150mg/kg hoặc >10g ở người lớn có thể gây độc tính. Điều trị ngay với N-acetylcysteine nếu quá liều"
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
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt khi dùng với benzodiazepine, rượu, hoặc thuốc an thần khác. Nguy cơ co giật tăng ở liều cao và khi dùng với SSRI/SNRI. Nguy cơ hội chứng serotonin khi dùng với MAOI hoặc SSRI/SNRI, có thể tử vong."

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
        "black_box_warnings": "Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao."
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
        "black_box_warnings": "Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao. Diclofenac có nguy cơ tăng men gan và chảy máu dạ dày cao hơn một số NSAID khác."
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
            "metabolism": "Gan: glucuronidation → morphine-3-glucuronide (không hoạt động) và morphine-6-glucuronide (hoạt động mạnh hơn, tích lũy ở suy thận)",
            "clearance": "Chủ yếu qua thận (morphine-6-glucuronide tích lũy ở suy thận)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em (nguy cơ quá liều).",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt khi dùng với benzodiazepine hoặc rượu. Morphine có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối thai kỳ."
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
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt ở ultra-rapid metabolizers (tạo nhiều morphine) hoặc khi dùng với benzodiazepine/rượu. Trẻ em <12 tuổi: không dùng cho ho. Trẻ em <18 tuổi sau cắt amidan/VA: chống chỉ định (nguy cơ ức chế hô hấp nghiêm trọng, có thể tử vong)."
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
        "black_box_warnings": "Nguy cơ co mạch nghiêm trọng, có thể gây nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ, có thể tử vong. CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên, tăng huyết áp không kiểm soát. Không dùng với ergotamine trong 24 giờ. Nếu có đau ngực, khó thở → ngừng ngay và đánh giá."
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
        "pregnancy": "C",
        "mechanism_of_action": "Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng nhanh, ngắn (4-6 giờ). Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch ở liều cao. Giảm phóng thích chất trung gian gây viêm từ mast cells.",
        "monitoring": [
            "Nhịp tim, huyết áp (đặc biệt khi dùng IV hoặc liều cao)",
            "Kali máu nếu dùng liều cao hoặc kéo dài",
            "Đáp ứng phế quản (peak flow, FEV1)",
            "Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp",
            "Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)"
        ],
        "precautions": [
            "Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên",
            "Nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS",
            "Tránh dùng với beta-blocker (đối kháng tác dụng)",
            "Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)",
            "Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ",
            "Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng",
            "Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "2-7 giờ (hít), 2-4 giờ (IV)",
            "onset": "5-15 phút (hít), 2-5 phút (IV)",
            "duration": "4-6 giờ",
            "protein_binding": "10%",
            "clearance": "Gan (chuyển hóa qua sulfation, một phần qua CYP450), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.",
        "black_box_warnings": "Không dùng đơn độc cho hen phế quản mạn tính - phải kết hợp với corticosteroid dạng hít. Dùng quá mức (>4 lần/ngày) có thể gây tăng nguy cơ tử vong do hen. Nếu cần dùng thường xuyên → cần đánh giá lại và tăng điều trị kiểm soát."
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
        "pregnancy": "C",
        "mechanism_of_action": "Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng dài (12 giờ) do liên kết chặt với receptor, giải phóng chậm. Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch. Giảm phóng thích chất trung gian gây viêm từ mast cells. Dùng để phòng ngừa, không dùng để cắt cơn (tác dụng chậm).",
        "monitoring": [
            "Nhịp tim, huyết áp (đặc biệt khi bắt đầu điều trị)",
            "Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa",
            "Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp",
            "Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)",
            "Tần suất dùng SABA (nếu tăng → cần đánh giá lại điều trị)"
        ],
        "precautions": [
            "PHẢI dùng kết hợp với ICS (inhaled corticosteroid) - không bao giờ dùng đơn độc cho hen phế quản",
            "Không dùng để cắt cơn (tác dụng chậm, không hiệu quả) - cần có SABA để cắt cơn",
            "Không dùng đơn độc cho hen phế quản cấp - nguy cơ tăng tử vong",
            "Tránh dùng với beta-blocker (đối kháng tác dụng)",
            "Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)",
            "Dùng đều đặn 2 lần/ngày (sáng và tối) để phòng ngừa",
            "Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng",
            "Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị và tăng ICS",
            "Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "5.5 giờ (dài hơn salbutamol)",
            "onset": "15-30 phút (chậm hơn SABA)",
            "duration": "12 giờ (dài)",
            "protein_binding": "96%",
            "clearance": "Gan (chuyển hóa qua CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.",
        "black_box_warnings": "KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen. Không dùng để cắt cơn hen cấp (tác dụng chậm). Chỉ dùng để phòng ngừa và phải luôn có SABA để cắt cơn."
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
        "pregnancy": "B",
        "mechanism_of_action": "Anticholinergic - ức chế muscarinic receptors (M1, M2, M3) ở cơ trơn phế quản, giảm acetylcholine-mediated co thắt phế quản. Giãn cơ trơn phế quản, giảm tiết dịch đường hô hấp. Không hấp thu hệ thống đáng kể khi dùng dạng hít (do ion hóa) → ít tác dụng phụ hệ thống hơn atropine. Tác dụng ngắn (4-6 giờ). An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích beta-1 receptors).",
        "monitoring": [
            "Đáp ứng phế quản (peak flow, FEV1)",
            "Nhịp tim, huyết áp (ít tác dụng tim mạch hơn beta-agonist)",
            "Dấu hiệu kích ứng mắt (nếu vào mắt - tăng nhãn áp, đỏ mắt)",
            "Dấu hiệu tăng nhãn áp (đau mắt, nhìn mờ) - đặc biệt ở bệnh nhân glaucoma",
            "Dấu hiệu bí tiểu (khó tiểu, đầy bụng) - hiếm nhưng cần chú ý",
            "Dấu hiệu khô miệng nặng (có thể ảnh hưởng sức khỏe răng miệng)"
        ],
        "precautions": [
            "Rửa miệng sau khi dùng để giảm kích ứng và tránh thuốc vào mắt",
            "Tránh để thuốc vào mắt (có thể gây tăng nhãn áp, đặc biệt ở bệnh nhân glaucoma)",
            "Thận trọng ở bệnh nhân glaucoma góc đóng (chống chỉ định) hoặc tăng nhãn áp",
            "Thận trọng ở bệnh nhân phì đại tuyến tiền liệt (có thể gây bí tiểu)",
            "Kết hợp với beta-agonist (SABA) cho hiệu quả tốt hơn - hiệp đồng tác dụng",
            "Dùng đều đặn cho COPD, dùng khi cần cho hen (kết hợp với SABA)",
            "Dạng hít: sử dụng đúng kỹ thuật để đạt hiệu quả tối đa",
            "Dạng nebulizer: phù hợp cho bệnh nhân không thể dùng dạng hít",
            "An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích tim)"
        ],
        "pharmacokinetics": {
            "half_life": "2 giờ",
            "onset": "15-30 phút (chậm hơn SABA)",
            "duration": "4-6 giờ",
            "protein_binding": "Không đáng kể (ion hóa, không hấp thu hệ thống)",
            "clearance": "Chủ yếu tại chỗ (phế quản), không chuyển hóa đáng kể"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.",
        "black_box_warnings": "Tránh để thuốc vào mắt - có thể gây tăng nhãn áp, đặc biệt nguy hiểm ở bệnh nhân glaucoma góc đóng. Rửa miệng sau khi dùng để tránh thuốc vào mắt."
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
        "pregnancy": "C",
        "mechanism_of_action": "Anticholinergic dài tác dụng - ức chế muscarinic receptors (M1, M2, M3) ở cơ trơn phế quản, giảm acetylcholine-mediated co thắt phế quản. Giãn cơ trơn phế quản, giảm tiết dịch đường hô hấp. Liên kết chặt với M3 receptors (chủ yếu) và M1 receptors, giải phóng chậm → tác dụng kéo dài 24 giờ. Không hấp thu hệ thống đáng kể khi dùng dạng hít (do ion hóa) → ít tác dụng phụ hệ thống. Tác dụng dài hơn ipratropium (4-6 giờ so với 24 giờ). An toàn hơn beta-agonist cho bệnh nhân tim mạch.",
        "monitoring": [
            "Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa",
            "Nhịp tim, huyết áp (ít tác dụng tim mạch hơn beta-agonist)",
            "Dấu hiệu kích ứng mắt (nếu vào mắt - tăng nhãn áp, đỏ mắt)",
            "Dấu hiệu tăng nhãn áp (đau mắt, nhìn mờ) - đặc biệt ở bệnh nhân glaucoma",
            "Dấu hiệu bí tiểu (khó tiểu, đầy bụng) - đặc biệt ở bệnh nhân phì đại tuyến tiền liệt",
            "Dấu hiệu khô miệng nặng (có thể ảnh hưởng sức khỏe răng miệng)",
            "Chức năng thận (thải qua thận, tích lũy ở suy thận)"
        ],
        "precautions": [
            "Rửa miệng sau khi dùng để giảm kích ứng và tránh thuốc vào mắt",
            "Tránh để thuốc vào mắt (có thể gây tăng nhãn áp, đặc biệt ở bệnh nhân glaucoma)",
            "Thận trọng ở bệnh nhân glaucoma góc đóng (chống chỉ định) hoặc tăng nhãn áp",
            "Thận trọng ở bệnh nhân phì đại tuyến tiền liệt nặng (có thể gây bí tiểu)",
            "Thận trọng ở suy thận (thải qua thận, tích lũy) - tránh dùng nếu CrCl <30",
            "Dùng 1 lần/ngày với HandiHaler (18mcg) hoặc 2 lần/ngày với Respimat (5mcg)",
            "Kết hợp với ICS cho hen phế quản nếu không kiểm soát",
            "Dạng hít: sử dụng đúng kỹ thuật để đạt hiệu quả tối đa",
            "An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích tim)",
            "Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn"
        ],
        "pharmacokinetics": {
            "half_life": "5-6 ngày (rất dài, do liên kết chặt với receptor)",
            "onset": "30-60 phút",
            "duration": "24 giờ (dài)",
            "protein_binding": "72%",
            "clearance": "Thận (thải qua thận, tích lũy ở suy thận)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. HandiHaler: bảo quản trong bao bì gốc. Kiểm tra hạn sử dụng định kỳ.",
        "black_box_warnings": "Tránh để thuốc vào mắt - có thể gây tăng nhãn áp, đặc biệt nguy hiểm ở bệnh nhân glaucoma góc đóng. Rửa miệng sau khi dùng để tránh thuốc vào mắt. Thận trọng ở suy thận - tích lũy có thể gây tăng tác dụng phụ."
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
        "pregnancy": "D",
        "mechanism_of_action": "Thuốc chống co giật và ổn định tâm trạng. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh, ngăn cản sự lan truyền của các xung động bất thường. Cũng có thể ức chế giải phóng glutamate và điều hòa dòng calci. Tự cảm ứng enzyme (auto-induction) - tăng chuyển hóa của chính nó và các thuốc khác. Được dùng trong điều trị co giật cục bộ, co giật toàn thể, đau dây thần kinh sinh ba (trigeminal neuralgia), và rối loạn lưỡng cực. Có nhiều tương tác thuốc do cảm ứng enzyme.",
        "monitoring": [
            "Nồng độ carbamazepine trong máu (therapeutic range: 4-12 mcg/ml) - QUAN TRỌNG",
            "Tần suất và mức độ co giật",
            "Dấu hiệu độc tính (chóng mặt, ataxia, lú lẫn, buồn nôn)",
            "Công thức máu (giảm bạch cầu, giảm tiểu cầu, thiếu máu bất sản - nguy hiểm)",
            "Dấu hiệu hội chứng Stevens-Johnson (phát ban nặng) - nguy hiểm",
            "Chức năng gan (ALT, AST) - có thể tăng men gan, hiếm viêm gan",
            "Nồng độ natri (hạ natri máu - thường gặp)",
            "Chức năng thận"
        ],
        "precautions": [
            "Tuân thủ chặt chẽ liều và lịch dùng",
            "KHÔNG được ngừng đột ngột (nguy cơ co giật)",
            "Nồng độ trong máu cần được theo dõi định kỳ",
            "Nguy cơ giảm bạch cầu, giảm tiểu cầu, thiếu máu bất sản (nguy hiểm) - theo dõi công thức máu",
            "Nguy cơ hội chứng Stevens-Johnson - ngừng ngay nếu có phát ban",
            "Hạ natri máu thường gặp - theo dõi natri",
            "Tự cảm ứng enzyme → liều cần tăng dần theo thời gian",
            "Tương tác với nhiều thuốc: giảm hiệu quả thuốc tránh thai, warfarin, và các thuốc khác (do cảm ứng enzyme)",
            "Tương tác với nhiều thuốc: tăng nồng độ với erythromycin, cimetidine (do ức chế enzyme)",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Thận trọng ở suy gan"
        ],
        "pharmacokinetics": {
            "half_life": "25-65 giờ (bình thường), giảm xuống 12-17 giờ sau khi tự cảm ứng enzyme",
            "onset": "Vài giờ đến vài ngày",
            "duration": "Dài (phụ thuộc liều)",
            "protein_binding": "75%",
            "metabolism": "Gan (CYP3A4) - tự cảm ứng enzyme, cũng cảm ứng các enzyme khác",
            "clearance": "Gan, bị ảnh hưởng bởi tự cảm ứng và các thuốc tương tác"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Nguy cơ hội chứng Stevens-Johnson và hoại tử thượng bì nhiễm độc (TEN), có thể tử vong. Nguy cơ thiếu máu bất sản và giảm bạch cầu nghiêm trọng. Ngừng ngay nếu có phát ban hoặc dấu hiệu giảm bạch cầu. Nguy cơ tự sát và hành vi tự sát. Ngừng đột ngột có thể gây co giật."

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
          "pregnancy": "C",
          "mechanism_of_action": "Xanthine oxidase inhibitor. Ức chế enzyme xanthine oxidase, enzyme chuyển hypoxanthine thành xanthine và xanthine thành acid uric. Giảm sản xuất acid uric, giảm nồng độ acid uric trong máu và nước tiểu. Được dùng để điều trị gout mạn tính và phòng ngừa tăng acid uric máu (ví dụ trong hóa trị).",
          "monitoring": [
              "Nồng độ acid uric máu (mục tiêu <6 mg/dL)",
              "Chức năng thận: creatinine, BUN (thải qua thận)",
              "Chức năng gan: ALT, AST (có thể gây tăng men gan)",
              "Dấu hiệu ban da (QUAN TRỌNG - có thể tiến triển thành SJS/TEN nếu nặng)",
              "Triệu chứng gout cấp (có thể xảy ra khi bắt đầu điều trị - cần dùng colchicine dự phòng)"
          ],
          "precautions": [
              "KHỞI ĐẦU với liều thấp (100mg/ngày), tăng dần mỗi 1-2 tuần để tránh cơn gout cấp",
              "Dùng kèm colchicine hoặc NSAID khi bắt đầu để dự phòng cơn gout cấp (1-2 tháng đầu)",
              "NGỪNG NGAY nếu có ban da - có thể tiến triển thành SJS/TEN (đe dọa tính mạng)",
              "Tránh dùng với ampicillin/amoxicillin (tăng nguy cơ ban da nặng)",
              "Thận trọng khi dùng với azathioprine/6-mercaptopurine (tăng độc tính - cần giảm liều 75%)",
              "Thận trọng khi dùng với warfarin (tăng tác dụng chống đông - theo dõi INR)",
              "Thận trọng ở bệnh nhân suy thận (giảm liều)",
              "Uống với nhiều nước để tránh sỏi thận"
          ],
          "pharmacokinetics": {
              "half_life": "1-2 giờ (allopurinol), 15-18 giờ (metabolite oxypurinol - hoạt chất)",
              "onset": "1-2 tuần (giảm acid uric máu)",
              "duration": "24 giờ (uống 1 lần/ngày)",
              "protein_binding": "Rất ít",
              "clearance": "Thận (chủ yếu, allopurinol và oxypurinol thải qua nước tiểu). Cần giảm liều ở suy thận"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "Có thể gây phản ứng da nghiêm trọng (ban da, SJS, TEN) đe dọa tính mạng. Ngừng ngay nếu có ban da. Nguy cơ tăng ở bệnh nhân suy thận, dùng đồng thời với ampicillin/amoxicillin, hoặc có tiền sử dị ứng allopurinol"
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
        "pregnancy": "C",
        "mechanism_of_action": "Glucocorticoid tổng hợp, tác dụng trung bình. Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm, ức chế phospholipase A2 → giảm prostaglandin và leukotriene. Có tác dụng mineralocorticoid nhẹ (ít hơn hydrocortisone). Ức chế miễn dịch. Được dùng trong nhiều tình trạng viêm và tự miễn. Tác dụng tương tự prednisone nhưng prednisolone là dạng hoạt động (không cần chuyển hóa ở gan).",
        "monitoring": [
            "Đường huyết (tăng đường huyết, đặc biệt ở bệnh nhân đái tháo đường)",
            "Huyết áp (tăng huyết áp)",
            "Điện giải (natri, kali)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Dạ dày (dấu hiệu loét, xuất huyết)",
            "Tâm thần (rối loạn tâm thần, mất ngủ, kích động)",
            "Xương (loãng xương nếu dùng kéo dài)",
            "Mắt (tăng nhãn áp, đục thủy tinh thể)",
            "Chức năng thượng thận (ức chế trục HPA nếu dùng kéo dài)"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột nếu dùng > 1 tuần (có thể gây suy thượng thận cấp - nguy hiểm tính mạng)",
            "Phải giảm liều dần dần (tapering) nếu dùng > 1 tuần",
            "Ức chế miễn dịch - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm nấm, lao",
            "Không dùng trong nhiễm nấm hệ thống không điều trị",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Thận trọng ở bệnh nhân loét dạ dày (tăng nguy cơ)",
            "Thận trọng ở bệnh nhân tăng huyết áp",
            "Dùng với thức ăn để giảm kích ứng dạ dày",
            "Dự phòng loãng xương nếu dùng kéo dài (bổ sung calcium, vitamin D)",
            "Theo dõi dấu hiệu nhiễm trùng (ức chế miễn dịch có thể che dấu triệu chứng)",
            "Liều thay thế: 5-7.5mg/ngày, liều chống viêm: 20-60mg/ngày"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (ngắn, nhưng tác dụng kéo dài hơn do tác động gen)",
            "onset": "1-2 giờ (PO)",
            "duration": "18-36 giờ",
            "protein_binding": "90-95%",
            "metabolism": "Gan (CYP3A4) - prednisolone là dạng hoạt động (khác prednisone)",
            "clearance": "Gan, không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ngừng đột ngột sau khi dùng kéo dài có thể gây suy thượng thận cấp, có thể tử vong. Ức chế miễn dịch mạnh có thể làm nặng nhiễm trùng hoặc gây nhiễm trùng cơ hội."

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
        "pregnancy": "D - Nguy cơ dị tật thai nhi",
        "mechanism_of_action": "Thuốc chống co giật, ổn định màng tế bào. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh, ngăn cản sự lan truyền của các xung động bất thường. Chỉ tác động lên các tế bào đang hoạt động mạnh (như trong co giật), không ảnh hưởng đến hoạt động bình thường. Điều hòa dòng calci và có thể ức chế giải phóng glutamate. Được dùng trong điều trị co giật cục bộ, co giật toàn thể, và status epilepticus. Cũng được dùng trong rối loạn nhịp tim (nhưng ít dùng hơn).",
        "monitoring": [
            "Nồng độ phenytoin trong máu (therapeutic range: 10-20 mcg/ml, free: 1-2 mcg/ml) - QUAN TRỌNG",
            "Tần suất và mức độ co giật",
            "Dấu hiệu độc tính (nystagmus ở >20 mcg/ml, ataxia ở >30 mcg/ml, lú lẫn ở >40 mcg/ml)",
            "Chức năng gan (ALT, AST, bilirubin) - có thể tăng men gan, hiếm viêm gan nặng",
            "Công thức máu (giảm bạch cầu, giảm tiểu cầu, thiếu máu megaloblastic do thiếu folate)",
            "Nồng độ folate và vitamin D (phenytoin làm giảm)",
            "Chức năng thận (creatinine)",
            "Dấu hiệu hội chứng Stevens-Johnson (phát ban nặng) - nguy hiểm",
            "Răng và nướu (tăng sản nướu)",
            "Xương (loãng xương do giảm vitamin D)"
        ],
        "precautions": [
            "Tuân thủ chặt chẽ liều và lịch dùng - bỏ liều có thể gây co giật",
            "KHÔNG được ngừng đột ngột (nguy cơ status epilepticus)",
            "Nồng độ trong máu cần được theo dõi định kỳ - có mối quan hệ không tuyến tính (saturable kinetics)",
            "Liều tăng nhỏ có thể làm nồng độ tăng rất nhiều ở liều cao (Michaelis-Menten kinetics)",
            "Tương tác với nhiều thuốc: giảm hiệu quả thuốc tránh thai, warfarin (cả hai đều tăng hoặc giảm tùy thuốc)",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Không nghiền viên nang hoặc viên nén (giảm hấp thu)",
            "Bổ sung folate và vitamin D khi dùng kéo dài",
            "Nguy cơ hội chứng Stevens-Johnson - ngừng ngay nếu có phát ban",
            "Thận trọng ở suy gan (giảm chuyển hóa)",
            "Liều IV: truyền chậm (không quá 50mg/phút) để tránh hạ huyết áp, rối loạn nhịp",
            "Không pha trong D5W (kết tủa), chỉ dùng NS"
        ],
        "pharmacokinetics": {
            "half_life": "22 giờ (bình thường), dài hơn ở liều cao (saturable kinetics)",
            "onset": "30-60 phút (PO), 15-30 phút (IV)",
            "duration": "Dài (phụ thuộc liều)",
            "protein_binding": "90% (rất cao), chỉ free phenytoin mới hoạt động",
            "metabolism": "Gan (CYP2C9, CYP2C19) - chuyển hóa mạnh",
            "clearance": "Gan, có thể bị ảnh hưởng bởi tình trạng dinh dưỡng, tuổi tác"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản ở nhiệt độ phòng, không đông lạnh, chỉ dùng NS để pha.",
        "black_box_warnings": "Nguy cơ hội chứng Stevens-Johnson và hoại tử thượng bì nhiễm độc (TEN), có thể tử vong. Ngừng ngay nếu có phát ban. Nguy cơ tự sát và hành vi tự sát. Giảm bạch cầu, giảm tiểu cầu có thể nặng. Ngừng đột ngột có thể gây status epilepticus."

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
        "pregnancy": "C",
        "mechanism_of_action": "Thuốc chống co giật thế hệ mới, cơ chế chưa hoàn toàn rõ ràng. Gắn với protein SV2A (synaptic vesicle protein 2A) trong tế bào thần kinh, ức chế giải phóng chất dẫn truyền thần kinh từ túi synap, giảm hoạt động bất thường của tế bào thần kinh. Không ức chế kênh natri hoặc calci như các thuốc chống co giật cổ điển. Có phổ rộng: hiệu quả với co giật cục bộ và co giật toàn thể. Được dùng như thuốc bổ trợ hoặc đơn trị liệu. Ít tương tác thuốc hơn phenytoin.",
        "monitoring": [
            "Tần suất và mức độ co giật",
            "Tâm thần (kích động, lo âu, trầm cảm, suy nghĩ tự sát) - tác dụng phụ thần kinh tâm thần quan trọng",
            "Dấu hiệu hành vi bất thường (thay đổi tâm trạng, kích động)",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận",
            "Công thức máu (hiếm giảm bạch cầu, giảm tiểu cầu)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Mệt mỏi, chóng mặt (thường gặp)",
            "Dấu hiệu nhiễm trùng (hiếm giảm bạch cầu)"
        ],
        "precautions": [
            "Tác dụng phụ thần kinh tâm thần: kích động, lo âu, trầm cảm, suy nghĩ tự sát - theo dõi sát, đặc biệt ở trẻ em và thanh thiếu niên",
            "Nguy cơ hành vi tự sát - cảnh báo bệnh nhân và gia đình",
            "KHÔNG được ngừng đột ngột (nguy cơ co giật)",
            "Phải điều chỉnh liều ở suy thận (giảm liều và tăng khoảng cách liều)",
            "Khởi đầu với liều thấp, tăng dần để giảm tác dụng phụ",
            "Có thể gây mệt mỏi, chóng mặt - thận trọng khi lái xe, vận hành máy móc",
            "Tương tác thuốc ít hơn các thuốc chống co giật cổ điển (không ức chế CYP450)",
            "Có thể dùng với hoặc không có thức ăn",
            "Thận trọng ở bệnh nhân có tiền sử bệnh tâm thần",
            "Giảm liều ở người cao tuổi (nếu có suy thận)"
        ],
        "pharmacokinetics": {
            "half_life": "6-8 giờ (bình thường), 10-11 giờ (suy thận nặng)",
            "onset": "Nhanh (vài giờ đến vài ngày)",
            "duration": "Dài (phụ thuộc liều)",
            "protein_binding": "< 10% (rất thấp)",
            "metabolism": "Enzyme huyết tương (không qua CYP450) - ít tương tác",
            "clearance": "Chủ yếu qua thận (66% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Viên nén: tránh ẩm.",
        "black_box_warnings": "Nguy cơ hành vi tự sát và ý tưởng tự sát. Cảnh báo bệnh nhân và gia đình về các dấu hiệu kích động, lo âu, trầm cảm, thay đổi tâm trạng, và hành vi bất thường. Ngừng đột ngột có thể gây co giật."

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
        "pregnancy": "C",
        "mechanism_of_action": "Glucocorticoid tổng hợp tác dụng dài và mạnh (tương đương 25-30mg hydrocortisone). Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm, ức chế phospholipase A2 → giảm prostaglandin và leukotriene. Ức chế miễn dịch mạnh. Tác dụng chống viêm và ức chế miễn dịch mạnh hơn hydrocortisone. Thời gian bán thải dài (36-72 giờ) do ít gắn với protein hơn hydrocortisone.",
        "monitoring": [
            "Đường huyết (tăng đường huyết, đặc biệt ở bệnh nhân đái tháo đường)",
            "Huyết áp (tăng huyết áp)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Điện giải (hạ kali, giữ natri)",
            "Tâm thần (rối loạn tâm thần, mất ngủ, kích động)",
            "Dạ dày (dấu hiệu loét, xuất huyết)",
            "Xương (loãng xương nếu dùng kéo dài)",
            "Mắt (tăng nhãn áp, đục thủy tinh thể)",
            "Chức năng thượng thận (ức chế trục HPA nếu dùng kéo dài)"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột nếu dùng > 1 tuần (có thể gây suy thượng thận cấp - nguy hiểm tính mạng)",
            "Phải giảm liều dần dần (tapering) nếu dùng > 1 tuần",
            "Ức chế miễn dịch mạnh - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm nấm, lao",
            "Không dùng trong nhiễm nấm hệ thống không điều trị (có thể làm nặng)",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Thận trọng ở bệnh nhân loét dạ dày (tăng nguy cơ)",
            "Thận trọng ở bệnh nhân tăng huyết áp (có thể tăng huyết áp)",
            "Dùng với thức ăn để giảm kích ứng dạ dày",
            "Dự phòng loãng xương nếu dùng kéo dài (bổ sung calcium, vitamin D)",
            "Theo dõi dấu hiệu nhiễm trùng (ức chế miễn dịch có thể che dấu triệu chứng)",
            "Thời gian bán thải dài → ức chế trục HPA lâu hơn hydrocortisone"
        ],
        "pharmacokinetics": {
            "half_life": "36-72 giờ (rất dài)",
            "onset": "1-2 giờ (PO/IV)",
            "duration": "36-72 giờ",
            "protein_binding": "77% (thấp hơn hydrocortisone)",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ngừng đột ngột sau khi dùng kéo dài có thể gây suy thượng thận cấp, có thể tử vong. Ức chế miễn dịch mạnh có thể làm nặng nhiễm trùng hoặc gây nhiễm trùng cơ hội."
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
        "pregnancy": "C",
        "mechanism_of_action": "Glucocorticoid tự nhiên (cortisol), tác dụng ngắn. Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm, ức chế phospholipase A2. Có tác dụng mineralocorticoid (giữ natri, thải kali) - mạnh hơn dexamethasone. Được dùng trong suy thượng thận để thay thế cortisol thiếu hụt. Tác dụng chống viêm và ức chế miễn dịch yếu hơn dexamethasone nhưng có tác dụng mineralocorticoid.",
        "monitoring": [
            "Đường huyết (tăng đường huyết)",
            "Huyết áp (tăng huyết áp, đặc biệt do giữ natri)",
            "Điện giải (natri, kali - giữ natri, thải kali)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Dạ dày (dấu hiệu loét, xuất huyết)",
            "Dấu hiệu suy thượng thận nếu ngừng đột ngột (mệt mỏi, hạ huyết áp, hạ natri máu)",
            "Dấu hiệu Cushing nếu dùng liều cao kéo dài",
            "Xương (loãng xương nếu dùng kéo dài)"
        ],
        "precautions": [
            "Trong suy thượng thận: KHÔNG được quên liều hoặc ngừng đột ngột (có thể gây suy thượng thận cấp - nguy hiểm tính mạng)",
            "Tăng liều trong stress (phẫu thuật, nhiễm trùng nặng) - cần tăng gấp 2-3 lần liều thay thế",
            "Giữ natri mạnh hơn dexamethasone → cần theo dõi natri, kali",
            "Không dùng trong nhiễm nấm hệ thống không điều trị",
            "Thận trọng ở bệnh nhân suy tim (giữ natri → phù)",
            "Thận trọng ở bệnh nhân tăng huyết áp (giữ natri → tăng huyết áp)",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Dùng với thức ăn để giảm kích ứng dạ dày",
            "Thời gian bán thải ngắn → cần chia liều trong ngày (2-3 lần/ngày) cho thay thế",
            "Trong stress dosing: dùng liều cao IV mỗi 6-8 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "8-12 giờ",
            "onset": "IV: 1 giờ; PO: 1-2 giờ",
            "duration": "8-12 giờ",
            "protein_binding": "90-95% (cao)",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng bột pha tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, trong suy thượng thận, quên liều hoặc ngừng đột ngột có thể gây suy thượng thận cấp, có thể tử vong. Trong stress, không tăng liều có thể dẫn đến suy thượng thận cấp."
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
        "pregnancy": "C",
        "mechanism_of_action": "Glucocorticoid tổng hợp tác dụng dài và mạnh (tương đương 25-30mg hydrocortisone, mạnh hơn dexamethasone một chút). Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm. Ức chế miễn dịch mạnh. Có tác dụng mineralocorticoid tối thiểu (ít hơn hydrocortisone và dexamethasone). Được dùng trong nhiều tình trạng viêm và tự miễn. Thường dùng để thúc đẩy trưởng thành phổi ở thai nhi (khi có nguy cơ sinh non).",
        "monitoring": [
            "Đường huyết (tăng đường huyết)",
            "Huyết áp (tăng huyết áp)",
            "Điện giải (natri, kali)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Dạ dày (dấu hiệu loét)",
            "Tâm thần (rối loạn tâm thần)",
            "Xương (loãng xương nếu dùng kéo dài)",
            "Mắt (tăng nhãn áp, đục thủy tinh thể)",
            "Trong thai kỳ: theo dõi thai nhi nếu dùng để thúc đẩy trưởng thành phổi"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột nếu dùng > 1 tuần (có thể gây suy thượng thận cấp)",
            "Phải giảm liều dần dần (tapering) nếu dùng > 1 tuần",
            "Ức chế miễn dịch mạnh - tăng nguy cơ nhiễm trùng",
            "Không dùng trong nhiễm nấm hệ thống không điều trị",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Thận trọng ở bệnh nhân loét dạ dày",
            "Dùng với thức ăn để giảm kích ứng dạ dày",
            "Dự phòng loãng xương nếu dùng kéo dài",
            "Trong thai kỳ: có thể dùng để thúc đẩy trưởng thành phổi (24-34 tuần) nhưng thận trọng",
            "Theo dõi dấu hiệu nhiễm trùng"
        ],
        "pharmacokinetics": {
            "half_life": "36-54 giờ (rất dài)",
            "onset": "1-2 giờ (PO/IM)",
            "duration": "36-54 giờ",
            "protein_binding": "64% (thấp hơn hydrocortisone)",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ngừng đột ngột sau khi dùng kéo dài có thể gây suy thượng thận cấp, có thể tử vong. Ức chế miễn dịch mạnh có thể làm nặng nhiễm trùng."

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
          "pregnancy": "B",
          "mechanism_of_action": "Macrolide antibiotic. Ức chế tổng hợp protein vi khuẩn bằng cách gắn vào 50S ribosomal subunit, ức chế peptide chain elongation. Phổ tác dụng: Gram-positive (Streptococcus, Staphylococcus), một số Gram-negative (Haemophilus influenzae), atypical pathogens (Mycoplasma, Chlamydia, Legionella). Có tác dụng kéo dài do thời gian bán hủy dài (68 giờ), cho phép phác đồ ngắn (3-5 ngày).",
          "monitoring": [
              "ECG: QT interval (có thể gây QT kéo dài, đặc biệt ở bệnh nhân có yếu tố nguy cơ)",
              "Triệu chứng rối loạn nhịp tim (torsades de pointes - hiếm nhưng nguy hiểm)",
              "Chức năng gan: ALT, AST (hiếm gây độc gan)",
              "Triệu chứng tiêu hóa: buồn nôn, nôn, tiêu chảy (phổ biến)",
              "Rối loạn thính giác (hiếm, thường ở liều cao hoặc dùng lâu dài)"
          ],
          "precautions": [
              "Tránh dùng ở bệnh nhân QT kéo dài hoặc có yếu tố nguy cơ (suy tim, hạ kali máu, hạ magie máu, dùng thuốc QT kéo dài khác)",
              "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu - theo dõi INR)",
              "Thận trọng khi dùng với digoxin (tăng nồng độ digoxin - theo dõi nồng độ)",
              "Thận trọng khi dùng với cyclosporine (tăng nồng độ cyclosporine)",
              "Có thể gây tiêu chảy (phổ biến) - có thể dẫn đến C. difficile colitis nếu nặng",
              "Thận trọng ở bệnh nhân suy gan nặng"
          ],
          "pharmacokinetics": {
              "half_life": "68 giờ (RẤT DÀI - cho phép phác đồ ngắn 3-5 ngày)",
              "onset": "2-3 giờ (PO), 1 giờ (IV)",
              "duration": "5-7 ngày sau liều cuối (do half-life dài)",
              "protein_binding": "7-50% (thay đổi theo nồng độ)",
              "clearance": "Chủ yếu qua phân (không đổi), một phần qua gan. Không phụ thuộc vào chức năng thận (không cần điều chỉnh liều ở suy thận)"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Bảo quản suspension trong tủ lạnh sau khi pha",
          "black_box_warnings": "Có thể gây QT kéo dài và torsades de pointes, đặc biệt ở bệnh nhân có yếu tố nguy cơ (suy tim, hạ kali máu, hạ magie máu, nhịp tim chậm, dùng thuốc QT kéo dài khác). Tránh dùng ở bệnh nhân QT kéo dài"
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
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Fluoroquinolone kháng sinh phổ rộng. Ức chế DNA gyrase (ở vi khuẩn Gram-âm) và topoisomerase IV (ở vi khuẩn Gram-dương), enzyme cần thiết cho sao chép và sửa chữa DNA. Dẫn đến tổn thương DNA và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, H. influenzae, Neisseria), một số Gram-dương (không phải MRSA), và một số vi khuẩn không điển hình (Legionella, Mycoplasma). Kháng thuốc phát triển nhanh nếu dùng không đúng.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles)",
            "Thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm)",
            "Tim mạch (QT kéo dài, rối loạn nhịp tim)",
            "Đường huyết (tăng hoặc hạ đường huyết - đặc biệt với sulfonylurea)",
            "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
            "Chức năng gan (ALT, AST) - hiếm viêm gan nặng"
        ],
        "precautions": [
            "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc",
            "Nguy cơ tăng ở: > 60 tuổi, dùng corticosteroid, ghép thận, ghép tim, phổi, hoạt động thể lực",
            "NGỪNG NGAY nếu có đau, sưng gân",
            "QT kéo dài → không dùng với các thuốc kéo dài QT khác, bệnh nhân có tiền sử rối loạn nhịp",
            "Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng",
            "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm (cách 2 giờ)",
            "Hạ đường huyết → thận trọng với sulfonylurea",
            "Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn",
            "Tránh dùng với sữa, sản phẩm sữa (giảm hấp thu)",
            "Uống nhiều nước để tránh kết tinh trong nước tiểu"
        ],
        "pharmacokinetics": {
            "half_life": "4 giờ (bình thường), 5-7 giờ (suy thận)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q12h (PO/IV), q8h cho Pseudomonas",
            "protein_binding": "20-40%",
            "metabolism": "Gan (CYP1A2) - một phần",
            "clearance": "Chủ yếu qua thận (40-60% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Tăng nguy cơ viêm gân và đứt gân ở mọi lứa tuổi. Nguy cơ tăng ở bệnh nhân > 60 tuổi, dùng corticosteroid, ghép cơ quan. Nguy cơ tổn thương thần kinh ngoại biên không hồi phục. Nguy cơ tác dụng phụ nghiêm trọng về gân, cơ, khớp, và thần kinh có thể xảy ra cùng lúc. Nguy cơ làm nặng bệnh nhược cơ. Tăng nguy cơ rối loạn tâm thần và hành vi tự sát."

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
        "pregnancy": "D - Chống chỉ định trong 3 tháng cuối",
        "mechanism_of_action": "Tetracycline kháng sinh phổ rộng. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 30S của ribosome, ngăn cản gắn aminoacyl-tRNA. Phổ kháng khuẩn: Gram-dương, Gram-âm, vi khuẩn không điển hình (Chlamydia, Mycoplasma, Rickettsia, Borrelia), và một số ký sinh trùng (Plasmodium). Không hiệu quả với Pseudomonas hoặc Proteus. Đặc biệt hiệu quả với vi khuẩn không điển hình và được dùng trong nhiễm trùng đường hô hấp, Lyme disease, và sốt rét.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dạ dày-ruột (buồn nôn, nôn, tiêu chảy, viêm thực quản)",
            "Da (tăng độ nhạy cảm với ánh sáng, phát ban)",
            "Răng và xương (ở trẻ em < 8 tuổi: ố vàng răng vĩnh viễn, chậm phát triển xương)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan, tăng áp lực nội sọ giả (ở phụ nữ)",
            "Thận (không tích lũy ở suy thận, nhưng theo dõi)"
        ],
        "precautions": [
            "KHÔNG dùng cho trẻ em < 8 tuổi (trừ trường hợp đe dọa tính mạng) - gây ố vàng răng vĩnh viễn, chậm phát triển xương",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng, mặc quần áo che phủ",
            "Uống với nhiều nước (ít nhất 200ml) và ở tư thế đứng để tránh viêm thực quản (đau khi nuốt, khó nuốt)",
            "KHÔNG uống nằm ngửa hoặc trước khi ngủ",
            "Tương tác với nhiều thuốc và thực phẩm: giảm hấp thu với antacid, sắt, canxi, magie, kẽm, sữa (cách 2 giờ)",
            "Tương tác với warfarin → tăng nguy cơ chảy máu (theo dõi INR)",
            "Tương tác với thuốc tránh thai → giảm hiệu quả (dùng biện pháp tránh thai khác)",
            "Tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị) - đặc biệt ở phụ nữ, ngừng nếu có",
            "Không dùng trong 3 tháng cuối thai kỳ (nguy cơ ố vàng răng, chậm phát triển xương ở trẻ)",
            "Uống với thức ăn để giảm kích ứng dạ dày (nhưng giảm hấp thu một phần)"
        ],
        "pharmacokinetics": {
            "half_life": "18-22 giờ (dài)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q12h hoặc q24h (PO/IV)",
            "protein_binding": "80-90%",
            "metabolism": "Gan (một phần), bài tiết một phần nguyên dạng",
            "clearance": "Gan và thận, KHÔNG tích lũy ở suy thận (khác với tetracycline cũ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nang: tránh ẩm. Bảo quản tốt hơn các tetracycline cũ (ít bị hỏng).",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ố vàng răng vĩnh viễn ở trẻ em < 8 tuổi là không hồi phục. Tăng áp lực nội sọ giả có thể gây mù. Viêm thực quản có thể nghiêm trọng."

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
        "pregnancy": "B - D trong 3 tháng đầu",
        "mechanism_of_action": "Nitroimidazole kháng sinh/kháng ký sinh trùng. Sau khi vào tế bào vi khuẩn/ký sinh trùng, bị khử bởi ferredoxin (có trong vi khuẩn kỵ khí và ký sinh trùng) → tạo ra các gốc tự do độc hại phá hủy DNA. Chỉ hoạt động với vi khuẩn kỵ khí (Bacteroides, Clostridium, giardia) và ký sinh trùng (Trichomonas, Giardia, Entamoeba). KHÔNG hoạt động với vi khuẩn hiếu khí. Đặc biệt hiệu quả với kỵ khí và được dùng trong nhiễm trùng bụng, nhiễm trùng phụ khoa, và nhiễm C. difficile.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Thần kinh (dị cảm, co giật, viêm dây thần kinh ngoại biên, chóng mặt, mất điều hòa)",
            "Dạ dày-ruột (buồn nôn, nôn, tiêu chảy, vị kim loại)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Số lượng bạch cầu (hiếm giảm bạch cầu)",
            "Phản ứng Disulfiram-like nếu uống rượu (buồn nôn, nôn, đỏ bừng, nhịp tim nhanh)"
        ],
        "precautions": [
            "TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng thuốc - gây phản ứng Disulfiram-like nặng (buồn nôn, nôn, đỏ bừng, nhịp tim nhanh, hạ huyết áp)",
            "Nguy cơ tổn thương thần kinh ngoại biên và trung ương (dị cảm, co giật, viêm dây thần kinh) - tăng ở dùng kéo dài, liều cao, suy gan",
            "Ngừng nếu có dấu hiệu tổn thương thần kinh",
            "Không dùng cho nhiễm trùng do vi khuẩn hiếu khí (không hiệu quả)",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Vị kim loại rất thường gặp - không phải tác dụng phụ nghiêm trọng nhưng khó chịu",
            "Có thể làm nước tiểu sẫm màu (vô hại)",
            "Thận trọng ở suy gan (giảm chuyển hóa → tăng nguy cơ tác dụng phụ thần kinh)",
            "Không dùng trong 3 tháng đầu thai kỳ (nguy cơ dị tật) - chỉ dùng khi thực sự cần thiết",
            "Pha trong NS, D5W, hoặc LR, truyền IV trong 30-60 phút"
        ],
        "pharmacokinetics": {
            "half_life": "6-8 giờ (bình thường), 9-15 giờ (suy gan)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q8h (PO/IV), q12h cho C. difficile (PO)",
            "protein_binding": "< 20%",
            "metabolism": "Gan (CYP450) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan (60-80%), cần điều chỉnh ở suy gan nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng. Viên nén: tránh ẩm. Dung dịch pha tiêm: sau khi pha, bảo quản ở nhiệt độ phòng 24 giờ, tránh ánh sáng.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, phản ứng Disulfiram-like với rượu có thể nặng. Tổn thương thần kinh có thể không hồi phục. Nguy cơ dị tật thai nhi nếu dùng trong 3 tháng đầu thai kỳ."

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
        "pregnancy": "A - An toàn, cần thiết cho thai kỳ",
        "mechanism_of_action": "Hormone tuyến giáp tổng hợp (T4, thyroxine). Bổ sung hoặc thay thế hormone tuyến giáp thiếu hụt. Trong tế bào, T4 được chuyển đổi thành T3 (triiodothyronine) - dạng hoạt động. T3 gắn với thyroid hormone receptor trong nhân tế bào, điều hòa biểu hiện gen, tăng chuyển hóa cơ bản, tăng nhịp tim, tăng nhiệt độ cơ thể, tăng nhu động ruột, và tăng phát triển tế bào. Được dùng trong suy giáp (hypothyroidism), bướu cổ, và sau phẫu thuật cắt tuyến giáp.",
        "monitoring": [
            "TSH (thyroid stimulating hormone) - mục tiêu: bình thường hóa TSH, kiểm tra mỗi 6-8 tuần khi điều chỉnh liều",
            "Free T4 (FT4) - mục tiêu: trong khoảng bình thường",
            "T3 (nếu cần, trong một số trường hợp)",
            "Nhịp tim và huyết áp (tăng ở quá liều)",
            "Dấu hiệu cường giáp (run, đổ mồ hôi, mất ngủ, nhịp tim nhanh, sụt cân) - dấu hiệu quá liều",
            "Dấu hiệu suy giáp (mệt mỏi, tăng cân, nhịp tim chậm, táo bón, lạnh) - dấu hiệu thiếu liều",
            "Xương (loãng xương nếu quá liều kéo dài)",
            "Tim mạch (rối loạn nhịp tim, đau thắt ngực ở bệnh nhân bệnh mạch vành nếu quá liều)"
        ],
        "precautions": [
            "PHẢI uống vào buổi sáng, khi đói, 30-60 phút trước khi ăn (thức ăn giảm hấp thu 40-60%)",
            "KHÔNG uống cùng với: sắt, canxi, antacid, sucralfate, cholestyramine (cách ít nhất 4 giờ)",
            "Bắt đầu với liều thấp, tăng dần dựa trên TSH",
            "Ở bệnh nhân bệnh mạch vành hoặc người cao tuổi: bắt đầu với liều rất thấp, tăng chậm",
            "Không được ngừng đột ngột (trừ khi có chỉ định)",
            "Liều thay thế: 1.6-1.8 mcg/kg/ngày",
            "TSH mục tiêu: 0.5-2.5 mIU/L (tùy tuổi và tình trạng)",
            "Khi điều chỉnh liều: kiểm tra TSH sau 6-8 tuần (TSH thay đổi chậm)",
            "Quá liều có thể gây cường giáp, rối loạn nhịp tim, đau thắt ngực ở bệnh nhân bệnh mạch vành",
            "Thận trọng ở phụ nữ có thai (nhu cầu tăng 25-50%)",
            "Không dùng để giảm cân (nguy hiểm)"
        ],
        "pharmacokinetics": {
            "half_life": "7 ngày (rất dài)",
            "onset": "3-5 ngày",
            "duration": "Dài (nhiều ngày)",
            "protein_binding": "99.97% (rất cao, gắn với TBG, transthyretin, albumin)",
            "metabolism": "Gan và các mô ngoại vi (deiodination thành T3)",
            "clearance": "Chủ yếu qua gan, một phần qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không được dùng để giảm cân ở bệnh nhân bình giáp. Quá liều có thể gây cường giáp, rối loạn nhịp tim, và đau thắt ngực ở bệnh nhân bệnh mạch vành. Ở bệnh nhân bệnh mạch vành, phải bắt đầu với liều thấp và tăng chậm."

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
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Prednisone là corticosteroid tổng hợp, chuyển hóa thành prednisolone (hoạt chất) trong gan. Gắn với thụ thể glucocorticoid trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (IL-1, IL-2, TNF-α, prostaglandin), giảm di chuyển bạch cầu đến vị trí viêm, ức chế chức năng miễn dịch",
        "monitoring": [
            "Đường huyết (corticosteroid gây tăng đường huyết)",
            "Huyết áp (có thể tăng huyết áp)",
            "Điện giải: K+, Na+ (mất kali, giữ natri)",
            "Cân nặng (giữ nước, tăng cân)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Dấu hiệu loét dạ dày (đau bụng, phân đen)",
            "Mật độ xương nếu dùng lâu dài (loãng xương)",
            "Chức năng thượng thận nếu dùng lâu dài (ACTH, cortisol)",
            "Mắt: đục thủy tinh thể, tăng nhãn áp"
        ],
        "precautions": [
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "GIẢM LIỀU DẦN DẦN khi ngừng (tránh suy thượng thận cấp) - không được ngừng đột ngột",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể",
            "Bổ sung canxi, vitamin D nếu dùng lâu dài (phòng loãng xương)",
            "Cân nhắc bổ sung kali nếu dùng lâu dài",
            "Tránh vaccine sống khi đang dùng corticosteroid",
            "Tăng liều trong stress (phẫu thuật, nhiễm trùng nặng)",
            "Giảm liều khi có nhiễm trùng (nếu có thể)",
            "Theo dõi đường huyết ở bệnh nhân đái tháo đường",
            "Dạy bệnh nhân không tự ý ngừng thuốc"
        ],
        "pharmacokinetics": {
            "half_life": "Prednisone: 3-4 giờ; Prednisolone (active): 2-3 giờ",
            "onset": "1-2 giờ",
            "duration": "18-36 giờ (tác dụng sinh học kéo dài hơn half-life)",
            "protein_binding": "70-90% (prednisolone)",
            "clearance": "Gan (chuyển hóa prednisone → prednisolone), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Không ngừng đột ngột sau khi dùng lâu dài - có thể gây suy thượng thận cấp đe dọa tính mạng. Corticosteroid có thể gây ức chế miễn dịch, tăng nguy cơ nhiễm trùng nặng, và che dấu triệu chứng nhiễm trùng"
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
        "pregnancy": "X - Chống chỉ định tuyệt đối",
        "mechanism_of_action": "Antimetabolite, folic acid antagonist. Ức chế enzyme dihydrofolate reductase (DHFR), ngăn cản chuyển đổi dihydrofolate thành tetrahydrofolate (THF). THF cần thiết cho tổng hợp purine và thymidine (DNA, RNA). Ức chế tổng hợp DNA và RNA → ức chế sự phát triển và phân chia tế bào. Tác động mạnh lên tế bào phân chia nhanh (tế bào ung thư, tế bào miễn dịch, tế bào niêm mạc, tế bào tủy xương). Được dùng trong điều trị ung thư (liều cao), viêm khớp dạng thấp, vảy nến (liều thấp), và các bệnh tự miễn khác.",
        "monitoring": [
            "Công thức máu (WBC, platelet, hemoglobin) - giảm bạch cầu, giảm tiểu cầu, thiếu máu - QUAN TRỌNG",
            "Chức năng gan (ALT, AST, bilirubin, albumin) - độc tính gan, xơ gan",
            "Chức năng thận (creatinine, eGFR) - độc tính thận",
            "X-quang phổi (xơ phổi - hiếm nhưng nguy hiểm)",
            "Nồng độ methotrexate trong máu (nếu dùng liều cao)",
            "Dấu hiệu nhiễm trùng (do giảm bạch cầu)",
            "Dấu hiệu chảy máu (do giảm tiểu cầu)",
            "Dấu hiệu độc tính niêm mạc (loét miệng, tiêu chảy)"
        ],
        "precautions": [
            "Độc tính nghiêm trọng - phải theo dõi chặt chẽ",
            "PHẢI dùng folic acid để giảm độc tính (5-10mg/tuần, không dùng cùng ngày với methotrexate)",
            "Giảm bạch cầu, giảm tiểu cầu, thiếu máu - theo dõi công thức máu mỗi 1-4 tuần",
            "Độc tính gan - có thể gây xơ gan, kiểm tra chức năng gan định kỳ",
            "Độc tính thận - uống nhiều nước, kiểm tra chức năng thận",
            "Không dùng ở suy thận nặng",
            "Không dùng ở suy gan",
            "Tương tác với NSAID, aspirin → tăng nồng độ methotrexate, tăng độc tính",
            "Tương tác với trimethoprim-sulfamethoxazole → tăng độc tính",
            "Không dùng ở phụ nữ có thai (gây dị tật thai nhi) - dùng biện pháp tránh thai",
            "Liều thấp (viêm khớp, vảy nến): 7.5-25mg/tuần, liều cao (ung thư): 100mg/m² trở lên",
            "Ngừng nếu có dấu hiệu độc tính nghiêm trọng"
        ],
        "pharmacokinetics": {
            "half_life": "3-10 giờ (liều thấp), 8-15 giờ (liều cao)",
            "onset": "Vài giờ đến vài ngày",
            "duration": "Dài (nhiều ngày, tích lũy)",
            "protein_binding": "50-60%",
            "metabolism": "Một phần trong gan, một phần bị polyglutamylation trong tế bào (tích lũy)",
            "clearance": "Chủ yếu qua thận (80-90%), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Dung dịch tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.",
        "black_box_warnings": "Độc tính nghiêm trọng, có thể tử vong. Giảm bạch cầu, giảm tiểu cầu, và thiếu máu có thể nặng. Độc tính gan có thể gây xơ gan. Độc tính thận có thể gây suy thận cấp. Phải theo dõi công thức máu và chức năng gan, thận định kỳ. Không dùng ở phụ nữ có thai (gây dị tật thai nhi)."

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
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Amoxicillin: aminopenicillin phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Clavulanate: beta-lactamase inhibitor, bảo vệ amoxicillin khỏi bị phân hủy bởi beta-lactamase. Kết hợp này mở rộng phổ kháng khuẩn, đặc biệt hiệu quả với H. influenzae, E. coli, và một số kỵ khí. Clavulanate không có hoạt tính kháng khuẩn riêng. Được dùng rộng rãi trong nhiễm trùng đường hô hấp, tiết niệu, da và mô mềm.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - tăng men gan (thường nhất thời), hiếm viêm gan (đặc biệt với clavulanate)",
            "Dấu hiệu nhiễm C. difficile",
            "Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV)",
            "Chức năng thận (creatinine) - hiếm viêm thận kẽ"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Nguy cơ viêm gan (đặc biệt do clavulanate) - thường nhất thời, hiếm nặng, tăng ở nam giới, dùng kéo dài",
            "Theo dõi men gan, ngừng nếu tăng nặng",
            "Phát ban thường gặp, đặc biệt ở bệnh nhân nhiễm virus (EBV, CMV) - không phải dị ứng thật",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Uống với thức ăn để giảm kích ứng dạ dày và tăng hấp thu",
            "Dùng đúng liều và đủ thời gian để tránh kháng thuốc",
            "Không dùng cho nhiễm trùng do Pseudomonas hoặc Enterococcus kháng"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (amoxicillin và clavulanate)",
            "onset": "1-2 giờ (PO)",
            "duration": "q8h hoặc q12h tùy công thức",
            "protein_binding": "17-20% (amoxicillin), 22-30% (clavulanate)",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận, cần điều chỉnh thận ở suy thận nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Sau khi pha (suspension): bảo quản trong tủ lạnh 10 ngày, sau đó vứt bỏ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ viêm gan (đặc biệt do clavulanate) có thể nặng, đặc biệt ở nam giới và dùng kéo dài. Phát ban thường gặp và có thể nhầm với dị ứng."

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
        "pregnancy": "C - An toàn trong cấp cứu",
        "mechanism_of_action": "Non-selective alpha và beta-adrenergic receptor agonist. Kích thích alpha-1 receptors → co mạch ngoại vi, tăng huyết áp. Kích thích beta-1 receptors → tăng nhịp tim, tăng co bóp cơ tim, tăng cung lượng tim. Kích thích beta-2 receptors → giãn phế quản, giãn mạch cơ xương. Trong ngừng tim: tăng áp lực tưới máu vành, tăng khả năng khử rung thành công.",
        "monitoring": [
            "Nhịp tim và huyết áp liên tục",
            "Điện tâm đồ (ECG) - theo dõi rối loạn nhịp",
            "Lactate máu (trong shock)",
            "Đường huyết (tăng đường huyết)",
            "Dấu hiệu thiếu máu cục bộ (đau ngực, thay đổi ST)",
            "Tổn thương mô tại chỗ tiêm (hoại tử nếu tiêm ngoài mạch)"
        ],
        "precautions": [
            "TUYỆT ĐỐI KHÔNG tiêm ngoài mạch (có thể gây hoại tử)",
            "Pha loãng đúng nồng độ: 1:1000 (1mg/ml) cho IM/SC, 1:10000 (0.1mg/ml) cho IV",
            "Trong anaphylaxis: tiêm IM ở đùi ngoài (hấp thu nhanh hơn cánh tay)",
            "Theo dõi sát trong 20 phút đầu (nguy cơ rối loạn nhịp, tăng huyết áp)",
            "Thận trọng ở bệnh nhân bệnh mạch vành (có thể gây nhồi máu cơ tim)",
            "Tránh dùng với thuốc chẹn beta (có thể gây tăng huyết áp nặng do không đối kháng alpha)",
            "Tiêm IV chậm, pha loãng để tránh tăng huyết áp đột ngột"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 phút (rất ngắn)",
            "onset": "IV: ngay lập tức; IM: 5-10 phút",
            "duration": "3-10 phút (IV), 10-30 phút (IM)",
            "metabolism": "MAO và COMT trong gan và mô",
            "clearance": "Rất nhanh, bị bất hoạt bởi enzyme"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Kiểm tra màu sắc trước dùng (hóa nâu = hỏng).",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, tiêm ngoài mạch có thể gây hoại tử mô. Liều cao có thể gây nhồi máu cơ tim, đột quỵ, hoặc tử vong."
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
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Anticholinergic (antimuscarinic). Kháng chọn lọc thụ thể muscarinic acetylcholine (M1-M5), ức chế tác dụng của acetylcholine. Tăng nhịp tim (ức chế vagal tone), giảm tiết (nước bọt, mồ hôi, dịch tiêu hóa, phế quản), giãn đồng tử và giảm co thắt cơ trơn (phế quản, ruột, bàng quang). Được dùng trong emergency để điều trị nhịp tim chậm có triệu chứng, block nhĩ thất, và như một chất giải độc trong quá liều organophosphate.",
        "monitoring": [
            "Nhịp tim (ECG monitoring - mục tiêu tăng nhịp tim)",
            "Dấu hiệu kháng cholinergic quá mức: khô miệng nặng, giãn đồng tử, bí tiểu, lú lẫn",
            "Nhãn áp (nếu có nguy cơ glaucoma)",
            "Triệu chứng nhịp tim chậm nghịch lý (paradoxical bradycardia) - có thể xảy ra với liều <0.5mg ở người lớn",
            "Phản ứng quá mức (nhịp tim nhanh, đánh trống ngực)"
        ],
        "precautions": [
            "QUAN TRỌNG: Liều tối thiểu người lớn 0.5mg để tránh nhịp tim chậm nghịch lý (liều thấp có thể kích thích trung tâm vagal)",
            "CHỐNG CHỈ ĐỊNH tuyệt đối: Glaucoma góc đóng (có thể gây tăng nhãn áp đe dọa thị giác)",
            "CHỐNG CHỈ ĐỊNH: Tắc nghẽn đường tiểu (có thể làm nặng thêm bí tiểu)",
            "CHỐNG CHỈ ĐỊNH: Nhịp tim nhanh (có thể làm tăng nhịp tim hơn nữa)",
            "Thận trọng ở người già (tăng nguy cơ lú lẫn, bí tiểu)",
            "Thận trọng ở bệnh nhân sốt (có thể làm tăng nhiệt độ do giảm tiết mồ hôi)",
            "Thận trọng khi dùng với các anticholinergics khác (tăng tác dụng phụ)",
            "Trong quá liều organophosphate: dùng liều cao hơn nhiều (2-5mg), có thể cần lặp lại nhiều lần cho đến khi đạt tác dụng (đồng tử co lại, giảm tiết)"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ (người lớn), 10-20 giờ (trẻ em)",
            "onset": "Vài phút (IV), 15-30 phút (IM)",
            "duration": "4-6 giờ (tác dụng lâm sàng)",
            "protein_binding": "50%",
            "clearance": "Thận (50-90% thải qua nước tiểu dưới dạng không đổi), gan (metabolite). Thời gian bán hủy dài hơn ở trẻ em"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch tiêm: bảo quản trong tủ mát (2-8°C) nếu có chỉ định, nhưng thường ổn định ở nhiệt độ phòng",
        "black_box_warnings": None
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
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Thuốc gây tê tại chỗ nhóm amide và thuốc chống loạn nhịp class IB. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh và tế bào cơ tim, ngăn cản khử cực và dẫn truyền xung động thần kinh. Ở tim: ức chế dẫn truyền trong các tế bào có thời gian khử cực dài (tâm thất), giảm tự động tính, giảm nguy cơ rối loạn nhịp thất. Tác dụng nhanh, thời gian bán thải ngắn. Được dùng trong gây tê tại chỗ, giảm đau tại chỗ, và điều trị rối loạn nhịp thất.",
        "monitoring": [
            "ECG liên tục (theo dõi rối loạn nhịp)",
            "Huyết áp và nhịp tim",
            "Dấu hiệu độc tính thần kinh trung ương (chóng mặt, ù tai, co giật, mất ý thức) - dấu hiệu đầu tiên của quá liều",
            "Dấu hiệu độc tính tim mạch (block nhĩ thất, nhịp tim chậm, rung thất) - dấu hiệu muộn, nguy hiểm",
            "Nồng độ lidocaine trong máu (nếu dùng kéo dài hoặc liều cao)",
            "Chức năng gan (lidocaine chuyển hóa mạnh ở gan)",
            "Dấu hiệu phản ứng dị ứng (hiếm)"
        ],
        "precautions": [
            "Độc tính thần kinh trung ương là dấu hiệu CẢNH BÁO SỚM - ngừng ngay nếu có chóng mặt, ù tai, co giật",
            "Độc tính tim mạch có thể xảy ra sau độc tính thần kinh - nguy hiểm tính mạng",
            "PHẢI điều chỉnh liều ở suy gan (giảm chuyển hóa → tích lũy → độc tính)",
            "Thận trọng ở suy tim (giảm phân bố → tăng nồng độ)",
            "Không dùng ở block nhĩ thất độ 2-3 hoặc block nhánh nếu không có máy tạo nhịp",
            "Liều gây tê tại chỗ: tuân thủ liều tối đa (không quá 4.5mg/kg không có epinephrine, 7mg/kg có epinephrine)",
            "Tiêm IV chậm (không quá 25-50mg/phút) để tránh độc tính",
            "Cần có sẵn thuốc chống co giật (benzodiazepine) và thiết bị hồi sức",
            "Giảm liều ở người cao tuổi (giảm chuyển hóa)"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ (bình thường), 3-5 giờ (suy gan)",
            "onset": "Ngay lập tức (IV), 2-5 phút (gây tê tại chỗ)",
            "duration": "10-20 phút (IV), 1-3 giờ (gây tê tại chỗ)",
            "protein_binding": "60-80%",
            "metabolism": "Gan (CYP3A4, CYP1A2) - chuyển hóa mạnh thành active metabolites",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch: tránh đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, độc tính tim mạch có thể gây block nhĩ thất, rung thất, và tử vong, đặc biệt ở suy gan hoặc quá liều. Độc tính thần kinh trung ương (co giật) là dấu hiệu cảnh báo sớm."

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
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Opioid receptor antagonist cạnh tranh. Gắn với ái lực cao vào mu-opioid receptor (và kappa, delta receptors), đẩy opioid ra khỏi receptor, đảo ngược hoàn toàn tác dụng của opioid (ức chế hô hấp, an thần, giảm đau, miosis). Tác dụng rất nhanh (1-2 phút IV), nhưng thời gian tác dụng ngắn (30-90 phút) do bị chuyển hóa nhanh, trong khi nhiều opioid có thời gian tác dụng dài hơn → cần lặp lại liều hoặc dùng infusion.",
        "monitoring": [
            "Độ bão hòa oxy (SpO2) và nhịp thở liên tục",
            "Mức độ ý thức (GCS)",
            "Dấu hiệu hội chứng cai opioid (kích động, vã mồ hôi, tăng huyết áp, nhịp tim nhanh)",
            "Huyết áp và nhịp tim",
            "Dấu hiệu tái ngộ độc opioid (thở chậm lại, giảm ý thức) - đặc biệt quan trọng nếu opioid có thời gian tác dụng dài hơn naloxone",
            "Co giật (hiếm nhưng nguy hiểm)"
        ],
        "precautions": [
            "Thời gian tác dụng NGẮN (30-90 phút) - opioid có thể tác dụng trở lại sau khi naloxone hết tác dụng",
            "Theo dõi sát ít nhất 2-4 giờ sau khi dùng naloxone (nguy cơ tái ngộ độc)",
            "Ở bệnh nhân nghiện opioid: naloxone có thể gây hội chứng cai nặng (kích động, nôn, tăng huyết áp) - cần chuẩn bị xử trí",
            "Không dùng quá liều (tăng nguy cơ hội chứng cai nặng, không tăng hiệu quả)",
            "Nếu cần duy trì: dùng infusion thay vì bolus lặp lại",
            "Thận trọng ở bệnh nhân có tiền sử co giật (có thể gây co giật)",
            "Dùng liều thấp (0.04-0.4mg) khi đảo ngược tác dụng opioid sau phẫu thuật để tránh đảo ngược hoàn toàn giảm đau"
        ],
        "pharmacokinetics": {
            "half_life": "30-90 phút (ngắn)",
            "onset": "1-2 phút (IV), 2-5 phút (IM)",
            "duration": "30-90 phút (tùy liều)",
            "metabolism": "Gan (glucuronidation)",
            "clearance": "Gan, thời gian bán thải ngắn hơn nhiều so với hầu hết opioid"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Có thể bảo quản ở nhiệt độ 2-8°C.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, thời gian tác dụng ngắn có thể dẫn đến tái ngộ độc opioid nếu không theo dõi đúng. Hội chứng cai opioid có thể nguy hiểm ở bệnh nhân nghiện."
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
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Benzodiazepine receptor antagonist cạnh tranh. Gắn với ái lực cao vào benzodiazepine receptor (một phần của GABA-A receptor complex), đẩy benzodiazepine ra khỏi receptor, đảo ngược tác dụng của benzodiazepine (an thần, ức chế hô hấp, giảm trương lực cơ, mất trí nhớ). Tác dụng rất nhanh (1-2 phút IV), nhưng thời gian tác dụng ngắn (45-90 phút) do bị chuyển hóa nhanh, trong khi nhiều benzodiazepine có thời gian tác dụng dài hơn → cần theo dõi sát, có thể cần lặp lại liều.",
        "monitoring": [
            "Mức độ ý thức (GCS) liên tục",
            "Nhịp thở và độ bão hòa oxy (SpO2)",
            "Dấu hiệu tái an thần/tái ức chế hô hấp (quan trọng - flumazenil hết tác dụng trước benzodiazepine)",
            "Dấu hiệu hội chứng cai benzodiazepine (kích động, run, co giật) - đặc biệt ở bệnh nhân nghiện",
            "Huyết áp và nhịp tim",
            "Co giật (nguy cơ ở bệnh nhân có tiền sử co giật, dùng benzodiazepine để chống co giật)",
            "Rối loạn nhịp tim (hiếm)"
        ],
        "precautions": [
            "Thời gian tác dụng NGẮN (45-90 phút) - benzodiazepine có thể tác dụng trở lại sau khi flumazenil hết",
            "Theo dõi sát ít nhất 2-4 giờ sau khi dùng (nguy cơ tái an thần, tái ức chế hô hấp)",
            "Ở bệnh nhân nghiện benzodiazepine: có thể gây hội chứng cai nặng (kích động, run, co giật) - cần chuẩn bị xử trí",
            "KHÔNG dùng ở bệnh nhân dùng benzodiazepine để chống co giật (có thể gây co giật nặng)",
            "KHÔNG dùng ở ngộ độc tricyclic antidepressant (có thể gây co giật, rối loạn nhịp)",
            "Khởi đầu với liều thấp (0.2mg), tăng dần nếu cần",
            "Không dùng quá liều (không tăng hiệu quả, tăng nguy cơ tác dụng phụ)",
            "Nếu cần duy trì: có thể dùng infusion, nhưng thường không khuyến cáo",
            "Thận trọng ở bệnh nhân có tiền sử co giật"
        ],
        "pharmacokinetics": {
            "half_life": "41-79 phút (ngắn)",
            "onset": "1-2 phút (IV)",
            "duration": "45-90 phút (tùy liều)",
            "protein_binding": "50%",
            "metabolism": "Gan (glucuronidation)",
            "clearance": "Gan, thời gian bán thải ngắn hơn nhiều so với hầu hết benzodiazepine"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, thời gian tác dụng ngắn có thể dẫn đến tái an thần và tái ức chế hô hấp nếu không theo dõi đúng. Hội chứng cai benzodiazepine có thể nguy hiểm ở bệnh nhân nghiện. Nguy cơ co giật ở bệnh nhân có tiền sử co giật hoặc ngộ độc tricyclic antidepressant."

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
        "pregnancy": "X - Chống chỉ định",
        "mechanism_of_action": "Statin (HMG-CoA reductase inhibitor). Ức chế không chọn lọc enzyme HMG-CoA reductase trong gan, enzyme chính trong tổng hợp cholesterol. Giảm tổng hợp cholesterol nội sinh → tăng số lượng LDL receptors trên bề mặt tế bào gan → tăng thanh thải LDL từ máu. Giảm LDL cholesterol, giảm triglyceride, tăng nhẹ HDL cholesterol. Có tác dụng chống viêm và ổn định mảng xơ vữa (pleiotropic effects). Được dùng trong tăng cholesterol máu, dự phòng biến cố tim mạch (nhồi máu cơ tim, đột quỵ).",
        "monitoring": [
            "Lipid profile (LDL, HDL, triglyceride, total cholesterol) - kiểm tra 4-12 tuần sau khi bắt đầu, sau đó định kỳ",
            "Chức năng gan (ALT, AST) - tăng men gan (thường nhất thời), hiếm viêm gan",
            "CK (creatine kinase) - tăng CK, dấu hiệu tiêu cơ vân (myopathy, rhabdomyolysis)",
            "Dấu hiệu tiêu cơ vân (đau cơ, yếu cơ, nước tiểu sẫm màu) - nguy hiểm",
            "Đường huyết (có thể tăng nhẹ đường huyết)",
            "HbA1c (tăng nguy cơ đái tháo đường type 2)"
        ],
        "precautions": [
            "Nguy cơ tiêu cơ vân (myopathy, rhabdomyolysis) - nguy hiểm, có thể gây suy thận cấp",
            "Nguy cơ tăng ở: liều cao, suy thận, suy gan, người cao tuổi, dùng với fibrate, niacin, cyclosporine, diltiazem, verapamil",
            "NGỪNG NGAY nếu có đau cơ, yếu cơ, CK tăng > 10 lần ULN, hoặc dấu hiệu tiêu cơ vân",
            "Nguy cơ tăng men gan - kiểm tra ALT/AST trước khi bắt đầu, sau 12 tuần, và định kỳ",
            "Tăng nguy cơ đái tháo đường type 2 (nhẹ)",
            "Không dùng trong thai kỳ (gây dị tật thai nhi) - dùng biện pháp tránh thai",
            "Không dùng ở suy gan hoạt động",
            "Tương tác với nhiều thuốc: cyclosporine, gemfibrozil, diltiazem, verapamil → tăng nguy cơ tiêu cơ vân",
            "Liều khởi đầu thường: 10-20mg/ngày, liều tối đa: 40mg/ngày",
            "Uống với hoặc không có thức ăn"
        ],
        "pharmacokinetics": {
            "half_life": "19 giờ (dài)",
            "onset": "1-2 tuần (giảm LDL)",
            "duration": "Dài (nhiều ngày)",
            "protein_binding": "88%",
            "metabolism": "Gan (CYP2C9, CYP2C19) - chuyển hóa yếu, ít tương tác hơn các statin khác",
            "clearance": "Chủ yếu qua gan (90%), một phần qua thận (10%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Nguy cơ tiêu cơ vân (rhabdomyolysis), có thể gây suy thận cấp và tử vong. Nguy cơ tăng ở liều cao, suy thận, và dùng với một số thuốc. Ngừng ngay nếu có đau cơ, yếu cơ, hoặc dấu hiệu tiêu cơ vân. Không dùng trong thai kỳ."

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
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 3, phổ rộng. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (một số), Gram-âm mạnh (Enterobacteriaceae, Neisseria, H. influenzae), và một số kỵ khí. Kháng được nhiều beta-lactamase do có cấu trúc vòng beta-lactam bền vững. Không hiệu quả với Pseudomonas aeruginosa, Enterococcus, hoặc MRSA. Thời gian bán thải dài (6-9 giờ) → chỉ cần tiêm 1 lần/ngày.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST, bilirubin) - có thể tăng, hiếm sỏi mật",
            "Sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao",
            "Chức năng thận (creatinine) - không cần điều chỉnh thận nhưng theo dõi",
            "Dấu hiệu nhiễm C. difficile",
            "Co giật (hiếm, nhưng có thể ở suy thận nặng)",
            "Phản ứng tại chỗ tiêm (đau, viêm tĩnh mạch)"
        ],
        "precautions": [
            "KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV (nguy cơ kết tủa ceftriaxone-calcium trong phổi, thận) - có thể tử vong",
            "Nguy cơ sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao, dùng kéo dài",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~5-10%)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Có thể gây tăng bilirubin (nhất thời, do đẩy bilirubin khỏi albumin)",
            "Pha trong NS, D5W, hoặc LR, tiêm IV hoặc IM",
            "Tiêm IM: pha với lidocaine 1% để giảm đau",
            "Không pha trộn với các thuốc khác (tương kỵ với nhiều thuốc, đặc biệt vancomycin, calcium)",
            "Thời gian bán thải dài → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h)"
        ],
        "pharmacokinetics": {
            "half_life": "6-9 giờ (rất dài cho cephalosporin)",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "24 giờ (liều 1-2g q24h), 12 giờ (viêm màng não: 2g q12h)",
            "protein_binding": "85-95% (rất cao)",
            "metabolism": "Không chuyển hóa, bài tiết nguyên dạng",
            "clearance": "40% qua thận, 60% qua mật (độc nhất trong cephalosporin) → không cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày. Không đông lạnh.",
        "black_box_warnings": "KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV - có thể gây kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong. Tránh dùng calci IV trong 48 giờ sau liều ceftriaxone cuối cùng ở trẻ sơ sinh."

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

# ========== ADDITIONAL COMMON DRUGS (Batch 1) - Added to DRUG_DATABASE ==========

DRUG_DATABASE.update({

# Antibiotics
"Piperacillin-tazobactam": {
    "group": "Antibiotic - Penicillin/Beta-lactamase Inhibitor",
    "vietnamese_name": "Piperacillin-tazobactam, Tazocin, Zosyn",
    "administration": ["IV"],
    "indications": [
        "Nhiễm khuẩn nặng (bệnh viện)",
        "Nhiễm khuẩn ổ bụng",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm phổi bệnh viện",
        "Nhiễm khuẩn đường tiết niệu phức tạp",
        "Nhiễm khuẩn huyết"
    ],
    "contraindications": [
        "Dị ứng penicillin",
        "Dị ứng beta-lactam"
    ],
    "dosage": {
        "adult_standard": "4.5g IV mỗi 8 giờ",
        "adult_severe": "4.5g IV mỗi 6 giờ",
        "adult_nosocomial_pneumonia": "4.5g IV mỗi 6 giờ",
        "notes": "Liều tối đa: 18g/ngày. Pha trong 50-150ml NS hoặc D5W, truyền trong 30 phút"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "4.5g IV mỗi 8 giờ",
        "under_30": "2.25g IV mỗi 8 giờ",
        "hemodialysis": "2.25g IV mỗi 8 giờ (sau lọc máu)"
    },
    "side_effects": [
        "Tiêu chảy",
        "Buồn nôn, nôn",
        "Phát ban",
        "Tăng men gan",
        "Giảm tiểu cầu (hiếm)",
        "Giảm bạch cầu (hiếm)"
    ],
    "interactions": [
        "Warfarin: có thể tăng INR",
        "Aminoglycosides: không pha chung, truyền riêng"
    ],
    "pregnancy": "B",
        "mechanism_of_action": "Piperacillin: penicillin phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Tazobactam: beta-lactamase inhibitor, bảo vệ piperacillin khỏi bị phân hủy bởi beta-lactamase (TEM, SHV, OXA). Kết hợp này mở rộng phổ kháng khuẩn, đặc biệt hiệu quả với Pseudomonas aeruginosa, Enterobacteriaceae (bao gồm một số ESBL), và kỵ khí. Tazobactam không có hoạt tính kháng khuẩn riêng, chỉ có tác dụng bảo vệ.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Điện giải (natri - mỗi 4.5g chứa 2.79 mEq natri, kali - có thể tăng)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Thời gian prothrombin/PT (hiếm giảm prothrombin)",
            "Số lượng tiểu cầu (hiếm giảm tiểu cầu)",
            "Đường huyết (có thể tăng hoặc giảm)"
        ],
        "precautions": [
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - đặc biệt quan trọng",
            "Hàm lượng natri cao (2.79 mEq/4.5g) - thận trọng ở suy tim, tăng huyết áp, phù",
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Có thể gây giảm prothrombin → tăng nguy cơ chảy máu, đặc biệt ở suy thận, suy gan, dùng kéo dài",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài",
            "Pha trong NS hoặc D5W, truyền IV trong 30 phút (liều chuẩn) hoặc 3-4 giờ (liều cao/extended infusion)",
            "Extended infusion (3-4 giờ) được khuyến cáo cho Pseudomonas aeruginosa để tối ưu hóa pharmacokinetics/pharmacodynamics (PK/PD)",
            "Không pha trộn với vancomycin (tạo kết tủa)"
        ],
        "pharmacokinetics": {
            "half_life": "0.7-1.2 giờ (piperacillin), 0.7-1 giờ (tazobactam)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều 4.5g q6h hoặc q8h, extended infusion q8h",
            "protein_binding": "30% (piperacillin), 20-30% (tazobactam)",
            "metabolism": "Piperacillin: thủy phân một phần, tazobactam: thủy phân",
            "clearance": "Chủ yếu qua thận (68% piperacillin, 80% tazobactam bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, hàm lượng natri cao có thể gây vấn đề ở bệnh nhân suy tim hoặc cần hạn chế natri. Giảm prothrombin có thể gây chảy máu nặng."

},

"Meropenem": {
    "group": "Antibiotic - Carbapenem",
    "vietnamese_name": "Meropenem, Meronem",
    "administration": ["IV"],
    "indications": [
        "Nhiễm khuẩn nặng đa kháng",
        "Nhiễm khuẩn bệnh viện",
        "Viêm màng não",
        "Nhiễm khuẩn ổ bụng",
        "Nhiễm khuẩn huyết"
    ],
    "contraindications": [
        "Dị ứng carbapenem",
        "Dị ứng beta-lactam nặng"
    ],
    "dosage": {
        "adult_standard": "1g IV mỗi 8 giờ",
        "adult_severe": "1g IV mỗi 6 giờ hoặc 2g IV mỗi 8 giờ",
        "adult_meningitis": "2g IV mỗi 8 giờ",
        "notes": "Truyền trong 15-30 phút. Phổ rộng, dự phòng kháng penicillinase"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "1g IV mỗi 12 giờ",
        "under_30": "500mg-1g IV mỗi 12 giờ",
        "hemodialysis": "500mg-1g IV mỗi 12 giờ (sau lọc máu)"
    },
    "side_effects": [
        "Tiêu chảy",
        "Phát ban",
        "Co giật (liều cao, suy thận)",
        "Tăng men gan",
        "Viêm tĩnh mạch tại chỗ tiêm"
    ],
    "interactions": [
        "Valproate: giảm nồng độ valproate (có thể gây co giật)",
        "Probenecid: tăng nồng độ meropenem"
    ],
    "pregnancy": "B",
        "mechanism_of_action": "Carbapenem kháng sinh beta-lactam. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), đặc biệt PBP-2, dẫn đến ly giải tế bào vi khuẩn. Phổ kháng khuẩn rộng, bao phủ cả vi khuẩn Gram-dương, Gram-âm, và kỵ khí. Kháng được nhiều beta-lactamase do có cấu trúc vòng beta-lactam bền vững. Đặc biệt hiệu quả với Enterobacteriaceae (bao gồm ESBL-producing), Pseudomonas aeruginosa, và kỵ khí.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP, procalcitonin)",
            "Cấy máu và cấy từ vị trí nhiễm trùng để đánh giá đáp ứng",
            "Dấu hiệu nhiễm trùng thứ phát (nấm, C. difficile)",
            "Co giật (nguy cơ tăng ở suy thận, bệnh thần kinh trung ương)",
            "Chức năng gan (ALT, AST) - hiếm nhưng có thể tăng",
            "Số lượng tiểu cầu (hiếm giảm tiểu cầu)"
        ],
        "precautions": [
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - giảm liều và tăng khoảng cách liều",
            "Nguy cơ co giật tăng ở: suy thận nặng (CrCl < 25), bệnh thần kinh trung ương, tiền sử co giật",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~1%)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy, phân lỏng",
            "Có thể gây kháng thuốc nếu dùng không đúng chỉ định - chỉ dùng khi thực sự cần",
            "Theo dõi nhiễm nấm thứ phát (đặc biệt Candida) khi dùng kéo dài",
            "Pha trong dung dịch NS hoặc D5W, truyền IV trong 15-30 phút",
            "Không pha trộn với các thuốc khác (có thể tương kỵ)"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (bình thường), 1.5-2.5 giờ (suy thận)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều 1g q8h đạt nồng độ hiệu quả",
            "protein_binding": "2% (rất thấp)",
            "metabolism": "Thủy phân trong gan (40%), không qua CYP450",
            "clearance": "Chủ yếu qua thận (70% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 2-4 giờ, hoặc trong tủ lạnh 24 giờ. Không đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ co giật tăng ở suy thận nặng và bệnh nhân có tiền sử co giật. Kháng thuốc có thể phát triển nếu dùng không đúng chỉ định."

},

"Clindamycin": {
    "group": "Antibiotic - Lincosamide",
    "vietnamese_name": "Clindamycin, Dalacin",
    "administration": ["PO", "IV", "IM"],
    "indications": [
        "Nhiễm khuẩn kỵ khí",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm phổi do vi khuẩn",
        "Nhiễm khuẩn răng miệng",
        "Sốt do chuột cắn"
    ],
    "contraindications": [
        "Dị ứng clindamycin",
        "Viêm đại tràng giả mạc trước đây"
    ],
    "dosage": {
        "adult_po": "150-450mg x 3-4 lần/ngày",
        "adult_iv": "600-900mg IV mỗi 8 giờ",
        "adult_severe": "900mg IV mỗi 8 giờ",
        "notes": "Có thể gây viêm đại tràng giả mạc (C. difficile). Dùng với thức ăn"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Không đổi",
        "under_30": "Không đổi (không thải qua thận)"
    },
    "side_effects": [
        "Tiêu chảy (phổ biến)",
        "Viêm đại tràng giả mạc (C. difficile - nghiêm trọng)",
        "Buồn nôn, nôn",
        "Phát ban",
        "Rối loạn vị giác"
    ],
    "interactions": [
        "Erythromycin: đối kháng",
        "Neuromuscular blockers: tăng tác dụng"
    ],
    "pregnancy": "B",
        "mechanism_of_action": "Lincosamide kháng sinh. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 50S của ribosome, ngăn cản quá trình dịch mã. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus, Streptococcus, bao gồm một số MRSA), kỵ khí (Bacteroides, Clostridium), và một số vi khuẩn không điển hình. Không hiệu quả với Enterobacteriaceae (Gram-âm). Đặc biệt hiệu quả với kỵ khí và được dùng trong nhiễm trùng răng miệng, xương, và mô mềm.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy, đau bụng) - nguy cơ CAO",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Số lượng bạch cầu (hiếm giảm bạch cầu, giảm bạch cầu trung tính)",
            "Phản ứng tại chỗ tiêm (viêm tĩnh mạch, đau)",
            "Phát ban (hiếm hội chứng Stevens-Johnson)"
        ],
        "precautions": [
            "Nguy cơ nhiễm C. difficile CAO - đây là một trong những kháng sinh có nguy cơ cao nhất",
            "NGỪNG NGAY nếu có tiêu chảy, đau bụng - có thể là C. difficile",
            "Không dùng cho điều trị dự phòng (trừ một số trường hợp đặc biệt) để giảm nguy cơ C. difficile",
            "Theo dõi sát dấu hiệu nhiễm C. difficile trong và sau khi dùng",
            "Có thể gây giảm bạch cầu trung tính (hiếm nhưng nguy hiểm)",
            "Tương kỵ với nhiều thuốc - không pha trộn",
            "Pha trong NS hoặc D5W, truyền IV trong ít nhất 10-60 phút (tùy liều)",
            "Không dùng cho nhiễm trùng do vi khuẩn Gram-âm (không hiệu quả)",
            "Uống với nước đầy đủ để giảm kích ứng thực quản"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "30-60 phút (PO), ngay lập tức (IV)",
            "duration": "q6h hoặc q8h (PO/IV)",
            "protein_binding": "90-95% (rất cao)",
            "metabolism": "Gan (CYP3A4) - một phần",
            "clearance": "Gan và thận, không cần điều chỉnh thận nhưng thận trọng ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C). Viên nang: tránh ẩm. Dung dịch pha tiêm: sau khi pha, bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ nhiễm C. difficile rất cao, có thể gây viêm đại tràng giả mạc nặng, có thể tử vong. Ngừng ngay nếu có tiêu chảy."

},

"Trimethoprim-sulfamethoxazole": {
    "group": "Antibiotic - Sulfonamide",
    "vietnamese_name": "Trimethoprim-sulfamethoxazole, Bactrim, Septra, Cotrimoxazole",
    "administration": ["PO", "IV"],
    "indications": [
        "Nhiễm khuẩn đường tiết niệu",
        "Viêm phổi do Pneumocystis jirovecii (PJP)",
        "Nhiễm khuẩn do Toxoplasma",
        "Nhiễm khuẩn do MRSA",
        "Nhiễm khuẩn đường hô hấp"
    ],
    "contraindications": [
        "Dị ứng sulfonamide",
        "Suy thận nặng (CrCl <15)",
        "Suy gan nặng",
        "Thiếu máu do thiếu folate",
        "Có thai (gần sinh)"
    ],
    "dosage": {
        "adult_uti": "160/800mg (DS) x 2 lần/ngày",
        "adult_pjp": "160/800mg (DS) x 3-4 lần/ngày",
        "adult_pjp_iv": "15-20mg/kg (TMP) IV mỗi 6-8 giờ",
        "notes": "Tỷ lệ TMP:SMX = 1:5. Dùng với nhiều nước"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "Tránh dùng nếu CrCl <15"
    },
    "side_effects": [
        "Phát ban (thường gặp)",
        "Tăng kali máu",
        "Giảm bạch cầu",
        "Thiếu máu",
        "Tăng creatinine (giả, không phản ánh suy thận)",
        "Độc tính da (SJS/TEN - hiếm nhưng nguy hiểm)"
    ],
    "interactions": [
        "Warfarin: tăng tác dụng",
        "Phenytoin: tăng nồng độ phenytoin",
        "ACE inhibitor: tăng kali máu",
        "Methotrexate: tăng độc tính"
    ],
    "pregnancy": "C - D gần sinh"
},

# Cardiovascular
"Spironolactone": {
    "group": "Cardiovascular - Aldosterone Antagonist (Potassium-sparing Diuretic)",
    "vietnamese_name": "Spironolactone, Aldactone",
    "administration": ["PO"],
    "indications": [
        "Suy tim (NYHA class II-IV)",
        "Xơ gan với cổ trướng",
        "Hội chứng Conn (tăng aldosterone)",
        "Tăng huyết áp (liều thấp)"
    ],
    "contraindications": [
        "Tăng kali máu",
        "Suy thận nặng (CrCl <30)",
        "Vô niệu",
        "Bệnh Addison"
    ],
    "dosage": {
        "adult_heart_failure": "12.5-25mg x 1 lần/ngày, tăng đến 25-50mg x 1 lần/ngày",
        "adult_ascites": "100-400mg/ngày chia 1-2 lần",
        "adult_htn": "25-100mg/ngày chia 1-2 lần",
        "notes": "Khởi đầu với liều thấp. Theo dõi kali máu"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Thận trọng",
        "under_30": "Chống chỉ định"
    },
    "side_effects": [
        "Tăng kali máu",
        "Vú to ở nam (gynecomastia)",
        "Rối loạn kinh nguyệt",
        "Buồn nôn",
        "Chóng mặt"
    ],
    "interactions": [
        "ACE inhibitor/ARB: tăng kali máu đáng kể",
        "Kali bổ sung: tăng kali máu",
        "Digoxin: tăng nồng độ digoxin"
    ],
    "pregnancy": "D",
        "mechanism_of_action": "Potassium-sparing diuretic, aldosterone antagonist. Đối kháng cạnh tranh với aldosterone tại mineralocorticoid receptor trong ống lượn xa và ống góp. Ngăn cản tác dụng của aldosterone (tái hấp thu natri, bài tiết kali). Dẫn đến tăng bài tiết natri và nước, giữ kali (không gây hạ kali). Có tác dụng chống androgen nhẹ (gây tác dụng phụ ở nam giới). Được dùng trong suy tim (giảm tử vong), xơ gan với cổ trướng, hội chứng Conn (cường aldosterone nguyên phát), và tăng huyết áp. Thường dùng kết hợp với loop diuretic hoặc thiazide để tránh hạ kali.",
        "monitoring": [
            "Điện giải (natri, kali) - tăng kali máu là tác dụng phụ chính (nguy hiểm)",
            "Chức năng thận (creatinine, eGFR) - không dùng nếu eGFR < 30",
            "Huyết áp",
            "Cân nặng và dấu hiệu phù",
            "Tác dụng phụ nội tiết (ở nam: vú to, rối loạn cương dương; ở nữ: rối loạn kinh nguyệt)",
            "Dấu hiệu quá liều (tăng kali nặng: yếu cơ, rối loạn nhịp tim)"
        ],
        "precautions": [
            "Tăng kali MÁU là tác dụng phụ chính - KHÔNG dùng nếu kali > 5 mEq/L hoặc eGFR < 30",
            "KHÔNG dùng với kali bổ sung hoặc các thuốc tăng kali khác (ACE inhibitor, ARB, trimethoprim) trừ khi được giám sát chặt chẽ",
            "Theo dõi kali thường xuyên, đặc biệt khi bắt đầu điều trị và tăng liều",
            "Tác dụng phụ nội tiết: vú to ở nam giới (gynecomastia), rối loạn cương dương, rối loạn kinh nguyệt ở nữ",
            "Liều thường: 25-100mg/ngày (PO), liều cao hơn cho hội chứng Conn",
            "Tác dụng chậm (vài ngày đến vài tuần)",
            "Không dùng ở suy thận nặng (eGFR < 30) hoặc tăng kali máu",
            "Thận trọng ở người cao tuổi (tăng nguy cơ tăng kali)",
            "Uống với thức ăn để tăng hấp thu"
        ],
        "pharmacokinetics": {
            "half_life": "10-35 giờ (dài)",
            "onset": "Vài ngày",
            "duration": "2-3 ngày sau khi ngừng",
            "protein_binding": "> 90%",
            "metabolism": "Gan (chuyển đổi thành active metabolites: canrenone)",
            "clearance": "Chủ yếu qua thận và gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, tăng kali máu có thể gây rối loạn nhịp tim nghiêm trọng, có thể tử vong, đặc biệt ở bệnh nhân suy thận hoặc dùng với các thuốc tăng kali khác. Phải theo dõi kali thường xuyên."

},

"Atenolol": {
    "group": "Cardiovascular - Beta-blocker (Selective)",
    "vietnamese_name": "Atenolol, Tenormin",
    "administration": ["PO"],
    "indications": [
        "Tăng huyết áp",
        "Đau thắt ngực",
        "Sau nhồi máu cơ tim",
        "Rối loạn nhịp tim"
    ],
    "contraindications": [
        "Hen phế quản nặng",
        "Block nhĩ thất độ 2-3",
        "Suy tim cấp không bù",
        "Nhịp tim chậm nặng"
    ],
    "dosage": {
        "adult_htn": "25-100mg x 1 lần/ngày",
        "adult_angina": "50-100mg x 1 lần/ngày",
        "adult_post_mi": "50-100mg x 1 lần/ngày",
        "notes": "Uống 1 lần/ngày. Chọn lọc beta-1"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "Giảm liều 75%, hoặc dùng mỗi 2 ngày"
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
          "Insulin: che dấu triệu chứng hạ đường huyết"
      ],
      "pregnancy": "D",
      "mechanism_of_action": "Selective beta-1 adrenergic receptor blocker. Ức chế tác dụng của catecholamines (epinephrine, norepinephrine) trên beta-1 receptors ở tim, giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp, giảm nhu cầu oxy cơ tim. Chọn lọc beta-1 hơn metoprolol, ít tác dụng trên beta-2 (ít gây co thắt phế quản hơn propranolol). Thải chủ yếu qua thận (khác với metoprolol - thải qua gan).",
      "monitoring": [
          "Nhịp tim và huyết áp (trước và sau khi bắt đầu)",
          "Chức năng thận: creatinine, BUN (thải chủ yếu qua thận - cần điều chỉnh liều)",
          "Dấu hiệu suy tim (khó thở, phù, tăng cân)",
          "Đường huyết (ở bệnh nhân đái tháo đường - che dấu triệu chứng hạ đường huyết)",
          "Triệu chứng mệt mỏi, lạnh tay chân"
      ],
      "precautions": [
          "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng). Phải giảm liều dần trong 1-2 tuần",
          "Thải chủ yếu qua thận - cần giảm liều ở bệnh nhân suy thận (CrCl <30: giảm 75% hoặc dùng mỗi 2 ngày)",
          "Thận trọng ở bệnh nhân hen phế quản/COPD (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản ở liều cao)",
          "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <50 bpm",
          "Thận trọng ở bệnh nhân đái tháo đường (che dấu triệu chứng hạ đường huyết)",
          "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)"
      ],
      "pharmacokinetics": {
          "half_life": "6-7 giờ (dài hơn metoprolol)",
          "onset": "1 giờ (PO)",
          "duration": "24 giờ (uống 1 lần/ngày)",
          "protein_binding": "5-15% (thấp, ít protein binding)",
          "clearance": "Thận (chủ yếu, 85-100% thải nguyên dạng qua nước tiểu). Không chuyển hóa qua gan"
      },
      "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
      "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực hoặc sau nhồi máu cơ tim - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, rối loạn nhịp tim nặng. Phải giảm liều dần dần trong 1-2 tuần"
  },

"Bisoprolol": {
    "group": "Cardiovascular - Beta-blocker (Selective)",
    "vietnamese_name": "Bisoprolol, Concor",
    "administration": ["PO"],
    "indications": [
        "Tăng huyết áp",
        "Suy tim (NYHA class II-IV)",
        "Đau thắt ngực"
    ],
    "contraindications": [
        "Hen phế quản nặng",
        "Block nhĩ thất độ 2-3",
        "Suy tim cấp không bù",
        "Nhịp tim chậm nặng (<60 bpm)"
    ],
    "dosage": {
        "adult_htn": "2.5-10mg x 1 lần/ngày",
        "adult_heart_failure": "1.25mg x 1 lần/ngày, tăng dần đến 10mg x 1 lần/ngày",
        "adult_angina": "5-10mg x 1 lần/ngày",
        "notes": "Uống 1 lần/ngày. Có bằng chứng giảm tỷ lệ tử vong trong suy tim"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Thận trọng, có thể giảm liều",
        "under_30": "Thận trọng, giảm liều"
    },
    "side_effects": [
        "Mệt mỏi",
        "Lạnh tay chân",
        "Nhịp tim chậm",
        "Chóng mặt",
        "Khó thở ở bệnh nhân hen/COPD"
    ],
          "interactions": [
          "Verapamil/Diltiazem: tăng nguy cơ block nhĩ thất",
          "Insulin: che dấu triệu chứng hạ đường huyết"
      ],
      "pregnancy": "C",
      "mechanism_of_action": "Selective beta-1 adrenergic receptor blocker. Ức chế tác dụng của catecholamines trên beta-1 receptors ở tim, giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp. Có bằng chứng mạnh làm giảm tỷ lệ tử vong và nhập viện trong suy tim mạn tính (NYHA class II-IV). Thải qua cả thận và gan (50-50%).",
      "monitoring": [
          "Nhịp tim và huyết áp (trước và sau khi bắt đầu, đặc biệt ở bệnh nhân suy tim)",
          "Dấu hiệu suy tim: khó thở, phù, tăng cân, giảm khả năng gắng sức",
          "Chức năng thận và gan (thải qua cả hai)",
          "Đường huyết (ở bệnh nhân đái tháo đường)",
          "Triệu chứng mệt mỏi, chóng mặt, lạnh tay chân"
      ],
      "precautions": [
          "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng, suy tim nặng). Phải giảm liều dần trong 1-2 tuần",
          "Khởi đầu với liều thấp (1.25mg/ngày) ở bệnh nhân suy tim, tăng dần mỗi 2-4 tuần",
          "Thận trọng ở bệnh nhân hen phế quản/COPD (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản)",
          "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <60 bpm",
          "Thận trọng ở bệnh nhân suy thận hoặc suy gan nặng",
          "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)"
      ],
      "pharmacokinetics": {
          "half_life": "9-12 giờ (dài, cho phép uống 1 lần/ngày)",
          "onset": "1-2 giờ (PO)",
          "duration": "24 giờ",
          "protein_binding": "30%",
          "clearance": "Thận (50%) và gan (50%) - chuyển hóa qua CYP3A4 và CYP2D6"
      },
      "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
      "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực hoặc suy tim - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, suy tim nặng. Phải giảm liều dần dần trong 1-2 tuần"
  },
  
  "Carvedilol": {
    "group": "Cardiovascular - Beta-blocker (Non-selective with Alpha-blocking)",
    "vietnamese_name": "Carvedilol, Dilatrend",
    "administration": ["PO"],
    "indications": [
        "Suy tim (NYHA class II-IV)",
        "Tăng huyết áp",
        "Sau nhồi máu cơ tim"
    ],
    "contraindications": [
        "Hen phế quản nặng",
        "Block nhĩ thất độ 2-3",
        "Suy tim cấp không bù",
        "Nhịp tim chậm nặng",
        "Suy gan nặng"
    ],
    "dosage": {
        "adult_heart_failure": "3.125mg x 2 lần/ngày, tăng dần mỗi 2 tuần đến 25mg x 2 lần/ngày",
        "adult_htn": "6.25-25mg x 2 lần/ngày",
        "adult_post_mi": "6.25-25mg x 2 lần/ngày",
        "notes": "Có bằng chứng giảm tỷ lệ tử vong trong suy tim. Có tác dụng giãn mạch"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Thận trọng",
        "under_30": "Thận trọng"
    },
    "side_effects": [
        "Mệt mỏi",
        "Chóng mặt",
        "Hạ huyết áp",
        "Nhịp tim chậm",
        "Phù chân (ít)"
    ],
          "interactions": [
          "Digoxin: tăng nồng độ digoxin",
          "Insulin: che dấu triệu chứng hạ đường huyết",
          "CYP2D6 inhibitors: tăng nồng độ carvedilol"
      ],
      "pregnancy": "C",
      "mechanism_of_action": "Non-selective beta-adrenergic receptor blocker (beta1 và beta2) kết hợp với alpha-1 adrenergic receptor blocker. Ức chế beta receptors làm giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp. Block alpha-1 receptors gây giãn mạch, giảm hậu gánh, cải thiện tuần hoàn. Có bằng chứng mạnh làm giảm tỷ lệ tử vong và nhập viện trong suy tim mạn tính (NYHA class II-IV).",
      "monitoring": [
          "Nhịp tim và huyết áp (trước và sau khi bắt đầu, đặc biệt ở bệnh nhân suy tim - có thể gây hạ huyết áp)",
          "Dấu hiệu suy tim: khó thở, phù, tăng cân, giảm khả năng gắng sức",
          "Chức năng gan (chống chỉ định trong suy gan nặng)",
          "Đường huyết (ở bệnh nhân đái tháo đường)",
          "Triệu chứng mệt mỏi, chóng mặt, hạ huyết áp, phù chân"
      ],
      "precautions": [
          "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng, suy tim nặng). Phải giảm liều dần trong 1-2 tuần",
          "Khởi đầu với liều rất thấp (3.125mg x 2 lần/ngày) ở bệnh nhân suy tim, tăng dần mỗi 2 tuần",
          "CHỐNG CHỈ ĐỊNH trong suy gan nặng",
          "Thận trọng ở bệnh nhân hen phế quản/COPD (non-selective, có thể gây co thắt phế quản nặng)",
          "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <60 bpm",
          "Có thể gây hạ huyết áp nặng (do tác dụng alpha-blocking) - theo dõi sát khi bắt đầu",
          "Thận trọng khi dùng với digoxin (tăng nồng độ digoxin)",
          "Thận trọng với CYP2D6 inhibitors (tăng nồng độ carvedilol)"
      ],
      "pharmacokinetics": {
          "half_life": "7-10 giờ",
          "onset": "1-2 giờ (PO)",
          "duration": "12-24 giờ (uống 2 lần/ngày)",
          "protein_binding": "98% (rất cao)",
          "clearance": "Gan (chủ yếu, chuyển hóa qua CYP2D6, CYP2C9, CYP3A4). Thải qua phân và nước tiểu"
      },
      "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
      "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực hoặc suy tim - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, suy tim nặng. Phải giảm liều dần dần trong 1-2 tuần"
  },

# Respiratory
"Montelukast": {
    "group": "Respiratory - Leukotriene Receptor Antagonist",
    "vietnamese_name": "Montelukast, Singulair",
    "administration": ["PO"],
    "indications": [
        "Hen phế quản (phòng ngừa)",
        "Viêm mũi dị ứng",
        "Co thắt phế quản do gắng sức"
    ],
    "contraindications": [
        "Dị ứng montelukast"
    ],
    "dosage": {
        "adult": "10mg x 1 lần/ngày (buổi tối)",
        "pediatric_6_14": "5mg x 1 lần/ngày",
        "pediatric_2_5": "4mg x 1 lần/ngày",
        "notes": "Uống buổi tối, có thể uống với hoặc không thức ăn"
    },
    "side_effects": [
        "Nhức đầu",
        "Buồn nôn",
        "Tiêu chảy",
        "Rối loạn giấc ngủ",
        "Thay đổi tâm trạng (hiếm)",
        "Phản ứng tâm thần (rất hiếm)"
    ],
    "interactions": [
        "Phenobarbital: giảm nồng độ montelukast",
        "Rifampin: giảm nồng độ montelukast"
    ],
    "pregnancy": "B"
},

# GI - Thay Pantoprazole (đã có) bằng Levofloxacin
"Levofloxacin": {
    "group": "Antibiotic - Fluoroquinolone",
    "vietnamese_name": "Levofloxacin, Tavanic",
    "administration": ["PO", "IV"],
    "indications": [
        "Viêm phổi cộng đồng",
        "Nhiễm khuẩn đường tiết niệu phức tạp",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm xoang",
        "Viêm tuyến tiền liệt do vi khuẩn"
    ],
    "contraindications": [
        "Dị ứng fluoroquinolone",
        "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
        "Có thai"
    ],
    "dosage": {
        "adult_po": "500-750mg x 1 lần/ngày",
        "adult_iv": "500-750mg IV x 1 lần/ngày",
        "adult_pneumonia": "500-750mg x 1 lần/ngày x 7-14 ngày",
        "notes": "Uống với nhiều nước. Tránh antacid, sắt trong 2 giờ"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "250-500mg x 1 lần/ngày"
    },
    "side_effects": [
        "Rối loạn tiêu hóa",
        "Nhức đầu",
        "Rối loạn giấc ngủ",
        "Rối loạn gân (viêm gân, đứt gân)",
        "QT kéo dài",
        "Hạ đường huyết (hiếm)"
    ],
    "interactions": [
        "Antacid/Sắt: giảm hấp thu",
        "Warfarin: tăng nguy cơ chảy máu",
        "Corticosteroid: tăng nguy cơ đứt gân"
    ],
    "pregnancy": "C"
}

})

# Update DRUG_GROUPS
DRUG_GROUPS["Antibiotics"] = DRUG_GROUPS.get("Antibiotics", []) + [
    "Piperacillin-tazobactam", "Meropenem", "Clindamycin", "Trimethoprim-sulfamethoxazole"
]
DRUG_GROUPS["Cardiovascular"] = DRUG_GROUPS.get("Cardiovascular", []) + [
    "Spironolactone", "Atenolol", "Bisoprolol", "Carvedilol"
]
DRUG_GROUPS["Respiratory"] = DRUG_GROUPS.get("Respiratory", []) + ["Montelukast"]
DRUG_GROUPS["Antibiotics"] = DRUG_GROUPS.get("Antibiotics", []) + ["Levofloxacin"]

# Update total count
TOTAL_DRUGS = len(DRUG_DATABASE)

