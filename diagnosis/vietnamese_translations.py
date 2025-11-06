"""
Vietnamese Translations for Symptoms and Risk Factors
Mapping từ tiếng Anh sang tiếng Việt cho DDx Generator
"""

# Symptom translations
SYMPTOM_TRANSLATIONS = {
    # Chest Pain related
    "chest_pain": "Đau ngực",
    "chest_pain_retrosternal": "Đau ngực sau xương ức",
    "chest_pain_crushing": "Đau ngực kiểu đè ép",
    "chest_pain_pleuritic": "Đau ngực kiểu màng phổi",
    "chest_pain_tearing": "Đau ngực kiểu xé",
    "chest_pain_severe": "Đau ngực dữ dội",
    "chest_wall_tenderness": "Đau thành ngực khi chạm",
    
    # Radiation
    "radiation": "Đau lan",
    "radiation_left_arm": "Đau lan cánh tay trái",
    "radiation_jaw": "Đau lan hàm",
    
    # Pain characteristics
    "exertional": "Khi gắng sức",
    "rest_pain": "Đau khi nghỉ ngơi",
    "positional_pain": "Đau theo tư thế",
    "reproducible": "Có thể tái hiện",
    "tenderness": "Đau khi chạm",
    
    # Pain timing
    "after_meals": "Sau bữa ăn",
    "worse_respiration": "Nặng hơn khi thở",
    "worse_lying_down": "Nặng hơn khi nằm",
    "worse_movement": "Nặng hơn khi vận động",
    
    # General symptoms
    "dyspnea": "Khó thở",
    "diaphoresis": "Vã mồ hôi",
    "nausea": "Buồn nôn",
    "anxiety": "Lo âu",
    "syncope": "Ngất",
    "tachycardia": "Nhịp tim nhanh",
    "hemoptysis": "Ho ra máu",
    "back_pain": "Đau lưng",
    "heartburn": "Ợ nóng",
    "regurgitation": "Trào ngược",
    "relieved_antacids": "Giảm khi dùng thuốc kháng axit",
    
    # Neurologic
    "neurologic_deficit": "Thiếu sót thần kinh",
    "pulse_deficit": "Thiếu hụt mạch",
    
    # Other
    "unilateral_leg_swelling": "Sưng chân một bên",
    "recent_immobility": "Bất động gần đây",
    "malignancy": "Bệnh ác tính",
    
    # Additional common symptoms
    "fever": "Sốt",
    "cough": "Ho",
    "productive_cough": "Ho có đờm",
    "acute_onset": "Khởi phát đột ngột",
    "hypotension": "Hạ huyết áp",
    "tachypnea": "Thở nhanh",
    "altered_mental_status": "Rối loạn ý thức",
    "wheezing": "Thở khò khè",
    "chest_tightness": "Tức ngực",
    "history_asthma_copd": "Tiền sử hen/COPD",
    "triggers": "Yếu tố khởi phát",
    "crackles": "Ran nổ",
    "consolidation": "Đông đặc",
    "source_infection": "Ổ nhiễm trùng",
    "hypothermia": "Hạ thân nhiệt",
    "pulsatile_mass": "Khối đập",
    "sudden": "Đột ngột",
}

# Risk factor translations
RISK_FACTOR_TRANSLATIONS = {
    "diabetes": "Tiểu đường",
    "hypertension": "Tăng huyết áp",
    "smoking": "Hút thuốc",
    "obesity": "Béo phì",
    "family_history_cad": "Tiền sử gia đình bệnh động mạch vành",
    "hyperlipidemia": "Rối loạn lipid máu",
    "atrial_fibrillation": "Rung nhĩ",
    "malignancy": "Bệnh ác tính",
    "immobility": "Bất động",
    "recent_surgery": "Phẫu thuật gần đây",
    "pregnancy": "Mang thai",
    "elderly": "Người cao tuổi",
    "immunocompromised": "Suy giảm miễn dịch",
    "comorbidities": "Bệnh kèm theo",
    "asthma_history": "Tiền sử hen",
    "copd_history": "Tiền sử COPD",
    "allergies": "Dị ứng",
}


def translate_symptom(symptom_key: str) -> str:
    """
    Translate symptom key to Vietnamese
    
    Args:
        symptom_key: Symptom key (e.g., "chest_pain", "diaphoresis")
    
    Returns:
        Vietnamese translation or formatted English if not found
    """
    # Try exact match first
    if symptom_key in SYMPTOM_TRANSLATIONS:
        return SYMPTOM_TRANSLATIONS[symptom_key]
    
    # Try case-insensitive match
    symptom_lower = symptom_key.lower()
    for key, translation in SYMPTOM_TRANSLATIONS.items():
        if key.lower() == symptom_lower:
            return translation
    
    # If not found, format the key nicely
    return symptom_key.replace("_", " ").title()


def translate_risk_factor(risk_factor_key: str) -> str:
    """
    Translate risk factor key to Vietnamese
    
    Args:
        risk_factor_key: Risk factor key (e.g., "diabetes", "hypertension")
    
    Returns:
        Vietnamese translation or formatted English if not found
    """
    # Try exact match first
    if risk_factor_key in RISK_FACTOR_TRANSLATIONS:
        return RISK_FACTOR_TRANSLATIONS[risk_factor_key]
    
    # Try case-insensitive match
    rf_lower = risk_factor_key.lower()
    for key, translation in RISK_FACTOR_TRANSLATIONS.items():
        if key.lower() == rf_lower:
            return translation
    
    # If not found, format the key nicely
    return risk_factor_key.replace("_", " ").title()

