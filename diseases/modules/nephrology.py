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
            "general": "Điều trị theo KDIGO 2025 guidelines. Mục tiêu: làm chậm tiến triển, điều trị biến chứng, chuẩn bị lọc máu/ghép thận. Ưu tiên thuốc có lợi ích thận và tim mạch.",
            "medications": [
                "ACE inhibitor hoặc ARB (nếu có protein niệu hoặc albumin niệu) - mục tiêu UACR <30 mg/g",
                "SGLT2 inhibitor (Dapagliflozin, Empagliflozin, Canagliflozin) - cho CKD với eGFR ≥20 ml/min/1.73m² và albumin niệu ≥200 mg/g, bất kể có đái tháo đường hay không",
                "Finerenone (MRA) - cho CKD type 2 diabetes với albumin niệu ≥30 mg/g và eGFR ≥25 ml/min/1.73m²",
                "Kiểm soát huyết áp (< 130/80 mmHg) - theo ACC/AHA 2025",
                "Kiểm soát đường huyết (nếu đái tháo đường) - HbA1c <7%",
                "Statin - cho tất cả CKD",
                "Điều chỉnh rối loạn điện giải (phosphorus, PTH)",
                "Erythropoietin (nếu thiếu máu và Hb <10 g/dL)"
            ],
            "procedures": [
                "Lọc máu (nếu CKD giai đoạn 5, eGFR <15 ml/min/1.73m² hoặc có chỉ định)",
                "Ghép thận (nếu phù hợp)",
                "Tạo cầu nối động-tĩnh mạch (AV fistula) - chuẩn bị lọc máu sớm",
                "Theo dõi định kỳ: eGFR, UACR, huyết áp, đường huyết"
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
        related_scores=["eGFR", "CKD Stage", "UACR", "KDIGO Risk Categories"],
        related_drugs=["ACE Inhibitor", "ARB", "SGLT2 inhibitor", "Finerenone", "Erythropoietin", "Furosemide"],
        related_protocols=["Suy thận mạn tính (CKD)"],
        icd10_codes=["N18.9", "N18.1", "N18.2", "N18.3", "N18.4", "N18.5"]
    ),

    Disease(
        id="post_strep_glomerulonephritis",
        name="Post-streptococcal Acute Glomerulonephritis",
        name_vn="Viêm cầu thận cấp sau nhiễm liên cầu",
        category="Nephrology",
        definition="Viêm cầu thận cấp sau nhiễm liên cầu xảy ra sau viêm họng/da do liên cầu beta tan huyết nhóm A, thường ở trẻ em.",
        causes=[
            "Nhiễm Streptococcus nhóm A (họng, da) 1-3 tuần trước",
            "Phản ứng miễn dịch gây lắng đọng phức hợp miễn dịch tại cầu thận"
        ],
        symptoms=[
            "Phù (mi mắt, chân)",
            "Tăng huyết áp",
            "Tiểu ít, nước tiểu sậm, có máu",
            "Đôi khi đau đầu, khó thở"
        ],
        diagnosis={
            "criteria": [
                "Tiền sử nhiễm liên cầu gần đây",
                "Nước tiểu: hồng cầu, trụ hồng cầu, protein niệu",
                "C3 giảm, ASO tăng",
                "Creatinine tăng nhẹ"
            ],
            "tests": [
                "Tổng phân tích nước tiểu",
                "C3, C4, ASO",
                "Creatinine, điện giải",
                "Huyết áp, cân nặng theo dõi phù"
            ],
            "imaging": [
                "Siêu âm thận (thường bình thường hoặc to nhẹ)"
            ]
        },
        treatment={
            "general": "Hỗ trợ là chính, đa số tự hồi phục; điều trị tăng huyết áp, phù, loại bỏ ổ nhiễm.",
            "medications": [
                "Lợi tiểu (Furosemide) nếu phù/nhiều nước",
                "Hạ áp: ACEi/ARB thận trọng nếu cần",
                "Kháng sinh nếu còn ổ nhiễm liên cầu"
            ],
            "procedures": [
                "Hạn chế muối, nước nếu phù nhiều",
                "Theo dõi huyết áp, nước tiểu",
                "Lọc máu hiếm khi cần (nếu biến chứng nặng)"
            ]
        },
        prevention=[
            "Điều trị viêm họng/da do liên cầu sớm bằng kháng sinh",
            "Vệ sinh cá nhân, tránh lây nhiễm"
        ],
        complications=[
            "Tăng huyết áp cấp (encephalopathy hiếm)",
            "Suy thận cấp (hiếm)",
            "Tiến triển mạn (rất hiếm)"
        ],
        related_scores=["Blood Pressure", "Serum Creatinine"],
        related_drugs=["Furosemide", "ACE Inhibitor"],
        related_protocols=["Post-strep GN Management"],
        icd10_codes=["N00.9"]
    ),

    Disease(
        id="nephrotic_syndrome",
        name="Nephrotic Syndrome",
        name_vn="Hội chứng thận hư",
        category="Nephrology",
        definition="Hội chứng thận hư đặc trưng bởi protein niệu cao, giảm albumin máu, phù và tăng lipid máu; gặp ở cả trẻ em và người lớn.",
        causes=[
            "Nguyên phát: Minimal change, FSGS, Membranous",
            "Thứ phát: đái tháo đường, lupus, nhiễm HBV/HCV, thuốc"
        ],
        symptoms=[
            "Phù toàn thân (mi mắt, chi, cổ trướng)",
            "Tiểu bọt do protein niệu",
            "Tăng cân, mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Protein niệu > 3.5 g/24h",
                "Albumin máu < 30 g/L",
                "Phù, tăng lipid máu",
                "Cân nhắc sinh thiết thận để chẩn đoán thể bệnh"
            ],
            "tests": [
                "Protein niệu 24h hoặc tỉ lệ protein/creatinin",
                "Albumin, cholesterol, triglyceride",
                "Chức năng thận, điện giải",
                "Sinh thiết thận (nếu người lớn hoặc nghi ngờ thứ phát)"
            ],
            "imaging": [
                "Siêu âm thận"
            ]
        },
        treatment={
            "general": "Giảm phù, bảo vệ thận, điều trị nguyên nhân/miễn dịch tùy thể.",
            "medications": [
                "Corticosteroid (minimal change, FSGS)",
                "ACEi/ARB giảm protein niệu, hạ áp",
                "Lợi tiểu (Furosemide ± Spironolactone)",
                "Statin (nếu tăng lipid)",
                "Kháng đông dự phòng chọn lọc (nếu albumin rất thấp)"
            ],
            "procedures": [
                "Hạn chế muối, nước",
                "Theo dõi cân nặng, huyết áp, nước tiểu",
                "Điều trị nguyên nhân thứ phát (HBV/HCV, lupus, đái tháo đường)"
            ]
        },
        prevention=[
            "Kiểm soát bệnh nền (đái tháo đường, lupus)",
            "Theo dõi tái phát sớm, tuân thủ thuốc"
        ],
        complications=[
            "Huyết khối tĩnh mạch",
            "Nhiễm trùng do mất Ig",
            "Suy thận tiến triển",
            "Phù phổi nếu quá tải dịch"
        ],
        related_scores=["Protein/Creatinine Ratio", "Serum Albumin"],
        related_drugs=["Prednisone", "ACE Inhibitor", "ARB", "Furosemide", "Statin"],
        related_protocols=["Nephrotic Syndrome"],
        icd10_codes=["N04.9"]
    ),
]
