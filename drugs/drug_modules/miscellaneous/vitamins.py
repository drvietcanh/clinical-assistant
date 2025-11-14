"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology"""

# Vitamins

VITAMINS_DRUGS = {
    "Folic Acid": {'group': 'Hematology - Vitamin', 'vietnamese_name': 'Acid Folic',
        'administration': ['PO'], 'indications': ['Thiếu máu do thiếu folate',
        'Dự phòng dị tật ống thần kinh trong thai kỳ',
        'Bệnh hồng cầu hình liềm', 'Đang dùng methotrexate'],
        'contraindications': ['Dị ứng'], 'dosage': {'adult_deficiency':
        '1-5mg x 1 lần/ngày', 'pregnancy': '0.4-0.8mg x 1 lần/ngày',
        'methotrexate': '5-10mg/tuần (24h sau methotrexate)', 'notes':
        'Dùng kèm vitamin B12 khi thiếu máu'}, 'side_effects': [
        'Hiếm khi có tác dụng phụ', 'Phản ứng dị ứng (hiếm)'], 'interactions':
        [
        'Methotrexate: giảm hiệu quả methotrexate (nhưng dùng để giảm độc tính)',
        'Phenytoin: giảm nồng độ phenytoin'], 'pregnancy':
        'A - Khuyến nghị dùng trong thai kỳ', 'mechanism_of_action':
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
        'black_box_warnings': None, 'drug_interactions': {'moderate': [{'drug':
        'Methotrexate', 'mechanism':
        'Folic acid giảm hiệu quả methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate)'
        , 'effect':
        'Giảm hiệu quả methotrexate (nhưng dùng để giảm độc tính methotrexate)',
        'management':
        'Dùng folic acid 24 giờ sau methotrexate (không dùng cùng lúc). Theo dõi đáp ứng điều trị methotrexate'
        }, {'drug': 'Phenytoin', 'mechanism':
        'Folic acid giảm nồng độ phenytoin (cơ chế chưa rõ)', 'effect':
        'Giảm nồng độ phenytoin, giảm hiệu quả chống co giật', 'management':
        'Theo dõi nồng độ phenytoin, có thể cần tăng liều phenytoin'}]},
        'contraindications': {'tuyệt_đối': ['Dị ứng folic acid'], 'tương_đối':
        ['Ung thư - thận trọng (folic acid có thể kích thích tế bào ung thư)',
        'Thiếu vitamin B12 chưa được điều trị - thận trọng (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)'
        ]}, 'pregnancy_lactation': {'fda_category': 'A', 'pregnancy_details':
        'Khuyến nghị dùng trong thai kỳ. Folic acid rất quan trọng cho sự phát triển bình thường của ống thần kinh trong thai kỳ (tuần 3-4), giúp ngăn ngừa dị tật ống thần kinh (spina bifida, anencephaly). Nên bắt đầu trước khi có thai 1 tháng và tiếp tục trong 3 tháng đầu thai kỳ. Liều dự phòng: 0.4-0.8mg/ngày. Liều điều trị thiếu máu: 1-5mg/ngày.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Folic acid bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Folic acid trong sữa mẹ có lợi cho trẻ.'
        , 'recommendation':
        'Có thể dùng an toàn khi cho con bú. Liều thường dùng (0.4-5mg/ngày) an toàn cho trẻ bú mẹ'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi liều', 'moderate':
        'Không đổi liều', 'severe': 'Không đổi liều', 'notes':
        'Folic acid là vitamin, không chuyển hóa ở gan. Suy gan không ảnh hưởng đến folic acid'
        }, 'overdose_management': {'symptoms': [
        'Hiếm khi có triệu chứng (folic acid ít độc)', 'Phản ứng dị ứng (hiếm)',
        'Có thể che dấu thiếu B12 nếu dùng liều cao (>1mg/ngày)'], 'antidote':
        'Không có thuốc giải độc đặc hiệu', 'treatment': [
        'Ngừng thuốc nếu có phản ứng dị ứng',
        'Điều trị hỗ trợ: Truyền dịch nếu cần',
        'Kiểm tra nồng độ vitamin B12 nếu dùng liều cao lâu dài',
        'Điều trị dị ứng nếu có (antihistamine, corticosteroid)'], 'monitoring':
        'Triệu chứng lâm sàng, dấu hiệu dị ứng, nồng độ vitamin B12 (nếu dùng liều cao lâu dài)'
        }, 'reversal_agents': {'available': False, 'agents': None, 'notes':
        'Không có thuốc giải độc đặc hiệu. Folic acid ít độc, hiếm khi cần điều trị đặc biệt'
        }, 'administration_instructions': {'oral': {'with_food':
        'Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ (nếu có)'
        , 'timing':
        'Với thiếu máu: 1-5mg x 1 lần/ngày. Với dự phòng dị tật ống thần kinh: 0.4-0.8mg x 1 lần/ngày (bắt đầu trước khi có thai 1 tháng, tiếp tục trong 3 tháng đầu). Với methotrexate: 5-10mg/tuần (dùng 24 giờ sau methotrexate, không dùng cùng lúc)'
        , 'notes':
        'Dùng kèm vitamin B12 khi thiếu máu (folic acid có thể che dấu thiếu B12). Với thiếu máu: luôn kiểm tra B12 trước khi dùng folic acid. Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)'
        }}, 'references': {'primary_sources': ['FDA Drug Label - Folic Acid',
        'UpToDate - Folic acid drug information',
        'CDC Guidelines for folic acid supplementation in pregnancy',
        'WHO Guidelines for folic acid supplementation',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics"],
        'last_updated': '2025-02-04', 'evidence_level':
        'High - Guidelines dựa trên chứng cứ từ CDC, WHO và FDA'}}}

__all__ = ['VITAMINS_DRUGS']
