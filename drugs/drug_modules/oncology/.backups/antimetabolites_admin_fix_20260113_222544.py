"""Oncology Medications
Active module - contains all oncology drug data"""

# Antimetabolites

ANTIMETABOLITES_DRUGS = {
    "5-Fluorouracil": {'group': 'Oncology - Antimetabolite',
        'vietnamese_name':
        '5-Fluorouracil, 5-FU, Fluorouracil', 'administration': ['IV'],
        'indications': [        'Ung thư đại trực tràng (adjuvant và metastatic)',
        'Ung thư dạ dày', 'Ung thư đầu cổ', 'Ung thư tụy', 'Ung thư vú',
        'Ung thư da (topical)'],
        'contraindications': [
        'Thiếu hụt DPD (dihydropyrimidine dehydrogenase)',
        'Giảm bạch cầu/tiểu cầu nặng', 'Có thai', 'Đang cho con bú'],
        'dosage':
        {'adult_bolus':
        '400-600mg/m² IV bolus ngày 1, sau đó 400-600mg/m²/ngày x 4 ngày (mỗi 4 tuần)'
        , 'adult_infusion':
        '1000mg/m²/ngày IV infusion x 4-5 ngày (mỗi 4 tuần)', 'adult_weekly':
        '500-600mg/m² IV mỗi tuần', 'adult_topical': '5% cream bôi 2 lần/ngày',
        'notes':
        'Phối hợp với leucovorin để tăng hiệu quả. Cần test DPD nếu có thể'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, có thể giảm liều 25%', 'under_30':
        'Thận trọng, giảm liều 25-50%'},
        'side_effects': [
        'Loét miệng (stomatitis - phổ biến)',
        'Tiêu chảy (phổ biến, có thể nặng)',
        'Giảm bạch cầu, tiểu cầu (myelosuppression)', 'Ban da', 'Rụng tóc',
        'Độc tim (hiếm nhưng nguy hiểm)', 'Rối loạn thần kinh (hiếm)',
        'Tăng bilirubin'],
        'interactions': [
        'Leucovorin: tăng hiệu quả và độc tính', 'Methotrexate: tăng độc tính',
        'Warfarin: tăng nguy cơ chảy máu', 'Phenytoin: tăng nồng độ phenytoin'],
        'pregnancy': 'D - Chống chỉ định', 'mechanism_of_action':
        '5-Fluorouracil (5-FU) là antimetabolite, chuyển hóa thành 5-fluorodeoxyuridine monophosphate (FdUMP) và 5-fluorouridine triphosphate (FUTP). FdUMP ức chế enzyme thymidylate synthase (TS), ngăn cản tổng hợp thymidine (thành phần DNA), dẫn đến thiếu hụt DNA và gây chết tế bào. FUTP tích hợp vào RNA, gây rối loạn tổng hợp protein. Thuốc tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. Hiệu quả tăng khi dùng kèm leucovorin (folinic acid) do tăng ức chế TS'
        , 'monitoring': [
        'Công thức máu toàn phần (CBC) trước mỗi chu kỳ và giữa các chu kỳ (theo dõi giảm bạch cầu, tiểu cầu)'
        , 'Chức năng gan (ALT, AST, bilirubin) trước và trong điều trị',
        'Dấu hiệu loét miệng (stomatitis) - phổ biến, có thể nặng',
        'Dấu hiệu tiêu chảy - phổ biến, có thể nặng (cần điều trị sớm)',
        'Dấu hiệu độc tim (đau ngực, khó thở, rối loạn nhịp) - hiếm nhưng nguy hiểm'
        'Test DPD (dihydropyrimidine dehydrogenase) trước điều trị nếu có thể (thiếu hụt DPD gây độc tính nặng)'
        , 'Dấu hiệu nhiễm trùng (sốt, ớn lạnh) do giảm bạch cầu'],
        'precautions': [
        'Test DPD trước điều trị nếu có thể (thiếu hụt DPD gây độc tính nặng, có thể tử vong)'
        , 'Giảm liều hoặc ngừng nếu có loét miệng nặng hoặc tiêu chảy nặng',
        'Dùng kèm leucovorin để tăng hiệu quả (nhưng cũng tăng độc tính)',
        'Theo dõi sát công thức máu (nguy cơ giảm bạch cầu, tiểu cầu cao)',
        'Tránh dùng nếu thiếu hụt DPD nặng',
        'Có thể gây độc tim (hiếm - cần theo dõi triệu chứng)',
        'Tương tác với warfarin (tăng nguy cơ chảy máu)',
        'Giảm liều 25-50% nếu suy thận'],
        'pharmacokinetics': {'half_life':
        '10-20 phút (ngắn)', 'onset': '1-2 tuần (tác dụng lâm sàng)',
        'duration': '4-6 giờ (tác dụng sinh học)', 'protein_binding': 'Minimal',
        'clearance':
        'Gan (chuyển hóa qua DPD - dihydropyrimidine dehydrogenase), thận (thải trừ)'
        },
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu'
        , 'black_box_warnings':
        'Thiếu hụt DPD (dihydropyrimidine dehydrogenase) có thể gây độc tính nặng và tử vong. Nên test DPD trước điều trị nếu có thể. Theo dõi sát độc tính và ngừng ngay nếu có dấu hiệu độc tính nặng'
        , 'drug_interactions': {
            'major': [
                {'drug': 'Methotrexate',
                 'mechanism': 'Cả hai đều là antimetabolite, tác dụng cộng dồn làm tăng độc tính tủy xương và niêm mạc.',
                 'effect': 'Tăng nguy cơ giảm bạch cầu, tiểu cầu, loét miệng, tiêu chảy nghiêm trọng',
                 'management': 'Thận trọng khi dùng đồng thời. Theo dõi CBC và dấu hiệu độc tính chặt chẽ. Có thể cần giảm liều hoặc tránh dùng đồng thời.'}
            ],
        'moderate': [
                {'drug': 'Warfarin',
                 'mechanism': '5-FU có thể ức chế chuyển hóa warfarin, tăng nồng độ warfarin trong máu.',
                 'effect': 'Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu',
                 'management': 'Theo dõi INR chặt chẽ khi bắt đầu hoặc ngừng 5-FU. Có thể cần giảm liều warfarin.'},
                {'drug': 'Phenytoin',
                 'mechanism': '5-FU có thể ức chế chuyển hóa phenytoin, tăng nồng độ phenytoin trong máu.',
                 'effect': 'Tăng nồng độ phenytoin, tăng độc tính phenytoin',
                 'management': 'Theo dõi nồng độ phenytoin và dấu hiệu độc tính. Có thể cần giảm liều phenytoin.'}
            ],
        'minor': [
                {'drug': 'Leucovorin',
                 'mechanism': 'Leucovorin tăng hiệu quả của 5-FU bằng cách tăng ức chế thymidylate synthase, nhưng cũng tăng độc tính.',
                 'effect': 'Tăng hiệu quả và độc tính của 5-FU',
                 'management': 'Dùng kèm để tăng hiệu quả, nhưng cần theo dõi độc tính chặt chẽ hơn.'}
            ]
        },
        'contraindications': {'tuyệt_đối': [
        'Thiếu hụt DPD (dihydropyrimidine dehydrogenase) nặng - chống chỉ định tuyệt đối, có thể gây tử vong'
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'],
        'tương_đối': [
        'Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục',
        'Suy thận (CrCl <30) - giảm liều 25-50%, theo dõi chặt chẽ',
        'Suy gan - thận trọng, có thể cần giảm liều',
        'Bệnh nhân cao tuổi - tăng nguy cơ độc tính']},
        'pregnancy_lactation':
        {'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. 5-FU gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        '5-FU bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.'
        , 'recommendation':
        'Không cho con bú khi dùng 5-FU. Ngừng cho con bú hoặc ngừng thuốc.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể cần giảm liều', 'severe':
        'Thận trọng, giảm liều 25-50%', 'notes':
        '5-FU chuyển hóa chủ yếu qua gan (DPD - dihydropyrimidine dehydrogenase). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ.'
        },
        'overdose_management': {'symptoms': ['Loét miệng nặng (stomatitis)',
        'Tiêu chảy nặng, mất nước',
        'Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)',
        'Độc tim (hiếm)', 'Rối loạn thần kinh (hiếm)', 'Tăng bilirubin'],
        'antidote':
        'Uridine triacetate (Vistogard) - antidote đặc hiệu cho quá liều 5-FU do thiếu hụt DPD'
        , 'treatment': ['Ngừng ngay 5-FU',
        'Nếu có thiếu hụt DPD và quá liều: dùng uridine triacetate (Vistogard) càng sớm càng tốt'
        , 'Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần',
        'Theo dõi CBC, chức năng gan, chức năng thận',
        'Điều trị loét miệng (súc miệng, thuốc giảm đau)',
        'Điều trị tiêu chảy (loperamide, bù dịch)',
        'Theo dõi và điều trị độc tim nếu có'],
        'monitoring':
        'CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc tim'
        },
        'reversal_agents': {'available': True, 'agents': [{'name':
        'Uridine triacetate (Vistogard)', 'indication':
        'Quá liều 5-FU do thiếu hụt DPD hoặc quá liều do lỗi dùng thuốc',
        'dose': '10g PO x 3 lần/ngày x 5 ngày (bắt đầu càng sớm càng tốt)',
        'notes':
        'Antidote đặc hiệu cho quá liều 5-FU. Hiệu quả nhất khi dùng trong vòng 96 giờ sau quá liều.'
        }]},
        'administration_instructions': {'oral': {'with_food':
        'Không áp dụng', 'timing': 'Không có dạng uống (chỉ có IV và topical)'},iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất', 'infusion_rate':
        'Bolus: tiêm trực tiếp. Infusion: truyền trong 4-24 giờ tùy phác đồ',
        'compatibility': ['NS', 'D5W'],
        'incompatibility': [],
        'notes':
        'Bolus: 400-600mg/m² tiêm trực tiếp. Infusion: 1000mg/m²/ngày truyền trong 4-24 giờ. Theo dõi extravasation.'
        }},
        'references': {'primary_sources': [
        'FDA Drug Label - 5-Fluorouracil',
        'UpToDate - 5-Fluorouracil Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-15', 'evidence_level':
        'High (FDA-approved, extensive clinical data)'}},
    "Gemcitabine": {'group': 'Oncology - Antimetabolite',
        'vietnamese_name':
        'Gemcitabine, Gemzar', 'administration': ['IV'],
        'indications': [
        'Ung thư tụy (adjuvant và metastatic)', 'Ung thư phổi không tế bào nhỏ (NSCLC)',
        'Ung thư bàng quang', 'Ung thư vú (metastatic)',
        'Ung thư buồng trứng'],
        'contraindications': [
        'Giảm bạch cầu/tiểu cầu nặng', 'Có thai', 'Đang cho con bú'],
        'dosage': {
        'adult_standard': '1000mg/m² IV ngày 1, 8, 15 (mỗi 28 ngày) hoặc ngày 1, 8 (mỗi 21 ngày)',
        'adult_pancreatic': '1000mg/m² IV ngày 1, 8, 15 (mỗi 28 ngày)',
        'adult_bladder': '1000mg/m² IV ngày 1, 8, 15 (mỗi 28 ngày)',
        'notes':
        'Truyền trong 30 phút. Có thể phối hợp với cisplatin, carboplatin, hoặc paclitaxel'},
        'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Thận trọng, có thể giảm liều 25%',
        'under_30': 'Thận trọng, giảm liều 25-50%'},
        'side_effects': [
        'Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến)',
        'Buồn nôn, nôn (nhẹ đến trung bình)', 'Phát ban, ngứa',
        'Sốt, ớn lạnh (flu-like syndrome - phổ biến)',
        'Phù ngoại biên (hiếm)', 'Độc phổi (viêm phổi kẽ - hiếm nhưng nguy hiểm)',
        'Độc gan (tăng transaminase - hiếm)', 'Rụng tóc (nhẹ)'],
        'interactions': [
        'Cisplatin: tăng độc tính tủy xương',
        'Warfarin: có thể tăng tác dụng chống đông',
        'Live vaccines: tránh dùng trong điều trị'],
        'mechanism_of_action':
        'Gemcitabine là antimetabolite pyrimidine, tương tự cytarabine. Gemcitabine được chuyển hóa thành gemcitabine triphosphate (dFdCTP) và gemcitabine diphosphate (dFdCDP). dFdCTP tích hợp vào DNA, gây chấm dứt chuỗi DNA (chain termination) và ngăn cản quá trình sao chép DNA. dFdCDP ức chế enzyme ribonucleotide reductase (RNR), ngăn cản tổng hợp deoxyribonucleotides (thành phần DNA), dẫn đến thiếu hụt DNA và gây chết tế bào. Gemcitabine tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. Gemcitabine có tác dụng tự tăng cường (self-potentiating) - tích hợp vào DNA làm tăng tích lũy dFdCTP. Hiệu quả với nhiều loại ung thư, đặc biệt ung thư tụy, phổi, bàng quang.'
        , 'monitoring': [
        'Công thức máu toàn phần (CBC) trước mỗi chu kỳ và giữa các chu kỳ (theo dõi giảm bạch cầu, tiểu cầu - phổ biến)'
        , 'Chức năng gan (ALT, AST) trước và trong điều trị (độc gan hiếm)',
        'Dấu hiệu nhiễm trùng (sốt, ớn lạnh) do giảm bạch cầu',
        'Dấu hiệu độc phổi (khó thở, ho, đau ngực) - viêm phổi kẽ hiếm nhưng nguy hiểm'
        , 'Dấu hiệu flu-like syndrome (sốt, ớn lạnh, đau cơ) - phổ biến, thường tự khỏi'
        , 'Dấu hiệu phát ban, ngứa'],
        'precautions': [
        'Theo dõi sát công thức máu (nguy cơ giảm bạch cầu, tiểu cầu cao)',
        'Giảm liều hoặc trì hoãn điều trị nếu giảm bạch cầu/tiểu cầu nặng',
        'Flu-like syndrome (sốt, ớn lạnh) - phổ biến, thường tự khỏi, có thể dùng acetaminophen'
        , 'Độc phổi (viêm phổi kẽ) - hiếm nhưng nguy hiểm, ngừng ngay nếu có dấu hiệu',
        'Tương tác với cisplatin (tăng độc tính tủy xương)',
        'Tương tác với warfarin (tăng nguy cơ chảy máu)',
        'Tránh dùng live vaccines trong điều trị',
        'Giảm liều 25-50% nếu suy thận'],
        'pharmacokinetics': {'half_life':
        '42-94 phút (ngắn)', 'onset': '1-2 tuần (tác dụng lâm sàng)',
        'duration': '4-6 giờ (tác dụng sinh học)', 'protein_binding': 'Minimal',
        'clearance':
        'Gan (chuyển hóa qua deamination), thận (thải trừ - 92% nguyên dạng)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Pha với NS hoặc D5W.'
        , 'black_box_warnings':
        'Giảm bạch cầu, tiểu cầu (myelosuppression) phổ biến. Theo dõi CBC trước mỗi chu kỳ. Độc phổi (viêm phổi kẽ) hiếm nhưng nguy hiểm - ngừng ngay nếu có dấu hiệu.'
        , 'drug_interactions': {'major': [{'drug': 'Cisplatin', 'mechanism':
        'Cả hai đều gây myelosuppression, tác dụng cộng dồn', 'effect':
        'Tăng nguy cơ giảm bạch cầu, tiểu cầu nghiêm trọng', 'management':
        'Theo dõi CBC chặt chẽ. Có thể cần giảm liều hoặc trì hoãn điều trị.'}],
        'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Gemcitabine có thể tăng tác dụng chống đông', 'effect':
        'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR chặt chẽ. Có thể cần giảm liều warfarin.'}],
        'minor': [{'drug':
        'Live vaccines', 'mechanism':
        'Gemcitabine ức chế miễn dịch, tăng nguy cơ nhiễm trùng từ vaccine', 'effect':
        'Tăng nguy cơ nhiễm trùng từ live vaccine', 'management':
        'Tránh dùng live vaccines trong điều trị và ít nhất 3 tháng sau điều trị.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng gemcitabine hoặc các thành phần khác',
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'],
        'tương_đối': [
        'Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục',
        'Suy thận (CrCl <30) - giảm liều 25-50%, theo dõi chặt chẽ',
        'Suy gan - thận trọng, có thể cần giảm liều',
        'Bệnh phổi - tăng nguy cơ độc phổi',
        'Bệnh nhân cao tuổi - tăng nguy cơ độc tính']},
        'pregnancy_lactation': {
        'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Gemcitabine gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Gemcitabine bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.'
        , 'recommendation':
        'Không cho con bú khi dùng gemcitabine. Ngừng cho con bú hoặc ngừng thuốc.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể cần giảm liều', 'severe':
        'Thận trọng, giảm liều 25-50%', 'notes':
        'Gemcitabine chuyển hóa một phần qua gan (deamination). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ.'},
        'overdose_management': {'symptoms': [
        'Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)',
        'Độc phổi (viêm phổi kẽ - khó thở, ho, đau ngực)',
        'Buồn nôn, nôn nặng', 'Độc gan (tăng transaminase)'],
        'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment': [
        'Ngừng ngay gemcitabine',
        'Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần',
        'Theo dõi CBC, chức năng gan, chức năng thận',
        'Điều trị độc phổi: corticosteroid nếu có viêm phổi kẽ',
        'Theo dõi và điều trị triệu chứng'],
        'monitoring':
        'CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc phổi'},
        'reversal_agents': {'available': False, 'agents': [],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Điều trị độc phổi (corticosteroid nếu có viêm phổi kẽ), độc tính máu, và nhiễm trùng hỗ trợ.'},
        'administration_instructions': {'oral': None, 'iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất. Nồng độ cuối: ≤40mg/ml.',
        'infusion_rate': 'Truyền trong 30 phút (tốc độ tiêu chuẩn)',
        'compatibility': ['NS', 'D5W'],
        'incompatibility': [],
        'notes':
        'Truyền trong 30 phút. Theo dõi extravasation. Có thể phối hợp với cisplatin, carboplatin, hoặc paclitaxel.'}},
        'references': {'primary_sources': ['FDA Drug Label - Gemcitabine (Gemzar)',
        'UpToDate - Gemcitabine Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05', 'evidence_level':
        'High (FDA-approved, extensive clinical data)'}},
    "Capecitabine": {
        "group": "Oncology - Antimetabolite",
        "vietnamese_name": "Capecitabine, Xeloda",
        "administration": ["PO"],
        "indications": [
            "Ung thư đại trực tràng (adjuvant và metastatic)",
            "Ung thư vú (metastatic)",
            "Ung thư dạ dày (metastatic)",
            "Ung thư tụy (metastatic)"
        ],
        "contraindications": [
            "Dị ứng capecitabine",
            "Thiếu hụt DPD (dihydropyrimidine dehydrogenase) nặng",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_standard": "1250mg/m² PO x 2 lần/ngày (ngày 1-14, mỗi 21 ngày)",
            "adult_reduced": "1000mg/m² PO x 2 lần/ngày nếu độc tính",
            "notes": "Uống với thức ăn (30 phút sau bữa ăn). Capecitabine là prodrug của 5-FU, chuyển hóa thành 5-FU trong tế bào ung thư. Dạng uống, tiện lợi hơn 5-FU IV."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30)"
        },
        "side_effects": [
            "Loét miệng (stomatitis - phổ biến)",
            "Tiêu chảy (phổ biến, có thể nặng)",
            "Hội chứng bàn tay-bàn chân (hand-foot syndrome - phổ biến, đặc trưng)",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Buồn nôn, nôn",
            "Mệt mỏi",
            "Độc tim (hiếm nhưng nguy hiểm)",
            "Tăng bilirubin"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu - theo dõi INR",
            "Phenytoin: tăng nồng độ phenytoin",
            "Leucovorin: tăng hiệu quả và độc tính"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Capecitabine là prodrug của 5-fluorouracil (5-FU), được chuyển hóa thành 5-FU trong tế bào ung thư qua 3 bước: (1) Capecitabine → 5'-deoxy-5-fluorocytidine (5'-DFCR) bởi carboxylesterase ở gan, (2) 5'-DFCR → 5'-deoxy-5-fluorouridine (5'-DFUR) bởi cytidine deaminase, (3) 5'-DFUR → 5-FU bởi thymidine phosphorylase (TP) trong tế bào ung thư. 5-FU sau đó chuyển hóa thành 5-fluorodeoxyuridine monophosphate (FdUMP) và 5-fluorouridine triphosphate (FUTP). FdUMP ức chế thymidylate synthase (TS), ngăn tổng hợp thymidine (thành phần DNA). FUTP tích hợp vào RNA, gây rối loạn tổng hợp protein. ĐẶC ĐIỂM: (1) Dạng uống của 5-FU, tiện lợi hơn 5-FU IV, (2) Chuyển hóa thành 5-FU trong tế bào ung thư (do TP cao hơn ở tế bào ung thư), (3) Tác dụng phụ tương tự 5-FU: loét miệng, tiêu chảy, myelosuppression, (4) Hội chứng bàn tay-bàn chân (hand-foot syndrome) - đặc trưng của capecitabine, (5) CHỐNG CHỈ ĐỊNH ở thiếu hụt DPD nặng (tương tự 5-FU).",
        "monitoring": [
            "Công thức máu toàn phần (CBC) trước mỗi chu kỳ và giữa các chu kỳ",
            "Chức năng gan (ALT, AST, bilirubin) trước và trong điều trị",
            "Dấu hiệu loét miệng (stomatitis) - phổ biến",
            "Dấu hiệu tiêu chảy - phổ biến, có thể nặng",
            "Hội chứng bàn tay-bàn chân (hand-foot syndrome) - phổ biến, đặc trưng",
            "Dấu hiệu độc tim (đau ngực, khó thở, rối loạn nhịp) - hiếm nhưng nguy hiểm",
            "Test DPD trước điều trị nếu có thể (thiếu hụt DPD gây độc tính nặng)",
            "INR nếu dùng với warfarin"
        ],
        "precautions": [
            "Test DPD trước điều trị nếu có thể (thiếu hụt DPD gây độc tính nặng, có thể tử vong)",
            "Uống với thức ăn (30 phút sau bữa ăn) để tăng hấp thu",
            "Hội chứng bàn tay-bàn chân (hand-foot syndrome) - phổ biến, đặc trưng, giảm liều hoặc ngừng nếu nặng",
            "Giảm liều hoặc ngừng nếu có loét miệng nặng hoặc tiêu chảy nặng",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30)",
            "Theo dõi sát công thức máu (nguy cơ giảm bạch cầu, tiểu cầu)",
            "Tương tác với warfarin (tăng nguy cơ chảy máu - theo dõi INR)",
            "Giảm liều 25% nếu suy thận (CrCl 30-60)"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ (capecitabine), 10-20 phút (5-FU)",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "Dài (do chuyển hóa thành 5-FU trong tế bào)",
            "protein_binding": "Minimal",
            "metabolism": "Gan (carboxylesterase, cytidine deaminase), sau đó chuyển hóa thành 5-FU trong tế bào ung thư (thymidine phosphorylase), cuối cùng chuyển hóa 5-FU qua DPD",
            "clearance": "Gan, thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Thiếu hụt DPD (dihydropyrimidine dehydrogenase) có thể gây độc tính nặng và tử vong. Nên test DPD trước điều trị nếu có thể. Theo dõi sát độc tính và ngừng ngay nếu có dấu hiệu độc tính nặng. CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Capecitabine/5-FU có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc ngừng capecitabine. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Phenytoin",
                    "mechanism": "Capecitabine/5-FU có thể ức chế chuyển hóa phenytoin",
                    "effect": "Tăng nồng độ phenytoin, tăng độc tính phenytoin",
                    "management": "Theo dõi nồng độ phenytoin và dấu hiệu độc tính. Có thể cần giảm liều phenytoin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng capecitabine",
                "Thiếu hụt DPD (dihydropyrimidine dehydrogenase) nặng - CHỐNG CHỈ ĐỊNH (có thể tử vong)",
                "Có thai - CHỐNG CHỈ ĐỊNH (category D)",
                "Đang cho con bú - CHỐNG CHỈ ĐỊNH",
                "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị",
                "Suy thận (CrCl 30-60) - giảm liều 25%",
                "Suy gan - thận trọng",
                "Bệnh nhân cao tuổi - tăng nguy cơ độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Capecitabine (chuyển hóa thành 5-FU) gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Capecitabine và 5-FU bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng capecitabine. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Capecitabine chuyển hóa qua gan (carboxylesterase, cytidine deaminase). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Loét miệng nặng (stomatitis)",
                "Tiêu chảy nặng, mất nước",
                "Hội chứng bàn tay-bàn chân nặng",
                "Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)",
                "Độc tim (hiếm)",
                "Tăng bilirubin"
            ],
            "antidote": "Uridine triacetate (Vistogard) - antidote đặc hiệu cho quá liều 5-FU do thiếu hụt DPD",
            "treatment": [
                "Ngừng ngay capecitabine",
                "Nếu có thiếu hụt DPD và quá liều: dùng uridine triacetate (Vistogard) càng sớm càng tốt",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần",
                "Theo dõi CBC, chức năng gan, chức năng thận",
                "Điều trị loét miệng (súc miệng, thuốc giảm đau)",
                "Điều trị tiêu chảy (loperamide, bù dịch)",
                "Điều trị hội chứng bàn tay-bàn chân (giảm liều, thuốc bôi)"
            ],
            "monitoring": "CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc tim"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Uridine triacetate (Vistogard)",
                    "indication": "Quá liều capecitabine/5-FU do thiếu hụt DPD hoặc quá liều do lỗi dùng thuốc",
                    "dose": "10g PO x 3 lần/ngày x 5 ngày (bắt đầu càng sớm càng tốt)",
                    "notes": "Antidote đặc hiệu cho quá liều 5-FU. Hiệu quả nhất khi dùng trong vòng 96 giờ sau quá liều."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn (30 phút sau bữa ăn) để tăng hấp thu.",
                "timing": "1250mg/m² PO x 2 lần/ngày (ngày 1-14, mỗi 21 ngày). Uống với thức ăn (30 phút sau bữa ăn). Có thể giảm liều xuống 1000mg/m² x 2 lần/ngày nếu độc tính.",
                "notes": "QUAN TRỌNG: 1) Uống với thức ăn (30 phút sau bữa ăn), 2) Hội chứng bàn tay-bàn chân - phổ biến, đặc trưng, 3) Test DPD trước điều trị nếu có thể, 4) CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30), 5) Theo dõi INR nếu dùng với warfarin."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Capecitabine (Xeloda)",
                "UpToDate - Capecitabine: Drug Information",
                "NCCN Guidelines - Colorectal Cancer",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data"
        }
    }
}

# Import antimetabolite antifolates
from .antimetabolite_antifolates import ANTIMETABOLITE_ANTIFOLATES_DRUGS

# Merge with antifolates
_ANTIMETABOLITES_BASE = ANTIMETABOLITES_DRUGS.copy()
ANTIMETABOLITES_DRUGS = {
    **_ANTIMETABOLITES_BASE,
    **ANTIMETABOLITE_ANTIFOLATES_DRUGS,
}

__all__ = ['ANTIMETABOLITES_DRUGS']
