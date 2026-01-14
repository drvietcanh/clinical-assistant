"""
Rheumatology Module
Diseases: Gout
"""

from typing import List
from diseases.data import Disease


RHEUMATOLOGY_DISEASES: List[Disease] = [
    Disease(
        id="gout",
        name="Gout",
        name_vn="Bệnh gút",
        category="Rheumatology",
        definition="Gout là bệnh viêm khớp do lắng đọng tinh thể urate trong khớp, gây đau dữ dội, phổ biến tại Việt Nam do thay đổi lối sống.",
        causes=[
            "Tăng acid uric máu (hyperuricemia)",
            "Nguyên nhân: béo phì, rượu bia, thực phẩm giàu purine (thịt đỏ, hải sản, nội tạng)",
            "Giảm thải acid uric qua thận",
            "Tăng sản xuất acid uric",
            "Yếu tố di truyền",
            "Một số thuốc: lợi tiểu, aspirin liều thấp"
        ],
        symptoms=[
            "Cơn cấp: đau dữ dội, sưng, nóng, đỏ khớp (thường khớp ngón chân cái)",
            "Đau thường về đêm, đau dữ dội",
            "Sốt nhẹ",
            "Gout mạn: hạt tophi, tổn thương khớp mạn tính"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng điển hình",
                "Acid uric máu tăng (> 7 mg/dL nam, > 6 mg/dL nữ)",
                "Hút dịch khớp: tinh thể urate dưới kính hiển vi",
                "Đáp ứng với Colchicine"
            ],
            "tests": [
                "Acid uric máu",
                "Hút dịch khớp (nếu có tràn dịch) - tìm tinh thể urate",
                "Chức năng thận",
                "X-quang khớp (nếu gout mạn)"
            ],
            "imaging": [
                "X-quang khớp (hạt tophi, tổn thương xương)",
                "Siêu âm khớp (tinh thể urate)",
                "Dual-energy CT (nếu cần)"
            ]
        },
        treatment={
            "general": "Điều trị cơn cấp: NSAID, Colchicine, hoặc Corticosteroid. Điều trị dự phòng: Allopurinol hoặc Febuxostat.",
            "medications": [
                "Cơn cấp: NSAID (Ibuprofen, Naproxen, Indomethacin) hoặc Colchicine hoặc Prednisone",
                "Dự phòng: Allopurinol (ức chế xanthine oxidase) hoặc Febuxostat",
                "Probenecid (tăng thải acid uric) - nếu không dung nạp Allopurinol",
                "Pegloticase (nếu kháng trị)"
            ],
            "procedures": [
                "Hút dịch khớp (nếu tràn dịch nhiều)",
                "Phẫu thuật cắt hạt tophi (nếu lớn, ảnh hưởng chức năng)"
            ]
        },
        prevention=[
            "Giảm cân (nếu thừa cân)",
            "Hạn chế rượu bia",
            "Hạn chế thực phẩm giàu purine (thịt đỏ, hải sản, nội tạng)",
            "Uống nhiều nước",
            "Dùng thuốc hạ acid uric (nếu có chỉ định)"
        ],
        complications=[
            "Gout mạn, tổn thương khớp",
            "Hạt tophi",
            "Sỏi thận (do acid uric)",
            "Bệnh thận do gout",
            "Nhiễm trùng khớp (nếu hạt tophi vỡ)"
        ],
        related_scores=["Serum Uric Acid"],
        related_drugs=["Allopurinol", "Febuxostat", "Colchicine", "Ibuprofen", "Prednisone"],
        related_protocols=[],
        icd10_codes=["M10.9", "M10.0", "M10.1"]
    ),

    Disease(
        id="systemic_lupus_erythematosus",
        name="Systemic Lupus Erythematosus",
        name_vn="Lupus ban đỏ hệ thống (SLE)",
        category="Rheumatology",
        definition="Lupus ban đỏ hệ thống (SLE) là bệnh tự miễn mạn tính, đặc trưng bởi viêm đa cơ quan do tự kháng thể, phổ biến ở phụ nữ trẻ.",
        causes=[
            "Tự miễn: hệ miễn dịch tấn công các cơ quan của chính cơ thể",
            "Yếu tố di truyền",
            "Yếu tố môi trường: ánh nắng mặt trời, nhiễm trùng, thuốc",
            "Hormone: estrogen (nữ giới chiếm 90%)",
            "Yếu tố nguy cơ: nữ, tuổi 15-45, người châu Á, châu Phi"
        ],
        symptoms=[
            "Phát ban hình cánh bướm ở mặt",
            "Đau khớp, viêm khớp",
            "Mệt mỏi, sốt",
            "Nhạy cảm ánh sáng",
            "Rụng tóc",
            "Loét miệng",
            "Viêm màng phổi, màng tim",
            "Bệnh thận (protein niệu, suy thận)",
            "Bệnh thần kinh (co giật, rối loạn tâm thần)"
        ],
        diagnosis={
            "criteria": [
                "SLICC hoặc ACR/EULAR 2019 criteria: ≥ 4 tiêu chuẩn",
                "Kháng thể kháng nhân (ANA) dương tính",
                "Kháng thể đặc hiệu: anti-dsDNA, anti-Sm, anti-phospholipid",
                "Bổ thể giảm (C3, C4)",
                "Tổn thương đa cơ quan"
            ],
            "tests": [
                "ANA (gần như 100% dương tính)",
                "Anti-dsDNA, Anti-Sm (đặc hiệu)",
                "Anti-phospholipid antibodies",
                "Bổ thể (C3, C4)",
                "Công thức máu (giảm bạch cầu, tiểu cầu)",
                "Chức năng thận, protein niệu",
                "Sinh thiết thận (nếu có bệnh thận)"
            ],
            "imaging": [
                "X-quang khớp",
                "Siêu âm thận",
                "CT/MRI (nếu có tổn thương thần kinh)"
            ]
        },
        treatment={
            "general": "Điều trị theo EULAR/ACR guidelines. Mục tiêu: kiểm soát triệu chứng, ngăn tổn thương cơ quan, giảm tử vong.",
            "medications": [
                "Hydroxychloroquine (thuốc nền, dùng suốt đời)",
                "Corticosteroid: Prednisone (điều trị đợt cấp)",
                "Immunosuppressant: Azathioprine, Mycophenolate, Cyclophosphamide (nếu nặng)",
                "Belimumab (nếu kháng trị)",
                "NSAID (nếu đau khớp nhẹ)",
                "Thuốc bảo vệ thận: ACE inhibitor (nếu có protein niệu)"
            ],
            "procedures": [
                "Tránh ánh nắng mặt trời (quan trọng)",
                "Theo dõi định kỳ: chức năng thận, huyết áp",
                "Điều trị biến chứng"
            ]
        },
        prevention=[
            "Tránh ánh nắng mặt trời (dùng kem chống nắng)",
            "Tránh stress",
            "Điều trị nhiễm trùng sớm",
            "Theo dõi định kỳ",
            "Tiêm vắc xin (nếu không đang dùng immunosuppressant)"
        ],
        complications=[
            "Bệnh thận lupus (nguy hiểm nhất)",
            "Bệnh thần kinh",
            "Bệnh tim mạch",
            "Nhiễm trùng (do immunosuppressant)",
            "Tử vong (nếu không điều trị)"
        ],
        related_scores=["SLEDAI", "SLICC/ACR Damage Index"],
        related_drugs=["Hydroxychloroquine", "Prednisone", "Azathioprine", "Mycophenolate", "Belimumab"],
        related_protocols=["SLE Management"],
        icd10_codes=["M32.9", "M32.0", "M32.1"]
    ),

    Disease(
        id="ankylosing_spondylitis",
        name="Ankylosing Spondylitis",
        name_vn="Viêm cột sống dính khớp",
        category="Rheumatology",
        definition="Viêm cột sống dính khớp là bệnh viêm khớp mạn tính, chủ yếu ảnh hưởng cột sống và khớp cùng chậu, gây đau và cứng, có thể dẫn đến dính khớp.",
        causes=[
            "Yếu tố di truyền: HLA-B27 (90% bệnh nhân)",
            "Tự miễn",
            "Yếu tố môi trường: nhiễm trùng",
            "Nam giới (tỷ lệ cao hơn nữ)",
            "Tuổi trẻ (20-30 tuổi)"
        ],
        symptoms=[
            "Đau lưng mạn tính, cứng lưng (đặc biệt buổi sáng)",
            "Đau khớp cùng chậu",
            "Đau cải thiện khi vận động, tăng khi nghỉ",
            "Giảm độ cong cột sống",
            "Viêm khớp ngoại biên (khớp gối, cổ chân)",
            "Viêm điểm bám gân (enthesitis)",
            "Viêm màng bồ đào (uveitis)",
            "Mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Modified New York criteria hoặc ASAS criteria",
                "Đau lưng mạn tính ≥ 3 tháng",
                "Hạn chế vận động cột sống",
                "Giảm độ giãn lồng ngực",
                "HLA-B27 dương tính",
                "X-quang: viêm khớp cùng chậu (sacroiliitis)"
            ],
            "tests": [
                "HLA-B27",
                "CRP, ESR (tăng)",
                "X-quang khớp cùng chậu",
                "MRI khớp cùng chậu (nếu X-quang bình thường)"
            ],
            "imaging": [
                "X-quang khớp cùng chậu (chuẩn vàng)",
                "MRI khớp cùng chậu (phát hiện sớm)",
                "X-quang cột sống (đánh giá dính khớp)"
            ]
        },
        treatment={
            "general": "Điều trị theo ASAS/EULAR guidelines. Mục tiêu: giảm đau, duy trì vận động, ngăn dính khớp.",
            "medications": [
                "NSAID: Ibuprofen, Naproxen, Indomethacin (thuốc đầu tay)",
                "Sulfasalazine (nếu có viêm khớp ngoại biên)",
                "TNF-alpha inhibitor: Adalimumab, Etanercept, Infliximab (nếu kháng NSAID)",
                "IL-17 inhibitor: Secukinumab (nếu kháng TNF)",
                "Corticosteroid (tiêm tại chỗ nếu cần)"
            ],
            "procedures": [
                "Vật lý trị liệu (quan trọng)",
                "Tập thể dục: kéo giãn, tăng cường cơ lưng",
                "Duy trì tư thế đúng",
                "Theo dõi định kỳ"
            ]
        },
        prevention=[
            "Tập thể dục đều đặn",
            "Duy trì tư thế đúng",
            "Điều trị sớm",
            "Tránh hút thuốc"
        ],
        complications=[
            "Dính khớp cột sống (bamboo spine)",
            "Gãy cột sống",
            "Viêm màng bồ đào",
            "Bệnh tim (hở van động mạch chủ)",
            "Loãng xương",
            "Tàn tật"
        ],
        related_scores=["BASDAI", "BASFI", "mSASSS"],
        related_drugs=["Ibuprofen", "Naproxen", "Sulfasalazine", "Adalimumab", "Etanercept"],
        related_protocols=["AS Management"],
        icd10_codes=["M45.9", "M45.0"]
    ),

    Disease(
        id="psoriatic_arthritis",
        name="Psoriatic Arthritis",
        name_vn="Viêm khớp vẩy nến",
        category="Rheumatology",
        definition="Viêm khớp vẩy nến là bệnh viêm khớp mạn tính kết hợp với bệnh vẩy nến da, có thể gây tổn thương khớp và móng.",
        causes=[
            "Bệnh vẩy nến da (30% bệnh nhân vẩy nến có viêm khớp)",
            "Yếu tố di truyền",
            "Yếu tố miễn dịch",
            "Yếu tố môi trường: nhiễm trùng, chấn thương",
            "Nam và nữ ngang nhau"
        ],
        symptoms=[
            "Viêm khớp: đau, sưng, cứng khớp",
            "Viêm khớp ngón tay, ngón chân (dactylitis - ngón tay hình xúc xích)",
            "Viêm điểm bám gân (enthesitis)",
            "Viêm cột sống (spondylitis)",
            "Tổn thương móng: rỗ, dày, tách móng",
            "Tổn thương da vẩy nến",
            "Mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "CASPAR criteria: bệnh vẩy nến + viêm khớp",
                "Tiền sử hoặc hiện tại có vẩy nến",
                "Viêm khớp",
                "Dactylitis hoặc enthesitis",
                "Tổn thương móng",
                "X-quang: tổn thương khớp"
            ],
            "tests": [
                "RF, Anti-CCP (âm tính - phân biệt với RA)",
                "CRP, ESR (tăng)",
                "X-quang khớp",
                "Siêu âm khớp (đánh giá viêm)"
            ],
            "imaging": [
                "X-quang khớp",
                "Siêu âm khớp",
                "MRI (nếu cần)"
            ]
        },
        treatment={
            "general": "Điều trị theo GRAPPA guidelines. Mục tiêu: kiểm soát viêm khớp và tổn thương da, ngăn tổn thương khớp.",
            "medications": [
                "NSAID (nếu nhẹ)",
                "DMARD: Methotrexate, Sulfasalazine, Leflunomide",
                "TNF-alpha inhibitor: Adalimumab, Etanercept, Infliximab (nếu kháng DMARD)",
                "IL-17 inhibitor: Secukinumab (điều trị cả da và khớp)",
                "IL-12/23 inhibitor: Ustekinumab",
                "Corticosteroid (tiêm tại chỗ hoặc uống ngắn hạn)"
            ],
            "procedures": [
                "Vật lý trị liệu",
                "Tập thể dục",
                "Điều trị tổn thương da",
                "Theo dõi định kỳ"
            ]
        },
        prevention=[
            "Điều trị vẩy nến sớm",
            "Tập thể dục",
            "Duy trì cân nặng hợp lý",
            "Tránh chấn thương"
        ],
        complications=[
            "Tổn thương khớp mạn tính",
            "Tàn tật",
            "Bệnh tim mạch",
            "Loãng xương",
            "Trầm cảm"
        ],
        related_scores=["DAS28", "PASI", "HAQ"],
        related_drugs=["Methotrexate", "Sulfasalazine", "Adalimumab", "Etanercept", "Secukinumab"],
        related_protocols=["PsA Management"],
        icd10_codes=["L40.5", "M07.3"]
    ),
]
