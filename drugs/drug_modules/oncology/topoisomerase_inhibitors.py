"""Oncology Medications
Active module - contains all oncology drug data"""

# Topoisomerase Inhibitors

TOPOISOMERASE_INHIBITORS_DRUGS = {
    "Irinotecan": {'group': 'Oncology - Topoisomerase Inhibitor', 'vietnamese_name':
        'Irinotecan, Camptosar, CPT-11', 'administration': ['IV'], 'indications': [
        'Ung thư đại trực tràng (metastatic)', 'Ung thư phổi không tế bào nhỏ (NSCLC)',
        'Ung thư tụy', 'Ung thư cổ tử cung'], 'contraindications': [
        'Dị ứng irinotecan', 'Giảm bạch cầu nặng (ANC <1500)',
        'Tiêu chảy nặng đang diễn ra', 'Có thai', 'Đang cho con bú'], 'dosage': {
        'adult_standard': '125mg/m² IV ngày 1, 8, 15, 22 (mỗi 6 tuần) hoặc 350mg/m² IV mỗi 3 tuần',
        'adult_folfiri': '180mg/m² IV ngày 1 (mỗi 2 tuần, với 5-FU và leucovorin)',
        'notes':
        'Cần premedication với atropine để giảm cholinergic syndrome. Theo dõi sát tiêu chảy'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Thận trọng, có thể giảm liều'}, 'side_effects': [
        'Tiêu chảy (phổ biến, có thể nặng và nguy hiểm) - sớm (cholinergic) và muộn (độc tính)'
        , 'Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến)',
        'Buồn nôn, nôn (phổ biến)', 'Cholinergic syndrome (đổ mồ hôi, chảy nước mũi, tăng tiết nước bọt - sớm)'
        , 'Rụng tóc (phổ biến)', 'Mệt mỏi',
        'Độc gan (tăng transaminase - hiếm)'], 'interactions': [
        '5-Fluorouracil: tăng độc tính tủy xương và tiêu chảy',
        'Ketoconazole: tăng nồng độ irinotecan (tránh dùng)',
        'CYP3A4 inhibitors: tăng nồng độ irinotecan',
        'CYP3A4 inducers: giảm nồng độ irinotecan',
        'Atropine: giảm cholinergic syndrome (dùng kèm)'], 'pregnancy':
        'D - Chống chỉ định', 'mechanism_of_action':
        'Irinotecan là topoisomerase I inhibitor (camptothecin derivative). Irinotecan là prodrug, được chuyển hóa ở gan thành SN-38 (chất hoạt động). SN-38 ức chế enzyme topoisomerase I, ngăn cản quá trình sửa chữa DNA sau khi sao chép. Topoisomerase I là enzyme quan trọng để tháo xoắn DNA trong quá trình sao chép và phiên mã. Bằng cách ức chế topoisomerase I, SN-38 gây đứt gãy DNA và chết tế bào. Irinotecan tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. Hiệu quả với ung thư đại trực tràng, phổi, tụy. Độc tính chính: tiêu chảy (sớm - cholinergic, muộn - độc tính) và myelosuppression.'
        , 'monitoring': [
        'Tiêu chảy - theo dõi sát (phổ biến, có thể nặng và nguy hiểm) - sớm (cholinergic, trong 24h) và muộn (độc tính, sau 24h)'
        , 'Công thức máu toàn phần (CBC) trước mỗi chu kỳ (theo dõi giảm bạch cầu, tiểu cầu - phổ biến)'
        , 'Cholinergic syndrome (đổ mồ hôi, chảy nước mũi, tăng tiết nước bọt, co thắt bụng) - sớm, trong 24h sau truyền'
        , 'Dấu hiệu nhiễm trùng (sốt, ớn lạnh) do giảm bạch cầu',
        'Chức năng gan (ALT, AST) trước và trong điều trị (độc gan hiếm)',
        'Dấu hiệu mất nước do tiêu chảy'], 'precautions': [
        'CẦN PREMEDICATION với atropine (0.25-1mg IV/SC) trước truyền để giảm cholinergic syndrome - QUAN TRỌNG'
        , 'Theo dõi sát tiêu chảy - phổ biến, có thể nặng và nguy hiểm, cần điều trị sớm'
        , 'Tiêu chảy sớm (cholinergic, trong 24h) - điều trị với atropine, loperamide'
        , 'Tiêu chảy muộn (độc tính, sau 24h) - điều trị với loperamide (4mg sau mỗi lần đi ngoài, tối đa 16mg/ngày), bù dịch'
        , 'Giảm liều hoặc trì hoãn điều trị nếu giảm bạch cầu nặng (ANC <1500)',
        'Giảm liều 25-50% nếu có tiêu chảy nặng ở chu kỳ trước',
        'Tương tác với 5-FU (tăng độc tính tủy xương và tiêu chảy)',
        'Tránh dùng với ketoconazole (tăng nồng độ irinotecan)',
        'Tương tác với CYP3A4 inhibitors/inducers (ảnh hưởng nồng độ irinotecan)'], 'pharmacokinetics': {
        'half_life': '6-12 giờ (irinotecan), 10-20 giờ (SN-38)', 'onset':
        '1-2 tuần (tác dụng lâm sàng)', 'duration': '24-48 giờ (tác dụng sinh học)',
        'protein_binding': '30-68% (irinotecan), 95% (SN-38)', 'clearance':
        'Gan (chuyển hóa irinotecan thành SN-38 qua CYP3A4, UGT1A1), thận (thải trừ - ít)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Pha với NS hoặc D5W.'
        , 'black_box_warnings':
        'Tiêu chảy phổ biến và có thể nặng, có thể tử vong. Theo dõi sát tiêu chảy và điều trị sớm. Tiêu chảy sớm (cholinergic, trong 24h) - điều trị với atropine. Tiêu chảy muộn (độc tính, sau 24h) - điều trị với loperamide, bù dịch. Giảm bạch cầu, tiểu cầu phổ biến. Thiếu hụt UGT1A1 (UGT1A1*28) tăng độc tính - nên test trước điều trị nếu có thể.'
        , 'drug_interactions': {'major': [{'drug': '5-Fluorouracil', 'mechanism':
        'Cả hai đều gây độc tính, tác dụng cộng dồn', 'effect':
        'Tăng độc tính tủy xương và tiêu chảy nghiêm trọng', 'management':
        'Theo dõi CBC và tiêu chảy chặt chẽ. Có thể cần giảm liều hoặc trì hoãn điều trị.'}, {
        'drug': 'Ketoconazole, Itraconazole', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ irinotecan và SN-38', 'effect':
        'Tăng nồng độ irinotecan, tăng độc tính', 'management':
        'Tránh dùng với ketoconazole, itraconazole. Nếu phải dùng, giảm liều irinotecan 50%.'}],
        'moderate': [{'drug': 'CYP3A4 inducers (Rifampin, Carbamazepine)', 'mechanism':
        'Cảm ứng CYP3A4, giảm nồng độ irinotecan', 'effect':
        'Giảm nồng độ irinotecan, giảm hiệu quả', 'management':
        'Theo dõi đáp ứng điều trị. Có thể cần tăng liều irinotecan.'}, {'drug':
        'UGT1A1 inhibitors', 'mechanism':
        'Ức chế chuyển hóa SN-38, tăng nồng độ SN-38', 'effect':
        'Tăng nồng độ SN-38, tăng độc tính', 'management':
        'Thận trọng, có thể cần giảm liều irinotecan.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng irinotecan hoặc các thành phần khác',
        'Tiêu chảy nặng đang diễn ra - chống chỉ định cho đến khi hồi phục',
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'], 'tương_đối': [
        'Giảm bạch cầu nặng (ANC <1500) - trì hoãn điều trị cho đến khi hồi phục',
        'Thiếu hụt UGT1A1 (UGT1A1*28) - tăng độc tính, giảm liều 25-50%',
        'Suy gan - thận trọng, có thể cần giảm liều (irinotecan chuyển hóa qua gan)',
        'Suy thận - thận trọng, có thể cần giảm liều',
        'Bệnh nhân cao tuổi - tăng nguy cơ độc tính']}, 'pregnancy_lactation': {
        'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Irinotecan gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Irinotecan và SN-38 bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.'
        , 'recommendation':
        'Không cho con bú khi dùng irinotecan. Ngừng cho con bú hoặc ngừng thuốc.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể cần giảm liều 25%', 'severe':
        'Thận trọng, giảm liều 25-50%', 'notes':
        'Irinotecan chuyển hóa chủ yếu qua gan (CYP3A4, UGT1A1). Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ.'},
        'overdose_management': {'symptoms': [
        'Tiêu chảy nặng, mất nước (nguy hiểm tính mạng)',
        'Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)',
        'Cholinergic syndrome nặng (đổ mồ hôi, chảy nước mũi, co thắt bụng)',
        'Buồn nôn, nôn nặng', 'Độc gan (tăng transaminase)'], 'antidote':
        'Atropine cho cholinergic syndrome. Không có antidote đặc hiệu cho độc tính tổng thể.',
        'treatment': [
        'Ngừng ngay irinotecan',
        'Xử trí tiêu chảy: loperamide (4mg sau mỗi lần đi ngoài, tối đa 16mg/ngày), bù dịch, điện giải'
        , 'Xử trí cholinergic syndrome: atropine (0.25-1mg IV/SC)',
        'Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần',
        'Theo dõi CBC, chức năng gan, chức năng thận',
        'Theo dõi và điều trị triệu chứng'], 'monitoring':
        'CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu mất nước, dấu hiệu cholinergic syndrome'},
        'reversal_agents': {'available': True, 'agents': [{'name': 'Atropine',
        'indication': 'Cholinergic syndrome (đổ mồ hôi, chảy nước mũi, co thắt bụng)',
        'dose': '0.25-1mg IV/SC, có thể lặp lại', 'notes':
        'Điều trị cholinergic syndrome sớm (trong 24h sau truyền)'}]},
        'administration_instructions': {'oral': None, 'iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất. Nồng độ cuối: 0.12-2.8mg/ml.',
        'infusion_rate':
        'Truyền trong 30-90 phút. Theo dõi sát trong và sau truyền.',
        'premedication':
        'CẦN PREMEDICATION: Atropine 0.25-1mg IV/SC trước truyền để giảm cholinergic syndrome.',
        'compatibility': ['NS', 'D5W'], 'incompatibility': [],
        'notes':
        'Theo dõi sát tiêu chảy (phổ biến, có thể nặng). Có thể phối hợp với 5-FU và leucovorin (FOLFIRI regimen).'}},
        'references': {'primary_sources': ['FDA Drug Label - Irinotecan (Camptosar)',
        'UpToDate - Irinotecan Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05', 'evidence_level':
        'High (FDA-approved, extensive clinical data)'}}
}

__all__ = ['TOPOISOMERASE_INHIBITORS_DRUGS']

























