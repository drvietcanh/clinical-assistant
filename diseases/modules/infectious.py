"""
Infectious Diseases Module
Diseases: Pneumonia, Sepsis, Tuberculosis, Dengue Fever
"""

from typing import List
from diseases.data import Disease


INFECTIOUS_DISEASES: List[Disease] = [
    Disease(
        id="pneumonia",
        name="Pneumonia",
        name_vn="Viêm phổi",
        category="Infectious",
        definition="Viêm phổi là tình trạng nhiễm trùng cấp tính của nhu mô phổi, gây ra bởi vi khuẩn, virus, nấm hoặc các tác nhân khác.",
        causes=[
            "Vi khuẩn: Streptococcus pneumoniae (phổ biến nhất), Haemophilus influenzae, Staphylococcus aureus",
            "Virus: Influenza, RSV, COVID-19",
            "Nấm: Pneumocystis jirovecii (ở bệnh nhân suy giảm miễn dịch)",
            "Các yếu tố nguy cơ: Tuổi cao, suy giảm miễn dịch, bệnh phổi mạn tính, hút thuốc"
        ],
        symptoms=[
            "Sốt, ớn lạnh",
            "Ho có đờm (đờm vàng/xanh, có thể có máu)",
            "Khó thở, thở nhanh",
            "Đau ngực (tăng khi ho hoặc thở sâu)",
            "Mệt mỏi, suy nhược",
            "Ở người già: có thể chỉ có lú lẫn, mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: sốt, ho, đờm, khó thở",
                "Khám phổi: ran nổ, giảm rì rào phế nang",
                "X-quang ngực: thâm nhiễm phổi",
                "Xét nghiệm: tăng bạch cầu, CRP, procalcitonin"
            ],
            "tests": [
                "Công thức máu (CBC)",
                "CRP, Procalcitonin",
                "Cấy đờm (nếu có)",
                "Cấy máu (nếu sốt cao, nghi ngờ nhiễm khuẩn huyết)",
                "Xét nghiệm virus (nếu nghi ngờ)"
            ],
            "imaging": [
                "X-quang ngực thẳng",
                "CT ngực (nếu cần thiết)"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân và mức độ nặng. Hầu hết bệnh nhân có thể điều trị ngoại trú.",
            "medications": [
                "CAP (Viêm phổi cộng đồng): Amoxicillin, Azithromycin, Levofloxacin",
                "HAP (Viêm phổi bệnh viện): Piperacillin-tazobactam, Ceftazidime, Meropenem",
                "Hỗ trợ: Hạ sốt (Paracetamol), Giảm ho, Oxy nếu cần"
            ],
            "procedures": [
                "Oxy liệu pháp nếu SpO2 < 90%",
                "Thở máy nếu suy hô hấp nặng",
                "Dẫn lưu mủ nếu có áp xe phổi"
            ]
        },
        prevention=[
            "Tiêm vắc xin phế cầu (Pneumovax 23, Prevnar 13)",
            "Tiêm vắc xin cúm hàng năm",
            "Bỏ thuốc lá",
            "Rửa tay thường xuyên"
        ],
        complications=[
            "Áp xe phổi",
            "Tràn dịch màng phổi",
            "Nhiễm khuẩn huyết",
            "Suy hô hấp",
            "ARDS (Hội chứng suy hô hấp cấp)"
        ],
        related_scores=["CURB-65", "PSI (Pneumonia Severity Index)"],
        related_drugs=["Amoxicillin", "Azithromycin", "Levofloxacin", "Ceftriaxone"],
        related_protocols=["Viêm phổi cộng đồng (CAP)"],
        icd10_codes=["J18.9", "J15.9", "J12.9"]
    ),
    
    Disease(
        id="sepsis",
        name="Sepsis",
        name_vn="Nhiễm khuẩn huyết / Sepsis",
        category="Infectious",
        definition="Sepsis là phản ứng của cơ thể đối với nhiễm trùng, gây ra rối loạn chức năng cơ quan đe dọa tính mạng.",
        causes=[
            "Nhiễm trùng: vi khuẩn, virus, nấm",
            "Nguồn nhiễm trùng phổ biến: phổi, đường tiết niệu, da, ổ bụng",
            "Yếu tố nguy cơ: tuổi cao, suy giảm miễn dịch, bệnh mạn tính"
        ],
        symptoms=[
            "Sốt hoặc hạ thân nhiệt",
            "Nhịp tim nhanh (>90/phút)",
            "Thở nhanh (>20/phút)",
            "Thay đổi ý thức (lú lẫn, kích động)",
            "Hạ huyết áp (sốc nhiễm khuẩn)",
            "Giảm lượng nước tiểu"
        ],
        diagnosis={
            "criteria": [
                "SOFA score ≥ 2 hoặc qSOFA ≥ 2",
                "Nhiễm trùng đã biết hoặc nghi ngờ",
                "Tăng lactate máu",
                "Tăng procalcitonin, CRP"
            ],
            "tests": [
                "Công thức máu (CBC)",
                "Lactate máu",
                "Procalcitonin, CRP",
                "Cấy máu (2 bộ, trước khi dùng kháng sinh)",
                "Cấy từ nguồn nhiễm trùng",
                "Chức năng thận, gan"
            ],
            "imaging": [
                "X-quang ngực",
                "CT scan (nếu cần tìm nguồn nhiễm trùng)",
                "Siêu âm ổ bụng"
            ]
        },
        treatment={
            "general": "Điều trị khẩn cấp với 1-hour bundle: kháng sinh sớm, bù dịch, vận mạch nếu cần.",
            "medications": [
                "Kháng sinh phổ rộng sớm (trong 1 giờ): Piperacillin-tazobactam, Meropenem",
                "Vận mạch: Norepinephrine (nếu sốc)",
                "Corticosteroid: Hydrocortisone (nếu sốc kháng trị)"
            ],
            "procedures": [
                "Bù dịch tĩnh mạch (30ml/kg trong 3 giờ đầu)",
                "Đặt catheter tĩnh mạch trung tâm",
                "Thở máy nếu suy hô hấp",
                "Lọc máu nếu suy thận"
            ]
        },
        prevention=[
            "Tiêm vắc xin",
            "Vệ sinh tay",
            "Chăm sóc vết thương đúng cách",
            "Điều trị nhiễm trùng sớm"
        ],
        complications=[
            "Sốc nhiễm khuẩn",
            "Suy đa tạng (MODS)",
            "ARDS",
            "Suy thận cấp",
            "Tử vong"
        ],
        related_scores=["SOFA", "qSOFA", "SIRS"],
        related_drugs=["Piperacillin-tazobactam", "Meropenem", "Vancomycin", "Norepinephrine"],
        related_protocols=["Sepsis 1-Hour Bundle", "Sepsis 3-Hour Bundle"],
        icd10_codes=["A41.9", "A41.51", "A41.52"]
    ),
    
    Disease(
        id="tuberculosis",
        name="Tuberculosis",
        name_vn="Lao phổi",
        category="Infectious",
        definition="Lao phổi là bệnh nhiễm trùng do Mycobacterium tuberculosis, chủ yếu ảnh hưởng đến phổi nhưng có thể ảnh hưởng đến các cơ quan khác. Là bệnh phổ biến tại Việt Nam.",
        causes=[
            "Mycobacterium tuberculosis",
            "Lây qua đường hô hấp (giọt bắn)",
            "Yếu tố nguy cơ: suy giảm miễn dịch (HIV), đái tháo đường, suy dinh dưỡng, tiếp xúc gần với người bệnh lao",
            "Sống trong điều kiện đông đúc, thiếu vệ sinh"
        ],
        symptoms=[
            "Ho kéo dài > 2 tuần (có thể có đờm, máu)",
            "Sốt nhẹ về chiều",
            "Ra mồ hôi đêm",
            "Sụt cân",
            "Mệt mỏi, suy nhược",
            "Đau ngực",
            "Khó thở (nếu nặng)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "X-quang ngực: thâm nhiễm phổi (thường ở đỉnh phổi)",
                "AFB (Acid-Fast Bacilli) dương tính trong đờm",
                "Xét nghiệm GeneXpert MTB/RIF (nhanh, chính xác)",
                "Cấy đờm dương tính với M. tuberculosis"
            ],
            "tests": [
                "AFB trong đờm (3 mẫu: sáng sớm)",
                "GeneXpert MTB/RIF (nhanh, phát hiện kháng rifampin)",
                "Cấy đờm (chuẩn vàng, nhưng chậm 4-8 tuần)",
                "Xét nghiệm kháng thuốc (nếu nghi ngờ lao kháng thuốc)",
                "Mantoux test hoặc IGRA (nếu cần)"
            ],
            "imaging": [
                "X-quang ngực (thâm nhiễm, hang lao)",
                "CT ngực (nếu cần đánh giá chi tiết)"
            ]
        },
        treatment={
            "general": "Điều trị theo DOTS (Directly Observed Treatment, Short-course). Phác đồ chuẩn: 6 tháng (2HRZE/4HR).",
            "medications": [
                "Phác đồ chuẩn: Isoniazid (H), Rifampin (R), Pyrazinamide (Z), Ethambutol (E) - 2 tháng đầu",
                "Sau đó: Isoniazid + Rifampin - 4 tháng tiếp theo",
                "Lao kháng thuốc: phác đồ dài hơn, thuốc thay thế",
                "Vitamin B6 (Pyridoxine) - khi dùng Isoniazid"
            ],
            "procedures": [
                "Điều trị DOTS (có giám sát)",
                "Theo dõi chức năng gan, thị lực",
                "Cách ly ban đầu (nếu AFB dương tính)"
            ]
        },
        prevention=[
            "Tiêm vắc xin BCG (trẻ sơ sinh)",
            "Điều trị lao tiềm ẩn (nếu có nguy cơ)",
            "Tránh tiếp xúc với người bệnh lao",
            "Vệ sinh tay, đeo khẩu trang",
            "Cải thiện điều kiện sống"
        ],
        complications=[
            "Lao màng phổi",
            "Lao màng não",
            "Lao xương khớp",
            "Lao thận",
            "Lao kháng thuốc (MDR-TB, XDR-TB)",
            "Tử vong (nếu không điều trị)"
        ],
        related_scores=["TB Score", "TB Treatment Response"],
        related_drugs=["Isoniazid", "Rifampin", "Pyrazinamide", "Ethambutol", "Streptomycin"],
        related_protocols=[],
        icd10_codes=["A15.9", "A15.0", "A15.1", "A16.9"]
    ),
    
    Disease(
        id="dengue_fever",
        name="Dengue Fever",
        name_vn="Sốt xuất huyết Dengue",
        category="Infectious",
        definition="Sốt xuất huyết Dengue là bệnh nhiễm virus do muỗi Aedes truyền, phổ biến tại Việt Nam, đặc biệt vào mùa mưa.",
        causes=[
            "Virus Dengue (DENV-1, DENV-2, DENV-3, DENV-4)",
            "Muỗi Aedes aegypti, Aedes albopictus truyền",
            "Yếu tố nguy cơ: sống trong vùng dịch, mùa mưa"
        ],
        symptoms=[
            "Sốt cao đột ngột (39-40°C), kéo dài 2-7 ngày",
            "Đau đầu, đau sau hốc mắt",
            "Đau cơ, đau khớp",
            "Phát ban",
            "Xuất huyết: chấm xuất huyết, chảy máu cam, chảy máu chân răng",
            "Sốt xuất huyết nặng: sốc, xuất huyết nặng, suy tạng"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Xét nghiệm: NS1 antigen (ngày 1-5), IgM/IgG (sau ngày 5)",
                "Giảm tiểu cầu (< 100,000/μL)",
                "Tăng hematocrit (cô đặc máu)",
                "Phân loại: sốt xuất huyết, sốt xuất huyết có dấu hiệu cảnh báo, sốt xuất huyết nặng"
            ],
            "tests": [
                "NS1 antigen (ngày 1-5)",
                "IgM/IgG Dengue (sau ngày 5)",
                "Công thức máu (giảm tiểu cầu, tăng hematocrit)",
                "Chức năng gan (ALT, AST tăng)",
                "Đông máu (nếu nghi ngờ nặng)"
            ],
            "imaging": [
                "Siêu âm bụng (tràn dịch màng bụng, màng phổi)",
                "X-quang ngực (tràn dịch màng phổi)"
            ]
        },
        treatment={
            "general": "Điều trị hỗ trợ. Quan trọng: bù dịch đúng cách, theo dõi sát dấu hiệu cảnh báo, sốc.",
            "medications": [
                "Paracetamol (hạ sốt) - tránh Aspirin, NSAID",
                "Bù dịch: Ringer lactate, Normal saline",
                "Truyền tiểu cầu (nếu tiểu cầu < 20,000 và xuất huyết)",
                "Truyền máu (nếu xuất huyết nặng)",
                "Không dùng kháng sinh (trừ khi có nhiễm khuẩn kèm)"
            ],
            "procedures": [
                "Theo dõi sát: tiểu cầu, hematocrit, dấu hiệu sốc",
                "Bù dịch tĩnh mạch (nếu có dấu hiệu cảnh báo hoặc sốc)",
                "Thở máy (nếu suy hô hấp)",
                "Lọc máu (nếu suy thận)"
            ]
        },
        prevention=[
            "Diệt muỗi, lăng quăng",
            "Đậy kín dụng cụ chứa nước",
            "Ngủ màn",
            "Mặc quần áo dài",
            "Dùng thuốc chống muỗi",
            "Vắc xin Dengue (Dengvaxia) - có chỉ định cụ thể"
        ],
        complications=[
            "Sốc sốt xuất huyết (DSS)",
            "Xuất huyết nặng",
            "Suy tạng (gan, thận)",
            "Suy hô hấp",
            "Tử vong (nếu không điều trị kịp thời)"
        ],
        related_scores=["Platelet Count", "Hematocrit", "Warning Signs"],
        related_drugs=["Paracetamol", "Ringer Lactate", "Normal Saline"],
        related_protocols=[],
        icd10_codes=["A90", "A91"]
    ),
    
    Disease(
        id="malaria",
        name="Malaria",
        name_vn="Sốt rét",
        category="Infectious",
        definition="Sốt rét là bệnh nhiễm ký sinh trùng do muỗi Anopheles truyền, vẫn còn lưu hành tại một số vùng miền núi Việt Nam.",
        causes=[
            "Ký sinh trùng: Plasmodium falciparum, P. vivax, P. malariae, P. ovale",
            "Muỗi Anopheles truyền",
            "Yếu tố nguy cơ: sống trong vùng lưu hành, không có biện pháp phòng ngừa"
        ],
        symptoms=[
            "Sốt cao, ớn lạnh, vã mồ hôi (chu kỳ 48-72h)",
            "Đau đầu, đau cơ",
            "Mệt mỏi",
            "Buồn nôn, nôn",
            "Thiếu máu",
            "Lách to",
            "Sốt rét nặng (P. falciparum): rối loạn ý thức, suy thận, sốc"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng + tiền sử vùng lưu hành",
                "Ký sinh trùng trong máu (thick/thin smear) - chuẩn vàng",
                "Test nhanh (RDT)",
                "PCR (nếu cần xác định loài)"
            ],
            "tests": [
                "Thick/thin smear (tìm ký sinh trùng)",
                "Test nhanh (RDT)",
                "PCR (nếu cần)",
                "Công thức máu (thiếu máu, giảm tiểu cầu)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị theo WHO guidelines. Quan trọng: điều trị sớm, đúng phác đồ, phòng ngừa tái phát (P. vivax).",
            "medications": [
                "P. falciparum: Artesunate + Mefloquine hoặc Artemether-Lumefantrine",
                "P. vivax: Chloroquine + Primaquine (diệt thể ngủ)",
                "P. malariae: Chloroquine",
                "Sốt rét nặng: Artesunate IV"
            ],
            "procedures": [
                "Theo dõi sát (nếu sốt rét nặng)",
                "Truyền máu (nếu thiếu máu nặng)",
                "Lọc máu (nếu suy thận)"
            ]
        },
        prevention=[
            "Ngủ màn có tẩm hóa chất",
            "Dùng thuốc chống muỗi",
            "Dự phòng: Doxycycline, Mefloquine (nếu đi vùng lưu hành)",
            "Diệt muỗi, lăng quăng"
        ],
        complications=[
            "Sốt rét nặng (P. falciparum)",
            "Thiếu máu",
            "Suy thận",
            "Sốc",
            "Tử vong (nếu không điều trị kịp thời)"
        ],
        related_scores=["Parasite Count", "Malaria Severity"],
        related_drugs=["Artesunate", "Mefloquine", "Artemether-Lumefantrine", "Chloroquine", "Primaquine"],
        related_protocols=["Malaria Treatment"],
        icd10_codes=["B50.9", "B51.9", "B52", "B53.0"]
    ),
    
    Disease(
        id="japanese_encephalitis",
        name="Japanese Encephalitis",
        name_vn="Viêm não Nhật Bản",
        category="Infectious",
        definition="Viêm não Nhật Bản là bệnh nhiễm virus do muỗi Culex truyền, nguy hiểm, có thể gây tử vong hoặc di chứng thần kinh, phổ biến tại Việt Nam.",
        causes=[
            "Virus Japanese Encephalitis (JEV)",
            "Muỗi Culex truyền (từ lợn, chim)",
            "Yếu tố nguy cơ: sống vùng nông thôn, mùa mưa, chưa tiêm vắc xin"
        ],
        symptoms=[
            "Giai đoạn cấp: sốt cao, đau đầu, nôn",
            "Rối loạn ý thức: lú lẫn, hôn mê",
            "Co giật",
            "Cứng gáy",
            "Liệt",
            "Thường không có triệu chứng (nhiễm không triệu chứng)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Dịch tễ: vùng lưu hành, mùa",
                "IgM JEV dương tính (CSF hoặc máu)",
                "PCR (nếu có)",
                "CT/MRI não: tổn thương thùy thái dương, nhân xám"
            ],
            "tests": [
                "IgM JEV (CSF hoặc máu)",
                "PCR (nếu có)",
                "CT/MRI não",
                "Dịch não tủy: tăng bạch cầu, protein"
            ],
            "imaging": [
                "CT não",
                "MRI não"
            ]
        },
        treatment={
            "general": "Điều trị hỗ trợ. Không có thuốc đặc hiệu. Quan trọng: hỗ trợ hô hấp, tuần hoàn, chống co giật.",
            "medications": [
                "Hỗ trợ: hạ sốt, chống co giật",
                "Corticosteroid (có thể giúp)",
                "Không có thuốc kháng virus đặc hiệu"
            ],
            "procedures": [
                "Thở máy (nếu suy hô hấp)",
                "Theo dõi sát",
                "Vật lý trị liệu (sau khi ổn định)"
            ]
        },
        prevention=[
            "Tiêm vắc xin JEV (quan trọng nhất)",
            "Ngủ màn",
            "Diệt muỗi",
            "Tránh vùng lưu hành"
        ],
        complications=[
            "Di chứng thần kinh: liệt, co giật, chậm phát triển",
            "Tử vong (20-30%)",
            "Tàn tật vĩnh viễn"
        ],
        related_scores=["GCS", "JEV IgM"],
        related_drugs=["Corticosteroid", "Anticonvulsant"],
        related_protocols=[],
        icd10_codes=["A83.0"]
    ),
    
    Disease(
        id="influenza",
        name="Influenza",
        name_vn="Cúm",
        category="Infectious",
        definition="Cúm là bệnh nhiễm virus đường hô hấp cấp tính, rất phổ biến tại Việt Nam, đặc biệt vào mùa đông xuân, có thể gây biến chứng nặng.",
        causes=[
            "Virus: Influenza A, B, C",
            "Lây qua đường hô hấp: giọt bắn, tiếp xúc",
            "Yếu tố nguy cơ: trẻ em, người già, phụ nữ mang thai, bệnh mạn tính, suy giảm miễn dịch"
        ],
        symptoms=[
            "Sốt cao đột ngột",
            "Ớn lạnh",
            "Đau đầu, đau cơ",
            "Mệt mỏi",
            "Ho, đau họng",
            "Sổ mũi",
            "Có thể có buồn nôn, nôn (ở trẻ em)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng điển hình",
                "Test nhanh cúm (RIDT)",
                "PCR (nếu cần xác định type)",
                "Dịch tễ: mùa cúm, tiếp xúc người bệnh"
            ],
            "tests": [
                "Test nhanh cúm (RIDT)",
                "PCR (nếu cần)",
                "Công thức máu (giảm bạch cầu)",
                "Cấy virus (nếu cần)"
            ],
            "imaging": [
                "X-quang ngực (nếu có biến chứng viêm phổi)"
            ]
        },
        treatment={
            "general": "Điều trị hỗ trợ. Kháng virus nếu có chỉ định (trong 48 giờ đầu).",
            "medications": [
                "Kháng virus: Oseltamivir, Zanamivir (nếu có chỉ định, trong 48h đầu)",
                "Hạ sốt: Paracetamol, Ibuprofen",
                "Nghỉ ngơi, uống nhiều nước",
                "Không dùng kháng sinh (trừ khi có nhiễm khuẩn kèm)"
            ],
            "procedures": [
                "Nghỉ ngơi",
                "Cách ly (tránh lây lan)",
                "Theo dõi biến chứng"
            ]
        },
        prevention=[
            "Tiêm vắc xin cúm hàng năm (quan trọng nhất)",
            "Rửa tay thường xuyên",
            "Đeo khẩu trang",
            "Tránh tiếp xúc người bệnh",
            "Che miệng khi ho, hắt hơi"
        ],
        complications=[
            "Viêm phổi (virus hoặc vi khuẩn thứ phát)",
            "Viêm cơ tim",
            "Viêm não",
            "Suy hô hấp",
            "Tử vong (nếu biến chứng nặng)"
        ],
        related_scores=["Influenza Severity"],
        related_drugs=["Oseltamivir", "Zanamivir", "Paracetamol"],
        related_protocols=["Influenza Management"],
        icd10_codes=["J11.1", "J10.1"]
    ),
]


