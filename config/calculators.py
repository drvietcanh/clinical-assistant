"""
Calculator Registry
All available calculators in the Clinical Assistant system
"""

ALL_CALCULATORS = {
    # Scores - Cardiology
    "ascvd": {"name": "ASCVD Risk Calculator", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "nyha": {"name": "NYHA Classification", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "killip": {"name": "Killip Classification", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "duke": {"name": "Duke Criteria", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "cha2ds2vasc": {
        "name": "CHA₂DS₂-VASc", 
        "category": "Tim mạch", 
        "icon": "❤️", 
        "page": "Scores",
        "reference": "Lip GY, et al. Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation using a novel risk factor-based approach: the euro heart survey on atrial fibrillation. Chest. 2010;137(2):263-72."
    },
    "hasbled": {"name": "HAS-BLED", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "score2": {"name": "SCORE2", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "score2_op": {"name": "SCORE2-OP", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "heart": {"name": "HEART Score", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "timi": {"name": "TIMI", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "grace": {"name": "GRACE", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "framingham": {"name": "Framingham", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "qtc": {"name": "QTc - Corrected QT Interval", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "arc_hbr": {"name": "ARC-HBR", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "crusade": {"name": "Crusade", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "dapt_score": {"name": "DAPT Score", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "pcp_hf": {"name": "PCP-HF", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "precise_dapt": {"name": "Precise Dapt", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "hfa_icos_anthracycline": {"name": "HFA-ICOS Anthracycline", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "hfa_icos_cml": {"name": "HFA-ICOS CML", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "hfa_icos_her2": {"name": "HFA-ICOS HER2", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "hfa_icos_multiple_myeloma": {"name": "HFA-ICOS Multiple Myeloma", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "hfa_icos_raf_mek": {"name": "HFA-ICOS RAF/MEK", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    "hfa_icos_vegf": {"name": "HFA-ICOS VEGF", "category": "Tim mạch", "icon": "❤️", "page": "Scores"},
    
    # Scores - Emergency
    "news2": {"name": "NEWS2", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "mews": {"name": "MEWS - Modified Early Warning Score", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "qsofa": {"name": "qSOFA", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "sofa": {
        "name": "SOFA", 
        "category": "Cấp cứu", 
        "icon": "🚨", 
        "page": "Scores",
        "reference": "Singer M, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-10."
    },
    "sofa2": {"name": "SOFA-2 (2025)", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "apache2": {"name": "APACHE II", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "apache3": {"name": "APACHE III", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "saps2": {"name": "SAPS II", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "saps3": {"name": "SAPS III", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "mods": {"name": "MODS", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "lods": {"name": "LODS", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "hospital_score": {"name": "HOSPITAL Score", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "lace_index": {"name": "LACE Index", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "alvarado": {"name": "Alvarado", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "apache4": {"name": "APACHE IV", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "charlson": {"name": "Charlson", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "crb65": {"name": "CRB-65", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "lactate_clearance": {"name": "Lactate Clearance", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "rdos": {"name": "RDOS", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "rox_index": {"name": "ROX Index", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    "scorten": {"name": "SCORTEN", "category": "Cấp cứu", "icon": "🚨", "page": "Scores"},
    
    # Scores - Respiratory
    "perc": {"name": "PERC Rule", "category": "Hô hấp", "icon": "🫁", "page": "Scores"},
    "curb65": {
        "name": "CURB-65", 
        "category": "Hô hấp", 
        "icon": "🫁", 
        "page": "Scores",
        "reference": "Lim WS, et al. Defining community acquired pneumonia severity on presentation to hospital: an international derivation and validation study. Thorax. 2003;58(5):377-82."
    },
    "psi_port": {"name": "PSI/PORT", "category": "Hô hấp", "icon": "🫁", "page": "Scores"},
    "wells_pe": {"name": "Wells PE", "category": "Hô hấp", "icon": "🫁", "page": "Scores"},
    "smartcop": {"name": "SMART-COP", "category": "Hô hấp", "icon": "🫁", "page": "Scores"},
    "bode": {"name": "BODE Index", "category": "Hô hấp", "icon": "🫁", "page": "Scores"},
    "ards_berlin": {"name": "ARDS Berlin Definition", "category": "Hô hấp", "icon": "🫁", "page": "Scores"},
    "pesi": {"name": "PESI", "category": "Hô hấp", "icon": "🫁", "page": "Scores"},
    "act": {"name": "ACT - Asthma Control Test", "category": "Hô hấp", "icon": "🫁", "page": "Scores"},
    "mmrc": {"name": "mMRC", "category": "Hô hấp", "icon": "🫁", "page": "Scores"},
    
    # Scores - Neurology
    "gcs": {"name": "GCS", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "nihss": {"name": "NIHSS", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "ich_score": {"name": "ICH Score", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "hunt_hess": {"name": "Hunt & Hess", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "mrs": {"name": "mRS", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "aspects": {"name": "ASPECTS", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "abcd2": {"name": "ABCD2", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "barthel": {"name": "Barthel Index", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "four_score": {"name": "FOUR Score", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "canadian_ct_head": {"name": "Canadian Ct Head", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "fast_ed": {"name": "FAST-ED", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "icans": {"name": "ICANS", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "ice_score": {"name": "ICE Score", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "mg_adl": {"name": "MG-ADL", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "mgfa": {"name": "MGFA", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "sudbury_vertigo": {"name": "Sudbury Vertigo", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    "canadian_stroke_scale": {"name": "Canadian Stroke Scale", "category": "Thần kinh", "icon": "🧠", "page": "Scores"},
    
    # Scores - GI/Hepatology
    "bisap": {"name": "BISAP Score", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "child_pugh": {"name": "Child-Pugh Score", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "meld": {"name": "MELD Score", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "meld_na": {"name": "MELD-Na", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "ranson": {"name": "Ranson Criteria", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "rockall": {"name": "Rockall Score", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "glasgow_blatchford": {"name": "Glasgow-Blatchford Score", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "aims65": {"name": "AIMS65 Score", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "acute_pancreatitis": {"name": "Acute Pancreatitis", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "erefs": {"name": "Erefs", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "fib4": {"name": "FIB-4", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "safe_score": {"name": "SAFE Score", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    "lactulose_calculator": {"name": "Lactulose Calculator", "category": "Tiêu hóa", "icon": "🩸", "page": "Scores"},
    
    # Scores - Nephrology
    "egfr": {"name": "eGFR - CKD-EPI & MDRD", "category": "Thận", "icon": "🧪", "page": "Scores"},
    "kdigo": {"name": "KDIGO Staging", "category": "Thận", "icon": "🧪", "page": "Scores"},
    "rifle": {"name": "RIFLE Criteria", "category": "Thận", "icon": "🧪", "page": "Scores"},
    "akin": {"name": "AKIN Criteria", "category": "Thận", "icon": "🧪", "page": "Scores"},
    "egfr_bsa": {"name": "eGFR with BSA", "category": "Thận", "icon": "🧪", "page": "Scores"},
    "dialysis_adequacy": {"name": "Dialysis Adequacy Calculator", "category": "Thận", "icon": "🧪", "page": "Scores"},
    
    # Scores - Hematology
    "padua": {"name": "Padua Prediction Score", "category": "Huyết học", "icon": "🩺", "page": "Scores"},
    "wells_dvt": {"name": "Wells DVT Score", "category": "Huyết học", "icon": "🩺", "page": "Scores"},
    "four_ts": {"name": "4Ts Score - HIT", "category": "Huyết học", "icon": "🩺", "page": "Scores"},
    "dic_score": {"name": "DIC Score (ISTH)", "category": "Huyết học", "icon": "🩺", "page": "Scores"},
    "warfarin_dosing": {"name": "Warfarin Dosing Calculator", "category": "Huyết học", "icon": "🩺", "page": "Scores"},
    "inr_target": {"name": "INR Target Calculator", "category": "Huyết học", "icon": "🩺", "page": "Scores"},
    "bleeding_risk": {"name": "Bleeding Risk Calculator", "category": "Huyết học", "icon": "🩺", "page": "Scores"},
    
    # Scores - Trauma
    "rts": {"name": "RTS - Revised Trauma Score", "category": "Chấn thương", "icon": "🦴", "page": "Scores"},
    "iss": {"name": "ISS - Injury Severity Score", "category": "Chấn thương", "icon": "🦴", "page": "Scores"},
    "nexus": {"name": "NEXUS C-Spine", "category": "Chấn thương", "icon": "🦴", "page": "Scores"},
    "canadian_cspine": {"name": "Canadian C-Spine Rule", "category": "Chấn thương", "icon": "🦴", "page": "Scores"},
    "triss": {"name": "TRISS", "category": "Chấn thương", "icon": "🦴", "page": "Scores"},
    
    # Scores - Pediatrics
    "apgar": {"name": "APGAR Score", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "pews": {"name": "PEWS - Pediatric Early Warning Score", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "pediatric_gcs": {"name": "Pediatric GCS", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "westley_croup": {"name": "Westley Croup Score", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "pelod2": {"name": "PELOD-2", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "prism3": {"name": "PRISM III", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "pim2": {"name": "PIM2 - Pediatric Index of Mortality 2", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "pediatric_sofa": {"name": "Pediatric SOFA", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "dhaka": {"name": "Dhaka", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "pecarn": {"name": "PECARN", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    "pediatric_dosing": {"name": "Pediatric Dosing", "category": "Nhi khoa", "icon": "👶", "page": "Scores"},
    
    # Scores - Surgery/Anesthesia
    "asa": {"name": "ASA Physical Status", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "aldrete": {"name": "Aldrete Score", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "mallampati": {"name": "Mallampati Classification", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "rcri": {"name": "RCRI - Revised Cardiac Risk Index", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "caprini": {"name": "Caprini VTE Risk Score", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "possum": {"name": "P-POSSUM Score", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "apfel_ponv": {"name": "Apfel Ponv", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "ariscat": {"name": "Ariscat", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "cam_icu": {"name": "Cam Icu", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "clavien_dindo": {"name": "Clavien Dindo", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "cormack_lehane": {"name": "Cormack Lehane", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "el_ganzouri": {"name": "El Ganzouri", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "four_at": {"name": "Four At", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "goldman_cardiac": {"name": "Goldman Cardiac", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "gupta_cardiac": {"name": "Gupta Cardiac", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "koivuranta_ponv": {"name": "Koivuranta Ponv", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "lemon": {"name": "Lemon", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "padss": {"name": "Padss", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "perioperative_anticoagulation": {"name": "Perioperative Anticoagulation", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "ramsay": {"name": "Ramsay", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "rass": {"name": "Rass", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "rhmp30": {"name": "Rhmp30", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "riker_sas": {"name": "Riker Sas", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "sort": {"name": "Sort", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "surgical_apgar": {"name": "Surgical Apgar", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "wifi": {"name": "Wifi", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    "wilson_risk": {"name": "Wilson Risk", "category": "Phẫu thuật", "icon": "🔪", "page": "Scores"},
    
    # Scores - Rheumatology
    "das28": {"name": "DAS28 - Disease Activity Score", "category": "Thấp khớp", "icon": "🦴", "page": "Scores"},
    "cdai": {"name": "CDAI - Clinical Disease Activity Index", "category": "Thấp khớp", "icon": "🦴", "page": "Scores"},
    "sdai": {"name": "SDAI - Simplified Disease Activity Index", "category": "Thấp khớp", "icon": "🦴", "page": "Scores"},
    "acr_ra": {"name": "ACR/EULAR RA Classification", "category": "Thấp khớp", "icon": "🦴", "page": "Scores"},
    "slicc": {"name": "SLICC Criteria", "category": "Thấp khớp", "icon": "🦴", "page": "Scores"},
    "sledai": {"name": "SLEDAI - SLE Disease Activity Index", "category": "Thấp khớp", "icon": "🦴", "page": "Scores"},
    "gout": {"name": "ACR/EULAR Gout Classification", "category": "Thấp khớp", "icon": "🦴", "page": "Scores"},
    
    # Scores - Psychiatry
    "phq9": {"name": "PHQ-9 - Patient Health Questionnaire", "category": "Tâm thần", "icon": "🧠", "page": "Scores"},
    "gad7": {"name": "GAD-7 - Generalized Anxiety Disorder", "category": "Tâm thần", "icon": "🧠", "page": "Scores"},
    "mmse": {"name": "MMSE - Mini Mental State Exam", "category": "Tâm thần", "icon": "🧠", "page": "Scores"},
    "moca": {"name": "MoCA - Montreal Cognitive Assessment", "category": "Tâm thần", "icon": "🧠", "page": "Scores"},
    "cam": {"name": "CAM - Confusion Assessment Method", "category": "Tâm thần", "icon": "🧠", "page": "Scores"},
    "ciwa": {"name": "CIWA-Ar", "category": "Tâm thần", "icon": "🧠", "page": "Scores"},
    "cows": {"name": "COWS - Clinical Opiate Withdrawal", "category": "Tâm thần", "icon": "🧠", "page": "Scores"},
    "gmaws": {"name": "GMAWS", "category": "Tâm thần", "icon": "🧠", "page": "Scores"},
    
    # Scores - Dermatology
    "pasi": {"name": "PASI - Psoriasis Area Severity Index", "category": "Da liễu", "icon": "🩹", "page": "Scores"},
    "scorad": {"name": "SCORAD - SCORing Atopic Dermatitis", "category": "Da liễu", "icon": "🩹", "page": "Scores"},
    "dlqi": {"name": "DLQI - Dermatology Life Quality Index", "category": "Da liễu", "icon": "🩹", "page": "Scores"},
    "burn_tbsa": {"name": "TBSA - Total Body Surface Area", "category": "Da liễu", "icon": "🩹", "page": "Scores"},
    "parkland": {"name": "Parkland Formula", "category": "Da liễu", "icon": "🩹", "page": "Scores"},
    
    # Scores - Oncology
    "ecog": {"name": "ECOG Performance Status", "category": "Ung thư", "icon": "🎗️", "page": "Scores"},
    "karnofsky": {"name": "Karnofsky Performance Scale", "category": "Ung thư", "icon": "🎗️", "page": "Scores"},
    "pps": {"name": "PPS - Palliative Performance Scale", "category": "Ung thư", "icon": "🎗️", "page": "Scores"},
    "cipn": {"name": "CIPN Grading", "category": "Ung thư", "icon": "🎗️", "page": "Scores"},
    "mskcc_rcc": {"name": "MSKCC RCC", "category": "Ung thư", "icon": "🎗️", "page": "Scores"},
    
    # Scores - Obstetrics
    "preeclampsia": {"name": "Preeclampsia Severity", "category": "Sản khoa", "icon": "🤰", "page": "Scores"},
    "bishop": {"name": "Bishop Score", "category": "Sản khoa", "icon": "🤰", "page": "Scores"},
    "modified_bishop": {"name": "Modified Bishop Score", "category": "Sản khoa", "icon": "🤰", "page": "Scores"},
    
    # Scores - ENT
    "epworth": {"name": "Epworth Sleepiness Scale", "category": "Tai mũi họng", "icon": "👂", "page": "Scores"},
    "stop_bang": {"name": "STOP-BANG Score", "category": "Tai mũi họng", "icon": "👂", "page": "Scores"},
    
    # Scores - Ophthalmology
    "iop_correction": {"name": "IOP Correction", "category": "Mắt", "icon": "👁️", "page": "Scores"},
    
    # Scores - Pain Assessment
    "nrs": {"name": "NRS - Numeric Rating Scale", "category": "Đánh giá đau", "icon": "😣", "page": "Scores"},
    "vas": {"name": "VAS - Visual Analog Scale", "category": "Đánh giá đau", "icon": "😣", "page": "Scores"},
    "flacc": {"name": "FLACC", "category": "Đánh giá đau", "icon": "😣", "page": "Scores"},
    "nips": {"name": "NIPS - Neonatal Infant Pain Scale", "category": "Đánh giá đau", "icon": "😣", "page": "Scores"},
    "wong_baker": {"name": "Wong-Baker Faces Scale", "category": "Đánh giá đau", "icon": "😣", "page": "Scores"},
    "dn4": {"name": "DN4 - Neuropathic Pain", "category": "Đánh giá đau", "icon": "😣", "page": "Scores"},
    
    # Scores - Nursing Care
    "braden": {"name": "Braden Scale", "category": "Điều dưỡng", "icon": "🩺", "page": "Scores"},
    "morse": {"name": "Morse Fall Scale", "category": "Điều dưỡng", "icon": "🩺", "page": "Scores"},
    
    # Scores - Metabolism/Endocrinology
    "crcl": {"name": "CrCl - Cockcroft-Gault", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "bmi_ibw_bsa": {"name": "BMI | IBW | BSA", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "osmolality": {"name": "Serum Osmolality & Gap", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "anion_gap": {"name": "Anion Gap", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "corrected_calcium": {"name": "Corrected Calcium", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "fena": {"name": "FENa - Fractional Excretion of Sodium", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "hba1c_eag": {"name": "HbA1c - eAG Converter", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "winter_formula": {"name": "Winter Formula", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "free_t4_index": {"name": "Free T4 Index (FTI)", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "findrisc": {"name": "FINDRISC", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "frax_risk": {"name": "FRAX Risk", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "free_water_deficit": {"name": "Free Water Deficit", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "homa_ir": {"name": "HOMA-IR", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "levothyroxine_dose": {"name": "Levothyroxine Dose", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "maintenance_fluids": {"name": "Maintenance Fluids", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "map": {"name": "Map", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "osteoporosis_dxa": {"name": "Osteoporosis Dxa", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    "sodium_correction_hyperglycemia": {"name": "Sodium Correction Hyperglycemia", "category": "Nội tiết", "icon": "💉", "page": "Scores"},
    
    # Scores - Infectious Disease
    "sirs": {"name": "SIRS - Systemic Inflammatory Response", "category": "Nhiễm khuẩn", "icon": "🦠", "page": "Scores"},
    "pitt_bacteremia": {"name": "Pitt Bacteremia Score", "category": "Nhiễm khuẩn", "icon": "🦠", "page": "Scores"},
    "mascc": {"name": "MASCC Risk Index", "category": "Nhiễm khuẩn", "icon": "🦠", "page": "Scores"},
    "centor": {"name": "Centor Score", "category": "Nhiễm khuẩn", "icon": "🦠", "page": "Scores"},
    "feverpain": {"name": "FeverPAIN Score", "category": "Nhiễm khuẩn", "icon": "🦠", "page": "Scores"},
    
    # Labs
    "cbc": {"name": "CBC", "category": "Xét nghiệm", "icon": "🔬", "page": "Labs"},
    "bmp": {"name": "BMP", "category": "Xét nghiệm", "icon": "🔬", "page": "Labs"},
    "cmp": {"name": "CMP", "category": "Xét nghiệm", "icon": "🔬", "page": "Labs"},
    "lft": {"name": "LFT", "category": "Xét nghiệm", "icon": "🔬", "page": "Labs"},
    "lipid": {"name": "Lipid Panel", "category": "Xét nghiệm", "icon": "🔬", "page": "Labs"},
    "cardiac_markers": {"name": "Cardiac Markers", "category": "Xét nghiệm", "icon": "🔬", "page": "Labs"},
    "coag": {"name": "Coagulation", "category": "Xét nghiệm", "icon": "🔬", "page": "Labs"},
    "thyroid": {"name": "Thyroid", "category": "Xét nghiệm", "icon": "🔬", "page": "Labs"},
    "abg": {"name": "ABG", "category": "Xét nghiệm", "icon": "🔬", "page": "Labs"},
    
    # Ventilator
    "ardsnet": {"name": "ARDSNet Calculator", "category": "Thở máy", "icon": "🫁", "page": "Ventilator"},
    "peep_fio2": {"name": "PEEP/FiO2 Table", "category": "Thở máy", "icon": "🫁", "page": "Ventilator"},
    
    # Protocols
    "sepsis": {"name": "Sepsis Bundle", "category": "Phác đồ", "icon": "📋", "page": "Protocols"},
    "copd": {"name": "COPD", "category": "Phác đồ", "icon": "📋", "page": "Protocols"},
    "asthma": {"name": "Asthma", "category": "Phác đồ", "icon": "📋", "page": "Protocols"},
    "acs": {"name": "ACS", "category": "Phác đồ", "icon": "📋", "page": "Protocols"},
    "heart_failure": {"name": "Heart Failure", "category": "Phác đồ", "icon": "📋", "page": "Protocols"},
}

