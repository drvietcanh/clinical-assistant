"""
Allergy and Immunology Module
Allergic diseases and immune system disorders
"""

from typing import List
from diseases.data import Disease


ALLERGY_IMMUNOLOGY_DISEASES: List[Disease] = [
    Disease(
        id="food_allergy",
        name="Food Allergy",
        name_vn="Dị ứng thực phẩm",
        category="Allergy/Immunology",
        definition="Dị ứng thực phẩm là phản ứng miễn dịch bất thường với thực phẩm, có thể gây phản ứng từ nhẹ đến nặng, đe dọa tính mạng.",
        causes=[
            "Thực phẩm phổ biến: đậu phộng, hải sản (tôm, cua), trứng, sữa, đậu nành, lúa mì",
            "Yếu tố di truyền",
            "Yếu tố môi trường",
            "Tuổi: trẻ em dễ dị ứng hơn"
        ],
        symptoms=[
            "Da: mề đay, phù mạch, ngứa",
            "Tiêu hóa: buồn nôn, nôn, tiêu chảy, đau bụng",
            "Hô hấp: khó thở, thở khò khè",
            "Tim mạch: hạ huyết áp, sốc",
            "Phản vệ (nếu nặng)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng sau ăn thực phẩm",
                "Test da (skin prick test)",
                "Test máu: IgE đặc hiệu",
                "Test thử thách (oral food challenge) - chuẩn vàng"
            ],
            "tests": [
                "Test da (skin prick test)",
                "IgE đặc hiệu (RAST, ImmunoCAP)",
                "Test thử thách (nếu cần)",
                "Test patch (nếu viêm da tiếp xúc)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Tránh thực phẩm gây dị ứng. Điều trị phản ứng cấp. Giáo dục bệnh nhân.",
            "medications": [
                "Tránh thực phẩm gây dị ứng (quan trọng nhất)",
                "Antihistamine (nếu phản ứng nhẹ)",
                "Epinephrine auto-injector (nếu có nguy cơ phản vệ)",
                "Corticosteroid (nếu phản ứng nặng)"
            ],
            "procedures": [
                "Giáo dục bệnh nhân và gia đình",
                "Đọc nhãn thực phẩm",
                "Mang epinephrine auto-injector",
                "Đeo vòng cảnh báo y tế"
            ]
        },
        prevention=[
            "Tránh thực phẩm gây dị ứng",
            "Đọc nhãn thực phẩm",
            "Mang epinephrine auto-injector",
            "Giáo dục về dị ứng"
        ],
        complications=[
            "Phản vệ",
            "Sốc phản vệ",
            "Tử vong (nếu không điều trị kịp thời)"
        ],
        related_scores=["Food Allergy Severity"],
        related_drugs=["Epinephrine", "Antihistamine", "Corticosteroid"],
        related_protocols=["Food Allergy Management"],
        icd10_codes=["Z91.01", "T78.1"]
    ),
    
    Disease(
        id="contact_dermatitis",
        name="Contact Dermatitis",
        name_vn="Viêm da tiếp xúc",
        category="Allergy/Immunology",
        definition="Viêm da tiếp xúc là phản ứng da khi tiếp xúc với chất gây dị ứng hoặc kích thích, phổ biến tại Việt Nam.",
        causes=[
            "Dị ứng (allergic): nickel, cao su, niken, mỹ phẩm, thuốc bôi",
            "Kích thích (irritant): hóa chất, xà phòng, chất tẩy rửa",
            "Yếu tố nguy cơ: da nhạy cảm, tiếp xúc thường xuyên"
        ],
        symptoms=[
            "Đỏ da",
            "Ngứa",
            "Mụn nước",
            "Bong vảy",
            "Nứt nẻ (nếu mạn)",
            "Vị trí: nơi tiếp xúc"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Tiền sử tiếp xúc",
                "Patch test (nếu dị ứng)",
                "Loại trừ: viêm da cơ địa, vẩy nến"
            ],
            "tests": [
                "Patch test (nếu dị ứng)",
                "Sinh thiết da (nếu không rõ)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Tránh chất gây dị ứng/kích thích. Điều trị viêm da. Mục tiêu: giảm viêm, ngứa.",
            "medications": [
                "Tránh chất gây dị ứng/kích thích",
                "Corticosteroid tại chỗ (mức độ phù hợp)",
                "Antihistamine (nếu ngứa nhiều)",
                "Dưỡng ẩm",
                "Corticosteroid toàn thân (nếu nặng, lan rộng)"
            ],
            "procedures": [
                "Tránh tiếp xúc",
                "Bảo vệ da (găng tay, quần áo)",
                "Giáo dục bệnh nhân"
            ]
        },
        prevention=[
            "Tránh chất gây dị ứng/kích thích",
            "Bảo vệ da",
            "Dưỡng ẩm da",
            "Đọc nhãn sản phẩm"
        ],
        complications=[
            "Viêm da mạn",
            "Nhiễm trùng da",
            "Ảnh hưởng chất lượng cuộc sống"
        ],
        related_scores=["Contact Dermatitis Severity"],
        related_drugs=["Topical Corticosteroid", "Antihistamine", "Prednisone"],
        related_protocols=[],
        icd10_codes=["L25.9", "L24.9"]
    ),
]
