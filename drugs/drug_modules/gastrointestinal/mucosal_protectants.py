"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Mucosal Protectants

MUCOSAL_PROTECTANTS_DRUGS = {
    "Sucralfate": {'group': 'Gastrointestinal - Mucosal Protectant', 'vietnamese_name':
        'Sucralfate, Carafate', 'administration': ['PO'], 'indications': [
        'Loét dạ dày tá tràng', 'Viêm dạ dày', 'Trào ngược dạ dày thực quản',
        'Loét do stress'], 'contraindications': ['Dị ứng sucralfate',
        'Suy thận nặng (tăng nguy cơ tích tụ nhôm)'], 'dosage': {'adult_ulcer':
        '1g x 4 lần/ngày (trước bữa ăn và trước khi ngủ) hoặc 2g x 2 lần/ngày',
        'adult_maintenance': '1g x 2 lần/ngày', 'notes':
        'Uống khi bụng đói (1 giờ trước bữa ăn). Không dùng với PPI, H2 blocker, antacid (cách 2 giờ)'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Thận trọng',
        'under_30': 'Tránh dùng (tích tụ nhôm)'}, 'side_effects': ['Táo bón',
        'Khô miệng', 'Buồn nôn', 'Đầy hơi', 'Tích tụ nhôm (suy thận)'],
        'interactions': ['PPI/H2 blocker/Antacid: giảm hiệu quả - cách 2 giờ',
        'Warfarin: có thể tăng tác dụng chống đông',
        'Phenytoin: giảm hấp thu phenytoin', 'Digoxin: giảm hấp thu digoxin',
        'Quinolone: giảm hấp thu quinolone',
        'Thyroxine: giảm hấp thu thyroxine'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Phức hợp sucrose-aluminum. Tạo lớp phủ bảo vệ trên vết loét dạ dày tá tràng. Phản ứng với acid dạ dày tạo thành gel dính, bám chặt vào vết loét, tạo hàng rào bảo vệ khỏi acid, pepsin, và muối mật. Kích thích tổng hợp prostaglandin, tăng tiết chất nhầy, tăng tái tạo niêm mạc. Cũng có thể hấp phụ pepsin và muối mật. Không giảm tiết acid như PPI/H2 blocker mà bảo vệ niêm mạc trực tiếp.'
        , 'monitoring': ['Đáp ứng lâm sàng (giảm đau, lành vết loét)',
        'Dấu hiệu tích tụ nhôm: rối loạn thần kinh, xương yếu (nếu dùng lâu dài ở suy thận)'
        , 'Chức năng thận (creatinine, BUN) - đặc biệt nếu dùng lâu dài',
        'INR nếu dùng với warfarin (có thể tăng tác dụng chống đông)',
        'Dấu hiệu táo bón nặng (tác dụng phụ thường gặp)'], 'precautions': [
        'Uống khi bụng đói (1 giờ trước bữa ăn) - cần acid dạ dày để tạo gel',
        'Không dùng với PPI, H2 blocker, antacid - cách 2 giờ (chúng làm giảm acid → giảm hiệu quả sucralfate)'
        ,
        'Không dùng với các thuốc khác - cách 2 giờ (sucralfate có thể giảm hấp thu)'
        , 'Thận trọng ở suy thận (CrCl 30-60) - giảm liều',
        'Tránh dùng ở suy thận nặng (CrCl <30) - tích tụ nhôm có thể gây độc',
        'Có thể gây táo bón - dùng thuốc nhuận tràng nếu cần',
        'Không nghiền hoặc nhai viên (giảm hiệu quả)',
        'Dùng đủ 4-8 tuần để lành vết loét hoàn toàn'], 'pharmacokinetics': {
        'half_life': 'Không áp dụng (tác dụng tại chỗ, không hấp thu)', 'onset':
        '1-2 giờ', 'duration': '6 giờ (lớp phủ bảo vệ)', 'protein_binding':
        'Không áp dụng (không hấp thu)', 'clearance':
        'Không hấp thu đáng kể, thải qua phân. Nhôm có thể tích tụ ở suy thận.'
        }, 'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm',
        'black_box_warnings':
        'Tích tụ nhôm ở suy thận nặng có thể gây độc tính thần kinh và xương. Tránh dùng ở suy thận nặng (CrCl <30).'
        , 'drug_interactions': {'major': [], 'moderate': [{'drug':
        'PPI, H2 blocker, Antacid', 'mechanism':
        'Giảm acid dạ dày, làm giảm khả năng tạo gel của sucralfate', 'effect':
        'Giảm hiệu quả của sucralfate', 'management':
        'Cách thời gian ít nhất 2 giờ. Uống sucralfate trước PPI/H2 blocker/antacid.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Sucralfate có thể tăng hấp thu warfarin hoặc tương tác khác', 'effect':
        'Có thể tăng tác dụng chống đông, tăng INR', 'management':
        'Theo dõi INR thường xuyên. Cách thời gian 2 giờ.'}, {'drug':
        'Phenytoin, Digoxin, Quinolone, Thyroxine', 'mechanism':
        'Sucralfate giảm hấp thu các thuốc này (hấp phụ hoặc chelate)',
        'effect': 'Giảm nồng độ thuốc, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ. Uống các thuốc khác trước sucralfate.'},
        {'drug': 'Iron salts, Vitamin D, Calcium', 'mechanism':
        'Sucralfate có thể giảm hấp thu', 'effect':
        'Giảm hấp thu iron, vitamin D, calcium', 'management':
        'Cách thời gian ít nhất 2 giờ'}], 'minor': []}, 'contraindications': {
        'tuyệt_đối': ['Dị ứng sucralfate',
        'Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH do tích tụ nhôm'],
        'tương_đối': [
        'Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều, theo dõi chức năng thận'
        , 'Táo bón nặng - có thể làm nặng thêm',
        'Đang dùng nhiều thuốc - tăng nguy cơ tương tác hấp thu']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Sucralfate là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Không hấp thu đáng kể, nên an toàn hơn trong thai kỳ. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Sucralfate không hấp thu đáng kể, không bài tiết vào sữa mẹ. An toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều', 'severe':
        'Không cần chỉnh liều. Sucralfate không hấp thu đáng kể, không chuyển hóa ở gan.'
        , 'notes':
        'Sucralfate không hấp thu đáng kể, không cần điều chỉnh liều ở suy gan.'
        }, 'overdose_management': {'symptoms': [
        'Sucralfate ít gây quá liều nghiêm trọng do không hấp thu',
        'Triệu chứng nhẹ: táo bón nặng, buồn nôn',
        'Ở suy thận nặng: tích tụ nhôm có thể gây độc tính thần kinh, xương yếu'
        ], 'antidote': 'Không có antidote đặc hiệu', 'treatment': [
        'Hỗ trợ triệu chứng (điều trị táo bón nếu cần)',
        'Theo dõi dấu hiệu tích tụ nhôm ở suy thận nặng',
        'Hầu hết trường hợp tự khỏi'], 'monitoring':
        'Theo dõi dấu hiệu tích tụ nhôm ở suy thận nặng (rối loạn thần kinh, xương yếu)'
        }, 'reversal_agents': None, 'administration_instructions': {'oral': {
        'with_food':
        'Uống KHI BỤNG ĐÓI (1 giờ trước bữa ăn) - quan trọng, cần acid dạ dày để tạo gel'
        , 'timing':
        'Uống 1 giờ trước bữa ăn và trước khi đi ngủ. Không uống với PPI, H2 blocker, antacid, hoặc các thuốc khác - cách ít nhất 2 giờ. KHÔNG nghiền hoặc nhai viên - nuốt nguyên viên với nước.'
        }, 'iv': {'reconstitution': 'Sucralfate chỉ có dạng uống (PO)',
        'infusion_rate': 'N/A', 'compatibility': [], 'incompatibility': [],
        'notes': 'Sucralfate chỉ có dạng uống, không có dạng IV'}},
        'references': {'primary_sources': ['FDA Drug Label - Sucralfate',
        'UpToDate - Sucralfate: Drug information', 'Micromedex - Sucralfate',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs'}}}

__all__ = ['MUCOSAL_PROTECTANTS_DRUGS']
