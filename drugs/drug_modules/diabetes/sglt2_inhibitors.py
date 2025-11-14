"""Diabetes Medications
Active module - contains all diabetes drug data"""

# SGLT2 Inhibitors

SGLT2_INHIBITORS_DRUGS = {
    "Empagliflozin": {'group': 'Diabetes - SGLT2 Inhibitor', 'vietnamese_name':
        'Empagliflozin, Jardiance', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2', 'Suy tim với phân suất tống máu giảm (HFrEF)',
        'Bệnh thận mạn tính (CKD) ở bệnh nhân đái tháo đường',
        'Giảm nguy cơ tim mạch'], 'contraindications': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <20)',
        'Đang lọc máu', 'Nhiễm trùng đường tiết niệu tái phát'], 'dosage': {
        'adult_type2_dm': '10-25mg x 1 lần/ngày', 'adult_heart_failure':
        '10mg x 1 lần/ngày', 'adult_ckd': '10mg x 1 lần/ngày (eGFR ≥20)',
        'notes': 'Uống bất kỳ lúc nào, không cần ăn. Giảm đường huyết nhẹ'},
        'renal_adjustment': {'normal': '10-25mg/ngày', '30_60':
        '10mg/ngày (eGFR ≥30)', 'under_30': 'Không dùng nếu eGFR <20'},
        'side_effects': ['Nhiễm trùng đường tiết niệu',
        'Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu)',
        'Mất nước, hạ huyết áp', 'Nhiễm toan ceton (hiếm)',
        'Gãy xương tăng nhẹ', 'Hoại thư Fournier (hiếm nhưng nguy hiểm)'],
        'interactions': ['Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết',
        'Diuretics: tăng nguy cơ mất nước', 'Digoxin: tăng nhẹ nồng độ digoxin'
        ], 'pregnancy': 'C', 'mechanism_of_action':
        'Empagliflozin là chất ức chế chọn lọc sodium-glucose cotransporter 2 (SGLT2) ở ống lượn gần của thận. SGLT2 chịu trách nhiệm tái hấp thu 90% glucose từ nước tiểu. Bằng cách ức chế SGLT2, empagliflozin ngăn chặn tái hấp thu glucose, làm tăng bài tiết glucose qua nước tiểu (glucosuria), từ đó giảm đường huyết. Cơ chế này không phụ thuộc vào insulin, giúp giảm đường huyết mà không tăng nguy cơ hạ đường huyết (trừ khi dùng với insulin hoặc sulfonylurea). Ngoài ra, empagliflozin có lợi ích tim mạch và thận: giảm thể tích tuần hoàn, giảm huyết áp, giảm albumin niệu, và cải thiện kết cục tim mạch ở bệnh nhân suy tim và bệnh thận mạn. Các nghiên cứu EMPA-REG OUTCOME, EMPEROR-Reduced, và EMPEROR-Preserved đã chứng minh lợi ích tim mạch và thận.'
        , 'monitoring': [
        'Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết',
        'Chức năng thận (eGFR, creatinine) - không dùng nếu eGFR <20',
        'Nhiễm trùng đường tiết niệu (UTI) - triệu chứng, cấy nước tiểu nếu cần',
        'Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu) - đặc biệt ở phụ nữ'
        ,
        'Dấu hiệu mất nước, hạ huyết áp (đặc biệt ở người cao tuổi, dùng diuretics)'
        ,
        'Nhiễm toan ceton (DKA) - glucose máu, ketone, pH máu nếu có triệu chứng',
        'Hoại thư Fournier (nhiễm trùng vùng sinh dục nặng) - hiếm nhưng nguy hiểm'
        , 'Gãy xương (đặc biệt ở người cao tuổi)'], 'precautions': [
        'Không dùng cho đái tháo đường type 1 (tăng nguy cơ nhiễm toan ceton)',
        'Không dùng nếu eGFR <20 (empagliflozin) hoặc <25 (dapagliflozin) - không hiệu quả'
        ,
        'Tăng nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục - vệ sinh tốt, uống nhiều nước'
        ,
        'Nguy cơ nhiễm toan ceton (DKA) - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính, nhịn ăn'
        ,
        'Nguy cơ mất nước, hạ huyết áp - đặc biệt ở người cao tuổi, dùng diuretics, suy tim'
        ,
        'Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea - có thể cần giảm liều'
        ,
        'Hoại thư Fournier - hiếm nhưng nguy hiểm, cần chú ý vệ sinh vùng sinh dục'
        , 'Uống nhiều nước để giảm nguy cơ nhiễm trùng',
        'Có thể dùng bất kỳ lúc nào, không cần ăn',
        'Lợi ích tim mạch và thận độc lập với tác dụng giảm đường huyết'],
        'pharmacokinetics': {'half_life': '12.4 giờ', 'onset': '1 giờ',
        'duration': '24 giờ', 'protein_binding': '86.2%', 'clearance':
        'Gan: chuyển hóa qua glucuronidation (phần lớn). Thận: bài tiết một phần nguyên dạng và metabolites. Không cần điều chỉnh liều ở suy gan, nhưng không dùng nếu eGFR <20.'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Insulin, Sulfonylurea (glibenclamide, gliclazide)', 'mechanism':
        'Tác dụng hiệp đồng giảm đường huyết', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Giảm liều insulin hoặc sulfonylurea khi bắt đầu empagliflozin. Theo dõi đường huyết chặt chẽ.'
        }, {'drug': 'Loop diuretics (furosemide, torsemide)', 'mechanism':
        'Tăng bài tiết natri và nước', 'effect':
        'Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp', 'management':
        'Thận trọng. Theo dõi huyết áp, cân nặng, chức năng thận. Có thể cần giảm liều diuretic.'
        }], 'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Empagliflozin có thể tăng nhẹ nồng độ digoxin', 'effect':
        'Tăng nguy cơ độc tính digoxin', 'management':
        'Theo dõi nồng độ digoxin, ECG. Điều chỉnh liều digoxin nếu cần.'}, {
        'drug': 'Thiazide diuretics (hydrochlorothiazide)', 'mechanism':
        'Tăng bài tiết natri và nước', 'effect':
        'Tăng nguy cơ mất nước, hạ huyết áp', 'management':
        'Thận trọng. Theo dõi huyết áp, cân nặng.'}], 'minor': [{'drug':
        'UDP-glucuronosyltransferase (UGT) inducers', 'mechanism':
        'Có thể giảm nồng độ empagliflozin', 'effect':
        'Giảm hiệu quả empagliflozin', 'management':
        'Thận trọng. Theo dõi đường huyết.'}]}, 'contraindications': {
        'tuyệt_đối': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <20)',
        'Đang lọc máu', 'Dị ứng empagliflozin'], 'tương_đối': [
        'Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng',
        'Suy tim nặng - tăng nguy cơ mất nước',
        'Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp',
        'Dùng diuretics - tăng nguy cơ mất nước',
        'Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Không có nghiên cứu đầy đủ ở người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Không nên dùng trong 3 tháng đầu trừ khi thực sự cần thiết. Có thể gây hạ đường huyết ở thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Empagliflozin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi (không chuyển hóa đáng kể qua gan)', 'notes':
        'Empagliflozin chủ yếu chuyển hóa qua glucuronidation ở gan, nhưng không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Chưa có nghiên cứu đầy đủ ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': ['Hạ đường huyết', 'Mất nước',
        'Hạ huyết áp', 'Nhiễm toan ceton (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Điều trị hạ đường huyết: Glucose 15-20g PO hoặc dextrose IV',
        'Bù dịch nếu mất nước, hạ huyết áp', 'Theo dõi đường huyết, điện giải',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính không hiệu quả (do không hấp thu qua đường tiêu hóa tốt)',
        'Theo dõi chức năng thận',
        'Nếu có nhiễm toan ceton: điều trị theo protocol DKA'], 'monitoring':
        'Đường huyết, huyết áp, cân nặng, chức năng thận, điện giải, dấu hiệu nhiễm toan ceton'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.',
        'timing':
        'Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Jardiance (empagliflozin)',
        'EMPA-REG OUTCOME Study - New England Journal of Medicine',
        'EMPEROR-Reduced Study - New England Journal of Medicine',
        'EMPEROR-Preserved Study - New England Journal of Medicine',
        'UpToDate - Empagliflozin: Drug information'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple large RCTs (EMPA-REG OUTCOME, EMPEROR-Reduced, EMPEROR-Preserved)'
        }},
    "Dapagliflozin": {'group': 'Diabetes - SGLT2 Inhibitor', 'vietnamese_name':
        'Dapagliflozin, Forxiga', 'administration': ['PO'], 'indications': [
        'Đái tháo đường type 2', 'Suy tim với phân suất tống máu giảm (HFrEF)',
        'Bệnh thận mạn tính (CKD) ở bệnh nhân đái tháo đường'],
        'contraindications': ['Đái tháo đường type 1', 'Nhiễm toan ceton',
        'Suy thận nặng (eGFR <25)', 'Đang lọc máu',
        'Nhiễm trùng đường tiết niệu tái phát'], 'dosage': {'adult_type2_dm':
        '5-10mg x 1 lần/ngày', 'adult_heart_failure': '10mg x 1 lần/ngày',
        'adult_ckd': '10mg x 1 lần/ngày (eGFR ≥25)', 'notes':
        'Uống bất kỳ lúc nào'}, 'renal_adjustment': {'normal': '5-10mg/ngày',
        '30_60': '10mg/ngày (eGFR ≥25)', 'under_30': 'Không dùng nếu eGFR <25'},
        'side_effects': ['Nhiễm trùng đường tiết niệu',
        'Nhiễm trùng đường sinh dục', 'Mất nước', 'Nhiễm toan ceton (hiếm)'],
        'interactions': ['Insulin/Sulfonylurea: tăng nguy cơ hạ đường huyết',
        'Diuretics: mất nước'], 'pregnancy': 'C', 'mechanism_of_action':
        'Dapagliflozin là chất ức chế chọn lọc sodium-glucose cotransporter 2 (SGLT2) ở ống lượn gần của thận. SGLT2 chịu trách nhiệm tái hấp thu 90% glucose từ nước tiểu. Bằng cách ức chế SGLT2, dapagliflozin ngăn chặn tái hấp thu glucose, làm tăng bài tiết glucose qua nước tiểu (glucosuria), từ đó giảm đường huyết. Cơ chế này không phụ thuộc vào insulin, giúp giảm đường huyết mà không tăng nguy cơ hạ đường huyết (trừ khi dùng với insulin hoặc sulfonylurea). Dapagliflozin có lợi ích tim mạch và thận: giảm thể tích tuần hoàn, giảm huyết áp, giảm albumin niệu, và cải thiện kết cục tim mạch ở bệnh nhân suy tim và bệnh thận mạn. Các nghiên cứu DECLARE-TIMI 58 và DAPA-HF đã chứng minh lợi ích tim mạch và thận.'
        , 'monitoring': [
        'Đường huyết (HbA1c, glucose máu) - đánh giá hiệu quả giảm đường huyết',
        'Chức năng thận (eGFR, creatinine) - không dùng nếu eGFR <25',
        'Nhiễm trùng đường tiết niệu (UTI) - triệu chứng, cấy nước tiểu nếu cần',
        'Nhiễm trùng đường sinh dục (nấm âm đạo, viêm quy đầu) - đặc biệt ở phụ nữ'
        ,
        'Dấu hiệu mất nước, hạ huyết áp (đặc biệt ở người cao tuổi, dùng diuretics)'
        ,
        'Nhiễm toan ceton (DKA) - glucose máu, ketone, pH máu nếu có triệu chứng',
        'Hoại thư Fournier (nhiễm trùng vùng sinh dục nặng) - hiếm nhưng nguy hiểm'
        ], 'precautions': [
        'Không dùng cho đái tháo đường type 1 (tăng nguy cơ nhiễm toan ceton)',
        'Không dùng nếu eGFR <25 - không hiệu quả',
        'Tăng nguy cơ nhiễm trùng đường tiết niệu và đường sinh dục - vệ sinh tốt, uống nhiều nước'
        ,
        'Nguy cơ nhiễm toan ceton (DKA) - đặc biệt ở bệnh nhân type 1, phẫu thuật, bệnh cấp tính, nhịn ăn'
        ,
        'Nguy cơ mất nước, hạ huyết áp - đặc biệt ở người cao tuổi, dùng diuretics, suy tim'
        ,
        'Tăng nguy cơ hạ đường huyết khi dùng với insulin hoặc sulfonylurea - có thể cần giảm liều'
        ,
        'Hoại thư Fournier - hiếm nhưng nguy hiểm, cần chú ý vệ sinh vùng sinh dục'
        , 'Uống nhiều nước để giảm nguy cơ nhiễm trùng',
        'Có thể dùng bất kỳ lúc nào, không cần ăn',
        'Lợi ích tim mạch và thận độc lập với tác dụng giảm đường huyết'],
        'pharmacokinetics': {'half_life': '12.9 giờ', 'onset': '1 giờ',
        'duration': '24 giờ', 'protein_binding': '91%', 'clearance':
        'Gan: chuyển hóa qua glucuronidation (phần lớn). Thận: bài tiết một phần nguyên dạng và metabolites. Không cần điều chỉnh liều ở suy gan, nhưng không dùng nếu eGFR <25.'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Insulin, Sulfonylurea (glibenclamide, gliclazide)', 'mechanism':
        'Tác dụng hiệp đồng giảm đường huyết', 'effect':
        'Tăng nguy cơ hạ đường huyết', 'management':
        'Giảm liều insulin hoặc sulfonylurea khi bắt đầu dapagliflozin. Theo dõi đường huyết chặt chẽ.'
        }, {'drug': 'Loop diuretics (furosemide, torsemide)', 'mechanism':
        'Tăng bài tiết natri và nước', 'effect':
        'Tăng nguy cơ mất nước, hạ huyết áp, suy thận cấp', 'management':
        'Thận trọng. Theo dõi huyết áp, cân nặng, chức năng thận. Có thể cần giảm liều diuretic.'
        }], 'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Dapagliflozin có thể tăng nhẹ nồng độ digoxin', 'effect':
        'Tăng nguy cơ độc tính digoxin', 'management':
        'Theo dõi nồng độ digoxin, ECG. Điều chỉnh liều digoxin nếu cần.'}, {
        'drug': 'Thiazide diuretics (hydrochlorothiazide)', 'mechanism':
        'Tăng bài tiết natri và nước', 'effect':
        'Tăng nguy cơ mất nước, hạ huyết áp', 'management':
        'Thận trọng. Theo dõi huyết áp, cân nặng.'}], 'minor': [{'drug':
        'UDP-glucuronosyltransferase (UGT) inducers', 'mechanism':
        'Có thể giảm nồng độ dapagliflozin', 'effect':
        'Giảm hiệu quả dapagliflozin', 'management':
        'Thận trọng. Theo dõi đường huyết.'}]}, 'contraindications': {
        'tuyệt_đối': ['Đái tháo đường type 1',
        'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <25)',
        'Đang lọc máu', 'Dị ứng dapagliflozin'], 'tương_đối': [
        'Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng',
        'Suy tim nặng - tăng nguy cơ mất nước',
        'Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp',
        'Dùng diuretics - tăng nguy cơ mất nước',
        'Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Không có nghiên cứu đầy đủ ở người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Không nên dùng trong 3 tháng đầu trừ khi thực sự cần thiết. Có thể gây hạ đường huyết ở thai nhi. Theo dõi đường huyết chặt chẽ trong thai kỳ.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Dapagliflozin bài tiết vào sữa mẹ ở nồng độ thấp. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi (không chuyển hóa đáng kể qua gan)', 'notes':
        'Dapagliflozin chủ yếu chuyển hóa qua glucuronidation ở gan, nhưng không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Chưa có nghiên cứu đầy đủ ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': ['Hạ đường huyết', 'Mất nước',
        'Hạ huyết áp', 'Nhiễm toan ceton (hiếm)'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Điều trị hạ đường huyết: Glucose 15-20g PO hoặc dextrose IV',
        'Bù dịch nếu mất nước, hạ huyết áp', 'Theo dõi đường huyết, điện giải',
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính không hiệu quả (do không hấp thu qua đường tiêu hóa tốt)',
        'Theo dõi chức năng thận',
        'Nếu có nhiễm toan ceton: điều trị theo protocol DKA'], 'monitoring':
        'Đường huyết, huyết áp, cân nặng, chức năng thận, điện giải, dấu hiệu nhiễm toan ceton'
        }, 'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.',
        'timing':
        'Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Nên uống vào cùng một thời điểm mỗi ngày để dễ nhớ.'
        }, 'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Forxiga (dapagliflozin)',
        'DECLARE-TIMI 58 Study - New England Journal of Medicine',
        'DAPA-HF Study - New England Journal of Medicine',
        'UpToDate - Dapagliflozin: Drug information'], 'last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple large RCTs (DECLARE-TIMI 58, DAPA-HF)'}}}

__all__ = ['SGLT2_INHIBITORS_DRUGS']
