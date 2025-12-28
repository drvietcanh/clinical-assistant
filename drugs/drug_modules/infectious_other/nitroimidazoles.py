"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Nitroimidazoles

NITROIMIDAZOLES_DRUGS = {
    "Metronidazole": {'group': 'Infectious Disease - Nitroimidazole Antibiotic',
        'vietnamese_name': 'Metronidazole, Flagyl', 'administration': ['PO',
        'IV'], 'indications': ['Nhiễm khuẩn kỵ khí', 'Giardia', 'Trichomonas',
        'Amebiasis', 'Bacterial vaginosis', 'H. pylori (kết hợp)',
        'C. difficile colitis'], 'contraindications': ['Dị ứng metronidazole',
        'Có thai (3 tháng đầu)', 'Dùng disulfiram trong 14 ngày'], 'dosage': {
        'adult_anaerobic': '500mg x 3 lần/ngày PO hoặc 500mg mỗi 6-8 giờ IV',
        'adult_giardia': '250mg x 3 lần/ngày x 7 ngày', 'adult_trichomonas':
        '2g x 1 lần hoặc 500mg x 2 lần/ngày x 7 ngày', 'adult_c_diff':
        '500mg x 3 lần/ngày x 10-14 ngày', 'adult_h_pylori':
        '500mg x 2 lần/ngày (với amoxicillin + PPI)', 'notes':
        'TRÁNH RƯỢU (phản ứng disulfiram-like). Uống với thức ăn'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Giảm liều 50%'}, 'side_effects': [
        'Vị kim loại trong miệng', 'Buồn nôn, nôn', 'Đau đầu',
        'Phản ứng với rượu (nôn, đỏ mặt, nhịp tim nhanh)', 'Co giật (liều cao)',
        'Bệnh thần kinh ngoại biên (dùng lâu dài)', 'Ban da'], 'interactions':
        ['Rượu: phản ứng disulfiram-like (nôn, đỏ mặt) - TRÁNH',
        'Warfarin: tăng tác dụng chống đông', 'Lithium: tăng nồng độ lithium',
        'Phenytoin: tăng nồng độ phenytoin', 'Disulfiram: chống chỉ định'],
        'pregnancy': 'B - D trong 3 tháng đầu', 'mechanism_of_action':
        'Nitroimidazole kháng sinh/kháng ký sinh trùng. Sau khi vào tế bào vi khuẩn/ký sinh trùng, bị khử bởi ferredoxin (có trong vi khuẩn kỵ khí và ký sinh trùng) → tạo ra các gốc tự do độc hại phá hủy DNA. Chỉ hoạt động với vi khuẩn kỵ khí (Bacteroides, Clostridium, giardia) và ký sinh trùng (Trichomonas, Giardia, Entamoeba). KHÔNG hoạt động với vi khuẩn hiếu khí. Đặc biệt hiệu quả với kỵ khí và được dùng trong nhiễm trùng bụng, nhiễm trùng phụ khoa, và nhiễm C. difficile.'
        , 'monitoring': ['Dấu hiệu nhiễm trùng (sốt, WBC)',
        'Cấy máu và cấy từ vị trí nhiễm trùng',
        'Thần kinh (dị cảm, co giật, viêm dây thần kinh ngoại biên, chóng mặt, mất điều hòa)'
        , 'Dạ dày-ruột (buồn nôn, nôn, tiêu chảy, vị kim loại)',
        'Chức năng gan (ALT, AST) - hiếm viêm gan',
        'Số lượng bạch cầu (hiếm giảm bạch cầu)',
        'Phản ứng Disulfiram-like nếu uống rượu (buồn nôn, nôn, đỏ bừng, nhịp tim nhanh)'
        ], 'precautions': [
        'TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng thuốc - gây phản ứng Disulfiram-like nặng (buồn nôn, nôn, đỏ bừng, nhịp tim nhanh, hạ huyết áp)'
        ,
        'Nguy cơ tổn thương thần kinh ngoại biên và trung ương (dị cảm, co giật, viêm dây thần kinh) - tăng ở dùng kéo dài, liều cao, suy gan'
        , 'Ngừng nếu có dấu hiệu tổn thương thần kinh',
        'Không dùng cho nhiễm trùng do vi khuẩn hiếu khí (không hiệu quả)',
        'Uống với thức ăn để giảm kích ứng dạ dày',
        'Vị kim loại rất thường gặp - không phải tác dụng phụ nghiêm trọng nhưng khó chịu'
        , 'Có thể làm nước tiểu sẫm màu (vô hại)',
        'Thận trọng ở suy gan (giảm chuyển hóa → tăng nguy cơ tác dụng phụ thần kinh)'
        ,
        'Không dùng trong 3 tháng đầu thai kỳ (nguy cơ dị tật) - chỉ dùng khi thực sự cần thiết'
        , 'Pha trong NS, D5W, hoặc LR, truyền IV trong 30-60 phút'],
        'pharmacokinetics': {'half_life':
        '6-8 giờ (bình thường), 9-15 giờ (suy gan)', 'onset':
        '1-2 giờ (PO), ngay lập tức (IV)', 'duration':
        'q8h (PO/IV), q12h cho C. difficile (PO)', 'protein_binding': '< 20%',
        'metabolism': 'Gan (CYP450) - chuyển hóa mạnh', 'clearance':
        'Chủ yếu qua gan (60-80%), cần điều chỉnh ở suy gan nặng'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng. Viên nén: tránh ẩm. Dung dịch pha tiêm: sau khi pha, bảo quản ở nhiệt độ phòng 24 giờ, tránh ánh sáng.'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, phản ứng Disulfiram-like với rượu có thể nặng. Tổn thương thần kinh có thể không hồi phục. Nguy cơ dị tật thai nhi nếu dùng trong 3 tháng đầu thai kỳ.'
        , 'drug_interactions': {'major': [{'drug': 'Rượu (Ethanol)',
        'mechanism':
        'Metronidazole ức chế aldehyde dehydrogenase, enzyme chuyển hóa acetaldehyde (sản phẩm chuyển hóa của ethanol) thành acetate. Kết quả là tích lũy acetaldehyde, gây phản ứng Disulfiram-like.'
        , 'effect':
        'Phản ứng Disulfiram-like nặng: buồn nôn, nôn, đỏ bừng mặt, nhịp tim nhanh, hạ huyết áp, khó thở, có thể đe dọa tính mạng'
        , 'management':
        'TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng metronidazole. Tránh tất cả các sản phẩm chứa rượu (thuốc ho, nước súc miệng, thực phẩm có rượu). Nếu uống rượu, ngừng ngay metronidazole và điều trị hỗ trợ.'
        }, {'drug': 'Disulfiram', 'mechanism':
        'Cả hai đều ức chế aldehyde dehydrogenase, tác dụng cộng dồn làm tăng nguy cơ phản ứng Disulfiram-like và tổn thương thần kinh.'
        , 'effect':
        'Tăng nguy cơ phản ứng Disulfiram-like nặng, tăng nguy cơ tổn thương thần kinh'
        , 'management':
        'CHỐNG CHỈ ĐỊNH: Không dùng metronidazole trong vòng 14 ngày sau khi ngừng disulfiram. Nếu đang dùng disulfiram, không dùng metronidazole.'
        }, {'drug': 'Warfarin', 'mechanism':
        'Metronidazole ức chế chuyển hóa warfarin qua CYP2C9, làm tăng nồng độ warfarin và tăng tác dụng chống đông.'
        , 'effect': 'Tăng INR, tăng nguy cơ chảy máu nghiêm trọng',
        'management':
        'Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng metronidazole). Giảm liều warfarin 30-50%. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày).'
        }], 'moderate': [{'drug': 'Lithium', 'mechanism':
        'Metronidazole có thể làm giảm thải trừ lithium, làm tăng nồng độ lithium trong máu.'
        , 'effect':
        'Tăng nồng độ lithium, tăng nguy cơ độc tính lithium (buồn nôn, run, lú lẫn, suy thận)'
        , 'management':
        'Theo dõi nồng độ lithium thường xuyên. Có thể cần giảm liều lithium. Theo dõi dấu hiệu độc tính lithium.'
        }, {'drug': 'Phenytoin', 'mechanism':
        'Metronidazole ức chế chuyển hóa phenytoin qua CYP2C9, làm tăng nồng độ phenytoin.'
        , 'effect':
        'Tăng nồng độ phenytoin, tăng nguy cơ độc tính (chóng mặt, rung giật nhãn cầu, lú lẫn, co giật)'
        , 'management':
        'Theo dõi nồng độ phenytoin. Có thể cần giảm liều phenytoin. Theo dõi dấu hiệu độc tính phenytoin.'
        }, {'drug': 'Phenobarbital', 'mechanism':
        'Phenobarbital có thể cảm ứng enzyme chuyển hóa metronidazole, làm giảm nồng độ metronidazole.'
        , 'effect': 'Giảm nồng độ metronidazole, giảm hiệu quả kháng khuẩn',
        'management':
        'Có thể cần tăng liều metronidazole. Theo dõi đáp ứng điều trị.'}],
        'minor': [{'drug': 'Cimetidine', 'mechanism':
        'Cimetidine có thể ức chế chuyển hóa metronidazole, làm tăng nhẹ nồng độ metronidazole.'
        , 'effect': 'Tăng nhẹ nồng độ metronidazole', 'management':
        'Theo dõi dấu hiệu tác dụng phụ. Thường không cần điều chỉnh liều.'}]},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng metronidazole hoặc nitroimidazole',
        'Đang dùng disulfiram hoặc đã dùng disulfiram trong vòng 14 ngày - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI'
        ], 'tương_đối': [
        'Có thai (3 tháng đầu) - nguy cơ dị tật thai nhi, chỉ dùng khi thực sự cần thiết'
        , 'Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tác dụng phụ thần kinh',
        'Bệnh thần kinh ngoại biên - tăng nguy cơ tổn thương thần kinh',
        'Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu',
        'Bệnh nhân đang dùng lithium - tăng nguy cơ độc tính lithium',
        'Nhiễm trùng do vi khuẩn hiếu khí - không hiệu quả']},
        'contraindications_detail': {'tuyệt_đối': [
        'Dị ứng metronidazole hoặc nitroimidazole',
        'Đang dùng disulfiram hoặc đã dùng disulfiram trong vòng 14 ngày - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI'
        ], 'tương_đối': [
        'Có thai (3 tháng đầu) - nguy cơ dị tật thai nhi, chỉ dùng khi thực sự cần thiết'
        , 'Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tác dụng phụ thần kinh',
        'Bệnh thần kinh ngoại biên - tăng nguy cơ tổn thương thần kinh',
        'Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu',
        'Bệnh nhân đang dùng lithium - tăng nguy cơ độc tính lithium',
        'Nhiễm trùng do vi khuẩn hiếu khí - không hiệu quả']},
        'reversal_agents': {'available': False, 'agents': []},
        'pregnancy_lactation': {'fda_category': 'B (D trong 3 tháng đầu)',
        'pregnancy_details':
        'Metronidazole là thuốc phân loại B trong tam cá nguyệt thứ hai và thứ ba, nhưng phân loại D trong tam cá nguyệt đầu tiên. Các nghiên cứu trên động vật cho thấy nguy cơ dị tật bẩm sinh khi dùng trong tam cá nguyệt đầu tiên. Các nghiên cứu trên người cho thấy nguy cơ dị tật tăng nhẹ khi dùng trong tam cá nguyệt đầu tiên. Tránh dùng trong tam cá nguyệt đầu tiên nếu có thể. Nếu cần thiết, chỉ dùng khi lợi ích vượt quá nguy cơ. Có thể dùng trong tam cá nguyệt thứ hai và thứ ba khi cần thiết.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Metronidazole bài tiết vào sữa mẹ ở nồng độ tương đương nồng độ trong máu mẹ. Nồng độ trong sữa mẹ cao và có thể gây vị đắng cho trẻ sơ sinh. Tuy nhiên, không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng liều thông thường.'
        , 'recommendation':
        'Có thể dùng khi cho con bú, nhưng thận trọng. Có thể gây vị đắng cho trẻ sơ sinh. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả. Có thể cân nhắc ngừng cho con bú trong thời gian ngắn nếu dùng liều cao.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Metronidazole chuyển hóa qua gan (CYP450), nhưng không tích lũy đáng kể ở suy gan nhẹ.'
        , 'moderate':
        'Thận trọng, có thể cần giảm liều 25-50%. Theo dõi chức năng gan và dấu hiệu tác dụng phụ thần kinh.'
        , 'severe':
        'Giảm liều 50% hoặc tăng khoảng cách giữa các liều (q12h thay vì q8h). Theo dõi chức năng gan chặt chẽ. Theo dõi dấu hiệu tác dụng phụ thần kinh (dị cảm, co giật). Có thể cần tránh dùng nếu suy gan rất nặng.'
        , 'notes':
        'Metronidazole chuyển hóa mạnh qua gan (CYP450), thải trừ chủ yếu qua gan (60-80%). Half-life tăng từ 6-8 giờ (bình thường) lên 9-15 giờ (suy gan). Tích lũy ở suy gan nặng, làm tăng nguy cơ tác dụng phụ thần kinh. Cần điều chỉnh liều ở suy gan nặng.'
        }, 'overdose_management': {'symptoms': [
        'Triệu chứng thần kinh: Co giật, rối loạn ý thức, dị cảm, viêm dây thần kinh ngoại biên, chóng mặt, mất điều hòa (đặc biệt ở suy gan, liều cao)'
        , 'Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, vị kim loại',
        'Triệu chứng Disulfiram-like: Buồn nôn, nôn, đỏ bừng mặt, nhịp tim nhanh, hạ huyết áp, khó thở (nếu uống rượu)'
        ,
        'Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)',
        'Triệu chứng gan: Tăng men gan, viêm gan (hiếm)',
        'Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)'],
        'antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
        'treatment': ['Ngừng ngay metronidazole',
        'Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital'
        , 'Điều trị phản ứng Disulfiram-like nếu có (nếu uống rượu):',
        '  - Ngừng ngay metronidazole', '  - Bù dịch đầy đủ',
        '  - Hỗ trợ hô hấp nếu cần', '  - Điều trị hạ huyết áp nếu cần',
        '  - Theo dõi dấu hiệu sinh tồn',
        'Điều trị tổn thương thần kinh ngoại biên:',
        '  - Ngừng ngay metronidazole', '  - Điều trị hỗ trợ (vật lý trị liệu)',
        '  - Tổn thương có thể không hồi phục hoàn toàn',
        'Điều trị chảy máu nếu có:',
        '  - Bổ sung vitamin K nếu giảm prothrombin',
        '  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng',
        '  - Điều chỉnh liều warfarin nếu đang dùng', 'Điều trị dị ứng nếu có:',
        '  - Epinephrine nếu sốc phản vệ', '  - Antihistamine, corticosteroid',
        '  - Hỗ trợ hô hấp nếu cần',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2',
        'Lọc máu: Hemodialysis có thể loại bỏ metronidazole một phần (protein binding <20%), nhưng không hiệu quả lắm do chuyển hóa chủ yếu qua gan.'
        ], 'monitoring':
        'Theo dõi dấu hiệu thần kinh (co giật, ý thức, dị cảm, viêm dây thần kinh), dấu hiệu Disulfiram-like (nếu uống rượu), PT/INR (nếu dùng với warfarin), chức năng gan (ALT, AST), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có tổn thương thần kinh hoặc suy gan.'
        }, 'reversal_agents': {'available': False, 'agents': []}, 'administration_instructions': {'oral': {
        'with_food':
        'Nên uống với thức ăn để giảm kích ứng dạ dày và vị kim loại. Uống với thức ăn không ảnh hưởng đáng kể đến hấp thu.'
        , 'timing':
        'Uống 2-3 lần/ngày tùy chỉ định (anaerobic: 3 lần/ngày, C. difficile: 3 lần/ngày, H. pylori: 2 lần/ngày). Cách đều trong ngày. TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng.'
        }, 'iv': {'reconstitution':
        "Pha với NS (0.9% NaCl), D5W (5% Dextrose), hoặc Ringer's Lactate. Nồng độ pha: 5mg/ml (tối đa). Pha 500mg trong 100ml = 5mg/ml. Pha 1g trong 200ml = 5mg/ml. Lắc kỹ để hòa tan hoàn toàn. Bảo quản tránh ánh sáng."
        , 'infusion_rate':
        'Truyền IV trong 30-60 phút. Tốc độ: 100ml/30 phút = ~3.3ml/phút, 100ml/60 phút = ~1.7ml/phút. KHÔNG truyền nhanh (bolus) - tăng nguy cơ tác dụng phụ.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)',
        "Ringer's Lactate"], 'incompatibility': [
        'Aminophylline - tạo kết tủa, không pha chung',
        'Phenytoin - có thể tạo kết tủa, không pha chung',
        'Các thuốc có tính kiềm hoặc acid mạnh'], 'notes':
        'QUAN TRỌNG: 1) TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng, 2) Truyền chậm (30-60 phút) để giảm tác dụng phụ, 3) Bảo quản tránh ánh sáng, 4) Theo dõi dấu hiệu tổn thương thần kinh, 5) Điều chỉnh liều ở suy gan nặng.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Metronidazole (Flagyl)',
        'UpToDate - Metronidazole: Drug Information',
        'Medscape - Metronidazole Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Metronidazole Monograph',
        'Micromedex - Metronidazole Drug Information',
        'IDSA Guidelines - Anaerobic Infections, C. difficile Infection'],
        'last_updated': '2025-02-03', 'evidence_level':
        'A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }}}

__all__ = ['NITROIMIDAZOLES_DRUGS']
