"""Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data"""

# Antihistamine (H1 Antagonist, 2nd generation)s

ANTIHISTAMINE_H1_ANTAGONIST_2ND_GENERATIONS_DRUGS = {
    "Cetirizine": {'group': 'Allergy - Antihistamine (H1 Antagonist, 2nd generation)',vietnamese_name': 'Cetirizine, Zyrtec', 'administration': ['PO'],
        'indications': ['Dị ứng (allergic rhinitis)', 'Mề đay (urticaria)',
        'Dị ứng mắt', 'Dị ứng da'],
        'contraindications': [
        'Suy thận nặng'],
        'dosage': {'adult': '10mg x 1 lần/ngày',
        'adult_max': '10mg x 2 lần/ngày', 'pediatric':
        '5mg x 1 lần/ngày (2-6 tuổi), 10mg/ngày (6-12 tuổi)', 'notes':
        'Non-sedating, an toàn cho trẻ em'},
        'renal_adjustment': {'normal':
        'Không đổi', '30_60': '5mg x 1 lần/ngày', 'under_30': '5mg cách ngày'},
        'side_effects': ['Buồn ngủ (ít, 10-15% người)', 'Khô miệng', 'Nhức đầu',
        'Mệt mỏi'],
        'interactions': [
        'Alcohol: có thể tăng buồn ngủ'],mechanism_of_action':
        'Cetirizine là metabolite của hydroxyzine, là antihistamine thế hệ thứ hai, đối kháng chọn lọc và có ái lực cao với thụ thể H1 ở ngoại biên. Cetirizine ít qua hàng rào máu-não (do là zwitterion ở pH sinh lý) nên ít gây buồn ngủ hơn so với antihistamine thế hệ thứ nhất, nhưng vẫn có thể gây buồn ngủ ở một số người (10-15%). Cetirizine ức chế phóng thích histamine từ mast cells và basophils, ngăn chặn tác dụng của histamine trên các thụ thể H1. Ngoài ra, cetirizine có tác dụng kháng viêm nhẹ do ức chế phóng thích các chất trung gian gây viêm và ức chế chemotaxis của eosinophils. Tác dụng tốt cho cả allergic rhinitis và urticaria.'
        ,         'monitoring': ['Đáp ứng điều trị (giảm triệu chứng dị ứng)',
        'Buồn ngủ (10-15% người dùng, mặc dù là thế hệ thứ hai)',
        'Chức năng thận (creatinine) - cần điều chỉnh liều ở suy thận',
        'Tác dụng phụ (khô miệng, nhức đầu, mệt mỏi)',
        'Tương tác với alcohol (có thể tăng buồn ngủ)'],contraindications_detail': {
        'tuyệt_đối': [
        'Dị ứng cetirizine hoặc hydroxyzine',
        'Suy thận nặng (CrCl <30) - chống chỉ định hoặc dùng liều rất thấp'],tương_đối': [
        'Suy thận nhẹ đến trung bình (CrCl 30-60) - giảm liều 50%',
        'Người cao tuổi - có thể tăng nguy cơ buồn ngủ',
        'Bệnh nhân có nguy cơ bí tiểu - tăng nguy cơ']},precautions': [
        'Có thể gây buồn ngủ ở một số người (10-15%) - thận trọng khi lái xe hoặc vận hành máy móc'
        'Cần điều chỉnh liều ở suy thận: CrCl 30-60 → 5mg/ngày, CrCl <30 → 5mg cách ngày'
        , 'Có thể dùng với thức ăn hoặc không',
        'An toàn cho trẻ em từ 2 tuổi trở lên',
        'An toàn trong thai kỳ (category B)',
        'Tránh dùng với alcohol (tăng buồn ngủ)',
        'Ít tương tác thuốc, an toàn cho hầu hết bệnh nhân',
        'Tác dụng kéo dài 24 giờ nên chỉ cần dùng 1 lần/ngày'],pharmacokinetics': {'half_life': '8-10 giờ', 'onset': '1 giờ',
        'duration': '24 giờ', 'protein_binding': '93%', 'clearance':
        'Thận: bài tiết chủ yếu qua thận (60-70% nguyên dạng, không chuyển hóa). Gan: ít chuyển hóa. Cần điều chỉnh liều ở suy thận.'
        },storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng syrup: bảo quản ở nhiệt độ phòng, đậy kín sau khi dùng.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [],moderate': [{'drug': 'Alcohol', 'mechanism':
        'Tăng tác dụng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng buồn ngủ, suy hô hấp', 'management':
        'Tránh dùng với rượu. Cảnh báo bệnh nhân về nguy cơ.'}],minor': [{
        'drug': 'Theophylline', 'mechanism':
        'Có thể tăng nhẹ nồng độ theophylline', 'effect':
        'Tăng nhẹ tác dụng theophylline', 'management':
        'Thận trọng. Theo dõi nồng độ theophylline nếu cần.'}]},contraindications': {'tuyệt_đối': [
        'Dị ứng cetirizine hoặc hydroxyzine',
        'Suy thận nặng (CrCl <30) - chống chỉ định hoặc dùng liều rất thấp'],tương_đối': [
        'Suy thận nhẹ đến trung bình (CrCl 30-60) - giảm liều 50%',
        'Người cao tuổi - có thể tăng nguy cơ buồn ngủ',
        'Bệnh nhân có nguy cơ bí tiểu - tăng nguy cơ']},pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'An toàn trong thai kỳ. Không có bằng chứng về dị tật bẩm sinh. Có thể dùng ở tất cả các tam cá nguyệt. Cetirizine là một trong những antihistamine được lựa chọn trong thai kỳ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Cetirizine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường <1% nồng độ mẹ. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Theo dõi dấu hiệu buồn ngủ ở trẻ (hiếm).'}
        },hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi', 'notes':
        'Cetirizine chủ yếu thải trừ qua thận (không chuyển hóa ở gan), không cần điều chỉnh liều ở suy gan. Tuy nhiên, suy gan nặng có thể ảnh hưởng đến protein binding.'
        },overdose_management': {'symptoms': [
        'Buồn ngủ (tăng so với liều điều trị)', 'Nhức đầu', 'Khô miệng',
        'Lú lẫn (hiếm)', 'Tim đập nhanh (hiếm)'],antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi ý thức, huyết áp, nhịp tim',
        'Điều trị hỗ trợ: truyền dịch nếu cần', 'Theo dõi ít nhất 4-6 giờ'],monitoring': 'Ý thức, huyết áp, nhịp tim'},reversal_agents': {
        'available': False, 'agents': []},administration_instructions': {
        'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn'
        , 'timing':
        'Dùng 1 lần/ngày (tác dụng kéo dài 24 giờ). Có thể dùng buổi sáng hoặc tối. CẦN ĐIỀU CHỈNH LIỀU Ở SUY THẬN: CrCl 30-60 → 5mg/ngày, CrCl <30 → 5mg cách ngày.'
        },iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],incompatibility': [],
        }},references': {'primary_sources': [
        'FDA Drug Label - Zyrtec (cetirizine)',
        'UpToDate - Cetirizine: Drug information',
        'Allergy & Clinical Immunology guidelines'],last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews'},risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': [],qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Renal function (CrCl) - dose adjustment needed', 'Sedation (10-15% of users)']
        },guideline_tags': [
            'EAACI Guidelines - Allergic Rhinitis',
            'AAAAI Guidelines - Urticaria',
            'FDA Drug Information - Cetirizine'
        ],
        "black_box_warnings": None,
},
    "Desloratadine": {'group': 'Allergy - Antihistamine (H1 Antagonist, 2nd generation)',vietnamese_name': 'Desloratadine, Aerius', 'administration': ['PO'],
        'indications': ['Dị ứng (allergic rhinitis)', 'Mề đay (urticaria)',
        'Dị ứng da'],
        'contraindications': ['Dị ứng'],
        'dosage': {
        'adult_standard': '5mg x 1 lần/ngày', 'adult_max': '5mg x 2 lần/ngày',
        'pediatric': '2.5mg x 1 lần/ngày (6-11 tuổi)', 'notes':
        'Là metabolite của loratadine, mạnh hơn và tác dụng dài hơn'},
        'side_effects': ['Buồn ngủ (rất hiếm)', 'Khô miệng', 'Nhức đầu',
        'Ít tác dụng phụ'],
        'interactions': ['Ít tương tác'],mechanism_of_action':
        'Desloratadine là antihistamine thế hệ 2, là metabolite hoạt động của loratadine. Thuốc ức chế chọn lọc receptor H1 ngoại vi, ngăn cản histamine gắn vào receptor và gây các phản ứng dị ứng (ngứa, hắt hơi, chảy nước mũi, nổi mề đay). Desloratadine không qua hàng rào máu-não (BBB) nên ít gây buồn ngủ hơn so với antihistamine thế hệ 1. Thuốc cũng có tác dụng ức chế giải phóng các chất trung gian gây viêm từ tế bào mast và basophil'
        , 'monitoring': ['Dấu hiệu phản ứng dị ứng (nếu có)',
        'Dấu hiệu buồn ngủ (rất hiếm nhưng cần theo dõi khi lái xe)',
        'Chức năng gan nếu dùng lâu dài'],precautions': [
        'Ít tác dụng phụ, ít gây buồn ngủ hơn antihistamine thế hệ 1',
        'Có thể dùng trong thai kỳ (category C)',
        'Dùng được ở trẻ em từ 6 tháng tuổi', 'Ít tương tác với các thuốc khác',
        'Có thể dùng với thức ăn hoặc không'],pharmacokinetics': {'half_life':
        '27 giờ (dài)', 'onset': '1-2 giờ', 'duration': '24 giờ',
        'protein_binding': '82-87%', 'clearance':
        'Gan (chuyển hóa), thận (thải trừ)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        None, 'drug_interactions': {'major': [],moderate': [],minor': [{
        'drug': 'CYP3A4 inhibitors (ketoconazole, itraconazole, erythromycin)',
        'mechanism': 'Có thể ức chế chuyển hóa desloratadine nhẹ.', 'effect':
        'Tăng nhẹ nồng độ desloratadine', 'management':
        'Thận trọng. Thường không cần điều chỉnh liều.'}]},contraindications':
        {'tuyệt_đối': ['Dị ứng desloratadine hoặc loratadine'],tương_đối': [
        'Suy gan nặng - thận trọng, có thể cần giảm liều',
        'Có thai - category C, thận trọng',
        'Trẻ em <6 tháng tuổi - không khuyến cáo']},pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Desloratadine là category C. Không có nghiên cứu đầy đủ ở phụ nữ có thai. Dùng được nếu lợi ích > nguy cơ. Thận trọng, đặc biệt trong tam cá nguyệt đầu.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Desloratadine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.',
        'recommendation': 'Có thể dùng khi cho con bú. An toàn cho trẻ bú mẹ.'}
        },hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Theo dõi chức năng gan.', 'moderate':
        'Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan.', 'severe':
        'Thận trọng, giảm liều. Suy gan nặng làm giảm chuyển hóa, có thể tăng nồng độ.'
        , 'notes':
        'Desloratadine chuyển hóa ở gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ.'
        },overdose_management': {'symptoms': ['Buồn ngủ nặng', 'Nhức đầu',
        'Khô miệng', 'Chóng mặt'],antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng desloratadine ngay lập tức', 'Theo dõi dấu hiệu sinh tồn',
        'Hỗ trợ hô hấp nếu cần', 'Theo dõi trong 24-48 giờ (half-life dài)'],monitoring': 'Dấu hiệu sinh tồn, mức độ ý thức, dấu hiệu buồn ngủ'},reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Theo dõi trong 24-48 giờ do half-life dài.'},administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Không ảnh hưởng hấp thu.',
        'timing': 'Uống 1 lần/ngày, bất kỳ lúc nào, cùng thời điểm mỗi ngày.'},iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],incompatibility': [],
        }},references': {'primary_sources': [
        'FDA Drug Label - Desloratadine (Clarinex)',
        'UpToDate - Desloratadine: Drug Information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ],evidence_level':
        'A - Dựa trên FDA drug labels và dữ liệu lâm sàng'}},
    "Fexofenadine": {'group': 'Allergy - Antihistamine (H1 Antagonist, 2nd generation)',vietnamese_name': 'Fexofenadine, Allegra', 'administration': ['PO'],
        'indications': ['Dị ứng (allergic rhinitis)', 'Mề đay (urticaria)',
        'Dị ứng da'],
        'contraindications': ['Dị ứng'],
        'dosage': {
        'adult_standard': '180mg x 1 lần/ngày hoặc 60mg x 2 lần/ngày',
        'adult_max': '180mg x 2 lần/ngày', 'pediatric':
        '30mg x 2 lần/ngày (6-11 tuổi)', 'notes':
        'Non-sedating, ít buồn ngủ nhất'},
        'side_effects': [
        'Rất ít tác dụng phụ', 'Buồn ngủ rất hiếm', 'Nhức đầu (hiếm)',
        'Mệt mỏi (hiếm)'],
        'interactions': [
        'Fruit juices (apple, orange, grapefruit): giảm hấp thu (cách xa 1-2 giờ)',
        'Antacids: giảm hấp thu (cách xa 2 giờ)'],mechanism_of_action':
        'Fexofenadine là metabolite hoạt động của terfenadine, là antihistamine thế hệ thứ hai, đối kháng chọn lọc và có ái lực cao với thụ thể H1 ở ngoại biên. Fexofenadine gần như không qua hàng rào máu-não (do là carboxylate anion ở pH sinh lý) nên không gây buồn ngủ và không có tác dụng anticholinergic. Fexofenadine ức chế phóng thích histamine từ mast cells và basophils, ngăn chặn tác dụng của histamine trên các thụ thể H1. Fexofenadine được coi là non-sedating nhất trong các antihistamine thế hệ thứ hai, phù hợp cho bệnh nhân cần tỉnh táo hoàn toàn. Tác dụng tốt cho cả allergic rhinitis và urticaria.'
        , 'monitoring': ['Đáp ứng điều trị (giảm triệu chứng dị ứng)',
        'Tác dụng phụ (rất hiếm: nhức đầu, mệt mỏi)',
        'Tương tác với fruit juices và antacids (giảm hấp thu)',
        'Chức năng thận nếu dùng lâu dài (mặc dù không cần điều chỉnh liều)'],precautions': [
        'Non-sedating nhất - không gây buồn ngủ, an toàn khi lái xe',
        'Không dùng với fruit juices (táo, cam, bưởi) - giảm hấp thu đáng kể, cách xa 1-2 giờ'
        , 'Không dùng với antacids - giảm hấp thu, cách xa 2 giờ',
        'Uống với nước lọc, không dùng với thức ăn có acid (có thể giảm hấp thu)',
        'Có thể dùng cho trẻ em từ 6 tuổi trở lên',
        'Thận trọng trong thai kỳ (category C) - cân nhắc lợi ích/nguy cơ',
        'Ít tương tác thuốc, an toàn cho hầu hết bệnh nhân',
        'Không cần điều chỉnh liều ở suy thận hoặc suy gan',
        'Tác dụng kéo dài 24 giờ nên chỉ cần dùng 1-2 lần/ngày tùy liều'],pharmacokinetics': {'half_life': '14.4 giờ', 'onset': '1-2 giờ',
        'duration': '24 giờ', 'protein_binding': '60-70%', 'clearance':
        'Thận: bài tiết chủ yếu qua thận (80% nguyên dạng, 11% metabolites). Gan: ít chuyển hóa. Không cần điều chỉnh liều ở suy thận hoặc suy gan (mặc dù có thể tích lũy nhẹ ở suy thận nặng).'
        },storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng viên nén tan nhanh: bảo quản trong bao bì kín, tránh ẩm.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [],moderate': [{'drug': 'Fruit juices (apple, orange, grapefruit)',
        'mechanism': 'Giảm hấp thu fexofenadine qua transporter', 'effect':
        'Giảm nồng độ fexofenadine, giảm hiệu quả', 'management':
        'KHÔNG dùng với fruit juices. Cách xa ít nhất 1-2 giờ. Uống với nước lọc.'
        }, {'drug': 'Antacids (aluminum, magnesium)', 'mechanism':
        'Giảm hấp thu fexofenadine', 'effect':
        'Giảm nồng độ fexofenadine, giảm hiệu quả', 'management':
        'Cách xa ít nhất 2 giờ. Uống với nước lọc.'}],minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng fexofenadine hoặc terfenadine'],tương_đối': [
        'Trẻ em <6 tuổi - an toàn từ 6 tuổi trở lên',
        'Suy thận nặng - có thể tích lũy nhẹ nhưng không cần điều chỉnh liều']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Không có bằng chứng rõ ràng về dị tật bẩm sinh, nhưng ít dữ liệu hơn so với loratadine và cetirizine. Cân nhắc dùng loratadine hoặc cetirizine (category B) nếu có thể.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Fexofenadine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Theo dõi dấu hiệu bất thường ở trẻ (hiếm).'
        }},hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe': 'Không đổi', 'notes':
        'Fexofenadine chủ yếu thải trừ qua thận (ít chuyển hóa ở gan), không cần điều chỉnh liều ở suy gan.'
        },overdose_management': {'symptoms': [
        'Nhức đầu (tăng so với liều điều trị)', 'Mệt mỏi', 'Buồn ngủ (hiếm)',
        'Lú lẫn (rất hiếm)'],antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi ý thức, huyết áp, nhịp tim',
        'Điều trị hỗ trợ: truyền dịch nếu cần', 'Theo dõi ít nhất 4-6 giờ'],monitoring': 'Ý thức, huyết áp, nhịp tim'},reversal_agents': {
        'available': False, 'agents': []},administration_instructions': {
        'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Uống với nước lọc. KHÔNG dùng với fruit juices (táo, cam, bưởi) - giảm hấp thu đáng kể'
        , 'timing':
        'Dùng 1-2 lần/ngày tùy liều (180mg x 1 lần/ngày hoặc 60mg x 2 lần/ngày). Cách xa fruit juices 1-2 giờ. Cách xa antacids 2 giờ.'
        },iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],incompatibility': [],
        }},references': {'primary_sources': [
        'FDA Drug Label - Allegra (fexofenadine)',
        'UpToDate - Fexofenadine: Drug information',
        'Allergy & Clinical Immunology guidelines'],last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews'},risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': [],qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Clinical response (reduction in allergy symptoms)', 'Interaction with fruit juices and antacids (decreased absorption)']
        },guideline_tags': [
            'EAACI Guidelines - Allergic Rhinitis',
            'AAAAI Guidelines - Urticaria',
            'FDA Drug Information - Fexofenadine'
        ],
        "black_box_warnings": None,
},
    "Levocetirizine": {'group': 'Allergy - Antihistamine (H1 Antagonist, 2nd generation)',vietnamese_name': 'Levocetirizine, Xyzal', 'administration': ['PO'],
        'indications': ['Dị ứng (allergic rhinitis)', 'Mề đay (urticaria)',
        'Dị ứng da'],
        'contraindications': [
        'Suy thận nặng'],
        'dosage': {'adult_standard': '5mg x 1 lần/ngày buổi tối', 'adult_max':
        '5mg x 2 lần/ngày', 'pediatric': '2.5mg x 1 lần/ngày (6-12 tuổi)',
        'notes': 'Là R-enantiomer của cetirizine, mạnh hơn cetirizine'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': '5mg cách ngày',
        'under_30': '5mg mỗi 3 ngày'},
        'side_effects': [
        'Buồn ngủ (ít hơn cetirizine)', 'Nhức đầu', 'Mệt mỏi', 'Khô miệng'],
        'interactions': ['Ít tương tác', 'Alcohol: có thể tăng buồn ngủ'],pregnancy': 'B', 'mechanism_of_action':
        'Levocetirizine là R-enantiomer của cetirizine, là antihistamine thế hệ 2. Thuốc ức chế chọn lọc receptor H1 ngoại vi, ngăn cản histamine gắn vào receptor và gây các phản ứng dị ứng. Levocetirizine mạnh hơn và tác dụng dài hơn so với cetirizine (racemic mixture). Thuốc không qua hàng rào máu-não (BBB) nên ít gây buồn ngủ hơn so với antihistamine thế hệ 1. Thuốc cũng có tác dụng ức chế giải phóng các chất trung gian gây viêm từ tế bào mast'
        , 'monitoring': ['Dấu hiệu phản ứng dị ứng (nếu có)',
        'Dấu hiệu buồn ngủ (ít hơn cetirizine nhưng cần theo dõi khi lái xe)',
        'Chức năng thận nếu suy thận (cần điều chỉnh liều)',
        'Chức năng gan nếu dùng lâu dài'],precautions': [
        'Giảm liều nếu suy thận (CrCl 30-60: 5mg cách ngày, <30: 5mg mỗi 3 ngày)',
        'Ít gây buồn ngủ hơn cetirizine',
        'Có thể dùng trong thai kỳ (category B)',
        'Dùng được ở trẻ em từ 6 tuổi', 'Tránh rượu (có thể tăng buồn ngủ)',
        'Có thể dùng với thức ăn hoặc không'],pharmacokinetics': {'half_life':
        '8 giờ', 'onset': '1 giờ', 'duration': '24 giờ', 'protein_binding':
        '91%', 'clearance':
        'Thận (thải trừ chủ yếu - 85%), gan (chuyển hóa - 15%)'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm', 'black_box_warnings':
        None, 'contraindications_detail': {
        'tuyệt_đối': [
        'Dị ứng levocetirizine hoặc cetirizine',
        'Suy thận nặng (CrCl <10) - chống chỉ định'],tương_đối': [
        'Suy thận (CrCl 30-60) - giảm liều (5mg cách ngày)',
        'Suy thận (CrCl 10-30) - giảm liều (5mg mỗi 3 ngày)',
        'Có thai - category B, thận trọng', 'Trẻ em <6 tuổi - không khuyến cáo'
        ]},drug_interactions': {'major': [],moderate': [{'drug':
        'Alcohol', 'mechanism':
        'Cả hai đều ức chế hệ thần kinh trung ương, tác dụng cộng dồn.',
        'effect': 'Tăng buồn ngủ, giảm khả năng lái xe', 'management':
        'Tránh rượu khi dùng levocetirizine.'}],minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng levocetirizine hoặc cetirizine',
        'Suy thận nặng (CrCl <10) - chống chỉ định'],tương_đối': [
        'Suy thận (CrCl 30-60) - giảm liều (5mg cách ngày)',
        'Suy thận (CrCl 10-30) - giảm liều (5mg mỗi 3 ngày)',
        'Có thai - category B, thận trọng', 'Trẻ em <6 tuổi - không khuyến cáo'
        ],pregnancy_details':
        'Levocetirizine là category B - an toàn hơn category C. Không có bằng chứng về dị tật thai nhi. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Levocetirizine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. An toàn cho trẻ bú mẹ.'}},hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Levocetirizine chủ yếu thải qua thận.',
        'moderate':
        'Không cần điều chỉnh liều. Levocetirizine chủ yếu thải qua thận.',
        'severe':
        'Không cần điều chỉnh liều. Levocetirizine chủ yếu thải qua thận.',
        'notes':
        'Levocetirizine chủ yếu thải qua thận (85%), chỉ 15% chuyển hóa ở gan. Suy gan không ảnh hưởng đáng kể đến nồng độ.'
        },overdose_management': {'symptoms': ['Buồn ngủ nặng', 'Nhức đầu',
        'Mệt mỏi', 'Khô miệng', 'Chóng mặt'],antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng levocetirizine ngay lập tức', 'Theo dõi dấu hiệu sinh tồn',
        'Hỗ trợ hô hấp nếu cần', 'Theo dõi trong 24-48 giờ'],monitoring':
        'Dấu hiệu sinh tồn, mức độ ý thức, dấu hiệu buồn ngủ'},reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay. Theo dõi trong 24-48 giờ do half-life dài.'},administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Không ảnh hưởng hấp thu.',
        'timing':
        'Uống 1 lần/ngày buổi tối (để giảm buồn ngủ ban ngày) hoặc bất kỳ lúc nào, cùng thời điểm mỗi ngày. Giảm liều nếu suy thận (CrCl 30-60: 5mg cách ngày, CrCl 10-30: 5mg mỗi 3 ngày).'
        },iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],incompatibility': [],
        }},references': {'primary_sources': [
        'FDA Drug Label - Levocetirizine (Xyzal)',
        'UpToDate - Levocetirizine: Drug Information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ]},
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Renal function"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "ARIA Guidelines - Allergic Rhinitis"
        ]
    },
    "Loratadine": {'group': 'Allergy - Antihistamine (H1 Antagonist, 2nd generation)',vietnamese_name': 'Loratadine, Clarityne', 'administration': ['PO'],
        'indications': ['Dị ứng (allergic rhinitis)', 'Mề đay (urticaria)',
        'Dị ứng thức ăn', 'Dị ứng da'],
        'contraindications': ['Dị ứng'],
        'dosage': {'adult_standard': '10mg x 1 lần/ngày', 'adult_max':
        '10mg x 2 lần/ngày', 'pediatric': '5mg x 1 lần/ngày (2-12 tuổi)',
        'notes': 'Non-sedating, ít tác dụng phụ'},
        'side_effects': [
        'Buồn ngủ (ít hơn 1st generation)', 'Khô miệng (hiếm)',
        'Nhức đầu (hiếm)', 'Ít tác dụng phụ hơn antihistamine 1st generation'],
        'interactions': ['Ít tương tác',
        'Erythromycin/Ketoconazole: tăng nồng độ (nhưng thường không cần điều chỉnh)'
        ],mechanism_of_action':
        'Loratadine là antihistamine thế hệ thứ hai, đối kháng chọn lọc và có ái lực cao với thụ thể H1 ở ngoại biên. Khác với antihistamine thế hệ thứ nhất (diphenhydramine, chlorpheniramine), loratadine ít qua hàng rào máu-não nên ít gây buồn ngủ và tác dụng phụ anticholinergic. Loratadine ức chế phóng thích histamine từ mast cells và basophils, ngăn chặn tác dụng của histamine trên các thụ thể H1 ở mạch máu, cơ trơn phế quản, và các mô khác. Điều này làm giảm các triệu chứng dị ứng như ngứa, chảy nước mũi, hắt hơi, và mề đay. Loratadine cũng có tác dụng kháng viêm nhẹ do ức chế phóng thích các chất trung gian gây viêm.'
        , 'monitoring': ['Đáp ứng điều trị (giảm triệu chứng dị ứng)',
        'Tác dụng phụ (buồn ngủ, khô miệng) - hiếm với loratadine',
        'Chức năng gan nếu dùng lâu dài hoặc có triệu chứng (hiếm)',
        'Tương tác với erythromycin, ketoconazole (có thể tăng nồng độ nhưng thường không cần điều chỉnh)'
        ],precautions': [
        'Non-sedating nhưng một số người vẫn có thể buồn ngủ nhẹ',
        'Có thể dùng với thức ăn hoặc không (hấp thu tốt)',
        'Thận trọng với bệnh nhân suy gan (metabolite qua CYP3A4 và CYP2D6)',
        'Có thể dùng cho trẻ em từ 2 tuổi trở lên',
        'An toàn trong thai kỳ (category B)',
        'Ít tương tác thuốc, an toàn cho hầu hết bệnh nhân',
        'Tác dụng kéo dài 24 giờ nên chỉ cần dùng 1 lần/ngày'],pharmacokinetics': {'half_life':
        '8-28 giờ (desloratadine - metabolite hoạt động có half-life dài hơn)',
        'onset': '1-3 giờ', 'duration': '24 giờ', 'protein_binding': '97-99%',
        'clearance':
        'Gan: chuyển hóa qua CYP3A4 và CYP2D6 thành desloratadine (metabolite hoạt động, mạnh hơn loratadine). Thận: bài tiết một phần nguyên dạng và metabolites.'
        },storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng syrup: bảo quản ở nhiệt độ phòng, đậy kín sau khi dùng.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [],moderate': [{'drug': 'Erythromycin, Ketoconazole, Itraconazole',
        'mechanism': 'Ức chế CYP3A4, giảm chuyển hóa loratadine', 'effect':
        'Tăng nồng độ loratadine và desloratadine', 'management':
        'Thận trọng. Thường không cần điều chỉnh liều nhưng có thể tăng buồn ngủ nhẹ.'
        }],minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng loratadine hoặc desloratadine'],tương_đối': [
        'Suy gan nặng - thận trọng (giảm chuyển hóa)',
        'Trẻ em <2 tuổi - an toàn từ 2 tuổi trở lên']},pregnancy_lactation':
        {'fda_category': 'B', 'pregnancy_details':
        'An toàn trong thai kỳ. Không có bằng chứng về dị tật bẩm sinh. Có thể dùng ở tất cả các tam cá nguyệt. Loratadine là một trong những antihistamine được lựa chọn trong thai kỳ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Loratadine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Theo dõi dấu hiệu buồn ngủ ở trẻ (hiếm).'}
        },hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Thận trọng, có thể giảm liều nhẹ', 'severe':
        'Thận trọng, giảm liều hoặc tránh dùng', 'notes':
        'Loratadine chuyển hóa ở gan qua CYP3A4 và CYP2D6 thành desloratadine (metabolite hoạt động). Suy gan có thể làm giảm chuyển hóa, tăng nguy cơ tích lũy.'
        },overdose_management': {'symptoms': [
        'Buồn ngủ (tăng so với liều điều trị)', 'Nhức đầu', 'Khô miệng',
        'Lú lẫn (hiếm)', 'Tim đập nhanh (hiếm)'],antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ', 'treatment': [
        'Rửa dạ dày nếu uống trong vòng 1-2 giờ',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ',
        'Theo dõi ý thức, huyết áp, nhịp tim',
        'Điều trị hỗ trợ: truyền dịch nếu cần', 'Theo dõi ít nhất 4-6 giờ'],monitoring': 'Ý thức, huyết áp, nhịp tim'},reversal_agents': {
        'available': False, 'agents': []},administration_instructions': {
        'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Hấp thu tốt trong cả hai trường hợp'
        , 'timing':
        'Dùng 1 lần/ngày (tác dụng kéo dài 24 giờ). Có thể dùng buổi sáng hoặc tối.'
        },iv': {'reconstitution': 'Không có dạng IV', 'infusion_rate': 'N/A',
        'compatibility': [],incompatibility': [],
        }},references': {'primary_sources': [
        'FDA Drug Label - Clarityne (loratadine)',
        'UpToDate - Loratadine: Drug information',
        'Allergy & Clinical Immunology guidelines'],last_updated':
        '2024-12-19', 'evidence_level':
        'High - Multiple RCTs and systematic reviews'},
        "black_box_warnings": None,
}}


__all__ = ['ANTIHISTAMINE_H1_ANTAGONIST_2ND_GENERATIONS_DRUGS']
