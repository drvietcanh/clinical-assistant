"""
Ophthalmology Module
Eye diseases and conditions
"""

from typing import List
from diseases.data import Disease


OPHTHALMOLOGY_DISEASES: List[Disease] = [
    Disease(
        id="cataract",
        name="Cataract",
        name_vn="Đục thủy tinh thể",
        category="Ophthalmology",
        definition="Đục thủy tinh thể là tình trạng thủy tinh thể bị đục, gây giảm thị lực, rất phổ biến ở người cao tuổi tại Việt Nam.",
        causes=[
            "Tuổi già (nguyên nhân chính)",
            "Đái tháo đường",
            "Chấn thương mắt",
            "Thuốc: corticosteroid",
            "Tia cực tím",
            "Hút thuốc",
            "Di truyền (hiếm)"
        ],
        symptoms=[
            "Giảm thị lực từ từ",
            "Mờ mắt",
            "Nhìn đôi (nếu một mắt)",
            "Nhạy cảm với ánh sáng",
            "Nhìn màu kém",
            "Thay đổi độ kính thường xuyên"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Khám mắt: thủy tinh thể đục",
                "Đo thị lực",
                "Soi đáy mắt: giảm ánh đồng tử đỏ"
            ],
            "tests": [
                "Đo thị lực",
                "Khám mắt bằng đèn khe",
                "Soi đáy mắt",
                "Đo nhãn áp"
            ],
            "imaging": []
        },
        treatment={
            "general": "Phẫu thuật thay thủy tinh thể là phương pháp điều trị duy nhất. Mục tiêu: phục hồi thị lực.",
            "medications": [
                "Không có thuốc điều trị",
                "Kính mắt (tạm thời, nếu nhẹ)"
            ],
            "procedures": [
                "Phẫu thuật thay thủy tinh thể (phacoemulsification) - phương pháp chính",
                "Đặt thủy tinh thể nhân tạo (IOL)",
                "Phẫu thuật ngoại trú, phục hồi nhanh"
            ]
        },
        prevention=[
            "Đeo kính râm (bảo vệ khỏi tia UV)",
            "Bỏ thuốc lá",
            "Kiểm soát đái tháo đường",
            "Khám mắt định kỳ",
            "Chế độ ăn giàu chất chống oxy hóa"
        ],
        complications=[
            "Mù (nếu không điều trị)",
            "Tăng nhãn áp",
            "Viêm màng bồ đào",
            "Biến chứng phẫu thuật (hiếm)"
        ],
        related_scores=["Visual Acuity", "Cataract Grade"],
        related_drugs=[],
        related_protocols=[],
        icd10_codes=["H26.9", "H25.9"]
    ),
    
    Disease(
        id="conjunctivitis",
        name="Conjunctivitis",
        name_vn="Viêm kết mạc",
        category="Ophthalmology",
        definition="Viêm kết mạc là tình trạng viêm màng kết mạc, rất phổ biến, có thể do virus, vi khuẩn, dị ứng.",
        causes=[
            "Virus: Adenovirus (phổ biến nhất), Herpes",
            "Vi khuẩn: Staphylococcus, Streptococcus, Haemophilus",
            "Dị ứng: phấn hoa, bụi, hóa chất",
            "Yếu tố nguy cơ: tiếp xúc người bệnh, vệ sinh kém, dị ứng"
        ],
        symptoms=[
            "Đỏ mắt",
            "Ngứa mắt",
            "Chảy nước mắt",
            "Dử mắt (ghèn)",
            "Cảm giác cộm, rát",
            "Sưng mí mắt",
            "Nhạy cảm với ánh sáng (nếu nặng)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Khám mắt: kết mạc đỏ, phù",
                "Phân loại: virus, vi khuẩn, dị ứng"
            ],
            "tests": [
                "Khám mắt bằng đèn khe",
                "Cấy dịch mắt (nếu nghi ngờ vi khuẩn)",
                "Test dị ứng (nếu nghi ngờ dị ứng)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị theo nguyên nhân. Virus tự khỏi. Vi khuẩn cần kháng sinh. Dị ứng cần tránh dị nguyên.",
            "medications": [
                "Virus: điều trị triệu chứng - nước mắt nhân tạo, chườm lạnh",
                "Vi khuẩn: kháng sinh nhỏ mắt (Chloramphenicol, Ofloxacin, Tobramycin)",
                "Dị ứng: Antihistamine nhỏ mắt, Corticosteroid nhỏ mắt (nếu nặng)",
                "Không dùng chung khăn, gối"
            ],
            "procedures": [
                "Vệ sinh mắt",
                "Chườm lạnh (giảm sưng)",
                "Cách ly (nếu lây)"
            ]
        },
        prevention=[
            "Rửa tay thường xuyên",
            "Không dụi mắt",
            "Không dùng chung khăn, gối",
            "Tránh dị nguyên (nếu dị ứng)",
            "Đeo kính bảo vệ"
        ],
        complications=[
            "Viêm giác mạc",
            "Giảm thị lực (nếu nặng)",
            "Lây lan",
            "Tái phát"
        ],
        related_scores=["Conjunctivitis Severity"],
        related_drugs=["Chloramphenicol", "Ofloxacin", "Tobramycin", "Antihistamine"],
        related_protocols=[],
        icd10_codes=["H10.9", "H10.0", "H10.1", "H10.2"]
    ),
    
    Disease(
        id="glaucoma",
        name="Glaucoma",
        name_vn="Tăng nhãn áp (Glaucoma)",
        category="Ophthalmology",
        definition="Glaucoma là nhóm bệnh gây tổn thương thần kinh thị giác do tăng nhãn áp, dẫn đến mất thị lực không hồi phục, phổ biến ở người cao tuổi.",
        causes=[
            "Tăng nhãn áp (nguyên nhân chính)",
            "Yếu tố nguy cơ: tuổi cao, tiền sử gia đình, đái tháo đường, cận thị, chấn thương mắt",
            "Phân loại: góc mở (phổ biến), góc đóng, bẩm sinh"
        ],
        symptoms=[
            "Giai đoạn sớm: thường không có triệu chứng",
            "Giai đoạn muộn: mất thị trường ngoại vi, nhìn đường hầm",
            "Góc đóng cấp: đau mắt dữ dội, đỏ mắt, nhìn mờ, nhìn hào quang, buồn nôn",
            "Mất thị lực (giai đoạn cuối)"
        ],
        diagnosis={
            "criteria": [
                "Tăng nhãn áp (> 21 mmHg)",
                "Tổn thương thần kinh thị giác (soi đáy mắt)",
                "Mất thị trường (perimetry)",
                "Góc tiền phòng: đánh giá bằng gonioscopy",
                "Phân loại: góc mở, góc đóng"
            ],
            "tests": [
                "Đo nhãn áp (tonometry)",
                "Soi đáy mắt (đánh giá thần kinh thị giác)",
                "Đo thị trường (perimetry)",
                "Gonioscopy (đánh giá góc)",
                "Đo độ dày giác mạc (pachymetry)"
            ],
            "imaging": [
                "OCT (Optical Coherence Tomography) - đánh giá thần kinh thị giác"
            ]
        },
        treatment={
            "general": "Điều trị mục tiêu: giảm nhãn áp, bảo vệ thần kinh thị giác. Điều trị suốt đời.",
            "medications": [
                "Thuốc nhỏ mắt: Prostaglandin (Latanoprost, Travoprost) - thuốc đầu tay",
                "Beta-blocker: Timolol",
                "Alpha-agonist: Brimonidine",
                "Carbonic anhydrase inhibitor: Dorzolamide",
                "Kết hợp nhiều thuốc (nếu cần)"
            ],
            "procedures": [
                "Laser: Trabeculoplasty (góc mở), Iridotomy (góc đóng)",
                "Phẫu thuật: Trabeculectomy (nếu thuốc không đủ)",
                "Theo dõi định kỳ (quan trọng)"
            ]
        },
        prevention=[
            "Khám mắt định kỳ (quan trọng, đặc biệt sau 40 tuổi)",
            "Điều trị sớm",
            "Dùng thuốc đều đặn",
            "Theo dõi nhãn áp"
        ],
        complications=[
            "Mất thị lực không hồi phục",
            "Mù",
            "Tổn thương thần kinh thị giác vĩnh viễn"
        ],
        related_scores=["Intraocular Pressure", "Visual Field", "Cup-to-Disc Ratio"],
        related_drugs=["Latanoprost", "Travoprost", "Timolol", "Brimonidine", "Dorzolamide"],
        related_protocols=["Glaucoma Management"],
        icd10_codes=["H40.9", "H40.1", "H40.2"]
    ),
]
