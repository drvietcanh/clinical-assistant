"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Catecholamine (Alpha & Beta Agonist)s

CATECHOLAMINE_(ALPHA_&_BETA_AGONIST)S_DRUGS = {
    "Epinephrine": {'group': 'Emergency - Catecholamine (Alpha & Beta Agonist)',
        'vietnamese_name': 'Epinephrine, Adrenaline', 'administration': ['IV',
        'IM', 'SC', 'INH', 'IT'], 'indications': ['Ngừng tim (cardiac arrest)',
        'Sốc phản vệ (anaphylaxis)', 'Sốc (shock)',
        'Cơn hen nặng (IV/nebulizer)', 'Co thắt thanh quản'],
        'contraindications': ['Không có trong cấp cứu ngừng tim',
        'Sốc phản vệ: không có chống chỉ định tuyệt đối'], 'dosage': {
        'adult_cardiac_arrest_iv': '1mg IV mỗi 3-5 phút (hoặc 0.1mg/kg)',
        'adult_cardiac_arrest_it': '2-2.5mg IT', 'adult_anaphylaxis_im':
        '0.3-0.5mg IM (0.3-0.5ml 1:1000) ở đùi ngoài', 'adult_anaphylaxis_iv':
        '0.1-0.25mg IV bolus (pha 1mg trong 10ml = 0.1mg/ml)', 'adult_shock':
        '0.1-2mcg/kg/phút IV infusion', 'pediatric_cardiac_arrest':
        '0.01mg/kg (0.1ml/kg 1:10000) IV/IT mỗi 3-5 phút',
        'pediatric_anaphylaxis_im':
        '0.01mg/kg IM (0.01ml/kg 1:1000) ở đùi ngoài (tối đa 0.5mg)', 'notes':
        '1:1000 = 1mg/ml (dùng IM/SC), 1:10000 = 0.1mg/ml (dùng IV). Đùi ngoài cho anaphylaxis'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Tim đập nhanh',
        'Tăng huyết áp', 'Lo lắng, run tay', 'Đau đầu',
        'Nhồi máu cơ tim (với liều cao)', 'Rối loạn nhịp tim',
        'Hoại tử (nếu tiêm ngoài mạch)'], 'interactions': [
        'Beta-blockers: đối kháng tác dụng', 'MAOIs: tăng tác dụng',
        'Tricyclic antidepressants: tăng tác dụng',
        'Digoxin: tăng nguy cơ loạn nhịp'], 'pregnancy':
        'C - An toàn trong cấp cứu', 'mechanism_of_action':
        'Non-selective alpha và beta-adrenergic receptor agonist. Kích thích alpha-1 receptors → co mạch ngoại vi, tăng huyết áp. Kích thích beta-1 receptors → tăng nhịp tim, tăng co bóp cơ tim, tăng cung lượng tim. Kích thích beta-2 receptors → giãn phế quản, giãn mạch cơ xương. Trong ngừng tim: tăng áp lực tưới máu vành, tăng khả năng khử rung thành công.'
        , 'monitoring': ['Nhịp tim và huyết áp liên tục',
        'Điện tâm đồ (ECG) - theo dõi rối loạn nhịp',
        'Lactate máu (trong shock)', 'Đường huyết (tăng đường huyết)',
        'Dấu hiệu thiếu máu cục bộ (đau ngực, thay đổi ST)',
        'Tổn thương mô tại chỗ tiêm (hoại tử nếu tiêm ngoài mạch)'],
        'precautions': ['TUYỆT ĐỐI KHÔNG tiêm ngoài mạch (có thể gây hoại tử)',
        'Pha loãng đúng nồng độ: 1:1000 (1mg/ml) cho IM/SC, 1:10000 (0.1mg/ml) cho IV'
        , 'Trong anaphylaxis: tiêm IM ở đùi ngoài (hấp thu nhanh hơn cánh tay)',
        'Theo dõi sát trong 20 phút đầu (nguy cơ rối loạn nhịp, tăng huyết áp)',
        'Thận trọng ở bệnh nhân bệnh mạch vành (có thể gây nhồi máu cơ tim)',
        'Tránh dùng với thuốc chẹn beta (có thể gây tăng huyết áp nặng do không đối kháng alpha)'
        , 'Tiêm IV chậm, pha loãng để tránh tăng huyết áp đột ngột'],
        'pharmacokinetics': {'half_life': '2-3 phút (rất ngắn)', 'onset':
        'IV: ngay lập tức; IM: 5-10 phút', 'duration':
        '3-10 phút (IV), 10-30 phút (IM)', 'protein_binding':
        'Không đáng kể (catecholamine)', 'clearance':
        'Rất nhanh, bị bất hoạt bởi enzyme (MAO và COMT trong gan và mô)'},
        'storage':
        'Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Kiểm tra màu sắc trước dùng (hóa nâu = hỏng).'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, tiêm ngoài mạch có thể gây hoại tử mô. Liều cao có thể gây nhồi máu cơ tim, đột quỵ, hoặc tử vong.'
        , 'drug_interactions': {'major': [{'drug':
        'Beta-blockers (non-selective)', 'mechanism':
        'Beta-blockers đối kháng tác dụng beta của epinephrine, nhưng không đối kháng tác dụng alpha. Kết quả: tăng huyết áp nặng do chỉ còn tác dụng co mạch alpha, không có tác dụng giãn mạch beta-2.'
        , 'effect':
        'Tăng huyết áp nặng, nguy cơ đột quỵ, nhồi máu cơ tim, phù phổi cấp',
        'management':
        'TRÁNH dùng epinephrine với beta-blockers non-selective. Nếu cần trong cấp cứu: dùng liều thấp, theo dõi huyết áp chặt chẽ. Có thể cần thuốc giãn mạch (phentolamine) nếu tăng huyết áp nặng.'
        }, {'drug': 'MAOIs (Monoamine Oxidase Inhibitors)', 'mechanism':
        'MAOIs ức chế enzyme MAO chuyển hóa epinephrine, làm tăng nồng độ và thời gian tác dụng của epinephrine.'
        , 'effect':
        'Tăng tác dụng và thời gian tác dụng của epinephrine, tăng nguy cơ tăng huyết áp nặng, nhồi máu cơ tim, đột quỵ'
        , 'management':
        'GIẢM LIỀU epinephrine xuống 10-25% liều thông thường. Theo dõi huyết áp chặt chẽ. Trong cấp cứu: dùng liều thấp nhất có hiệu quả.'
        }, {'drug': 'Tricyclic Antidepressants (TCAs)', 'mechanism':
        'TCAs ức chế tái hấp thu norepinephrine, tăng nồng độ catecholamine, tăng tác dụng của epinephrine.'
        , 'effect':
        'Tăng tác dụng của epinephrine, tăng nguy cơ tăng huyết áp nặng, rối loạn nhịp tim'
        , 'management':
        'Thận trọng, giảm liều epinephrine. Theo dõi huyết áp và ECG chặt chẽ.'
        }], 'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Digoxin làm tăng nhạy cảm của cơ tim với catecholamine, tăng nguy cơ rối loạn nhịp tim.'
        , 'effect':
        'Tăng nguy cơ rối loạn nhịp tim (nhịp nhanh thất, rung thất), đặc biệt ở bệnh nhân digoxin độc tính'
        , 'management':
        'Thận trọng, theo dõi ECG chặt chẽ. Kiểm tra nồng độ digoxin nếu có thể. Tránh dùng epinephrine nếu có dấu hiệu digoxin độc tính.'
        }, {'drug': 'Alpha-blockers', 'mechanism':
        'Alpha-blockers đối kháng tác dụng alpha của epinephrine, có thể làm giảm hiệu quả điều trị sốc.'
        , 'effect': 'Giảm hiệu quả điều trị sốc, có thể cần liều cao hơn',
        'management':
        'Có thể cần tăng liều epinephrine. Theo dõi đáp ứng điều trị.'}],
        'minor': [{'drug': 'Beta-2 agonists (Salbutamol, Salmeterol)',
        'mechanism':
        'Cùng tác dụng beta-2, có thể tăng tác dụng giãn phế quản và tăng nhịp tim.'
        , 'effect': 'Tăng nhịp tim, run tay (nhẹ)', 'management':
        'Theo dõi nhịp tim. Không cần điều chỉnh liều thường quy.'}]},
        'contraindications': {'tuyệt_đối': [
        'Không có chống chỉ định tuyệt đối trong cấp cứu ngừng tim',
        'Dị ứng epinephrine (hiếm nhưng nguy hiểm)'], 'tương_đối': [
        'Bệnh mạch vành - tăng nguy cơ nhồi máu cơ tim, đau thắt ngực',
        'Tăng huyết áp nặng không kiểm soát - có thể làm tăng huyết áp hơn nữa',
        'Rối loạn nhịp tim nặng - có thể làm nặng rối loạn nhịp',
        'Đột quỵ gần đây - tăng nguy cơ tái phát',
        'Pheochromocytoma - tăng nguy cơ tăng huyết áp nặng, cơn tăng huyết áp',
        'Dùng với beta-blockers non-selective - tăng huyết áp nặng',
        'Dùng với MAOIs - tăng tác dụng, cần giảm liều',
        'Dùng với TCAs - tăng tác dụng, cần thận trọng',
        'Bệnh nhân cao tuổi - tăng nhạy cảm với tác dụng phụ',
        'Bệnh nhân có bệnh mạch máu ngoại biên - tăng nguy cơ thiếu máu cục bộ'
        ]}, 'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Epinephrine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Epinephrine có thể qua nhau thai và có thể gây co mạch, giảm tưới máu nhau thai. Tuy nhiên, trong cấp cứu (sốc phản vệ, ngừng tim), lợi ích cứu sống mẹ vượt quá nguy cơ cho thai nhi. Sốc phản vệ và ngừng tim có thể gây tử vong cho cả mẹ và thai nhi nếu không điều trị. Epinephrine được sử dụng trong cấp cứu ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Epinephrine có thời gian bán thải rất ngắn (2-3 phút) và bị chuyển hóa nhanh. Không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Epinephrine có thời gian bán thải rất ngắn và không bài tiết vào sữa mẹ.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Epinephrine chuyển hóa nhanh bởi MAO và COMT, nhưng không phụ thuộc vào chức năng gan.'
        , 'moderate': 'Không cần điều chỉnh liều.', 'severe':
        'Không cần điều chỉnh liều. Epinephrine chuyển hóa nhanh, không tích lũy ở suy gan.'
        , 'notes':
        'Epinephrine bị chuyển hóa nhanh bởi enzyme MAO và COMT trong gan và mô, nhưng không phụ thuộc vào chức năng gan. Không cần điều chỉnh liều ở bệnh nhân suy gan.'
        }, 'overdose_management': {'symptoms': [
        'Tăng huyết áp nặng (có thể >200/120 mmHg)',
        'Nhịp tim nhanh nặng (>150-200 bpm)', 'Nhồi máu cơ tim', 'Đột quỵ',
        'Phù phổi cấp', 'Rối loạn nhịp tim (rung nhĩ, rung thất)', 'Co giật',
        'Hoại tử mô (nếu tiêm ngoài mạch)'], 'antidote':
        'Không có antidote đặc hiệu. Có thể dùng thuốc giãn mạch (phentolamine, nitroglycerin) để đối kháng tác dụng alpha. Beta-blockers có thể đối kháng tác dụng beta nhưng nguy hiểm (tăng huyết áp nặng).'
        , 'treatment': ['Ngừng ngay epinephrine nếu đang truyền',
        'Theo dõi ECG và huyết áp liên tục', 'Nếu tăng huyết áp nặng:',
        '  - Phentolamine 5-10mg IV (đối kháng alpha, giảm huyết áp)',
        '  - Hoặc Nitroglycerin IV (giãn mạch, giảm huyết áp)',
        '  - Hoặc Labetalol (alpha + beta blocker) - thận trọng',
        'Nếu nhịp tim nhanh nặng:',
        '  - Beta-blocker (metoprolol, esmolol) - THẬN TRỌNG, chỉ dùng nếu không có tăng huyết áp nặng'
        , '  - Nếu có tăng huyết áp + nhịp nhanh: Labetalol',
        'Nếu nhồi máu cơ tim: Điều trị theo protocol nhồi máu cơ tim (aspirin, clopidogrel, statin, có thể cần can thiệp)'
        , 'Nếu đột quỵ: Điều trị theo protocol đột quỵ',
        'Nếu phù phổi cấp: Furosemide, nitroglycerin, hỗ trợ hô hấp',
        'Nếu rối loạn nhịp: Điều trị theo protocol rối loạn nhịp',
        'Nếu hoại tử mô (tiêm ngoài mạch):',
        '  - Phentolamine 5-10mg pha trong 10-15ml NS tiêm quanh vùng hoại tử (trong vòng 12 giờ)'
        , '  - Chườm ấm', '  - Có thể cần phẫu thuật nếu hoại tử nặng',
        'Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG trong ít nhất 2-4 giờ'
        ], 'monitoring':
        'Theo dõi ECG, huyết áp, nhịp tim liên tục trong ít nhất 2-4 giờ sau khi dùng. Theo dõi lâu hơn nếu có biến chứng (nhồi máu cơ tim, đột quỵ, rối loạn nhịp).'
        }, 'reversal_agents': {'available': True, 'agents': [{'agent':
        'Phentolamine', 'mechanism':
        'Alpha-blocker, đối kháng tác dụng alpha của epinephrine (co mạch, tăng huyết áp)'
        , 'indication':
        'Tăng huyết áp nặng do quá liều epinephrine, hoại tử mô do tiêm ngoài mạch'
        , 'dose':
        '5-10mg IV cho tăng huyết áp, 5-10mg pha trong 10-15ml NS tiêm quanh vùng hoại tử (trong vòng 12 giờ)'
        }, {'agent': 'Nitroglycerin', 'mechanism': 'Giãn mạch, giảm huyết áp',
        'indication': 'Tăng huyết áp nặng do quá liều epinephrine', 'dose':
        '5-10mcg/phút IV, tăng dần đến khi đạt huyết áp mục tiêu'}, {'agent':
        'Beta-blockers (thận trọng)', 'mechanism':
        'Đối kháng tác dụng beta của epinephrine (nhịp tim nhanh)',
        'indication':
        'Nhịp tim nhanh nặng do quá liều epinephrine (CHỈ dùng nếu không có tăng huyết áp nặng)'
        , 'dose':
        'Metoprolol 5mg IV hoặc Esmolol 0.5mg/kg IV bolus, sau đó 50-200mcg/kg/phút IV infusion'
        }]}, 'administration_instructions': {'oral': None, 'iv': {
        'reconstitution':
        'Pha loãng: 1mg epinephrine (1ml 1:1000) trong 9ml NS = 0.1mg/ml (1:10000). Hoặc dùng trực tiếp dung dịch 1:10000 nếu có.'
        , 'infusion_rate':
        'Cardiac arrest: 1mg IV bolus mỗi 3-5 phút. Anaphylaxis: 0.1-0.25mg IV bolus (pha loãng). Shock: 0.1-2mcg/kg/phút IV infusion (pha 1mg trong 250ml D5W = 4mcg/ml).'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],
        'incompatibility': [
        'Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion.'
        ], 'notes':
        'QUAN TRỌNG: 1) Pha đúng nồng độ: 1:1000 (1mg/ml) cho IM/SC, 1:10000 (0.1mg/ml) cho IV, 2) TUYỆT ĐỐI KHÔNG tiêm ngoài mạch (hoại tử), 3) Trong anaphylaxis: tiêm IM ở đùi ngoài (hấp thu nhanh hơn), 4) Theo dõi huyết áp và ECG chặt chẽ, 5) Kiểm tra màu sắc trước dùng (hóa nâu = hỏng).'
        }, 'im': {'reconstitution': 'Dùng trực tiếp dung dịch 1:1000 (1mg/ml).',
        'injection_site':
        'Đùi ngoài (vastus lateralis) - hấp thu nhanh nhất. Có thể dùng cánh tay nhưng hấp thu chậm hơn.'
        , 'notes':
        'Anaphylaxis: 0.3-0.5mg IM ở đùi ngoài. Trẻ em: 0.01mg/kg IM ở đùi ngoài (tối đa 0.5mg). Tiêm sâu vào cơ, không tiêm vào mỡ dưới da.'
        }, 'inhaled': {'reconstitution':
        'Dùng dung dịch 1:1000 (1mg/ml) pha trong 3-5ml NS cho nebulizer.',
        'dose':
        '0.5-1mg (0.5-1ml 1:1000) pha trong 3-5ml NS, khí dung mỗi 15-20 phút nếu cần.'
        , 'notes': 'Dùng trong cơn hen nặng. Theo dõi nhịp tim và huyết áp.'}},
        'references': {'primary_sources': ['FDA Drug Label - Epinephrine',
        'ACLS Guidelines 2020 - American Heart Association',
        'Anaphylaxis Guidelines - World Allergy Organization',
        'UpToDate - Epinephrine: Drug Information',
        'Medscape - Epinephrine Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Epinephrine Monograph',
        'Micromedex - Epinephrine Drug Information'], 'last_updated':
        '2025-02-03', 'evidence_level':
        'A - Dựa trên FDA drug labels, ACLS guidelines, anaphylaxis guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }}}

__all__ = ['CATECHOLAMINE_(ALPHA_&_BETA_AGONIST)S_DRUGS']
