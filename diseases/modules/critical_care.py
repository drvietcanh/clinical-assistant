"""
Critical Care Module
Intensive care and life-threatening conditions
"""

from typing import List
from diseases.data import Disease


CRITICAL_CARE_DISEASES: List[Disease] = [
    Disease(
        id="ards",
        name="Acute Respiratory Distress Syndrome",
        name_vn="Hội chứng suy hô hấp cấp (ARDS)",
        category="Critical Care",
        definition="ARDS là hội chứng suy hô hấp cấp tính nặng, đặc trưng bởi tổn thương phế nang lan tỏa, phù phổi không do tim, giảm oxy máu khó điều chỉnh.",
        causes=[
            "Nhiễm trùng: viêm phổi, sepsis, COVID-19",
            "Chấn thương: chấn thương ngực, bỏng",
            "Hít phải: hít dịch dạ dày, khói độc",
            "Tắc mạch phổi",
            "Viêm tụy cấp",
            "Truyền máu",
            "Dùng thuốc: heroin, aspirin"
        ],
        symptoms=[
            "Khó thở nặng, tăng dần",
            "Giảm oxy máu (PaO2/FiO2 < 300 mmHg)",
            "Thở nhanh",
            "Xanh tím",
            "Cần thở máy",
            "Tổn thương phổi hai bên trên X-quang"
        ],
        diagnosis={
            "criteria": [
                "Berlin Definition 2012:",
                "1. Khởi phát trong vòng 1 tuần",
                "2. X-quang ngực: tổn thương phổi hai bên",
                "3. Phù phổi không do tim hoặc quá tải dịch",
                "4. Giảm oxy máu: PaO2/FiO2 ≤ 300 mmHg (với PEEP ≥ 5 cmH2O)",
                "Phân loại: nhẹ (200-300), trung bình (100-200), nặng (< 100)"
            ],
            "tests": [
                "Khí máu động mạch: PaO2/FiO2",
                "X-quang ngực",
                "CT ngực (nếu cần)",
                "Siêu âm tim (loại trừ suy tim)",
                "Echocardiography (đánh giá chức năng tim)"
            ],
            "imaging": [
                "X-quang ngực",
                "CT ngực",
                "Siêu âm tim"
            ]
        },
        treatment={
            "general": "Điều trị theo ARDS Network protocol. Mục tiêu: cải thiện oxy hóa, bảo vệ phổi, điều trị nguyên nhân.",
            "medications": [
                "Thở máy: chiến lược bảo vệ phổi (tidal volume 6 ml/kg, PEEP cao, FiO2 thấp)",
                "Nằm sấp (prone positioning) - nếu nặng",
                "Corticosteroid: Methylprednisolone (nếu COVID-19, một số trường hợp)",
                "Điều trị nguyên nhân",
                "An thần, giãn cơ (nếu cần)"
            ],
            "procedures": [
                "Thở máy: chiến lược bảo vệ phổi",
                "Nằm sấp (prone positioning)",
                "ECMO (Extracorporeal Membrane Oxygenation) - nếu rất nặng",
                "Điều trị nguyên nhân",
                "Quản lý dịch (hạn chế dịch nếu có thể)"
            ]
        },
        prevention=[
            "Điều trị sớm nhiễm trùng",
            "Phòng ngừa hít sặc",
            "Quản lý dịch cẩn thận",
            "Thở máy an toàn"
        ],
        complications=[
            "Tử vong (tỷ lệ cao: 30-50%)",
            "Tổn thương phổi mạn",
            "Nhiễm trùng bệnh viện",
            "Barotrauma",
            "Suy đa tạng"
        ],
        related_scores=["PaO2/FiO2", "APACHE II", "SOFA Score", "Lung Injury Score"],
        related_drugs=["Methylprednisolone", "Sedatives", "Neuromuscular Blockers"],
        related_protocols=["ARDS Network Protocol", "Lung Protective Ventilation"],
        icd10_codes=["J80"]
    ),
    
    Disease(
        id="septic_shock",
        name="Septic Shock",
        name_vn="Sốc nhiễm khuẩn",
        category="Critical Care",
        definition="Sốc nhiễm khuẩn là tình trạng sốc do nhiễm trùng, đặc trưng bởi hạ huyết áp không đáp ứng với bù dịch, rối loạn vi tuần hoàn, suy đa tạng.",
        causes=[
            "Nhiễm trùng: vi khuẩn, virus, nấm",
            "Nguồn nhiễm: phổi, bụng, đường tiết niệu, da",
            "Yếu tố nguy cơ: suy giảm miễn dịch, tuổi cao, bệnh mạn tính, phẫu thuật"
        ],
        symptoms=[
            "Sốt hoặc hạ thân nhiệt",
            "Hạ huyết áp (không đáp ứng bù dịch)",
            "Nhịp tim nhanh",
            "Thở nhanh",
            "Rối loạn ý thức",
            "Thiểu niệu",
            "Da lạnh, ẩm",
            "Tăng lactate máu"
        ],
        diagnosis={
            "criteria": [
                "Sepsis-3 Definition:",
                "1. Nhiễm trùng đã biết hoặc nghi ngờ",
                "2. SOFA score ≥ 2 (tăng từ baseline)",
                "3. Sốc: hạ huyết áp kéo dài cần vasopressor + lactate ≥ 2 mmol/L",
                "Loại trừ: sốc do nguyên nhân khác"
            ],
            "tests": [
                "Cấy máu, dịch (nếu có)",
                "Công thức máu, CRP, Procalcitonin",
                "Lactate máu",
                "Chức năng thận, gan",
                "Khí máu động mạch",
                "SOFA score"
            ],
            "imaging": [
                "X-quang ngực",
                "CT (nếu cần tìm nguồn nhiễm)",
                "Siêu âm (nếu nghi ngờ nguồn bụng)"
            ]
        },
        treatment={
            "general": "Điều trị theo Surviving Sepsis Campaign 2025 guidelines. Mục tiêu: kháng sinh sớm (1 giờ đầu), bù dịch, vasopressor, điều trị nguyên nhân, theo dõi lactate.",
            "medications": [
                "Kháng sinh phổ rộng sớm (trong 1 giờ đầu sau nhận diện sepsis) - ưu tiên cao nhất",
                "Bù dịch: Crystalloid (30 ml/kg ban đầu, điều chỉnh theo đáp ứng)",
                "Vasopressor: Norepinephrine (thuốc đầu tay) - nếu hạ huyết áp kéo dài sau bù dịch",
                "Vasopressin - có thể thêm nếu cần norepinephrine liều cao",
                "Corticosteroid: Hydrocortisone (nếu kháng vasopressor hoặc có chỉ định khác)",
                "Điều trị nguyên nhân: dẫn lưu, phẫu thuật (trong 12 giờ đầu nếu có thể)",
                "Điều chỉnh kháng sinh theo kết quả cấy và procalcitonin"
            ],
            "procedures": [
                "Kháng sinh sớm (1 giờ đầu) - ưu tiên cao nhất",
                "Bù dịch tích cực (theo dõi đáp ứng)",
                "Vasopressor (nếu cần) - norepinephrine qua đường tĩnh mạch trung tâm",
                "Thở máy (nếu suy hô hấp) - chiến lược bảo vệ phổi",
                "Lọc máu (nếu suy thận, AKI)",
                "Dẫn lưu, phẫu thuật (nếu cần) - trong 12 giờ đầu",
                "Theo dõi lactate - mục tiêu giảm lactate ≥20% trong 2 giờ đầu"
            ]
        },
        prevention=[
            "Điều trị nhiễm trùng sớm",
            "Vệ sinh tay",
            "Phòng ngừa nhiễm trùng bệnh viện",
            "Tiêm vắc xin"
        ],
        complications=[
            "Suy đa tạng",
            "Tử vong (tỷ lệ cao: 40-50%)",
            "Tổn thương thận mạn",
            "Tổn thương thần kinh"
        ],
        related_scores=["SOFA Score", "APACHE II", "qSOFA", "Lactate"],
        related_drugs=["Norepinephrine", "Vasopressin", "Hydrocortisone", "Broad-spectrum Antibiotics"],
        related_protocols=["Surviving Sepsis Campaign", "Early Goal-Directed Therapy"],
        icd10_codes=["A41.9", "R57.2"]
    ),
    
    Disease(
        id="cardiogenic_shock",
        name="Cardiogenic Shock",
        name_vn="Sốc tim",
        category="Critical Care",
        definition="Sốc tim là tình trạng suy tim cấp nặng, không đủ cung lượng tim để duy trì tưới máu mô, dẫn đến hạ huyết áp, thiếu máu mô.",
        causes=[
            "Nhồi máu cơ tim cấp (nguyên nhân chính)",
            "Suy tim cấp",
            "Rối loạn nhịp tim nặng",
            "Viêm cơ tim",
            "Bệnh van tim cấp",
            "Thuyên tắc phổi lớn",
            "Chèn ép tim (tamponade)"
        ],
        symptoms=[
            "Hạ huyết áp (SBP < 90 mmHg)",
            "Nhịp tim nhanh hoặc chậm",
            "Thiểu niệu",
            "Rối loạn ý thức",
            "Da lạnh, ẩm",
            "Tăng lactate máu",
            "Phù phổi (nếu suy tim trái)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: hạ huyết áp, thiếu máu mô",
                "Siêu âm tim: giảm chức năng tim (EF < 40%), rối loạn vận động vùng",
                "Đo cung lượng tim: giảm (CI < 2.2 L/min/m²)",
                "Tăng áp lực đổ đầy (nếu có catheter)",
                "ECG: nhồi máu cơ tim, rối loạn nhịp"
            ],
            "tests": [
                "ECG",
                "Troponin, CK-MB",
                "BNP, NT-proBNP",
                "Siêu âm tim",
                "Khí máu động mạch",
                "Lactate máu",
                "Catheter động mạch phổi (nếu có)"
            ],
            "imaging": [
                "Siêu âm tim",
                "X-quang ngực",
                "Coronary angiography (nếu nhồi máu cơ tim)"
            ]
        },
        treatment={
            "general": "Điều trị theo AHA/ACC guidelines. Mục tiêu: cải thiện cung lượng tim, tưới máu mô, điều trị nguyên nhân.",
            "medications": [
                "Inotrope: Dobutamine, Milrinone (tăng co bóp tim)",
                "Vasopressor: Norepinephrine, Epinephrine (nếu hạ huyết áp nặng)",
                "Điều trị nhồi máu cơ tim: Aspirin, Clopidogrel, Statin",
                "Reperfusion: PCI hoặc thrombolysis (nếu nhồi máu cơ tim)",
                "Diuretic (nếu quá tải dịch)"
            ],
            "procedures": [
                "PCI (nếu nhồi máu cơ tim)",
                "Thrombolysis (nếu không có PCI)",
                "IABP (Intra-aortic Balloon Pump)",
                "ECMO (nếu nặng)",
                "Thở máy (nếu suy hô hấp)",
                "Lọc máu (nếu suy thận)"
            ]
        },
        prevention=[
            "Điều trị sớm nhồi máu cơ tim",
            "Quản lý suy tim",
            "Phòng ngừa rối loạn nhịp tim"
        ],
        complications=[
            "Tử vong (tỷ lệ cao: 50-70%)",
            "Suy đa tạng",
            "Rối loạn nhịp tim",
            "Tổn thương thận"
        ],
        related_scores=["Cardiac Index", "Ejection Fraction", "APACHE II", "SOFA Score"],
        related_drugs=["Dobutamine", "Milrinone", "Norepinephrine", "Epinephrine"],
        related_protocols=["Cardiogenic Shock Management", "PCI Protocol"],
        icd10_codes=["R57.0"]
    ),
    
    Disease(
        id="mods",
        name="Multiple Organ Dysfunction Syndrome",
        name_vn="Hội chứng suy đa tạng (MODS)",
        category="Critical Care",
        definition="MODS là tình trạng suy chức năng đồng thời của ≥ 2 cơ quan, thường do nhiễm trùng, chấn thương, hoặc bệnh nặng, có tỷ lệ tử vong cao.",
        causes=[
            "Sepsis, sốc nhiễm khuẩn",
            "Chấn thương nặng",
            "Bỏng nặng",
            "Viêm tụy cấp nặng",
            "Sốc tim",
            "Phẫu thuật lớn",
            "Truyền máu"
        ],
        symptoms=[
            "Suy hô hấp: cần thở máy, ARDS",
            "Suy tuần hoàn: hạ huyết áp, cần vasopressor",
            "Suy thận: thiểu niệu, tăng creatinine",
            "Suy gan: tăng bilirubin, ALT, AST",
            "Rối loạn đông máu: giảm tiểu cầu, PT kéo dài",
            "Rối loạn ý thức",
            "Suy đa tạng tiến triển"
        ],
        diagnosis={
            "criteria": [
                "Suy ≥ 2 cơ quan (SOFA score ≥ 2 cho mỗi tạng)",
                "Các tạng thường bị:",
                "1. Phổi: ARDS, PaO2/FiO2 < 300",
                "2. Thận: AKI, creatinine tăng",
                "3. Gan: bilirubin > 2 mg/dL, ALT/AST tăng",
                "4. Tim mạch: hạ huyết áp, cần vasopressor",
                "5. Đông máu: giảm tiểu cầu, PT kéo dài",
                "6. Thần kinh: GCS < 15"
            ],
            "tests": [
                "SOFA score (đánh giá từng tạng)",
                "Chức năng thận: creatinine, BUN",
                "Chức năng gan: bilirubin, ALT, AST",
                "Đông máu: tiểu cầu, PT, aPTT",
                "Khí máu động mạch",
                "Lactate máu"
            ],
            "imaging": [
                "X-quang ngực",
                "CT (nếu cần)",
                "Siêu âm (đánh giá các tạng)"
            ]
        },
        treatment={
            "general": "Điều trị hỗ trợ từng tạng, điều trị nguyên nhân. Mục tiêu: duy trì chức năng tạng, ngăn tiến triển.",
            "medications": [
                "Điều trị nguyên nhân: kháng sinh (nếu nhiễm trùng)",
                "Hỗ trợ hô hấp: thở máy",
                "Hỗ trợ tuần hoàn: vasopressor, inotrope",
                "Hỗ trợ thận: lọc máu",
                "Hỗ trợ gan: điều trị triệu chứng",
                "Hỗ trợ đông máu: truyền tiểu cầu, huyết tương"
            ],
            "procedures": [
                "Thở máy",
                "Lọc máu",
                "ECMO (nếu cần)",
                "Hỗ trợ đa tạng",
                "Điều trị nguyên nhân"
            ]
        },
        prevention=[
            "Điều trị sớm nhiễm trùng",
            "Phòng ngừa sốc",
            "Quản lý dịch cẩn thận",
            "Phòng ngừa nhiễm trùng bệnh viện"
        ],
        complications=[
            "Tử vong (tỷ lệ rất cao: 50-80%)",
            "Tổn thương tạng vĩnh viễn",
            "Nhiễm trùng bệnh viện",
            "Chảy máu"
        ],
        related_scores=["SOFA Score", "APACHE II", "MODS Score", "Marshall Score"],
        related_drugs=["Broad-spectrum Antibiotics", "Vasopressors", "Inotropes"],
        related_protocols=["MODS Management", "Organ Support"],
        icd10_codes=["R65.2", "R65.3"]
    ),
]
