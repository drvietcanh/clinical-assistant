"""
ENT (Ear, Nose, Throat) Module
Diseases: Acute Pharyngitis, Sinusitis, Otitis Media
"""

from typing import List
from diseases.data import Disease


ENT_DISEASES: List[Disease] = [
    Disease(
        id="acute_pharyngitis",
        name="Acute Pharyngitis",
        name_vn="Viêm họng cấp",
        category="ENT",
        definition="Viêm họng cấp là tình trạng viêm nhiễm cấp tính vùng họng, rất phổ biến tại Việt Nam, đặc biệt khi thay đổi thời tiết.",
        causes=[
            "Virus: Rhinovirus, Adenovirus, Influenza, COVID-19 (80-90%)",
            "Vi khuẩn: Streptococcus pyogenes (Group A Strep) - 10-20%",
            "Yếu tố nguy cơ: thay đổi thời tiết, tiếp xúc người bệnh, suy giảm miễn dịch"
        ],
        symptoms=[
            "Đau họng, rát họng",
            "Khó nuốt",
            "Sốt (thường nhẹ nếu virus, cao nếu vi khuẩn)",
            "Ho",
            "Sổ mũi, nghẹt mũi (nếu virus)",
            "Sưng hạch cổ",
            "Đau đầu, mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Khám họng: đỏ, phù nề, có thể có mủ (nếu vi khuẩn)",
                "Test nhanh Strep A (nếu nghi ngờ vi khuẩn)",
                "Cấy dịch họng (nếu cần)"
            ],
            "tests": [
                "Khám lâm sàng",
                "Test nhanh Strep A",
                "Cấy dịch họng (nếu nghi ngờ vi khuẩn)",
                "Công thức máu (nếu sốt cao)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị theo nguyên nhân. Hầu hết do virus, tự khỏi. Vi khuẩn cần kháng sinh.",
            "medications": [
                "Virus: điều trị triệu chứng - Paracetamol, Ibuprofen (hạ sốt, giảm đau)",
                "Vi khuẩn: Penicillin V hoặc Amoxicillin (10 ngày)",
                "Nếu dị ứng Penicillin: Azithromycin, Clarithromycin",
                "Súc họng nước muối, viên ngậm"
            ],
            "procedures": [
                "Nghỉ ngơi, uống nhiều nước",
                "Súc họng nước muối ấm"
            ]
        },
        prevention=[
            "Rửa tay thường xuyên",
            "Tránh tiếp xúc người bệnh",
            "Đeo khẩu trang",
            "Tiêm vắc xin cúm"
        ],
        complications=[
            "Viêm họng mạn",
            "Áp xe quanh amidan (nếu vi khuẩn)",
            "Viêm tai giữa",
            "Viêm xoang",
            "Sốt thấp khớp (nếu Strep A không điều trị)"
        ],
        related_scores=["Centor Score", "McIsaac Score"],
        related_drugs=["Amoxicillin", "Penicillin V", "Azithromycin", "Paracetamol"],
        related_protocols=[],
        icd10_codes=["J02.9", "J02.0"]
    ),
    
    Disease(
        id="sinusitis",
        name="Sinusitis",
        name_vn="Viêm xoang",
        category="ENT",
        definition="Viêm xoang là tình trạng viêm nhiễm các xoang cạnh mũi, phổ biến tại Việt Nam do khí hậu ẩm, ô nhiễm.",
        causes=[
            "Virus: thường sau cảm lạnh",
            "Vi khuẩn: Streptococcus pneumoniae, Haemophilus influenzae, Moraxella catarrhalis",
            "Nấm (hiếm)",
            "Yếu tố nguy cơ: dị ứng, polyp mũi, lệch vách ngăn mũi, khí hậu ẩm"
        ],
        symptoms=[
            "Nghẹt mũi",
            "Chảy dịch mũi (vàng/xanh nếu vi khuẩn)",
            "Đau đầu, đau mặt (vùng xoang)",
            "Giảm khứu giác",
            "Ho (do dịch chảy xuống họng)",
            "Sốt (nếu vi khuẩn)",
            "Mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Khám mũi: niêm mạc phù nề, có dịch mủ",
                "Phân loại: cấp (< 4 tuần), bán cấp (4-12 tuần), mạn (> 12 tuần)"
            ],
            "tests": [
                "Khám lâm sàng",
                "Nội soi mũi xoang (nếu có)",
                "CT xoang (nếu mạn, nghi ngờ biến chứng)",
                "Cấy dịch mũi (nếu cần)"
            ],
            "imaging": [
                "CT xoang (chuẩn vàng cho viêm xoang mạn)",
                "X-quang xoang (ít dùng)"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân và mức độ. Mục tiêu: giảm viêm, thông thoáng xoang.",
            "medications": [
                "Rửa mũi bằng nước muối sinh lý",
                "Corticosteroid xịt mũi (Fluticasone, Mometasone)",
                "Kháng sinh: Amoxicillin-clavulanate, Levofloxacin (nếu vi khuẩn, > 7-10 ngày)",
                "Decongestant (Pseudoephedrine) - ngắn hạn",
                "Antihistamine (nếu dị ứng)"
            ],
            "procedures": [
                "Rửa mũi xoang",
                "Phẫu thuật nội soi xoang (nếu mạn, kháng trị)"
            ]
        },
        prevention=[
            "Điều trị dị ứng",
            "Rửa mũi thường xuyên",
            "Tránh khói thuốc, ô nhiễm",
            "Điều trị cảm lạnh sớm"
        ],
        complications=[
            "Viêm xoang mạn",
            "Viêm màng não",
            "Áp xe quanh ổ mắt",
            "Viêm xương sọ",
            "Polyp mũi"
        ],
        related_scores=["Sinusitis Severity"],
        related_drugs=["Amoxicillin-clavulanate", "Levofloxacin", "Fluticasone", "Mometasone"],
        related_protocols=[],
        icd10_codes=["J01.9", "J32.9"]
    ),
    
    Disease(
        id="otitis_media",
        name="Otitis Media",
        name_vn="Viêm tai giữa",
        category="ENT",
        definition="Viêm tai giữa là tình trạng viêm nhiễm tai giữa, rất phổ biến ở trẻ em tại Việt Nam.",
        causes=[
            "Vi khuẩn: Streptococcus pneumoniae, Haemophilus influenzae, Moraxella catarrhalis",
            "Virus: RSV, Rhinovirus",
            "Yếu tố nguy cơ: trẻ em, viêm đường hô hấp trên, hút thuốc thụ động, bú bình nằm"
        ],
        symptoms=[
            "Đau tai (trẻ em: quấy khóc, kéo tai)",
            "Sốt",
            "Chảy dịch tai (nếu thủng màng nhĩ)",
            "Giảm thính lực",
            "Mệt mỏi, chán ăn",
            "Ở trẻ nhỏ: quấy khóc, khó ngủ"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Soi tai: màng nhĩ đỏ, phồng, có dịch",
                "Phân loại: viêm tai giữa cấp (AOM), viêm tai giữa có tràn dịch (OME)"
            ],
            "tests": [
                "Soi tai (otoscopy)",
                "Đo nhĩ lượng (tympanometry) - nếu có",
                "Cấy dịch tai (nếu chảy dịch)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị theo AAP guidelines. Trẻ > 2 tuổi, nhẹ có thể theo dõi. Nặng hoặc < 2 tuổi cần kháng sinh.",
            "medications": [
                "Kháng sinh: Amoxicillin (80-90 mg/kg/ngày) - thuốc đầu tay",
                "Nếu dị ứng Penicillin: Azithromycin, Cefdinir",
                "Nếu kháng Amoxicillin: Amoxicillin-clavulanate",
                "Giảm đau: Paracetamol, Ibuprofen",
                "Nhỏ tai (nếu thủng màng nhĩ, có chỉ định)"
            ],
            "procedures": [
                "Theo dõi (nếu nhẹ, trẻ > 2 tuổi)",
                "Chọc màng nhĩ (nếu áp lực cao, đau nhiều)",
                "Đặt ống thông khí (nếu tái phát nhiều lần)"
            ]
        },
        prevention=[
            "Tiêm vắc xin phế cầu, Hib",
            "Tiêm vắc xin cúm",
            "Bú mẹ (giảm nguy cơ)",
            "Tránh hút thuốc thụ động",
            "Điều trị viêm đường hô hấp trên sớm"
        ],
        complications=[
            "Thủng màng nhĩ",
            "Viêm xương chũm",
            "Giảm thính lực",
            "Viêm màng não",
            "Viêm tai giữa mạn"
        ],
        related_scores=["AOM Severity"],
        related_drugs=["Amoxicillin", "Amoxicillin-clavulanate", "Azithromycin", "Cefdinir"],
        related_protocols=[],
        icd10_codes=["H66.9", "H65.9"]
    ),
    
    Disease(
        id="tonsillitis",
        name="Tonsillitis",
        name_vn="Viêm amidan",
        category="ENT",
        definition="Viêm amidan là tình trạng viêm nhiễm amidan, rất phổ biến, đặc biệt ở trẻ em, có thể cấp hoặc mạn tính.",
        causes=[
            "Virus: Adenovirus, Rhinovirus, EBV (phổ biến nhất)",
            "Vi khuẩn: Streptococcus pyogenes (Group A Strep) - 15-30%",
            "Yếu tố nguy cơ: trẻ em, tiếp xúc người bệnh, suy giảm miễn dịch"
        ],
        symptoms=[
            "Đau họng",
            "Khó nuốt",
            "Sốt",
            "Amidan sưng, đỏ, có thể có mủ (nếu vi khuẩn)",
            "Sưng hạch cổ",
            "Hơi thở hôi",
            "Đau đầu, mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Khám họng: amidan sưng, đỏ, có thể có mủ",
                "Test nhanh Strep A (nếu nghi ngờ vi khuẩn)",
                "Cấy dịch họng (nếu cần)",
                "Phân loại: cấp, mạn, tái phát"
            ],
            "tests": [
                "Khám lâm sàng",
                "Test nhanh Strep A",
                "Cấy dịch họng (nếu nghi ngờ vi khuẩn)",
                "Công thức máu (tăng bạch cầu nếu vi khuẩn)",
                "Monospot test (nếu nghi ngờ EBV)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị theo nguyên nhân. Virus tự khỏi. Vi khuẩn cần kháng sinh. Phẫu thuật nếu tái phát nhiều lần.",
            "medications": [
                "Virus: điều trị triệu chứng - Paracetamol, Ibuprofen",
                "Vi khuẩn: Penicillin V hoặc Amoxicillin (10 ngày)",
                "Nếu dị ứng Penicillin: Azithromycin, Clarithromycin",
                "Súc họng nước muối, viên ngậm"
            ],
            "procedures": [
                "Nghỉ ngơi, uống nhiều nước",
                "Súc họng nước muối",
                "Cắt amidan (nếu tái phát nhiều lần: ≥ 7 lần/năm, ≥ 5 lần/năm trong 2 năm, ≥ 3 lần/năm trong 3 năm)"
            ]
        },
        prevention=[
            "Rửa tay thường xuyên",
            "Tránh tiếp xúc người bệnh",
            "Đeo khẩu trang",
            "Vệ sinh răng miệng"
        ],
        complications=[
            "Áp xe quanh amidan",
            "Viêm tai giữa",
            "Viêm xoang",
            "Sốt thấp khớp (nếu Strep A không điều trị)",
            "Viêm cầu thận (nếu Strep A không điều trị)"
        ],
        related_scores=["Centor Score", "McIsaac Score"],
        related_drugs=["Amoxicillin", "Penicillin V", "Azithromycin", "Paracetamol"],
        related_protocols=[],
        icd10_codes=["J03.9", "J35.0"]
    ),

    Disease(
        id="allergic_rhinitis",
        name="Allergic Rhinitis",
        name_vn="Viêm mũi dị ứng",
        category="ENT",
        definition="Viêm mũi dị ứng là tình trạng viêm niêm mạc mũi qua trung gian IgE do tiếp xúc dị nguyên hô hấp, rất thường gặp tại Việt Nam.",
        causes=[
            "Dị nguyên hít phải: bụi nhà, phấn hoa, lông thú, nấm mốc, gián",
            "Yếu tố nguy cơ: tiền sử cơ địa dị ứng (hen, eczema), gia đình có người bị dị ứng, môi trường ô nhiễm"
        ],
        symptoms=[
            "Hắt hơi thành tràng",
            "Ngạt mũi, chảy mũi nước trong",
            "Ngứa mũi, ngứa mắt, đỏ mắt",
            "Giảm ngửi, đau đầu, mệt mỏi (nếu kéo dài)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng điển hình, tái diễn theo mùa hoặc quanh năm",
                "Khám mũi: niêm mạc nhợt, phù nề, nhiều dịch trong",
                "Test dị ứng da hoặc IgE đặc hiệu (nếu cần xác định dị nguyên)"
            ],
            "tests": [
                "Test lẩy da (skin prick test) với dị nguyên hít",
                "Định lượng IgE tổng và IgE đặc hiệu",
                "Nội soi mũi xoang (loại trừ polyp, viêm xoang mạn)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Mục tiêu là kiểm soát triệu chứng, cải thiện chất lượng sống và giảm nguy cơ hen.",
            "medications": [
                "Kháng histamine uống thế hệ 2: Cetirizine, Loratadine, Fexofenadine",
                "Corticosteroid xịt mũi: Fluticasone, Mometasone (hiệu quả nhất dài hạn)",
                "Thuốc co mạch mũi (ngắn hạn, tối đa 5-7 ngày) nếu nghẹt nhiều",
                "Kháng leukotriene (Montelukast) nếu kèm hen",
                "Rửa mũi bằng dung dịch nước muối"
            ],
            "procedures": [
                "Tránh, giảm tiếp xúc dị nguyên (giặt chăn ga, hút bụi, dùng máy lọc không khí)",
                "Liệu pháp giải mẫn cảm đặc hiệu (AIT) nếu có điều kiện"
            ]
        },
        prevention=[
            "Giảm bụi nhà, nấm mốc, lông thú trong môi trường sống",
            "Đóng cửa sổ khi mùa phấn hoa nhiều, dùng khẩu trang",
            "Không hút thuốc, tránh khói thuốc"
        ],
        complications=[
            "Viêm xoang mạn tính",
            "Polyp mũi",
            "Khởi phát hoặc làm nặng hen phế quản",
            "Rối loạn giấc ngủ, giảm tập trung"
        ],
        related_scores=["ARIA Classification"],
        related_drugs=["Cetirizine", "Loratadine", "Fluticasone", "Montelukast"],
        related_protocols=["Allergic Rhinitis Management"],
        icd10_codes=["J30.4", "J30.1"]
    ),

    Disease(
        id="acute_laryngitis",
        name="Acute Laryngitis",
        name_vn="Viêm thanh quản cấp",
        category="ENT",
        definition="Viêm thanh quản cấp là tình trạng viêm niêm mạc thanh quản, thường do virus, biểu hiện khàn tiếng, mất tiếng, ho khan.",
        causes=[
            "Nhiễm virus đường hô hấp trên",
            "Quá dùng giọng nói (la hét, nói nhiều)",
            "Hít khói thuốc, khí kích thích",
            "Trào ngược dạ dày thực quản"
        ],
        symptoms=[
            "Khàn tiếng hoặc mất tiếng",
            "Ho khan, đau rát họng",
            "Cảm giác vướng ở họng",
            "Sốt nhẹ, mệt mỏi (nếu do nhiễm trùng)"
        ],
        diagnosis={
            "criteria": [
                "Lâm sàng: khàn tiếng cấp sau nhiễm virus hoặc quá dùng giọng",
                "Nội soi thanh quản (nếu cần): niêm mạc đỏ, phù nề",
                "Loại trừ các nguyên nhân nghiêm trọng (u, liệt dây thanh) nếu khàn tiếng kéo dài > 3 tuần"
            ],
            "tests": [
                "Thường không cần xét nghiệm",
                "Nội soi thanh quản sợi mềm nếu khàn tiếng kéo dài hoặc cảnh báo"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị chủ yếu là nghỉ giọng và điều chỉnh yếu tố thuận lợi.",
            "medications": [
                "Hạ sốt, giảm đau: Paracetamol, Ibuprofen",
                "Thuốc ho, siro làm dịu họng",
                "PPI hoặc thuốc kháng acid nếu kèm GERD",
                "Kháng sinh chỉ dùng khi có bằng chứng nhiễm khuẩn"
            ],
            "procedures": [
                "Nghỉ nói, tránh la hét, tránh thì thầm kéo dài",
                "Uống đủ nước, làm ẩm không khí"
            ]
        },
        prevention=[
            "Hạn chế lạm dụng giọng nói",
            "Tránh hút thuốc, khói thuốc và khí kích thích",
            "Điều trị trào ngược dạ dày thực quản nếu có"
        ],
        complications=[
            "Viêm thanh quản mạn",
            "Nốt dây thanh do quá dùng giọng",
            "Ảnh hưởng công việc với người dùng giọng nhiều (giáo viên, ca sĩ)"
        ],
        related_scores=[],
        related_drugs=["Paracetamol", "Ibuprofen"],
        related_protocols=["Acute Laryngitis Management"],
        icd10_codes=["J04.0"]
    ),
]
