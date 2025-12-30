"""
Endocrinology Module
Diseases: Type 2 Diabetes, Hyperthyroidism, Hypothyroidism
"""

from typing import List
from diseases.data import Disease


ENDOCRINOLOGY_DISEASES: List[Disease] = [
    Disease(
        id="diabetes_type2",
        name="Type 2 Diabetes Mellitus",
        name_vn="Đái tháo đường type 2",
        category="Endocrinology",
        definition="Đái tháo đường type 2 là rối loạn chuyển hóa đặc trưng bởi tăng đường huyết do kháng insulin và/hoặc thiếu insulin tương đối.",
        causes=[
            "Kháng insulin",
            "Thiếu insulin tương đối",
            "Yếu tố nguy cơ: béo phì, ít vận động, tiền sử gia đình, tuổi cao"
        ],
        symptoms=[
            "Tiểu nhiều (polyuria)",
            "Khát nhiều (polydipsia)",
            "Ăn nhiều (polyphagia)",
            "Sụt cân",
            "Mệt mỏi",
            "Nhìn mờ",
            "Vết thương lâu lành"
        ],
        diagnosis={
            "criteria": [
                "HbA1c ≥ 6.5%",
                "Đường huyết đói ≥ 126 mg/dL (≥ 7.0 mmol/L)",
                "Đường huyết ngẫu nhiên ≥ 200 mg/dL (≥ 11.1 mmol/L) + triệu chứng",
                "OGTT: đường huyết 2h ≥ 200 mg/dL"
            ],
            "tests": [
                "HbA1c",
                "Đường huyết đói",
                "OGTT (nếu cần)",
                "Chức năng thận",
                "Lipid máu",
                "Microalbumin niệu"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị đa yếu tố: kiểm soát đường huyết, huyết áp, lipid, phòng ngừa biến chứng.",
            "medications": [
                "Metformin (thuốc đầu tay)",
                "SGLT2 inhibitor (nếu có bệnh tim/thận)",
                "GLP-1 agonist (nếu có bệnh tim)",
                "DPP-4 inhibitor",
                "Sulfonylurea",
                "Insulin (nếu cần)"
            ],
            "procedures": [
                "Theo dõi đường huyết tại nhà",
                "Khám mắt định kỳ",
                "Khám bàn chân định kỳ"
            ]
        },
        prevention=[
            "Giảm cân (nếu thừa cân)",
            "Chế độ ăn lành mạnh",
            "Tập thể dục đều đặn",
            "Kiểm tra đường huyết định kỳ"
        ],
        complications=[
            "Bệnh võng mạc đái tháo đường",
            "Bệnh thận đái tháo đường",
            "Bệnh thần kinh đái tháo đường",
            "Bệnh mạch máu (bàn chân đái tháo đường)",
            "Bệnh tim mạch",
            "Nhiễm toan ceton (hiếm ở type 2)"
        ],
        related_scores=["HbA1c", "Fasting Glucose"],
        related_drugs=["Metformin", "SGLT2 inhibitor", "GLP-1 agonist", "Insulin"],
        related_protocols=[],
        icd10_codes=["E11.9", "E11.65", "E11.21", "E11.40"]
    ),
    
    Disease(
        id="hyperthyroidism",
        name="Hyperthyroidism",
        name_vn="Cường giáp",
        category="Endocrinology",
        definition="Cường giáp là tình trạng tăng sản xuất hormone tuyến giáp, dẫn đến tăng chuyển hóa.",
        causes=[
            "Basedow (Graves' disease) - nguyên nhân chính",
            "Bướu giáp đa nhân độc",
            "Viêm giáp (thyroiditis)",
            "U tuyến giáp độc",
            "Quá liều hormone tuyến giáp"
        ],
        symptoms=[
            "Nhịp tim nhanh, đánh trống ngực",
            "Sụt cân dù ăn nhiều",
            "Ra mồ hôi nhiều",
            "Run tay",
            "Mệt mỏi, yếu cơ",
            "Khó ngủ",
            "Tiêu chảy",
            "Mắt lồi (nếu Basedow)"
        ],
        diagnosis={
            "criteria": [
                "TSH giảm, T3/T4 tăng",
                "Triệu chứng lâm sàng",
                "Siêu âm tuyến giáp",
                "Xạ hình tuyến giáp (nếu cần)"
            ],
            "tests": [
                "TSH, T3, T4",
                "Anti-TPO, Anti-Tg (nếu Basedow)",
                "TRAb (Thyroid Receptor Antibody) - nếu Basedow",
                "Siêu âm tuyến giáp",
                "Xạ hình tuyến giáp (nếu cần)"
            ],
            "imaging": [
                "Siêu âm tuyến giáp",
                "Xạ hình tuyến giáp"
            ]
        },
        treatment={
            "general": "Điều trị theo ATA guidelines. Mục tiêu: bình thường hóa hormone tuyến giáp, giảm triệu chứng.",
            "medications": [
                "Methimazole hoặc Propylthiouracil (PTU) - ức chế sản xuất hormone",
                "Beta-blocker (Propranolol) - giảm triệu chứng",
                "I-131 (Radioactive Iodine) - điều trị dứt điểm",
                "Corticosteroid (nếu cơn cường giáp cấp)"
            ],
            "procedures": [
                "Phẫu thuật cắt tuyến giáp (nếu có chỉ định)",
                "Theo dõi chức năng tuyến giáp định kỳ"
            ]
        },
        prevention=[
            "Điều trị sớm",
            "Theo dõi định kỳ",
            "Tránh quá liều hormone tuyến giáp"
        ],
        complications=[
            "Cơn cường giáp cấp (thyroid storm)",
            "Rối loạn nhịp tim (rung nhĩ)",
            "Suy tim",
            "Loãng xương",
            "Tử vong (nếu cơn cường giáp cấp)"
        ],
        related_scores=["TSH", "T3", "T4", "TRAb"],
        related_drugs=["Methimazole", "Propylthiouracil", "Propranolol", "I-131"],
        related_protocols=["Hyperthyroidism Management"],
        icd10_codes=["E05.9", "E05.0", "E05.1"]
    ),
    
    Disease(
        id="hypothyroidism",
        name="Hypothyroidism",
        name_vn="Suy giáp",
        category="Endocrinology",
        definition="Suy giáp là tình trạng giảm sản xuất hormone tuyến giáp, dẫn đến giảm chuyển hóa.",
        causes=[
            "Hashimoto (viêm giáp tự miễn) - nguyên nhân chính",
            "Sau phẫu thuật cắt tuyến giáp",
            "Sau điều trị I-131",
            "Thiếu i-ốt",
            "Thuốc: Lithium, Amiodarone"
        ],
        symptoms=[
            "Mệt mỏi, suy nhược",
            "Tăng cân",
            "Lạnh",
            "Da khô, tóc rụng",
            "Táo bón",
            "Trầm cảm",
            "Nhịp tim chậm",
            "Phù niêm"
        ],
        diagnosis={
            "criteria": [
                "TSH tăng, T4 giảm",
                "Triệu chứng lâm sàng",
                "Anti-TPO, Anti-Tg (nếu Hashimoto)"
            ],
            "tests": [
                "TSH, T4",
                "T3 (nếu cần)",
                "Anti-TPO, Anti-Tg",
                "Siêu âm tuyến giáp"
            ],
            "imaging": [
                "Siêu âm tuyến giáp"
            ]
        },
        treatment={
            "general": "Điều trị thay thế hormone tuyến giáp. Mục tiêu: bình thường hóa TSH, giảm triệu chứng.",
            "medications": [
                "Levothyroxine (T4) - thuốc đầu tay",
                "Bắt đầu liều thấp, tăng dần",
                "Theo dõi TSH sau 4-6 tuần",
                "Dùng suốt đời"
            ],
            "procedures": [
                "Theo dõi TSH định kỳ (6-12 tháng/lần)",
                "Điều chỉnh liều theo TSH"
            ]
        },
        prevention=[
            "Bổ sung i-ốt (nếu thiếu)",
            "Theo dõi sau phẫu thuật/điều trị tuyến giáp",
            "Điều trị sớm"
        ],
        complications=[
            "Hôn mê phù niêm (myxedema coma) - nguy hiểm",
            "Suy tim",
            "Trầm cảm",
            "Loãng xương (nếu quá liều)",
            "Tử vong (nếu hôn mê phù niêm)"
        ],
        related_scores=["TSH", "T4"],
        related_drugs=["Levothyroxine"],
        related_protocols=["Hypothyroidism Management"],
        icd10_codes=["E03.9", "E03.0", "E03.1"]
    ),
]
