"""
Cardiology Module
Diseases: Heart Failure, MI, Hypertension, AFib, CAD, Valvular, Myocarditis, Pericarditis, DCM
"""

from typing import List
from diseases.data import Disease


CARDIOLOGY_DISEASES: List[Disease] = [
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
    
    Disease(
        id="hypertension",
        name="Hypertension",
        name_vn="Tăng huyết áp",
        category="Cardiology",
        definition="Tăng huyết áp là tình trạng huyết áp tâm thu ≥ 140 mmHg hoặc huyết áp tâm trương ≥ 90 mmHg, là bệnh phổ biến tại Việt Nam.",
        causes=[
            "Tăng huyết áp nguyên phát (90-95%): không rõ nguyên nhân",
            "Tăng huyết áp thứ phát: bệnh thận, cường aldosterone, hẹp động mạch thận, u tủy thượng thận",
            "Yếu tố nguy cơ: tuổi cao, béo phì, ít vận động, ăn mặn, rượu bia, hút thuốc, stress, tiền sử gia đình"
        ],
        symptoms=[
            "Thường không có triệu chứng (bệnh thầm lặng)",
            "Đau đầu (nếu huyết áp rất cao)",
            "Chóng mặt",
            "Mờ mắt",
            "Đánh trống ngực",
            "Khó thở (nếu có biến chứng)"
        ],
        diagnosis={
            "criteria": [
                "Huyết áp ≥ 140/90 mmHg (đo nhiều lần, nhiều lần khám)",
                "Phân loại: Tăng huyết áp độ 1 (140-159/90-99), độ 2 (160-179/100-109), độ 3 (≥180/≥110)",
                "Đánh giá tổn thương cơ quan đích: tim, thận, mắt, não"
            ],
            "tests": [
                "Đo huyết áp (nhiều lần, cả 2 tay)",
                "Công thức máu",
                "Chức năng thận (creatinine, BUN)",
                "Điện giải (Na, K)",
                "Lipid máu",
                "Đường huyết",
                "ECG",
                "Siêu âm tim (nếu cần)"
            ],
            "imaging": [
                "ECG",
                "Siêu âm tim (đánh giá phì đại thất trái)",
                "Siêu âm thận (nếu nghi ngờ nguyên nhân thận)"
            ]
        },
        treatment={
            "general": "Điều trị theo JNC 8/ACC/AHA guidelines. Mục tiêu: < 130/80 mmHg (nếu có nguy cơ tim mạch cao) hoặc < 140/90 mmHg.",
            "medications": [
                "ACE inhibitor hoặc ARB (ưu tiên nếu có đái tháo đường, bệnh thận)",
                "Thiazide diuretic (Hydrochlorothiazide, Chlorthalidone)",
                "Calcium channel blocker (Amlodipine)",
                "Beta-blocker (nếu có chỉ định khác)",
                "Kết hợp 2-3 thuốc nếu cần"
            ],
            "procedures": [
                "Thay đổi lối sống: giảm muối, giảm cân, tập thể dục",
                "Theo dõi huyết áp tại nhà",
                "Điều trị nguyên nhân (nếu tăng huyết áp thứ phát)"
            ]
        },
        prevention=[
            "Chế độ ăn ít muối (< 5g/ngày)",
            "Giảm cân (nếu thừa cân)",
            "Tập thể dục đều đặn",
            "Hạn chế rượu bia",
            "Bỏ thuốc lá",
            "Quản lý stress"
        ],
        complications=[
            "Bệnh tim mạch: nhồi máu cơ tim, suy tim, đột quỵ",
            "Bệnh thận mạn tính",
            "Bệnh võng mạc",
            "Bệnh mạch máu ngoại vi",
            "Tăng huyết áp ác tính (hiếm)"
        ],
        related_scores=["Blood Pressure", "Framingham Risk Score", "ASCVD Risk"],
        related_drugs=["ACE Inhibitor", "ARB", "Amlodipine", "Hydrochlorothiazide", "Metoprolol"],
        related_protocols=["Hypertension Management"],
        icd10_codes=["I10", "I11.9", "I12.9", "I13.9"]
    ),
    
    Disease(
        id="atrial_fibrillation",
        name="Atrial Fibrillation",
        name_vn="Rung nhĩ",
        category="Cardiology",
        definition="Rung nhĩ là rối loạn nhịp tim phổ biến nhất, đặc trưng bởi nhịp tim không đều, nhanh, do rối loạn hoạt động điện của tâm nhĩ.",
        causes=[
            "Bệnh tim: bệnh mạch vành, suy tim, bệnh van tim",
            "Tăng huyết áp",
            "Bệnh phổi mạn tính",
            "Cường giáp",
            "Rượu bia",
            "Tuổi cao",
            "Vô căn (lone AF)"
        ],
        symptoms=[
            "Đánh trống ngực",
            "Khó thở",
            "Mệt mỏi",
            "Choáng váng, ngất",
            "Đau ngực",
            "Có thể không có triệu chứng"
        ],
        diagnosis={
            "criteria": [
                "ECG: không có sóng P, nhịp không đều, tần số nhanh (100-180/phút)",
                "Phân loại: paroxysmal (< 7 ngày, tự hết), persistent (> 7 ngày), permanent (không thể chuyển nhịp)"
            ],
            "tests": [
                "ECG (12 chuyển đạo)",
                "Holter ECG (24-48h) nếu cần",
                "Siêu âm tim (đánh giá chức năng tim, kích thước nhĩ trái)",
                "TSH (loại trừ cường giáp)",
                "Chức năng thận (để tính liều thuốc chống đông)"
            ],
            "imaging": [
                "ECG",
                "Siêu âm tim",
                "Holter ECG"
            ]
        },
        treatment={
            "general": "Điều trị theo AHA/ACC/HRS guidelines. Mục tiêu: kiểm soát nhịp/tần số, chống đông, phòng ngừa biến chứng.",
            "medications": [
                "Chống đông: Warfarin, DOAC (Dabigatran, Rivaroxaban, Apixaban) - theo CHA2DS2-VASc score",
                "Kiểm soát tần số: Beta-blocker, Diltiazem, Verapamil, Digoxin",
                "Chuyển nhịp: Amiodarone, Flecainide, Propafenone (nếu phù hợp)",
                "Chống loạn nhịp: Amiodarone, Sotalol"
            ],
            "procedures": [
                "Cardioversion (chuyển nhịp bằng sốc điện hoặc thuốc)",
                "Ablation (đốt điện) - nếu phù hợp",
                "Đặt pacemaker (nếu cần)"
            ]
        },
        prevention=[
            "Kiểm soát huyết áp",
            "Điều trị bệnh tim",
            "Hạn chế rượu bia",
            "Điều trị cường giáp",
            "Chống đông (nếu có chỉ định)"
        ],
        complications=[
            "Đột quỵ (nguy cơ cao nhất)",
            "Suy tim",
            "Nhồi máu cơ tim",
            "Tử vong"
        ],
        related_scores=["CHA2DS2-VASc", "HAS-BLED"],
        related_drugs=["Warfarin", "Dabigatran", "Rivaroxaban", "Apixaban", "Amiodarone", "Metoprolol"],
        related_protocols=["Atrial Fibrillation Management"],
        icd10_codes=["I48.0", "I48.1", "I48.9"]
    ),
    
    Disease(
        id="coronary_artery_disease",
        name="Coronary Artery Disease",
        name_vn="Bệnh mạch vành",
        category="Cardiology",
        definition="Bệnh mạch vành là tình trạng hẹp hoặc tắc nghẽn động mạch vành do xơ vữa động mạch, dẫn đến thiếu máu cơ tim.",
        causes=[
            "Xơ vữa động mạch",
            "Yếu tố nguy cơ: tăng huyết áp, đái tháo đường, rối loạn lipid máu, hút thuốc, béo phì, ít vận động, tuổi cao, tiền sử gia đình"
        ],
        symptoms=[
            "Đau ngực (đau thắt ngực): đau khi gắng sức, giảm khi nghỉ",
            "Khó thở khi gắng sức",
            "Mệt mỏi",
            "Có thể không có triệu chứng (thiếu máu cơ tim thầm lặng)"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "ECG: ST chênh xuống khi gắng sức",
                "Test gắng sức: dương tính",
                "Chụp mạch vành: hẹp ≥ 50%",
                "CT mạch vành: hẹp động mạch vành"
            ],
            "tests": [
                "ECG",
                "Test gắng sức (treadmill)",
                "Siêu âm tim gắng sức",
                "Chụp mạch vành (Coronary angiography) - chuẩn vàng",
                "CT mạch vành (nếu phù hợp)"
            ],
            "imaging": [
                "ECG",
                "Siêu âm tim",
                "Chụp mạch vành",
                "CT mạch vành"
            ]
        },
        treatment={
            "general": "Điều trị theo ACC/AHA guidelines. Mục tiêu: giảm triệu chứng, phòng ngừa nhồi máu cơ tim, cải thiện tiên lượng.",
            "medications": [
                "Aspirin 75-100mg",
                "Statin (Atorvastatin 40-80mg)",
                "Beta-blocker (nếu có chỉ định)",
                "ACE inhibitor (nếu có suy tim, đái tháo đường)",
                "Nitrate (nếu đau ngực)",
                "Clopidogrel (nếu đặt stent)"
            ],
            "procedures": [
                "PCI (Percutaneous Coronary Intervention) - đặt stent",
                "CABG (Coronary Artery Bypass Graft) - nếu phù hợp"
            ]
        },
        prevention=[
            "Kiểm soát các yếu tố nguy cơ",
            "Aspirin",
            "Statin",
            "Chế độ ăn lành mạnh",
            "Tập thể dục",
            "Bỏ thuốc lá"
        ],
        complications=[
            "Nhồi máu cơ tim",
            "Suy tim",
            "Rối loạn nhịp tim",
            "Đột tử",
            "Tử vong"
        ],
        related_scores=["TIMI Risk Score", "GRACE Score", "Framingham Risk Score"],
        related_drugs=["Aspirin", "Atorvastatin", "Clopidogrel", "ACE Inhibitor", "Beta-blocker"],
        related_protocols=["Stable Angina", "ACS - Hội chứng vành cấp"],
        icd10_codes=["I25.9", "I25.1", "I25.10"]
    ),
    
    Disease(
        id="valvular_heart_disease",
        name="Valvular Heart Disease",
        name_vn="Bệnh van tim",
        category="Cardiology",
        definition="Bệnh van tim là tình trạng tổn thương van tim (hẹp hoặc hở), ảnh hưởng đến dòng máu qua tim.",
        causes=[
            "Hẹp van hai lá: thấp tim (phổ biến tại Việt Nam), vôi hóa",
            "Hở van hai lá: sa van, thấp tim, nhồi máu cơ tim",
            "Hẹp van động mạch chủ: vôi hóa (người già), thấp tim",
            "Hở van động mạch chủ: giãn động mạch chủ, viêm nội tâm mạc",
            "Bệnh van ba lá: thường do tăng áp phổi"
        ],
        symptoms=[
            "Khó thở (khi gắng sức, tiến triển)",
            "Mệt mỏi",
            "Đau ngực",
            "Ngất (nếu hẹp van động mạch chủ nặng)",
            "Phù chân",
            "Đánh trống ngực"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Tiếng thổi tim",
                "Siêu âm tim: đánh giá mức độ hẹp/hở, chức năng tim",
                "ECG: dấu hiệu phì đại tâm thất"
            ],
            "tests": [
                "Siêu âm tim (Echocardiography) - chuẩn vàng",
                "ECG",
                "X-quang ngực",
                "Chụp mạch vành (nếu cần phẫu thuật)"
            ],
            "imaging": [
                "Siêu âm tim",
                "ECG",
                "X-quang ngực",
                "CT tim (nếu cần)"
            ]
        },
        treatment={
            "general": "Điều trị theo AHA/ACC guidelines. Mục tiêu: giảm triệu chứng, phòng ngừa biến chứng, phẫu thuật khi có chỉ định.",
            "medications": [
                "Lợi tiểu (nếu suy tim)",
                "ACE inhibitor (nếu hở van, suy tim)",
                "Beta-blocker (nếu hẹp van động mạch chủ)",
                "Kháng sinh dự phòng (nếu có chỉ định)",
                "Chống đông (nếu rung nhĩ)"
            ],
            "procedures": [
                "Phẫu thuật thay/sửa van (nếu có chỉ định)",
                "Nong van bằng bóng (nếu hẹp van hai lá)",
                "TAVI (Transcatheter Aortic Valve Implantation) - nếu hẹp van động mạch chủ, nguy cơ cao"
            ]
        },
        prevention=[
            "Điều trị thấp tim (phòng ngừa)",
            "Kháng sinh dự phòng (nếu có chỉ định)",
            "Kiểm soát huyết áp",
            "Theo dõi định kỳ"
        ],
        complications=[
            "Suy tim",
            "Rối loạn nhịp tim (rung nhĩ)",
            "Viêm nội tâm mạc",
            "Đột tử",
            "Tử vong"
        ],
        related_scores=["Valve Area", "Gradient", "Ejection Fraction"],
        related_drugs=["Furosemide", "ACE Inhibitor", "Warfarin", "Amiodarone"],
        related_protocols=["Valvular Heart Disease Management"],
        icd10_codes=["I05.9", "I06.9", "I08.9", "I34.1", "I35.9"]
    ),
    
    Disease(
        id="myocarditis",
        name="Myocarditis",
        name_vn="Viêm cơ tim",
        category="Cardiology",
        definition="Viêm cơ tim là tình trạng viêm cơ tim, thường do virus, có thể dẫn đến suy tim, rối loạn nhịp tim.",
        causes=[
            "Virus: Coxsackie B, Adenovirus, Parvovirus B19, COVID-19",
            "Vi khuẩn: Streptococcus, Staphylococcus",
            "Nấm, ký sinh trùng",
            "Thuốc: một số thuốc hóa trị",
            "Tự miễn: lupus, viêm khớp dạng thấp"
        ],
        symptoms=[
            "Đau ngực",
            "Khó thở",
            "Mệt mỏi",
            "Sốt",
            "Đánh trống ngực",
            "Phù chân",
            "Có thể không có triệu chứng"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Troponin tăng",
                "Siêu âm tim: rối loạn vận động, giảm EF",
                "MRI tim: tăng tín hiệu T2, late gadolinium enhancement",
                "Sinh thiết cơ tim (nếu cần)"
            ],
            "tests": [
                "Troponin, CK-MB",
                "CRP, ESR",
                "Siêu âm tim",
                "MRI tim (nếu có)",
                "Sinh thiết cơ tim (nếu cần)"
            ],
            "imaging": [
                "Siêu âm tim",
                "MRI tim",
                "ECG"
            ]
        },
        treatment={
            "general": "Điều trị hỗ trợ. Nghỉ ngơi, điều trị suy tim, rối loạn nhịp tim. Hầu hết tự khỏi.",
            "medications": [
                "ACE inhibitor (nếu suy tim)",
                "Beta-blocker (nếu suy tim, rối loạn nhịp)",
                "Lợi tiểu (nếu suy tim)",
                "Corticosteroid (nếu tự miễn)",
                "Kháng virus (nếu có chỉ định)"
            ],
            "procedures": [
                "Nghỉ ngơi (quan trọng)",
                "Thở máy (nếu suy hô hấp)",
                "Lọc máu (nếu suy thận)",
                "Ghép tim (nếu nặng, không đáp ứng)"
            ]
        },
        prevention=[
            "Tiêm vắc xin",
            "Vệ sinh tay",
            "Tránh tiếp xúc với người bệnh",
            "Điều trị nhiễm trùng sớm"
        ],
        complications=[
            "Suy tim",
            "Rối loạn nhịp tim",
            "Giãn cơ tim",
            "Đột tử",
            "Tử vong"
        ],
        related_scores=["Ejection Fraction", "Troponin"],
        related_drugs=["ACE Inhibitor", "Beta-blocker", "Furosemide", "Prednisone"],
        related_protocols=[],
        icd10_codes=["I40.9", "I40.0", "I40.1"]
    ),
    
    Disease(
        id="pericarditis",
        name="Pericarditis",
        name_vn="Viêm màng ngoài tim",
        category="Cardiology",
        definition="Viêm màng ngoài tim là tình trạng viêm màng ngoài tim, thường gây đau ngực, có thể có tràn dịch màng ngoài tim.",
        causes=[
            "Virus: Coxsackie, Echovirus, Adenovirus, COVID-19",
            "Vi khuẩn: lao (phổ biến tại Việt Nam), vi khuẩn khác",
            "Ung thư",
            "Sau nhồi máu cơ tim (Dressler syndrome)",
            "Tự miễn: lupus, viêm khớp dạng thấp",
            "Vô căn"
        ],
        symptoms=[
            "Đau ngực (đau nhói, tăng khi nằm, giảm khi ngồi cúi người)",
            "Sốt",
            "Khó thở",
            "Mệt mỏi",
            "Ho"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Tiếng cọ màng ngoài tim",
                "ECG: ST chênh lên lan tỏa, PR chênh xuống",
                "Siêu âm tim: tràn dịch màng ngoài tim",
                "Tăng CRP, ESR"
            ],
            "tests": [
                "ECG",
                "Siêu âm tim",
                "CRP, ESR",
                "Troponin (có thể tăng nhẹ)",
                "X-quang ngực"
            ],
            "imaging": [
                "ECG",
                "Siêu âm tim",
                "X-quang ngực",
                "CT ngực (nếu cần)"
            ]
        },
        treatment={
            "general": "Điều trị theo nguyên nhân. Mục tiêu: giảm đau, giảm viêm, phòng ngừa biến chứng.",
            "medications": [
                "NSAID: Ibuprofen, Aspirin (2-4 tuần)",
                "Colchicine (3 tháng) - giảm tái phát",
                "Corticosteroid (nếu kháng NSAID hoặc tự miễn)",
                "Kháng sinh (nếu vi khuẩn)",
                "Điều trị lao (nếu lao)"
            ],
            "procedures": [
                "Chọc dò màng ngoài tim (nếu tràn dịch nhiều, ép tim)",
                "Cắt màng ngoài tim (nếu viêm màng ngoài tim co thắt)"
            ]
        },
        prevention=[
            "Điều trị nhiễm trùng sớm",
            "Điều trị lao",
            "Theo dõi sau nhồi máu cơ tim"
        ],
        complications=[
            "Chèn ép tim (cardiac tamponade)",
            "Viêm màng ngoài tim co thắt",
            "Tái phát",
            "Tử vong (nếu chèn ép tim)"
        ],
        related_scores=["Pericardial Effusion", "Tamponade"],
        related_drugs=["Ibuprofen", "Aspirin", "Colchicine", "Prednisone"],
        related_protocols=[],
        icd10_codes=["I30.9", "I30.0", "I30.1"]
    ),
    
    Disease(
        id="dilated_cardiomyopathy",
        name="Dilated Cardiomyopathy",
        name_vn="Bệnh cơ tim giãn",
        category="Cardiology",
        definition="Bệnh cơ tim giãn là tình trạng giãn và suy giảm chức năng tâm thất, dẫn đến suy tim.",
        causes=[
            "Vô căn (không rõ nguyên nhân)",
            "Sau viêm cơ tim",
            "Di truyền",
            "Rượu bia",
            "Thuốc: hóa trị (doxorubicin)",
            "Bệnh mạch vành",
            "Tăng huyết áp lâu ngày"
        ],
        symptoms=[
            "Khó thở (khi gắng sức, khi nằm)",
            "Mệt mỏi",
            "Phù chân",
            "Đánh trống ngực",
            "Ho",
            "Giảm khả năng gắng sức"
        ],
        diagnosis={
            "criteria": [
                "Triệu chứng lâm sàng",
                "Siêu âm tim: giãn tâm thất, EF giảm (< 40%)",
                "X-quang ngực: bóng tim to",
                "Loại trừ nguyên nhân: bệnh mạch vành, bệnh van tim"
            ],
            "tests": [
                "Siêu âm tim - chuẩn vàng",
                "ECG",
                "X-quang ngực",
                "Chụp mạch vành (loại trừ bệnh mạch vành)",
                "MRI tim (nếu cần)"
            ],
            "imaging": [
                "Siêu âm tim",
                "ECG",
                "X-quang ngực",
                "MRI tim"
            ]
        },
        treatment={
            "general": "Điều trị suy tim. Mục tiêu: cải thiện chức năng tim, giảm triệu chứng, phòng ngừa đột tử.",
            "medications": [
                "ACE inhibitor hoặc ARB",
                "Beta-blocker",
                "ARNI (nếu phù hợp)",
                "SGLT2 inhibitor",
                "Lợi tiểu (nếu phù)",
                "Digoxin (nếu cần)",
                "Spironolactone (nếu EF < 35%)"
            ],
            "procedures": [
                "Đặt ICD (nếu EF < 35%)",
                "CRT (nếu có block nhánh)",
                "Ghép tim (nếu nặng)"
            ]
        },
        prevention=[
            "Tránh rượu bia",
            "Điều trị viêm cơ tim sớm",
            "Kiểm soát huyết áp",
            "Theo dõi định kỳ"
        ],
        complications=[
            "Suy tim nặng",
            "Rối loạn nhịp tim",
            "Đột tử",
            "Huyết khối",
            "Tử vong"
        ],
        related_scores=["Ejection Fraction", "NYHA Class"],
        related_drugs=["ACE Inhibitor", "Beta-blocker", "ARNI", "SGLT2 inhibitor", "Furosemide"],
        related_protocols=["Heart Failure Management"],
        icd10_codes=["I42.0", "I42.9"]
    ),
]
