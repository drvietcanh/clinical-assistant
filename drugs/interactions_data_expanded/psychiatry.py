"""
Psychiatry Drug Interactions
Expanded database for psychiatry drug interactions
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

PSYCHIATRY_INTERACTIONS = {
    # ========== SSRIs (Selective Serotonin Reuptake Inhibitors) ==========
    
    # Fluoxetine + Warfarin (already in main file)
    ("Fluoxetine", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Fluoxetine ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu/dừng fluoxetine. Cân nhắc giảm liều warfarin",
        "references": "Micromedex"
    },
    
    # Fluoxetine + Tramadol (already in main file)
    ("Fluoxetine", "Tramadol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ co giật, nhầm lẫn, hôn mê",
        "clinical_significance": "Nguy cơ hội chứng serotonin tăng đáng kể. Có thể gây tử vong.",
        "management": "Tránh dùng chung. Nếu cần thiết: dùng liều thấp, theo dõi sát",
        "references": "Micromedex"
    },
    
    ("Fluoxetine", "MAO Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin nặng, có thể tử vong",
        "clinical_significance": "Nguy cơ hội chứng serotonin rất cao. Có thể tử vong.",
        "management": "TRÁNH DÙNG CHUNG. Cách xa ít nhất 14 ngày sau khi ngừng MAO inhibitor",
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    ("Fluoxetine", "Tricyclic Antidepressant"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Fluoxetine ức chế chuyển hóa TCA, tăng nồng độ TCA",
        "description": "Tăng nguy cơ độc tính TCA (rối loạn nhịp tim, co giật)",
        "management": "Tránh dùng chung. Nếu cần: giảm liều TCA, theo dõi nồng độ TCA",
        "references": "Micromedex"
    },
    
    ("Sertraline", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    
    ("Sertraline", "Tramadol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("Paroxetine", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Paroxetine ức chế CYP2D6, có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },
    
    ("Paroxetine", "Tramadol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("Citalopram", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Citalopram kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim (torsades de pointes)",
        "management": "Tránh dùng với thuốc kéo dài QT. Giới hạn liều citalopram ≤40mg/ngày",
        "references": "FDA, Micromedex"
    },
    
    ("Escitalopram", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Escitalopram kéo dài QT nhẹ",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Thận trọng khi dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    # ========== SNRIs (Serotonin-Norepinephrine Reuptake Inhibitors) ==========
    
    ("Venlafaxine", "MAO Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin nặng",
        "management": "TRÁNH DÙNG CHUNG. Cách xa ít nhất 14 ngày",
        "references": "FDA, Micromedex"
    },
    
    ("Venlafaxine", "Tramadol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("Duloxetine", "MAO Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin nặng",
        "management": "TRÁNH DÙNG CHUNG. Cách xa ít nhất 14 ngày",
        "references": "FDA, Micromedex"
    },
    
    ("Duloxetine", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng duloxetine",
        "references": "Micromedex"
    },
    
    # ========== TRICYCLIC ANTIDEPRESSANTS (TCAs) ==========
    
    ("Tricyclic Antidepressant", "MAO Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin và tăng huyết áp",
        "description": "Tăng nguy cơ hội chứng serotonin nặng, tăng huyết áp",
        "management": "TRÁNH DÙNG CHUNG. Cách xa ít nhất 14 ngày",
        "references": "FDA, Micromedex"
    },
    
    ("Tricyclic Antidepressant", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "TCA kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Tránh dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    ("Tricyclic Antidepressant", "Anticholinergic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng anticholinergic",
        "description": "Tăng nguy cơ khô miệng, bí tiểu, nhầm lẫn",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Tricyclic Antidepressant", "Clonidine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "TCA đối kháng tác dụng hạ huyết áp của clonidine",
        "description": "Giảm hiệu quả hạ huyết áp",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    # ========== MOOD STABILIZERS ==========
    
    ("Lithium", "ACE Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "ACE inhibitor làm giảm đào thải lithium, tăng nồng độ lithium",
        "description": "Tăng nguy cơ độc tính lithium",
        "management": "Theo dõi nồng độ lithium khi bắt đầu/dừng ACE inhibitor. Cân nhắc giảm liều lithium",
        "references": "Micromedex"
    },
    
    ("Lithium", "ARB"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "ARB có thể tăng nồng độ lithium",
        "description": "Tăng nguy cơ độc tính lithium",
        "management": "Theo dõi nồng độ lithium khi dùng ARB",
        "references": "Micromedex"
    },
    
    ("Lithium", "Thiazide"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Thiazide làm giảm đào thải lithium, tăng nồng độ lithium",
        "description": "Tăng nguy cơ độc tính lithium",
        "clinical_significance": "Nồng độ lithium có thể tăng 2-3 lần. Nguy cơ độc tính lithium nặng.",
        "management": "Giảm liều lithium 30-50% khi dùng thiazide. Theo dõi nồng độ lithium",
        "references": "Micromedex"
    },
    
    ("Lithium", "NSAID"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "NSAID làm giảm đào thải lithium",
        "description": "Tăng nồng độ lithium",
        "management": "Theo dõi nồng độ lithium khi dùng NSAID",
        "references": "Micromedex"
    },
    
    ("Lithium", "Metronidazole"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng nồng độ lithium",
        "description": "Tăng nguy cơ độc tính lithium",
        "management": "Theo dõi nồng độ lithium khi dùng metronidazole",
        "references": "Micromedex"
    },
    
    ("Lithium", "Theophylline"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Theophylline làm tăng đào thải lithium, giảm nồng độ lithium",
        "description": "Giảm hiệu quả lithium",
        "management": "Tăng liều lithium khi dùng theophylline. Theo dõi nồng độ lithium",
        "references": "Micromedex"
    },
    
    ("Lithium", "Caffeine"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Caffeine có thể tăng đào thải lithium nhẹ",
        "description": "Giảm nhẹ nồng độ lithium",
        "management": "Theo dõi nồng độ lithium",
        "references": "Micromedex"
    },
    
    # ========== ANTIPSYCHOTICS ==========
    
    ("Haloperidol", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Haloperidol kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Tránh dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    ("Risperidone", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Risperidone kéo dài QT nhẹ",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Thận trọng khi dùng với thuốc kéo dài QT",
        "references": "Micromedex"
    },
    
    ("Olanzapine", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Olanzapine kéo dài QT nhẹ",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Thận trọng khi dùng với thuốc kéo dài QT",
        "references": "Micromedex"
    },
    
    ("Quetiapine", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Quetiapine kéo dài QT nhẹ",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Thận trọng khi dùng với thuốc kéo dài QT",
        "references": "Micromedex"
    },
    
    ("Antipsychotic", "Anticholinergic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng anticholinergic",
        "description": "Tăng nguy cơ khô miệng, bí tiểu, nhầm lẫn",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    # ========== BENZODIAZEPINES ==========
    
    # Diphenhydramine + Benzodiazepine (already in main file)
    ("Diphenhydramine", "Benzodiazepine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng an thần, ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ quá mức, suy hô hấp",
        "management": "Tránh dùng chung. Nếu cần: dùng liều thấp, theo dõi sát",
        "references": "Micromedex"
    },
    
    ("Benzodiazepine", "Alcohol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ quá mức, suy hô hấp, tử vong",
        "management": "Tránh uống rượu khi dùng benzodiazepine",
        "references": "Micromedex"
    },
    
    ("Benzodiazepine", "Opioid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương và hô hấp",
        "description": "Tăng nguy cơ suy hô hấp, tử vong",
        "clinical_significance": "Nguy cơ suy hô hấp và tử vong tăng đáng kể.",
        "management": "Thận trọng khi dùng chung. Dùng liều thấp, theo dõi sát",
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    ("Benzodiazepine", "Cimetidine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine ức chế chuyển hóa benzodiazepine, tăng nồng độ",
        "description": "Tăng tác dụng an thần",
        "management": "Thận trọng khi dùng chung. Có thể cần giảm liều benzodiazepine",
        "references": "Micromedex"
    },
    
    # ========== MAO INHIBITORS ==========
    
    ("MAO Inhibitor", "SSRI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin nặng, có thể tử vong",
        "management": "TRÁNH DÙNG CHUNG. Cách xa ít nhất 14 ngày",
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    ("MAO Inhibitor", "SNRI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin nặng",
        "management": "TRÁNH DÙNG CHUNG. Cách xa ít nhất 14 ngày",
        "references": "FDA, Micromedex"
    },
    
    ("MAO Inhibitor", "Tramadol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin nặng",
        "management": "TRÁNH DÙNG CHUNG",
        "references": "FDA, Micromedex"
    },
    
    ("MAO Inhibitor", "Tyramine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "MAO inhibitor + tyramine (trong thực phẩm) gây tăng huyết áp nặng",
        "description": "Tăng nguy cơ tăng huyết áp nặng, đột quỵ",
        "clinical_significance": "Tăng huyết áp có thể rất nặng, gây đột quỵ, tử vong.",
        "management": "Tránh thực phẩm giàu tyramine (phô mai, rượu vang đỏ, thịt chế biến)",
        "references": "Micromedex"
    },
    
    ("MAO Inhibitor", "Dextromethorphan"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
}

