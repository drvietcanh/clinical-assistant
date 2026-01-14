"""Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data"""

# Vitamin B12s

VITAMIN_B12S_DRUGS = {
    "Vitamin B12": {'group': 'Vitamins/Supplements - Vitamin B12',vietnamese_name':
        'Vitamin B12, Cyanocobalamin, Methylcobalamin', 'administration': ['PO',
        'IM', 'SC'],
        'indications': ['Thiếu máu hồng cầu to', 'Bệnh thần kinh do thiếu B12',
        'Dự phòng thiếu B12', 'Sau phẫu thuật cắt dạ dày'],
        'contraindications':
        ['Dị ứng vitamin B12/cobalt',
        "Leber's disease (thoái hóa thần kinh thị giác di truyền)"],
        'dosage':
        {'adult_po': '1,000-2,000mcg x 1 lần/ngày', 'adult_im_loading':
        '1,000mcg IM mỗi ngày x 1 tuần, sau đó mỗi tuần x 4 tuần',
        'adult_im_maintenance': '1,000mcg IM mỗi tháng',
        'adult_deficiency_severe':
        '1,000mcg IM mỗi ngày x 1-2 tuần, sau đó mỗi tuần x 4 tuần', 'notes':
        'IM cho thiếu máu nặng. PO cho thiếu nhẹ hoặc dự phòng'},renal_adjustment': {'normal': 'Không đổi', '30_60': 'Không đổi',
        'under_30': 'Không đổi'},side_effects': ['Phản ứng tại chỗ tiêm (IM)',
        'Ban da (hiếm)', 'Phản ứng dị ứng (hiếm)',
        'Tăng đông máu (liều rất cao)'],interactions': [
        'Acid folic: che dấu thiếu B12',
        'Chloramphenicol: giảm đáp ứng với B12',
        'Metformin: giảm nồng độ B12 (dùng lâu dài)',
        'PPI/H2 blocker: giảm hấp thu B12'],pregnancy':
        'A - An toàn, cần thiết', 'mechanism_of_action':
        'Vitamin B12 (cobalamin) là coenzyme cần thiết cho tổng hợp DNA, methyl transfer, và chuyển hóa homocysteine thành methionine. Vitamin B12 kết hợp với folic acid để tổng hợp DNA, đặc biệt quan trọng cho sự phát triển tế bào hồng cầu. Thiếu B12 gây thiếu máu hồng cầu to (megaloblastic anemia) và tổn thương thần kinh (neuropathy, dementia, myelopathy). Vitamin B12 được hấp thu qua đường tiêu hóa nhờ intrinsic factor (từ dạ dày), sau đó dự trữ trong gan. Thiếu B12 thường do thiếu intrinsic factor (pernicious anemia, cắt dạ dày), thiếu hấp thu (bệnh Crohn, cắt ruột), hoặc thiếu trong chế độ ăn (ăn chay). Vitamin B12 có 2 dạng: cyanocobalamin (tổng hợp) và methylcobalamin (tự nhiên).'
        , 'monitoring': [
        'Hemoglobin, MCV (mean corpuscular volume) - theo dõi đáp ứng điều trị thiếu máu'
        , 'Nồng độ B12 trong máu (mục tiêu: >300 pg/mL)',
        'Methylmalonic acid (MMA) - tăng khi thiếu B12',
        'Homocysteine - tăng khi thiếu B12',
        'Dấu hiệu tổn thương thần kinh (tê bì, yếu chân tay, mất trí nhớ)',
        'Đáp ứng điều trị (giảm triệu chứng thiếu máu và thần kinh)'],precautions': [
        'IM cho thiếu máu nặng hoặc thiếu hấp thu (nhanh hơn, hiệu quả hơn PO)',
        'PO cho thiếu nhẹ hoặc dự phòng (cần liều cao hơn)',
        'Thiếu B12 có thể che dấu bởi folic acid - luôn kiểm tra B12 khi thiếu máu'
        , 'Thiếu B12 không điều trị có thể gây tổn thương thần kinh vĩnh viễn',
        'An toàn trong thai kỳ và cho con bú',
        "Thận trọng ở bệnh nhân Leber's disease (thoái hóa thần kinh thị giác)",
        'Theo dõi đáp ứng điều trị (tăng hemoglobin, giảm triệu chứng thần kinh)',
        'Dùng kèm folic acid khi thiếu máu (nhưng không thay thế B12)'],pharmacokinetics': {'half_life': '6 ngày (dự trữ trong gan)', 'onset':
        'Vài ngày đến vài tuần (tác dụng tích tụ)', 'duration':
        'Dự trữ trong gan kéo dài 3-5 năm', 'protein_binding':
        'Gắn với transcobalamin', 'clearance':
        'Dự trữ trong gan, thải trừ qua mật và nước tiểu'},storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng, tránh nhiệt độ cao',
        'black_box_warnings': None, 'contraindications_detail': {
        'tuyệt_đối': ['Dị ứng vitamin B12 hoặc cobalt',
        "Leber's disease (thoái hóa thần kinh thị giác di truyền) - B12 có thể làm nặng bệnh"
        ],tương_đối': [
        'Thiếu B12 do thiếu intrinsic factor (pernicious anemia) - cần dùng IM, không dùng PO'
        , 'Thiếu hấp thu ở ruột - cần dùng IM, không dùng PO']},drug_interactions': {'major': [],moderate': [{'drug': 'Metformin', 'mechanism':
        'Metformin dùng lâu dài có thể giảm hấp thu vitamin B12 ở ruột, dẫn đến thiếu B12.'
        , 'effect': 'Giảm nồng độ B12, tăng nguy cơ thiếu B12', 'management':
        'Theo dõi nồng độ B12 định kỳ ở bệnh nhân dùng metformin lâu dài (>2 năm). Bổ sung B12 nếu thiếu.'
        }, {'drug':
        'PPI (Omeprazole, Pantoprazole), H2 blockers (Ranitidine, Famotidine)',
        'mechanism':
        'Giảm acid dạ dày, giảm tách B12 khỏi protein trong thức ăn, giảm hấp thu.'
        , 'effect': 'Giảm hấp thu B12, tăng nguy cơ thiếu B12', 'management':
        'Theo dõi nồng độ B12 định kỳ ở bệnh nhân dùng PPI/H2 blocker lâu dài (>2 năm). Bổ sung B12 nếu thiếu.'
        }, {'drug': 'Folic acid', 'mechanism':
        'Folic acid có thể che dấu thiếu B12 (cải thiện thiếu máu nhưng không cải thiện tổn thương thần kinh).'
        , 'effect':
        'Che dấu thiếu B12, dẫn đến tổn thương thần kinh không được điều trị',
        'management':
        'Luôn kiểm tra B12 khi thiếu máu. Không dùng folic acid đơn độc mà không kiểm tra B12.'
        }],minor': [{'drug': 'Chloramphenicol', 'mechanism':
        'Chloramphenicol có thể giảm đáp ứng với B12 trong điều trị thiếu máu.',
        'effect': 'Giảm đáp ứng với B12', 'management':
        'Thận trọng. Theo dõi đáp ứng điều trị thiếu máu.'}]},contraindications': {'tuyệt_đối': ['Dị ứng vitamin B12 hoặc cobalt',
        "Leber's disease (thoái hóa thần kinh thị giác di truyền) - B12 có thể làm nặng bệnh"
        ],tương_đối': [
        'Thiếu B12 do thiếu intrinsic factor (pernicious anemia) - cần dùng IM, không dùng PO'
        , 'Thiếu hấp thu ở ruột - cần dùng IM, không dùng PO']},pregnancy_lactation': {'fda_category': 'A', 'pregnancy_details':
        'Vitamin B12 an toàn và cần thiết trong thai kỳ. Thiếu B12 trong thai kỳ có thể gây thiếu máu ở mẹ, chậm phát triển thần kinh ở thai nhi, và các biến chứng khác. Nhu cầu B12 tăng trong thai kỳ. Khuyến cáo: 2.6 mcg/ngày trong thai kỳ. Phụ nữ thiếu B12 cần bổ sung đủ trước và trong thai kỳ.'
        , 'lactation': {'safety': 'Compatible', 'details':
        'Vitamin B12 bài tiết vào sữa mẹ. Nồng độ B12 trong sữa mẹ phụ thuộc vào nồng độ B12 của mẹ. Thiếu B12 ở mẹ có thể dẫn đến thiếu B12 ở trẻ bú mẹ.'
        , 'recommendation':
        'Có thể dùng khi cho con bú. Khuyến cáo: 2.8 mcg/ngày khi cho con bú. Phụ nữ thiếu B12 cần bổ sung đủ để đảm bảo đủ B12 cho trẻ.'
        }},hepatic_adjustment': {'mild':
        'Không cần điều chỉnh liều. B12 được dự trữ trong gan, nhưng suy gan nhẹ không ảnh hưởng đáng kể.'
        , 'moderate':
        'Không cần điều chỉnh liều. B12 được dự trữ trong gan, nhưng suy gan trung bình không ảnh hưởng đáng kể.'
        , 'severe':
        'Không cần điều chỉnh liều. B12 được dự trữ trong gan, nhưng suy gan nặng không ảnh hưởng đáng kể đến nồng độ B12.'
        , 'notes':
        'Vitamin B12 được dự trữ trong gan. Suy gan không ảnh hưởng đáng kể đến nồng độ B12 trong máu. Tuy nhiên, suy gan có thể ảnh hưởng đến dự trữ B12.'
        },overdose_management': {'symptoms': [
        'Rất hiếm khi có triệu chứng quá liều (B12 là vitamin tan trong nước, thải trừ qua nước tiểu)'
        , 'Phản ứng dị ứng (hiếm): phát ban, ngứa, sốc phản vệ',
        'Tăng đông máu (với liều rất cao, hiếm)',
        'Phản ứng tại chỗ tiêm (IM): đau, sưng, đỏ'],antidote':
        'Không có antidote đặc hiệu. Điều trị hỗ trợ.', 'treatment': [
        'Ngừng B12 nếu có phản ứng dị ứng', 'Điều trị phản ứng dị ứng:',
        '  - Antihistamine nếu phản ứng nhẹ', '  - Epinephrine nếu sốc phản vệ',
        '  - Corticosteroid nếu phản ứng nặng', 'Theo dõi dấu hiệu sinh tồn',
        'Điều trị phản ứng tại chỗ tiêm: chườm lạnh, giảm đau'],monitoring':
        'Dấu hiệu phản ứng dị ứng, dấu hiệu sinh tồn, phản ứng tại chỗ tiêm'},reversal_agents': {'available': False, 'agents': [],notes':
        'Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng.'},administration_instructions': {'oral': {'with_food':
        'Có thể uống với hoặc không thức ăn. Hấp thu tốt trong cả hai trường hợp.',
        'timing':
        'Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Uống cùng thời điểm mỗi ngày để dễ nhớ.'
        },im': {'reconstitution':
        'Vitamin B12 IM thường có sẵn dạng tiêm sẵn. Không cần pha.',
        'injection_site': 'Tiêm bắp (deltoid hoặc gluteal). Xoay vị trí tiêm.',
        'injection_rate': 'Tiêm chậm, đều', 'notes':
        'IM cho thiếu máu nặng hoặc thiếu hấp thu. Tiêm bắp, xoay vị trí tiêm. Theo dõi phản ứng tại chỗ.'
        },sc': {'reconstitution':
        'Vitamin B12 SC thường có sẵn dạng tiêm sẵn. Không cần pha.',
        'injection_site': 'Tiêm dưới da (bụng, đùi). Xoay vị trí tiêm.',
        'injection_rate': 'Tiêm chậm, đều', 'notes':
        'SC có thể dùng thay cho IM. Tiêm dưới da, xoay vị trí tiêm.'},iv': {
        'reconstitution': 'Không khuyến cáo dùng IV thường quy',
        'infusion_rate': 'N/A', 'compatibility': ['N/A'],incompatibility': [
        'N/A'],notes':
        'Vitamin B12 chủ yếu dùng PO, IM, hoặc SC. IV chỉ dùng trong trường hợp đặc biệt.'
        }},references': {'primary_sources': [
        'FDA Drug Label - Vitamin B12 (Cyanocobalamin, Methylcobalamin)',
        'UpToDate - Vitamin B12 deficiency',
        'American Society of Hematology Guidelines - Vitamin B12 Deficiency',
        "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
        ],evidence_level':
        'A - Dựa trên FDA drug labels, ASH guidelines, và dữ liệu lâm sàng'},
        "black_box_warnings": None,
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Hemoglobin, MCV", "B12 levels (target: >300 pg/mL)", "MMA (methylmalonic acid)", "Homocysteine", "Clinical signs of neuropathy"]
        },
        "guideline_tags": [
            "ASH Guidelines - Vitamin B12 Deficiency",
            "FDA Drug Information - Vitamin B12",
            "UpToDate - Vitamin B12 deficiency",
            "ACOG Guidelines - Vitamin B12 in Pregnancy"
        ],
}}

__all__ = ['VITAMIN_B12S_DRUGS']
