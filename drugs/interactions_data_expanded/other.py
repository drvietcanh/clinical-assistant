"""
Other Drug Interactions
Expanded database for other drug class interactions
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

OTHER_INTERACTIONS = {
    # ========== NSAIDs ==========
    
    # Warfarin + Ibuprofen (already in main file)
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
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "description": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "management": "Thận trọng khi dùng chung. Dùng PPI bảo vệ dạ dày",
        "references": "Micromedex"
    },
    
    ("NSAID", "Corticosteroid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "description": "Tăng nguy cơ xuất huyết dạ dày-ruột nặng",
        "management": "Thận trọng khi dùng chung. Dùng PPI bảo vệ dạ dày",
        "references": "Micromedex"
    },
    
    ("NSAID", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết",
        "description": "NSAID làm tăng nguy cơ xuất huyết dạ dày và tăng tác dụng chống đông",
        "management": "Tránh dùng chung. Dùng Paracetamol thay thế",
        "references": "Micromedex"
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
    
    ("Morphine", "Phenytoin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Phenytoin có thể giảm tác dụng morphine",
        "description": "Giảm hiệu quả giảm đau",
        "management": "Có thể cần tăng liều morphine",
        "references": "Micromedex"
    },
    
    ("Codeine", "CYP2D6 Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "CYP2D6 inhibitor giảm chuyển hóa codeine thành morphine",
        "description": "Giảm hiệu quả giảm đau của codeine",
        "management": "Cân nhắc dùng opioid khác",
        "references": "Micromedex"
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
    
    # ========== CORTICOSTEROIDS ==========
    
    ("Corticosteroid", "NSAID"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "description": "Tăng nguy cơ xuất huyết dạ dày-ruột nặng",
        "management": "Thận trọng khi dùng chung. Dùng PPI bảo vệ dạ dày",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid có thể tăng hoặc giảm tác dụng warfarin",
        "description": "Tác dụng không dự đoán được",
        "management": "Theo dõi INR khi bắt đầu/dừng corticosteroid",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Insulin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid làm tăng đường huyết, giảm tác dụng insulin",
        "description": "Giảm hiệu quả insulin",
        "management": "Tăng liều insulin khi dùng corticosteroid. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Antidiabetic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid làm tăng đường huyết",
        "description": "Giảm hiệu quả thuốc hạ đường huyết",
        "management": "Tăng liều thuốc hạ đường huyết. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Diuretic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid gây giữ natri, giảm tác dụng lợi tiểu",
        "description": "Giảm hiệu quả lợi tiểu",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid gây hạ kali máu, tăng nguy cơ ngộ độc digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi kali máu và nồng độ digoxin",
        "references": "Micromedex"
    },
    
    # ========== ANTIHISTAMINES ==========
    
    # Diphenhydramine + Benzodiazepine (already in main file)
    ("Diphenhydramine", "Benzodiazepine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng an thần, ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ quá mức, suy hô hấp",
        "management": "Tránh dùng chung. Nếu cần: dùng liều thấp, theo dõi sát",
        "references": "Micromedex"
    },
    
    ("Diphenhydramine", "Alcohol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ quá mức, suy hô hấp",
        "management": "Tránh uống rượu khi dùng diphenhydramine",
        "references": "Micromedex"
    },
    
    ("Diphenhydramine", "Opioid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ suy hô hấp",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Loratadine", "Ketoconazole"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ketoconazole ức chế chuyển hóa loratadine",
        "description": "Tăng nồng độ loratadine",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    # ========== ANTIFUNGALS ==========
    
    # Ketoconazole + Warfarin (already in main file)
    ("Ketoconazole", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Giảm liều warfarin 30-50%. Theo dõi INR 2-3 lần/tuần",
        "references": "Micromedex"
    },
    
    ("Ketoconazole", "Simvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Tránh dùng chung. Nếu cần: giảm liều simvastatin",
        "references": "FDA, Micromedex"
    },
    
    ("Ketoconazole", "Atorvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế CYP3A4, tăng nồng độ atorvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Tránh dùng chung. Nếu cần: giảm liều atorvastatin",
        "references": "FDA, Micromedex"
    },
    
    ("Ketoconazole", "Cyclosporine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế chuyển hóa cyclosporine",
        "description": "Tăng nồng độ cyclosporine",
        "management": "Giảm liều cyclosporine 50-75% khi dùng ketoconazole",
        "references": "Micromedex"
    },
    
    ("Ketoconazole", "Tacrolimus"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế chuyển hóa tacrolimus",
        "description": "Tăng nồng độ tacrolimus",
        "management": "Giảm liều tacrolimus 50-75% khi dùng ketoconazole",
        "references": "Micromedex"
    },
    
    ("Fluconazole", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Fluconazole ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    
    ("Fluconazole", "Phenytoin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Fluconazole ức chế chuyển hóa phenytoin",
        "description": "Tăng nồng độ phenytoin",
        "management": "Theo dõi nồng độ phenytoin, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Itraconazole", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Itraconazole ức chế CYP3A4, có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },
    
    # ========== ANTIVIRALS ==========
    
    ("Ritonavir", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ritonavir ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng ritonavir",
        "references": "Micromedex"
    },
    
    ("Ritonavir", "Simvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ritonavir ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Tránh dùng chung. Cân nhắc dùng pravastatin hoặc rosuvastatin",
        "references": "FDA, Micromedex"
    },
    
    ("Ritonavir", "Atorvastatin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ritonavir ức chế CYP3A4, tăng nồng độ atorvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều atorvastatin. Theo dõi CK",
        "references": "Micromedex"
    },
    
    # ========== ANTICONVULSANTS ==========
    
    ("Phenytoin", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Phenytoin cảm ứng CYP2C9, giảm tác dụng warfarin. Cũng có thể ức chế trong một số trường hợp",
        "description": "Tương tác phức tạp, có thể tăng hoặc giảm tác dụng warfarin",
        "clinical_significance": "Tương tác không dự đoán được. INR có thể dao động.",
        "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin dựa trên INR",
        "references": "Micromedex"
    },
    
    ("Phenytoin", "Oral Contraceptive"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Phenytoin cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung hoặc chuyển sang biện pháp khác",
        "references": "Micromedex"
    },
    
    ("Phenytoin", "Folic Acid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Folic acid có thể giảm nồng độ phenytoin",
        "description": "Giảm hiệu quả phenytoin",
        "management": "Theo dõi nồng độ phenytoin khi bổ sung folic acid",
        "references": "Micromedex"
    },
    
    ("Carbamazepine", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Carbamazepine cảm ứng CYP2C9, giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tăng liều warfarin khi bắt đầu carbamazepine. Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },
    
    ("Carbamazepine", "Oral Contraceptive"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Carbamazepine cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung hoặc chuyển sang biện pháp khác",
        "references": "Micromedex"
    },
    
    ("Carbamazepine", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa carbamazepine, tăng nồng độ carbamazepine",
        "description": "Tăng nguy cơ độc tính carbamazepine",
        "management": "Theo dõi nồng độ carbamazepine, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Valproic Acid", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Valproic acid có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng valproic acid",
        "references": "Micromedex"
    },
    
    ("Valproic Acid", "Aspirin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ xuất huyết",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    # ========== ORAL CONTRACEPTIVES ==========
    
    # Oral Contraceptive + Antibiotics (already in main file)
    ("Oral Contraceptive", "Antibiotics"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Một số kháng sinh làm giảm hiệu quả tránh thai",
        "description": "Rifampin, một số kháng sinh phổ rộng có thể giảm hiệu quả",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung khi dùng kháng sinh",
        "references": "Clinical Pharmacology"
    },
    
    ("Oral Contraceptive", "Rifampin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rifampin cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "clinical_significance": "Hiệu quả tránh thai giảm đáng kể. Nguy cơ có thai cao.",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung (barrier method) hoặc chuyển sang biện pháp khác",
        "references": "Micromedex"
    },
    
    ("Oral Contraceptive", "Phenytoin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Phenytoin cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung hoặc chuyển sang biện pháp khác",
        "references": "Micromedex"
    },
    
    ("Oral Contraceptive", "Carbamazepine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Carbamazepine cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung hoặc chuyển sang biện pháp khác",
        "references": "Micromedex"
    },
    
    ("Oral Contraceptive", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng oral contraceptive",
        "references": "Micromedex"
    },
    
    # ========== THYROID HORMONES ==========
    
    ("Thyroid Hormone", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Thyroid hormone tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu/dừng thyroid hormone",
        "references": "Micromedex"
    },
    
    ("Thyroid Hormone", "Cholestyramine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cholestyramine giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 4 giờ",
        "references": "Micromedex"
    },
    
    ("Thyroid Hormone", "Iron"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Iron giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Thyroid Hormone", "Calcium"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Calcium giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    # ========== THEOPHYLLINE ==========
    
    ("Theophylline", "Ciprofloxacin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ciprofloxacin ức chế chuyển hóa theophylline, tăng nồng độ theophylline",
        "description": "Tăng nguy cơ ngộ độc theophylline (co giật, rối loạn nhịp tim)",
        "clinical_significance": "Nồng độ theophylline có thể tăng 2-3 lần. Nguy cơ co giật, rối loạn nhịp tim, tử vong.",
        "management": "Giảm liều theophylline 30-50%. Theo dõi nồng độ theophylline. Cân nhắc dùng levofloxacin thay thế",
        "alternatives": {
            "for_ciprofloxacin": ["Levofloxacin", "Moxifloxacin"]
        },
        "references": "Micromedex"
    },
    
    ("Theophylline", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa theophylline",
        "description": "Tăng nồng độ theophylline",
        "management": "Theo dõi nồng độ theophylline, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Theophylline", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế chuyển hóa theophylline",
        "description": "Tăng nồng độ theophylline",
        "management": "Theo dõi nồng độ theophylline",
        "references": "Micromedex"
    },
    
    ("Theophylline", "Cimetidine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine ức chế chuyển hóa theophylline",
        "description": "Tăng nồng độ theophylline",
        "management": "Theo dõi nồng độ theophylline, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Theophylline", "Rifampin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Rifampin cảm ứng chuyển hóa theophylline",
        "description": "Giảm nồng độ theophylline",
        "management": "Tăng liều theophylline khi dùng rifampin. Theo dõi nồng độ theophylline",
        "references": "Micromedex"
    },
    
    ("Theophylline", "Lithium"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Theophylline làm tăng đào thải lithium, giảm nồng độ lithium",
        "description": "Giảm hiệu quả lithium",
        "management": "Tăng liều lithium khi dùng theophylline. Theo dõi nồng độ lithium",
        "references": "Micromedex"
    },
    
    # ========== IRON ==========
    
    ("Iron", "Quinolone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Iron chelate với quinolone, giảm hấp thu",
        "description": "Giảm đáng kể hấp thu quinolone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Iron", "Tetracycline"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Iron chelate với tetracycline, giảm hấp thu",
        "description": "Giảm hấp thu tetracycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Iron", "Thyroid Hormone"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Iron giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Iron", "Levofloxacin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Iron chelate với levofloxacin, giảm hấp thu",
        "description": "Giảm hấp thu levofloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    # ========== CALCIUM ==========
    
    ("Calcium", "Quinolone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Calcium chelate với quinolone, giảm hấp thu",
        "description": "Giảm hấp thu quinolone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Calcium", "Tetracycline"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Calcium chelate với tetracycline, giảm hấp thu",
        "description": "Giảm hấp thu tetracycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Calcium", "Thyroid Hormone"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Calcium giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Calcium", "Ceftriaxone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ceftriaxone kết hợp với calcium tạo kết tủa không tan",
        "description": "Nguy cơ kết tủa trong phổi, thận, có thể tử vong",
        "management": "KHÔNG trộn ceftriaxone với calcium trong cùng một đường truyền. Cách xa ít nhất 48 giờ nếu dùng IV calcium",
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    # ========== HERBAL/SUPPLEMENTS ==========
    
    ("Ginkgo Biloba", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ginkgo có thể tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Tránh dùng chung. Theo dõi INR nếu cần dùng",
        "references": "Micromedex"
    },
    
    ("Ginseng", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ginseng có thể giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tránh dùng chung. Theo dõi INR nếu cần dùng",
        "references": "Micromedex"
    },
    
    ("St. John's Wort", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "St. John's Wort cảm ứng CYP2C9, giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("St. John's Wort", "Oral Contraceptive"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "St. John's Wort cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("St. John's Wort", "SSRI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("St. John's Wort", "Cyclosporine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "St. John's Wort cảm ứng chuyển hóa cyclosporine",
        "description": "Giảm nồng độ cyclosporine, nguy cơ thải ghép",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("Vitamin K", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Vitamin K là chất đối kháng của warfarin",
        "description": "Giảm hiệu quả chống đông",
        "clinical_significance": "INR có thể giảm đáng kể. Nguy cơ huyết khối tái phát.",
        "management": "Tránh bổ sung vitamin K không cần thiết. Nếu cần: điều chỉnh liều warfarin và theo dõi INR",
        "references": "Micromedex"
    },
}

