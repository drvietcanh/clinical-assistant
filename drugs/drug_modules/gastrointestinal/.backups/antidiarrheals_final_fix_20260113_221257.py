"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Antidiarrheals

ANTIDIARRHEALS_DRUGS = {
    "Bismuth subsalicylate": {'group': 'Gastrointestinal - Antidiarrheal',
        "pregnancy": "C - Chứa salicylate, tránh trong thai kỳ",
        'vietnamese_name': 'Bismuth subsalicylate, Pepto-Bismol', 'administration': [
        'PO'],
        'indications': [
        'Tiêu chảy cấp', 'Tiêu chảy du lịch (traveler\'s diarrhea)',
        'Khó tiêu, đau bụng', 'Buồn nôn', 'Ợ chua'],
        'contraindications': [
        'Dị ứng aspirin hoặc salicylates', 'Trẻ em <12 tuổi (nguy cơ hội chứng Reye)',
        'Dùng aspirin hoặc thuốc chống đông', 'Suy thận nặng'],
        'dosage': {
        'adult_po': '524mg (2 viên hoặc 30ml) mỗi 30-60 phút (tối đa 8 liều/ngày)',
        'adult_max': '4.2g/ngày (8 liều)', 'notes':
        'Không dùng quá 2 ngày. Có thể làm phân đen (bình thường)'},
        'side_effects': [
        'Phân đen (bình thường, không nguy hiểm)', 'Lưỡi đen (bình thường)',
        'Táo bón (nếu dùng quá nhiều)', 'Buồn nôn', 'Nguy cơ hội chứng Reye (trẻ em)',
        'Nguy cơ chảy máu (nếu dùng với aspirin hoặc thuốc chống đông)'],
        'interactions': [
        'Aspirin: tăng nguy cơ chảy máu, tăng nguy cơ hội chứng Reye',
        'Warfarin: tăng nguy cơ chảy máu',
        'Tetracycline, Quinolone: giảm hấp thu kháng sinh (cách xa 2 giờ)',
        'Probenecid: giảm tác dụng probenecid'],
        'mechanism_of_action':
        'Bismuth subsalicylate là thuốc chống tiêu chảy và kháng khuẩn. Bismuth có tác dụng kháng khuẩn tại chỗ, ức chế sự phát triển của vi khuẩn gây tiêu chảy (E. coli, Salmonella, Shigella). Salicylate (từ phân hủy bismuth subsalicylate) có tác dụng chống viêm và giảm tiết dịch ruột. Bismuth cũng tạo lớp bảo vệ trên niêm mạc dạ dày và ruột, giảm kích ứng. Tác dụng: giảm tiêu chảy, giảm đau bụng, giảm buồn nôn, và có tác dụng kháng khuẩn. Bismuth subsalicylate được chuyển hóa thành bismuth carbonate và salicylate trong dạ dày. Salicylate được hấp thu và có tác dụng toàn thân (giống aspirin), nên có nguy cơ tương tác với aspirin và thuốc chống đông.'
        , 'monitoring': [
        'Đáp ứng lâm sàng (giảm tần suất đi ngoài, cải thiện tính chất phân)',
        'Phân đen, lưỡi đen - bình thường, không nguy hiểm, sẽ hết sau khi ngừng thuốc'
        , 'Dấu hiệu chảy máu (nếu dùng với aspirin hoặc warfarin) - theo dõi dấu hiệu chảy máu'
        , 'Dấu hiệu hội chứng Reye (nếu dùng ở trẻ em) - sốt, nôn, lú lẫn, co giật (nguy hiểm)'
        , 'Tương tác với tetracycline, quinolone (giảm hấp thu) - cần cách xa 2 giờ'],
        'precautions': [
        'CHỐNG CHỈ ĐỊNH ở trẻ em <12 tuổi - nguy cơ hội chứng Reye (nguy hiểm tính mạng)'
        , 'CHỐNG CHỈ ĐỊNH nếu dùng aspirin hoặc thuốc chống đông - tăng nguy cơ chảy máu'
        , 'Phân đen, lưỡi đen - bình thường, không nguy hiểm, sẽ hết sau khi ngừng thuốc'
        , 'Không dùng quá 2 ngày nếu không cải thiện (cần đánh giá lại nguyên nhân)'
        , 'Không vượt quá 4.2g/ngày (8 liều) - tăng nguy cơ tác dụng phụ'
        , 'Thận trọng ở bệnh nhân suy thận nặng - tích lũy bismuth và salicylate'
        , 'Uống cách xa tetracycline, quinolone ít nhất 2 giờ (giảm hấp thu kháng sinh)'
        , 'Thận trọng ở bệnh nhân có tiền sử loét dạ dày (salicylate có thể kích ứng)'
        , 'Nếu dùng với probenecid - giảm tác dụng probenecid'],
        'pharmacokinetics': {
        'half_life': 'Bismuth: không hấp thu đáng kể; Salicylate: 2-3 giờ (giống aspirin)',
        'onset': '30-60 phút', 'duration': '4-6 giờ', 'protein_binding':
        'Salicylate: 50-80%', 'metabolism':
        'Dạ dày: chuyển hóa thành bismuth carbonate và salicylate. Gan: salicylate chuyển hóa (giống aspirin).'
        , 'clearance':
        'Bismuth: không hấp thu, thải trừ qua phân. Salicylate: thận (thải trừ, giống aspirin).'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng lỏng: lắc kỹ trước khi dùng.'
        , 'black_box_warnings':
        'CHỐNG CHỈ ĐỊNH ở trẻ em <12 tuổi - nguy cơ hội chứng Reye (nguy hiểm tính mạng). CHỐNG CHỈ ĐỊNH nếu dùng aspirin hoặc thuốc chống đông - tăng nguy cơ chảy máu nghiêm trọng.'
        , 'drug_interactions': {'major': [{'drug': 'Aspirin', 'mechanism':
        'Cả hai đều chứa salicylate, tăng nồng độ salicylate', 'effect':
        'Tăng nguy cơ chảy máu, tăng nguy cơ hội chứng Reye, tăng nguy cơ độc tính salicylate'
        , 'management': 'CHỐNG CHỈ ĐỊNH - không dùng cùng aspirin.'}, {'drug': 'Warfarin',
        'mechanism': 'Salicylate tăng nguy cơ chảy máu, có thể tăng tác dụng warfarin',
        'effect': 'Tăng nguy cơ chảy máu nghiêm trọng', 'management':
        'CHỐNG CHỈ ĐỊNH - không dùng cùng warfarin. Theo dõi INR nếu phải dùng.'}],
        'moderate': [{'drug': 'Tetracycline, Quinolone (Ciprofloxacin, Levofloxacin)',
        'mechanism': 'Bismuth chelate với kháng sinh, giảm hấp thu', 'effect':
        'Giảm hấp thu kháng sinh, giảm hiệu quả', 'management':
        'Uống bismuth subsalicylate cách xa kháng sinh ít nhất 2 giờ.'}, {'drug':
        'Probenecid', 'mechanism': 'Salicylate giảm tác dụng probenecid', 'effect':
        'Giảm hiệu quả probenecid', 'management':
        'Tránh dùng cùng. Nếu phải dùng, tăng liều probenecid.'}],
        'minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng aspirin hoặc salicylates',
        'Trẻ em <12 tuổi - nguy cơ hội chứng Reye (nguy hiểm tính mạng)',
        'Dùng aspirin hoặc thuốc chống đông (warfarin) - tăng nguy cơ chảy máu nghiêm trọng'
        , 'Suy thận nặng - tích lũy bismuth và salicylate'],tương_đối': [
        'Suy thận nhẹ đến trung bình - thận trọng, tích lũy bismuth và salicylate',
        'Loét dạ dày - salicylate có thể kích ứng',
        'Mang thai - salicylate có thể ảnh hưởng thai nhi',
        'Dùng với tetracycline, quinolone - giảm hấp thu, cần cách xa 2 giờ']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Bismuth subsalicylate là FDA category C. Salicylate (từ phân hủy bismuth subsalicylate) có thể ảnh hưởng thai nhi, đặc biệt trong tam cá nguyệt cuối (nguy cơ đóng ống động mạch sớm, chảy máu). Tránh dùng trong tam cá nguyệt cuối. Có thể dùng trong tam cá nguyệt đầu và giữa nếu lợi ích > nguy cơ, nhưng nên tránh nếu có thể.'
        , 'lactation': {'safety': 'Compatible with caution', 'details':
        'Bismuth không hấp thu đáng kể, không bài tiết vào sữa mẹ. Salicylate có thể bài tiết vào sữa mẹ ở nồng độ thấp. Nguy cơ tác dụng phụ ở trẻ bú mẹ thấp nhưng có thể có.'
        , 'recommendation':
        'Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu tác dụng phụ.'}},hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Thận trọng',
        'severe': 'Thận trọng - salicylate chuyển hóa ở gan, có thể tích lũy', 'notes':
        'Salicylate chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa, tăng nguy cơ tích lũy. Thận trọng ở suy gan nặng.'},overdose_management': {'symptoms': [
        'Triệu chứng salicylate quá liều: ù tai, chóng mặt, buồn nôn, nôn, tăng thông khí, nhiễm toan chuyển hóa'
        , 'Triệu chứng bismuth quá liều: táo bón nặng, suy thận (hiếm)',
        'Hội chứng Reye (nếu dùng ở trẻ em): sốt, nôn, lú lẫn, co giật, hôn mê'],antidote':
        'Không có antidote đặc hiệu cho bismuth. Điều trị salicylate quá liều: bicarbonate để kiềm hóa nước tiểu và tăng thải trừ salicylate.',
        'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu bệnh nhân tỉnh táo)',
        'Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ',
        'Điều trị salicylate quá liều: bicarbonate để kiềm hóa nước tiểu (pH >7.5), tăng thải trừ salicylate'
        , 'Theo dõi nồng độ salicylate trong máu nếu có',
        'Điều trị nhiễm toan chuyển hóa: bicarbonate',
        'Hỗ trợ hô hấp nếu cần',
        'Lọc máu: có thể cần nếu salicylate quá liều nặng',
        'Điều trị hội chứng Reye nếu có (hỗ trợ, điều trị triệu chứng)'],
        'monitoring':
        'Theo dõi: nồng độ salicylate trong máu, pH máu, bicarbonate, dấu hiệu nhiễm toan chuyển hóa, ý thức, dấu hiệu hội chứng Reye (nếu trẻ em)'},reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị salicylate quá liều: bicarbonate để kiềm hóa nước tiểu và tăng thải trừ.'},administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không với thức ăn', 'timing':
        '524mg (2 viên hoặc 30ml) mỗi 30-60 phút khi có triệu chứng (tối đa 8 liều/ngày = 4.2g/ngày). Không dùng quá 2 ngày nếu không cải thiện. Uống cách xa tetracycline, quinolone ít nhất 2 giờ.'
        },iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],incompatibility': []}},references': {'primary_sources': ['FDA Drug Label - Pepto-Bismol',
        'UpToDate - Bismuth subsalicylate: Drug information', 'Micromedex - Bismuth subsalicylate',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics"],last_updated':
        '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'},
        "renal_adjustment": {
             "normal": "Không đổi",
             "30_60": "Thận trọng, có thể giảm liều",
             "under_30": "Giảm liều hoặc tránh dùng",
             "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy thận."
         },
    "Loperamide": {'group': 'Gastrointestinal - Antidiarrheal',
        'vietnamese_name':
        'Loperamide, Imodium', 'administration': ['PO'],
        'indications': [
        'Tiêu chảy cấp', 'Tiêu chảy mạn tính'],
        'contraindications': [
        'Tiêu chảy do nhiễm khuẩn (nặng)', 'Viêm đại tràng giả mạc', 'Tắc ruột',
        'Trẻ em <2 tuổi'],adult_maintenance': '2mg sau mỗi lần đi ngoài (tối đa 16mg/ngày)',
        'notes': 'Không dùng quá 48 giờ nếu không cải thiện'},
        'side_effects':
        ['Táo bón', 'Buồn nôn', 'Đau bụng', 'Buồn ngủ'],
        'interactions': [
        'Opioids: tăng tác dụng (ít dùng chung)'],
        'mechanism_of_action':
        'Opioid mu-receptor agonist ở ruột (peripheral opioid). Ức chế acetylcholine và prostaglandin ở cơ trơn ruột, giảm nhu động ruột, tăng trương lực cơ thắt hậu môn, tăng hấp thu nước từ phân. Tác dụng chống tiêu chảy. Không qua hàng rào máu-não đáng kể ở liều điều trị → ít tác dụng phụ thần kinh và ít nguy cơ nghiện hơn opioid hệ thống. Tuy nhiên, liều cao có thể qua hàng rào máu-não và gây tác dụng opioid hệ thống.'
        , 'monitoring': [
        'Đáp ứng lâm sàng (giảm tần suất đi ngoài, cải thiện tính chất phân)',
        'Dấu hiệu quá liều: ức chế hô hấp, giảm ý thức, co đồng tử (miosis)',
        'Dấu hiệu táo bón nặng (có thể gây tắc ruột giả)',
        'Dấu hiệu nhiễm khuẩn (nếu giữ vi khuẩn trong ruột quá lâu)',
        'Dấu hiệu viêm đại tràng giả mạc (tiêu chảy nặng, đau bụng, sốt) - nguy cơ nếu dùng với kháng sinh'
        ],
        'precautions': [
        'Chỉ dùng cho tiêu chảy không nhiễm khuẩn hoặc đã điều trị nhiễm khuẩn',
        'Không dùng quá 48 giờ nếu không cải thiện (cần đánh giá lại nguyên nhân)',
        'Không dùng cho tiêu chảy nhiễm khuẩn nặng (có thể giữ vi khuẩn trong ruột)'
        , 'Không dùng cho viêm đại tràng giả mạc (có thể làm nặng thêm)',
        'Không dùng cho trẻ em <2 tuổi (nguy cơ ức chế hô hấp)',
        'Không vượt quá 16mg/ngày (tăng nguy cơ tác dụng phụ hệ thống)',
        'Ngừng ngay nếu có dấu hiệu quá liều (ức chế hô hấp, giảm ý thức)',
        'Thận trọng ở bệnh nhân suy gan (giảm chuyển hóa)',
        'Thận trọng ở bệnh nhân suy thận (tích lũy)',
        'Nếu dùng với kháng sinh → tăng nguy cơ viêm đại tràng giả mạc'],
        'pharmacokinetics': {'half_life': '7-14 giờ', 'onset': '1-2 giờ',
        'duration': '4-6 giờ', 'protein_binding': '97%', 'metabolism':
        'Gan (chuyển hóa qua CYP3A4, CYP2C8)', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em (nguy cơ quá liều).'
        , 'black_box_warnings':
        'Liều cao có thể gây ức chế hô hấp nặng, có thể tử vong, đặc biệt ở trẻ em. Không dùng quá liều khuyến cáo (16mg/ngày). Không dùng cho trẻ em <2 tuổi. Không dùng cho tiêu chảy nhiễm khuẩn nặng - có thể giữ vi khuẩn trong ruột và làm nặng bệnh. Ngừng ngay nếu có dấu hiệu quá liều.'
        , 'drug_interactions': {'major': [{'drug':
        'Opioids (morphine, codeine, fentanyl, etc.)', 'mechanism':
        'Tác dụng hiệp đồng ức chế opioid mu-receptor', 'effect':
        'Tăng nguy cơ ức chế hô hấp, tăng nguy cơ tác dụng phụ opioid hệ thống',
        'management':
        'Tránh dùng cùng. Thận trọng nếu phải dùng cùng (giảm liều cả hai).'}],
        'moderate': [{'drug':
        'CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir, clarithromycin)'
        , 'mechanism': 'Ức chế chuyển hóa loperamide qua CYP3A4', 'effect':
        'Tăng nồng độ loperamide, tăng nguy cơ tác dụng phụ hệ thống (ức chế hô hấp)'
        , 'management':
        'Tránh dùng cùng hoặc giảm liều loperamide. Theo dõi dấu hiệu quá liều.'
        }, {'drug': 'CYP2C8 inhibitors (gemfibrozil)', 'mechanism':
        'Ức chế chuyển hóa loperamide', 'effect': 'Tăng nồng độ loperamide',
        'management': 'Thận trọng, giảm liều loperamide'}],
        'minor': []},contraindications': {'tuyệt_đối': ['Dị ứng loperamide',
        'Tiêu chảy nhiễm khuẩn nặng (C. difficile, E. coli O157:H7) - có thể giữ vi khuẩn trong ruột'
        , 'Viêm đại tràng giả mạc - có thể làm nặng thêm', 'Tắc ruột cơ học',
        'Trẻ em <2 tuổi - nguy cơ ức chế hô hấp',
        'Liều cao với CYP3A4 inhibitors - CHỐNG CHỈ ĐỊNH'],tương_đối': [
        'Suy gan nặng - giảm liều, tăng nguy cơ tích lũy',
        'Suy thận nặng - giảm liều, tăng nguy cơ tích lũy',
        'Tiêu chảy nhiễm khuẩn nhẹ - thận trọng, đã điều trị kháng sinh',
        'Trẻ em 2-6 tuổi - thận trọng, giảm liều',
        'Đang dùng opioids - tăng nguy cơ tác dụng phụ']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Loperamide là FDA category C. Nghiên cứu trên động vật cho thấy có thể gây độc tính cho thai nhi ở liều cao. Không có nghiên cứu đầy đủ trên người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng nên tránh trong tam cá nguyệt đầu nếu có thể. Dùng liều thấp nhất có hiệu quả.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Loperamide bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú ở liều điều trị.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}},hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Giảm liều 50%', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Loperamide chuyển hóa ở gan qua CYP3A4 và CYP2C8. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ hệ thống.'
        , 'notes':
        'Loperamide chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ, tăng nguy cơ ức chế hô hấp. Giảm liều hoặc tránh dùng ở suy gan nặng.'
        },overdose_management': {'symptoms': [
        'Ức chế hô hấp nặng (triệu chứng chính, có thể tử vong)',
        'Giảm ý thức, hôn mê', 'Co đồng tử (miosis)', 'Táo bón nặng, tắc ruột',
        'Buồn nôn, nôn', 'Buồn ngủ, lú lẫn'],antidote':
        'Naloxone (opioid antagonist) - có thể đảo ngược ức chế hô hấp',
        'treatment': [
        'Naloxone 0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)',
        'Hỗ trợ hô hấp: thông khí, oxy, nếu cần đặt nội khí quản',
        'Theo dõi dấu hiệu sinh tồn chặt chẽ',
        'Activated charcoal nếu uống trong vòng 1-2 giờ',
        'Điều trị tắc ruột nếu có'],
        'monitoring':
        'Theo dõi dấu hiệu sinh tồn (nhịp thở, SpO2, ý thức), dấu hiệu tắc ruột'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Naloxone', 'dose':
        '0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)',
        'mechanism': 'Opioid mu-receptor antagonist, đảo ngược ức chế hô hấp',
        'notes': 'Có thể đảo ngược ức chế hô hấp do quá liều loperamide'}]},administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không với thức ăn', 'timing':
        'Liều đầu: 4mg. Sau đó: 2mg sau mỗi lần đi ngoài (tối đa 16mg/ngày). Không dùng quá 48 giờ nếu không cải thiện.'
        },iv': {'reconstitution': 'Loperamide chỉ có dạng uống (PO)',
        'infusion_rate': 'N/A', 'compatibility': [],incompatibility': [],notes': 'Loperamide chỉ có dạng uống, không có dạng IV'}},references': {'primary_sources': ['FDA Drug Label - Loperamide',
        'UpToDate - Loperamide: Drug information', 'Micromedex - Loperamide',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'FDA Safety Communication - Loperamide abuse and overdose (2016)'],last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs, safety warnings'},
        "renal_adjustment": {
             "normal": "Không đổi",
             "30_60": "Thận trọng, có thể giảm liều",
             "under_30": "Giảm liều hoặc tránh dùng",
             "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy thận."
         },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [],
        },
        "guideline_tags": [
            "ACG 2017 GERD Guidelines",
            "FDA - Over-the-counter antacids",
        ]
    }
}

__all__ = ['ANTIDIARRHEALS_DRUGS']
