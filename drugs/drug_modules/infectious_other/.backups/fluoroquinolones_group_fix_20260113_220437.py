"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Fluoroquinolones

FLUOROQUINOLONES_DRUGS = {
    "Ciprofloxacin": {'group': 'Antibiotic - Fluoroquinolone',vietnamese_name':
        'Ciprofloxacin, Cipro', 'administration': ['PO', 'IV'],indications':
        ['Nhiễm khuẩn đường tiết niệu', 'Nhiễm khuẩn đường tiêu hóa',
        'Nhiễm khuẩn da mô mềm', 'Nhiễm khuẩn xương khớp',
        'Viêm phổi (một số loại)'],contraindications': [
        'Dị ứng fluoroquinolone', 'Có thai',
        'Trẻ em <18 tuổi (trừ trường hợp đặc biệt)', 'QT kéo dài'],dosage': {
        'adult_uti': '250-500mg PO x 2 lần/ngày', 'adult_uti_complicated':
        '500-750mg PO x 2 lần/ngày', 'adult_iv': '200-400mg IV mỗi 12 giờ',
        'adult_severe': '400mg IV mỗi 8 giờ', 'notes':
        'Uống cách xa antacid 2 giờ. Không dùng với sữa'},renal_adjustment':
        {'normal': 'Không đổi', '30_60': 'Giảm liều 25-50%', 'under_30':
        'Giảm liều 50-75%'},side_effects': ['Rối loạn tiêu hóa',
        'Đau gân, viêm gân (có thể đứt gân)', 'QT kéo dài', 'Co giật (hiếm)',
        'Nhạy cảm ánh sáng', 'Rối loạn tâm thần (hiếm)'],interactions': [
        'Antacid: giảm hấp thu', 'Warfarin: tăng INR',
        'Theophylline: tăng nồng độ theophylline',
        'Probenecid: tăng nồng độ ciprofloxacin'],pregnancy':
        'C - Tránh dùng', 'mechanism_of_action':
        'Ciprofloxacin là fluoroquinolone kháng sinh phổ rộng thuộc thế hệ thứ hai. Ức chế DNA gyrase (topoisomerase II) ở vi khuẩn Gram-âm và topoisomerase IV ở vi khuẩn Gram-dương, các enzyme cần thiết cho quá trình sao chép, phiên mã, sửa chữa, và tái tổ hợp DNA. Dẫn đến tổn thương DNA không thể sửa chữa và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, H. influenzae, Neisseria, Moraxella), một số Gram-dương (không phải MRSA), và một số vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Kháng thuốc phát triển nhanh nếu dùng không đúng hoặc không đủ liều.'
        , 'monitoring': [
        'Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị'
        'Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm'
        'Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc'
        'Thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần)'
        'Tim mạch (ECG - QT kéo dài, rối loạn nhịp tim) - đặc biệt ở bệnh nhân có nguy cơ'
        , 'Đường huyết (tăng hoặc hạ đường huyết - đặc biệt với sulfonylurea)',
        'Chức năng thận (creatinine, BUN) - điều chỉnh liều ở suy thận',
        'Chức năng gan (ALT, AST) - hiếm viêm gan nặng'],precautions': [
        'Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc'
        'Nguy cơ tăng ở: > 60 tuổi, dùng corticosteroid, ghép thận, ghép tim, ghép phổi, hoạt động thể lực'
        , 'NGỪNG NGAY nếu có đau, sưng gân - nghỉ ngơi, không vận động',
        'QT kéo dài → không dùng với các thuốc kéo dài QT khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp'
        'Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID (tăng nguy cơ)'
        'Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng, mặc quần áo che'
        'Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm, canxi (cách ít nhất 2 giờ)'
        'Hạ đường huyết → thận trọng với sulfonylurea (glibenclamide, gliclazide)',
        'Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn, viêm khớp'
        , 'Tránh dùng với sữa, sản phẩm sữa (giảm hấp thu)',
        'Uống nhiều nước để tránh kết tinh trong nước tiểu',
        'Không dùng trong thai kỳ (nguy cơ tổn thương sụn thai nhi)'],pharmacokinetics': {'half_life':
        '4 giờ (bình thường), 5-7 giờ (suy thận nặng)', 'onset':
        '1-2 giờ (PO), ngay lập tức (IV)', 'duration':
        'q12h (PO/IV), q8h cho Pseudomonas hoặc nhiễm trùng nặng',
        'protein_binding': '20-40%', 'clearance':
        'Chủ yếu qua thận (40-60% bài tiết nguyên dạng), một phần qua gan (CYP1A2). Cần điều chỉnh liều ở suy thận (CrCl <30).'
        },storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín, tránh ẩm. IV: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi pha. Dung dịch đã pha: bảo quản ở nhiệt độ phòng, dùng trong vòng 24 giờ.'
        , 'black_box_warnings':
        'Tăng nguy cơ viêm gân và đứt gân ở mọi lứa tuổi. Nguy cơ tăng ở bệnh nhân > 60 tuổi, dùng corticosteroid, ghép cơ quan. Nguy cơ tổn thương thần kinh ngoại biên không hồi phục. Nguy cơ tác dụng phụ nghiêm trọng về gân, cơ, khớp, và thần kinh có thể xảy ra cùng lúc. Nguy cơ làm nặng bệnh nhược cơ. Tăng nguy cơ rối loạn tâm thần và hành vi tự sát. Chỉ dùng khi không có lựa chọn khác.'
        , 'drug_interactions': {
            'major': [
                {'drug': 'Antacids (Aluminum, Magnesium), Sucralfate, Sắt, Kẽm, Canxi',
                 'mechanism': 'Cation (Al3+, Mg2+, Fe2+, Zn2+, Ca2+) tạo phức hợp không hòa tan với ciprofloxacin, giảm hấp thu.',
                 'effect': 'Giảm hấp thu ciprofloxacin, giảm nồng độ trong máu, giảm hiệu quả điều trị',
                 'management': 'Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống ciprofloxacin. Không uống cùng lúc.'},
                {'drug': 'Warfarin',
                 'mechanism': 'Ciprofloxacin ức chế CYP2C9, làm giảm chuyển hóa warfarin, tăng nồng độ warfarin.',
                 'effect': 'Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng',
                 'management': 'Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng ciprofloxacin. Giảm liều warfarin khi bắt đầu ciprofloxacin. Điều chỉnh liều warfarin theo INR.'},
                {'drug': 'Theophylline',
                 'mechanism': 'Ciprofloxacin ức chế CYP1A2, làm giảm chuyển hóa theophylline, tăng nồng độ theophylline.',
                 'effect': 'Tăng nồng độ theophylline, tăng độc tính theophylline (buồn nôn, nôn, co giật, rối loạn nhịp tim)',
                 'management': 'Giảm liều theophylline 25-50% khi bắt đầu ciprofloxacin. Theo dõi nồng độ theophylline. Theo dõi dấu hiệu độc tính.'}
            ],moderate': [
                {'drug': 'Probenecid',
                 'mechanism': 'Probenecid ức chế bài tiết ống thận của ciprofloxacin, tăng nồng độ.',
                 'effect': 'Tăng nồng độ ciprofloxacin, tăng tác dụng phụ',
                 'management': 'Theo dõi tác dụng phụ. Có thể cần giảm liều ciprofloxacin.'},
                {'drug': 'NSAID (Ibuprofen, Naproxen)',
                 'mechanism': 'Cả hai đều có thể gây co giật, tác dụng cộng dồn.',
                 'effect': 'Tăng nguy cơ co giật',
                 'management': 'Tránh dùng đồng thời nếu có thể. Thận trọng ở bệnh nhân có tiền sử co giật.'},
                {'drug': 'Corticosteroid',
                 'mechanism': 'Cả hai đều tăng nguy cơ đứt gân, tác dụng cộng dồn.',
                 'effect': 'Tăng nguy cơ viêm gân, đứt gân',
                 'management': 'TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ dấu hiệu đau, sưng gân. Ngừng ngay nếu có đau gân.'}
            ],minor': [
                {'drug': 'Sulfonylureas',
                 'mechanism': 'Ciprofloxacin có thể gây hạ đường huyết.',
                 'effect': 'Tăng nguy cơ hạ đường huyết',
                 'management': 'Theo dõi đường huyết. Điều chỉnh liều sulfonylurea nếu cần.'}
            ]
        },contraindications': {'tuyệt_đối': [
        'Dị ứng ciprofloxacin hoặc các fluoroquinolone khác',
        'Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi',
        'Trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn, viêm khớp'
        'QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng'
        , 'Bệnh nhược cơ nặng - có thể làm nặng bệnh'],tương_đối': [
        'Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân',
        'Dùng corticosteroid - tăng nguy cơ đứt gân',
        'Ghép cơ quan - tăng nguy cơ đứt gân',
        'Tiền sử co giật - tăng nguy cơ co giật',
        'Suy thận nặng (CrCl <30) - giảm liều đáng kể',
        'Suy gan - thận trọng, có thể giảm chuyển hóa',
        'Dùng với warfarin - tăng nguy cơ chảy máu',
        'Dùng với theophylline - tăng độc tính theophylline',
        'Hoạt động thể lực nặng - tăng nguy cơ đứt gân']},contraindications_detail': {'tuyệt_đối': [
        'Dị ứng ciprofloxacin hoặc các fluoroquinolone khác',
        'Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi',
        'Trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn, viêm khớp'
        'QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng'
        , 'Bệnh nhược cơ nặng - có thể làm nặng bệnh'],tương_đối': [
        'Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân',
        'Dùng corticosteroid - tăng nguy cơ đứt gân',
        'Ghép cơ quan - tăng nguy cơ đứt gân',
        'Tiền sử co giật - tăng nguy cơ co giật',
        'Suy thận nặng (CrCl <30) - giảm liều đáng kể',
        'Suy gan - thận trọng, có thể giảm chuyển hóa',
        'Dùng với warfarin - tăng nguy cơ chảy máu',
        'Dùng với theophylline - tăng độc tính theophylline',
        'Hoạt động thể lực nặng - tăng nguy cơ đứt gân']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Ciprofloxacin là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể gây tổn thương sụn ở khớp ở thai nhi. Có báo cáo về tổn thương sụn ở trẻ em khi dùng trong thai kỳ. CHỐNG CHỈ ĐỊNH trong thai kỳ trừ khi lợi ích vượt quá nguy cơ rõ ràng và không có lựa chọn khác. Nhiễm trùng nặng có thể gây nguy hiểm cho thai nhi, nhưng nên dùng kháng sinh khác nếu có thể.'
        , 'lactation': {'safety': 'Compatible (với thận trọng)', 'details':
        'Ciprofloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, fluoroquinolone có thể gây tổn thương sụn ở trẻ sơ sinh.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với thận trọng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh. Tránh dùng nếu có lựa chọn khác.'
        }},hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Ciprofloxacin chuyển hóa một phần qua gan nhưng không phụ thuộc nhiều vào chức năng gan.'
        , 'moderate':
        'Không cần điều chỉnh liều. Thận trọng nếu có suy thận kèm theo.',
        'severe':
        'Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.'
        , 'notes':
        'Ciprofloxacin chuyển hóa một phần qua gan (CYP1A2), thải trừ chủ yếu qua thận (40-60% nguyên dạng). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận.'
        },overdose_management': {'symptoms': [
        'Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng',
        'Triệu chứng thần kinh: Co giật, kích động, lo âu, mất ngủ, trầm cảm, rối loạn tâm thần, hành vi tự sát'
        , 'Triệu chứng gân: Đau gân, viêm gân, đứt gân (đặc biệt gân Achilles)',
        'Triệu chứng tim mạch: QT kéo dài, rối loạn nhịp tim, có thể gây tử vong',
        'Triệu chứng chuyển hóa: Hạ hoặc tăng đường huyết',
        'Triệu chứng nghiêm trọng: Tổn thương thần kinh ngoại biên không hồi phục, rối loạn nhịp tim nghiêm trọng, đứt gân'
        ],antidote':
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
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2'],monitoring':
        'Theo dõi dấu hiệu sinh tồn, ECG, dấu hiệu thần kinh, dấu hiệu gân, đường huyết trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (loạn nhịp, co giật, đứt gân).'
        },reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: ngừng ngay ciprofloxacin, rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ, theo dõi dấu hiệu sinh tồn và ECG, điều trị co giật nếu có (benzodiazepine), điều trị rối loạn nhịp tim nếu có, điều trị đau gân nếu có (nghỉ ngơi, chườm lạnh), điều trị hạ đường huyết nếu có (truyền glucose), điều trị triệu chứng tiêu hóa.'},administration_instructions': {'oral': {
        'with_food':
        'Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để tránh kết tinh trong nước tiểu. KHÔNG uống với sữa hoặc sản phẩm sữa (giảm hấp thu).'
        , 'timing':
        'Uống 2 lần/ngày (q12h), cách đều 12 giờ. Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống antacid, sucralfate, sắt, kẽm, canxi. Không uống cùng lúc với các cation này.'
        },iv': {'reconstitution':
        'Pha với NS hoặc D5W. Nồng độ pha: 1-2mg/ml (tối đa). Pha 200mg trong 100ml dịch = 2mg/ml. Pha 400mg trong 200ml dịch = 2mg/ml.'
        , 'infusion_rate':
        'Truyền trong 60 phút (ít nhất 60 phút). Không truyền quá nhanh. Tốc độ: 100ml/60 phút = ~1.7ml/phút. 200ml/60 phút = ~3.3ml/phút.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],incompatibility': [
        'Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với cation (Al3+, Mg2+, Ca2+).'
        ],notes':
        'Theo dõi chức năng thận, dấu hiệu gân, thần kinh trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần. Liều: 200-400mg mỗi 12 giờ (q12h), hoặc 400mg mỗi 8 giờ (q8h) cho Pseudomonas hoặc nhiễm trùng nặng.'
        }},pediatric_dosing': {'neonates':
        'CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nguy cơ tổn thương sụn, viêm khớp.',
        'infants':
        'CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nguy cơ tổn thương sụn, viêm khớp.',
        'children':
        'CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nếu bắt buộc: 10-15mg/kg/ngày IV chia 2 lần (tối đa 400mg/ngày). Theo dõi chặt chẽ dấu hiệu đau gân, viêm gân. Nguy cơ tổn thương sụn, viêm khớp.',
        'adolescents':
        'CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác). Nếu bắt buộc: liều người lớn (250-500mg PO x 2 lần/ngày hoặc 200-400mg IV mỗi 12 giờ). Theo dõi chặt chẽ dấu hiệu đau gân, viêm gân.',
        'notes':
        'CHỐNG CHỈ ĐỊNH ở trẻ <18 tuổi do nguy cơ tổn thương sụn, viêm khớp. Chỉ dùng trong trường hợp đặc biệt như nhiễm trùng nặng (ví dụ: nhiễm trùng Pseudomonas nặng) không có lựa chọn khác. Nếu dùng, theo dõi chặt chẽ dấu hiệu đau gân, viêm gân, đứt gân. Ngừng ngay nếu có đau gân.'},geriatric_dosing': {'considerations':
        'Người cao tuổi (>60 tuổi) có nguy cơ cao hơn đứt gân, viêm gân (đặc biệt gân Achilles). Suy thận phổ biến hơn, cần điều chỉnh liều. Tăng nguy cơ QT kéo dài, rối loạn nhịp tim. Tăng nguy cơ co giật.',
        'dose_adjustment':
        'Điều chỉnh liều theo chức năng thận: CrCl 30-60 → giảm liều 25-50%, CrCl <30 → giảm liều 50-75%. Khởi đầu với liều thấp hơn. Thận trọng với liều cao.',
        'monitoring':
        'Theo dõi chặt chẽ dấu hiệu đau gân, viêm gân, đứt gân (đặc biệt gân Achilles). Theo dõi ECG (QT interval). Theo dõi chức năng thận (creatinine, CrCl). Theo dõi dấu hiệu thần kinh (co giật, kích động). Ngừng ngay nếu có đau gân.'},brand_names': {'vietnam': [
        'Ciprofloxacin', 'Cipro', 'Ciprobay', 'Ciproxin', 'Ciprofloxacin Stada'],common': [
        'Cipro', 'Ciprofloxacin', 'Ciprobay'],range': '5,000 - 25,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note':
        'Giá thay đổi theo thương hiệu và nhà thuốc. Ciprofloxacin generic thường rẻ hơn (5,000-15,000 VND/viên 500mg). Dạng IV: 50,000-150,000 VND/lọ 200mg.'},references': {'primary_sources': [
        'FDA Drug Label - Ciprofloxacin (Cipro)',
        'UpToDate - Ciprofloxacin: Drug Information',
        'Medscape - Ciprofloxacin Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Ciprofloxacin Monograph',
        'Micromedex - Ciprofloxacin Drug Information',
        'IDSA Guidelines - Antimicrobial Therapy'],last_updated':
        '2024-12-19', 'evidence_level':
        'A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }},
    
    "Gemifloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Gemifloxacin, Factive",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi mắc phải cộng đồng (CAP)",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn đường tiết niệu"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Có thai",
            "Trẻ em <18 tuổi",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_cap": "320mg x 1 lần/ngày x 5-7 ngày",
            "adult_uti": "320mg x 1 lần/ngày x 3-7 ngày",
            "notes": "Uống cách xa antacid 2 giờ. Không dùng với sữa. Dùng 1 lần/ngày."
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
            "Rối loạn tâm thần (hiếm)",
            "Phát ban (phổ biến hơn các fluoroquinolone khác)"
        ],
        "interactions": [
            "Antacid: giảm hấp thu",
            "Warfarin: tăng INR",
            "Probenecid: tăng nồng độ gemifloxacin"
        ],
        "pregnancy": "C - Tránh dùng",
        "mechanism_of_action": "Gemifloxacin là fluoroquinolone kháng sinh phổ rộng thuộc thế hệ thứ tư. Ức chế DNA gyrase (topoisomerase II) ở vi khuẩn Gram-âm và topoisomerase IV ở vi khuẩn Gram-dương, các enzyme cần thiết cho quá trình sao chép, phiên mã, sửa chữa, và tái tổ hợp DNA. Dẫn đến tổn thương DNA không thể sửa chữa và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, H. influenzae, Neisseria, Moraxella), Gram-dương (Streptococcus pneumoniae, bao gồm một số chủng kháng penicillin), và một số vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Gemifloxacin có hoạt tính tốt với Streptococcus pneumoniae, thường dùng trong điều trị viêm phổi mắc phải cộng đồng. Dùng 1 lần/ngày.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
            "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles)",
            "Thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần)",
            "Tim mạch (ECG - QT kéo dài, rối loạn nhịp tim)",
            "Phát ban - phổ biến hơn các fluoroquinolone khác",
            "Chức năng thận (creatinine, BUN) - điều chỉnh liều ở suy thận"
        ],
        "precautions": [
            "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles)",
            "NGỪNG NGAY nếu có đau, sưng gân",
            "QT kéo dài → không dùng với các thuốc kéo dài QT khác",
            "Co giật → không dùng ở bệnh nhân có tiền sử co giật",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp",
            "Phát ban - phổ biến hơn các fluoroquinolone khác, ngừng nếu có phát ban nặng",
            "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm, canxi (cách ít nhất 2 giờ)",
            "Điều chỉnh liều ở suy thận (CrCl <50 - giảm liều 25-75%)"
        ],
        "pharmacokinetics": {
            "half_life": "7-8 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "24 giờ",
            "protein_binding": "60-70%",
            "clearance": "Thận: bài tiết chủ yếu qua thận (25-40% nguyên dạng), gan (chuyển hóa một phần). Dùng 1 lần/ngày."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles). QT kéo dài và rối loạn nhịp tim. Rối loạn thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Gemifloxacin có thể ức chế chuyển hóa warfarin, tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc ngừng gemifloxacin. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacid, Sucralfate, Sắt, Kẽm, Canxi",
                    "mechanism": "Tạo phức hợp không hòa tan, giảm hấp thu gemifloxacin",
                    "effect": "Giảm hấp thu gemifloxacin, giảm hiệu quả",
                    "management": "Cách ít nhất 2 giờ. Uống gemifloxacin trước antacid/sucralfate/sắt/kẽm/canxi 2 giờ, hoặc sau 4 giờ."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của gemifloxacin, tăng nồng độ",
                    "effect": "Tăng nồng độ gemifloxacin, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều gemifloxacin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng gemifloxacin hoặc các fluoroquinolone khác",
                "Có thai (category C) - tránh dùng",
                "Trẻ em <18 tuổi - nguy cơ đứt gân, viêm gân",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Tiền sử co giật"
            ],
            "tương_đối": [
                "Suy thận (CrCl <50) - giảm liều 25-75%",
                "Người già (>60 tuổi) - tăng nguy cơ đứt gân, viêm gân",
                "Dùng corticosteroid - tăng nguy cơ đứt gân, viêm gân"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Gemifloxacin là category C. Tránh dùng trong thai kỳ, đặc biệt trong tam cá nguyệt thứ ba.",
            "lactation": {
                "safety": "Compatible",
                "details": "Gemifloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Gemifloxacin chuyển hóa một phần qua gan nhưng chủ yếu thải qua thận.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị và độc tính.",
            "notes": "Gemifloxacin chủ yếu thải qua thận, một phần chuyển hóa qua gan. Suy gan thường không ảnh hưởng đáng kể đến nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn tiêu hóa (buồn nôn, nôn, tiêu chảy)",
                "Đau gân, viêm gân",
                "Co giật",
                "Rối loạn tâm thần (kích động, lo âu, trầm cảm)",
                "QT kéo dài, rối loạn nhịp tim",
                "Phát ban"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng gemifloxacin ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Điều trị co giật nếu có (benzodiazepines)",
                "Theo dõi ECG (QT interval)",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị hỗ trợ: truyền dịch nếu cần"
            ],
            "monitoring": "ECG (QT interval), dấu hiệu sinh tồn, dấu hiệu co giật, dấu hiệu rối loạn tâm thần, phát ban"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ.",
                "timing": "Uống 1 lần/ngày. Cách xa antacid, sucralfate, sắt, kẽm, canxi ít nhất 2 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Gemifloxacin (Factive)",
                "UpToDate - Gemifloxacin: Drug Information",
                "Micromedex - Gemifloxacin",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"musculoskeletal": "Black Box Warning - Tendon rupture, tendonitis (especially Achilles)", "neurological": "Black Box Warning - Peripheral neuropathy (may be irreversible)", "cardiovascular": "QT prolongation - Black Box Warning", "dermatologic": "Photosensitivity", "psychiatric": "CNS effects (seizures, psychosis)"},
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Tendon signs (Black Box Warning - stop immediately if tendon pain/swelling)", "ECG (QT prolongation - Black Box Warning)", "Neurological signs (peripheral neuropathy - Black Box Warning)", "CNS effects (seizures, psychosis)", "Photosensitivity", "Renal function (dose adjustment required)"],
            "look_alike_sound_alike": ["Gemifloxacin", "Gatifloxacin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Tendon Rupture/Tendonitis",
            "FDA Black Box Warning - Peripheral Neuropathy (may be irreversible)",
            "FDA Black Box Warning - QT Prolongation",
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    "Norfloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Norfloxacin, Noroxin",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu không biến chứng",
            "Nhiễm khuẩn đường tiết niệu tái phát",
            "Viêm tuyến tiền liệt do vi khuẩn"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Có thai",
            "Trẻ em <18 tuổi",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_uti_uncomplicated": "400mg x 2 lần/ngày x 3 ngày",
            "adult_uti_complicated": "400mg x 2 lần/ngày x 7-10 ngày",
            "adult_prostatitis": "400mg x 2 lần/ngày x 28 ngày",
            "notes": "Uống cách xa antacid 2 giờ. Không dùng với sữa. Hấp thu kém, chỉ dùng cho nhiễm khuẩn đường tiết niệu."
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
            "Theophylline: tăng nồng độ theophylline"
        ],
        "pregnancy": "C - Tránh dùng",
        "mechanism_of_action": "Norfloxacin là fluoroquinolone kháng sinh phổ rộng thuộc thế hệ thứ nhất. Ức chế DNA gyrase (topoisomerase II) ở vi khuẩn Gram-âm, các enzyme cần thiết cho quá trình sao chép, phiên mã, sửa chữa, và tái tổ hợp DNA. Dẫn đến tổn thương DNA không thể sửa chữa và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, H. influenzae, Neisseria), một số Gram-dương. Norfloxacin hấp thu kém qua đường uống (30-40%), nồng độ trong máu thấp, nhưng nồng độ trong nước tiểu cao, nên chỉ dùng cho nhiễm khuẩn đường tiết niệu. Không hiệu quả với Pseudomonas aeruginosa (kém hơn ciprofloxacin).",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
            "Cấy nước tiểu để xác định vi khuẩn và độ nhạy cảm",
            "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles)",
            "Thần kinh trung ương (co giật, kích động, mất ngủ)",
            "Tim mạch (ECG - QT kéo dài)",
            "Chức năng thận (creatinine, BUN) - điều chỉnh liều ở suy thận"
        ],
        "precautions": [
            "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles)",
            "NGỪNG NGAY nếu có đau, sưng gân",
            "QT kéo dài → không dùng với các thuốc kéo dài QT khác",
            "Co giật → không dùng ở bệnh nhân có tiền sử co giật",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp",
            "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm, canxi (cách ít nhất 2 giờ)",
            "Điều chỉnh liều ở suy thận (CrCl <50 - giảm liều 25-75%)",
            "Chỉ dùng cho nhiễm khuẩn đường tiết niệu (hấp thu kém, nồng độ trong máu thấp)"
        ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "12 giờ",
            "protein_binding": "10-15%",
            "clearance": "Thận: bài tiết chủ yếu qua thận (30% nguyên dạng), gan (chuyển hóa một phần). Hấp thu kém (30-40%), nồng độ trong máu thấp, nhưng nồng độ trong nước tiểu cao."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles). QT kéo dài và rối loạn nhịp tim. Rối loạn thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Norfloxacin có thể ức chế chuyển hóa warfarin, tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc ngừng norfloxacin. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Norfloxacin ức chế chuyển hóa theophylline qua CYP1A2",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính",
                    "management": "Theo dõi nồng độ theophylline và dấu hiệu độc tính. Giảm liều theophylline 25-50%."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacid, Sucralfate, Sắt, Kẽm, Canxi",
                    "mechanism": "Tạo phức hợp không hòa tan, giảm hấp thu norfloxacin",
                    "effect": "Giảm hấp thu norfloxacin, giảm hiệu quả",
                    "management": "Cách ít nhất 2 giờ. Uống norfloxacin trước antacid/sucralfate/sắt/kẽm/canxi 2 giờ, hoặc sau 4 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng norfloxacin hoặc các fluoroquinolone khác",
                "Có thai (category C) - tránh dùng",
                "Trẻ em <18 tuổi - nguy cơ đứt gân, viêm gân",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Tiền sử co giật"
            ],
            "tương_đối": [
                "Suy thận (CrCl <50) - giảm liều 25-75%",
                "Người già (>60 tuổi) - tăng nguy cơ đứt gân, viêm gân",
                "Dùng corticosteroid - tăng nguy cơ đứt gân, viêm gân"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Norfloxacin là category C. Tránh dùng trong thai kỳ, đặc biệt trong tam cá nguyệt thứ ba.",
            "lactation": {
                "safety": "Compatible",
                "details": "Norfloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Norfloxacin chuyển hóa một phần qua gan nhưng chủ yếu thải qua thận.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị và độc tính.",
            "notes": "Norfloxacin chủ yếu thải qua thận, một phần chuyển hóa qua gan. Suy gan thường không ảnh hưởng đáng kể đến nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn tiêu hóa (buồn nôn, nôn, tiêu chảy)",
                "Đau gân, viêm gân",
                "Co giật",
                "Rối loạn tâm thần (kích động, lo âu, trầm cảm)",
                "QT kéo dài, rối loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng norfloxacin ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Điều trị co giật nếu có (benzodiazepines)",
                "Theo dõi ECG (QT interval)",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị hỗ trợ: truyền dịch nếu cần"
            ],
            "monitoring": "ECG (QT interval), dấu hiệu sinh tồn, dấu hiệu co giật, dấu hiệu rối loạn tâm thần"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ.",
                "timing": "Uống 2 lần/ngày (mỗi 12 giờ). Cách xa antacid, sucralfate, sắt, kẽm, canxi ít nhất 2 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Norfloxacin (Noroxin)",
                "UpToDate - Norfloxacin: Drug Information",
                "Micromedex - Norfloxacin",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"musculoskeletal": "Black Box Warning - Tendon rupture, tendonitis (especially Achilles)", "neurological": "Black Box Warning - Peripheral neuropathy (may be irreversible)", "cardiovascular": "QT prolongation - Black Box Warning", "dermatologic": "Photosensitivity", "psychiatric": "CNS effects (seizures, psychosis)"},
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Tendon signs (Black Box Warning - stop immediately if tendon pain/swelling)", "ECG (QT prolongation - Black Box Warning)", "Neurological signs (peripheral neuropathy - Black Box Warning)", "CNS effects (seizures, psychosis)", "Photosensitivity", "Renal function (dose adjustment required)"],
            "look_alike_sound_alike": ["Norfloxacin", "Ciprofloxacin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Tendon Rupture/Tendonitis",
            "FDA Black Box Warning - Peripheral Neuropathy (may be irreversible)",
            "FDA Black Box Warning - QT Prolongation",
            "IDSA Guidelines - Urinary Tract Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    
    "Ofloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Ofloxacin, Floxin",
        "administration": ["PO", "IV", "Ophthalmic", "Otic"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn da mô mềm",
            "Viêm kết mạc (ophthalmic)",
            "Viêm tai ngoài (otic)"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Có thai",
            "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_po": "200-400mg x 2 lần/ngày",
            "adult_iv": "200-400mg IV mỗi 12 giờ",
            "adult_ophthalmic": "1-2 giọt vào mắt bị nhiễm trùng mỗi 2-4 giờ x 2 ngày, sau đó mỗi 4-6 giờ",
            "adult_otic": "10 giọt vào tai bị nhiễm trùng x 2 lần/ngày x 10 ngày",
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
            "Probenecid: tăng nồng độ ofloxacin"
        ],
        "pregnancy": "C - Tránh dùng",
        "mechanism_of_action": "Ofloxacin là fluoroquinolone kháng sinh phổ rộng thuộc thế hệ thứ hai. Ức chế DNA gyrase (topoisomerase II) ở vi khuẩn Gram-âm và topoisomerase IV ở vi khuẩn Gram-dương, các enzyme cần thiết cho quá trình sao chép, phiên mã, sửa chữa, và tái tổ hợp DNA. Dẫn đến tổn thương DNA không thể sửa chữa và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, H. influenzae, Neisseria, Moraxella), một số Gram-dương, và một số vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Ofloxacin có hoạt tính tốt với Chlamydia trachomatis, thường dùng trong điều trị nhiễm Chlamydia. Không hiệu quả với Pseudomonas aeruginosa (kém hơn ciprofloxacin).",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
            "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc",
            "Thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần)",
            "Tim mạch (ECG - QT kéo dài, rối loạn nhịp tim) - đặc biệt ở bệnh nhân có nguy cơ",
            "Chức năng thận (creatinine, BUN) - điều chỉnh liều ở suy thận",
            "Chức năng gan (ALT, AST) - hiếm viêm gan nặng"
        ],
        "precautions": [
            "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc",
            "Nguy cơ tăng ở: > 60 tuổi, dùng corticosteroid, ghép thận, ghép tim, ghép phổi, hoạt động thể lực",
            "NGỪNG NGAY nếu có đau, sưng gân - nghỉ ngơi, không vận động",
            "QT kéo dài → không dùng với các thuốc kéo dài QT khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp",
            "Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID (tăng nguy cơ)",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng, mặc quần áo che",
            "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm, canxi (cách ít nhất 2 giờ)",
            "Điều chỉnh liều ở suy thận (CrCl <50 - giảm liều 25-50%)",
            "Không hiệu quả với Pseudomonas aeruginosa (dùng ciprofloxacin thay thế)"
        ],
        "pharmacokinetics": {
            "half_life": "5-7 giờ",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "12 giờ",
            "protein_binding": "20-32%",
            "clearance": "Thận (80-90% thải nguyên dạng), gan (10-20% chuyển hóa)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dạng ophthalmic/otic: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
        "black_box_warnings": "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc. Nguy cơ tăng ở > 60 tuổi, dùng corticosteroid, ghép tạng, hoạt động thể lực. NGỪNG NGAY nếu có đau, sưng gân. QT kéo dài và rối loạn nhịp tim. Rối loạn thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Ofloxacin có thể ức chế chuyển hóa warfarin, tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc ngừng ofloxacin. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Ofloxacin ức chế chuyển hóa theophylline qua CYP1A2",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính (buồn nôn, nôn, co giật, rối loạn nhịp tim)",
                    "management": "Theo dõi nồng độ theophylline và dấu hiệu độc tính. Giảm liều theophylline 25-50%."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacid, Sucralfate, Sắt, Kẽm, Canxi",
                    "mechanism": "Tạo phức hợp không hòa tan, giảm hấp thu ofloxacin",
                    "effect": "Giảm hấp thu ofloxacin, giảm hiệu quả",
                    "management": "Cách ít nhất 2 giờ. Uống ofloxacin trước antacid/sucralfate/sắt/kẽm/canxi 2 giờ, hoặc sau 4 giờ."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của ofloxacin, tăng nồng độ",
                    "effect": "Tăng nồng độ ofloxacin, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều ofloxacin."
                },
                {
                    "drug": "NSAIDs",
                    "mechanism": "Tăng nguy cơ co giật",
                    "effect": "Tăng nguy cơ co giật",
                    "management": "Thận trọng. Tránh dùng với bệnh nhân có tiền sử co giật."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ofloxacin hoặc các fluoroquinolone khác",
                "Có thai (category C) - tránh dùng",
                "Trẻ em <18 tuổi (trừ trường hợp đặc biệt) - nguy cơ đứt gân, viêm gân",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Tiền sử co giật"
            ],
            "tương_đối": [
                "Suy thận (CrCl <50) - giảm liều 25-75%",
                "Suy gan - thận trọng",
                "Người già (>60 tuổi) - tăng nguy cơ đứt gân, viêm gân",
                "Dùng corticosteroid - tăng nguy cơ đứt gân, viêm gân",
                "Ghép tạng - tăng nguy cơ đứt gân, viêm gân"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ofloxacin là category C. Nghiên cứu trên động vật cho thấy có thể gây độc tính cho thai nhi (tổn thương sụn khớp). Không có nghiên cứu đầy đủ trên người. Tránh dùng trong thai kỳ, đặc biệt trong tam cá nguyệt thứ ba (nguy cơ tổn thương sụn khớp thai nhi).",
            "lactation": {
                "safety": "Compatible",
                "details": "Ofloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ofloxacin chuyển hóa một phần qua gan nhưng chủ yếu thải qua thận.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị và độc tính.",
            "notes": "Ofloxacin chủ yếu thải qua thận (80-90% thải nguyên dạng), một phần chuyển hóa qua gan (10-20%). Suy gan thường không ảnh hưởng đáng kể đến nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn tiêu hóa (buồn nôn, nôn, tiêu chảy)",
                "Đau gân, viêm gân",
                "Co giật",
                "Rối loạn tâm thần (kích động, lo âu, trầm cảm)",
                "QT kéo dài, rối loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ofloxacin ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Điều trị co giật nếu có (benzodiazepines)",
                "Theo dõi ECG (QT interval)",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị hỗ trợ: truyền dịch nếu cần"
            ],
            "monitoring": "ECG (QT interval), dấu hiệu sinh tồn, dấu hiệu co giật, dấu hiệu rối loạn tâm thần"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ.",
                "timing": "Uống 2 lần/ngày (mỗi 12 giờ). Cách xa antacid, sucralfate, sắt, kẽm, canxi ít nhất 2 giờ."
            },
            "iv": {
                "reconstitution": "Ofloxacin IV: 200-400mg pha với 50-100ml NaCl 0.9% hoặc D5W",
                "infusion_rate": "Truyền trong 30-60 phút (không truyền nhanh)",
                "compatibility": ["NaCl 0.9%", "D5W"],
                "incompatibility": [],
                "notes": "Không truyền nhanh (tăng nguy cơ co giật). Truyền trong 30-60 phút."
            },
            "ophthalmic": {
                "reconstitution": "N/A",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "1-2 giọt vào mắt bị nhiễm trùng mỗi 2-4 giờ x 2 ngày, sau đó mỗi 4-6 giờ. Không chạm đầu ống vào mắt."
            },
            "otic": {
                "reconstitution": "N/A",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "10 giọt vào tai bị nhiễm trùng x 2 lần/ngày x 10 ngày. Giữ đầu nghiêng 5 phút sau khi nhỏ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ofloxacin (Floxin)",
                "UpToDate - Ofloxacin: Drug Information",
                "Micromedex - Ofloxacin",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs"
        }
    },
    
    "Sparfloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Sparfloxacin, Sparflo",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi mắc phải cộng đồng (CAP)",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn đường tiết niệu"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Có thai",
            "Trẻ em <18 tuổi",
            "QT kéo dài",
            "Nhạy cảm ánh sáng nặng"
        ],
        "dosage": {
            "adult_cap": "200mg x 1 lần/ngày x 7-10 ngày (ngày đầu: 400mg x 1 lần)",
            "adult_uti": "200mg x 1 lần/ngày x 3-7 ngày",
            "notes": "Ngày đầu: 400mg x 1 lần (loading dose), sau đó 200mg x 1 lần/ngày. Uống cách xa antacid 2 giờ. Không dùng với sữa."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Đau gân, viêm gân (có thể đứt gân)",
            "QT kéo dài (nhiều hơn các fluoroquinolone khác)",
            "Nhạy cảm ánh sáng (phổ biến, có thể nặng)",
            "Co giật (hiếm)",
            "Rối loạn tâm thần (hiếm)"
        ],
        "interactions": [
            "Antacid: giảm hấp thu",
            "Warfarin: tăng INR",
            "Thuốc QT kéo dài: tăng nguy cơ rối loạn nhịp",
            "Probenecid: tăng nồng độ sparfloxacin"
        ],
        "pregnancy": "C - Tránh dùng",
        "mechanism_of_action": "Sparfloxacin là fluoroquinolone kháng sinh phổ rộng. Ức chế DNA gyrase (topoisomerase II) ở vi khuẩn Gram-âm và topoisomerase IV ở vi khuẩn Gram-dương, các enzyme cần thiết cho quá trình sao chép, phiên mã, sửa chữa, và tái tổ hợp DNA. Dẫn đến tổn thương DNA không thể sửa chữa và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, H. influenzae, Neisseria, Moraxella), Gram-dương (Streptococcus pneumoniae, bao gồm một số chủng kháng penicillin), và một số vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Sparfloxacin có hoạt tính tốt với Streptococcus pneumoniae và các vi khuẩn không điển hình. Đặc biệt: nguy cơ QT kéo dài và nhạy cảm ánh sáng cao hơn các fluoroquinolone khác.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
            "ECG - QT interval (QUAN TRỌNG: sparfloxacin có nguy cơ QT kéo dài cao hơn các fluoroquinolone khác)",
            "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles)",
            "Nhạy cảm ánh sáng - phát ban, bỏng nắng (phổ biến, có thể nặng)",
            "Thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần)",
            "Chức năng thận (creatinine, BUN) - điều chỉnh liều ở suy thận"
        ],
        "precautions": [
            "QT KÉO DÀI - nguy cơ cao hơn các fluoroquinolone khác → không dùng với các thuốc QT kéo dài khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp, suy tim, hạ kali máu, hạ magie máu",
            "NHẠY CẢM ÁNH SÁNG - phổ biến và có thể nặng → tránh ánh nắng trực tiếp, dùng kem chống nắng SPF 30+, mặc quần áo che, đội mũ",
            "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - NGỪNG NGAY nếu có đau, sưng gân",
            "Co giật → không dùng ở bệnh nhân có tiền sử co giật",
            "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm, canxi (cách ít nhất 2 giờ)",
            "Điều chỉnh liều ở suy thận (CrCl <50 - giảm liều 25-75%)"
        ],
        "pharmacokinetics": {
            "half_life": "16-20 giờ (dài)",
            "onset": "1-2 giờ (PO)",
            "duration": "24 giờ",
            "protein_binding": "45-50%",
            "clearance": "Thận: bài tiết chủ yếu qua thận (một phần nguyên dạng), gan (chuyển hóa một phần). Dùng 1 lần/ngày sau liều loading."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Nguy cơ QT kéo dài và rối loạn nhịp tim (torsades de pointes) - cao hơn các fluoroquinolone khác. Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles). Nhạy cảm ánh sáng nặng - có thể gây bỏng nắng nghiêm trọng. Rối loạn thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Sparfloxacin có thể ức chế chuyển hóa warfarin, tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc ngừng sparfloxacin. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Thuốc QT kéo dài (Amiodarone, Sotalol, Antipsychotics)",
                    "mechanism": "Cả hai đều kéo dài QT, tác dụng cộng hợp",
                    "effect": "Tăng nguy cơ QT kéo dài nặng, torsades de pointes, rối loạn nhịp tim nguy hiểm",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, theo dõi ECG chặt chẽ. Theo dõi kali, magie."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacid, Sucralfate, Sắt, Kẽm, Canxi",
                    "mechanism": "Tạo phức hợp không hòa tan, giảm hấp thu sparfloxacin",
                    "effect": "Giảm hấp thu sparfloxacin, giảm hiệu quả",
                    "management": "Cách ít nhất 2 giờ. Uống sparfloxacin trước antacid/sucralfate/sắt/kẽm/canxi 2 giờ, hoặc sau 4 giờ."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của sparfloxacin, tăng nồng độ",
                    "effect": "Tăng nồng độ sparfloxacin, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều sparfloxacin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng sparfloxacin hoặc các fluoroquinolone khác",
                "Có thai (category C) - tránh dùng",
                "Trẻ em <18 tuổi - nguy cơ đứt gân, viêm gân",
                "QT kéo dài hoặc rối loạn nhịp tim nặng",
                "Tiền sử co giật",
                "Nhạy cảm ánh sáng nặng"
            ],
            "tương_đối": [
                "Suy thận (CrCl <50) - giảm liều 25-75%",
                "Người già (>60 tuổi) - tăng nguy cơ đứt gân, viêm gân, QT kéo dài",
                "Dùng corticosteroid - tăng nguy cơ đứt gân, viêm gân",
                "Suy tim - tăng nguy cơ QT kéo dài",
                "Hạ kali máu, hạ magie máu - tăng nguy cơ QT kéo dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Sparfloxacin là category C. Tránh dùng trong thai kỳ, đặc biệt trong tam cá nguyệt thứ ba.",
            "lactation": {
                "safety": "Compatible",
                "details": "Sparfloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Sparfloxacin chuyển hóa một phần qua gan nhưng chủ yếu thải qua thận.",
            "moderate": "Không cần điều chỉnh liều thường quy. Theo dõi đáp ứng điều trị.",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi đáp ứng điều trị và độc tính.",
            "notes": "Sparfloxacin chủ yếu thải qua thận, một phần chuyển hóa qua gan. Suy gan thường không ảnh hưởng đáng kể đến nồng độ."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn tiêu hóa (buồn nôn, nôn, tiêu chảy)",
                "Đau gân, viêm gân",
                "QT kéo dài nặng, rối loạn nhịp tim (torsades de pointes)",
                "Co giật",
                "Rối loạn tâm thần (kích động, lo âu, trầm cảm)",
                "Nhạy cảm ánh sáng nặng (bỏng nắng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng sparfloxacin ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục (QT interval) - QUAN TRỌNG",
                "Điều trị rối loạn nhịp tim nếu có (magnesium sulfate cho torsades de pointes)",
                "Điều trị co giật nếu có (benzodiazepines)",
                "Theo dõi dấu hiệu sinh tồn",
                "Điều trị hỗ trợ: truyền dịch nếu cần",
                "Bảo vệ khỏi ánh sáng (nhạy cảm ánh sáng)"
            ],
            "monitoring": "ECG liên tục (QT interval), dấu hiệu sinh tồn, dấu hiệu co giật, dấu hiệu rối loạn tâm thần, nhạy cảm ánh sáng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ.",
                "timing": "Ngày đầu: 400mg x 1 lần (loading dose). Sau đó: 200mg x 1 lần/ngày. Cách xa antacid, sucralfate, sắt, kẽm, canxi ít nhất 2 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sparfloxacin (Sparflo)",
                "UpToDate - Sparfloxacin: Drug Information",
                "Micromedex - Sparfloxacin",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved, multiple RCTs"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"musculoskeletal": "Black Box Warning - Tendon rupture, tendonitis (especially Achilles)", "neurological": "Black Box Warning - Peripheral neuropathy (may be irreversible)", "cardiovascular": "Severe QT prolongation - Black Box Warning (higher risk than other fluoroquinolones)", "dermatologic": "Severe photosensitivity - Black Box Warning", "psychiatric": "CNS effects (seizures, psychosis)"},
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (QT prolongation - Black Box Warning, higher risk than other fluoroquinolones)", "Tendon signs (Black Box Warning - stop immediately if tendon pain/swelling)", "Neurological signs (peripheral neuropathy - Black Box Warning)", "Photosensitivity (Black Box Warning - severe)", "CNS effects (seizures, psychosis)", "Renal function (dose adjustment required)"],
            "look_alike_sound_alike": ["Sparfloxacin", "Ciprofloxacin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Severe QT Prolongation (higher risk than other fluoroquinolones)",
            "FDA Black Box Warning - Tendon Rupture/Tendonitis",
            "FDA Black Box Warning - Peripheral Neuropathy (may be irreversible)",
            "FDA Black Box Warning - Severe Photosensitivity",
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
}

__all__ = ['FLUOROQUINOLONES_DRUGS']
