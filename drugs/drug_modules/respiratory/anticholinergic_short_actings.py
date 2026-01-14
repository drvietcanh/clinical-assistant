"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Anticholinergic (Short-acting)s

ANTICHOLINERGIC_SHORT_ACTINGS_DRUGS = {
    "Ipratropium": {'group': 'Respiratory - Anticholinergic (Short-acting)',
        "pregnancy": "B - Không có bằng chứng về nguy cơ ở người",
        'vietnamese_name':
        'Ipratropium, Atrovent', 'administration': ['Inhalation', 'Nebulizer'],
        'indications': ['COPD (cắt cơn và phòng ngừa)',
        'Hen phế quản (kết hợp với SABA)', 'Co thắt phế quản',
        'Chảy nước mũi (dạng xịt mũi)'],
        'contraindications': [
        'Dị ứng atropine/ipratropium', 'Glaucoma góc đóng', 'Tăng nhãn áp'],
        'dosage': {'adult_inhalation': '1-2 puffs (20-40mcg) mỗi 6-8 giờ',
        'adult_nebulizer': '250-500mcg mỗi 6-8 giờ', 'adult_max':
        '12 puffs/ngày hoặc 3 lần nebulizer/ngày', 'notes':
        'Tác dụng sau 15-30 phút, kéo dài 4-6 giờ. An toàn hơn beta-agonist cho bệnh nhân tim mạch'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': ['Khô miệng', 'Đắng miệng',
        'Ho', 'Kích ứng mắt (nếu vào mắt)', 'Tăng nhãn áp (nếu vào mắt)',
        'Bí tiểu (hiếm)'],
        'interactions': [
        'Anticholinergic khác: tăng tác dụng phụ',
        'Beta-agonist: hiệp đồng tốt'],
        'mechanism_of_action':
        'Anticholinergic - ức chế muscarinic receptors (M1, M2, M3) ở cơ trơn phế quản, giảm acetylcholine-mediated co thắt phế quản. Giãn cơ trơn phế quản, giảm tiết dịch đường hô hấp. Không hấp thu hệ thống đáng kể khi dùng dạng hít (do ion hóa) → ít tác dụng phụ hệ thống hơn atropine. Tác dụng ngắn (4-6 giờ). An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích beta-1 receptors).'
        , 'monitoring': ['Đáp ứng phế quản (peak flow, FEV1)',
        'Nhịp tim, huyết áp (ít tác dụng tim mạch hơn beta-agonist)',
        'Dấu hiệu kích ứng mắt (nếu vào mắt - tăng nhãn áp, đỏ mắt)',
        'Dấu hiệu tăng nhãn áp (đau mắt, nhìn mờ) - đặc biệt ở bệnh nhân glaucoma',
        'Dấu hiệu bí tiểu (khó tiểu, đầy bụng) - hiếm nhưng cần chú ý',
        'Dấu hiệu khô miệng nặng (có thể ảnh hưởng sức khỏe răng miệng)'],
        'precautions': [
        'Rửa miệng sau khi dùng để giảm kích ứng và tránh thuốc vào mắt',
        'Tránh để thuốc vào mắt (có thể gây tăng nhãn áp, đặc biệt ở bệnh nhân glaucoma)'
        'Thận trọng ở bệnh nhân glaucoma góc đóng (chống chỉ định) hoặc tăng nhãn áp'
        , 'Thận trọng ở bệnh nhân phì đại tuyến tiền liệt (có thể gây bí tiểu)',
        'Kết hợp với beta-agonist (SABA) cho hiệu quả tốt hơn - hiệp đồng tác dụng'
        , 'Dùng đều đặn cho COPD, dùng khi cần cho hen (kết hợp với SABA)',
        'Dạng hít: sử dụng đúng kỹ thuật để đạt hiệu quả tối đa',
        'Dạng nebulizer: phù hợp cho bệnh nhân không thể dùng dạng hít',
        'An toàn hơn beta-agonist cho bệnh nhân tim mạch (không kích thích tim)'
        ], 'onset':
        '15-30 phút (chậm hơn SABA)', 'duration': '4-6 giờ', 'protein_binding':
        'Không đáng kể (ion hóa, không hấp thu hệ thống)', 'clearance':
        'Chủ yếu tại chỗ (phế quản), không chuyển hóa đáng kể'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings':
        'Tránh để thuốc vào mắt - có thể gây tăng nhãn áp, đặc biệt nguy hiểm ở bệnh nhân glaucoma góc đóng. Rửa miệng sau khi dùng để tránh thuốc vào mắt.'
        , 'drug_interactions': {'major': [],
        'moderate': [{'drug':
        'Anticholinergic khác (Atropine, Scopolamine, Benztropine, Oxybutynin)',
        'mechanism':
        'Tăng tác dụng anticholinergic, tăng tác dụng phụ anticholinergic',
        'effect':
        'Tăng khô miệng, bí tiểu, táo bón, tăng nhãn áp, nhìn mờ, nhịp tim nhanh',
        'management':
        'Thận trọng khi dùng cùng. Theo dõi tác dụng phụ anticholinergic. Có thể cần giảm liều hoặc tránh dùng cùng.'
        }],
        'moderate': [{'drug': 'Beta-2 agonists (SABA, LABA)', 'mechanism': 'Hiệp đồng tác dụng giãn phế quản', 'effect':
        'Tăng hiệu quả giãn phế quản (tác dụng tích cực)', 'management':
        'Có thể dùng kết hợp để tăng hiệu quả. Không cần điều chỉnh liều.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng với ipratropium, atropine hoặc các thành phần khác',
        'Glaucoma góc đóng (chống chỉ định tuyệt đối)',
        'Tăng nhãn áp nặng không kiểm soát'],
        'tương_đối': [
        'Glaucoma góc mở - thận trọng, theo dõi nhãn áp',
        'Tăng nhãn áp nhẹ - thận trọng, tránh để thuốc vào mắt',
        'Phì đại tuyến tiền liệt - có thể gây bí tiểu',
        'Bí tiểu - có thể làm nặng', 'Táo bón nặng - có thể làm nặng',
        'Nhược cơ - có thể làm nặng',
        'Dùng với anticholinergic khác - tăng tác dụng phụ']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Ipratropium là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Ipratropium được sử dụng rộng rãi trong thai kỳ để điều trị COPD và hen, và có vẻ an toàn. Hấp thu toàn thân rất ít từ dạng hít (do ion hóa), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Ipratropium bài tiết rất ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        }},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi', 'notes':
        'Ipratropium không chuyển hóa đáng kể ở gan. Hấp thu toàn thân tối thiểu từ dạng hít. Không cần điều chỉnh liều ở suy gan.'
        },
        'overdose_management': {'symptoms': ['Khô miệng nặng', 'Bí tiểu',
        'Táo bón nặng', 'Tăng nhãn áp (nếu vào mắt)', 'Nhìn mờ',
        'Đỏ mắt, đau mắt', 'Nhịp tim nhanh (hiếm, nếu hấp thu toàn thân)',
        'Kích động, lú lẫn (hiếm)',
        'Co giật (rất hiếm, chỉ khi hấp thu toàn thân lớn)'],
        'antidote':
        'Không có antidote đặc hiệu. Physostigmine (cholinergic) có thể được dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân, nhưng thận trọng và chỉ dùng trong môi trường có hỗ trợ hô hấp.'
        , 'treatment': ['Ngừng ngay ipratropium',
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
        'Theo dõi: nhãn áp (nếu có triệu chứng mắt), nhịp tim, huyết áp, tình trạng bí tiểu, táo bón. Theo dõi ít nhất 4-6 giờ do thời gian tác dụng (4-6 giờ).'
        },
        'reversal_agents': {'available': True, 'agents': [{'agent':
        'Physostigmine', 'mechanism':
        'Ức chế acetylcholinesterase, tăng acetylcholine, đối kháng tác dụng anticholinergic'
        , 'indication':
        'Quá liều nghiêm trọng với tác dụng toàn thân (hiếm với ipratropium dạng hít)'
        , 'caution':
        'Thận trọng, chỉ dùng trong môi trường có hỗ trợ hô hấp. Có thể gây co thắt phế quản, tăng tiết dịch, co giật. Chỉ dùng khi quá liều nghiêm trọng với tác dụng toàn thân.'
        }],
        'notes':
        'Không có antidote đặc hiệu cho ipratropium. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine chỉ dùng trong trường hợp quá liều nghiêm trọng với tác dụng toàn thân (rất hiếm với dạng hít).'
        },
        'administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dạng hít (MDI): Lắc kỹ trước khi dùng. Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).'
        , 'timing':
        'Dùng mỗi 6-8 giờ khi cần (PRN) hoặc đều đặn cho COPD. Tối đa 12 puffs/ngày.'
        , 'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và QUAN TRỌNG: tránh thuốc vào mắt (có thể gây tăng nhãn áp).'
        , 'with_saba':
        'Có thể dùng kết hợp với beta-agonist (SABA) cho hiệu quả tốt hơn - hiệp đồng tác dụng.'
        , 'notes':
        'Tránh để thuốc vào mắt - rửa tay sau khi dùng. Nếu thuốc vào mắt, rửa ngay bằng nước sạch. Dạng nebulizer: phù hợp cho bệnh nhân không thể dùng dạng hít.'
        }, 'nebulizer': {'reconstitution':
        'Dùng dung dịch ipratropium 0.025% (250mcg/ml). Liều thường: 0.5-1ml (125-250mcg) pha với 2-4ml nước muối sinh lý.'
        , 'administration':
        'Dùng qua nebulizer, thở bình thường trong 10-15 phút cho đến khi hết thuốc.'
        , 'timing':
        'Mỗi 6-8 giờ khi cần hoặc đều đặn cho COPD. Tối đa 3 lần/ngày.',
        'after_use': 'Súc miệng sau khi dùng. Rửa tay để tránh thuốc vào mắt.'}
        },
        'references': {'primary_sources': [
        'FDA Label: Atrovent (Ipratropium)',
        'UpToDate: Anticholinergic bronchodilators in COPD',
        'GOLD Guidelines 2024: COPD Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Ipratropium'],
        "evidence_level": "High - FDA approved, multiple RCTs, clinical guidelines"
        }
    }

__all__ = ['ANTICHOLINERGIC_SHORT_ACTINGS_DRUGS']
