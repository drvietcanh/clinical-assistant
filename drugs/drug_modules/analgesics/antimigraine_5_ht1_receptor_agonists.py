"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Antimigraine (5-HT1 Receptor Agonist)s

ANTIMIGRAINE_5_HT1_RECEPTOR_AGONISTS_DRUGS = {
    "Sumatriptan": {'group': 'Analgesic - Antimigraine (5-HT1 Receptor Agonist)',
        'vietnamese_name': 'Sumatriptan, Imitrex', 'administration': ['PO',
        'SC', 'Nasal'], 'indications': [
        'Migraine có tiền triệu (aura) hoặc không', 'Cluster headache'],
        'contraindications': ['Bệnh mạch vành', 'Nhồi máu cơ tim',
        'Đau thắt ngực không ổn định', 'Đột quỵ, TIA',
        'Bệnh mạch máu ngoại biên', 'Tăng huyết áp không kiểm soát',
        'Dùng MAO inhibitor trong 14 ngày', 'Dùng ergotamine trong 24 giờ'],
        'dosage': {'adult_po':
        '25-100mg, có thể lặp sau 2 giờ (tối đa 200mg/ngày)', 'adult_sc':
        '6mg SC, có thể lặp sau 1 giờ (tối đa 12mg/ngày)', 'adult_nasal':
        '5-20mg xịt mũi, có thể lặp sau 2 giờ (tối đa 40mg/ngày)', 'notes':
        'Dùng ngay khi có triệu chứng migraine. Không dùng để phòng ngừa'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'}, 'side_effects': [
        'Cảm giác nóng, đỏ, ngứa (SC injection)',
        'Đau ngực, khó thở (tương tự đau thắt ngực)', 'Nhức đầu', 'Chóng mặt',
        'Buồn nôn', 'Co thắt cơ', 'Yếu, mệt mỏi',
        'Nguy cơ đau tim (hiếm nhưng nguy hiểm)'], 'interactions': [
        'Ergotamine/Dihydroergotamine: chống chỉ định (trong 24 giờ)',
        'MAO inhibitor: chống chỉ định (trong 14 ngày)',
        'SSRI/SNRI: tăng nguy cơ hội chứng serotonin',
        'Thuốc ức chế CYP2D6: tăng nồng độ sumatriptan'], 'pregnancy': 'C',
        'mechanism_of_action':
        '5-HT1B/1D receptor agonist (selective serotonin receptor agonist, triptan). Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine). Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua cả hai cơ chế: co mạch và ức chế viêm thần kinh. Tác dụng nhanh (10-30 phút SC, 30-60 phút PO).'
        , 'monitoring': ['Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)',
        'Dấu hiệu co mạch: đau ngực, khó thở, đau cổ, hàm (có thể giống đau thắt ngực)'
        , 'Dấu hiệu bệnh mạch vành: đau ngực, khó thở, đau lan (nguy hiểm)',
        'Huyết áp (có thể tăng nhẹ)',
        'Dấu hiệu hội chứng serotonin: kích động, tăng thân nhiệt, tăng phản xạ (nếu dùng với SSRI/SNRI)'
        , 'Dấu hiệu quá liều: co mạch nặng, thiếu máu cục bộ'], 'precautions':
        ['Dùng ngay khi có triệu chứng migraine (không chờ đến khi đau nặng)',
        'Không dùng để phòng ngừa - chỉ dùng để cắt cơn',
        'CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên'
        , 'CHỐNG CHỈ ĐỊNH trong tăng huyết áp không kiểm soát',
        'Không dùng với ergotamine/dihydroergotamine trong 24 giờ - tăng nguy cơ co mạch nặng'
        ,
        'Không dùng với MAO inhibitor trong 14 ngày - tăng nguy cơ tác dụng phụ',
        'Thận trọng khi dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Nếu đau ngực, khó thở → ngừng ngay và đánh giá',
        'Không vượt quá liều tối đa (200mg/ngày PO, 12mg/ngày SC, 40mg/ngày nasal)'
        ,
        'Nếu không đáp ứng sau 2 liều → không dùng thêm, đánh giá lại chẩn đoán'
        ], 'pharmacokinetics': {'half_life': '2 giờ', 'onset':
        'SC: 10-15 phút; PO: 30-60 phút; Nasal: 15-30 phút', 'duration':
        '2-4 giờ', 'protein_binding': '14-21%', 'metabolism':
        'Gan (chuyển hóa qua MAO-A, một phần qua CYP2D6)', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng SC: bảo quản trong tủ lạnh, để ở nhiệt độ phòng trước khi dùng.'
        , 'black_box_warnings':
        'Nguy cơ co mạch nghiêm trọng, có thể gây nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ, có thể tử vong. CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên, tăng huyết áp không kiểm soát. Không dùng với ergotamine trong 24 giờ. Nếu có đau ngực, khó thở → ngừng ngay và đánh giá.'
        , 'drug_interactions': {'major': [{'drug':
        'Ergotamine, Dihydroergotamine', 'mechanism':
        'Cả hai đều gây co mạch, tăng nguy cơ co mạch nghiêm trọng', 'effect':
        'Tăng nguy cơ co mạch nghiêm trọng, nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ'
        , 'management':
        'CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.'
        }, {'drug': 'MAO Inhibitors (Phenelzine, Tranylcypromine)', 'mechanism':
        'Ức chế MAO-A (chuyển hóa sumatriptan), tăng nồng độ sumatriptan',
        'effect': 'Tăng nguy cơ tác dụng phụ, co mạch nghiêm trọng',
        'management':
        'CHỐNG CHỈ ĐỊNH - không dùng với MAO inhibitor trong 14 ngày.'}],
        'moderate': [{'drug': 'SSRI/SNRI (Fluoxetine, Sertraline, Venlafaxine)',
        'mechanism':
        'Cả hai đều tăng serotonin, tăng nguy cơ hội chứng serotonin', 'effect':
        'Tăng nguy cơ hội chứng serotonin (kích động, tăng thân nhiệt, tăng phản xạ)'
        , 'management':
        'Thận trọng, theo dõi dấu hiệu hội chứng serotonin. Có thể cần tránh dùng cùng.'
        }, {'drug': 'Thuốc ức chế CYP2D6', 'mechanism':
        'Giảm chuyển hóa sumatriptan, tăng nồng độ', 'effect':
        'Tăng tác dụng phụ, tăng nguy cơ co mạch', 'management':
        'Thận trọng, theo dõi tác dụng phụ. Có thể cần giảm liều sumatriptan.'}
        ], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng với sumatriptan hoặc các thành phần khác',
        'Bệnh mạch vành (CAD)', 'Nhồi máu cơ tim',
        'Đau thắt ngực không ổn định', 'Đột quỵ, TIA',
        'Bệnh mạch máu ngoại biên', 'Tăng huyết áp không kiểm soát',
        'Dùng MAO inhibitor trong 14 ngày',
        'Dùng ergotamine/dihydroergotamine trong 24 giờ'], 'tương_đối': [
        'Bệnh tim mạch khác (suy tim, loạn nhịp) - thận trọng, đánh giá tim mạch trước'
        , 'Tăng huyết áp đã kiểm soát - thận trọng',
        'Tiền sử đau thắt ngực - thận trọng',
        'Dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Suy thận nặng - thận trọng']}, 'pregnancy_lactation': {'fda_category':
        'C', 'pregnancy_details':
        'Sumatriptan là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Sumatriptan được sử dụng trong thai kỳ để điều trị migraine và có vẻ an toàn. Tuy nhiên, có nguy cơ co mạch có thể ảnh hưởng đến thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng thận trọng.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Sumatriptan bài tiết vào sữa mẹ với nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation': 'Có thể dùng an toàn khi cho con bú.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng - sumatriptan chuyển hóa qua gan (MAO-A, CYP2D6), có thể tích lũy'
        , 'severe': 'Thận trọng - có thể tích lũy, tăng tác dụng phụ', 'notes':
        'Sumatriptan chuyển hóa qua gan (MAO-A, một phần CYP2D6). Ở suy gan, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ tác dụng phụ. Có thể cần giảm liều.'
        }, 'overdose_management': {'symptoms': ['Co mạch nghiêm trọng',
        'Nhồi máu cơ tim', 'Đột quỵ', 'Thiếu máu cục bộ', 'Đau ngực nặng',
        'Khó thở nặng', 'Tăng huyết áp nghiêm trọng',
        'Hội chứng serotonin (nếu dùng với SSRI/SNRI)', 'Kích động, lú lẫn'],
        'antidote':
        'Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch, nhưng thận trọng.'
        , 'treatment': ['Ngừng ngay sumatriptan',
        'Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)',
        'Theo dõi tim mạch liên tục (ECG, huyết áp, SpO2)',
        'Điều trị nhồi máu cơ tim nếu có (theo protocol)',
        'Điều trị đột quỵ nếu có (theo protocol)',
        'Nitroglycerin để giãn mạch (thận trọng, có thể gây hạ huyết áp)',
        'Điều trị hội chứng serotonin nếu có (dantrolene, benzodiazepine)',
        'Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)',
        'Theo dõi và điều trị triệu chứng'], 'monitoring':
        'Theo dõi liên tục: ECG, huyết áp, SpO2, dấu hiệu co mạch, dấu hiệu nhồi máu cơ tim, dấu hiệu đột quỵ, dấu hiệu hội chứng serotonin. Theo dõi ít nhất 24 giờ do thời gian bán thải (2 giờ) và nguy cơ biến chứng.'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Nitroglycerin', 'mechanism': 'Giãn mạch, đối kháng tác dụng co mạch',
        'indication': 'Quá liều gây co mạch nghiêm trọng, đau ngực', 'caution':
        'Thận trọng, có thể gây hạ huyết áp. Chỉ dùng khi có co mạch nghiêm trọng.'
        }], 'notes':
        'Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch trong trường hợp quá liều nghiêm trọng, nhưng thận trọng. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng.'
        }, 'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn', 'timing':
        'Dùng ngay khi có triệu chứng migraine. Không dùng để phòng ngừa. Có thể lặp sau 2 giờ nếu cần (tối đa 200mg/ngày).'
        }, 'iv': None, 'sc': {'technique':
        'Dạng SC: Tiêm dưới da, thường ở đùi hoặc cánh tay. Liều: 6mg SC.',
        'timing':
        'Dùng ngay khi có triệu chứng migraine. Có thể lặp sau 1 giờ nếu cần (tối đa 12mg/ngày).'
        , 'notes':
        'Tác dụng nhanh nhất (10-15 phút). Bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi dùng.'
        }, 'nasal': {'technique':
        'Dạng xịt mũi: Xịt vào một bên mũi, nhắm mắt và miệng khi xịt.',
        'timing':
        'Dùng ngay khi có triệu chứng migraine. Có thể lặp sau 2 giờ nếu cần (tối đa 40mg/ngày).'
        , 'notes':
        'Tác dụng nhanh (15-30 phút). Có thể gây vị đắng trong miệng.'}},
        'references': {'primary_sources': ['FDA Label: Imitrex (Sumatriptan)',
        'UpToDate: Triptans for acute migraine',
        'American Headache Society Guidelines',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Sumatriptan'], 'last_updated': '2025-02-03',
        'evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'}},
    "Rizatriptan": {'group': 'Analgesic - Antimigraine (5-HT1 Receptor Agonist)',
        'vietnamese_name': 'Rizatriptan, Maxalt', 'administration': ['PO',
        'ODT'], 'indications': [
        'Migraine có tiền triệu (aura) hoặc không', 'Cluster headache'],
        'contraindications': ['Bệnh mạch vành', 'Nhồi máu cơ tim',
        'Đau thắt ngực không ổn định', 'Đột quỵ, TIA',
        'Bệnh mạch máu ngoại biên', 'Tăng huyết áp không kiểm soát',
        'Dùng MAO inhibitor trong 14 ngày', 'Dùng ergotamine trong 24 giờ'],
        'dosage': {'adult_po': '5-10mg, có thể lặp sau 2 giờ (tối đa 30mg/ngày)',
        'adult_odt': '5-10mg ODT, có thể lặp sau 2 giờ (tối đa 30mg/ngày)',
        'notes':
        'Dùng ngay khi có triệu chứng migraine. Nếu dùng với propranolol: giảm liều 50% (5mg thay vì 10mg)'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'}, 'side_effects': [
        'Đau ngực, khó thở (tương tự đau thắt ngực)', 'Nhức đầu', 'Chóng mặt',
        'Buồn nôn', 'Yếu, mệt mỏi', 'Nguy cơ đau tim (hiếm nhưng nguy hiểm)'],
        'interactions': [
        'Ergotamine/Dihydroergotamine: chống chỉ định (trong 24 giờ)',
        'MAO inhibitor: chống chỉ định (trong 14 ngày)',
        'Propranolol: tăng nồng độ rizatriptan (giảm liều rizatriptan 50%)',
        'SSRI/SNRI: tăng nguy cơ hội chứng serotonin'], 'pregnancy': 'C',
        'mechanism_of_action':
        '5-HT1B/1D receptor agonist (selective serotonin receptor agonist, triptan). Tương tự sumatriptan nhưng có tác dụng nhanh hơn và hiệu quả hơn. Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine). Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua cả hai cơ chế: co mạch và ức chế viêm thần kinh. Tác dụng nhanh (30-60 phút PO). Có dạng ODT (orally disintegrating tablet) - thuận tiện hơn, không cần nước.'
        , 'monitoring': [
        'Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)',
        'Dấu hiệu co mạch: đau ngực, khó thở, đau cổ, hàm (có thể giống đau thắt ngực)'
        , 'Dấu hiệu bệnh mạch vành: đau ngực, khó thở, đau lan (nguy hiểm)',
        'Huyết áp (có thể tăng nhẹ)',
        'Dấu hiệu hội chứng serotonin: kích động, tăng thân nhiệt, tăng phản xạ (nếu dùng với SSRI/SNRI)'
        , 'Tương tác với propranolol (tăng nồng độ, cần giảm liều 50%)'], 'precautions': [
        'Dùng ngay khi có triệu chứng migraine (không chờ đến khi đau nặng)',
        'Không dùng để phòng ngừa - chỉ dùng để cắt cơn',
        'CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên'
        , 'CHỐNG CHỈ ĐỊNH trong tăng huyết áp không kiểm soát',
        'Không dùng với ergotamine/dihydroergotamine trong 24 giờ - tăng nguy cơ co mạch nặng'
        ,
        'Không dùng với MAO inhibitor trong 14 ngày - tăng nguy cơ tác dụng phụ',
        'Nếu dùng với propranolol: GIẢM LIỀU RIZATRIPTAN 50% (5mg thay vì 10mg) - propranolol tăng nồng độ rizatriptan'
        , 'Thận trọng khi dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Nếu đau ngực, khó thở → ngừng ngay và đánh giá',
        'Không vượt quá liều tối đa (30mg/ngày)',
        'Dạng ODT: đặt trên lưỡi, không cần nước, thuận tiện hơn'], 'pharmacokinetics': {
        'half_life': '2-3 giờ', 'onset': 'PO: 30-60 phút; ODT: 30-60 phút',
        'duration': '2-4 giờ', 'protein_binding': '14%', 'metabolism':
        'Gan (chuyển hóa qua MAO-A, một phần qua CYP2D6)', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ). Propranolol ức chế MAO-A, tăng nồng độ rizatriptan.'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng ODT: bảo quản trong bao bì kín, tránh ẩm.'
        , 'black_box_warnings':
        'Nguy cơ co mạch nghiêm trọng, có thể gây nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ, có thể tử vong. CHỐNG CHỈ ĐỊNH trong bệnh mạch vành, nhồi máu cơ tim, đột quỵ, TIA, bệnh mạch máu ngoại biên, tăng huyết áp không kiểm soát. Không dùng với ergotamine trong 24 giờ. Nếu có đau ngực, khó thở → ngừng ngay và đánh giá.'
        , 'drug_interactions': {'major': [{'drug':
        'Ergotamine, Dihydroergotamine', 'mechanism':
        'Cả hai đều gây co mạch, tăng nguy cơ co mạch nghiêm trọng', 'effect':
        'Tăng nguy cơ co mạch nghiêm trọng, nhồi máu cơ tim, đột quỵ, thiếu máu cục bộ'
        , 'management':
        'CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.'}, {
        'drug': 'MAO Inhibitors (Phenelzine, Tranylcypromine)', 'mechanism':
        'Ức chế MAO-A (chuyển hóa rizatriptan), tăng nồng độ rizatriptan',
        'effect': 'Tăng nguy cơ tác dụng phụ, co mạch nghiêm trọng', 'management':
        'CHỐNG CHỈ ĐỊNH - không dùng với MAO inhibitor trong 14 ngày.'}, {'drug':
        'Propranolol', 'mechanism': 'Ức chế MAO-A, tăng nồng độ rizatriptan',
        'effect': 'Tăng nồng độ rizatriptan, tăng tác dụng phụ', 'management':
        'GIẢM LIỀU RIZATRIPTAN 50% (5mg thay vì 10mg) khi dùng với propranolol.'}],
        'moderate': [{'drug': 'SSRI/SNRI (Fluoxetine, Sertraline, Venlafaxine)',
        'mechanism': 'Cả hai đều tăng serotonin, tăng nguy cơ hội chứng serotonin',
        'effect': 'Tăng nguy cơ hội chứng serotonin (kích động, tăng thân nhiệt, tăng phản xạ)'
        , 'management':
        'Thận trọng, theo dõi dấu hiệu hội chứng serotonin. Có thể cần tránh dùng cùng.'}],
        'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng với rizatriptan hoặc các thành phần khác',
        'Bệnh mạch vành (CAD)', 'Nhồi máu cơ tim',
        'Đau thắt ngực không ổn định', 'Đột quỵ, TIA',
        'Bệnh mạch máu ngoại biên', 'Tăng huyết áp không kiểm soát',
        'Dùng MAO inhibitor trong 14 ngày',
        'Dùng ergotamine/dihydroergotamine trong 24 giờ'], 'tương_đối': [
        'Bệnh tim mạch khác (suy tim, loạn nhịp) - thận trọng, đánh giá tim mạch trước'
        , 'Tăng huyết áp đã kiểm soát - thận trọng',
        'Tiền sử đau thắt ngực - thận trọng',
        'Dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin',
        'Dùng với propranolol - giảm liều rizatriptan 50%',
        'Suy thận nặng - thận trọng']}, 'pregnancy_lactation': {'fda_category':
        'C', 'pregnancy_details':
        'Rizatriptan là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Rizatriptan được sử dụng trong thai kỳ để điều trị migraine và có vẻ an toàn. Tuy nhiên, có nguy cơ co mạch có thể ảnh hưởng đến thai nhi. Có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng thận trọng.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Rizatriptan bài tiết vào sữa mẹ với nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation': 'Có thể dùng an toàn khi cho con bú.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng - rizatriptan chuyển hóa qua gan (MAO-A, CYP2D6), có thể tích lũy'
        , 'severe': 'Thận trọng - có thể tích lũy, tăng tác dụng phụ', 'notes':
        'Rizatriptan chuyển hóa qua gan (MAO-A, một phần CYP2D6). Ở suy gan, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ tác dụng phụ. Có thể cần giảm liều.'},
        'overdose_management': {'symptoms': ['Co mạch nghiêm trọng',
        'Nhồi máu cơ tim', 'Đột quỵ', 'Thiếu máu cục bộ', 'Đau ngực nặng',
        'Khó thở nặng', 'Tăng huyết áp nghiêm trọng',
        'Hội chứng serotonin (nếu dùng với SSRI/SNRI)', 'Kích động, lú lẫn'],
        'antidote':
        'Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch, nhưng thận trọng.'
        , 'treatment': ['Ngừng ngay rizatriptan',
        'Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)',
        'Theo dõi tim mạch liên tục (ECG, huyết áp, SpO2)',
        'Điều trị nhồi máu cơ tim nếu có (theo protocol)',
        'Điều trị đột quỵ nếu có (theo protocol)',
        'Nitroglycerin để giãn mạch (thận trọng, có thể gây hạ huyết áp)',
        'Điều trị hội chứng serotonin nếu có (dantrolene, benzodiazepine)',
        'Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)',
        'Theo dõi và điều trị triệu chứng'], 'monitoring':
        'Theo dõi liên tục: ECG, huyết áp, SpO2, dấu hiệu co mạch, dấu hiệu nhồi máu cơ tim, dấu hiệu đột quỵ, dấu hiệu hội chứng serotonin. Theo dõi ít nhất 24 giờ do thời gian bán thải (2-3 giờ) và nguy cơ biến chứng.'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Nitroglycerin', 'mechanism': 'Giãn mạch, đối kháng tác dụng co mạch',
        'indication': 'Quá liều gây co mạch nghiêm trọng, đau ngực', 'caution':
        'Thận trọng, có thể gây hạ huyết áp. Chỉ dùng khi có co mạch nghiêm trọng.'}],
        'notes':
        'Không có antidote đặc hiệu. Nitroglycerin có thể được dùng để giãn mạch trong trường hợp quá liều nghiêm trọng, nhưng thận trọng. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng.'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn', 'timing':
        'Dùng ngay khi có triệu chứng migraine. Không dùng để phòng ngừa. Có thể lặp sau 2 giờ nếu cần (tối đa 30mg/ngày). Nếu dùng với propranolol: giảm liều 50% (5mg thay vì 10mg).'
        }, 'iv': None, 'odt': {'technique':
        'Dạng ODT (orally disintegrating tablet): Đặt trên lưỡi, để tan tự nhiên, không cần nước. Nuốt nước bọt sau khi tan.'
        , 'timing':
        'Dùng ngay khi có triệu chứng migraine. Có thể lặp sau 2 giờ nếu cần (tối đa 30mg/ngày). Nếu dùng với propranolol: giảm liều 50% (5mg thay vì 10mg).'
        , 'notes':
        'Thuận tiện hơn dạng uống thông thường, không cần nước. Bảo quản trong bao bì kín, tránh ẩm.'}},
        'references': {'primary_sources': ['FDA Label: Maxalt (Rizatriptan)',
        'UpToDate: Triptans for acute migraine',
        'American Headache Society Guidelines',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Rizatriptan'], 'last_updated': '2025-02-05',
        'evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'}}}

__all__ = ['ANTIMIGRAINE_5_HT1_RECEPTOR_AGONISTS_DRUGS']
