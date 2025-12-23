"""
Mapping between Articles and Protocols for bidirectional linking.

This module provides mapping between article IDs (from content/articles/*.md)
and protocol render functions (from protocols/ modules).
"""

from typing import Optional, Dict, List, Tuple


# Mapping: article_id -> protocol information
ARTICLE_TO_PROTOCOL: Dict[str, Dict[str, str]] = {
    # Cardiology
    "acs_management": {
        "protocol_function": "render_acs",
        "protocol_name": "ACS - Hội Chứng Vành Cấp",
        "specialty": "Tim mạch cấp cứu",
        "specialty_selector": "Tim mạch (Cardiology)",
        "protocol_display": "💔 ACS - Hội chứng vành cấp"
    },
    "acute_heart_failure": {
        "protocol_function": "render_hf",
        "protocol_name": "Suy tim Cấp",
        "specialty": "Tim mạch",
        "specialty_selector": "Tim mạch (Cardiology)",
        "protocol_display": "💔 Suy tim Cấp"
    },
    "suy-tim-cap-phan-loai-scai-va-xu-tri": {
        "protocol_function": "render_acute_decompensated_hf",
        "protocol_name": "Suy tim Mất Bù Cấp",
        "specialty": "Tim mạch",
        "specialty_selector": "Tim mạch (Cardiology)",
        "protocol_display": "💔 Suy tim Mất Bù Cấp (ADHF)"
    },
    "atrial_fibrillation": {
        "protocol_function": "render_atrial_fibrillation",
        "protocol_name": "Rung Nhĩ",
        "specialty": "Tim mạch",
        "specialty_selector": "Tim mạch (Cardiology)",
        "protocol_display": "💓 Rung Nhĩ (Atrial Fibrillation)"
    },
    "thuyen-tac-phoi-cap-phan-tang-nguy-co-va-dieu-tri-esc": {
        "protocol_function": "render_dvt_pe",
        "protocol_name": "DVT/PE Management",
        "specialty": "Tim mạch",
        "specialty_selector": "Tim mạch (Cardiology)",
        "protocol_display": "🩸 DVT/PE Management"
    },
    
    # Emergency / Critical Care
    "sepsis_bundle": {
        "protocol_function": "render_sepsis",
        "protocol_name": "Sepsis 1-Hour Bundle",
        "specialty": "Hồi sức / Nhiễm khuẩn",
        "specialty_selector": "🚨 Cấp cứu (Emergency)",
        "protocol_display": "🦠 Sepsis 1-Hour Bundle"
    },
    "stroke_management": {
        "protocol_function": "render_stroke",
        "protocol_name": "Stroke Management",
        "specialty": "Thần kinh / Cấp cứu",
        "specialty_selector": "🚨 Cấp cứu (Emergency)",
        "protocol_display": "🧠 Stroke Management"
    },
    "anaphylaxis": {
        "protocol_function": "render_anaphylaxis",
        "protocol_name": "Anaphylaxis",
        "specialty": "Cấp cứu",
        "specialty_selector": "🚨 Cấp cứu (Emergency)",
        "protocol_display": "🚨 Anaphylaxis"
    },
    "cap-cuu-noi-tiet-dka-hhs-bao-giap": {
        "protocol_function": "render_dka",
        "protocol_name": "DKA Protocol",
        "specialty": "Nội tiết / Cấp cứu",
        "specialty_selector": "🚨 Cấp cứu (Emergency)",
        "protocol_display": "🍭 DKA Protocol"
    },
    "electrolyte_disorders": {
        "protocol_function": "render_electrolytes",
        "protocol_name": "Electrolyte Emergency",
        "specialty": "Cấp cứu",
        "specialty_selector": "🚨 Cấp cứu (Emergency)",
        "protocol_display": "⚡ Electrolyte Emergency"
    },
    "xuat-huyet-tieu-hoa-tren-do-loet-khong-gian-tinh-mach": {
        "protocol_function": "render_gi_bleeding",
        "protocol_name": "GI Bleeding",
        "specialty": "Tiêu hóa / Cấp cứu",
        "specialty_selector": "🚨 Cấp cứu (Emergency)",
        "protocol_display": "🩸 GI Bleeding"
    },
    
    # Respiratory
    "copd_asthma_exacerbation": {
        "protocol_function": "render_copd",
        "protocol_name": "COPD Exacerbation",
        "specialty": "Hô hấp",
        "specialty_selector": "🫁 Hô hấp (Respiratory)",
        "protocol_display": "🫁 COPD Exacerbation"
    },
    "ards_ventilation": {
        "protocol_function": "render_ards",
        "protocol_name": "ARDS Management",
        "specialty": "Hồi sức / Thở máy",
        "specialty_selector": "🏥 Hồi sức (Critical Care)",
        "protocol_display": "🫁 ARDS Management"
    },
    "ards-berlin-thong-khi-bao-ve-phoi-prone-peep-ecmo": {
        "protocol_function": "render_ards",
        "protocol_name": "ARDS Management",
        "specialty": "Hồi sức / Thở máy",
        "specialty_selector": "🏥 Hồi sức (Critical Care)",
        "protocol_display": "🫁 ARDS Management"
    },
    "viem-phoi-cong-dong-cap-ats-idsa": {
        "protocol_function": "render_cap",
        "protocol_name": "Viêm phổi cộng đồng (CAP)",
        "specialty": "Hô hấp",
        "specialty_selector": "🫁 Hô hấp (Respiratory)",
        "protocol_display": "🫁 Viêm phổi cộng đồng (CAP)"
    },
    "viem-phoi-benh-vien-hap-va-vap-ats-idsa": {
        "protocol_function": "render_hap_vap",
        "protocol_name": "HAP/VAP Guidelines",
        "specialty": "Nhiễm khuẩn",
        "specialty_selector": "🦠 Nhiễm khuẩn (Infectious)",
        "protocol_display": "🏥 HAP/VAP Guidelines"
    },
    
    # Nephrology
    "aki_kdigo": {
        "protocol_function": "render_aki",
        "protocol_name": "AKI Management",
        "specialty": "Thận",
        "specialty_selector": "🧪 Thận (Nephrology)",
        "protocol_display": "🧪 AKI Management"
    },
    "suy-than-cap-va-man-o-nguoi-lon": {
        "protocol_function": "render_ckd",
        "protocol_name": "Suy thận mạn tính (CKD)",
        "specialty": "Thận",
        "specialty_selector": "🧪 Thận (Nephrology)",
        "protocol_display": "🫘 Suy thận mạn tính (CKD)"
    },
    
    # Gastroenterology
    "acid_suppression": {
        "protocol_function": "render_stress_ulcer",
        "protocol_name": "Stress Ulcer Prophylaxis",
        "specialty": "Tiêu hóa / Hồi sức",
        "specialty_selector": "🏥 Hồi sức (Critical Care)",
        "protocol_display": "🩸 Stress Ulcer Prophylaxis"
    },
    "hoi-chung-suy-gan-cap-tren-nen-man-aclf": {
        "protocol_function": "render_acute_liver_failure",
        "protocol_name": "Suy gan Cấp",
        "specialty": "Tiêu hóa",
        "specialty_selector": "🫀 Tiêu hóa (Gastroenterology)",
        "protocol_display": "🫀 Suy gan Cấp (Acute Liver Failure)"
    },
    "xo-gan-con-bu-theo-doi-lau-dai": {
        "protocol_function": "render_cirrhosis",
        "protocol_name": "Quản lý Xơ Gan",
        "specialty": "Tiêu hóa",
        "specialty_selector": "🫀 Tiêu hóa (Gastroenterology)",
        "protocol_display": "🫀 Quản lý Xơ Gan (Cirrhosis Management)"
    },
    "viem-gan-virus-b-man-o-nguoi-lon": {
        "protocol_function": "render_hepatitis_b",
        "protocol_name": "Điều trị Viêm Gan B",
        "specialty": "Tiêu hóa",
        "specialty_selector": "🫀 Tiêu hóa (Gastroenterology)",
        "protocol_display": "🫀 Điều trị Viêm Gan B (Hepatitis B Treatment)"
    },
    "viem-gan-virus-c-man-o-nguoi-lon": {
        "protocol_function": "render_hepatitis_c",
        "protocol_name": "Điều trị Viêm Gan C",
        "specialty": "Tiêu hóa",
        "specialty_selector": "🫀 Tiêu hóa (Gastroenterology)",
        "protocol_display": "🫀 Điều trị Viêm Gan C (Hepatitis C Treatment)"
    },
    "viem-loet-da-day-ta-trang": {
        "protocol_function": "render_h_pylori_gastritis",
        "protocol_name": "Viêm Loét Dạ Dày HP (+)",
        "specialty": "Tiêu hóa",
        "specialty_selector": "🫀 Tiêu hóa (Gastroenterology)",
        "protocol_display": "🫀 Viêm Loét Dạ Dày HP (+) (H. pylori Gastritis/Ulcer)"
    },
    
    # Endocrinology
    "t2dm_inpatient_outpatient": {
        "protocol_function": "render_hypoglycemia",  # Closest related
        "protocol_name": "Hạ đường huyết",
        "specialty": "Nội tiết",
        "specialty_selector": "⚕️ Nội tiết (Endocrinology)",
        "protocol_display": "🍭 Hạ đường huyết (Hypoglycemia)"
    },
    "dai-thao-duong-typ-2-ngoai-tru-ada-2024": {
        "protocol_function": "render_hhs",  # HHS for hyperglycemia
        "protocol_name": "HHS",
        "specialty": "Nội tiết",
        "specialty_selector": "⚕️ Nội tiết (Endocrinology)",
        "protocol_display": "🍭 HHS (Hyperglycemic Hyperosmolar State)"
    },
    
    # Neurology
    "cerebrovascular_medications": {
        "protocol_function": "render_stroke",
        "protocol_name": "Stroke Management",
        "specialty": "Thần kinh",
        "specialty_selector": "🧠 Thần kinh (Neurology)",
        "protocol_display": "🧠 Stroke Management"
    },
    
    # Obstetrics
    "pregnancy_hypertension_preeclampsia": {
        "protocol_function": "render_eclampsia",
        "protocol_name": "Sản giật",
        "specialty": "Sản khoa",
        "specialty_selector": "🤰 Sản khoa (Obstetrics)",
        "protocol_display": "🤰 Sản giật (Eclampsia)"
    },
}

