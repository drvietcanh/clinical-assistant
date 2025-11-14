"""Diabetes Medications
Active module - contains all diabetes drug data"""

# Sulfonylureas

SULFONYLUREAS_DRUGS = {
    "Glibenclamide": {'group': 'Diabetes - Sulfonylurea', 'vietnamese_name':
        'Glibenclamide, Daonil', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2'], 'contraindications': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng', 'Suy gan nặng',
        'Có thai'], 'dosage': {'adult_start':
        '2.5-5mg x 1 lần/ngày trước bữa sáng', 'adult_usual':
        '5-15mg/ngày chia 1-2 lần', 'adult_max': '20mg/ngày', 'notes':
        'Nguy cơ hạ đường huyết cao, đặc biệt ở người già, suy thận'},
        'side_effects': ['Hạ đường huyết (thường gặp, có thể nặng)', 'Tăng cân',
        'Ban da', 'Rối loạn tiêu hóa'], 'interactions': [
        'Warfarin: có thể tăng tác dụng chống đông',
        'Rượu: tăng nguy cơ hạ đường huyết',
        'Beta-blocker: che dấu triệu chứng hạ đường huyết'], 'pregnancy':
        'C - Tránh dùng trong thai kỳ', 'mechanism_of_action':
        'Glibenclamide (glyburide) là thuốc sulfonylurea thế hệ thứ hai, kích thích tế bào beta tuyến tụy tiết insulin. Glibenclamide gắn vào SUR1 (sulfonylurea receptor 1) trên kênh KATP (ATP-sensitive K+ channel) ở màng tế bào beta, làm đóng kênh KATP. Điều này ngăn chặn dòng kali ra ngoài, làm khử cực màng tế bào (depolarization), mở kênh canxi phụ thuộc điện thế, tăng dòng canxi vào tế bào, và kích thích giải phóng insulin từ các hạt tiết. Glibenclamide chỉ hoạt động khi còn chức năng tế bào beta (cần có insulin nội sinh). Glibenclamide có tác dụng mạnh và thời gian bán thải dài, dẫn đến nguy cơ hạ đường huyết cao hơn các sulfonylurea khác, đặc biệt ở người cao tuổi và suy thận. Glibenclamide cũng có thể làm giảm đề kháng insulin ngoại vi và giảm sản xuất glucose ở gan.'
        , 'monitoring': [
        'Đường huyết: HbA1c (mỗi 3 tháng), đường huyết đói, đường huyết sau ăn - đánh giá hiệu quả'
        ,
        'Dấu hiệu hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn, co giật, hôn mê - QUAN TRỌNG'
        , 'Đường huyết khi nghi ngờ hạ đường huyết - đo ngay',
        'Cân nặng - sulfonylureas có thể gây tăng cân',
        'Chức năng thận (creatinine, eGFR) - suy thận tăng nguy cơ hạ đường huyết (tăng thời gian bán thải)'
        ,
        'Chức năng gan (ALT, AST) - nếu có bệnh gan (tăng nguy cơ hạ đường huyết)',
        'Tương tác với warfarin (tăng INR), rượu (tăng nguy cơ hạ đường huyết), beta-blocker (che dấu triệu chứng hạ đường huyết)'
        ], 'precautions': [
        'Hạ đường huyết là tác dụng phụ phổ biến nhất và nghiêm trọng - bệnh nhân cần biết dấu hiệu và cách xử trí (uống nước đường, nước ngọt, hoặc glucose)'
        ,
        'Nguy cơ hạ đường huyết cao hơn các sulfonylurea khác do thời gian bán thải dài'
        ,
        'Nguy cơ tăng ở: người cao tuổi, suy thận, suy gan, bỏ bữa, uống rượu, tập luyện quá mức'
        ,
        'KHÔNG dùng ở đái tháo đường type 1 hoặc nhiễm toan ceton (không có insulin nội sinh)'
        ,
        'Thận trọng ở bệnh nhân suy thận - tăng nguy cơ hạ đường huyết (có thể cần giảm liều hoặc tránh dùng)'
        , 'Thận trọng ở bệnh nhân suy gan - tăng nguy cơ hạ đường huyết',
        'Uống với thức ăn hoặc trước bữa ăn để tránh hạ đường huyết',
        'Tránh bỏ bữa - tăng nguy cơ hạ đường huyết',
        'Tránh rượu - tăng nguy cơ hạ đường huyết (có thể gây hạ đường huyết kéo dài)'
        ,
        'Beta-blocker có thể che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run) - chỉ còn vã mồ hôi, lú lẫn'
        , 'Có thể tăng cân - cần tư vấn chế độ ăn và tập luyện',
        'Không dùng trong thai kỳ (có thể gây hạ đường huyết ở trẻ sơ sinh)',
        'Bắt đầu với liều thấp (2.5-5mg/ngày) và tăng dần'], 'pharmacokinetics':
        {'half_life': '10 giờ (bình thường), tăng ở suy thận', 'onset':
        '2-4 giờ', 'duration': '16-24 giờ (dùng 1-2 lần/ngày)',
        'protein_binding': '99% (gắn chặt với albumin)', 'clearance':
        'Gan: chuyển hóa qua CYP2C9 và CYP3A4 thành metabolites không hoạt động. Thận: bài tiết một phần nguyên dạng và metabolites. Thời gian bán thải tăng ở suy thận (tăng nguy cơ hạ đường huyết).'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings':
        'Nguy cơ hạ đường huyết nghiêm trọng, có thể gây tử vong. Nguy cơ tăng ở người cao tuổi, suy thận, suy gan, bỏ bữa, uống rượu. Bệnh nhân cần biết dấu hiệu và cách xử trí hạ đường huyết. Không dùng ở đái tháo đường type 1 hoặc nhiễm toan ceton.'
        , 'drug_interactions': {'major': [{'drug': 'Rượu (ethanol)',
        'mechanism':
        'Ức chế sản xuất glucose ở gan, tăng nguy cơ hạ đường huyết', 'effect':
        'Hạ đường huyết nghiêm trọng, có thể kéo dài', 'management':
        'TRÁNH RƯỢU hoàn toàn khi dùng glibenclamide. Cảnh báo bệnh nhân về nguy cơ.'
        }, {'drug': 'Beta-blockers (propranolol, metoprolol)', 'mechanism':
        'Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run)', 'effect':
        'Khó nhận biết hạ đường huyết, tăng nguy cơ hạ đường huyết nặng',
        'management':
        'Thận trọng. Theo dõi đường huyết chặt chẽ. Bệnh nhân cần biết các triệu chứng hạ đường huyết không bị che dấu (vã mồ hôi, lú lẫn).'
        }], 'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Glibenclamide có thể tăng tác dụng chống đông', 'effect':
        'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}, {
        'drug': 'CYP2C9 inhibitors (fluconazole, amiodarone)', 'mechanism':
        'Ức chế chuyển hóa glibenclamide, tăng nồng độ', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Theo dõi đường huyết. Có thể cần giảm liều glibenclamide.'
        }, {'drug': 'Salicylates (aspirin liều cao)', 'mechanism':
        'Tăng tác dụng giảm đường huyết', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Theo dõi đường huyết.'}], 'minor': [{'drug':
        'Chloramphenicol', 'mechanism': 'Tăng nồng độ glibenclamide', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Theo dõi đường huyết.'}]}, 'contraindications': {
        'tuyệt_đối': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường',
        'Dị ứng glibenclamide hoặc sulfonylurea',
        'Suy thận nặng (CrCl <30) - tăng nguy cơ hạ đường huyết nghiêm trọng'],
        'tương_đối': ['Suy gan nặng - tăng nguy cơ hạ đường huyết',
        'Người cao tuổi - tăng nguy cơ hạ đường huyết',
        'Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát',
        'Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh',
        'Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết',
        'Uống rượu - tăng nguy cơ hạ đường huyết nghiêm trọng',
        'Dùng beta-blocker - che dấu triệu chứng hạ đường huyết']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng THƯỜNG TRÁNH DÙNG. Sulfonylureas có thể gây hạ đường huyết ở trẻ sơ sinh. Insulin là lựa chọn ưu tiên trong thai kỳ. Nếu dùng, theo dõi đường huyết chặt chẽ và ngừng trước khi sinh để tránh hạ đường huyết ở trẻ sơ sinh.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Glibenclamide bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây hạ đường huyết ở trẻ bú mẹ do nồng độ thấp.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với theo dõi chặt chẽ. Theo dõi dấu hiệu hạ đường huyết ở trẻ (quấy khóc, bú kém, vã mồ hôi).'
        }}, 'hepatic_adjustment': {'mild': 'Thận trọng, giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan và đường huyết',
        'severe': 'CHỐNG CHỈ ĐỊNH', 'notes':
        'Glibenclamide chuyển hóa ở gan qua CYP2C9 và CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ hạ đường huyết nghiêm trọng. Không dùng ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': [
        'Hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn, co giật, hôn mê'
        , 'Hạ đường huyết có thể kéo dài (do thời gian bán thải dài)',
        'Hạ đường huyết nghiêm trọng có thể gây tử vong hoặc tổn thương não vĩnh viễn'
        ], 'antidote': 'Glucose (đường uống hoặc IV)', 'treatment': [
        'Nếu tỉnh táo: Glucose 15-20g PO (nước đường, nước ngọt, kẹo)',
        'Nếu hôn mê hoặc không thể uống: Dextrose 50% 50ml IV hoặc glucagon 1mg SC/IM'
        ,
        'Theo dõi đường huyết mỗi 15-30 phút trong ít nhất 4-6 giờ (do thời gian bán thải dài)'
        , 'Duy trì glucose IV nếu cần (dextrose 5% hoặc 10% truyền liên tục)',
        'Theo dõi ít nhất 24 giờ (do thời gian bán thải dài, có thể tái phát hạ đường huyết)'
        ,
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ (nhưng ưu tiên điều trị hạ đường huyết)'
        , 'Than hoạt tính (hiệu quả hạn chế do hấp thu nhanh)',
        'Hỗ trợ hô hấp và tuần hoàn nếu cần', 'Theo dõi ý thức, dấu hiệu sống'],
        'monitoring':
        'Đường huyết (mỗi 15-30 phút trong ít nhất 4-6 giờ), ý thức, dấu hiệu sống, điện giải, chức năng thận'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Glucose', 'route': 'PO hoặc IV', 'dose':
        '15-20g PO hoặc dextrose 50% 50ml IV', 'notes':
        'Điều trị hạ đường huyết ngay lập tức'}, {'agent': 'Glucagon', 'route':
        'SC hoặc IM', 'dose': '1mg SC/IM', 'notes':
        'Nếu không thể truyền IV, dùng glucagon để tăng đường huyết'}]},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc trước bữa ăn (15-30 phút trước bữa ăn) để tránh hạ đường huyết. Không bỏ bữa sau khi uống.'
        , 'timing':
        'Uống 1-2 lần/ngày, thường trước bữa sáng và/hoặc bữa tối. Khởi đầu với liều thấp (2.5-5mg/ngày) và tăng dần. Uống đúng giờ mỗi ngày.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Glyburide (glibenclamide)',
        'UpToDate - Glyburide: Drug information',
        'UK Prospective Diabetes Study (UKPDS)',
        'American Diabetes Association guidelines',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - Multiple large RCTs (UKPDS) and extensive clinical experience'}},
    "Gliclazide": {'group': 'Diabetes - Sulfonylurea', 'vietnamese_name':
        'Gliclazide, Diamicron', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2'], 'contraindications': ['Đái tháo đường type 1',
        'Nhiễm toan ceton', 'Suy thận nặng'], 'dosage': {'adult_standard':
        '80-320mg/ngày chia 1-2 lần', 'adult_modified_release':
        '30-120mg x 1 lần/ngày', 'notes':
        'Ít nguy cơ hạ đường huyết hơn glibenclamide'}, 'side_effects': [
        'Hạ đường huyết', 'Tăng cân', 'Ban da'], 'interactions': [
        'Tương tự sulfonylurea khác'], 'pregnancy': 'C', 'mechanism_of_action':
        'Sulfonylurea thế hệ 2. Kích thích tế bào beta tuyến tụy tiết insulin bằng cách đóng kênh KATP (ATP-sensitive K+ channel), làm khử cực màng tế bào, mở kênh Ca2+, và giải phóng insulin. Chỉ hoạt động khi còn chức năng tế bào beta. Gliclazide ưu điểm: thời gian bán hủy ngắn hơn, ít nguy cơ hạ đường huyết hơn glibenclamide.'
        , 'monitoring': [
        'Đường huyết: HbA1c (mỗi 3 tháng), đường huyết đói, đường huyết sau ăn',
        'Dấu hiệu hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, lú lẫn, co giật',
        'Cân nặng - sulfonylureas có thể gây tăng cân',
        'Chức năng thận: creatinine, eGFR (suy thận tăng nguy cơ hạ đường huyết)',
        'Chức năng gan: ALT, AST (nếu có bệnh gan)'], 'precautions': [
        'Uống với thức ăn hoặc trước bữa ăn để tránh hạ đường huyết',
        'KHÔNG dùng ở đái tháo đường type 1 hoặc nhiễm toan ceton',
        'Thận trọng ở bệnh nhân suy thận - tăng nguy cơ hạ đường huyết (có thể cần giảm liều hoặc tránh dùng)'
        , 'Thận trọng ở bệnh nhân suy gan - tăng nguy cơ hạ đường huyết',
        'Hạ đường huyết là tác dụng phụ phổ biến nhất - bệnh nhân cần biết dấu hiệu và cách xử trí'
        , 'Tránh bỏ bữa - tăng nguy cơ hạ đường huyết',
        'Tránh rượu - tăng nguy cơ hạ đường huyết',
        'Có thể tăng cân - cần tư vấn chế độ ăn và tập luyện',
        'Gliclazide ưu điểm: thời gian bán hủy ngắn hơn, ít hạ đường huyết hơn glibenclamide'
        ], 'pharmacokinetics': {'half_life':
        '10-12 giờ (ngắn hơn glibenclamide)', 'onset': '30-60 phút (PO)',
        'duration': '12-24 giờ', 'protein_binding': '85-95%', 'clearance':
        'Gan (CYP2C9), thận (metabolites)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Hạ đường huyết có thể gây nguy hiểm tính mạng, đặc biệt ở bệnh nhân suy thận, suy gan, người già. Bệnh nhân cần biết dấu hiệu và cách xử trí hạ đường huyết'
        , 'drug_interactions': {'major': [{'drug': 'Rượu (ethanol)',
        'mechanism':
        'Ức chế sản xuất glucose ở gan, tăng nguy cơ hạ đường huyết', 'effect':
        'Hạ đường huyết nghiêm trọng', 'management':
        'TRÁNH RƯỢU hoàn toàn khi dùng gliclazide. Cảnh báo bệnh nhân về nguy cơ.'
        }, {'drug': 'Beta-blockers (propranolol, metoprolol)', 'mechanism':
        'Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run)', 'effect':
        'Khó nhận biết hạ đường huyết', 'management':
        'Thận trọng. Theo dõi đường huyết chặt chẽ.'}], 'moderate': [{'drug':
        'CYP2C9 inhibitors (fluconazole, amiodarone)', 'mechanism':
        'Ức chế chuyển hóa gliclazide, tăng nồng độ', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Theo dõi đường huyết. Có thể cần giảm liều gliclazide.'},
        {'drug': 'Salicylates (aspirin liều cao)', 'mechanism':
        'Tăng tác dụng giảm đường huyết', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Theo dõi đường huyết.'}], 'minor': [{'drug':
        'Chloramphenicol', 'mechanism': 'Tăng nồng độ gliclazide', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Theo dõi đường huyết.'}]}, 'contraindications': {
        'tuyệt_đối': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường',
        'Dị ứng gliclazide hoặc sulfonylurea',
        'Suy thận nặng (CrCl <30) - tăng nguy cơ hạ đường huyết'], 'tương_đối':
        ['Suy gan nặng - tăng nguy cơ hạ đường huyết',
        'Người cao tuổi - tăng nguy cơ hạ đường huyết',
        'Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát',
        'Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh',
        'Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết',
        'Uống rượu - tăng nguy cơ hạ đường huyết']}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng THƯỜNG TRÁNH DÙNG. Sulfonylureas có thể gây hạ đường huyết ở trẻ sơ sinh. Insulin là lựa chọn ưu tiên trong thai kỳ. Nếu dùng, theo dõi đường huyết chặt chẽ và ngừng trước khi sinh.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Gliclazide bài tiết vào sữa mẹ ở nồng độ thấp. Ít có nguy cơ gây hạ đường huyết ở trẻ bú mẹ do nồng độ thấp.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với theo dõi chặt chẽ. Theo dõi dấu hiệu hạ đường huyết ở trẻ.'
        }}, 'hepatic_adjustment': {'mild': 'Thận trọng, giảm liều nhẹ',
        'moderate': 'Giảm liều 25-50%. Theo dõi chức năng gan và đường huyết',
        'severe': 'CHỐNG CHỈ ĐỊNH', 'notes':
        'Gliclazide chuyển hóa ở gan qua CYP2C9. Suy gan làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ hạ đường huyết. Không dùng ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': [
        'Hạ đường huyết: run, vã mồ hôi, nhịp tim nhanh, đói, lú lẫn, co giật, hôn mê'
        ,
        'Hạ đường huyết ít kéo dài hơn glibenclamide (do thời gian bán thải ngắn hơn)'
        ], 'antidote': 'Glucose (đường uống hoặc IV)', 'treatment': [
        'Nếu tỉnh táo: Glucose 15-20g PO (nước đường, nước ngọt, kẹo)',
        'Nếu hôn mê hoặc không thể uống: Dextrose 50% 50ml IV hoặc glucagon 1mg SC/IM'
        , 'Theo dõi đường huyết mỗi 15-30 phút trong ít nhất 4 giờ',
        'Duy trì glucose IV nếu cần (dextrose 5% hoặc 10% truyền liên tục)',
        'Theo dõi ít nhất 12-24 giờ (thời gian ngắn hơn glibenclamide)',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ (nhưng ưu tiên điều trị hạ đường huyết)'
        , 'Than hoạt tính (hiệu quả hạn chế)',
        'Hỗ trợ hô hấp và tuần hoàn nếu cần'], 'monitoring':
        'Đường huyết (mỗi 15-30 phút trong ít nhất 4 giờ), ý thức, dấu hiệu sống, điện giải'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Glucose', 'route': 'PO hoặc IV', 'dose':
        '15-20g PO hoặc dextrose 50% 50ml IV', 'notes':
        'Điều trị hạ đường huyết ngay lập tức'}, {'agent': 'Glucagon', 'route':
        'SC hoặc IM', 'dose': '1mg SC/IM', 'notes':
        'Nếu không thể truyền IV, dùng glucagon để tăng đường huyết'}]},
        'administration_instructions': {'oral': {'with_food':
        'Uống với thức ăn hoặc trước bữa ăn (15-30 phút trước bữa ăn) để tránh hạ đường huyết. Không bỏ bữa sau khi uống.'
        , 'timing':
        'Uống 1-2 lần/ngày, thường trước bữa sáng và/hoặc bữa tối. Dạng modified-release: 1 lần/ngày với bữa sáng. Khởi đầu với liều thấp và tăng dần.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Diamicron (gliclazide)',
        'UpToDate - Gliclazide: Drug information',
        'UK Prospective Diabetes Study (UKPDS)',
        'American Diabetes Association guidelines',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - Multiple large RCTs (UKPDS) and extensive clinical experience'}}}

__all__ = ['SULFONYLUREAS_DRUGS']
