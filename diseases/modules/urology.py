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
]
