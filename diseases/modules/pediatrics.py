"""
Pediatrics Module
Children's diseases and conditions
"""

from typing import List
from diseases.data import Disease


PEDIATRICS_DISEASES: List[Disease] = [
    Disease(
        id="malnutrition",
        name="Malnutrition",
        name_vn="Suy dinh dưỡng",
        category="Pediatrics",
        definition="Suy dinh dưỡng là tình trạng thiếu hụt dinh dưỡng, rất phổ biến ở trẻ em vùng nông thôn Việt Nam, ảnh hưởng đến phát triển thể chất và trí tuệ.",
        causes=[
            "Thiếu cung cấp: nghèo đói, thiếu thức ăn",
            "Kém hấp thu: bệnh tiêu hóa, nhiễm ký sinh trùng",
            "Tăng nhu cầu: bệnh mạn tính, nhiễm trùng",
            "Yếu tố xã hội: thiếu kiến thức dinh dưỡng, vệ sinh kém"
        ],
        symptoms=[
            "Sụt cân, chậm tăng cân",
            "Thấp còi (stunting)",
            "Gầy mòn (wasting)",
            "Mệt mỏi, kém hoạt động",
            "Chậm phát triển tâm thần vận động",
            "Da khô, tóc khô, dễ rụng",
            "Phù (nếu thiếu protein nặng - kwashiorkor)"
        ],
        diagnosis={
            "criteria": [
                "Đánh giá nhân trắc: cân nặng, chiều cao, vòng cánh tay",
                "Z-score: < -2 SD (suy dinh dưỡng)",
                "Phân loại: nhẹ (-2 đến -3 SD), trung bình (-3 đến -4 SD), nặng (< -4 SD)",
                "Đánh giá nguyên nhân"
            ],
            "tests": [
                "Đo cân nặng, chiều cao",
                "Tính Z-score (WHO growth charts)",
                "Albumin, prealbumin",
                "Hemoglobin (thiếu máu)",
                "Xét nghiệm ký sinh trùng"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị đa yếu tố: bổ sung dinh dưỡng, điều trị nguyên nhân, giáo dục gia đình.",
            "medications": [
                "Bổ sung dinh dưỡng: sữa công thức đặc biệt, thức ăn bổ sung",
                "Bổ sung vi chất: sắt, kẽm, vitamin A, D",
                "Điều trị nhiễm ký sinh trùng",
                "Điều trị nhiễm trùng"
            ],
            "procedures": [
                "Giáo dục dinh dưỡng cho gia đình",
                "Theo dõi tăng trưởng",
                "Điều trị nguyên nhân",
                "Hỗ trợ xã hội"
            ]
        },
        prevention=[
            "Nuôi con bằng sữa mẹ",
            "Chế độ ăn đầy đủ, đa dạng",
            "Bổ sung vi chất",
            "Vệ sinh, nước sạch",
            "Giáo dục dinh dưỡng",
            "Tẩy giun định kỳ"
        ],
        complications=[
            "Chậm phát triển thể chất",
            "Chậm phát triển trí tuệ",
            "Thiếu máu",
            "Nhiễm trùng",
            "Tử vong (nếu nặng)"
        ],
        related_scores=["Z-score", "MUAC", "Weight-for-Height"],
        related_drugs=["Iron", "Zinc", "Vitamin A", "Vitamin D"],
        related_protocols=[],
        icd10_codes=["E46", "E43", "E44.0", "E44.1"]
    ),
    
    Disease(
        id="hand_foot_mouth_disease",
        name="Hand, Foot and Mouth Disease",
        name_vn="Bệnh tay chân miệng",
        category="Pediatrics",
        definition="Bệnh tay chân miệng là bệnh truyền nhiễm do virus, phổ biến ở trẻ em Việt Nam, thường bùng phát thành dịch.",
        causes=[
            "Virus: Enterovirus (Coxsackie A16, Enterovirus 71)",
            "Lây qua đường tiêu hóa, tiếp xúc",
            "Yếu tố nguy cơ: trẻ nhỏ, môi trường đông đúc, vệ sinh kém"
        ],
        symptoms=[
            "Sốt",
            "Phát ban: mụn nước ở lòng bàn tay, bàn chân, miệng",
            "Loét miệng (gây đau, khó ăn)",
            "Mệt mỏi",
            "Chán ăn",
            "Có thể không có triệu chứng"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng điển hình",
                "Phát ban đặc trưng",
                "PCR virus (nếu cần xác định)",
                "Phân loại: nhẹ, có biến chứng thần kinh, có biến chứng tim mạch"
            ],
            "tests": [
                "Khám lâm sàng",
                "PCR virus (nếu cần)",
                "Công thức máu",
                "Theo dõi dấu hiệu biến chứng"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị hỗ trợ. Quan trọng: theo dõi sát dấu hiệu biến chứng thần kinh, tim mạch.",
            "medications": [
                "Hạ sốt: Paracetamol",
                "Giảm đau miệng: thuốc bôi, súc miệng",
                "Bù dịch (nếu sốt cao, không ăn được)",
                "Không dùng kháng sinh (trừ khi có nhiễm khuẩn kèm)"
            ],
            "procedures": [
                "Theo dõi sát: dấu hiệu thần kinh (giật mình, run chi), tim mạch",
                "Cách ly (tránh lây lan)",
                "Vệ sinh tay, đồ chơi"
            ]
        },
        prevention=[
            "Vệ sinh tay thường xuyên",
            "Vệ sinh đồ chơi, dụng cụ",
            "Cách ly trẻ bệnh",
            "Vệ sinh môi trường"
        ],
        complications=[
            "Viêm não",
            "Viêm màng não",
            "Viêm cơ tim",
            "Suy hô hấp",
            "Tử vong (nếu biến chứng nặng)"
        ],
        related_scores=["HFMD Severity"],
        related_drugs=["Paracetamol"],
        related_protocols=[],
        icd10_codes=["B08.4"]
    ),
    
    Disease(
        id="upper_respiratory_infection",
        name="Upper Respiratory Infection (URI)",
        name_vn="Nhiễm khuẩn hô hấp trên",
        category="Pediatrics",
        definition="Nhiễm khuẩn hô hấp trên là tình trạng nhiễm trùng cấp tính các cơ quan đường hô hấp trên (mũi, họng, xoang, thanh quản), rất phổ biến ở trẻ em.",
        causes=[
            "Virus (phổ biến nhất): Rhinovirus, Influenza, Parainfluenza, Adenovirus, RSV",
            "Vi khuẩn: Streptococcus pneumoniae, Haemophilus influenzae, Moraxella catarrhalis (thường gây bội nhiễm)",
            "Yếu tố nguy cơ: thay đổi thời tiết, môi trường ô nhiễm, tiếp xúc người bệnh"
        ],
        symptoms=[
            "Sốt (nhẹ hoặc cao)",
            "Ho",
            "Chảy mũi, nghẹt mũi",
            "Đau họng",
            "Hắt hơi",
            "Mệt mỏi, quấy khóc (trẻ nhỏ)",
            "Nôn trớ (do đờm)"
        ],
        diagnosis={
            "criteria": [
                "Chủ yếu dựa vào lâm sàng",
                "Loại trừ nhiễm khuẩn hô hấp dưới (viêm phổi)"
            ],
            "tests": [
                "Không cần xét nghiệm thường quy",
                "Công thức máu (nếu sốt cao kéo dài)",
                "Test cúm (nếu nghi ngờ)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị triệu chứng là chủ yếu. Hạn chế kháng sinh nếu do virus.",
            "medications": [
                "Hạ sốt: Paracetamol, Ibuprofen",
                "Vệ sinh mũi: Nước muối sinh lý",
                "Giảm ho: thuốc ho thảo dược (trẻ em)",
                "Kháng sinh: CHỈ DÙNG khi có bằng chứng nhiễm khuẩn hoặc nguy cơ cao (viêm tai giữa, viêm xoang cấp do vi khuẩn)"
            ],
            "procedures": [
                "Vệ sinh mũi họng sạch sẽ",
                "Giữ ấm",
                "Uống đủ nước"
            ]
        },
        prevention=[
            "Giữ ấm cơ thể",
            "Vệ sinh mũi họng",
            "Rửa tay thường xuyên",
            "Tránh tiếp xúc nguồn lây",
            "Tiêm chủng đầy đủ (Cúm, Phế cầu)"
        ],
        complications=[
            "Viêm tai giữa",
            "Viêm xoang",
            "Viêm phổi (bội nhiễm)",
            "Khởi phát cơn hen"
        ],
        related_scores=["Centor Criteria"],
        related_drugs=["Paracetamol", "Ibuprofen", "Sodium Chloride"],
        related_protocols=["URI Management"],
        icd10_codes=["J06.9", "J00", "J02.9"]
    ),

    Disease(
        id="bronchiolitis",
        name="Bronchiolitis",
        name_vn="Viêm tiểu phế quản",
        category="Pediatrics",
        definition="Viêm tiểu phế quản là bệnh viêm nhiễm cấp tính các tiểu phế quản, thường do virus, hay gặp ở trẻ < 2 tuổi, đặc biệt là trẻ nhũ nhi.",
        causes=[
            "Virus hợp bào hô hấp (RSV) - nguyên nhân hàng đầu",
            "Influenza virus, Adenovirus, Parainfluenza virus",
            "Yếu tố nguy cơ: trẻ < 6 tháng, sinh non, tim bẩm sinh, phổi mạn"
        ],
        symptoms=[
            "Khởi phát: ho, chảy mũi, sốt nhẹ",
            "Toàn phát: thở nhanh, khó thở, khò khè",
            "Rút lõm lồng ngực",
            "Tím tái (nếu nặng)",
            "Bú kém, bỏ bú"
        ],
        diagnosis={
            "criteria": [
                "Lâm sàng: trẻ < 2 tuổi, khò khè lần đầu, có triệu chứng viêm long hô hấp",
                "Loại trừ: hen phế quản, dị vật đường thở"
            ],
            "tests": [
                "Test nhanh RSV (nếu cần cách ly)",
                "SpO2 (đánh giá mức độ)",
                "Khí máu động mạch (nếu suy hô hấp nặng)"
            ],
            "imaging": [
                "X-quang phổi: ứ khí phế nang, xẹp phổi rải rác (không chỉ định thường quy nếu nhẹ)"
            ]
        },
        treatment={
            "general": "Điều trị hỗ trợ hô hấp và dinh dưỡng là quan trọng nhất.",
            "medications": [
                "Hạ sốt",
                "Khí dung nước muối ưu trương (có thể cân nhắc)",
                "KHÔNG khuyến cáo thường quy: Corticoid, thuốc giãn phế quản, kháng sinh (trừ khi bội nhiễm)",
                "Oxy (nếu SaO2 < 90-92%)"
            ],
            "procedures": [
                "Hút đờm dãi, thông thoáng đường thở",
                "Hỗ trợ hô hấp: Oxy, NCPAP (nếu suy hô hấp)",
                "Đảm bảo dinh dưỡng, nước điện giải (nuôi ăn tĩnh mạch nếu bú kém)"
            ]
        },
        prevention=[
            "Tránh tiếp xúc nguồn lây",
            "Rửa tay",
            "Nuôi con bằng sữa mẹ",
            "Tránh khói thuốc lá",
            "Palivizumab (dự phòng cho trẻ nguy cơ cao - đắt tiền)"
        ],
        complications=[
            "Suy hô hấp",
            "Ngừng thở (trẻ nhỏ)",
            "Bội nhiễm phổi",
            "Xẹp phổi"
        ],
        related_scores=["Bronchiolitis Severity Score"],
        related_drugs=["Paracetamol", "Hypertonic Saline"],
        related_protocols=["Bronchiolitis Management"],
        icd10_codes=["J21.9", "J21.0", "J21.8"]
    ),

    Disease(
        id="pneumonia_child",
        name="Community-Acquired Pneumonia in Children",
        name_vn="Viêm phổi cộng đồng ở trẻ em",
        category="Pediatrics",
        definition="Viêm phổi cộng đồng ở trẻ em là nhiễm trùng phổi do vi khuẩn, virus hoặc các tác nhân khác, là nguyên nhân tử vong hàng đầu ở trẻ em dưới 5 tuổi tại Việt Nam.",
        causes=[
            "Vi khuẩn: Streptococcus pneumoniae (phổ biến nhất), Haemophilus influenzae, Staphylococcus aureus",
            "Virus: RSV, Influenza, Adenovirus, Parainfluenza",
            "Mycoplasma pneumoniae (trẻ lớn)",
            "Chlamydia pneumoniae",
            "Yếu tố nguy cơ: suy dinh dưỡng, thiếu vắc xin, suy giảm miễn dịch, ô nhiễm không khí"
        ],
        symptoms=[
            "Sốt, ho",
            "Khó thở, thở nhanh (tachypnea)",
            "Rút lõm lồng ngực",
            "Thở rên (grunting)",
            "Tím tái (nếu nặng)",
            "Bỏ bú, bỏ ăn",
            "Mệt mỏi, li bì",
            "Đau ngực (trẻ lớn)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: sốt, ho, khó thở",
                "Thở nhanh theo tuổi: < 2 tháng: > 60 lần/phút, 2-12 tháng: > 50, 1-5 tuổi: > 40",
                "Rút lõm lồng ngực",
                "X-quang phổi: thâm nhiễm",
                "Phân loại: nhẹ, trung bình, nặng"
            ],
            "tests": [
                "X-quang phổi",
                "Công thức máu, CRP, Procalcitonin",
                "Cấy máu (nếu nặng)",
                "Test nhanh virus (nếu nghi ngờ)",
                "Khí máu (nếu suy hô hấp)"
            ],
            "imaging": [
                "X-quang phổi (chuẩn vàng)",
                "CT phổi (nếu không điển hình)"
            ]
        },
        treatment={
            "general": "Điều trị theo WHO/PIDS guidelines. Phân loại mức độ nặng để quyết định điều trị ngoại trú hay nhập viện. Kháng sinh nếu nghi ngờ vi khuẩn.",
            "medications": [
                "Kháng sinh: Amoxicillin (nhẹ), Amoxicillin-Clavulanate hoặc Ceftriaxone (trung bình-nặng)",
                "Macrolide: Azithromycin (nếu nghi ngờ Mycoplasma)",
                "Vancomycin (nếu nghi ngờ MRSA)",
                "Hạ sốt: Paracetamol",
                "Oxygen (nếu SpO2 < 92%)",
                "Điều trị hỗ trợ: bù dịch, dinh dưỡng"
            ],
            "procedures": [
                "Điều trị ngoại trú (nếu nhẹ, không có dấu hiệu nguy hiểm)",
                "Nhập viện (nếu nặng, suy hô hấp, bỏ ăn)",
                "ICU (nếu suy hô hấp nặng)",
                "Theo dõi sát: nhịp thở, SpO2, tình trạng tổng thể"
            ]
        },
        prevention=[
            "Tiêm vắc xin: PCV (Pneumococcal), Hib, Influenza",
            "Nuôi con bằng sữa mẹ",
            "Dinh dưỡng đầy đủ",
            "Vệ sinh môi trường",
            "Tránh tiếp xúc với người bệnh"
        ],
        complications=[
            "Tràn dịch màng phổi",
            "Áp xe phổi",
            "Suy hô hấp",
            "Nhiễm trùng huyết",
            "Tử vong (nếu không điều trị)"
        ],
        related_scores=["IMCI Pneumonia Classification", "WHO Pneumonia Severity"],
        related_drugs=["Amoxicillin", "Amoxicillin-Clavulanate", "Ceftriaxone", "Azithromycin"],
        related_protocols=["Pediatric Pneumonia Management"],
        icd10_codes=["J18.9", "J15.9", "J12.9"]
    ),

    Disease(
        id="diarrhea_child",
        name="Acute Diarrhea in Children",
        name_vn="Tiêu chảy cấp ở trẻ em",
        category="Pediatrics",
        definition="Tiêu chảy cấp ở trẻ em là đi ngoài phân lỏng ≥ 3 lần/ngày, kéo dài < 14 ngày, là nguyên nhân tử vong hàng đầu ở trẻ em dưới 5 tuổi do mất nước.",
        causes=[
            "Virus: Rotavirus (phổ biến nhất), Norovirus, Adenovirus",
            "Vi khuẩn: E. coli, Shigella, Salmonella, Campylobacter, Vibrio cholerae",
            "Ký sinh trùng: Giardia, Cryptosporidium",
            "Yếu tố nguy cơ: vệ sinh kém, nước uống không an toàn, suy dinh dưỡng, thiếu vắc xin"
        ],
        symptoms=[
            "Đi ngoài phân lỏng, nhiều lần",
            "Nôn",
            "Sốt",
            "Đau bụng",
            "Mất nước: khát, khô miệng, giảm tiểu, mắt trũng, da nhăn",
            "Mất nước nặng: li bì, không uống được, sốc"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: đi ngoài phân lỏng ≥ 3 lần/ngày",
                "Đánh giá mất nước: nhẹ, trung bình, nặng",
                "Phân loại theo WHO: không mất nước, mất nước, sốc"
            ],
            "tests": [
                "Đánh giá lâm sàng mất nước",
                "Soi phân (nếu nghi ngờ ký sinh trùng)",
                "Cấy phân (nếu nghi ngờ vi khuẩn, nặng)",
                "Điện giải (nếu mất nước nặng)",
                "Test nhanh Rotavirus (nếu có)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị theo WHO guidelines. Nguyên tắc: bù nước và điện giải (ORS), tiếp tục cho ăn, kháng sinh chỉ khi cần.",
            "medications": [
                "ORS (Oral Rehydration Solution): bù nước đường uống",
                "Zinc: giảm thời gian và mức độ tiêu chảy",
                "Kháng sinh: chỉ khi có chỉ định (Shigella, Cholera, Giardia)",
                "Probiotic: có thể hỗ trợ",
                "Truyền dịch tĩnh mạch (nếu mất nước nặng, không uống được)"
            ],
            "procedures": [
                "Điều trị ngoại trú (nếu không mất nước hoặc mất nước nhẹ)",
                "Nhập viện (nếu mất nước trung bình-nặng, sốc)",
                "Truyền dịch tĩnh mạch: Ringer Lactate hoặc Normal Saline",
                "Theo dõi: lượng nước vào-ra, cân nặng, dấu hiệu mất nước"
            ]
        },
        prevention=[
            "Tiêm vắc xin Rotavirus",
            "Nuôi con bằng sữa mẹ",
            "Vệ sinh: rửa tay, nước sạch",
            "Vệ sinh thực phẩm",
            "Cải thiện dinh dưỡng"
        ],
        complications=[
            "Mất nước nặng",
            "Sốc",
            "Rối loạn điện giải",
            "Suy dinh dưỡng",
            "Tử vong (nếu không điều trị)"
        ],
        related_scores=["WHO Dehydration Assessment", "IMCI Diarrhea Classification"],
        related_drugs=["ORS", "Zinc", "Metronidazole", "Azithromycin"],
        related_protocols=["Pediatric Diarrhea Management"],
        icd10_codes=["A09", "K59.1", "A00.9"]
    ),

    Disease(
        id="measles",
        name="Measles",
        name_vn="Sởi",
        category="Pediatrics",
        definition="Sởi là bệnh truyền nhiễm cấp tính do virus Measles, đặc trưng bởi sốt, phát ban, viêm kết mạc, có thể gây biến chứng nặng và tử vong ở trẻ em.",
        causes=[
            "Virus Measles (Morbillivirus)",
            "Lây qua đường hô hấp: giọt bắn, không khí",
            "Rất dễ lây (R0 ≈ 12-18)",
            "Yếu tố nguy cơ: chưa tiêm vắc xin, suy dinh dưỡng, suy giảm miễn dịch"
        ],
        symptoms=[
            "Giai đoạn ủ bệnh: 10-14 ngày",
            "Giai đoạn tiền triệu: sốt cao, ho, sổ mũi, viêm kết mạc, đốm Koplik (trong miệng)",
            "Phát ban: bắt đầu sau tai, lan xuống mặt, thân, tay chân",
            "Ban dát sẩn, hợp lại thành mảng",
            "Ban kéo dài 5-7 ngày, bong vảy",
            "Sốt cao, mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: sốt, phát ban, viêm kết mạc, ho",
                "Đốm Koplik (đặc hiệu)",
                "Tiền sử tiếp xúc",
                "Xét nghiệm: IgM, PCR"
            ],
            "tests": [
                "IgM Measles (dương tính sau 3 ngày phát ban)",
                "PCR Measles",
                "IgG (tăng 4 lần trong huyết thanh đôi)",
                "Công thức máu: giảm bạch cầu"
            ],
            "imaging": [
                "X-quang phổi (nếu có biến chứng viêm phổi)"
            ]
        },
        treatment={
            "general": "Điều trị hỗ trợ. Không có thuốc kháng virus đặc hiệu. Phòng ngừa bằng vắc xin. Điều trị biến chứng.",
            "medications": [
                "Vitamin A: giảm tử vong và biến chứng (200,000 IU cho trẻ ≥ 12 tháng, 100,000 IU cho trẻ 6-12 tháng)",
                "Hạ sốt: Paracetamol",
                "Kháng sinh (nếu có bội nhiễm vi khuẩn)",
                "Ribavirin (nếu suy giảm miễn dịch, nặng)",
                "Điều trị biến chứng"
            ],
        "procedures": [
                "Cách ly (quan trọng)",
                "Nghỉ ngơi",
                "Bù dịch",
                "Điều trị biến chứng: viêm phổi, viêm não, viêm tai giữa"
            ]
        },
        prevention=[
            "Tiêm vắc xin MMR (Measles-Mumps-Rubella): 2 liều",
            "Tiêm vắc xin cho trẻ 9-12 tháng",
            "Tiêm nhắc lại lúc 18 tháng",
            "Tiêm vắc xin cho người tiếp xúc (trong 72h)",
            "Cách ly người bệnh"
        ],
        complications=[
            "Viêm phổi (nguy hiểm nhất)",
            "Viêm não (1/1000)",
            "Viêm tai giữa",
            "Tiêu chảy",
            "Suy dinh dưỡng",
            "Tử vong (1-3/1000 ở trẻ em khỏe mạnh)"
        ],
        related_scores=["Measles Severity"],
        related_drugs=["Vitamin A", "Paracetamol", "Ribavirin"],
        related_protocols=["Measles Management"],
        icd10_codes=["B05.9", "B05.0", "B05.1", "B05.2"]
    ),
]
