"""
Hematology Module
Diseases: Iron Deficiency Anemia, Thrombocytopenia
"""

from typing import List
from diseases.data import Disease


HEMATOLOGY_DISEASES: List[Disease] = [
    Disease(
        id="iron_deficiency_anemia",
        name="Iron Deficiency Anemia",
        name_vn="Thiếu máu thiếu sắt",
        category="Hematology",
        definition="Thiếu máu thiếu sắt là tình trạng giảm hemoglobin do thiếu sắt, nguyên nhân phổ biến nhất của thiếu máu tại Việt Nam.",
        causes=[
            "Mất máu mạn tính: xuất huyết tiêu hóa, kinh nguyệt nhiều, giun móc",
            "Thiếu cung cấp: chế độ ăn thiếu sắt, kém hấp thu",
            "Tăng nhu cầu: mang thai, trẻ em đang lớn",
            "Rối loạn hấp thu: bệnh celiac, cắt dạ dày"
        ],
        symptoms=[
            "Mệt mỏi, suy nhược",
            "Da xanh, niêm mạc nhợt",
            "Khó thở khi gắng sức",
            "Đánh trống ngực",
            "Đau đầu, chóng mặt",
            "Móng tay dễ gãy, tóc rụng",
            "Viêm lưỡi, khó nuốt (Plummer-Vinson syndrome)"
        ],
        diagnosis={
            "criteria": [
                "Hemoglobin giảm (nam < 13 g/dL, nữ < 12 g/dL)",
                "MCV giảm (microcytic anemia)",
                "Ferritin giảm (< 15 ng/mL)",
                "Sắt huyết thanh giảm, TIBC tăng",
                "Transferrin saturation < 15%"
            ],
            "tests": [
                "Công thức máu (CBC): Hb, MCV, MCH giảm",
                "Ferritin (tiêu chuẩn vàng)",
                "Sắt huyết thanh, TIBC",
                "Transferrin saturation",
                "Tìm nguyên nhân: nội soi dạ dày, xét nghiệm phân (tìm máu ẩn, giun móc)"
            ],
            "imaging": [
                "Nội soi dạ dày tá tràng (nếu nghi ngờ xuất huyết tiêu hóa)",
                "Nội soi đại tràng (nếu cần)"
            ]
        },
        treatment={
            "general": "Điều trị nguyên nhân + bổ sung sắt. Mục tiêu: tăng Hb, bổ sung dự trữ sắt.",
            "medications": [
                "Sắt uống: Ferrous sulfate 325mg x 1-2 lần/ngày (sau ăn, với vitamin C)",
                "Sắt tiêm tĩnh mạch (nếu không dung nạp hoặc cần tăng nhanh)",
                "Truyền máu (nếu thiếu máu nặng, có triệu chứng)"
            ],
            "procedures": [
                "Điều trị nguyên nhân: cầm máu, tẩy giun",
                "Theo dõi: Hb, ferritin sau 4-6 tuần"
            ]
        },
        prevention=[
            "Chế độ ăn giàu sắt (thịt đỏ, rau xanh, đậu)",
            "Bổ sung sắt khi mang thai",
            "Tẩy giun định kỳ",
            "Điều trị xuất huyết tiêu hóa"
        ],
        complications=[
            "Thiếu máu nặng",
            "Suy tim (nếu thiếu máu nặng kéo dài)",
            "Chậm phát triển (ở trẻ em)",
            "Biến chứng thai kỳ"
        ],
        related_scores=["Hemoglobin", "MCV", "Ferritin"],
        related_drugs=["Ferrous Sulfate", "Iron IV"],
        related_protocols=[],
        icd10_codes=["D50.9", "D50.0", "D50.8"]
    ),
    
    Disease(
        id="thrombocytopenia",
        name="Thrombocytopenia",
        name_vn="Giảm tiểu cầu",
        category="Hematology",
        definition="Giảm tiểu cầu là tình trạng số lượng tiểu cầu < 150,000/μL, có thể gây xuất huyết.",
        causes=[
            "Giảm sản xuất: bệnh tủy xương, hóa trị, thiếu B12/folate",
            "Tăng phá hủy: ITP (Immune Thrombocytopenic Purpura), DIC, HUS/TTP",
            "Tăng tiêu thụ: xuất huyết nặng, DIC",
            "Phân bố lại: lách to",
            "Giả tạo: đông máu trong ống nghiệm"
        ],
        symptoms=[
            "Xuất huyết da: chấm xuất huyết, ban xuất huyết",
            "Chảy máu mũi, chân răng",
            "Xuất huyết tiêu hóa, tiết niệu",
            "Xuất huyết não (nếu tiểu cầu < 10,000)",
            "Thường không có triệu chứng nếu tiểu cầu > 50,000"
        ],
        diagnosis={
            "criteria": [
                "Tiểu cầu < 150,000/μL",
                "Công thức máu: giảm tiểu cầu",
                "Phết máu ngoại vi: đánh giá hình thái tiểu cầu",
                "Tủy đồ (nếu cần): đánh giá sản xuất tiểu cầu"
            ],
            "tests": [
                "Công thức máu (CBC)",
                "Phết máu ngoại vi",
                "Đông máu (PT, PTT, fibrinogen)",
                "Tủy đồ (nếu nghi ngờ giảm sản xuất)",
                "Test kháng thể kháng tiểu cầu (nếu ITP)"
            ],
            "imaging": [
                "Siêu âm bụng (đánh giá lách to)",
                "CT (nếu nghi ngờ xuất huyết nội sọ)"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân. Mục tiêu: tăng tiểu cầu, phòng ngừa xuất huyết.",
            "medications": [
                "ITP: Corticosteroid (Prednisone), IVIG, Rituximab",
                "Truyền tiểu cầu (nếu xuất huyết nặng hoặc tiểu cầu < 10,000)",
                "Tranexamic acid (nếu xuất huyết)",
                "Điều trị nguyên nhân: kháng sinh (nếu nhiễm trùng), điều trị DIC"
            ],
            "procedures": [
                "Cắt lách (nếu ITP kháng trị)",
                "Truyền tiểu cầu (nếu cần)",
                "Theo dõi sát nếu tiểu cầu thấp"
            ]
        },
        prevention=[
            "Tránh thuốc gây giảm tiểu cầu",
            "Điều trị nguyên nhân sớm",
            "Theo dõi định kỳ nếu có nguy cơ"
        ],
        complications=[
            "Xuất huyết nặng",
            "Xuất huyết não (nguy hiểm nhất)",
            "Xuất huyết tiêu hóa",
            "Tử vong (nếu xuất huyết nặng)"
        ],
        related_scores=["Platelet Count", "Bleeding Score"],
        related_drugs=["Prednisone", "IVIG", "Rituximab", "Tranexamic Acid"],
        related_protocols=[],
        icd10_codes=["D69.6", "D69.3", "D69.4"]
    ),
]
