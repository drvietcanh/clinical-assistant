"""
Oncology Module
Cancer and malignant diseases
"""

from typing import List
from diseases.data import Disease


ONCOLOGY_DISEASES: List[Disease] = [
    Disease(
        id="lung_cancer",
        name="Lung Cancer",
        name_vn="Ung thư phổi",
        category="Oncology",
        definition="Ung thư phổi là ung thư phổ biến nhất tại Việt Nam, thường liên quan đến hút thuốc lá, có tiên lượng xấu nếu phát hiện muộn.",
        causes=[
            "Hút thuốc lá (nguyên nhân chính - 85%)",
            "Hút thuốc thụ động",
            "Ô nhiễm không khí",
            "Tiếp xúc radon, asbestos",
            "Yếu tố di truyền",
            "Tiền sử bệnh phổi"
        ],
        symptoms=[
            "Ho mạn tính, ho ra máu",
            "Khó thở",
            "Đau ngực",
            "Sụt cân",
            "Mệt mỏi",
            "Khàn tiếng (nếu chèn ép dây thần kinh)",
            "Thường không có triệu chứng ở giai đoạn sớm"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "X-quang ngực: khối u phổi",
                "CT ngực: đánh giá khối u, hạch",
                "Sinh thiết: xác định loại mô học (adenocarcinoma, squamous, small cell)",
                "Đánh giá giai đoạn: TNM staging"
            ],
            "tests": [
                "CT ngực có tiêm thuốc cản quang",
                "Sinh thiết: qua nội soi phế quản, CT-guided, phẫu thuật",
                "PET-CT (đánh giá di căn)",
                "MRI não (nếu nghi ngờ di căn não)",
                "Xét nghiệm gen (EGFR, ALK, PD-L1) - nếu adenocarcinoma"
            ],
            "imaging": [
                "CT ngực",
                "PET-CT",
                "MRI não",
                "X-quang ngực"
            ]
        },
        treatment={
            "general": "Điều trị đa mô thức: phẫu thuật, hóa trị, xạ trị, điều trị đích, miễn dịch. Tùy giai đoạn và loại mô học.",
            "medications": [
                "Hóa trị: Cisplatin, Carboplatin + Pemetrexed, Paclitaxel",
                "Điều trị đích: Gefitinib, Erlotinib (nếu EGFR+), Crizotinib (nếu ALK+)",
                "Miễn dịch: Pembrolizumab, Nivolumab (nếu PD-L1+)",
                "Xạ trị"
            ],
            "procedures": [
                "Phẫu thuật cắt thùy/phổi (nếu giai đoạn sớm, có thể phẫu thuật)",
                "Xạ trị",
                "Hóa trị",
                "Chăm sóc giảm nhẹ"
            ]
        },
        prevention=[
            "Bỏ thuốc lá (quan trọng nhất)",
            "Tránh hút thuốc thụ động",
            "Tránh ô nhiễm không khí",
            "Tầm soát (nếu nguy cơ cao: hút thuốc > 30 pack-years)"
        ],
        complications=[
            "Di căn: não, xương, gan, tuyến thượng thận",
            "Tràn dịch màng phổi",
            "Suy hô hấp",
            "Hội chứng cận ung thư",
            "Tử vong"
        ],
        related_scores=["TNM Stage", "Performance Status"],
        related_drugs=["Cisplatin", "Carboplatin", "Pemetrexed", "Gefitinib", "Pembrolizumab"],
        related_protocols=["Lung Cancer Management"],
        icd10_codes=["C34.9", "C34.1", "C34.2"]
    ),
    
    Disease(
        id="hepatocellular_carcinoma",
        name="Hepatocellular Carcinoma",
        name_vn="Ung thư gan",
        category="Oncology",
        definition="Ung thư gan là ung thư phổ biến tại Việt Nam, thường liên quan đến viêm gan B, C mạn và xơ gan.",
        causes=[
            "Viêm gan B mạn (nguyên nhân chính tại Việt Nam)",
            "Viêm gan C mạn",
            "Xơ gan",
            "Rượu bia",
            "Aflatoxin",
            "Béo phì, đái tháo đường"
        ],
        symptoms=[
            "Giai đoạn sớm: thường không có triệu chứng",
            "Giai đoạn muộn: đau bụng, sụt cân, vàng da",
            "Cổ trướng",
            "Xuất huyết tiêu hóa",
            "Sốt",
            "Mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Tiền sử viêm gan B/C, xơ gan",
                "AFP (Alpha-fetoprotein) tăng",
                "Siêu âm: khối u gan",
                "CT/MRI: đánh giá khối u, mạch máu",
                "Sinh thiết (nếu cần)",
                "Đánh giá giai đoạn: BCLC staging"
            ],
            "tests": [
                "AFP",
                "Siêu âm gan",
                "CT/MRI gan có tiêm thuốc cản quang",
                "Sinh thiết gan (nếu cần)",
                "Chức năng gan"
            ],
            "imaging": [
                "Siêu âm gan",
                "CT gan",
                "MRI gan"
            ]
        },
        treatment={
            "general": "Điều trị đa mô thức: phẫu thuật, TACE, RFA, sorafenib. Tùy giai đoạn và chức năng gan.",
            "medications": [
                "Sorafenib, Lenvatinib (điều trị đích)",
                "Atezolizumab + Bevacizumab (miễn dịch + kháng mạch)",
                "Hóa trị (ít hiệu quả)"
            ],
            "procedures": [
                "Phẫu thuật cắt gan (nếu giai đoạn sớm, chức năng gan tốt)",
                "Ghép gan (nếu giai đoạn sớm, phù hợp)",
                "TACE (Transarterial Chemoembolization)",
                "RFA (Radiofrequency Ablation)",
                "TARE (Transarterial Radioembolization)"
            ]
        },
        prevention=[
            "Tiêm vắc xin viêm gan B",
            "Điều trị viêm gan B, C",
            "Bỏ rượu bia",
            "Tầm soát định kỳ (nếu viêm gan B/C, xơ gan)"
        ],
        complications=[
            "Di căn: phổi, xương, não",
            "Suy gan",
            "Xuất huyết",
            "Tử vong"
        ],
        related_scores=["BCLC Stage", "Child-Pugh Score", "AFP"],
        related_drugs=["Sorafenib", "Lenvatinib", "Atezolizumab", "Bevacizumab"],
        related_protocols=["Hepatocellular Carcinoma Management"],
        icd10_codes=["C22.0"]
    ),
    
    Disease(
        id="breast_cancer",
        name="Breast Cancer",
        name_vn="Ung thư vú",
        category="Oncology",
        definition="Ung thư vú là ung thư phổ biến nhất ở phụ nữ tại Việt Nam, cần tầm soát định kỳ để phát hiện sớm.",
        causes=[
            "Yếu tố di truyền: BRCA1, BRCA2",
            "Tuổi cao",
            "Tiền sử ung thư vú",
            "Tiền sử gia đình",
            "Hormone: kinh nguyệt sớm, mãn kinh muộn, không sinh con, không cho con bú",
            "Rượu bia, béo phì"
        ],
        symptoms=[
            "Khối u vú (thường không đau)",
            "Thay đổi da vú: lõm, đỏ, loét",
            "Thay đổi núm vú: tụt, tiết dịch",
            "Hạch nách",
            "Thường không có triệu chứng ở giai đoạn sớm"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Siêu âm vú",
                "Chụp nhũ ảnh (mammography)",
                "Sinh thiết: xác định loại mô học, ER/PR, HER2",
                "Đánh giá giai đoạn: TNM staging"
            ],
            "tests": [
                "Siêu âm vú",
                "Chụp nhũ ảnh",
                "Sinh thiết (FNA, core biopsy)",
                "Xét nghiệm: ER, PR, HER2, Ki-67",
                "CT ngực bụng (đánh giá di căn)",
                "Xét nghiệm gen (nếu có chỉ định)"
            ],
            "imaging": [
                "Siêu âm vú",
                "Chụp nhũ ảnh",
                "MRI vú (nếu cần)",
                "CT ngực bụng"
            ]
        },
        treatment={
            "general": "Điều trị đa mô thức: phẫu thuật, hóa trị, xạ trị, nội tiết, điều trị đích. Tùy giai đoạn và đặc điểm khối u.",
            "medications": [
                "Hóa trị: AC (Adriamycin + Cyclophosphamide), TAC, TC",
                "Nội tiết: Tamoxifen, Aromatase inhibitor (nếu ER/PR+)",
                "Điều trị đích: Trastuzumab, Pertuzumab (nếu HER2+)",
                "CDK4/6 inhibitor: Palbociclib (nếu ER+, HER2-)",
                "Xạ trị"
            ],
            "procedures": [
                "Phẫu thuật: cắt khối u (lumpectomy) hoặc cắt vú (mastectomy)",
                "Nạo hạch nách",
                "Xạ trị",
                "Hóa trị",
                "Tái tạo vú (nếu có chỉ định)"
            ]
        },
        prevention=[
            "Tầm soát định kỳ: tự khám vú, siêu âm, chụp nhũ ảnh",
            "Duy trì cân nặng hợp lý",
            "Hạn chế rượu bia",
            "Cho con bú",
            "Điều trị dự phòng (nếu nguy cơ cao)"
        ],
        complications=[
            "Di căn: xương, phổi, gan, não",
            "Tái phát",
            "Phù tay (sau nạo hạch)",
            "Tử vong"
        ],
        related_scores=["TNM Stage", "ER/PR", "HER2"],
        related_drugs=["Tamoxifen", "Trastuzumab", "Adriamycin", "Cyclophosphamide", "Palbociclib"],
        related_protocols=["Breast Cancer Management"],
        icd10_codes=["C50.9", "C50.1", "C50.2"]
    ),
]
