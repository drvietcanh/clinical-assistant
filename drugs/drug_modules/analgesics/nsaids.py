"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# NSAIDs

NSAIDS_DRUGS = {
    "Ibuprofen": {'group': 'Analgesic - NSAID', 'vietnamese_name': 'Ibuprofen, Brufen',
        'administration': ['PO'], 'indications': ['Đau nhẹ đến trung bình',
        'Viêm khớp', 'Sốt', 'Đau bụng kinh'], 'contraindications': [
        'Loét dạ dày tá tràng đang hoạt động', 'Suy thận nặng', 'Suy gan nặng',
        'Có thai (3 tháng cuối)', 'Dị ứng NSAID/aspirin'], 'dosage': {
        'adult_pain': '200-400mg mỗi 4-6 giờ (tối đa 2.4g/ngày)',
        'adult_arthritis': '400-800mg x 3-4 lần/ngày (tối đa 3.2g/ngày)',
        'notes': 'Uống với thức ăn để giảm kích ứng dạ dày'}, 'side_effects': [
        'Chảy máu dạ dày', 'Suy thận', 'Tăng huyết áp', 'Phù', 'Đau đầu',
        'Ban da'], 'interactions': ['Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Aspirin: tăng nguy cơ chảy máu dạ dày',
        'Methotrexate: tăng độc tính methotrexate'], 'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Prostaglandin tham gia vào quá trình đau, viêm, sốt, bảo vệ niêm mạc dạ dày, và điều hòa thận'
        , 'monitoring': [
        'Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)'], 'precautions': [
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'Cân nhắc dùng PPI hoặc misoprostol nếu có nguy cơ loét dạ dày',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể'],
        'pharmacokinetics': {'half_life': '2-4 giờ', 'onset': '30-60 phút',
        'duration': '4-6 giờ', 'protein_binding': '99%', 'clearance':
        'Gan (chuyển hóa qua CYP2C9, CYP2C8), thận (thải trừ)'}, 'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Thận trọng, giảm liều 25-50%', 'under_30':
        'Tránh dùng hoặc giảm liều mạnh. Theo dõi chức năng thận chặt chẽ'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ'
        , 'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu',
        'effect': 'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }], 'moderate': [{'drug': 'ACE inhibitor, ARB', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Aspirin (liều thấp)', 'mechanism':
        'Ibuprofen có thể ức chế tác dụng chống kết tập tiểu cầu của aspirin',
        'effect': 'Giảm hiệu quả phòng ngừa nhồi máu cơ tim của aspirin',
        'management':
        'Dùng aspirin ít nhất 2 giờ trước ibuprofen, hoặc cân nhắc NSAID khác'}, {
        'drug': 'Methotrexate', 'mechanism':
        'Giảm thải trừ methotrexate qua thận', 'effect':
        'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }], 'minor': [{'drug': 'Corticosteroid', 'mechanism':
        'Tăng nguy cơ loét dạ dày', 'effect': 'Tăng nguy cơ chảy máu dạ dày',
        'management': 'Cân nhắc dùng PPI hoặc misoprostol để bảo vệ dạ dày'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng ibuprofen hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'], 'tương_đối':
        ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ']}, 'pregnancy_lactation':
        {'fda_category': 'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Ibuprofen bài tiết vào sữa mẹ ở nồng độ rất thấp (<0.6% liều mẹ). Half-life ngắn (2-4 giờ) nên ít tích lũy. An toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn. Theo dõi trẻ về dấu hiệu bất thường (hiếm).'}}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Ibuprofen chuyển hóa ở gan qua CYP2C9 và CYP2C8. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ibuprofen ít gây độc gan trực tiếp hơn một số NSAID khác (như diclofenac).'
        }, 'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ',
        'Ức chế hô hấp (hiếm, ở liều rất cao)', 'Hạ huyết áp', 'Suy thận cấp',
        'Chảy máu dạ dày', 'Co giật (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim',
        'Hỗ trợ hô hấp nếu có ức chế hô hấp (hiếm)',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 4-6 giờ do half-life ngắn (2-4 giờ)'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        'Mỗi 4-6 giờ (do half-life ngắn). Dùng với bữa ăn để giảm tác dụng phụ dạ dày. Liều tối đa: 2.4g/ngày (đau) hoặc 3.2g/ngày (viêm khớp).'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'pediatric_dosing': {
        'neonates': 'Không khuyến cáo cho trẻ <6 tháng tuổi',
        'infants': '10mg/kg mỗi 6-8 giờ (tối đa 40mg/kg/ngày). Dùng cho sốt và đau',
        'children': '10mg/kg mỗi 6-8 giờ (tối đa 40mg/kg/ngày). Dùng cho sốt, đau, viêm khớp. Liều tối đa: 2.4g/ngày',
        'adolescents': '200-400mg mỗi 4-6 giờ (tối đa 2.4g/ngày). Liều người lớn',
        'notes': 'Dùng cho sốt, đau, viêm khớp ở trẻ em. Uống với thức ăn để giảm kích ứng dạ dày. Theo dõi dấu hiệu chảy máu dạ dày, suy thận'
    }, 'geriatric_dosing': {
        'considerations': 'Người cao tuổi nhạy cảm hơn với tác dụng phụ (chảy máu dạ dày, suy thận). Suy thận, suy tim phổ biến hơn',
        'dose_adjustment': 'Khởi đầu với liều thấp hơn (200mg mỗi 6-8 giờ). Giảm liều nếu có suy thận (CrCl <60). Tránh dùng lâu dài',
        'monitoring': 'Theo dõi dấu hiệu chảy máu dạ dày sát hơn. Theo dõi chức năng thận (creatinine, BUN) thường xuyên. Theo dõi huyết áp'
    }, 'brand_names': {
        'vietnam': ['Brufen', 'Ibuprofen Stada', 'Ibuprofen', 'Advil', 'Nurofen'],
        'common': ['Advil', 'Motrin', 'Ibuprofen', 'Brufen', 'Nurofen']
    }, 'cost_estimate': {
        'unit': 'VND',
        'range': '3,000 - 15,000 VND/viên (tùy hàm lượng và thương hiệu)',
        'note': 'Giá thay đổi theo thương hiệu và nhà thuốc. Ibuprofen generic thường rẻ hơn (3,000-8,000 VND/viên 400mg).'
    }, 'references': {'primary_sources': [
        'FDA Drug Label - Advil, Motrin (ibuprofen)',
        'UpToDate - Ibuprofen: Drug information',
        'Lexicomp - Ibuprofen monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-04', 'evidence_level':
        'High - FDA-approved, extensive clinical data'}},
    "Naproxen": {'group': 'Analgesic - NSAID', 'vietnamese_name': 'Naproxen, Naprosyn',
        'administration': ['PO'], 'indications': ['Đau nhẹ đến trung bình',
        'Viêm khớp dạng thấp', 'Viêm khớp xương khớp',
        'Viêm cột sống dính khớp', 'Đau bụng kinh', 'Đau đầu do căng thẳng',
        'Gout cấp'], 'contraindications': [
        'Loét dạ dày tá tràng đang hoạt động', 'Suy thận nặng', 'Suy gan nặng',
        'Có thai (3 tháng cuối)', 'Dị ứng NSAID/aspirin', 'Suy tim nặng'],
        'dosage': {'adult_pain': '250-500mg x 2 lần/ngày (tối đa 1.25g/ngày)',
        'adult_arthritis': '250-500mg x 2 lần/ngày (tối đa 1.5g/ngày)',
        'adult_dysmenorrhea':
        '500mg ngay khi có triệu chứng, sau đó 250mg mỗi 6-8 giờ', 'adult_gout':
        '750mg ngay, sau đó 250mg mỗi 8 giờ', 'notes':
        'Tác dụng kéo dài hơn ibuprofen. Uống với thức ăn'}, 'renal_adjustment':
        {'normal': 'Không đổi', '30_60': 'Thận trọng, giảm liều', 'under_30':
        'Tránh dùng'}, 'side_effects': ['Chảy máu dạ dày', 'Suy thận',
        'Tăng huyết áp', 'Phù', 'Đau đầu', 'Ban da', 'Nhạy cảm với ánh sáng'],
        'interactions': ['Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Aspirin: giảm hiệu quả naproxen', 'Lithium: tăng nồng độ lithium',
        'Methotrexate: tăng độc tính methotrexate'], 'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Prostaglandin tham gia vào quá trình đau, viêm, sốt, bảo vệ niêm mạc dạ dày, và điều hòa thận. Tác dụng kháng viêm và giảm đau mạnh hơn ibuprofen. Thời gian bán thải dài hơn ibuprofen (12-17 giờ) → tác dụng kéo dài hơn, có thể dùng 2 lần/ngày.'
        , 'monitoring': [
        'Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)', 'Lithium máu nếu dùng với lithium',
        'Nhạy cảm với ánh sáng (ban da khi tiếp xúc ánh nắng)'], 'precautions':
        ['Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'Cân nhắc dùng PPI hoặc misoprostol nếu có nguy cơ loét dạ dày',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Tránh tiếp xúc ánh nắng quá nhiều (nhạy cảm với ánh sáng)',
        'Thời gian bán thải dài → tích lũy ở bệnh nhân suy thận, suy gan'],
        'pharmacokinetics': {'half_life': '12-17 giờ (dài hơn ibuprofen)',
        'onset': '30-60 phút', 'duration': '8-12 giờ', 'protein_binding': '99%',
        'clearance': 'Gan (chuyển hóa qua CYP2C9, CYP1A2), thận (thải trừ)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp',
        'black_box_warnings':
        'Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao.'
        , 'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu',
        'effect': 'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }], 'moderate': [{'drug': 'ACE inhibitor, ARB', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Aspirin (liều thấp)', 'mechanism':
        'Naproxen có thể ức chế tác dụng chống kết tập tiểu cầu của aspirin',
        'effect': 'Giảm hiệu quả phòng ngừa nhồi máu cơ tim của aspirin',
        'management':
        'Dùng aspirin ít nhất 2 giờ trước naproxen, hoặc cân nhắc NSAID khác'},
        {'drug': 'Lithium', 'mechanism': 'Giảm thải trừ lithium qua thận',
        'effect': 'Tăng nồng độ lithium, tăng nguy cơ độc tính', 'management':
        'Theo dõi lithium máu thường xuyên. Có thể cần giảm liều lithium'}, {
        'drug': 'Methotrexate', 'mechanism':
        'Giảm thải trừ methotrexate qua thận', 'effect':
        'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }], 'minor': [{'drug': 'Corticosteroid', 'mechanism':
        'Tăng nguy cơ loét dạ dày', 'effect': 'Tăng nguy cơ chảy máu dạ dày',
        'management': 'Cân nhắc dùng PPI hoặc misoprostol để bảo vệ dạ dày'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng naproxen hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'], 'tương_đối':
        ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ']}, 'pregnancy_lactation':
        {'fda_category': 'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Naproxen bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <1% liều mẹ. Half-life dài (12-17 giờ) nhưng nồng độ trong sữa mẹ thấp nên ít ảnh hưởng đến trẻ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn. Theo dõi trẻ về dấu hiệu bất thường (hiếm).'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Naproxen chuyển hóa ở gan qua CYP2C9 và CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, naproxen ít gây độc gan hơn một số NSAID khác (như diclofenac).'
        }, 'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ',
        'Ức chế hô hấp (hiếm, ở liều rất cao)', 'Hạ huyết áp', 'Suy thận cấp',
        'Chảy máu dạ dày', 'Co giật (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim',
        'Hỗ trợ hô hấp nếu có ức chế hô hấp (hiếm)',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 12-24 giờ do half-life dài (12-17 giờ)'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        'Mỗi 8-12 giờ (do half-life dài). Có thể dùng 2 lần/ngày. Dùng với bữa ăn để giảm tác dụng phụ dạ dày.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Naprosyn (naproxen)',
        'UpToDate - Naproxen: Drug information',
        'Lexicomp - Naproxen monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-06', 'evidence_level':
        'High - FDA-approved, extensive clinical data'}},
    "Diclofenac": {'group': 'Analgesic - NSAID', 'vietnamese_name': 'Diclofenac, Voltaren',
        'administration': ['PO', 'IM', 'Topical'], 'indications': [
        'Đau nhẹ đến trung bình', 'Viêm khớp dạng thấp', 'Viêm khớp xương khớp',
        'Đau sau phẫu thuật', 'Đau do chấn thương', 'Viêm gân (topical)'],
        'contraindications': ['Loét dạ dày tá tràng đang hoạt động',
        'Suy thận nặng', 'Suy gan nặng', 'Có thai (3 tháng cuối)',
        'Dị ứng NSAID/aspirin', 'Suy tim nặng'], 'dosage': {'adult_po':
        '50mg x 2-3 lần/ngày hoặc 75-100mg x 1 lần/ngày (extended release)',
        'adult_im': '75mg IM x 1-2 lần/ngày (tối đa 3 ngày)', 'adult_topical':
        'Bôi 2-4g x 3-4 lần/ngày', 'notes':
        'Hiệu quả cao nhưng nguy cơ tác dụng phụ cao'}, 'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Thận trọng, giảm liều', 'under_30':
        'Tránh dùng'}, 'side_effects': [
        'Chảy máu dạ dày (cao hơn các NSAID khác)', 'Suy thận', 'Tăng huyết áp',
        'Phù', 'Tăng men gan', 'Đau đầu', 'Ban da'], 'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Digoxin: tăng nồng độ digoxin',
        'Methotrexate: tăng độc tính methotrexate'], 'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), ưu tiên COX-2 hơn một số NSAID khác. Giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Prostaglandin tham gia vào quá trình đau, viêm, sốt, bảo vệ niêm mạc dạ dày, và điều hòa thận. Tác dụng kháng viêm và giảm đau mạnh. Có nhiều dạng: uống, tiêm bắp, bôi tại chỗ. Dạng bôi tại chỗ có ít tác dụng phụ hệ thống hơn.'
        , 'monitoring': [
        'Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng) - nguy cơ cao hơn các NSAID khác'
        , 'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (ALT, AST) - diclofenac có nguy cơ tăng men gan cao hơn',
        'Dấu hiệu suy tim (giữ nước, phù)', 'Lithium máu nếu dùng với lithium',
        'Cyclosporine levels nếu dùng với cyclosporine'], 'precautions': [
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'Cân nhắc dùng PPI hoặc misoprostol nếu có nguy cơ loét dạ dày (nguy cơ cao)'
        , 'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Dạng bôi tại chỗ: ít tác dụng phụ hệ thống, phù hợp cho đau cục bộ',
        'IM: chỉ dùng tối đa 3 ngày, không dùng lâu dài',
        'Theo dõi chức năng gan chặt chẽ (nguy cơ tăng men gan)'],
        'pharmacokinetics': {'half_life':
        '1-2 giờ (ngắn), nhưng tác dụng kéo dài do tích lũy trong dịch khớp',
        'onset': '30-60 phút (PO), 10-15 phút (IM)', 'duration': '8-12 giờ',
        'protein_binding': '99.7%', 'clearance':
        'Gan (chuyển hóa qua CYP2C9, CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng bôi: bảo quản ở nhiệt độ phòng, không làm lạnh.'
        , 'black_box_warnings':
        'Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao. Diclofenac có nguy cơ tăng men gan và chảy máu dạ dày cao hơn một số NSAID khác.'
        , 'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu',
        'effect': 'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }], 'moderate': [{'drug': 'ACE inhibitor, ARB', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Digoxin', 'mechanism': 'Giảm thải trừ digoxin qua thận',
        'effect':
        'Tăng nồng độ digoxin, tăng nguy cơ độc tính (nhịp tim chậm, block nhĩ thất)'
        , 'management':
        'Theo dõi digoxin máu thường xuyên. Có thể cần giảm liều digoxin'}, {
        'drug': 'Methotrexate', 'mechanism':
        'Giảm thải trừ methotrexate qua thận', 'effect':
        'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }, {'drug': 'Cyclosporine', 'mechanism': 'Tăng nguy cơ độc tính thận',
        'effect': 'Tăng nguy cơ suy thận cấp', 'management':
        'Theo dõi creatinine, BUN chặt chẽ. Cân nhắc NSAID khác hoặc giảm liều cyclosporine'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng diclofenac hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy gan nặng (do nguy cơ tăng men gan cao)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'], 'tương_đối':
        ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan trung bình - thận trọng, theo dõi men gan chặt chẽ',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ, đặc biệt chảy máu dạ dày']
        }, 'pregnancy_lactation': {'fda_category':
        'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Diclofenac bài tiết vào sữa mẹ ở nồng độ rất thấp (<0.1% liều mẹ). An toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dạng bôi tại chỗ: ít ảnh hưởng hệ thống, an toàn hơn.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi nhưng theo dõi men gan',
        'moderate': 'Thận trọng, giảm liều 25-50%, theo dõi men gan chặt chẽ',
        'severe': 'TRÁNH DÙNG (chống chỉ định)', 'notes':
        'Diclofenac chuyển hóa ở gan qua CYP2C9 và CYP3A4. Có nguy cơ tăng men gan cao hơn các NSAID khác. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính gan.'
        }, 'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ', 'Hạ huyết áp',
        'Suy thận cấp', 'Chảy máu dạ dày', 'Tăng men gan (ALT, AST)',
        'Co giật (hiếm)'], 'antidote': 'Không có antidote đặc hiệu',
        'treatment': ['Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi chức năng gan (ALT, AST) - diclofenac có nguy cơ cao',
        'Theo dõi huyết áp, nhịp tim', 'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, ALT/AST, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 12-24 giờ'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày (quan trọng với diclofenac do nguy cơ cao)'
        , 'timing':
        'Mỗi 8-12 giờ. Dùng với bữa ăn để giảm tác dụng phụ dạ dày.'}, 'im': {
        'notes':
        'Tiêm bắp sâu. Chỉ dùng tối đa 3 ngày, không dùng lâu dài. Có thể gây đau tại chỗ tiêm.'
        }, 'topical': {'notes':
        'Dạng bôi tại chỗ: Bôi 2-4g x 3-4 lần/ngày lên vùng đau. Ít tác dụng phụ hệ thống hơn dạng uống. Không bôi trên vùng da bị tổn thương hoặc niêm mạc.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Voltaren (diclofenac)',
        'UpToDate - Diclofenac: Drug information',
        'Lexicomp - Diclofenac monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-06', 'evidence_level':
        'High - FDA-approved, extensive clinical data'}},
    "Meloxicam": {'group': 'Analgesic - NSAID', 'vietnamese_name': 'Meloxicam, Mobic',
        'administration': ['PO'], 'indications': ['Đau nhẹ đến trung bình',
        'Viêm khớp dạng thấp', 'Viêm khớp xương khớp', 'Đau bụng kinh'],
        'contraindications': ['Loét dạ dày tá tràng đang hoạt động',
        'Suy thận nặng', 'Suy gan nặng', 'Có thai (3 tháng cuối)',
        'Dị ứng NSAID/aspirin'], 'dosage': {'adult_po':
        '7.5-15mg x 1 lần/ngày', 'notes':
        'COX-2 selective, ít tác dụng phụ dạ dày hơn NSAID không chọn lọc. Uống với thức ăn'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, giảm liều', 'under_30': 'Tránh dùng'}, 'side_effects': [
        'Chảy máu dạ dày (ít hơn NSAID không chọn lọc)', 'Suy thận', 'Tăng huyết áp',
        'Phù', 'Đau đầu', 'Ban da', 'Nhạy cảm với ánh sáng'], 'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Methotrexate: tăng độc tính methotrexate'], 'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế chọn lọc enzyme cyclooxygenase-2 (COX-2) hơn COX-1, giảm tổng hợp prostaglandin gây viêm (từ COX-2) nhưng ít ảnh hưởng đến prostaglandin bảo vệ dạ dày (từ COX-1). Do đó, meloxicam có ít tác dụng phụ dạ dày hơn NSAID không chọn lọc (như ibuprofen, naproxen). Tác dụng kháng viêm và giảm đau. Thời gian bán thải dài (15-20 giờ) → có thể dùng 1 lần/ngày.',
        'monitoring': [
        'Dấu hiệu chảy máu dạ dày (ít hơn NSAID không chọn lọc nhưng vẫn có)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)'], 'precautions': [
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'COX-2 selective → ít tác dụng phụ dạ dày hơn NSAID không chọn lọc, nhưng vẫn có nguy cơ',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Thời gian bán thải dài → tích lũy ở bệnh nhân suy thận, suy gan'], 'pharmacokinetics': {
        'half_life': '15-20 giờ (dài)', 'onset': '30-60 phút', 'duration': '24 giờ',
        'protein_binding': '99%', 'clearance':
        'Gan (chuyển hóa qua CYP2C9, CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Không dùng trong 3 tháng cuối thai kỳ - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi. NSAID có thể gây tăng nguy cơ nhồi máu cơ tim và đột quỵ, đặc biệt khi dùng lâu dài hoặc liều cao.',
        'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu', 'effect':
        'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }], 'moderate': [{'drug': 'ACE inhibitor, ARB', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Methotrexate', 'mechanism': 'Giảm thải trừ methotrexate qua thận',
        'effect': 'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng meloxicam hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'], 'tương_đối': [
        'Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ']}, 'pregnancy_lactation': {
        'fda_category': 'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.',
        'lactation': {'safety': 'Compatible', 'details':
        'Meloxicam bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <1% liều mẹ. An toàn cho trẻ bú mẹ.',
        'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn. Theo dõi trẻ về dấu hiệu bất thường (hiếm).'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Meloxicam chuyển hóa ở gan qua CYP2C9 và CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, meloxicam ít gây độc gan hơn một số NSAID khác.'},
        'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ', 'Hạ huyết áp', 'Suy thận cấp',
        'Chảy máu dạ dày', 'Co giật (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 24-48 giờ do half-life dài (15-20 giờ)'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        '1 lần/ngày (do half-life dài). Có thể dùng vào buổi sáng hoặc tối. Dùng với bữa ăn để giảm tác dụng phụ dạ dày.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'}},
        'references': {'primary_sources': [
        'FDA Drug Label - Mobic (meloxicam)',
        'UpToDate - Meloxicam: Drug information',
        'Lexicomp - Meloxicam monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05', 'evidence_level':
        'High - FDA-approved, extensive clinical data'}},
    "Celecoxib": {'group': 'Analgesic - NSAID (COX-2 Selective)', 'vietnamese_name':
        'Celecoxib, Celebrex', 'administration': ['PO'], 'indications': [
        'Đau nhẹ đến trung bình', 'Viêm khớp dạng thấp', 'Viêm khớp xương khớp',
        'Đau bụng kinh', 'Đau cấp tính'], 'contraindications': [
        'Dị ứng celecoxib, sulfonamides', 'Loét dạ dày tá tràng đang hoạt động',
        'Suy thận nặng', 'Suy gan nặng', 'Có thai (3 tháng cuối)',
        'Bệnh tim mạch nặng'], 'dosage': {'adult_po':
        '100-200mg x 1-2 lần/ngày (tối đa 400mg/ngày)', 'notes':
        'COX-2 selective, ít tác dụng phụ dạ dày nhất. Tăng nguy cơ tim mạch'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, giảm liều', 'under_30': 'Tránh dùng'}, 'side_effects': [
        'Tăng nguy cơ nhồi máu cơ tim, đột quỵ (cao hơn NSAID khác)',
        'Chảy máu dạ dày (ít hơn NSAID không chọn lọc)', 'Suy thận', 'Tăng huyết áp',
        'Phù', 'Đau đầu', 'Ban da'], 'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Fluconazole: tăng nồng độ celecoxib (ức chế CYP2C9)',
        'Methotrexate: tăng độc tính methotrexate'], 'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế chọn lọc mạnh enzyme cyclooxygenase-2 (COX-2), ít ảnh hưởng đến COX-1. Giảm tổng hợp prostaglandin gây viêm (từ COX-2) nhưng ít ảnh hưởng đến prostaglandin bảo vệ dạ dày và chống kết tập tiểu cầu (từ COX-1). Do đó, celecoxib có ít tác dụng phụ dạ dày nhất trong các NSAID, nhưng tăng nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ) do giảm prostacyclin (bảo vệ tim mạch) từ COX-2. Tác dụng kháng viêm và giảm đau.',
        'monitoring': [
        'Dấu hiệu biến cố tim mạch (đau ngực, khó thở, đột quỵ) - nguy cơ cao hơn NSAID khác',
        'Dấu hiệu chảy máu dạ dày (ít hơn NSAID không chọn lọc nhưng vẫn có)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)'], 'precautions': [
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'COX-2 selective → ít tác dụng phụ dạ dày nhất, nhưng TĂNG NGUY CƠ TIM MẠCH',
        'CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh tim mạch nặng, tiền sử nhồi máu cơ tim, đột quỵ',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Tương tác với fluconazole (tăng nồng độ celecoxib)'], 'pharmacokinetics': {
        'half_life': '11 giờ', 'onset': '30-60 phút', 'duration': '12-24 giờ',
        'protein_binding': '97%', 'clearance':
        'Gan (chuyển hóa qua CYP2C9), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Tăng nguy cơ nhồi máu cơ tim và đột quỵ nghiêm trọng, có thể tử vong. Nguy cơ tăng khi dùng lâu dài hoặc liều cao. CHỐNG CHỈ ĐỊNH ở bệnh nhân có bệnh tim mạch nặng, tiền sử nhồi máu cơ tim, đột quỵ. Không dùng trong 3 tháng cuối thai kỳ.',
        'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Celecoxib ức chế COX-2, có thể tăng nguy cơ chảy máu', 'effect':
        'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }, {'drug': 'Fluconazole, các thuốc ức chế CYP2C9', 'mechanism':
        'Ức chế chuyển hóa celecoxib qua CYP2C9', 'effect':
        'Tăng nồng độ celecoxib, tăng nguy cơ tác dụng phụ', 'management':
        'Giảm liều celecoxib 50% khi dùng với fluconazole. Theo dõi tác dụng phụ.'}],
        'moderate': [{'drug': 'ACE inhibitor, ARB', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng NSAID nếu có dấu hiệu suy thận'
        }, {'drug': 'Methotrexate', 'mechanism': 'Giảm thải trừ methotrexate qua thận',
        'effect': 'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng celecoxib, sulfonamides (celecoxib chứa nhóm sulfonamide)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Bệnh tim mạch nặng, tiền sử nhồi máu cơ tim, đột quỵ - CHỐNG CHỈ ĐỊNH do tăng nguy cơ biến cố tim mạch'
        , 'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'], 'tương_đối': [
        'Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ, đặc biệt biến cố tim mạch']},
        'pregnancy_lactation': {'fda_category': 'C - D trong tam cá nguyệt 3',
        'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.',
        'lactation': {'safety': 'Compatible', 'details':
        'Celecoxib bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <1% liều mẹ. An toàn cho trẻ bú mẹ.',
        'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn. Theo dõi trẻ về dấu hiệu bất thường (hiếm).'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Celecoxib chuyển hóa ở gan qua CYP2C9. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tương tác với fluconazole (ức chế CYP2C9) làm tăng nồng độ celecoxib.'},
        'overdose_management': {'symptoms': ['Buồn nôn, nôn, đau bụng',
        'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ', 'Hạ huyết áp', 'Suy thận cấp',
        'Chảy máu dạ dày', 'Biến cố tim mạch (đau ngực, khó thở)', 'Co giật (hiếm)'],
        'antidote': 'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim, ECG (nguy cơ biến cố tim mạch)',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ECG, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu, dấu hiệu biến cố tim mạch. Theo dõi ít nhất 24 giờ do half-life (11 giờ)'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        '1-2 lần/ngày. Có thể dùng vào buổi sáng và tối. Dùng với bữa ăn để giảm tác dụng phụ dạ dày. Liều tối đa: 400mg/ngày.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'}},
        'references': {'primary_sources': [
        'FDA Drug Label - Celebrex (celecoxib)',
        'UpToDate - Celecoxib: Drug information',
        'Lexicomp - Celecoxib monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05', 'evidence_level':
        'High - FDA-approved, extensive clinical data'}},
    "Ketorolac": {'group': 'Analgesic - NSAID', 'vietnamese_name':
        'Ketorolac, Toradol', 'administration': ['PO', 'IV', 'IM'], 'indications': [
        'Đau cấp tính vừa đến nặng (ngắn hạn)', 'Đau sau phẫu thuật',
        'Đau do chấn thương', 'Đau bụng kinh nặng'], 'contraindications': [
        'Loét dạ dày tá tràng đang hoạt động', 'Suy thận nặng', 'Suy gan nặng',
        'Có thai (3 tháng cuối)', 'Dị ứng NSAID/aspirin', 'Suy tim nặng',
        'Chảy máu đang hoạt động', 'Dùng lâu dài (>5 ngày)'], 'dosage': {
        'adult_iv_im': '30mg IV/IM mỗi 6 giờ (tối đa 120mg/ngày, tối đa 5 ngày)',
        'adult_po': '10mg PO mỗi 4-6 giờ (tối đa 40mg/ngày, tối đa 5 ngày)',
        'adult_loading': '60mg IM x 1, sau đó 30mg mỗi 6 giờ', 'notes':
        'CHỈ dùng ngắn hạn (≤5 ngày). Tác dụng giảm đau mạnh, tương đương opioid nhẹ. Nguy cơ chảy máu cao hơn NSAID khác.'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Giảm liều 50%', 'under_30': 'CHỐNG CHỈ ĐỊNH'}, 'side_effects': [
        'Chảy máu dạ dày (nguy cơ cao, đặc biệt khi dùng >5 ngày)',
        'Chảy máu nói chung (tăng nguy cơ)', 'Suy thận cấp (nguy cơ cao)',
        'Tăng huyết áp', 'Phù', 'Đau đầu', 'Ban da', 'Buồn nôn, nôn'], 'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng (đặc biệt nguy hiểm)',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Methotrexate: tăng độc tính methotrexate',
        'Probenecid: tăng nồng độ ketorolac'], 'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), giảm tổng hợp prostaglandin, thromboxane, và prostacyclin. Ketorolac có tác dụng giảm đau mạnh, tương đương opioid nhẹ (như morphine 10mg), nhưng không gây nghiện và không ức chế hô hấp. Tuy nhiên, ketorolac có nguy cơ chảy máu và suy thận cao hơn các NSAID khác, đặc biệt khi dùng >5 ngày. CHỈ dùng ngắn hạn (≤5 ngày) cho đau cấp tính.',
        'monitoring': [
        'Dấu hiệu chảy máu (dạ dày, niêm mạc, chảy máu nói chung) - nguy cơ cao, đặc biệt khi dùng >5 ngày'
        , 'Creatinine, BUN mỗi ngày nếu dùng >2 ngày (nguy cơ suy thận cấp cao)',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Chức năng gan (transaminase) nếu dùng lâu dài',
        'Dấu hiệu suy tim (giữ nước, phù)',
        'Công thức máu (CBC) nếu có dấu hiệu chảy máu'], 'precautions': [
        'CHỈ dùng ngắn hạn (≤5 ngày) - CHỐNG CHỈ ĐỊNH dùng lâu dài',
        'Nguy cơ chảy máu cao hơn NSAID khác - tránh dùng ở bệnh nhân có nguy cơ chảy máu',
        'Nguy cơ suy thận cấp cao - tránh dùng ở bệnh nhân suy thận, mất nước',
        'Tránh dùng với warfarin (tăng nguy cơ chảy máu nặng)',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm)',
        'Ngừng trước phẫu thuật 5-7 ngày (tăng nguy cơ chảy máu)',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
        'Theo dõi chức năng thận mỗi ngày nếu dùng >2 ngày',
        'IV/IM: chuyển sang PO sớm nhất có thể'], 'pharmacokinetics': {
        'half_life': '2.5-8 giờ', 'onset': '10-30 phút (IV/IM), 30-60 phút (PO)',
        'duration': '4-6 giờ', 'protein_binding': '99%', 'clearance':
        'Gan (chuyển hóa qua CYP2C9, glucuronidation), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng IV/IM: bảo quản ở nhiệt độ phòng, không đông lạnh.',
        'black_box_warnings':
        'CHỈ dùng ngắn hạn (≤5 ngày). CHỐNG CHỈ ĐỊNH dùng lâu dài. Tăng nguy cơ chảy máu nghiêm trọng (dạ dày, niêm mạc, chảy máu nói chung), đặc biệt khi dùng >5 ngày. Tăng nguy cơ suy thận cấp, đặc biệt ở bệnh nhân suy thận, mất nước, dùng ACE inhibitor/ARB. Không dùng trong 3 tháng cuối thai kỳ.',
        'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-1, giảm tổng hợp thromboxane, tăng nguy cơ chảy máu', 'effect':
        'Tăng nguy cơ chảy máu nặng, tăng INR (đặc biệt nguy hiểm với ketorolac)',
        'management':
        'CHỐNG CHỈ ĐỊNH dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần. Cân nhắc dùng thuốc giảm đau khác.'
        }, {'drug': 'Probenecid', 'mechanism': 'Giảm thải trừ ketorolac qua thận',
        'effect': 'Tăng nồng độ ketorolac, tăng nguy cơ tác dụng phụ', 'management':
        'Giảm liều ketorolac 50% khi dùng với probenecid. Theo dõi tác dụng phụ.'}],
        'moderate': [{'drug': 'ACE inhibitor, ARB', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp (đặc biệt cao với ketorolac)',
        'management':
        'Thận trọng. Tránh dùng nếu có thể. Theo dõi creatinine, BUN mỗi ngày. Cân nhắc ngừng ketorolac nếu có dấu hiệu suy thận'
        }, {'drug': 'Methotrexate', 'mechanism': 'Giảm thải trừ methotrexate qua thận',
        'effect': 'Tăng độc tính methotrexate (giảm bạch cầu, suy tủy)', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, giảm liều methotrexate và theo dõi công thức máu chặt chẽ'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng ketorolac hoặc NSAID/aspirin (phản vệ, hen suyễn do aspirin)',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH',
        'Chảy máu đang hoạt động - CHỐNG CHỈ ĐỊNH',
        'Dùng lâu dài (>5 ngày) - CHỐNG CHỈ ĐỊNH',
        'Dùng với warfarin hoặc thuốc chống đông - CHỐNG CHỈ ĐỊNH (nguy cơ chảy máu nặng)'
        ], 'tương_đối': [
        'Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều 50%, theo dõi chặt chẽ',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Mất nước - tăng nguy cơ suy thận cấp',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Người cao tuổi - tăng nguy cơ tác dụng phụ, đặc biệt chảy máu và suy thận',
        'Dùng >2 ngày - tăng nguy cơ chảy máu và suy thận']}, 'pregnancy_lactation': {
        'fda_category': 'C - D trong tam cá nguyệt 3', 'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ, nhưng chỉ dùng ngắn hạn (≤5 ngày). Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi, tăng áp lực động mạch phổi ở trẻ sơ sinh. Tránh dùng trong 3 tháng cuối.',
        'lactation': {'safety': 'Compatible with caution', 'details':
        'Ketorolac bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ <0.4% liều mẹ. Tuy nhiên, do nguy cơ chảy máu và suy thận cao, nên thận trọng khi dùng khi cho con bú.',
        'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn (≤5 ngày), nhưng thận trọng. Theo dõi trẻ về dấu hiệu bất thường.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Ketorolac chuyển hóa ở gan qua CYP2C9 và glucuronidation. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ketorolac ít gây độc gan trực tiếp hơn một số NSAID khác.'},
        'overdose_management': {'symptoms': ['Chảy máu dạ dày nặng (triệu chứng chính)',
        'Chảy máu nói chung (niêm mạc, chảy máu nội tạng)', 'Suy thận cấp nặng',
        'Buồn nôn, nôn, đau bụng', 'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ',
        'Hạ huyết áp', 'Co giật (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Ngừng ngay ketorolac',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN) mỗi ngày - nguy cơ suy thận cấp cao',
        'Theo dõi dấu hiệu chảy máu chặt chẽ (dạ dày, niêm mạc, chảy máu nói chung)',
        'Theo dõi huyết áp, nhịp tim',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Điều trị chảy máu nếu có (truyền máu, điều trị hỗ trợ)',
        'Điều trị hỗ trợ triệu chứng'], 'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN (mỗi ngày), công thức máu, dấu hiệu chảy máu (dạ dày, niêm mạc, chảy máu nói chung). Theo dõi ít nhất 24-48 giờ do nguy cơ chảy máu và suy thận cao.'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        'Mỗi 4-6 giờ. CHỈ dùng tối đa 5 ngày. Dùng với bữa ăn để giảm tác dụng phụ dạ dày. Liều tối đa: 40mg/ngày (PO).'
        }, 'iv': {'reconstitution':
        'Ketorolac IV: 30mg pha với 50-100ml NaCl 0.9% hoặc dextrose 5%', 'infusion_rate':
        'Truyền trong 15-30 phút', 'compatibility': ['NaCl 0.9%', 'Dextrose 5%'],
        'incompatibility': ['Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'CHỈ dùng tối đa 5 ngày. Chuyển sang PO sớm nhất có thể. Theo dõi chức năng thận mỗi ngày. Liều tối đa: 120mg/ngày (IV/IM).'
        }, 'im': {'notes':
        'Tiêm bắp sâu. CHỈ dùng tối đa 5 ngày. Chuyển sang PO sớm nhất có thể. Theo dõi chức năng thận mỗi ngày. Liều tối đa: 120mg/ngày (IV/IM).'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Toradol (ketorolac)',
        'UpToDate - Ketorolac: Drug information',
        'Lexicomp - Ketorolac monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05',         'evidence_level':
        'High - FDA-approved, extensive clinical data'}},
    "Etoricoxib": {'group': 'Analgesic - NSAID (COX-2 Selective)',
        'vietnamese_name': 'Etoricoxib, Arcoxia', 'administration': ['PO'],
        'indications': ['Đau nhẹ đến trung bình', 'Viêm khớp', 'Đau bụng kinh',
        'Gout cấp'], 'contraindications': [
        'Loét dạ dày tá tràng đang hoạt động', 'Suy thận nặng', 'Suy gan nặng',
        'Có thai (3 tháng cuối)', 'Dị ứng NSAID/aspirin',
        'Bệnh tim mạch nặng'], 'dosage': {
        'adult_pain': '60-90mg x 1 lần/ngày',
        'adult_arthritis': '60-90mg x 1 lần/ngày',
        'adult_gout': '120mg x 1 lần/ngày (tối đa 5 ngày)',
        'adult_max': '120mg/ngày', 'notes':
        'COX-2 selective, ít tác dụng phụ dạ dày hơn NSAID không chọn lọc. Dùng 1 lần/ngày.'
        }, 'side_effects': [
        'Tăng nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ)',
        'Tăng huyết áp', 'Phù', 'Suy thận', 'Chóng mặt', 'Đau đầu',
        'Ít tác dụng phụ dạ dày hơn NSAID không chọn lọc'], 'interactions': [
        'Warfarin: tăng nguy cơ chảy máu nặng',
        'ACE inhibitor: giảm hiệu quả, tăng nguy cơ suy thận',
        'Lithium: tăng nồng độ lithium',
        'Methotrexate: tăng độc tính methotrexate'], 'pregnancy':
        'C - D trong 3 tháng cuối', 'mechanism_of_action':
        'Ức chế chọn lọc enzyme cyclooxygenase-2 (COX-2), giảm tổng hợp prostaglandin gây viêm và đau. Ít ức chế COX-1 (enzyme bảo vệ niêm mạc dạ dày) nên ít tác dụng phụ dạ dày hơn NSAID không chọn lọc. Tuy nhiên, vẫn có nguy cơ biến cố tim mạch (nhồi máu cơ tim, đột quỵ) tương tự các COX-2 selective khác. Dùng 1 lần/ngày, tiện lợi.'
        , 'monitoring': [
        'Dấu hiệu biến cố tim mạch (đau ngực, khó thở, yếu một bên)',
        'Huyết áp (NSAID có thể tăng huyết áp)',
        'Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ',
        'Dấu hiệu suy tim (giữ nước, phù)',
        'INR nếu dùng với warfarin'], 'precautions': [
        'Tăng nguy cơ biến cố tim mạch - không dùng ở bệnh nhân có bệnh tim mạch nặng',
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày',
        'Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp',
        'Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả, tăng nguy cơ suy thận)',
        'Không dùng trong 3 tháng cuối thai kỳ',
        'Theo dõi INR nếu dùng với warfarin',
        'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể'], 'pharmacokinetics': {
        'half_life': '22 giờ (dài)', 'onset': '30-60 phút', 'duration':
        '24 giờ (dài, dùng 1 lần/ngày)', 'protein_binding': '92%', 'clearance':
        'Gan (chuyển hóa qua CYP3A4, CYP2C9, CYP2D6), thận (thải trừ)'}, 'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Thận trọng, giảm liều 25-50%', 'under_30':
        'Tránh dùng hoặc giảm liều mạnh. Theo dõi chức năng thận chặt chẽ'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        'Tăng nguy cơ biến cố tim mạch nghiêm trọng (nhồi máu cơ tim, đột quỵ) - có thể tử vong. Nguy cơ tăng ở bệnh nhân có bệnh tim mạch. Không dùng trong 3 tháng cuối thai kỳ.'
        , 'drug_interactions': {'major': [{'drug':
        'Warfarin, các thuốc chống đông khác', 'mechanism':
        'Ức chế COX-2, tăng nguy cơ chảy máu', 'effect':
        'Tăng nguy cơ chảy máu nặng, tăng INR', 'management':
        'Tránh dùng đồng thời. Nếu phải dùng, theo dõi INR thường xuyên, giảm liều warfarin nếu cần'
        }], 'moderate': [{'drug': 'ACE inhibitor, ARB', 'mechanism':
        'Giảm tổng hợp prostaglandin ở thận, giảm lưu lượng máu thận', 'effect':
        'Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp', 'management':
        'Thận trọng. Theo dõi creatinine, BUN. Cân nhắc ngừng etoricoxib nếu có dấu hiệu suy thận'
        }, {'drug': 'Lithium', 'mechanism': 'Giảm thải trừ lithium qua thận',
        'effect': 'Tăng nồng độ lithium, tăng độc tính', 'management':
        'Theo dõi nồng độ lithium. Có thể cần giảm liều lithium.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng etoricoxib hoặc NSAID/aspirin',
        'Loét dạ dày tá tràng đang hoạt động',
        'Tam cá nguyệt 3 thai kỳ (3 tháng cuối)',
        'Bệnh tim mạch nặng (nhồi máu cơ tim gần đây, suy tim nặng)',
        'Suy thận nặng (CrCl <30) và đang dùng ACE inhibitor/ARB'], 'tương_đối':
        ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều',
        'Suy gan nặng - thận trọng, giảm liều',
        'Suy tim nặng - tăng nguy cơ giữ nước, suy tim nặng hơn',
        'Bệnh mạch vành, tiền sử nhồi máu cơ tim - tăng nguy cơ biến cố tim mạch',
        'Tăng huyết áp không kiểm soát - NSAID có thể tăng huyết áp',
        'Dùng warfarin hoặc thuốc chống đông - tăng nguy cơ chảy máu']},
        'pregnancy_lactation': {'fda_category': 'C - D trong tam cá nguyệt 3',
        'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ. Tam cá nguyệt 3: CHỐNG CHỈ ĐỊNH - có thể gây đóng ống động mạch sớm, thiểu ối, suy thận thai nhi.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Etoricoxib bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với liều ngắn hạn.'}}, 'hepatic_adjustment': {
        'mild': 'Không đổi', 'moderate': 'Thận trọng, giảm liều 25-50%', 'severe':
        'Tránh dùng hoặc giảm liều mạnh', 'notes':
        'Etoricoxib chuyển hóa ở gan qua CYP3A4, CYP2C9, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.'
        }, 'overdose_management': {'symptoms': [
        'Buồn nôn, nôn, đau bụng', 'Chóng mặt, nhức đầu', 'Lú lẫn, buồn ngủ',
        'Hạ huyết áp', 'Suy thận cấp', 'Chảy máu dạ dày'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi chức năng thận (creatinine, BUN), điện giải',
        'Theo dõi huyết áp, nhịp tim',
        'Truyền dịch nếu hạ huyết áp, suy thận',
        'Theo dõi dấu hiệu chảy máu dạ dày', 'Điều trị hỗ trợ triệu chứng'],
        'monitoring':
        'Huyết áp, nhịp tim, ý thức, creatinine, BUN, điện giải, dấu hiệu chảy máu. Theo dõi ít nhất 24 giờ do half-life dài (22 giờ).'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày', 'timing':
        'Dùng 1 lần/ngày (tiện lợi). Liều tối đa: 120mg/ngày.'}, 'iv': None},
        'references': {'primary_sources': [
        'FDA Drug Label - Arcoxia (Etoricoxib)',
        'UpToDate - Etoricoxib: Drug information'], 'last_updated': '2025-02-05',
        'evidence_level': 'High - FDA approved'}}}

__all__ = ['NSAIDS_DRUGS']
