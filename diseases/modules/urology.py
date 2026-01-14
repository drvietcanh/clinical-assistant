"""
Urology Module
Urinary tract and male reproductive system diseases
"""

from typing import List
from diseases.data import Disease


UROLOGY_DISEASES: List[Disease] = [
    Disease(
        id="urinary_tract_infection",
        name="Urinary Tract Infection",
        name_vn="Nhiễm trùng đường tiết niệu",
        category="Urology",
        definition="Nhiễm trùng đường tiết niệu là nhiễm trùng bất kỳ phần nào của đường tiết niệu (thận, niệu quản, bàng quang, niệu đạo), rất phổ biến, đặc biệt ở phụ nữ.",
        causes=[
            "Vi khuẩn: E. coli (80-90%), Klebsiella, Proteus, Enterococcus",
            "Yếu tố nguy cơ: phụ nữ (niệu đạo ngắn), quan hệ tình dục, đặt ống thông tiểu, sỏi thận, đái tháo đường, mang thai"
        ],
        symptoms=[
            "Tiểu buốt, tiểu rắt",
            "Tiểu nhiều lần, tiểu gấp",
            "Đau vùng bụng dưới (nếu viêm bàng quang)",
            "Đau lưng, sốt (nếu viêm thận)",
            "Nước tiểu đục, có mùi hôi",
            "Tiểu máu (đôi khi)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Tổng phân tích nước tiểu: bạch cầu, nitrite dương tính",
                "Cấy nước tiểu: > 10^5 CFU/ml (hoặc > 10^3 nếu có triệu chứng)",
                "Phân loại: viêm bàng quang (dưới), viêm thận (trên)"
            ],
            "tests": [
                "Tổng phân tích nước tiểu",
                "Cấy nước tiểu (trước khi dùng kháng sinh)",
                "Công thức máu (nếu sốt)",
                "Chức năng thận (nếu viêm thận)"
            ],
            "imaging": [
                "Siêu âm thận bàng quang (nếu tái phát, viêm thận)",
                "CT ổ bụng (nếu nghi ngờ áp xe)"
            ]
        },
        treatment={
            "general": "Điều trị theo IDSA guidelines. Kháng sinh theo kháng sinh đồ. Uống nhiều nước.",
            "medications": [
                "Viêm bàng quang: Nitrofurantoin, Trimethoprim-Sulfamethoxazole, Fosfomycin",
                "Viêm thận: Ciprofloxacin, Levofloxacin, Ceftriaxone (nếu nặng)",
                "Giảm đau: Paracetamol, Ibuprofen",
                "Uống nhiều nước"
            ],
            "procedures": [
                "Uống nhiều nước (2-3 lít/ngày)",
                "Điều trị sỏi thận (nếu có)",
                "Loại bỏ ống thông tiểu (nếu có)"
            ]
        },
        prevention=[
            "Uống nhiều nước",
            "Đi tiểu sau quan hệ tình dục",
            "Vệ sinh đúng cách (lau từ trước ra sau)",
            "Tránh nhịn tiểu lâu",
            "Điều trị sỏi thận"
        ],
        complications=[
            "Viêm thận",
            "Nhiễm khuẩn huyết",
            "Áp xe thận",
            "Suy thận (nếu nặng)",
            "Tái phát"
        ],
        related_scores=["UTI Severity"],
        related_drugs=["Nitrofurantoin", "Trimethoprim-Sulfamethoxazole", "Ciprofloxacin", "Levofloxacin"],
        related_protocols=["UTI Management"],
        icd10_codes=["N39.0", "N10", "N12"]
    ),
    
    Disease(
        id="kidney_stones",
        name="Kidney Stones",
        name_vn="Sỏi thận",
        category="Urology",
        definition="Sỏi thận là tình trạng hình thành sỏi trong thận, niệu quản, bàng quang, rất phổ biến tại Việt Nam.",
        causes=[
            "Calcium oxalate (phổ biến nhất)",
            "Calcium phosphate",
            "Uric acid",
            "Struvite (nhiễm trùng)",
            "Cystine (hiếm, di truyền)",
            "Yếu tố nguy cơ: uống ít nước, ăn nhiều muối, protein, béo phì, tiền sử gia đình"
        ],
        symptoms=[
            "Đau quặn thận (renal colic): đau dữ dội vùng thắt lưng, lan xuống bẹn",
            "Tiểu máu",
            "Buồn nôn, nôn",
            "Tiểu buốt, tiểu rắt (nếu sỏi ở bàng quang)",
            "Sốt (nếu có nhiễm trùng)",
            "Có thể không có triệu chứng (sỏi nhỏ)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "CT không tiêm thuốc cản quang (chuẩn vàng)",
                "Siêu âm thận (nếu không có CT)",
                "Xét nghiệm nước tiểu: hồng cầu, tinh thể",
                "Phân tích sỏi (nếu lấy được)"
            ],
            "tests": [
                "CT không tiêm thuốc cản quang",
                "Siêu âm thận",
                "Tổng phân tích nước tiểu",
                "Chức năng thận",
                "Điện giải, canxi, acid uric",
                "Phân tích sỏi (nếu có)"
            ],
            "imaging": [
                "CT không tiêm thuốc cản quang (chuẩn vàng)",
                "Siêu âm thận",
                "X-quang bụng (nếu sỏi cản quang)"
            ]
        },
        treatment={
            "general": "Điều trị theo AUA guidelines. Sỏi nhỏ có thể tự ra. Sỏi lớn cần can thiệp.",
            "medications": [
                "Giảm đau: NSAID (Ketorolac, Ibuprofen), Opioid (nếu cần)",
                "Giãn cơ: Tamsulosin (giúp sỏi ra)",
                "Kiềm hóa nước tiểu (nếu sỏi acid uric)",
                "Allopurinol (nếu sỏi acid uric tái phát)"
            ],
            "procedures": [
                "Uống nhiều nước (2-3 lít/ngày)",
                "Tán sỏi ngoài cơ thể (ESWL)",
                "Nội soi tán sỏi (URS)",
                "Tán sỏi qua da (PCNL) - nếu sỏi lớn",
                "Phẫu thuật mở (hiếm)"
            ]
        },
        prevention=[
            "Uống nhiều nước (2-3 lít/ngày)",
            "Chế độ ăn ít muối, ít protein động vật",
            "Hạn chế oxalate (rau chân vịt, đậu phộng)",
            "Điều trị tăng acid uric (nếu có)",
            "Theo dõi định kỳ"
        ],
        complications=[
            "Tắc nghẽn đường tiết niệu",
            "Nhiễm trùng đường tiết niệu",
            "Suy thận (nếu tắc nghẽn lâu)",
            "Tái phát",
            "Tổn thương thận"
        ],
        related_scores=["Stone Size", "Stone Location"],
        related_drugs=["Ketorolac", "Tamsulosin", "Allopurinol"],
        related_protocols=["Kidney Stones Management"],
        icd10_codes=["N20.0", "N20.1", "N20.2"]
    ),
    
    Disease(
        id="benign_prostatic_hyperplasia",
        name="Benign Prostatic Hyperplasia",
        name_vn="Phì đại tuyến tiền liệt lành tính (BPH)",
        category="Urology",
        definition="BPH là tình trạng phì đại lành tính tuyến tiền liệt, rất phổ biến ở nam giới cao tuổi, gây triệu chứng tiết niệu dưới.",
        causes=[
            "Tuổi cao (nguyên nhân chính)",
            "Hormone: testosterone, DHT",
            "Yếu tố di truyền",
            "Yếu tố môi trường: béo phì, ít vận động"
        ],
        symptoms=[
            "Tiểu khó, tiểu yếu",
            "Tiểu nhiều lần, tiểu đêm",
            "Tiểu gấp, tiểu không kiểm soát",
            "Tiểu không hết, tiểu nhỏ giọt",
            "Bí tiểu cấp (nếu nặng)",
            "Nhiễm trùng đường tiết niệu"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Khám trực tràng: tuyến tiền liệt to, mềm, đều",
                "IPSS (International Prostate Symptom Score)",
                "PSA (loại trừ ung thư)",
                "Siêu âm: kích thước tuyến tiền liệt, thể tích nước tiểu tồn dư"
            ],
            "tests": [
                "IPSS",
                "PSA",
                "Siêu âm tuyến tiền liệt, bàng quang",
                "Đo lưu lượng nước tiểu (uroflowmetry)",
                "Chức năng thận"
            ],
            "imaging": [
                "Siêu âm tuyến tiền liệt, bàng quang"
            ]
        },
        treatment={
            "general": "Điều trị theo AUA guidelines. Tùy mức độ triệu chứng: theo dõi, thuốc, hoặc phẫu thuật.",
            "medications": [
                "Alpha-blocker: Tamsulosin, Alfuzosin (giảm triệu chứng)",
                "5-alpha reductase inhibitor: Finasteride, Dutasteride (giảm kích thước tuyến)",
                "Kết hợp: Alpha-blocker + 5-ARI (nếu tuyến lớn)",
                "Anticholinergic (nếu tiểu gấp nhiều)"
            ],
            "procedures": [
                "Theo dõi (nếu triệu chứng nhẹ)",
                "Phẫu thuật: TURP (Transurethral Resection of Prostate) - chuẩn vàng",
                "Phẫu thuật laser: HoLEP, GreenLight",
                "Phẫu thuật mở (nếu tuyến rất lớn)"
            ]
        },
        prevention=[
            "Không có cách phòng ngừa",
            "Tập thể dục",
            "Duy trì cân nặng hợp lý",
            "Điều trị sớm"
        ],
        complications=[
            "Bí tiểu cấp",
            "Nhiễm trùng đường tiết niệu",
            "Sỏi bàng quang",
            "Suy thận (nếu tắc nghẽn lâu)",
            "Tổn thương thận"
        ],
        related_scores=["IPSS", "PSA", "Prostate Volume"],
        related_drugs=["Tamsulosin", "Alfuzosin", "Finasteride", "Dutasteride"],
        related_protocols=["BPH Management"],
        icd10_codes=["N40.0", "N40.1"]
    ),

    Disease(
        id="acute_pyelonephritis",
        name="Acute Pyelonephritis",
        name_vn="Viêm bể thận - thận cấp",
        category="Urology",
        definition="Viêm bể thận cấp là nhiễm trùng cấp thận và đài bể thận, thường do vi khuẩn Gram âm, cần điều trị kháng sinh sớm để tránh biến chứng.",
        causes=[
            "E. coli (phổ biến nhất), Klebsiella, Proteus",
            "Nguy cơ: nữ, tắc nghẽn niệu (sỏi), thai kỳ, đặt sonde, đái tháo đường"
        ],
        symptoms=[
            "Sốt cao, rét run",
            "Đau hông lưng, điểm niệu đạo-cột sống (+)",
            "Tiểu buốt, tiểu rắt, có thể tiểu máu",
            "Buồn nôn, nôn"
        ],
        diagnosis={
            "criteria": [
                "Sốt + đau hông lưng + hội chứng bàng quang",
                "Nước tiểu: bạch cầu, nitrite, cấy >=10^5 CFU/ml"
            ],
            "tests": [
                "Tổng phân tích nước tiểu, cấy nước tiểu",
                "Công thức máu, CRP/Procalcitonin",
                "Siêu âm thận (loại trừ tắc nghẽn, áp xe)"
            ],
            "imaging": [
                "Siêu âm thận",
                "CT không cản quang nếu nghi sỏi/tắc"
            ]
        },
        treatment={
            "general": "Kháng sinh sớm, đủ liều; nhập viện nếu nặng, có tắc nghẽn hoặc thai kỳ.",
            "medications": [
                "Ceftriaxone/Cefotaxime hoặc Fluoroquinolone (nếu không chống chỉ định)",
                "Carbapenem nếu nghi đa kháng",
                "Giảm đau, hạ sốt"
            ],
            "procedures": [
                "Uống đủ nước",
                "Dẫn lưu tắc nghẽn nếu có (sonde JJ, dẫn lưu qua da)",
                "Theo dõi lâm sàng và cấy kiểm tra khi cần"
            ]
        },
        prevention=[
            "Điều trị sỏi, tắc nghẽn",
            "Uống đủ nước",
            "Vệ sinh, tránh nhịn tiểu"
        ],
        complications=[
            "Áp xe thận/quanh thận",
            "Nhiễm khuẩn huyết",
            "Suy thận cấp"
        ],
        related_scores=["UTI Severity"],
        related_drugs=["Ceftriaxone", "Ciprofloxacin", "Meropenem"],
        related_protocols=["Pyelonephritis Management"],
        icd10_codes=["N10"]
    ),

    Disease(
        id="acute_prostatitis",
        name="Acute Prostatitis",
        name_vn="Viêm tuyến tiền liệt cấp",
        category="Urology",
        definition="Viêm tuyến tiền liệt cấp là nhiễm khuẩn cấp tính tuyến tiền liệt, gây đau tầng sinh môn, sốt, rối loạn tiểu tiện.",
        causes=[
            "E. coli, Enterobacteriaceae",
            "Nguy cơ: đặt sonde, thủ thuật niệu, quan hệ hậu môn, phì đại TLT gây ứ đọng"
        ],
        symptoms=[
            "Sốt, rét run",
            "Đau tầng sinh môn, đau hạ vị",
            "Tiểu buốt, tiểu khó, tiểu máu có thể",
            "Có thể bí tiểu cấp"
        ],
        diagnosis={
            "criteria": [
                "Sốt + đau tầng sinh môn + rối loạn tiểu tiện",
                "Khám trực tràng: tuyến tiền liệt sưng, nóng, đau (tránh xoa bóp mạnh)",
                "Cấy nước tiểu (và máu nếu sốt cao)"
            ],
            "tests": [
                "Cấy nước tiểu, kháng sinh đồ",
                "Công thức máu, CRP",
                "Cấy máu nếu sốt cao"
            ],
            "imaging": [
                "Siêu âm qua trực tràng nếu nghi áp xe",
                "Siêu âm bụng loại trừ bí tiểu"
            ]
        },
        treatment={
            "general": "Kháng sinh phổ rộng thấm tốt vào TLT, thời gian 2-4 tuần; dẫn lưu bàng quang nếu bí tiểu.",
            "medications": [
                "Fluoroquinolone (Ciprofloxacin/Levofloxacin) nếu nhạy",
                "Hoặc Ceftriaxone, Piperacillin-tazobactam (nếu nặng)",
                "Giảm đau, hạ sốt",
                "Alpha-blocker (Tamsulosin) hỗ trợ tiểu tiện"
            ],
            "procedures": [
                "Đặt sonde tiểu trên xương mu (suprapubic) nếu bí tiểu, tránh sonde niệu đạo",
                "Dẫn lưu áp xe nếu có"
            ]
        },
        prevention=[
            "Vệ sinh trước thủ thuật niệu",
            "Điều trị sớm UTI",
            "Uống đủ nước"
        ],
        complications=[
            "Áp xe tuyến tiền liệt",
            "Nhiễm khuẩn huyết",
            "Tiến triển thành viêm mạn"
        ],
        related_scores=[],
        related_drugs=["Ciprofloxacin", "Levofloxacin", "Ceftriaxone", "Piperacillin-tazobactam", "Tamsulosin"],
        related_protocols=["Acute Prostatitis"],
        icd10_codes=["N41.0"]
    ),
]
