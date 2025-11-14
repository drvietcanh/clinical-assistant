"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Proton Pump Inhibitor (PPI)s

PROTON_PUMP_INHIBITOR_(PPI)S_DRUGS = {
    "Omeprazole": {'group': 'Gastrointestinal - Proton Pump Inhibitor (PPI)',
        'vietnamese_name': 'Omeprazole, Losec', 'administration': ['PO', 'IV'],
        'indications': ['Loét dạ dày tá tràng',
        'Trào ngược dạ dày thực quản (GERD)', 'Hội chứng Zollinger-Ellison',
        'Phòng ngừa loét do stress',
        'Eradication H. pylori (kết hợp với kháng sinh)'], 'contraindications':
        ['Dị ứng', 'Dùng cùng atazanavir'], 'dosage': {'adult_po':
        '20-40mg x 1-2 lần/ngày', 'adult_iv': '40mg x 1-2 lần/ngày', 'h_pylori':
        '20mg x 2 lần/ngày (với amoxicillin + clarithromycin)', 'notes':
        'Uống 30 phút trước bữa ăn, không nhai/cắn viên'}, 'side_effects': [
        'Nhức đầu', 'Tiêu chảy', 'Đau bụng', 'Tăng nguy cơ nhiễm C. difficile',
        'Gãy xương (dùng lâu dài, liều cao)',
        'Thiếu vitamin B12 (dùng lâu dài)', 'Thiếu magnesium (dùng lâu dài)'],
        'interactions': ['Clopidogrel: giảm hiệu quả clopidogrel',
        'Warfarin: có thể tăng tác dụng', 'Phenytoin: tăng nồng độ phenytoin',
        'Methotrexate: tăng nồng độ methotrexate'], 'pregnancy': 'C',
        'mechanism_of_action':
        'Ức chế không hồi phục H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày'
        , 'monitoring': ['Triệu chứng cải thiện (đau dạ dày, ợ chua)',
        'Vitamin B12 mỗi 1-2 năm nếu dùng lâu dài',
        'Magnesium nếu có triệu chứng (chuột rút, yếu cơ) hoặc dùng lâu dài',
        'Mật độ xương nếu dùng lâu dài, liều cao (phụ nữ >50 tuổi)',
        'Theo dõi nhiễm C. difficile nếu có tiêu chảy'], 'precautions': [
        'Uống 30 phút trước bữa ăn (để tối đa hóa hiệu quả)',
        'Không nhai/cắn viên bao tan trong ruột',
        'Dùng liều thấp nhất có hiệu quả, thời gian ngắn nhất',
        'Cân nhắc giảm liều hoặc ngừng sau 4-8 tuần nếu có thể',
        'Bổ sung vitamin B12 nếu dùng lâu dài', 'Bổ sung magnesium nếu thiếu'],
        'pharmacokinetics': {'half_life':
        '0.5-1 giờ (ngắn), nhưng tác dụng kéo dài do ức chế không hồi phục',
        'onset': '1-3 giờ', 'duration': '24 giờ (một liều)', 'protein_binding':
        '95%', 'clearance': 'Gan (CYP2C19, CYP3A4)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Giảm hiệu quả clopidogrel khi dùng đồng thời. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài'
        , 'drug_interactions': {'major': [{'drug': 'Clopidogrel', 'mechanism':
        'Omeprazole ức chế CYP2C19, enzyme cần thiết để chuyển hóa clopidogrel thành dạng hoạt động'
        , 'effect':
        'Giảm hiệu quả chống kết tập tiểu cầu của clopidogrel, tăng nguy cơ biến cố tim mạch'
        , 'management':
        'Tránh dùng cùng. Chuyển sang pantoprazole (ít ảnh hưởng hơn) hoặc PPI khác không ức chế CYP2C19. Nếu phải dùng, cân nhắc dùng cách thời gian (omeprazole trước clopidogrel 12 giờ).'
        }, {'drug': 'Atazanavir (HIV protease inhibitor)', 'mechanism':
        'PPI làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)',
        'effect':
        'Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV, tăng nguy cơ kháng thuốc'
        , 'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng omeprazole với atazanavir. Dùng H2 blocker hoặc PPI khác cách thời gian (12 giờ).'
        }], 'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Omeprazole ức chế CYP2C9 nhẹ, có thể tăng nồng độ warfarin', 'effect':
        'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}, {
        'drug': 'Phenytoin', 'mechanism':
        'Omeprazole ức chế CYP2C19, giảm chuyển hóa phenytoin', 'effect':
        'Tăng nồng độ phenytoin, tăng nguy cơ độc tính (chóng mặt, nystagmus, ataxia)'
        , 'management':
        'Theo dõi nồng độ phenytoin. Giảm liều phenytoin nếu cần.'}, {'drug':
        'Methotrexate (liều cao)', 'mechanism':
        'PPI giảm thải trừ methotrexate qua thận (cạnh tranh với organic anion transporters)'
        , 'effect':
        'Tăng nồng độ methotrexate, tăng nguy cơ độc tính (myelosuppression, mucositis, nephrotoxicity)'
        , 'management':
        'Thận trọng. Tạm ngừng PPI khi dùng methotrexate liều cao. Theo dõi chức năng thận, công thức máu.'
        }, {'drug': 'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)',
        'effect': 'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole (ít ảnh hưởng pH hơn).'
        }, {'drug': 'Iron salts (ferrous sulfate, ferrous fumarate)',
        'mechanism':
        'PPI giảm acid dạ dày, giảm chuyển Fe3+ thành Fe2+ (dạng hấp thu được)',
        'effect': 'Giảm hấp thu sắt, có thể gây thiếu máu thiếu sắt',
        'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng sắt dạng chelate (iron bisglycinate) ít phụ thuộc acid.'
        }, {'drug': 'Vitamin B12 (cobalamin)', 'mechanism':
        'PPI giảm acid dạ dày, giảm tách B12 khỏi protein thức ăn', 'effect':
        'Giảm hấp thu B12, có thể gây thiếu máu thiếu B12 sau 2-3 năm dùng PPI',
        'management':
        'Bổ sung B12 định kỳ nếu dùng PPI lâu dài (>2 năm). Theo dõi B12 máu mỗi 1-2 năm.'
        }], 'minor': [{'drug': 'Diazepam', 'mechanism': 'Ức chế CYP2C19 nhẹ',
        'effect': 'Tăng nồng độ diazepam nhẹ', 'management':
        'Thận trọng, không cần điều chỉnh liều thường quy'}, {'drug':
        'Citalopram, Escitalopram', 'mechanism': 'Ức chế CYP2C19', 'effect':
        'Tăng nồng độ SSRI nhẹ', 'management':
        'Thận trọng, theo dõi tác dụng phụ SSRI'}]}, 'contraindications': {
        'tuyệt_đối': ['Dị ứng omeprazole hoặc PPI khác',
        'Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối do giảm hấp thu atazanavir'
        ], 'tương_đối': [
        'Suy gan nặng (Child-Pugh C) - giảm liều tối đa 20mg/ngày',
        'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng',
        'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài',
        'Nhiễm C. difficile - tăng nguy cơ',
        'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài',
        'Thiếu magnesium - bổ sung nếu dùng lâu dài']}, 'pregnancy_lactation':
        {'fda_category': 'C', 'pregnancy_details':
        'Omeprazole là FDA category C. Nghiên cứu trên động vật cho thấy có thể gây độc tính cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Một số nghiên cứu quan sát lớn không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, đặc biệt trong GERD nặng hoặc loét dạ dày. Dùng liều thấp nhất có hiệu quả.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Omeprazole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ rất thấp (<0.01% liều mẹ). Không có báo cáo tác dụng phụ ở trẻ bú mẹ. An toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng (20-40mg/ngày). Theo dõi trẻ nếu có lo ngại.'
        }}, 'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều, nhưng thận trọng', 'severe':
        'Giảm liều tối đa 20mg/ngày (Child-Pugh C). Omeprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4. Suy gan nặng làm giảm clearance, tăng nồng độ thuốc.'
        , 'notes':
        'Omeprazole chuyển hóa ở gan. Suy gan nặng làm giảm chuyển hóa, tăng nồng độ. Tuy nhiên, PPI thường được dung nạp tốt ngay cả ở suy gan. Giảm liều ở suy gan nặng (Child-Pugh C).'
        }, 'overdose_management': {'symptoms': [
        'PPI ít gây quá liều nghiêm trọng do an toàn tốt',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy, chóng mặt',
        'Liều rất cao có thể gây: buồn ngủ, lú lẫn'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': ['Hỗ trợ triệu chứng nếu có',
        'Theo dõi dấu hiệu sinh tồn',
        'Nếu uống trong vòng 1-2 giờ: có thể cân nhắc activated charcoal (hiệu quả thấp)'
        , 'Hầu hết trường hợp tự khỏi, không cần điều trị đặc hiệu'],
        'monitoring': 'Theo dõi dấu hiệu sinh tồn, triệu chứng thần kinh nhẹ'},
        'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Uống 30 phút TRƯỚC bữa ăn (quan trọng - để PPI hoạt động khi proton pump được kích hoạt bởi thức ăn)'
        , 'timing':
        'Uống vào buổi sáng trước bữa sáng (hoặc 30 phút trước bữa tối nếu dùng 2 lần/ngày). KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated) - phải nuốt nguyên viên. Nếu khó nuốt, có thể mở viên và rắc vào thức ăn mềm (táo, sữa chua) nhưng phải nuốt ngay, không nhai.'
        }, 'iv': {'reconstitution':
        'Omeprazole IV: 40mg pha với 100ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate': 'Truyền trong 20-30 phút', 'compatibility': [
        'NaCl 0.9%', 'Dextrose 5%'], 'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể. Bảo quản dung dịch đã pha ở nhiệt độ phòng, dùng trong 12 giờ.'
        }}, 'references': {'primary_sources': ['FDA Drug Label - Omeprazole',
        'UpToDate - Proton pump inhibitors: Overview of use and adverse effects',
        'Micromedex - Omeprazole',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Lancet - Proton pump inhibitors and risk of fractures (2006)',
        'JAMA - Clopidogrel-omeprazole interaction (2010)'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs, systematic reviews'}},
    "Lansoprazole": {'group': 'Gastrointestinal - Proton Pump Inhibitor (PPI)',
        'vietnamese_name': 'Lansoprazole, Prevacid', 'administration': ['PO'],
        'indications': ['Loét dạ dày tá tràng',
        'Trào ngược dạ dày thực quản (GERD)', 'Hội chứng Zollinger-Ellison',
        'Tiệt trừ H. pylori (kết hợp)'], 'contraindications': [
        'Dị ứng lansoprazole/PPI'], 'dosage': {'adult_ulcer':
        '15-30mg x 1 lần/ngày', 'adult_gerd': '15-30mg x 1 lần/ngày',
        'adult_h_pylori':
        '30mg x 2 lần/ngày (với amoxicillin + clarithromycin)', 'notes':
        'Uống trước bữa ăn 30 phút. Viên tan trong miệng không cần nước'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Đau đầu', 'Tiêu chảy',
        'Đau bụng', 'Tăng nguy cơ nhiễm trùng (Clostridium difficile)',
        'Loãng xương (dùng lâu dài)', 'Thiếu vitamin B12 (dùng lâu dài)',
        'Thiếu magie (hiếm)'], 'interactions': [
        'Warfarin: tăng nhẹ nguy cơ chảy máu',
        'Digoxin: tăng nhẹ nồng độ digoxin',
        'Ketoconazole/Itraconazole: giảm hấp thu (giảm acid dạ dày)',
        'Methotrexate: tăng nồng độ methotrexate'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Ức chế không hồi phục enzyme H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, ức chế bước cuối cùng trong quá trình tiết acid dạ dày. Ức chế cả acid kích thích và acid cơ bản. Cần chuyển hóa ở gan thành dạng hoạt động (sulfenamide). Tác dụng mạnh hơn H2 blocker. Thời gian bán thải ngắn nhưng tác dụng kéo dài do ức chế không hồi phục enzyme.'
        , 'monitoring': ['Đáp ứng lâm sàng (giảm đau, triệu chứng GERD)',
        'Magie máu nếu dùng lâu dài (>1 năm) - có thể giảm magie',
        'Vitamin B12 nếu dùng lâu dài (>2 năm) - có thể thiếu B12',
        'Mật độ xương (DEXA scan) nếu dùng lâu dài và có nguy cơ loãng xương',
        'Dấu hiệu nhiễm C. difficile (tiêu chảy nặng, đau bụng) - tăng nguy cơ',
        'Chức năng thận (nếu dùng lâu dài với nguy cơ suy thận)'],
        'precautions': ['Uống trước bữa ăn 30 phút (tăng hiệu quả)',
        'Viên tan trong miệng: đặt trên lưỡi, để tan tự nhiên, không cần nước',
        'Không nghiền hoặc nhai viên (bao tan trong ruột)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Cân nhắc ngừng sau 4-8 tuần nếu không cần thiết (giảm nguy cơ tác dụng phụ)'
        , 'Cân nhắc dùng liều cách ngày hoặc ngắt quãng nếu dùng lâu dài',
        'Thận trọng ở bệnh nhân suy gan nặng (giảm liều)',
        'Không dùng với các thuốc cần acid để hấp thu (ketoconazole, itraconazole, iron salts)'
        ], 'pharmacokinetics': {'half_life':
        '1-2 giờ (ngắn, nhưng tác dụng kéo dài do ức chế không hồi phục)',
        'onset': '1-3 giờ', 'duration': '24 giờ (một lần/ngày)',
        'protein_binding': '97%', 'clearance':
        'Gan (chuyển hóa qua CYP2C19, CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên tan trong miệng: bảo quản trong bao bì gốc, tránh ẩm.'
        , 'black_box_warnings':
        'Dùng lâu dài (>1 năm) có thể tăng nguy cơ loãng xương, gãy xương hông, cổ tay, cột sống. Dùng lâu dài có thể tăng nguy cơ thiếu vitamin B12. Tăng nguy cơ nhiễm C. difficile.'
        , 'drug_interactions': {'major': [{'drug':
        'Atazanavir (HIV protease inhibitor)', 'mechanism':
        'PPI làm tăng pH dạ dày, giảm hấp thu atazanavir', 'effect':
        'Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV', 'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng lansoprazole với atazanavir.'}],
        'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Lansoprazole ức chế CYP2C9 nhẹ', 'effect':
        'Tăng INR nhẹ, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}, {
        'drug': 'Digoxin', 'mechanism':
        'Lansoprazole có thể tăng nồng độ digoxin nhẹ', 'effect':
        'Tăng nồng độ digoxin nhẹ', 'management':
        'Theo dõi nồng độ digoxin. Thận trọng.'}, {'drug':
        'Methotrexate (liều cao)', 'mechanism':
        'PPI giảm thải trừ methotrexate qua thận', 'effect':
        'Tăng nồng độ methotrexate, tăng nguy cơ độc tính', 'management':
        'Thận trọng. Tạm ngừng PPI khi dùng methotrexate liều cao.'}, {'drug':
        'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'PPI tăng pH dạ dày, giảm hấp thu azole antifungals', 'effect':
        'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ.'}, {'drug': 'Iron salts, Vitamin B12',
        'mechanism': 'PPI giảm acid dạ dày, giảm hấp thu', 'effect':
        'Giảm hấp thu sắt và B12', 'management':
        'Cách thời gian ít nhất 2 giờ. Bổ sung B12 nếu dùng lâu dài.'}],
        'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng lansoprazole hoặc PPI khác',
        'Dùng cùng atazanavir (HIV protease inhibitor)'], 'tương_đối': [
        'Suy gan nặng (Child-Pugh C) - giảm liều tối đa 15mg/ngày',
        'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng',
        'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài',
        'Nhiễm C. difficile - tăng nguy cơ',
        'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài',
        'Thiếu magnesium - bổ sung nếu dùng lâu dài']}, 'pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'Lansoprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Lansoprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. An toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều, nhưng thận trọng', 'severe':
        'Giảm liều tối đa 15mg/ngày (Child-Pugh C). Lansoprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4.'
        , 'notes':
        'Suy gan nặng làm giảm chuyển hóa, tăng nồng độ. Giảm liều ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': [
        'PPI ít gây quá liều nghiêm trọng',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': ['Hỗ trợ triệu chứng',
        'Theo dõi dấu hiệu sinh tồn', 'Hầu hết trường hợp tự khỏi'],
        'monitoring': 'Theo dõi dấu hiệu sinh tồn'}, 'reversal_agents': None,
        'administration_instructions': {'oral': {'with_food':
        'Uống 30 phút TRƯỚC bữa ăn (quan trọng)', 'timing':
        'Uống vào buổi sáng trước bữa sáng. Viên tan trong miệng: đặt trên lưỡi, để tan tự nhiên, không cần nước. KHÔNG nghiền hoặc nhai viên bao tan trong ruột.'
        }, 'iv': {'reconstitution': 'Không có dạng IV cho lansoprazole',
        'infusion_rate': 'N/A', 'compatibility': [], 'incompatibility': [],
        'notes': 'Lansoprazole chỉ có dạng uống (PO)'}}, 'references': {
        'primary_sources': ['FDA Drug Label - Lansoprazole',
        'UpToDate - Proton pump inhibitors: Overview of use and adverse effects',
        'Micromedex - Lansoprazole',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs'}},
    "Esomeprazole": {'group': 'Gastrointestinal - Proton Pump Inhibitor (PPI)',
        'vietnamese_name': 'Esomeprazole, Nexium', 'administration': ['PO',
        'IV'], 'indications': ['Loét dạ dày tá tràng',
        'Trào ngược dạ dày thực quản (GERD)', 'Hội chứng Zollinger-Ellison',
        'Tiệt trừ H. pylori (kết hợp)', 'Loét do NSAID (dự phòng)'],
        'contraindications': ['Dị ứng esomeprazole/PPI'], 'dosage': {'adult_po':
        '20-40mg x 1 lần/ngày', 'adult_iv': '20-40mg x 1 lần/ngày',
        'adult_h_pylori':
        '20mg x 2 lần/ngày (với amoxicillin + clarithromycin)',
        'adult_gerd_healing': '40mg x 1 lần/ngày x 4-8 tuần', 'notes':
        'Enantiomer của omeprazole (S-omeprazole). Uống trước bữa ăn'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Đau đầu', 'Tiêu chảy',
        'Đau bụng', 'Tăng nguy cơ nhiễm trùng (C. difficile)',
        'Loãng xương (dùng lâu dài)', 'Thiếu vitamin B12 (dùng lâu dài)',
        'Thiếu magie (hiếm)'], 'interactions': [
        'Warfarin: tăng nhẹ nguy cơ chảy máu',
        'Ketoconazole/Itraconazole: giảm hấp thu',
        'Clopidogrel: có thể giảm hiệu quả (controversial)',
        'Methotrexate: tăng nồng độ methotrexate'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Enantiomer S của omeprazole. Ức chế không hồi phục enzyme H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, ức chế bước cuối cùng trong quá trình tiết acid dạ dày. Chuyển hóa qua CYP2C19 ít hơn omeprazole (racemic) → hiệu quả tốt hơn và ổn định hơn. Ức chế cả acid kích thích và acid cơ bản. Tác dụng mạnh hơn và ổn định hơn omeprazole do ít chuyển hóa qua CYP2C19.'
        , 'monitoring': ['Đáp ứng lâm sàng (giảm đau, triệu chứng GERD)',
        'Magie máu nếu dùng lâu dài (>1 năm) - có thể giảm magie',
        'Vitamin B12 nếu dùng lâu dài (>2 năm) - có thể thiếu B12',
        'Mật độ xương (DEXA scan) nếu dùng lâu dài và có nguy cơ loãng xương',
        'Dấu hiệu nhiễm C. difficile (tiêu chảy nặng, đau bụng) - tăng nguy cơ',
        'INR nếu dùng với warfarin (tăng nguy cơ chảy máu)',
        'Chức năng thận (nếu dùng lâu dài với nguy cơ suy thận)'],
        'precautions': ['Uống trước bữa ăn 30 phút (tăng hiệu quả)',
        'Không nghiền hoặc nhai viên (bao tan trong ruột)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Cân nhắc ngừng sau 4-8 tuần nếu không cần thiết (giảm nguy cơ tác dụng phụ)'
        , 'Cân nhắc dùng liều cách ngày hoặc ngắt quãng nếu dùng lâu dài',
        'Thận trọng ở bệnh nhân suy gan nặng (giảm liều)',
        'Không dùng với các thuốc cần acid để hấp thu (ketoconazole, itraconazole, iron salts)'
        ,
        'Cân nhắc tương tác với clopidogrel (có thể giảm hiệu quả - controversial, cân nhắc dùng PPI khác)'
        ], 'pharmacokinetics': {'half_life':
        '1-1.5 giờ (ngắn, nhưng tác dụng kéo dài do ức chế không hồi phục)',
        'onset': '1-3 giờ', 'duration': '24 giờ (một lần/ngày)',
        'protein_binding': '97%', 'clearance':
        'Gan (chuyển hóa qua CYP2C19 ít hơn omeprazole, CYP3A4), thận (thải trừ)'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên bao tan trong ruột: không nghiền hoặc nhai.'
        , 'black_box_warnings':
        'Dùng lâu dài (>1 năm) có thể tăng nguy cơ loãng xương, gãy xương hông, cổ tay, cột sống. Dùng lâu dài có thể tăng nguy cơ thiếu vitamin B12. Tăng nguy cơ nhiễm C. difficile.'
        , 'drug_interactions': {'major': [{'drug':
        'Atazanavir (HIV protease inhibitor)', 'mechanism':
        'PPI làm tăng pH dạ dày, giảm hấp thu atazanavir', 'effect':
        'Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV', 'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng esomeprazole với atazanavir.'}, {
        'drug': 'Clopidogrel', 'mechanism':
        'Esomeprazole ức chế CYP2C19, enzyme cần thiết để chuyển hóa clopidogrel',
        'effect':
        'Giảm hiệu quả chống kết tập tiểu cầu của clopidogrel (controversial, nhưng nên thận trọng)'
        , 'management':
        'Thận trọng. Cân nhắc dùng pantoprazole (ít ảnh hưởng hơn) hoặc cách thời gian.'
        }], 'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Esomeprazole ức chế CYP2C9 nhẹ', 'effect':
        'Tăng INR nhẹ, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}, {
        'drug': 'Methotrexate (liều cao)', 'mechanism':
        'PPI giảm thải trừ methotrexate qua thận', 'effect':
        'Tăng nồng độ methotrexate, tăng nguy cơ độc tính', 'management':
        'Thận trọng. Tạm ngừng PPI khi dùng methotrexate liều cao.'}, {'drug':
        'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'PPI tăng pH dạ dày, giảm hấp thu azole antifungals', 'effect':
        'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ.'}, {'drug': 'Iron salts, Vitamin B12',
        'mechanism': 'PPI giảm acid dạ dày, giảm hấp thu', 'effect':
        'Giảm hấp thu sắt và B12', 'management':
        'Cách thời gian ít nhất 2 giờ. Bổ sung B12 nếu dùng lâu dài.'}],
        'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng esomeprazole hoặc PPI khác',
        'Dùng cùng atazanavir (HIV protease inhibitor)'], 'tương_đối': [
        'Suy gan nặng (Child-Pugh C) - giảm liều tối đa 20mg/ngày',
        'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng',
        'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài',
        'Nhiễm C. difficile - tăng nguy cơ',
        'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài',
        'Thiếu magnesium - bổ sung nếu dùng lâu dài']}, 'pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'Esomeprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. An toàn hơn omeprazole (category C) trong thai kỳ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Esomeprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. An toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều, nhưng thận trọng', 'severe':
        'Giảm liều tối đa 20mg/ngày (Child-Pugh C). Esomeprazole chuyển hóa ở gan qua CYP2C19 (ít hơn omeprazole) và CYP3A4.'
        , 'notes':
        'Esomeprazole ít phụ thuộc CYP2C19 hơn omeprazole, nên ít ảnh hưởng hơn ở suy gan. Tuy nhiên, vẫn giảm liều ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': [
        'PPI ít gây quá liều nghiêm trọng',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': ['Hỗ trợ triệu chứng',
        'Theo dõi dấu hiệu sinh tồn', 'Hầu hết trường hợp tự khỏi'],
        'monitoring': 'Theo dõi dấu hiệu sinh tồn'}, 'reversal_agents': None,
        'administration_instructions': {'oral': {'with_food':
        'Uống 30 phút TRƯỚC bữa ăn (quan trọng)', 'timing':
        'Uống vào buổi sáng trước bữa sáng (hoặc trước bữa tối nếu dùng 2 lần/ngày). KHÔNG nghiền hoặc nhai viên bao tan trong ruột - phải nuốt nguyên viên.'
        }, 'iv': {'reconstitution':
        'Esomeprazole IV: 20-40mg pha với 100ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate': 'Truyền trong 10-30 phút', 'compatibility': [
        'NaCl 0.9%', 'Dextrose 5%'], 'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể.'}},
        'references': {'primary_sources': ['FDA Drug Label - Esomeprazole',
        'UpToDate - Proton pump inhibitors: Overview of use and adverse effects',
        'Micromedex - Esomeprazole',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs'}}}

__all__ = ['PROTON_PUMP_INHIBITOR_(PPI)S_DRUGS']
