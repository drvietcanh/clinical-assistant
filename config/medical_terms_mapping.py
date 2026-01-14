"""
Medical Terms Mapping - Vietnamese Localization
Mapping từ thuật ngữ y khoa tiếng Anh sang tiếng Việt
"""

# Field Labels - Labels hiển thị trong UI
FIELD_LABELS = {
    "ADMINISTRATION": "Đường dùng",
    "INDICATIONS": "Chỉ định",
    "CONTRAINDICATIONS": "Chống chỉ định",
    "DOSAGE": "Liều dùng",
    "PRECAUTIONS": "Thận trọng",
    "INTERACTIONS": "Tương tác thuốc",
    "MECHANISM OF ACTION": "Cơ chế tác dụng",
    "MECHANISM": "Cơ chế tác dụng",
    "PHARMACOKINETICS": "Dược động học",
    "SIDE EFFECTS": "Tác dụng phụ",
    "WARNINGS": "Cảnh báo",
    "MONITORING": "Theo dõi",
    "STORAGE": "Bảo quản",
    "BLACK BOX WARNINGS": "Cảnh báo hộp đen",
    "DRUG INTERACTIONS": "Tương tác thuốc",
    "ADMINISTRATION INSTRUCTIONS": "Hướng dẫn sử dụng",
    "TOXICITY MANAGEMENT": "Xử trí ngộ độc",
    "PREGNANCY": "An toàn thai kỳ",
    "LACTATION": "An toàn cho con bú",
}

# Interaction Severity Labels
INTERACTION_SEVERITY = {
    "Major": "Nghiêm trọng",
    "Moderate": "Trung bình",
    "Minor": "Nhẹ",
    "No Interaction": "Không có tương tác",
    "Same Drug": "Cùng thuốc",
}

# Pregnancy & Lactation Terms
PREGNANCY_TERMS = {
    "FDA Pregnancy Category": "Phân loại FDA thai kỳ",
    "first trimester": "Tam cá nguyệt đầu",
    "second trimester": "Tam cá nguyệt giữa",
    "third trimester": "Tam cá nguyệt cuối",
    "Moderately Safe": "Tương đối an toàn",
    "Compatible with monitoring": "Tương thích khi theo dõi",
    "Compatible": "Tương thích",
    "Unknown": "Chưa rõ",
}

# Medical Terms trong nội dung
MEDICAL_TERMS = {
    "maintenance therapy": "Điều trị duy trì",
    "ceiling effect": "Hiệu ứng trần",
    "protein binding": "Gắn protein",
    "clearance": "Thanh thải",
    "half life": "Thời gian bán hủy",
    "half-life": "Thời gian bán hủy",
    "onset": "Thời gian khởi phát",
    "duration": "Thời gian tác dụng",
    "affinity": "Ái lực",
    "active metabolite": "Chất chuyển hóa hoạt động",
    "procedural sedation": "An thần cho thủ thuật",
    "ICU sedation": "An thần ICU",
    "narrow therapeutic index": "Chỉ số điều trị hẹp",
    "trough levels": "Nồng độ đáy",
    "peak levels": "Nồng độ đỉnh",
}

# Monitoring Terms
MONITORING_TERMS = {
    "Respiratory rate": "Nhịp thở",
    "Sedation": "Mức độ an thần",
    "Constipation": "Táo bón",
    "LFT": "Chức năng gan",
    "RFT": "Chức năng thận",
    "GI symptoms": "Triệu chứng tiêu hóa",
    "Blood pressure": "Huyết áp",
    "Cardiovascular symptoms": "Triệu chứng tim mạch",
    "Blood glucose": "Đường huyết",
    "Renal function": "Chức năng thận",
    "Hepatic function": "Chức năng gan",
    "Cognitive function": "Chức năng nhận thức",
    "Driving ability": "Khả năng lái xe",
    "Level of consciousness": "Mức độ ý thức",
    "Vital Signs": "Dấu hiệu sinh tồn",
    "GCS": "Thang điểm Glasgow",
    "Respiratory": "Hô hấp",
}

# Evidence Levels
EVIDENCE_LEVELS = {
    "Level A - Strong Evidence": "Mức A - Bằng chứng mạnh",
    "Level B - Moderate Evidence": "Mức B - Bằng chứng trung bình",
    "Level C - Limited Evidence": "Mức C - Bằng chứng hạn chế",
    "Level D - Weak Evidence": "Mức D - Bằng chứng yếu",
    "Expert Opinion": "Ý kiến chuyên gia",
    "Strong Evidence": "Bằng chứng mạnh",
    "Moderate Evidence": "Bằng chứng trung bình",
    "Limited Evidence": "Bằng chứng hạn chế",
    "Weak Evidence": "Bằng chứng yếu",
    "High Quality": "Chất lượng cao",
    "Moderate Quality": "Chất lượng trung bình",
    "Low Quality": "Chất lượng thấp",
    "Very Low Quality": "Chất lượng rất thấp",
    "Level I (High Quality)": "Mức I (Chất lượng cao)",
    "Level IIa (Moderate Quality)": "Mức IIa (Chất lượng trung bình)",
    "Level IIb (Low Quality)": "Mức IIb (Chất lượng thấp)",
    "Level III (Very Low Quality)": "Mức III (Chất lượng rất thấp)",
    "Strong": "Mạnh",
    "Weak": "Yếu",
}

# Risk Levels
RISK_LEVELS = {
    "low": "Thấp",
    "moderate": "Trung bình",
    "high": "Cao",
    "very_low": "Rất thấp",
    "very_high": "Rất cao",
    "critical": "Nghiêm trọng",
}

# Combined mapping for easy lookup
MEDICAL_TERMS_MAPPING = {
    **FIELD_LABELS,
    **INTERACTION_SEVERITY,
    **PREGNANCY_TERMS,
    **MEDICAL_TERMS,
    **MONITORING_TERMS,
    **EVIDENCE_LEVELS,
    **RISK_LEVELS,
}


def get_medical_term_vn(term: str, default: str = None) -> str:
    """
    Lấy thuật ngữ tiếng Việt cho một thuật ngữ tiếng Anh
    
    Args:
        term: Thuật ngữ tiếng Anh
        default: Giá trị mặc định nếu không tìm thấy (mặc định là trả về term gốc)
    
    Returns:
        Thuật ngữ tiếng Việt hoặc default/term gốc
    """
    if not term:
        return term
    
    # Try exact match first
    if term in MEDICAL_TERMS_MAPPING:
        return MEDICAL_TERMS_MAPPING[term]
    
    # Try case-insensitive match
    term_lower = term.lower()
    for key, value in MEDICAL_TERMS_MAPPING.items():
        if key.lower() == term_lower:
            return value
    
    # Return default or original term
    return default if default is not None else term


def format_drug_field_label(field_name: str) -> str:
    """
    Format field name thành label tiếng Việt để hiển thị
    
    Args:
        field_name: Tên field (ví dụ: "administration", "indications")
    
    Returns:
        Label tiếng Việt (ví dụ: "Đường dùng", "Chỉ định")
    """
    # Convert snake_case to UPPER CASE for lookup
    field_upper = field_name.upper().replace("_", " ")
    
    # Try exact match in FIELD_LABELS
    if field_upper in FIELD_LABELS:
        return FIELD_LABELS[field_upper]
    
    # Try with underscores replaced
    field_upper_underscore = field_name.upper().replace(" ", "_")
    if field_upper_underscore in FIELD_LABELS:
        return FIELD_LABELS[field_upper_underscore]
    
    # Fallback: capitalize and return
    return field_name.replace("_", " ").title()
