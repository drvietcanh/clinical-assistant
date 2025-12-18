"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Catecholamine (Alpha & Beta Agonist)s

CATECHOLAMINE_ALPHA_BETA_AGONISTS_DRUGS = {
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
        }},
    
    "Norepinephrine": {
        "group": "Emergency - Catecholamine (Alpha & Beta Agonist)",
        "vietnamese_name": "Norepinephrine, Noradrenaline, Levophed",
        "administration": ["IV"],
        "indications": [
            "Sốc nhiễm khuẩn (septic shock)",
            "Sốc tim (cardiogenic shock)",
            "Sốc giảm thể tích (sau khi bù dịch)",
            "Hạ huyết áp nặng trong cấp cứu"
        ],
        "contraindications": [
            "Không có chống chỉ định tuyệt đối trong cấp cứu",
            "Thiếu máu cục bộ mô (nếu có thể tránh)"
        ],
        "dosage": {
            "adult_shock": "0.05-2 mcg/kg/phút IV infusion (khởi đầu 0.05-0.1 mcg/kg/phút)",
            "adult_septic_shock": "0.05-2 mcg/kg/phút IV infusion",
            "adult_cardiogenic_shock": "0.05-2 mcg/kg/phút IV infusion",
            "notes": "Pha 4mg trong 250ml D5W = 16 mcg/ml. Truyền qua đường tĩnh mạch trung tâm để tránh hoại tử nếu rò rỉ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tăng huyết áp",
            "Co mạch ngoại vi (giảm tưới máu mô)",
            "Hoại tử mô (nếu rò rỉ ngoài mạch)",
            "Rối loạn nhịp tim (hiếm)",
            "Tăng đường huyết",
            "Giảm tưới máu thận (với liều cao)"
        ],
        "interactions": [
            "MAOIs: tăng tác dụng",
            "TCAs: tăng tác dụng",
            "Beta-blockers: tăng huyết áp nặng"
        ],
        "pregnancy": "C - An toàn trong cấp cứu",
        "mechanism_of_action": "Chủ yếu alpha-adrenergic receptor agonist (alpha-1 và alpha-2), một số tác dụng beta-1. Kích thích alpha-1 receptors → co mạch ngoại vi mạnh, tăng huyết áp. Kích thích beta-1 receptors → tăng nhịp tim và co bóp cơ tim nhẹ. Không có tác dụng beta-2 (không giãn phế quản). Trong sốc: tăng huyết áp và tưới máu cơ quan quan trọng.",
        "monitoring": [
            "Huyết áp liên tục (arterial line nếu có thể)",
            "Nhịp tim và ECG",
            "Lactate máu (tưới máu mô)",
            "Đường huyết",
            "Tưới máu mô (da, thận, chi)",
            "Dấu hiệu hoại tử tại chỗ tiêm"
        ],
        "precautions": [
            "TUYỆT ĐỐI phải truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử nếu rò rỉ)",
            "Theo dõi tưới máu mô (da, thận) - có thể giảm với liều cao",
            "Bù dịch đầy đủ trước khi dùng (trừ sốc tim)",
            "Giảm liều khi huyết áp đã ổn định",
            "Theo dõi lactate để đánh giá tưới máu mô"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 phút (rất ngắn)",
            "onset": "Ngay lập tức sau khi bắt đầu truyền",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "Không đáng kể",
            "clearance": "Rất nhanh, bị bất hoạt bởi MAO và COMT"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Kiểm tra màu sắc trước dùng (hóa nâu = hỏng).",
        "black_box_warnings": "Hoại tử mô nếu rò rỉ ngoài mạch - phải truyền qua đường tĩnh mạch trung tâm.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Norepinephrine",
                "Surviving Sepsis Campaign Guidelines",
                "UpToDate - Norepinephrine: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Dopamine": {
        "group": "Emergency - Catecholamine (Alpha & Beta Agonist)",
        "vietnamese_name": "Dopamine, Intropin",
        "administration": ["IV"],
        "indications": [
            "Sốc (sau khi bù dịch)",
            "Hạ huyết áp nặng",
            "Suy thận cấp (liều thấp - renal dose)",
            "Suy tim cấp"
        ],
        "contraindications": [
            "Pheochromocytoma",
            "Rối loạn nhịp tim nặng",
            "Không dùng liều thấp cho suy thận (không có bằng chứng)"
        ],
        "dosage": {
            "adult_renal_dose": "1-3 mcg/kg/phút IV (tăng tưới máu thận - không khuyến cáo)",
            "adult_cardiac_dose": "3-10 mcg/kg/phút IV (tăng cung lượng tim)",
            "adult_vasopressor_dose": "10-20 mcg/kg/phút IV (tăng huyết áp)",
            "notes": "Pha 400mg trong 250ml D5W = 1600 mcg/ml. Tác dụng phụ thuộc liều."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Rối loạn nhịp tim",
            "Tăng huyết áp (liều cao)",
            "Co mạch ngoại vi (liều cao)",
            "Hoại tử mô (nếu rò rỉ)",
            "Buồn nôn, nôn"
        ],
        "interactions": [
            "MAOIs: tăng tác dụng",
            "TCAs: tăng tác dụng",
            "Beta-blockers: tăng huyết áp"
        ],
        "pregnancy": "C - An toàn trong cấp cứu",
        "mechanism_of_action": "Tác dụng phụ thuộc liều: Liều thấp (1-3 mcg/kg/phút): kích thích dopamine receptors → tăng tưới máu thận (không khuyến cáo, không có bằng chứng). Liều trung bình (3-10 mcg/kg/phút): kích thích beta-1 receptors → tăng nhịp tim, tăng co bóp cơ tim, tăng cung lượng tim. Liều cao (10-20 mcg/kg/phút): kích thích alpha-1 receptors → co mạch, tăng huyết áp.",
        "monitoring": [
            "Huyết áp liên tục",
            "Nhịp tim và ECG (rối loạn nhịp)",
            "Cung lượng tim (nếu có thể)",
            "Tưới máu mô",
            "Dấu hiệu hoại tử tại chỗ tiêm"
        ],
        "precautions": [
            "Truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử)",
            "Không dùng liều thấp cho suy thận (không có bằng chứng hiệu quả)",
            "Theo dõi rối loạn nhịp tim",
            "Bù dịch đầy đủ trước khi dùng",
            "Giảm liều khi huyết áp đã ổn định"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 phút (rất ngắn)",
            "onset": "Ngay lập tức",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "Không đáng kể",
            "clearance": "Rất nhanh, bị bất hoạt bởi MAO và COMT"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh.",
        "black_box_warnings": "Hoại tử mô nếu rò rỉ ngoài mạch. Không dùng liều thấp cho suy thận (không có bằng chứng).",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dopamine",
                "Surviving Sepsis Campaign Guidelines",
                "UpToDate - Dopamine: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Dobutamine": {
        "group": "Emergency - Catecholamine (Alpha & Beta Agonist)",
        "vietnamese_name": "Dobutamine, Dobutrex",
        "administration": ["IV"],
        "indications": [
            "Suy tim cấp",
            "Sốc tim (cardiogenic shock)",
            "Stress test tim (dobutamine stress echo)",
            "Sau phẫu thuật tim"
        ],
        "contraindications": [
            "Hẹp động mạch chủ nặng",
            "Rối loạn nhịp tim nặng",
            "Sốc giảm thể tích (chưa bù dịch)"
        ],
        "dosage": {
            "adult_heart_failure": "2.5-15 mcg/kg/phút IV infusion",
            "adult_cardiogenic_shock": "2.5-20 mcg/kg/phút IV infusion",
            "adult_stress_test": "5-40 mcg/kg/phút IV (tăng dần)",
            "notes": "Pha 250mg trong 250ml D5W = 1000 mcg/ml. Khởi đầu 2.5-5 mcg/kg/phút."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tăng nhịp tim",
            "Rối loạn nhịp tim",
            "Hạ huyết áp (do giãn mạch)",
            "Đau ngực",
            "Khó thở"
        ],
        "interactions": [
            "Beta-blockers: đối kháng tác dụng",
            "MAOIs: tăng tác dụng"
        ],
        "pregnancy": "C - An toàn trong cấp cứu",
        "mechanism_of_action": "Chủ yếu beta-1-adrenergic receptor agonist, một số tác dụng beta-2 và alpha-1. Kích thích beta-1 receptors → tăng nhịp tim, tăng co bóp cơ tim mạnh, tăng cung lượng tim. Kích thích beta-2 receptors → giãn mạch nhẹ. Kích thích alpha-1 receptors → co mạch nhẹ. Kết quả: tăng cung lượng tim, giảm áp lực đổ đầy tim, ít ảnh hưởng đến huyết áp.",
        "monitoring": [
            "Huyết áp liên tục",
            "Nhịp tim và ECG (rối loạn nhịp)",
            "Cung lượng tim (nếu có thể)",
            "Áp lực đổ đầy tim (CVP, PCWP)",
            "Dấu hiệu thiếu máu cục bộ (đau ngực)"
        ],
        "precautions": [
            "Bù dịch đầy đủ trước khi dùng (tránh hạ huyết áp)",
            "Theo dõi rối loạn nhịp tim",
            "Thận trọng ở bệnh nhân bệnh mạch vành",
            "Giảm liều khi cung lượng tim đã cải thiện",
            "Không dùng trong sốc giảm thể tích"
        ],
        "pharmacokinetics": {
            "half_life": "2 phút (rất ngắn)",
            "onset": "Ngay lập tức",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "Không đáng kể",
            "clearance": "Rất nhanh, bị bất hoạt bởi COMT"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, có thể gây rối loạn nhịp tim nặng.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dobutamine",
                "ACLS Guidelines",
                "UpToDate - Dobutamine: Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Vasopressin": {
        "group": "Emergency - Vasopressor (Non-catecholamine)",
        "vietnamese_name": "Vasopressin, Arginine vasopressin",
        "administration": ["IV"],
        "indications": [
            "Sốc nhiễm khuẩn (septic shock) cần vasopressor liều cao",
            "Sốc giãn mạch (vasodilatory shock) kháng catecholamine",
            "Hạ huyết áp nặng trong ICU (dùng kèm norepinephrine)"
        ],
        "contraindications": [
            "Thiếu máu cục bộ mô nặng (chi, ruột, tim) - thận trọng",
            "Sốc giảm thể tích chưa bù dịch đầy đủ"
        ],
        "dosage": {
            "adult_shock_fixed_dose": "0.03 units/phút IV liên tục (0.01–0.03 units/phút)",
            "adult_shock_high_dose": "0.04–0.06 units/phút IV (tránh vượt quá nếu không có chỉ định chuyên sâu)",
            "notes": "Dùng như thuốc bổ sung (add‑on) cho norepinephrine, KHÔNG thay thế hoàn toàn norepinephrine. Không titrate nhanh theo huyết áp như catecholamine."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Co mạch ngoại vi (lạnh đầu chi, tím đầu ngón)",
            "Thiếu máu cục bộ chi, ruột, cơ tim (liều cao, dùng kéo dài)",
            "Hạ natri máu (nếu dùng kéo dài)",
            "Đau đầu, buồn nôn"
        ],
        "interactions": [
            "Các vasopressor khác (norepinephrine, epinephrine, dopamine): tăng nguy cơ thiếu máu cục bộ chi",
            "Sodium bicarbonate: KHÔNG pha chung cùng line (môi trường kiềm làm giảm hiệu lực vasopressors)"
        ],
        "pregnancy": "C - Có thể dùng trong cấp cứu nếu lợi ích > nguy cơ",
        "mechanism_of_action": "Vasopressin là hormon nội sinh (arginine vasopressin). Kích thích V1a receptors trên cơ trơn mạch máu → co mạch mạnh, tăng huyết áp; kích thích V2 receptors tại ống góp thận → tăng tái hấp thu nước. Trong sốc nhiễm khuẩn, bệnh nhân thường thiếu tương đối vasopressin nội sinh, nên bổ sung liều thấp giúp phục hồi trương lực mạch mà không làm tăng nhịp tim.",
        "monitoring": [
            "Huyết áp động mạch (ưu tiên arterial line)",
            "Tưới máu chi (màu da, nhiệt độ, refill mao mạch)",
            "Dấu hiệu thiếu máu cục bộ ruột (đau bụng, chướng bụng, lactate tăng)",
            "Điện giải, đặc biệt natri máu",
            "Nước tiểu giờ (diuresis)"
        ],
        "precautions": [
            "Không dùng đơn độc liều cao để thay norepinephrine – chỉ dùng như thuốc bổ sung.",
            "Tránh vượt quá 0.06 units/phút trừ khi có chỉ định và theo dõi rất sát.",
            "Thận trọng ở bệnh nhân có bệnh mạch máu ngoại vi, bệnh mạch vành, nguy cơ thiếu máu cục bộ ruột.",
            "Bù dịch đầy đủ trước khi dùng (tránh sốc giảm thể tích).",
            "Dùng line truyền riêng, không pha chung với sodium bicarbonate."
        ],
        "pharmacokinetics": {
            "half_life": "10–20 phút",
            "onset": "Vài phút sau khi bắt đầu truyền",
            "duration": "Ngắn, cần truyền liên tục",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan, thận và phân hủy bởi peptidase."
        },
        "storage": "Bảo quản theo hướng dẫn chế phẩm (thường 2–8°C), tránh đông lạnh. Dung dịch đã pha: dùng trong thời gian khuyến cáo của nhà sản xuất, tránh ánh sáng trực tiếp.",
        "black_box_warnings": None,
        "references": {
            "primary_sources": [
                "Surviving Sepsis Campaign Guidelines 2021",
                "UpToDate - Vasopressin for vasodilatory shock",
                "FDA Drug Label - Vasopressin"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    }
}

__all__ = ['CATECHOLAMINE_ALPHA_BETA_AGONISTS_DRUGS']
