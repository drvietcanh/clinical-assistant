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

    Disease(
        id="gastric_cancer",
        name="Gastric Cancer",
        name_vn="Ung thư dạ dày",
        category="Oncology",
        definition="Ung thư dạ dày là khối u ác tính xuất phát từ niêm mạc dạ dày, phổ biến ở Việt Nam, thường được chẩn đoán muộn do triệu chứng không đặc hiệu.",
        causes=[
            "Helicobacter pylori (nguyên nhân chính)",
            "Chế độ ăn: muối, thực phẩm hun khói, ít rau quả",
            "Hút thuốc lá",
            "Rượu bia",
            "Tiền sử gia đình",
            "Bệnh dạ dày mạn tính: viêm teo dạ dày, dị sản ruột",
            "Polyp dạ dày",
            "Béo phì"
        ],
        symptoms=[
            "Giai đoạn sớm: thường không có triệu chứng",
            "Đau bụng vùng thượng vị",
            "Đầy bụng, khó tiêu",
            "Buồn nôn, nôn",
            "Chán ăn, sụt cân",
            "Nuốt khó (nếu u ở tâm vị)",
            "Nôn ra máu, đi ngoài phân đen",
            "Thiếu máu",
            "Giai đoạn muộn: khối u bụng, di căn"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: đau bụng, sụt cân, khó tiêu",
                "Nội soi dạ dày: thấy khối u, sinh thiết",
                "Chẩn đoán mô bệnh học: adenocarcinoma (90%), lymphoma, GIST",
                "Đánh giá giai đoạn: CT, EUS, PET-CT"
            ],
            "tests": [
                "Nội soi dạ dày + sinh thiết (chuẩn vàng)",
                "Chẩn đoán mô bệnh học",
                "Test H. pylori",
                "CEA, CA 19-9 (marker)",
                "Công thức máu (thiếu máu)"
            ],
            "imaging": [
                "CT bụng-ngực (đánh giá giai đoạn)",
                "EUS (Endoscopic Ultrasound) - đánh giá độ xâm lấn",
                "PET-CT (nếu cần)",
                "X-quang dạ dày (nếu không nội soi được)"
            ]
        },
        treatment={
            "general": "Điều trị đa mô thức: phẫu thuật, hóa trị, xạ trị. Phẫu thuật là điều trị chính nếu có thể cắt bỏ được.",
            "medications": [
                "Hóa trị: FLOT (5-FU, Leucovorin, Oxaliplatin, Docetaxel), ECF/ECX (Epirubicin, Cisplatin, 5-FU/Capecitabine)",
                "Trastuzumab (nếu HER2 dương tính)",
                "Pembrolizumab (nếu MSI-H hoặc PD-L1 dương tính)",
                "Điều trị triệu chứng: giảm đau, chống nôn"
            ],
            "procedures": [
                "Phẫu thuật: cắt dạ dày một phần hoặc toàn bộ + nạo hạch",
                "Nội soi cắt niêm mạc (EMR/ESD) - nếu ung thư sớm",
                "Xạ trị (kết hợp với hóa trị)",
                "Điều trị H. pylori (nếu dương tính)"
            ]
        },
        prevention=[
            "Điều trị H. pylori",
            "Chế độ ăn: giảm muối, tăng rau quả",
            "Bỏ thuốc lá, hạn chế rượu bia",
            "Tầm soát (nếu có yếu tố nguy cơ)",
            "Điều trị viêm dạ dày mạn tính"
        ],
        complications=[
            "Di căn: gan, phổi, phúc mạc, xương",
            "Tắc nghẽn dạ dày",
            "Xuất huyết tiêu hóa",
            "Thủng dạ dày",
            "Suy kiệt",
            "Tử vong"
        ],
        related_scores=["TNM Stage", "HER2", "MSI", "PD-L1"],
        related_drugs=["5-FU", "Cisplatin", "Oxaliplatin", "Trastuzumab", "Pembrolizumab"],
        related_protocols=["Gastric Cancer Management"],
        icd10_codes=["C16.9", "C16.0", "C16.1", "C16.2"]
    ),

    Disease(
        id="colorectal_cancer",
        name="Colorectal Cancer",
        name_vn="Ung thư đại trực tràng",
        category="Oncology",
        definition="Ung thư đại trực tràng là khối u ác tính xuất phát từ đại tràng hoặc trực tràng, phổ biến ở Việt Nam, có thể phòng ngừa bằng tầm soát và cắt polyp.",
        causes=[
            "Polyp đại tràng (adenoma) - tiền ung thư",
            "Tiền sử gia đình: FAP, HNPCC (Lynch syndrome)",
            "Bệnh viêm ruột mạn tính: UC, Crohn",
            "Chế độ ăn: ít chất xơ, nhiều thịt đỏ, thịt chế biến",
            "Hút thuốc lá",
            "Rượu bia",
            "Béo phì",
            "Ít vận động",
            "Tuổi cao (> 50)"
        ],
        symptoms=[
            "Giai đoạn sớm: thường không có triệu chứng",
            "Thay đổi thói quen đại tiện: táo bón, tiêu chảy",
            "Máu trong phân (đỏ tươi hoặc đen)",
            "Đau bụng",
            "Sụt cân",
            "Mệt mỏi, thiếu máu",
            "Cảm giác đi ngoài không hết",
            "Khối u bụng (nếu lớn)",
            "Tắc ruột (nếu muộn)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: thay đổi thói quen đại tiện, máu trong phân",
                "Nội soi đại tràng: thấy khối u, sinh thiết",
                "Chẩn đoán mô bệnh học: adenocarcinoma",
                "Đánh giá giai đoạn: CT, MRI (trực tràng), PET-CT"
            ],
            "tests": [
                "Nội soi đại tràng + sinh thiết (chuẩn vàng)",
                "Test máu ẩn trong phân (FOBT) - tầm soát",
                "CEA (marker)",
                "Chẩn đoán mô bệnh học",
                "Test di truyền (nếu nghi ngờ Lynch syndrome)"
            ],
            "imaging": [
                "CT bụng-ngực (đánh giá giai đoạn)",
                "MRI vùng chậu (ung thư trực tràng)",
                "PET-CT (nếu cần)",
                "Siêu âm bụng"
            ]
        },
        treatment={
            "general": "Điều trị đa mô thức: phẫu thuật, hóa trị, xạ trị. Phẫu thuật là điều trị chính. Tầm soát và cắt polyp có thể phòng ngừa.",
            "medications": [
                "Hóa trị: FOLFOX (5-FU, Leucovorin, Oxaliplatin), FOLFIRI (5-FU, Leucovorin, Irinotecan), CAPOX (Capecitabine, Oxaliplatin)",
                "Bevacizumab (kháng VEGF)",
                "Cetuximab, Panitumumab (nếu KRAS wild-type)",
                "Pembrolizumab (nếu MSI-H)",
                "Điều trị triệu chứng"
            ],
            "procedures": [
                "Phẫu thuật: cắt đại tràng/trực tràng + nạo hạch",
                "Nội soi cắt polyp (nếu ung thư sớm)",
                "Xạ trị (ung thư trực tràng, kết hợp với hóa trị)",
                "Tầm soát định kỳ sau điều trị"
            ]
        },
        prevention=[
            "Tầm soát: nội soi đại tràng từ 50 tuổi (hoặc sớm hơn nếu có yếu tố nguy cơ)",
            "Cắt polyp",
            "Chế độ ăn: nhiều chất xơ, ít thịt đỏ",
            "Tập thể dục",
            "Bỏ thuốc lá, hạn chế rượu bia",
            "Duy trì cân nặng hợp lý"
        ],
        complications=[
            "Di căn: gan, phổi, phúc mạc",
            "Tắc ruột",
            "Xuất huyết tiêu hóa",
            "Thủng đại tràng",
            "Suy kiệt",
            "Tử vong"
        ],
        related_scores=["TNM Stage", "KRAS", "MSI", "PD-L1"],
        related_drugs=["5-FU", "Oxaliplatin", "Irinotecan", "Bevacizumab", "Cetuximab"],
        related_protocols=["Colorectal Cancer Management"],
        icd10_codes=["C18.9", "C19", "C20", "C21.8"]
    ),
]
