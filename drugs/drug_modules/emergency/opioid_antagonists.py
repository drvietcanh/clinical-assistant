"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Opioid Antagonists

OPIOID_ANTAGONISTS_DRUGS = {
    "Naloxone": {'group': 'Emergency - Opioid Antagonist', 'vietnamese_name':
        'Naloxone, Narcan', 'administration': ['IV', 'IM', 'SC', 'INH', 'IO'],
        'indications': ['Quá liều opioid (nghiện)', 'Ngộ độc opioid',
        'Đảo ngược tác dụng opioid sau phẫu thuật',
        'Đảo ngược tác dụng opioid trong ICU'], 'contraindications': [
        'Dị ứng naloxone'], 'dosage': {'adult_overdose':
        '0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút đến khi đáp ứng',
        'adult_reversal': '0.04-0.4mg IV titrate đến khi đáp ứng',
        'adult_infusion': '0.25-6.25mcg/kg/giờ IV (nếu cần duy trì)',
        'pediatric_overdose': '0.01mg/kg IV/IM/IO, lặp lại đến khi đáp ứng',
        'pediatric_infusion': '2.5-10mcg/kg/giờ IV', 'notes':
        'Tác dụng ngắn (20-90 phút), có thể cần lặp lại hoặc infusion. Theo dõi hội chứng cai'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': [
        'Hội chứng cai opioid (nếu bệnh nhân nghiện)', 'Hạ huyết áp',
        'Rối loạn nhịp tim', 'Co giật (hiếm)', 'Phù phổi (hiếm)'],
        'interactions': ['Opioids: đảo ngược tác dụng'], 'pregnancy':
        'C - An toàn', 'mechanism_of_action':
        'Opioid receptor antagonist cạnh tranh. Gắn với ái lực cao vào mu-opioid receptor (và kappa, delta receptors), đẩy opioid ra khỏi receptor, đảo ngược hoàn toàn tác dụng của opioid (ức chế hô hấp, an thần, giảm đau, miosis). Tác dụng rất nhanh (1-2 phút IV), nhưng thời gian tác dụng ngắn (30-90 phút) do bị chuyển hóa nhanh, trong khi nhiều opioid có thời gian tác dụng dài hơn → cần lặp lại liều hoặc dùng infusion.'
        , 'monitoring': ['Độ bão hòa oxy (SpO2) và nhịp thở liên tục',
        'Mức độ ý thức (GCS)',
        'Dấu hiệu hội chứng cai opioid (kích động, vã mồ hôi, tăng huyết áp, nhịp tim nhanh)'
        , 'Huyết áp và nhịp tim',
        'Dấu hiệu tái ngộ độc opioid (thở chậm lại, giảm ý thức) - đặc biệt quan trọng nếu opioid có thời gian tác dụng dài hơn naloxone'
        , 'Co giật (hiếm nhưng nguy hiểm)'], 'precautions': [
        'Thời gian tác dụng NGẮN (30-90 phút) - opioid có thể tác dụng trở lại sau khi naloxone hết tác dụng'
        ,
        'Theo dõi sát ít nhất 2-4 giờ sau khi dùng naloxone (nguy cơ tái ngộ độc)',
        'Ở bệnh nhân nghiện opioid: naloxone có thể gây hội chứng cai nặng (kích động, nôn, tăng huyết áp) - cần chuẩn bị xử trí'
        ,
        'Không dùng quá liều (tăng nguy cơ hội chứng cai nặng, không tăng hiệu quả)'
        , 'Nếu cần duy trì: dùng infusion thay vì bolus lặp lại',
        'Thận trọng ở bệnh nhân có tiền sử co giật (có thể gây co giật)',
        'Dùng liều thấp (0.04-0.4mg) khi đảo ngược tác dụng opioid sau phẫu thuật để tránh đảo ngược hoàn toàn giảm đau'
        ], 'pharmacokinetics': {'half_life': '30-90 phút (ngắn)', 'onset':
        '1-2 phút (IV), 2-5 phút (IM)', 'duration': '30-90 phút (tùy liều)',
        'protein_binding': '45%', 'clearance':
        'Gan (glucuronidation), thời gian bán thải ngắn hơn nhiều so với hầu hết opioid'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Có thể bảo quản ở nhiệt độ 2-8°C.'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, thời gian tác dụng ngắn có thể dẫn đến tái ngộ độc opioid nếu không theo dõi đúng. Hội chứng cai opioid có thể nguy hiểm ở bệnh nhân nghiện.'
        , 'drug_interactions': {'major': [{'drug':
        'Opioids (Morphine, Fentanyl, Heroin, Methadone, etc.)', 'mechanism':
        'Naloxone là opioid receptor antagonist cạnh tranh, đẩy opioid ra khỏi receptor, đảo ngược hoàn toàn tác dụng của opioid.'
        , 'effect':
        'Đảo ngược tác dụng opioid (ức chế hô hấp, an thần, giảm đau, miosis). Nếu opioid có thời gian tác dụng dài hơn naloxone → tái ngộ độc sau khi naloxone hết tác dụng.'
        , 'management':
        'Đây là tác dụng điều trị mong muốn. Tuy nhiên, cần theo dõi sát ít nhất 2-4 giờ sau khi dùng naloxone vì nguy cơ tái ngộ độc. Nếu opioid có thời gian tác dụng dài (methadone, buprenorphine), có thể cần infusion naloxone.'
        }], 'moderate': [{'drug': 'Buprenorphine', 'mechanism':
        'Buprenorphine có ái lực rất cao với opioid receptor, khó bị đẩy ra bởi naloxone. Có thể cần liều cao hơn hoặc không đáp ứng.'
        , 'effect':
        'Có thể không đảo ngược hoàn toàn tác dụng của buprenorphine, hoặc cần liều naloxone cao hơn'
        , 'management':
        'Có thể cần liều naloxone cao hơn (2-4mg) hoặc infusion. Theo dõi sát, có thể cần hỗ trợ hô hấp nếu không đáp ứng.'
        }], 'minor': []}, 'contraindications': {'tuyệt_đối': [
        'Dị ứng naloxone (hiếm)'], 'tương_đối': [
        'Bệnh nhân nghiện opioid - có thể gây hội chứng cai nặng (kích động, nôn, tăng huyết áp, nhịp tim nhanh)'
        ,
        'Bệnh nhân dùng opioid để giảm đau mãn tính - có thể đảo ngược hoàn toàn giảm đau, gây đau nặng'
        , 'Bệnh nhân có tiền sử co giật - có thể gây co giật',
        'Bệnh nhân có bệnh tim mạch - hội chứng cai có thể gây tăng huyết áp, nhịp tim nhanh, nguy cơ biến cố tim mạch'
        ]}, 'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Naloxone là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Naloxone có thể qua nhau thai. Tuy nhiên, trong quá liều opioid, lợi ích cứu sống mẹ (và thai nhi) vượt quá nguy cơ. Quá liều opioid có thể gây tử vong cho cả mẹ và thai nhi (ức chế hô hấp, thiếu oxy). Naloxone được sử dụng trong cấp cứu ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Naloxone có thời gian bán thải ngắn (30-90 phút) và bị chuyển hóa nhanh. Không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Naloxone có thời gian bán thải ngắn và không bài tiết vào sữa mẹ.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Naloxone chuyển hóa qua gan nhưng không tích lũy ở suy gan nhẹ.'
        , 'moderate': 'Không cần điều chỉnh liều.', 'severe':
        'Không cần điều chỉnh liều. Naloxone chuyển hóa qua gan nhưng không tích lũy ở suy gan nặng.'
        , 'notes':
        'Naloxone chuyển hóa qua gan (glucuronidation), nhưng không tích lũy ở suy gan. Không cần điều chỉnh liều ở bệnh nhân suy gan.'
        }, 'overdose_management': {'symptoms': [
        'Hội chứng cai opioid nặng (kích động, nôn, tăng huyết áp, nhịp tim nhanh, run, đau cơ)'
        , 'Co giật (hiếm)', 'Phù phổi cấp (hiếm)', 'Rối loạn nhịp tim (hiếm)',
        'Tăng huyết áp nặng',
        'Tái ngộ độc opioid (sau khi naloxone hết tác dụng)'], 'antidote':
        'Không có antidote đặc hiệu cho quá liều naloxone. Có thể dùng opioid (morphine, fentanyl) để đối kháng tác dụng nếu hội chứng cai quá nặng, nhưng THẬN TRỌNG (có thể gây ức chế hô hấp trở lại).'
        , 'treatment': ['Ngừng ngay naloxone nếu đang truyền',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2',
        'Nếu hội chứng cai nặng:', '  - Hỗ trợ tâm lý, an ủi bệnh nhân',
        '  - Nếu tăng huyết áp nặng: Thuốc hạ huyết áp (labetalol, clonidine)',
        '  - Nếu nôn: Thuốc chống nôn (ondansetron, metoclopramide)',
        '  - Nếu đau: Thuốc giảm đau không opioid (paracetamol, ibuprofen)',
        '  - THẬN TRỌNG: Không dùng opioid để điều trị hội chứng cai (có thể gây ức chế hô hấp trở lại)'
        , 'Nếu co giật:', '  - Benzodiazepine (diazepam, lorazepam) IV',
        '  - Theo dõi hô hấp (benzodiazepine có thể ức chế hô hấp)',
        'Nếu phù phổi cấp:', '  - Hỗ trợ hô hấp: Thở oxy, CPAP/BiPAP nếu cần',
        '  - Furosemide nếu có suy tim',
        '  - Nitroglycerin nếu có tăng huyết áp', 'Nếu tái ngộ độc opioid:',
        '  - Dùng lại naloxone (0.4-2mg IV/IM)',
        '  - Hoặc dùng infusion naloxone (0.25-6.25mcg/kg/giờ IV)',
        '  - Theo dõi sát nhịp thở và SpO2',
        'Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2 trong ít nhất 2-4 giờ'
        ], 'monitoring':
        'Theo dõi dấu hiệu sinh tồn (huyết áp, nhịp tim, nhịp thở, SpO2) liên tục trong ít nhất 2-4 giờ sau khi dùng naloxone. Theo dõi lâu hơn nếu có biến chứng (hội chứng cai nặng, co giật, phù phổi, tái ngộ độc opioid).'
        }, 'reversal_agents': {'available': False, 'agents': [], 'notes':
        'Không có reversal agent cho naloxone. Nếu hội chứng cai quá nặng, có thể dùng opioid (morphine, fentanyl) để đối kháng, nhưng THẬN TRỌNG vì có thể gây ức chế hô hấp trở lại.'
        }, 'administration_instructions': {'oral': None, 'iv': {
        'reconstitution':
        'Dùng trực tiếp từ lọ (0.4mg/ml hoặc 1mg/ml). Không cần pha loãng cho bolus. Cho infusion: pha 2mg trong 500ml D5W hoặc NS = 4mcg/ml.'
        , 'infusion_rate':
        'Overdose: 0.4-2mg IV bolus, lặp lại mỗi 2-3 phút đến khi đáp ứng. Reversal: 0.04-0.4mg IV titrate đến khi đáp ứng. Infusion: 0.25-6.25mcg/kg/giờ IV (pha 2mg trong 500ml = 4mcg/ml).'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],
        'incompatibility': [
        'Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion.'
        ], 'notes':
        'QUAN TRỌNG: 1) Tác dụng ngắn (30-90 phút) - opioid có thể tác dụng trở lại, 2) Theo dõi sát ít nhất 2-4 giờ sau khi dùng, 3) Nếu opioid có thời gian tác dụng dài (methadone, buprenorphine), có thể cần infusion, 4) Ở bệnh nhân nghiện: có thể gây hội chứng cai nặng, 5) Dùng liều thấp (0.04-0.4mg) khi đảo ngược tác dụng opioid sau phẫu thuật.'
        }, 'im': {'reconstitution':
        'Dùng trực tiếp từ lọ (0.4mg/ml hoặc 1mg/ml).', 'injection_site':
        'Cánh tay hoặc đùi ngoài.', 'notes':
        'Overdose: 0.4-2mg IM, lặp lại mỗi 2-3 phút đến khi đáp ứng. Trẻ em: 0.01mg/kg IM, lặp lại đến khi đáp ứng. Tác dụng chậm hơn IV (2-5 phút so với 1-2 phút).'
        }, 'inhaled': {'reconstitution':
        'Dùng dạng xịt mũi (Narcan Nasal Spray) - 4mg/0.1ml.', 'dose':
        '4mg (1 lần xịt) vào một bên mũi. Lặp lại sau 2-3 phút nếu không đáp ứng (có thể đổi bên mũi).'
        , 'notes':
        'Dùng trong quá liều opioid ngoài bệnh viện. Tác dụng tương tự IM. Theo dõi sát sau khi dùng.'
        }}, 'references': {'primary_sources': ['FDA Drug Label - Naloxone',
        'ACLS Guidelines 2020 - American Heart Association',
        'Opioid Overdose Guidelines - CDC',
        'UpToDate - Naloxone: Drug Information',
        'Medscape - Naloxone Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Naloxone Monograph',
        'Micromedex - Naloxone Drug Information'], 'last_updated': '2025-02-03',
        'evidence_level':
        'A - Dựa trên FDA drug labels, ACLS guidelines, opioid overdose guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        }}}

__all__ = ['OPIOID_ANTAGONISTS_DRUGS']
