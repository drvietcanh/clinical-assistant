"""
Nephrology Module
Diseases: AKI, CKD
"""

from typing import List
from diseases.data import Disease


NEPHROLOGY_DISEASES: List[Disease] = [
    Disease(
        id="aki",
        name="Acute Kidney Injury",
        name_vn="Tổn thương thận cấp (AKI)",
        category="Nephrology",
        definition="AKI là tình trạng suy giảm chức năng thận đột ngột trong vài giờ đến vài ngày.",
        causes=[
            "Prerenal: Giảm tưới máu thận (mất nước, suy tim, hạ huyết áp)",
            "Renal: Tổn thương thận (viêm cầu thận, hoại tử ống thận cấp)",
            "Postrenal: Tắc nghẽn đường tiết niệu (sỏi, u)"
        ],
        symptoms=[
            "Giảm lượng nước tiểu",
            "Phù",
            "Mệt mỏi",
            "Buồn nôn, nôn",
            "Lú lẫn",
            "Khó thở (do ứ dịch)"
        ],
        diagnosis={
            "criteria": [
                "Creatinine tăng ≥ 0.3 mg/dL trong 48h",
                "Creatinine tăng ≥ 1.5 lần baseline",
                "Lượng nước tiểu < 0.5 ml/kg/h trong 6h"
            ],
            "tests": [
                "Creatinine, BUN",
                "Điện giải (Na, K)",
                "Phân tích nước tiểu",
                "Siêu âm thận"
            ],
            "imaging": [
                "Siêu âm thận",
                "CT ổ bụng (nếu nghi ngờ tắc nghẽn)"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân. Mục tiêu: phục hồi chức năng thận, điều chỉnh rối loạn điện giải.",
            "medications": [
                "Điều chỉnh rối loạn điện giải",
                "Lợi tiểu (nếu phù, suy tim)",
                "Tránh thuốc độc thận (NSAID, aminoglycoside)"
            ],
            "procedures": [
                "Bù dịch (nếu prerenal)",
                "Lọc máu (nếu nặng, ure cao, toan máu, phù phổi)"
            ]
        },
        prevention=[
            "Tránh mất nước",
            "Tránh thuốc độc thận",
            "Theo dõi chức năng thận khi dùng thuốc",
            "Điều trị sớm nhiễm trùng"
        ],
        complications=[
            "Suy thận mạn",
            "Rối loạn điện giải",
            "Toan máu",
            "Phù phổi",
            "Tử vong"
        ],
        related_scores=["RIFLE", "AKIN", "KDIGO AKI Stage"],
        related_drugs=["Furosemide", "Dopamine"],
        related_protocols=["AKI Management"],
        icd10_codes=["N17.9", "N19"]
    ),
    
    Disease(
        id="chronic_kidney_disease",
        name="Chronic Kidney Disease",
        name_vn="Suy thận mạn tính (CKD)",
        category="Nephrology",
        definition="CKD là tình trạng suy giảm chức năng thận mạn tính, kéo dài ≥ 3 tháng, phổ biến tại Việt Nam.",
        causes=[
            "Đái tháo đường (nguyên nhân chính)",
            "Tăng huyết áp",
            "Viêm cầu thận",
            "Bệnh thận đa nang",
            "Bệnh thận do thuốc",
            "Bệnh thận do tắc nghẽn"
        ],
        symptoms=[
            "Giai đoạn sớm: thường không có triệu chứng",
            "Giai đoạn muộn: mệt mỏi, phù, buồn nôn, ngứa",
            "Thiếu máu",
            "Xương yếu",
            "Tăng huyết áp"
        ],
        diagnosis={
            "criteria": [
                "eGFR < 60 ml/min/1.73m² hoặc tổn thương thận ≥ 3 tháng",
                "Phân loại theo KDIGO: G1-G5 (theo eGFR), A1-A3 (theo albumin niệu)"
            ],
            "tests": [
                "Creatinine, eGFR",
                "Albumin niệu (UACR)",
                "Chức năng thận, điện giải",
                "Công thức máu (thiếu máu)",
                "Siêu âm thận"
            ],
            "imaging": [
                "Siêu âm thận",
                "CT thận (nếu cần)"
            ]
        },
        treatment={
            "general": "Điều trị theo KDIGO guidelines. Mục tiêu: làm chậm tiến triển, điều trị biến chứng, chuẩn bị lọc máu/ghép thận.",
            "medications": [
                "ACE inhibitor hoặc ARB (nếu có protein niệu)",
                "Kiểm soát huyết áp (< 130/80 mmHg)",
                "Kiểm soát đường huyết (nếu đái tháo đường)",
                "Statin",
                "Điều chỉnh rối loạn điện giải",
                "Erythropoietin (nếu thiếu máu)"
            ],
            "procedures": [
                "Lọc máu (nếu CKD giai đoạn 5)",
                "Ghép thận (nếu phù hợp)",
                "Tạo cầu nối động-tĩnh mạch (AV fistula) - chuẩn bị lọc máu"
            ]
        },
        prevention=[
            "Kiểm soát đái tháo đường",
            "Kiểm soát huyết áp",
            "Tránh thuốc độc thận",
            "Theo dõi chức năng thận định kỳ"
        ],
        complications=[
            "Suy thận giai đoạn cuối (ESRD)",
            "Thiếu máu",
            "Bệnh xương do thận",
            "Tăng huyết áp",
            "Bệnh tim mạch",
            "Tử vong"
        ],
        related_scores=["eGFR", "CKD Stage", "UACR"],
        related_drugs=["ACE Inhibitor", "ARB", "Erythropoietin", "Furosemide"],
        related_protocols=["Suy thận mạn tính (CKD)"],
        icd10_codes=["N18.9", "N18.1", "N18.2", "N18.3", "N18.4", "N18.5"]
    ),
]