# Reverse mapping: protocol_function -> article_id(s)
PROTOCOL_TO_ARTICLE: Dict[str, List[str]] = {}
for article_id, protocol_info in ARTICLE_TO_PROTOCOL.items():
    func = protocol_info["protocol_function"]
    if func not in PROTOCOL_TO_ARTICLE:
        PROTOCOL_TO_ARTICLE[func] = []
    PROTOCOL_TO_ARTICLE[func].append(article_id)


def get_protocol_for_article(article_id: str) -> Optional[Dict[str, str]]:
    """
    Get protocol information for a given article ID.
    
    Args:
        article_id: The article ID (filename without .md extension)
        
    Returns:
        Dictionary with protocol info or None if not found
    """
    return ARTICLE_TO_PROTOCOL.get(article_id)


def get_articles_for_protocol(protocol_function: str) -> List[str]:
    """
    Get article ID(s) for a given protocol function.
    
    Args:
        protocol_function: The protocol render function name (e.g., "render_acs")
        
    Returns:
        List of article IDs (may be empty)
    """
    return PROTOCOL_TO_ARTICLE.get(protocol_function, [])


def get_protocol_deep_link(article_id: str) -> Optional[Tuple[str, str, str]]:
    """
    Get deep link information for navigating from article to protocol.
    
    Args:
        article_id: The article ID
        
    Returns:
        Tuple of (page_path, specialty_selector, protocol_display) or None
    """
    protocol_info = get_protocol_for_article(article_id)
    if not protocol_info:
        return None
    
    page_path = "pages/04_📋_Protocols.py"
    specialty_selector = protocol_info.get("specialty_selector")
    protocol_display = protocol_info.get("protocol_display")
    
    return (page_path, specialty_selector, protocol_display)


def get_article_deep_link(protocol_function: str) -> Optional[Tuple[str, str]]:
    """
    Get deep link information for navigating from protocol to article.
    
    Args:
        protocol_function: The protocol render function name
        
    Returns:
        Tuple of (page_path, article_id) or None
    """
    article_ids = get_articles_for_protocol(protocol_function)
    if not article_ids:
        return None
    
    # Use the first article if multiple exist
    article_id = article_ids[0]
    page_path = "pages/12_📚_In_Depth_Articles.py"
    
    return (page_path, article_id)


def has_protocol(article_id: str) -> bool:
    """Check if an article has an associated protocol."""
    return article_id in ARTICLE_TO_PROTOCOL


def has_article(protocol_function: str) -> bool:
    """Check if a protocol has an associated article."""
    return protocol_function in PROTOCOL_TO_ARTICLE and len(PROTOCOL_TO_ARTICLE[protocol_function]) > 0

