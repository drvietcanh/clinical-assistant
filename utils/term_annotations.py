"""
Term Annotations Helper
Hệ thống chú thích tự động cho thuật ngữ y khoa
"""

from typing import Dict, Optional, Tuple
import streamlit as st

# Dictionary of medical terms with their annotations
# Format: {term: (vietnamese_name, full_explanation, show_annotation)}
MEDICAL_TERM_ANNOTATIONS: Dict[str, Tuple[str, str, bool]] = {
    # Abbreviations that need annotation
    'CAP': ('Viêm phổi cộng đồng', 'Community-Acquired Pneumonia', True),
    'HAP': ('Viêm phổi bệnh viện', 'Hospital-Acquired Pneumonia', True),
    'VAP': ('Viêm phổi liên quan thở máy', 'Ventilator-Associated Pneumonia', True),
    'UTI': ('Nhiễm trùng đường tiểu', 'Urinary Tract Infection', True),
    'SSTI': ('Nhiễm trùng da và mô mềm', 'Skin and Soft Tissue Infection', True),
    'CNS': ('Hệ thần kinh trung ương', 'Central Nervous System', True),
    'IAI': ('Nhiễm trùng ổ bụng', 'Intra-Abdominal Infection', True),
    'SEPSIS': ('Nhiễm trùng huyết', 'Sepsis', True),
    'BACTEREMIA': ('Nhiễm khuẩn huyết', 'Bacteremia', True),
    'OSTEOMYELITIS': ('Viêm tủy xương', 'Osteomyelitis', True),
    'ENDOCARDITIS': ('Viêm nội tâm mạc', 'Endocarditis', True),
    
    # Clinical scores
    'CHADS2-VASc': ('CHADS2-VASc', 'Thang điểm đánh giá nguy cơ đột quỵ ở bệnh nhân rung nhĩ', True),
    'HAS-BLED': ('HAS-BLED', 'Thang điểm đánh giá nguy cơ chảy máu', True),
    'SOFA': ('SOFA', 'Thang điểm đánh giá suy đa tạng', True),
    'APACHE': ('APACHE', 'Thang điểm đánh giá mức độ nặng bệnh nhân hồi sức', True),
    'NEWS2': ('NEWS2', 'Thang điểm cảnh báo sớm quốc gia (phiên bản 2)', True),
    'QSOFA': ('QSOFA', 'Tiêu chí nhanh đánh giá nhiễm trùng huyết', True),
    'SIRS': ('SIRS', 'Tiêu chí hội chứng đáp ứng viêm hệ thống', True),
    'GCS': ('GCS', 'Thang điểm hôn mê Glasgow', True),
    'NIHSS': ('NIHSS', 'Thang điểm đột quỵ của Viện Sức khỏe Quốc gia Hoa Kỳ', True),
    'MRS': ('MRS', 'Thang điểm Rankin sửa đổi', True),
    'GRACE': ('GRACE', 'Thang điểm đánh giá nguy cơ tử vong trong hội chứng mạch vành cấp', True),
    'TIMI': ('TIMI', 'Thang điểm đánh giá nguy cơ trong hội chứng mạch vành cấp', True),
    'WELLS': ('WELLS', 'Thang điểm đánh giá nguy cơ thuyên tắc phổi', True),
    'PERC': ('PERC', 'Tiêu chí loại trừ thuyên tắc phổi', True),
    'NYHA': ('NYHA', 'Phân loại suy tim theo Hiệp hội Tim mạch New York', True),
    
    # Renal
    'CKD-EPI': ('CKD-EPI', 'Công thức ước tính độ lọc cầu thận (Collaboration)', True),
    'MDRD': ('MDRD', 'Công thức Modification of Diet in Renal Disease', True),
    'FENa': ('FENa', 'Phân số bài tiết Natri', True),
    'CKD': ('Bệnh thận mạn', 'Chronic Kidney Disease', True),
    'ESRD': ('Suy thận giai đoạn cuối', 'End-Stage Renal Disease', True),
    'AKI': ('Suy thận cấp', 'Acute Kidney Injury', True),
    
    # Diseases
    'COPD': ('Bệnh phổi tắc nghẽn mạn tính', 'Chronic Obstructive Pulmonary Disease', True),
    'ARDS': ('Hội chứng suy hô hấp cấp', 'Acute Respiratory Distress Syndrome', True),
    'DVT': ('Huyết khối tĩnh mạch sâu', 'Deep Vein Thrombosis', True),
    'PE': ('Thuyên tắc phổi', 'Pulmonary Embolism', True),
    'ACS': ('Hội chứng mạch vành cấp', 'Acute Coronary Syndrome', True),
    'STEMI': ('Nhồi máu cơ tim ST chênh lên', 'ST-Elevation Myocardial Infarction', True),
    'NSTEMI': ('Nhồi máu cơ tim ST không chênh lên', 'Non-ST-Elevation Myocardial Infarction', True),
    'AFib': ('Rung nhĩ', 'Atrial Fibrillation', True),
    'CHF': ('Suy tim', 'Congestive Heart Failure', True),
    'HF': ('Suy tim', 'Heart Failure', True),
    'MI': ('Nhồi máu cơ tim', 'Myocardial Infarction', True),
    'CAD': ('Bệnh động mạch vành', 'Coronary Artery Disease', True),
    'TIA': ('Cơn thiếu máu não thoáng qua', 'Transient Ischemic Attack', True),
    'CVA': ('Đột quỵ', 'Cerebrovascular Accident', True),
    'ICH': ('Xuất huyết nội sọ', 'Intracerebral Hemorrhage', True),
    'SAH': ('Xuất huyết dưới nhện', 'Subarachnoid Hemorrhage', True),
    'SDH': ('Tụ máu dưới màng cứng', 'Subdural Hematoma', True),
    'EDH': ('Tụ máu ngoài màng cứng', 'Epidural Hematoma', True),
    
    # Hematology
    'ITP': ('Xuất huyết giảm tiểu cầu miễn dịch', 'Immune Thrombocytopenic Purpura', True),
    'DIC': ('Đông máu rải rác trong lòng mạch', 'Disseminated Intravascular Coagulation', True),
    'TTP': ('Hội chứng tan máu tăng ure máu', 'Thrombotic Thrombocytopenic Purpura', True),
    'HUS': ('Hội chứng tan máu tăng ure máu', 'Hemolytic Uremic Syndrome', True),
    
    # Drug classes
    'Beta-lactam': ('Beta-lactam', 'Nhóm kháng sinh có cấu trúc beta-lactam (Penicillin, Cephalosporin, Carbapenem)', True),
    'Fluoroquinolone': ('Fluoroquinolone', 'Nhóm kháng sinh fluoroquinolone', True),
    'Macrolide': ('Macrolide', 'Nhóm kháng sinh macrolide', True),
    'Glycopeptide': ('Glycopeptide', 'Nhóm kháng sinh glycopeptide (Vancomycin, Teicoplanin)', True),
    'Aminoglycoside': ('Aminoglycoside', 'Nhóm kháng sinh aminoglycoside', True),
    'Lincosamide': ('Lincosamide', 'Nhóm kháng sinh lincosamide', True),
    'Tetracycline': ('Tetracycline', 'Nhóm kháng sinh tetracycline', True),
    
    # Procedures
    'CRRT': ('Lọc máu liên tục', 'Continuous Renal Replacement Therapy', True),
    'CT scan': ('Chụp cắt lớp vi tính', 'Computed Tomography', True),
    'MRI': ('Chụp cộng hưởng từ', 'Magnetic Resonance Imaging', True),
    'ECG': ('Điện tâm đồ', 'Electrocardiogram', True),
    'EKG': ('Điện tâm đồ', 'Electrocardiogram', True),
    'EEG': ('Điện não đồ', 'Electroencephalogram', True),
    'EMG': ('Điện cơ đồ', 'Electromyogram', True),
    
    # Lab tests
    'WBC': ('Bạch cầu', 'White Blood Cell', True),
    'RBC': ('Hồng cầu', 'Red Blood Cell', True),
    'PT': ('Thời gian Prothrombin', 'Prothrombin Time', True),
    'INR': ('Tỷ lệ bình thường hóa quốc tế', 'International Normalized Ratio', True),
    'PTT': ('Thời gian Thromboplastin từng phần', 'Partial Thromboplastin Time', True),
    'aPTT': ('Thời gian Thromboplastin từng phần hoạt hóa', 'Activated Partial Thromboplastin Time', True),
    'CRP': ('Protein phản ứng C', 'C-Reactive Protein', True),
    'ESR': ('Tốc độ lắng máu', 'Erythrocyte Sedimentation Rate', True),
    'PCT': ('Procalcitonin', 'Procalcitonin', True),
    
    # ABG
    'ABG': ('Khí máu động mạch', 'Arterial Blood Gas', True),
    'pCO2': ('Áp suất riêng phần CO2', 'Partial Pressure of Carbon Dioxide', True),
    'pO2': ('Áp suất riêng phần O2', 'Partial Pressure of Oxygen', True),
    'HCO3': ('Bicarbonate', 'Bicarbonate', True),
    'BE': ('Base Excess', 'Base Excess', True),
    'SaO2': ('Độ bão hòa oxy động mạch', 'Arterial Oxygen Saturation', True),
    'SpO2': ('Độ bão hòa oxy mao mạch', 'Peripheral Oxygen Saturation', True),
    
    # Ventilator
    'FiO2': ('Nồng độ oxy trong khí thở vào', 'Fraction of Inspired Oxygen', True),
    'PEEP': ('Áp lực dương cuối thì thở ra', 'Positive End-Expiratory Pressure', True),
    'RR': ('Tần số thở', 'Respiratory Rate', True),
    'TV': ('Thể tích khí lưu thông', 'Tidal Volume', True),
    'MV': ('Thể tích phút', 'Minute Volume', True),
    'I:E': ('Tỷ lệ hít vào:thở ra', 'Inspiratory:Expiratory Ratio', True),
    'PIP': ('Áp lực đỉnh', 'Peak Inspiratory Pressure', True),
    
    # Terms that don't need annotation (commonly used)
    'ICU': ('ICU', '', False),
    'TDM': ('TDM', '', False),
    'eGFR': ('eGFR', '', False),
    'CrCl': ('CrCl', '', False),
    'IV': ('IV', '', False),
    'PO': ('PO', '', False),
    'IM': ('IM', '', False),
    'SC': ('SC', '', False),
    'FDA': ('FDA', '', False),
    'BMI': ('BMI', '', False),
    'BSA': ('BSA', '', False),
}


