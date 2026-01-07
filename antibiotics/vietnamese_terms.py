"""
Vietnamese Terminology Mapping
Centralized mapping for all Vietnamese medical terms used in Antibiotics module
"""

# Vietnamese labels for InfectionSite enum
INFECTION_SITE_VI = {
    "CAP": "Viêm phổi cộng đồng",
    "HAP": "Viêm phổi bệnh viện",
    "VAP": "Viêm phổi liên quan thở máy",
    "UTI": "Nhiễm trùng đường tiểu",
    "SSTI": "Nhiễm trùng da và mô mềm",
    "CNS": "Nhiễm trùng hệ thần kinh trung ương",
    "IAI": "Nhiễm trùng ổ bụng",
    "BACTEREMIA": "Nhiễm khuẩn huyết",
    "SEPSIS": "Nhiễm trùng huyết",
    "OSTEOMYELITIS": "Viêm tủy xương",
    "ENDOCARDITIS": "Viêm nội tâm mạc"
}

# Vietnamese labels for Severity enum
SEVERITY_VI = {
    "MILD": "Nhẹ",
    "MODERATE": "Trung bình",
    "SEVERE": "Nặng",
    "ICU": "ICU"
}

# Vietnamese labels for Setting enum
SETTING_VI = {
    "OPD": "Ngoại trú",
    "WARD": "Nội trú",
    "ICU": "ICU"
}

# Vietnamese labels for RegimenType enum
REGIMEN_TYPE_VI = {
    "FIRST_LINE": "Tuyến đầu",
    "ALTERNATIVE": "Thay thế",
    "RESCUE": "Cứu cánh",
    "STEP_DOWN": "Giảm liều"
}

# Vietnamese labels for RecommendationLevel enum
RECOMMENDATION_LEVEL_VI = {
    "STRONG": "Mạnh",
    "WEAK": "Yếu",
    "CONDITIONAL": "Có điều kiện"
}

# Vietnamese labels for evidence grades
EVIDENCE_GRADE_VI = {
    "A": "Mạnh (A)",
    "B": "Yếu (B)",
    "C": "Có điều kiện (C)"
}

