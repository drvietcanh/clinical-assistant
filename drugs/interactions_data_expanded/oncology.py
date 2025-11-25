"""
Oncology Drug Interactions
Expanded database for oncology drug interactions
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

ONCOLOGY_INTERACTIONS = {
    # ========== METHOTREXATE ==========
    
    # Methotrexate + NSAID (already in main file)
    ("Methotrexate", "NSAID"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "NSAID làm giảm đào thải methotrexate, tăng nguy cơ độc tính",
        "description": "Tăng nguy cơ giảm bạch cầu, thiếu máu, nhiễm độc gan thận",
        "clinical_significance": "Nguy cơ độc tính methotrexate tăng đáng kể. Có thể gây suy thận cấp, tử vong.",
        "management": "Tránh dùng chung. Nếu cần: dùng liều thấp NSAID, theo dõi công thức máu, chức năng gan thận",
        "references": "Micromedex"
    },
    
    # Methotrexate + TMP-SMX (already in main file)
    ("Methotrexate", "Trimethoprim-Sulfamethoxazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính methotrexate",
        "description": "Tăng nguy cơ giảm bạch cầu, thiếu máu, nhiễm độc gan thận",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: theo dõi công thức máu thường xuyên",
        "references": "AHFS Drug Information"
    },
    
    ("Methotrexate", "Penicillin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Penicillin làm giảm đào thải methotrexate",
        "description": "Tăng nguy cơ độc tính methotrexate",
        "management": "Theo dõi công thức máu khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Methotrexate", "PPI"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "PPI có thể tăng nồng độ methotrexate",
        "description": "Tăng nguy cơ độc tính methotrexate",
        "management": "Thận trọng khi dùng chung. Theo dõi công thức máu",
        "references": "Micromedex"
    },
    
    ("Methotrexate", "Probenecid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Probenecid làm giảm đào thải methotrexate",
        "description": "Tăng nguy cơ độc tính methotrexate",
        "management": "Tránh dùng chung. Nếu cần: giảm liều methotrexate",
        "references": "Micromedex"
    },
    
    # ========== 5-FLUOROURACIL (5-FU) ==========
    
    ("5-Fluorouracil", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "5-FU ức chế chuyển hóa warfarin, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Giảm liều warfarin 30-50%. Theo dõi INR 2-3 lần/tuần",
        "references": "Micromedex"
    },
    
    ("5-Fluorouracil", "Phenytoin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "5-FU có thể tăng nồng độ phenytoin",
        "description": "Tăng nguy cơ độc tính phenytoin",
        "management": "Theo dõi nồng độ phenytoin",
        "references": "Micromedex"
    },
    
    # ========== CYCLOPHOSPHAMIDE ==========
    
    ("Cyclophosphamide", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng cyclophosphamide",
        "references": "Micromedex"
    },
    
    ("Cyclophosphamide", "Allopurinol"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Allopurinol có thể tăng độc tính cyclophosphamide",
        "description": "Tăng nguy cơ độc tính",
        "management": "Thận trọng khi dùng chung. Theo dõi công thức máu",
        "references": "Micromedex"
    },
    
    # ========== DOXORUBICIN ==========
    
    ("Doxorubicin", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Doxorubicin kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Tránh dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    ("Doxorubicin", "Trastuzumab"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính tim",
        "description": "Tăng nguy cơ suy tim",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng tim",
        "references": "Micromedex"
    },
    
    # ========== PACLITAXEL ==========
    
    ("Paclitaxel", "CYP3A4 Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "CYP3A4 inhibitor tăng nồng độ paclitaxel",
        "description": "Tăng nguy cơ độc tính paclitaxel",
        "management": "Thận trọng khi dùng với ketoconazole, clarithromycin, etc.",
        "references": "Micromedex"
    },
    
    ("Paclitaxel", "CYP3A4 Inducer"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "CYP3A4 inducer giảm nồng độ paclitaxel",
        "description": "Giảm hiệu quả paclitaxel",
        "management": "Thận trọng khi dùng với rifampin, carbamazepine, etc.",
        "references": "Micromedex"
    },
    
    # ========== IMATINIB ==========
    
    ("Imatinib", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Imatinib ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Tránh dùng chung. Cân nhắc dùng LMWH thay thế",
        "references": "Micromedex"
    },
    
    ("Imatinib", "CYP3A4 Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "CYP3A4 inhibitor tăng nồng độ imatinib",
        "description": "Tăng nguy cơ độc tính imatinib",
        "management": "Thận trọng khi dùng với ketoconazole, clarithromycin, etc.",
        "references": "Micromedex"
    },
    
    ("Imatinib", "CYP3A4 Inducer"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "CYP3A4 inducer giảm nồng độ imatinib",
        "description": "Giảm hiệu quả imatinib",
        "management": "Thận trọng khi dùng với rifampin, carbamazepine, etc.",
        "references": "Micromedex"
    },
    
    # ========== SORAFENIB ==========
    
    ("Sorafenib", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng sorafenib",
        "references": "Micromedex"
    },
    
    # ========== SUNITINIB ==========
    
    ("Sunitinib", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Sunitinib kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Tránh dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    # ========== VINCRISTINE ==========
    
    ("Vincristine", "CYP3A4 Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "CYP3A4 inhibitor tăng nồng độ vincristine",
        "description": "Tăng nguy cơ độc tính thần kinh",
        "management": "Thận trọng khi dùng với ketoconazole, clarithromycin, etc.",
        "references": "Micromedex"
    },
    
    # ========== CISPLATIN ==========
    
    ("Cisplatin", "Aminoglycoside"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính thận",
        "description": "Tăng nguy cơ suy thận",
        "management": "Tránh dùng chung nếu có thể. Theo dõi chức năng thận sát",
        "references": "Micromedex"
    },
    
    ("Cisplatin", "Loop Diuretic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng độc tính thận",
        "description": "Tăng nguy cơ suy thận",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận",
        "references": "Micromedex"
    },
    
    # ========== BUSULFAN ==========
    
    ("Busulfan", "Metronidazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Metronidazole ức chế chuyển hóa busulfan",
        "description": "Tăng nguy cơ độc tính busulfan",
        "management": "Tránh dùng chung. Nếu cần: giảm liều busulfan",
        "references": "Micromedex"
    },
    
    # ========== IMMUNOSUPPRESSANTS ==========
    
    ("Cyclosporine", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa cyclosporine",
        "description": "Tăng nồng độ cyclosporine",
        "management": "Theo dõi nồng độ cyclosporine, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Cyclosporine", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế chuyển hóa cyclosporine",
        "description": "Tăng nồng độ cyclosporine",
        "management": "Theo dõi nồng độ cyclosporine, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Cyclosporine", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế chuyển hóa cyclosporine",
        "description": "Tăng nồng độ cyclosporine",
        "management": "Giảm liều cyclosporine 50-75% khi dùng ketoconazole",
        "references": "Micromedex"
    },
    
    ("Tacrolimus", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa tacrolimus",
        "description": "Tăng nồng độ tacrolimus",
        "management": "Theo dõi nồng độ tacrolimus, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Tacrolimus", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế chuyển hóa tacrolimus",
        "description": "Tăng nồng độ tacrolimus",
        "management": "Theo dõi nồng độ tacrolimus, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Tacrolimus", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế chuyển hóa tacrolimus",
        "description": "Tăng nồng độ tacrolimus",
        "management": "Giảm liều tacrolimus 50-75% khi dùng ketoconazole",
        "references": "Micromedex"
    },
}

