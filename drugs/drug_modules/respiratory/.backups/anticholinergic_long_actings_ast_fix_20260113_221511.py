"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Anticholinergic (Long-acting)s

ANTICHOLINERGIC_LONG_ACTINGS_DRUGS = {
    "Aclidinium": {'group': 'Respiratory - Anticholinergic (Long-acting)',
        'vietnamese_name': 'Aclidinium, Tudorza Pressair', 'administration': [
        'Inhalation (DPI)'],
        'indications': [
        'COPD (phòng ngừa, đơn trị hoặc kết hợp với formoterol)'],
        'contraindications': ['Dị ứng atropine/aclidinium', 'Glaucoma góc đóng',
        'Tăng nhãn áp', 'Phì đại tuyến tiền liệt nặng'],
        'dosage': {
        'adult_inhalation': '400mcg x 2 lần/ngày (sáng và tối)', 'notes':
        'Tác dụng kéo dài 12 giờ. Dùng 2 lần/ngày (khác tiotropium dùng 1 lần/ngày)'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Thận trọng'},
        'side_effects': [
        'Khô miệng (thường gặp)', 'Ho', 'Nhiễm trùng đường hô hấp trên',
        'Táo bón', 'Bí tiểu', 'Kích ứng mắt (nếu vào mắt)'],
        'interactions': [
        'Anticholinergic khác: tăng tác dụng phụ', 'Beta-agonist: hiệp đồng'],pregnancy': 'C', 'mechanism_of_action':
        'Anticholinergic dài tác dụng - ức chế muscarinic receptors (M1, M2, M3) ở cơ trơn phế quản, giảm acetylcholine-mediated co thắt phế quản. Giãn cơ trơn phế quản, giảm tiết dịch đường hô hấp. Tác dụng kéo dài 12 giờ (ngắn hơn tiotropium 24 giờ). Không hấp thu hệ thống đáng kể khi dùng dạng hít (do ion hóa) → ít tác dụng phụ hệ thống. Thường dùng kết hợp với formoterol (LABA) trong fixed-dose combination (Duaklir). An toàn hơn beta-agonist cho bệnh nhân tim mạch.'
        , 'monitoring': [
        'Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa',
        'Nhịp tim, huyết áp (ít tác dụng tim mạch hơn beta-agonist)',
        'Dấu hiệu kích ứng mắt (nếu vào mắt - tăng nhãn áp, đỏ mắt)',
        'Dấu hiệu tăng nhãn áp (đau mắt, nhìn mờ) - đặc biệt ở bệnh nhân glaucoma',
        'Dấu hiệu bí tiểu (khó tiểu, đầy bụng) - đặc biệt ở bệnh nhân phì đại tuyến tiền liệt'
        , 'Dấu hiệu khô miệng nặng (có thể ảnh hưởng sức khỏe răng miệng)'],
        'precautions': [
        'Rửa miệng sau khi dùng để giảm kích ứng và tránh thuốc vào mắt',
        'Tránh để thuốc vào mắt (có thể gây tăng nhãn áp, đặc biệt ở bệnh nhân glaucoma)'
        'Thận trọng ở bệnh nhân glaucoma góc đóng (chống chỉ định) hoặc tăng nhãn áp'
        'Thận trọng ở bệnh nhân phì đại tuyến tiền liệt nặng (có thể gây bí tiểu)',
        'Dùng 2 lần/ngày (sáng và tối), khác tiotropium dùng 1 lần/ngày',
        'Dạng hít: sử dụng đúng kỹ thuật để đạt hiệu quả tối đa',
        'An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích tim)',
        'Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn',
        'Có thể dùng kết hợp với formoterol (LABA) trong fixed-dose combination'],
        'pharmacokinetics': {'half_life': '5-8 giờ', 'onset': '15-30 phút',
        'duration': '12 giờ (ngắn hơn tiotropium 24 giờ)', 'protein_binding': 'N/A',
        'clearance': 'Thận (thải qua thận, ít tích lũy hơn tiotropium)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. DPI: bảo quản trong bao bì gốc. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings':
        'Tránh để thuốc vào mắt - có thể gây tăng nhãn áp, đặc biệt nguy hiểm ở bệnh nhân glaucoma góc đóng. Rửa miệng sau khi dùng để tránh thuốc vào mắt.'
        , 'drug_interactions': {'major': [],moderate': [{'drug':
        'Anticholinergic khác (Atropine, Scopolamine, Benztropine, Oxybutynin, Ipratropium, Tiotropium)'
        , 'mechanism':
        'Tăng tác dụng anticholinergic, tăng tác dụng phụ anticholinergic',
        'effect': 'Tăng khô miệng, bí tiểu, táo bón, tăng nhãn áp, nhìn mờ',
        'management':
        'Thận trọng khi dùng cùng. Theo dõi tác dụng phụ anticholinergic. Có thể cần giảm liều hoặc tránh dùng cùng.'
        }],
        'moderate': [{'drug': 'Beta-2 agonists (SABA, LABA)', 'mechanism': 'Hiệp đồng tác dụng giãn phế quản', 'effect':
        'Tăng hiệu quả giãn phế quản (tác dụng tích cực)', 'management':
        'Có thể dùng kết hợp để tăng hiệu quả. Không cần điều chỉnh liều.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng với aclidinium, atropine hoặc các thành phần khác',
        'Glaucoma góc đóng (chống chỉ định tuyệt đối)',
        'Tăng nhãn áp nặng không kiểm soát'],
        'tương_đối': [
        'Glaucoma góc mở - thận trọng, theo dõi nhãn áp',
        'Tăng nhãn áp nhẹ - thận trọng, tránh để thuốc vào mắt',
        'Phì đại tuyến tiền liệt nặng - có thể gây bí tiểu',
        'Bí tiểu - có thể làm nặng', 'Táo bón nặng - có thể làm nặng',
        'Suy thận trung bình (CrCl 30-60 ml/min) - thận trọng, theo dõi tác dụng phụ'
        , 'Nhược cơ - có thể làm nặng',
        'Dùng với anticholinergic khác - tăng tác dụng phụ']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Aclidinium là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Aclidinium được sử dụng trong thai kỳ để điều trị COPD và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do ion hóa), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Aclidinium bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi', 'notes':
        'Aclidinium không chuyển hóa đáng kể ở gan. Hấp thu toàn thân tối thiểu từ dạng hít. Không cần điều chỉnh liều ở suy gan.'
        },overdose_management': {'symptoms': ['Khô miệng nặng', 'Bí tiểu',
        'Táo bón nặng', 'Tăng nhãn áp (nếu vào mắt)', 'Nhìn mờ',
        'Đỏ mắt, đau mắt', 'Nhịp tim nhanh (hiếm, nếu hấp thu toàn thân)',
        'Kích động, lú lẫn (hiếm)'],antidote':
        'Không có antidote đặc hiệu. Physostigmine (cholinergic) có thể được dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân, nhưng thận trọng và chỉ dùng trong môi trường có hỗ trợ hô hấp.'
        , 'treatment': ['Ngừng ngay aclidinium',
        'Rửa mắt ngay nếu thuốc vào mắt (dùng nước sạch hoặc nước muối sinh lý)',
        'Điều trị tăng nhãn áp nếu có (dùng thuốc nhỏ mắt chống tăng nhãn áp, khám bác sĩ mắt)'
        , 'Hỗ trợ bí tiểu nếu cần (đặt ống thông tiểu)',
        'Điều trị táo bón nếu cần (thuốc nhuận tràng, thụt tháo)',
        'Theo dõi nhãn áp nếu có triệu chứng mắt',
        'Theo dõi nhịp tim, huyết áp nếu có triệu chứng toàn thân',
        'Hỗ trợ hô hấp nếu cần (hiếm)',
        'Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (thận trọng, có hỗ trợ hô hấp)'
        ],
        'monitoring':
        'Theo dõi: nhãn áp (nếu có triệu chứng mắt), nhịp tim, huyết áp, tình trạng bí tiểu, táo bón. Theo dõi ít nhất 12-24 giờ.'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Physostigmine', 'mechanism':
        'Ức chế acetylcholinesterase, tăng acetylcholine, đối kháng tác dụng anticholinergic'
        , 'indication':
        'Quá liều nghiêm trọng với tác dụng toàn thân (hiếm với aclidinium dạng hít)'
        , 'caution':
        'Thận trọng, chỉ dùng trong môi trường có hỗ trợ hô hấp. Có thể gây co thắt phế quản, tăng tiết dịch, co giật. Chỉ dùng khi quá liều nghiêm trọng với tác dụng toàn thân.'
        }],notes':
        'Không có antidote đặc hiệu cho aclidinium. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (rất hiếm với dạng hít).'
        },administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dùng dạng hít DPI (Pressair). Mở nắp, nhấn nút để nạp thuốc, hít sâu và giữ hơi thở 10 giây. Dùng 2 lần/ngày (400mcg mỗi lần).'
        , 'timing': 'Dùng 2 lần/ngày (sáng và tối), cách nhau khoảng 12 giờ.',
        'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và QUAN TRỌNG: tránh thuốc vào mắt (có thể gây tăng nhãn áp).'
        , 'notes':
        'Tránh để thuốc vào mắt - rửa tay sau khi dùng. Nếu thuốc vào mắt, rửa ngay bằng nước sạch. Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn. Có thể dùng kết hợp với formoterol (LABA) trong fixed-dose combination (Duaklir).'
        }},references': {'primary_sources': [
        'FDA Label: Tudorza Pressair (Aclidinium)',
        'UpToDate: Long-acting anticholinergic bronchodilators in COPD',
        'GOLD Guidelines 2024: COPD Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Aclidinium'],evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'
        }},
    "Glycopyrronium": {'group': 'Respiratory - Anticholinergic (Long-acting)',
        'vietnamese_name': 'Glycopyrronium, Glycopyrrolate, Seebri Breezhaler',
        'administration': ['Inhalation (DPI)'],
        'indications': [
        'COPD (phòng ngừa, kết hợp với indacaterol)'],
        'contraindications': ['Dị ứng atropine/glycopyrronium', 'Glaucoma góc đóng',
        'Tăng nhãn áp', 'Phì đại tuyến tiền liệt nặng'],
        'dosage': {
        'adult_inhalation': '50mcg x 1 lần/ngày (kết hợp với indacaterol)',
        'notes':
        'Tác dụng kéo dài 24 giờ. Chỉ có dạng fixed-dose combination với indacaterol (Ultibro Breezhaler)'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Thận trọng'},
        'side_effects': [
        'Khô miệng (thường gặp)', 'Ho', 'Nhiễm trùng đường hô hấp trên',
        'Táo bón', 'Bí tiểu', 'Kích ứng mắt (nếu vào mắt)'],
        'interactions': [
        'Anticholinergic khác: tăng tác dụng phụ', 'Beta-agonist: hiệp đồng'],pregnancy': 'C', 'mechanism_of_action':
        'Anticholinergic dài tác dụng - ức chế muscarinic receptors (M1, M2, M3) ở cơ trơn phế quản, giảm acetylcholine-mediated co thắt phế quản. Giãn cơ trơn phế quản, giảm tiết dịch đường hô hấp. Tác dụng kéo dài 24 giờ (tương tự tiotropium). Không hấp thu hệ thống đáng kể khi dùng dạng hít (do ion hóa) → ít tác dụng phụ hệ thống. Chỉ có dạng fixed-dose combination với indacaterol (LABA) trong Ultibro Breezhaler. An toàn hơn beta-agonist cho bệnh nhân tim mạch.'
        , 'monitoring': [
        'Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa',
        'Nhịp tim, huyết áp (ít tác dụng tim mạch hơn beta-agonist)',
        'Dấu hiệu kích ứng mắt (nếu vào mắt - tăng nhãn áp, đỏ mắt)',
        'Dấu hiệu tăng nhãn áp (đau mắt, nhìn mờ) - đặc biệt ở bệnh nhân glaucoma',
        'Dấu hiệu bí tiểu (khó tiểu, đầy bụng) - đặc biệt ở bệnh nhân phì đại tuyến tiền liệt'
        , 'Dấu hiệu khô miệng nặng (có thể ảnh hưởng sức khỏe răng miệng)'],
        'precautions': [
        'Rửa miệng sau khi dùng để giảm kích ứng và tránh thuốc vào mắt',
        'Tránh để thuốc vào mắt (có thể gây tăng nhãn áp, đặc biệt ở bệnh nhân glaucoma)'
        'Thận trọng ở bệnh nhân glaucoma góc đóng (chống chỉ định) hoặc tăng nhãn áp'
        'Thận trọng ở bệnh nhân phì đại tuyến tiền liệt nặng (có thể gây bí tiểu)',
        'Chỉ có dạng fixed-dose combination với indacaterol (Ultibro Breezhaler) - không có dạng đơn độc'
        , 'Dùng 1 lần/ngày (thuận tiện)',
        'Dạng hít: sử dụng đúng kỹ thuật để đạt hiệu quả tối đa',
        'An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích tim)',
        'Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn'],
        'pharmacokinetics': {'half_life': '2-3 giờ (ngắn hơn tiotropium)',
        'onset': '5-15 phút', 'duration': '24 giờ (dài)',
        'protein_binding': 'N/A', 'clearance':
        'Thận (thải qua thận, ít tích lũy hơn tiotropium)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. DPI: bảo quản trong bao bì gốc. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings':
        'Tránh để thuốc vào mắt - có thể gây tăng nhãn áp, đặc biệt nguy hiểm ở bệnh nhân glaucoma góc đóng. Rửa miệng sau khi dùng để tránh thuốc vào mắt.'
        , 'drug_interactions': {'major': [],moderate': [{'drug':
        'Anticholinergic khác (Atropine, Scopolamine, Benztropine, Oxybutynin, Ipratropium, Tiotropium, Aclidinium)'
        , 'mechanism':
        'Tăng tác dụng anticholinergic, tăng tác dụng phụ anticholinergic',
        'effect': 'Tăng khô miệng, bí tiểu, táo bón, tăng nhãn áp, nhìn mờ',
        'management':
        'Thận trọng khi dùng cùng. Theo dõi tác dụng phụ anticholinergic. Có thể cần giảm liều hoặc tránh dùng cùng.'
        }],
        'moderate': [{'drug': 'Beta-2 agonists (SABA, LABA)', 'mechanism': 'Hiệp đồng tác dụng giãn phế quản', 'effect':
        'Tăng hiệu quả giãn phế quản (tác dụng tích cực)', 'management':
        'Có thể dùng kết hợp để tăng hiệu quả. Không cần điều chỉnh liều.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng với glycopyrronium, atropine hoặc các thành phần khác',
        'Glaucoma góc đóng (chống chỉ định tuyệt đối)',
        'Tăng nhãn áp nặng không kiểm soát'],
        'tương_đối': [
        'Glaucoma góc mở - thận trọng, theo dõi nhãn áp',
        'Tăng nhãn áp nhẹ - thận trọng, tránh để thuốc vào mắt',
        'Phì đại tuyến tiền liệt nặng - có thể gây bí tiểu',
        'Bí tiểu - có thể làm nặng', 'Táo bón nặng - có thể làm nặng',
        'Suy thận trung bình (CrCl 30-60 ml/min) - thận trọng, theo dõi tác dụng phụ'
        , 'Nhược cơ - có thể làm nặng',
        'Dùng với anticholinergic khác - tăng tác dụng phụ']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Glycopyrronium là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Glycopyrronium được sử dụng trong thai kỳ để điều trị COPD và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do ion hóa), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Glycopyrronium bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi', 'notes':
        'Glycopyrronium không chuyển hóa đáng kể ở gan. Hấp thu toàn thân tối thiểu từ dạng hít. Không cần điều chỉnh liều ở suy gan.'
        },overdose_management': {'symptoms': ['Khô miệng nặng', 'Bí tiểu',
        'Táo bón nặng', 'Tăng nhãn áp (nếu vào mắt)', 'Nhìn mờ',
        'Đỏ mắt, đau mắt', 'Nhịp tim nhanh (hiếm, nếu hấp thu toàn thân)',
        'Kích động, lú lẫn (hiếm)'],antidote':
        'Không có antidote đặc hiệu. Physostigmine (cholinergic) có thể được dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân, nhưng thận trọng và chỉ dùng trong môi trường có hỗ trợ hô hấp.'
        , 'treatment': ['Ngừng ngay glycopyrronium',
        'Rửa mắt ngay nếu thuốc vào mắt (dùng nước sạch hoặc nước muối sinh lý)',
        'Điều trị tăng nhãn áp nếu có (dùng thuốc nhỏ mắt chống tăng nhãn áp, khám bác sĩ mắt)'
        , 'Hỗ trợ bí tiểu nếu cần (đặt ống thông tiểu)',
        'Điều trị táo bón nếu cần (thuốc nhuận tràng, thụt tháo)',
        'Theo dõi nhãn áp nếu có triệu chứng mắt',
        'Theo dõi nhịp tim, huyết áp nếu có triệu chứng toàn thân',
        'Hỗ trợ hô hấp nếu cần (hiếm)',
        'Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (thận trọng, có hỗ trợ hô hấp)'
        ],
        'monitoring':
        'Theo dõi: nhãn áp (nếu có triệu chứng mắt), nhịp tim, huyết áp, tình trạng bí tiểu, táo bón. Theo dõi ít nhất 24 giờ.'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Physostigmine', 'mechanism':
        'Ức chế acetylcholinesterase, tăng acetylcholine, đối kháng tác dụng anticholinergic'
        , 'indication':
        'Quá liều nghiêm trọng với tác dụng toàn thân (hiếm với glycopyrronium dạng hít)'
        , 'caution':
        'Thận trọng, chỉ dùng trong môi trường có hỗ trợ hô hấp. Có thể gây co thắt phế quản, tăng tiết dịch, co giật. Chỉ dùng khi quá liều nghiêm trọng với tác dụng toàn thân.'
        }],notes':
        'Không có antidote đặc hiệu cho glycopyrronium. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (rất hiếm với dạng hít).'
        },administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dùng dạng hít DPI (Breezhaler). Mở nắp, đặt capsule vào buồng, đóng nắp, nhấn nút để đâm thủng capsule, hít sâu và giữ hơi thở 10 giây. Chỉ có dạng fixed-dose combination với indacaterol (Ultibro Breezhaler).'
        , 'timing': 'Dùng 1 lần/ngày, tốt nhất vào buổi sáng, cách nhau 24 giờ.',
        'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và QUAN TRỌNG: tránh thuốc vào mắt (có thể gây tăng nhãn áp).'
        , 'notes':
        'Tránh để thuốc vào mắt - rửa tay sau khi dùng. Nếu thuốc vào mắt, rửa ngay bằng nước sạch. Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn. Chỉ có dạng fixed-dose combination với indacaterol (Ultibro Breezhaler).'
        }},references': {'primary_sources': [
        'FDA Label: Seebri Breezhaler (Glycopyrronium)',
        'UpToDate: Long-acting anticholinergic bronchodilators in COPD',
        'GOLD Guidelines 2024: COPD Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Glycopyrronium'],evidence_level':
        'High - FDA approved, multiple RCTs'},
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["ophthalmic"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Intraocular pressure", "Renal function"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "GOLD Guidelines - COPD Management"
        ]
    },
    "Tiotropium": {'group': 'Respiratory - Anticholinergic (Long-acting)',
        'vietnamese_name':
        'Tiotropium, Spiriva', 'administration': [
        'Inhalation (HandiHaler hoặc Respimat)'],
        'indications': [
        'COPD (phòng ngừa)',
        'Hen phế quản (kết hợp với ICS, nếu không kiểm soát)'],
        'contraindications': ['Dị ứng atropine/tiotropium', 'Glaucoma góc đóng',
        'Tăng nhãn áp', 'Phì đại tuyến tiền liệt nặng'],
        'dosage': {
        'adult_handihaler': '18mcg x 1 lần/ngày', 'adult_respimat':
        '5mcg x 2 lần/ngày (sáng và tối)', 'notes':
        'Tác dụng kéo dài 24 giờ. Dùng 1 lần/ngày với HandiHaler'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Tránh dùng (thải qua thận)'},
        'side_effects': [
        'Khô miệng (thường gặp)', 'Ho', 'Nhiễm trùng đường hô hấp trên',
        'Táo bón', 'Bí tiểu', 'Kích ứng mắt (nếu vào mắt)'],
        'interactions': [
        'Anticholinergic khác: tăng tác dụng phụ', 'Beta-agonist: hiệp đồng'],pregnancy': 'C', 'mechanism_of_action':
        'Anticholinergic dài tác dụng - ức chế muscarinic receptors (M1, M2, M3) ở cơ trơn phế quản, giảm acetylcholine-mediated co thắt phế quản. Giãn cơ trơn phế quản, giảm tiết dịch đường hô hấp. Liên kết chặt với M3 receptors (chủ yếu) và M1 receptors, giải phóng chậm → tác dụng kéo dài 24 giờ. Không hấp thu hệ thống đáng kể khi dùng dạng hít (do ion hóa) → ít tác dụng phụ hệ thống. Tác dụng dài hơn ipratropium (4-6 giờ so với 24 giờ). An toàn hơn beta-agonist cho bệnh nhân tim mạch.'
        , 'monitoring': [
        'Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa',
        'Nhịp tim, huyết áp (ít tác dụng tim mạch hơn beta-agonist)',
        'Dấu hiệu kích ứng mắt (nếu vào mắt - tăng nhãn áp, đỏ mắt)',
        'Dấu hiệu tăng nhãn áp (đau mắt, nhìn mờ) - đặc biệt ở bệnh nhân glaucoma',
        'Dấu hiệu bí tiểu (khó tiểu, đầy bụng) - đặc biệt ở bệnh nhân phì đại tuyến tiền liệt'
        , 'Dấu hiệu khô miệng nặng (có thể ảnh hưởng sức khỏe răng miệng)',
        'Chức năng thận (thải qua thận, tích lũy ở suy thận)'],
        'precautions':
        ['Rửa miệng sau khi dùng để giảm kích ứng và tránh thuốc vào mắt',
        'Tránh để thuốc vào mắt (có thể gây tăng nhãn áp, đặc biệt ở bệnh nhân glaucoma)'
        'Thận trọng ở bệnh nhân glaucoma góc đóng (chống chỉ định) hoặc tăng nhãn áp'
        'Thận trọng ở bệnh nhân phì đại tuyến tiền liệt nặng (có thể gây bí tiểu)',
        'Thận trọng ở suy thận (thải qua thận, tích lũy) - tránh dùng nếu CrCl <30'
        'Dùng 1 lần/ngày với HandiHaler (18mcg) hoặc 2 lần/ngày với Respimat (5mcg)'
        , 'Kết hợp với ICS cho hen phế quản nếu không kiểm soát',
        'Dạng hít: sử dụng đúng kỹ thuật để đạt hiệu quả tối đa',
        'An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích tim)',
        'Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn'],
        'pharmacokinetics': {'half_life':
        '5-6 ngày (rất dài, do liên kết chặt với receptor)', 'onset':
        '30-60 phút', 'duration': '24 giờ (dài)', 'protein_binding': '72%',
        'clearance': 'Thận (thải qua thận, tích lũy ở suy thận)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. HandiHaler: bảo quản trong bao bì gốc. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings':
        'Tránh để thuốc vào mắt - có thể gây tăng nhãn áp, đặc biệt nguy hiểm ở bệnh nhân glaucoma góc đóng. Rửa miệng sau khi dùng để tránh thuốc vào mắt. Thận trọng ở suy thận - tích lũy có thể gây tăng tác dụng phụ.'
        , 'drug_interactions': {'major': [],moderate': [{'drug':
        'Anticholinergic khác (Atropine, Scopolamine, Benztropine, Oxybutynin, Ipratropium)'
        , 'mechanism':
        'Tăng tác dụng anticholinergic, tăng tác dụng phụ anticholinergic',
        'effect': 'Tăng khô miệng, bí tiểu, táo bón, tăng nhãn áp, nhìn mờ',
        'management':
        'Thận trọng khi dùng cùng. Theo dõi tác dụng phụ anticholinergic. Có thể cần giảm liều hoặc tránh dùng cùng.'
        }],
        'moderate': [{'drug': 'Beta-2 agonists (SABA, LABA)', 'mechanism': 'Hiệp đồng tác dụng giãn phế quản', 'effect':
        'Tăng hiệu quả giãn phế quản (tác dụng tích cực)', 'management':
        'Có thể dùng kết hợp để tăng hiệu quả. Không cần điều chỉnh liều.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng với tiotropium, atropine hoặc các thành phần khác',
        'Glaucoma góc đóng (chống chỉ định tuyệt đối)',
        'Tăng nhãn áp nặng không kiểm soát',
        'Suy thận nặng (CrCl <30 ml/min) - tích lũy, tăng tác dụng phụ'],
        'tương_đối': ['Glaucoma góc mở - thận trọng, theo dõi nhãn áp',
        'Tăng nhãn áp nhẹ - thận trọng, tránh để thuốc vào mắt',
        'Phì đại tuyến tiền liệt nặng - có thể gây bí tiểu',
        'Bí tiểu - có thể làm nặng', 'Táo bón nặng - có thể làm nặng',
        'Suy thận trung bình (CrCl 30-60 ml/min) - thận trọng, theo dõi tác dụng phụ'
        , 'Nhược cơ - có thể làm nặng',
        'Dùng với anticholinergic khác - tăng tác dụng phụ']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Tiotropium là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Tiotropium được sử dụng trong thai kỳ để điều trị COPD và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do ion hóa), nên tác dụng toàn thân tối thiểu. Tuy nhiên, tiotropium thải qua thận và có thời gian bán thải rất dài (5-6 ngày), nên có thể tích lũy. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Tiotropium bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        }},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi', 'notes':
        'Tiotropium không chuyển hóa đáng kể ở gan. Hấp thu toàn thân tối thiểu từ dạng hít. Không cần điều chỉnh liều ở suy gan.'
        },overdose_management': {'symptoms': ['Khô miệng nặng', 'Bí tiểu',
        'Táo bón nặng', 'Tăng nhãn áp (nếu vào mắt)', 'Nhìn mờ',
        'Đỏ mắt, đau mắt', 'Nhịp tim nhanh (hiếm, nếu hấp thu toàn thân)',
        'Kích động, lú lẫn (hiếm)',
        'Co giật (rất hiếm, chỉ khi hấp thu toàn thân lớn)'],antidote':
        'Không có antidote đặc hiệu. Physostigmine (cholinergic) có thể được dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân, nhưng thận trọng và chỉ dùng trong môi trường có hỗ trợ hô hấp.'
        , 'treatment': ['Ngừng ngay tiotropium',
        'Rửa mắt ngay nếu thuốc vào mắt (dùng nước sạch hoặc nước muối sinh lý)',
        'Điều trị tăng nhãn áp nếu có (dùng thuốc nhỏ mắt chống tăng nhãn áp, khám bác sĩ mắt)'
        , 'Hỗ trợ bí tiểu nếu cần (đặt ống thông tiểu)',
        'Điều trị táo bón nếu cần (thuốc nhuận tràng, thụt tháo)',
        'Theo dõi nhãn áp nếu có triệu chứng mắt',
        'Theo dõi nhịp tim, huyết áp nếu có triệu chứng toàn thân',
        'Hỗ trợ hô hấp nếu cần (hiếm)',
        'Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (thận trọng, có hỗ trợ hô hấp)'
        , 'Lưu ý: Thời gian bán thải rất dài (5-6 ngày) → theo dõi kéo dài'],
        'monitoring':
        'Theo dõi: nhãn áp (nếu có triệu chứng mắt), nhịp tim, huyết áp, tình trạng bí tiểu, táo bón, chức năng thận. Theo dõi ít nhất 24 giờ, nhưng có thể cần theo dõi lâu hơn do thời gian bán thải rất dài (5-6 ngày).'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Physostigmine', 'mechanism':
        'Ức chế acetylcholinesterase, tăng acetylcholine, đối kháng tác dụng anticholinergic'
        , 'indication':
        'Quá liều nghiêm trọng với tác dụng toàn thân (hiếm với tiotropium dạng hít)'
        , 'caution':
        'Thận trọng, chỉ dùng trong môi trường có hỗ trợ hô hấp. Có thể gây co thắt phế quản, tăng tiết dịch, co giật. Chỉ dùng khi quá liều nghiêm trọng với tác dụng toàn thân.'
        }],notes':
        'Không có antidote đặc hiệu cho tiotropium. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (rất hiếm với dạng hít). Lưu ý: Thời gian bán thải rất dài (5-6 ngày) → tác dụng có thể kéo dài.'
        },administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'handihaler': {'technique':
        'HandiHaler: Mở nắp, đặt capsule vào buồng, đóng nắp, nhấn nút để đâm thủng capsule, hít sâu và giữ hơi thở 10 giây. Dùng 1 lần/ngày (18mcg).'
        , 'timing':
        'Dùng 1 lần/ngày, tốt nhất vào buổi sáng, cách nhau 24 giờ.',
        'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và QUAN TRỌNG: tránh thuốc vào mắt (có thể gây tăng nhãn áp).'
        },respimat': {'technique':
        'Respimat: Xoay nắp để mở, xoay base để nạp thuốc, nhấn nút để phun thuốc, hít sâu và giữ hơi thở 10 giây. Dùng 2 lần/ngày (5mcg mỗi lần).'
        , 'timing': 'Dùng 2 lần/ngày (sáng và tối), cách nhau khoảng 12 giờ.',
        'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và QUAN TRỌNG: tránh thuốc vào mắt (có thể gây tăng nhãn áp).'
        },notes':
        'Tránh để thuốc vào mắt - rửa tay sau khi dùng. Nếu thuốc vào mắt, rửa ngay bằng nước sạch. Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn. Thận trọng ở suy thận (CrCl <30) - tránh dùng hoặc giảm liều.'
        }},references': {'primary_sources': [
        'FDA Label: Spiriva (Tiotropium)',
        'UpToDate: Long-acting anticholinergic bronchodilators in COPD',
        'GOLD Guidelines 2024: COPD Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Tiotropium'],evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'
        }},
    "Umeclidinium": {'group': 'Respiratory - Anticholinergic (Long-acting)',
        "pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        'vietnamese_name': 'Umeclidinium, Incruse Ellipta',
        'administration': ['Inhalation (DPI)'],
        'indications': [
        'COPD (phòng ngừa, kết hợp với vilanterol hoặc vilanterol/fluticasone)'],
        'contraindications': ['Dị ứng atropine/umeclidinium', 'Glaucoma góc đóng',
        'Tăng nhãn áp', 'Phì đại tuyến tiền liệt nặng'],
        'dosage': {
        'adult_inhalation': '62.5mcg x 1 lần/ngày (kết hợp với vilanterol hoặc vilanterol/fluticasone)',
        'notes':
        'Tác dụng kéo dài 24 giờ. Chỉ có dạng fixed-dose combination với vilanterol (Anoro Ellipta) hoặc vilanterol/fluticasone (Trelegy Ellipta)'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Thận trọng'},
        'side_effects': [
        'Khô miệng (thường gặp)', 'Ho', 'Nhiễm trùng đường hô hấp trên',
        'Táo bón', 'Bí tiểu', 'Kích ứng mắt (nếu vào mắt)',
        'Nấm miệng (nếu dùng với fluticasone)'],
        'interactions': [
        'Anticholinergic khác: tăng tác dụng phụ', 'Beta-agonist: hiệp đồng',
        'Ritonavir: tăng nồng độ fluticasone (tránh dùng)'],
        'mechanism_of_action':
        'Anticholinergic dài tác dụng - ức chế muscarinic receptors (M1, M2, M3) ở cơ trơn phế quản, giảm acetylcholine-mediated co thắt phế quản. Giãn cơ trơn phế quản, giảm tiết dịch đường hô hấp. Tác dụng kéo dài 24 giờ (tương tự tiotropium). Không hấp thu hệ thống đáng kể khi dùng dạng hít (do ion hóa) → ít tác dụng phụ hệ thống. Chỉ có dạng fixed-dose combination với vilanterol (LABA) trong Anoro Ellipta hoặc vilanterol/fluticasone (ICS) trong Trelegy Ellipta. An toàn hơn beta-agonist cho bệnh nhân tim mạch.'
        , 'monitoring': [
        'Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa',
        'Nhịp tim, huyết áp (ít tác dụng tim mạch hơn beta-agonist)',
        'Dấu hiệu kích ứng mắt (nếu vào mắt - tăng nhãn áp, đỏ mắt)',
        'Dấu hiệu tăng nhãn áp (đau mắt, nhìn mờ) - đặc biệt ở bệnh nhân glaucoma',
        'Dấu hiệu bí tiểu (khó tiểu, đầy bụng) - đặc biệt ở bệnh nhân phì đại tuyến tiền liệt'
        , 'Dấu hiệu khô miệng nặng (có thể ảnh hưởng sức khỏe răng miệng)',
        'Nấm miệng (nếu dùng với fluticasone) - súc miệng sau khi dùng'],
        'precautions': [
        'Rửa miệng sau khi dùng để giảm kích ứng và tránh thuốc vào mắt',
        'Tránh để thuốc vào mắt (có thể gây tăng nhãn áp, đặc biệt ở bệnh nhân glaucoma)'
        'Thận trọng ở bệnh nhân glaucoma góc đóng (chống chỉ định) hoặc tăng nhãn áp'
        'Thận trọng ở bệnh nhân phì đại tuyến tiền liệt nặng (có thể gây bí tiểu)',
        'Chỉ có dạng fixed-dose combination với vilanterol (Anoro Ellipta) hoặc vilanterol/fluticasone (Trelegy Ellipta) - không có dạng đơn độc'
        , 'Dùng 1 lần/ngày (thuận tiện)',
        'Dạng hít: sử dụng đúng kỹ thuật để đạt hiệu quả tối đa',
        'An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích tim)',
        'Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn',
        'TRÁNH DÙNG với ritonavir (nếu dùng Trelegy - tăng nồng độ fluticasone)',
        'Súc miệng sau khi dùng để tránh nấm miệng (nếu dùng Trelegy)'],
        'pharmacokinetics': {'half_life': '11 giờ', 'onset': '5-15 phút',
        'duration': '24 giờ (dài)', 'protein_binding': '89%', 'clearance':
        'Thận (thải qua thận, ít tích lũy hơn tiotropium)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. DPI: bảo quản trong bao bì gốc. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings':
        'Tránh để thuốc vào mắt - có thể gây tăng nhãn áp, đặc biệt nguy hiểm ở bệnh nhân glaucoma góc đóng. Rửa miệng sau khi dùng để tránh thuốc vào mắt. TRÁNH DÙNG với ritonavir (nếu dùng Trelegy).'
        , 'drug_interactions': {'major': [{'drug': 'Ritonavir', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ fluticasone (nếu dùng Trelegy)', 'effect':
        'Tăng nguy cơ ức chế trục HPA, hội chứng Cushing', 'management':
        'TRÁNH DÙNG với ritonavir nếu dùng Trelegy (umeclidinium/vilanterol/fluticasone).'
        }],
        'moderate': [{'drug':
        'Anticholinergic khác (Atropine, Scopolamine, Benztropine, Oxybutynin, Ipratropium, Tiotropium, Aclidinium, Glycopyrronium)'
        , 'mechanism':
        'Tăng tác dụng anticholinergic, tăng tác dụng phụ anticholinergic',
        'effect': 'Tăng khô miệng, bí tiểu, táo bón, tăng nhãn áp, nhìn mờ',
        'management':
        'Thận trọng khi dùng cùng. Theo dõi tác dụng phụ anticholinergic. Có thể cần giảm liều hoặc tránh dùng cùng.'
        }],
        'moderate': [{'drug': 'Beta-2 agonists (SABA, LABA)', 'mechanism': 'Hiệp đồng tác dụng giãn phế quản', 'effect':
        'Tăng hiệu quả giãn phế quản (tác dụng tích cực)', 'management':
        'Có thể dùng kết hợp để tăng hiệu quả. Không cần điều chỉnh liều.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng với umeclidinium, atropine hoặc các thành phần khác',
        'Glaucoma góc đóng (chống chỉ định tuyệt đối)',
        'Tăng nhãn áp nặng không kiểm soát',
        'Dùng với ritonavir (nếu dùng Trelegy) - chống chỉ định tuyệt đối'],
        'tương_đối': [
        'Glaucoma góc mở - thận trọng, theo dõi nhãn áp',
        'Tăng nhãn áp nhẹ - thận trọng, tránh để thuốc vào mắt',
        'Phì đại tuyến tiền liệt nặng - có thể gây bí tiểu',
        'Bí tiểu - có thể làm nặng', 'Táo bón nặng - có thể làm nặng',
        'Suy thận trung bình (CrCl 30-60 ml/min) - thận trọng, theo dõi tác dụng phụ'
        , 'Nhược cơ - có thể làm nặng',
        'Dùng với anticholinergic khác - tăng tác dụng phụ']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Umeclidinium là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Umeclidinium được sử dụng trong thai kỳ để điều trị COPD và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do ion hóa), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Umeclidinium bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi', 'notes':
        'Umeclidinium không chuyển hóa đáng kể ở gan. Hấp thu toàn thân tối thiểu từ dạng hít. Không cần điều chỉnh liều ở suy gan.'
        },overdose_management': {'symptoms': ['Khô miệng nặng', 'Bí tiểu',
        'Táo bón nặng', 'Tăng nhãn áp (nếu vào mắt)', 'Nhìn mờ',
        'Đỏ mắt, đau mắt', 'Nhịp tim nhanh (hiếm, nếu hấp thu toàn thân)',
        'Kích động, lú lẫn (hiếm)'],antidote':
        'Không có antidote đặc hiệu. Physostigmine (cholinergic) có thể được dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân, nhưng thận trọng và chỉ dùng trong môi trường có hỗ trợ hô hấp.'
        , 'treatment': ['Ngừng ngay umeclidinium',
        'Rửa mắt ngay nếu thuốc vào mắt (dùng nước sạch hoặc nước muối sinh lý)',
        'Điều trị tăng nhãn áp nếu có (dùng thuốc nhỏ mắt chống tăng nhãn áp, khám bác sĩ mắt)'
        , 'Hỗ trợ bí tiểu nếu cần (đặt ống thông tiểu)',
        'Điều trị táo bón nếu cần (thuốc nhuận tràng, thụt tháo)',
        'Theo dõi nhãn áp nếu có triệu chứng mắt',
        'Theo dõi nhịp tim, huyết áp nếu có triệu chứng toàn thân',
        'Hỗ trợ hô hấp nếu cần (hiếm)',
        'Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (thận trọng, có hỗ trợ hô hấp)'
        ],
        'monitoring':
        'Theo dõi: nhãn áp (nếu có triệu chứng mắt), nhịp tim, huyết áp, tình trạng bí tiểu, táo bón. Theo dõi ít nhất 24 giờ.'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Physostigmine', 'mechanism':
        'Ức chế acetylcholinesterase, tăng acetylcholine, đối kháng tác dụng anticholinergic'
        , 'indication':
        'Quá liều nghiêm trọng với tác dụng toàn thân (hiếm với umeclidinium dạng hít)'
        , 'caution':
        'Thận trọng, chỉ dùng trong môi trường có hỗ trợ hô hấp. Có thể gây co thắt phế quản, tăng tiết dịch, co giật. Chỉ dùng khi quá liều nghiêm trọng với tác dụng toàn thân.'
        }],notes':
        'Không có antidote đặc hiệu cho umeclidinium. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (rất hiếm với dạng hít).'
        },administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dùng dạng hít DPI (Ellipta). Xoay nắp để mở, xoay base để nạp thuốc, nhấn nút để phun thuốc, hít sâu và giữ hơi thở 10 giây. Chỉ có dạng fixed-dose combination với vilanterol (Anoro Ellipta) hoặc vilanterol/fluticasone (Trelegy Ellipta).'
        , 'timing': 'Dùng 1 lần/ngày, tốt nhất vào buổi sáng, cách nhau 24 giờ.',
        'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và QUAN TRỌNG: tránh thuốc vào mắt (có thể gây tăng nhãn áp). Nếu dùng Trelegy, súc miệng để tránh nấm miệng.'
        , 'notes':
        'Tránh để thuốc vào mắt - rửa tay sau khi dùng. Nếu thuốc vào mắt, rửa ngay bằng nước sạch. Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn. Chỉ có dạng fixed-dose combination với vilanterol (Anoro Ellipta) hoặc vilanterol/fluticasone (Trelegy Ellipta). TRÁNH DÙNG với ritonavir nếu dùng Trelegy.'
        }},references': {'primary_sources': [
        'FDA Label: Incruse Ellipta (Umeclidinium)',
        'UpToDate: Long-acting anticholinergic bronchodilators in COPD',
        'GOLD Guidelines 2024: COPD Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Umeclidinium'],evidence_level': 'High - FDA approved, multiple RCTs, clinical guidelines'},
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["ophthalmic"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Intraocular pressure", "Renal function"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "GOLD Guidelines - COPD Management"
        ]
    }
}

__all__ = ['ANTICHOLINERGIC_LONG_ACTINGS_DRUGS']
