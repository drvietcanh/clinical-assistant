"""Diabetes Medications
Active module - contains all diabetes drug data"""

# DPP-4 Inhibitors

DPP_4_INHIBITORS_DRUGS = {
    "Sitagliptin": {'group': 'Diabetes - DPP-4 Inhibitor', 'vietnamese_name':
        'Sitagliptin, Januvia', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2'], 'contraindications': ['Đái tháo đường type 1',
        'Nhiễm toan ceton', 'Dị ứng sitagliptin', 'Suy thận nặng (CrCl <30)'],
        'dosage': {'adult_normal_renal': '100mg x 1 lần/ngày',
        'adult_moderate_renal': '50mg x 1 lần/ngày (CrCl 30-50)',
        'adult_severe_renal': '25mg x 1 lần/ngày (CrCl <30)', 'notes':
        'Uống bất kỳ lúc nào. Ít gây hạ đường huyết'}, 'renal_adjustment': {
        'normal': '100mg/ngày', '30_60': '50mg/ngày (CrCl 30-50)', 'under_30':
        '25mg/ngày (CrCl <30)'}, 'side_effects': ['Nhức đầu',
        'Nhiễm trùng đường hô hấp trên', 'Viêm tụy cấp (hiếm nhưng nguy hiểm)',
        'Đau khớp nghiêm trọng (hiếm)', 'Suy tim (tăng nhẹ nguy cơ)'],
        'interactions': [
        'Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết',
        'Digoxin: tăng nhẹ nồng độ digoxin'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Sitagliptin là chất ức chế chọn lọc dipeptidyl peptidase-4 (DPP-4), enzyme chịu trách nhiệm phân hủy incretin hormones (GLP-1 và GIP). Bằng cách ức chế DPP-4, sitagliptin làm tăng nồng độ GLP-1 và GIP, các hormone được tiết ra từ ruột non sau khi ăn. GLP-1 và GIP kích thích tiết insulin từ tế bào beta tuyến tụy phụ thuộc vào glucose (chỉ tiết khi đường huyết cao), đồng thời ức chế tiết glucagon từ tế bào alpha tuyến tụy. Điều này dẫn đến giảm đường huyết sau ăn và giảm sản xuất glucose từ gan. Cơ chế này phụ thuộc vào glucose nên ít gây hạ đường huyết so với sulfonylurea. Sitagliptin cũng làm chậm làm rỗng dạ dày và có thể giảm cảm giác thèm ăn nhẹ.'
        , 'monitoring': [
        'Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết',
        'Chức năng thận (creatinine, CrCl) - cần điều chỉnh liều: CrCl 30-50 → 50mg/ngày, CrCl <30 → 25mg/ngày'
        ,
        'Triệu chứng viêm tụy cấp (đau bụng nặng, buồn nôn, nôn) - hiếm nhưng nguy hiểm'
        , 'Đau khớp nghiêm trọng - hiếm, cần ngừng thuốc nếu xảy ra',
        'Triệu chứng suy tim (khó thở, phù) - tăng nhẹ nguy cơ suy tim',
        'Dấu hiệu phản ứng dị ứng (phát ban, phù mạch) - hiếm',
        'Tác dụng phụ (nhức đầu, nhiễm trùng đường hô hấp trên)'],
        'precautions': ['Không dùng cho đái tháo đường type 1 (không hiệu quả)',
        'Cần điều chỉnh liều ở suy thận: CrCl 30-50 → 50mg/ngày, CrCl <30 → 25mg/ngày'
        ,
        'Nguy cơ viêm tụy cấp - hiếm nhưng nguy hiểm, ngừng ngay nếu có đau bụng nặng'
        , 'Nguy cơ đau khớp nghiêm trọng - hiếm, ngừng thuốc nếu xảy ra',
        'Tăng nhẹ nguy cơ suy tim - thận trọng ở bệnh nhân có tiền sử suy tim',
        'Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea',
        'Ít gây hạ đường huyết khi dùng đơn độc (do cơ chế phụ thuộc glucose)',
        'Có thể dùng bất kỳ lúc nào, không cần ăn',
        'An toàn trong thai kỳ (category B)',
        'Tương tác nhẹ với digoxin - có thể tăng nồng độ digoxin'],
        'pharmacokinetics': {'half_life': '12.4 giờ', 'onset': '1-2 giờ',
        'duration': '24 giờ', 'protein_binding': '38%', 'clearance':
        'Thận: bài tiết chủ yếu qua thận (79% nguyên dạng, không chuyển hóa). Gan: ít chuyển hóa. Cần điều chỉnh liều ở suy thận.'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [],
        'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Sitagliptin có thể tăng nhẹ nồng độ digoxin', 'effect':
        'Tăng nguy cơ độc tính digoxin', 'management':
        'Theo dõi nồng độ digoxin, ECG. Điều chỉnh liều digoxin nếu cần.'}, {
        'drug': 'Insulin, Sulfonylurea (glibenclamide, gliclazide)',
        'mechanism': 'Tác dụng hiệp đồng giảm đường huyết', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Theo dõi đường huyết. Có thể cần giảm liều insulin hoặc sulfonylurea.'
        }], 'minor': [{'drug': 'CYP3A4 substrates', 'mechanism':
        'Sitagliptin ít chuyển hóa qua CYP, ít tương tác', 'effect':
        'Tương tác tối thiểu', 'management': 'Không cần điều chỉnh liều'}]},
        'contraindications': {'tuyệt_đối': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường', 'Dị ứng sitagliptin',
        'Viêm tụy cấp đang diễn ra'], 'tương_đối': [
        'Suy thận nặng (CrCl <30) - cần giảm liều (25mg/ngày)',
        'Suy thận trung bình (CrCl 30-50) - cần giảm liều (50mg/ngày)',
        'Tiền sử viêm tụy cấp - tăng nguy cơ',
        'Tiền sử suy tim - tăng nhẹ nguy cơ suy tim',
        'Đau khớp nghiêm trọng - ngừng thuốc nếu xảy ra']},
        'pregnancy_lactation': {'fda_category': 'B', 'pregnancy_details':
        'Không có bằng chứng về nguy cơ gây dị tật thai nhi ở động vật. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Ít dữ liệu ở người, nhưng không có báo cáo về dị tật thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Sitagliptin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi (chủ yếu thải qua thận, không phụ thuộc gan)',
        'notes':
        'Sitagliptin chủ yếu bài tiết qua thận (79% nguyên dạng), không chuyển hóa đáng kể qua gan. Không cần điều chỉnh liều ở suy gan.'
        }, 'overdose_management': {'symptoms': [
        'Hạ đường huyết (nếu dùng với insulin hoặc sulfonylurea)',
        'Đau bụng, buồn nôn, nôn (dấu hiệu viêm tụy)', 'Nhức đầu', 'Đau khớp'],
        'antidote': 'Không có antidote đặc hiệu', 'treatment': [
        'Điều trị hạ đường huyết nếu có: Glucose 15-20g PO hoặc dextrose IV',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ', 'Than hoạt tính',
        'Theo dõi đường huyết, chức năng thận',
        'Nếu có dấu hiệu viêm tụy cấp: ngừng thuốc, điều trị hỗ trợ, theo dõi amylase/lipase'
        , 'Điều trị hỗ trợ'], 'monitoring':
        'Đường huyết, chức năng thận, dấu hiệu viêm tụy (đau bụng, amylase/lipase), đau khớp'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.',
        'timing':
        'Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Januvia (sitagliptin)',
        'UpToDate - Sitagliptin: Drug information',
        'TECOS Study - New England Journal of Medicine',
        'American Diabetes Association guidelines'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews (TECOS study)'}},
    "Vildagliptin": {'group': 'Diabetes - DPP-4 Inhibitor', 'vietnamese_name':
        'Vildagliptin, Galvus', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2'], 'contraindications': ['Đái tháo đường type 1',
        'Nhiễm toan ceton', 'Suy gan nặng'], 'dosage': {'adult_standard':
        '50mg x 2 lần/ngày (sáng và tối)', 'adult_metformin_combination':
        '50mg x 2 lần/ngày', 'notes': 'Uống với bữa ăn. Ít gây hạ đường huyết'},
        'renal_adjustment': {'normal': '50mg x 2 lần/ngày', '30_60':
        '50mg x 2 lần/ngày', 'under_30': 'Thận trọng'}, 'side_effects': [
        'Nhức đầu', 'Chóng mặt', 'Nhiễm trùng đường hô hấp',
        'Viêm tụy cấp (hiếm)', 'Đau khớp (hiếm)'], 'interactions': [
        'Insulin/Sulfonylurea: có thể tăng nguy cơ hạ đường huyết'],
        'pregnancy': 'C', 'mechanism_of_action':
        'Vildagliptin là DPP-4 (dipeptidyl peptidase-4) inhibitor, ức chế enzyme DPP-4 phân hủy incretin hormones (GLP-1 và GIP). Khi DPP-4 bị ức chế, nồng độ GLP-1 và GIP tăng, kích thích tế bào beta tụy tiết insulin (glucose-dependent) và ức chế tế bào alpha tụy tiết glucagon. Kết quả là tăng tiết insulin và giảm glucagon, giảm đường huyết sau ăn và đường huyết đói. Vildagliptin chỉ hoạt động khi đường huyết cao, nên ít gây hạ đường huyết hơn so với sulfonylurea'
        , 'monitoring': ['HbA1c mỗi 3 tháng', 'Đường huyết đói và sau ăn',
        'Chức năng gan (ALT, AST) trước và trong điều trị (nguy cơ viêm tụy cấp)',
        'Dấu hiệu viêm tụy cấp (đau bụng, nôn - hiếm nhưng nguy hiểm)',
        'Chức năng thận (creatinine, eGFR) định kỳ'], 'precautions': [
        'Uống với bữa ăn (tăng hấp thu)',
        'Ít gây hạ đường huyết hơn sulfonylurea (glucose-dependent)',
        'Có thể dùng kết hợp với metformin, sulfonylurea, hoặc insulin',
        'Ngừng ngay nếu có dấu hiệu viêm tụy cấp (hiếm nhưng nguy hiểm)',
        'Có thể dùng trong thai kỳ (category C)',
        'Thận trọng nếu suy thận nặng (CrCl <30)',
        'Có thể tăng nguy cơ hạ đường huyết khi dùng với insulin/sulfonylurea'],
        'pharmacokinetics': {'half_life': '2-3 giờ (ngắn)', 'onset':
        '2-4 tuần (giảm HbA1c)', 'duration': '12-24 giờ', 'protein_binding':
        '9%', 'clearance': 'Thận (thải trừ chủ yếu), gan (chuyển hóa)'},
        'storage': 'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm',
        'black_box_warnings':
        'Có thể gây viêm tụy cấp hiếm nhưng nguy hiểm. Ngừng ngay nếu có dấu hiệu viêm tụy cấp (đau bụng, nôn)'
        , 'drug_interactions': {'major': [], 'moderate': [{'drug':
        'Insulin, Sulfonylurea (Glibenclamide, Gliclazide)', 'mechanism':
        'Vildagliptin tăng tiết insulin, tác dụng cộng dồn với insulin/sulfonylurea.'
        , 'effect': 'Tăng nguy cơ hạ đường huyết', 'management':
        'Thận trọng. Có thể cần giảm liều insulin/sulfonylurea. Theo dõi đường huyết chặt chẽ.'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Đái tháo đường type 1 - không hiệu quả (cần insulin)',
        'Nhiễm toan ceton - cần insulin, không dùng vildagliptin',
        'Suy gan nặng - chống chỉ định'], 'tương_đối': [
        'Suy thận nặng (CrCl <30) - thận trọng, có thể cần giảm liều',
        'Có thai - category C, thận trọng',
        'Viêm tụy trước đây - tăng nguy cơ viêm tụy cấp']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Vildagliptin là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt đầu.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Không biết vildagliptin có bài tiết vào sữa mẹ hay không. Thận trọng khi dùng khi cho con bú.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Theo dõi chức năng gan.', 'moderate':
        'Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan chặt chẽ.',
        'severe':
        'Chống chỉ định. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc tính.',
        'notes':
        'Vildagliptin chuyển hóa ở gan. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ độc tính, đặc biệt viêm tụy cấp.'
        }, 'overdose_management': {'symptoms': [
        'Hạ đường huyết (nếu dùng với insulin/sulfonylurea)',
        'Viêm tụy cấp (đau bụng, nôn, sốt)', 'Nhức đầu, chóng mặt'], 'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng vildagliptin ngay lập tức',
        'Nếu hạ đường huyết: glucose đường uống hoặc IV, theo dõi đường huyết',
        'Nếu viêm tụy cấp: điều trị hỗ trợ, nhịn ăn, truyền dịch, giảm đau, theo dõi chức năng tụy'
        , 'Theo dõi đường huyết, chức năng gan, chức năng tụy'], 'monitoring':
        'Đường huyết, dấu hiệu viêm tụy cấp, chức năng gan, dấu hiệu sinh tồn'},
        'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Uống với bữa ăn (tăng hấp thu). Có thể uống sáng và tối với bữa ăn.',
        'timing': 'Uống 2 lần/ngày (sáng và tối), cách đều, với bữa ăn.'}, 'iv':
        {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Vildagliptin (Galvus)',
        'UpToDate - Vildagliptin: Drug Information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ], 'last_updated': '2025-02-04', 'evidence_level':
        'A - Dựa trên FDA drug labels và dữ liệu lâm sàng'}}}

__all__ = ['DPP_4_INHIBITORS_DRUGS']
