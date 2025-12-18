"""Oncology Medications
Active module - contains all oncology drug data"""

# Taxanes

TAXANES_DRUGS = {
    "Paclitaxel": {'group': 'Oncology - Taxane', 'vietnamese_name':
        'Paclitaxel, Taxol', 'administration': ['IV'], 'indications': [
        'Ung thư vú (adjuvant và metastatic)', 'Ung thư phổi không tế bào nhỏ (NSCLC)',
        'Ung thư buồng trứng', 'Ung thư tụy', 'Ung thư đầu cổ',
        'Kaposi sarcoma (AIDS-related)'], 'contraindications': [
        'Dị ứng paclitaxel hoặc Cremophor EL', 'Giảm bạch cầu nặng (ANC <1500)',
        'Có thai', 'Đang cho con bú'], 'dosage': {'adult_standard':
        '135-175mg/m² IV mỗi 3 tuần (truyền 3 giờ)',
        'adult_weekly': '80-100mg/m² IV mỗi tuần (truyền 1 giờ)',
        'adult_dose_dense': '175mg/m² IV mỗi 2 tuần (với G-CSF support)', 'notes':
        'Cần premedication với dexamethasone, diphenhydramine, H2 blocker để giảm phản ứng quá mẫn'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'}, 'side_effects': [
        'Phản ứng quá mẫn (hypersensitivity - phổ biến, nguy hiểm)',
        'Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến)',
        'Độc thần kinh ngoại biên (tê bì, dị cảm - phổ biến, tích lũy)',
        'Rụng tóc (phổ biến)', 'Buồn nôn, nôn (nhẹ đến trung bình)',
        'Đau cơ, đau khớp (phổ biến)', 'Độc tim (bradycardia, rối loạn nhịp - hiếm)',
        'Độc gan (tăng transaminase - hiếm)'], 'interactions': [
        'Cisplatin: tăng độc tính (dùng paclitaxel trước cisplatin)',
        'Doxorubicin: có thể tăng độc tim',
        'Ketoconazole: tăng nồng độ paclitaxel (tránh dùng)',
        'CYP2C8 inhibitors: tăng nồng độ paclitaxel'], 'pregnancy':
        'D - Chống chỉ định', 'mechanism_of_action':
        'Paclitaxel là taxane, ổn định microtubules bằng cách gắn vào beta-tubulin, ngăn cản quá trình depolymerization (phân giải) của microtubules. Điều này ngăn chặn quá trình phân chia tế bào (mitosis) ở giai đoạn metaphase, dẫn đến chết tế bào. Microtubules là cấu trúc quan trọng cho quá trình phân chia tế bào, vận chuyển nội bào, và duy trì hình dạng tế bào. Bằng cách ổn định microtubules, paclitaxel gây rối loạn chức năng tế bào và chết tế bào ung thư. Paclitaxel tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. Hiệu quả với nhiều loại ung thư, đặc biệt ung thư vú, phổi, buồng trứng.'
        , 'monitoring': [
        'Phản ứng quá mẫn (hypersensitivity) - theo dõi trong 30 phút đầu truyền (phổ biến, nguy hiểm)'
        , 'Công thức máu toàn phần (CBC) trước mỗi chu kỳ (theo dõi giảm bạch cầu, tiểu cầu - phổ biến)'
        , 'Độc thần kinh ngoại biên (tê bì, dị cảm tay chân) - phổ biến, tích lũy, có thể không hồi phục'
        , 'Dấu hiệu nhiễm trùng (sốt, ớn lạnh) do giảm bạch cầu',
        'Dấu hiệu độc tim (bradycardia, rối loạn nhịp) - hiếm nhưng nguy hiểm',
        'Chức năng gan (ALT, AST) trước và trong điều trị (độc gan hiếm)',
        'Dấu hiệu đau cơ, đau khớp - phổ biến'], 'precautions': [
        'CẦN PREMEDICATION với dexamethasone (20mg PO 12h và 6h trước), diphenhydramine (50mg IV), H2 blocker (ranitidine 50mg IV) để giảm phản ứng quá mẫn - QUAN TRỌNG'
        , 'Theo dõi sát trong 30 phút đầu truyền (phản ứng quá mẫn thường xảy ra trong 10 phút đầu)'
        , 'Giảm liều hoặc trì hoãn điều trị nếu giảm bạch cầu nặng (ANC <1500)',
        'Độc thần kinh ngoại biên - phổ biến, tích lũy, có thể không hồi phục, giảm liều hoặc ngừng nếu nặng'
        , 'Tương tác với cisplatin (tăng độc tính - dùng paclitaxel trước cisplatin)',
        'Tương tác với doxorubicin (có thể tăng độc tim)',
        'Tránh dùng với ketoconazole (tăng nồng độ paclitaxel)',
        'Truyền qua filter không chứa DEHP (Cremophor EL có thể hòa tan DEHP)'], 'pharmacokinetics': {
        'half_life': '5-17 giờ (dài)', 'onset': '1-2 tuần (tác dụng lâm sàng)',
        'duration': '24-48 giờ (tác dụng sinh học)', 'protein_binding': '89-98%',
        'clearance':
        'Gan (chuyển hóa qua CYP2C8, CYP3A4), thận (thải trừ - ít, <5%)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Pha với NS hoặc D5W. Dùng filter không chứa DEHP.'
        , 'black_box_warnings':
        'Phản ứng quá mẫn (hypersensitivity) phổ biến và có thể nghiêm trọng, có thể tử vong. CẦN PREMEDICATION với dexamethasone, diphenhydramine, H2 blocker. Theo dõi sát trong 30 phút đầu truyền. Độc thần kinh ngoại biên phổ biến, tích lũy, có thể không hồi phục.'
        , 'drug_interactions': {'major': [{'drug': 'Cisplatin', 'mechanism':
        'Cả hai đều gây độc tính, tác dụng cộng dồn', 'effect':
        'Tăng độc tính tủy xương và thần kinh', 'management':
        'Dùng paclitaxel trước cisplatin (giảm độc tính). Theo dõi CBC và độc thần kinh chặt chẽ.'}, {
        'drug': 'Ketoconazole, Itraconazole', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ paclitaxel', 'effect':
        'Tăng nồng độ paclitaxel, tăng độc tính', 'management':
        'Tránh dùng với ketoconazole, itraconazole. Nếu phải dùng, giảm liều paclitaxel.'}],
        'moderate': [{'drug': 'Doxorubicin', 'mechanism':
        'Cả hai đều có thể gây độc tim', 'effect': 'Tăng nguy cơ độc tim', 'management':
        'Theo dõi chức năng tim chặt chẽ. Có thể cần giảm liều hoặc tránh dùng đồng thời.'}],
        'minor': [{'drug': 'CYP2C8 inhibitors (gemfibrozil)', 'mechanism':
        'Ức chế chuyển hóa paclitaxel', 'effect': 'Tăng nồng độ paclitaxel', 'management':
        'Thận trọng, có thể cần giảm liều paclitaxel.'}]}, 'contraindications': {
        'tuyệt_đối': [
        'Dị ứng paclitaxel hoặc Cremophor EL (chất phụ gia)',
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'], 'tương_đối': [
        'Giảm bạch cầu nặng (ANC <1500) - trì hoãn điều trị cho đến khi hồi phục',
        'Độc thần kinh ngoại biên nặng - giảm liều hoặc ngừng',
        'Suy gan - thận trọng, có thể cần giảm liều',
        'Bệnh tim - tăng nguy cơ độc tim',
        'Bệnh nhân cao tuổi - tăng nguy cơ độc tính']}, 'pregnancy_lactation': {
        'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Paclitaxel gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Paclitaxel bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.'
        , 'recommendation':
        'Không cho con bú khi dùng paclitaxel. Ngừng cho con bú hoặc ngừng thuốc.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể cần giảm liều 25%', 'severe':
        'Thận trọng, giảm liều 25-50%', 'notes':
        'Paclitaxel chuyển hóa chủ yếu qua gan (CYP2C8, CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ.'},
        'overdose_management': {'symptoms': [
        'Phản ứng quá mẫn nặng (sốc phản vệ - nguy hiểm tính mạng)',
        'Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)',
        'Độc thần kinh ngoại biên nặng (tê bì, dị cảm, yếu cơ)',
        'Độc tim (bradycardia, rối loạn nhịp)', 'Độc gan (tăng transaminase)'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment': [
        'Ngừng ngay paclitaxel',
        'Xử trí phản ứng quá mẫn: epinephrine, diphenhydramine, corticosteroid, H2 blocker, hỗ trợ hô hấp'
        , 'Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần',
        'Theo dõi CBC, chức năng gan, chức năng thận',
        'Theo dõi và điều trị triệu chứng'], 'monitoring':
        'CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc thần kinh, dấu hiệu độc tim'},
        'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': None, 'iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất. Nồng độ cuối: 0.3-1.2mg/ml. Dùng filter không chứa DEHP (Cremophor EL có thể hòa tan DEHP).',
        'infusion_rate':
        'Truyền trong 3 giờ (phác đồ 3 tuần) hoặc 1 giờ (phác đồ hàng tuần). Theo dõi sát trong 30 phút đầu.',
        'premedication':
        'CẦN PREMEDICATION: Dexamethasone 20mg PO 12h và 6h trước, Diphenhydramine 50mg IV, H2 blocker (ranitidine 50mg IV) trước truyền.',
        'compatibility': ['NS', 'D5W'], 'incompatibility': ['DEHP-containing filters'],
        'notes':
        'Truyền qua filter không chứa DEHP. Theo dõi sát trong 30 phút đầu (phản ứng quá mẫn). Có thể phối hợp với carboplatin, cisplatin, hoặc doxorubicin.'}},
        'references': {'primary_sources': ['FDA Drug Label - Paclitaxel (Taxol)',
        'UpToDate - Paclitaxel Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05', 'evidence_level':
        'High (FDA-approved, extensive clinical data)'}},
    "Docetaxel": {'group': 'Oncology - Taxane', 'vietnamese_name':
        'Docetaxel, Taxotere', 'administration': ['IV'], 'indications': [
        'Ung thư vú (adjuvant và metastatic)', 'Ung thư phổi không tế bào nhỏ (NSCLC)',
        'Ung thư tuyến tiền liệt (castration-resistant)', 'Ung thư dạ dày',
        'Ung thư đầu cổ'], 'contraindications': ['Dị ứng docetaxel hoặc polysorbate 80',
        'Giảm bạch cầu nặng (ANC <1500)', 'Có thai', 'Đang cho con bú'], 'dosage': {
        'adult_standard': '60-100mg/m² IV mỗi 3 tuần (truyền 1 giờ)',
        'adult_weekly': '30-40mg/m² IV mỗi tuần (truyền 1 giờ)',
        'adult_prostate': '75mg/m² IV mỗi 3 tuần (với prednisone)', 'notes':
        'Cần premedication với dexamethasone để giảm phản ứng quá mẫn và giữ nước'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'}, 'side_effects': [
        'Phản ứng quá mẫn (hypersensitivity - phổ biến, nguy hiểm)',
        'Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến)',
        'Độc thần kinh ngoại biên (tê bì, dị cảm - phổ biến, tích lũy)',
        'Giữ nước (fluid retention - phổ biến, tích lũy)',
        'Rụng tóc (phổ biến)', 'Buồn nôn, nôn (nhẹ đến trung bình)',
        'Đau cơ, đau khớp (phổ biến)', 'Độc gan (tăng transaminase - phổ biến)',
        'Độc da (rash, nail changes - phổ biến)'], 'interactions': [
        'Cisplatin: tăng độc tính (dùng docetaxel trước cisplatin)',
        'Ketoconazole: tăng nồng độ docetaxel (tránh dùng)',
        'CYP3A4 inhibitors: tăng nồng độ docetaxel',
        'CYP3A4 inducers: giảm nồng độ docetaxel'], 'pregnancy':
        'D - Chống chỉ định', 'mechanism_of_action':
        'Docetaxel là taxane, tương tự paclitaxel, ổn định microtubules bằng cách gắn vào beta-tubulin, ngăn cản quá trình depolymerization (phân giải) của microtubules. Điều này ngăn chặn quá trình phân chia tế bào (mitosis) ở giai đoạn metaphase, dẫn đến chết tế bào. Docetaxel có ái lực cao hơn với beta-tubulin so với paclitaxel, nên hiệu quả mạnh hơn. Docetaxel tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. Hiệu quả với nhiều loại ung thư, đặc biệt ung thư vú, phổi, tuyến tiền liệt.'
        , 'monitoring': [
        'Phản ứng quá mẫn (hypersensitivity) - theo dõi trong 30 phút đầu truyền (phổ biến, nguy hiểm)'
        , 'Công thức máu toàn phần (CBC) trước mỗi chu kỳ (theo dõi giảm bạch cầu, tiểu cầu - phổ biến)'
        , 'Độc thần kinh ngoại biên (tê bì, dị cảm tay chân) - phổ biến, tích lũy, có thể không hồi phục'
        , 'Giữ nước (fluid retention) - phổ biến, tích lũy, theo dõi cân nặng, phù ngoại biên'
        , 'Dấu hiệu nhiễm trùng (sốt, ớn lạnh) do giảm bạch cầu',
        'Chức năng gan (ALT, AST) trước và trong điều trị (độc gan phổ biến)',
        'Dấu hiệu đau cơ, đau khớp - phổ biến',
        'Dấu hiệu độc da (rash, nail changes) - phổ biến'], 'precautions': [
        'CẦN PREMEDICATION với dexamethasone (8mg PO x 2 lần/ngày x 3 ngày, bắt đầu 1 ngày trước) để giảm phản ứng quá mẫn và giữ nước - QUAN TRỌNG'
        , 'Theo dõi sát trong 30 phút đầu truyền (phản ứng quá mẫn thường xảy ra trong 10 phút đầu)'
        , 'Giảm liều hoặc trì hoãn điều trị nếu giảm bạch cầu nặng (ANC <1500)',
        'Độc thần kinh ngoại biên - phổ biến, tích lũy, có thể không hồi phục, giảm liều hoặc ngừng nếu nặng'
        , 'Giữ nước (fluid retention) - phổ biến, tích lũy, có thể nặng, cần premedication với dexamethasone'
        , 'Tương tác với cisplatin (tăng độc tính - dùng docetaxel trước cisplatin)',
        'Tránh dùng với ketoconazole (tăng nồng độ docetaxel)',
        'Tương tác với CYP3A4 inhibitors/inducers (ảnh hưởng nồng độ docetaxel)'], 'pharmacokinetics': {
        'half_life': '11 giờ (dài)', 'onset': '1-2 tuần (tác dụng lâm sàng)',
        'duration': '24-48 giờ (tác dụng sinh học)', 'protein_binding': '94%',
        'clearance':
        'Gan (chuyển hóa qua CYP3A4), thận (thải trừ - ít, <5%)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Pha với NS hoặc D5W.'
        , 'black_box_warnings':
        'Phản ứng quá mẫn (hypersensitivity) phổ biến và có thể nghiêm trọng, có thể tử vong. CẦN PREMEDICATION với dexamethasone. Theo dõi sát trong 30 phút đầu truyền. Độc thần kinh ngoại biên phổ biến, tích lũy, có thể không hồi phục. Giữ nước (fluid retention) phổ biến, tích lũy, có thể nặng.'
        , 'drug_interactions': {'major': [{'drug': 'Cisplatin', 'mechanism':
        'Cả hai đều gây độc tính, tác dụng cộng dồn', 'effect':
        'Tăng độc tính tủy xương và thần kinh', 'management':
        'Dùng docetaxel trước cisplatin (giảm độc tính). Theo dõi CBC và độc thần kinh chặt chẽ.'}, {
        'drug': 'Ketoconazole, Itraconazole', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ docetaxel', 'effect':
        'Tăng nồng độ docetaxel, tăng độc tính', 'management':
        'Tránh dùng với ketoconazole, itraconazole. Nếu phải dùng, giảm liều docetaxel.'}],
        'moderate': [{'drug': 'CYP3A4 inducers (Rifampin, Carbamazepine)', 'mechanism':
        'Cảm ứng CYP3A4, giảm nồng độ docetaxel', 'effect':
        'Giảm nồng độ docetaxel, giảm hiệu quả', 'management':
        'Theo dõi đáp ứng điều trị. Có thể cần tăng liều docetaxel.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng docetaxel hoặc polysorbate 80 (chất phụ gia)',
        'Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)',
        'Đang cho con bú - chống chỉ định'], 'tương_đối': [
        'Giảm bạch cầu nặng (ANC <1500) - trì hoãn điều trị cho đến khi hồi phục',
        'Độc thần kinh ngoại biên nặng - giảm liều hoặc ngừng',
        'Suy gan - CHỐNG CHỈ ĐỊNH (docetaxel chuyển hóa qua gan, suy gan tăng độc tính nghiêm trọng)'
        , 'Giữ nước nặng - giảm liều hoặc ngừng',
        'Bệnh nhân cao tuổi - tăng nguy cơ độc tính']}, 'pregnancy_lactation': {
        'fda_category': 'D', 'pregnancy_details':
        'Chống chỉ định trong thai kỳ. Docetaxel gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.'
        , 'lactation': {'safety': 'Incompatible', 'details':
        'Docetaxel bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.'
        , 'recommendation':
        'Không cho con bú khi dùng docetaxel. Ngừng cho con bú hoặc ngừng thuốc.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'CHỐNG CHỈ ĐỊNH - docetaxel chuyển hóa qua gan, suy gan tăng độc tính nghiêm trọng',
        'severe':
        'CHỐNG CHỈ ĐỊNH - docetaxel chuyển hóa qua gan, suy gan tăng độc tính nghiêm trọng', 'notes':
        'Docetaxel chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính nghiêm trọng. CHỐNG CHỈ ĐỊNH trong suy gan.'},
        'overdose_management': {'symptoms': [
        'Phản ứng quá mẫn nặng (sốc phản vệ - nguy hiểm tính mạng)',
        'Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)',
        'Độc thần kinh ngoại biên nặng (tê bì, dị cảm, yếu cơ)',
        'Giữ nước nặng (phù ngoại biên, tràn dịch màng phổi, màng bụng)',
        'Độc gan (tăng transaminase)'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment': [
        'Ngừng ngay docetaxel',
        'Xử trí phản ứng quá mẫn: epinephrine, diphenhydramine, corticosteroid, H2 blocker, hỗ trợ hô hấp'
        , 'Xử trí giữ nước: furosemide, hạn chế muối, theo dõi cân nặng',
        'Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần',
        'Theo dõi CBC, chức năng gan, chức năng thận',
        'Theo dõi và điều trị triệu chứng'], 'monitoring':
        'CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc thần kinh, dấu hiệu giữ nước (cân nặng, phù)'},
        'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': None, 'iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất. Nồng độ cuối: 0.3-0.9mg/ml.',
        'infusion_rate':
        'Truyền trong 1 giờ. Theo dõi sát trong 30 phút đầu.',
        'premedication':
        'CẦN PREMEDICATION: Dexamethasone 8mg PO x 2 lần/ngày x 3 ngày, bắt đầu 1 ngày trước truyền để giảm phản ứng quá mẫn và giữ nước.',
        'compatibility': ['NS', 'D5W'], 'incompatibility': [],
        'notes':
        'Theo dõi sát trong 30 phút đầu (phản ứng quá mẫn). Có thể phối hợp với carboplatin, cisplatin, hoặc prednisone (ung thư tuyến tiền liệt).'}},
        'references': {'primary_sources': ['FDA Drug Label - Docetaxel (Taxotere)',
        'UpToDate - Docetaxel Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-02-05', 'evidence_level':
        'High (FDA-approved, extensive clinical data)'}}
}

__all__ = ['TAXANES_DRUGS']

























