"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Fluoroquinolones

FLUOROQUINOLONES_DRUGS = {
    "Ciprofloxacin": {'group': 'Antibiotic - Fluoroquinolone', 'vietnamese_name':
        'Ciprofloxacin, Cipro', 'administration': ['PO', 'IV'], 'indications':
        ['Nhiễm khuẩn đường tiết niệu', 'Nhiễm khuẩn đường tiêu hóa',
        'Nhiễm khuẩn da mô mềm', 'Nhiễm khuẩn xương khớp',
        'Viêm phổi (một số loại)'], 'contraindications': [
        'Dị ứng fluoroquinolone', 'Có thai',
        'Trẻ em <18 tuổi (trừ trường hợp đặc biệt)', 'QT kéo dài'], 'dosage': {
        'adult_uti': '250-500mg PO x 2 lần/ngày', 'adult_uti_complicated':
        '500-750mg PO x 2 lần/ngày', 'adult_iv': '200-400mg IV mỗi 12 giờ',
        'adult_severe': '400mg IV mỗi 8 giờ', 'notes':
        'Uống cách xa antacid 2 giờ. Không dùng với sữa'}, 'renal_adjustment':
        {'normal': 'Không đổi', '30_60': 'Giảm liều 25-50%', 'under_30':
        'Giảm liều 50-75%'}, 'side_effects': ['Rối loạn tiêu hóa',
        'Đau gân, viêm gân (có thể đứt gân)', 'QT kéo dài', 'Co giật (hiếm)',
        'Nhạy cảm ánh sáng', 'Rối loạn tâm thần (hiếm)'], 'interactions': [
        'Antacid: giảm hấp thu', 'Warfarin: tăng INR',
        'Theophylline: tăng nồng độ theophylline',
        'Probenecid: tăng nồng độ ciprofloxacin'], 'pregnancy':
        'C - Tránh dùng', 'mechanism_of_action':
        'Ciprofloxacin là fluoroquinolone kháng sinh phổ rộng thuộc thế hệ thứ hai. Ức chế DNA gyrase (topoisomerase II) ở vi khuẩn Gram-âm và topoisomerase IV ở vi khuẩn Gram-dương, các enzyme cần thiết cho quá trình sao chép, phiên mã, sửa chữa, và tái tổ hợp DNA. Dẫn đến tổn thương DNA không thể sửa chữa và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, H. influenzae, Neisseria, Moraxella), một số Gram-dương (không phải MRSA), và một số vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Kháng thuốc phát triển nhanh nếu dùng không đúng hoặc không đủ liều.'
        , 'monitoring': [
        'Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị'
        ,
        'Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm'
        ,
        'Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc'
        ,
        'Thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần)'
        ,
        'Tim mạch (ECG - QT kéo dài, rối loạn nhịp tim) - đặc biệt ở bệnh nhân có nguy cơ'
        , 'Đường huyết (tăng hoặc hạ đường huyết - đặc biệt với sulfonylurea)',
        'Chức năng thận (creatinine, BUN) - điều chỉnh liều ở suy thận',
        'Chức năng gan (ALT, AST) - hiếm viêm gan nặng'], 'precautions': [
        'Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc'
        ,
        'Nguy cơ tăng ở: > 60 tuổi, dùng corticosteroid, ghép thận, ghép tim, ghép phổi, hoạt động thể lực'
        , 'NGỪNG NGAY nếu có đau, sưng gân - nghỉ ngơi, không vận động',
        'QT kéo dài → không dùng với các thuốc kéo dài QT khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp'
        ,
        'Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID (tăng nguy cơ)'
        ,
        'Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng, mặc quần áo che'
        ,
        'Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm, canxi (cách ít nhất 2 giờ)'
        ,
        'Hạ đường huyết → thận trọng với sulfonylurea (glibenclamide, gliclazide)',
        'Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn, viêm khớp'
        , 'Tránh dùng với sữa, sản phẩm sữa (giảm hấp thu)',
        'Uống nhiều nước để tránh kết tinh trong nước tiểu',
        'Không dùng trong thai kỳ (nguy cơ tổn thương sụn thai nhi)'],
        'pharmacokinetics': {'half_life':
        '4 giờ (bình thường), 5-7 giờ (suy thận nặng)', 'onset':
        '1-2 giờ (PO), ngay lập tức (IV)', 'duration':
        'q12h (PO/IV), q8h cho Pseudomonas hoặc nhiễm trùng nặng',
        'protein_binding': '20-40%', 'clearance':
        'Chủ yếu qua thận (40-60% bài tiết nguyên dạng), một phần qua gan (CYP1A2). Cần điều chỉnh liều ở suy thận (CrCl <30).'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín, tránh ẩm. IV: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi pha. Dung dịch đã pha: bảo quản ở nhiệt độ phòng, dùng trong vòng 24 giờ.'
        , 'black_box_warnings':
        'Tăng nguy cơ viêm gân và đứt gân ở mọi lứa tuổi. Nguy cơ tăng ở bệnh nhân > 60 tuổi, dùng corticosteroid, ghép cơ quan. Nguy cơ tổn thương thần kinh ngoại biên không hồi phục. Nguy cơ tác dụng phụ nghiêm trọng về gân, cơ, khớp, và thần kinh có thể xảy ra cùng lúc. Nguy cơ làm nặng bệnh nhược cơ. Tăng nguy cơ rối loạn tâm thần và hành vi tự sát. Chỉ dùng khi không có lựa chọn khác.'
        , 'drug_interactions': {'major': [{'drug':
        'Antacids (Aluminum, Magnesium), Sucralfate, Sắt, Kẽm, Canxi',
        'mechanism':
        'Cation (Al3+, Mg2+, Fe2+, Zn2+, Ca2+) tạo phức hợp không hòa tan với ciprofloxacin, giảm hấp thu.'
        , 'effect':
        'Giảm hấp thu ciprofloxacin, giảm nồng độ trong máu, giảm hiệu quả điều trị'
        , 'management':
        'Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống ciprofloxacin. Không uống cùng lúc.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Ciprofloxacin ức chế CYP2C9, làm giảm chuyển hóa warfarin, tăng nồng độ warfarin.'
        , 'effect':
        'Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng',
        'management':
        'Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng ciprofloxacin. Giảm liều warfarin khi bắt đầu ciprofloxacin. Điều chỉnh liều warfarin theo INR.'
        }, {'drug': 'Theophylline', 'mechanism':
        'Ciprofloxacin ức chế CYP1A2, làm giảm chuyển hóa theophylline, tăng nồng độ theophylline.'
        , 'effect':
        'Tăng nồng độ theophylline, tăng độc tính theophylline (buồn nôn, nôn, co giật, rối loạn nhịp tim)'
        , 'management':
        'Giảm liều theophylline 25-50% khi bắt đầu ciprofloxacin. Theo dõi nồng độ theophylline. Theo dõi dấu hiệu độc tính.'
        }], 'moderate': [{'drug': 'Probenecid', 'mechanism':
        'Probenecid ức chế bài tiết ống thận của ciprofloxacin, tăng nồng độ.',
        'effect': 'Tăng nồng độ ciprofloxacin, tăng tác dụng phụ', 'management':
        'Theo dõi tác dụng phụ. Có thể cần giảm liều ciprofloxacin.'}, {'drug':
        'NSAID (Ibuprofen, Naproxen)', 'mechanism':
        'Cả hai đều có thể gây co giật, tác dụng cộng dồn.', 'effect':
        'Tăng nguy cơ co giật', 'management':
        'Tránh dùng đồng thời nếu có thể. Thận trọng ở bệnh nhân có tiền sử co giật.'
        }, {'drug': 'Corticosteroid', 'mechanism':
        'Cả hai đều tăng nguy cơ đứt gân, tác dụng cộng dồn.', 'effect':
        'Tăng nguy cơ viêm gân, đứt gân', 'management':
        'TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ dấu hiệu đau, sưng gân. Ngừng ngay nếu có đau gân.'
        }], 'minor': [{'drug': 'Sulfonylurea (Glibenclamide, Gliclazide)',
        'mechanism': 'Ciprofloxacin có thể gây hạ đường huyết.', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Theo dõi đường huyết. Điều chỉnh liều sulfonylurea nếu cần.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng ciprofloxacin hoặc các fluoroquinolone khác',
        'Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi',
        'Trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn, viêm khớp'
        ,
        'QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng'
        , 'Bệnh nhược cơ nặng - có thể làm nặng bệnh'], 'tương_đối': [
        'Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân',
        'Dùng corticosteroid - tăng nguy cơ đứt gân',
        'Ghép cơ quan - tăng nguy cơ đứt gân',
        'Tiền sử co giật - tăng nguy cơ co giật',
        'Suy thận nặng (CrCl <30) - giảm liều đáng kể',
        'Suy gan - thận trọng, có thể giảm chuyển hóa',
        'Dùng với warfarin - tăng nguy cơ chảy máu',
        'Dùng với theophylline - tăng độc tính theophylline',
        'Hoạt động thể lực nặng - tăng nguy cơ đứt gân']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Ciprofloxacin là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể gây tổn thương sụn ở khớp ở thai nhi. Có báo cáo về tổn thương sụn ở trẻ em khi dùng trong thai kỳ. CHỐNG CHỈ ĐỊNH trong thai kỳ trừ khi lợi ích vượt quá nguy cơ rõ ràng và không có lựa chọn khác. Nhiễm trùng nặng có thể gây nguy hiểm cho thai nhi, nhưng nên dùng kháng sinh khác nếu có thể.'
        , 'lactation': {'safety': 'Compatible (với thận trọng)', 'details':
        'Ciprofloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, fluoroquinolone có thể gây tổn thương sụn ở trẻ sơ sinh.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với thận trọng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh. Tránh dùng nếu có lựa chọn khác.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Ciprofloxacin chuyển hóa một phần qua gan nhưng không phụ thuộc nhiều vào chức năng gan.'
        , 'moderate':
        'Không cần điều chỉnh liều. Thận trọng nếu có suy thận kèm theo.',
        'severe':
        'Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.'
        , 'notes':
        'Ciprofloxacin chuyển hóa một phần qua gan (CYP1A2), thải trừ chủ yếu qua thận (40-60% nguyên dạng). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng',
        'Triệu chứng thần kinh: Co giật, kích động, lo âu, mất ngủ, trầm cảm, rối loạn tâm thần, hành vi tự sát'
        , 'Triệu chứng gân: Đau gân, viêm gân, đứt gân (đặc biệt gân Achilles)',
        'Triệu chứng tim mạch: QT kéo dài, rối loạn nhịp tim, có thể gây tử vong',
        'Triệu chứng chuyển hóa: Hạ hoặc tăng đường huyết',
        'Triệu chứng nghiêm trọng: Tổn thương thần kinh ngoại biên không hồi phục, rối loạn nhịp tim nghiêm trọng, đứt gân'
        ], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': ['Ngừng ngay ciprofloxacin',
        'Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)'
        , 'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG',
        'Điều trị co giật nếu có:', '  - Benzodiazepine (diazepam, lorazepam)',
        '  - Theo dõi thần kinh chặt chẽ', 'Điều trị rối loạn nhịp tim nếu có:',
        '  - Theo dõi ECG liên tục', '  - Điều trị loạn nhịp nếu cần',
        'Điều trị đau gân nếu có:', '  - Ngừng ngay ciprofloxacin',
        '  - Nghỉ ngơi, không vận động', '  - Chườm lạnh',
        '  - Thuốc giảm đau nếu cần', 'Điều trị hạ đường huyết nếu có:',
        '  - Truyền glucose', '  - Theo dõi đường huyết',
        'Điều trị triệu chứng tiêu hóa:', '  - Chống nôn nếu cần',
        '  - Truyền dịch nếu mất nước',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2'],
        'monitoring':
        'Theo dõi dấu hiệu sinh tồn, ECG, dấu hiệu thần kinh, dấu hiệu gân, đường huyết trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (loạn nhịp, co giật, đứt gân).'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để tránh kết tinh trong nước tiểu. KHÔNG uống với sữa hoặc sản phẩm sữa (giảm hấp thu).'
        , 'timing':
        'Uống 2 lần/ngày (q12h), cách đều 12 giờ. Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống antacid, sucralfate, sắt, kẽm, canxi. Không uống cùng lúc với các cation này.'
        }, 'iv': {'reconstitution':
        'Pha với NS hoặc D5W. Nồng độ pha: 1-2mg/ml (tối đa). Pha 200mg trong 100ml dịch = 2mg/ml. Pha 400mg trong 200ml dịch = 2mg/ml.'
        , 'infusion_rate':
        'Truyền trong 60 phút (ít nhất 60 phút). Không truyền quá nhanh. Tốc độ: 100ml/60 phút = ~1.7ml/phút. 200ml/60 phút = ~3.3ml/phút.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],
        'incompatibility': [
        'Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với cation (Al3+, Mg2+, Ca2+).'
        ], 'notes':
        'Theo dõi chức năng thận, dấu hiệu gân, thần kinh trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần. Liều: 200-400mg mỗi 12 giờ (q12h), hoặc 400mg mỗi 8 giờ (q8h) cho Pseudomonas hoặc nhiễm trùng nặng.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Ciprofloxacin (Cipro)',
        'UpToDate - Ciprofloxacin: Drug Information',
        'Medscape - Ciprofloxacin Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Ciprofloxacin Monograph',
        'Micromedex - Ciprofloxacin Drug Information',
        'IDSA Guidelines - Antimicrobial Therapy'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }}}

__all__ = ['FLUOROQUINOLONES_DRUGS']
