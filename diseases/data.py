"""
Disease Encyclopedia Database
Comprehensive information about common diseases and conditions
"""

from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class Disease:
    """Disease information"""
    id: str
    name: str
    name_vn: str  # Vietnamese name
    category: str  # Cardiology, Infectious, etc.
    definition: str = ""
    causes: List[str] = field(default_factory=list)
    symptoms: List[str] = field(default_factory=list)
    diagnosis: dict = field(default_factory=dict)  # {"criteria": [], "tests": [], "imaging": []}
    treatment: dict = field(default_factory=dict)  # {"general": "", "medications": [], "procedures": []}
    prevention: List[str] = field(default_factory=list)
    complications: List[str] = field(default_factory=list)
    related_scores: List[str] = field(default_factory=list)  # e.g., ["CURB-65", "PSI"]
    related_drugs: List[str] = field(default_factory=list)  # e.g., ["Amoxicillin", "Azithromycin"]
    related_protocols: List[str] = field(default_factory=list)  # e.g., ["pneumonia_treatment"]
    icd10_codes: List[str] = field(default_factory=list)  # e.g., ["J18.9", "J15.9"]


# Diseases Database
# Starting with 50-100 common diseases
DISEASES_DATABASE: List[Disease] = [
    # === INFECTIOUS DISEASES ===
    Disease(
        id="pneumonia",
        name="Pneumonia",
        name_vn="Viêm phổi",
        category="Infectious",
        definition="Viêm phổi là tình trạng nhiễm trùng cấp tính của nhu mô phổi, gây ra bởi vi khuẩn, virus, nấm hoặc các tác nhân khác.",
        causes=[
            "Vi khuẩn: Streptococcus pneumoniae (phổ biến nhất), Haemophilus influenzae, Staphylococcus aureus",
            "Virus: Influenza, RSV, COVID-19",
            "Nấm: Pneumocystis jirovecii (ở bệnh nhân suy giảm miễn dịch)",
            "Các yếu tố nguy cơ: Tuổi cao, suy giảm miễn dịch, bệnh phổi mạn tính, hút thuốc"
        ],
        symptoms=[
            "Sốt, ớn lạnh",
            "Ho có đờm (đờm vàng/xanh, có thể có máu)",
            "Khó thở, thở nhanh",
            "Đau ngực (tăng khi ho hoặc thở sâu)",
            "Mệt mỏi, suy nhược",
            "Ở người già: có thể chỉ có lú lẫn, mệt mỏi"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng: sốt, ho, đờm, khó thở",
                "Khám phổi: ran nổ, giảm rì rào phế nang",
                "X-quang ngực: thâm nhiễm phổi",
                "Xét nghiệm: tăng bạch cầu, CRP, procalcitonin"
            ],
            "tests": [
                "Công thức máu (CBC)",
                "CRP, Procalcitonin",
                "Cấy đờm (nếu có)",
                "Cấy máu (nếu sốt cao, nghi ngờ nhiễm khuẩn huyết)",
                "Xét nghiệm virus (nếu nghi ngờ)"
            ],
            "imaging": [
                "X-quang ngực thẳng",
                "CT ngực (nếu cần thiết)"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân và mức độ nặng. Hầu hết bệnh nhân có thể điều trị ngoại trú.",
            "medications": [
                "CAP (Viêm phổi cộng đồng): Amoxicillin, Azithromycin, Levofloxacin",
                "HAP (Viêm phổi bệnh viện): Piperacillin-tazobactam, Ceftazidime, Meropenem",
                "Hỗ trợ: Hạ sốt (Paracetamol), Giảm ho, Oxy nếu cần"
            ],
            "procedures": [
                "Oxy liệu pháp nếu SpO2 < 90%",
                "Thở máy nếu suy hô hấp nặng",
                "Dẫn lưu mủ nếu có áp xe phổi"
            ]
        },
        prevention=[
            "Tiêm vắc xin phế cầu (Pneumovax 23, Prevnar 13)",
            "Tiêm vắc xin cúm hàng năm",
            "Bỏ thuốc lá",
            "Rửa tay thường xuyên"
        ],
        complications=[
            "Áp xe phổi",
            "Tràn dịch màng phổi",
            "Nhiễm khuẩn huyết",
            "Suy hô hấp",
            "ARDS (Hội chứng suy hô hấp cấp)"
        ],
        related_scores=["CURB-65", "PSI (Pneumonia Severity Index)"],
        related_drugs=["Amoxicillin", "Azithromycin", "Levofloxacin", "Ceftriaxone"],
        related_protocols=["Viêm phổi cộng đồng (CAP)"],
        icd10_codes=["J18.9", "J15.9", "J12.9"]
    ),
    
    Disease(
        id="sepsis",
        name="Sepsis",
        name_vn="Nhiễm khuẩn huyết / Sepsis",
        category="Infectious",
        definition="Sepsis là phản ứng của cơ thể đối với nhiễm trùng, gây ra rối loạn chức năng cơ quan đe dọa tính mạng.",
        causes=[
            "Nhiễm trùng: vi khuẩn, virus, nấm",
            "Nguồn nhiễm trùng phổ biến: phổi, đường tiết niệu, da, ổ bụng",
            "Yếu tố nguy cơ: tuổi cao, suy giảm miễn dịch, bệnh mạn tính"
        ],
        symptoms=[
            "Sốt hoặc hạ thân nhiệt",
            "Nhịp tim nhanh (>90/phút)",
            "Thở nhanh (>20/phút)",
            "Thay đổi ý thức (lú lẫn, kích động)",
            "Hạ huyết áp (sốc nhiễm khuẩn)",
            "Giảm lượng nước tiểu"
        ],
        diagnosis={
            "criteria": [
                "SOFA score ≥ 2 hoặc qSOFA ≥ 2",
                "Nhiễm trùng đã biết hoặc nghi ngờ",
                "Tăng lactate máu",
                "Tăng procalcitonin, CRP"
            ],
            "tests": [
                "Công thức máu (CBC)",
                "Lactate máu",
                "Procalcitonin, CRP",
                "Cấy máu (2 bộ, trước khi dùng kháng sinh)",
                "Cấy từ nguồn nhiễm trùng",
                "Chức năng thận, gan"
            ],
            "imaging": [
                "X-quang ngực",
                "CT scan (nếu cần tìm nguồn nhiễm trùng)",
                "Siêu âm ổ bụng"
            ]
        },
        treatment={
            "general": "Điều trị khẩn cấp với 1-hour bundle: kháng sinh sớm, bù dịch, vận mạch nếu cần.",
            "medications": [
                "Kháng sinh phổ rộng sớm (trong 1 giờ): Piperacillin-tazobactam, Meropenem",
                "Vận mạch: Norepinephrine (nếu sốc)",
                "Corticosteroid: Hydrocortisone (nếu sốc kháng trị)"
            ],
            "procedures": [
                "Bù dịch tĩnh mạch (30ml/kg trong 3 giờ đầu)",
                "Đặt catheter tĩnh mạch trung tâm",
                "Thở máy nếu suy hô hấp",
                "Lọc máu nếu suy thận"
            ]
        },
        prevention=[
            "Tiêm vắc xin",
            "Vệ sinh tay",
            "Chăm sóc vết thương đúng cách",
            "Điều trị nhiễm trùng sớm"
        ],
        complications=[
            "Sốc nhiễm khuẩn",
            "Suy đa tạng (MODS)",
            "ARDS",
            "Suy thận cấp",
            "Tử vong"
        ],
        related_scores=["SOFA", "qSOFA", "SIRS"],
        related_drugs=["Piperacillin-tazobactam", "Meropenem", "Vancomycin", "Norepinephrine"],
        related_protocols=["Sepsis 1-Hour Bundle", "Sepsis 3-Hour Bundle"],
        icd10_codes=["A41.9", "A41.51", "A41.52"]
    ),
    
    # === CARDIOLOGY ===
    Disease(
        id="heart_failure",
        name="Heart Failure",
        name_vn="Suy tim",
        category="Cardiology",
        definition="Suy tim là tình trạng tim không bơm đủ máu để đáp ứng nhu cầu của cơ thể.",
        causes=[
            "Bệnh mạch vành (nhồi máu cơ tim)",
            "Tăng huyết áp",
            "Bệnh van tim",
            "Bệnh cơ tim",
            "Rối loạn nhịp tim",
            "Bệnh tim bẩm sinh"
        ],
        symptoms=[
            "Khó thở (khi gắng sức, khi nằm - orthopnea)",
            "Mệt mỏi, suy nhược",
            "Phù chân, mắt cá chân",
            "Tăng cân (do ứ dịch)",
            "Ho khan, đặc biệt khi nằm",
            "Nhịp tim nhanh, đánh trống ngực"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "BNP hoặc NT-proBNP tăng",
                "Siêu âm tim: EF giảm, rối loạn vận động vùng",
                "X-quang ngực: bóng tim to, phù phổi"
            ],
            "tests": [
                "BNP hoặc NT-proBNP",
                "Troponin (nếu nghi ngờ nhồi máu)",
                "Chức năng thận, điện giải",
                "TSH (loại trừ suy giáp)"
            ],
            "imaging": [
                "Siêu âm tim (Echocardiography)",
                "X-quang ngực",
                "ECG"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân và mức độ. Mục tiêu: giảm triệu chứng, cải thiện chức năng tim, giảm tử vong.",
            "medications": [
                "ACE inhibitor hoặc ARB (nếu không dung nạp)",
                "Beta-blocker (Metoprolol, Bisoprolol)",
                "ARNI (Sacubitril/Valsartan) cho HFrEF",
                "SGLT2 inhibitor (Dapagliflozin, Empagliflozin)",
                "Lợi tiểu (Furosemide) cho phù",
                "Digoxin (nếu rung nhĩ)"
            ],
            "procedures": [
                "Đặt ICD (nếu EF < 35%)",
                "CRT (Cardiac Resynchronization Therapy)",
                "Ghép tim (nếu nặng)"
            ]
        },
        prevention=[
            "Kiểm soát huyết áp",
            "Điều trị bệnh mạch vành",
            "Bỏ thuốc lá",
            "Chế độ ăn ít muối",
            "Tập thể dục đều đặn"
        ],
        complications=[
            "Suy tim cấp",
            "Rối loạn nhịp tim",
            "Đột tử",
            "Suy thận",
            "Tử vong"
        ],
        related_scores=["NYHA Class", "BNP", "NT-proBNP"],
        related_drugs=["ACE Inhibitor", "ARB", "Beta-blocker", "ARNI", "SGLT2 inhibitor", "Furosemide"],
        related_protocols=["Suy tim Cấp", "Suy tim Mất Bù Cấp (ADHF)"],
        icd10_codes=["I50.9", "I50.1", "I50.2", "I50.3"]
    ),
    
    Disease(
        id="myocardial_infarction",
        name="Acute Myocardial Infarction",
        name_vn="Nhồi máu cơ tim cấp",
        category="Cardiology",
        definition="Nhồi máu cơ tim cấp là tình trạng hoại tử cơ tim do tắc nghẽn động mạch vành.",
        causes=[
            "Tắc nghẽn động mạch vành do huyết khối",
            "Xơ vữa động mạch",
            "Co thắt động mạch vành",
            "Yếu tố nguy cơ: tăng huyết áp, đái tháo đường, hút thuốc, rối loạn lipid máu"
        ],
        symptoms=[
            "Đau ngực (đau thắt, đè ép, lan ra cánh tay trái, hàm)",
            "Khó thở",
            "Vã mồ hôi",
            "Buồn nôn, nôn",
            "Choáng váng, ngất"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "ECG: ST chênh lên (STEMI) hoặc ST chênh xuống/T đảo (NSTEMI)",
                "Troponin tăng",
                "Siêu âm tim: rối loạn vận động vùng"
            ],
            "tests": [
                "Troponin I hoặc T (tăng trong 3-4 giờ)",
                "CK-MB",
                "Công thức máu, chức năng thận",
                "Lipid máu"
            ],
            "imaging": [
                "ECG (12 chuyển đạo)",
                "Siêu âm tim",
                "Chụp mạch vành (Coronary angiography)"
            ]
        },
        treatment={
            "general": "Điều trị khẩn cấp: tái tưới máu sớm (PCI hoặc thrombolysis), thuốc chống đông, chống kết tập tiểu cầu.",
            "medications": [
                "Aspirin 325mg (nhai)",
                "Clopidogrel hoặc Ticagrelor",
                "Atorvastatin 80mg",
                "ACE inhibitor",
                "Beta-blocker (nếu không chống chỉ định)",
                "Thrombolysis (nếu không có PCI)"
            ],
            "procedures": [
                "PCI (Percutaneous Coronary Intervention) - ưu tiên",
                "CABG (Coronary Artery Bypass Graft) - nếu phù hợp",
                "Thrombolysis - nếu không có PCI"
            ]
        },
        prevention=[
            "Kiểm soát các yếu tố nguy cơ",
            "Aspirin (nếu có chỉ định)",
            "Statin",
            "Chế độ ăn lành mạnh",
            "Tập thể dục"
        ],
        complications=[
            "Rối loạn nhịp tim (rung thất, block AV)",
            "Suy tim",
            "Vỡ tim",
            "Huyết khối trong tim",
            "Tử vong"
        ],
        related_scores=["TIMI Risk Score", "GRACE Score"],
        related_drugs=["Aspirin", "Clopidogrel", "Ticagrelor", "Atorvastatin", "ACE Inhibitor"],
        related_protocols=["STEMI (ST-Elevation Myocardial Infarction)", "NSTEMI", "ACS - Hội chứng vành cấp"],
        icd10_codes=["I21.9", "I21.11", "I21.19", "I21.29"]
    ),
    
    # === RESPIRATORY ===
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
            "general": "Điều trị theo GOLD guidelines. Mục tiêu: giảm triệu chứng, giảm đợt cấp, cải thiện chất lượng cuộc sống.",
            "medications": [
                "Bronchodilator: SABA (Salbutamol), LABA (Salmeterol, Formoterol)",
                "Anticholinergic: SAMA (Ipratropium), LAMA (Tiotropium)",
                "ICS (Inhaled Corticosteroid) nếu đợt cấp thường xuyên",
                "Kháng sinh nếu đợt cấp do vi khuẩn",
                "Oxy liệu pháp nếu SpO2 < 88%"
            ],
            "procedures": [
                "Oxy liệu pháp dài hạn (LTOT)",
                "Thở máy không xâm lấn (NIV) trong đợt cấp",
                "Phẫu thuật giảm thể tích phổi (nếu phù hợp)"
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
        related_scores=["GOLD Classification", "mMRC", "CAT Score"],
        related_drugs=["Salbutamol", "Salmeterol", "Tiotropium", "Budesonide", "Prednisone"],
        related_protocols=["COPD Exacerbation"],
        icd10_codes=["J44.9", "J44.0", "J44.1"]
    ),
    
    # === ENDOCRINOLOGY ===
    Disease(
        id="diabetes_type2",
        name="Type 2 Diabetes Mellitus",
        name_vn="Đái tháo đường type 2",
        category="Endocrinology",
        definition="Đái tháo đường type 2 là rối loạn chuyển hóa đặc trưng bởi tăng đường huyết do kháng insulin và/hoặc thiếu insulin tương đối.",
        causes=[
            "Kháng insulin",
            "Thiếu insulin tương đối",
            "Yếu tố nguy cơ: béo phì, ít vận động, tiền sử gia đình, tuổi cao"
        ],
        symptoms=[
            "Tiểu nhiều (polyuria)",
            "Khát nhiều (polydipsia)",
            "Ăn nhiều (polyphagia)",
            "Sụt cân",
            "Mệt mỏi",
            "Nhìn mờ",
            "Vết thương lâu lành"
        ],
        diagnosis={
            "criteria": [
                "HbA1c ≥ 6.5%",
                "Đường huyết đói ≥ 126 mg/dL (≥ 7.0 mmol/L)",
                "Đường huyết ngẫu nhiên ≥ 200 mg/dL (≥ 11.1 mmol/L) + triệu chứng",
                "OGTT: đường huyết 2h ≥ 200 mg/dL"
            ],
            "tests": [
                "HbA1c",
                "Đường huyết đói",
                "OGTT (nếu cần)",
                "Chức năng thận",
                "Lipid máu",
                "Microalbumin niệu"
            ],
            "imaging": []
        },
        treatment={
            "general": "Điều trị đa yếu tố: kiểm soát đường huyết, huyết áp, lipid, phòng ngừa biến chứng.",
            "medications": [
                "Metformin (thuốc đầu tay)",
                "SGLT2 inhibitor (nếu có bệnh tim/thận)",
                "GLP-1 agonist (nếu có bệnh tim)",
                "DPP-4 inhibitor",
                "Sulfonylurea",
                "Insulin (nếu cần)"
            ],
            "procedures": [
                "Theo dõi đường huyết tại nhà",
                "Khám mắt định kỳ",
                "Khám bàn chân định kỳ"
            ]
        },
        prevention=[
            "Giảm cân (nếu thừa cân)",
            "Chế độ ăn lành mạnh",
            "Tập thể dục đều đặn",
            "Kiểm tra đường huyết định kỳ"
        ],
        complications=[
            "Bệnh võng mạc đái tháo đường",
            "Bệnh thận đái tháo đường",
            "Bệnh thần kinh đái tháo đường",
            "Bệnh mạch máu (bàn chân đái tháo đường)",
            "Bệnh tim mạch",
            "Nhiễm toan ceton (hiếm ở type 2)"
        ],
        related_scores=["HbA1c", "Fasting Glucose"],
        related_drugs=["Metformin", "SGLT2 inhibitor", "GLP-1 agonist", "Insulin"],
        related_protocols=[],
        icd10_codes=["E11.9", "E11.65", "E11.21", "E11.40"]
    ),
    
    # === NEPHROLOGY ===
    Disease(
        id="aki",
        name="Acute Kidney Injury",
        name_vn="Tổn thương thận cấp (AKI)",
        category="Nephrology",
        definition="AKI là tình trạng suy giảm chức năng thận đột ngột trong vài giờ đến vài ngày.",
        causes=[
            "Prerenal: Giảm tưới máu thận (mất nước, suy tim, hạ huyết áp)",
            "Renal: Tổn thương thận (viêm cầu thận, hoại tử ống thận cấp)",
            "Postrenal: Tắc nghẽn đường tiết niệu (sỏi, u)"
        ],
        symptoms=[
            "Giảm lượng nước tiểu",
            "Phù",
            "Mệt mỏi",
            "Buồn nôn, nôn",
            "Lú lẫn",
            "Khó thở (do ứ dịch)"
        ],
        diagnosis={
            "criteria": [
                "Creatinine tăng ≥ 0.3 mg/dL trong 48h",
                "Creatinine tăng ≥ 1.5 lần baseline",
                "Lượng nước tiểu < 0.5 ml/kg/h trong 6h"
            ],
            "tests": [
                "Creatinine, BUN",
                "Điện giải (Na, K)",
                "Phân tích nước tiểu",
                "Siêu âm thận"
            ],
            "imaging": [
                "Siêu âm thận",
                "CT ổ bụng (nếu nghi ngờ tắc nghẽn)"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân. Mục tiêu: phục hồi chức năng thận, điều chỉnh rối loạn điện giải.",
            "medications": [
                "Điều chỉnh rối loạn điện giải",
                "Lợi tiểu (nếu phù, suy tim)",
                "Tránh thuốc độc thận (NSAID, aminoglycoside)"
            ],
            "procedures": [
                "Bù dịch (nếu prerenal)",
                "Lọc máu (nếu nặng, ure cao, toan máu, phù phổi)"
            ]
        },
        prevention=[
            "Tránh mất nước",
            "Tránh thuốc độc thận",
            "Theo dõi chức năng thận khi dùng thuốc",
            "Điều trị sớm nhiễm trùng"
        ],
        complications=[
            "Suy thận mạn",
            "Rối loạn điện giải",
            "Toan máu",
            "Phù phổi",
            "Tử vong"
        ],
        related_scores=["RIFLE", "AKIN", "KDIGO AKI Stage"],
        related_drugs=["Furosemide", "Dopamine"],
        related_protocols=["AKI Management"],
        icd10_codes=["N17.9", "N19"]
    ),
    
    # === NEUROLOGY ===
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
]


# Category mapping
CATEGORY_MAPPING = {
    "Infectious": ["pneumonia", "sepsis"],
    "Cardiology": ["heart_failure", "myocardial_infarction"],
    "Respiratory": ["copd"],
    "Endocrinology": ["diabetes_type2"],
    "Nephrology": ["aki"],
    "Neurology": ["stroke"],
}


def get_all_diseases() -> List[Disease]:
    """Get all diseases"""
    return DISEASES_DATABASE


def get_diseases_by_category(category: str) -> List[Disease]:
    """Get diseases filtered by category"""
    if not category or category == "All":
        return DISEASES_DATABASE
    return [d for d in DISEASES_DATABASE if d.category == category]


def get_category_list() -> List[str]:
    """Get list of all categories"""
    categories = set(d.category for d in DISEASES_DATABASE)
    return sorted(list(categories))

