"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Anticholinergics

ANTICHOLINERGICS_DRUGS = {
    "Atropine": {'group': 'Emergency - Anticholinergic',
        'vietnamese_name': 'Atropine',
        'administration': ['IV', 'IM', 'IO', 'IT'],
        'indications': [
        'Nhịp tim chậm có triệu chứng', 'Block nhĩ thất',
        'Quá liều organophosphate', 'Chuẩn bị phẫu thuật (giảm tiết)',
        'Ngừng tim với nhịp chậm/PEA'],
        'contraindications': [
        'Glaucoma góc đóng', 'Tắc nghẽn đường tiểu', 'Nhịp tim nhanh', 'Sốt'],
        'dosage': {'adult_bradycardia': '0.5-1mg IV mỗi 3-5 phút (tối đa 3mg)',
        'adult_cardiac_arrest': '1mg IV/IT, lặp lại mỗi 3-5 phút',
        'adult_organophosphate': '2-5mg IV, lặp lại đến khi đạt tác dụng',
        'pediatric_bradycardia': '0.02mg/kg IV (tối thiểu 0.1mg, tối đa 0.5mg)',
        'pediatric_cardiac_arrest': '0.02mg/kg IV/IT (tối thiểu 0.1mg)',
        'notes':
        'Liều tối thiểu người lớn 0.5mg để tránh nhịp tim chậm nghịch lý'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},
        'side_effects': ['Nhịp tim nhanh',
        'Khô miệng', 'Giãn đồng tử', 'Táo bón', 'Bí tiểu', 'Lú lẫn (người già)',
        'Tăng nhãn áp'],
        'interactions': [
        'Các anticholinergics khác: tăng tác dụng',
        'Digoxin: có thể tăng nồng độ digoxin'],
        'mechanism_of_action':
        'Anticholinergic (antimuscarinic). Kháng chọn lọc thụ thể muscarinic acetylcholine (M1-M5), ức chế tác dụng của acetylcholine. Tăng nhịp tim (ức chế vagal tone), giảm tiết (nước bọt, mồ hôi, dịch tiêu hóa, phế quản), giãn đồng tử và giảm co thắt cơ trơn (phế quản, ruột, bàng quang). Được dùng trong emergency để điều trị nhịp tim chậm có triệu chứng, block nhĩ thất, và như một chất giải độc trong quá liều organophosphate.'
        , 'monitoring': ['Nhịp tim (ECG monitoring - mục tiêu tăng nhịp tim)',
        'Dấu hiệu kháng cholinergic quá mức: khô miệng nặng, giãn đồng tử, bí tiểu, lú lẫn'
        , 'Nhãn áp (nếu có nguy cơ glaucoma)',
        'Triệu chứng nhịp tim chậm nghịch lý (paradoxical bradycardia) - có thể xảy ra với liều <0.5mg ở người lớn'
        , 'Phản ứng quá mức (nhịp tim nhanh, đánh trống ngực)'],
        'precautions':
        [
        'QUAN TRỌNG: Liều tối thiểu người lớn 0.5mg để tránh nhịp tim chậm nghịch lý (liều thấp có thể kích thích trung tâm vagal)'
        'CHỐNG CHỈ ĐỊNH tuyệt đối: Glaucoma góc đóng (có thể gây tăng nhãn áp đe dọa thị giác)'
        , 'CHỐNG CHỈ ĐỊNH: Tắc nghẽn đường tiểu (có thể làm nặng thêm bí tiểu)',
        'CHỐNG CHỈ ĐỊNH: Nhịp tim nhanh (có thể làm tăng nhịp tim hơn nữa)',
        'Thận trọng ở người già (tăng nguy cơ lú lẫn, bí tiểu)',
        'Thận trọng ở bệnh nhân sốt (có thể làm tăng nhiệt độ do giảm tiết mồ hôi)'
        'Thận trọng khi dùng với các anticholinergics khác (tăng tác dụng phụ)',
        'Trong quá liều organophosphate: dùng liều cao hơn nhiều (2-5mg), có thể cần lặp lại nhiều lần cho đến khi đạt tác dụng (đồng tử co lại, giảm tiết)'
        ],
        'pharmacokinetics': {'half_life':
        '2-4 giờ (Người lớn), 10-20 giờ (Trẻ em)', 'onset':
        'Vài phút (IV), 15-30 phút (IM)', 'duration':
        '4-6 giờ (tác dụng lâm sàng)', 'protein_binding': '50%', 'clearance':
        'Thận (50-90% thải qua nước tiểu dưới dạng không đổi), gan (metabolite). Thời gian bán hủy dài hơn ở trẻ em'
        },
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch tiêm: bảo quản trong tủ mát (2-8°C) nếu có chỉ định, nhưng thường ổn định ở nhiệt độ phòng'
        , 'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Các anticholinergics khác (Benztropine, Diphenhydramine, Scopolamine)',
        'mechanism': 'Tác dụng cộng dồn kháng cholinergic, tăng tác dụng phụ.',
        'effect':
        'Tăng tác dụng phụ: khô miệng nặng, bí tiểu, lú lẫn, tăng nhãn áp',
        'management':
        'Thận trọng khi dùng đồng thời. Giảm liều hoặc tránh dùng nếu có thể. Theo dõi dấu hiệu kháng cholinergic quá mức.'
        }],
        'moderate': [{'drug': 'Digoxin', 'mechanism':
        'Atropine có thể làm chậm nhu động ruột, tăng hấp thu digoxin.',
        'effect': 'Tăng nồng độ digoxin, tăng nguy cơ độc tính', 'management':
        'Theo dõi nồng độ digoxin và dấu hiệu độc tính digoxin. Điều chỉnh liều digoxin nếu cần.'
        }, {'drug': 'Thuốc chống trầm cảm ba vòng (TCA)', 'mechanism':
        'Cả hai đều có tác dụng kháng cholinergic, tác dụng cộng dồn.',
        'effect':
        'Tăng tác dụng phụ kháng cholinergic: khô miệng, bí tiểu, lú lẫn',
        'management':
        'Thận trọng khi dùng đồng thời. Theo dõi dấu hiệu kháng cholinergic quá mức.'
        }],
        'minor': [{'drug': 'Ketamine', 'mechanism':
        'Atropine có thể làm tăng nhịp tim, có thể tương tác với ketamine.',
        'effect': 'Tăng nhịp tim', 'management':
        'Theo dõi nhịp tim khi dùng đồng thời.'}]},
        'contraindications': {
        'tuyệt_đối': [
        'Glaucoma góc đóng (có thể gây tăng nhãn áp đe dọa thị giác)',
        'Tắc nghẽn đường tiểu (có thể làm nặng thêm bí tiểu)',
        'Nhịp tim nhanh (có thể làm tăng nhịp tim hơn nữa)', 'Dị ứng atropine'],
        'tương_đối': ['Sốt (có thể làm tăng nhiệt độ do giảm tiết mồ hôi)',
        'Người già (tăng nguy cơ lú lẫn, bí tiểu)',
        'Bệnh mạch vành (tăng nhịp tim có thể làm nặng thêm)',
        'Bệnh phổi tắc nghẽn mạn tính (COPD) - có thể làm tăng độ nhớt đờm']},contraindications_detail': {
        'tuyệt_đối': [
        'Glaucoma góc đóng (có thể gây tăng nhãn áp đe dọa thị giác)',
        'Tắc nghẽn đường tiểu (có thể làm nặng thêm bí tiểu)',
        'Nhịp tim nhanh (có thể làm tăng nhịp tim hơn nữa)', 'Dị ứng atropine'],
        'tương_đối': ['Sốt (có thể làm tăng nhiệt độ do giảm tiết mồ hôi)',
        'Người già (tăng nguy cơ lú lẫn, bí tiểu)',
        'Bệnh mạch vành (tăng nhịp tim có thể làm nặng thêm)',
        'Bệnh phổi tắc nghẽn mạn tính (COPD) - có thể làm tăng độ nhớt đờm']},
        'black_box_warnings': None,
        'pregnancy_lactation': {'fda_category': 'C', 'pregnancy_details':
        'Atropine là category C. Có thể đi qua nhau thai nhưng thường an toàn trong thai kỳ khi dùng với liều điều trị. Dùng được trong cấp cứu. Dùng liều thấp nhất hiệu quả.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Atropine bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú với liều điều trị. Ít báo cáo về tác dụng phụ ở trẻ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Theo dõi dấu hiệu bất thường ở trẻ (hiếm).'
        }},
        'hepatic_adjustment': {'mild': 'Không cần điều chỉnh liều.',
        'moderate': 'Không cần điều chỉnh liều.', 'severe':
        'Không cần điều chỉnh liều.', 'notes':
        'Atropine chủ yếu thải trừ qua thận, không cần điều chỉnh liều ở suy gan.'
        },
        'overdose_management': {'symptoms': [
        'Kháng cholinergic quá mức: khô miệng nặng, khô da, giảm tiết mồ hôi',
        'Giãn đồng tử, mờ mắt, tăng nhãn áp', 'Nhịp tim nhanh, loạn nhịp tim',
        'Bí tiểu, táo bón', 'Lú lẫn, ảo giác, co giật (hiếm)',
        'Sốt (do giảm tiết mồ hôi)', 'Khó thở (do giảm tiết phế quản)'],
        'antidote':
        'Physostigmine - chất ức chế cholinesterase, tăng acetylcholine, đối kháng atropine.'
        , 'treatment': ['Ngừng atropine ngay lập tức',
        'Nếu nhẹ: điều trị hỗ trợ, theo dõi',
        'Nếu nặng: dùng physostigmine 0.5-2mg IV chậm (có thể lặp lại sau 10-30 phút nếu cần). Thận trọng với liều cao physostigmine (có thể gây cholinergic crisis).'
        , 'Theo dõi dấu hiệu sinh tồn: nhịp tim, huyết áp, nhiệt độ',
        'Điều trị sốt: làm mát, paracetamol',
        'Điều trị bí tiểu: đặt ống thông tiểu nếu cần',
        'Điều trị tăng nhãn áp: thuốc nhỏ mắt pilocarpine',
        'Theo dõi ít nhất 4-6 giờ (half-life 2-4 giờ ở người lớn, 10-20 giờ ở trẻ em)'
        ],
        'monitoring':
        'Nhịp tim, huyết áp, nhiệt độ, nhãn áp, ý thức, dấu hiệu kháng cholinergic. Theo dõi ít nhất 4-6 giờ (lâu hơn ở trẻ em).'
        },
        'reversal_agents': {'available': True, 'agents': [{'name':
        'Physostigmine', 'mechanism':
        'Physostigmine ức chế cholinesterase, tăng nồng độ acetylcholine, đối kháng tác dụng kháng cholinergic của atropine.'
        , 'indication':
        'Quá liều atropine gây kháng cholinergic quá mức (lú lẫn, co giật, nhịp tim nhanh nặng)'
        , 'dosage':
        '0.5-2mg IV chậm (có thể lặp lại sau 10-30 phút nếu cần). Thận trọng với liều cao (có thể gây cholinergic crisis).'
        , 'notes':
        'Chỉ dùng khi có triệu chứng nặng. Thận trọng với liều cao physostigmine (có thể gây cholinergic crisis với các triệu chứng: tăng tiết, co thắt phế quản, chậm nhịp tim).'
        }]},
        'administration_instructions': {'oral': {'with_food':
        'N/A - Không có dạng uống', 'timing': 'N/A'},iv': {'reconstitution':
        'Pha với D5W hoặc Normal saline. Có thể dùng trực tiếp nếu đã pha sẵn.',
        'infusion_rate':
        'Tiêm IV bolus nhanh (trong cấp cứu). Không cần truyền chậm.',
        'compatibility': ['D5W', 'Normal saline'],
        'incompatibility': [
        'Không trộn với các thuốc khác'],
        'notes':
        'QUAN TRỌNG: Liều tối thiểu người lớn 0.5mg để tránh nhịp tim chậm nghịch lý. Trong quá liều organophosphate: dùng liều cao hơn nhiều (2-5mg), có thể lặp lại nhiều lần.'
        }},
        'references': {'primary_sources': ['FDA Drug Label - Atropine',
        'ACLS Guidelines - Bradycardia Management',
        'UpToDate - Atropine drug information',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
        'Lexicomp Online - Atropine Monograph'],
        'evidence_level':
        'A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn'
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Vital Signs"]
        },
        "guideline_tags": [
            "ACLS Guidelines - Bradycardia Management",
            "FDA Drug Label - Atropine",
            "ISMP High Alert Medications - Emergency Medications"
        ],
        "black_box_warnings": None,
}}

__all__ = ['ANTICHOLINERGICS_DRUGS']
