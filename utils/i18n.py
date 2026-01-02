"""
Internationalization (i18n) Foundation
Multi-language support foundation
"""

from typing import Dict, Optional
from enum import Enum


class Language(Enum):
    """Supported languages"""
    VIETNAMESE = "vi"
    ENGLISH = "en"


# Translation dictionaries
TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "vi": {
        # Common
        "home": "Trang chủ",
        "search": "Tìm kiếm",
        "settings": "Cài đặt",
        "about": "Giới thiệu",
        "close": "Đóng",
        "save": "Lưu",
        "cancel": "Hủy",
        "submit": "Gửi",
        "back": "Quay lại",
        "next": "Tiếp theo",
        "previous": "Trước",
        
        # Calculators
        "calculator": "Máy tính",
        "score": "Thang điểm",
        "result": "Kết quả",
        "calculate": "Tính toán",
        "reset": "Đặt lại",
        
        # Drugs
        "drug": "Thuốc",
        "drugs": "Thuốc",
        "dosage": "Liều dùng",
        "indication": "Chỉ định",
        "contraindication": "Chống chỉ định",
        "side_effect": "Tác dụng phụ",
        "interaction": "Tương tác",
        
        # Protocols
        "protocol": "Phác đồ",
        "protocols": "Phác đồ",
        "guideline": "Hướng dẫn",
        "recommendation": "Khuyến cáo",
        "evidence": "Bằng chứng",
        
        # Common medical terms
        "patient": "Bệnh nhân",
        "diagnosis": "Chẩn đoán",
        "treatment": "Điều trị",
        "monitoring": "Theo dõi",
        "warning": "Cảnh báo",
        "critical": "Nghiêm trọng",
    },
    "en": {
        # Common
        "home": "Home",
        "search": "Search",
        "settings": "Settings",
        "about": "About",
        "close": "Close",
        "save": "Save",
        "cancel": "Cancel",
        "submit": "Submit",
        "back": "Back",
        "next": "Next",
        "previous": "Previous",
        
        # Calculators
        "calculator": "Calculator",
        "score": "Score",
        "result": "Result",
        "calculate": "Calculate",
        "reset": "Reset",
        
        # Drugs
        "drug": "Drug",
        "drugs": "Drugs",
        "dosage": "Dosage",
        "indication": "Indication",
        "contraindication": "Contraindication",
        "side_effect": "Side Effect",
        "interaction": "Interaction",
        
        # Protocols
        "protocol": "Protocol",
        "protocols": "Protocols",
        "guideline": "Guideline",
        "recommendation": "Recommendation",
        "evidence": "Evidence",
        
        # Common medical terms
        "patient": "Patient",
        "diagnosis": "Diagnosis",
        "treatment": "Treatment",
        "monitoring": "Monitoring",
        "warning": "Warning",
        "critical": "Critical",
    }
}


def get_translation(key: str, language: str = "vi") -> str:
    """
    Get translation for a key
    
    Args:
        key: Translation key
        language: Language code ("vi" or "en")
    
    Returns:
        Translated string or key if not found
    """
    return TRANSLATIONS.get(language, TRANSLATIONS["vi"]).get(key, key)


def t(key: str, language: Optional[str] = None) -> str:
    """
    Shortcut for get_translation
    
    Args:
        key: Translation key
        language: Language code (defaults to session state or "vi")
    
    Returns:
        Translated string
    """
    import streamlit as st
    
    if language is None:
        language = st.session_state.get('language', 'vi')
    
    return get_translation(key, language)


def set_language(language: str) -> None:
    """
    Set current language in session state
    
    Args:
        language: Language code ("vi" or "en")
    """
    import streamlit as st
    st.session_state['language'] = language


def get_current_language() -> str:
    """
    Get current language from session state
    
    Returns:
        Language code
    """
    import streamlit as st
    return st.session_state.get('language', 'vi')


__all__ = [
    'Language',
    'TRANSLATIONS',
    'get_translation',
    't',
    'set_language',
    'get_current_language',
]

