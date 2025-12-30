"""
Orthopedics Module
Bone, joint, and musculoskeletal diseases
"""

from typing import List
from diseases.data import Disease


ORTHOPEDICS_DISEASES: List[Disease] = [
    Disease(
        id="osteoarthritis",
        name="Osteoarthritis",
        name_vn="Thoái hóa khớp",
        category="Orthopedics",
        definition="Thoái hóa khớp là bệnh mạn tính do tổn thương sụn khớp, phổ biến ở người cao tuổi tại Việt Nam.",
        causes=[
            "Tuổi cao",
            "Chấn thương khớp",
            "Béo phì",
            "Di truyền",
            "Lạm dụng khớp",
            "Yếu tố nghề nghiệp"
        ],
        symptoms=[
            "Đau khớp (tăng khi vận động, giảm khi nghỉ)",
            "Cứng khớp (buổi sáng, < 30 phút)",
            "Hạn chế vận động",
            "Tiếng lạo xạo khớp",
            "Biến dạng khớp (giai đoạn muộn)",
            "Vị trí: gối, háng, cột sống, bàn tay"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "X-quang: hẹp khe khớp, gai xương, xơ hóa xương dưới sụn",
                "Loại trừ: viêm khớp dạng thấp, gout"
            ],
            "tests": [
                "X-quang khớp",
                "MRI (nếu cần đánh giá sụn)",
                "Xét nghiệm: loại trừ viêm (CRP, RF)"
            ],
            "imaging": [
                "X-quang khớp",
                "MRI khớp (nếu cần)"
            ]
        },
        treatment={
            "general": "Điều trị theo ACR/OARSI guidelines. Mục tiêu: giảm đau, cải thiện chức năng, làm chậm tiến triển.",
            "medications": [
                "NSAID: Ibuprofen, Naproxen, Celecoxib (giảm đau, viêm)",
                "Paracetamol (nếu đau nhẹ)",
                "Glucosamine, Chondroitin (có thể giúp)",
                "Tiêm corticosteroid vào khớp (nếu cần)",
                "Tiêm hyaluronic acid (nếu gối)"
            ],
            "procedures": [
                "Vật lý trị liệu",
                "Giảm cân (nếu béo phì)",
                "Tập thể dục (tăng cường cơ)",
                "Thay khớp (nếu nặng, ảnh hưởng chức năng)"
            ]
        },
        prevention=[
            "Duy trì cân nặng hợp lý",
            "Tập thể dục đều đặn",
            "Tránh chấn thương khớp",
            "Điều trị sớm"
        ],
        complications=[
            "Đau mạn tính",
            "Hạn chế vận động",
            "Tàn tật",
            "Ảnh hưởng chất lượng cuộc sống"
        ],
        related_scores=["WOMAC", "KOOS"],
        related_drugs=["Ibuprofen", "Naproxen", "Celecoxib", "Glucosamine"],
        related_protocols=["Osteoarthritis Management"],
        icd10_codes=["M19.9", "M15.9"]
    ),
    
    Disease(
        id="rheumatoid_arthritis",
        name="Rheumatoid Arthritis",
        name_vn="Viêm khớp dạng thấp",
        category="Orthopedics",
        definition="Viêm khớp dạng thấp là bệnh tự miễn mạn tính, gây viêm nhiều khớp, dẫn đến tổn thương khớp và biến dạng.",
        causes=[
            "Bệnh tự miễn",
            "Yếu tố di truyền",
            "Yếu tố môi trường: hút thuốc, nhiễm trùng",
            "Nữ giới (tỷ lệ cao hơn nam)",
            "Tuổi trung niên"
        ],
        symptoms=[
            "Đau, sưng nhiều khớp (đối xứng)",
            "Cứng khớp buổi sáng (> 1 giờ)",
            "Mệt mỏi, sốt nhẹ",
            "Nốt thấp (rheumatoid nodules)",
            "Biến dạng khớp (giai đoạn muộn)",
            "Tổn thương ngoài khớp: mắt, phổi, tim"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "RF (Rheumatoid Factor) dương tính",
                "Anti-CCP dương tính (đặc hiệu hơn)",
                "CRP, ESR tăng",
                "X-quang: tổn thương khớp"
            ],
            "tests": [
                "RF, Anti-CCP",
                "CRP, ESR",
                "Công thức máu (thiếu máu)",
                "X-quang khớp bàn tay, bàn chân"
            ],
            "imaging": [
                "X-quang khớp",
                "MRI (nếu cần đánh giá sớm)",
                "Siêu âm khớp"
            ]
        },
        treatment={
            "general": "Điều trị theo ACR/EULAR guidelines. Mục tiêu: kiểm soát viêm, ngăn tổn thương khớp, cải thiện chức năng.",
            "medications": [
                "DMARD: Methotrexate (thuốc đầu tay), Sulfasalazine, Hydroxychloroquine",
                "Biologic: Adalimumab, Etanercept, Rituximab (nếu kháng DMARD)",
                "Corticosteroid: Prednisone (ngắn hạn, liều thấp)",
                "NSAID: giảm đau, viêm"
            ],
            "procedures": [
                "Vật lý trị liệu",
                "Phẫu thuật (nếu biến dạng nặng)",
                "Theo dõi định kỳ"
            ]
        },
        prevention=[
            "Bỏ thuốc lá",
            "Điều trị sớm",
            "Theo dõi định kỳ"
        ],
        complications=[
            "Biến dạng khớp",
            "Tàn tật",
            "Tổn thương tim, phổi",
            "Loãng xương",
            "Nhiễm trùng (do thuốc ức chế miễn dịch)"
        ],
        related_scores=["DAS28", "HAQ"],
        related_drugs=["Methotrexate", "Sulfasalazine", "Adalimumab", "Etanercept", "Prednisone"],
        related_protocols=["Rheumatoid Arthritis Management"],
        icd10_codes=["M06.9", "M05.9"]
    ),
    
    Disease(
        id="osteoporosis",
        name="Osteoporosis",
        name_vn="Loãng xương",
        category="Orthopedics",
        definition="Loãng xương là tình trạng giảm mật độ xương, tăng nguy cơ gãy xương, phổ biến ở phụ nữ sau mãn kinh và người cao tuổi.",
        causes=[
            "Tuổi cao",
            "Mãn kinh (phụ nữ)",
            "Thiếu canxi, vitamin D",
            "Ít vận động",
            "Hút thuốc, rượu bia",
            "Thuốc: corticosteroid",
            "Bệnh: cường giáp, suy thận"
        ],
        symptoms=[
            "Thường không có triệu chứng cho đến khi gãy xương",
            "Đau lưng (nếu gãy đốt sống)",
            "Giảm chiều cao",
            "Gù lưng",
            "Gãy xương sau chấn thương nhẹ"
        ],
        diagnosis={
            "criteria": [
                "DEXA scan: T-score ≤ -2.5 (loãng xương) hoặc -1.0 đến -2.5 (giảm mật độ xương)",
                "Gãy xương do loãng xương",
                "FRAX score (đánh giá nguy cơ gãy xương)"
            ],
            "tests": [
                "DEXA scan (chuẩn vàng)",
                "X-quang (nếu nghi ngờ gãy xương)",
                "Canxi, vitamin D, PTH",
                "FRAX score"
            ],
            "imaging": [
                "DEXA scan",
                "X-quang (nếu gãy xương)"
            ]
        },
        treatment={
            "general": "Điều trị theo NOF/IOF guidelines. Mục tiêu: tăng mật độ xương, giảm nguy cơ gãy xương.",
            "medications": [
                "Bisphosphonate: Alendronate, Risedronate, Zoledronic acid",
                "Denosumab (kháng RANKL)",
                "Teriparatide (PTH) - nếu nặng",
                "Bổ sung: Canxi 1000-1200 mg/ngày, Vitamin D 800-1000 IU/ngày"
            ],
            "procedures": [
                "Tập thể dục (tăng cường cơ, xương)",
                "Phòng ngã",
                "Điều trị gãy xương (nếu có)"
            ]
        },
        prevention=[
            "Bổ sung canxi, vitamin D",
            "Tập thể dục đều đặn",
            "Bỏ thuốc lá, hạn chế rượu bia",
            "Phòng ngã",
            "Điều trị sớm"
        ],
        complications=[
            "Gãy xương (cổ xương đùi, đốt sống, cổ tay)",
            "Tàn tật",
            "Giảm chất lượng cuộc sống",
            "Tử vong (nếu gãy cổ xương đùi)"
        ],
        related_scores=["T-score", "FRAX Score"],
        related_drugs=["Alendronate", "Risedronate", "Zoledronic Acid", "Denosumab", "Calcium", "Vitamin D"],
        related_protocols=["Osteoporosis Management"],
        icd10_codes=["M81.9", "M80.9"]
    ),
]
