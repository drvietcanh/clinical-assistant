"""
Configuration file for all scoring systems
Defines available calculators organized by specialty
"""

SCORES_BY_SPECIALTY = {
    "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)": {
        "NEWS2": {"name": "NEWS2 - National Early Warning Score 2", "desc": "Hệ thống cảnh báo sớm cho bệnh nhân nội trú (DÙNG HÀNG NGÀY)", "status": "✅"},
        "qSOFA": {"name": "qSOFA - Quick SOFA", "desc": "Sàng lọc nhiễm trùng huyết", "status": "✅"},
        "SOFA": {"name": "SOFA - Sequential Organ Failure Assessment", "desc": "Đánh giá suy cơ quan", "status": "✅"},
        "SOFA-2 (2025)": {"name": "SOFA-2 (2025) ⭐", "desc": "SOFA cập nhật 2025 - HFNC, ECMO, RRT, vasopressor mới", "status": "✅"},
        "APACHE II": {"name": "APACHE II", "desc": "Dự đoán tử vong ICU", "status": "✅"},
        "SAPS II": {"name": "SAPS II - Simplified Acute Physiology Score", "desc": "Độ nặng bệnh nhân ICU", "status": "✅"},
        "MODS": {"name": "MODS - Multiple Organ Dysfunction Score", "desc": "Rối loạn đa cơ quan", "status": "✅"},
    },
    
    "❤️ Tim mạch (Cardiology)": {
        "ASCVD Risk": {"name": "ASCVD Risk Calculator ⭐", "desc": "Nguy cơ tim mạch 10 năm - ACC/AHA Pooled Cohort Equations (THAY THẾ FRAMINGHAM)", "status": "✅"},
        "NYHA": {"name": "NYHA Classification", "desc": "Phân loại chức năng suy tim (DÙNG HÀNG NGÀY)", "status": "✅"},
        "Killip": {"name": "Killip Classification", "desc": "Suy tim cấp trong AMI (DÙNG HÀNG NGÀY)", "status": "✅"},
        "Duke": {"name": "Duke Criteria", "desc": "Chẩn đoán viêm nội tâm mạc", "status": "✅"},
        "CHA2DS2-VASc": {"name": "CHA₂DS₂-VASc", "desc": "Nguy cơ đột quỵ trong rung nhĩ", "status": "✅"},
        "HAS-BLED": {"name": "HAS-BLED", "desc": "Nguy cơ chảy máu khi dùng kháng đông", "status": "✅"},
        "SCORE2": {"name": "SCORE2", "desc": "Nguy cơ tim mạch 10 năm (40-69 tuổi)", "status": "✅"},
        "SCORE2-OP": {"name": "SCORE2-OP", "desc": "Nguy cơ tim mạch (≥70 tuổi)", "status": "✅"},
        "HEART Score": {"name": "HEART Score", "desc": "Đau ngực cấp - nguy cơ ACS", "status": "✅"},
        "TIMI Risk": {"name": "TIMI Risk Score", "desc": "Nguy cơ NSTEMI/STEMI", "status": "✅"},
        "GRACE Score": {"name": "GRACE Score", "desc": "Tiên lượng ACS", "status": "✅"},
        "Framingham": {"name": "Framingham Risk Score", "desc": "Nguy cơ tim mạch 10 năm (Historical)", "status": "✅"},
        "Corrected QT": {"name": "QTc - Corrected QT Interval", "desc": "QT điều chỉnh theo nhịp tim", "status": "✅"},
    },
    
    "🫁 Hô hấp (Respiratory)": {
        "PERC": {"name": "PERC Rule", "desc": "Loại trừ PE không cần D-dimer (DÙNG HÀNG NGÀY)", "status": "✅"},
        "CURB-65": {"name": "CURB-65", "desc": "Mức độ nặng viêm phổi", "status": "✅"},
        "PSI/PORT": {"name": "PSI/PORT Score", "desc": "Tiên lượng viêm phổi cộng đồng", "status": "✅"},
        "Wells PE": {"name": "Wells PE Score", "desc": "Nguy cơ thuyên tắc phổi", "status": "✅"},
        "PESI": {"name": "PESI - Pulmonary Embolism Severity Index", "desc": "Mức độ nặng và tiên lượng thuyên tắc phổi", "status": "✅"},
        "SMART-COP": {"name": "SMART-COP", "desc": "Cần hỗ trợ hô hấp trong viêm phổi", "status": "✅"},
        "BODE Index": {"name": "BODE Index", "desc": "Tiên lượng COPD", "status": "✅"},
        "ARDS Berlin": {"name": "ARDS Berlin Definition", "desc": "Tiêu chuẩn chẩn đoán ARDS (Berlin 2012)", "status": "✅"},
    },
    
    "🧠 Thần kinh (Neurology)": {
        "GCS": {"name": "GCS - Glasgow Coma Scale", "desc": "Mức độ ý thức", "status": "✅"},
        "NIHSS": {"name": "NIHSS - NIH Stroke Scale", "desc": "Mức độ nặng đột quỵ", "status": "✅"},
        "ICH Score": {"name": "ICH Score", "desc": "Tiên lượng xuất huyết nội sọ", "status": "✅"},
        "Hunt & Hess": {"name": "Hunt & Hess Scale", "desc": "Phân loại xuất huyết dưới nhện", "status": "✅"},
        "mRS": {"name": "mRS - Modified Rankin Scale", "desc": "Mức độ khuyết tật sau đột quỵ", "status": "✅"},
        "ASPECTS": {"name": "ASPECTS - Alberta Stroke Program Early CT Score", "desc": "Đánh giá thay đổi thiếu máu sớm trên CT - Quyết định thrombolysis/thrombectomy", "status": "✅"},
        "ABCD2": {"name": "ABCD2 Score", "desc": "Phân tầng nguy cơ đột quỵ sau TIA", "status": "✅"},
        "Barthel Index": {"name": "Barthel Index", "desc": "Đánh giá chức năng hoạt động hàng ngày (ADL)", "status": "✅"},
    },
    
    "🩸 Tiêu Hóa - Gan Mật (GI/Hepatology)": {
        "BISAP": {"name": "BISAP Score", "desc": "Tiên lượng viêm tụy cấp (DÙNG HÀNG NGÀY)", "status": "✅"},
        "Child-Pugh": {"name": "Child-Pugh Score", "desc": "Mức độ xơ gan", "status": "✅"},
        "MELD": {"name": "MELD Score", "desc": "Tiên lượng bệnh gan mạn & ghép gan", "status": "✅"},
        "Glasgow-Blatchford": {"name": "Glasgow-Blatchford Score", "desc": "UGIB - quyết định xuất viện", "status": "✅"},
        "Rockall Score": {"name": "Rockall Score", "desc": "UGIB - tiên lượng tử vong", "status": "✅"},
        "MELD-Na": {"name": "MELD-Na", "desc": "MELD điều chỉnh theo Na", "status": "✅"},
        "Ranson": {"name": "Ranson Criteria", "desc": "Tiên lượng viêm tụy cấp", "status": "✅"},
    },
    
    "🩺 Huyết Học & Đông máu (Hematology)": {
        "Padua": {"name": "Padua Prediction Score", "desc": "Nguy cơ VTE - Chỉ định prophylaxis (DÙNG HÀNG NGÀY)", "status": "✅"},
        "Wells DVT": {"name": "Wells DVT Score", "desc": "Nguy cơ huyết khối tĩnh mạch sâu", "status": "✅"},
        "4Ts Score": {"name": "4Ts Score - HIT", "desc": "Giảm tiểu cầu do heparin", "status": "✅"},
        "DIC Score": {"name": "DIC Score (ISTH)", "desc": "Đông máu rải rác trong lòng mạch", "status": "✅"},
    },
    
    "🧪 Thận - Điện Giải (Nephrology)": {
        "eGFR": {"name": "eGFR - CKD-EPI & MDRD", "desc": "Tính tốc độ lọc cầu thận (DÙNG HÀNG NGÀY)", "status": "✅"},
        "KDIGO": {"name": "KDIGO Staging", "desc": "Giai đoạn AKI (Tiêu chuẩn hiện đại)", "status": "✅"},
        "RIFLE": {"name": "RIFLE Criteria", "desc": "Phân loại AKI (Historical)", "status": "✅"},
        "AKIN": {"name": "AKIN Criteria", "desc": "Suy thận cấp (Historical)", "status": "✅"},
    },
    
    "🦴 Chấn Thương & Chỉnh Hình (Trauma/Orthopedics)": {
        "RTS": {"name": "RTS - Revised Trauma Score", "desc": "Tiên lượng chấn thương (sinh lý)", "status": "✅"},
        "ISS": {"name": "ISS - Injury Severity Score", "desc": "Mức độ nặng đa chấn thương (giải phẫu)", "status": "✅"},
        "NEXUS": {"name": "NEXUS C-Spine", "desc": "Cần chụp X-quang cột sống cổ", "status": "✅"},
        "Canadian C-Spine": {"name": "Canadian C-Spine Rule", "desc": "Chỉ định chụp cột sống cổ", "status": "✅"},
    },
    
    "👂 Tai Mũi Họng (ENT)": {
        "Epworth": {"name": "Epworth Sleepiness Scale", "desc": "Đánh giá buồn ngủ ban ngày", "status": "✅"},
        "STOP-BANG": {"name": "STOP-BANG Score", "desc": "Sàng lọc OSA", "status": "✅"},
    },
    
    "👶 Nhi Khoa (Pediatrics)": {
        "Westley Croup": {"name": "Westley Croup Score", "desc": "Mức độ nặng croup (DÙNG HÀNG NGÀY)", "status": "✅"},
        "PEWS": {"name": "PEWS - Pediatric Early Warning Score", "desc": "Cảnh báo sớm nhi", "status": "✅"},
        "APGAR": {"name": "APGAR Score", "desc": "Đánh giá trẻ sơ sinh", "status": "✅"},
        "Pediatric GCS": {"name": "Pediatric GCS", "desc": "Ý thức trẻ em", "status": "✅"},
        "PELOD-2": {"name": "PELOD-2 - Pediatric Logistic Organ Dysfunction", "desc": "Suy đa cơ quan ICU nhi", "status": "✅"},
        "PRISM III": {"name": "PRISM III - Pediatric Risk of Mortality", "desc": "Nguy cơ tử vong ICU nhi", "status": "✅"},
        "Pediatric SOFA": {"name": "Pediatric SOFA (pSOFA)", "desc": "Suy đa cơ quan ICU nhi - Điều chỉnh theo tuổi", "status": "✅"},
    },
    
    "🤰 Sản Khoa (Obstetrics)": {
        "Preeclampsia": {"name": "Preeclampsia Severity", "desc": "Mức độ nặng tiền sản giật (DÙNG HÀNG NGÀY)", "status": "✅"},
        "Bishop Score": {"name": "Bishop Score", "desc": "Đánh giá cổ tử cung", "status": "✅"},
        "Modified Bishop": {"name": "Modified Bishop Score", "desc": "Dự đoán chuyển dạ", "status": "✅"},
    },
    
    "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)": {
        "CrCl": {"name": "CrCl - Cockcroft-Gault", "desc": "Độ thanh thải Creatinine - Điều chỉnh liều thuốc (DÙNG HÀNG NGÀY)", "status": "✅"},
        "BMI/IBW/BSA": {"name": "BMI | IBW | BSA", "desc": "Chỉ số cơ thể - BMI, Cân nặng lý tưởng, Diện tích da (DÙNG HÀNG NGÀY)", "status": "✅"},
        "Osmolality": {"name": "Serum Osmolality & Gap", "desc": "Độ thẩm thấu - Nghi ngờ ngộ độc (DÙNG HÀNG NGÀY)", "status": "✅"},
        "Anion Gap": {"name": "Anion Gap", "desc": "Khoảng trống anion - rối loạn acid-base", "status": "✅"},
        "Corrected Ca": {"name": "Corrected Calcium", "desc": "Canxi điều chỉnh theo albumin", "status": "✅"},
        "FENa": {"name": "FENa - Fractional Excretion of Sodium", "desc": "Phân biệt AKI tiền thận/thận", "status": "✅"},
        "HbA1c": {"name": "HbA1c - eAG Converter", "desc": "Chuyển đổi HbA1c sang đường huyết trung bình", "status": "✅"},
        "Winter Formula": {"name": "Winter Formula", "desc": "PCO2 dự đoán trong toan chuyển hóa", "status": "✅"},
        "Free T4 Index": {"name": "Free T4 Index (FTI)", "desc": "Chỉ số T4 tự do", "status": "✅"},
    },
    
    "🦴 Thấp Khớp - Miễn Dịch (Rheumatology/Immunology)": {
        "DAS28": {"name": "DAS28 - Disease Activity Score", "desc": "Hoạt động bệnh viêm khớp dạng thấp", "status": "✅"},
        "CDAI": {"name": "CDAI - Clinical Disease Activity Index", "desc": "Chỉ số hoạt động lâm sàng RA", "status": "✅"},
        "SDAI": {"name": "SDAI - Simplified Disease Activity Index", "desc": "Chỉ số đơn giản hóa RA", "status": "✅"},
        "ACR Criteria": {"name": "ACR/EULAR RA Classification", "desc": "Tiêu chuẩn chẩn đoán viêm khớp dạng thấp", "status": "✅"},
        "SLICC": {"name": "SLICC Criteria", "desc": "Tiêu chuẩn lupus ban đỏ hệ thống", "status": "✅"},
        "SLEDAI": {"name": "SLEDAI - SLE Disease Activity Index", "desc": "Hoạt động bệnh lupus", "status": "✅"},
        "Gout Diagnostic": {"name": "ACR/EULAR Gout Classification", "desc": "Chẩn đoán bệnh gout", "status": "✅"},
    },
    
    "🦠 Nhiễm khuẩn (Infectious Disease)": {
        "SIRS": {"name": "SIRS - Systemic Inflammatory Response", "desc": "Hội chứng đáp ứng viêm toàn thân", "status": "✅"},
        "Pitt Bacteremia": {"name": "Pitt Bacteremia Score", "desc": "Tiên lượng nhiễm khuẩn huyết", "status": "✅"},
        "MASCC": {"name": "MASCC Risk Index", "desc": "Nguy cơ sốt giảm bạch cầu hạt", "status": "✅"},
        "Centor": {"name": "Centor Score", "desc": "Viêm họng do liên cầu", "status": "✅"},
        "FeverPAIN": {"name": "FeverPAIN Score", "desc": "Viêm amidan - cần kháng sinh", "status": "✅"},
    },
    
    "🩹 Da Liễu (Dermatology)": {
        "PASI": {"name": "PASI - Psoriasis Area Severity Index", "desc": "Mức độ nặng vẩy nến", "status": "✅"},
        "SCORAD": {"name": "SCORAD - SCORing Atopic Dermatitis", "desc": "Điểm viêm da cơ địa", "status": "✅"},
        "DLQI": {"name": "DLQI - Dermatology Life Quality Index", "desc": "Chất lượng cuộc sống bệnh da", "status": "✅"},
        "Burn TBSA": {"name": "TBSA - Total Body Surface Area", "desc": "Diện tích bỏng (quy tắc số 9)", "status": "✅"},
        "Parkland Formula": {"name": "Parkland Formula", "desc": "Truyền dịch ban đầu cho bỏng", "status": "✅"},
    },
    
    "🎗️ Ung thư (Oncology)": {
        "ECOG": {"name": "ECOG Performance Status", "desc": "Trạng thái thể trạng bệnh nhân ung thư", "status": "✅"},
        "Karnofsky": {"name": "Karnofsky Performance Scale", "desc": "Thang đo thể trạng", "status": "✅"},
        "Palliative Performance": {"name": "PPS - Palliative Performance Scale", "desc": "Thể trạng chăm sóc giảm nhẹ", "status": "✅"},
        "CIPN Grading": {"name": "CIPN Grading", "desc": "Phân độ tổn thương thần kinh ngoại biên", "status": "✅"},
    },
    
    "🧠 Tâm Thần - Tâm Lý (Psychiatry/Psychology)": {
        "PHQ-9": {"name": "PHQ-9 - Patient Health Questionnaire", "desc": "Sàng lọc trầm cảm", "status": "✅"},
        "GAD-7": {"name": "GAD-7 - Generalized Anxiety Disorder", "desc": "Rối loạn lo âu lan tỏa", "status": "✅"},
        "MMSE": {"name": "MMSE - Mini Mental State Exam", "desc": "Đánh giá nhận thức", "status": "✅"},
        "MoCA": {"name": "MoCA - Montreal Cognitive Assessment", "desc": "Đánh giá nhận thức Montreal", "status": "✅"},
        "CAM": {"name": "CAM - Confusion Assessment Method", "desc": "Đánh giá hôn mê lú lẫn", "status": "✅"},
        "CIWA-Ar": {"name": "CIWA-Ar", "desc": "Cai rượu - mức độ nặng", "status": "✅"},
        "COWS": {"name": "COWS - Clinical Opiate Withdrawal", "desc": "Cai opioid", "status": "✅"},
    },
    
    "🔪 Phẫu Thuật & Gây Mê (Surgery/Anesthesia)": {
        "ASA": {"name": "ASA Physical Status", "desc": "Phân loại nguy cơ phẫu thuật", "status": "✅"},
        "P-POSSUM": {"name": "P-POSSUM Score", "desc": "Nguy cơ tử vong phẫu thuật", "status": "✅"},
        "RCRI": {"name": "RCRI - Revised Cardiac Risk Index", "desc": "Nguy cơ tim mạch phẫu thuật", "status": "✅"},
        "Caprini": {"name": "Caprini VTE Risk Score", "desc": "Nguy cơ huyết khối sau phẫu thuật", "status": "✅"},
        "Aldrete Score": {"name": "Aldrete Score", "desc": "Hồi tỉnh sau gây mê", "status": "✅"},
        "Mallampati": {"name": "Mallampati Classification", "desc": "Đánh giá đường thở khó", "status": "✅"},
    },
    
    "👁️ Mắt (Ophthalmology)": {
        "Intraocular Pressure": {"name": "IOP Correction", "desc": "Điều chỉnh nhãn áp theo CCT", "status": "✅"},
    },
    
    "😣 Đánh giá đau (Pain Assessment)": {
        "NRS": {"name": "NRS - Numeric Rating Scale", "desc": "Thang điểm số đánh giá đau (0-10) - DÙNG HÀNG NGÀY", "status": "✅"},
        "VAS": {"name": "VAS - Visual Analogue Scale", "desc": "Thang đo thị giác đánh giá đau (0-100mm)", "status": "✅"},
        "FLACC": {"name": "FLACC - Face, Legs, Activity, Cry, Consolability", "desc": "Đánh giá đau ở trẻ em (2 tháng - 7 tuổi)", "status": "✅"},
        "NIPS": {"name": "NIPS - Neonatal Infant Pain Scale", "desc": "Đánh giá đau ở trẻ sơ sinh (0-2 tháng)", "status": "✅"},
        "Wong-Baker": {"name": "Wong-Baker Faces Rating Scale", "desc": "Thang điểm khuôn mặt đánh giá đau (trẻ em và người lớn)", "status": "✅"},
        "DN4": {"name": "DN4 - Douleur Neuropathique 4", "desc": "Chẩn đoán đau thần kinh", "status": "✅"},
    },
    
    "🛏️ Chăm sóc điều dưỡng (Nursing Care)": {
        "Braden": {"name": "Braden Scale", "desc": "Đánh giá nguy cơ loét tì đè (DÙNG HÀNG NGÀY)", "status": "✅"},
        "Morse": {"name": "Morse Fall Scale", "desc": "Đánh giá nguy cơ té ngã (DÙNG HÀNG NGÀY)", "status": "✅"},
    },
}

