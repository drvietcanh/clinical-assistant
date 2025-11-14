"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Antidiarrheals

ANTIDIARRHEALS_DRUGS = {
    "Loperamide": {'group': 'Gastrointestinal - Antidiarrheal', 'vietnamese_name':
        'Loperamide, Imodium', 'administration': ['PO'], 'indications': [
        'Tiêu chảy cấp', 'Tiêu chảy mạn tính'], 'contraindications': [
        'Tiêu chảy do nhiễm khuẩn (nặng)', 'Viêm đại tràng giả mạc', 'Tắc ruột',
        'Trẻ em <2 tuổi'], 'dosage': {'adult_loading': '4mg x 1 lần',
        'adult_maintenance': '2mg sau mỗi lần đi ngoài (tối đa 16mg/ngày)',
        'notes': 'Không dùng quá 48 giờ nếu không cải thiện'}, 'side_effects':
        ['Táo bón', 'Buồn nôn', 'Đau bụng', 'Buồn ngủ'], 'interactions': [
        'Opioids: tăng tác dụng (ít dùng chung)'], 'pregnancy': 'C',
        'mechanism_of_action':
        'Opioid mu-receptor agonist ở ruột (peripheral opioid). Ức chế acetylcholine và prostaglandin ở cơ trơn ruột, giảm nhu động ruột, tăng trương lực cơ thắt hậu môn, tăng hấp thu nước từ phân. Tác dụng chống tiêu chảy. Không qua hàng rào máu-não đáng kể ở liều điều trị → ít tác dụng phụ thần kinh và ít nguy cơ nghiện hơn opioid hệ thống. Tuy nhiên, liều cao có thể qua hàng rào máu-não và gây tác dụng opioid hệ thống.'
        , 'monitoring': [
        'Đáp ứng lâm sàng (giảm tần suất đi ngoài, cải thiện tính chất phân)',
        'Dấu hiệu quá liều: ức chế hô hấp, giảm ý thức, co đồng tử (miosis)',
        'Dấu hiệu táo bón nặng (có thể gây tắc ruột giả)',
        'Dấu hiệu nhiễm khuẩn (nếu giữ vi khuẩn trong ruột quá lâu)',
        'Dấu hiệu viêm đại tràng giả mạc (tiêu chảy nặng, đau bụng, sốt) - nguy cơ nếu dùng với kháng sinh'
        ], 'precautions': [
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
        'Gan (chuyển hóa), thận (thải trừ)'}, 'storage':
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
        'management': 'Thận trọng, giảm liều loperamide'}], 'minor': []},
        'contraindications': {'tuyệt_đối': ['Dị ứng loperamide',
        'Tiêu chảy nhiễm khuẩn nặng (C. difficile, E. coli O157:H7) - có thể giữ vi khuẩn trong ruột'
        , 'Viêm đại tràng giả mạc - có thể làm nặng thêm', 'Tắc ruột cơ học',
        'Trẻ em <2 tuổi - nguy cơ ức chế hô hấp',
        'Liều cao với CYP3A4 inhibitors - CHỐNG CHỈ ĐỊNH'], 'tương_đối': [
        'Suy gan nặng - giảm liều, tăng nguy cơ tích lũy',
        'Suy thận nặng - giảm liều, tăng nguy cơ tích lũy',
        'Tiêu chảy nhiễm khuẩn nhẹ - thận trọng, đã điều trị kháng sinh',
        'Trẻ em 2-6 tuổi - thận trọng, giảm liều',
        'Đang dùng opioids - tăng nguy cơ tác dụng phụ']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Loperamide là FDA category C. Nghiên cứu trên động vật cho thấy có thể gây độc tính cho thai nhi ở liều cao. Không có nghiên cứu đầy đủ trên người. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ, nhưng nên tránh trong tam cá nguyệt đầu nếu có thể. Dùng liều thấp nhất có hiệu quả.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Loperamide bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú ở liều điều trị.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Dùng liều thường dùng.'}},
        'hepatic_adjustment': {'mild': 'Không cần chỉnh liều', 'moderate':
        'Giảm liều 50%', 'severe':
        'Giảm liều 50% hoặc tránh dùng. Loperamide chuyển hóa ở gan qua CYP3A4 và CYP2C8. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ hệ thống.'
        , 'notes':
        'Loperamide chuyển hóa ở gan. Suy gan nặng làm tăng nồng độ, tăng nguy cơ ức chế hô hấp. Giảm liều hoặc tránh dùng ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': [
        'Ức chế hô hấp nặng (triệu chứng chính, có thể tử vong)',
        'Giảm ý thức, hôn mê', 'Co đồng tử (miosis)', 'Táo bón nặng, tắc ruột',
        'Buồn nôn, nôn', 'Buồn ngủ, lú lẫn'], 'antidote':
        'Naloxone (opioid antagonist) - có thể đảo ngược ức chế hô hấp',
        'treatment': [
        'Naloxone 0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)',
        'Hỗ trợ hô hấp: thông khí, oxy, nếu cần đặt nội khí quản',
        'Theo dõi dấu hiệu sinh tồn chặt chẽ',
        'Activated charcoal nếu uống trong vòng 1-2 giờ',
        'Điều trị tắc ruột nếu có'], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn (nhịp thở, SpO2, ý thức), dấu hiệu tắc ruột'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Naloxone', 'dose':
        '0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút nếu cần (tối đa 10mg)',
        'mechanism': 'Opioid mu-receptor antagonist, đảo ngược ức chế hô hấp',
        'notes': 'Có thể đảo ngược ức chế hô hấp do quá liều loperamide'}]},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không với thức ăn', 'timing':
        'Liều đầu: 4mg. Sau đó: 2mg sau mỗi lần đi ngoài (tối đa 16mg/ngày). Không dùng quá 48 giờ nếu không cải thiện.'
        }, 'iv': {'reconstitution': 'Loperamide chỉ có dạng uống (PO)',
        'infusion_rate': 'N/A', 'compatibility': [], 'incompatibility': [],
        'notes': 'Loperamide chỉ có dạng uống, không có dạng IV'}},
        'references': {'primary_sources': ['FDA Drug Label - Loperamide',
        'UpToDate - Loperamide: Drug information', 'Micromedex - Loperamide',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'FDA Safety Communication - Loperamide abuse and overdose (2016)'],
        'last_updated': '2024-12-19', 'evidence_level':
        'High - FDA approved, multiple RCTs, safety warnings'}}}

__all__ = ['ANTIDIARRHEALS_DRUGS']
