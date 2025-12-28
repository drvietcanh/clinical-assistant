"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Anthelmintics

ANTHELMINTICS_DRUGS = {
    "Albendazole": {'group': 'Infectious Disease - Anthelmintic', 'vietnamese_name':
        'Albendazole, Albenza', 'administration': ['PO'], 'indications': [
        'Giun sán (giun đũa, giun móc, giun tóc, giun kim)', 'Sán dây',
        'Sán lá gan', 'Hydatid disease (Echinococcus)', 'Neurocysticercosis'],
        'contraindications': ['Dị ứng albendazole/benzimidazole', 'Có thai',
        'Suy gan nặng', 'Giảm bạch cầu'], 'dosage': {'adult_intestinal_worms':
        '400mg x 1 lần (đơn liều) hoặc 400mg x 2 lần/ngày x 3 ngày',
        'adult_echinococcus': '400mg x 2 lần/ngày x 28 ngày (có thể lặp lại)',
        'adult_neurocysticercosis': '400mg x 2 lần/ngày x 8-30 ngày',
        'adult_hydatid': '10-15mg/kg/ngày x 28 ngày', 'notes':
        'Uống với thức ăn béo để tăng hấp thu. Uống kèm corticosteroid cho neurocysticercosis'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'}, 'side_effects': ['Đau đầu', 'Buồn nôn, nôn',
        'Đau bụng', 'Tiêu chảy', 'Giảm bạch cầu', 'Tăng men gan', 'Ban da',
        'Rụng tóc (dùng lâu dài)'], 'interactions': [
        'Dexamethasone: tăng nồng độ albendazole',
        'Praziquantel: tăng nồng độ albendazole',
        'Cimetidine: tăng nồng độ albendazole',
        'Phenytoin/Carbamazepine: giảm nồng độ albendazole'], 'pregnancy':
        'D - Chống chỉ định', 'mechanism_of_action':
        'Albendazole là benzimidazole carbamate, ức chế tubulin polymerization trong tế bào ký sinh trùng, gây mất microtubule, phá vỡ cấu trúc tế bào và chức năng của ký sinh trùng. Thuốc ngăn chặn vận chuyển glucose và các chất dinh dưỡng khác trong tế bào ký sinh trùng, dẫn đến mất năng lượng và chết. Albendazole có tác dụng phổ rộng trên nhiều loại giun sán, bao gồm giun đũa, giun móc, giun tóc, giun kim, sán dây, và sán lá gan. Đặc biệt hiệu quả trong điều trị hydatid disease và neurocysticercosis do tác dụng hệ thống tốt hơn mebendazole.'
        , 'monitoring': [
        'Công thức máu (CBC) - theo dõi giảm bạch cầu, đặc biệt khi dùng lâu dài',
        'Chức năng gan (ALT, AST, bilirubin) - theo dõi độc tính gan',
        'Triệu chứng lâm sàng (đau đầu, buồn nôn, đau bụng)',
        'Đáp ứng điều trị (xét nghiệm phân sau điều trị)',
        'Dấu hiệu nhiễm độc (rụng tóc, ban da) khi dùng lâu dài'],
        'precautions': [
        'Uống với thức ăn béo để tăng hấp thu (tăng nồng độ trong máu 5 lần)',
        'Dùng kèm corticosteroid (dexamethasone) cho neurocysticercosis để giảm phản ứng viêm'
        ,
        'Theo dõi chức năng gan thường xuyên khi dùng lâu dài (hydatid disease, neurocysticercosis)'
        , 'Tránh dùng trong thai kỳ (gây dị tật thai nhi)',
        'Kiểm tra thai trước khi bắt đầu điều trị',
        'Dùng biện pháp tránh thai hiệu quả trong và sau điều trị',
        'Thận trọng ở bệnh nhân suy gan',
        'Theo dõi công thức máu khi dùng lâu dài (nguy cơ giảm bạch cầu)'],
        'pharmacokinetics': {'half_life':
        '8-12 giờ (albendazole sulfoxide - chất chuyển hóa hoạt động)', 'onset':
        '2-4 giờ', 'duration': '24-48 giờ', 'protein_binding': '70%',
        'clearance':
        'Gan (chuyển hóa thành albendazole sulfoxide), thải trừ qua mật và nước tiểu'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Cần kiểm tra thai trước khi bắt đầu điều trị'
        , 'drug_interactions': {'major': [{'drug': 'Dexamethasone', 'mechanism':
        'Tăng nồng độ albendazole sulfoxide (chất chuyển hóa hoạt động) qua ức chế CYP3A4'
        , 'effect': 'Tăng nồng độ albendazole, tăng hiệu quả và độc tính',
        'management':
        'Theo dõi chức năng gan và công thức máu. Có thể cần giảm liều albendazole'
        }, {'drug': 'Praziquantel', 'mechanism':
        'Tăng nồng độ albendazole sulfoxide', 'effect':
        'Tăng hiệu quả điều trị, nhưng cũng tăng độc tính', 'management':
        'Theo dõi chức năng gan và công thức máu'}], 'moderate': [{'drug':
        'Cimetidine', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ albendazole sulfoxide', 'effect':
        'Tăng nồng độ albendazole', 'management': 'Theo dõi chức năng gan'}, {
        'drug': 'Phenytoin, Carbamazepine', 'mechanism':
        'Cảm ứng CYP3A4, tăng chuyển hóa albendazole', 'effect':
        'Giảm nồng độ albendazole, giảm hiệu quả', 'management':
        'Có thể cần tăng liều albendazole hoặc dùng thuốc khác'}]},
        'contraindications': {'tuyệt_đối': [
        'Có thai (category D - gây dị tật thai nhi)',
        'Dị ứng albendazole hoặc benzimidazole', 'Suy gan nặng (Child-Pugh C)'],
        'tương_đối': [
        'Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, theo dõi chức năng gan'
        , 'Giảm bạch cầu - thận trọng, theo dõi công thức máu',
        'Suy thận nặng (CrCl <30) - thận trọng']}, 'pregnancy_lactation': {
        'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Albendazole có thể gây dị tật thai nhi và tử vong thai nhi. Cần kiểm tra thai trước khi bắt đầu điều trị. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả trong và sau điều trị ít nhất 1 tháng.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Albendazole bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình trạng lâm sàng'
        }}, 'hepatic_adjustment': {'mild':
        'Không đổi liều, nhưng theo dõi chức năng gan', 'moderate':
        'Thận trọng, theo dõi chức năng gan thường xuyên', 'severe':
        'Tránh dùng hoặc dùng liều thấp dưới sự giám sát chặt chẽ. Theo dõi ALT/AST, bilirubin thường xuyên'
        , 'notes':
        'Albendazole chuyển hóa ở gan thành albendazole sulfoxide (hoạt chất). Suy gan có thể làm giảm chuyển hóa và tăng tích lũy, tăng nguy cơ độc tính gan'
        }, 'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Đau đầu, chóng mặt', 'Tăng men gan (ALT, AST)', 'Giảm bạch cầu',
        'Ban da, rụng tóc'], 'antidote': 'Không có thuốc giải độc đặc hiệu',
        'treatment': ['Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1 giờ',
        'Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải',
        'Theo dõi chức năng gan (ALT, AST, bilirubin) thường xuyên',
        'Theo dõi công thức máu (CBC) - theo dõi giảm bạch cầu',
        'Điều trị triệu chứng: Thuốc chống nôn, giảm đau nếu cần'],
        'monitoring':
        'Chức năng gan (ALT, AST, bilirubin), công thức máu (CBC), triệu chứng lâm sàng'
        },         'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có thuốc giải độc đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: rửa dạ dày nếu sớm, than hoạt tính, theo dõi chức năng gan và công thức máu, điều trị triệu chứng.'},
        'administration_instructions': {'oral': {'with_food':
        'BẮT BUỘC uống với thức ăn béo (bữa ăn có chất béo) để tăng hấp thu. Uống với thức ăn béo tăng nồng độ trong máu lên 5 lần so với uống khi đói'
        , 'timing':
        'Uống với bữa ăn chính (sáng, trưa, tối). Với hydatid disease và neurocysticercosis: 400mg x 2 lần/ngày với bữa ăn'
        , 'notes':
        'Với neurocysticercosis: dùng kèm corticosteroid (dexamethasone) để giảm phản ứng viêm. Với hydatid disease: có thể cần lặp lại chu kỳ 28 ngày'
        }},         'references': {'primary_sources': [
        'FDA Drug Label - Albendazole (Albenza)',
        'UpToDate - Albendazole drug information',
        'WHO Guidelines for treatment of echinococcosis',
        'WHO Guidelines for treatment of neurocysticercosis',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics"],
        'last_updated': '2025-02-04', 'evidence_level':
        'High - Guidelines dựa trên chứng cứ từ WHO và FDA'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['Hepatotoxicity (especially with long-term use)', 'Bone marrow suppression (leukopenia)', 'Teratogenicity (pregnancy category D)'],
            'qt_prolongation': False,
            'hepatotoxicity': True,
            'nephrotoxicity': False,
            'requires_monitoring': ['Hepatic function (ALT, AST, bilirubin) - CRITICAL for long-term use', 'CBC (leukopenia) - especially long-term', 'Pregnancy test before treatment']
        },
        'guideline_tags': [
            'WHO Guidelines - Echinococcosis Treatment',
            'WHO Guidelines - Neurocysticercosis Treatment',
            'FDA Black Box Warning - Albendazole and Pregnancy (Category D)',
            'CDC Guidelines - Parasitic Infections'
        ]},
    "Mebendazole": {'group': 'Infectious Disease - Anthelmintic', 'vietnamese_name':
        'Mebendazole, Vermox', 'administration': ['PO'], 'indications': [
        'Giun sán (giun đũa, giun móc, giun tóc, giun kim)', 'Sán dây',
        'Trichinosis'], 'contraindications': [
        'Dị ứng mebendazole/benzimidazole', 'Có thai', 'Trẻ em <1 tuổi'],
        'dosage': {'adult_intestinal_worms': '100mg x 2 lần/ngày x 3 ngày',
        'adult_pinworm': '100mg x 1 lần (đơn liều), lặp lại sau 2-3 tuần',
        'adult_whipworm': '100mg x 2 lần/ngày x 3 ngày', 'adult_tapeworm':
        '100mg x 2 lần/ngày x 3 ngày', 'notes':
        'Uống với thức ăn hoặc không đều được. Không hấp thu tốt nên ít tác dụng phụ hệ thống'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Đau bụng', 'Tiêu chảy',
        'Buồn nôn', 'Ban da', 'Giảm bạch cầu (dùng lâu dài, liều cao)',
        'Độc gan (hiếm)'], 'interactions': [
        'Cimetidine: có thể tăng nồng độ mebendazole',
        'Carbamazepine/Phenytoin: có thể giảm nồng độ mebendazole'],
        'pregnancy': 'D - Chống chỉ định', 'mechanism_of_action':
        'Mebendazole là benzimidazole carbamate, ức chế tubulin polymerization trong tế bào ký sinh trùng, gây mất microtubule và phá vỡ cấu trúc tế bào. Thuốc ngăn chặn vận chuyển glucose và các chất dinh dưỡng trong tế bào ký sinh trùng, dẫn đến mất năng lượng và chết. Khác với albendazole, mebendazole hấp thu kém qua đường tiêu hóa (<5%), nên chủ yếu tác dụng tại chỗ trong ruột, ít tác dụng phụ hệ thống. Thuốc hiệu quả trên giun đũa, giun móc, giun tóc, giun kim, và sán dây. Thường dùng cho nhiễm giun đường ruột đơn giản, ít dùng cho nhiễm nấm hệ thống.'
        , 'monitoring': ['Triệu chứng lâm sàng (đau bụng, tiêu chảy, buồn nôn)',
        'Đáp ứng điều trị (xét nghiệm phân sau 2-3 tuần)',
        'Công thức máu (nếu dùng lâu dài, liều cao) - theo dõi giảm bạch cầu',
        'Chức năng gan (nếu dùng lâu dài, liều cao)',
        'Dấu hiệu dị ứng (ban da)'], 'precautions': [
        'Có thể uống với thức ăn hoặc không (không ảnh hưởng nhiều do hấp thu kém)'
        ,
        'Không hấp thu tốt nên ít tác dụng phụ hệ thống (ưu điểm so với albendazole)'
        , 'Phù hợp cho nhiễm giun đường ruột đơn giản',
        'Lặp lại liều sau 2-3 tuần cho giun kim (để diệt ấu trùng mới nở)',
        'Tránh dùng trong thai kỳ (gây dị tật thai nhi)',
        'Không dùng cho trẻ em <1 tuổi', 'Thận trọng ở bệnh nhân suy gan nặng',
        'Theo dõi công thức máu nếu dùng lâu dài hoặc liều cao'],
        'pharmacokinetics': {'half_life':
        '2-9 giờ (rất thay đổi do hấp thu kém)', 'onset': '2-4 giờ', 'duration':
        '24-48 giờ', 'protein_binding': '90-95%', 'clearance':
        'Hấp thu kém (<5%), chủ yếu thải trừ qua phân, một phần qua nước tiểu'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi',
        'drug_interactions': {'moderate': [{'drug': 'Cimetidine', 'mechanism':
        'Có thể ức chế chuyển hóa mebendazole, tăng nồng độ', 'effect':
        'Tăng nồng độ mebendazole (nhưng ít ảnh hưởng do hấp thu kém)',
        'management': 'Theo dõi tác dụng phụ'}, {'drug':
        'Carbamazepine, Phenytoin', 'mechanism': 'Cảm ứng enzyme chuyển hóa',
        'effect':
        'Có thể giảm nồng độ mebendazole (nhưng ít ảnh hưởng do hấp thu kém)',
        'management': 'Theo dõi đáp ứng điều trị'}]}, 'contraindications': {
        'tuyệt_đối': ['Có thai (category D - gây dị tật thai nhi)',
        'Dị ứng mebendazole hoặc benzimidazole', 'Trẻ em <1 tuổi'], 'tương_đối':
        ['Suy gan nặng - thận trọng',
        'Giảm bạch cầu - thận trọng khi dùng lâu dài']}, 'pregnancy_lactation':
        {'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Mebendazole có thể gây dị tật thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả trong và sau điều trị.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Mebendazole hấp thu kém (<5%) nên ít bài tiết vào sữa mẹ. Tuy nhiên, không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình trạng lâm sàng'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi liều', 'moderate':
        'Không đổi liều', 'severe': 'Thận trọng, theo dõi chức năng gan',
        'notes':
        'Mebendazole hấp thu kém qua đường tiêu hóa (<5%), chủ yếu tác dụng tại chỗ trong ruột, ít tác dụng phụ hệ thống. Suy gan ít ảnh hưởng do hấp thu kém'
        }, 'overdose_management': {'symptoms': ['Đau bụng, tiêu chảy',
        'Buồn nôn, nôn', 'Ban da', 'Giảm bạch cầu (nếu dùng liều cao, lâu dài)',
        'Độc gan (hiếm)'], 'antidote': 'Không có thuốc giải độc đặc hiệu',
        'treatment': ['Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1 giờ',
        'Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải',
        'Điều trị triệu chứng: Thuốc chống nôn, giảm đau nếu cần',
        'Theo dõi công thức máu nếu dùng liều cao, lâu dài',
        'Theo dõi chức năng gan nếu có triệu chứng'], 'monitoring':
        'Triệu chứng lâm sàng, công thức máu (nếu dùng liều cao), chức năng gan (nếu có triệu chứng)'
        },         'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có thuốc giải độc đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ: rửa dạ dày nếu sớm, than hoạt tính, điều trị triệu chứng, theo dõi công thức máu và chức năng gan nếu cần.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với thức ăn hoặc không (không ảnh hưởng nhiều do hấp thu kém). Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ'
        , 'timing':
        'Uống với bữa ăn hoặc không. Với giun đũa, giun móc, giun tóc, sán dây: 100mg x 2 lần/ngày x 3 ngày. Với giun kim: 100mg x 1 lần (đơn liều), lặp lại sau 2-3 tuần'
        , 'notes':
        'Lặp lại liều sau 2-3 tuần cho giun kim để diệt ấu trùng mới nở. Không hấp thu tốt nên ít tác dụng phụ hệ thống (ưu điểm so với albendazole)'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Mebendazole (Vermox)',
        'UpToDate - Mebendazole drug information',
        'WHO Guidelines for treatment of soil-transmitted helminthiasis',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics"],
        'last_updated': '2025-02-04', 'evidence_level':
        'High - Guidelines dựa trên chứng cứ từ WHO và FDA'}},
    "Praziquantel": {'group': 'Infectious Disease - Anthelmintic', 'vietnamese_name':
        'Praziquantel', 'administration': ['PO'], 'indications': [
        'Schistosomiasis (sán máng)', 'Cestodes: Taenia spp., Diphyllobothrium',
        'Neurocysticercosis (off-label)', 'Clonorchis/Opisthorchis (sán lá gan nhỏ)']
        , 'contraindications': [
        'Dị ứng praziquantel', 'Ocular cysticercosis', 'Dùng rifampin đồng thời']
        , 'dosage': {'adult_schisto': '20mg/kg x 3 lần/ngày x 1 ngày (cách 4-6 giờ)',
        'adult_cestode': '5-10mg/kg x 1 lần (taeniasis) hoặc 25mg/kg x 3 lần/ngày x 1 ngày (cestode khác)',
        'adult_neurocysticercosis': '50-100mg/kg/ngày chia 3 lần x 14 ngày',
        'notes': 'Uống với thức ăn; nuốt nguyên viên, không nhai vì đắng'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng do thiếu dữ liệu'}, 'side_effects': [
        'Đau đầu, chóng mặt, buồn ngủ', 'Buồn nôn, đau bụng', 'Vị đắng/kim loại',
        'Tăng men gan thoáng qua', 'Co giật/loạn cảm hiếm gặp (neurocysticercosis)']
        , 'interactions': [
        'Rifampin: giảm mạnh nồng độ praziquantel (tránh phối hợp)',
        'Cimetidine, azole: tăng nồng độ praziquantel',
        'Phenytoin/carbamazepine: giảm nồng độ praziquantel'], 'pregnancy':
        'B - Tránh trong 3 tháng đầu, dùng được từ tam cá nguyệt 2-3 nếu cần'
        , 'mechanism_of_action':
        'Tăng tính thấm màng tế bào ký sinh trùng với ion Ca2+, gây co cứng cơ, liệt và chết ký sinh trùng; hiệu quả trên sán dây, sán lá, schistosoma.'
        , 'monitoring': [
        'Triệu chứng lâm sàng, xét nghiệm phân/nước tiểu sau điều trị',
        'Chức năng gan nếu dùng liều cao/kéo dài', 'Theo dõi thần kinh ở bệnh nhân neurocysticercosis']
        , 'precautions': [
        'Tránh dùng đồng thời rifampin (giảm nồng độ, thất bại điều trị)',
        'Thận trọng suy gan (tăng nồng độ)', 'Có thể gây ngủ gà/chóng mặt: tránh lái xe 24 giờ',
        'Neurocysticercosis: dùng kèm corticosteroid để giảm phản ứng viêm', 'Không nhai viên do vị rất đắng'],
        'pharmacokinetics': {'half_life': '1-2.5 giờ', 'onset': '1-3 giờ',
        'duration': '6-8 giờ', 'protein_binding': '80%', 'clearance':
        'Chuyển hóa gan (CYP3A4), thải trừ qua thận và mật'}, 'storage':
        'Bảo quản nhiệt độ phòng, tránh ẩm, tránh ánh sáng', 'black_box_warnings':
        None, 'drug_interactions': {'major': [{'drug': 'Rifampin', 'mechanism':
        'Cảm ứng CYP3A4 mạnh, giảm nồng độ praziquantel', 'effect':
        'Giảm hiệu quả điều trị', 'management': 'Tránh phối hợp'}], 'moderate': [
        {'drug': 'Cimetidine, Azole', 'mechanism': 'Ức chế CYP3A4', 'effect':
        'Tăng nồng độ praziquantel', 'management': 'Theo dõi tác dụng phụ'},
        {'drug': 'Phenytoin, Carbamazepine', 'mechanism': 'Cảm ứng CYP',
        'effect': 'Giảm nồng độ praziquantel', 'management': 'Cân nhắc tăng liều hoặc chọn thuốc khác'}]}
        , 'contraindications': {'tuyệt_đối': ['Dị ứng praziquantel',
        'Ocular cysticercosis', 'Dùng rifampin đồng thời'], 'tương_đối': [
        'Suy gan (tăng nồng độ, thận trọng)']}, 'contraindications_detail': {
        'tuyệt_đối': ['Dị ứng praziquantel',
        'Ocular cysticercosis', 'Dùng rifampin đồng thời'], 'tương_đối': [
        'Suy gan (tăng nồng độ, thận trọng)']}, 'black_box_warnings': None,
        'pregnancy_lactation': {
        'fda_category': 'B', 'pregnancy_details':
        'Tránh tam cá nguyệt 1; có thể dùng tam cá nguyệt 2-3 nếu lợi ích vượt nguy cơ'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Bài tiết ít vào sữa; có thể cho bú sau 72 giờ nếu muốn giảm phơi nhiễm'
        , 'recommendation': 'Cân nhắc tạm ngừng cho bú 72 giờ sau liều cuối trong trường hợp liều cao'}},
        'hepatic_adjustment': {'mild': 'Không đổi, nhưng theo dõi', 'moderate':
        'Thận trọng, có thể cần giảm liều', 'severe':
        'Tránh hoặc dùng dưới giám sát chặt'}, 'overdose_management': {
        'symptoms': ['Chóng mặt, buồn ngủ', 'Buồn nôn, nôn', 'Loạn cảm, ảo giác hiếm'],
        'antidote': 'Không có', 'treatment': ['Hỗ trợ, than hoạt nếu sớm',
        'Theo dõi huyết động, thần kinh']}, 'reversal_agents': {'available':
        False, 'agents': None, 'notes': 'Không có thuốc giải độc đặc hiệu'},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn để giảm kích ứng dạ dày', 'timing':
        'Chia liều cách nhau 4-6 giờ trong ngày điều trị', 'notes':
        'Nuốt nguyên viên, không nhai do vị rất đắng'}}, 'references': {
        'primary_sources': ['WHO schistosomiasis treatment guideline',
        'UpToDate - Praziquantel', 'FDA label'], 'last_updated': '2025-02-06',
        'evidence_level': 'High - hướng dẫn WHO/FDA'}},
    "Ivermectin": {'group': 'Infectious Disease - Anthelmintic', 'vietnamese_name':
        'Ivermectin', 'administration': ['PO'], 'indications': [
        'Strongyloidiasis', 'Onchocerciasis', 'Ấu trùng di trú da', 'Ghẻ/chấy (off-label)']
        , 'contraindications': ['Dị ứng ivermectin', 'Trẻ <15kg (thiếu dữ liệu)'],
        'dosage': {'adult_strongyloides': '200 mcg/kg PO x 1, lặp lại sau 2 tuần nếu cần',
        'adult_onchocerciasis': '150 mcg/kg PO mỗi 3-12 tháng', 'adult_scabies':
        '200 mcg/kg PO, lặp lại sau 7-14 ngày (off-label)', 'notes':
        'Uống lúc bụng đói với nước; cân nặng để tính liều'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': [
        'Chóng mặt, mệt mỏi', 'Buồn nôn, tiêu chảy', 'Phản ứng Mazzotti (ngứa, ban, sốt) khi điều trị onchocerciasis'
        ], 'interactions': ['Warfarin: tăng INR hiếm gặp', 'Thuốc ức chế P-gp: thận trọng (nguy cơ độc thần kinh)']
        , 'pregnancy': 'C - tránh nếu có thể', 'mechanism_of_action':
        'Gắn kênh chloride glutamate-gated của ký sinh trùng, tăng dòng chloride, gây liệt và chết ký sinh trùng; không qua hàng máu não người nên an toàn với người.'
        , 'monitoring': [
        'Triệu chứng lâm sàng và xét nghiệm phân (strongyloides)',
        'Theo dõi phản ứng Mazzotti (ngứa, phát ban, sốt) khi điều trị onchocerciasis',
        'Cân nhắc công thức máu và chức năng gan nếu điều trị nhiều đợt'],
        'precautions': [
        'Thận trọng đồng nhiễm Loa loa (nguy cơ viêm não do ấu trùng chết)',
        'Tránh lái xe nếu chóng mặt/mệt', 'Không dùng cho trẻ <15kg do thiếu dữ liệu'
        ], 'pharmacokinetics': {'half_life': '12-36 giờ', 'onset': '4-6 giờ',
        'duration': 'Cao nhất trong 1-2 ngày', 'protein_binding': '93%',
        'clearance': 'Chuyển hóa gan (CYP3A4), thải trừ chủ yếu qua phân'},
        'storage': 'Bảo quản nhiệt độ phòng, tránh ẩm', 'black_box_warnings':
        None, 'drug_interactions': {'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Tăng INR chưa rõ cơ chế', 'effect': 'Tăng nguy cơ chảy máu',
        'management': 'Theo dõi INR khi bắt đầu/dừng ivermectin'}]}, 
        'contraindications': {'tuyệt_đối': ['Dị ứng ivermectin'], 'tương_đối': [
        'Trẻ <15kg', 'Đồng nhiễm Loa loa (nguy cơ biến chứng thần kinh)']},
        'contraindications_detail': {'tuyệt_đối': ['Dị ứng ivermectin'], 'tương_đối': [
        'Trẻ <15kg', 'Đồng nhiễm Loa loa (nguy cơ biến chứng thần kinh)']},
        'black_box_warnings': None,
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Tránh nếu có thể; dùng khi lợi ích vượt trội nguy cơ', 'lactation': {
        'safety': 'Thấp', 'details':
        'Bài tiết ít vào sữa; WHO cho phép dùng liều đơn ở phụ nữ cho con bú >1 tuần tuổi'
        , 'recommendation': 'Có thể dùng nếu cần; theo dõi trẻ sơ sinh'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Thận trọng',
        'severe': 'Thiếu dữ liệu, thận trọng tối đa'}, 'overdose_management': {
        'symptoms': ['Chóng mặt, nôn', 'Hạ huyết áp, ngủ gà', 'Co giật hiếm'],
        'antidote': 'Không có', 'treatment': ['Hỗ trợ, than hoạt nếu sớm',
        'Theo dõi huyết áp, hô hấp', 'Điều trị triệu chứng']},
        'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có thuốc giải độc đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ, than hoạt nếu sớm, theo dõi huyết áp, hô hấp, và điều trị triệu chứng.'}, 'administration_instructions': {
        'oral': {'with_food': 'Uống lúc đói với nước (tăng hấp thu nhẹ)',
        'timing': 'Uống 1 lần; lặp lại theo chỉ định', 'notes':
        'Tính liều theo cân nặng, làm tròn theo viên 3mg/6mg nếu cần'}},
        'references': {'primary_sources': [
        'WHO guidelines for strongyloidiasis/onchocerciasis',
        'UpToDate - Ivermectin', 'CDC DPDx - Ivermectin'],
        'last_updated': '2025-02-06', 'evidence_level': 'High - WHO/CDC/UpToDate'},
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['Mazzotti reaction (itching, rash, fever) when treating onchocerciasis', 'Neurological toxicity (rare, with P-gp inhibitors)'],
            'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Clinical symptoms and stool examination (for strongyloidiasis)', 'Mazzotti reaction (itching, rash, fever) when treating onchocerciasis', 'INR if co-administered with warfarin', 'CBC and hepatic function if multiple courses']
        },
        'guideline_tags': [
            'WHO Guidelines - Strongyloidiasis Treatment',
            'WHO Guidelines - Onchocerciasis Treatment',
            'CDC Guidelines - Parasitic Infections',
            'FDA Drug Information - Ivermectin'
        ]},
    "Levamisole": {'group': 'Infectious Disease - Anthelmintic', 'vietnamese_name':
        'Levamisole', 'administration': ['PO'], 'indications': [
        'Tẩy giun (giun đũa, giun móc) - ít dùng hiện nay'], 'contraindications':
        ['Dị ứng levamisole', 'Tiền sử giảm bạch cầu hạt', 'Có thai'],
        'dosage': {'adult_roundworm': '150mg x 1 lần (đơn liều) sau ăn tối',
        'notes': 'Ít dùng do nguy cơ giảm bạch cầu hạt; cân nhắc thuốc khác an toàn hơn'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'}, 'side_effects': [
        'Buồn nôn, nôn, đau bụng', 'Nhức đầu, chóng mặt', 'Vị kim loại',
        'Giảm bạch cầu hạt hiếm nhưng nghiêm trọng'], 'interactions': [
        'Clozapine: tăng nguy cơ giảm bạch cầu hạt', 'Warfarin: có thể tăng INR'],
        'pregnancy': 'C - tránh dùng', 'mechanism_of_action':
        'Kích thích hạch thần kinh cơ của giun, gây liệt cơ và tống xuất giun; có tác dụng điều hòa miễn dịch nhẹ.'
        , 'monitoring': [
        'Công thức máu nếu dùng >1 liều hoặc có triệu chứng nhiễm trùng',
        'Triệu chứng thần kinh/tiêu hóa'], 'precautions': [
        'Nguy cơ giảm bạch cầu hạt: ngừng ngay nếu sốt/đau họng',
        'Ít dùng; ưu tiên albendazole/mebendazole nếu không chống chỉ định'],
        'pharmacokinetics': {'half_life': '3-6 giờ', 'onset': '1-2 giờ',
        'duration': '12-24 giờ', 'protein_binding': '~20%', 'clearance':
        'Chuyển hóa gan, thải trừ qua thận'}, 'storage':
        'Bảo quản nhiệt độ phòng, tránh ẩm', 'black_box_warnings': None,
        'drug_interactions': {'moderate': [{'drug': 'Clozapine', 'mechanism':
        'Tăng nguy cơ giảm bạch cầu hạt', 'effect': 'Tăng nguy cơ nhiễm trùng',
        'management': 'Tránh phối hợp'}, {'drug': 'Warfarin', 'mechanism':
        'Chưa rõ, có thể tăng INR', 'effect': 'Tăng nguy cơ chảy máu',
        'management': 'Theo dõi INR nếu phối hợp'}]},         'contraindications': {
        'tuyệt_đối': ['Dị ứng levamisole', 'Tiền sử giảm bạch cầu hạt', 'Có thai'],
        'tương_đối': ['Suy gan, suy thận - thận trọng']},
        'contraindications_detail': {
        'tuyệt_đối': ['Dị ứng levamisole', 'Tiền sử giảm bạch cầu hạt', 'Có thai'],
        'tương_đối': ['Suy gan, suy thận - thận trọng']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Tránh dùng; cân nhắc thuốc khác an toàn hơn', 'lactation': {
        'safety': 'Unknown', 'details': 'Không có dữ liệu; tránh dùng nếu có thể',
        'recommendation': 'Nếu buộc dùng, theo dõi trẻ dấu hiệu độc tính'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Thận trọng',
        'severe': 'Tránh nếu có thể'}, 'overdose_management': {
        'symptoms': ['Buồn nôn, nôn, chóng mặt', 'Co giật hiếm'],
        'antidote': 'Không có', 'treatment': ['Điều trị hỗ trợ, than hoạt nếu sớm',
        'Theo dõi CBC, dấu hiệu nhiễm trùng']},         'reversal_agents': {
        'available': False, 'agents': [], 'notes': 'Không có thuốc giải độc đặc hiệu. Điều trị quá liều chủ yếu là điều trị hỗ trợ, than hoạt nếu sớm, theo dõi CBC và dấu hiệu nhiễm trùng.'},
        'administration_instructions': {'oral': {'with_food':
        'Uống sau ăn tối để giảm kích ứng dạ dày', 'timing': 'Liều đơn',
        'notes': 'Theo dõi CBC nếu phải lặp lại hoặc nghi ngờ giảm bạch cầu'}},
        'references': {'primary_sources': [
        'WHO deworming guideline (historical use)', 'UpToDate - Levamisole'],
        'last_updated': '2025-02-06', 'evidence_level': 'Moderate - dữ liệu hạn chế hiện nay'}         "black_box_warnings": None,
}}

__all__ = ['ANTHELMINTICS_DRUGS']
