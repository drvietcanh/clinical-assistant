"""
Neurology Module
Diseases: Stroke, Epilepsy
"""

from typing import List
from diseases.data import Disease


NEUROLOGY_DISEASES: List[Disease] = [
    Disease(
        id="stroke",
        name="Acute Ischemic Stroke",
        name_vn="Đột quỵ thiếu máu cục bộ cấp",
        category="Neurology",
        definition="Đột quỵ thiếu máu cục bộ là tình trạng giảm tưới máu não do tắc nghẽn mạch máu não.",
        causes=[
            "Huyết khối tại chỗ",
            "Thuyên tắc từ tim (rung nhĩ, bệnh van tim)",
            "Thuyên tắc từ động mạch lớn",
            "Yếu tố nguy cơ: tăng huyết áp, đái tháo đường, rung nhĩ, hút thuốc"
        ],
        symptoms=[
            "Yếu hoặc liệt một bên (FAST: Face, Arm, Speech, Time)",
            "Nói khó hoặc không nói được",
            "Nhìn mờ hoặc mù một mắt",
            "Chóng mặt, mất thăng bằng",
            "Đau đầu dữ dội",
            "Lú lẫn"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng đột ngột",
                "CT não: loại trừ xuất huyết",
                "MRI não: vùng nhồi máu",
                "Siêu âm mạch máu cổ"
            ],
            "tests": [
                "CT não (khẩn cấp)",
                "MRI não (nếu có)",
                "Công thức máu, đông máu",
                "Chức năng thận, đường huyết"
            ],
            "imaging": [
                "CT não (không tiêm thuốc cản quang)",
                "MRI não + DWI",
                "CTA (CT Angiography)",
                "Siêu âm mạch máu cổ"
            ]
        },
        treatment={
            "general": "Điều trị khẩn cấp: tái tưới máu sớm (tPA trong 4.5h, thrombectomy trong 6-24h), phòng ngừa biến chứng.",
            "medications": [
                "tPA (Alteplase) - nếu trong 4.5h, không chống chỉ định",
                "Aspirin 325mg (sau 24h nếu dùng tPA)",
                "Clopidogrel (nếu TIA hoặc stroke nhẹ)",
                "Statin (Atorvastatin 80mg)",
                "Kiểm soát huyết áp (tránh hạ quá nhanh)"
            ],
            "procedures": [
                "Thrombectomy (lấy huyết khối cơ học) - nếu trong 6-24h",
                "Đặt stent mạch cảnh (nếu hẹp nặng)"
            ]
        },
        prevention=[
            "Kiểm soát huyết áp: mục tiêu <130/80 mmHg theo AHA/ASA 2024-2025",
            "Kiểm soát đái tháo đường: HbA1c <7%, xem xét GLP-1 agonists cho phòng ngừa đột quỵ ở người có rủi ro chuyển hóa cao",
            "Chống đông (nếu rung nhĩ): DOAC hoặc Warfarin theo CHA2DS2-VASc score",
            "Statin: PCSK9 inhibitors để hạ LDL-C nếu cần",
            "Chế độ ăn Địa Trung Hải: dầu olive, hạt có dầu, hạn chế carbs tinh chế",
            "Hoạt động thể lực ≥150 phút/tuần",
            "Ngủ đủ và chất lượng tốt",
            "Bỏ thuốc lá",
            "Đánh giá các yếu tố phi-y tế: tình trạng kinh tế xã hội, bất bình đẳng, tác động giới",
            "Colchicine trong một số trường hợp phòng ngừa (đang nghiên cứu)"
        ],
        complications=[
            "Tái phát đột quỵ",
            "Xuất huyết não (nếu dùng tPA)",
            "Co giật",
            "Viêm phổi hít",
            "Tử vong"
        ],
        related_scores=["NIHSS", "mRS", "ASPECTS"],
        related_drugs=["Alteplase", "Aspirin", "Clopidogrel", "Atorvastatin"],
        related_protocols=["Stroke Management"],
        icd10_codes=["I63.9", "I64"]
    ),
    
    Disease(
        id="epilepsy",
        name="Epilepsy",
        name_vn="Động kinh",
        category="Neurology",
        definition="Động kinh là rối loạn thần kinh đặc trưng bởi các cơn co giật tái phát do hoạt động điện bất thường của não.",
        causes=[
            "Vô căn (không rõ nguyên nhân)",
            "Sau chấn thương đầu",
            "Sau đột quỵ",
            "U não",
            "Nhiễm trùng não (viêm màng não, viêm não)",
            "Bệnh di truyền",
            "Rối loạn chuyển hóa"
        ],
        symptoms=[
            "Cơn co giật: co cứng, co giật toàn thân hoặc cục bộ",
            "Mất ý thức",
            "Nhìn chằm chằm (absence seizure)",
            "Rối loạn hành vi",
            "Sau cơn: mệt mỏi, lú lẫn"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: cơn co giật tái phát",
                "EEG: sóng bất thường",
                "MRI não: tìm nguyên nhân",
                "Phân loại: focal, generalized, unknown"
            ],
            "tests": [
                "EEG (Electroencephalography)",
                "MRI não",
                "CT não (nếu không có MRI)",
                "Công thức máu, điện giải",
                "Đường huyết"
            ],
            "imaging": [
                "MRI não",
                "CT não",
                "EEG"
            ]
        },
        treatment={
            "general": "Điều trị theo ILAE guidelines. Mục tiêu: kiểm soát cơn co giật, giảm tác dụng phụ, cải thiện chất lượng cuộc sống.",
            "medications": [
                "Antiepileptic drugs (AED): Carbamazepine, Valproate, Lamotrigine, Levetiracetam, Topiramate",
                "Bắt đầu một thuốc, tăng dần liều",
                "Kết hợp 2-3 thuốc nếu cần",
                "Dùng đều đặn, không tự ý ngừng"
            ],
            "procedures": [
                "Phẫu thuật (nếu kháng thuốc, có tổn thương rõ)",
                "Kích thích dây thần kinh phế vị (VNS)",
                "Theo dõi nồng độ thuốc trong máu"
            ]
        },
        prevention=[
            "Điều trị nguyên nhân",
            "Tránh yếu tố kích thích (thiếu ngủ, rượu bia, stress)",
            "Dùng thuốc đều đặn",
            "Đeo vòng cảnh báo y tế"
        ],
        complications=[
            "Status epilepticus (cơn co giật kéo dài)",
            "Chấn thương do ngã",
            "SUDEP (Sudden Unexpected Death in Epilepsy)",
            "Tác dụng phụ thuốc",
            "Suy giảm nhận thức"
        ],
        related_scores=["EEG", "Seizure Frequency"],
        related_drugs=["Carbamazepine", "Valproate", "Lamotrigine", "Levetiracetam", "Topiramate"],
        related_protocols=[],
        icd10_codes=["G40.9", "G40.1", "G40.2", "G40.3"]
    ),
    
    Disease(
        id="migraine",
        name="Migraine",
        name_vn="Đau nửa đầu (Migraine)",
        category="Neurology",
        definition="Migraine là bệnh đau đầu nguyên phát, đặc trưng bởi cơn đau đầu một bên, kèm buồn nôn, nhạy cảm ánh sáng/tiếng động, rất phổ biến.",
        causes=[
            "Nguyên nhân chưa rõ",
            "Yếu tố di truyền",
            "Yếu tố kích thích: stress, thức ăn (rượu, phô mai, chocolate), thay đổi hormone, thiếu ngủ, thay đổi thời tiết",
            "Nữ giới (tỷ lệ cao hơn nam)",
            "Tuổi trung niên"
        ],
        symptoms=[
            "Đau đầu một bên (có thể hai bên), đau nhói, đau vừa đến nặng",
            "Buồn nôn, nôn",
            "Nhạy cảm ánh sáng (photophobia)",
            "Nhạy cảm tiếng động (phonophobia)",
            "Aura (30%): rối loạn thị giác, cảm giác, vận động (trước cơn đau)",
            "Tăng khi vận động",
            "Kéo dài 4-72 giờ"
        ],
        diagnosis={
            "criteria": [
                "ICHD-3 criteria: ≥ 5 cơn đau đầu với đặc điểm migraine",
                "Đau đầu kéo dài 4-72 giờ",
                "Có ≥ 2: một bên, nhói, vừa-nặng, tăng khi vận động",
                "Có ≥ 1: buồn nôn/vom, nhạy cảm ánh sáng/tiếng động"
            ],
            "tests": [
                "Đánh giá lâm sàng",
                "Loại trừ: CT/MRI não (nếu có triệu chứng báo động)",
                "Xét nghiệm: loại trừ nguyên nhân thứ phát"
            ],
            "imaging": [
                "CT/MRI não (nếu có triệu chứng báo động hoặc lần đầu)"
            ]
        },
        treatment={
            "general": "Điều trị theo AHS guidelines. Mục tiêu: cắt cơn, phòng ngừa, cải thiện chất lượng cuộc sống.",
            "medications": [
                "Cắt cơn: Triptan (Sumatriptan, Rizatriptan), NSAID (Ibuprofen, Naproxen), Paracetamol",
                "Phòng ngừa: Beta-blocker (Propranolol), Topiramate, Amitriptyline, CGRP antagonist",
                "Chống nôn: Metoclopramide, Ondansetron"
            ],
            "procedures": [
                "Nghỉ ngơi trong phòng tối, yên tĩnh",
                "Tránh yếu tố kích thích",
                "Theo dõi nhật ký đau đầu"
            ]
        },
        prevention=[
            "Tránh yếu tố kích thích",
            "Ngủ đủ giấc",
            "Quản lý stress",
            "Tập thể dục",
            "Chế độ ăn đều đặn"
        ],
        complications=[
            "Migraine mạn tính (≥ 15 ngày/tháng)",
            "Ảnh hưởng công việc, cuộc sống",
            "Lạm dụng thuốc",
            "Trầm cảm, lo âu"
        ],
        related_scores=["MIDAS", "HIT-6"],
        related_drugs=["Sumatriptan", "Rizatriptan", "Ibuprofen", "Propranolol", "Topiramate"],
        related_protocols=["Migraine Management"],
        icd10_codes=["G43.9", "G43.0", "G43.1"]
    ),
    
    Disease(
        id="parkinson_disease",
        name="Parkinson's Disease",
        name_vn="Bệnh Parkinson",
        category="Neurology",
        definition="Bệnh Parkinson là rối loạn thoái hóa thần kinh, đặc trưng bởi run, cứng cơ, chậm vận động, mất thăng bằng, phổ biến ở người cao tuổi.",
        causes=[
            "Thoái hóa tế bào thần kinh sản xuất dopamine (substantia nigra)",
            "Nguyên nhân chưa rõ",
            "Yếu tố di truyền (một số trường hợp)",
            "Yếu tố môi trường: thuốc trừ sâu, kim loại nặng",
            "Tuổi cao"
        ],
        symptoms=[
            "Run (tremor): khi nghỉ, giảm khi vận động",
            "Cứng cơ (rigidity)",
            "Chậm vận động (bradykinesia)",
            "Mất thăng bằng (postural instability)",
            "Dáng đi: bước nhỏ, không vung tay",
            "Giảm biểu cảm mặt",
            "Rối loạn giọng nói",
            "Rối loạn nuốt"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: ≥ 2 trong 4: run, cứng cơ, chậm vận động, mất thăng bằng",
                "Đáp ứng với Levodopa",
                "Loại trừ: Parkinson do thuốc, bệnh khác"
            ],
            "tests": [
                "Đánh giá lâm sàng",
                "Test Levodopa",
                "DaTscan (nếu cần)",
                "MRI não (loại trừ bệnh khác)"
            ],
            "imaging": [
                "MRI não",
                "DaTscan (nếu có)"
            ]
        },
        treatment={
            "general": "Điều trị triệu chứng. Mục tiêu: cải thiện vận động, giảm triệu chứng, duy trì chức năng.",
            "medications": [
                "Levodopa/Carbidopa (thuốc đầu tay)",
                "Dopamine agonist: Pramipexole, Ropinirole",
                "MAO-B inhibitor: Selegiline, Rasagiline",
                "COMT inhibitor: Entacapone (kết hợp với Levodopa)",
                "Anticholinergic: Trihexyphenidyl (nếu run nhiều)"
            ],
            "procedures": [
                "Vật lý trị liệu",
                "Ngôn ngữ trị liệu",
                "Kích thích não sâu (DBS) - nếu kháng thuốc",
                "Theo dõi định kỳ"
            ]
        },
        prevention=[
            "Không có cách phòng ngừa",
            "Tránh tiếp xúc thuốc trừ sâu",
            "Tập thể dục",
            "Điều trị sớm"
        ],
        complications=[
            "Tàn tật",
            "Suy giảm nhận thức",
            "Trầm cảm",
            "Rối loạn nuốt, viêm phổi hít",
            "Tử vong"
        ],
        related_scores=["UPDRS", "Hoehn & Yahr Scale"],
        related_drugs=["Levodopa", "Carbidopa", "Pramipexole", "Ropinirole", "Selegiline"],
        related_protocols=["Parkinson's Disease Management"],
        icd10_codes=["G20"]
    ),

    Disease(
        id="bacterial_meningitis",
        name="Bacterial Meningitis",
        name_vn="Viêm màng não mủ",
        category="Neurology",
        definition="Viêm màng não mủ là nhiễm trùng màng não do vi khuẩn, là cấp cứu thần kinh, có thể gây tử vong hoặc di chứng nặng nếu không điều trị kịp thời.",
        causes=[
            "Vi khuẩn: Streptococcus pneumoniae (phổ biến nhất), Neisseria meningitidis, Haemophilus influenzae type b, Listeria monocytogenes",
            "Theo tuổi: trẻ sơ sinh (Group B Streptococcus, E. coli), trẻ em (S. pneumoniae, N. meningitidis), người lớn (S. pneumoniae, N. meningitidis)",
            "Yếu tố nguy cơ: suy giảm miễn dịch, chấn thương đầu, nhiễm trùng gần (viêm xoang, viêm tai)",
            "Lây qua đường hô hấp (N. meningitidis)"
        ],
        symptoms=[
            "Sốt cao",
            "Đau đầu dữ dội",
            "Cổ cứng (nuchal rigidity)",
            "Sợ ánh sáng (photophobia)",
            "Buồn nôn, nôn",
            "Lú lẫn, rối loạn ý thức",
            "Co giật",
            "Phát ban (nếu N. meningitidis)",
            "Trẻ em: sốt, bỏ ăn, li bì, thóp phồng"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: sốt, đau đầu, cổ cứng",
                "Dịch não tủy: tăng bạch cầu, tăng protein, giảm glucose",
                "Nhuộm Gram, cấy dịch não tủy",
                "Phân biệt với viêm màng não virus"
            ],
            "tests": [
                "Chọc dò tủy sống (LP) - khẩn cấp",
                "Dịch não tủy: tế bào, protein, glucose, cấy",
                "Nhuộm Gram",
                "PCR (nếu có)",
                "Cấy máu",
                "CT não (trước LP nếu có dấu hiệu tăng áp lực nội sọ)"
            ],
            "imaging": [
                "CT não (trước LP nếu nghi ngờ tăng áp lực nội sọ)",
                "MRI não (nếu có biến chứng)"
            ]
        },
        treatment={
            "general": "Điều trị khẩn cấp. Kháng sinh đường tĩnh mạch ngay, không chờ kết quả cấy. Điều trị hỗ trợ.",
            "medications": [
                "Kháng sinh đường tĩnh mạch ngay (trước LP nếu cần):",
                "- Trẻ sơ sinh: Ampicillin + Cefotaxime",
                "- Trẻ em: Ceftriaxone hoặc Cefotaxime",
                "- Người lớn: Ceftriaxone + Vancomycin (nếu nghi ngờ kháng Penicillin)",
                "- Nếu nghi Listeria: Ampicillin",
                "Dexamethasone (trước hoặc cùng với kháng sinh đầu tiên) - giảm di chứng",
                "Điều trị hỗ trợ: hạ sốt, chống co giật, kiểm soát áp lực nội sọ"
            ],
            "procedures": [
                "Chọc dò tủy sống",
                "ICU (nếu nặng)",
                "Theo dõi áp lực nội sọ",
                "Điều trị biến chứng"
            ]
        },
        prevention=[
            "Tiêm vắc xin: PCV (Pneumococcal), MenACWY (Meningococcal), Hib",
            "Dự phòng kháng sinh cho người tiếp xúc (N. meningitidis): Rifampin, Ciprofloxacin",
            "Điều trị nhiễm trùng gần (viêm xoang, viêm tai)"
        ],
        complications=[
            "Tử vong (10-30% nếu không điều trị)",
            "Di chứng thần kinh: điếc, mù, liệt, động kinh",
            "Suy giảm nhận thức",
            "Áp xe não",
            "Viêm màng não mạn tính"
        ],
        related_scores=["Glasgow Coma Scale", "Meningitis Severity"],
        related_drugs=["Ceftriaxone", "Cefotaxime", "Vancomycin", "Ampicillin", "Dexamethasone"],
        related_protocols=["Bacterial Meningitis Management"],
        icd10_codes=["G00.9", "G00.0", "G00.1", "G00.2"]
    ),

    Disease(
        id="viral_meningitis",
        name="Viral Meningitis",
        name_vn="Viêm màng não virus",
        category="Neurology",
        definition="Viêm màng não virus là nhiễm trùng màng não do virus, thường nhẹ hơn viêm màng não mủ, tự khỏi trong vài tuần.",
        causes=[
            "Virus: Enterovirus (phổ biến nhất), HSV-2, VZV, Mumps, Arbovirus",
            "Lây qua đường hô hấp, phân-miệng",
            "Yếu tố nguy cơ: mùa hè-thu (Enterovirus), suy giảm miễn dịch"
        ],
        symptoms=[
            "Sốt",
            "Đau đầu",
            "Cổ cứng (nhẹ hơn viêm màng não mủ)",
            "Sợ ánh sáng",
            "Buồn nôn, nôn",
            "Mệt mỏi",
            "Phát ban (nếu Enterovirus)",
            "Thường không có rối loạn ý thức nặng"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: sốt, đau đầu, cổ cứng",
                "Dịch não tủy: tăng bạch cầu lympho, protein bình thường hoặc tăng nhẹ, glucose bình thường",
                "PCR virus",
                "Phân biệt với viêm màng não mủ"
            ],
            "tests": [
                "Chọc dò tủy sống",
                "Dịch não tủy: tế bào (lympho), protein, glucose",
                "PCR Enterovirus, HSV, VZV",
                "Cấy virus",
                "Công thức máu"
            ],
            "imaging": [
                "CT/MRI não (nếu không điển hình)"
            ]
        },
        treatment={
            "general": "Điều trị hỗ trợ. Hầu hết tự khỏi. Kháng virus nếu HSV hoặc VZV.",
            "medications": [
                "Acyclovir (nếu HSV hoặc VZV)",
                "Hạ sốt: Paracetamol",
                "Giảm đau",
                "Điều trị hỗ trợ"
            ],
            "procedures": [
                "Nghỉ ngơi",
                "Bù dịch",
                "Theo dõi (hầu hết tự khỏi)"
            ]
        },
        prevention=[
            "Vệ sinh: rửa tay",
            "Tiêm vắc xin: MMR (Mumps), Varicella (VZV)",
            "Tránh tiếp xúc với người bệnh"
        ],
        complications=[
            "Thường tự khỏi không di chứng",
            "Di chứng (hiếm): điếc, động kinh",
            "Viêm não (nếu HSV)"
        ],
        related_scores=[],
        related_drugs=["Acyclovir", "Paracetamol"],
        related_protocols=["Viral Meningitis Management"],
        icd10_codes=["A87.9", "A87.0", "A87.1"]
    ),

    Disease(
        id="bells_palsy",
        name="Bell's Palsy",
        name_vn="Liệt mặt ngoại biên (Bell's Palsy)",
        category="Neurology",
        definition="Liệt mặt ngoại biên (Bell's Palsy) là liệt dây thần kinh mặt (CN VII) một bên, thường tự khỏi, nguyên nhân có thể do virus HSV-1.",
        causes=[
            "Nguyên nhân chưa rõ",
            "Có thể do virus HSV-1 tái hoạt",
            "Yếu tố nguy cơ: nhiễm trùng đường hô hấp trên, thai kỳ, đái tháo đường",
            "Viêm, phù dây thần kinh mặt trong ống xương thái dương"
        ],
        symptoms=[
            "Liệt mặt một bên đột ngột (trong vài giờ đến vài ngày)",
            "Không nhắm được mắt",
            "Không nhăn trán được",
            "Miệng méo, chảy nước dãi",
            "Mất vị giác (2/3 trước lưỡi)",
            "Nhạy cảm tiếng động (hyperacusis)",
            "Đau sau tai (có thể)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: liệt mặt một bên đột ngột",
                "Loại trừ: đột quỵ, u não, bệnh Lyme, viêm tai giữa",
                "Không có triệu chứng thần kinh khác"
            ],
            "tests": [
                "Đánh giá lâm sàng",
                "MRI não (nếu không điển hình, nghi ngờ đột quỵ hoặc u)",
                "EMG (nếu cần đánh giá mức độ tổn thương)",
                "Test HSV (nếu có)"
            ],
            "imaging": [
                "MRI não (nếu không điển hình)"
            ]
        },
        treatment={
            "general": "Điều trị sớm bằng Corticosteroid. Kháng virus nếu nghi ngờ HSV. Bảo vệ mắt.",
            "medications": [
                "Prednisone 60-80mg/ngày x 7 ngày, giảm dần (thuốc đầu tay)",
                "Acyclovir hoặc Valacyclovir (nếu nghi ngờ HSV)",
                "Nhỏ mắt, băng mắt (bảo vệ giác mạc)"
            ],
            "procedures": [
                "Vật lý trị liệu: massage mặt, tập vận động",
                "Bảo vệ mắt: nhỏ mắt, đeo kính, băng mắt khi ngủ",
                "Theo dõi định kỳ"
            ]
        },
        prevention=[
            "Không có cách phòng ngừa",
            "Điều trị sớm"
        ],
        complications=[
            "Di chứng: liệt mặt không hồi phục hoàn toàn",
            "Co thắt cơ mặt (synkinesis)",
            "Khô mắt, loét giác mạc",
            "Ảnh hưởng thẩm mỹ, tâm lý"
        ],
        related_scores=["House-Brackmann Scale", "Facial Nerve Function"],
        related_drugs=["Prednisone", "Acyclovir", "Valacyclovir"],
        related_protocols=["Bell's Palsy Management"],
        icd10_codes=["G51.0"]
    ),
]
