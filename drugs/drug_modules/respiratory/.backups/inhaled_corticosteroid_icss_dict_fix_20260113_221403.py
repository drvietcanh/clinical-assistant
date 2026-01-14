"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Inhaled Corticosteroid (ICS)s

INHALED_CORTICOSTEROID_ICSS_DRUGS = {
    "Beclomethasone inhaled": {'group': 'Respiratory - Inhaled Corticosteroid (ICS)',
        "pregnancy": "C - Corticosteroid, thận trọng trong thai kỳ",
        'vietnamese_name': 'Beclomethasone, Beclovent, Qvar', 'administration': [
        'Inhalation'],
        'indications': [
        'Hen phế quản (kiểm soát, phòng ngừa)',
        'COPD (nếu có nhiều đợt cấp)'],
        'contraindications': [
        'Nhiễm trùng đường hô hấp nặng chưa điều trị', 'Dị ứng'],
        'dosage': {
        'adult_inhalation_low': '200-400mcg x 2 lần/ngày',
        'adult_inhalation_medium': '400-800mcg x 2 lần/ngày',
        'adult_inhalation_high': '800-1600mcg x 2 lần/ngày', 'notes':
        'Súc miệng sau khi dùng để tránh nấm miệng. Không dùng cho cắt cơn cấp'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': ['Nấm miệng (candidiasis)',
        'Khàn tiếng', 'Ho', 'Khô miệng', 'Tác dụng toàn thân (liều cao)',
        'Ức chế trục hạ đồi-tuyến yên-thượng thận (liều cao)'],
        'interactions': [
        'Ritonavir: tăng nồng độ beclomethasone (tránh dùng)',
        'Ketoconazole/Itraconazole: tăng nồng độ'],
        'mechanism_of_action':
        'Beclomethasone là corticosteroid hít (inhaled corticosteroid, ICS) có tác dụng kháng viêm mạnh tại chỗ. Beclomethasone gắn vào glucocorticoid receptor trong tế bào, sau đó di chuyển vào nhân và gắn vào glucocorticoid response elements (GRE) trên DNA, kích hoạt hoặc ức chế biểu hiện gen. Dẫn đến: ức chế tổng hợp các cytokine gây viêm (IL-1, IL-2, IL-4, IL-5, TNF-α), giảm phóng thích các chất trung gian gây viêm từ mast cells và eosinophils, giảm thâm nhập tế bào viêm, giảm phù nề niêm mạc phế quản, và tăng số lượng beta-2 receptors. Beclomethasone có tác dụng chủ yếu tại chỗ (phế quản), ít hấp thu toàn thân nên ít tác dụng phụ toàn thân. Tuy nhiên, một phần nhỏ vẫn được hấp thu và có thể gây tác dụng toàn thân ở liều cao. Beclomethasone được chuyển hóa nhanh ở gan (first-pass metabolism cao) nên tác dụng toàn thân ít hơn so với corticosteroid uống. Beclomethasone là ICS đầu tiên được sử dụng rộng rãi.'
        , 'monitoring': [
        'Đáp ứng điều trị (giảm triệu chứng hen, tần suất cơn cấp, nhu cầu dùng SABA)'
        'Nấm miệng (candidiasis) - kiểm tra lưỡi, miệng, đặc biệt nếu không súc miệng sau khi dùng'
        , 'Khàn tiếng, ho, kích ứng họng - tác dụng phụ tại chỗ phổ biến',
        'Tác dụng toàn thân (chỉ ở liều cao): ức chế trục HPA, chậm phát triển ở trẻ em, loãng xương, tăng huyết áp'
        , 'Chức năng gan nếu có triệu chứng (hiếm)',
        'Tương tác với ritonavir, ketoconazole, itraconazole (tăng nồng độ beclomethasone)'],
        'precautions': [
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG'
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, beclomethasone là thuốc duy trì'
        'Tác dụng phát huy sau vài ngày đến vài tuần - không mong đợi tác dụng tức thì'
        , 'Không ngừng đột ngột - giảm liều dần dần',
        'Tác dụng toàn thân hiếm với liều thường nhưng có thể xảy ra ở liều cao (>1600mcg/ngày)'
        'Thận trọng với bệnh nhân lao phổi, nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước'
        'Tránh dùng với ritonavir (tăng đáng kể nồng độ beclomethasone, tăng nguy cơ ức chế HPA)'
        , 'Thận trọng với ketoconazole, itraconazole (tăng nồng độ beclomethasone)',
        'Theo dõi chậm phát triển ở trẻ em nếu dùng liều cao',
        'Dùng đều đặn hàng ngày, không phải khi cần'],
        'pharmacokinetics': {
        'half_life': '15 giờ (trong phổi), 2-3 giờ (toàn thân sau hấp thu)',
        'onset': 'Vài giờ đến vài ngày (tác dụng kháng viêm)', 'duration':
        '12-24 giờ (dùng 2 lần/ngày)', 'protein_binding': '87%', 'clearance':
        'Gan: chuyển hóa nhanh qua CYP3A4 (first-pass metabolism cao, ~85-90% bị chuyển hóa). Thận: bài tiết một phần metabolites. Hấp thu toàn thân ít do chuyển hóa nhanh ở gan. Phần lớn tác dụng tại chỗ (phế quản).'},storage':
        'Dạng hít (MDI/DPI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Không đông lạnh. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Ritonavir', 'mechanism':
        'Ức chế CYP3A4, tăng đáng kể nồng độ beclomethasone', 'effect':
        'Tăng nguy cơ ức chế trục HPA, hội chứng Cushing, suy thượng thận',
        'management':
        'TRÁNH DÙNG với ritonavir. Nếu cần dùng, giảm liều beclomethasone đáng kể và theo dõi chặt chẽ.'}],
        'moderate': [{'drug': 'Ketoconazole, Itraconazole', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ beclomethasone', 'effect':
        'Tăng nguy cơ tác dụng toàn thân, ức chế HPA', 'management':
        'Thận trọng, theo dõi tác dụng toàn thân. Có thể cần giảm liều beclomethasone.'}],
        'minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng với beclomethasone hoặc các thành phần khác',
        'Nhiễm trùng đường hô hấp nặng chưa điều trị (lao phổi, nấm)'],
        'tương_đối': [
        'Lao phổi - cần điều trị lao trước, thận trọng',
        'Nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước',
        'Dùng với ritonavir - tránh dùng',
        'Dùng với ketoconazole, itraconazole - thận trọng']},contraindications_detail': {'tuyệt_đối': [
        'Dị ứng với beclomethasone hoặc các thành phần khác',
        'Nhiễm trùng đường hô hấp nặng chưa điều trị (lao phổi, nấm)'],
        'tương_đối': [
        'Lao phổi - cần điều trị lao trước, thận trọng',
        'Nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước',
        'Dùng với ritonavir - tránh dùng',
        'Dùng với ketoconazole, itraconazole - thận trọng']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Beclomethasone là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Beclomethasone được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do chuyển hóa nhanh ở gan), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Beclomethasone bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'}},hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe':
        'Thận trọng - beclomethasone chuyển hóa qua CYP3A4 ở gan, có thể tích lũy ở suy gan nặng'
        , 'notes':
        'Beclomethasone chuyển hóa nhanh qua CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng toàn thân. Theo dõi chặt chẽ tác dụng toàn thân. Có thể cần giảm liều.'},overdose_management': {'symptoms': [
        'Ức chế trục HPA (mệt mỏi, yếu, hạ huyết áp)',
        'Hội chứng Cushing (tăng cân, mặt tròn, tăng huyết áp)',
        'Tăng đường huyết', 'Loãng xương (liều cao kéo dài)',
        'Chậm phát triển ở trẻ em (liều cao)', 'Nấm miệng nặng',
        'Khàn tiếng nặng'],treatment': [
        'Ngừng ngay beclomethasone hoặc giảm liều đáng kể',
        'Theo dõi chức năng trục HPA (cortisol, ACTH)',
        'Bổ sung corticosteroid nếu có suy thượng thận',
        'Điều trị tăng đường huyết nếu cần', 'Theo dõi và điều trị triệu chứng'],
        'monitoring':
        'Theo dõi: chức năng trục HPA (cortisol, ACTH), đường huyết, huyết áp, cân nặng, chiều cao (ở trẻ em). Theo dõi ít nhất vài tuần do tác dụng kéo dài.'},reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là ngừng thuốc, giảm liều, và hỗ trợ. Có thể cần bổ sung corticosteroid nếu có suy thượng thận.'},administration_instructions': {'oral': None, 'iv': None, 'inhalation': {
        'technique':
        'Dạng hít (MDI/DPI): Lắc kỹ trước khi dùng (nếu MDI). Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).'
        , 'timing':
        'Dùng 2 lần/ngày (sáng và tối), đều đặn hàng ngày, không phải khi cần.',
        'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG.'
        , 'notes':
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp. Tác dụng phát huy sau vài ngày đến vài tuần.'}},references': {'primary_sources': ['FDA Label: Beclovent (Beclomethasone)',
        'UpToDate: Inhaled corticosteroids in asthma',
        'GINA Guidelines 2024: Asthma Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Beclomethasone'],evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'},
        "black_box_warnings": None,
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': [],qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': [],look_alike_sound_alike': []
        },guideline_tags': [
            'GINA Guidelines 2024 - Asthma Management - Inhaled corticosteroids',
            'FDA Warning - TRÁNH DÙNG với ritonavir (tăng đáng kể nồng độ beclomethasone, tăng nguy cơ ức chế HPA)',
            'WHO Guidelines - Essential medicines for asthma'
        ]
},
    "Budesonide inhaled": {'group': 'Respiratory - Inhaled Corticosteroid (ICS)',
        "pregnancy": "B - Corticosteroid, có thể sử dụng trong thai kỳ",
        ', 'vietnamese_name':
        'Budesonide, Pulmicort', 'administration': ['Inhalation', 'Nebulizer'],
        'indications': ['Hen phế quản (kiểm soát, phòng ngừa)',
        'COPD (nếu có nhiều đợt cấp)', 'Viêm phế quản co thắt'],
        'contraindications': ['Nhiễm trùng đường hô hấp nặng chưa điều trị',
        'Dị ứng'],adult_inhalation_medium': '400-800mcg x 2 lần/ngày',
        'adult_inhalation_high': '800-1600mcg x 2 lần/ngày', 'adult_nebulizer':
        '0.5-1mg x 2 lần/ngày', 'notes':
        'Súc miệng sau khi dùng để tránh nấm miệng. Không dùng cho cắt cơn cấp'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': ['Nấm miệng (candidiasis)',
        'Khàn tiếng', 'Ho', 'Khô miệng', 'Tác dụng toàn thân (liều cao)',
        'Ức chế trục hạ đồi-tuyến yên-thượng thận (liều cao)'],
        'interactions':
        ['Ritonavir: tăng nồng độ budesonide (tránh dùng)',
        'Ketoconazole/Itraconazole: tăng nồng độ'],
        'mechanism_of_action':
        'Budesonide là corticosteroid hít (inhaled corticosteroid, ICS) có tác dụng kháng viêm mạnh tại chỗ. Budesonide gắn vào glucocorticoid receptor trong tế bào, sau đó di chuyển vào nhân và gắn vào glucocorticoid response elements (GRE) trên DNA, kích hoạt hoặc ức chế biểu hiện gen. Dẫn đến: ức chế tổng hợp các cytokine gây viêm (IL-1, IL-2, IL-4, IL-5, TNF-α), giảm phóng thích các chất trung gian gây viêm từ mast cells và eosinophils, giảm thâm nhập tế bào viêm, giảm phù nề niêm mạc phế quản, và tăng số lượng beta-2 receptors. Budesonide có tác dụng chủ yếu tại chỗ (phế quản), ít hấp thu toàn thân nên ít tác dụng phụ toàn thân. Tuy nhiên, một phần nhỏ vẫn được hấp thu và có thể gây tác dụng toàn thân ở liều cao. Budesonide được chuyển hóa nhanh ở gan (first-pass metabolism cao) nên tác dụng toàn thân ít hơn so với corticosteroid uống.'
        , 'monitoring': [
        'Đáp ứng điều trị (giảm triệu chứng hen, tần suất cơn cấp, nhu cầu dùng SABA)'
        'Nấm miệng (candidiasis) - kiểm tra lưỡi, miệng, đặc biệt nếu không súc miệng sau khi dùng'
        , 'Khàn tiếng, ho, kích ứng họng - tác dụng phụ tại chỗ phổ biến',
        'Tác dụng toàn thân (chỉ ở liều cao): ức chế trục HPA, chậm phát triển ở trẻ em, loãng xương, tăng huyết áp'
        , 'Chức năng gan nếu có triệu chứng (hiếm)',
        'Tương tác với ritonavir, ketoconazole, itraconazole (tăng nồng độ budesonide)'
        ],
        'precautions': [
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG'
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, budesonide là thuốc duy trì'
        'Tác dụng phát huy sau vài ngày đến vài tuần - không mong đợi tác dụng tức thì'
        , 'Không ngừng đột ngột - giảm liều dần dần',
        'Tác dụng toàn thân hiếm với liều thường nhưng có thể xảy ra ở liều cao (>1600mcg/ngày)'
        'Thận trọng với bệnh nhân lao phổi, nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước'
        'Tránh dùng với ritonavir (tăng đáng kể nồng độ budesonide, tăng nguy cơ ức chế HPA)'
        , 'Thận trọng với ketoconazole, itraconazole (tăng nồng độ budesonide)',
        'Theo dõi chậm phát triển ở trẻ em nếu dùng liều cao',
        'Có thể dùng cho trẻ em (có dạng nebulizer)',
        'Dùng đều đặn hàng ngày, không phải khi cần'],
        'pharmacokinetics': {
        'half_life': '2-3 giờ (trong phổi), 4-6 giờ (toàn thân sau hấp thu)',
        'onset': 'Vài giờ đến vài ngày (tác dụng kháng viêm)', 'duration':
        '12-24 giờ (dùng 2 lần/ngày)', 'protein_binding': '88-90%', 'clearance':
        'Gan: chuyển hóa nhanh qua CYP3A4 (first-pass metabolism cao, ~85-90% bị chuyển hóa). Thận: bài tiết một phần metabolites. Hấp thu toàn thân ít do chuyển hóa nhanh ở gan. Phần lớn tác dụng tại chỗ (phế quản).'
        },storage':
        'Dạng hít (MDI/DPI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Không đông lạnh. Nebulizer suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 2 giờ sau khi mở gói. Bảo quản trong tủ lạnh nếu không dùng ngay (2-8°C), để nhiệt độ phòng trước khi dùng.'
        ,         'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Ritonavir', 'mechanism':
        'Ức chế CYP3A4, tăng đáng kể nồng độ budesonide', 'effect':
        'Tăng nguy cơ ức chế trục HPA, hội chứng Cushing, suy thượng thận',
        'management':
        'TRÁNH DÙNG với ritonavir. Nếu cần dùng, giảm liều budesonide đáng kể và theo dõi chặt chẽ.'
        }, {'drug': 'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ budesonide', 'effect':
        'Tăng nguy cơ tác dụng toàn thân, ức chế HPA', 'management':
        'Thận trọng, theo dõi tác dụng toàn thân. Có thể cần giảm liều budesonide.'
        }],
        'minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng với budesonide hoặc các thành phần khác',
        'Nhiễm trùng đường hô hấp nặng chưa điều trị (lao phổi, nấm)'],
        'tương_đối': ['Lao phổi - cần điều trị lao trước, thận trọng',
        'Nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước',
        'Dùng với ritonavir - tránh dùng',
        'Dùng với ketoconazole, itraconazole - thận trọng']},contraindications_detail': {'tuyệt_đối': [
        'Dị ứng với budesonide hoặc các thành phần khác',
        'Nhiễm trùng đường hô hấp nặng chưa điều trị (lao phổi, nấm)'],
        'tương_đối': ['Lao phổi - cần điều trị lao trước, thận trọng',
        'Nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước',
        'Dùng với ritonavir - tránh dùng',
        'Dùng với ketoconazole, itraconazole - thận trọng']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Budesonide là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Budesonide được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do chuyển hóa nhanh ở gan), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Budesonide bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        }},hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe':
        'Thận trọng - budesonide chuyển hóa qua CYP3A4 ở gan, có thể tích lũy ở suy gan nặng'
        , 'notes':
        'Budesonide chuyển hóa nhanh qua CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng toàn thân. Theo dõi chặt chẽ tác dụng toàn thân. Có thể cần giảm liều.'
        },overdose_management': {'symptoms': [
        'Ức chế trục HPA (mệt mỏi, yếu, hạ huyết áp)',
        'Hội chứng Cushing (tăng cân, mặt tròn, tăng huyết áp)',
        'Tăng đường huyết', 'Loãng xương (liều cao kéo dài)',
        'Chậm phát triển ở trẻ em (liều cao)', 'Nấm miệng nặng',
        'Khàn tiếng nặng'],treatment': ['Ngừng ngay budesonide hoặc giảm liều đáng kể',
        'Theo dõi chức năng trục HPA (cortisol, ACTH)',
        'Bổ sung corticosteroid nếu có suy thượng thận',
        'Điều trị tăng đường huyết nếu cần', 'Theo dõi và điều trị triệu chứng'
        ],
        'monitoring':
        'Theo dõi: chức năng trục HPA (cortisol, ACTH), đường huyết, huyết áp, cân nặng, chiều cao (ở trẻ em). Theo dõi ít nhất vài tuần do tác dụng kéo dài.'
        },reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là ngừng thuốc, giảm liều, và hỗ trợ. Có thể cần bổ sung corticosteroid nếu có suy thượng thận.'
        },administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dạng hít (MDI/DPI): Lắc kỹ trước khi dùng (nếu MDI). Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).'
        , 'timing':
        'Dùng 2 lần/ngày (sáng và tối), đều đặn hàng ngày, không phải khi cần.',
        'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG.'
        , 'notes':
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp. Tác dụng phát huy sau vài ngày đến vài tuần.'
        },nebulizer': {'reconstitution':
        'Dùng budesonide nebulizer suspension. Lắc kỹ trước khi dùng.',
        'administration':
        'Dùng qua nebulizer, thở bình thường trong 10-15 phút.', 'timing':
        'Dùng 2 lần/ngày (sáng và tối). Dùng trong vòng 2 giờ sau khi mở gói.',
        'after_use': 'Súc miệng sau khi dùng.'}},references': {
        'primary_sources': ['FDA Label: Pulmicort (Budesonide)',
        'UpToDate: Inhaled corticosteroids in asthma',
        'GINA Guidelines 2024: Asthma Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Budesonide'],evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines',
        "black_box_warnings": None,
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': [],qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': [],look_alike_sound_alike': []
        },guideline_tags': [
            'GINA Guidelines 2024 - Asthma Management - Inhaled corticosteroids',
            'FDA Warning - TRÁNH DÙNG với ritonavir (tăng đáng kể nồng độ budesonide, tăng nguy cơ ức chế HPA)',
            'WHO Guidelines - Essential medicines for asthma'
        ]
    },
    "Ciclesonide": {'group': 'Respiratory - Inhaled Corticosteroid (ICS)',
        "pregnancy": "C - Corticosteroid, thận trọng trong thai kỳ",
        'vietnamese_name': 'Ciclesonide, Alvesco', 'administration': [
        'Inhalation'],
        'indications': [
        'Hen phế quản (kiểm soát, phòng ngừa)',
        'COPD (nếu có nhiều đợt cấp)'],
        'contraindications': [
        'Nhiễm trùng đường hô hấp nặng chưa điều trị', 'Dị ứng'],
        'dosage': {
        'adult_inhalation_low': '80-160mcg x 2 lần/ngày',
        'adult_inhalation_medium': '160-320mcg x 2 lần/ngày',
        'adult_inhalation_high': '320-640mcg x 2 lần/ngày', 'notes':
        'Súc miệng sau khi dùng để tránh nấm miệng. Không dùng cho cắt cơn cấp'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': ['Nấm miệng (candidiasis)',
        'Khàn tiếng', 'Ho', 'Khô miệng', 'Tác dụng toàn thân (liều cao)'],
        'interactions': [
        'Ritonavir: tăng nồng độ ciclesonide (tránh dùng)',
        'Ketoconazole/Itraconazole: tăng nồng độ'],
        'mechanism_of_action':
        'Ciclesonide là corticosteroid hít (inhaled corticosteroid, ICS) có tác dụng kháng viêm mạnh tại chỗ. Ciclesonide là prodrug, được chuyển thành des-ciclesonide (hoạt chất) bởi esterase trong phổi. Des-ciclesonide gắn vào glucocorticoid receptor trong tế bào, sau đó di chuyển vào nhân và gắn vào glucocorticoid response elements (GRE) trên DNA, kích hoạt hoặc ức chế biểu hiện gen. Dẫn đến: ức chế tổng hợp các cytokine gây viêm, giảm phóng thích các chất trung gian gây viêm từ mast cells và eosinophils, giảm thâm nhập tế bào viêm, giảm phù nề niêm mạc phế quản. Ciclesonide có tác dụng chủ yếu tại chỗ (phế quản), ít hấp thu toàn thân nên ít tác dụng phụ toàn thân. Đặc điểm: là prodrug, được kích hoạt tại phổi, ít tác dụng toàn thân hơn các ICS khác.'
        , 'monitoring': [
        'Đáp ứng điều trị (giảm triệu chứng hen, tần suất cơn cấp, nhu cầu dùng SABA)'
        'Nấm miệng (candidiasis) - kiểm tra lưỡi, miệng, đặc biệt nếu không súc miệng sau khi dùng'
        , 'Khàn tiếng, ho, kích ứng họng - tác dụng phụ tại chỗ phổ biến',
        'Tác dụng toàn thân (chỉ ở liều cao): ức chế trục HPA, chậm phát triển ở trẻ em'
        , 'Chức năng gan nếu có triệu chứng (hiếm)',
        'Tương tác với ritonavir, ketoconazole, itraconazole (tăng nồng độ)'],
        'precautions': [
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG'
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, ciclesonide là thuốc duy trì'
        'Tác dụng phát huy sau vài ngày đến vài tuần - không mong đợi tác dụng tức thì'
        , 'Không ngừng đột ngột - giảm liều dần dần',
        'Tác dụng toàn thân hiếm với liều thường nhưng có thể xảy ra ở liều cao (>640mcg/ngày)'
        'Thận trọng với bệnh nhân lao phổi, nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước'
        'Tránh dùng với ritonavir (tăng đáng kể nồng độ ciclesonide, tăng nguy cơ ức chế HPA)'
        , 'Thận trọng với ketoconazole, itraconazole (tăng nồng độ ciclesonide)',
        'Dùng đều đặn hàng ngày, không phải khi cần'],
        'pharmacokinetics': {
        'half_life': '5-7 giờ (des-ciclesonide)', 'onset':
        'Vài giờ đến vài ngày (tác dụng kháng viêm)', 'duration':
        '12-24 giờ (dùng 2 lần/ngày)', 'protein_binding': '99%', 'clearance':
        'Gan: chuyển hóa qua CYP3A4 (first-pass metabolism cao). Thận: bài tiết một phần metabolites. Ciclesonide là prodrug, được kích hoạt tại phổi thành des-ciclesonide. Hấp thu toàn thân ít do chuyển hóa nhanh ở gan. Phần lớn tác dụng tại chỗ (phế quản).'
        },storage':
        'Dạng hít (MDI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Không đông lạnh. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Ritonavir', 'mechanism':
        'Ức chế CYP3A4, tăng đáng kể nồng độ ciclesonide', 'effect':
        'Tăng nguy cơ ức chế trục HPA, hội chứng Cushing, suy thượng thận',
        'management':
        'TRÁNH DÙNG với ritonavir. Nếu cần dùng, giảm liều ciclesonide đáng kể và theo dõi chặt chẽ.'
        }, {'drug': 'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ ciclesonide', 'effect':
        'Tăng nguy cơ tác dụng toàn thân, ức chế HPA', 'management':
        'Thận trọng, theo dõi tác dụng toàn thân. Có thể cần giảm liều ciclesonide.'
        }],
        'minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng với ciclesonide hoặc các thành phần khác',
        'Nhiễm trùng đường hô hấp nặng chưa điều trị (lao phổi, nấm)'],
        'tương_đối': [
        'Lao phổi - cần điều trị lao trước, thận trọng',
        'Nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước',
        'Dùng với ritonavir - tránh dùng',
        'Dùng với ketoconazole, itraconazole - thận trọng']},contraindications_detail': {'tuyệt_đối': [
        'Dị ứng với ciclesonide hoặc các thành phần khác',
        'Nhiễm trùng đường hô hấp nặng chưa điều trị (lao phổi, nấm)'],
        'tương_đối': [
        'Lao phổi - cần điều trị lao trước, thận trọng',
        'Nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước',
        'Dùng với ritonavir - tránh dùng',
        'Dùng với ketoconazole, itraconazole - thận trọng']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Ciclesonide là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Ciclesonide được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do chuyển hóa nhanh ở gan), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Ciclesonide bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        }},hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe':
        'Thận trọng - ciclesonide chuyển hóa qua CYP3A4 ở gan, có thể tích lũy ở suy gan nặng'
        , 'notes':
        'Ciclesonide chuyển hóa nhanh qua CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng toàn thân. Theo dõi chặt chẽ tác dụng toàn thân. Có thể cần giảm liều.'
        },overdose_management': {'symptoms': [
        'Ức chế trục HPA (mệt mỏi, yếu, hạ huyết áp)',
        'Hội chứng Cushing (tăng cân, mặt tròn, tăng huyết áp)',
        'Tăng đường huyết', 'Loãng xương (liều cao kéo dài)',
        'Chậm phát triển ở trẻ em (liều cao)', 'Nấm miệng nặng',
        'Khàn tiếng nặng'],treatment': [
        'Ngừng ngay ciclesonide hoặc giảm liều đáng kể',
        'Theo dõi chức năng trục HPA (cortisol, ACTH)',
        'Bổ sung corticosteroid nếu có suy thượng thận',
        'Điều trị tăng đường huyết nếu cần', 'Theo dõi và điều trị triệu chứng'],
        'monitoring':
        'Theo dõi: chức năng trục HPA (cortisol, ACTH), đường huyết, huyết áp, cân nặng, chiều cao (ở trẻ em). Theo dõi ít nhất vài tuần do tác dụng kéo dài.'
        },reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là ngừng thuốc, giảm liều, và hỗ trợ. Có thể cần bổ sung corticosteroid nếu có suy thượng thận.'
        },administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dạng hít (MDI): Lắc kỹ trước khi dùng. Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).'
        , 'timing':
        'Dùng 2 lần/ngày (sáng và tối), đều đặn hàng ngày, không phải khi cần.',
        'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG.'
        , 'notes':
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp. Tác dụng phát huy sau vài ngày đến vài tuần. Ciclesonide là prodrug, được kích hoạt tại phổi.'}},references': {'primary_sources': [
        'FDA Label: Alvesco (Ciclesonide)',
        'UpToDate: Inhaled corticosteroids in asthma',
        'GINA Guidelines 2024: Asthma Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Ciclesonide'],evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'},
        "black_box_warnings": None,
        'risk_flags': {
            'high_alert': False,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': [],qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': [],look_alike_sound_alike': []
        },guideline_tags': [
            'GINA Guidelines 2024 - Asthma Management - Inhaled corticosteroids',
            'FDA Warning - TRÁNH DÙNG với ritonavir (tăng đáng kể nồng độ ciclesonide, tăng nguy cơ ức chế HPA)',
            'WHO Guidelines - Essential medicines for asthma'
        ]
    },
    "Fluticasone inhaled": {'group': 'Respiratory - Inhaled Corticosteroid (ICS)',
        "pregnancy": "C - Corticosteroid, thận trọng trong thai kỳ",
        ', 'vietnamese_name':
        'Fluticasone, Flixotide', 'administration': ['Inhalation'],
        'indications': ['Hen phế quản (kiểm soát, phòng ngừa)',
        'COPD (kết hợp với LABA nếu nhiều đợt cấp)'],
        'contraindications': [
        'Nhiễm trùng đường hô hấp nặng', 'Dị ứng'],
        'dosage': {
        'adult_inhalation_low': '100-250mcg x 2 lần/ngày',
        'adult_inhalation_medium': '250-500mcg x 2 lần/ngày',
        'adult_inhalation_high': '500-1000mcg x 2 lần/ngày', 'notes':
        'Súc miệng sau khi dùng. Thường dùng kết hợp với LABA (Salmeterol)'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': ['Nấm miệng', 'Khàn tiếng',
        'Ho', 'Kích ứng cổ họng', 'Tác dụng toàn thân (liều cao)',
        'Chậm phát triển ở trẻ em (liều cao)'],
        'interactions': [
        'Ritonavir: tăng đáng kể nồng độ fluticasone - tránh dùng',
        'Ketoconazole: tăng nồng độ'],
        'mechanism_of_action':
        'Fluticasone là corticosteroid hít (inhaled corticosteroid, ICS) có tác dụng kháng viêm mạnh tại chỗ. Fluticasone gắn vào glucocorticoid receptor trong tế bào, sau đó di chuyển vào nhân và gắn vào glucocorticoid response elements (GRE) trên DNA, kích hoạt hoặc ức chế biểu hiện gen. Dẫn đến: ức chế tổng hợp các cytokine gây viêm (IL-1, IL-2, IL-4, IL-5, TNF-α), giảm phóng thích các chất trung gian gây viêm từ mast cells và eosinophils, giảm thâm nhập tế bào viêm, giảm phù nề niêm mạc phế quản, và tăng số lượng beta-2 receptors. Fluticasone có tác dụng chủ yếu tại chỗ (phế quản), ít hấp thu toàn thân nên ít tác dụng phụ toàn thân. Tuy nhiên, một phần nhỏ vẫn được hấp thu và có thể gây tác dụng toàn thân ở liều cao. Fluticasone được chuyển hóa nhanh ở gan (first-pass metabolism cao) nhưng thời gian bán thải dài hơn budesonide. Thường dùng kết hợp với LABA (long-acting beta-2 agonist) như salmeterol trong dạng fixed-dose combination.'
        , 'monitoring': [
        'Đáp ứng điều trị (giảm triệu chứng hen, tần suất cơn cấp, nhu cầu dùng SABA)'
        'Nấm miệng (candidiasis) - kiểm tra lưỡi, miệng, đặc biệt nếu không súc miệng sau khi dùng'
        , 'Khàn tiếng, ho, kích ứng cổ họng - tác dụng phụ tại chỗ phổ biến',
        'Tác dụng toàn thân (chỉ ở liều cao): ức chế trục HPA, chậm phát triển ở trẻ em, loãng xương, tăng huyết áp'
        , 'Chức năng gan nếu có triệu chứng (hiếm)',
        'Tương tác với ritonavir (tăng đáng kể nồng độ), ketoconazole (tăng nồng độ)'
        ],
        'precautions': [
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG'
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, fluticasone là thuốc duy trì'
        'Tác dụng phát huy sau vài ngày đến vài tuần - không mong đợi tác dụng tức thì'
        , 'Không ngừng đột ngột - giảm liều dần dần',
        'Tác dụng toàn thân hiếm với liều thường nhưng có thể xảy ra ở liều cao (>1000mcg/ngày)'
        'Thận trọng với bệnh nhân lao phổi, nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước'
        'TRÁNH DÙNG với ritonavir (tăng đáng kể nồng độ fluticasone, tăng nguy cơ ức chế HPA nghiêm trọng, có thể gây hội chứng Cushing)'
        'Thận trọng với ketoconazole, itraconazole (tăng nồng độ fluticasone)',
        'Theo dõi chậm phát triển ở trẻ em nếu dùng liều cao',
        'Thường dùng kết hợp với LABA (salmeterol) trong dạng fixed-dose combination (Seretide/Advair)'
        , 'Dùng đều đặn hàng ngày, không phải khi cần'],
        'pharmacokinetics': {
        'half_life': '7-8 giờ (trong phổi), 13-17 giờ (toàn thân sau hấp thu)',
        'onset': 'Vài giờ đến vài ngày (tác dụng kháng viêm)', 'duration':
        '12-24 giờ (dùng 2 lần/ngày)', 'protein_binding': '91%', 'clearance':
        'Gan: chuyển hóa nhanh qua CYP3A4 (first-pass metabolism cao, ~99% bị chuyển hóa). Thận: bài tiết một phần metabolites. Hấp thu toàn thân ít do chuyển hóa nhanh ở gan. Phần lớn tác dụng tại chỗ (phế quản). Thời gian bán thải dài hơn budesonide.'
        },storage':
        'Dạng hít (MDI/DPI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Không đông lạnh. Kiểm tra xem có còn thuốc (lắc, nghe tiếng). Dạng fixed-dose combination với salmeterol: bảo quản tương tự.'
        , 'black_box_warnings':
        'TRÁNH DÙNG với ritonavir (tăng đáng kể nồng độ fluticasone, tăng nguy cơ ức chế trục HPA nghiêm trọng, có thể gây hội chứng Cushing, suy thượng thận). Nguy cơ chậm phát triển ở trẻ em với liều cao.'
        , 'drug_interactions': {'major': [{'drug': 'Ritonavir', 'mechanism':
        'Ức chế CYP3A4, tăng đáng kể nồng độ fluticasone', 'effect':
        'Tăng nguy cơ ức chế trục HPA nghiêm trọng, hội chứng Cushing, suy thượng thận'
        , 'management':
        'TRÁNH DÙNG với ritonavir. Nếu cần dùng, giảm liều fluticasone đáng kể hoặc xem xét thuốc thay thế (budesonide). Theo dõi chặt chẽ.'
        }, {'drug': 'Ketoconazole, Itraconazole, Posaconazole', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ fluticasone', 'effect':
        'Tăng nguy cơ tác dụng toàn thân, ức chế HPA', 'management':
        'Thận trọng, theo dõi tác dụng toàn thân. Có thể cần giảm liều fluticasone.'
        }],
        'minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng với fluticasone hoặc các thành phần khác',
        'Nhiễm trùng đường hô hấp nặng chưa điều trị (lao phổi, nấm)',
        'Dùng với ritonavir - chống chỉ định tuyệt đối'],
        'tương_đối': [
        'Lao phổi - cần điều trị lao trước, thận trọng',
        'Nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước',
        'Dùng với ketoconazole, itraconazole - thận trọng']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Fluticasone là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Fluticasone được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hấp thu toàn thân ít từ dạng hít (do chuyển hóa nhanh ở gan), nên tác dụng toàn thân tối thiểu. Có thể được dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Fluticasone bài tiết ít vào sữa mẹ do hấp thu toàn thân tối thiểu từ dạng hít. Nồng độ trong sữa mẹ rất thấp, không đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        }},hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe':
        'Thận trọng - fluticasone chuyển hóa qua CYP3A4 ở gan, có thể tích lũy ở suy gan nặng'
        , 'notes':
        'Fluticasone chuyển hóa nhanh qua CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng toàn thân. Theo dõi chặt chẽ tác dụng toàn thân. Có thể cần giảm liều.'
        },overdose_management': {'symptoms': [
        'Ức chế trục HPA (mệt mỏi, yếu, hạ huyết áp)',
        'Hội chứng Cushing (tăng cân, mặt tròn, tăng huyết áp)',
        'Tăng đường huyết', 'Loãng xương (liều cao kéo dài)',
        'Chậm phát triển ở trẻ em (liều cao)', 'Nấm miệng nặng',
        'Khàn tiếng nặng'],treatment': ['Ngừng ngay fluticasone hoặc giảm liều đáng kể',
        'Theo dõi chức năng trục HPA (cortisol, ACTH)',
        'Bổ sung corticosteroid nếu có suy thượng thận',
        'Điều trị tăng đường huyết nếu cần', 'Theo dõi và điều trị triệu chứng'
        ],
        'monitoring':
        'Theo dõi: chức năng trục HPA (cortisol, ACTH), đường huyết, huyết áp, cân nặng, chiều cao (ở trẻ em). Theo dõi ít nhất vài tuần do tác dụng kéo dài.'
        },reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là ngừng thuốc, giảm liều, và hỗ trợ. Có thể cần bổ sung corticosteroid nếu có suy thượng thận.'
        },administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dạng hít (MDI/DPI): Lắc kỹ trước khi dùng (nếu MDI). Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).'
        , 'timing':
        'Dùng 2 lần/ngày (sáng và tối), đều đặn hàng ngày, không phải khi cần.',
        'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG.'
        , 'with_laba':
        'Thường dùng kết hợp với LABA (salmeterol) trong dạng fixed-dose combination (Seretide/Advair).'
        , 'notes':
        'Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp. Tác dụng phát huy sau vài ngày đến vài tuần. TRÁNH DÙNG với ritonavir.'
        }},references': {'primary_sources': [
        'FDA Label: Flixotide (Fluticasone)',
        'UpToDate: Inhaled corticosteroids in asthma',
        'GINA Guidelines 2024: Asthma Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Fluticasone'],evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'},risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': [],qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': [],look_alike_sound_alike': []
        },guideline_tags': [
            'FDA Black Box Warning - TRÁNH DÙNG với ritonavir (tăng đáng kể nồng độ fluticasone, tăng nguy cơ ức chế trục HPA nghiêm trọng, có thể gây hội chứng Cushing, suy thượng thận)',
            'ISMP High Alert Medications',
            'GINA Guidelines 2024 - Asthma Management - Inhaled corticosteroids',
            'WHO Guidelines - Essential medicines for asthma'
        ]
        }
}

__all__ = ['INHALED_CORTICOSTEROID_ICSS_DRUGS']
