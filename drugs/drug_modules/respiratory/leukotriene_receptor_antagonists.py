"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Leukotriene Receptor Antagonists

LEUKOTRIENE_RECEPTOR_ANTAGONISTS_DRUGS = {
    "Montelukast": {'group': 'Respiratory - Leukotriene Receptor Antagonist',
        'vietnamese_name': 'Montelukast, Singulair', 'administration': ['PO'],
        'indications': ['Hen phế quản (phòng ngừa)', 'Viêm mũi dị ứng',
        'Co thắt phế quản do gắng sức'], 'contraindications': [
        'Dị ứng montelukast'], 'dosage': {'adult':
        '10mg x 1 lần/ngày (buổi tối)', 'pediatric_6_14': '5mg x 1 lần/ngày',
        'pediatric_2_5': '4mg x 1 lần/ngày', 'notes':
        'Uống buổi tối, có thể uống với hoặc không thức ăn'}, 'side_effects': [
        'Nhức đầu', 'Buồn nôn', 'Tiêu chảy', 'Rối loạn giấc ngủ',
        'Thay đổi tâm trạng (hiếm)', 'Phản ứng tâm thần (rất hiếm)'],
        'interactions': ['Phenobarbital: giảm nồng độ montelukast',
        'Rifampin: giảm nồng độ montelukast'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Montelukast là chất đối kháng chọn lọc thụ thể leukotriene D4 (LTD4), thuộc nhóm leukotriene receptor antagonist (LTRA). Leukotriene là các chất trung gian gây viêm được tổng hợp từ acid arachidonic qua con đường 5-lipoxygenase. Leukotriene D4 gắn vào CysLT1 receptor trên cơ trơn phế quản, mạch máu, và các tế bào viêm, gây co thắt phế quản, tăng tính thấm mạch máu, phù nề, và tăng tiết chất nhầy. Montelukast ức chế LTD4 gắn vào CysLT1 receptor, ngăn chặn các tác dụng này, từ đó giảm co thắt phế quản, giảm viêm, và giảm triệu chứng hen. Montelukast có tác dụng phòng ngừa hen, đặc biệt hen do dị ứng và hen do gắng sức. Không dùng cho cắt cơn cấp. Tác dụng phát huy sau vài giờ đến vài ngày, dùng hàng ngày để duy trì.'
        , 'monitoring': [
        'Đáp ứng điều trị (giảm triệu chứng hen, giảm tần suất cơn cấp, giảm nhu cầu dùng SABA)'
        ,
        'Rối loạn tâm thần (thay đổi tâm trạng, lo âu, trầm cảm, hành vi bất thường, ý nghĩ tự sát) - hiếm nhưng nghiêm trọng, đặc biệt ở trẻ em và thanh thiếu niên'
        , 'Rối loạn giấc ngủ (mất ngủ, ác mộng)',
        'Nhức đầu, buồn nôn, tiêu chảy - tác dụng phụ phổ biến nhưng thường nhẹ',
        'Chức năng gan nếu có triệu chứng (hiếm)',
        'Tương tác với phenobarbital, rifampin (giảm nồng độ montelukast)'],
        'precautions': [
        'Rối loạn tâm thần - nguy cơ thay đổi tâm trạng, lo âu, trầm cảm, hành vi bất thường, ý nghĩ tự sát, đặc biệt ở trẻ em và thanh thiếu niên'
        ,
        'NGỪNG NGAY và liên hệ bác sĩ nếu có thay đổi tâm trạng, hành vi bất thường, ý nghĩ tự sát'
        ,
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, montelukast là thuốc phòng ngừa'
        ,
        'Tác dụng phát huy sau vài giờ đến vài ngày - không mong đợi tác dụng tức thì'
        ,
        'Dùng hàng ngày, tốt nhất vào buổi tối, có thể uống với hoặc không thức ăn'
        ,
        'Không thay thế ICS (inhaled corticosteroid) - có thể dùng kết hợp với ICS'
        , 'Hiệu quả với hen do dị ứng và hen do gắng sức',
        'Thận trọng với phenobarbital, rifampin (giảm nồng độ montelukast, có thể giảm hiệu quả)'
        , 'An toàn trong thai kỳ (category B)',
        'Có thể dùng cho trẻ em từ 2 tuổi trở lên (liều điều chỉnh theo tuổi)',
        'Theo dõi chặt chẽ ở trẻ em và thanh thiếu niên về rối loạn tâm thần'],
        'pharmacokinetics': {'half_life': '2.7-5.5 giờ', 'onset':
        'Vài giờ đến vài ngày (tác dụng phòng ngừa)', 'duration':
        '24 giờ (dùng 1 lần/ngày)', 'protein_binding': '>99%', 'clearance':
        'Gan: chuyển hóa qua CYP2C8, CYP3A4, và CYP2C9 thành metabolites không hoạt động. Thận: bài tiết một phần nguyên dạng và metabolites. Tương tác với CYP inducers (phenobarbital, rifampin) có thể giảm nồng độ.'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén/capsule: bảo quản trong bao bì kín. Dạng nhai: bảo quản ở nhiệt độ phòng, tránh ẩm. Dạng bột: bảo quản ở nhiệt độ phòng, pha với nước, thức ăn mềm, hoặc sữa công thức trước khi dùng.'
        , 'black_box_warnings':
        'Nguy cơ rối loạn tâm thần nghiêm trọng, bao gồm thay đổi tâm trạng, lo âu, trầm cảm, hành vi bất thường, và ý nghĩ tự sát. Nguy cơ tăng ở trẻ em và thanh thiếu niên. Ngừng ngay và liên hệ bác sĩ nếu có thay đổi tâm trạng, hành vi bất thường, hoặc ý nghĩ tự sát.'
        , 'drug_interactions': {'major': [], 'moderate': [{'drug':
        'Phenobarbital', 'mechanism':
        'Cảm ứng CYP2C8, CYP3A4, giảm nồng độ montelukast', 'effect':
        'Giảm hiệu quả montelukast, có thể không kiểm soát được hen',
        'management':
        'Theo dõi đáp ứng điều trị. Có thể cần tăng liều montelukast hoặc xem xét thuốc thay thế.'
        }, {'drug': 'Rifampin', 'mechanism':
        'Cảm ứng CYP2C8, CYP3A4, giảm nồng độ montelukast', 'effect':
        'Giảm hiệu quả montelukast, có thể không kiểm soát được hen',
        'management':
        'Theo dõi đáp ứng điều trị. Có thể cần tăng liều montelukast hoặc xem xét thuốc thay thế.'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng với montelukast hoặc các thành phần khác'], 'tương_đối': [
        'Rối loạn tâm thần (trầm cảm, lo âu, rối loạn hành vi) - thận trọng, theo dõi chặt chẽ'
        , 'Tiền sử tự sát - thận trọng, theo dõi chặt chẽ',
        'Dùng với phenobarbital, rifampin - có thể giảm hiệu quả']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Montelukast là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Montelukast được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Montelukast bài tiết vào sữa mẹ với nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation': 'Có thể dùng an toàn khi cho con bú.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi', 'notes':
        'Montelukast chuyển hóa qua gan (CYP2C8, CYP3A4, CYP2C9) nhưng không tích lũy ở suy gan. Không cần điều chỉnh liều ở suy gan.'
        }, 'overdose_management': {'symptoms': ['Nhức đầu', 'Buồn nôn, nôn',
        'Tiêu chảy', 'Rối loạn giấc ngủ', 'Thay đổi tâm trạng, kích động',
        'Rối loạn tâm thần (hiếm)'], 'antidote': 'Không có antidote đặc hiệu',
        'treatment': ['Ngừng ngay montelukast',
        'Hỗ trợ và điều trị triệu chứng',
        'Theo dõi rối loạn tâm thần (đặc biệt ở trẻ em và thanh thiếu niên)',
        'Theo dõi chức năng gan nếu có triệu chứng'], 'monitoring':
        'Theo dõi: tâm trạng, hành vi, ý nghĩ tự sát (đặc biệt ở trẻ em và thanh thiếu niên), nhức đầu, buồn nôn, tiêu chảy, chức năng gan. Theo dõi ít nhất 24 giờ.'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng.'
        }, 'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn', 'timing':
        'Uống 1 lần/ngày, tốt nhất vào buổi tối', 'pediatric':
        'Trẻ em 6-14 tuổi: 5mg/ngày. Trẻ em 2-5 tuổi: 4mg/ngày. Dạng nhai hoặc bột.'
        }, 'iv': None}, 'references': {'primary_sources': [
        'FDA Label: Singulair (Montelukast)',
        'UpToDate: Leukotriene receptor antagonists in asthma',
        'GINA Guidelines 2024: Asthma Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Montelukast'], 'last_updated': '2025-02-03',
        'evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'}}}

__all__ = ['LEUKOTRIENE_RECEPTOR_ANTAGONISTS_DRUGS']
