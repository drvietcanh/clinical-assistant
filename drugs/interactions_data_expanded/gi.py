"""
Gastrointestinal Drug Interactions
Expanded database for GI drug interactions
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

GI_INTERACTIONS = {
    # ========== PROTON PUMP INHIBITORS (PPIs) ==========
    
    # Omeprazole + Clopidogrel (already in main file)
    ("Omeprazole", "Clopidogrel"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Omeprazole ức chế CYP2C19, giảm tác dụng chống kết tập tiểu cầu của clopidogrel",
        "description": "Có thể làm giảm hiệu quả phòng ngừa đột quỵ/nhồi máu cơ tim",
        "management": "Cân nhắc dùng PPI khác (pantoprazole, lansoprazole) hoặc H2 blocker",
        "references": "FDA"
    },
    
    ("Omeprazole", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Omeprazole ức chế CYP2C19, có thể làm tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên khi bắt đầu/dừng omeprazole",
        "references": "Clinical Pharmacology"
    },
    
    ("Omeprazole", "Phenytoin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Omeprazole ức chế chuyển hóa phenytoin",
        "description": "Tăng nồng độ phenytoin",
        "management": "Theo dõi nồng độ phenytoin, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Pantoprazole", "Warfarin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Tương tác tối thiểu với warfarin",
        "description": "Tăng nhẹ nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu pantoprazole",
        "references": "Micromedex"
    },
    
    ("Lansoprazole", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng lansoprazole",
        "references": "Micromedex"
    },
    
    ("Esomeprazole", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng esomeprazole",
        "references": "Micromedex"
    },
    
    ("PPI", "Methotrexate"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "PPI có thể tăng nồng độ methotrexate",
        "description": "Tăng nguy cơ độc tính methotrexate",
        "management": "Thận trọng khi dùng chung. Theo dõi công thức máu",
        "references": "Micromedex"
    },
    
    # ========== H2 BLOCKERS ==========
    
    ("Cimetidine", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng cimetidine. Cân nhắc dùng H2 blocker khác",
        "references": "Micromedex"
    },
    
    ("Cimetidine", "Phenytoin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine ức chế chuyển hóa phenytoin",
        "description": "Tăng nồng độ phenytoin",
        "management": "Theo dõi nồng độ phenytoin, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Cimetidine", "Theophylline"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine ức chế chuyển hóa theophylline",
        "description": "Tăng nồng độ theophylline",
        "management": "Theo dõi nồng độ theophylline, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Cimetidine", "Metformin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine làm giảm đào thải metformin, tăng nồng độ metformin",
        "description": "Tăng nguy cơ tác dụng phụ metformin",
        "management": "Thận trọng khi dùng chung. Có thể cần giảm liều metformin",
        "references": "Micromedex"
    },
    
    ("Cimetidine", "Benzodiazepine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine ức chế chuyển hóa benzodiazepine, tăng nồng độ",
        "description": "Tăng tác dụng an thần",
        "management": "Thận trọng khi dùng chung. Có thể cần giảm liều benzodiazepine",
        "references": "Micromedex"
    },
    
    ("Ranitidine", "Warfarin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Tương tác tối thiểu với warfarin",
        "description": "Tăng nhẹ nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng ranitidine",
        "references": "Micromedex"
    },
    
    ("Famotidine", "Warfarin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Tương tác tối thiểu với warfarin",
        "description": "Tăng nhẹ nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng famotidine",
        "references": "Micromedex"
    },
    
    # ========== ANTACIDS ==========
    
    ("Antacid", "Quinolone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid (Ca, Mg, Al) chelate với quinolone, giảm hấp thu",
        "description": "Giảm đáng kể hấp thu quinolone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Antacid", "Tetracycline"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid chelate với tetracycline, giảm hấp thu",
        "description": "Giảm hấp thu tetracycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Antacid", "Iron"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Antacid giảm hấp thu iron",
        "description": "Giảm hấp thu iron",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Antacid", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Antacid có thể giảm hấp thu digoxin",
        "description": "Giảm hấp thu digoxin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    # ========== METOCLOPRAMIDE ==========
    
    ("Metoclopramide", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Metoclopramide kéo dài QT nhẹ",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Thận trọng khi dùng với thuốc kéo dài QT",
        "references": "Micromedex"
    },
    
    ("Metoclopramide", "Anticholinergic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Đối kháng tác dụng",
        "description": "Giảm hiệu quả metoclopramide",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    # ========== DOMPERIDONE ==========
    
    ("Domperidone", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Domperidone kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Tránh dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    # ========== CHOLESTYRAMINE ==========
    
    ("Cholestyramine", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cholestyramine giảm hấp thu warfarin",
        "description": "Giảm hiệu quả chống đông",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Cholestyramine", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cholestyramine giảm hấp thu digoxin",
        "description": "Giảm hiệu quả digoxin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Cholestyramine", "Thyroid Hormone"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cholestyramine giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 4 giờ",
        "references": "Micromedex"
    },
    
    ("Cholestyramine", "Thiazide"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cholestyramine giảm hấp thu thiazide",
        "description": "Giảm hiệu quả thiazide",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    # ========== PPIs (continued) ==========
    
    ("PPI", "Clopidogrel"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "PPI (đặc biệt omeprazole, esomeprazole) ức chế CYP2C19, giảm tác dụng clopidogrel",
        "description": "Có thể làm giảm hiệu quả phòng ngừa đột quỵ/nhồi máu cơ tim",
        "management": "Cân nhắc dùng pantoprazole hoặc H2 blocker thay thế",
        "references": "FDA"
    },
    
    ("PPI", "Atazanavir"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "PPI làm giảm hấp thu atazanavir",
        "description": "Giảm đáng kể hiệu quả atazanavir",
        "management": "Tránh dùng chung. Cách xa ít nhất 12 giờ",
        "references": "FDA, Micromedex"
    },
    
    # ========== H2 BLOCKERS (continued) ==========
    
    ("Cimetidine", "Lidocaine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine ức chế chuyển hóa lidocaine, tăng nồng độ",
        "description": "Tăng nguy cơ độc tính lidocaine",
        "management": "Thận trọng khi dùng chung. Có thể cần giảm liều lidocaine",
        "references": "Micromedex"
    },
    
    ("Cimetidine", "Procainamide"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine ức chế chuyển hóa procainamide, tăng nồng độ",
        "description": "Tăng nguy cơ độc tính procainamide",
        "management": "Thận trọng khi dùng chung. Có thể cần giảm liều procainamide",
        "references": "Micromedex"
    },
    
    # ========== ANTACIDS (continued) ==========
    
    ("Antacid", "Ciprofloxacin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid (Ca, Mg, Al) chelate với ciprofloxacin, giảm hấp thu",
        "description": "Giảm đáng kể hấp thu ciprofloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Antacid", "Levofloxacin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid chelate với levofloxacin, giảm hấp thu",
        "description": "Giảm hấp thu levofloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
}

