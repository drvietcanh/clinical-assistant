"""
Symptom Checker Data
Symptom-diagnosis mapping and symptom database
"""

from typing import Dict, List
from dataclasses import dataclass

# Import DDx data from diagnosis module
try:
    from diagnosis.ddx_data_data import (
        FEVER_DDX,
        CHEST_PAIN_DDX,
        DYSPNEA_DDX,
        ABDOMINAL_PAIN_DDX,
        ALL_SCENARIOS,
        SYMPTOM_ALIASES
    )
    _DDX_LOADED = True
except ImportError:
    _DDX_LOADED = False
    FEVER_DDX = {}
    CHEST_PAIN_DDX = {}
    DYSPNEA_DDX = {}
    ABDOMINAL_PAIN_DDX = {}
    ALL_SCENARIOS = {}
    SYMPTOM_ALIASES = {}


@dataclass
class Symptom:
    """Symptom information"""
    name: str
    name_vn: str
    category: str  # General, Respiratory, Cardiovascular, etc.
    severity: str = "moderate"  # mild, moderate, severe
    urgent: bool = False  # Whether this symptom requires urgent care


# Common symptoms database
SYMPTOM_DATABASE: List[Symptom] = [
    # General
    Symptom("fever", "Sốt", "General", "moderate", False),
    Symptom("fatigue", "Mệt mỏi", "General", "mild", False),
    Symptom("weight_loss", "Sụt cân", "General", "moderate", False),
    Symptom("night_sweats", "Đổ mồ hôi đêm", "General", "moderate", False),
    
    # Respiratory
    Symptom("cough", "Ho", "Respiratory", "moderate", False),
    Symptom("productive_cough", "Ho có đờm", "Respiratory", "moderate", False),
    Symptom("dyspnea", "Khó thở", "Respiratory", "severe", True),
    Symptom("chest_pain", "Đau ngực", "Respiratory", "severe", True),
    Symptom("wheezing", "Thở khò khè", "Respiratory", "moderate", False),
    
    # Cardiovascular
    Symptom("chest_pain_crushing", "Đau ngực đè ép", "Cardiovascular", "severe", True),
    Symptom("palpitations", "Đánh trống ngực", "Cardiovascular", "moderate", False),
    Symptom("syncope", "Ngất", "Cardiovascular", "severe", True),
    Symptom("dizziness", "Chóng mặt", "Cardiovascular", "moderate", False),
    
    # GI
    Symptom("abdominal_pain", "Đau bụng", "GI", "moderate", False),
    Symptom("nausea", "Buồn nôn", "GI", "moderate", False),
    Symptom("vomiting", "Nôn", "GI", "moderate", False),
    Symptom("diarrhea", "Tiêu chảy", "GI", "moderate", False),
    Symptom("constipation", "Táo bón", "GI", "mild", False),
    Symptom("jaundice", "Vàng da", "GI", "moderate", False),
    
    # Neurological
    Symptom("headache", "Đau đầu", "Neurological", "moderate", False),
    Symptom("seizure", "Co giật", "Neurological", "severe", True),
    Symptom("altered_mental_status", "Thay đổi ý thức", "Neurological", "severe", True),
    Symptom("acute_limb_weakness", "Yếu chi cấp", "Neurological", "severe", True),
    Symptom("dizziness", "Chóng mặt", "Neurological", "moderate", False),
    Symptom("vertigo", "Chóng mặt xoay tròn", "Neurological", "moderate", False),
    
    # Other
    Symptom("rash", "Phát ban", "Dermatology", "moderate", False),
    Symptom("joint_pain", "Đau khớp", "Rheumatology", "moderate", False),
    Symptom("back_pain", "Đau lưng", "Rheumatology", "moderate", False),
    Symptom("dysuria", "Tiểu buốt", "Urology", "moderate", False),
    Symptom("frequency", "Tiểu nhiều lần", "Urology", "moderate", False),
]


def get_all_symptoms() -> List[Symptom]:
    """Get all symptoms"""
    return SYMPTOM_DATABASE


def get_symptoms_by_category(category: str) -> List[Symptom]:
    """Get symptoms filtered by category"""
    if not category or category == "All":
        return SYMPTOM_DATABASE
    return [s for s in SYMPTOM_DATABASE if s.category == category]


def get_symptom_diagnosis_mapping() -> Dict:
    """Get symptom-diagnosis mapping from DDx data"""
    if not _DDX_LOADED:
        return {}
    return ALL_SCENARIOS


def get_urgent_symptoms() -> List[str]:
    """Get list of urgent symptoms"""
    return [s.name for s in SYMPTOM_DATABASE if s.urgent]

