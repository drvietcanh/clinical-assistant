"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Beta-lactams

BETA_LACTAMS_DRUGS = {
    "Amoxicillin-clavulanate": {'group':
        'Antibiotic - Beta-lactam (Penicillin + Beta-lactamase inhibitor)',
        'vietnamese_name': 'Amoxicillin-clavulanate, Augmentin, Amoclav',
        'administration': ['PO', 'IV'], 'indications': [
        'Nhiễm khuẩn đường hô hấp trên/dưới', 'Nhiễm khuẩn đường tiết niệu',
        'Nhiễm khuẩn da mô mềm', 'Nhiễm khuẩn răng miệng',
        'Nhiễm khuẩn tai mũi họng (trẻ em)'], 'contraindications': [
        'Dị ứng penicillin', 'Viêm gan do amoxicillin-clavulanate trước đây',
        'Dị ứng beta-lactam'], 'dosage': {'adult_po':
        '875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày',
        'pediatric_po_suspension':
        '20-40mg amoxicillin/kg/ngày chia 2-3 lần (tối đa 875mg/125mg)',
        'pediatric_po_tablet':
        '25-45mg amoxicillin/kg/ngày chia 2 lần (trên 40kg: dùng liều người lớn)',
        'adult_iv': '1000/200mg IV mỗi 8 giờ', 'pediatric_iv':
        '90mg amoxicillin/kg/ngày chia 3 lần (tối đa 1000/200mg mỗi 8 giờ)',
        'notes':
        'Có dạng suspension cho trẻ em. Uống với thức ăn để giảm tiêu chảy'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Giảm liều hoặc tăng khoảng cách', 'under_30':
        'Liều thấp hơn, khoảng cách dài hơn'}, 'side_effects': [
        'Tiêu chảy (phổ biến)', 'Buồn nôn', 'Phát ban',
        'Viêm gan (hiếm nhưng nguy hiểm)', 'Nhiễm trùng nấm Candida'],
        'interactions': ['Warfarin: tăng INR',
        'Methotrexate: tăng độc tính methotrexate',
        'Allopurinol: tăng nguy cơ phát ban',
        'Thuốc tránh thai: có thể giảm hiệu quả'], 'pregnancy': 'B - An toàn',
        'mechanism_of_action':
        'Amoxicillin: aminopenicillin phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Clavulanate: beta-lactamase inhibitor, bảo vệ amoxicillin khỏi bị phân hủy bởi beta-lactamase. Kết hợp này mở rộng phổ kháng khuẩn, đặc biệt hiệu quả với H. influenzae, E. coli, và một số kỵ khí. Clavulanate không có hoạt tính kháng khuẩn riêng. Được dùng rộng rãi trong nhiễm trùng đường hô hấp, tiết niệu, da và mô mềm.'
        , 'monitoring': ['Dấu hiệu nhiễm trùng (sốt, WBC)',
        'Cấy máu và cấy từ vị trí nhiễm trùng',
        'Chức năng gan (ALT, AST) - tăng men gan (thường nhất thời), hiếm viêm gan (đặc biệt với clavulanate)'
        , 'Dấu hiệu nhiễm C. difficile',
        'Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV)',
        'Chức năng thận (creatinine) - hiếm viêm thận kẽ'], 'precautions': [
        'Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)',
        'Nguy cơ viêm gan (đặc biệt do clavulanate) - thường nhất thời, hiếm nặng, tăng ở nam giới, dùng kéo dài'
        , 'Theo dõi men gan, ngừng nếu tăng nặng',
        'Phát ban thường gặp, đặc biệt ở bệnh nhân nhiễm virus (EBV, CMV) - không phải dị ứng thật'
        , 'Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy',
        'Uống với thức ăn để giảm kích ứng dạ dày và tăng hấp thu',
        'Dùng đúng liều và đủ thời gian để tránh kháng thuốc',
        'Không dùng cho nhiễm trùng do Pseudomonas hoặc Enterococcus kháng'],
        'pharmacokinetics': {'half_life': '1 giờ (amoxicillin và clavulanate)',
        'onset': '1-2 giờ (PO)', 'duration': 'q8h hoặc q12h tùy công thức',
        'protein_binding': '17-20% (amoxicillin), 22-30% (clavulanate)',
        'metabolism': 'Một phần trong gan', 'clearance':
        'Chủ yếu qua thận, cần điều chỉnh thận ở suy thận nặng'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Sau khi pha (suspension): bảo quản trong tủ lạnh 10 ngày, sau đó vứt bỏ.'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, nguy cơ viêm gan (đặc biệt do clavulanate) có thể nặng, đặc biệt ở nam giới và dùng kéo dài. Phát ban thường gặp và có thể nhầm với dị ứng.'
        , 'drug_interactions': {'major': [{'drug': 'Warfarin', 'mechanism':
        'Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin.'
        , 'effect': 'Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu',
        'management':
        'Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng amoxicillin-clavulanate. Điều chỉnh liều warfarin nếu cần.'
        }, {'drug': 'Methotrexate', 'mechanism':
        'Amoxicillin-clavulanate ức chế bài tiết methotrexate ở ống thận, làm giảm thải trừ methotrexate.'
        , 'effect':
        'Tăng nồng độ methotrexate, tăng độc tính (giảm bạch cầu, thiếu máu, độc gan, độc thận)'
        , 'management':
        'TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate, theo dõi chặt chẽ công thức máu, chức năng gan, thận. Ngừng methotrexate nếu có dấu hiệu độc tính.'
        }], 'moderate': [{'drug': 'Allopurinol', 'mechanism':
        'Cơ chế chưa rõ ràng, có thể liên quan đến phản ứng miễn dịch.',
        'effect':
        'Tăng nguy cơ phát ban, phản ứng dị ứng (đặc biệt phát ban maculopapular)',
        'management':
        'Thận trọng khi dùng đồng thời. Theo dõi dấu hiệu phát ban. Ngừng ngay nếu có phát ban nặng hoặc phản ứng dị ứng.'
        }, {'drug': 'Thuốc tránh thai nội tiết', 'mechanism':
        'Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen, giảm nồng độ estrogen.'
        , 'effect':
        'Có thể giảm hiệu quả thuốc tránh thai, tăng nguy cơ mang thai',
        'management':
        'Khuyến nghị sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng amoxicillin-clavulanate và 7 ngày sau khi ngừng thuốc.'
        }, {'drug': 'Probenecid', 'mechanism':
        'Probenecid ức chế bài tiết amoxicillin ở ống thận, làm tăng nồng độ amoxicillin.'
        , 'effect': 'Tăng nồng độ amoxicillin, tăng tác dụng phụ', 'management':
        'Có thể dùng để tăng nồng độ amoxicillin nếu cần. Theo dõi tác dụng phụ. Giảm liều amoxicillin nếu cần.'
        }], 'minor': [{'drug': 'Antacids', 'mechanism':
        'Antacids có thể giảm nhẹ hấp thu amoxicillin.', 'effect':
        'Giảm nhẹ hấp thu amoxicillin', 'management':
        'Cách 2 giờ nếu có thể. Không ảnh hưởng đáng kể ở liều điều trị thông thường.'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng amoxicillin, clavulanate, hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam'
        ,
        'Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao'
        ,
        'Viêm gan do amoxicillin-clavulanate trước đây - nguy cơ tái phát cao, có thể nặng hơn'
        ], 'tương_đối': [
        'Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng',
        'Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách',
        'Suy gan - thận trọng, có thể giảm chuyển hóa',
        'Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)',
        'Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát',
        'Dùng với methotrexate - tăng độc tính methotrexate',
        'Dùng với allopurinol - tăng nguy cơ phát ban']}, 'pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'Amoxicillin-clavulanate phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Amoxicillin và clavulanate bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Penicillin là một trong những kháng sinh an toàn nhất khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban).'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Amoxicillin và clavulanate chuyển hóa một phần qua gan nhưng không đáng kể.'
        , 'moderate':
        'Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.'
        , 'severe':
        'Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận.'
        , 'notes':
        'Amoxicillin và clavulanate chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua thận (60-70% bài tiết nguyên dạng qua nước tiểu). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, nguy cơ viêm gan do clavulanate tăng ở bệnh nhân có bệnh gan, đặc biệt nam giới và dùng kéo dài. Theo dõi chặt chẽ chức năng gan.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng',
        'Triệu chứng thần kinh: Kích động, co giật (hiếm, thường ở liều rất cao)',
        'Triệu chứng thận: Tăng creatinine, suy thận cấp (hiếm)',
        'Triệu chứng da: Phát ban, mày đay',
        'Triệu chứng gan: Tăng men gan, viêm gan (đặc biệt với clavulanate)',
        'Triệu chứng nghiêm trọng: Co giật, suy thận cấp, viêm gan nặng'],
        'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': ['Ngừng ngay amoxicillin-clavulanate',
        'Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)'
        , 'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2',
        'Điều trị triệu chứng tiêu hóa:', '  - Chống nôn nếu cần',
        '  - Truyền dịch nếu mất nước', '  - Theo dõi điện giải',
        'Điều trị co giật nếu có:', '  - Benzodiazepine (diazepam, lorazepam)',
        '  - Theo dõi hô hấp', 'Điều trị tăng men gan/viêm gan nếu có:',
        '  - Theo dõi ALT, AST, bilirubin', '  - Điều trị hỗ trợ gan',
        '  - Nếu viêm gan nặng: điều trị suy gan',
        'Điều trị suy thận cấp nếu có:',
        '  - Theo dõi creatinine, BUN, lượng nước tiểu',
        '  - Điều trị suy thận cấp',
        'Lọc máu (hemodialysis) có thể loại bỏ một phần amoxicillin nhưng không được khuyến nghị thường quy'
        , 'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2'],
        'monitoring':
        'Theo dõi dấu hiệu sinh tồn, chức năng gan (ALT, AST, bilirubin), chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu da trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (suy gan, suy thận, co giật).'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Uống với thức ăn để giảm kích ứng dạ dày, giảm tiêu chảy, và tăng hấp thu. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.'
        , 'timing':
        'Uống 2-3 lần/ngày tùy công thức (875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày). Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều.'
        }, 'iv': {'reconstitution':
        'Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.'
        , 'infusion_rate':
        'Truyền IV trong 30 phút (không truyền nhanh hơn). Có thể truyền trong 15-20 phút nếu cần nhưng không khuyến nghị.'
        , 'compatibility': ['NaCl 0.9%', 'D5W (Dextrose 5%)',
        "Lactated Ringer's (LR) - thận trọng, kiểm tra tương thích",
        'Nước cất vô trùng'], 'incompatibility': [
        'Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền',
        'Aminoglycosides (mất hoạt tính nếu trộn trực tiếp)',
        'Probenecid (không trộn, dùng riêng)'], 'notes':
        'Truyền IV trong 30 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha.'
        }}, 'references': {'primary_sources': [
        'FDA Label: Augmentin (amoxicillin-clavulanate)',
        'UpToDate: Amoxicillin-clavulanate drug information',
        'Lexicomp: Amoxicillin-clavulanate monograph',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Sanford Guide to Antimicrobial Therapy'], 'last_updated': '2025-02-03',
        'evidence_level':
        'Level 1 - FDA approved, multiple clinical trials, extensive clinical experience'
        }},
    "Amoxicillin suspension": {'group': 'Antibiotic - Beta-lactam (Penicillin)', 'vietnamese_name':
        'Amoxicillin suspension, Amoxicillin sirô', 'administration': ['PO'],
        'indications': ['Nhiễm khuẩn đường hô hấp', 'Nhiễm khuẩn tai mũi họng',
        'Nhiễm khuẩn đường tiết niệu', 'Nhiễm khuẩn da mô mềm',
        'Helicobacter pylori (phối hợp)'], 'contraindications': [
        'Dị ứng penicillin', 'Dị ứng beta-lactam'], 'dosage': {
        'pediatric_otitis': '80-90mg/kg/ngày chia 2 lần (10 ngày)',
        'pediatric_pneumonia': '80-100mg/kg/ngày chia 3-4 lần', 'pediatric_uti':
        '25-50mg/kg/ngày chia 3 lần', 'pediatric_suspension_common':
        '20-40mg/kg/ngày chia 2-3 lần', 'notes':
        'Có dạng suspension 125mg/5ml, 250mg/5ml cho trẻ em. Uống với hoặc không thức ăn'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Giảm liều hoặc tăng khoảng cách', 'under_30':
        'Liều thấp hơn, khoảng cách dài hơn'}, 'side_effects': ['Tiêu chảy',
        'Buồn nôn', 'Phát ban', 'Nhiễm trùng nấm Candida',
        'Giảm bạch cầu (hiếm)'], 'interactions': ['Warfarin: tăng INR',
        'Methotrexate: tăng độc tính', 'Allopurinol: tăng nguy cơ phát ban',
        'Thuốc tránh thai: có thể giảm hiệu quả'], 'pregnancy': 'B - An toàn',
        'mechanism_of_action':
        'Amoxicillin là aminopenicillin (beta-lactam antibiotic), ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs) trên màng tế bào vi khuẩn. Amoxicillin là chất tương tự penicillin nhưng có nhóm amin, giúp tăng khả năng xuyên qua màng ngoài của vi khuẩn Gram-âm và tăng phổ kháng khuẩn. Amoxicillin ức chế enzyme transpeptidase, ngăn chặn liên kết chéo giữa các chuỗi peptidoglycan trong thành tế bào vi khuẩn, dẫn đến làm suy yếu và vỡ thành tế bào khi vi khuẩn phân chia. Amoxicillin có phổ kháng khuẩn rộng: Gram-dương (Streptococcus, Enterococcus, một số Staphylococcus không kháng penicillinase), Gram-âm (H. influenzae, E. coli, Proteus mirabilis, Salmonella, Shigella), và một số kỵ khí. Không hiệu quả với vi khuẩn tiết beta-lactamase (cần kết hợp với clavulanate). Dạng suspension phù hợp cho trẻ em, dễ uống và hấp thu tốt.'
        , 'monitoring': [
        'Dấu hiệu nhiễm trùng: sốt, WBC, CRP (theo dõi đáp ứng điều trị)',
        'Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để đánh giá hiệu quả',
        'Dấu hiệu dị ứng: phát ban, mề đay, khó thở, sốc phản vệ (đặc biệt ở lần đầu tiên dùng)'
        , 'Tiêu chảy (phổ biến, có thể là nhiễm C. difficile nếu nặng)',
        'Chức năng thận (creatinine) nếu dùng liều cao hoặc suy thận',
        'Dấu hiệu nhiễm C. difficile: tiêu chảy nặng, đau bụng, sốt (cần ngừng và điều trị)'
        , 'Chức năng gan (ALT, AST) nếu có triệu chứng (hiếm)',
        'Công thức máu (giảm bạch cầu, thiếu máu hiếm)',
        'INR nếu dùng với warfarin (tăng nguy cơ chảy máu)'], 'precautions': [
        'Không dùng ở bệnh nhân dị ứng penicillin hoặc beta-lactam (phản ứng chéo với cephalosporin ~5-10%)'
        , 'Lắc kỹ suspension trước khi dùng (thuốc lắng xuống đáy)',
        'Có thể uống với hoặc không thức ăn (hấp thu tốt)',
        'Dùng đủ liều và đủ thời gian (thường 7-10 ngày) để tránh kháng thuốc',
        'Thận trọng ở bệnh nhân suy thận (giảm liều hoặc tăng khoảng cách)',
        'Thận trọng ở bệnh nhân có tiền sử nhiễm C. difficile (tăng nguy cơ tái phát)'
        , 'Thận trọng với allopurinol (tăng nguy cơ phát ban)',
        'Thận trọng với methotrexate (amoxicillin làm giảm thải trừ methotrexate, tăng độc tính)'
        , 'Có thể giảm hiệu quả thuốc tránh thai (dùng biện pháp dự phòng)',
        'Theo dõi tiêu chảy - nếu nặng hoặc kéo dài, có thể là nhiễm C. difficile',
        'Dùng đúng liều theo cân nặng ở trẻ em (tính theo mg/kg)'],
        'pharmacokinetics': {'half_life': '1-1.5 giờ', 'onset':
        '1-2 giờ (đạt nồng độ đỉnh trong máu)', 'duration':
        '6-8 giờ (dùng 2-3 lần/ngày)', 'protein_binding': '20%', 'clearance':
        'Thận: bài tiết chủ yếu qua nước tiểu (không thay đổi, 60-70% trong 6-8 giờ). Một phần nhỏ qua mật. Hấp thu tốt qua đường uống (75-90%), không bị ảnh hưởng bởi thức ăn. Dạng suspension hấp thu tương tự viên nén.'
        }, 'storage':
        'Bảo quản suspension ở nhiệt độ phòng (15-30°C) hoặc trong tủ lạnh (2-8°C) - theo hướng dẫn trên nhãn. Lắc kỹ trước khi dùng. Sau khi pha (nếu là bột pha nước): bảo quản trong tủ lạnh (2-8°C), dùng trong vòng 7-14 ngày (theo hướng dẫn). Tránh đông lạnh. Để nơi khô ráo, tránh ánh sáng trực tiếp, tránh xa tầm tay trẻ em.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Methotrexate', 'mechanism':
        'Amoxicillin làm giảm thải trừ methotrexate qua thận, tăng nồng độ methotrexate.'
        , 'effect':
        'Tăng độc tính methotrexate (giảm bạch cầu, độc gan, độc thận, viêm niêm mạc)'
        , 'management':
        'Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi công thức máu, chức năng gan, thận chặt chẽ. Có thể cần giảm liều methotrexate.'
        }, {'drug': 'Allopurinol', 'mechanism':
        'Cơ chế chưa rõ ràng, nhưng allopurinol làm tăng nguy cơ phản ứng da nghiêm trọng với amoxicillin.'
        , 'effect':
        'Tăng nguy cơ phát ban nghiêm trọng, SJS, TEN (đe dọa tính mạng)',
        'management':
        'Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi sát dấu hiệu phát ban. Ngừng ngay nếu có phát ban.'
        }], 'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Amoxicillin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, ảnh hưởng đến chuyển hóa vitamin K, tăng tác dụng warfarin.'
        , 'effect': 'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên khi dùng amoxicillin. Điều chỉnh liều warfarin nếu cần.'
        }, {'drug': 'Thuốc tránh thai (estrogen)', 'mechanism':
        'Amoxicillin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, giảm tái hấp thu estrogen, giảm hiệu quả thuốc tránh thai.'
        , 'effect': 'Giảm hiệu quả thuốc tránh thai, tăng nguy cơ có thai',
        'management':
        'Dùng biện pháp tránh thai dự phòng (bao cao su) trong thời gian dùng amoxicillin và 7 ngày sau.'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng penicillin - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (phản ứng chéo với cephalosporin ~5-10%)'
        , 'Dị ứng beta-lactam', 'Sốc phản vệ với penicillin trước đây'],
        'tương_đối': [
        'Dị ứng cephalosporin - thận trọng (phản ứng chéo ~5-10%)',
        'Nhiễm C. difficile trước đây - tăng nguy cơ tái phát',
        'Suy thận nặng - giảm liều hoặc tăng khoảng cách',
        'Đang dùng methotrexate - tăng độc tính methotrexate',
        'Đang dùng allopurinol - tăng nguy cơ phát ban']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Amoxicillin là category B - an toàn trong thai kỳ. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Không có bằng chứng về dị tật thai nhi. Có thể dùng trong tất cả các tam cá nguyệt.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Amoxicillin bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Có thể gây tiêu chảy nhẹ hoặc phát ban ở trẻ, nhưng hiếm.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. An toàn cho trẻ bú mẹ. Theo dõi dấu hiệu tiêu chảy hoặc phát ban ở trẻ.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận, không chuyển hóa ở gan.'
        , 'moderate':
        'Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận.',
        'severe':
        'Không cần điều chỉnh liều. Amoxicillin chủ yếu thải qua thận.',
        'notes':
        'Amoxicillin chủ yếu thải qua thận (60-70% trong 6-8 giờ), không chuyển hóa ở gan. Suy gan không ảnh hưởng đến nồng độ amoxicillin.'
        }, 'overdose_management': {'symptoms': [
        'Tiêu chảy nặng (có thể là nhiễm C. difficile)', 'Buồn nôn, nôn',
        'Phát ban, mề đay', 'Sốc phản vệ (hiếm nhưng nguy hiểm)',
        'Co giật (với liều rất cao, suy thận)',
        'Rối loạn điện giải (natri cao nếu dùng liều lớn)'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng amoxicillin ngay lập tức',
        'Nếu sốc phản vệ: epinephrine, corticosteroids, antihistamines, hỗ trợ hô hấp'
        ,
        'Nếu tiêu chảy nặng: điều trị C. difficile nếu xác định (metronidazole, vancomycin)'
        , 'Nếu co giật: benzodiazepines (diazepam, lorazepam)',
        'Điều chỉnh điện giải nếu cần', 'Hỗ trợ hô hấp và tuần hoàn nếu cần',
        'Theo dõi dấu hiệu sinh tồn'], 'monitoring':
        'Dấu hiệu sinh tồn, dấu hiệu dị ứng, tiêu chảy, điện giải, dấu hiệu nhiễm C. difficile'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Hấp thu tốt, không bị ảnh hưởng bởi thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.'
        , 'timing':
        'Uống 2-3 lần/ngày tùy chỉ định, cách đều. Lắc kỹ suspension trước khi dùng (thuốc lắng xuống đáy). Dùng đúng liều theo cân nặng ở trẻ em (tính theo mg/kg).'
        }, 'iv': {'reconstitution': 'N/A - chỉ có dạng uống', 'infusion_rate':
        'N/A', 'compatibility': [], 'incompatibility': [], 'notes':
        'Chỉ có dạng uống (suspension)'}}, 'references': {'primary_sources': [
        'FDA Drug Label - Amoxicillin',
        'UpToDate - Amoxicillin: Drug Information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ], 'last_updated': '2025-02-04', 'evidence_level':
        'A - Dựa trên FDA drug labels và dữ liệu lâm sàng'}}}

__all__ = ['BETA_LACTAMS_DRUGS']
