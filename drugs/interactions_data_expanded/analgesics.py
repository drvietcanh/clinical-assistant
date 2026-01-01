"""
Analgesics Drug Interactions
Expanded database for analgesics (NSAIDs, Opioids, Acetaminophen)
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

ANALGESICS_INTERACTIONS = {
    # ========== NSAIDs ==========
    
    # Warfarin + Ibuprofen
    ("Warfarin", "Ibuprofen"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết",
        "description": "NSAID làm tăng nguy cơ xuất huyết dạ dày và tăng tác dụng chống đông",
        "clinical_significance": "Nguy cơ xuất huyết dạ dày-ruột tăng 2-4 lần. Có thể gây xuất huyết nặng, đặc biệt ở người cao tuổi.",
        "management": "Tránh dùng chung. Dùng Paracetamol thay thế nếu cần giảm đau/sốt",
        "alternatives": {
            "for_ibuprofen": ["Paracetamol", "Acetaminophen"],
            "for_warfarin": ["Dabigatran", "Rivaroxaban", "Apixaban"]
        },
        "references": "Micromedex"
    },
    
    ("Warfarin", "Naproxen"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "description": "NSAID làm tăng nguy cơ xuất huyết dạ dày và tăng tác dụng chống đông",
        "management": "Tránh dùng chung. Dùng Paracetamol thay thế",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Diclofenac"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "description": "NSAID làm tăng nguy cơ xuất huyết",
        "management": "Tránh dùng chung. Dùng Paracetamol thay thế",
        "references": "Micromedex"
    },
    
    ("NSAID", "ACE Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "NSAID làm giảm tác dụng hạ huyết áp của ACE inhibitor và tăng nguy cơ suy thận",
        "description": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận",
        "management": "Thận trọng khi dùng chung. Theo dõi huyết áp và chức năng thận",
        "references": "Micromedex"
    },
    
    ("NSAID", "ARB"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "NSAID làm giảm tác dụng hạ huyết áp của ARB và tăng nguy cơ suy thận",
        "description": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận",
        "management": "Thận trọng khi dùng chung. Theo dõi huyết áp và chức năng thận",
        "references": "Micromedex"
    },
    
    ("NSAID", "Lithium"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "NSAID làm giảm đào thải lithium",
        "description": "Tăng nồng độ lithium",
        "management": "Theo dõi nồng độ lithium khi dùng NSAID",
        "references": "Micromedex"
    },
    
    ("NSAID", "Methotrexate"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "NSAID làm giảm đào thải methotrexate, tăng nguy cơ độc tính",
        "description": "Tăng nguy cơ giảm bạch cầu, thiếu máu, nhiễm độc gan thận",
        "management": "Tránh dùng chung. Nếu cần: dùng liều thấp NSAID, theo dõi công thức máu, chức năng gan thận",
        "references": "Micromedex"
    },
    
    ("NSAID", "Aspirin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột. Ibuprofen có thể ức chế tác dụng bảo vệ tim mạch của aspirin.",
        "description": "Tăng nguy cơ xuất huyết dạ dày-ruột, giảm hiệu quả aspirin",
        "management": "Thận trọng khi dùng chung. Uống aspirin ít nhất 30 phút trước hoặc 8 giờ sau khi uống ibuprofen.",
        "references": "Micromedex, FDA"
    },
    
    ("NSAID", "Corticosteroid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "description": "Tăng nguy cơ xuất huyết dạ dày-ruột nặng",
        "management": "Thận trọng khi dùng chung. Dùng PPI bảo vệ dạ dày",
        "references": "Micromedex"
    },
    
    ("Celecoxib", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Celecoxib có thể tăng nguy cơ xuất huyết",
        "description": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "management": "Theo dõi INR khi dùng celecoxib",
        "references": "Micromedex"
    },
    
    ("Meloxicam", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Meloxicam có thể tăng nguy cơ xuất huyết",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng meloxicam",
        "references": "Micromedex"
    },

    ("Indomethacin", "Lithium"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Indomethacin làm giảm đào thải lithium",
        "description": "Tăng nồng độ lithium mạnh hơn các NSAID khác",
        "management": "Theo dõi nồng độ lithium sát sao",
        "references": "Micromedex"
    },

    ("Ketorolac", "NSAID"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết tiêu hóa nghiêm trọng",
        "description": "Chống chỉ định dùng chung Ketorolac với các NSAID khác",
        "management": "CHỐNG CHỈ ĐỊNH DÙNG CHUNG",
        "references": "FDA Boxed Warning"
    },

    # ========== OPIOIDS ==========
    
    ("Opioid", "Benzodiazepine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương và hô hấp",
        "description": "Tăng nguy cơ suy hô hấp, tử vong",
        "clinical_significance": "Nguy cơ suy hô hấp và tử vong tăng đáng kể.",
        "management": "Thận trọng khi dùng chung. Dùng liều thấp, theo dõi sát",
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    ("Opioid", "Alcohol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương và hô hấp",
        "description": "Tăng nguy cơ suy hô hấp, tử vong",
        "management": "Tránh uống rượu khi dùng opioid",
        "references": "Micromedex"
    },
    
    ("Opioid", "MAO Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin và phản ứng nghiêm trọng",
        "description": "Tăng nguy cơ hội chứng serotonin, suy hô hấp",
        "management": "TRÁNH DÙNG CHUNG",
        "references": "FDA, Micromedex"
    },
    
    ("Tramadol", "SSRI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ co giật, nhầm lẫn, hôn mê",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("Tramadol", "SNRI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("Tramadol", "MAO Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin nặng",
        "management": "TRÁNH DÙNG CHUNG",
        "references": "FDA, Micromedex"
    },
    
    ("Tramadol", "Carbamazepine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Carbamazepine cảm ứng chuyển hóa tramadol",
        "description": "Giảm hiệu quả tramadol",
        "management": "Có thể cần tăng liều tramadol",
        "references": "Micromedex"
    },

    ("Tramadol", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tramadol có thể làm tăng INR",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR và triệu chứng xuất huyết",
        "references": "Micromedex"
    },

    ("Fentanyl", "CYP3A4 Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "CYP3A4 inhibitor (Ketoconazole, Erythromycin...) tăng nồng độ fentanyl",
        "description": "Tăng nguy cơ suy hô hấp, tử vong",
        "management": "Giảm liều fentanyl khi dùng CYP3A4 inhibitor, theo dõi hô hấp",
        "references": "Micromedex"
    },
    
    ("Methadone", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Methadone kéo dài khoảng QT",
        "description": "Tăng nguy cơ xoắn đỉnh (Torsades de pointes)",
        "management": "Tránh dùng chung, theo dõi ECG",
        "references": "FDA"
    },

    # ========== ACETAMINOPHEN (PARACETAMOL) ==========

    ("Acetaminophen", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Liều cao acetaminophen (>2g/ngày) kéo dài dùng >1 tuần có thể làm tăng INR",
        "description": "Tăng nguy cơ xuất huyết ở liều cao kéo dài",
        "management": "Theo dõi INR nếu dùng paracetamol liều cao kéo dài",
        "references": "Micromedex"
    },

    ("Acetaminophen", "Alcohol"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ độc tính trên gan",
        "description": "Nguy cơ tổn thương gan khi dùng quá liều hoặc ở người nghiện rượu",
        "management": "Hạn chế rượu, không dùng quá liều tối đa (4g/ngày)",
        "references": "FDA"
    },
    
    ("Acetaminophen", "Isoniazid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ độc tính trên gan",
        "description": "Tăng nguy cơ tổn thương gan",
        "management": "Thận trọng và theo dõi chức năng gan",
        "references": "Micromedex"
    },

    # ========== MUSCLE RELAXANTS ==========
    
    ("Cyclobenzaprine", "MAO Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tương tự cấu trúc TCA, có thể gây hội chứng serotonin hoặc cơn tăng huyết áp",
        "description": "Nguy cơ cao, chống chỉ định",
        "management": "CHỐNG CHỈ ĐỊNH DÙNG CHUNG. Cách nhau 14 ngày",
        "references": "Micromedex"
    },

    ("Cyclobenzaprine", "Serotonergic Agents"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Nguy cơ khi dùng với SSRI, SNRI, Tramadol",
        "management": "Theo dõi triệu chứng hội chứng serotonin",
        "references": "Micromedex"
    },

    # ========== GABAPENTINOIDS ==========
    
    ("Gabapentin", "Opioid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ, suy hô hấp",
        "clinical_significance": "Kết hợp này làm tăng nguy cơ tử vong do opioid.",
        "management": "Thận trọng dùng liều thấp nhất có hiệu quả, theo dõi hô hấp",
        "references": "FDA Warning 2019"
    },
    
    ("Pregabalin", "Opioid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ, suy hô hấp",
        "clinical_significance": "Kết hợp này làm tăng nguy cơ tử vong do opioid.",
        "management": "Thận trọng dùng liều thấp nhất có hiệu quả, theo dõi hô hấp",
        "references": "FDA Warning 2019"
    }
}
