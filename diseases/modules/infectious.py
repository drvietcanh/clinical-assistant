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

    Disease(
        id="covid_19",
        name="COVID-19",
        name_vn="COVID-19",
        category="Infectious",
        definition="COVID-19 là bệnh nhiễm virus SARS-CoV-2, gây tổn thương chủ yếu đường hô hấp nhưng có thể ảnh hưởng đa cơ quan.",
        causes=[
            "Virus SARS-CoV-2",
            "Lây qua giọt bắn, khí dung, tiếp xúc gần",
            "Yếu tố nguy cơ: tuổi cao, bệnh mạn tính (tim mạch, phổi, đái tháo đường), béo phì, suy giảm miễn dịch"
        ],
        symptoms=[
            "Sốt, ho khan",
            "Mệt mỏi, đau mỏi cơ",
            "Mất mùi, mất vị",
            "Khó thở, đau ngực",
            "Đau họng, nghẹt mũi",
            "Tiêu chảy, buồn nôn (ít gặp hơn)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng + yếu tố dịch tễ",
                "Xét nghiệm PCR SARS-CoV-2 dương tính",
                "Test nhanh kháng nguyên dương tính (độ nhạy thấp hơn)",
                "Hình ảnh tổn thương phổi trên X-quang/CT (nếu có viêm phổi)"
            ],
            "tests": [
                "RT-PCR SARS-CoV-2 (dịch mũi họng)",
                "Test nhanh kháng nguyên",
                "Công thức máu, CRP, D-dimer, Ferritin",
                "Khí máu động mạch (nếu khó thở)"
            ],
            "imaging": [
                "X-quang ngực",
                "CT ngực (tổn thương kính mờ, tổn thương ngoại biên)"
            ]
        },
        treatment={
            "general": "Điều trị theo mức độ: nhẹ điều trị ngoại trú, nặng cần nhập viện, hỗ trợ hô hấp và kháng virus/corticoid khi có chỉ định.",
            "medications": [
                "Thuốc kháng virus (tuỳ phác đồ quốc gia, ví dụ: Remdesivir)",
                "Corticosteroid (Dexamethasone) nếu có suy hô hấp",
                "Kháng đông (Heparin trọng lượng phân tử thấp) nếu nguy cơ huyết khối cao",
                "Thuốc điều trị triệu chứng: hạ sốt, giảm ho"
            ],
            "procedures": [
                "Oxy liệu pháp qua gọng mũi/mặt nạ",
                "HFNC hoặc thở máy không/xâm lấn nếu suy hô hấp",
                "Điều trị hồi sức tích cực nếu ARDS, sốc nhiễm khuẩn"
            ]
        },
        prevention=[
            "Tiêm vắc xin COVID-19 đầy đủ liều, nhắc lại theo khuyến cáo",
            "Đeo khẩu trang nơi đông người, kín",
            "Rửa tay thường xuyên",
            "Giữ khoảng cách, thông khí tốt",
            "Cách ly khi có triệu chứng hoặc test dương tính"
        ],
        complications=[
            "Viêm phổi nặng, ARDS",
            "Huyết khối tĩnh mạch/động mạch",
            "Tổn thương tim, thận",
            "Hội chứng hậu COVID kéo dài",
            "Tử vong (đặc biệt ở nhóm nguy cơ cao)"
        ],
        related_scores=["NEWS2", "SpO2", "ROX Index"],
        related_drugs=["Remdesivir", "Dexamethasone", "Enoxaparin", "Paracetamol"],
        related_protocols=["COVID-19 Management"],
        icd10_codes=["U07.1", "U07.2"]
    ),

    Disease(
        id="acute_gastroenteritis",
        name="Acute Gastroenteritis",
        name_vn="Tiêu chảy cấp / Viêm dạ dày ruột cấp",
        category="Infectious",
        definition="Tiêu chảy cấp là tình trạng đi phân lỏng ≥ 3 lần/ngày, kéo dài < 14 ngày, thường do nhiễm virus, vi khuẩn hoặc ký sinh trùng.",
        causes=[
            "Virus: Rotavirus, Norovirus, Adenovirus",
            "Vi khuẩn: E. coli, Salmonella, Shigella, Campylobacter, Vibrio cholerae",
            "Ký sinh trùng: Giardia, Entamoeba histolytica",
            "Ăn/uống thực phẩm, nước nhiễm bẩn"
        ],
        symptoms=[
            "Tiêu chảy nhiều lần, phân lỏng hoặc nước",
            "Buồn nôn, nôn",
            "Đau bụng quặn",
            "Có thể sốt",
            "Dấu mất nước: khát, da khô, tiểu ít, chóng mặt"
        ],
        diagnosis={
            "criteria": [
                "Lâm sàng: tiêu chảy cấp, thời gian < 14 ngày",
                "Đánh giá mức độ mất nước",
                "Xét nghiệm phân khi nghi ngờ bệnh nặng, dịch tễ đặc biệt hoặc kéo dài"
            ],
            "tests": [
                "Tổng phân tích phân, soi tươi",
                "Cấy phân (nếu nghi vi khuẩn xâm nhập, dịch tễ)",
                "Xét nghiệm Rotavirus ở trẻ em (nếu cần)",
                "Điện giải đồ, ure/creatinin nếu mất nước nặng"
            ],
            "imaging": []
        },
        treatment={
            "general": "Nguyên tắc chính là bù nước và điện giải, chỉ dùng kháng sinh khi có chỉ định.",
            "medications": [
                "Oresol (ORS) uống từng ngụm nhỏ",
                "Truyền dịch tĩnh mạch nếu mất nước nặng hoặc không uống được",
                "Kháng sinh (Ciprofloxacin, Azithromycin, Ceftriaxone) nếu nghi ngờ vi khuẩn xâm nhập hoặc tả",
                "Racecadotril, Loperamide (tránh ở trẻ nhỏ và tiêu chảy xâm nhập)",
                "Kẽm (trẻ em)"
            ],
            "procedures": [
                "Đánh giá và phân loại mức độ mất nước",
                "Theo dõi lượng nước vào/ra",
                "Cách ly, vệ sinh tay để tránh lây lan"
            ]
        },
        prevention=[
            "Vệ sinh ăn uống, ăn chín uống sôi",
            "Rửa tay bằng xà phòng, đặc biệt sau khi đi vệ sinh và trước khi ăn",
            "Tiêm vắc xin Rotavirus cho trẻ",
            "Xử lý phân, rác thải đúng cách"
        ],
        complications=[
            "Mất nước nặng, sốc giảm thể tích",
            "Rối loạn điện giải",
            "Suy thận cấp",
            "Suy dinh dưỡng ở trẻ em"
        ],
        related_scores=["Dehydration Assessment"],
        related_drugs=["ORS", "Ciprofloxacin", "Azithromycin", "Ceftriaxone"],
        related_protocols=["Acute Diarrhea Management"],
        icd10_codes=["A09", "A00.9"]
    ),

    Disease(
        id="typhoid_fever",
        name="Typhoid Fever",
        name_vn="Thương hàn",
        category="Infectious",
        definition="Thương hàn là bệnh nhiễm khuẩn toàn thân do Salmonella typhi, lây qua đường tiêu hoá, vẫn còn gặp tại các nước đang phát triển.",
        causes=[
            "Vi khuẩn Salmonella enterica serotype Typhi",
            "Lây qua thức ăn, nước uống nhiễm phân người bệnh hoặc người mang trùng",
            "Vệ sinh môi trường và an toàn thực phẩm kém"
        ],
        symptoms=[
            "Sốt cao kéo dài, thường tăng dần",
            "Đau đầu, mệt mỏi",
            "Đau bụng, tiêu chảy hoặc táo bón",
            "Gan lách to",
            "Ban dạng hồng ban trên bụng ngực (rose spots, không phải lúc nào cũng có)"
        ],
        diagnosis={
            "criteria": [
                "Lâm sàng: sốt kéo dài, nhiễm khuẩn toàn thân",
                "Cấy máu dương tính với Salmonella typhi (chuẩn vàng)",
                "Cấy tuỷ xương (nhạy hơn, ít làm)",
                "Huyết thanh Widal ít giá trị, chỉ hỗ trợ"
            ],
            "tests": [
                "Cấy máu (trước kháng sinh)",
                "Công thức máu (thường giảm bạch cầu tương đối)",
                "Chức năng gan, thận",
                "Siêu âm bụng (gan lách to, biến chứng)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị kháng sinh sớm, đủ liều; chăm sóc hỗ trợ, theo dõi biến chứng.",
            "medications": [
                "Ceftriaxone hoặc Cefotaxime tiêm tĩnh mạch",
                "Azithromycin đường uống (trường hợp nhẹ, ngoại trú)",
                "Fluoroquinolone (Ciprofloxacin) ở vùng không kháng thuốc",
                "Hạ sốt: Paracetamol"
            ],
            "procedures": [
                "Nghỉ ngơi tại giường",
                "Bù dịch, dinh dưỡng đầy đủ",
                "Theo dõi thủng ruột, xuất huyết tiêu hóa"
            ]
        },
        prevention=[
            "Tiêm vắc xin thương hàn cho người nguy cơ, đi đến vùng dịch",
            "Vệ sinh ăn uống, nước sạch",
            "Vệ sinh tay, xử lý phân đúng cách",
            "Quản lý người lành mang trùng"
        ],
        complications=[
            "Thủng ruột, xuất huyết tiêu hóa",
            "Viêm cơ tim, viêm phổi",
            "Sốc nhiễm khuẩn",
            "Tử vong nếu không điều trị"
        ],
        related_scores=[],
        related_drugs=["Ceftriaxone", "Azithromycin", "Ciprofloxacin"],
        related_protocols=["Typhoid Fever Management"],
        icd10_codes=["A01.0"]
    ),

    Disease(
        id="helminth_infection",
        name="Intestinal Helminth Infection",
        name_vn="Nhiễm giun đường ruột",
        category="Infectious",
        definition="Nhiễm giun đường ruột (giun đũa, giun móc, giun kim, giun tóc) rất phổ biến tại vùng nhiệt đới như Việt Nam, lây qua đường tiêu hoá.",
        causes=[
            "Giun đũa (Ascaris lumbricoides)",
            "Giun móc/mỏ (Ancylostoma duodenale, Necator americanus)",
            "Giun kim (Enterobius vermicularis)",
            "Giun tóc (Trichuris trichiura)",
            "Ăn uống, vệ sinh kém; trẻ hay chơi đất cát"
        ],
        symptoms=[
            "Có thể không triệu chứng (nhiễm nhẹ)",
            "Đau bụng, đầy hơi",
            "Rối loạn tiêu hoá, tiêu chảy hoặc táo bón",
            "Ngứa hậu môn (giun kim)",
            "Thiếu máu thiếu sắt (giun móc)",
            "Suy dinh dưỡng, chậm phát triển ở trẻ em"
        ],
        diagnosis={
            "criteria": [
                "Lâm sàng + yếu tố dịch tễ",
                "Tìm trứng/giun trong phân (soi phân)",
                "Test băng dính ở hậu môn (giun kim)"
            ],
            "tests": [
                "Soi phân tìm trứng giun",
                "Công thức máu (thiếu máu, tăng bạch cầu ái toan)",
                "Đôi khi thấy giun khi nội soi hoặc chụp X-quang"
            ],
            "imaging": []
        },
        treatment={
            "general": "Tẩy giun bằng thuốc, lặp lại định kỳ; kết hợp cải thiện vệ sinh môi trường.",
            "medications": [
                "Albendazole liều duy nhất hoặc 3 ngày",
                "Mebendazole",
                "Pyrantel pamoate (một số trường hợp)",
                "Bổ sung sắt nếu thiếu máu"
            ],
            "procedures": [
                "Giáo dục vệ sinh: rửa tay, cắt móng tay",
                "Xử lý phân hợp vệ sinh",
                "Chương trình tẩy giun cộng đồng định kỳ"
            ]
        },
        prevention=[
            "Tẩy giun định kỳ 6–12 tháng/lần (trẻ em, người nguy cơ)",
            "Rửa tay trước khi ăn và sau khi đi vệ sinh",
            "Không đi chân đất ở vùng đất ẩm",
            "Ăn chín uống sôi, rửa sạch rau sống"
        ],
        complications=[
            "Tắc ruột do búi giun (hiếm nhưng nặng)",
            "Thiếu máu mạn tính (giun móc)",
            "Suy dinh dưỡng, chậm phát triển",
            "Viêm đường mật, tụy do giun chui ống mật (giun đũa)"
        ],
        related_scores=[],
        related_drugs=["Albendazole", "Mebendazole"],
        related_protocols=["Deworming Program"],
        icd10_codes=["B76.9", "B77.9", "B79"]
    ),

    Disease(
        id="hepatitis_a",
        name="Hepatitis A",
        name_vn="Viêm gan A cấp",
        category="Infectious",
        definition="Viêm gan A là bệnh viêm gan cấp tính do virus HAV, lây qua đường tiêu hoá, thường tự khỏi nhưng có thể gây bùng phát tại cộng đồng.",
        causes=[
            "Virus Hepatitis A (HAV)",
            "Ăn uống, nước uống nhiễm bẩn",
            "Đi lại, sống trong vùng dịch tễ viêm gan A"
        ],
        symptoms=[
            "Sốt nhẹ, mệt mỏi",
            "Chán ăn, buồn nôn, nôn",
            "Đau hạ sườn phải",
            "Vàng da, vàng mắt",
            "Nước tiểu sẫm màu, phân bạc màu"
        ],
        diagnosis={
            "criteria": [
                "Tăng men gan (ALT, AST)",
                "IgM anti-HAV dương tính",
                "Loại trừ các nguyên nhân viêm gan virus khác"
            ],
            "tests": [
                "ALT, AST, Bilirubin, INR",
                "IgM anti-HAV",
                "Siêu âm gan (loại trừ nguyên nhân khác)"
            ],
            "imaging": [
                "Siêu âm gan (thường bình thường hoặc gan to nhẹ)"
            ]
        },
        treatment={
            "general": "Điều trị chủ yếu là nghỉ ngơi, dinh dưỡng, tránh thuốc độc gan, theo dõi suy gan cấp.",
            "medications": [
                "Nghỉ ngơi, bù dịch đầy đủ",
                "Tránh rượu và thuốc độc gan",
                "Điều trị triệu chứng: chống nôn, hạ sốt (Paracetamol liều thấp)"
            ],
            "procedures": [
                "Theo dõi dấu hiệu suy gan cấp: INR tăng, lơ mơ, hôn mê",
                "Nhập viện nếu nặng"
            ]
        },
        prevention=[
            "Tiêm vắc xin viêm gan A cho trẻ em và người nguy cơ",
            "Vệ sinh ăn uống, nước sạch",
            "Rửa tay sau khi đi vệ sinh và trước khi ăn"
        ],
        complications=[
            "Viêm gan tối cấp (hiếm nhưng nặng)",
            "Vàng da kéo dài",
            "Hiếm khi chuyển mạn tính"
        ],
        related_scores=[],
        related_drugs=["Paracetamol"],
        related_protocols=["Acute Hepatitis Management"],
        icd10_codes=["B15.9"]
    ),

    Disease(
        id="cholera",
        name="Cholera",
        name_vn="Bệnh tả",
        category="Infectious",
        definition="Tả là nhiễm khuẩn cấp đường tiêu hóa do Vibrio cholerae, gây tiêu chảy nước ồ ạt, dễ bùng phát dịch ở vùng thiếu nước sạch.",
        causes=[
            "Vibrio cholerae O1/O139",
            "Ăn uống nước/đá/rau sống nhiễm bẩn",
            "Vệ sinh môi trường kém, mùa mưa lũ"
        ],
        symptoms=[
            "Tiêu chảy nước như nước vo gạo, số lượng lớn",
            "Nôn ói",
            "Khát nhiều, co quắp do mất nước",
            "Không sốt hoặc sốt nhẹ"
        ],
        diagnosis={
            "criteria": [
                "Tiêu chảy nước cấp ồ ạt, mất nước nhanh",
                "Yếu tố dịch tễ: vùng có dịch tả",
                "Cấy phân hoặc test nhanh phát hiện Vibrio cholerae"
            ],
            "tests": [
                "Cấy phân (chuẩn vàng)",
                "Test nhanh kháng nguyên tả",
                "Điện giải đồ, ure/creatinin"
            ],
            "imaging": []
        },
        treatment={
            "general": "Bù dịch và điện giải là then chốt; kháng sinh rút ngắn thời gian thải khuẩn.",
            "medications": [
                "ORS uống nếu còn uống được",
                "Truyền Ringer lactate/NaCl 0.9% nếu mất nước nặng",
                "Kháng sinh: Doxycycline liều đơn, hoặc Azithromycin, Ciprofloxacin theo kháng thuốc địa phương",
                "Kẽm cho trẻ em"
            ],
            "procedures": [
                "Theo dõi sát dấu mất nước, mạch, huyết áp",
                "Cách ly nguồn lây, xử lý phân an toàn"
            ]
        },
        prevention=[
            "Nước sạch, ăn chín uống sôi",
            "Vệ sinh tay, xử lý phân đúng cách",
            "Vắc xin tả uống cho vùng nguy cơ cao"
        ],
        complications=[
            "Sốc giảm thể tích",
            "Suy thận cấp",
            "Rối loạn điện giải, toan chuyển hóa",
            "Tử vong nếu mất nước nặng không bù kịp"
        ],
        related_scores=["Dehydration Assessment"],
        related_drugs=["ORS", "Ringer Lactate", "Doxycycline", "Azithromycin"],
        related_protocols=["Cholera Management"],
        icd10_codes=["A00.9"]
    ),

    Disease(
        id="hiv_aids_clinical",
        name="HIV/AIDS (Clinical Stage)",
        name_vn="Nhiễm HIV/AIDS giai đoạn lâm sàng",
        category="Infectious",
        definition="Nhiễm HIV tiến triển gây suy giảm miễn dịch, dễ nhiễm trùng cơ hội; AIDS khi có bệnh chỉ điểm hoặc CD4 rất thấp.",
        causes=[
            "Virus HIV-1/2",
            "Lây qua đường máu, tình dục, mẹ-con",
            "Yếu tố nguy cơ: tiêm chích ma túy, quan hệ không an toàn, truyền máu không sàng lọc"
        ],
        symptoms=[
            "Giai đoạn sớm: không triệu chứng hoặc hội chứng giả cúm",
            "Giai đoạn tiến triển: sụt cân, sốt kéo dài, tiêu chảy mạn",
            "Nhiễm trùng cơ hội: lao, PCP, nấm, CMV",
            "Hạch to, loét miệng, nấm miệng"
        ],
        diagnosis={
            "criteria": [
                "Xét nghiệm khẳng định HIV dương tính (kháng thể/kháng nguyên, PCR)",
                "Đánh giá CD4, tải lượng virus",
                "Chẩn đoán giai đoạn lâm sàng theo WHO/CDC"
            ],
            "tests": [
                "HIV Ab/Ag, PCR tải lượng",
                "CD4 count",
                "Screen lao, viêm gan B/C, giang mai",
                "Công thức máu, chức năng gan thận"
            ],
            "imaging": [
                "X-quang ngực/CT nếu nghi lao, PCP"
            ]
        },
        treatment={
            "general": "Điều trị ARV sớm và suốt đời, dự phòng và điều trị nhiễm trùng cơ hội.",
            "medications": [
                "Phác đồ ARV chuẩn (TDF + 3TC + DTG hoặc tương đương)",
                "Dự phòng PCP: Cotrimoxazole khi CD4 thấp",
                "Điều trị lao đồng nhiễm theo phác đồ quốc gia",
                "Điều trị nhiễm trùng cơ hội tùy tác nhân"
            ],
            "procedures": [
                "Tư vấn tuân thủ ARV",
                "Tiêm chủng phù hợp tình trạng miễn dịch",
                "Theo dõi tải lượng virus, CD4 định kỳ"
            ]
        },
        prevention=[
            "Bao cao su, quan hệ an toàn",
            "Không dùng chung kim tiêm",
            "Điều trị dự phòng sau phơi nhiễm (PEP), trước phơi nhiễm (PrEP)",
            "Sàng lọc máu, mẹ-bé dự phòng lây truyền"
        ],
        complications=[
            "Nhiễm trùng cơ hội (PCP, toxoplasma, CMV, lao)",
            "U lympho không Hodgkin, sarcoma Kaposi",
            "Suy kiệt, tử vong nếu không điều trị"
        ],
        related_scores=["CD4 Count", "Viral Load"],
        related_drugs=["Tenofovir", "Lamivudine", "Dolutegravir", "Cotrimoxazole"],
        related_protocols=["HIV Management"],
        icd10_codes=["B24"]
    ),

    Disease(
        id="rotavirus_gastroenteritis_child",
        name="Rotavirus Gastroenteritis (Child)",
        name_vn="Tiêu chảy do Rotavirus (trẻ em)",
        category="Infectious",
        definition="Tiêu chảy cấp do Rotavirus là nguyên nhân hàng đầu gây tiêu chảy mất nước ở trẻ nhỏ, thường mùa đông xuân.",
        causes=[
            "Rotavirus nhóm A",
            "Lây qua đường phân-miệng, thực phẩm/nước nhiễm bẩn, bề mặt đồ chơi"
        ],
        symptoms=[
            "Nôn ói, tiêu chảy nước nhiều lần",
            "Sốt nhẹ",
            "Dấu mất nước: khát, mắt trũng, tiểu ít",
            "Có thể kèm ho, sổ mũi nhẹ"
        ],
        diagnosis={
            "criteria": [
                "Trẻ <5 tuổi, tiêu chảy nước cấp + nôn",
                "Test kháng nguyên Rotavirus trong phân (+) hỗ trợ"
            ],
            "tests": [
                "Test nhanh kháng nguyên Rotavirus",
                "Điện giải đồ, ure/creatinin nếu mất nước nặng"
            ],
            "imaging": []
        },
        treatment={
            "general": "Bù nước/điện giải là chính; không cần kháng sinh.",
            "medications": [
                "ORS uống từng ngụm nhỏ",
                "Truyền dịch nếu mất nước trung bình-nặng",
                "Kẽm bổ sung cho trẻ em",
                "Hạ sốt: Paracetamol"
            ],
            "procedures": [
                "Theo dõi phân loại mất nước",
                "Dinh dưỡng đầy đủ, tiếp tục cho bú",
                "Cách ly, vệ sinh tay để hạn chế lây lan"
            ]
        },
        prevention=[
            "Vắc xin Rotavirus cho trẻ nhỏ",
            "Rửa tay, vệ sinh đồ chơi, ăn chín uống sôi",
            "Xử lý phân an toàn"
        ],
        complications=[
            "Mất nước nặng, sốc",
            "Rối loạn điện giải",
            "Suy thận cấp (hiếm, do mất nước nặng)"
        ],
        related_scores=["Dehydration Assessment"],
        related_drugs=["ORS", "Zinc", "Paracetamol"],
        related_protocols=["Acute Diarrhea Management"],
        icd10_codes=["A08.0"]
    ),
]


