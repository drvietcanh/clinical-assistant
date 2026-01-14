"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Antiarrhythmics

ANTIARRHYTHMICS_DRUGS = {
    "Adenosine": {'group': 'Emergency - Antiarrhythmic',
        'vietnamese_name': 'Adenosine',
        'administration': ['IV', 'IO'],
        'indications': [
        'Nhịp nhanh trên thất (SVT) - cấp cứu', 'Chẩn đoán rối loạn nhịp',
        'Cuồng nhĩ'],
        'contraindications': [
        'Block nhĩ thất độ 2-3 (không có máy tạo nhịp)', 'Hội chứng sick sinus',
        'Hen phế quản nặng', 'Dị ứng adenosine'],
        'dosage': {'adult_svt_first':
        '6mg IV bolus nhanh (1-2 giây) + flush nhanh 20ml NS',
        'adult_svt_second': '12mg IV nếu không đáp ứng (có thể lặp lại 1 lần)',
        'adult_max': '12mg (tối đa)', 'pediatric_svt_first':
        '0.1mg/kg IV (tối đa 6mg)', 'pediatric_svt_second':
        '0.2mg/kg IV nếu không đáp ứng (tối đa 12mg)', 'notes':
        'Phải tiêm bolus nhanh (1-2 giây) và flush ngay 20ml. Có thể gây ngừng tim tạm thời'
        },
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': [
        'Ngừng tim tạm thời (thường <10 giây - bình thường)',
        'Cảm giác khó chịu ở ngực', 'Khó thở', 'Đỏ mặt', 'Chóng mặt',
        'Loạn nhịp (thoáng qua)'],
        'interactions': [
        'Theophylline/Caffeine: đối kháng tác dụng',
        'Dipyridamole: tăng tác dụng', 'Carbamazepine: tăng tác dụng'],pregnancy': 'C - An toàn', 'mechanism_of_action':
        'Adenosine là một nucleoside nội sinh kích hoạt các thụ thể A1 adenosine ở nút nhĩ-thất (AV node), làm tăng thời gian dẫn truyền và kéo dài thời gian refrac của nút AV. Tác dụng này chặn tạm thời dẫn truyền qua nút AV, phá vỡ vòng re-entry trong SVT và chuyển nhịp về xoang. Có thời gian bán thải cực ngắn (<10 giây) do bị bắt giữ nhanh bởi tế bào hồng cầu và nội mô, nên tác dụng thoáng qua và an toàn'
        , 'monitoring': [
        'ECG liên tục trong và sau khi tiêm (ngừng tim tạm thời có thể xảy ra)',
        'Nhịp tim, huyết áp trong và sau khi tiêm (1-2 phút)',
        'Dấu hiệu sốc phản vệ (hiếm nhưng nguy hiểm)',
        'Dấu hiệu co thắt phế quản (đặc biệt ở bệnh nhân hen)',
        'Đáp ứng điều trị (chuyển về nhịp xoang)'],
        'precautions': [
        'PHẢI tiêm bolus nhanh (1-2 giây) và flush ngay 20ml NS để đảm bảo thuốc vào tim trước khi bị bắt giữ'
        , 'Nếu tiêm chậm → thuốc bị bắt giữ bởi tế bào máu → không hiệu quả',
        'Chuẩn bị sẵn thiết bị hồi sức tim phổi (CPR, defibrillator) vì có thể gây ngừng tim tạm thời'
        'Tránh dùng ở bệnh nhân hen phế quản nặng (có thể gây co thắt phế quản)',
        'Tránh dùng ở block AV độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp)'
        'Có thể gây ngừng tim tạm thời <10 giây (bình thường, không cần điều trị)',
        'Nếu không đáp ứng với 6mg, có thể tăng lên 12mg (tối đa)',
        'Tránh dùng với theophylline hoặc caffeine (đối kháng tác dụng)'],
        'pharmacokinetics': {'half_life': '<10 giây (cực ngắn)', 'onset':
        'Ngay lập tức (vài giây)', 'duration': '10-30 giây (tạm thời)',
        'protein_binding': 'Không đáng kể', 'clearance':
        'Bắt giữ nhanh bởi tế bào hồng cầu và nội mô, chuyển hóa thành inosine và adenosine monophosphate'
        },storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Bảo vệ khỏi ánh sáng'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Theophylline, Caffeine', 'mechanism':
        'Theophylline và caffeine là chất đối kháng adenosine receptor, ức chế tác dụng của adenosine.'
        , 'effect':
        'Giảm hoặc mất hiệu quả điều trị SVT, có thể cần liều cao hơn hoặc không đáp ứng'
        , 'management':
        'Tránh dùng adenosine nếu bệnh nhân đang dùng theophylline hoặc uống caffeine gần đây. Nếu cần, có thể cần liều cao hơn (12mg) hoặc dùng phương pháp khác (adenosine không hiệu quả).'
        }, {'drug': 'Dipyridamole', 'mechanism':
        'Dipyridamole ức chế bắt giữ adenosine bởi tế bào, tăng nồng độ và thời gian tác dụng của adenosine.'
        , 'effect':
        'Tăng tác dụng và thời gian tác dụng của adenosine, tăng nguy cơ tác dụng phụ (ngừng tim kéo dài, block AV)'
        , 'management':
        'GIẢM LIỀU adenosine xuống 50-75% (1.5-3mg thay vì 6mg). Theo dõi chặt chẽ ECG. Chuẩn bị sẵn thiết bị hồi sức.'
        }],
        'moderate': [{'drug': 'Carbamazepine', 'mechanism':
        'Carbamazepine có thể tăng tác dụng của adenosine (cơ chế không rõ ràng, có thể liên quan đến bắt giữ adenosine).'
        , 'effect':
        'Tăng tác dụng và thời gian tác dụng của adenosine, tăng nguy cơ tác dụng phụ'
        , 'management':
        'Thận trọng, có thể cần giảm liều adenosine. Theo dõi chặt chẽ ECG.'},
        {'drug': 'Digoxin', 'mechanism':
        'Digoxin có thể tăng độ nhạy cảm của nút AV với adenosine.', 'effect':
        'Tăng nguy cơ block AV, ngừng tim kéo dài', 'management':
        'Thận trọng, theo dõi ECG chặt chẽ. Có thể cần giảm liều adenosine.'}],
        'minor': [{'drug': 'Beta-blockers', 'mechanism':
        'Beta-blockers có thể tăng độ nhạy cảm của nút AV với adenosine.',
        'effect': 'Tăng nguy cơ block AV (nhẹ)', 'management':
        'Theo dõi ECG. Không cần điều chỉnh liều thường quy.'}]},contraindications': {'tuyệt_đối': [
        'Block nhĩ thất độ 2-3 (AV block) không có máy tạo nhịp',
        'Hội chứng sick sinus (sick sinus syndrome) không có máy tạo nhịp',
        'Hen phế quản nặng hoặc co thắt phế quản nặng', 'Dị ứng adenosine',
        'Rung nhĩ/rung thất (không phải chỉ định)'],tương_đối': [
        'Block AV độ 1 - thận trọng, có thể làm nặng',
        'Hen phế quản nhẹ đến trung bình - thận trọng, có thể gây co thắt phế quản'
        , 'Suy tim - thận trọng, có thể gây ngừng tim kéo dài',
        'Suy thận nặng - không cần điều chỉnh liều nhưng thận trọng',
        'Dùng với dipyridamole - giảm liều 50-75%',
        'Dùng với theophylline/caffeine - có thể không hiệu quả',
        'Nhịp tim chậm (<50 bpm) - thận trọng, có thể gây ngừng tim']},pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Adenosine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Adenosine có thời gian bán thải cực ngắn (<10 giây) và tác dụng thoáng qua, nên ít có khả năng ảnh hưởng đến thai nhi. Được sử dụng trong cấp cứu để điều trị SVT ở phụ nữ có thai và có vẻ an toàn. SVT có thể gây nguy hiểm cho cả mẹ và thai nhi (giảm tưới máu, thiếu oxy). Adenosine có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong cấp cứu.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Adenosine có thời gian bán thải cực ngắn (<10 giây), nên không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Tác dụng thoáng qua và bị bắt giữ nhanh bởi tế bào. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Adenosine có tác dụng cực ngắn và không bài tiết vào sữa mẹ.'
        }},hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Adenosine không chuyển hóa qua gan, bị bắt giữ bởi tế bào máu.'
        , 'moderate': 'Không cần điều chỉnh liều.', 'severe':
        'Không cần điều chỉnh liều. Adenosine không chuyển hóa qua gan.',
        'notes':
        'Adenosine không chuyển hóa qua gan, bị bắt giữ nhanh bởi tế bào hồng cầu và nội mô, chuyển hóa thành inosine. Không cần điều chỉnh liều ở bệnh nhân suy gan.'
        },overdose_management': {'symptoms': [
        'Ngừng tim tạm thời kéo dài (>10-30 giây) - có thể tiến triển thành ngừng tim thực sự'
        , 'Block AV độ 2-3 kéo dài - có thể gây nhịp chậm nặng, suy tim',
        'Rung nhĩ/rung thất - hiếm nhưng nguy hiểm',
        'Co thắt phế quản nặng - khó thở, suy hô hấp',
        'Sốc phản vệ - phát ban, phù mạch, sốc (hiếm)', 'Tụt huyết áp nặng',
        'Nhịp chậm nặng (<30-40 bpm)'],antidote':
        'Không có antidote đặc hiệu. Theophylline hoặc aminophylline có thể đối kháng tác dụng adenosine (nếu có block AV kéo dài).'
        , 'treatment': ['Ngừng ngay adenosine nếu đang truyền (nếu có)',
        'Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học',
        'Theo dõi ECG liên tục: Nhịp tim, block AV, loạn nhịp',
        'Nếu ngừng tim tạm thời <10 giây: Quan sát, thường tự hồi phục',
        'Nếu ngừng tim kéo dài >10-30 giây hoặc block AV độ 2-3:',
        '  - Hỗ trợ hô hấp, thở oxy',
        '  - Nếu nhịp chậm nặng: Atropine 0.5-1mg IV (nếu không có block AV)',
        '  - Nếu block AV kéo dài: Theophylline 100-200mg IV hoặc aminophylline (đối kháng adenosine)'
        , '  - Nếu ngừng tim thực sự: CPR, defibrillation nếu cần',
        'Nếu co thắt phế quản: Salbutamol dạng hít hoặc IV, corticosteroid nếu cần'
        , 'Nếu sốc phản vệ: Epinephrine, diphenhydramine, corticosteroid',
        'Hỗ trợ huyết động: Truyền dịch, thuốc vận mạch nếu cần',
        'Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2 trong ít nhất 30-60 phút'
        ],
        'monitoring':
        'Theo dõi ECG liên tục, dấu hiệu sinh tồn trong ít nhất 30-60 phút sau khi dùng. Theo dõi lâu hơn nếu có biến chứng (block AV, ngừng tim, co thắt phế quản).'
        },reversal_agents': {'available': True, 'agents': [{'agent':
        'Theophylline / Aminophylline', 'mechanism':
        'Đối kháng adenosine receptors, đảo ngược tác dụng block AV của adenosine',
        'indication': 'Block AV kéo dài sau khi dùng adenosine', 'dose':
        'Theophylline 100-200mg IV hoặc Aminophylline 5-6mg/kg IV'}]},administration_instructions': {'oral': None, 'iv': {'reconstitution':
        'Dùng trực tiếp từ lọ, không cần pha. Có thể pha trong NS nếu cần nhưng thường dùng trực tiếp.'
        , 'infusion_rate':
        'BOLUS NHANH: Tiêm trực tiếp vào tĩnh mạch lớn (tĩnh mạch ngoại biên lớn hoặc tĩnh mạch trung tâm) trong 1-2 giây. SAU ĐÓ NGAY LẬP TỨC flush 20ml NS nhanh để đẩy thuốc vào tim trước khi bị bắt giữ bởi tế bào máu. KHÔNG được tiêm chậm hoặc truyền - sẽ không hiệu quả.'
        , 'compatibility': ['NS (0.9% NaCl) - để flush'],incompatibility': [
        'Không trộn với các thuốc khác. Tiêm bolus riêng biệt.'],notes':
        'QUAN TRỌNG: 1) Tiêm bolus NHANH (1-2 giây) vào tĩnh mạch lớn, 2) Flush NGAY 20ml NS nhanh, 3) Theo dõi ECG liên tục, 4) Chuẩn bị sẵn thiết bị hồi sức. Nếu tiêm chậm → thuốc bị bắt giữ → không hiệu quả. Liều đầu: 6mg, nếu không đáp ứng: 12mg (tối đa).'
        }},references': {'primary_sources': ['FDA Drug Label - Adenosine',
        'ACLS Guidelines 2020 - American Heart Association',
        'UpToDate - Adenosine: Drug Information',
        'Medscape - Adenosine Drug Reference',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Adenosine Monograph',
        'Micromedex - Adenosine Drug Information'],last_updated':
        '2024-12-19', 'evidence_level':
        'A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG"]
        },
        "guideline_tags": [
            "ACLS Guidelines 2020 - American Heart Association",
            "FDA Drug Label - Adenosine",
            "ISMP High Alert Medications - Emergency Medications"
        ],
        "black_box_warnings": None,
}}

__all__ = ['ANTIARRHYTHMICS_DRUGS']
