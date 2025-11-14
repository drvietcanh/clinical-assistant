"""Infectious Disease & Antibiotic Drugs (Other) - Macrolides, Fluoroquinolones, Antimalarials, etc."""

# Antimalarials

ANTIMALARIALS_DRUGS = {
    "Chloroquine": {'group': 'Infectious Disease - Antimalarial', 'vietnamese_name':
        'Chloroquine, Aralen', 'administration': ['PO'], 'indications': [
        'Sốt rét (phòng ngừa và điều trị)', 'Amebiasis ngoài gan',
        'Lupus ban đỏ hệ thống', 'Viêm khớp dạng thấp'], 'contraindications': [
        'Dị ứng chloroquine/4-aminoquinoline', 'Bệnh võng mạc', 'Bệnh gan nặng',
        'Bệnh thận nặng', 'Rối loạn tạo máu'], 'dosage': {
        'adult_malaria_treatment':
        '600mg base (1g phosphate) ngày đầu, sau đó 300mg base (500mg phosphate) sau 6-8 giờ, sau đó 300mg base/ngày x 2 ngày'
        , 'adult_malaria_prophylaxis':
        '300mg base (500mg phosphate) x 1 lần/tuần, bắt đầu 1-2 tuần trước khi đi, tiếp tục trong khi ở và 4 tuần sau khi về'
        , 'adult_lupus': '200-400mg base/ngày', 'notes':
        'Rất độc cho võng mạc nếu dùng lâu dài. Theo dõi mắt định kỳ'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Giảm liều 50%',
        'under_30': 'Tránh dùng'}, 'side_effects': [
        'Độc võng mạc (dùng lâu dài, không hồi phục)', 'Rối loạn thị giác',
        'Ban da, rụng tóc', 'Rối loạn tạo máu', 'Rối loạn tim mạc (liều cao)',
        'Co giật (quá liều)', 'Độc gan'], 'interactions': [
        'Digoxin: tăng nồng độ digoxin', 'Cimetidine: tăng nồng độ chloroquine',
        'Ampicillin: giảm hấp thu ampicillin',
        'Kaolin: giảm hấp thu chloroquine'], 'pregnancy':
        'C - Thận trọng, nhưng có thể dùng cho sốt rét', 'mechanism_of_action':
        'Chloroquine là 4-aminoquinoline, ức chế polymerase của ký sinh trùng sốt rét, ngăn cản tổng hợp DNA và RNA. Thuốc tích lũy trong lysosome của ký sinh trùng, tăng pH và ức chế tiêu hóa hemoglobin. Đối với sốt rét, chloroquine diệt thể vô tính trong hồng cầu. Đối với bệnh tự miễn (lupus, RA), chloroquine ức chế hoạt động của tế bào miễn dịch và giảm sản xuất cytokine viêm'
        , 'monitoring': [
        'Khám mắt định kỳ mỗi 6-12 tháng nếu dùng lâu dài (theo dõi độc võng mạc)',
        'Thị trường (visual field) mỗi 6-12 tháng nếu dùng lâu dài',
        'Chức năng gan (ALT, AST) định kỳ',
        'Công thức máu toàn phần (CBC) định kỳ',
        'Điện tâm đồ nếu dùng liều cao (theo dõi rối loạn nhịp)',
        'Dấu hiệu rối loạn thị giác (nhìn mờ, ám điểm)',
        'Dấu hiệu độc võng mạc (không hồi phục nếu phát hiện muộn)'],
        'precautions': [
        'Rất độc cho võng mạc nếu dùng lâu dài - cần khám mắt định kỳ',
        'Ngừng ngay nếu có dấu hiệu độc võng mạc (nhìn mờ, ám điểm)',
        'Giảm liều 50% nếu suy thận (CrCl 30-60)',
        'Tránh dùng nếu suy thận nặng (CrCl <30)',
        'Có thể dùng trong thai kỳ cho sốt rét (category C)',
        'Tránh dùng với kaolin (giảm hấp thu)',
        'Tương tác với digoxin (tăng nồng độ digoxin)',
        'Có thể gây rối loạn nhịp tim nếu dùng liều cao (cần theo dõi ECG)'],
        'pharmacokinetics': {'half_life': '20-60 ngày (rất dài, tích lũy)',
        'onset': '2-3 giờ (sốt rét), 4-8 tuần (lupus/RA)', 'duration':
        '7-14 ngày (sốt rét), kéo dài (lupus/RA)', 'protein_binding': '55%',
        'clearance': 'Gan (chuyển hóa), thận (thải trừ - chậm)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings':
        'Có thể gây độc võng mạc nặng và không hồi phục nếu dùng lâu dài. Cần khám mắt định kỳ mỗi 6-12 tháng khi dùng lâu dài. Ngừng ngay nếu có dấu hiệu độc võng mạc'
        , 'drug_interactions': {'major': [{'drug': 'Digoxin', 'mechanism':
        'Chloroquine tăng nồng độ digoxin (cơ chế chưa rõ)', 'effect':
        'Tăng nồng độ digoxin, tăng nguy cơ độc tính digoxin (rối loạn nhịp, buồn nôn)'
        , 'management':
        'Theo dõi nồng độ digoxin, giảm liều digoxin nếu cần. Theo dõi ECG và triệu chứng độc tính digoxin'
        }], 'moderate': [{'drug': 'Cimetidine', 'mechanism':
        'Ức chế chuyển hóa chloroquine', 'effect':
        'Tăng nồng độ chloroquine, tăng độc tính', 'management':
        'Theo dõi độc tính chloroquine (võng mạc, gan, máu)'}, {'drug':
        'Ampicillin', 'mechanism': 'Chloroquine giảm hấp thu ampicillin',
        'effect': 'Giảm hiệu quả ampicillin', 'management':
        'Tách thời gian dùng (cách nhau ít nhất 2 giờ)'}, {'drug': 'Kaolin',
        'mechanism': 'Kaolin giảm hấp thu chloroquine', 'effect':
        'Giảm hiệu quả chloroquine', 'management':
        'Tách thời gian dùng (cách nhau ít nhất 2 giờ)'}]}, 'contraindications':
        {'tuyệt_đối': ['Dị ứng chloroquine hoặc 4-aminoquinoline',
        'Bệnh võng mạc (retinopathy) - đặc biệt nếu dùng lâu dài',
        'Suy gan nặng', 'Suy thận nặng (CrCl <30)'], 'tương_đối': [
        'Rối loạn tạo máu - thận trọng, theo dõi công thức máu',
        'Bệnh tim mạch - thận trọng với liều cao (có thể gây rối loạn nhịp)',
        'Bệnh võng mạc nhẹ - thận trọng, khám mắt thường xuyên']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Có thể dùng trong thai kỳ cho sốt rét (category C). Sốt rét có thể đe dọa tính mạng mẹ và thai nhi, nên điều trị vẫn cần thiết. Tuy nhiên, thận trọng với liều cao và dùng lâu dài (lupus, RA) do nguy cơ độc võng mạc. Cân nhắc lợi ích/nguy cơ.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Chloroquine bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình trạng lâm sàng. Sốt rét có thể đe dọa tính mạng, nên điều trị vẫn cần thiết'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi liều', 'moderate':
        'Không đổi liều, nhưng theo dõi chức năng gan', 'severe':
        'Tránh dùng hoặc dùng liều thấp dưới sự giám sát chặt chẽ. Theo dõi ALT/AST, bilirubin thường xuyên'
        , 'notes':
        'Chloroquine chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa và tăng tích lũy, tăng nguy cơ độc tính gan'
        }, 'overdose_management': {'symptoms': [
        'Rối loạn thị giác (nhìn mờ, ám điểm)',
        'Độc võng mạc (không hồi phục nếu phát hiện muộn)',
        'Rối loạn nhịp tim (liều cao)', 'Co giật (quá liều)',
        'Rối loạn tạo máu (giảm bạch cầu, giảm tiểu cầu)', 'Độc gan',
        'Ban da, rụng tóc'], 'antidote': 'Không có thuốc giải độc đặc hiệu',
        'treatment': ['Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1 giờ',
        'Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải',
        'Theo dõi ECG nếu có triệu chứng rối loạn nhịp',
        'Điều trị co giật nếu có (benzodiazepine)',
        'Theo dõi chức năng gan (ALT, AST, bilirubin)',
        'Theo dõi công thức máu (CBC) - theo dõi rối loạn tạo máu',
        'Khám mắt ngay (theo dõi độc võng mạc)',
        'Điều trị triệu chứng: Thuốc chống nôn, giảm đau nếu cần'],
        'monitoring':
        'ECG (nếu có triệu chứng rối loạn nhịp), chức năng gan (ALT, AST, bilirubin), công thức máu (CBC), khám mắt (theo dõi độc võng mạc), triệu chứng lâm sàng'
        }, 'reversal_agents': {'available': False, 'agents': None, 'notes':
        'Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ và theo dõi. Quan trọng: khám mắt ngay để phát hiện độc võng mạc sớm'
        }, 'administration_instructions': {'oral': {'with_food':
        'Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ'
        , 'timing':
        'Với sốt rét: 600mg base (1g phosphate) ngày đầu, sau đó 300mg base (500mg phosphate) sau 6-8 giờ, sau đó 300mg base/ngày x 2 ngày. Với phòng ngừa: 300mg base (500mg phosphate) x 1 lần/tuần. Với lupus/RA: 200-400mg base/ngày'
        , 'notes':
        'Rất độc cho võng mạc nếu dùng lâu dài (lupus, RA). Cần khám mắt định kỳ mỗi 6-12 tháng. Ngừng ngay nếu có dấu hiệu độc võng mạc. Tránh dùng với kaolin (giảm hấp thu)'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Chloroquine (Aralen)',
        'UpToDate - Chloroquine drug information',
        'WHO Guidelines for the treatment of malaria',
        'American Academy of Ophthalmology Guidelines for chloroquine retinopathy screening'
        , "Goodman & Gilman's Pharmacological Basis of Therapeutics"],
        'last_updated': '2025-02-04', 'evidence_level':
        'High - Guidelines dựa trên chứng cứ từ WHO, FDA và AAO'}},
    "Artesunate": {'group': 'Infectious Disease - Antimalarial (Artemisinin)',
        'vietnamese_name': 'Artesunate', 'administration': ['PO', 'IV', 'IM',
        'Rectal'], 'indications': ['Sốt rét nặng (severe malaria)',
        'Sốt rét kháng chloroquine', 'Sốt rét sốt rét P. falciparum',
        'Điều trị kết hợp sốt rét (ACT)'], 'contraindications': [
        'Dị ứng artesunate/artemisinin',
        '3 tháng đầu thai kỳ (trừ sốt rét nặng)',
        'Dùng đơn độc (phải dùng kết hợp)'], 'dosage': {'adult_severe_iv':
        '2.4mg/kg IV ngay, sau đó 1.2mg/kg sau 12 và 24 giờ, sau đó mỗi ngày',
        'adult_po':
        '200mg ngày đầu, sau đó 100mg x 1 lần/ngày x 5 ngày (với artemether-lumefantrine)'
        , 'adult_act':
        'Theo phác đồ ACT (artesunate + amodiaquine/ mefloquine/piperaquine)',
        'notes':
        'PHẢI dùng kết hợp với thuốc sốt rét khác (ACT). Không dùng đơn độc'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Thận trọng'}, 'side_effects': ['Nhức đầu', 'Chóng mặt',
        'Buồn nôn', 'Rối loạn tiêu hóa', 'Nhịp tim chậm (hiếm)',
        'Độc tính thần kinh (dùng lâu dài, liều cao - hiếm)'], 'interactions':
        ['Thuốc sốt rét khác: dùng kết hợp (ACT protocol)',
        'Warfarin: có thể tăng tác dụng chống đông',
        'CYP2A6 substrates: có thể tăng nồng độ'], 'pregnancy':
        'D - Tránh trong 3 tháng đầu (trừ sốt rét nặng)', 'mechanism_of_action':
        'Artesunate là dẫn xuất artemisinin (sesquiterpene lactone), chuyển hóa thành dihydroartemisinin (hoạt chất). Tác động nhanh và mạnh lên ký sinh trùng sốt rét bằng cách tạo ra các gốc tự do (free radicals) trong hồng cầu bị nhiễm, gây stress oxy hóa và phá vỡ màng tế bào ký sinh trùng. Artesunate diệt cả thể vô tính và thể giao tử (gametocyte), đặc biệt hiệu quả với P. falciparum kháng chloroquine. Thuốc có tác dụng nhanh (fast-acting), giảm số lượng ký sinh trùng trong 24-48 giờ'
        , 'monitoring': [
        'Theo dõi sốt và triệu chứng sốt rét (giảm nhanh trong 24-48 giờ)',
        'Ký sinh trùng trong máu (parasitemia) mỗi 6-12 giờ trong sốt rét nặng',
        'Chức năng gan (ALT, AST) nếu dùng lâu dài',
        'Dấu hiệu rối loạn nhịp tim (nhịp chậm - hiếm)',
        'Dấu hiệu độc tính thần kinh nếu dùng lâu dài, liều cao (hiếm)',
        'Đường huyết nếu dùng IV (có thể gây hạ đường huyết)'], 'precautions':
        [
        'PHẢI dùng kết hợp với thuốc sốt rét khác (ACT protocol) - không dùng đơn độc'
        ,
        'Tránh dùng trong 3 tháng đầu thai kỳ (trừ sốt rét nặng - cân nhắc lợi ích/nguy cơ)'
        , 'Dùng đúng phác đồ ACT để tránh kháng thuốc',
        'Không dùng đơn độc (dễ gây kháng thuốc)',
        'Có thể gây hạ đường huyết nếu dùng IV (theo dõi)',
        'Có thể gây nhịp tim chậm (hiếm - theo dõi ECG nếu có triệu chứng)',
        'Có thể tương tác với warfarin (tăng tác dụng chống đông)',
        'Dùng kết hợp với amodiaquine, mefloquine, hoặc piperaquine theo phác đồ ACT'
        ], 'pharmacokinetics': {'half_life':
        '45 phút (artesunate), 1-2 giờ (dihydroartemisinin)', 'onset':
        '1-2 giờ (giảm sốt, triệu chứng)', 'duration': '4-6 giờ (ngắn)',
        'protein_binding': 'Moderate', 'clearance':
        'Gan (chuyển hóa nhanh qua CYP2A6, esterase), thận (thải trừ)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để tủ lạnh (2-8°C) nếu yêu cầu'
        , 'black_box_warnings':
        'KHÔNG được dùng đơn độc - phải dùng kết hợp với thuốc sốt rét khác theo phác đồ ACT để tránh kháng thuốc. Tránh dùng trong 3 tháng đầu thai kỳ trừ sốt rét nặng (cân nhắc lợi ích/nguy cơ)'
        , 'drug_interactions': {'major': [{'drug':
        'Dùng đơn độc (không kết hợp)', 'mechanism':
        'Dùng artesunate đơn độc dễ gây kháng thuốc', 'effect':
        'Kháng thuốc sốt rét, thất bại điều trị', 'management':
        'PHẢI dùng kết hợp với thuốc sốt rét khác theo phác đồ ACT (artesunate + amodiaquine/mefloquine/piperaquine)'
        }], 'moderate': [{'drug': 'Warfarin', 'mechanism':
        'Có thể tăng tác dụng chống đông', 'effect':
        'Tăng INR, tăng nguy cơ chảy máu', 'management':
        'Theo dõi INR thường xuyên, điều chỉnh liều warfarin nếu cần'}, {'drug':
        'CYP2A6 substrates', 'mechanism':
        'Artesunate chuyển hóa qua CYP2A6, có thể ức chế hoặc cảm ứng',
        'effect':
        'Có thể tăng hoặc giảm nồng độ các thuốc chuyển hóa qua CYP2A6',
        'management': 'Thận trọng, theo dõi tác dụng phụ'}]},
        'contraindications': {'tuyệt_đối': [
        'Dùng đơn độc (phải dùng kết hợp với thuốc sốt rét khác)',
        'Dị ứng artesunate hoặc artemisinin'], 'tương_đối': [
        '3 tháng đầu thai kỳ - tránh trừ sốt rét nặng (cân nhắc lợi ích/nguy cơ)',
        'Suy thận nặng (CrCl <30) - thận trọng', 'Suy gan nặng - thận trọng']},
        'pregnancy_lactation': {'fda_category': 'D', 'pregnancy_details':
        'Tránh dùng trong 3 tháng đầu thai kỳ trừ sốt rét nặng (cân nhắc lợi ích/nguy cơ). Sốt rét nặng có thể đe dọa tính mạng mẹ và thai nhi, nên điều trị vẫn cần thiết. Có thể dùng trong tam cá nguyệt 2 và 3 nếu cần. Phải dùng kết hợp với thuốc sốt rét khác theo phác đồ ACT.'
        , 'lactation': {'safety': 'Unknown', 'details':
        'Artesunate bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc tùy theo tình trạng lâm sàng. Sốt rét nặng có thể đe dọa tính mạng, nên điều trị vẫn cần thiết'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi liều', 'moderate':
        'Không đổi liều, nhưng theo dõi chức năng gan', 'severe':
        'Thận trọng, theo dõi chức năng gan thường xuyên', 'notes':
        'Artesunate chuyển hóa nhanh ở gan qua CYP2A6 và esterase. Suy gan có thể làm giảm chuyển hóa, nhưng ít tích lũy do half-life ngắn'
        }, 'overdose_management': {'symptoms': ['Nhức đầu, chóng mặt',
        'Buồn nôn, nôn', 'Rối loạn tiêu hóa', 'Nhịp tim chậm (hiếm)',
        'Hạ đường huyết (nếu dùng IV)',
        'Độc tính thần kinh (nếu dùng lâu dài, liều cao - hiếm)'], 'antidote':
        'Không có thuốc giải độc đặc hiệu', 'treatment': ['Ngừng thuốc ngay',
        'Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải',
        'Theo dõi đường huyết nếu dùng IV (có thể gây hạ đường huyết)',
        'Theo dõi nhịp tim (ECG) nếu có triệu chứng nhịp chậm',
        'Điều trị triệu chứng: Thuốc chống nôn, giảm đau nếu cần',
        'Theo dõi chức năng gan nếu dùng lâu dài'], 'monitoring':
        'Triệu chứng lâm sàng, đường huyết (nếu dùng IV), nhịp tim (ECG nếu có triệu chứng), chức năng gan (nếu dùng lâu dài)'
        }, 'reversal_agents': {'available': False, 'agents': None, 'notes':
        'Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ và theo dõi'},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với thức ăn hoặc không', 'timing':
        'Theo phác đồ ACT. Thường: 200mg ngày đầu, sau đó 100mg x 1 lần/ngày x 5 ngày (với artemether-lumefantrine hoặc các phác đồ ACT khác)'
        , 'notes':
        'PHẢI dùng kết hợp với thuốc sốt rét khác (amodiaquine, mefloquine, piperaquine) theo phác đồ ACT. Không dùng đơn độc'
        }, 'iv': {'reconstitution':
        'Pha trong D5W hoặc NS. Dùng ngay sau khi pha', 'infusion_rate':
        'Truyền trong 5-10 phút', 'compatibility': ['D5W', 'NS'],
        'incompatibility': ['Không pha trộn với các thuốc khác'], 'notes':
        'Dùng cho sốt rét nặng. Liều: 2.4mg/kg IV ngay, sau đó 1.2mg/kg sau 12 và 24 giờ, sau đó mỗi ngày. Theo dõi đường huyết (có thể gây hạ đường huyết)'
        }, 'im': {'notes':
        'Có thể dùng IM cho sốt rét nặng nếu không có IV. Liều tương tự IV'},
        'rectal': {'notes':
        'Có thể dùng đường trực tràng cho trẻ em hoặc khi không có đường uống/IV. Liều theo cân nặng'
        }}, 'references': {'primary_sources': [
        'WHO Guidelines for the treatment of malaria',
        'WHO Guidelines for ACT (Artemisinin-based Combination Therapy)',
        'UpToDate - Artesunate drug information',
        'CDC Guidelines for treatment of malaria',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics"],
        'last_updated': '2025-02-04', 'evidence_level':
        'High - Guidelines dựa trên chứng cứ từ WHO và CDC'}}}

__all__ = ['ANTIMALARIALS_DRUGS']
