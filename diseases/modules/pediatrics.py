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
]
