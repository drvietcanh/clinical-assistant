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
        }, 'reversal_agents': {'available': False, 'agents': None, 'notes':
        'Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ và theo dõi'},
        'administration_instructions': {'oral': {'with_food':
        'BẮT BUỘC uống với thức ăn béo (bữa ăn có chất béo) để tăng hấp thu. Uống với thức ăn béo tăng nồng độ trong máu lên 5 lần so với uống khi đói'
        , 'timing':
        'Uống với bữa ăn chính (sáng, trưa, tối). Với hydatid disease và neurocysticercosis: 400mg x 2 lần/ngày với bữa ăn'
        , 'notes':
        'Với neurocysticercosis: dùng kèm corticosteroid (dexamethasone) để giảm phản ứng viêm. Với hydatid disease: có thể cần lặp lại chu kỳ 28 ngày'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Albendazole (Albenza)',
        'UpToDate - Albendazole drug information',
        'WHO Guidelines for treatment of echinococcosis',
        'WHO Guidelines for treatment of neurocysticercosis',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics"],
        'last_updated': '2025-02-04', 'evidence_level':
        'High - Guidelines dựa trên chứng cứ từ WHO và FDA'}},
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
        }, 'reversal_agents': {'available': False, 'agents': None, 'notes':
        'Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ và theo dõi'},
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
        'High - Guidelines dựa trên chứng cứ từ WHO và FDA'}}}

__all__ = ['ANTHELMINTICS_DRUGS']
