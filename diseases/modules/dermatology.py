"""
Dermatology Module
Diseases: Atopic Dermatitis, Psoriasis
"""

from typing import List
from diseases.data import Disease


DERMATOLOGY_DISEASES: List[Disease] = [
    Disease(
        id="atopic_dermatitis",
        name="Atopic Dermatitis",
        name_vn="Viêm da cơ địa",
        category="Dermatology",
        definition="Viêm da cơ địa là bệnh viêm da mạn tính, tái phát, thường gặp ở trẻ em, đặc trưng bởi ngứa và tổn thương da.",
        causes=[
            "Yếu tố di truyền",
            "Rối loạn hàng rào da",
            "Dị ứng: bụi, phấn hoa, thức ăn",
            "Yếu tố môi trường: khô, lạnh, hóa chất",
            "Stress"
        ],
        symptoms=[
            "Ngứa dữ dội",
            "Tổn thương da: đỏ, khô, bong vảy, mụn nước",
            "Vị trí: mặt (trẻ em), nếp gấp (người lớn)",
            "Da dày lên, nứt nẻ (lichenification)",
            "Nhiễm trùng da thứ phát"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Tiền sử dị ứng (hen, viêm mũi dị ứng)",
                "Test dị ứng (nếu cần)",
                "Sinh thiết da (nếu không rõ)"
            ],
            "tests": [
                "Test dị ứng (patch test, prick test)",
                "IgE toàn phần (thường tăng)",
                "Sinh thiết da (nếu cần)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị đa yếu tố: dưỡng ẩm, tránh yếu tố kích thích, thuốc chống viêm.",
            "medications": [
                "Dưỡng ẩm: thường xuyên, sau tắm",
                "Corticosteroid tại chỗ (mức độ nhẹ đến trung bình)",
                "Calcineurin inhibitor tại chỗ (Tacrolimus, Pimecrolimus) - nếu kháng corticosteroid",
                "Kháng histamine (nếu ngứa nhiều)",
                "Kháng sinh (nếu nhiễm trùng)",
                "Corticosteroid toàn thân (nếu nặng, ngắn hạn)"
            ],
            "procedures": [
                "Tránh yếu tố kích thích",
                "Quang trị liệu (nếu nặng)",
                "Giáo dục bệnh nhân về chăm sóc da"
            ]
        },
        prevention=[
            "Dưỡng ẩm da thường xuyên",
            "Tránh yếu tố kích thích",
            "Tắm nước ấm, không quá nóng",
            "Mặc quần áo cotton, tránh len",
            "Giảm stress"
        ],
        complications=[
            "Nhiễm trùng da (Staphylococcus, Herpes)",
            "Viêm da tiếp xúc",
            "Rối loạn giấc ngủ (do ngứa)",
            "Ảnh hưởng chất lượng cuộc sống"
        ],
        related_scores=["SCORAD", "EASI"],
        related_drugs=["Topical Corticosteroid", "Tacrolimus", "Pimecrolimus", "Antihistamine"],
        related_protocols=["Atopic Dermatitis"],
        icd10_codes=["L20.9", "L20.8"]
    ),
    
    Disease(
        id="psoriasis",
        name="Psoriasis",
        name_vn="Vẩy nến",
        category="Dermatology",
        definition="Vẩy nến là bệnh viêm da mạn tính, đặc trưng bởi các mảng đỏ, bong vảy bạc, tái phát.",
        causes=[
            "Yếu tố di truyền",
            "Yếu tố miễn dịch",
            "Yếu tố kích thích: nhiễm trùng, stress, thuốc, chấn thương da",
            "Rượu bia, hút thuốc"
        ],
        symptoms=[
            "Mảng đỏ, bong vảy bạc",
            "Vị trí: khuỷu tay, đầu gối, da đầu, thân mình",
            "Ngứa (nhẹ đến trung bình)",
            "Tổn thương móng (rỗ, dày)",
            "Viêm khớp vẩy nến (30% bệnh nhân)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng điển hình",
                "Dấu hiệu Auspitz (chảy máu khi cạo vảy)",
                "Sinh thiết da (nếu không rõ)"
            ],
            "tests": [
                "Sinh thiết da (nếu cần)",
                "Xét nghiệm viêm khớp (nếu có triệu chứng khớp)"
            ],
            "imaging": [
                "X-quang khớp (nếu viêm khớp vẩy nến)"
            ]
        },
        treatment={
            "general": "Điều trị theo mức độ. Mục tiêu: giảm tổn thương, cải thiện chất lượng cuộc sống.",
            "medications": [
                "Nhẹ: Corticosteroid tại chỗ, Vitamin D analogues (Calcipotriol)",
                "Trung bình: UVB, PUVA",
                "Nặng: Methotrexate, Cyclosporine, Acitretin",
                "Sinh học: Adalimumab, Etanercept, Infliximab (nếu nặng, kháng thuốc)"
            ],
            "procedures": [
                "Quang trị liệu (UVB, PUVA)",
                "Giáo dục bệnh nhân"
            ]
        },
        prevention=[
            "Tránh yếu tố kích thích",
            "Giảm stress",
            "Bỏ thuốc lá, hạn chế rượu bia",
            "Dưỡng ẩm da"
        ],
        complications=[
            "Viêm khớp vẩy nến",
            "Bệnh tim mạch",
            "Trầm cảm",
            "Nhiễm trùng da"
        ],
        related_scores=["PASI", "BSA"],
        related_drugs=["Topical Corticosteroid", "Calcipotriol", "Methotrexate", "Cyclosporine", "Adalimumab"],
        related_protocols=["Psoriasis"],
        icd10_codes=["L40.9", "L40.0", "L40.1"]
    ),
    
    Disease(
        id="acne_vulgaris",
        name="Acne Vulgaris",
        name_vn="Mụn trứng cá",
        category="Dermatology",
        definition="Mụn trứng cá là bệnh da phổ biến, đặc biệt ở thanh thiếu niên, do viêm nang lông và tuyến bã, ảnh hưởng đến thẩm mỹ và tâm lý.",
        causes=[
            "Tăng tiết bã nhờn",
            "Tắc nghẽn nang lông",
            "Vi khuẩn: Propionibacterium acnes",
            "Viêm",
            "Hormone: androgen (dậy thì, PCOS)",
            "Yếu tố: mỹ phẩm, thuốc, stress, chế độ ăn"
        ],
        symptoms=[
            "Mụn đầu trắng, đầu đen",
            "Mụn đỏ, viêm",
            "Mụn mủ",
            "Mụn nang, nốt (nếu nặng)",
            "Vị trí: mặt, ngực, lưng",
            "Sẹo (nếu nặng, không điều trị)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng điển hình",
                "Phân loại: nhẹ, trung bình, nặng",
                "Loại trừ: rosacea, viêm nang lông"
            ],
            "tests": [
                "Khám lâm sàng",
                "Test hormone (nếu nghi ngờ rối loạn hormone)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị theo mức độ. Mục tiêu: giảm viêm, giảm tắc nghẽn, diệt vi khuẩn, ngăn sẹo.",
            "medications": [
                "Nhẹ: Benzoyl peroxide, Retinoid tại chỗ (Tretinoin, Adapalene)",
                "Trung bình: + Kháng sinh tại chỗ (Clindamycin, Erythromycin)",
                "Nặng: + Kháng sinh toàn thân (Doxycycline, Minocycline)",
                "Rất nặng: Isotretinoin (cần theo dõi chặt chẽ)",
                "Nội tiết: OCP (nếu nữ, có chỉ định)"
            ],
            "procedures": [
                "Rửa mặt nhẹ nhàng",
                "Tránh nặn mụn",
                "Laser, ánh sáng (nếu cần)",
                "Điều trị sẹo (nếu có)"
            ]
        },
        prevention=[
            "Vệ sinh da đúng cách",
            "Tránh mỹ phẩm gây tắc nghẽn",
            "Chế độ ăn lành mạnh",
            "Quản lý stress",
            "Điều trị sớm"
        ],
        complications=[
            "Sẹo",
            "Tăng sắc tố sau viêm",
            "Ảnh hưởng tâm lý",
            "Tự ti, trầm cảm"
        ],
        related_scores=["Acne Severity"],
        related_drugs=["Benzoyl Peroxide", "Tretinoin", "Adapalene", "Clindamycin", "Doxycycline", "Isotretinoin"],
        related_protocols=["Acne Management"],
        icd10_codes=["L70.9", "L70.0"]
    ),
    
    Disease(
        id="tinea",
        name="Tinea",
        name_vn="Nấm da",
        category="Dermatology",
        definition="Nấm da là nhiễm nấm trên da, rất phổ biến tại Việt Nam do khí hậu nóng ẩm, có thể ở nhiều vị trí khác nhau.",
        causes=[
            "Nấm: Trichophyton, Microsporum, Epidermophyton",
            "Yếu tố: ẩm ướt, nóng, vệ sinh kém, suy giảm miễn dịch",
            "Lây từ người, động vật, đất"
        ],
        symptoms=[
            "Tổn thương da: đỏ, có vảy, ngứa",
            "Hình tròn, lan rộng từ trung tâm",
            "Bờ rõ, có thể có mụn nước",
            "Vị trí: thân mình (tinea corporis), bẹn (tinea cruris), chân (tinea pedis), đầu (tinea capitis), móng (tinea unguium)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng điển hình",
                "Soi tươi KOH: thấy sợi nấm",
                "Cấy nấm (nếu cần)",
                "Wood's lamp (một số loại nấm phát quang)"
            ],
            "tests": [
                "Soi tươi KOH (chuẩn vàng)",
                "Cấy nấm",
                "Sinh thiết (nếu không rõ)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị tại chỗ hoặc toàn thân tùy vị trí và mức độ. Mục tiêu: diệt nấm, ngăn tái phát.",
            "medications": [
                "Tại chỗ: Clotrimazole, Miconazole, Terbinafine, Ketoconazole",
                "Toàn thân: Terbinafine, Itraconazole, Fluconazole (nếu lan rộng, móng, đầu)",
                "Thời gian: 2-4 tuần (tại chỗ), 2-12 tuần (toàn thân, tùy vị trí)"
            ],
            "procedures": [
                "Vệ sinh da",
                "Giữ khô ráo",
                "Tránh dùng chung khăn, quần áo",
                "Điều trị động vật (nếu lây từ động vật)"
            ]
        },
        prevention=[
            "Vệ sinh da, giữ khô ráo",
            "Không dùng chung khăn, quần áo",
            "Mang dép trong phòng tắm công cộng",
            "Điều trị sớm"
        ],
        complications=[
            "Nhiễm khuẩn thứ phát",
            "Tái phát",
            "Lan rộng",
            "Tổn thương móng (nếu không điều trị)"
        ],
        related_scores=["Tinea Severity"],
        related_drugs=["Clotrimazole", "Miconazole", "Terbinafine", "Itraconazole", "Ketoconazole"],
        related_protocols=[],
        icd10_codes=["B35.9", "B35.0", "B35.1", "B35.2", "B35.3", "B35.4"]
    ),

    Disease(
        id="urticaria",
        name="Urticaria",
        name_vn="Mề đay",
        category="Dermatology",
        definition="Mề đay là phản ứng da đặc trưng bởi các sẩn phù (wheals) ngứa, có thể cấp tính (< 6 tuần) hoặc mạn tính (≥ 6 tuần).",
        causes=[
            "Dị ứng: thức ăn (tôm, cua, đậu phộng), thuốc, côn trùng đốt",
            "Nhiễm trùng: virus, vi khuẩn",
            "Yếu tố vật lý: lạnh, nóng, ánh sáng, áp lực",
            "Stress",
            "Bệnh tự miễn",
            "Vô căn (mạn tính)"
        ],
        symptoms=[
            "Sẩn phù (wheals): nổi gờ, đỏ, ngứa",
            "Ngứa dữ dội",
            "Sẩn có thể hợp lại thành mảng lớn",
            "Sẩn thường biến mất trong 24h, không để lại dấu vết",
            "Phù mạch (angioedema): sưng môi, mí mắt, lưỡi",
            "Cấp tính: < 6 tuần",
            "Mạn tính: ≥ 6 tuần, tái phát"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: sẩn phù ngứa",
                "Tiền sử dị ứng",
                "Test dị ứng (nếu cấp tính)",
                "Loại trừ: bệnh khác (vascultis, mastocytosis)"
            ],
            "tests": [
                "Đánh giá lâm sàng",
                "Test dị ứng (nếu nghi ngờ)",
                "Công thức máu, IgE",
                "Test tự miễn (nếu mạn tính)",
                "Sinh thiết da (nếu không điển hình)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị theo EAACI/GA²LEN/EDF guidelines. Mục tiêu: giảm ngứa, giảm sẩn, cải thiện chất lượng cuộc sống.",
            "medications": [
                "Antihistamine H1: Cetirizine, Loratadine, Fexofenadine (thuốc đầu tay)",
                "Antihistamine H1 thế hệ 2 (không gây buồn ngủ): dùng liều cao nếu cần",
                "Antihistamine H2: Ranitidine (kết hợp với H1)",
                "Corticosteroid: Prednisone (nếu nặng, ngắn hạn)",
                "Omalizumab (nếu mạn tính kháng trị)",
                "Cyclosporine (nếu kháng trị)"
            ],
            "procedures": [
                "Tránh yếu tố kích thích",
                "Làm mát da (nếu ngứa)",
                "Theo dõi phù mạch (có thể nguy hiểm)"
            ]
        },
        prevention=[
            "Tránh yếu tố kích thích",
            "Tránh thức ăn dị ứng",
            "Quản lý stress",
            "Điều trị nhiễm trùng sớm"
        ],
        complications=[
            "Phù mạch (nguy hiểm nếu ở đường thở)",
            "Sốc phản vệ (nếu dị ứng nặng)",
            "Ảnh hưởng chất lượng cuộc sống",
            "Mất ngủ (do ngứa)"
        ],
        related_scores=["UAS7", "CU-Q2oL"],
        related_drugs=["Cetirizine", "Loratadine", "Fexofenadine", "Prednisone", "Omalizumab"],
        related_protocols=["Urticaria Management"],
        icd10_codes=["L50.9", "L50.0", "L50.1", "L50.2"]
    ),

    Disease(
        id="herpes_zoster",
        name="Herpes Zoster",
        name_vn="Zona thần kinh",
        category="Dermatology",
        definition="Zona thần kinh là bệnh do virus Varicella-Zoster (VZV) tái hoạt, gây phát ban đau đớn theo dây thần kinh, phổ biến ở người cao tuổi.",
        causes=[
            "Virus Varicella-Zoster (VZV) tái hoạt sau khi đã bị thủy đậu",
            "Suy giảm miễn dịch: tuổi cao, stress, bệnh mạn tính, thuốc ức chế miễn dịch",
            "Yếu tố nguy cơ: tuổi > 50, suy giảm miễn dịch, ung thư, HIV"
        ],
        symptoms=[
            "Đau, ngứa, tê bì theo dây thần kinh (trước khi phát ban)",
            "Phát ban: mụn nước thành chùm theo dây thần kinh",
            "Thường một bên cơ thể",
            "Vị trí thường gặp: ngực, lưng, mặt (dây thần kinh V)",
            "Mụn nước vỡ, đóng vảy",
            "Đau dữ dội",
            "Sốt, mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: phát ban theo dây thần kinh",
                "Tiền sử thủy đậu",
                "Xét nghiệm: PCR hoặc nuôi cấy virus (nếu cần)"
            ],
            "tests": [
                "Đánh giá lâm sàng",
                "PCR VZV (nếu không điển hình)",
                "Nuôi cấy virus",
                "Tzanck smear (tìm tế bào đa nhân khổng lồ)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị kháng virus sớm (trong 72h) để giảm đau và ngăn đau thần kinh sau zona. Điều trị đau.",
            "medications": [
                "Antiviral: Acyclovir, Valacyclovir, Famciclovir (trong 72h đầu)",
                "Giảm đau: Paracetamol, NSAID, Gabapentin, Pregabalin",
                "Opioid (nếu đau nặng)",
                "Corticosteroid: Prednisone (nếu nặng, giảm đau)",
                "Thuốc bôi: Acyclovir cream, Calamine lotion"
            ],
            "procedures": [
                "Giữ vết thương sạch",
                "Tránh gãi",
                "Theo dõi biến chứng"
            ]
        },
        prevention=[
            "Tiêm vắc xin zona (Shingrix) cho người ≥ 50 tuổi",
            "Tiêm vắc xin thủy đậu (nếu chưa bị)",
            "Tăng cường miễn dịch"
        ],
        complications=[
            "Đau thần kinh sau zona (postherpetic neuralgia) - phổ biến, kéo dài",
            "Nhiễm khuẩn da",
            "Zona mắt (có thể mù)",
            "Zona tai (Ramsay Hunt syndrome)",
            "Viêm não, viêm màng não (hiếm)"
        ],
        related_scores=["Pain Scale"],
        related_drugs=["Acyclovir", "Valacyclovir", "Famciclovir", "Gabapentin", "Pregabalin"],
        related_protocols=["Herpes Zoster Management"],
        icd10_codes=["B02.9", "B02.0", "B02.1", "B02.2"]
    ),

    Disease(
        id="scabies",
        name="Scabies",
        name_vn="Ghẻ",
        category="Dermatology",
        definition="Ghẻ là bệnh da do ký sinh trùng Sarcoptes scabiei, gây ngứa dữ dội, lây lan qua tiếp xúc gần, phổ biến ở Việt Nam.",
        causes=[
            "Ký sinh trùng Sarcoptes scabiei var. hominis",
            "Lây qua tiếp xúc da-da kéo dài",
            "Lây qua quần áo, chăn gối (ít gặp)",
            "Yếu tố nguy cơ: sống đông đúc, vệ sinh kém, suy giảm miễn dịch"
        ],
        symptoms=[
            "Ngứa dữ dội, đặc biệt về đêm",
            "Sẩn đỏ, mụn nước nhỏ",
            "Đường hang (burrow): đường ngoằn ngoèo, dài vài mm",
            "Vị trí: kẽ ngón tay, cổ tay, khuỷu tay, nách, bụng, bộ phận sinh dục",
            "Trẻ em: có thể ở lòng bàn tay, bàn chân, mặt",
            "Gãi nhiều gây nhiễm khuẩn thứ phát"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: ngứa về đêm, sẩn, đường hang",
                "Tìm thấy ký sinh trùng hoặc trứng dưới kính hiển vi",
                "Tiền sử tiếp xúc"
            ],
            "tests": [
                "Cạo da tìm ký sinh trùng (skin scraping)",
                "Kính hiển vi: tìm Sarcoptes scabiei, trứng, phân",
                "Dermoscopy (nếu có)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị đồng thời tất cả người tiếp xúc. Bôi thuốc toàn thân, giặt quần áo, chăn gối.",
            "medications": [
                "Permethrin 5% cream (thuốc đầu tay): bôi toàn thân, để 8-14h, rửa sạch",
                "Ivermectin uống (nếu kháng Permethrin hoặc ghẻ vảy)",
                "Benzyl benzoate 25% lotion",
                "Sulfur 10% ointment",
                "Điều trị ngứa: Antihistamine, Corticosteroid bôi",
                "Kháng sinh (nếu nhiễm khuẩn thứ phát)"
            ],
            "procedures": [
                "Bôi thuốc toàn thân (trừ mặt, đầu)",
                "Giặt quần áo, chăn gối ở nhiệt độ cao",
                "Điều trị đồng thời tất cả người trong gia đình",
                "Tái khám sau 1-2 tuần"
            ]
        },
        prevention=[
            "Vệ sinh cá nhân",
            "Tránh tiếp xúc với người bị ghẻ",
            "Giặt quần áo, chăn gối thường xuyên",
            "Điều trị đồng thời tất cả người tiếp xúc"
        ],
        complications=[
            "Nhiễm khuẩn da thứ phát (impetigo)",
            "Chàm hóa",
            "Ghẻ vảy (crusted scabies) - ở người suy giảm miễn dịch",
            "Ngứa kéo dài sau điều trị (do dị ứng)"
        ],
        related_scores=[],
        related_drugs=["Permethrin", "Ivermectin", "Benzyl Benzoate", "Sulfur"],
        related_protocols=["Scabies Management"],
        icd10_codes=["B86"]
    ),
]
