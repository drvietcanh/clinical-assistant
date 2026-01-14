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

    Disease(
        id="vitamin_b12_deficiency_anemia",
        name="Vitamin B12 Deficiency Anemia",
        name_vn="Thiếu máu thiếu vitamin B12",
        category="Hematology",
        definition="Thiếu máu đại hồng cầu do thiếu vitamin B12, thường gặp ở người ăn chay tuyệt đối, kém hấp thu, hoặc sau cắt dạ dày.",
        causes=[
            "Giảm hấp thu: viêm dạ dày teo, thiếu yếu tố nội tại, cắt dạ dày",
            "Chế độ ăn thiếu (ăn chay tuyệt đối lâu dài)",
            "Tăng nhu cầu: mang thai",
            "Thuốc: metformin, ức chế bơm proton kéo dài"
        ],
        symptoms=[
            "Mệt mỏi, da xanh",
            "Lưỡi đỏ, đau (viêm lưỡi)",
            "Tê bì, dị cảm, mất thăng bằng (tổn thương thần kinh)",
            "Thiếu máu đại hồng cầu"
        ],
        diagnosis={
            "criteria": [
                "Hb giảm, MCV tăng",
                "Vitamin B12 huyết thanh thấp",
                "Có thể Homocysteine, MMA tăng",
                "Loại trừ thiếu folate"
            ],
            "tests": [
                "CBC (MCV cao)",
                "Vitamin B12, Folate",
                "Homocysteine/MMA (nếu cần)",
                "Kháng thể kháng yếu tố nội tại (nếu nghi thiếu máu ác tính)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Bổ sung vitamin B12, điều chỉnh nguyên nhân kém hấp thu.",
            "medications": [
                "Vitamin B12 tiêm hoặc uống liều cao",
                "Acid folic nếu thiếu phối hợp",
                "Điều trị nguyên nhân dạ dày/ruột"
            ],
            "procedures": [
                "Theo dõi Hb, MCV, thần kinh",
                "Giáo dục dinh dưỡng"
            ]
        },
        prevention=[
            "Chế độ ăn đủ B12 (thịt, cá, sữa) hoặc bổ sung cho người ăn chay",
            "Theo dõi ở người dùng metformin/PPI lâu dài"
        ],
        complications=[
            "Tổn thương thần kinh không hồi phục nếu kéo dài",
            "Thiếu máu nặng"
        ],
        related_scores=[],
        related_drugs=["Vitamin B12", "Folic Acid"],
        related_protocols=["Macrocytic Anemia"],
        icd10_codes=["D51.9"]
    ),

    Disease(
        id="anemia_of_chronic_disease",
        name="Anemia of Chronic Disease",
        name_vn="Thiếu máu bệnh mạn",
        category="Hematology",
        definition="Thiếu máu nhẹ-vừa do viêm mạn, bệnh mạn (thận, viêm khớp, ung thư), với sắt huyết thanh thấp nhưng ferritin bình thường/tăng.",
        causes=[
            "Bệnh viêm mạn: viêm khớp dạng thấp, lupus",
            "Bệnh thận mạn",
            "Ung thư, nhiễm trùng mạn",
            "Cơ chế: tăng hepcidin, giảm sử dụng sắt"
        ],
        symptoms=[
            "Mệt mỏi, da nhợt",
            "Triệu chứng nhẹ, tương ứng Hb 8-11 g/dL"
        ],
        diagnosis={
            "criteria": [
                "Hb giảm nhẹ-vừa, MCV bình thường/giảm nhẹ",
                "Sắt huyết thanh giảm, TIBC giảm hoặc bình thường, ferritin bình thường/tăng",
                "Có bệnh nền mạn tính"
            ],
            "tests": [
                "CBC, MCV",
                "Sắt huyết thanh, TIBC, Ferritin",
                "CRP, ESR (viêm)",
                "Creatinine (nếu bệnh thận)"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị bệnh nền, không tự ý bổ sung sắt khi ferritin không thiếu.",
            "medications": [
                "Điều trị bệnh mạn (kháng viêm, kiểm soát bệnh)",
                "Erythropoietin nếu bệnh thận và Hb thấp",
                "Sắt IV chỉ nếu kèm thiếu sắt thật sự"
            ],
            "procedures": [
                "Theo dõi Hb định kỳ",
                "Điều chỉnh điều trị theo bệnh nền"
            ]
        },
        prevention=[
            "Kiểm soát tốt bệnh mạn",
            "Tầm soát thiếu sắt thật sự nếu nghi ngờ"
        ],
        complications=[
            "Giảm chất lượng sống",
            "Phải truyền máu nếu Hb giảm sâu (hiếm)"
        ],
        related_scores=[],
        related_drugs=["Erythropoietin"],
        related_protocols=["Anemia of Chronic Disease"],
        icd10_codes=["D63.8"]
    ),

    Disease(
        id="thalassemia_minor",
        name="Beta Thalassemia Minor",
        name_vn="Thalassemia thể nhẹ (beta)",
        category="Hematology",
        definition="Thalassemia thể nhẹ là thể mang gen, thiếu máu nhẹ, MCV thấp, thường phát hiện tình cờ; cần tư vấn di truyền.",
        causes=[
            "Đột biến gen beta-globin dị hợp tử",
            "Thường gặp ở vùng lưu hành thalassemia"
        ],
        symptoms=[
            "Thường không triệu chứng",
            "Thiếu máu nhẹ, MCV thấp",
            "Có thể mệt nhẹ"
        ],
        diagnosis={
            "criteria": [
                "Thiếu máu nhược sắc hồng cầu nhỏ, MCV thấp",
                "Điện di Hb: HbA2 tăng",
                "Ferritin bình thường (loại trừ thiếu sắt)"
            ],
            "tests": [
                "CBC, MCV, MCH",
                "Ferritin",
                "Điện di Hb",
                "Tư vấn di truyền khi lập gia đình"
            ],
            "imaging": []
        },
        treatment={
            "general": "Không cần điều trị đặc hiệu; tránh bổ sung sắt nếu không thiếu.",
            "medications": [
                "Bổ sung acid folic (tùy tình huống)",
                "Không dùng sắt nếu ferritin bình thường"
            ],
            "procedures": [
                "Tư vấn di truyền tiền hôn nhân/sinh sản"
            ]
        },
        prevention=[
            "Sàng lọc mang gen tại vùng lưu hành",
            "Tư vấn di truyền"
        ],
        complications=[
            "Nguy cơ con mắc thalassemia thể nặng nếu cả hai bố mẹ mang gen"
        ],
        related_scores=[],
        related_drugs=["Folic Acid"],
        related_protocols=["Thalassemia Screening"],
        icd10_codes=["D56.3"]
    ),
]
