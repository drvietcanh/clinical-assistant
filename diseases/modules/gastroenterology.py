"""
Gastroenterology Module
Diseases: PUD, GERD, Hepatitis B, Cirrhosis
"""

from typing import List
from diseases.data import Disease


GASTROENTEROLOGY_DISEASES: List[Disease] = [
    Disease(
        id="peptic_ulcer_disease",
        name="Peptic Ulcer Disease",
        name_vn="Loét dạ dày tá tràng",
        category="Gastroenterology",
        definition="Loét dạ dày tá tràng là tổn thương niêm mạc dạ dày hoặc tá tràng, phổ biến tại Việt Nam.",
        causes=[
            "Helicobacter pylori (H. pylori) - nguyên nhân chính",
            "NSAID (Aspirin, Ibuprofen, Naproxen)",
            "Stress (loét do stress)",
            "Hút thuốc, rượu bia",
            "Hội chứng Zollinger-Ellison (hiếm)"
        ],
        symptoms=[
            "Đau bụng vùng thượng vị (đau rát, nóng)",
            "Đau tăng khi đói, giảm khi ăn (loét tá tràng)",
            "Đau tăng khi ăn (loét dạ dày)",
            "Buồn nôn, nôn",
            "Ợ hơi, đầy bụng",
            "Xuất huyết tiêu hóa (nôn máu, đi ngoài phân đen)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Nội soi dạ dày tá tràng: thấy ổ loét",
                "Test H. pylori: UBT, test phân, sinh thiết"
            ],
            "tests": [
                "Nội soi dạ dày tá tràng (chuẩn vàng)",
                "Test H. pylori: UBT (Urea Breath Test), test phân, test máu",
                "Sinh thiết (nếu nghi ngờ ung thư)",
                "Công thức máu (nếu xuất huyết)"
            ],
            "imaging": [
                "Nội soi dạ dày tá tràng",
                "X-quang dạ dày có thuốc cản quang (ít dùng)"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân. Mục tiêu: lành ổ loét, diệt H. pylori (nếu có), phòng ngừa tái phát.",
            "medications": [
                "PPI (Omeprazole, Pantoprazole, Esomeprazole) - 4-8 tuần",
                "Diệt H. pylori: PPI + 2 kháng sinh (Amoxicillin + Clarithromycin hoặc Metronidazole) + Bismuth - 10-14 ngày",
                "H2RA (Ranitidine, Famotidine) - nếu không dung nạp PPI",
                "Antacid (nếu triệu chứng nhẹ)",
                "Tránh NSAID (nếu có thể)"
            ],
            "procedures": [
                "Nội soi cầm máu (nếu xuất huyết)",
                "Phẫu thuật (nếu thủng, hẹp môn vị)"
            ]
        },
        prevention=[
            "Diệt H. pylori",
            "Tránh NSAID (nếu có thể)",
            "Bỏ thuốc lá, hạn chế rượu bia",
            "Quản lý stress"
        ],
        complications=[
            "Xuất huyết tiêu hóa",
            "Thủng dạ dày/tá tràng",
            "Hẹp môn vị",
            "Ung thư dạ dày (nếu H. pylori lâu ngày)"
        ],
        related_scores=["Helicobacter pylori Test", "Ulcer Size"],
        related_drugs=["Omeprazole", "Pantoprazole", "Amoxicillin", "Clarithromycin", "Metronidazole"],
        related_protocols=["Peptic Ulcer Disease", "H. pylori Eradication"],
        icd10_codes=["K25.9", "K26.9", "K27.9"]
    ),
    
    Disease(
        id="gastroesophageal_reflux",
        name="Gastroesophageal Reflux Disease",
        name_vn="Trào ngược dạ dày thực quản (GERD)",
        category="Gastroenterology",
        definition="GERD là tình trạng trào ngược dịch dạ dày lên thực quản, gây triệu chứng và/hoặc tổn thương niêm mạc thực quản.",
        causes=[
            "Rối loạn cơ thắt thực quản dưới (LES)",
            "Thoát vị hoành",
            "Chậm làm rỗng dạ dày",
            "Tăng áp lực ổ bụng (béo phì, mang thai)",
            "Yếu tố kích thích: rượu bia, thuốc lá, thức ăn cay, cà phê"
        ],
        symptoms=[
            "Ợ nóng (heartburn)",
            "Ợ chua",
            "Trào ngược (regurgitation)",
            "Đau ngực",
            "Khó nuốt",
            "Đau họng"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng điển hình",
                "Test điều trị với PPI (PPI test)",
                "Nội soi thực quản: viêm thực quản, Barrett thực quản",
                "pH monitoring (nếu nghi ngờ)"
            ],
            "tests": [
                "Nội soi thực quản dạ dày (nếu có triệu chứng báo động hoặc > 50 tuổi)",
                "Test điều trị với PPI (PPI test)",
                "pH monitoring 24h (nếu nghi ngờ)",
                "Manometry thực quản (nếu nghi ngờ rối loạn vận động)"
            ],
            "imaging": [
                "Nội soi thực quản dạ dày",
                "X-quang thực quản có thuốc cản quang (ít dùng)"
            ]
        },
        treatment={
            "general": "Điều trị theo ACG/AGA guidelines. Mục tiêu: giảm triệu chứng, lành viêm thực quản, phòng ngừa biến chứng.",
            "medications": [
                "PPI (Omeprazole, Pantoprazole, Esomeprazole) - 4-8 tuần, có thể dùng dài hạn",
                "H2RA (Ranitidine, Famotidine) - nếu PPI không dung nạp",
                "Antacid (nếu triệu chứng nhẹ)",
                "Prokinetic (Metoclopramide, Domperidone) - nếu chậm làm rỗng dạ dày"
            ],
            "procedures": [
                "Thay đổi lối sống: giảm cân, nâng đầu giường, tránh ăn trước khi ngủ",
                "Phẫu thuật (fundoplication) - nếu kháng thuốc, có chỉ định"
            ]
        },
        prevention=[
            "Giảm cân (nếu thừa cân)",
            "Tránh thức ăn kích thích",
            "Không nằm sau khi ăn",
            "Nâng đầu giường",
            "Bỏ thuốc lá, hạn chế rượu bia"
        ],
        complications=[
            "Viêm thực quản",
            "Barrett thực quản",
            "Hẹp thực quản",
            "Ung thư thực quản (nếu Barrett lâu ngày)"
        ],
        related_scores=["GERD Score", "Reflux Symptom Index"],
        related_drugs=["Omeprazole", "Pantoprazole", "Ranitidine", "Metoclopramide"],
        related_protocols=["GERD Management"],
        icd10_codes=["K21.9", "K21.0"]
    ),
    
    Disease(
        id="hepatitis_b",
        name="Hepatitis B",
        name_vn="Viêm gan B",
        category="Gastroenterology",
        definition="Viêm gan B là bệnh nhiễm virus HBV, phổ biến tại Việt Nam, có thể dẫn đến viêm gan mạn, xơ gan, ung thư gan.",
        causes=[
            "Virus HBV (Hepatitis B Virus)",
            "Lây qua đường máu, quan hệ tình dục, từ mẹ sang con",
            "Yếu tố nguy cơ: tiêm chích ma túy, quan hệ tình dục không an toàn, truyền máu không sàng lọc"
        ],
        symptoms=[
            "Viêm gan cấp: mệt mỏi, vàng da, vàng mắt, đau bụng, nôn",
            "Viêm gan mạn: thường không có triệu chứng, hoặc mệt mỏi nhẹ",
            "Có thể không có triệu chứng"
        ],
        diagnosis={
            "criteria": [
                "HBsAg dương tính",
                "Anti-HBc IgM (nếu viêm gan cấp)",
                "HBV DNA (đánh giá tải lượng virus)",
                "Chức năng gan: ALT, AST tăng",
                "Phân loại: viêm gan cấp, viêm gan mạn, người lành mang virus"
            ],
            "tests": [
                "HBsAg, Anti-HBc, Anti-HBs",
                "HBV DNA",
                "Chức năng gan (ALT, AST, Bilirubin, Albumin, PT)",
                "Siêu âm gan",
                "FibroScan (đánh giá xơ hóa gan)"
            ],
            "imaging": [
                "Siêu âm gan",
                "CT/MRI gan (nếu cần)",
                "FibroScan"
            ]
        },
        treatment={
            "general": "Điều trị theo AASLD guidelines. Mục tiêu: ức chế virus, cải thiện chức năng gan, phòng ngừa xơ gan, ung thư gan.",
            "medications": [
                "Nucleos(t)ide analogues: Tenofovir, Entecavir (ưu tiên)",
                "Lamivudine, Adefovir (ít dùng hơn)",
                "Interferon (nếu phù hợp, ít dùng)",
                "Theo dõi: HBV DNA, chức năng gan"
            ],
            "procedures": [
                "Theo dõi định kỳ: HBV DNA, chức năng gan, siêu âm gan",
                "Sinh thiết gan (nếu cần)",
                "Ghép gan (nếu xơ gan nặng)"
            ]
        },
        prevention=[
            "Tiêm vắc xin viêm gan B (quan trọng)",
            "Sàng lọc máu",
            "Quan hệ tình dục an toàn",
            "Không dùng chung kim tiêm",
            "Dự phòng sau phơi nhiễm (HBIG + vắc xin)"
        ],
        complications=[
            "Viêm gan mạn",
            "Xơ gan",
            "Ung thư gan",
            "Suy gan",
            "Tử vong"
        ],
        related_scores=["HBV DNA", "ALT", "Fibrosis Score"],
        related_drugs=["Tenofovir", "Entecavir", "Lamivudine"],
        related_protocols=["Hepatitis B Management"],
        icd10_codes=["B16.9", "B18.0", "B18.1"]
    ),
    
    Disease(
        id="cirrhosis",
        name="Cirrhosis",
        name_vn="Xơ gan",
        category="Gastroenterology",
        definition="Xơ gan là tình trạng thay thế mô gan bình thường bằng mô xơ, dẫn đến suy giảm chức năng gan, phổ biến tại Việt Nam.",
        causes=[
            "Viêm gan B, C mạn",
            "Rượu bia",
            "Viêm gan nhiễm mỡ không do rượu (NAFLD/NASH)",
            "Bệnh gan tự miễn",
            "Bệnh gan do thuốc",
            "Bệnh gan di truyền (Wilson, Hemochromatosis)"
        ],
        symptoms=[
            "Giai đoạn sớm: thường không có triệu chứng",
            "Giai đoạn muộn: mệt mỏi, vàng da, phù chân, cổ trướng",
            "Xuất huyết tiêu hóa (do giãn tĩnh mạch thực quản)",
            "Lú lẫn (bệnh não gan)",
            "Giảm cân"
        ],
        diagnosis={
            "criteria": [
                "Tiền sử bệnh gan",
                "Triệu chứng lâm sàng",
                "Chức năng gan: giảm albumin, tăng bilirubin, PT kéo dài",
                "Siêu âm gan: gan nhỏ, bờ không đều, cổ trướng",
                "Sinh thiết gan (nếu cần)"
            ],
            "tests": [
                "Chức năng gan (ALT, AST, Bilirubin, Albumin, PT/INR)",
                "Công thức máu (giảm tiểu cầu)",
                "Siêu âm gan",
                "FibroScan (đánh giá độ xơ hóa)",
                "Nội soi dạ dày (tìm giãn tĩnh mạch thực quản)"
            ],
            "imaging": [
                "Siêu âm gan",
                "CT/MRI gan",
                "FibroScan"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân và biến chứng. Mục tiêu: làm chậm tiến triển, điều trị biến chứng, phòng ngừa ung thư gan.",
            "medications": [
                "Điều trị nguyên nhân: diệt virus (nếu viêm gan B/C), bỏ rượu",
                "Lợi tiểu (Furosemide, Spironolactone) cho cổ trướng",
                "Lactulose (cho bệnh não gan)",
                "Beta-blocker (Propranolol) - phòng ngừa xuất huyết do giãn tĩnh mạch",
                "Kháng sinh (nếu nhiễm trùng dịch cổ trướng)"
            ],
            "procedures": [
                "Chọc dò dịch cổ trướng (nếu cần)",
                "Nội soi cầm máu (nếu xuất huyết do giãn tĩnh mạch)",
                "TIPS (Transjugular Intrahepatic Portosystemic Shunt) - nếu cổ trướng kháng trị",
                "Ghép gan (nếu nặng)"
            ]
        },
        prevention=[
            "Điều trị viêm gan B, C",
            "Bỏ rượu bia",
            "Kiểm soát cân nặng",
            "Tiêm vắc xin viêm gan A, B",
            "Theo dõi định kỳ"
        ],
        complications=[
            "Cổ trướng",
            "Xuất huyết do giãn tĩnh mạch thực quản",
            "Bệnh não gan",
            "Nhiễm trùng dịch cổ trướng (SBP)",
            "Ung thư gan",
            "Suy gan",
            "Tử vong"
        ],
        related_scores=["Child-Pugh Score", "MELD Score", "Fibrosis Stage"],
        related_drugs=["Furosemide", "Spironolactone", "Lactulose", "Propranolol", "Tenofovir"],
        related_protocols=["Cirrhosis Management", "Ascites Management"],
        icd10_codes=["K74.6", "K74.60", "K74.69"]
    ),
    
    Disease(
        id="irritable_bowel_syndrome",
        name="Irritable Bowel Syndrome",
        name_vn="Hội chứng ruột kích thích (IBS)",
        category="Gastroenterology",
        definition="IBS là rối loạn chức năng đường tiêu hóa mạn tính, đặc trưng bởi đau bụng và thay đổi thói quen đại tiện, phổ biến tại Việt Nam.",
        causes=[
            "Nguyên nhân chưa rõ",
            "Rối loạn vận động ruột",
            "Tăng nhạy cảm nội tạng",
            "Rối loạn hệ vi sinh đường ruột",
            "Yếu tố tâm lý: stress, lo âu",
            "Thức ăn: FODMAP, lactose"
        ],
        symptoms=[
            "Đau bụng (giảm sau đại tiện)",
            "Thay đổi thói quen đại tiện: tiêu chảy, táo bón, hoặc xen kẽ",
            "Đầy bụng, chướng bụng",
            "Phân có nhầy",
            "Cảm giác đi không hết",
            "Triệu chứng tăng khi stress"
        ],
        diagnosis={
            "criteria": [
                "Rome IV criteria: đau bụng ≥ 1 ngày/tuần trong 3 tháng + ≥ 2: liên quan đại tiện, thay đổi tần số, thay đổi hình dạng phân",
                "Loại trừ: bệnh thực thể (viêm ruột, ung thư)",
                "Phân loại: IBS-D (tiêu chảy), IBS-C (táo bón), IBS-M (hỗn hợp)"
            ],
            "tests": [
                "Công thức máu (loại trừ thiếu máu, viêm)",
                "CRP, ESR (loại trừ viêm ruột)",
                "Test không dung nạp lactose",
                "Nội soi đại tràng (nếu có triệu chứng báo động: > 50 tuổi, tiền sử gia đình ung thư, thiếu máu)"
            ],
            "imaging": [
                "Nội soi đại tràng (nếu có chỉ định)"
            ]
        },
        treatment={
            "general": "Điều trị đa yếu tố: chế độ ăn, thuốc, quản lý stress. Mục tiêu: giảm triệu chứng, cải thiện chất lượng cuộc sống.",
            "medications": [
                "Chế độ ăn FODMAP thấp",
                "Chất xơ: Psyllium (nếu táo bón)",
                "Antispasmodic: Hyoscine, Mebeverine",
                "Loperamide (nếu tiêu chảy)",
                "Laxative (nếu táo bón)",
                "Probiotic",
                "Antidepressant liều thấp (nếu có lo âu, trầm cảm)"
            ],
            "procedures": [
                "Giáo dục bệnh nhân",
                "Quản lý stress",
                "Tập thể dục",
                "Theo dõi triệu chứng"
            ]
        },
        prevention=[
            "Chế độ ăn lành mạnh",
            "Quản lý stress",
            "Tập thể dục",
            "Tránh thức ăn kích thích"
        ],
        complications=[
            "Ảnh hưởng chất lượng cuộc sống",
            "Lo âu, trầm cảm",
            "Hạn chế hoạt động xã hội"
        ],
        related_scores=["IBS Severity", "Bristol Stool Scale"],
        related_drugs=["Hyoscine", "Mebeverine", "Loperamide", "Psyllium", "Probiotic"],
        related_protocols=["IBS Management"],
        icd10_codes=["K58.9", "K58.0", "K58.1"]
    ),
    
    Disease(
        id="gastritis",
        name="Gastritis",
        name_vn="Viêm dạ dày",
        category="Gastroenterology",
        definition="Viêm dạ dày là tình trạng viêm niêm mạc dạ dày, rất phổ biến tại Việt Nam, có thể cấp hoặc mạn tính.",
        causes=[
            "Helicobacter pylori (nguyên nhân chính)",
            "NSAID, Aspirin",
            "Rượu bia",
            "Stress",
            "Bệnh tự miễn (hiếm)",
            "Yếu tố nguy cơ: hút thuốc, chế độ ăn không đều"
        ],
        symptoms=[
            "Đau bụng vùng thượng vị",
            "Buồn nôn, nôn",
            "Đầy bụng, khó tiêu",
            "Ợ hơi, ợ chua",
            "Có thể không có triệu chứng (mạn tính)",
            "Chán ăn"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Nội soi dạ dày: niêm mạc đỏ, phù nề, có thể có xung huyết",
                "Test H. pylori: test nhanh urease, C13 breath test, cấy",
                "Sinh thiết (nếu cần)"
            ],
            "tests": [
                "Nội soi dạ dày",
                "Test H. pylori: test nhanh urease, C13 breath test",
                "Sinh thiết (nếu cần)",
                "Công thức máu (thiếu máu nếu có xuất huyết)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị theo nguyên nhân. Nếu có H. pylori, điều trị diệt khuẩn. Tránh yếu tố kích thích.",
            "medications": [
                "Nếu có H. pylori: Triple therapy (PPI + Amoxicillin + Clarithromycin) hoặc Quadruple therapy",
                "PPI: Omeprazole, Lansoprazole (giảm acid)",
                "H2 blocker: Ranitidine, Famotidine",
                "Antacid: Aluminum hydroxide, Magnesium hydroxide",
                "Bảo vệ niêm mạc: Sucralfate",
                "Tránh NSAID, rượu bia"
            ],
            "procedures": [
                "Nội soi dạ dày",
                "Điều trị H. pylori (nếu có)",
                "Theo dõi (nếu mạn tính)"
            ]
        },
        prevention=[
            "Điều trị H. pylori",
            "Tránh NSAID không cần thiết",
            "Hạn chế rượu bia",
            "Chế độ ăn đều đặn",
            "Quản lý stress"
        ],
        complications=[
            "Loét dạ dày",
            "Xuất huyết tiêu hóa",
            "Ung thư dạ dày (nếu H. pylori mạn, không điều trị)",
            "Thiếu máu (nếu xuất huyết mạn)"
        ],
        related_scores=["Gastritis Severity"],
        related_drugs=["Omeprazole", "Lansoprazole", "Amoxicillin", "Clarithromycin", "Ranitidine"],
        related_protocols=["Gastritis Management", "H. pylori Eradication"],
        icd10_codes=["K29.9", "K29.0", "K29.5"]
    ),
    
    Disease(
        id="acute_pancreatitis",
        name="Acute Pancreatitis",
        name_vn="Viêm tụy cấp",
        category="Gastroenterology",
        definition="Viêm tụy cấp là tình trạng viêm cấp tính của tụy, có thể từ nhẹ đến nặng, đe dọa tính mạng.",
        causes=[
            "Sỏi mật (nguyên nhân chính)",
            "Rượu bia",
            "Tăng triglyceride",
            "Thuốc",
            "Chấn thương",
            "Nhiễm trùng",
            "Tăng canxi máu",
            "Vô căn"
        ],
        symptoms=[
            "Đau bụng dữ dội vùng thượng vị, lan ra sau lưng",
            "Buồn nôn, nôn",
            "Sốt",
            "Bụng chướng",
            "Vàng da (nếu do sỏi mật)",
            "Shock (nếu nặng)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: đau bụng đặc trưng",
                "Amylase, Lipase tăng ≥ 3 lần bình thường",
                "CT bụng: viêm tụy, có thể có hoại tử",
                "Phân loại: nhẹ, nặng (theo Atlanta criteria)"
            ],
            "tests": [
                "Amylase, Lipase (tăng ≥ 3 lần)",
                "Công thức máu, CRP",
                "Chức năng thận, gan",
                "CT bụng có tiêm thuốc cản quang",
                "Siêu âm bụng (tìm sỏi mật)"
            ],
            "imaging": [
                "CT bụng (chuẩn vàng)",
                "Siêu âm bụng",
                "MRI/MRCP (nếu cần)"
            ]
        },
        treatment={
            "general": "Điều trị theo Atlanta guidelines. Mục tiêu: giảm đau, bù dịch, điều trị nguyên nhân, phòng ngừa biến chứng.",
            "medications": [
                "Giảm đau: Morphine, Fentanyl",
                "Bù dịch tích cực: Crystalloid",
                "Không ăn uống (NPO) ban đầu",
                "PPI (giảm tiết acid)",
                "Kháng sinh (nếu có nhiễm trùng, hoại tử)",
                "Điều trị nguyên nhân: ERCP (nếu sỏi mật)"
            ],
            "procedures": [
                "Nghỉ tụy: NPO, nuôi dưỡng tĩnh mạch",
                "Bù dịch tích cực",
                "ERCP + cắt cơ vòng Oddi (nếu sỏi mật)",
                "Dẫn lưu (nếu có áp xe, hoại tử)",
                "Phẫu thuật (nếu cần)"
            ]
        },
        prevention=[
            "Điều trị sỏi mật",
            "Hạn chế rượu bia",
            "Điều trị tăng triglyceride",
            "Tránh thuốc gây viêm tụy"
        ],
        complications=[
            "Hoại tử tụy",
            "Áp xe tụy",
            "Giả tụy nang",
            "Suy đa tạng",
            "Tử vong (nếu nặng: 10-30%)"
        ],
        related_scores=["Ranson Score", "APACHE II", "BISAP Score", "CTSI"],
        related_drugs=["Morphine", "Fentanyl", "PPI"],
        related_protocols=["Acute Pancreatitis Management"],
        icd10_codes=["K85.9", "K85.0", "K85.1"]
    ),

    Disease(
        id="ulcerative_colitis",
        name="Ulcerative Colitis",
        name_vn="Viêm loét đại trực tràng chảy máu",
        category="Gastroenterology",
        definition="Viêm loét đại trực tràng chảy máu (UC) là bệnh viêm ruột mạn tính (IBD), gây viêm và loét ở niêm mạc đại tràng và trực tràng.",
        causes=[
            "Tự miễn (hệ miễn dịch tấn công ruột)",
            "Di truyền",
            "Môi trường (chế độ ăn, vi khuẩn)",
            "Yếu tố nguy cơ: tiền sử gia đình, tuổi trẻ (15-30) hoặc lớn tuổi (50-70)"
        ],
        symptoms=[
            "Tiêu chảy kéo dài, thường có máu và nhầy",
            "Đau bụng, co thắt bụng",
            "Mót rặn (tenesmus)",
            "Sụt cân",
            "Sốt (nếu nặng)",
            "Mệt mỏi",
            "Biểu hiện ngoài ruột: đau khớp, viêm mắt, ban da"
        ],
        diagnosis={
            "criteria": [
                "Lâm sàng: tiêu chảy máu mạn tính",
                "Nội soi đại tràng: viêm loét liên tục từ trực tràng lan lên",
                "Mô bệnh học: viêm mạn tính lớp niêm mạc, áp xe hốc",
                "Loại trừ nhiễm trùng (cấy phân)"
            ],
            "tests": [
                "Công thức máu (thiếu máu, tăng bạch cầu)",
                "CRP, ESR (đánh giá mức độ viêm)",
                "Calprotectin trong phân (chẩn đoán phân biệt với IBS)",
                "Cấy phân (loại trừ nhiễm khuẩn, lỵ amip, C.difficile)"
            ],
            "imaging": [
                "Nội soi đại trực tràng (chuẩn vàng)",
                "CT/MRI bụng (đánh giá biến chứng)",
                "X-quang bụng (nếu nghi ngờ phình đại tràng nhiễm độc)"
            ]
        },
        treatment={
            "general": "Mục tiêu: lui bệnh niêm mạc, kiểm soát triệu chứng, nâng cao chất lượng sống. Điều trị leo thang (Step-up) hoặc Top-down tùy mức độ.",
            "medications": [
                "5-ASA (Mesalamine, Sulfasalazine) - cho mức độ nhẹ-trung bình",
                "Corticosteroid (Prednisolone, Hydrocortisone) - cho đợt cấp",
                "Thuốc ức chế miễn dịch (Azathioprine, 6-MP) - duy trì",
                "Thuốc sinh học (Infliximab, Adalimumab, Vedolizumab) - cho mức độ trung bình-nặng"
            ],
            "procedures": [
                "Nội soi theo dõi ung thư (sau 8-10 năm mắc bệnh)",
                "Phẫu thuật cắt đại tràng (nếu kháng trị, biến chứng thủng, ung thư)"
            ]
        },
        prevention=[
            "Tuân thủ điều trị duy trì",
            "Chế độ ăn phù hợp (tránh kích thích, fiber thấp trong đợt cấp)",
            "Tầm soát ung thư đại tràng",
            "Quản lý stress"
        ],
        complications=[
            "Phình đại tràng nhiễm độc (Toxic megacolon)",
            "Thủng ruột",
            "Xuất huyết ồ ạt",
            "Ung thư đại trực tràng (nguy cơ tăng theo thời gian)",
            "Suy dinh dưỡng"
        ],
        related_scores=["Mayo Score", "Truelove and Witts Criteria"],
        related_drugs=["Mesalamine", "Prednisolone", "Azathioprine", "Infliximab"],
        related_protocols=["IBD Management"],
        icd10_codes=["K51.9", "K51.0", "K51.5", "K51.8"]
    ),
]
