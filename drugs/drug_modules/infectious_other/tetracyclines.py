"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Tetracyclines

TETRACYCLINES_DRUGS = {
    "Doxycycline": {'group': 'Infectious Disease - Tetracycline Antibiotic', 'vietnamese_name':
        'Doxycycline, Vibramycin', 'administration': ['PO', 'IV'],
        'indications': ['Nhiễm trùng đường hô hấp',
        'Nhiễm trùng da (mụn trứng cá)', 'Chlamydia', 'Lyme disease',
        'Sốt rét phòng ngừa', 'Rickettsia', 'Mycoplasma'], 'contraindications':
        ['Dị ứng doxycycline/tetracycline', 'Có thai (3 tháng cuối)',
        'Trẻ em <8 tuổi (gây vàng răng)'], 'dosage': {'adult_respiratory':
        '100mg x 2 lần/ngày x 7-14 ngày', 'adult_chlamydia':
        '100mg x 2 lần/ngày x 7 ngày', 'adult_acne': '50-100mg x 1-2 lần/ngày',
        'adult_malaria_prophylaxis': '100mg x 1 lần/ngày', 'notes':
        'Uống với nhiều nước, tránh nằm ngay sau khi uống. Tránh nắng'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Buồn nôn, nôn',
        'Loét thực quản (nếu không uống đủ nước)',
        'Phản ứng quang hóa (nhạy cảm ánh sáng)', 'Vàng răng (trẻ em, có thai)',
        'Tăng áp lực nội sọ (hiếm)', 'Độc gan (liều cao)'], 'interactions': [
        'Antacid/Sắt/Calcium: giảm hấp thu - cách 2 giờ',
        'Warfarin: tăng tác dụng chống đông', 'Digoxin: tăng nồng độ digoxin',
        'Phenytoin/Carbamazepine: giảm nồng độ doxycycline'], 'pregnancy':
        'D - Chống chỉ định trong 3 tháng cuối', 'mechanism_of_action':
        'Tetracycline kháng sinh phổ rộng. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 30S của ribosome, ngăn cản gắn aminoacyl-tRNA. Phổ kháng khuẩn: Gram-dương, Gram-âm, vi khuẩn không điển hình (Chlamydia, Mycoplasma, Rickettsia, Borrelia), và một số ký sinh trùng (Plasmodium). Không hiệu quả với Pseudomonas hoặc Proteus. Đặc biệt hiệu quả với vi khuẩn không điển hình và được dùng trong nhiễm trùng đường hô hấp, Lyme disease, và sốt rét.'
        , 'monitoring': ['Dấu hiệu nhiễm trùng (sốt, WBC)',
        'Cấy máu và cấy từ vị trí nhiễm trùng',
        'Dạ dày-ruột (buồn nôn, nôn, tiêu chảy, viêm thực quản)',
        'Da (tăng độ nhạy cảm với ánh sáng, phát ban)',
        'Răng và xương (ở trẻ em < 8 tuổi: ố vàng răng vĩnh viễn, chậm phát triển xương)'
        ,
        'Chức năng gan (ALT, AST) - hiếm viêm gan, tăng áp lực nội sọ giả (ở phụ nữ)'
        , 'Thận (không tích lũy ở suy thận, nhưng theo dõi)'], 'precautions': [
        'KHÔNG dùng cho trẻ em < 8 tuổi (trừ trường hợp đe dọa tính mạng) - gây ố vàng răng vĩnh viễn, chậm phát triển xương'
        ,
        'Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng, mặc quần áo che phủ'
        ,
        'Uống với nhiều nước (ít nhất 200ml) và ở tư thế đứng để tránh viêm thực quản (đau khi nuốt, khó nuốt)'
        , 'KHÔNG uống nằm ngửa hoặc trước khi ngủ',
        'Tương tác với nhiều thuốc và thực phẩm: giảm hấp thu với antacid, sắt, canxi, magie, kẽm, sữa (cách 2 giờ)'
        , 'Tương tác với warfarin → tăng nguy cơ chảy máu (theo dõi INR)',
        'Tương tác với thuốc tránh thai → giảm hiệu quả (dùng biện pháp tránh thai khác)'
        ,
        'Tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị) - đặc biệt ở phụ nữ, ngừng nếu có'
        ,
        'Không dùng trong 3 tháng cuối thai kỳ (nguy cơ ố vàng răng, chậm phát triển xương ở trẻ)'
        ,
        'Uống với thức ăn để giảm kích ứng dạ dày (nhưng giảm hấp thu một phần)'
        ], 'pharmacokinetics': {'half_life': '18-22 giờ (dài)', 'onset':
        '1-2 giờ (PO), ngay lập tức (IV)', 'duration': 'q12h hoặc q24h (PO/IV)',
        'protein_binding': '80-90%', 'metabolism':
        'Gan (một phần), bài tiết một phần nguyên dạng', 'clearance':
        'Gan và thận, KHÔNG tích lũy ở suy thận (khác với tetracycline cũ)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nang: tránh ẩm. Bảo quản tốt hơn các tetracycline cũ (ít bị hỏng).'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, ố vàng răng vĩnh viễn ở trẻ em < 8 tuổi là không hồi phục. Tăng áp lực nội sọ giả có thể gây mù. Viêm thực quản có thể nghiêm trọng.'
        , 'drug_interactions': {'major': [{'drug':
        'Antacid, Sắt, Calcium, Magnesium, Kẽm, Bismuth', 'mechanism':
        'Các cation hóa trị 2+ (Ca²⁺, Mg²⁺, Fe²⁺, Zn²⁺) tạo phức hợp không hòa tan với doxycycline, làm giảm hấp thu doxycycline.'
        , 'effect':
        'Giảm hấp thu doxycycline đáng kể (50-90%), giảm hiệu quả kháng khuẩn',
        'management':
        'Cách ít nhất 2 giờ giữa doxycycline và các thuốc/thực phẩm chứa cation (antacid, sắt, canxi, magie, kẽm, sữa, bismuth). Uống doxycycline trước bữa ăn hoặc 2 giờ sau bữa ăn nếu bữa ăn chứa nhiều sữa hoặc thực phẩm giàu canxi.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Doxycycline có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể đẩy warfarin khỏi albumin (protein binding cao).'
        , 'effect': 'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng doxycycline). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân dùng kéo dài (>7 ngày).'
        }], 'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Doxycycline có thể làm tăng hấp thu digoxin bằng cách thay đổi hệ vi khuẩn đường ruột, làm tăng nồng độ digoxin.'
        , 'effect':
        'Tăng nồng độ digoxin, tăng nguy cơ độc tính digoxin (buồn nôn, rối loạn nhịp tim)'
        , 'management':
        'Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin. Theo dõi dấu hiệu độc tính digoxin.'
        }, {'drug': 'Phenytoin, Carbamazepine', 'mechanism':
        'Phenytoin và carbamazepine cảm ứng enzyme chuyển hóa doxycycline, làm giảm nồng độ doxycycline.'
        , 'effect': 'Giảm nồng độ doxycycline, giảm hiệu quả kháng khuẩn',
        'management':
        'Có thể cần tăng liều doxycycline. Theo dõi đáp ứng điều trị.'}, {
        'drug': 'Thuốc tránh thai đường uống', 'mechanism':
        'Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột. Ngoài ra, doxycycline có thể cảm ứng enzyme chuyển hóa estrogen.'
        , 'effect':
        'Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)',
        'management':
        'Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng.'
        }], 'minor': [{'drug': 'Penicillin', 'mechanism':
        'Doxycycline có thể đối kháng với penicillin trong một số trường hợp (ức chế tổng hợp protein vs ức chế tổng hợp thành tế bào).'
        , 'effect': 'Giảm hiệu quả kháng khuẩn của penicillin (hiếm)',
        'management':
        'Tránh dùng đồng thời nếu có thể. Chọn một trong hai thuốc tùy theo chỉ định.'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng doxycycline hoặc tetracycline',
        'Có thai (3 tháng cuối) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (nguy cơ ố vàng răng, chậm phát triển xương ở trẻ)'
        ,
        'Trẻ em < 8 tuổi - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (trừ trường hợp đe dọa tính mạng như sốt rét, rickettsia) - nguy cơ ố vàng răng vĩnh viễn, chậm phát triển xương'
        ], 'tương_đối': [
        'Có thai (3 tháng đầu và giữa) - nguy cơ ố vàng răng, chậm phát triển xương ở trẻ, chỉ dùng khi thực sự cần thiết'
        , 'Suy gan nặng - tăng nguy cơ độc gan',
        'Tăng áp lực nội sọ giả - có thể làm nặng thêm',
        'Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu',
        'Bệnh nhân đang dùng digoxin - tăng nguy cơ độc tính digoxin',
        'Nhạy cảm với ánh sáng - tăng nguy cơ phản ứng quang hóa']},
        'pregnancy_lactation': {'fda_category': 'D', 'pregnancy_details':
        'Doxycycline là thuốc phân loại D. Các nghiên cứu trên động vật và người cho thấy nguy cơ ố vàng răng vĩnh viễn và chậm phát triển xương ở trẻ khi dùng trong thai kỳ, đặc biệt trong tam cá nguyệt thứ hai và thứ ba. Chống chỉ định trong tam cá nguyệt thứ hai và thứ ba. Tránh dùng trong tam cá nguyệt đầu tiên nếu có thể. Chỉ dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong các trường hợp đe dọa tính mạng như sốt rét, rickettsia.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Doxycycline bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, có thể gây ố vàng răng ở trẻ sơ sinh nếu dùng kéo dài.'
        , 'recommendation':
        'Có thể dùng khi cho con bú, nhưng thận trọng. Tránh dùng kéo dài. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Doxycycline chuyển hóa một phần qua gan, nhưng không tích lũy đáng kể ở suy gan nhẹ.'
        , 'moderate':
        'Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan và dấu hiệu độc gan.'
        , 'severe':
        'Giảm liều 25-50% hoặc tăng khoảng cách giữa các liều. Theo dõi chức năng gan chặt chẽ. Có thể cần tránh dùng nếu suy gan rất nặng.'
        , 'notes':
        'Doxycycline chuyển hóa một phần qua gan, nhưng thải trừ chủ yếu qua gan và thận. Không tích lũy đáng kể ở suy gan nhẹ, nhưng có thể tích lũy ở suy gan nặng. Cần điều chỉnh liều ở suy gan nặng. Khác với tetracycline cũ, doxycycline không tích lũy ở suy thận.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, viêm thực quản (đau khi nuốt, khó nuốt)'
        ,
        'Triệu chứng gan: Tăng men gan, viêm gan (đặc biệt ở liều cao, suy gan)',
        'Triệu chứng thần kinh: Tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị) - đặc biệt ở phụ nữ, có thể gây mù'
        ,
        'Triệu chứng da: Phản ứng quang hóa nặng (phát ban, bỏng da khi tiếp xúc với ánh sáng)'
        ,
        'Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)',
        'Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)'],
        'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': ['Ngừng ngay doxycycline',
        'Điều trị viêm thực quản nếu có:', '  - Uống nhiều nước',
        '  - Tránh nằm ngửa', '  - Điều trị giảm đau nếu cần',
        '  - Có thể cần nội soi nếu nghiêm trọng',
        'Điều trị tăng áp lực nội sọ giả nếu có:', '  - Ngừng ngay doxycycline',
        '  - Điều trị bằng acetazolamide hoặc mannitol nếu cần',
        '  - Theo dõi thị lực và dấu hiệu thần kinh',
        '  - Có thể cần chọc dò tủy sống để giảm áp lực',
        'Điều trị phản ứng quang hóa nếu có:', '  - Tránh ánh nắng trực tiếp',
        '  - Dùng kem chống nắng', '  - Điều trị phát ban/bỏng da',
        'Điều trị chảy máu nếu có:',
        '  - Bổ sung vitamin K nếu giảm prothrombin',
        '  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng',
        '  - Điều chỉnh liều warfarin nếu đang dùng',
        'Điều trị độc gan nếu có:', '  - Ngừng ngay doxycycline',
        '  - Điều trị hỗ trợ gan', '  - Theo dõi chức năng gan',
        'Điều trị dị ứng nếu có:', '  - Epinephrine nếu sốc phản vệ',
        '  - Antihistamine, corticosteroid', '  - Hỗ trợ hô hấp nếu cần',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2',
        'Lọc máu: Hemodialysis không hiệu quả do protein binding cao (80-90%)'],
        'monitoring':
        'Theo dõi dấu hiệu tiêu hóa (buồn nôn, nôn, viêm thực quản), dấu hiệu tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị), dấu hiệu phản ứng quang hóa (phát ban, bỏng da), chức năng gan (ALT, AST), PT/INR (nếu dùng với warfarin), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có tăng áp lực nội sọ giả hoặc độc gan.'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhưng giảm hấp thu một phần. Tránh uống với sữa hoặc thực phẩm giàu canxi (giảm hấp thu đáng kể).'
        , 'timing':
        'Uống 1-2 lần/ngày tùy chỉ định (respiratory: 2 lần/ngày, chlamydia: 2 lần/ngày, acne: 1-2 lần/ngày, malaria prophylaxis: 1 lần/ngày). Cách đều trong ngày. Uống với nhiều nước (ít nhất 200ml) và ở tư thế đứng để tránh viêm thực quản. KHÔNG uống nằm ngửa hoặc trước khi ngủ. Cách ít nhất 2 giờ với antacid, sắt, canxi, magie, kẽm, sữa.'
        }, 'iv': {'reconstitution':
        'Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 0.1-1mg/ml. Pha 100mg trong 100ml = 1mg/ml. Pha 200mg trong 200ml = 1mg/ml. Lắc kỹ để hòa tan hoàn toàn. Bảo quản tránh ánh sáng.'
        , 'infusion_rate':
        'Truyền IV trong 1-4 giờ. Tốc độ: 100ml/1 giờ = ~1.7ml/phút, 200ml/4 giờ = ~0.83ml/phút. KHÔNG truyền nhanh (bolus) - tăng nguy cơ tác dụng phụ.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],
        'incompatibility': ["Ringer's Lactate - có thể tạo kết tủa với canxi",
        'Các dung dịch chứa canxi, magie, sắt - tạo kết tủa',
        'Các thuốc có tính kiềm hoặc acid mạnh'], 'notes':
        'QUAN TRỌNG: 1) Uống với nhiều nước và ở tư thế đứng để tránh viêm thực quản, 2) Tránh ánh nắng trực tiếp, dùng kem chống nắng, 3) Cách ít nhất 2 giờ với antacid, sắt, canxi, magie, kẽm, sữa, 4) KHÔNG dùng cho trẻ em < 8 tuổi (trừ trường hợp đe dọa tính mạng), 5) KHÔNG dùng trong 3 tháng cuối thai kỳ, 6) Theo dõi dấu hiệu tăng áp lực nội sọ giả.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Doxycycline (Vibramycin)',
        'UpToDate - Doxycycline: Drug Information',
        'Medscape - Doxycycline Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Doxycycline Monograph',
        'Micromedex - Doxycycline Drug Information',
        'IDSA Guidelines - Community-Acquired Pneumonia, Tick-Borne Infections'
        ], 'last_updated': '2025-02-03', 'evidence_level':
        'A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }}}

__all__ = ['TETRACYCLINES_DRUGS']
