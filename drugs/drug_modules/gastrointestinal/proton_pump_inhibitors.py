"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Proton Pump Inhibitors

PROTON_PUMP_INHIBITORS_DRUGS = {
    "Pantoprazole": {'group': 'Gastrointestinal - Proton Pump Inhibitor', 'vietnamese_name':
        'Pantoprazole, Pantoloc', 'administration': ['PO', 'IV'], 'indications':
        ['Loét dạ dày tá tràng', 'GERD', 'Phòng ngừa loét do stress'],
        'contraindications': ['Dị ứng'], 'dosage': {'adult_po':
        '40mg x 1-2 lần/ngày', 'adult_iv': '40mg x 1-2 lần/ngày', 'notes':
        'Ít tương tác hơn omeprazole với clopidogrel'}, 'side_effects': [
        'Nhức đầu', 'Tiêu chảy', 'Tương tự omeprazole'], 'interactions': [
        'Ít tương tác hơn omeprazole'], 'pregnancy': 'B', 'mechanism_of_action':
        'Proton pump inhibitor (PPI). Ức chế H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày mạnh và kéo dài. Khác với H2 blockers, PPI ức chế bước cuối cùng của quá trình tiết acid, nên hiệu quả hơn. Pantoprazole ít tương tác với CYP450 hơn omeprazole.'
        , 'monitoring': ['Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng',
        'Mg2+ máu (nếu dùng kéo dài >3 tháng) - PPI có thể gây hạ magie máu',
        'Vitamin B12 (nếu dùng kéo dài >2 năm) - PPI giảm hấp thu B12',
        'Dấu hiệu nhiễm trùng: PPI tăng nguy cơ viêm phổi, C. difficile colitis',
        'Loãng xương: PPI dùng kéo dài có thể tăng nguy cơ gãy xương (cần monitor nếu >1 năm)'
        ], 'precautions': [
        'Uống 30-60 phút TRƯỚC bữa ăn (để PPI hoạt động khi proton pump được kích hoạt)'
        ,
        'KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated)',
        'Pantoprazole ưu điểm: ít tương tác với CYP450 hơn omeprazole, ít ảnh hưởng đến clopidogrel hơn'
        , 'Dùng ngắn hạn khi có thể - tránh dùng kéo dài không cần thiết',
        'Thận trọng ở bệnh nhân loãng xương (PPI dùng kéo dài có thể tăng nguy cơ gãy xương)'
        ,
        'Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều nhưng monitor)',
        'Tăng nguy cơ viêm phổi, C. difficile colitis (đặc biệt ở người già, suy giảm miễn dịch)'
        ], 'pharmacokinetics': {'half_life':
        '1 giờ (ngắn), nhưng tác dụng kéo dài 24h do ức chế không thuận nghịch proton pump'
        , 'onset': '1-3 ngày (tác dụng đầy đủ)', 'duration':
        '24 giờ (mặc dù half-life ngắn)', 'protein_binding': '98%', 'clearance':
        'Gan (CYP2C19, CYP3A4) - ít tương tác hơn omeprazole'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài'
        , 'drug_interactions': {'major': [{'drug':
        'Atazanavir (HIV protease inhibitor)', 'mechanism':
        'PPI làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)',
        'effect': 'Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV',
        'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng pantoprazole với atazanavir. Dùng H2 blocker hoặc cách thời gian 12 giờ.'
        }], 'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Pantoprazole ít ức chế CYP450 hơn omeprazole, nhưng vẫn có thể tương tác nhẹ'
        , 'effect': 'Có thể tăng INR nhẹ', 'management':
        'Theo dõi INR thường xuyên. Pantoprazole ít ảnh hưởng hơn omeprazole.'},
        {'drug': 'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)',
        'effect': 'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole.'}, {
        'drug': 'Iron salts (ferrous sulfate, ferrous fumarate)', 'mechanism':
        'PPI giảm acid dạ dày, giảm chuyển Fe3+ thành Fe2+', 'effect':
        'Giảm hấp thu sắt', 'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng sắt dạng chelate.'}, {'drug':
        'Vitamin B12 (cobalamin)', 'mechanism':
        'PPI giảm acid dạ dày, giảm tách B12 khỏi protein thức ăn', 'effect':
        'Giảm hấp thu B12 sau 2-3 năm dùng PPI', 'management':
        'Bổ sung B12 định kỳ nếu dùng lâu dài (>2 năm).'}], 'minor': [{'drug':
        'Clopidogrel', 'mechanism':
        'Pantoprazole ít ức chế CYP2C19 hơn omeprazole', 'effect':
        'Ít ảnh hưởng đến clopidogrel hơn omeprazole, nhưng vẫn thận trọng',
        'management':
        'Pantoprazole là lựa chọn tốt hơn omeprazole khi cần dùng với clopidogrel. Vẫn nên tránh dùng cùng nếu có thể.'
        }]}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng pantoprazole hoặc PPI khác',
        'Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối'
        ], 'tương_đối': [
        'Suy gan nặng (Child-Pugh C) - thận trọng, có thể giảm liều',
        'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng',
        'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài',
        'Nhiễm C. difficile - tăng nguy cơ',
        'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài',
        'Thiếu magnesium - bổ sung nếu dùng lâu dài']}, 'pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'Pantoprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. An toàn hơn omeprazole (category C) trong thai kỳ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Pantoprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. Không có báo cáo tác dụng phụ ở trẻ bú mẹ. An toàn khi cho con bú.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng (40mg/ngày).'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều, nhưng thận trọng', 'severe':
        'Thận trọng ở suy gan nặng (Child-Pugh C). Có thể giảm liều. Pantoprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4, nhưng ít phụ thuộc vào CYP2C19 hơn omeprazole.'
        , 'notes':
        'Pantoprazole ít tương tác với CYP450 hơn omeprazole, nên ít ảnh hưởng hơn ở suy gan. Tuy nhiên, vẫn thận trọng ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': [
        'PPI ít gây quá liều nghiêm trọng',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy, chóng mặt'],
        'antidote': 'Không có antidote đặc hiệu', 'treatment': [
        'Hỗ trợ triệu chứng', 'Theo dõi dấu hiệu sinh tồn',
        'Hầu hết trường hợp tự khỏi'], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn, triệu chứng nhẹ'}, 'reversal_agents': None,
        'administration_instructions': {'oral': {'with_food':
        'Uống 30-60 phút TRƯỚC bữa ăn (quan trọng - để PPI hoạt động khi proton pump được kích hoạt)'
        , 'timing':
        'Uống vào buổi sáng trước bữa sáng (hoặc trước bữa tối nếu dùng 2 lần/ngày). KHÔNG được nhai hoặc nghiền viên bao tan trong ruột - phải nuốt nguyên viên.'
        }, 'iv': {'reconstitution':
        'Pantoprazole IV: 40mg pha với 100ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate':
        'Truyền trong 15 phút (IV bolus) hoặc 30 phút (infusion)',
        'compatibility': ['NaCl 0.9%', 'Dextrose 5%'], 'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể.'}},
        'references': {'primary_sources': ['FDA Drug Label - Pantoprazole',
        'UpToDate - Proton pump inhibitors: Overview of use and adverse effects',
        'Micromedex - Pantoprazole',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'JAMA - Pantoprazole vs omeprazole and clopidogrel interaction (2010)'],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs'}},
    "Lansoprazole": {'group': 'Gastrointestinal - Proton Pump Inhibitor', 'vietnamese_name':
        'Lansoprazole, Prevacid', 'administration': ['PO'], 'indications':
        ['Loét dạ dày tá tràng', 'GERD', 'Phòng ngừa loét do stress', 'Zollinger-Ellison syndrome'],
        'contraindications': ['Dị ứng lansoprazole hoặc PPI'], 'dosage': {'adult_standard':
        '15-30mg x 1 lần/ngày', 'adult_gerd': '30mg x 1 lần/ngày', 'adult_ulcer':
        '30mg x 1 lần/ngày x 4-8 tuần', 'notes':
        'Uống 30 phút trước bữa ăn. Có thể mở viên nang và trộn với nước táo nếu cần'}, 'side_effects': [
        'Nhức đầu', 'Tiêu chảy', 'Đau bụng', 'Buồn nôn', 'Tương tự các PPI khác'], 'interactions': [
        'Warfarin: có thể tăng INR', 'Theophylline: tăng nồng độ theophylline',
        'Ketoconazole: giảm hấp thu (cách xa 2 giờ)'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Proton pump inhibitor (PPI). Ức chế H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày mạnh và kéo dài. Lansoprazole được chuyển hóa chủ yếu qua CYP2C19 và CYP3A4. Tương tự omeprazole nhưng có thể có tương tác ít hơn với một số thuốc.',
        'monitoring': ['Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng',
        'Mg2+ máu (nếu dùng kéo dài >3 tháng) - PPI có thể gây hạ magie máu',
        'Vitamin B12 (nếu dùng kéo dài >2 năm) - PPI giảm hấp thu B12',
        'Dấu hiệu nhiễm trùng: PPI tăng nguy cơ viêm phổi, C. difficile colitis',
        'Loãng xương: PPI dùng kéo dài có thể tăng nguy cơ gãy xương (cần monitor nếu >1 năm)'],
        'precautions': [
        'Uống 30 phút TRƯỚC bữa ăn (để PPI hoạt động khi proton pump được kích hoạt)',
        'KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated)',
        'Có thể mở viên nang và trộn với nước táo nếu bệnh nhân không nuốt được viên',
        'Dùng ngắn hạn khi có thể - tránh dùng kéo dài không cần thiết',
        'Thận trọng ở bệnh nhân loãng xương (PPI dùng kéo dài có thể tăng nguy cơ gãy xương)',
        'Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều nhưng monitor)',
        'Tăng nguy cơ viêm phổi, C. difficile colitis (đặc biệt ở người già, suy giảm miễn dịch)'],
        'pharmacokinetics': {'half_life':
        '1-2 giờ (ngắn), nhưng tác dụng kéo dài 24h do ức chế không thuận nghịch proton pump',
        'onset': '1-3 ngày (tác dụng đầy đủ)', 'duration':
        '24 giờ (mặc dù half-life ngắn)', 'protein_binding': '97%', 'clearance':
        'Gan (CYP2C19, CYP3A4)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài',
        'drug_interactions': {'major': [{'drug':
        'Atazanavir (HIV protease inhibitor)', 'mechanism':
        'PPI làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)',
        'effect': 'Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV', 'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng lansoprazole với atazanavir. Dùng H2 blocker hoặc cách thời gian 12 giờ.'}],
        'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Lansoprazole ức chế CYP2C19, có thể ảnh hưởng đến chuyển hóa warfarin',
        'effect': 'Có thể tăng INR', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}, {'drug':
        'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)',
        'effect': 'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole.'}, {'drug':
        'Theophylline', 'mechanism':
        'Lansoprazole có thể ức chế chuyển hóa theophylline, tăng nồng độ',
        'effect': 'Tăng nồng độ theophylline, tăng độc tính', 'management':
        'Theo dõi nồng độ theophylline và điều chỉnh liều nếu cần.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng lansoprazole hoặc PPI khác',
        'Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối'], 'tương_đối': [
        'Suy gan nặng (Child-Pugh C) - thận trọng, có thể giảm liều',
        'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng',
        'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài',
        'Nhiễm C. difficile - tăng nguy cơ',
        'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài',
        'Thiếu magnesium - bổ sung nếu dùng lâu dài']}, 'pregnancy_lactation': {'fda_category': 'B',
        'pregnancy_details':
        'Lansoprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.',
        'lactation': {'safety': 'Compatible', 'details':
        'Lansoprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. Không có báo cáo tác dụng phụ ở trẻ bú mẹ. An toàn khi cho con bú.',
        'recommendation': 'Có thể dùng khi cho con bú. Dùng liều thường dùng (15-30mg/ngày).'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều, nhưng thận trọng', 'severe':
        'Thận trọng ở suy gan nặng (Child-Pugh C). Có thể giảm liều. Lansoprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4.',
        'notes':
        'Lansoprazole chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ. Thận trọng ở suy gan nặng.'},
        'overdose_management': {'symptoms': [
        'PPI ít gây quá liều nghiêm trọng',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy, chóng mặt'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Hỗ trợ triệu chứng', 'Theo dõi dấu hiệu sinh tồn',
        'Hầu hết trường hợp tự khỏi'], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn, triệu chứng nhẹ'}, 'reversal_agents': None,
        'administration_instructions': {'oral': {'with_food':
        'Uống 30 phút TRƯỚC bữa ăn (quan trọng - để PPI hoạt động khi proton pump được kích hoạt)',
        'timing':
        'Uống vào buổi sáng trước bữa sáng. KHÔNG được nhai hoặc nghiền viên bao tan trong ruột - phải nuốt nguyên viên. Có thể mở viên nang và trộn với nước táo nếu bệnh nhân không nuốt được viên.'},
        'iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [], 'incompatibility': [], 'notes': 'Chỉ có dạng uống'}},
        'references': {'primary_sources': ['FDA Drug Label - Lansoprazole',
        'UpToDate - Proton pump inhibitors: Overview of use and adverse effects',
        'Micromedex - Lansoprazole',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"], 'last_updated':
        '2025-02-04', 'evidence_level': 'High - FDA approved, multiple RCTs'}},
    "Esomeprazole": {'group': 'Gastrointestinal - Proton Pump Inhibitor', 'vietnamese_name':
        'Esomeprazole, Nexium', 'administration': ['PO', 'IV'], 'indications':
        ['Loét dạ dày tá tràng', 'GERD', 'Phòng ngừa loét do stress', 'Zollinger-Ellison syndrome'],
        'contraindications': ['Dị ứng esomeprazole hoặc PPI'], 'dosage': {'adult_standard':
        '20-40mg x 1 lần/ngày', 'adult_gerd': '40mg x 1 lần/ngày', 'adult_ulcer':
        '40mg x 1 lần/ngày x 4-8 tuần', 'adult_iv': '20-40mg IV x 1-2 lần/ngày', 'notes':
        'Uống 30-60 phút trước bữa ăn. Esomeprazole là S-enantiomer của omeprazole, hiệu quả hơn'}, 'side_effects': [
        'Nhức đầu', 'Tiêu chảy', 'Đau bụng', 'Buồn nôn', 'Tương tự các PPI khác'], 'interactions': [
        'Warfarin: có thể tăng INR', 'Clopidogrel: có thể giảm hiệu quả (ức chế CYP2C19)',
        'Ketoconazole: giảm hấp thu (cách xa 2 giờ)'], 'pregnancy': 'B',
        'mechanism_of_action':
        'Proton pump inhibitor (PPI). Esomeprazole là S-enantiomer của omeprazole, có dược động học tốt hơn và hiệu quả mạnh hơn omeprazole. Ức chế H+/K+-ATPase (proton pump) ở tế bào thành dạ dày, giảm tiết acid dạ dày mạnh và kéo dài. Esomeprazole được chuyển hóa chủ yếu qua CYP2C19 và CYP3A4.',
        'monitoring': ['Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng',
        'Mg2+ máu (nếu dùng kéo dài >3 tháng) - PPI có thể gây hạ magie máu',
        'Vitamin B12 (nếu dùng kéo dài >2 năm) - PPI giảm hấp thu B12',
        'Dấu hiệu nhiễm trùng: PPI tăng nguy cơ viêm phổi, C. difficile colitis',
        'Loãng xương: PPI dùng kéo dài có thể tăng nguy cơ gãy xương (cần monitor nếu >1 năm)'],
        'precautions': [
        'Uống 30-60 phút TRƯỚC bữa ăn (để PPI hoạt động khi proton pump được kích hoạt)',
        'KHÔNG được nhai hoặc nghiền viên bao tan trong ruột (enteric-coated)',
        'Esomeprazole là S-enantiomer của omeprazole, hiệu quả mạnh hơn và dược động học tốt hơn',
        'Dùng ngắn hạn khi có thể - tránh dùng kéo dài không cần thiết',
        'Thận trọng ở bệnh nhân loãng xương (PPI dùng kéo dài có thể tăng nguy cơ gãy xương)',
        'Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều nhưng monitor)',
        'Tăng nguy cơ viêm phổi, C. difficile colitis (đặc biệt ở người già, suy giảm miễn dịch)',
        'Thận trọng với clopidogrel (ức chế CYP2C19, có thể giảm hiệu quả clopidogrel)'],
        'pharmacokinetics': {'half_life':
        '1-1.5 giờ (ngắn), nhưng tác dụng kéo dài 24h do ức chế không thuận nghịch proton pump',
        'onset': '1-3 ngày (tác dụng đầy đủ)', 'duration':
        '24 giờ (mặc dù half-life ngắn)', 'protein_binding': '97%', 'clearance':
        'Gan (CYP2C19, CYP3A4) - ít phụ thuộc CYP2C19 hơn omeprazole'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm) và liều cao. Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài',
        'drug_interactions': {'major': [{'drug':
        'Atazanavir (HIV protease inhibitor)', 'mechanism':
        'PPI làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)',
        'effect': 'Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV', 'management':
        'CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng esomeprazole với atazanavir. Dùng H2 blocker hoặc cách thời gian 12 giờ.'}],
        'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Esomeprazole ức chế CYP2C19, có thể ảnh hưởng đến chuyển hóa warfarin',
        'effect': 'Có thể tăng INR', 'management':
        'Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần.'}, {'drug':
        'Clopidogrel', 'mechanism':
        'Esomeprazole ức chế CYP2C19, enzyme cần thiết để kích hoạt clopidogrel',
        'effect': 'Giảm hiệu quả clopidogrel, tăng nguy cơ huyết khối', 'management':
        'Thận trọng. Cân nhắc dùng pantoprazole thay vì esomeprazole khi cần dùng với clopidogrel. Hoặc cách thời gian.'},
        {'drug': 'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'PPI tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)',
        'effect': 'Giảm nồng độ azole, giảm hiệu quả điều trị', 'management':
        'Cách thời gian ít nhất 2 giờ. Hoặc dùng dạng lỏng posaconazole.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng esomeprazole hoặc PPI khác',
        'Dùng cùng atazanavir (HIV protease inhibitor) - CHỐNG CHỈ ĐỊNH tuyệt đối'], 'tương_đối': [
        'Suy gan nặng (Child-Pugh C) - thận trọng, có thể giảm liều',
        'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng',
        'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài',
        'Nhiễm C. difficile - tăng nguy cơ',
        'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài',
        'Thiếu magnesium - bổ sung nếu dùng lâu dài',
        'Dùng với clopidogrel - thận trọng (có thể giảm hiệu quả clopidogrel)']}, 'pregnancy_lactation': {'fda_category': 'B',
        'pregnancy_details':
        'Esomeprazole là FDA category B. Nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Một số nghiên cứu quan sát không cho thấy tăng nguy cơ dị tật bẩm sinh. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.',
        'lactation': {'safety': 'Compatible', 'details':
        'Esomeprazole bài tiết vào sữa mẹ ở nồng độ rất thấp. Không có báo cáo tác dụng phụ ở trẻ bú mẹ. An toàn khi cho con bú.',
        'recommendation': 'Có thể dùng khi cho con bú. Dùng liều thường dùng (20-40mg/ngày).'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Không cần chỉnh liều, nhưng thận trọng', 'severe':
        'Thận trọng ở suy gan nặng (Child-Pugh C). Có thể giảm liều. Esomeprazole chuyển hóa ở gan qua CYP2C19 và CYP3A4, nhưng ít phụ thuộc CYP2C19 hơn omeprazole.',
        'notes':
        'Esomeprazole chuyển hóa ở gan nhưng ít phụ thuộc CYP2C19 hơn omeprazole. Thận trọng ở suy gan nặng.'},
        'overdose_management': {'symptoms': [
        'PPI ít gây quá liều nghiêm trọng',
        'Triệu chứng nhẹ: nhức đầu, buồn nôn, tiêu chảy, chóng mặt'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Hỗ trợ triệu chứng', 'Theo dõi dấu hiệu sinh tồn',
        'Hầu hết trường hợp tự khỏi'], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn, triệu chứng nhẹ'}, 'reversal_agents': None,
        'administration_instructions': {'oral': {'with_food':
        'Uống 30-60 phút TRƯỚC bữa ăn (quan trọng - để PPI hoạt động khi proton pump được kích hoạt)',
        'timing':
        'Uống vào buổi sáng trước bữa sáng (hoặc trước bữa tối nếu dùng 2 lần/ngày). KHÔNG được nhai hoặc nghiền viên bao tan trong ruột - phải nuốt nguyên viên.'},
        'iv': {'reconstitution':
        'Esomeprazole IV: 20-40mg pha với 100ml NaCl 0.9% hoặc dextrose 5%',
        'infusion_rate':
        'Truyền trong 10-30 phút', 'compatibility': ['NaCl 0.9%', 'Dextrose 5%'],
        'incompatibility': [
        'Không pha với các thuốc khác trong cùng đường truyền'], 'notes':
        'Chỉ dùng IV khi không uống được. Chuyển sang PO sớm nhất có thể.'}},
        'references': {'primary_sources': ['FDA Drug Label - Esomeprazole',
        'UpToDate - Proton pump inhibitors: Overview of use and adverse effects',
        'Micromedex - Esomeprazole',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"], 'last_updated':
        '2025-02-04', 'evidence_level': 'High - FDA approved, multiple RCTs'}}}

__all__ = ['PROTON_PUMP_INHIBITORS_DRUGS']