def get_term_with_annotation(
    term: str, 
    show_annotation: Optional[bool] = None,
    format_type: str = 'tooltip'
) -> str:
    """
    Get Vietnamese term with optional annotation
    
    Args:
        term: Medical term (can be English abbreviation or Vietnamese)
        show_annotation: Whether to show annotation (None = use default from dict)
        format_type: 'tooltip', 'inline', or 'plain'
    
    Returns:
        Formatted string with term and annotation
    """
    term_upper = term.upper().strip()
    
    # Try exact match first
    if term_upper in MEDICAL_TERM_ANNOTATIONS:
        vietnamese_name, explanation, default_show = MEDICAL_TERM_ANNOTATIONS[term_upper]
        
        if show_annotation is None:
            show_annotation = default_show
        
        if not show_annotation or not explanation:
            return vietnamese_name
        
        if format_type == 'tooltip':
            # Return HTML with title attribute for tooltip
            return f'<span title="{explanation} ({term_upper})">{vietnamese_name}</span>'
        elif format_type == 'inline':
            return f'{vietnamese_name} ({term_upper}: {explanation})'
        elif format_type == 'plain':
            return vietnamese_name
        else:
            return f'{vietnamese_name} ({term_upper})'
    
    # Try partial match (e.g., "CHADS2-VASc" in text)
    for abbrev, (vietnamese_name, explanation, default_show) in MEDICAL_TERM_ANNOTATIONS.items():
        if abbrev in term_upper:
            if show_annotation is None:
                show_annotation = default_show
            
            if not show_annotation or not explanation:
                return vietnamese_name
            
            if format_type == 'tooltip':
                return f'<span title="{explanation} ({abbrev})">{vietnamese_name}</span>'
            elif format_type == 'inline':
                return f'{vietnamese_name} ({abbrev}: {explanation})'
            else:
                return vietnamese_name
    
    # Not found, return original
    return term


