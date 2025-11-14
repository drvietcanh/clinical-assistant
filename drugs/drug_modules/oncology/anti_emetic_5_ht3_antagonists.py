"""Oncology Medications
Active module - contains all oncology drug data"""

# Anti-emetic (5-HT3 Antagonist)s

ANTI_EMETIC_(5_HT3_ANTAGONIST)S_DRUGS = {
    "Granisetron": {'group': 'Oncology - Anti-emetic (5-HT3 Antagonist)', 'vietnamese_name':
        'Granisetron, Kytril', 'administration': ['PO', 'IV'], 'indications': [
        'Phòng và điều trị nôn do hóa trị', 'Phòng nôn sau phẫu thuật',
        'Nôn do xạ trị'], 'contraindications': [
        'Dị ứng granisetron hoặc 5-HT3 antagonists'], 'dosage': {'adult_iv':
        '1mg IV x 1 lần trước hóa trị hoặc 0.01mg/kg IV', 'adult_po':
        '1-2mg PO x 1 lần trước hóa trị, có thể lặp lại sau 12 giờ',
        'adult_prevention': '1-2mg PO x 1-2 lần/ngày', 'notes':
        'Có thể dùng 30 phút - 1 giờ trước hóa trị'}, 'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Không đổi', 'under_30': 'Không đổi'},
        'side_effects': ['Đau đầu (phổ biến)', 'Táo bón', 'Chóng mặt',
        'Mệt mỏi', 'Tăng transaminase (hiếm)', 'QT kéo dài (hiếm)'],
        'interactions': ['Apomorphine: chống chỉ định (tăng tác dụng)',
        'Các 5-HT3 antagonists khác: không nên dùng đồng thời'], 'pregnancy':
        'B - Thận trọng', 'mechanism_of_action':
        'Granisetron là 5-HT3 receptor antagonist, ức chế chọn lọc receptor serotonin type 3 (5-HT3) ở cả ngoại vi (dây thần kinh phế vị trong ruột) và trung ương (vùng chemoreceptor trigger zone - CTZ). Thuốc ngăn cản serotonin gắn vào receptor 5-HT3, giảm kích thích gây nôn từ hóa trị và xạ trị. Granisetron có ái lực cao với receptor 5-HT3 và tác dụng kéo dài, hiệu quả trong phòng và điều trị nôn do hóa trị, đặc biệt với các thuốc gây nôn mạnh (cisplatin, doxorubicin)'
        , 'monitoring': ['Đáp ứng điều trị (giảm nôn, buồn nôn)',
        'Dấu hiệu đau đầu (phổ biến)', 'Dấu hiệu táo bón (phổ biến)',
        'Điện tâm đồ (ECG) nếu có nguy cơ QT kéo dài (hiếm)',
        'Chức năng gan nếu dùng lâu dài (tăng transaminase - hiếm)'],
        'precautions': [
        'Dùng 30 phút - 1 giờ trước hóa trị để đạt hiệu quả tối đa',
        'Có thể dùng IV hoặc PO',
        'Có thể dùng kết hợp với corticosteroid (dexamethasone) để tăng hiệu quả',
        'Tránh dùng với apomorphine (chống chỉ định)',
        'Không nên dùng đồng thời với các 5-HT3 antagonists khác',
        'Có thể gây QT kéo dài (hiếm - cần theo dõi nếu có nguy cơ)',
        'Có thể dùng trong thai kỳ (category B - thận trọng)'],
        'pharmacokinetics': {'half_life': '3-5 giờ (IV), 6-9 giờ (PO)', 'onset':
        '1-3 phút (IV), 30-60 phút (PO)', 'duration': '24 giờ',
        'protein_binding': '65%', 'clearance':
        'Gan (chuyển hóa qua CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Apomorphine', 'mechanism':
        'Granisetron ức chế 5-HT3 receptor, có thể tăng tác dụng của apomorphine, gây hạ huyết áp nghiêm trọng.'
        , 'effect':
        'Tăng tác dụng apomorphine, hạ huyết áp nghiêm trọng, nguy cơ tử vong',
        'management': 'CHỐNG CHỈ ĐỊNH - không dùng đồng thời.'}], 'moderate': [
        {'drug': 'Các 5-HT3 antagonists khác (Ondansetron, Palonosetron)',
        'mechanism':
        'Cả hai đều ức chế 5-HT3 receptor, không có lợi ích bổ sung.', 'effect':
        'Không tăng hiệu quả, có thể tăng tác dụng phụ', 'management':
        'Không nên dùng đồng thời. Chọn một trong hai.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng granisetron hoặc 5-HT3 antagonists'], 'tương_đối': [
        'Bệnh nhân có tiền sử QT kéo dài - thận trọng, theo dõi ECG',
        'Suy gan - thận trọng, có thể cần giảm liều']}, 'pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'Có thể dùng trong thai kỳ nếu cần. Không có bằng chứng dị tật thai nhi, nhưng dữ liệu còn hạn chế. Dùng với thận trọng.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Granisetron bài tiết vào sữa mẹ ở nồng độ thấp. Chưa có đủ dữ liệu về an toàn cho trẻ sơ sinh.'
        , 'recommendation':
        'Thận trọng khi cho con bú. Có thể dùng nếu lợi ích vượt trội nguy cơ.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể cần giảm liều', 'severe':
        'Thận trọng, giảm liều 25-50%', 'notes':
        'Granisetron chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ.'
        }, 'overdose_management': {'symptoms': ['Đau đầu nặng', 'Táo bón nặng',
        'Chóng mặt', 'QT kéo dài (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': ['Ngừng thuốc',
        'Supportive care', 'Theo dõi ECG nếu có QT kéo dài',
        'Điều trị táo bón nếu cần'], 'monitoring': 'ECG, dấu hiệu lâm sàng'},
        'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food': 'Có thể uống với hoặc không thức ăn', 'timing':
        'Uống 30 phút - 1 giờ trước hóa trị'}, 'iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất', 'infusion_rate':
        'Tiêm trực tiếp hoặc truyền trong 5 phút', 'compatibility': ['NS',
        'D5W'], 'incompatibility': [], 'notes':
        '1mg IV x 1 lần trước hóa trị hoặc 0.01mg/kg IV. Có thể tiêm trực tiếp hoặc truyền trong 5 phút.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Granisetron (Kytril)',
        'UpToDate - Granisetron Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-15', 'evidence_level':
        'High (FDA-approved, extensive clinical data)'}},
    "Palonosetron": {'group': 'Oncology - Anti-emetic (5-HT3 Antagonist)', 'vietnamese_name':
        'Palonosetron, Aloxi', 'administration': ['IV'], 'indications': [
        'Phòng nôn do hóa trị (ngắn và trung hạn)', 'Phòng nôn sau phẫu thuật'],
        'contraindications': ['Dị ứng palonosetron hoặc 5-HT3 antagonists'],
        'dosage': {'adult_chemotherapy': '0.25mg IV x 1 lần trước hóa trị',
        'adult_surgery': '0.075mg IV x 1 lần trước gây mê', 'notes':
        'Tác dụng dài (48-72 giờ), chỉ cần 1 liều'}, 'renal_adjustment': {
        'normal': 'Không đổi', '30_60': 'Không đổi', 'under_30': 'Không đổi'},
        'side_effects': ['Đau đầu', 'Táo bón', 'Chóng mặt', 'Mệt mỏi',
        'QT kéo dài (hiếm)'], 'interactions': ['Apomorphine: chống chỉ định'],
        'pregnancy': 'B - Thận trọng', 'mechanism_of_action':
        'Palonosetron là 5-HT3 receptor antagonist thế hệ 2, ức chế chọn lọc receptor serotonin type 3 (5-HT3) ở cả ngoại vi và trung ương. Palonosetron có ái lực cao hơn và thời gian bán thải dài hơn so với các 5-HT3 antagonists thế hệ 1 (ondansetron, granisetron), cho phép dùng 1 liều duy nhất để phòng nôn trong 48-72 giờ. Thuốc ngăn cản serotonin gắn vào receptor 5-HT3, giảm kích thích gây nôn từ hóa trị. Palonosetron đặc biệt hiệu quả với hóa trị gây nôn trung hạn (delayed nausea)'
        , 'monitoring': ['Đáp ứng điều trị (giảm nôn, buồn nôn)',
        'Dấu hiệu đau đầu (phổ biến)', 'Dấu hiệu táo bón (phổ biến)',
        'Điện tâm đồ (ECG) nếu có nguy cơ QT kéo dài (hiếm)',
        'Chức năng gan nếu dùng lâu dài'], 'precautions': [
        'Dùng 30 phút trước hóa trị để đạt hiệu quả tối đa',
        'Chỉ cần dùng 1 liều (tác dụng kéo dài 48-72 giờ)',
        'Có thể dùng kết hợp với corticosteroid (dexamethasone) để tăng hiệu quả',
        'Tránh dùng với apomorphine (chống chỉ định)',
        'Có thể gây QT kéo dài (hiếm - cần theo dõi nếu có nguy cơ)',
        'Có thể dùng trong thai kỳ (category B - thận trọng)',
        'Tác dụng dài hơn so với ondansetron và granisetron'],
        'pharmacokinetics': {'half_life': '40 giờ (rất dài)', 'onset':
        '5 phút (IV)', 'duration': '48-72 giờ (rất dài)', 'protein_binding':
        '62%', 'clearance':
        'Gan (chuyển hóa qua CYP2D6, CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Apomorphine', 'mechanism':
        'Palonosetron ức chế 5-HT3 receptor, có thể tăng tác dụng của apomorphine, gây hạ huyết áp nghiêm trọng.'
        , 'effect':
        'Tăng tác dụng apomorphine, hạ huyết áp nghiêm trọng, nguy cơ tử vong',
        'management': 'CHỐNG CHỈ ĐỊNH - không dùng đồng thời.'}], 'moderate': [
        ], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng palonosetron hoặc 5-HT3 antagonists'], 'tương_đối': [
        'Bệnh nhân có tiền sử QT kéo dài - thận trọng, theo dõi ECG',
        'Suy gan - thận trọng, có thể cần giảm liều']}, 'pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'Có thể dùng trong thai kỳ nếu cần. Không có bằng chứng dị tật thai nhi, nhưng dữ liệu còn hạn chế. Dùng với thận trọng.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Palonosetron bài tiết vào sữa mẹ ở nồng độ thấp. Chưa có đủ dữ liệu về an toàn cho trẻ sơ sinh.'
        , 'recommendation':
        'Thận trọng khi cho con bú. Có thể dùng nếu lợi ích vượt trội nguy cơ.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể cần giảm liều', 'severe':
        'Thận trọng, giảm liều 25-50%', 'notes':
        'Palonosetron chuyển hóa chủ yếu qua gan (CYP2D6, CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ.'
        }, 'overdose_management': {'symptoms': ['Đau đầu nặng', 'Táo bón nặng',
        'Chóng mặt', 'QT kéo dài (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': ['Ngừng thuốc',
        'Supportive care', 'Theo dõi ECG nếu có QT kéo dài',
        'Điều trị táo bón nếu cần'], 'monitoring': 'ECG, dấu hiệu lâm sàng'},
        'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food': 'Không áp dụng', 'timing':
        'Không có dạng uống (chỉ có IV)'}, 'iv': {'reconstitution':
        'Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất', 'infusion_rate':
        'Tiêm trực tiếp hoặc truyền trong 30 giây', 'compatibility': ['NS',
        'D5W'], 'incompatibility': [], 'notes':
        '0.25mg IV x 1 lần trước hóa trị hoặc 0.075mg IV x 1 lần trước gây mê. Tiêm trực tiếp hoặc truyền trong 30 giây. Chỉ cần 1 liều (tác dụng kéo dài 48-72 giờ).'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Palonosetron (Aloxi)',
        'UpToDate - Palonosetron Drug Information',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-15', 'evidence_level':
        'High (FDA-approved, extensive clinical data)'}}}

__all__ = ['ANTI_EMETIC_(5_HT3_ANTAGONIST)S_DRUGS']
