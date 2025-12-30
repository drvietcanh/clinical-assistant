"""
Obstetrics and Gynecology Module
Pregnancy, childbirth, and women's health
"""

from typing import List
from diseases.data import Disease


OBSTETRICS_GYNECOLOGY_DISEASES: List[Disease] = [
    Disease(
        id="pelvic_inflammatory_disease",
        name="Pelvic Inflammatory Disease",
        name_vn="Viêm nhiễm phụ khoa",
        category="Obstetrics/Gynecology",
        definition="Viêm nhiễm phụ khoa là tình trạng viêm nhiễm cơ quan sinh dục nữ (tử cung, vòi trứng, buồng trứng), phổ biến tại Việt Nam.",
        causes=[
            "Vi khuẩn: Chlamydia trachomatis, Neisseria gonorrhoeae, Mycoplasma genitalium",
            "Vi khuẩn kỵ khí: Bacteroides, Prevotella",
            "Yếu tố nguy cơ: quan hệ tình dục không an toàn, nhiều bạn tình, tiền sử PID"
        ],
        symptoms=[
            "Đau bụng dưới",
            "Sốt",
            "Khí hư bất thường (mủ, mùi hôi)",
            "Đau khi quan hệ tình dục",
            "Rối loạn kinh nguyệt",
            "Buồn nôn, nôn",
            "Có thể không có triệu chứng"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Khám phụ khoa: đau khi di động tử cung, đau vùng phụ",
                "Xét nghiệm: tăng bạch cầu, CRP",
                "Siêu âm: dịch vùng chậu, dày vòi trứng",
                "Cấy dịch cổ tử cung"
            ],
            "tests": [
                "Cấy dịch cổ tử cung (Chlamydia, Gonorrhea)",
                "Công thức máu, CRP",
                "Siêu âm vùng chậu",
                "Test thai (loại trừ thai ngoài tử cung)"
            ],
            "imaging": [
                "Siêu âm vùng chậu",
                "CT vùng chậu (nếu nghi ngờ áp xe)"
            ]
        },
        treatment={
            "general": "Điều trị kháng sinh phổ rộng sớm. Mục tiêu: diệt vi khuẩn, phòng ngừa biến chứng.",
            "medications": [
                "Kháng sinh: Ceftriaxone + Doxycycline + Metronidazole",
                "Hoặc: Ofloxacin + Metronidazole (nếu dị ứng)",
                "Điều trị bạn tình",
                "Giảm đau: NSAID"
            ],
            "procedures": [
                "Nghỉ ngơi",
                "Dẫn lưu áp xe (nếu có)",
                "Phẫu thuật (nếu nặng, không đáp ứng)"
            ]
        },
        prevention=[
            "Quan hệ tình dục an toàn",
            "Sử dụng bao cao su",
            "Điều trị sớm nhiễm trùng",
            "Điều trị bạn tình"
        ],
        complications=[
            "Vô sinh",
            "Thai ngoài tử cung",
            "Đau vùng chậu mạn tính",
            "Áp xe vùng chậu",
            "Viêm phúc mạc"
        ],
        related_scores=["PID Severity"],
        related_drugs=["Ceftriaxone", "Doxycycline", "Metronidazole", "Ofloxacin"],
        related_protocols=[],
        icd10_codes=["N73.9", "N70.9"]
    ),
    
    Disease(
        id="uterine_fibroids",
        name="Uterine Fibroids",
        name_vn="U xơ tử cung",
        category="Obstetrics/Gynecology",
        definition="U xơ tử cung là khối u lành tính của cơ tử cung, rất phổ biến ở phụ nữ, đặc biệt phụ nữ trong độ tuổi sinh sản.",
        causes=[
            "Nguyên nhân chưa rõ",
            "Yếu tố di truyền",
            "Hormone: estrogen, progesterone",
            "Yếu tố nguy cơ: tuổi, béo phì, tiền sử gia đình"
        ],
        symptoms=[
            "Thường không có triệu chứng",
            "Rong kinh, cường kinh",
            "Đau bụng dưới",
            "Đau khi quan hệ tình dục",
            "Tiểu nhiều (nếu u lớn, chèn ép bàng quang)",
            "Táo bón (nếu chèn ép trực tràng)",
            "Vô sinh, sảy thai (nếu u lớn)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Khám phụ khoa: tử cung to, không đều",
                "Siêu âm: khối u trong tử cung",
                "MRI (nếu cần đánh giá chi tiết)"
            ],
            "tests": [
                "Siêu âm vùng chậu",
                "MRI (nếu cần)",
                "Công thức máu (thiếu máu nếu rong kinh)"
            ],
            "imaging": [
                "Siêu âm vùng chậu",
                "MRI tử cung"
            ]
        },
        treatment={
            "general": "Điều trị theo triệu chứng và kích thước u. Mục tiêu: giảm triệu chứng, bảo tồn tử cung nếu có thể.",
            "medications": [
                "Hormone: Progestin, GnRH agonist (giảm kích thước u)",
                "Tranexamic acid (giảm rong kinh)",
                "NSAID (giảm đau)",
                "Bổ sung sắt (nếu thiếu máu)"
            ],
            "procedures": [
                "Theo dõi (nếu không có triệu chứng, u nhỏ)",
                "Phẫu thuật cắt u (myomectomy) - bảo tồn tử cung",
                "Cắt tử cung (hysterectomy) - nếu u lớn, nhiều u, không còn nhu cầu sinh con",
                "Thuyên tắc động mạch tử cung (UAE)",
                "Cắt u bằng sóng siêu âm (FUS)"
            ]
        },
        prevention=[
            "Không có cách phòng ngừa",
            "Theo dõi định kỳ",
            "Điều trị sớm nếu có triệu chứng"
        ],
        complications=[
            "Thiếu máu (do rong kinh)",
            "Vô sinh",
            "Sảy thai",
            "Biến chứng thai kỳ",
            "Thoái hóa u (hiếm)"
        ],
        related_scores=["Fibroid Size", "Symptom Score"],
        related_drugs=["Progestin", "GnRH Agonist", "Tranexamic Acid"],
        related_protocols=[],
        icd10_codes=["D25.9", "D25.0", "D25.1", "D25.2"]
    ),
    
    Disease(
        id="polycystic_ovary_syndrome",
        name="Polycystic Ovary Syndrome",
        name_vn="Hội chứng buồng trứng đa nang (PCOS)",
        category="Obstetrics/Gynecology",
        definition="PCOS là rối loạn nội tiết phổ biến ở phụ nữ trong độ tuổi sinh sản, đặc trưng bởi rối loạn kinh nguyệt, tăng androgen, buồng trứng đa nang.",
        causes=[
            "Nguyên nhân chưa rõ",
            "Kháng insulin",
            "Rối loạn hormone: tăng androgen, LH/FSH bất thường",
            "Yếu tố di truyền",
            "Yếu tố môi trường: béo phì, ít vận động"
        ],
        symptoms=[
            "Rối loạn kinh nguyệt: vô kinh, thiểu kinh",
            "Tăng androgen: rậm lông, mụn trứng cá, rụng tóc",
            "Béo phì",
            "Khó thụ thai",
            "Buồng trứng đa nang (siêu âm)",
            "Tăng nguy cơ đái tháo đường, tăng huyết áp"
        ],
        diagnosis={
            "criteria": [
                "Rotterdam criteria: ≥ 2 trong 3:",
                "1. Rối loạn rụng trứng (vô kinh/thiểu kinh)",
                "2. Tăng androgen (lâm sàng hoặc xét nghiệm)",
                "3. Buồng trứng đa nang (siêu âm: ≥ 12 nang, thể tích tăng)"
            ],
            "tests": [
                "Hormone: LH, FSH, Testosterone, DHEA-S",
                "Đường huyết, HbA1c, Insulin",
                "Lipid máu",
                "Siêu âm vùng chậu",
                "Loại trừ: cường giáp, tăng prolactin, u tuyến thượng thận"
            ],
            "imaging": [
                "Siêu âm vùng chậu"
            ]
        },
        treatment={
            "general": "Điều trị theo triệu chứng và mục tiêu. Mục tiêu: điều hòa kinh nguyệt, giảm androgen, cải thiện khả năng thụ thai.",
            "medications": [
                "Điều hòa kinh nguyệt: OCP (Oral Contraceptive Pill)",
                "Giảm androgen: Spironolactone, Finasteride",
                "Kháng insulin: Metformin",
                "Kích thích rụng trứng: Clomiphene, Letrozole (nếu muốn có thai)"
            ],
            "procedures": [
                "Giảm cân (nếu béo phì) - quan trọng",
                "Tập thể dục",
                "Chế độ ăn lành mạnh",
                "Theo dõi định kỳ"
            ]
        },
        prevention=[
            "Duy trì cân nặng hợp lý",
            "Tập thể dục",
            "Chế độ ăn lành mạnh",
            "Điều trị sớm"
        ],
        complications=[
            "Vô sinh",
            "Đái tháo đường type 2",
            "Tăng huyết áp",
            "Rối loạn lipid máu",
            "Ung thư nội mạc tử cung (nếu vô kinh lâu)",
            "Bệnh tim mạch"
        ],
        related_scores=["PCOS Criteria", "Androgen Score"],
        related_drugs=["OCP", "Metformin", "Spironolactone", "Clomiphene"],
        related_protocols=[],
        icd10_codes=["E28.2"]
    ),
]
