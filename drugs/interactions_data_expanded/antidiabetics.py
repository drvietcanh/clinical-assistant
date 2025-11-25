"""
Antidiabetic Drug Interactions
Expanded database for antidiabetic drug interactions
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

ANTIDIABETIC_INTERACTIONS = {
    # ========== METFORMIN ==========
    
    # Metformin + Contrast Media (already in main file)
    ("Metformin", "Contrast Media"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ nhiễm toan lactic",
        "description": "Metformin + thuốc cản quang có thể gây nhiễm toan lactic nguy hiểm",
        "clinical_significance": "Nguy cơ nhiễm toan lactic tăng đáng kể, đặc biệt ở bệnh nhân suy thận. Có thể tử vong.",
        "management": "Ngừng metformin 48 giờ trước và sau khi tiêm thuốc cản quang. Kiểm tra creatinine trước khi dùng lại",
        "references": "FDA, ACR Guidelines"
    },
    
    ("Metformin", "Alcohol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ nhiễm toan lactic",
        "description": "Rượu + metformin tăng nguy cơ nhiễm toan lactic",
        "management": "Tránh uống rượu khi dùng metformin",
        "references": "Micromedex"
    },
    
    ("Metformin", "Cimetidine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine làm giảm đào thải metformin, tăng nồng độ metformin",
        "description": "Tăng nguy cơ tác dụng phụ metformin",
        "management": "Thận trọng khi dùng chung. Có thể cần giảm liều metformin",
        "references": "Micromedex"
    },
    
    ("Metformin", "Furosemide"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Furosemide có thể tăng nồng độ metformin",
        "description": "Tăng nguy cơ tác dụng phụ metformin",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Metformin", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nhẹ nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    # ========== SULFONYLUREAS ==========
    
    # Sulfonylurea + Warfarin (already in main file)
    ("Sulfonylurea", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    
    ("Sulfonylurea", "Beta-blocker"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Beta-blocker che giấu triệu chứng hạ đường huyết",
        "description": "Tăng nguy cơ hạ đường huyết nặng",
        "management": "Thận trọng khi dùng chung. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    ("Sulfonylurea", "Alcohol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rượu tăng tác dụng hạ đường huyết của sulfonylurea",
        "description": "Tăng nguy cơ hạ đường huyết nặng",
        "management": "Tránh uống rượu khi dùng sulfonylurea",
        "references": "Micromedex"
    },
    
    ("Sulfonylurea", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    
    ("Sulfonylurea", "Salicylate"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Salicylate tăng tác dụng hạ đường huyết",
        "description": "Tăng nguy cơ hạ đường huyết",
        "management": "Thận trọng khi dùng chung. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    ("Sulfonylurea", "Chloramphenicol"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Chloramphenicol ức chế chuyển hóa sulfonylurea",
        "description": "Tăng tác dụng hạ đường huyết",
        "management": "Thận trọng khi dùng chung. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    # ========== DPP-4 INHIBITORS ==========
    
    ("Sitagliptin", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nhẹ nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Saxagliptin", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nhẹ nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Linagliptin", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nhẹ nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    # ========== SGLT2 INHIBITORS ==========
    
    ("Canagliflozin", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nhẹ nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Dapagliflozin", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nhẹ nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Empagliflozin", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nhẹ nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("SGLT2 Inhibitor", "Diuretic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ mất nước và hạ huyết áp",
        "description": "Tăng nguy cơ mất nước, hạ huyết áp",
        "management": "Thận trọng khi dùng chung. Theo dõi huyết áp và tình trạng mất nước",
        "references": "Micromedex"
    },
    
    ("SGLT2 Inhibitor", "ACE Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ hạ huyết áp và suy thận cấp",
        "description": "Tăng nguy cơ hạ huyết áp, suy thận cấp",
        "management": "Thận trọng khi dùng chung. Theo dõi huyết áp và chức năng thận",
        "references": "Micromedex"
    },
    
    # ========== GLP-1 AGONISTS ==========
    
    ("Liraglutide", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể làm chậm hấp thu digoxin",
        "description": "Giảm nhẹ hấp thu digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Semaglutide", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể làm chậm hấp thu digoxin",
        "description": "Giảm nhẹ hấp thu digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("GLP-1 Agonist", "Warfarin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể làm chậm hấp thu warfarin",
        "description": "Giảm nhẹ hấp thu warfarin",
        "management": "Theo dõi INR",
        "references": "Micromedex"
    },
    
    # ========== INSULIN ==========
    
    ("Insulin", "Beta-blocker"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Beta-blocker che giấu triệu chứng hạ đường huyết và làm giảm phản ứng phục hồi",
        "description": "Tăng nguy cơ hạ đường huyết nặng",
        "clinical_significance": "Beta-blocker che giấu triệu chứng hạ đường huyết (nhịp tim nhanh, run tay). Bệnh nhân có thể không nhận biết hạ đường huyết.",
        "management": "Thận trọng khi dùng chung. Theo dõi đường huyết sát. Giáo dục bệnh nhân về triệu chứng hạ đường huyết",
        "references": "Micromedex"
    },
    
    ("Insulin", "Alcohol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rượu tăng tác dụng hạ đường huyết của insulin",
        "description": "Tăng nguy cơ hạ đường huyết nặng",
        "management": "Tránh uống rượu khi dùng insulin. Nếu uống: ăn đầy đủ",
        "references": "Micromedex"
    },
    
    ("Insulin", "Corticosteroid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid làm tăng đường huyết, giảm tác dụng insulin",
        "description": "Giảm hiệu quả insulin",
        "management": "Tăng liều insulin khi dùng corticosteroid. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    ("Insulin", "Thiazide"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Thiazide làm tăng đường huyết nhẹ",
        "description": "Giảm nhẹ hiệu quả insulin",
        "management": "Theo dõi đường huyết khi dùng thiazide",
        "references": "Micromedex"
    },
    
    ("Insulin", "Salicylate"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Salicylate tăng tác dụng hạ đường huyết",
        "description": "Tăng nguy cơ hạ đường huyết",
        "management": "Thận trọng khi dùng chung. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    # ========== THIAZOLIDINEDIONES (TZDs) ==========
    
    ("Pioglitazone", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nhẹ nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Rosiglitazone", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nhẹ nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("TZD", "Insulin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ phù và suy tim",
        "description": "Tăng nguy cơ phù, suy tim",
        "management": "Thận trọng khi dùng chung. Theo dõi dấu hiệu suy tim",
        "references": "FDA, Micromedex"
    },
    
    # ========== ALPHA-GLUCOSIDASE INHIBITORS ==========
    
    ("Acarbose", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể giảm nhẹ hấp thu digoxin",
        "description": "Giảm nhẹ hấp thu digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Miglitol", "Digoxin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể giảm nhẹ hấp thu digoxin",
        "description": "Giảm nhẹ hấp thu digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
}

