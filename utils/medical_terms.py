"""
Medical Terms Utilities - Helper functions for Vietnamese localization
"""

from config.medical_terms_mapping import (
    get_medical_term_vn,
    format_drug_field_label,
    FIELD_LABELS,
    INTERACTION_SEVERITY,
    PREGNANCY_TERMS,
    MEDICAL_TERMS,
    MONITORING_TERMS,
    EVIDENCE_LEVELS,
    RISK_LEVELS,
    MEDICAL_TERMS_MAPPING,
)


def translate_monitoring_list(monitoring_list: list) -> list:
    """
    Dịch danh sách các thuật ngữ monitoring từ tiếng Anh sang tiếng Việt
    
    Args:
        monitoring_list: Danh sách các thuật ngữ monitoring tiếng Anh
    
    Returns:
        Danh sách đã được dịch sang tiếng Việt
    """
    if not monitoring_list:
        return []
    
    translated = []
    for item in monitoring_list:
        if isinstance(item, str):
            # Try to translate
            translated_item = get_medical_term_vn(item, item)
            translated.append(translated_item)
        else:
            translated.append(item)
    
    return translated


def translate_interaction_severity(severity: str) -> str:
    """
    Dịch mức độ nghiêm trọng của tương tác thuốc
    
    Args:
        severity: Mức độ nghiêm trọng (Major, Moderate, Minor, etc.)
    
    Returns:
        Thuật ngữ tiếng Việt
    """
    return INTERACTION_SEVERITY.get(severity, severity)


def translate_evidence_level(level: str) -> str:
    """
    Dịch mức độ bằng chứng
    
    Args:
        level: Mức độ bằng chứng (Level A, Level B, etc.)
    
    Returns:
        Thuật ngữ tiếng Việt
    """
    return EVIDENCE_LEVELS.get(level, level)


def translate_risk_level(level: str) -> str:
    """
    Dịch mức độ rủi ro
    
    Args:
        level: Mức độ rủi ro (low, moderate, high, etc.)
    
    Returns:
        Thuật ngữ tiếng Việt
    """
    return RISK_LEVELS.get(level.lower(), level)


def translate_text_content(text: str) -> str:
    """
    Dịch các thuật ngữ y khoa trong một đoạn text
    
    Args:
        text: Đoạn text có thể chứa thuật ngữ tiếng Anh
    
    Returns:
        Text đã được dịch các thuật ngữ
    """
    if not text:
        return text
    
    result = str(text)
    
    # Replace medical terms (longer phrases first to avoid partial matches)
    # Sort by length descending
    sorted_terms = sorted(MEDICAL_TERMS.items(), key=lambda x: len(x[0]), reverse=True)
    
    import re
    for en_term, vn_term in sorted_terms:
        # Case-insensitive replacement with word boundaries where appropriate
        # For multi-word terms, use word boundaries
        if ' ' in en_term:
            pattern = re.compile(r'\b' + re.escape(en_term) + r'\b', re.IGNORECASE)
        else:
            # For single words, be more careful to avoid partial matches
            pattern = re.compile(r'\b' + re.escape(en_term) + r'\b', re.IGNORECASE)
        result = pattern.sub(vn_term, result)
    
    # Also translate monitoring terms
    for en_term, vn_term in MONITORING_TERMS.items():
        if ' ' in en_term:
            pattern = re.compile(r'\b' + re.escape(en_term) + r'\b', re.IGNORECASE)
        else:
            pattern = re.compile(r'\b' + re.escape(en_term) + r'\b', re.IGNORECASE)
        result = pattern.sub(vn_term, result)
    
    return result


def translate_drug_field_content(field_name: str, field_value: any) -> any:
    """
    Dịch nội dung của một field trong drug data
    
    Args:
        field_name: Tên field (ví dụ: "mechanism_of_action", "monitoring")
        field_value: Giá trị của field (có thể là string, list, dict)
    
    Returns:
        Giá trị đã được dịch
    """
    if field_value is None:
        return field_value
    
    # For monitoring field, translate list items
    if field_name == "monitoring" and isinstance(field_value, list):
        return translate_monitoring_list(field_value)
    
    # For string fields that might contain medical terms
    if isinstance(field_value, str):
        return translate_text_content(field_value)
    
    # For dict fields, recursively translate values
    if isinstance(field_value, dict):
        translated_dict = {}
        for key, value in field_value.items():
            translated_dict[key] = translate_drug_field_content(key, value)
        return translated_dict
    
    # For list fields, translate each item
    if isinstance(field_value, list):
        return [translate_drug_field_content(field_name, item) for item in field_value]
    
    return field_value
