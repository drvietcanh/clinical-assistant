"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Long-acting Beta-2 Agonist (LABA)s

LONG_ACTING_BETA_2_AGONIST_LABAS_DRUGS = {
    "Formoterol": {'group': 'Respiratory - Long-acting Beta-2 Agonist (LABA)',',
"pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        'vietnamese_name': 'Formoterol, Foradil, Oxeze', 'administration': [
        'Inhalation'], 'indications': [
        'Hen phế quản (phòng ngừa, phải dùng với ICS)', 'COPD (phòng ngừa)',
        'Co thắt phế quản ban đêm', 'Dự phòng co thắt do vận động'],
        'contraindications': ['Dị ứng', 'Nhịp tim nhanh nặng',
        'Hen phế quản cấp (không dùng đơn độc)'], 'dosage': {'adult_inhalation':
        '12mcg x 2 lần/ngày (sáng và tối) hoặc 24mcg x 1 lần/ngày', 'notes':
        'PHẢI dùng kết hợp với ICS. Tác dụng nhanh hơn salmeterol (5 phút vs 15-30 phút). Tác dụng kéo dài 12 giờ'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Tim đập nhanh', 'Run cơ',
        'Đau đầu', 'Co thắt phế quản nghịch lý (hiếm)', 'Loạn nhịp tim (hiếm)'],
        'interactions': ['Beta-blocker: đối kháng tác dụng',
        'Theophylline: tăng tác dụng phụ'],
        'mechanism_of_action':
        'Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng dài (12 giờ) do liên kết chặt với receptor. Khác với salmeterol, formoterol có tác dụng nhanh hơn (5 phút vs 15-30 phút) do có ái lực cao hơn và giải phóng nhanh hơn từ receptor. Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch. Giảm phóng thích chất trung gian gây viêm từ mast cells. Dùng để phòng ngừa, nhưng có thể dùng để cắt cơn nhẹ do tác dụng nhanh (tuy nhiên vẫn nên dùng SABA cho cơn cấp).'
        , 'monitoring': [
        'Nhịp tim, huyết áp (đặc biệt khi bắt đầu điều trị)',
        'Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa',
        'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp',
        'Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)',
        'Tần suất dùng SABA (nếu tăng → cần đánh giá lại điều trị)'], 'precautions': [
        'PHẢI dùng kết hợp với ICS (inhaled corticosteroid) - không bao giờ dùng đơn độc cho hen phế quản'
        'Tác dụng nhanh hơn salmeterol (5 phút) - có thể dùng để cắt cơn nhẹ, nhưng vẫn nên dùng SABA cho cơn cấp'
        , 'Không dùng đơn độc cho hen phế quản cấp - nguy cơ tăng tử vong',
        'Tránh dùng với beta-blocker (đối kháng tác dụng)',
        'Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)'
        , 'Dùng đều đặn 2 lần/ngày (sáng và tối) để phòng ngừa',
        'Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng',
        'Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị và tăng ICS',
        'Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị'], 'pharmacokinetics': {
        'half_life': '10 giờ (dài hơn salmeterol)', 'onset':
        '5 phút (nhanh hơn salmeterol - 15-30 phút)', 'duration': '12 giờ (dài)',
        'protein_binding': '61-64%', 'clearance':
        'Gan (chuyển hóa qua CYP2D6, CYP2C19, glucuronidation), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings':
        'KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen. Chỉ dùng để phòng ngừa và phải luôn có SABA để cắt cơn.'
        , 'drug_interactions': {'major': [{'drug':
        'Beta-blockers (không chọn lọc: Propranolol, Nadolol)', 'mechanism':
        'Đối kháng tác dụng beta-2, chặn tác dụng giãn phế quản của formoterol',
        'effect':
        'Đối kháng tác dụng giãn phế quản, có thể gây co thắt phế quản nặng, suy hô hấp'
        , 'management':
        'TRÁNH DÙNG với beta-blocker không chọn lọc. Nếu bệnh nhân cần beta-blocker, dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng. Theo dõi chặt chẽ đáp ứng phế quản.'
        }, {'drug': 'Theophylline', 'mechanism':
        'Cả hai đều kích thích beta-adrenergic, có thể tăng tác dụng phụ và độc tính'
        , 'effect':
        'Tăng tác dụng phụ (run, tim đập nhanh, loạn nhịp), tăng nguy cơ độc tính theophylline'
        , 'management':
        'Theo dõi nồng độ theophylline. Theo dõi nhịp tim và triệu chứng. Có thể cần giảm liều theophylline.'
        }, {'drug': 'Digoxin', 'mechanism':
        'Formoterol có thể gây hạ kali máu và tăng nhịp tim, tăng nguy cơ độc tính digoxin'
        , 'effect':
        'Tăng nguy cơ loạn nhịp tim, tăng độc tính digoxin (đặc biệt khi hạ kali máu)'
        , 'management':
        'Theo dõi nồng độ digoxin và kali máu. Theo dõi ECG nếu có triệu chứng. Có thể cần điều chỉnh liều digoxin.'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng với formoterol hoặc các thành phần khác',
        'Nhịp tim nhanh nặng không kiểm soát (>120 bpm)',
        'Rối loạn nhịp tim nặng (rung nhĩ, rung thất không kiểm soát)',
        'Hen phế quản cấp (không dùng đơn độc, không dùng để cắt cơn)'], 'tương_đối': [
        'Bệnh tim mạch (suy tim, bệnh mạch vành) - thận trọng, theo dõi chặt chẽ',
        'Tăng huyết áp không kiểm soát - có thể tăng huyết áp',
        'Loạn nhịp tim nhẹ - có thể làm nặng',
        'Đái tháo đường - có thể tăng đường huyết',
        'Hạ kali máu - có thể làm nặng',
        'Cường giáp - tăng nhạy cảm với catecholamine',
        'Dùng với digoxin - tăng nguy cơ loạn nhịp',
        'Dùng với theophylline - tăng tác dụng phụ']}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Formoterol là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Formoterol được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hen phế quản không kiểm soát có thể gây nguy hiểm cho cả mẹ và thai nhi (thiếu oxy, suy thai). Formoterol có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng PHẢI dùng kết hợp với ICS. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Formoterol bài tiết ít vào sữa mẹ. Nồng độ trong sữa mẹ rất thấp do hấp thu toàn thân ít từ dạng hít. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe':
        'Thận trọng - formoterol chuyển hóa qua gan (CYP2D6, CYP2C19), có thể tích lũy ở suy gan nặng'
        , 'notes':
        'Formoterol chuyển hóa qua CYP2D6, CYP2C19, và glucuronidation ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ nhịp tim và tác dụng phụ. Có thể cần giảm liều hoặc tăng khoảng cách giữa các liều.'},
        'overdose_management': {'symptoms': [
        'Nhịp tim nhanh nghiêm trọng (>150 bpm)', 'Run cơ nặng',
        'Loạn nhịp tim (rung nhĩ, rung thất)', 'Đau ngực', 'Khó thở nặng',
        'Co thắt phế quản nghịch lý', 'Hạ kali máu nghiêm trọng',
        'Tăng đường huyết', 'Kích động, lo âu', 'Đau đầu nặng'], 'antidote':
        'Không có antidote đặc hiệu. Beta-blocker chọn lọc beta-1 (atenolol, metoprolol) có thể được dùng để đối kháng tác dụng tim mạch, nhưng thận trọng vì có thể làm nặng co thắt phế quản.'
        , 'treatment': ['Ngừng ngay formoterol',
        'Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)',
        'Theo dõi nhịp tim, huyết áp, ECG liên tục',
        'Điều trị loạn nhịp tim nếu có (theo protocol)',
        'Bổ sung kali nếu hạ kali máu', 'Điều trị tăng đường huyết nếu cần',
        'Nếu có co thắt phế quản nghịch lý: dùng ipratropium hoặc corticosteroid, tránh dùng SABA'
        , 'Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)',
        'Theo dõi và điều trị triệu chứng'], 'monitoring':
        'Theo dõi liên tục: nhịp tim, huyết áp, ECG, SpO2, kali máu, đường huyết, đáp ứng phế quản. Theo dõi ít nhất 12-24 giờ do thời gian bán thải dài (10 giờ).'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Beta-blocker chọn lọc beta-1 (Atenolol, Metoprolol)', 'mechanism':
        'Đối kháng tác dụng beta-adrenergic, giảm tác dụng tim mạch',
        'indication': 'Quá liều gây nhịp tim nhanh nghiêm trọng, loạn nhịp tim',
        'caution':
        'Thận trọng vì có thể làm nặng co thắt phế quản. Chỉ dùng khi tác dụng tim mạch nghiêm trọng và có hỗ trợ hô hấp sẵn sàng.'}],
        'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Beta-blocker chọn lọc beta-1 có thể được dùng để đối kháng tác dụng tim mạch nhưng thận trọng.'},
        'administration_instructions': {'oral': None, 'iv': None, 'inhalation': {
        'technique':
        'Dùng dạng hít (MDI hoặc DPI). Lắc kỹ trước khi dùng (nếu MDI). Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).'
        , 'timing':
        'Dùng 2 lần/ngày (sáng và tối), cách nhau khoảng 12 giờ. Dùng đều đặn hàng ngày, không phải khi cần. Tác dụng nhanh (5 phút) - có thể dùng để cắt cơn nhẹ, nhưng vẫn nên dùng SABA cho cơn cấp.'
        , 'with_ics':
        'PHẢI dùng kết hợp với ICS (inhaled corticosteroid). Có thể dùng riêng hoặc dùng dạng fixed-dose combination (Symbicort: budesonide + formoterol).'
        , 'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và tránh nấm miệng (đặc biệt nếu dùng với ICS).'
        , 'notes':
        'Tác dụng nhanh hơn salmeterol (5 phút vs 15-30 phút) - có thể dùng để cắt cơn nhẹ, nhưng vẫn nên dùng SABA (salbutamol) cho cơn cấp. Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị.'}},
        'references': {'primary_sources': ['FDA Label: Foradil (Formoterol)',
        'UpToDate: Long-acting beta-2 agonists in asthma',
        'GINA Guidelines 2024: Asthma Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Formoterol'],
        'evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': ['cardiac'],
            'qt_prolongation': True,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['ECG'],
            'look_alike_sound_alike': []
        },
        'guideline_tags': [
            'FDA Black Box Warning - KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen.',
            'ISMP High Alert Medications',
            'GINA Guidelines 2024 - Asthma Management - LABA must be combined with ICS',
            'AHA/ACC Guidelines - Cardiovascular monitoring with beta-2 agonists'
        ]},
    "Indacaterol": {'group': 'Respiratory - Long-acting Beta-2 Agonist (LABA)',
        'vietnamese_name': 'Indacaterol, Onbrez Breezhaler, Arcapta Neohaler',
        'administration': ['Inhalation (DPI)'], 'indications': [
        'COPD (phòng ngừa, đơn trị hoặc kết hợp với LAMA)',
        'Hen phế quản (phòng ngừa, phải dùng với ICS)'],
        'contraindications': ['Dị ứng indacaterol',
        'Nhịp tim nhanh nặng', 'Hen phế quản cấp (không dùng đơn độc)'],
        'dosage': {'adult_inhalation': '75-150mcg x 1 lần/ngày', 'notes':
        'Tác dụng kéo dài 24 giờ. Dùng 1 lần/ngày (thuận tiện hơn salmeterol/formoterol). PHẢI dùng kết hợp với ICS cho hen phế quản'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Tim đập nhanh', 'Run cơ',
        'Đau đầu', 'Ho (thường gặp khi bắt đầu)', 'Co thắt phế quản nghịch lý (hiếm)',
        'Loạn nhịp tim (hiếm)'], 'interactions': [
        'Beta-blocker: đối kháng tác dụng', 'Theophylline: tăng tác dụng phụ'],
        'pregnancy': 'C', 'mechanism_of_action':
        'Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng rất dài (24 giờ) do liên kết chặt với receptor, giải phóng chậm. Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch. Khác với salmeterol và formoterol (tác dụng 12 giờ), indacaterol có tác dụng 24 giờ → dùng 1 lần/ngày, thuận tiện hơn. Giảm phóng thích chất trung gian gây viêm từ mast cells. Dùng để phòng ngừa, không dùng để cắt cơn (tác dụng chậm).'
        , 'monitoring': [
        'Nhịp tim, huyết áp (đặc biệt khi bắt đầu điều trị)',
        'Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa',
        'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp',
        'Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)',
        'Tần suất dùng SABA (nếu tăng → cần đánh giá lại điều trị)'],
        'precautions': [
        'PHẢI dùng kết hợp với ICS (inhaled corticosteroid) cho hen phế quản - không bao giờ dùng đơn độc cho hen'
        'Không dùng để cắt cơn (tác dụng chậm, không hiệu quả) - cần có SABA để cắt cơn'
        , 'Không dùng đơn độc cho hen phế quản cấp - nguy cơ tăng tử vong',
        'Tránh dùng với beta-blocker (đối kháng tác dụng)',
        'Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)'
        , 'Dùng 1 lần/ngày (thuận tiện hơn salmeterol/formoterol cần 2 lần/ngày)',
        'Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng',
        'Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị và tăng ICS',
        'Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị'],
        'pharmacokinetics': {'half_life': '45.5-126 giờ (rất dài)',
        'onset': '5 phút (nhanh)', 'duration': '24 giờ (rất dài)',
        'protein_binding': '94-96%', 'clearance':
        'Gan (chuyển hóa qua UGT1A1, CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. DPI: bảo quản trong bao bì gốc. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings':
        'KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen. Không dùng để cắt cơn hen cấp (tác dụng chậm). Chỉ dùng để phòng ngừa và phải luôn có SABA để cắt cơn.'
        , 'drug_interactions': {'major': [{'drug':
        'Beta-blockers (không chọn lọc: Propranolol, Nadolol)', 'mechanism':
        'Đối kháng tác dụng beta-2, chặn tác dụng giãn phế quản của indacaterol',
        'effect':
        'Đối kháng tác dụng giãn phế quản, có thể gây co thắt phế quản nặng, suy hô hấp'
        , 'management':
        'TRÁNH DÙNG với beta-blocker không chọn lọc. Nếu bệnh nhân cần beta-blocker, dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng. Theo dõi chặt chẽ đáp ứng phế quản.'
        }, {'drug': 'Theophylline', 'mechanism':
        'Cả hai đều kích thích beta-adrenergic, có thể tăng tác dụng phụ và độc tính'
        , 'effect':
        'Tăng tác dụng phụ (run, tim đập nhanh, loạn nhịp), tăng nguy cơ độc tính theophylline'
        , 'management':
        'Theo dõi nồng độ theophylline. Theo dõi nhịp tim và triệu chứng. Có thể cần giảm liều theophylline.'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng với indacaterol hoặc các thành phần khác',
        'Nhịp tim nhanh nặng không kiểm soát (>120 bpm)',
        'Rối loạn nhịp tim nặng (rung nhĩ, rung thất không kiểm soát)',
        'Hen phế quản cấp (không dùng đơn độc, không dùng để cắt cơn)'], 'tương_đối': [
        'Bệnh tim mạch (suy tim, bệnh mạch vành) - thận trọng, theo dõi chặt chẽ',
        'Tăng huyết áp không kiểm soát - có thể tăng huyết áp',
        'Loạn nhịp tim nhẹ - có thể làm nặng',
        'Đái tháo đường - có thể tăng đường huyết',
        'Hạ kali máu - có thể làm nặng',
        'Cường giáp - tăng nhạy cảm với catecholamine']},
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Indacaterol là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Indacaterol được sử dụng trong thai kỳ để điều trị COPD và có vẻ an toàn. Hen phế quản không kiểm soát có thể gây nguy hiểm cho cả mẹ và thai nhi (thiếu oxy, suy thai). Indacaterol có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng PHẢI dùng kết hợp với ICS. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Indacaterol bài tiết ít vào sữa mẹ. Nồng độ trong sữa mẹ rất thấp do hấp thu toàn thân ít từ dạng hít. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'}},
        'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe':
        'Thận trọng - indacaterol chuyển hóa qua gan (UGT1A1, CYP3A4), có thể tích lũy ở suy gan nặng'
        , 'notes':
        'Indacaterol chuyển hóa qua UGT1A1 và CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ nhịp tim và tác dụng phụ. Có thể cần giảm liều.'
        }, 'overdose_management': {'symptoms': [
        'Nhịp tim nhanh nghiêm trọng (>150 bpm)', 'Run cơ nặng',
        'Loạn nhịp tim (rung nhĩ, rung thất)', 'Đau ngực', 'Khó thở nặng',
        'Co thắt phế quản nghịch lý', 'Hạ kali máu nghiêm trọng',
        'Tăng đường huyết', 'Kích động, lo âu', 'Đau đầu nặng'], 'antidote':
        'Không có antidote đặc hiệu. Beta-blocker chọn lọc beta-1 (atenolol, metoprolol) có thể được dùng để đối kháng tác dụng tim mạch, nhưng thận trọng vì có thể làm nặng co thắt phế quản.'
        , 'treatment': ['Ngừng ngay indacaterol',
        'Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)',
        'Theo dõi nhịp tim, huyết áp, ECG liên tục',
        'Điều trị loạn nhịp tim nếu có (theo protocol)',
        'Bổ sung kali nếu hạ kali máu', 'Điều trị tăng đường huyết nếu cần',
        'Nếu có co thắt phế quản nghịch lý: dùng ipratropium hoặc corticosteroid, tránh dùng SABA'
        , 'Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)',
        'Theo dõi và điều trị triệu chứng'], 'monitoring':
        'Theo dõi liên tục: nhịp tim, huyết áp, ECG, SpO2, kali máu, đường huyết, đáp ứng phế quản. Theo dõi ít nhất 24-48 giờ do thời gian bán thải rất dài (45.5-126 giờ).'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Beta-blocker chọn lọc beta-1 (Atenolol, Metoprolol)', 'mechanism':
        'Đối kháng tác dụng beta-adrenergic, giảm tác dụng tim mạch',
        'indication': 'Quá liều gây nhịp tim nhanh nghiêm trọng, loạn nhịp tim',
        'caution':
        'Thận trọng vì có thể làm nặng co thắt phế quản. Chỉ dùng khi tác dụng tim mạch nghiêm trọng và có hỗ trợ hô hấp sẵn sàng.'
        }], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Beta-blocker chọn lọc beta-1 có thể được dùng để đối kháng tác dụng tim mạch nhưng thận trọng.'
        }, 'administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dùng dạng hít DPI (Breezhaler/Neohaler). Mở nắp, đặt capsule vào buồng, đóng nắp, nhấn nút để đâm thủng capsule, hít sâu và giữ hơi thở 10 giây.'
        , 'timing':
        'Dùng 1 lần/ngày, tốt nhất vào buổi sáng, cách nhau 24 giờ. Thuận tiện hơn salmeterol/formoterol (cần 2 lần/ngày).'
        , 'with_ics':
        'PHẢI dùng kết hợp với ICS (inhaled corticosteroid) cho hen phế quản. Có thể dùng riêng hoặc dùng dạng fixed-dose combination.'
        , 'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và tránh nấm miệng (đặc biệt nếu dùng với ICS).'
        , 'notes':
        'Không dùng để cắt cơn (tác dụng chậm). Luôn có SABA (salbutamol) sẵn sàng để cắt cơn. Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị.'
        }},         'references': {'primary_sources': [
        'FDA Label: Arcapta Neohaler (Indacaterol)',
        'UpToDate: Long-acting beta-2 agonists in asthma and COPD',
        'GINA Guidelines 2024: Asthma Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Indacaterol'],
        'evidence_level': 'High - FDA approved, multiple RCTs, clinical guidelines'},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': ['cardiac'],
            'qt_prolongation': True,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['ECG'],
            'look_alike_sound_alike': []
        },
        'guideline_tags': [
            'FDA Black Box Warning - KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen.',
            'ISMP High Alert Medications',
            'GINA Guidelines 2024 - Asthma Management - LABA must be combined with ICS',
            'GOLD Guidelines 2024 - COPD Management'
        ]},
    "Olodaterol": {'group': 'Respiratory - Long-acting Beta-2 Agonist (LABA)',',
"pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        'vietnamese_name': 'Olodaterol, Striverdi', 'administration': [
        'Inhalation'], 'indications': [
        'COPD (phòng ngừa)', 'Hen phế quản (phải dùng với ICS)'],
        'contraindications': ['Dị ứng', 'Nhịp tim nhanh nặng',
        'Hen phế quản cấp (không dùng đơn độc)'], 'dosage': {'adult_inhalation':
        '5mcg x 1 lần/ngày', 'notes':
        'Dùng 1 lần/ngày. PHẢI dùng kết hợp với ICS cho hen. Tác dụng kéo dài 24 giờ'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Tim đập nhanh', 'Run cơ',
        'Đau đầu', 'Co thắt phế quản nghịch lý (hiếm)', 'Loạn nhịp tim (hiếm)'],
        'interactions': ['Beta-blocker: đối kháng tác dụng',
        'Theophylline: tăng tác dụng phụ'],
        'mechanism_of_action':
        'Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng dài (24 giờ) do liên kết chặt với receptor và thời gian bán thải dài. Chọn lọc beta-2 cao hơn các LABA khác, ít tác dụng tim mạch hơn. Dùng 1 lần/ngày, tiện lợi hơn các LABA khác (2 lần/ngày). Dùng để phòng ngừa, không dùng để cắt cơn.'
        , 'monitoring': ['Nhịp tim, huyết áp (đặc biệt khi bắt đầu điều trị)',
        'Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa',
        'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp',
        'Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)',
        'Tần suất dùng SABA (nếu tăng → cần đánh giá lại điều trị)'], 'precautions': [
        'PHẢI dùng kết hợp với ICS (inhaled corticosteroid) cho hen phế quản - không bao giờ dùng đơn độc'
        'Không dùng để cắt cơn (tác dụng chậm) - cần có SABA để cắt cơn'
        , 'Không dùng đơn độc cho hen phế quản cấp - nguy cơ tăng tử vong',
        'Tránh dùng với beta-blocker (đối kháng tác dụng)',
        'Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp',
        'Dùng đều đặn 1 lần/ngày (tiện lợi hơn các LABA khác)',
        'Rửa miệng sau khi dùng dạng hít để giảm kích ứng',
        'Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị'], 'pharmacokinetics': {
        'half_life': '45 giờ (rất dài)', 'onset': '5 phút', 'duration': '24 giờ (dài nhất trong các LABA)',
        'protein_binding': '60%', 'clearance':
        'Gan (chuyển hóa qua UGT, CYP2C8), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh.'
        , 'black_box_warnings':
        'KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen.'
        , 'drug_interactions': {'major': [{'drug':
        'Beta-blockers (không chọn lọc)', 'mechanism':
        'Đối kháng tác dụng beta-2', 'effect':
        'Đối kháng tác dụng giãn phế quản', 'management':
        'TRÁNH DÙNG với beta-blocker không chọn lọc.'}, {'drug': 'Theophylline', 'mechanism': 'Cả hai đều kích thích beta-adrenergic', 'effect':
        'Tăng tác dụng phụ', 'management':
        'Theo dõi nồng độ theophylline và nhịp tim.'}], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng với olodaterol', 'Nhịp tim nhanh nặng không kiểm soát',
        'Hen phế quản cấp (không dùng đơn độc)'], 'tương_đối': [
        'Bệnh tim mạch - thận trọng', 'Tăng huyết áp không kiểm soát',
        'Loạn nhịp tim nhẹ - có thể làm nặng']}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Olodaterol là thuốc phân loại C. Có thể dùng khi lợi ích vượt quá nguy cơ, nhưng PHẢI dùng kết hợp với ICS cho hen.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Olodaterol bài tiết ít vào sữa mẹ. Có thể dùng an toàn khi cho con bú.'
        , 'recommendation': 'Có thể dùng khi cho con bú.'}}, 'hepatic_adjustment': {
        'mild': 'Không đổi', 'moderate': 'Không đổi', 'severe':
        'Thận trọng - olodaterol chuyển hóa qua gan, có thể tích lũy ở suy gan nặng'
        , 'notes': 'Theo dõi chặt chẽ nhịp tim và tác dụng phụ ở suy gan nặng.'},
        'overdose_management': {'symptoms': [
        'Nhịp tim nhanh nghiêm trọng', 'Run cơ nặng', 'Loạn nhịp tim',
        'Co thắt phế quản nghịch lý', 'Hạ kali máu nghiêm trọng'], 'antidote':
        'Không có antidote đặc hiệu', 'treatment': [
        'Ngừng ngay olodaterol', 'Hỗ trợ hô hấp nếu cần',
        'Theo dõi nhịp tim, huyết áp, ECG liên tục',
        'Điều trị loạn nhịp tim nếu có', 'Bổ sung kali nếu hạ kali máu'],
        'monitoring':
        'Theo dõi liên tục: nhịp tim, huyết áp, ECG, SpO2, kali máu. Theo dõi ít nhất 24-48 giờ do thời gian bán thải dài (45 giờ).'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Beta-blocker chọn lọc beta-1', 'mechanism':
        'Đối kháng tác dụng beta-adrenergic', 'indication':
        'Quá liều gây nhịp tim nhanh nghiêm trọng', 'caution':
        'Thận trọng vì có thể làm nặng co thắt phế quản.'}], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ.'},
        'administration_instructions': {'oral': None, 'iv': None, 'inhalation': {
        'technique':
        'Dùng dạng hít (DPI). Hít sâu và giữ hơi thở 10 giây.',
        'timing': 'Dùng 1 lần/ngày (tiện lợi hơn các LABA khác).',
        'with_ics':
        'PHẢI dùng kết hợp với ICS cho hen phế quản.',
        'after_use': 'Súc miệng sau khi dùng.',
        'notes': 'Không dùng để cắt cơn. Luôn có SABA sẵn sàng.'}},
        'references': {'primary_sources': [
        'FDA Label: Striverdi (Olodaterol)',
        'UpToDate: Long-acting beta-2 agonists in COPD',
        'GOLD Guidelines 2024: COPD Management'],
        'evidence_level': 'High - FDA approved, clinical guidelines'},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': ['cardiac'],
            'qt_prolongation': True,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['ECG'],
            'look_alike_sound_alike': []
        },
        'guideline_tags': [
            'FDA Black Box Warning - KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen.',
            'ISMP High Alert Medications',
            'GINA Guidelines 2024 - Asthma Management - LABA must be combined with ICS',
            'GOLD Guidelines 2024 - COPD Management'
        ]},
    "Salmeterol": {'group': 'Respiratory - Long-acting Beta-2 Agonist (LABA)',',
"pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        'vietnamese_name': 'Salmeterol, Serevent', 'administration': [
        'Inhalation'], 'indications': [
        'Hen phế quản (phòng ngừa, phải dùng với ICS)', 'COPD (phòng ngừa)',
        'Co thắt phế quản ban đêm', 'Dự phòng co thắt do vận động'],
        'contraindications': ['Dị ứng', 'Nhịp tim nhanh nặng',
        'Hen phế quản cấp (không dùng đơn độc)'], 'dosage': {'adult_inhalation':
        '50mcg x 2 lần/ngày (sáng và tối)', 'notes':
        'PHẢI dùng kết hợp với ICS. Không dùng đơn độc cho hen. Tác dụng kéo dài 12 giờ'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Tim đập nhanh', 'Run cơ',
        'Đau đầu', 'Co thắt phế quản nghịch lý (hiếm)', 'Loạn nhịp tim (hiếm)'],
        'interactions': ['Beta-blocker: đối kháng tác dụng',
        'Theophylline: tăng tác dụng phụ'],
        'mechanism_of_action':
        'Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng dài (12 giờ) do liên kết chặt với receptor, giải phóng chậm. Chọn lọc beta-2 hơn beta-1 nhưng vẫn có tác dụng tim mạch. Giảm phóng thích chất trung gian gây viêm từ mast cells. Dùng để phòng ngừa, không dùng để cắt cơn (tác dụng chậm).'
        , 'monitoring': ['Nhịp tim, huyết áp (đặc biệt khi bắt đầu điều trị)',
        'Đáp ứng phế quản (peak flow, FEV1) - đánh giá hiệu quả phòng ngừa',
        'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp',
        'Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm)',
        'Tần suất dùng SABA (nếu tăng → cần đánh giá lại điều trị)'],
        'precautions': [
        'PHẢI dùng kết hợp với ICS (inhaled corticosteroid) - không bao giờ dùng đơn độc cho hen phế quản'
        'Không dùng để cắt cơn (tác dụng chậm, không hiệu quả) - cần có SABA để cắt cơn'
        , 'Không dùng đơn độc cho hen phế quản cấp - nguy cơ tăng tử vong',
        'Tránh dùng với beta-blocker (đối kháng tác dụng)',
        'Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)'
        , 'Dùng đều đặn 2 lần/ngày (sáng và tối) để phòng ngừa',
        'Rửa miệng sau khi dùng dạng hít để giảm kích ứng và nấm miệng',
        'Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị và tăng ICS',
        'Nếu không đáp ứng → cần đánh giá lại chẩn đoán và điều trị'],
        'pharmacokinetics': {'half_life': '5.5 giờ (dài hơn salbutamol)',
        'onset': '15-30 phút (chậm hơn SABA)', 'duration': '12 giờ (dài)',
        'protein_binding': '96%', 'clearance':
        'Gan (chuyển hóa qua CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh nhiệt độ cao, tránh ánh sáng trực tiếp. Không làm lạnh. Kiểm tra hạn sử dụng định kỳ.'
        , 'black_box_warnings':
        'KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen. Không dùng để cắt cơn hen cấp (tác dụng chậm). Chỉ dùng để phòng ngừa và phải luôn có SABA để cắt cơn.'
        , 'drug_interactions': {'major': [{'drug':
        'Beta-blockers (không chọn lọc: Propranolol, Nadolol)', 'mechanism':
        'Đối kháng tác dụng beta-2, chặn tác dụng giãn phế quản của salmeterol',
        'effect':
        'Đối kháng tác dụng giãn phế quản, có thể gây co thắt phế quản nặng, suy hô hấp'
        , 'management':
        'TRÁNH DÙNG với beta-blocker không chọn lọc. Nếu bệnh nhân cần beta-blocker, dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng. Theo dõi chặt chẽ đáp ứng phế quản.'
        }, {'drug': 'Theophylline', 'mechanism':
        'Cả hai đều kích thích beta-adrenergic, có thể tăng tác dụng phụ và độc tính'
        , 'effect':
        'Tăng tác dụng phụ (run, tim đập nhanh, loạn nhịp), tăng nguy cơ độc tính theophylline'
        , 'management':
        'Theo dõi nồng độ theophylline. Theo dõi nhịp tim và triệu chứng. Có thể cần giảm liều theophylline.'
        }, {'drug': 'Digoxin', 'mechanism':
        'Salmeterol có thể gây hạ kali máu và tăng nhịp tim, tăng nguy cơ độc tính digoxin'
        , 'effect':
        'Tăng nguy cơ loạn nhịp tim, tăng độc tính digoxin (đặc biệt khi hạ kali máu)'
        , 'management':
        'Theo dõi nồng độ digoxin và kali máu. Theo dõi ECG nếu có triệu chứng. Có thể cần điều chỉnh liều digoxin.'
        }, {'drug': 'Diuretics (Furosemide, Thiazide)', 'mechanism':
        'Cả hai đều có thể gây hạ kali máu, tăng nguy cơ hạ kali máu nghiêm trọng',
        'effect':
        'Tăng nguy cơ hạ kali máu nghiêm trọng, loạn nhịp tim, yếu cơ',
        'management':
        'Theo dõi kali máu thường xuyên. Bổ sung kali nếu cần. Có thể cần điều chỉnh liều diuretic.'
        }], 'moderate': [{'drug': 'Tricyclic antidepressants (TCA)', 'mechanism':
        'TCA tăng nhạy cảm với catecholamine, có thể tăng tác dụng tim mạch',
        'effect': 'Tăng nhịp tim, tăng huyết áp (nhẹ)', 'management':
        'Theo dõi nhịp tim và huyết áp. Không cần điều chỉnh liều thường quy.'}
        ]}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng với salmeterol hoặc các thành phần khác',
        'Nhịp tim nhanh nặng không kiểm soát (>120 bpm)',
        'Rối loạn nhịp tim nặng (rung nhĩ, rung thất không kiểm soát)',
        'Hen phế quản cấp (không dùng đơn độc, không dùng để cắt cơn)'],
        'tương_đối': [
        'Bệnh tim mạch (suy tim, bệnh mạch vành) - thận trọng, theo dõi chặt chẽ',
        'Tăng huyết áp không kiểm soát - có thể tăng huyết áp',
        'Loạn nhịp tim nhẹ - có thể làm nặng',
        'Đái tháo đường - có thể tăng đường huyết',
        'Hạ kali máu - có thể làm nặng',
        'Cường giáp - tăng nhạy cảm với catecholamine',
        'Dùng với digoxin - tăng nguy cơ loạn nhịp',
        'Dùng với theophylline - tăng tác dụng phụ']}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Salmeterol là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Salmeterol được sử dụng trong thai kỳ để điều trị hen và có vẻ an toàn. Hen phế quản không kiểm soát có thể gây nguy hiểm cho cả mẹ và thai nhi (thiếu oxy, suy thai). Salmeterol có thể được dùng khi lợi ích vượt quá nguy cơ, nhưng PHẢI dùng kết hợp với ICS. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Salmeterol bài tiết ít vào sữa mẹ. Nồng độ trong sữa mẹ rất thấp do hấp thu toàn thân ít từ dạng hít. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Dạng hít được ưu tiên để giảm tác dụng toàn thân.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate': 'Không đổi',
        'severe':
        'Thận trọng - salmeterol chuyển hóa qua gan (CYP3A4), có thể tích lũy ở suy gan nặng'
        , 'notes':
        'Salmeterol chuyển hóa qua CYP3A4 ở gan. Ở suy gan nặng, có thể tích lũy và tăng tác dụng phụ. Theo dõi chặt chẽ nhịp tim và tác dụng phụ. Có thể cần giảm liều hoặc tăng khoảng cách giữa các liều.'
        }, 'overdose_management': {'symptoms': [
        'Nhịp tim nhanh nghiêm trọng (>150 bpm)', 'Run cơ nặng',
        'Loạn nhịp tim (rung nhĩ, rung thất)', 'Đau ngực', 'Khó thở nặng',
        'Co thắt phế quản nghịch lý', 'Hạ kali máu nghiêm trọng',
        'Tăng đường huyết', 'Kích động, lo âu', 'Đau đầu nặng'], 'antidote':
        'Không có antidote đặc hiệu. Beta-blocker chọn lọc beta-1 (atenolol, metoprolol) có thể được dùng để đối kháng tác dụng tim mạch, nhưng thận trọng vì có thể làm nặng co thắt phế quản.'
        , 'treatment': ['Ngừng ngay salmeterol',
        'Hỗ trợ hô hấp nếu cần (oxy, thở máy nếu suy hô hấp)',
        'Theo dõi nhịp tim, huyết áp, ECG liên tục',
        'Điều trị loạn nhịp tim nếu có (theo protocol)',
        'Bổ sung kali nếu hạ kali máu', 'Điều trị tăng đường huyết nếu cần',
        'Nếu có co thắt phế quản nghịch lý: dùng ipratropium hoặc corticosteroid, tránh dùng SABA'
        , 'Hỗ trợ tim mạch nếu cần (IV fluids, vasopressors nếu hạ huyết áp)',
        'Theo dõi và điều trị triệu chứng'], 'monitoring':
        'Theo dõi liên tục: nhịp tim, huyết áp, ECG, SpO2, kali máu, đường huyết, đáp ứng phế quản. Theo dõi ít nhất 12-24 giờ do thời gian bán thải dài (5.5 giờ).'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Beta-blocker chọn lọc beta-1 (Atenolol, Metoprolol)', 'mechanism':
        'Đối kháng tác dụng beta-adrenergic, giảm tác dụng tim mạch',
        'indication': 'Quá liều gây nhịp tim nhanh nghiêm trọng, loạn nhịp tim',
        'caution':
        'Thận trọng vì có thể làm nặng co thắt phế quản. Chỉ dùng khi tác dụng tim mạch nghiêm trọng và có hỗ trợ hô hấp sẵn sàng.'
        }], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Beta-blocker chọn lọc beta-1 có thể được dùng để đối kháng tác dụng tim mạch nhưng thận trọng.'
        }, 'administration_instructions': {'oral': None, 'iv': None,
        'inhalation': {'technique':
        'Dùng dạng hít (MDI hoặc DPI). Lắc kỹ trước khi dùng (nếu MDI). Hít sâu và giữ hơi thở 10 giây. Đợi 30-60 giây trước khi dùng liều thứ hai (nếu cần).'
        , 'timing':
        'Dùng 2 lần/ngày (sáng và tối), cách nhau khoảng 12 giờ. Dùng đều đặn hàng ngày, không phải khi cần.'
        , 'with_ics':
        'PHẢI dùng kết hợp với ICS (inhaled corticosteroid). Có thể dùng riêng hoặc dùng dạng fixed-dose combination (Seretide/Advair: fluticasone + salmeterol).'
        , 'after_use':
        'Súc miệng và súc họng sau mỗi lần dùng để giảm kích ứng và tránh nấm miệng (đặc biệt nếu dùng với ICS).'
        , 'notes':
        'Không dùng để cắt cơn (tác dụng chậm). Luôn có SABA (salbutamol) sẵn sàng để cắt cơn. Nếu cần dùng SABA thường xuyên → cần đánh giá lại điều trị.'
        }},         'references': {'primary_sources': [
        'FDA Label: Serevent (Salmeterol)',
        'UpToDate: Long-acting beta-2 agonists in asthma',
        'GINA Guidelines 2024: Asthma Management',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        'Micromedex: Salmeterol'],
        'evidence_level':
        'High - FDA approved, multiple RCTs, clinical guidelines'},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': ['cardiac'],
            'qt_prolongation': True,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['ECG'],
            'look_alike_sound_alike': []
        },
        'guideline_tags': [
            'FDA Black Box Warning - KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - phải dùng kết hợp với ICS. Dùng đơn độc LABA có thể tăng nguy cơ tử vong do hen.',
            'ISMP High Alert Medications',
            'GINA Guidelines 2024 - Asthma Management - LABA must be combined with ICS',
            'AHA/ACC Guidelines - Cardiovascular monitoring with beta-2 agonists'
        ]},
    "Vilanterol": {'group': 'Respiratory - Long-acting Beta-2 Agonist (LABA)',',
"pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        'vietnamese_name': 'Vilanterol, Breo Ellipta', 'administration': [
        'Inhalation'], 'indications': [
        'COPD (phòng ngừa)', 'Hen phế quản (phải dùng với ICS)'],
        'contraindications': ['Dị ứng', 'Nhịp tim nhanh nặng',
        'Hen phế quản cấp (không dùng đơn độc)'], 'dosage': {'adult_inhalation':
        '25mcg x 1 lần/ngày', 'notes':
        'Dùng 1 lần/ngày. Chỉ có dạng fixed-dose combination với fluticasone (Breo Ellipta). Tác dụng kéo dài 24 giờ'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Tim đập nhanh', 'Run cơ',
        'Đau đầu', 'Nấm miệng (do ICS)', 'Co thắt phế quản nghịch lý (hiếm)'],
        'interactions': ['Beta-blocker: đối kháng tác dụng',
        'Ritonavir: tăng nồng độ fluticasone (tránh dùng)'],
        'mechanism_of_action':
        'Kích thích beta-2 adrenergic receptors ở cơ trơn phế quản, kích hoạt adenylate cyclase → tăng cAMP → giãn cơ trơn phế quản. Tác dụng dài (24 giờ) do liên kết chặt với receptor. Chọn lọc beta-2 cao. Chỉ có dạng fixed-dose combination với fluticasone furoate (ICS) trong Breo Ellipta. Dùng 1 lần/ngày, tiện lợi.'
        , 'monitoring': ['Nhịp tim, huyết áp (đặc biệt khi bắt đầu điều trị)',
        'Đáp ứng phế quản (peak flow, FEV1)',
        'Nấm miệng (do ICS) - súc miệng sau khi dùng',
        'Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng'], 'precautions': [
        'Chỉ có dạng fixed-dose combination với fluticasone (Breo Ellipta) - không có dạng đơn độc'
        'Không dùng để cắt cơn - cần có SABA để cắt cơn',
        'Súc miệng sau khi dùng để tránh nấm miệng (do ICS)',
        'TRÁNH DÙNG với ritonavir (tăng nồng độ fluticasone)',
        'Tránh dùng với beta-blocker (đối kháng tác dụng)',
        'Dùng đều đặn 1 lần/ngày'], 'pharmacokinetics': {
        'half_life': '11 giờ', 'onset': '5-15 phút', 'duration': '24 giờ',
        'protein_binding': '94%', 'clearance':
        'Gan (chuyển hóa qua CYP3A4), thận (thải trừ)'}, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp.'
        , 'black_box_warnings':
        'KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - chỉ có dạng kết hợp với ICS. TRÁNH DÙNG với ritonavir.'
        , 'drug_interactions': {'major': [{'drug': 'Ritonavir', 'mechanism':
        'Ức chế CYP3A4, tăng nồng độ fluticasone', 'effect':
        'Tăng nguy cơ ức chế trục HPA, hội chứng Cushing', 'management':
        'TRÁNH DÙNG với ritonavir.'}, {'drug': 'Beta-blockers (không chọn lọc)',
        'mechanism': 'Đối kháng tác dụng beta-2', 'effect':
        'Đối kháng tác dụng giãn phế quản', 'management':
        'TRÁNH DÙNG với beta-blocker không chọn lọc.'}], 'moderate': [], 'minor': []},
        'contraindications': {'tuyệt_đối': [
        'Dị ứng với vilanterol hoặc fluticasone',
        'Nhịp tim nhanh nặng không kiểm soát',
        'Dùng với ritonavir - chống chỉ định tuyệt đối'], 'tương_đối': [
        'Bệnh tim mạch - thận trọng', 'Tăng huyết áp không kiểm soát',
        'Lao phổi - cần điều trị lao trước']}, 'pregnancy_lactation': {
        'fda_category': 'C', 'pregnancy_details':
        'Vilanterol/fluticasone là thuốc phân loại C. Có thể dùng khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Vilanterol bài tiết ít vào sữa mẹ. Có thể dùng an toàn khi cho con bú.'
        , 'recommendation': 'Có thể dùng khi cho con bú.'}}, 'hepatic_adjustment': {
        'mild': 'Không đổi', 'moderate': 'Không đổi', 'severe':
        'Thận trọng - vilanterol chuyển hóa qua gan, có thể tích lũy ở suy gan nặng'
        , 'notes': 'Theo dõi chặt chẽ nhịp tim và tác dụng phụ ở suy gan nặng.'},
        'overdose_management': {'symptoms': [
        'Nhịp tim nhanh nghiêm trọng', 'Run cơ nặng', 'Loạn nhịp tim',
        'Co thắt phế quản nghịch lý'],
        'treatment': [
        'Ngừng ngay vilanterol/fluticasone', 'Hỗ trợ hô hấp nếu cần',
        'Theo dõi nhịp tim, huyết áp, ECG liên tục',
        'Điều trị loạn nhịp tim nếu có'], 'monitoring':
        'Theo dõi liên tục: nhịp tim, huyết áp, ECG, SpO2. Theo dõi ít nhất 12-24 giờ.'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Beta-blocker chọn lọc beta-1', 'mechanism':
        'Đối kháng tác dụng beta-adrenergic', 'indication':
        'Quá liều gây nhịp tim nhanh nghiêm trọng', 'caution':
        'Thận trọng vì có thể làm nặng co thắt phế quản.'}], 'notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ.'},
        'administration_instructions': {'oral': None, 'iv': None, 'inhalation': {
        'technique':
        'Dùng dạng hít (DPI - Ellipta). Hít sâu và giữ hơi thở 10 giây.',
        'timing': 'Dùng 1 lần/ngày (tiện lợi).',
        'with_ics':
        'Chỉ có dạng fixed-dose combination với fluticasone (Breo Ellipta).',
        'after_use': 'Súc miệng sau khi dùng để tránh nấm miệng.',
        'notes': 'Không dùng để cắt cơn. Luôn có SABA sẵn sàng.'}},
        'references': {'primary_sources': [
        'FDA Label: Breo Ellipta (Vilanterol/Fluticasone)',
        'UpToDate: Long-acting beta-2 agonists in COPD',
        'GOLD Guidelines 2024: COPD Management'],
        'evidence_level': 'High - FDA approved, clinical guidelines'},
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'icu_critical_care_only': False,
            'bleeding_risk': False,
            'organ_toxicity': ['cardiac'],
            'qt_prolongation': True,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['ECG'],
            'look_alike_sound_alike': []
        },
        'guideline_tags': [
            'FDA Black Box Warning - KHÔNG BAO GIỜ dùng đơn độc cho hen phế quản - chỉ có dạng kết hợp với ICS. TRÁNH DÙNG với ritonavir.',
            'ISMP High Alert Medications',
            'GINA Guidelines 2024 - Asthma Management - LABA must be combined with ICS',
            'GOLD Guidelines 2024 - COPD Management'
        ]}}


__all__ = ['LONG_ACTING_BETA_2_AGONIST_LABAS_DRUGS']
