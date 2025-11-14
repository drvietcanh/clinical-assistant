"""Oncology Medications
Active module - contains all oncology drug data"""

# Antimetabolites

ANTIMETABOLITES_DRUGS = {
    "5-Fluorouracil": {'group': 'Oncology - Antimetabolite', 'vietnamese_name':
        '5-Fluorouracil, 5-FU, Fluorouracil', 'administration': ['IV'],
        'indications': ['Ung thư đại trực tràng (adjuvant và metastatic)',
        'Ung thư dạ dày', 'Ung thư đầu cổ', 'Ung thư tụy', 'Ung thư vú',
        'Ung thư da (topical)'], 'contraindications': ['Dị ứng 5-FU',
        'Thiếu hụt DPD (dihydropyrimidine dehydrogenase)',
        'Giảm bạch cầu/tiểu cầu nặng', 'Có thai', 'Đang cho con bú'], 'dosage':
        {'adult_bolus':
        '400-600mg/m² IV bolus ngày 1, sau đó 400-600mg/m²/ngày x 4 ngày (mỗi 4 tuần)'
        , 'adult_infusion':
        '1000mg/m²/ngày IV infusion x 4-5 ngày (mỗi 4 tuần)', 'adult_weekly':
        '500-600mg/m² IV mỗi tuần', 'adult_topical': '5% cream bôi 2 lần/ngày',
        'notes':
        'Phối hợp với leucovorin để tăng hiệu quả. Cần test DPD nếu có thể'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60':
        'Thận trọng, có thể giảm liều 25%', 'under_30':
        'Thận trọng, giảm liều 25-50%'}, 'side_effects': [
        'Loét miệng (stomatitis - phổ biến)',
        'Tiêu chảy (phổ biến, có thể nặng)',
        'Giảm bạch cầu, tiểu cầu (myelosuppression)', 'Ban da', 'Rụng tóc',
        'Độc tim (hiếm nhưng nguy hiểm)', 'Rối loạn thần kinh (hiếm)',
        'Tăng bilirubin'], 'interactions': [
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
        ,
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
        'Giảm liều 25-50% nếu suy thận'], 'pharmacokinetics': {'half_life':
        '10-20 phút (ngắn)', 'onset': '1-2 tuần (tác dụng lâm sàng)',
        'duration': '4-6 giờ (tác dụng sinh học)', 'protein_binding': 'Minimal',
        'clearance':
        'Gan (chuyển hóa qua DPD - dihydropyrimidine dehydrogenase), thận (thải trừ)'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu'
        , 'black_box_warnings':
        'Thiếu hụt DPD (dihydropyrimidine dehydrogenase) có thể gây độc tính nặng và tử vong. Nên test DPD trước điều trị nếu có thể. Theo dõi sát độc tính và ngừng ngay nếu có dấu hiệu độc tính nặng'
        , 'drug_interactions': {'major': [{'drug': 'Methotrexate', 'mechanism':
        'Cả hai đều là antimetabolite, tác dụng cộng dồn làm tăng độc tính tủy xương và niêm mạc.'
        , 'effect':
        'Tăng nguy cơ giảm bạch cầu, tiểu cầu, loét miệng, tiêu chảy nghiêm trọng',
        'management':
        'Thận trọng khi dùng đồng thời. Theo dõi CBC và dấu hiệu độc tính chặt chẽ. Có thể cần giảm liều hoặc tránh dùng đồng thời.'
        }], 'moderate': [{'drug': 'Warfarin', 'mechanism':
        '5-FU có thể ức chế chuyển hóa warfarin, tăng nồng độ warfarin trong máu.',
        'effect': 'Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu',
        'management':
        'Theo dõi INR chặt chẽ khi bắt đầu hoặc ngừng 5-FU. Có thể cần giảm liều warfarin.'
        }, {'drug': 'Phenytoin', 'mechanism':
        '5-FU có thể ức chế chuyển hóa phenytoin, tăng nồng độ phenytoin trong máu.'
        , 'effect': 'Tăng nồng độ phenytoin, tăng độc tính phenytoin',
        'management':
        'Theo dõi nồng độ phenytoin và dấu hiệu độc tính. Có thể cần giảm liều phenytoin.'
        }], 'minor': [{'drug': 'Leucovorin', 'mechanism':
        'Leucovorin tăng hiệu quả của 5-FU bằng cách tăng ức chế thymidylate synthase, nhưng cũng tăng độc tính.'
        , 'effect': 'Tăng hiệu quả và độc tính của 5-FU', 'management':
        'Dùng kèm để tăng hiệu quả, nhưng cần theo dõi độc tính chặt chẽ hơn.'}
        ]}, 'contraindications': {'tuyệt_đối': ['Dị ứng 5-FU',
        'Thiếu hụt DPD (dihydropyrimidine dehydrogenase) nặng - chống chỉ định tuyệt đối, có thể gây tử vong'
        ,
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'], 'tương_đối': [
        'Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục',
        'Suy thận (CrCl <30) - giảm liều 25-50%, theo dõi chặt chẽ',
        'Suy gan - thận trọng, có thể cần giảm liều',
        'Bệnh nhân cao tuổi - tăng nguy cơ độc tính']}, 'pregnancy_lactation':
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
        }, 'overdose_management': {'symptoms': ['Loét miệng nặng (stomatitis)',
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
        'Theo dõi và điều trị độc tim nếu có'], 'monitoring':
        'CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc tim'
        }, 'reversal_agents': {'available': True, 'agents': [{'name':
        'Uridine triacetate (Vistogard)', 'indication':
        'Quá liều 5-FU do thiếu hụt DPD hoặc quá liều do lỗi dùng thuốc',
        'dose': '10g PO x 3 lần/ngày x 5 ngày (bắt đầu càng sớm càng tốt)',
        'notes':
        'Antidote đặc hiệu cho quá liều 5-FU. Hiệu quả nhất khi dùng trong vòng 96 giờ sau quá liều.'
        }]}, 'administration_instructions': {'oral': {'with_food':
        'Không áp dụng', 'timing': 'Không có dạng uống (chỉ có IV và topical)'},
        'iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất', 'infusion_rate':
        'Bolus: tiêm trực tiếp. Infusion: truyền trong 4-24 giờ tùy phác đồ',
        'compatibility': ['NS', 'D5W'], 'incompatibility': [], 'notes':
        'Bolus: 400-600mg/m² tiêm trực tiếp. Infusion: 1000mg/m²/ngày truyền trong 4-24 giờ. Theo dõi extravasation.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - 5-Fluorouracil',
        'UpToDate - 5-Fluorouracil Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-15', 'evidence_level':
        'High (FDA-approved, extensive clinical data)'}}}

__all__ = ['ANTIMETABOLITES_DRUGS']
