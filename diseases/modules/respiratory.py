"""
Respiratory Diseases Module
Diseases: COPD, Asthma
"""

from typing import List
from diseases.data import Disease


RESPIRATORY_DISEASES: List[Disease] = [
    Disease(
        id="copd",
        name="Chronic Obstructive Pulmonary Disease",
        name_vn="Bệnh phổi tắc nghẽn mạn tính (COPD)",
        category="Respiratory",
        definition="COPD là bệnh phổi mạn tính đặc trưng bởi tắc nghẽn luồng khí không hồi phục hoàn toàn.",
        causes=[
            "Hút thuốc lá (nguyên nhân chính)",
            "Ô nhiễm không khí",
            "Tiếp xúc với khói, bụi nghề nghiệp",
            "Thiếu alpha-1 antitrypsin (hiếm)"
        ],
        symptoms=[
            "Ho mạn tính",
            "Khạc đờm",
            "Khó thở khi gắng sức (tiến triển)",
            "Thở khò khè",
            "Tức ngực"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Spirometry: FEV1/FVC < 0.70 sau bronchodilator",
                "X-quang ngực: khí phế thũng, tăng sáng phổi"
            ],
            "tests": [
                "Spirometry (chức năng hô hấp)",
                "X-quang ngực",
                "CT ngực (nếu cần)",
                "Khí máu động mạch (nếu nặng)"
            ],
            "imaging": [
                "X-quang ngực",
                "CT ngực (để đánh giá khí phế thũng)"
            ]
        },
        treatment={
            "general": "Điều trị theo GOLD 2025 guidelines. Mục tiêu: giảm triệu chứng, giảm đợt cấp, cải thiện chất lượng cuộc sống. Điều chỉnh phân tầng thuốc, chiến lược giảm nguy cơ đợt cấp, điều trị cá thể hóa.",
            "medications": [
                "Bronchodilator: SABA (Salbutamol), LABA (Salmeterol, Formoterol, Indacaterol)",
                "Anticholinergic: SAMA (Ipratropium), LAMA (Tiotropium, Umeclidinium, Glycopyrronium)",
                "ICS/LABA kết hợp nếu đợt cấp thường xuyên hoặc eosinophilic phenotype",
                "Triple therapy (ICS/LABA/LAMA) cho bệnh nhân có đợt cấp thường xuyên",
                "Biologics cho COPD eosinophilic: Dupilumab (dupilumab) - giảm đợt cấp ~30-34%, Mepolizumab (Nucala) - cho COPD có eosinophilia",
                "Kháng sinh nếu đợt cấp do vi khuẩn",
                "Oxy liệu pháp nếu SpO2 < 88%",
                "Roflumilast (PDE4 inhibitor) cho bệnh nhân nặng có đợt cấp thường xuyên"
            ],
            "procedures": [
                "Oxy liệu pháp dài hạn (LTOT) - nếu SpO2 ≤88% hoặc ≤89% với biến chứng",
                "Thở máy không xâm lấn (NIV) trong đợt cấp nặng",
                "Phẫu thuật giảm thể tích phổi (LVRS) hoặc phẫu thuật cắt bóng khí phế thũng (nếu phù hợp)",
                "Ghép phổi (nếu nặng, trẻ tuổi)",
                "Theo dõi định kỳ: spirometry, đánh giá triệu chứng, đợt cấp"
            ]
        },
        prevention=[
            "Bỏ thuốc lá (quan trọng nhất)",
            "Tránh khói thuốc, ô nhiễm",
            "Tiêm vắc xin cúm, phế cầu",
            "Tập thể dục, phục hồi chức năng phổi"
        ],
        complications=[
            "Đợt cấp COPD",
            "Suy hô hấp",
            "Tâm phế mạn",
            "Tràn khí màng phổi",
            "Tử vong"
        ],
        related_scores=["GOLD Classification", "mMRC", "CAT Score", "COPD Assessment Test"],
        related_drugs=["Salbutamol", "Salmeterol", "Tiotropium", "Umeclidinium", "Glycopyrronium", "Budesonide", "Formoterol", "Dupilumab", "Mepolizumab", "Roflumilast", "Prednisone"],
        related_protocols=["COPD Exacerbation"],
        icd10_codes=["J44.9", "J44.0", "J44.1"]
    ),
    
    Disease(
        id="asthma",
        name="Asthma",
        name_vn="Hen phế quản",
        category="Respiratory",
        definition="Hen phế quản là bệnh viêm mạn tính đường thở, đặc trưng bởi tắc nghẽn đường thở có thể hồi phục, tăng phản ứng đường thở.",
        causes=[
            "Yếu tố di truyền",
            "Dị ứng: bụi, phấn hoa, lông thú, nấm mốc",
            "Nhiễm trùng đường hô hấp",
            "Ô nhiễm không khí",
            "Hút thuốc (chủ động, thụ động)",
            "Yếu tố kích thích: lạnh, gắng sức, stress"
        ],
        symptoms=[
            "Khó thở, thở khò khè",
            "Ho (đặc biệt về đêm, sáng sớm)",
            "Tức ngực",
            "Triệu chứng thay đổi theo thời gian, có thể tự hết hoặc sau dùng thuốc"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: khó thở, thở khò khè, ho, tức ngực",
                "Spirometry: FEV1/FVC < 0.75, tăng FEV1 > 12% sau bronchodilator",
                "Test kích thích: methacholine, mannitol (nếu cần)",
                "Peak flow: biến thiên > 20%"
            ],
            "tests": [
                "Spirometry (trước và sau bronchodilator)",
                "Peak expiratory flow (PEF)",
                "Test kích thích (nếu cần)",
                "Test dị ứng (nếu nghi ngờ dị ứng)",
                "X-quang ngực (loại trừ bệnh khác)"
            ],
            "imaging": [
                "X-quang ngực",
                "CT ngực (nếu nghi ngờ bệnh khác)"
            ]
        },
        treatment={
            "general": "Điều trị theo GINA 2025 và CHEST 2025 guidelines. Mục tiêu: kiểm soát triệu chứng, giảm đợt cấp, duy trì chức năng phổi bình thường. Điều trị cá nhân hóa dựa trên phenotype và biomarkers.",
            "medications": [
                "SABA (Salbutamol) - cắt cơn, nhưng không dùng đơn độc",
                "ICS (Inhaled Corticosteroid) - kiểm soát, bắt đầu sớm",
                "ICS-LABA kết hợp (Formoterol-Budesonide, Salmeterol-Fluticasone) - step 3-4",
                "LTRA (Montelukast) - nếu dị ứng hoặc không dung nạp ICS",
                "Biologics cho hen nặng (theo CHEST 2025):",
                "  - Omalizumab hoặc Dupilumab cho hen dị ứng + ≥1 đợt cấp/năm",
                "  - Dupilumab ưu tiên hơn Omalizumab nếu phụ thuộc steroid hoặc tái nhập viện",
                "  - Anti-IL-5/5Ra (Mepolizumab, Benralizumab, Reslizumab) cho eosinophilic asthma",
                "  - Tezepelumab cho hen nặng không kiểm soát",
                "  - Depemokimab (liều 2 lần/năm) - đang được EMA khuyến nghị phê duyệt",
                "Corticosteroid uống (nếu đợt cấp nặng) - giảm liều sớm",
                "Nếu không đáp ứng sau 4-6 tháng với một biologic, chuyển sang biologic khác"
            ],
            "procedures": [
                "Giáo dục bệnh nhân về hen",
                "Tránh yếu tố kích thích",
                "Theo dõi peak flow tại nhà",
                "Action plan cho đợt cấp",
                "Đánh giá biomarkers: BEC (blood eosinophil count), FeNO (fractional exhaled nitric oxide)",
                "Điều chỉnh liều ICS-LABA ở step-4 để giảm phơi nhiễm ICS liều cao"
            ]
        },
        prevention=[
            "Tránh yếu tố kích thích",
            "Dùng thuốc kiểm soát đều đặn",
            "Tiêm vắc xin cúm",
            "Quản lý dị ứng",
            "Bỏ thuốc lá"
        ],
        complications=[
            "Đợt cấp nặng (status asthmaticus)",
            "Suy hô hấp",
            "Xẹp phổi",
            "Tràn khí màng phổi",
            "Tử vong (nếu không điều trị kịp thời)"
        ],
        related_scores=["FEV1", "PEF", "Asthma Control Test"],
        related_drugs=["Salbutamol", "Budesonide", "Salmeterol", "Montelukast", "Prednisone"],
        related_protocols=["Asthma Exacerbation"],
        icd10_codes=["J45.9", "J45.0", "J45.1"]
    ),

    Disease(
        id="acute_bronchitis",
        name="Acute Bronchitis",
        name_vn="Viêm phế quản cấp",
        category="Respiratory",
        definition="Viêm phế quản cấp là tình trạng viêm cấp các phế quản, thường sau nhiễm virus đường hô hấp trên, rất hay gặp tại Việt Nam.",
        causes=[
            "Virus: Influenza, Parainfluenza, RSV, Rhinovirus",
            "Vi khuẩn (ít hơn): Mycoplasma pneumoniae, Bordetella pertussis",
            "Yếu tố nguy cơ: hút thuốc, ô nhiễm không khí, bệnh phổi nền"
        ],
        symptoms=[
            "Ho khan hoặc ho có đờm, thường kéo dài 1-3 tuần",
            "Đau ngực kiểu rát sau xương ức khi ho",
            "Sốt nhẹ, mệt mỏi",
            "Khò khè nhẹ",
            "Có thể còn ho kéo dài sau khi hết triệu chứng khác"
        ],
        diagnosis={
            "criteria": [
                "Lâm sàng: ho cấp < 3 tuần, nghe phổi có ran rít, ran ngáy",
                "Không có dấu viêm phổi (không thở nhanh nhiều, không hội chứng đông đặc)",
                "X-quang ngực bình thường hoặc chỉ tăng đậm phế quản"
            ],
            "tests": [
                "Thường không cần xét nghiệm ở ca nhẹ",
                "X-quang ngực nếu sốt cao, khó thở, nghi viêm phổi",
                "Xét nghiệm cúm, COVID-19 (nếu cần)"
            ],
            "imaging": [
                "X-quang ngực (loại trừ viêm phổi)"
            ]
        },
        treatment={
            "general": "Chủ yếu điều trị triệu chứng; kháng sinh không dùng thường quy vì đa số do virus.",
            "medications": [
                "Thuốc giảm ho, long đờm (Bromhexine, Acetylcysteine)",
                "Hạ sốt, giảm đau: Paracetamol, Ibuprofen",
                "Thuốc giãn phế quản dạng hít nếu khò khè nhiều",
                "Kháng sinh chỉ dùng nếu nghi bội nhiễm vi khuẩn hoặc bệnh nền nặng"
            ],
            "procedures": [
                "Uống nhiều nước, nghỉ ngơi",
                "Tránh hút thuốc và khói thuốc",
                "Theo dõi dấu hiệu nặng lên (sốt cao kéo dài, khó thở)"
            ]
        },
        prevention=[
            "Tiêm vắc xin cúm, COVID-19",
            "Bỏ thuốc lá",
            "Giảm tiếp xúc khói, bụi, ô nhiễm",
            "Rửa tay, vệ sinh đường hô hấp"
        ],
        complications=[
            "Viêm phổi",
            "Đợt cấp COPD hoặc hen ở bệnh nhân có bệnh nền",
            "Ho kéo dài gây mất ngủ, mệt mỏi"
        ],
        related_scores=[],
        related_drugs=["Paracetamol", "Ibuprofen", "Bromhexine", "Salbutamol"],
        related_protocols=["Acute Bronchitis Management"],
        icd10_codes=["J20.9"]
    ),

    Disease(
        id="idiopathic_pulmonary_fibrosis",
        name="Idiopathic Pulmonary Fibrosis",
        name_vn="Xơ phổi vô căn (IPF)",
        category="Respiratory",
        definition="Xơ phổi vô căn (IPF) là bệnh phổi mạn tính tiến triển, đặc trưng bởi xơ hóa phổi không rõ nguyên nhân, dẫn đến suy giảm chức năng phổi và tử vong.",
        causes=[
            "Nguyên nhân không rõ (vô căn)",
            "Yếu tố nguy cơ: tuổi cao (>50 tuổi), nam giới, hút thuốc lá",
            "Tiếp xúc với bụi, khói",
            "Yếu tố di truyền (một số trường hợp)",
            "Trào ngược dạ dày thực quản (GERD)"
        ],
        symptoms=[
            "Khó thở khi gắng sức (tiến triển)",
            "Ho khan",
            "Mệt mỏi",
            "Sụt cân",
            "Ngón tay dùi trống (clubbing)",
            "Ran nổ hai bên phổi"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: khó thở, ho khan",
                "CT ngực độ phân giải cao (HRCT): hình ảnh xơ phổi, dạng lưới, dạng tổ ong (honeycombing)",
                "Mô bệnh học: UIP (Usual Interstitial Pneumonia) pattern",
                "Loại trừ các nguyên nhân khác: tiếp xúc nghề nghiệp, thuốc, bệnh mô liên kết"
            ],
            "tests": [
                "CT ngực độ phân giải cao (HRCT) - chuẩn vàng",
                "Chức năng hô hấp: FVC, DLCO giảm",
                "6-minute walk test",
                "Khí máu động mạch (nếu nặng)",
                "Sinh thiết phổi (nếu CT không điển hình)"
            ],
            "imaging": [
                "CT ngực độ phân giải cao (HRCT)",
                "X-quang ngực (hình ảnh xơ phổi hai bên)"
            ]
        },
        treatment={
            "general": "Điều trị theo ATS/ERS/JRS/ALAT guidelines. Mục tiêu: làm chậm tiến triển, giảm đợt cấp, cải thiện chất lượng sống. Nerandomilast (Jascayd) được FDA phê duyệt 2025 - thuốc mới đầu tiên cho IPF sau hơn 10 năm.",
            "medications": [
                "Nerandomilast (Jascayd) - thuốc mới được FDA phê duyệt 2025, giúp giảm suy giảm FVC",
                "Pirfenidone - làm chậm tiến triển FVC",
                "Nintedanib - làm chậm tiến triển FVC",
                "Điều trị GERD: PPI (nếu có)",
                "Oxy liệu pháp nếu SpO2 < 88%",
                "Điều trị triệu chứng: giảm ho, giảm đau"
            ],
            "procedures": [
                "Oxy liệu pháp dài hạn (LTOT) - nếu SpO2 ≤88% hoặc ≤89% với biến chứng",
                "Phục hồi chức năng phổi",
                "Ghép phổi - chỉ định cho bệnh nhân trẻ, không có bệnh kèm nặng",
                "Theo dõi định kỳ: FVC, DLCO, CT ngực, 6-minute walk test"
            ]
        },
        prevention=[
            "Bỏ thuốc lá",
            "Tránh tiếp xúc với bụi, khói",
            "Điều trị GERD nếu có",
            "Tiêm vắc xin cúm, phế cầu"
        ],
        complications=[
            "Đợt cấp IPF (acute exacerbation) - nguy cơ tử vong cao",
            "Suy hô hấp",
            "Tâm phế mạn",
            "Ung thư phổi (nguy cơ tăng)",
            "Tràn khí màng phổi",
            "Tử vong (tiên lượng xấu, trung bình sống 3-5 năm sau chẩn đoán)"
        ],
        related_scores=["FVC", "DLCO", "GAP Index", "6-minute walk test"],
        related_drugs=["Nerandomilast", "Pirfenidone", "Nintedanib", "PPI"],
        related_protocols=["IPF Management", "Pulmonary Fibrosis"],
        icd10_codes=["J84.10", "J84.112"]
    ),
]
