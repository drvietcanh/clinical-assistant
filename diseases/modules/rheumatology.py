"""
Rheumatology Module
Diseases: Gout
"""

from typing import List
from diseases.data import Disease


RHEUMATOLOGY_DISEASES: List[Disease] = [
    Disease(
        id="gout",
        name="Gout",
        name_vn="Bệnh gút",
        category="Rheumatology",
        definition="Gout là bệnh viêm khớp do lắng đọng tinh thể urate trong khớp, gây đau dữ dội, phổ biến tại Việt Nam do thay đổi lối sống.",
        causes=[
            "Tăng acid uric máu (hyperuricemia)",
            "Nguyên nhân: béo phì, rượu bia, thực phẩm giàu purine (thịt đỏ, hải sản, nội tạng)",
            "Giảm thải acid uric qua thận",
            "Tăng sản xuất acid uric",
            "Yếu tố di truyền",
            "Một số thuốc: lợi tiểu, aspirin liều thấp"
        ],
        symptoms=[
            "Cơn cấp: đau dữ dội, sưng, nóng, đỏ khớp (thường khớp ngón chân cái)",
            "Đau thường về đêm, đau dữ dội",
            "Sốt nhẹ",
            "Gout mạn: hạt tophi, tổn thương khớp mạn tính"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng điển hình",
                "Acid uric máu tăng (> 7 mg/dL nam, > 6 mg/dL nữ)",
                "Hút dịch khớp: tinh thể urate dưới kính hiển vi",
                "Đáp ứng với Colchicine"
            ],
            "tests": [
                "Acid uric máu",
                "Hút dịch khớp (nếu có tràn dịch) - tìm tinh thể urate",
                "Chức năng thận",
                "X-quang khớp (nếu gout mạn)"
            ],
            "imaging": [
                "X-quang khớp (hạt tophi, tổn thương xương)",
                "Siêu âm khớp (tinh thể urate)",
                "Dual-energy CT (nếu cần)"
            ]
        },
        treatment={
            "general": "Điều trị cơn cấp: NSAID, Colchicine, hoặc Corticosteroid. Điều trị dự phòng: Allopurinol hoặc Febuxostat.",
            "medications": [
                "Cơn cấp: NSAID (Ibuprofen, Naproxen, Indomethacin) hoặc Colchicine hoặc Prednisone",
                "Dự phòng: Allopurinol (ức chế xanthine oxidase) hoặc Febuxostat",
                "Probenecid (tăng thải acid uric) - nếu không dung nạp Allopurinol",
                "Pegloticase (nếu kháng trị)"
            ],
            "procedures": [
                "Hút dịch khớp (nếu tràn dịch nhiều)",
                "Phẫu thuật cắt hạt tophi (nếu lớn, ảnh hưởng chức năng)"
            ]
        },
        prevention=[
            "Giảm cân (nếu thừa cân)",
            "Hạn chế rượu bia",
            "Hạn chế thực phẩm giàu purine (thịt đỏ, hải sản, nội tạng)",
            "Uống nhiều nước",
            "Dùng thuốc hạ acid uric (nếu có chỉ định)"
        ],
        complications=[
            "Gout mạn, tổn thương khớp",
            "Hạt tophi",
            "Sỏi thận (do acid uric)",
            "Bệnh thận do gout",
            "Nhiễm trùng khớp (nếu hạt tophi vỡ)"
        ],
        related_scores=["Serum Uric Acid"],
        related_drugs=["Allopurinol", "Febuxostat", "Colchicine", "Ibuprofen", "Prednisone"],
        related_protocols=[],
        icd10_codes=["M10.9", "M10.0", "M10.1"]
    ),
]
