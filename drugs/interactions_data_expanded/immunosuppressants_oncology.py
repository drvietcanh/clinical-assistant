"""
Immunosuppressants and Oncology Drug Interactions
Expanded database for immunosuppressants and oncology drugs
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

IMMUNOSUPPRESSANTS_ONCOLOGY_INTERACTIONS = {
    # ========== IMMUNOSUPPRESSANTS (General) ==========

    # Azathioprine
    ("Azathioprine", "Allopurinol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Allopurinol ức chế xanthine oxidase, enzym chuyển hóa azathioprine/6-MP",
        "description": "Tăng nồng độ 6-MP gấp 4 lần, gây suy tủy nghiêm trọng",
        "clinical_significance": "Nguy cơ suy tủy xương, nhiễm trùng, tử vong.",
        "management": "Giảm liều azathioprine xuống còn 25-33% liều bình thường khi dùng chung với allopurinol. Theo dõi sát công thức máu.",
        "references": "FDA Boxed Warning, Micromedex"
    },

    ("Azathioprine", "Febuxostat"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Febuxostat ức chế xanthine oxidase, tăng nồng độ chất chuyển hóa độc hại của azathioprine",
        "description": "Nguy cơ suy tủy nghiêm trọng",
        "management": "CHỐNG CHỈ ĐỊNH DÙNG CHUNG",
        "references": "Micromedex"
    },

    # Mycophenolate
    ("Mycophenolate", "Antacid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Antacid chứa nhôm/magie làm giảm hấp thu mycophenolate",
        "description": "Giảm hiệu quả bảo vệ cơ quan ghép",
        "management": "Uống cách nhau ít nhất 2 giờ",
        "references": "Micromedex"
    },

    ("Mycophenolate", "Cholestyramine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cholestyramine làm giảm tái hấp thu mycophenolate (chu trình gan ruột)",
        "description": "Giảm nồng độ thuốc đáng kể",
        "management": "Tránh dùng chung nếu có thể, hoặc theo dõi nồng độ",
        "references": "Micromedex"
    },
    
    # Cyclosporine (Migrated from other.py + Expanded)
    ("Cyclosporine", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa cyclosporine",
        "description": "Tăng nồng độ cyclosporine",
        "management": "Theo dõi nồng độ cyclosporine, giảm liều",
        "references": "Micromedex"
    },
    
    ("Cyclosporine", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế chuyển hóa cyclosporine",
        "description": "Tăng nồng độ cyclosporine",
        "management": "Theo dõi nồng độ cyclosporine, giảm liều",
        "references": "Micromedex"
    },
    
    ("Cyclosporine", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế chuyển hóa cyclosporine",
        "description": "Tăng nồng độ cyclosporine",
        "management": "Giảm liều cyclosporine 50-75% khi dùng ketoconazole",
        "references": "Micromedex"
    },

    ("Cyclosporine", "St. John's Wort"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "St. John's Wort cảm ứng CYP3A4, giảm nồng độ cyclosporine",
        "description": "Giảm đáng kể hiệu quả cyclosporine, nguy cơ thải ghép",
        "management": "Tránh dùng chung. Theo dõi nồng độ cyclosporine",
        "references": "FDA, Micromedex"
    },
    
    ("Cyclosporine", "Statin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cạnh tranh CYP3A4 và OATP1B1, tăng nồng độ statin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Tránh dùng với simvastatin/lovastatin liều cao. Các statin khác dùng liều thấp.",
        "references": "FDA"
    },

    # Tacrolimus (Migrated from other.py + Expanded)
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

    ("Tacrolimus", "St. John's Wort"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "St. John's Wort cảm ứng CYP3A4, giảm nồng độ tacrolimus",
        "description": "Giảm đáng kể hiệu quả tacrolimus, nguy cơ thải ghép",
        "management": "Tránh dùng chung. Theo dõi nồng độ tacrolimus",
        "references": "FDA, Micromedex"
    },

    ("Rifampin", "Cyclosporine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rifampin cảm ứng CYP3A4/P-gp → giảm mạnh nồng độ cyclosporine",
        "description": "Nguy cơ thải ghép hoặc bùng phát bệnh nền",
        "management": "Tránh phối hợp; nếu bắt buộc, tăng liều và theo dõi nồng độ cyclosporine rất sát.",
        "references": "Micromedex, Transplant Guidelines"
    },

    ("Rifampin", "Tacrolimus"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cảm ứng CYP3A4/P-gp → giảm mạnh nồng độ tacrolimus",
        "description": "Tăng nguy cơ thải ghép/đợt cấp",
        "management": "Tránh phối hợp; nếu bắt buộc dùng rifampin, cần tăng liều tacrolimus đáng kể và theo dõi nồng độ huyết tương.",
        "references": "Micromedex, Transplant Guidelines"
    },

    ("Rifampin", "Lopinavir/ritonavir"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cảm ứng CYP3A4 mạnh → giảm nồng độ PI; rifampin cũng bị ảnh hưởng",
        "description": "Giảm hiệu quả điều trị HIV, nguy cơ kháng thuốc",
        "management": "Tránh phối hợp. Dùng rifabutin (liều giảm) hoặc đổi phác đồ ARV phù hợp.",
        "references": "WHO HIV/TB Guidelines"
    },

    # ========== METHOTREXATE ==========
    
    ("Methotrexate", "NSAID"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "NSAID làm giảm đào thải methotrexate, tăng nguy cơ độc tính",
        "description": "Tăng nguy cơ giảm bạch cầu, thiếu máu, nhiễm độc gan thận",
        "clinical_significance": "Nguy cơ độc tính methotrexate tăng đáng kể. Có thể gây suy thận cấp, tử vong.",
        "management": "Tránh dùng chung. Nếu cần: dùng liều thấp NSAID, theo dõi công thức máu, chức năng gan thận",
        "references": "Micromedex"
    },
    
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
    
    # ========== ONCOLOGY - CHEMOTHERAPY (Migrated from oncology.py) ==========
    
    # 5-Fluorouracil (5-FU)
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
    
    # Cyclophosphamide
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
    
    # Doxorubicin
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
    
    # Paclitaxel
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
    
    # Imatinib
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
    
    # Sorafenib
    ("Sorafenib", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng sorafenib",
        "references": "Micromedex"
    },
    
    # Sunitinib
    ("Sunitinib", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Sunitinib kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Tránh dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    # Vincristine
    ("Vincristine", "CYP3A4 Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "CYP3A4 inhibitor tăng nồng độ vincristine",
        "description": "Tăng nguy cơ độc tính thần kinh",
        "management": "Thận trọng khi dùng với ketoconazole, clarithromycin, etc.",
        "references": "Micromedex"
    },
    
    # Cisplatin
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
    
    # Busulfan
    ("Busulfan", "Metronidazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Metronidazole ức chế chuyển hóa busulfan",
        "description": "Tăng nguy cơ độc tính busulfan",
        "management": "Tránh dùng chung. Nếu cần: giảm liều busulfan",
        "references": "Micromedex"
    },
    
    # Tamoxifen
    ("Tamoxifen", "CYP2D6 Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "CYP2D6 (Fluoxetine, Paroxetine...) chuyển hóa tamoxifen thành dạng hoạt động. Ức chế CYP2D6 làm giảm hiệu quả tamoxifen.",
        "description": "Giảm hiệu quả điều trị ung thư vú",
        "management": "Tránh dùng với thuốc ức chế mạnh CYP2D6 (như fluoxetine, paroxetine). Dùng venlafaxine nếu cần thuốc chống trầm cảm.",
        "references": "Clinical Pharmacology"
    }
}
