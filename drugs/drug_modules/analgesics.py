"""
Analgesic and Pain Medications
Generated from drug_database_data.py
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
            "protein_binding": "20-35%",
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
}

__all__ = ['ANALGESICS_DRUGS']
