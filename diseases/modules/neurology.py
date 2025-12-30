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
            "Kiểm soát huyết áp",
            "Kiểm soát đái tháo đường",
            "Chống đông (nếu rung nhĩ)",
            "Statin",
            "Bỏ thuốc lá"
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
]
