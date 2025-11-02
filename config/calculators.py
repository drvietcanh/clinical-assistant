"""
Calculator Registry
All available calculators in the Clinical Assistant system
"""

ALL_CALCULATORS = {
    # Scores - Cardiology
    "nyha": {"name": "NYHA Classification", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "killip": {"name": "Killip Classification", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "duke": {"name": "Duke Criteria", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "cha2ds2vasc": {"name": "CHA₂DS₂-VASc", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "hasbled": {"name": "HAS-BLED", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "score2": {"name": "SCORE2", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "score2_op": {"name": "SCORE2-OP", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "heart": {"name": "HEART Score", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "timi": {"name": "TIMI", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "grace": {"name": "GRACE", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "framingham": {"name": "Framingham", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "qtc": {"name": "QTc - Corrected QT Interval", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    
    # Scores - Emergency
    "qsofa": {"name": "qSOFA", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "sofa": {"name": "SOFA", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "sofa2": {"name": "SOFA-2 (2025)", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "apache2": {"name": "APACHE II", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "saps2": {"name": "SAPS II", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "mods": {"name": "MODS", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    
    # Scores - Respiratory
    "perc": {"name": "PERC Rule", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "curb65": {"name": "CURB-65", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "psi_port": {"name": "PSI/PORT", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "wells_pe": {"name": "Wells PE", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "smartcop": {"name": "SMART-COP", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "bode": {"name": "BODE Index", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    
    # Scores - Neurology
    "gcs": {"name": "GCS", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "nihss": {"name": "NIHSS", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "ich_score": {"name": "ICH Score", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "hunt_hess": {"name": "Hunt & Hess", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "mrs": {"name": "mRS", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    
    # Scores - GI/Hepatology
    "bisap": {"name": "BISAP Score", "category": "Tiêu Hóa", "icon": "🩸", "page": "Scores"},
    "child_pugh": {"name": "Child-Pugh Score", "category": "Tiêu Hóa", "icon": "🩸", "page": "Scores"},
    "meld": {"name": "MELD Score", "category": "Tiêu Hóa", "icon": "🩸", "page": "Scores"},
    "meld_na": {"name": "MELD-Na", "category": "Tiêu Hóa", "icon": "🩸", "page": "Scores"},
    "ranson": {"name": "Ranson Criteria", "category": "Tiêu Hóa", "icon": "🩸", "page": "Scores"},
    "rockall": {"name": "Rockall Score", "category": "Tiêu Hóa", "icon": "🩸", "page": "Scores"},
    "glasgow_blatchford": {"name": "Glasgow-Blatchford Score", "category": "Tiêu Hóa", "icon": "🩸", "page": "Scores"},
    
    # Scores - Nephrology
    "egfr": {"name": "eGFR - CKD-EPI & MDRD", "category": "Thận", "icon": "🧪", "page": "Scores"},
    "kdigo": {"name": "KDIGO Staging", "category": "Thận", "icon": "🧪", "page": "Scores"},
    "rifle": {"name": "RIFLE Criteria", "category": "Thận", "icon": "🧪", "page": "Scores"},
    "akin": {"name": "AKIN Criteria", "category": "Thận", "icon": "🧪", "page": "Scores"},
    
    # Scores - Hematology
    "padua": {"name": "Padua Prediction Score", "category": "Huyết Học", "icon": "🩺", "page": "Scores"},
    "wells_dvt": {"name": "Wells DVT Score", "category": "Huyết Học", "icon": "🩺", "page": "Scores"},
    "four_ts": {"name": "4Ts Score - HIT", "category": "Huyết Học", "icon": "🩺", "page": "Scores"},
    "dic_score": {"name": "DIC Score (ISTH)", "category": "Huyết Học", "icon": "🩺", "page": "Scores"},
    
    # Scores - Trauma
    "rts": {"name": "RTS - Revised Trauma Score", "category": "Chấn Thương", "icon": "🦴", "page": "Scores"},
    "iss": {"name": "ISS - Injury Severity Score", "category": "Chấn Thương", "icon": "🦴", "page": "Scores"},
    "nexus": {"name": "NEXUS C-Spine", "category": "Chấn Thương", "icon": "🦴", "page": "Scores"},
    "canadian_cspine": {"name": "Canadian C-Spine Rule", "category": "Chấn Thương", "icon": "🦴", "page": "Scores"},
    
    # Scores - Pediatrics
    "apgar": {"name": "APGAR Score", "category": "Nhi Khoa", "icon": "👶", "page": "Scores"},
    "pews": {"name": "PEWS - Pediatric Early Warning Score", "category": "Nhi Khoa", "icon": "👶", "page": "Scores"},
    "pediatric_gcs": {"name": "Pediatric GCS", "category": "Nhi Khoa", "icon": "👶", "page": "Scores"},
    "westley_croup": {"name": "Westley Croup Score", "category": "Nhi Khoa", "icon": "👶", "page": "Scores"},
    
    # Scores - Surgery/Anesthesia
    "asa": {"name": "ASA Physical Status", "category": "Phẫu Thuật", "icon": "🔪", "page": "Scores"},
    "aldrete": {"name": "Aldrete Score", "category": "Phẫu Thuật", "icon": "🔪", "page": "Scores"},
    "mallampati": {"name": "Mallampati Classification", "category": "Phẫu Thuật", "icon": "🔪", "page": "Scores"},
    "rcri": {"name": "RCRI - Revised Cardiac Risk Index", "category": "Phẫu Thuật", "icon": "🔪", "page": "Scores"},
    "caprini": {"name": "Caprini VTE Risk Score", "category": "Phẫu Thuật", "icon": "🔪", "page": "Scores"},
    "possum": {"name": "P-POSSUM Score", "category": "Phẫu Thuật", "icon": "🔪", "page": "Scores"},
    
    # Scores - Rheumatology
    "das28": {"name": "DAS28 - Disease Activity Score", "category": "Thấp Khớp", "icon": "🦴", "page": "Scores"},
    "cdai": {"name": "CDAI - Clinical Disease Activity Index", "category": "Thấp Khớp", "icon": "🦴", "page": "Scores"},
    "sdai": {"name": "SDAI - Simplified Disease Activity Index", "category": "Thấp Khớp", "icon": "🦴", "page": "Scores"},
    "acr_ra": {"name": "ACR/EULAR RA Classification", "category": "Thấp Khớp", "icon": "🦴", "page": "Scores"},
    "slicc": {"name": "SLICC Criteria", "category": "Thấp Khớp", "icon": "🦴", "page": "Scores"},
    "sledai": {"name": "SLEDAI - SLE Disease Activity Index", "category": "Thấp Khớp", "icon": "🦴", "page": "Scores"},
    "gout": {"name": "ACR/EULAR Gout Classification", "category": "Thấp Khớp", "icon": "🦴", "page": "Scores"},
    
    # Scores - Psychiatry
    "phq9": {"name": "PHQ-9 - Patient Health Questionnaire", "category": "Tâm Thần", "icon": "🧠", "page": "Scores"},
    "gad7": {"name": "GAD-7 - Generalized Anxiety Disorder", "category": "Tâm Thần", "icon": "🧠", "page": "Scores"},
    "mmse": {"name": "MMSE - Mini Mental State Exam", "category": "Tâm Thần", "icon": "🧠", "page": "Scores"},
    "moca": {"name": "MoCA - Montreal Cognitive Assessment", "category": "Tâm Thần", "icon": "🧠", "page": "Scores"},
    "cam": {"name": "CAM - Confusion Assessment Method", "category": "Tâm Thần", "icon": "🧠", "page": "Scores"},
    "ciwa": {"name": "CIWA-Ar", "category": "Tâm Thần", "icon": "🧠", "page": "Scores"},
    "cows": {"name": "COWS - Clinical Opiate Withdrawal", "category": "Tâm Thần", "icon": "🧠", "page": "Scores"},
    
    # Scores - Dermatology
    "pasi": {"name": "PASI - Psoriasis Area Severity Index", "category": "Da Liễu", "icon": "🩹", "page": "Scores"},
    "scorad": {"name": "SCORAD - SCORing Atopic Dermatitis", "category": "Da Liễu", "icon": "🩹", "page": "Scores"},
    "dlqi": {"name": "DLQI - Dermatology Life Quality Index", "category": "Da Liễu", "icon": "🩹", "page": "Scores"},
    "burn_tbsa": {"name": "TBSA - Total Body Surface Area", "category": "Da Liễu", "icon": "🩹", "page": "Scores"},
    "parkland": {"name": "Parkland Formula", "category": "Da Liễu", "icon": "🩹", "page": "Scores"},
    
    # Scores - Oncology
    "ecog": {"name": "ECOG Performance Status", "category": "Ung Thư", "icon": "🎗️", "page": "Scores"},
    "karnofsky": {"name": "Karnofsky Performance Scale", "category": "Ung Thư", "icon": "🎗️", "page": "Scores"},
    "pps": {"name": "PPS - Palliative Performance Scale", "category": "Ung Thư", "icon": "🎗️", "page": "Scores"},
    "cipn": {"name": "CIPN Grading", "category": "Ung Thư", "icon": "🎗️", "page": "Scores"},
    
    # Scores - Obstetrics
    "preeclampsia": {"name": "Preeclampsia Severity", "category": "Sản Khoa", "icon": "🤰", "page": "Scores"},
    "bishop": {"name": "Bishop Score", "category": "Sản Khoa", "icon": "🤰", "page": "Scores"},
    "modified_bishop": {"name": "Modified Bishop Score", "category": "Sản Khoa", "icon": "🤰", "page": "Scores"},
    
    # Scores - ENT
    "epworth": {"name": "Epworth Sleepiness Scale", "category": "Tai Mũi Họng", "icon": "👂", "page": "Scores"},
    "stop_bang": {"name": "STOP-BANG Score", "category": "Tai Mũi Họng", "icon": "👂", "page": "Scores"},
    
    # Scores - Ophthalmology
    "iop_correction": {"name": "IOP Correction", "category": "Mắt", "icon": "👁️", "page": "Scores"},
    
    # Scores - Metabolism/Endocrinology
    "crcl": {"name": "CrCl - Cockcroft-Gault", "category": "Nội Tiết", "icon": "💉", "page": "Scores"},
    "bmi_ibw_bsa": {"name": "BMI | IBW | BSA", "category": "Nội Tiết", "icon": "💉", "page": "Scores"},
    "osmolality": {"name": "Serum Osmolality & Gap", "category": "Nội Tiết", "icon": "💉", "page": "Scores"},
    "anion_gap": {"name": "Anion Gap", "category": "Nội Tiết", "icon": "💉", "page": "Scores"},
    "corrected_calcium": {"name": "Corrected Calcium", "category": "Nội Tiết", "icon": "💉", "page": "Scores"},
    "fena": {"name": "FENa - Fractional Excretion of Sodium", "category": "Nội Tiết", "icon": "💉", "page": "Scores"},
    "hba1c_eag": {"name": "HbA1c - eAG Converter", "category": "Nội Tiết", "icon": "💉", "page": "Scores"},
    "winter_formula": {"name": "Winter Formula", "category": "Nội Tiết", "icon": "💉", "page": "Scores"},
    "free_t4_index": {"name": "Free T4 Index (FTI)", "category": "Nội Tiết", "icon": "💉", "page": "Scores"},
    
    # Scores - Infectious Disease
    "sirs": {"name": "SIRS - Systemic Inflammatory Response", "category": "Nhiễm Khuẩn", "icon": "🦠", "page": "Scores"},
    "pitt_bacteremia": {"name": "Pitt Bacteremia Score", "category": "Nhiễm Khuẩn", "icon": "🦠", "page": "Scores"},
    "mascc": {"name": "MASCC Risk Index", "category": "Nhiễm Khuẩn", "icon": "🦠", "page": "Scores"},
    "centor": {"name": "Centor Score", "category": "Nhiễm Khuẩn", "icon": "🦠", "page": "Scores"},
    "feverpain": {"name": "FeverPAIN Score", "category": "Nhiễm Khuẩn", "icon": "🦠", "page": "Scores"},
    
    # Labs
    "cbc": {"name": "CBC", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "bmp": {"name": "BMP", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "cmp": {"name": "CMP", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "lft": {"name": "LFT", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "lipid": {"name": "Lipid Panel", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "cardiac_markers": {"name": "Cardiac Markers", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "coag": {"name": "Coagulation", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "thyroid": {"name": "Thyroid", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "abg": {"name": "ABG", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    
    # Ventilator
    "ardsnet": {"name": "ARDSNet Calculator", "category": "Thở Máy", "icon": "🫁", "page": "Ventilator"},
    "peep_fio2": {"name": "PEEP/FiO2 Table", "category": "Thở Máy", "icon": "🫁", "page": "Ventilator"},
    
    # Protocols
    "sepsis": {"name": "Sepsis Bundle", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
    "copd": {"name": "COPD", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
    "asthma": {"name": "Asthma", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
    "acs": {"name": "ACS", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
    "heart_failure": {"name": "Heart Failure", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
}

