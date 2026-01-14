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
# Organized by module/functionality for easier maintenance
TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "vi": {
        # ========== COMMON UI ==========
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
        "delete": "Xóa",
        "edit": "Chỉnh sửa",
        "view": "Xem",
        "download": "Tải xuống",
        "export": "Xuất",
        "import": "Nhập",
        "refresh": "Làm mới",
        "clear": "Xóa",
        "filter": "Lọc",
        "reset": "Đặt lại",
        
        # ========== STATUS MESSAGES ==========
        "success": "Thành công",
        "error": "Lỗi",
        "warning": "Cảnh báo",
        "info": "Thông tin",
        "loading": "Đang tải",
        "no_data": "Không có dữ liệu",
        "not_found": "Không tìm thấy",
        
        # ========== CALCULATORS & SCORES ==========
        "calculator": "Máy tính",
        "score": "Thang điểm",
        "scores": "Thang điểm",
        "result": "Kết quả",
        "results": "Kết quả",
        "calculate": "Tính toán",
        "calculation": "Tính toán",
        "input": "Nhập liệu",
        "output": "Kết quả",
        "formula": "Công thức",
        "interpretation": "Giải thích",
        "risk_level": "Mức độ nguy cơ",
        "low_risk": "Nguy cơ thấp",
        "moderate_risk": "Nguy cơ trung bình",
        "high_risk": "Nguy cơ cao",
        
        # ========== DRUGS ==========
        "drug": "Thuốc",
        "drugs": "Thuốc",
        "drug_database": "Cơ sở dữ liệu thuốc",
        "dosage": "Liều dùng",
        "dosing": "Liều dùng",
        "indication": "Chỉ định",
        "indications": "Chỉ định",
        "contraindication": "Chống chỉ định",
        "contraindications": "Chống chỉ định",
        "side_effect": "Tác dụng phụ",
        "side_effects": "Tác dụng phụ",
        "interaction": "Tương tác",
        "interactions": "Tương tác",
        "drug_class": "Nhóm thuốc",
        "mechanism": "Cơ chế tác dụng",
        "pharmacokinetics": "Dược động học",
        "pregnancy": "An toàn thai kỳ",
        "lactation": "An toàn cho con bú",
        "renal_adjustment": "Điều chỉnh theo thận",
        "hepatic_adjustment": "Điều chỉnh theo gan",
        "monitoring": "Theo dõi",
        "precautions": "Thận trọng",
        "warnings": "Cảnh báo",
        "black_box_warning": "Cảnh báo hộp đen",
        "tdm": "TDM",
        "therapeutic_range": "Khoảng điều trị",
        "target_level": "Nồng độ mục tiêu",
        
        # ========== ANTIBIOTICS ==========
        "antibiotic": "Kháng sinh",
        "antibiotics": "Kháng sinh",
        "infection_site": "Vị trí nhiễm trùng",
        "severity": "Mức độ nặng",
        "mild": "Nhẹ",
        "moderate": "Trung bình",
        "severe": "Nặng",
        "setting": "Môi trường điều trị",
        "outpatient": "Ngoại trú",
        "inpatient": "Nội trú",
        "first_line": "Tuyến đầu",
        "alternative": "Thay thế",
        "rescue": "Cứu cánh",
        "step_down": "Giảm liều",
        "iv_to_po": "Chuyển IV → PO",
        "de_escalation": "Giảm liều",
        "stewardship": "Quản lý kháng sinh",
        "spectrum": "Phổ tác dụng",
        "resistance": "Kháng thuốc",
        "guideline_source": "Nguồn hướng dẫn",
        
        # ========== PROTOCOLS ==========
        "protocol": "Phác đồ",
        "protocols": "Phác đồ",
        "guideline": "Hướng dẫn",
        "guidelines": "Hướng dẫn",
        "recommendation": "Khuyến cáo",
        "recommendations": "Khuyến cáo",
        "evidence": "Bằng chứng",
        "evidence_level": "Mức độ bằng chứng",
        "high_quality": "Chất lượng cao",
        "moderate_quality": "Chất lượng trung bình",
        "low_quality": "Chất lượng thấp",
        "very_low_quality": "Chất lượng rất thấp",
        "specialty": "Chuyên khoa",
        "related_protocols": "Phác đồ liên quan",
        "related_scores": "Thang điểm liên quan",
        "version": "Phiên bản",
        "last_updated": "Cập nhật lần cuối",
        
        # ========== DIAGNOSIS ==========
        "diagnosis": "Chẩn đoán",
        "differential_diagnosis": "Chẩn đoán phân biệt",
        "symptom": "Triệu chứng",
        "symptoms": "Triệu chứng",
        "risk_factor": "Yếu tố nguy cơ",
        "risk_factors": "Yếu tố nguy cơ",
        "disease": "Bệnh",
        "diseases": "Bệnh",
        "icd10": "ICD-10",
        "icd10_code": "Mã ICD-10",
        
        # ========== CRITICAL CARE ==========
        "critical_care": "Hồi sức",
        "ventilator": "Thở máy",
        "ventilation": "Thông khí",
        "abg": "Khí máu động mạch",
        "hemodynamics": "Huyết động học",
        "sedation": "An thần",
        "analgesia": "Giảm đau",
        "crrt": "CRRT",
        "hemodialysis": "Lọc máu",
        "icu": "ICU",
        
        # ========== ANALYTICS ==========
        "analytics": "Phân tích",
        "usage_statistics": "Thống kê sử dụng",
        "dashboard": "Bảng điều khiển",
        "statistics": "Thống kê",
        "insights": "Insights",
        "total_calculations": "Tổng số lần tính",
        "most_used": "Dùng nhiều nhất",
        "specialty_focus": "Chuyên khoa trọng tâm",
        "this_week": "Tuần này",
        "top_pages": "Trang được xem nhiều nhất",
        "top_features": "Tính năng phổ biến",
        "data_management": "Quản lý dữ liệu",
        "export_analytics": "Xuất phân tích",
        "refresh_data": "Làm mới dữ liệu",
        "clear_analytics": "Xóa phân tích",
        "peak_usage_hours": "Khung giờ sử dụng cao điểm",
        "daily_usage": "Tần suất sử dụng",
        "specialty_breakdown": "Phân bố theo chuyên khoa",
        
        # ========== NAVIGATION ==========
        "navigation": "Điều hướng",
        "main_menu": "Trang chủ",
        "quick_access": "Truy cập nhanh",
        "favorites": "Yêu Thích",
        "recently_used": "Gần Đây",
        "modules": "Modules",
        "categories": "Danh mục",
        
        # ========== COMMON MEDICAL TERMS ==========
        "patient": "Bệnh nhân",
        "patients": "Bệnh nhân",
        "treatment": "Điều trị",
        "monitoring": "Theo dõi",
        "critical": "Nghiêm trọng",
        "emergency": "Cấp cứu",
        "urgent": "Khẩn cấp",
        "routine": "Thường quy",
        
        # ========== SPECIALTIES ==========
        "cardiology": "Tim mạch",
        "neurology": "Thần kinh",
        "critical_care_specialty": "Hồi sức",
        "nephrology": "Thận học",
        "hematology": "Huyết học",
        "endocrinology": "Nội tiết",
        "gastroenterology": "Tiêu hóa",
        "pulmonology": "Hô hấp",
        "dermatology": "Da liễu",
        "pediatrics": "Nhi khoa",
        "obstetrics_gynecology": "Sản phụ khoa",
        "emergency_medicine": "Cấp cứu",
        "oncology": "Ung bướu",
        "psychiatry": "Tâm thần",
        "metabolism": "Chuyển hóa",
        
        # ========== LAB TESTS ==========
        "lab_test": "Xét nghiệm",
        "lab_tests": "Xét nghiệm",
        "creatinine": "Creatinine",
        "egfr": "eGFR",
        "crcl": "CrCl",
        "bun": "BUN",
        "glucose": "Đường huyết",
        "hemoglobin": "Hemoglobin",
        "hematocrit": "Hematocrit",
        "platelet": "Tiểu cầu",
        "wbc": "WBC",
        "rbc": "RBC",
        
        # ========== TIME & FREQUENCY ==========
        "daily": "Hàng ngày",
        "weekly": "Hàng tuần",
        "monthly": "Hàng tháng",
        "once": "Một lần",
        "twice": "Hai lần",
        "three_times": "Ba lần",
        "four_times": "Bốn lần",
        "as_needed": "Khi cần",
        "immediately": "Ngay lập tức",
        
        # ========== ROUTES OF ADMINISTRATION ==========
        "oral": "Đường uống",
        "intravenous": "Đường tĩnh mạch",
        "intramuscular": "Đường tiêm bắp",
        "subcutaneous": "Đường tiêm dưới da",
        "topical": "Bôi ngoài da",
        "inhalation": "Hít",
        
        # ========== MISC ==========
        "notes": "Ghi chú",
        "references": "Tài liệu tham khảo",
        "related": "Liên quan",
        "details": "Chi tiết",
        "summary": "Tóm tắt",
        "description": "Mô tả",
        "rationale": "Lý do",
        "comments": "Nhận xét",
    },
    "en": {
        # ========== COMMON UI ==========
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
        "delete": "Delete",
        "edit": "Edit",
        "view": "View",
        "download": "Download",
        "export": "Export",
        "import": "Import",
        "refresh": "Refresh",
        "clear": "Clear",
        "filter": "Filter",
        "reset": "Reset",
        
        # ========== STATUS MESSAGES ==========
        "success": "Success",
        "error": "Error",
        "warning": "Warning",
        "info": "Info",
        "loading": "Loading",
        "no_data": "No data",
        "not_found": "Not found",
        
        # ========== CALCULATORS & SCORES ==========
        "calculator": "Calculator",
        "score": "Score",
        "scores": "Scores",
        "result": "Result",
        "results": "Results",
        "calculate": "Calculate",
        "calculation": "Calculation",
        "input": "Input",
        "output": "Output",
        "formula": "Formula",
        "interpretation": "Interpretation",
        "risk_level": "Risk Level",
        "low_risk": "Low Risk",
        "moderate_risk": "Moderate Risk",
        "high_risk": "High Risk",
        
        # ========== DRUGS ==========
        "drug": "Drug",
        "drugs": "Drugs",
        "drug_database": "Drug Database",
        "dosage": "Dosage",
        "dosing": "Dosing",
        "indication": "Indication",
        "indications": "Indications",
        "contraindication": "Contraindication",
        "contraindications": "Contraindications",
        "side_effect": "Side Effect",
        "side_effects": "Side Effects",
        "interaction": "Interaction",
        "interactions": "Interactions",
        "drug_class": "Drug Class",
        "mechanism": "Mechanism of Action",
        "pharmacokinetics": "Pharmacokinetics",
        "pregnancy": "Pregnancy",
        "lactation": "Lactation",
        "renal_adjustment": "Renal Adjustment",
        "hepatic_adjustment": "Hepatic Adjustment",
        "monitoring": "Monitoring",
        "precautions": "Precautions",
        "warnings": "Warnings",
        "black_box_warning": "Black Box Warning",
        "tdm": "TDM",
        "therapeutic_range": "Therapeutic Range",
        "target_level": "Target Level",
        
        # ========== ANTIBIOTICS ==========
        "antibiotic": "Antibiotic",
        "antibiotics": "Antibiotics",
        "infection_site": "Infection Site",
        "severity": "Severity",
        "mild": "Mild",
        "moderate": "Moderate",
        "severe": "Severe",
        "setting": "Setting",
        "outpatient": "Outpatient",
        "inpatient": "Inpatient",
        "first_line": "First-line",
        "alternative": "Alternative",
        "rescue": "Rescue",
        "step_down": "Step-down",
        "iv_to_po": "IV to PO",
        "de_escalation": "De-escalation",
        "stewardship": "Stewardship",
        "spectrum": "Spectrum",
        "resistance": "Resistance",
        "guideline_source": "Guideline Source",
        
        # ========== PROTOCOLS ==========
        "protocol": "Protocol",
        "protocols": "Protocols",
        "guideline": "Guideline",
        "guidelines": "Guidelines",
        "recommendation": "Recommendation",
        "recommendations": "Recommendations",
        "evidence": "Evidence",
        "evidence_level": "Evidence Level",
        "high_quality": "High Quality",
        "moderate_quality": "Moderate Quality",
        "low_quality": "Low Quality",
        "very_low_quality": "Very Low Quality",
        "specialty": "Specialty",
        "related_protocols": "Related Protocols",
        "related_scores": "Related Scores",
        "version": "Version",
        "last_updated": "Last Updated",
        
        # ========== DIAGNOSIS ==========
        "diagnosis": "Diagnosis",
        "differential_diagnosis": "Differential Diagnosis",
        "symptom": "Symptom",
        "symptoms": "Symptoms",
        "risk_factor": "Risk Factor",
        "risk_factors": "Risk Factors",
        "disease": "Disease",
        "diseases": "Diseases",
        "icd10": "ICD-10",
        "icd10_code": "ICD-10 Code",
        
        # ========== CRITICAL CARE ==========
        "critical_care": "Critical Care",
        "ventilator": "Ventilator",
        "ventilation": "Ventilation",
        "abg": "Arterial Blood Gas",
        "hemodynamics": "Hemodynamics",
        "sedation": "Sedation",
        "analgesia": "Analgesia",
        "crrt": "CRRT",
        "hemodialysis": "Hemodialysis",
        "icu": "ICU",
        
        # ========== ANALYTICS ==========
        "analytics": "Analytics",
        "usage_statistics": "Usage Statistics",
        "dashboard": "Dashboard",
        "statistics": "Statistics",
        "insights": "Insights",
        "total_calculations": "Total Calculations",
        "most_used": "Most Used",
        "specialty_focus": "Specialty Focus",
        "this_week": "This Week",
        "top_pages": "Top Pages",
        "top_features": "Top Features",
        "data_management": "Data Management",
        "export_analytics": "Export Analytics",
        "refresh_data": "Refresh Data",
        "clear_analytics": "Clear Analytics",
        "peak_usage_hours": "Peak Usage Hours",
        "daily_usage": "Daily Usage",
        "specialty_breakdown": "Specialty Breakdown",
        
        # ========== NAVIGATION ==========
        "navigation": "Navigation",
        "main_menu": "Main Menu",
        "quick_access": "Quick Access",
        "favorites": "Favorites",
        "recently_used": "Recently Used",
        "modules": "Modules",
        "categories": "Categories",
        
        # ========== COMMON MEDICAL TERMS ==========
        "patient": "Patient",
        "patients": "Patients",
        "treatment": "Treatment",
        "monitoring": "Monitoring",
        "critical": "Critical",
        "emergency": "Emergency",
        "urgent": "Urgent",
        "routine": "Routine",
        
        # ========== SPECIALTIES ==========
        "cardiology": "Cardiology",
        "neurology": "Neurology",
        "critical_care_specialty": "Critical Care",
        "nephrology": "Nephrology",
        "hematology": "Hematology",
        "endocrinology": "Endocrinology",
        "gastroenterology": "Gastroenterology",
        "pulmonology": "Pulmonology",
        "dermatology": "Dermatology",
        "pediatrics": "Pediatrics",
        "obstetrics_gynecology": "Obstetrics & Gynecology",
        "emergency_medicine": "Emergency Medicine",
        "oncology": "Oncology",
        "psychiatry": "Psychiatry",
        "metabolism": "Metabolism",
        
        # ========== LAB TESTS ==========
        "lab_test": "Lab Test",
        "lab_tests": "Lab Tests",
        "creatinine": "Creatinine",
        "egfr": "eGFR",
        "crcl": "CrCl",
        "bun": "BUN",
        "glucose": "Glucose",
        "hemoglobin": "Hemoglobin",
        "hematocrit": "Hematocrit",
        "platelet": "Platelet",
        "wbc": "WBC",
        "rbc": "RBC",
        
        # ========== TIME & FREQUENCY ==========
        "daily": "Daily",
        "weekly": "Weekly",
        "monthly": "Monthly",
        "once": "Once",
        "twice": "Twice",
        "three_times": "Three Times",
        "four_times": "Four Times",
        "as_needed": "As Needed",
        "immediately": "Immediately",
        
        # ========== ROUTES OF ADMINISTRATION ==========
        "oral": "Oral",
        "intravenous": "Intravenous",
        "intramuscular": "Intramuscular",
        "subcutaneous": "Subcutaneous",
        "topical": "Topical",
        "inhalation": "Inhalation",
        
        # ========== MISC ==========
        "notes": "Notes",
        "references": "References",
        "related": "Related",
        "details": "Details",
        "summary": "Summary",
        "description": "Description",
        "rationale": "Rationale",
        "comments": "Comments",
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