# Common Vietnamese medical terms
COMMON_TERMS_VI = {
    "Infection Site": "Vị trí nhiễm trùng",
    "Severity": "Mức độ nặng",
    "Setting": "Môi trường điều trị",
    "First-line": "Tuyến đầu",
    "Alternative": "Thay thế",
    "Rescue": "Cứu cánh",
    "Step-down": "Giảm liều (IV→PO)",
    "Indication": "Chỉ định",
    "Rationale": "Lý do",
    "Special Populations": "Đối tượng đặc biệt",
    "Warnings": "Cảnh báo",
    "Guideline Source": "Nguồn hướng dẫn",
    "Drugs": "Thuốc",
    "Dosing": "Liều dùng",
    "Indications": "Chỉ định",
    "Contraindications": "Chống chỉ định",
    "Side Effects": "Tác dụng phụ",
    "Interactions": "Tương tác",
    "Notes": "Ghi chú",
    "Risk Factors": "Yếu tố nguy cơ",
    "Filters": "Bộ lọc",
    "Search protocols": "Tìm kiếm phác đồ",
    "Search by infection, drug, or guideline...": "Tìm theo nhiễm trùng, thuốc hoặc hướng dẫn...",
    "Found": "Tìm thấy",
    "protocol(s)": "phác đồ",
    "No protocols found. Try adjusting your filters or search query.": "Không tìm thấy phác đồ. Vui lòng điều chỉnh bộ lọc hoặc từ khóa tìm kiếm.",
    "Start Antibiotic Wizard": "Bắt đầu Trợ lý Chọn Kháng Sinh",
    "Back to Protocols": "Quay lại Phác đồ",
    "Open Critical Care Protocol": "Mở Phác đồ Hồi sức",
    "Global Search": "Tìm kiếm Toàn cục",
    "Critical Care": "Hồi sức",
    "Drug Database": "Cơ sở dữ liệu Thuốc",
    "Detail": "Chi tiết",
    "TDM": "TDM",
    "Step-down Options (IV → PO)": "Tùy chọn Giảm liều (IV → PO)",
    "Comorbidities": "Bệnh kèm theo",
    "CKD": "Bệnh thận mạn",
    "Immunocompromised": "Suy giảm miễn dịch",
    "Pregnancy": "Mang thai",
    "Get Recommendations": "Nhận Đề xuất",
    "No matching protocols found. Try adjusting your criteria.": "Không tìm thấy phác đồ phù hợp. Vui lòng điều chỉnh tiêu chí.",
    "Found": "Tìm thấy",
    "recommendation(s)": "đề xuất",
    "Recommendation": "Đề xuất",
    "Adjust dose for renal function": "Điều chỉnh liều theo chức năng thận",
    "Consider pregnancy safety": "Cân nhắc an toàn khi mang thai",
    "Beta-lactam allergy - alternative regimen": "Dị ứng beta-lactam - phác đồ thay thế",
    "By Drug Class": "Theo Nhóm Thuốc",
    "By Infection": "Theo Nhiễm Trùng",
    "Stewardship": "Quản lý Kháng Sinh",
    "Tools": "Công cụ",
    "This view will organize antibiotics by drug class:": "Chế độ xem này sẽ tổ chức kháng sinh theo nhóm thuốc:",
    "This view will include:": "Chế độ xem này sẽ bao gồm:",
    "De-escalation guidelines": "Hướng dẫn giảm liều",
    "IV → PO switch criteria": "Tiêu chí chuyển IV → PO",
    "Renal dosing summary": "Tóm tắt liều theo thận",
    "Duration of therapy recommendations": "Khuyến cáo thời gian điều trị",
    "Antibiotic stewardship principles": "Nguyên tắc quản lý kháng sinh",
    # Drug classes
    "Beta-lactams": "Beta-lactam",
    "Fluoroquinolones": "Fluoroquinolone",
    "Macrolides": "Macrolide",
    "Glycopeptides": "Glycopeptide",
    "Aminoglycosides": "Aminoglycoside",
    "Lincosamides": "Lincosamide",
    "Tetracyclines": "Tetracycline",
    "Others": "Khác",
    "Drug Class": "Nhóm Thuốc",
    "Spectrum of activity": "Phổ tác dụng",
    "Common indications": "Chỉ định thường gặp",
    "Dosing guidelines": "Hướng dẫn liều",
    "Resistance patterns": "Mô hình kháng thuốc",
    "Mechanism of action": "Cơ chế tác dụng",
    # Stewardship terms
    "De-escalation": "Giảm liều",
    "IV to PO": "Chuyển IV → PO",
    "Renal dosing": "Liều theo thận",
    "Treatment duration": "Thời gian điều trị",
    "Stewardship principles": "Nguyên tắc quản lý",
    "Clinical criteria": "Tiêu chí lâm sàng",
    "Microbiological criteria": "Tiêu chí vi sinh",
    "Bioavailability": "Độ hấp thu",
    "CrCl": "CrCl",
    "eGFR": "eGFR",
    "Normal dose": "Liều bình thường",
    "Standard duration": "Thời gian chuẩn",
    "Short duration": "Rút ngắn",
    "Extended duration": "Kéo dài"
}

def get_vietnamese_label(term: str, category: str = "common") -> str:
    """
    Get Vietnamese label for a term
    
    Args:
        term: English term
        category: Category of term (infection_site, severity, setting, regimen_type, recommendation_level, common)
    
    Returns:
        Vietnamese label or original term if not found
    """
    mapping = {
        "infection_site": INFECTION_SITE_VI,
        "severity": SEVERITY_VI,
        "setting": SETTING_VI,
        "regimen_type": REGIMEN_TYPE_VI,
        "recommendation_level": RECOMMENDATION_LEVEL_VI,
        "common": COMMON_TERMS_VI
    }
    
    category_map = mapping.get(category, COMMON_TERMS_VI)
    return category_map.get(term, term)
