"""
Psychiatry Module
Diseases: Major Depression, Anxiety Disorder
"""

from typing import List
from diseases.data import Disease


PSYCHIATRY_DISEASES: List[Disease] = [
    Disease(
        id="major_depression",
        name="Major Depressive Disorder",
        name_vn="Trầm cảm",
        category="Psychiatry",
        definition="Trầm cảm là rối loạn tâm thần đặc trưng bởi cảm xúc buồn bã, mất hứng thú kéo dài, ảnh hưởng đến chức năng hàng ngày.",
        causes=[
            "Yếu tố sinh học: rối loạn chất dẫn truyền thần kinh (serotonin, norepinephrine)",
            "Yếu tố di truyền",
            "Yếu tố tâm lý: stress, sang chấn",
            "Bệnh mạn tính",
            "Thuốc: corticosteroid, interferon"
        ],
        symptoms=[
            "Cảm xúc buồn bã, trống rỗng",
            "Mất hứng thú, niềm vui",
            "Mệt mỏi, suy nhược",
            "Rối loạn giấc ngủ (mất ngủ hoặc ngủ nhiều)",
            "Thay đổi cảm giác ngon miệng",
            "Khó tập trung, quyết định",
            "Cảm giác tội lỗi, vô giá trị",
            "Ý nghĩ tự tử"
        ],
        diagnosis={
            "criteria": [
                "≥ 5 triệu chứng trong 2 tuần (theo DSM-5)",
                "Bao gồm: buồn bã hoặc mất hứng thú",
                "Ảnh hưởng chức năng hàng ngày",
                "Loại trừ: do chất, bệnh thực thể"
            ],
            "tests": [
                "Đánh giá lâm sàng (PHQ-9, BDI)",
                "Xét nghiệm: TSH, B12, folate (loại trừ nguyên nhân thực thể)",
                "Công thức máu"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị đa yếu tố: thuốc chống trầm cảm, liệu pháp tâm lý, thay đổi lối sống.",
            "medications": [
                "SSRI: Sertraline, Escitalopram, Fluoxetine (thuốc đầu tay)",
                "SNRI: Venlafaxine, Duloxetine",
                "TCA: Amitriptyline (nếu kháng SSRI)",
                "Bắt đầu liều thấp, tăng dần",
                "Dùng ít nhất 6-12 tháng sau khi đáp ứng"
            ],
            "procedures": [
                "Liệu pháp tâm lý: CBT (Cognitive Behavioral Therapy)",
                "ECT (Electroconvulsive Therapy) - nếu nặng, kháng thuốc",
                "Theo dõi sát nguy cơ tự tử"
            ]
        },
        prevention=[
            "Quản lý stress",
            "Tập thể dục",
            "Ngủ đủ giấc",
            "Hỗ trợ xã hội",
            "Điều trị sớm"
        ],
        complications=[
            "Tự tử",
            "Lạm dụng chất",
            "Rối loạn lo âu",
            "Ảnh hưởng công việc, gia đình",
            "Tử vong (do tự tử)"
        ],
        related_scores=["PHQ-9", "BDI", "HAM-D"],
        related_drugs=["Sertraline", "Escitalopram", "Fluoxetine", "Venlafaxine"],
        related_protocols=[],
        icd10_codes=["F32.9", "F32.0", "F32.1", "F32.2", "F33.9"]
    ),
    
    Disease(
        id="anxiety_disorder",
        name="Anxiety Disorder",
        name_vn="Rối loạn lo âu",
        category="Psychiatry",
        definition="Rối loạn lo âu là nhóm bệnh đặc trưng bởi lo âu, sợ hãi quá mức, ảnh hưởng đến cuộc sống hàng ngày.",
        causes=[
            "Yếu tố di truyền",
            "Yếu tố môi trường: stress, sang chấn",
            "Rối loạn chất dẫn truyền thần kinh",
            "Bệnh thực thể: cường giáp, rối loạn nhịp tim",
            "Thuốc: caffeine, steroid"
        ],
        symptoms=[
            "Lo âu, lo lắng quá mức",
            "Bồn chồn, căng thẳng",
            "Khó tập trung",
            "Rối loạn giấc ngủ",
            "Mệt mỏi",
            "Đánh trống ngực, khó thở",
            "Đổ mồ hôi, run tay",
            "Cơn hoảng sợ (panic attack)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lo âu kéo dài ≥ 6 tháng",
                "Ảnh hưởng chức năng hàng ngày",
                "Loại trừ: do chất, bệnh thực thể",
                "Phân loại: GAD, Panic disorder, Social anxiety, Phobia"
            ],
            "tests": [
                "Đánh giá lâm sàng (GAD-7)",
                "Xét nghiệm: TSH, ECG (loại trừ nguyên nhân thực thể)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị đa yếu tố: thuốc, liệu pháp tâm lý, thay đổi lối sống.",
            "medications": [
                "SSRI: Sertraline, Escitalopram (thuốc đầu tay)",
                "SNRI: Venlafaxine, Duloxetine",
                "Benzodiazepine: Alprazolam, Lorazepam (ngắn hạn, cơn cấp)",
                "Buspirone",
                "Beta-blocker: Propranolol (nếu triệu chứng thể chất)"
            ],
            "procedures": [
                "Liệu pháp tâm lý: CBT",
                "Thư giãn, thiền",
                "Tránh caffeine, rượu bia"
            ]
        },
        prevention=[
            "Quản lý stress",
            "Tập thể dục",
            "Ngủ đủ giấc",
            "Tránh caffeine, rượu bia",
            "Hỗ trợ xã hội"
        ],
        complications=[
            "Trầm cảm",
            "Lạm dụng chất",
            "Rối loạn giấc ngủ",
            "Ảnh hưởng công việc, xã hội"
        ],
        related_scores=["GAD-7", "PHQ-9"],
        related_drugs=["Sertraline", "Escitalopram", "Alprazolam", "Lorazepam", "Propranolol"],
        related_protocols=[],
        icd10_codes=["F41.9", "F41.0", "F41.1"]
    ),
]
