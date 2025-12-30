"""
Emergency Module
Diseases: Anaphylaxis, Acute Poisoning
"""

from typing import List
from diseases.data import Disease


EMERGENCY_DISEASES: List[Disease] = [
    Disease(
        id="anaphylaxis",
        name="Anaphylaxis",
        name_vn="Phản vệ",
        category="Emergency",
        definition="Phản vệ là phản ứng dị ứng cấp tính, đe dọa tính mạng, xảy ra trong vài phút đến vài giờ sau tiếp xúc dị nguyên.",
        causes=[
            "Thức ăn: đậu phộng, hải sản, trứng, sữa",
            "Thuốc: penicillin, aspirin, NSAID",
            "Côn trùng đốt: ong, kiến",
            "Latex",
            "Vắc xin",
            "Chất cản quang"
        ],
        symptoms=[
            "Tổn thương da: mề đay, phù mạch",
            "Hô hấp: khó thở, thở khò khè, phù thanh quản",
            "Huyết động: hạ huyết áp, sốc",
            "Tiêu hóa: buồn nôn, nôn, đau bụng",
            "Tri giác: lú lẫn, ngất"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng cấp tính sau tiếp xúc dị nguyên",
                "≥ 2 hệ cơ quan bị ảnh hưởng",
                "Hoặc hạ huyết áp sau tiếp xúc dị nguyên đã biết"
            ],
            "tests": [
                "Đánh giá lâm sàng (khẩn cấp)",
                "Tryptase (nếu có thể, trong 1-2 giờ)",
                "Test dị ứng (sau khi ổn định)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị khẩn cấp: Adrenaline IM ngay lập tức, hỗ trợ hô hấp, tuần hoàn.",
            "medications": [
                "Adrenaline (Epinephrine) IM 0.3-0.5mg (0.01 mg/kg trẻ em) - ngay lập tức",
                "Oxy",
                "Truyền dịch (nếu hạ huyết áp)",
                "Antihistamine: Diphenhydramine",
                "Corticosteroid: Methylprednisolone (phòng ngừa phản ứng muộn)",
                "Albuterol khí dung (nếu co thắt phế quản)"
            ],
            "procedures": [
                "Đặt nội khí quản (nếu phù thanh quản)",
                "Theo dõi 4-6 giờ (24 giờ nếu nặng)",
                "Giáo dục bệnh nhân về epinephrine auto-injector"
            ]
        },
        prevention=[
            "Tránh dị nguyên đã biết",
            "Đeo vòng cảnh báo y tế",
            "Mang epinephrine auto-injector",
            "Giáo dục bệnh nhân và người thân"
        ],
        complications=[
            "Sốc phản vệ",
            "Suy hô hấp",
            "Ngừng tim",
            "Tử vong (nếu không điều trị kịp thời)"
        ],
        related_scores=["Anaphylaxis Severity"],
        related_drugs=["Epinephrine", "Diphenhydramine", "Methylprednisolone", "Albuterol"],
        related_protocols=["Anaphylaxis emergency protocol"],
        icd10_codes=["T78.2", "T80.5"]
    ),
    
    Disease(
        id="acute_poisoning",
        name="Acute Poisoning",
        name_vn="Ngộ độc cấp",
        category="Emergency",
        definition="Ngộ độc cấp là tình trạng tiếp xúc với chất độc, gây tổn thương cấp tính, đe dọa tính mạng.",
        causes=[
            "Thuốc: paracetamol, aspirin, thuốc ngủ, opioid",
            "Hóa chất: thuốc trừ sâu, rượu methanol",
            "Thực phẩm: nấm độc, cá nóc",
            "Khí độc: CO, H2S",
            "Tự tử, tai nạn"
        ],
        symptoms=[
            "Tùy chất độc: buồn nôn, nôn, đau bụng",
            "Rối loạn ý thức: lú lẫn, hôn mê",
            "Rối loạn hô hấp",
            "Rối loạn tim mạch",
            "Co giật"
        ],
        diagnosis={
            "criteria": [
                "Tiền sử tiếp xúc chất độc",
                "Triệu chứng lâm sàng",
                "Xét nghiệm độc chất",
                "Đánh giá mức độ nặng"
            ],
            "tests": [
                "Xét nghiệm độc chất (nếu có)",
                "Paracetamol level (nếu nghi ngờ)",
                "Salicylate level (nếu nghi ngờ)",
                "Công thức máu, chức năng gan, thận",
                "Khí máu động mạch",
                "ECG"
            ],
            "imaging": [
                "X-quang bụng (nếu nuốt dị vật)",
                "CT não (nếu rối loạn ý thức)"
            ]
        },
        treatment={
            "general": "Điều trị khẩn cấp: hỗ trợ hô hấp, tuần hoàn, giải độc đặc hiệu, loại bỏ chất độc.",
            "medications": [
                "Giải độc đặc hiệu: N-acetylcysteine (paracetamol), Naloxone (opioid), Flumazenil (benzodiazepine)",
                "Than hoạt (activated charcoal) - nếu trong 1 giờ",
                "Hỗ trợ: chống co giật, điều chỉnh rối loạn điện giải",
                "Antidote: Atropine (organophosphate), Pralidoxime"
            ],
            "procedures": [
                "Rửa dạ dày (nếu trong 1 giờ, không có chống chỉ định)",
                "Thở máy (nếu suy hô hấp)",
                "Lọc máu (nếu cần)",
                "Theo dõi sát"
            ]
        },
        prevention=[
            "Bảo quản thuốc, hóa chất an toàn",
            "Giáo dục về ngộ độc",
            "Điều trị rối loạn tâm thần",
            "Gọi trung tâm chống độc"
        ],
        complications=[
            "Suy đa tạng",
            "Tổn thương gan (paracetamol)",
            "Tổn thương thận",
            "Tử vong"
        ],
        related_scores=["GCS", "APACHE II"],
        related_drugs=["N-acetylcysteine", "Naloxone", "Activated Charcoal", "Atropine"],
        related_protocols=["Paracetamol overdose"],
        icd10_codes=["T50.9", "T36.9", "T65.9"]
    ),
]
