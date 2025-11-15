"""Corticosteroids - Short/Intermediate Acting"""

SHORT_INTERMEDIATE_ACTING = {
    "Prednisolone": {'group': 'Endocrinology - Corticosteroid', 'vietnamese_name':
    'Prednisolone', 'administration': ['PO'], 'indications': [
    'Viêm khớp dạng thấp', 'Hen phế quản', 'Bệnh tự miễn',
    'Suy thượng thận', 'Dị ứng nặng'], 'contraindications': [
    'Nhiễm khuẩn hệ thống không điều trị',
    'Loét dạ dày tá tràng đang hoạt động', 'Dị ứng'], 'dosage': {
    'adult_standard': '5-60mg/ngày tùy chỉ định', 'adult_high':
    '1-2mg/kg/ngày cho bệnh nặng', 'notes':
    'Giảm dần liều khi ngừng, không ngừng đột ngột. Uống buổi sáng với thức ăn'
    }, 'side_effects': ['Tăng đường huyết', 'Tăng huyết áp', 'Loãng xương',
    'Ức chế miễn dịch', 'Tăng cân', 'Loét dạ dày', 'Rối loạn tâm thần',
    'Ức chế trục HPA (khi ngừng)'], 'interactions': [
    'Warfarin: thay đổi tác dụng chống đông',
    'NSAID: tăng nguy cơ loét dạ dày', 'Insulin/OAD: tăng đường huyết',
    'Vaccines: giảm hiệu quả vaccine'], 'pregnancy': 'C',
    'mechanism_of_action':
    'Glucocorticoid tổng hợp, tác dụng trung bình. Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm, ức chế phospholipase A2 → giảm prostaglandin và leukotriene. Có tác dụng mineralocorticoid nhẹ (ít hơn hydrocortisone). Ức chế miễn dịch. Được dùng trong nhiều tình trạng viêm và tự miễn. Tác dụng tương tự prednisone nhưng prednisolone là dạng hoạt động (không cần chuyển hóa ở gan).'
    , 'monitoring': [
    'Đường huyết (tăng đường huyết, đặc biệt ở bệnh nhân đái tháo đường)',
    'Huyết áp (tăng huyết áp)', 'Điện giải (natri, kali)',
    'Dấu hiệu nhiễm trùng (ức chế miễn dịch)',
    'Dạ dày (dấu hiệu loét, xuất huyết)',
    'Tâm thần (rối loạn tâm thần, mất ngủ, kích động)',
    'Xương (loãng xương nếu dùng kéo dài)',
    'Mắt (tăng nhãn áp, đục thủy tinh thể)',
    'Chức năng thượng thận (ức chế trục HPA nếu dùng kéo dài)'],
    'precautions': [
    'KHÔNG được ngừng đột ngột nếu dùng > 1 tuần (có thể gây suy thượng thận cấp - nguy hiểm tính mạng)'
    , 'Phải giảm liều dần dần (tapering) nếu dùng > 1 tuần',
    'Ức chế miễn dịch - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm nấm, lao',
    'Không dùng trong nhiễm nấm hệ thống không điều trị',
    'Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)',
    'Thận trọng ở bệnh nhân loét dạ dày (tăng nguy cơ)',
    'Thận trọng ở bệnh nhân tăng huyết áp',
    'Dùng với thức ăn để giảm kích ứng dạ dày',
    'Dự phòng loãng xương nếu dùng kéo dài (bổ sung calcium, vitamin D)',
    'Theo dõi dấu hiệu nhiễm trùng (ức chế miễn dịch có thể che dấu triệu chứng)'
    , 'Liều thay thế: 5-7.5mg/ngày, liều chống viêm: 20-60mg/ngày'],
    'pharmacokinetics': {'half_life':
    '2-3 giờ (ngắn, nhưng tác dụng kéo dài hơn do tác động gen)', 'onset':
    '1-2 giờ (PO)', 'duration': '18-36 giờ', 'protein_binding': '90-95%',
    'metabolism':
    'Gan (CYP3A4) - prednisolone là dạng hoạt động (khác prednisone)',
    'clearance': 'Gan, không cần điều chỉnh thận'}, 'storage':
    'Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.'
    , 'black_box_warnings':
    'Không có black box warning. Tuy nhiên, ngừng đột ngột sau khi dùng kéo dài có thể gây suy thượng thận cấp, có thể tử vong. Ức chế miễn dịch mạnh có thể làm nặng nhiễm trùng hoặc gây nhiễm trùng cơ hội.'
    , 'drug_interactions': {'major': [{'drug':
    'Ketoconazole, Itraconazole (Azole antifungals)', 'mechanism':
    'Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa prednisolone, tăng nồng độ và tác dụng.'
    , 'effect':
    'Tăng nồng độ prednisolone, tăng tác dụng và tác dụng phụ (Cushing, tăng đường huyết, ức chế miễn dịch)'
    , 'management':
    'Giảm liều prednisolone 25-50% khi dùng với azole antifungals. Theo dõi đường huyết, dấu hiệu Cushing.'
    }, {'drug': 'Rifampin, Rifabutin', 'mechanism':
    'Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa prednisolone, giảm nồng độ và hiệu quả.'
    , 'effect': 'Giảm nồng độ prednisolone, giảm hiệu quả điều trị',
    'management':
    'Tăng liều prednisolone 25-50% khi dùng với rifampin. Theo dõi đáp ứng điều trị.'
    }, {'drug': 'Warfarin', 'mechanism':
    'Corticosteroid có thể thay đổi chuyển hóa warfarin và ảnh hưởng đến đông máu.'
    , 'effect':
    'Thay đổi INR (có thể tăng hoặc giảm), tăng nguy cơ chảy máu hoặc huyết khối'
    , 'management':
    'Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng prednisolone. Điều chỉnh liều warfarin nếu cần.'
    }], 'moderate': [{'drug': 'NSAID (Ibuprofen, Naproxen, Diclofenac)',
    'mechanism':
    'Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.', 'effect':
    'Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa nghiêm trọng',
    'management':
    'Cân nhắc dùng PPI hoặc misoprostol. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu chảy máu dạ dày.'
    }, {'drug': 'Phenytoin, Phenobarbital, Carbamazepine', 'mechanism':
    'Cảm ứng enzyme chuyển hóa, tăng chuyển hóa prednisolone.', 'effect':
    'Giảm nồng độ prednisolone, giảm hiệu quả', 'management':
    'Tăng liều prednisolone. Theo dõi đáp ứng điều trị.'}, {'drug':
    'Cyclosporine, Tacrolimus', 'mechanism':
    'Cả hai đều ức chế miễn dịch, tác dụng cộng dồn. Có thể ảnh hưởng đến chuyển hóa.'
    , 'effect':
    'Tăng ức chế miễn dịch, tăng nguy cơ nhiễm trùng, tăng nguy cơ độc tính',
    'management':
    'Giảm liều cả hai thuốc. Theo dõi chức năng thận, dấu hiệu nhiễm trùng.'
    }], 'minor': [{'drug': 'Diuretics (Thiazide, Furosemide)', 'mechanism':
    'Corticosteroid gây giữ natri, có thể đối kháng tác dụng lợi tiểu.',
    'effect': 'Giảm hiệu quả lợi tiểu, có thể gây giữ nước', 'management':
    'Theo dõi cân nặng, dấu hiệu giữ nước. Có thể cần điều chỉnh liều lợi tiểu.'
    }]}, 'contraindications': {'tuyệt_đối': [
    'Nhiễm nấm hệ thống không điều trị (cryptococcosis, histoplasmosis, coccidioidomycosis) - corticosteroid làm nặng nhiễm nấm'
    , 'Dị ứng prednisolone hoặc các corticosteroid khác',
    'Nhiễm virus hoạt động (herpes simplex keratitis, varicella zoster lan tỏa) - trừ khi chỉ định đặc biệt'
    ], 'tương_đối': [
    'Nhiễm trùng đang hoạt động - có thể làm nặng, che dấu triệu chứng',
    'Đái tháo đường - tăng đường huyết, cần theo dõi và điều chỉnh',
    'Tăng huyết áp - có thể tăng huyết áp, giữ nước',
    'Suy tim - giữ nước, có thể làm nặng',
    'Loãng xương - tăng nguy cơ gãy xương',
    'Loét dạ dày tá tràng - tăng nguy cơ loét',
    'Rối loạn tâm thần - có thể làm nặng', 'Glaucoma - có thể tăng nhãn áp',
    'Có thai - có thể ảnh hưởng đến thai nhi',
    'Suy gan - prednisolone là dạng hoạt động, không cần chuyển hóa nhưng thận trọng'
    , 'Suy thận - không cần điều chỉnh liều nhưng thận trọng']},
    'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
    'Prednisolone là thuốc phân loại C. Corticosteroid có thể đi qua nhau thai và có thể ảnh hưởng đến thai nhi. Dùng lâu dài hoặc liều cao trong thai kỳ có thể gây ức chế thượng thận ở trẻ sơ sinh, chậm phát triển, tăng nguy cơ sứt môi/vòm miệng (khi dùng trong tam cá nguyệt đầu), và các tác dụng phụ khác. Tuy nhiên, prednisolone được sử dụng trong thai kỳ để điều trị một số bệnh tự miễn và hen phế quản. Nên dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Tránh dùng liều cao kéo dài trong thai kỳ nếu có thể.'
    , 'lactation': {'safety': 'Compatible (với dùng ngắn hạn)', 'details':
    'Prednisolone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ với liều thường dùng. Với liều cao hoặc kéo dài, có thể ảnh hưởng đến trẻ sơ sinh.'
    , 'recommendation':
    'Có thể dùng khi cho con bú với liều điều trị tiêu chuẩn. Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài.'
    }}, 'hepatic_adjustment': {'mild':
    'Không cần điều chỉnh liều. Prednisolone là dạng hoạt động, không cần chuyển hóa ở gan (khác với prednisone).'
    , 'moderate':
    'Không cần điều chỉnh liều. Prednisolone là dạng hoạt động, không phụ thuộc vào chức năng gan.'
    , 'severe':
    'Không cần điều chỉnh liều. Prednisolone là dạng hoạt động, không phụ thuộc vào chức năng gan. Tuy nhiên, thận trọng ở bệnh nhân suy gan nặng.'
    , 'notes':
    'Prednisolone là dạng hoạt động của prednisone, không cần chuyển hóa ở gan. Đây là ưu điểm so với prednisone ở bệnh nhân suy gan - có thể dùng prednisolone thay vì prednisone ở bệnh nhân suy gan.'
    }, 'overdose_management': {'symptoms': [
    'Triệu chứng Cushing: Tăng cân, mặt tròn, tích mỡ, bướu trâu, vết rạn da, tăng huyết áp'
    ,
    'Triệu chứng chuyển hóa: Tăng đường huyết nghiêm trọng, toan chuyển hóa, hạ kali máu'
    ,
    'Triệu chứng tiêu hóa: Loét dạ dày, xuất huyết tiêu hóa, thủng dạ dày',
    'Triệu chứng thần kinh: Kích động, loạn thần, trầm cảm, co giật, hôn mê',
    'Triệu chứng miễn dịch: Nhiễm trùng nghiêm trọng (do ức chế miễn dịch), che dấu triệu chứng nhiễm trùng'
    , 'Triệu chứng tim mạch: Suy tim, phù, giữ nước, tăng huyết áp nặng',
    'Triệu chứng nghiêm trọng: Suy thượng thận cấp (khi ngừng đột ngột sau dùng lâu dài), sốc, tử vong'
    ], 'antidote':
    'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
    'treatment': [
    'Ngừng ngay prednisolone nếu có thể (nhưng KHÔNG ngừng đột ngột nếu đã dùng >2 tuần - phải giảm dần)'
    , 'Nếu ngừng đột ngột sau dùng lâu dài:',
    '  - Bắt đầu lại corticosteroid ngay (hydrocortisone 100mg IV mỗi 6-8 giờ)'
    , '  - Giảm dần liều theo thời gian', 'Điều trị tăng đường huyết:',
    '  - Theo dõi đường huyết thường xuyên', '  - Insulin nếu cần',
    '  - Điều chỉnh liều đái tháo đường',
    'Điều trị loét dạ dày/xuất huyết tiêu hóa:',
    '  - PPI (omeprazole, pantoprazole)', '  - Truyền máu nếu cần',
    '  - Nội soi dạ dày nếu nghi ngờ thủng', 'Điều trị rối loạn tâm thần:',
    '  - An thần nếu kích động, loạn thần', '  - Antipsychotic nếu cần',
    '  - Theo dõi thần kinh chặt chẽ', 'Điều trị nhiễm trùng:',
    '  - Kháng sinh nếu có nhiễm trùng',
    '  - Theo dõi dấu hiệu nhiễm trùng (có thể che dấu)',
    'Điều chỉnh điện giải:', '  - Bổ sung kali nếu hạ kali máu',
    '  - Điều chỉnh natri nếu cần', 'Hỗ trợ huyết động:',
    '  - Truyền dịch nếu cần', '  - Thuốc vận mạch nếu sốc',
    'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, đường huyết'
    ], 'monitoring':
    'Theo dõi đường huyết, điện giải, dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu loét dạ dày, tâm thần trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng. Nếu ngừng đột ngột sau dùng lâu dài, theo dõi dấu hiệu suy thượng thận cấp trong ít nhất 1-2 tuần.'
    }, 'reversal_agents': None, 'administration_instructions': {'oral': {
    'with_food':
    'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.'
    , 'timing':
    'Uống 1-4 lần/ngày tùy chỉ định. Có thể uống buổi sáng (để giảm ảnh hưởng đến giấc ngủ) hoặc chia đều trong ngày. Với liều cao, chia nhiều lần. Với liều thấp, có thể uống 1 lần buổi sáng.'
    }, 'iv': {'reconstitution':
    'Prednisolone chủ yếu dùng đường uống. Nếu cần IV, có thể dùng methylprednisolone thay thế.'
    , 'infusion_rate': 'N/A - chủ yếu dùng đường uống', 'compatibility': [
    'N/A'], 'incompatibility': ['N/A'], 'notes':
    'Prednisolone chủ yếu dùng đường uống. Nếu cần dùng IV, cân nhắc dùng methylprednisolone hoặc hydrocortisone thay thế.'
    }}, 'references': {'primary_sources': ['FDA Drug Label - Prednisolone',
    'UpToDate - Prednisolone: Drug Information',
    'Medscape - Prednisolone Drug Reference',
    "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
    'Lexicomp Online - Prednisolone Monograph',
    'Micromedex - Prednisolone Drug Information',
    'Endocrine Society Guidelines - Corticosteroid Use'], 'last_updated':
    '2025-02-03', 'evidence_level':
    'A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
    }},
    "Methylprednisolone": {'group': 'Endocrinology - Corticosteroid', 'vietnamese_name':
    'Methylprednisolone, Medrol', 'administration': ['PO', 'IV', 'IM'],
    'indications': ['Viêm khớp dạng thấp', 'Hen phế quản', 'Bệnh tự miễn',
    'Sốc phản vệ (kết hợp)', 'Chấn thương tủy sống',
    'Đợt cấp bệnh đa xơ cứng'], 'contraindications': [
    'Nhiễm nấm hệ thống không điều trị', 'Dị ứng'], 'dosage': {'adult_po':
    '4-48mg/ngày chia 1-4 lần', 'adult_iv_pulse':
    '250-1000mg IV x 1 lần/ngày x 3-5 ngày', 'adult_iv_standard':
    '40-125mg IV mỗi 6-12 giờ', 'spinal_cord_injury':
    '30mg/kg IV x 1 lần, sau đó 5.4mg/kg/giờ x 23 giờ', 'notes':
    'IV pulse therapy cho bệnh nặng. Giảm dần liều khi ngừng'},
    'side_effects': ['Tăng đường huyết', 'Tăng huyết áp', 'Loãng xương',
    'Ức chế miễn dịch', 'Tăng cân', 'Loét dạ dày', 'Rối loạn tâm thần'],
    'interactions': ['Warfarin: thay đổi tác dụng chống đông',
    'NSAID: tăng nguy cơ loét dạ dày',
    'Ketoconazole: tăng nồng độ methylprednisolone'], 'pregnancy': 'C',
    'mechanism_of_action':
    'Methylprednisolone là một corticosteroid tổng hợp, tương tự cortisol tự nhiên nhưng có hoạt tính mạnh hơn. Tác dụng qua thụ thể glucocorticoid (GR) trong tế bào, điều hòa biểu hiện gen (gen activation và repression). Ức chế tổng hợp và giải phóng các chất trung gian gây viêm (prostaglandin, leukotriene, cytokine), ức chế di cư bạch cầu và hoạt động miễn dịch. Tác dụng chống viêm, chống dị ứng, ức chế miễn dịch mạnh. Có tác dụng mineralocorticoid nhẹ hơn hydrocortisone'
    , 'monitoring': ['Đường huyết (glucose) khi dùng liều cao hoặc kéo dài',
    'Huyết áp (corticosteroid có thể tăng huyết áp)',
    'Điện giải (natri, kali) khi dùng liều cao',
    'Dấu hiệu nhiễm trùng (ức chế miễn dịch, có thể che dấu triệu chứng)',
    'Dấu hiệu loét dạ dày (đau bụng, phân đen, nôn ra máu)',
    'Tâm thần (kích động, trầm cảm, loạn thần - đặc biệt liều cao)',
    'Dấu hiệu Cushing (tăng cân, mặt tròn, tích mỡ)',
    'Mật độ xương nếu dùng lâu dài'], 'precautions': [
    'GIẢM DẦN liều khi ngừng (tránh suy thượng thận cấp)',
    'Không ngừng đột ngột nếu dùng >2 tuần',
    'Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể',
    'Cân nhắc bổ sung canxi, vitamin D, bisphosphonate nếu dùng lâu dài',
    'Theo dõi sát dấu hiệu nhiễm trùng (có thể che dấu triệu chứng)',
    'Cân nhắc dùng PPI khi dùng liều cao hoặc kéo dài (giảm nguy cơ loét)',
    'Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)',
    'Thận trọng ở bệnh nhân tăng huyết áp, suy tim (giữ nước)',
    'IV pulse therapy (250-1000mg) chỉ dùng cho bệnh nặng, cần theo dõi sát'
    ], 'pharmacokinetics': {'half_life': '18-36 giờ (dài)', 'onset':
    'Vài giờ (PO), nhanh (IV)', 'duration': '24-36 giờ', 'protein_binding':
    '77% (gắn với transcortin và albumin)', 'clearance':
    'Gan (chuyển hóa qua CYP3A4), thận (thải trừ)'}, 'storage':
    'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản theo hướng dẫn nhà sản xuất'
    , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
    'Ketoconazole, Itraconazole (Azole antifungals)', 'mechanism':
    'Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa methylprednisolone, tăng nồng độ và tác dụng.'
    , 'effect':
    'Tăng nồng độ methylprednisolone, tăng tác dụng và tác dụng phụ (Cushing, tăng đường huyết, ức chế miễn dịch)'
    , 'management':
    'Giảm liều methylprednisolone 25-50% khi dùng với azole antifungals. Theo dõi đường huyết, dấu hiệu Cushing.'
    }, {'drug': 'Rifampin, Rifabutin', 'mechanism':
    'Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa methylprednisolone, giảm nồng độ và hiệu quả.'
    , 'effect': 'Giảm nồng độ methylprednisolone, giảm hiệu quả điều trị',
    'management':
    'Tăng liều methylprednisolone 25-50% khi dùng với rifampin. Theo dõi đáp ứng điều trị.'
    }, {'drug': 'Warfarin', 'mechanism':
    'Corticosteroid có thể thay đổi chuyển hóa warfarin và ảnh hưởng đến đông máu.'
    , 'effect':
    'Thay đổi INR (có thể tăng hoặc giảm), tăng nguy cơ chảy máu hoặc huyết khối'
    , 'management':
    'Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng methylprednisolone. Điều chỉnh liều warfarin nếu cần.'
    }], 'moderate': [{'drug': 'NSAID (Ibuprofen, Naproxen, Diclofenac)',
    'mechanism':
    'Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.', 'effect':
    'Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa nghiêm trọng',
    'management':
    'Cân nhắc dùng PPI hoặc misoprostol. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu chảy máu dạ dày.'
    }, {'drug': 'Phenytoin, Phenobarbital, Carbamazepine', 'mechanism':
    'Cảm ứng enzyme chuyển hóa, tăng chuyển hóa methylprednisolone.',
    'effect': 'Giảm nồng độ methylprednisolone, giảm hiệu quả',
    'management':
    'Tăng liều methylprednisolone. Theo dõi đáp ứng điều trị.'}, {'drug':
    'Cyclosporine, Tacrolimus', 'mechanism':
    'Cả hai đều ức chế miễn dịch, tác dụng cộng dồn. Có thể ảnh hưởng đến chuyển hóa.'
    , 'effect':
    'Tăng ức chế miễn dịch, tăng nguy cơ nhiễm trùng, tăng nguy cơ độc tính',
    'management':
    'Giảm liều cả hai thuốc. Theo dõi chức năng thận, dấu hiệu nhiễm trùng.'
    }], 'minor': [{'drug': 'Diuretics (Thiazide, Furosemide)', 'mechanism':
    'Corticosteroid gây giữ natri, có thể đối kháng tác dụng lợi tiểu.',
    'effect': 'Giảm hiệu quả lợi tiểu, có thể gây giữ nước', 'management':
    'Theo dõi cân nặng, dấu hiệu giữ nước. Có thể cần điều chỉnh liều lợi tiểu.'
    }]}, 'contraindications': {'tuyệt_đối': [
    'Nhiễm nấm hệ thống không điều trị (cryptococcosis, histoplasmosis, coccidioidomycosis) - corticosteroid làm nặng nhiễm nấm'
    , 'Dị ứng methylprednisolone hoặc các corticosteroid khác',
    'Nhiễm virus hoạt động (herpes simplex keratitis, varicella zoster lan tỏa) - trừ khi chỉ định đặc biệt'
    ], 'tương_đối': [
    'Nhiễm trùng đang hoạt động - có thể làm nặng, che dấu triệu chứng',
    'Đái tháo đường - tăng đường huyết, cần theo dõi và điều chỉnh',
    'Tăng huyết áp - có thể tăng huyết áp, giữ nước',
    'Suy tim - giữ nước, có thể làm nặng',
    'Loãng xương - tăng nguy cơ gãy xương',
    'Loét dạ dày tá tràng - tăng nguy cơ loét',
    'Rối loạn tâm thần - có thể làm nặng', 'Glaucoma - có thể tăng nhãn áp',
    'Có thai - có thể ảnh hưởng đến thai nhi',
    'Suy gan - có thể giảm chuyển hóa',
    'Suy thận - không cần điều chỉnh liều nhưng thận trọng']},
    'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
    'Methylprednisolone là thuốc phân loại C. Corticosteroid có thể đi qua nhau thai và có thể ảnh hưởng đến thai nhi. Dùng lâu dài hoặc liều cao trong thai kỳ có thể gây ức chế thượng thận ở trẻ sơ sinh, chậm phát triển, tăng nguy cơ sứt môi/vòm miệng (khi dùng trong tam cá nguyệt đầu), và các tác dụng phụ khác. Tuy nhiên, corticosteroid được sử dụng trong thai kỳ để điều trị một số bệnh tự miễn và hen phế quản. Nên dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Tránh dùng liều cao kéo dài trong thai kỳ nếu có thể.'
    , 'lactation': {'safety': 'Compatible (với dùng ngắn hạn)', 'details':
    'Methylprednisolone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ với liều thường dùng. Với liều cao hoặc kéo dài, có thể ảnh hưởng đến trẻ sơ sinh.'
    , 'recommendation':
    'Có thể dùng khi cho con bú với liều điều trị tiêu chuẩn. Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài.'
    }}, 'hepatic_adjustment': {'mild':
    'Không cần điều chỉnh liều. Methylprednisolone chuyển hóa qua gan nhưng không phụ thuộc nhiều vào chức năng gan.'
    , 'moderate':
    'Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình.'
    , 'severe':
    'Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng thời gian bán thải.'
    , 'notes':
    'Methylprednisolone chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng có thể làm giảm chuyển hóa, tăng thời gian bán thải, tăng nồng độ và tác dụng. Theo dõi tác dụng phụ chặt chẽ ở bệnh nhân suy gan.'
    }, 'overdose_management': {'symptoms': [
    'Triệu chứng Cushing: Tăng cân, mặt tròn, tích mỡ, bướu trâu, vết rạn da, tăng huyết áp'
    ,
    'Triệu chứng chuyển hóa: Tăng đường huyết nghiêm trọng, toan chuyển hóa, hạ kali máu'
    ,
    'Triệu chứng tiêu hóa: Loét dạ dày, xuất huyết tiêu hóa, thủng dạ dày',
    'Triệu chứng thần kinh: Kích động, loạn thần, trầm cảm, co giật, hôn mê',
    'Triệu chứng miễn dịch: Nhiễm trùng nghiêm trọng (do ức chế miễn dịch), che dấu triệu chứng nhiễm trùng'
    , 'Triệu chứng tim mạch: Suy tim, phù, giữ nước, tăng huyết áp nặng',
    'Triệu chứng nghiêm trọng: Suy thượng thận cấp (khi ngừng đột ngột sau dùng lâu dài), sốc, tử vong'
    ], 'antidote':
    'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
    'treatment': [
    'Ngừng ngay methylprednisolone nếu có thể (nhưng KHÔNG ngừng đột ngột nếu đã dùng >2 tuần - phải giảm dần)'
    , 'Nếu ngừng đột ngột sau dùng lâu dài:',
    '  - Bắt đầu lại corticosteroid ngay (hydrocortisone 100mg IV mỗi 6-8 giờ)'
    , '  - Giảm dần liều theo thời gian', 'Điều trị tăng đường huyết:',
    '  - Theo dõi đường huyết thường xuyên', '  - Insulin nếu cần',
    '  - Điều chỉnh liều đái tháo đường',
    'Điều trị loét dạ dày/xuất huyết tiêu hóa:',
    '  - PPI (omeprazole, pantoprazole)', '  - Truyền máu nếu cần',
    '  - Nội soi dạ dày nếu nghi ngờ thủng', 'Điều trị rối loạn tâm thần:',
    '  - An thần nếu kích động, loạn thần', '  - Antipsychotic nếu cần',
    '  - Theo dõi thần kinh chặt chẽ', 'Điều trị nhiễm trùng:',
    '  - Kháng sinh nếu có nhiễm trùng',
    '  - Theo dõi dấu hiệu nhiễm trùng (có thể che dấu)',
    'Điều chỉnh điện giải:', '  - Bổ sung kali nếu hạ kali máu',
    '  - Điều chỉnh natri nếu cần', 'Hỗ trợ huyết động:',
    '  - Truyền dịch nếu cần', '  - Thuốc vận mạch nếu sốc',
    'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, đường huyết'
    ], 'monitoring':
    'Theo dõi đường huyết, điện giải, dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu loét dạ dày, tâm thần trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng. Nếu ngừng đột ngột sau dùng lâu dài, theo dõi dấu hiệu suy thượng thận cấp trong ít nhất 1-2 tuần.'
    }, 'reversal_agents': None, 'administration_instructions': {'oral': {
    'with_food':
    'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.'
    , 'timing':
    'Uống 1-4 lần/ngày tùy chỉ định. Có thể uống buổi sáng (để giảm ảnh hưởng đến giấc ngủ) hoặc chia đều trong ngày. Với liều cao, chia nhiều lần. Với liều thấp, có thể uống 1 lần buổi sáng.'
    }, 'iv': {'reconstitution':
    'Pha với NS hoặc D5W. Nồng độ pha: 1-5mg/ml. Pha 125mg trong 50ml dịch = 2.5mg/ml. Pha 500mg trong 100ml dịch = 5mg/ml. Pha 1g trong 250ml dịch = 4mg/ml.'
    , 'infusion_rate':
    'Truyền trong 15-60 phút tùy liều. Liều thấp (40-125mg): truyền trong 15-30 phút. Liều cao (250-1000mg): truyền trong 30-60 phút. Không truyền quá nhanh. Tốc độ: 50ml/30 phút = ~1.7ml/phút. 100ml/60 phút = ~1.7ml/phút.'
    , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],
    'incompatibility': [
    'Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với thuốc có tính kiềm hoặc axit.'
    ], 'notes':
    'IV pulse therapy (250-1000mg) chỉ dùng cho bệnh nặng, cần theo dõi sát. Theo dõi đường huyết, huyết áp, điện giải trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần.'
    }}, 'references': {'primary_sources': [
    'FDA Drug Label - Methylprednisolone (Medrol)',
    'UpToDate - Methylprednisolone: Drug Information',
    'Medscape - Methylprednisolone Drug Reference',
    "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
    'Lexicomp Online - Methylprednisolone Monograph',
    'Micromedex - Methylprednisolone Drug Information',
    'Endocrine Society Guidelines - Corticosteroid Use'], 'last_updated':
    '2024-12-19', 'evidence_level':
    'A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
    }},
    "Hydrocortisone": {'group': 'Endocrinology - Corticosteroid', 'vietnamese_name':
    'Hydrocortisone, Cortef', 'administration': ['PO', 'IV', 'IM',
    'Topical'], 'indications': ['Suy thượng thận', 'Phản ứng dị ứng nặng',
    'Sốc phản vệ (kết hợp)', 'Viêm khớp', 'Bệnh Addison', 'Phù não'],
    'contraindications': ['Nhiễm nấm hệ thống không điều trị', 'Dị ứng'],
    'dosage': {'adult_replacement':
    '15-25mg/ngày (20mg buổi sáng, 10mg buổi tối)', 'adult_stress':
    '50-100mg IV mỗi 6-8 giờ', 'adult_shock':
    '100mg IV x 1 lần, sau đó 50-100mg mỗi 6 giờ', 'adult_antiinflammatory':
    '20-240mg/ngày', 'notes': 'Glucocorticoid tự nhiên, tác dụng ngắn'},
    'side_effects': ['Tăng đường huyết', 'Tăng huyết áp', 'Giữ natri, phù',
    'Loét dạ dày', 'Ức chế miễn dịch'], 'interactions': [
    'Warfarin: thay đổi tác dụng chống đông',
    'NSAID: tăng nguy cơ loét dạ dày'], 'pregnancy': 'C',
    'mechanism_of_action':
    'Glucocorticoid tự nhiên (cortisol), tác dụng ngắn. Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm, ức chế phospholipase A2. Có tác dụng mineralocorticoid (giữ natri, thải kali) - mạnh hơn dexamethasone. Được dùng trong suy thượng thận để thay thế cortisol thiếu hụt. Tác dụng chống viêm và ức chế miễn dịch yếu hơn dexamethasone nhưng có tác dụng mineralocorticoid.'
    , 'monitoring': ['Đường huyết (tăng đường huyết)',
    'Huyết áp (tăng huyết áp, đặc biệt do giữ natri)',
    'Điện giải (natri, kali - giữ natri, thải kali)',
    'Dấu hiệu nhiễm trùng (ức chế miễn dịch)',
    'Dạ dày (dấu hiệu loét, xuất huyết)',
    'Dấu hiệu suy thượng thận nếu ngừng đột ngột (mệt mỏi, hạ huyết áp, hạ natri máu)'
    , 'Dấu hiệu Cushing nếu dùng liều cao kéo dài',
    'Xương (loãng xương nếu dùng kéo dài)'], 'precautions': [
    'Trong suy thượng thận: KHÔNG được quên liều hoặc ngừng đột ngột (có thể gây suy thượng thận cấp - nguy hiểm tính mạng)'
    ,
    'Tăng liều trong stress (phẫu thuật, nhiễm trùng nặng) - cần tăng gấp 2-3 lần liều thay thế'
    , 'Giữ natri mạnh hơn dexamethasone → cần theo dõi natri, kali',
    'Không dùng trong nhiễm nấm hệ thống không điều trị',
    'Thận trọng ở bệnh nhân suy tim (giữ natri → phù)',
    'Thận trọng ở bệnh nhân tăng huyết áp (giữ natri → tăng huyết áp)',
    'Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)',
    'Dùng với thức ăn để giảm kích ứng dạ dày',
    'Thời gian bán thải ngắn → cần chia liều trong ngày (2-3 lần/ngày) cho thay thế'
    , 'Trong stress dosing: dùng liều cao IV mỗi 6-8 giờ'],
    'pharmacokinetics': {'half_life': '8-12 giờ', 'onset':
    'IV: 1 giờ; PO: 1-2 giờ', 'duration': '8-12 giờ', 'protein_binding':
    '90-95% (cao)', 'metabolism': 'Gan (CYP3A4)', 'clearance':
    'Gan, không cần điều chỉnh thận'}, 'storage':
    'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng bột pha tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.'
    , 'black_box_warnings':
    'Không có black box warning. Tuy nhiên, trong suy thượng thận, quên liều hoặc ngừng đột ngột có thể gây suy thượng thận cấp, có thể tử vong. Trong stress, không tăng liều có thể dẫn đến suy thượng thận cấp.'
    , 'drug_interactions': {'major': [{'drug':
    'Ketoconazole, Itraconazole (Azole antifungals)', 'mechanism':
    'Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa hydrocortisone, tăng nồng độ và tác dụng.'
    , 'effect':
    'Tăng nồng độ hydrocortisone, tăng tác dụng và tác dụng phụ (Cushing, tăng đường huyết, ức chế miễn dịch)'
    , 'management':
    'Giảm liều hydrocortisone 25-50% khi dùng với azole antifungals. Theo dõi đường huyết, dấu hiệu Cushing.'
    }, {'drug': 'Rifampin, Rifabutin', 'mechanism':
    'Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa hydrocortisone, giảm nồng độ và hiệu quả.'
    , 'effect':
    'Giảm nồng độ hydrocortisone, giảm hiệu quả điều trị - đặc biệt nguy hiểm trong suy thượng thận'
    , 'management':
    'Tăng liều hydrocortisone 25-50% khi dùng với rifampin. Trong suy thượng thận, cần tăng liều thay thế. Theo dõi dấu hiệu suy thượng thận.'
    }, {'drug': 'Warfarin', 'mechanism':
    'Corticosteroid có thể thay đổi chuyển hóa warfarin và ảnh hưởng đến đông máu.'
    , 'effect':
    'Thay đổi INR (có thể tăng hoặc giảm), tăng nguy cơ chảy máu hoặc huyết khối'
    , 'management':
    'Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng hydrocortisone. Điều chỉnh liều warfarin nếu cần.'
    }], 'moderate': [{'drug': 'NSAID (Ibuprofen, Naproxen, Diclofenac)',
    'mechanism':
    'Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.', 'effect':
    'Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa nghiêm trọng',
    'management':
    'Cân nhắc dùng PPI hoặc misoprostol. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu chảy máu dạ dày.'
    }, {'drug': 'Phenytoin, Phenobarbital, Carbamazepine', 'mechanism':
    'Cảm ứng enzyme chuyển hóa, tăng chuyển hóa hydrocortisone.', 'effect':
    'Giảm nồng độ hydrocortisone, giảm hiệu quả - đặc biệt nguy hiểm trong suy thượng thận'
    , 'management':
    'Tăng liều hydrocortisone. Trong suy thượng thận, cần tăng liều thay thế. Theo dõi dấu hiệu suy thượng thận.'
    }, {'drug': 'Cyclosporine, Tacrolimus', 'mechanism':
    'Cả hai đều ức chế miễn dịch, tác dụng cộng dồn. Có thể ảnh hưởng đến chuyển hóa.'
    , 'effect':
    'Tăng ức chế miễn dịch, tăng nguy cơ nhiễm trùng, tăng nguy cơ độc tính',
    'management':
    'Giảm liều cả hai thuốc. Theo dõi chức năng thận, dấu hiệu nhiễm trùng.'
    }], 'minor': [{'drug': 'Diuretics (Thiazide, Furosemide)', 'mechanism':
    'Hydrocortisone có tác dụng mineralocorticoid mạnh (giữ natri), có thể đối kháng tác dụng lợi tiểu.'
    , 'effect':
    'Giảm hiệu quả lợi tiểu, có thể gây giữ nước, tăng mất kali',
    'management':
    'Theo dõi cân nặng, dấu hiệu giữ nước, kali máu. Có thể cần điều chỉnh liều lợi tiểu, bổ sung kali.'
    }]}, 'contraindications': {'tuyệt_đối': [
    'Nhiễm nấm hệ thống không điều trị (cryptococcosis, histoplasmosis, coccidioidomycosis) - corticosteroid làm nặng nhiễm nấm'
    , 'Dị ứng hydrocortisone hoặc các corticosteroid khác',
    'Nhiễm virus hoạt động (herpes simplex keratitis, varicella zoster lan tỏa) - trừ khi chỉ định đặc biệt'
    ], 'tương_đối': [
    'Nhiễm trùng đang hoạt động - có thể làm nặng, che dấu triệu chứng',
    'Đái tháo đường - tăng đường huyết, cần theo dõi và điều chỉnh',
    'Tăng huyết áp - có thể tăng huyết áp, giữ nước (do tác dụng mineralocorticoid)'
    ,
    'Suy tim - giữ nước, có thể làm nặng (đặc biệt do tác dụng mineralocorticoid)'
    , 'Loãng xương - tăng nguy cơ gãy xương',
    'Loét dạ dày tá tràng - tăng nguy cơ loét',
    'Rối loạn tâm thần - có thể làm nặng', 'Glaucoma - có thể tăng nhãn áp',
    'Có thai - có thể ảnh hưởng đến thai nhi',
    'Suy gan - có thể giảm chuyển hóa',
    'Suy thận - không cần điều chỉnh liều nhưng thận trọng']},
    'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
    'Hydrocortisone là thuốc phân loại C. Corticosteroid có thể đi qua nhau thai và có thể ảnh hưởng đến thai nhi. Dùng lâu dài hoặc liều cao trong thai kỳ có thể gây ức chế thượng thận ở trẻ sơ sinh, chậm phát triển, tăng nguy cơ sứt môi/vòm miệng (khi dùng trong tam cá nguyệt đầu), và các tác dụng phụ khác. Tuy nhiên, hydrocortisone được sử dụng trong thai kỳ để điều trị suy thượng thận và một số bệnh tự miễn. Nên dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Trong suy thượng thận, cần tiếp tục điều trị nhưng với liều thấp nhất hiệu quả.'
    , 'lactation': {'safety': 'Compatible (với dùng ngắn hạn)', 'details':
    'Hydrocortisone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ với liều thay thế thông thường. Với liều cao hoặc kéo dài, có thể ảnh hưởng đến trẻ sơ sinh.'
    , 'recommendation':
    'Có thể dùng khi cho con bú với liều thay thế tiêu chuẩn (15-25mg/ngày). Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài.'
    }}, 'hepatic_adjustment': {'mild':
    'Không cần điều chỉnh liều. Hydrocortisone chuyển hóa qua gan nhưng không phụ thuộc nhiều vào chức năng gan.'
    , 'moderate':
    'Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình. Trong suy thượng thận, cần theo dõi dấu hiệu suy thượng thận.'
    , 'severe':
    'Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng thời gian bán thải. Trong suy thượng thận, cần theo dõi dấu hiệu suy thượng thận chặt chẽ.'
    , 'notes':
    'Hydrocortisone chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng có thể làm giảm chuyển hóa, tăng thời gian bán thải, tăng nồng độ và tác dụng. Theo dõi tác dụng phụ chặt chẽ ở bệnh nhân suy gan. Trong suy thượng thận, không được giảm liều quá mức - cần cân bằng giữa điều chỉnh liều và đảm bảo đủ liều thay thế.'
    }, 'overdose_management': {'symptoms': [
    'Triệu chứng Cushing: Tăng cân, mặt tròn, tích mỡ, bướu trâu, vết rạn da, tăng huyết áp'
    ,
    'Triệu chứng chuyển hóa: Tăng đường huyết nghiêm trọng, toan chuyển hóa, hạ kali máu (do tác dụng mineralocorticoid)'
    ,
    'Triệu chứng tiêu hóa: Loét dạ dày, xuất huyết tiêu hóa, thủng dạ dày',
    'Triệu chứng thần kinh: Kích động, loạn thần, trầm cảm, co giật, hôn mê',
    'Triệu chứng miễn dịch: Nhiễm trùng nghiêm trọng (do ức chế miễn dịch), che dấu triệu chứng nhiễm trùng'
    ,
    'Triệu chứng tim mạch: Suy tim, phù, giữ nước, tăng huyết áp nặng (đặc biệt do tác dụng mineralocorticoid)'
    ,
    'Triệu chứng nghiêm trọng: Suy thượng thận cấp (khi ngừng đột ngột sau dùng lâu dài hoặc quên liều trong suy thượng thận), sốc, tử vong'
    ], 'antidote':
    'Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.',
    'treatment': [
    'Ngừng ngay hydrocortisone nếu có thể (nhưng KHÔNG ngừng đột ngột nếu đã dùng >2 tuần hoặc trong suy thượng thận - phải giảm dần)'
    ,
    'Nếu ngừng đột ngột sau dùng lâu dài hoặc quên liều trong suy thượng thận:'
    ,
    '  - Bắt đầu lại corticosteroid ngay (hydrocortisone 100mg IV mỗi 6-8 giờ)'
    , '  - Giảm dần liều theo thời gian', 'Điều trị tăng đường huyết:',
    '  - Theo dõi đường huyết thường xuyên', '  - Insulin nếu cần',
    '  - Điều chỉnh liều đái tháo đường',
    'Điều trị loét dạ dày/xuất huyết tiêu hóa:',
    '  - PPI (omeprazole, pantoprazole)', '  - Truyền máu nếu cần',
    '  - Nội soi dạ dày nếu nghi ngờ thủng', 'Điều trị rối loạn tâm thần:',
    '  - An thần nếu kích động, loạn thần', '  - Antipsychotic nếu cần',
    '  - Theo dõi thần kinh chặt chẽ', 'Điều trị nhiễm trùng:',
    '  - Kháng sinh nếu có nhiễm trùng',
    '  - Theo dõi dấu hiệu nhiễm trùng (có thể che dấu)',
    'Điều chỉnh điện giải (đặc biệt quan trọng với hydrocortisone do tác dụng mineralocorticoid):'
    , '  - Bổ sung kali nếu hạ kali máu',
    '  - Điều chỉnh natri nếu cần (có thể giữ natri)',
    '  - Theo dõi cân nặng, dấu hiệu giữ nước', 'Hỗ trợ huyết động:',
    '  - Truyền dịch nếu cần', '  - Thuốc vận mạch nếu sốc',
    'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, đường huyết'
    ], 'monitoring':
    'Theo dõi đường huyết, điện giải (đặc biệt natri, kali), dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu loét dạ dày, tâm thần trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng. Nếu ngừng đột ngột sau dùng lâu dài hoặc quên liều trong suy thượng thận, theo dõi dấu hiệu suy thượng thận cấp trong ít nhất 1-2 tuần.'
    }, 'reversal_agents': None, 'administration_instructions': {'oral': {
    'with_food':
    'Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.'
    , 'timing':
    'Với liều thay thế: uống 2-3 lần/ngày (ví dụ: 20mg buổi sáng, 10mg buổi tối). Với liều chống viêm: uống 1-4 lần/ngày tùy chỉ định. Có thể uống buổi sáng (để giảm ảnh hưởng đến giấc ngủ) hoặc chia đều trong ngày.'
    }, 'iv': {'reconstitution':
    'Pha với NS hoặc D5W. Nồng độ pha: 1-5mg/ml. Pha 100mg trong 50ml dịch = 2mg/ml. Pha 250mg trong 100ml dịch = 2.5mg/ml.'
    , 'infusion_rate':
    'Truyền trong 15-30 phút. Không truyền quá nhanh. Tốc độ: 50ml/30 phút = ~1.7ml/phút. 100ml/30 phút = ~3.3ml/phút.'
    , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],
    'incompatibility': [
    'Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với thuốc có tính kiềm hoặc axit.'
    ], 'notes':
    'Trong stress dosing (phẫu thuật, nhiễm trùng nặng): dùng 50-100mg IV mỗi 6-8 giờ. Trong sốc: 100mg IV x 1 lần, sau đó 50-100mg mỗi 6 giờ. Theo dõi đường huyết, huyết áp, điện giải trong quá trình truyền.'
    }}, 'references': {'primary_sources': [
    'FDA Drug Label - Hydrocortisone (Cortef)',
    'UpToDate - Hydrocortisone: Drug Information',
    'Medscape - Hydrocortisone Drug Reference',
    "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
    'Lexicomp Online - Hydrocortisone Monograph',
    'Micromedex - Hydrocortisone Drug Information',
    'Endocrine Society Guidelines - Adrenal Insufficiency Management'],
    'last_updated': '2025-02-03', 'evidence_level':
    'A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
    }},
}