def render_term_with_tooltip(term: str, show_annotation: Optional[bool] = None) -> None:
    """
    Render term with Streamlit tooltip
    
    Args:
        term: Medical term
        show_annotation: Whether to show annotation
    """
    term_upper = term.upper().strip()
    
    if term_upper in MEDICAL_TERM_ANNOTATIONS:
        vietnamese_name, explanation, default_show = MEDICAL_TERM_ANNOTATIONS[term_upper]
        
        if show_annotation is None:
            show_annotation = default_show
        
        if show_annotation and explanation:
            st.markdown(
                f'<span title="{explanation} ({term_upper})">{vietnamese_name}</span>',
                unsafe_allow_html=True
            )
        else:
            st.write(vietnamese_name)
    else:
        st.write(term)


def get_all_annotated_terms() -> Dict[str, Tuple[str, str]]:
    """
    Get all terms that have annotations
    
    Returns:
        Dictionary of {term: (vietnamese_name, explanation)}
    """
    return {
        term: (vietnamese_name, explanation)
        for term, (vietnamese_name, explanation, show_annotation) in MEDICAL_TERM_ANNOTATIONS.items()
        if show_annotation and explanation
    }


def check_term_needs_annotation(term: str) -> bool:
    """
    Check if a term needs annotation
    
    Args:
        term: Medical term
    
    Returns:
        True if term needs annotation
    """
    term_upper = term.upper().strip()
    
    if term_upper in MEDICAL_TERM_ANNOTATIONS:
        _, _, show_annotation = MEDICAL_TERM_ANNOTATIONS[term_upper]
        return show_annotation
    
    return False


__all__ = [
    'get_term_with_annotation',
    'render_term_with_tooltip',
    'get_all_annotated_terms',
    'check_term_needs_annotation',
    'MEDICAL_TERM_ANNOTATIONS',
]
