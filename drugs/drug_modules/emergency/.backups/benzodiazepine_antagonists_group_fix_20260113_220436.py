"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Benzodiazepine Antagonists

BENZODIAZEPINE_ANTAGONISTS_DRUGS = {
    "Flumazenil": {'group': 'Emergency - Benzodiazepine Antagonist',vietnamese_name':
        'Flumazenil, Anexate', 'administration': ['IV'],indications': [
        'Quá liều benzodiazepine',
        'Đảo ngược tác dụng benzodiazepine sau phẫu thuật',
        'Quá liều zolpidem/zopiclone'],contraindications': [
        'Dị ứng flumazenil', 'Động kinh (đang điều trị với benzodiazepine)',
        'Quá liều tricyclic antidepressants',
        'Phụ thuộc benzodiazepine lâu dài'],dosage': {'adult_overdose':
        '0.2mg IV, lặp lại 0.2mg mỗi 1 phút đến khi đáp ứng (tối đa 1mg)',
        'adult_reversal': '0.1-0.2mg IV titrate đến khi đáp ứng', 'pediatric':
        '0.01mg/kg IV (tối đa 0.2mg), lặp lại đến khi đáp ứng', 'notes':
        'Tác dụng ngắn (30-60 phút), có thể cần lặp lại. Nguy cơ co giật ở bệnh nhân động kinh'
        },renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},side_effects': [
        'Co giật (nguy hiểm ở bệnh nhân động kinh)',
        'Hội chứng cai benzodiazepine', 'Buồn nôn, nôn', 'Chóng mặt', 'Lo lắng',
        'Rối loạn nhịp tim'],interactions': [
        'Benzodiazepines: đảo ngược tác dụng',
        'Tricyclic antidepressants: tăng nguy cơ co giật'],pregnancy':
        'C - Thận trọng', 'mechanism_of_action':
        'Benzodiazepine receptor antagonist cạnh tranh. Gắn với ái lực cao vào benzodiazepine receptor (một phần của GABA-A receptor complex), đẩy benzodiazepine ra khỏi receptor, đảo ngược tác dụng của benzodiazepine (an thần, ức chế hô hấp, giảm trương lực cơ, mất trí nhớ). Tác dụng rất nhanh (1-2 phút IV), nhưng thời gian tác dụng ngắn (45-90 phút) do bị chuyển hóa nhanh, trong khi nhiều benzodiazepine có thời gian tác dụng dài hơn → cần theo dõi sát, có thể cần lặp lại liều.'
        , 'monitoring': ['Mức độ ý thức (GCS) liên tục',
        'Nhịp thở và độ bão hòa oxy (SpO2)',
        'Dấu hiệu tái an thần/tái ức chế hô hấp (quan trọng - flumazenil hết tác dụng trước benzodiazepine)'
        'Dấu hiệu hội chứng cai benzodiazepine (kích động, run, co giật) - đặc biệt ở bệnh nhân nghiện'
        , 'Huyết áp và nhịp tim',
        'Co giật (nguy cơ ở bệnh nhân có tiền sử co giật, dùng benzodiazepine để chống co giật)'
        , 'Rối loạn nhịp tim (hiếm)'],precautions': [
        'Thời gian tác dụng NGẮN (45-90 phút) - benzodiazepine có thể tác dụng trở lại sau khi flumazenil hết'
        'Theo dõi sát ít nhất 2-4 giờ sau khi dùng (nguy cơ tái an thần, tái ức chế hô hấp)'
        'Ở bệnh nhân nghiện benzodiazepine: có thể gây hội chứng cai nặng (kích động, run, co giật) - cần chuẩn bị xử trí'
        'KHÔNG dùng ở bệnh nhân dùng benzodiazepine để chống co giật (có thể gây co giật nặng)'
        'KHÔNG dùng ở ngộ độc tricyclic antidepressant (có thể gây co giật, rối loạn nhịp)'
        , 'Khởi đầu với liều thấp (0.2mg), tăng dần nếu cần',
        'Không dùng quá liều (không tăng hiệu quả, tăng nguy cơ tác dụng phụ)',
        'Nếu cần duy trì: có thể dùng infusion, nhưng thường không khuyến cáo',
        'Thận trọng ở bệnh nhân có tiền sử co giật'],pharmacokinetics': {
        'half_life': '41-79 phút (ngắn)', 'onset': '1-2 phút (IV)', 'duration':
        '45-90 phút (tùy liều)', 'protein_binding': '50%', 'metabolism':
        'Gan (glucuronidation)', 'clearance':
        'Gan, thời gian bán thải ngắn hơn nhiều so với hầu hết benzodiazepine'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ.'
        , 'black_box_warnings':
        'Không có black box warning. Tuy nhiên, thời gian tác dụng ngắn có thể dẫn đến tái an thần và tái ức chế hô hấp nếu không theo dõi đúng. Hội chứng cai benzodiazepine có thể nguy hiểm ở bệnh nhân nghiện. Nguy cơ co giật ở bệnh nhân có tiền sử co giật hoặc ngộ độc tricyclic antidepressant.'
        , 'drug_interactions': {'major': [{'drug':
        'Benzodiazepines (Diazepam, Midazolam, Lorazepam, etc.)', 'mechanism':
        'Flumazenil là benzodiazepine receptor antagonist cạnh tranh, đẩy benzodiazepine ra khỏi receptor, đảo ngược hoàn toàn tác dụng của benzodiazepine.'
        , 'effect':
        'Đảo ngược tác dụng benzodiazepine (an thần, ức chế hô hấp, giảm trương lực cơ, mất trí nhớ). Nếu benzodiazepine có thời gian tác dụng dài hơn flumazenil → tái an thần sau khi flumazenil hết tác dụng.'
        , 'management':
        'Đây là tác dụng điều trị mong muốn. Tuy nhiên, cần theo dõi sát ít nhất 2-4 giờ sau khi dùng flumazenil vì nguy cơ tái an thần. Nếu benzodiazepine có thời gian tác dụng dài (diazepam, clonazepam), có thể cần lặp lại liều flumazenil.'
        }, {'drug': 'Tricyclic Antidepressants (TCAs)', 'mechanism':
        'Flumazenil có thể làm giảm ngưỡng co giật, và TCAs cũng làm giảm ngưỡng co giật. Kết hợp: tăng nguy cơ co giật nặng.'
        , 'effect':
        'Tăng nguy cơ co giật nặng, rối loạn nhịp tim, nguy hiểm tính mạng',
        'management':
        'CHỐNG CHỈ ĐỊNH dùng flumazenil ở ngộ độc tricyclic antidepressant. Nếu không chắc chắn, không dùng flumazenil.'
        }],moderate': [{'drug':
        'Zolpidem, Zopiclone (Non-benzodiazepine hypnotics)', 'mechanism':
        'Zolpidem và zopiclone tác dụng trên benzodiazepine receptor, có thể bị đảo ngược bởi flumazenil.'
        , 'effect':
        'Có thể đảo ngược tác dụng của zolpidem/zopiclone, nhưng có thể không hoàn toàn'
        , 'management':
        'Có thể dùng flumazenil để đảo ngược quá liều zolpidem/zopiclone. Theo dõi sát.'
        }],minor': []},contraindications': {'tuyệt_đối': [
        'Dị ứng flumazenil (hiếm)',
        'Động kinh đang điều trị với benzodiazepine - có thể gây co giật nặng',
        'Quá liều tricyclic antidepressant - tăng nguy cơ co giật, rối loạn nhịp tim'
        'Phụ thuộc benzodiazepine lâu dài - có thể gây hội chứng cai nặng, co giật'
        ],tương_đối': [
        'Bệnh nhân nghiện benzodiazepine - có thể gây hội chứng cai nặng (kích động, run, co giật)'
        , 'Bệnh nhân có tiền sử co giật - tăng nguy cơ co giật',
        'Bệnh nhân dùng benzodiazepine để chống co giật - có thể gây co giật nặng',
        'Bệnh nhân có bệnh tim mạch - hội chứng cai có thể gây tăng huyết áp, nhịp tim nhanh'
        'Ngộ độc hỗn hợp (nhiều thuốc) - không chắc chắn thành phần → không dùng flumazenil'
        ],pregnancy_details':
        'Flumazenil là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Flumazenil có thể qua nhau thai. Tuy nhiên, trong quá liều benzodiazepine, lợi ích cứu sống mẹ (và thai nhi) vượt quá nguy cơ. Quá liều benzodiazepine có thể gây tử vong cho cả mẹ và thai nhi (ức chế hô hấp, thiếu oxy). Flumazenil được sử dụng trong cấp cứu ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Flumazenil có thời gian bán thải ngắn (41-79 phút) và bị chuyển hóa nhanh. Không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Flumazenil có thời gian bán thải ngắn và không bài tiết vào sữa mẹ.'
        }},hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Flumazenil chuyển hóa qua gan nhưng không tích lũy ở suy gan nhẹ.'
        , 'moderate': 'Không cần điều chỉnh liều.', 'severe':
        'Không cần điều chỉnh liều. Flumazenil chuyển hóa qua gan nhưng không tích lũy ở suy gan nặng.'
        , 'notes':
        'Flumazenil chuyển hóa qua gan (glucuronidation), nhưng không tích lũy ở suy gan. Không cần điều chỉnh liều ở bệnh nhân suy gan.'
        },overdose_management': {'symptoms': [
        'Hội chứng cai benzodiazepine nặng (kích động, run, co giật, lo lắng)',
        'Co giật nặng (đặc biệt nguy hiểm ở bệnh nhân có tiền sử co giật hoặc ngộ độc TCA)'
        , 'Rối loạn nhịp tim (hiếm, thường liên quan đến ngộ độc TCA)',
        'Tăng huyết áp',
        'Tái an thần/tái ức chế hô hấp (sau khi flumazenil hết tác dụng)'],antidote':
        'Không có antidote đặc hiệu cho quá liều flumazenil. Có thể dùng benzodiazepine (diazepam, midazolam) để đối kháng tác dụng nếu hội chứng cai quá nặng hoặc co giật, nhưng THẬN TRỌNG (có thể gây ức chế hô hấp trở lại).'
        , 'treatment': ['Ngừng ngay flumazenil nếu đang truyền',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, mức độ ý thức'
        , 'Nếu co giật:',
        '  - Benzodiazepine (diazepam 5-10mg IV, lorazepam 2-4mg IV) - đây là điều trị chính'
        , '  - Nếu không đáp ứng: Phenytoin, phenobarbital',
        '  - Theo dõi hô hấp (benzodiazepine có thể ức chế hô hấp)',
        'Nếu hội chứng cai nặng:', '  - Hỗ trợ tâm lý, an ủi bệnh nhân',
        '  - Nếu tăng huyết áp nặng: Thuốc hạ huyết áp (labetalol, clonidine)',
        '  - Nếu lo lắng nặng: Benzodiazepine (diazepam, lorazepam) - THẬN TRỌNG',
        'Nếu rối loạn nhịp tim:', '  - Điều trị theo protocol rối loạn nhịp',
        '  - Nếu liên quan đến ngộ độc TCA: Điều trị theo protocol ngộ độc TCA',
        'Nếu tái an thần/tái ức chế hô hấp:',
        '  - Dùng lại flumazenil (0.2mg IV, lặp lại đến khi đáp ứng)',
        '  - Hoặc dùng benzodiazepine nếu cần an thần (THẬN TRỌNG)',
        '  - Theo dõi sát nhịp thở và SpO2',
        'Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, mức độ ý thức trong ít nhất 2-4 giờ'
        ],monitoring':
        'Theo dõi dấu hiệu sinh tồn (huyết áp, nhịp tim, nhịp thở, SpO2, mức độ ý thức) liên tục trong ít nhất 2-4 giờ sau khi dùng flumazenil. Theo dõi lâu hơn nếu có biến chứng (hội chứng cai nặng, co giật, tái an thần).'
        },reversal_agents': {'available': False, 'agents': [],notes':
        'Không có reversal agent cho flumazenil. Nếu hội chứng cai quá nặng hoặc co giật, có thể dùng benzodiazepine (diazepam, midazolam, lorazepam) để đối kháng, nhưng THẬN TRỌNG vì có thể gây ức chế hô hấp trở lại.'
        },administration_instructions': {'oral': None, 'iv': {
        'reconstitution':
        'Dùng trực tiếp từ lọ (0.1mg/ml). Không cần pha loãng.',
        'infusion_rate':
        'Overdose: 0.2mg IV, lặp lại 0.2mg mỗi 1 phút đến khi đáp ứng (tối đa 1mg). Reversal: 0.1-0.2mg IV titrate đến khi đáp ứng. Trẻ em: 0.01mg/kg IV (tối đa 0.2mg), lặp lại đến khi đáp ứng.'
        , 'compatibility': ['NS (0.9% NaCl)', 'D5W (5% Dextrose)'],incompatibility': [
        'Không trộn với các thuốc khác. Tiêm bolus riêng biệt.'],notes':
        'QUAN TRỌNG: 1) Tác dụng ngắn (45-90 phút) - benzodiazepine có thể tác dụng trở lại, 2) Theo dõi sát ít nhất 2-4 giờ sau khi dùng, 3) CHỐNG CHỈ ĐỊNH ở ngộ độc TCA hoặc động kinh đang điều trị với benzodiazepine, 4) Ở bệnh nhân nghiện: có thể gây hội chứng cai nặng, 5) Khởi đầu với liều thấp (0.2mg), tăng dần nếu cần.'
        }},references': {'primary_sources': ['FDA Drug Label - Flumazenil',
        'ACLS Guidelines 2020 - American Heart Association',
        'Benzodiazepine Overdose Guidelines',
        'UpToDate - Flumazenil: Drug Information',
        'Medscape - Flumazenil Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Flumazenil Monograph',
        'Micromedex - Flumazenil Drug Information'],last_updated':
        '2025-02-03', 'evidence_level':
        'A - Dựa trên FDA drug labels, ACLS guidelines, benzodiazepine overdose guidelines, và dữ liệu lâm sàng từ nhiều nguồn',
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Vital Signs", "GCS", "Respiratory"]
        },
        "guideline_tags": [
            "ACLS Guidelines 2020 - American Heart Association",
            "FDA Drug Label - Flumazenil",
            "Benzodiazepine Overdose Guidelines",
            "ISMP High Alert Medications - Emergency Medications"
        ]}}

__all__ = ['BENZODIAZEPINE_ANTAGONISTS_DRUGS']
