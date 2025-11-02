"""
Calculator Registry
All available calculators in the Clinical Assistant system
"""

ALL_CALCULATORS = {
    # Scores - Cardiology
    "cha2ds2vasc": {"name": "CHA₂DS₂-VASc", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "hasbled": {"name": "HAS-BLED", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "score2": {"name": "SCORE2", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "score2_op": {"name": "SCORE2-OP", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "heart": {"name": "HEART Score", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "timi": {"name": "TIMI", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "grace": {"name": "GRACE", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "framingham": {"name": "Framingham", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    
    # Scores - Emergency
    "qsofa": {"name": "qSOFA", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "sofa": {"name": "SOFA", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "sofa2": {"name": "SOFA-2 (2025)", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "apache2": {"name": "APACHE II", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "saps2": {"name": "SAPS II", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "mods": {"name": "MODS", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    
    # Scores - Respiratory
    "curb65": {"name": "CURB-65", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "psi_port": {"name": "PSI/PORT", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "wells_pe": {"name": "Wells PE", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "smartcop": {"name": "SMART-COP", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    
    # Scores - Neurology
    "gcs": {"name": "GCS", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "nihss": {"name": "NIHSS", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "ich_score": {"name": "ICH Score", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "hunt_hess": {"name": "Hunt & Hess", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "mrs": {"name": "mRS", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    
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

