"""Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data"""

# Folates

FOLATES_DRUGS = {
    "Folic acid": {'group': 'Vitamins/Supplements - Folate', 'vietnamese_name':
        'Folic acid, Folate, Vitamin B9', 'administration': ['PO'],
        'indications': ['Thiếu acid folic',
        'Thiếu máu hồng cầu to do thiếu folate',
        'Dự phòng dị tật ống thần kinh (có thai)', 'Dự phòng thiếu máu',
        'Điều trị methotrexate độc tính'], 'contraindications': [
        'Dị ứng acid folic', 'Ung thư (trừ khi điều trị thiếu máu do hóa trị)'],
        'dosage': {'adult_deficiency': '1-5mg x 1 lần/ngày', 'adult_pregnancy':
        '400-800mcg x 1 lần/ngày (bắt đầu trước khi có thai)',
        'adult_maintenance': '400mcg x 1 lần/ngày', 'adult_methotrexate':
        '1-5mg x 1 lần/ngày (sau khi dùng methotrexate)', 'notes':
        'Uống trước khi có thai ít nhất 1 tháng để dự phòng dị tật ống thần kinh'
        }, 'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'}, 'side_effects': ['Rất ít tác dụng phụ',
        'Ban da (hiếm)', 'Phản ứng dị ứng (hiếm)'], 'interactions': [
        'Methotrexate: giảm hiệu quả methotrexate (trừ khi dùng để điều trị độc tính)'
        , 'Phenytoin: giảm nồng độ phenytoin',
        'Chloramphenicol: giảm đáp ứng với acid folic',
        'Sulfasalazine: giảm hấp thu acid folic'], 'pregnancy':
        'A - An toàn, cần thiết (dự phòng dị tật ống thần kinh)',
        'mechanism_of_action':
        'Folic acid (folate, vitamin B9) là coenzyme cần thiết cho tổng hợp DNA và RNA, đặc biệt quan trọng trong quá trình phân chia tế bào. Folic acid được chuyển đổi thành tetrahydrofolate (THF), tham gia vào các phản ứng methyl transfer, tổng hợp purine và pyrimidine (các nucleotide của DNA/RNA). Folic acid cần thiết cho sự phát triển bình thường của ống thần kinh trong thai kỳ (tuần 3-4), giúp ngăn ngừa dị tật ống thần kinh (spina bifida, anencephaly). Thiếu folic acid gây thiếu máu hồng cầu to do giảm tổng hợp DNA, dẫn đến tế bào hồng cầu chưa trưởng thành. Folic acid cũng được dùng để giảm độc tính của methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate).'
        , 'monitoring': [
        'Hemoglobin, MCV (mean corpuscular volume) - theo dõi đáp ứng điều trị thiếu máu'
        , 'Nồng độ folate trong máu (nếu cần)',
        'Nồng độ vitamin B12 (thiếu B12 có thể che dấu bởi folic acid)',
        'Đáp ứng điều trị (giảm triệu chứng thiếu máu)',
        'Dấu hiệu dị ứng (hiếm)'], 'precautions': [
        'Dùng kèm vitamin B12 khi thiếu máu (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)'
        , 'Với thiếu máu: luôn kiểm tra B12 trước khi dùng folic acid',
        'Dự phòng dị tật ống thần kinh: bắt đầu trước khi có thai 1 tháng, tiếp tục trong 3 tháng đầu'
        ,
        'Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)',
        'Liều cao (>1mg/ngày) có thể che dấu thiếu B12',
        'An toàn trong thai kỳ và cho con bú', 'Hiếm khi có tác dụng phụ',
        'Thận trọng ở bệnh nhân ung thư (folic acid có thể kích thích tế bào ung thư)'
        ], 'pharmacokinetics': {'half_life': 'Không áp dụng (vitamin)', 'onset':
        'Vài ngày đến vài tuần (tác dụng tích tụ)', 'duration':
        'Phụ thuộc vào dự trữ trong cơ thể', 'protein_binding': 'Không đáng kể',
        'clearance': 'Thận (thải trừ qua nước tiểu), một phần dự trữ trong gan'
        }, 'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng',
        'black_box_warnings': None, 'drug_interactions': {'major': [{'drug':
        'Methotrexate', 'mechanism':
        'Folic acid đối kháng với tác dụng của methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate).'
        , 'effect':
        'Giảm hiệu quả methotrexate trong điều trị ung thư/viêm khớp',
        'management':
        'KHÔNG dùng folic acid cùng lúc với methotrexate trong điều trị ung thư/viêm khớp. Chỉ dùng folic acid để điều trị độc tính methotrexate, và phải dùng 24 giờ sau methotrexate.'
        }], 'moderate': [{'drug': 'Phenytoin', 'mechanism':
        'Folic acid có thể giảm nồng độ phenytoin trong máu.', 'effect':
        'Giảm nồng độ phenytoin, giảm hiệu quả chống động kinh, tăng nguy cơ co giật'
        , 'management':
        'Theo dõi nồng độ phenytoin khi bắt đầu hoặc ngừng folic acid. Có thể cần tăng liều phenytoin.'
        }, {'drug': 'Sulfasalazine', 'mechanism':
        'Sulfasalazine giảm hấp thu folic acid ở ruột.', 'effect':
        'Giảm hấp thu folic acid, tăng nguy cơ thiếu folate', 'management':
        'Bổ sung folic acid khi dùng sulfasalazine lâu dài. Theo dõi nồng độ folate.'
        }], 'minor': [{'drug': 'Chloramphenicol', 'mechanism':
        'Chloramphenicol có thể giảm đáp ứng với folic acid trong điều trị thiếu máu.'
        , 'effect': 'Giảm đáp ứng với folic acid', 'management':
        'Thận trọng. Theo dõi đáp ứng điều trị thiếu máu.'}, {'drug':
        'Vitamin B12', 'mechanism':
        'Folic acid có thể che dấu thiếu B12 (cải thiện thiếu máu nhưng không cải thiện tổn thương thần kinh).'
        , 'effect':
        'Che dấu thiếu B12, dẫn đến tổn thương thần kinh không được điều trị',
        'management':
        'Luôn kiểm tra B12 khi thiếu máu. Không dùng folic acid đơn độc mà không kiểm tra B12.'
        }]}, 'contraindications': {'tuyệt_đối': ['Dị ứng folic acid',
        'Ung thư đang điều trị bằng methotrexate (trừ khi dùng để điều trị độc tính methotrexate)'
        ], 'tương_đối': [
        'Ung thư (không điều trị) - folic acid có thể kích thích tế bào ung thư',
        'Thiếu B12 chưa được điều trị - folic acid có thể che dấu thiếu B12']},
        'pregnancy_lactation': {'fda_category': 'A', 'pregnancy_details':
        'Folic acid an toàn và cần thiết trong thai kỳ, đặc biệt quan trọng để dự phòng dị tật ống thần kinh (spina bifida, anencephaly). Dị tật ống thần kinh xảy ra trong tuần 3-4 của thai kỳ, trước khi nhiều phụ nữ biết mình có thai. Do đó, phụ nữ trong độ tuổi sinh đẻ nên bổ sung folic acid trước khi có thai. Khuyến cáo: 400-800 mcg/ngày trước và trong 3 tháng đầu thai kỳ. Phụ nữ có tiền sử dị tật ống thần kinh hoặc dùng một số thuốc (valproate, carbamazepine) cần liều cao hơn (4-5 mg/ngày).'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Folic acid bài tiết vào sữa mẹ. Nồng độ folic acid trong sữa mẹ phụ thuộc vào nồng độ folic acid của mẹ. Bổ sung folic acid cho mẹ giúp tăng nồng độ trong sữa mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Khuyến cáo: 500 mcg/ngày khi cho con bú. Phụ nữ thiếu folate cần bổ sung đủ để đảm bảo đủ folate cho trẻ.'
        }}, 'hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. Folic acid chủ yếu thải trừ qua thận, không chuyển hóa ở gan.'
        , 'moderate':
        'Không cần điều chỉnh liều. Folic acid chủ yếu thải trừ qua thận, không chuyển hóa ở gan.'
        , 'severe':
        'Không cần điều chỉnh liều. Folic acid chủ yếu thải trừ qua thận, không chuyển hóa ở gan.'
        , 'notes':
        'Folic acid chủ yếu thải trừ qua thận, một phần dự trữ trong gan. Suy gan không ảnh hưởng đáng kể đến nồng độ folic acid.'
        }, 'overdose_management': {'symptoms': [
        'Rất hiếm khi có triệu chứng quá liều (folic acid là vitamin tan trong nước, thải trừ qua nước tiểu)'
        , 'Phản ứng dị ứng (hiếm): phát ban, ngứa',
        'Che dấu thiếu B12 (với liều cao >1mg/ngày) - cải thiện thiếu máu nhưng không cải thiện tổn thương thần kinh'
        ], 'antidote': 'Không có antidote đặc hiệu. Điều trị hỗ trợ.',
        'treatment': ['Ngừng folic acid nếu có phản ứng dị ứng',
        'Điều trị phản ứng dị ứng: antihistamine nếu cần',
        'Kiểm tra B12 nếu nghi ngờ che dấu thiếu B12',
        'Theo dõi dấu hiệu sinh tồn'], 'monitoring':
        'Dấu hiệu phản ứng dị ứng, nồng độ B12 nếu nghi ngờ che dấu thiếu B12'},
        'reversal_agents': {'available': False, 'agents': []},
        'administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Hấp thu tốt trong cả hai trường hợp.',
        'timing':
        'Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Uống cùng thời điểm mỗi ngày để dễ nhớ. Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc).'
        }, 'iv': {'reconstitution':
        'Folic acid chủ yếu dùng đường uống. IV chỉ dùng trong trường hợp đặc biệt.'
        , 'infusion_rate': 'N/A - chủ yếu dùng đường uống', 'compatibility': [
        'N/A'], 'incompatibility': ['N/A'], 'notes':
        'Folic acid chủ yếu dùng đường uống. IV chỉ dùng trong trường hợp đặc biệt.'
        }}, 'references': {'primary_sources': [
        'FDA Drug Label - Folic Acid (Folate)',
        'CDC Guidelines - Folic Acid for Prevention of Neural Tube Defects',
        'American College of Obstetricians and Gynecologists (ACOG) - Folic Acid Supplementation'
        , 'UpToDate - Folic acid deficiency',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ], 'last_updated': '2025-02-04', 'evidence_level':
        'A - Dựa trên FDA drug labels, CDC/ACOG guidelines, và dữ liệu lâm sàng'}}}

__all__ = ['FOLATES_DRUGS']
