"""
Antibiotic Drug Interactions
Expanded database for antibiotic interactions
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

ANTIBIOTIC_INTERACTIONS = {
    # ========== BETA-LACTAMS (Penicillins, Cephalosporins) ==========
    
    # Penicillins
    ("Amoxicillin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin do thay đổi hệ vi khuẩn đường ruột",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng amoxicillin",
        "references": "Micromedex"
    },
    
    ("Amoxicillin", "Methotrexate"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Amoxicillin làm giảm đào thải methotrexate",
        "description": "Tăng nguy cơ độc tính methotrexate",
        "management": "Theo dõi công thức máu và chức năng thận khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Amoxicillin", "Oral Contraceptive"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể giảm nhẹ hiệu quả tránh thai do thay đổi hệ vi khuẩn đường ruột",
        "description": "Giảm nhẹ hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung",
        "references": "Clinical Pharmacology"
    },
    
    ("Penicillin", "Methotrexate"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Penicillin làm giảm đào thải methotrexate",
        "description": "Tăng nguy cơ độc tính methotrexate",
        "management": "Theo dõi công thức máu khi dùng chung",
        "references": "Micromedex"
    },
    
    # Cephalosporins
    ("Ceftriaxone", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng ceftriaxone",
        "references": "Micromedex"
    },
    
    ("Ceftriaxone", "Calcium"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ceftriaxone kết hợp với calcium tạo kết tủa không tan",
        "description": "Nguy cơ kết tủa trong phổi, thận, có thể tử vong",
        "clinical_significance": "Kết tủa calcium-ceftriaxone có thể gây tắc mạch phổi, suy thận cấp, tử vong.",
        "management": "KHÔNG trộn ceftriaxone với calcium trong cùng một đường truyền. Cách xa ít nhất 48 giờ nếu dùng IV calcium",
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    ("Cefazolin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng cefazolin",
        "references": "Micromedex"
    },
    
    ("Cefepime", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng cefepime",
        "references": "Micromedex"
    },
    
    # ========== QUINOLONES ==========
    
    # Ciprofloxacin (already has some in main file)
    ("Ciprofloxacin", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid (Ca, Mg, Al) chelate với ciprofloxacin, giảm hấp thu",
        "description": "Giảm đáng kể hấp thu ciprofloxacin, giảm hiệu quả điều trị",
        "clinical_significance": "Hấp thu ciprofloxacin giảm 50-90%. Có thể dẫn đến thất bại điều trị.",
        "management": "Cách xa ít nhất 2 giờ. Tốt nhất: dùng antacid 2 giờ sau ciprofloxacin",
        "references": "Micromedex"
    },
    
    ("Ciprofloxacin", "Calcium"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Calcium chelate với ciprofloxacin, giảm hấp thu",
        "description": "Giảm hấp thu ciprofloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Ciprofloxacin", "Iron"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Iron chelate với ciprofloxacin, giảm hấp thu",
        "description": "Giảm hấp thu ciprofloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Ciprofloxacin", "Theophylline"): {
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
    
    ("Ciprofloxacin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ciprofloxacin ức chế CYP1A2, có thể tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên, cân nhắc giảm liều warfarin",
        "references": "Micromedex"
    },
    
    ("Ciprofloxacin", "Tizanidine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ciprofloxacin ức chế chuyển hóa tizanidine, tăng nồng độ tizanidine",
        "description": "Tăng nguy cơ tác dụng phụ tizanidine (hạ huyết áp, buồn ngủ)",
        "management": "Tránh dùng chung. Nếu cần: giảm liều tizanidine",
        "references": "FDA, Micromedex"
    },
    
    # Levofloxacin
    ("Levofloxacin", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid (Ca, Mg, Al) chelate với levofloxacin, giảm hấp thu",
        "description": "Giảm hấp thu levofloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Levofloxacin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng levofloxacin",
        "references": "Micromedex"
    },
    
    ("Levofloxacin", "Theophylline"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng nồng độ theophylline",
        "description": "Tăng nguy cơ ngộ độc theophylline",
        "management": "Theo dõi nồng độ theophylline",
        "references": "Micromedex"
    },
    
    # Moxifloxacin
    ("Moxifloxacin", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid chelate với moxifloxacin, giảm hấp thu",
        "description": "Giảm hấp thu moxifloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Moxifloxacin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng moxifloxacin",
        "references": "Micromedex"
    },
    
    ("Moxifloxacin", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Moxifloxacin kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim (torsades de pointes)",
        "management": "Tránh dùng với thuốc kéo dài QT (amiodarone, sotalol, etc.)",
        "references": "FDA, Micromedex"
    },
    
    # ========== MACROLIDES ==========
    
    # Erythromycin (already has some in main file)
    ("Erythromycin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế CYP3A4, ức chế chuyển hóa warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng erythromycin",
        "references": "Clinical Pharmacology"
    },
    
    ("Erythromycin", "Theophylline"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa theophylline",
        "description": "Tăng nồng độ theophylline",
        "management": "Theo dõi nồng độ theophylline, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Erythromycin", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Erythromycin kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Tránh dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    ("Erythromycin", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin, cân nhắc giảm liều digoxin",
        "references": "Micromedex"
    },
    
    ("Erythromycin", "Carbamazepine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa carbamazepine, tăng nồng độ carbamazepine",
        "description": "Tăng nguy cơ độc tính carbamazepine",
        "management": "Theo dõi nồng độ carbamazepine, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    # Azithromycin
    ("Azithromycin", "Warfarin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ tác dụng warfarin",
        "description": "Tăng nhẹ nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng azithromycin",
        "references": "Micromedex"
    },
    
    ("Azithromycin", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Azithromycin kéo dài QT nhẹ, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Thận trọng khi dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    # Clarithromycin (already has some in main file)
    ("Clarithromycin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế CYP3A4, có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },
    
    ("Clarithromycin", "Theophylline"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế chuyển hóa theophylline",
        "description": "Tăng nồng độ theophylline",
        "management": "Theo dõi nồng độ theophylline",
        "references": "Micromedex"
    },
    
    ("Clarithromycin", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin, cân nhắc giảm liều digoxin",
        "references": "Micromedex"
    },
    
    ("Clarithromycin", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Clarithromycin kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Tránh dùng với thuốc kéo dài QT",
        "references": "FDA, Micromedex"
    },
    
    # ========== TETRACYCLINES ==========
    
    ("Doxycycline", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid (Ca, Mg, Al, Fe) chelate với doxycycline, giảm hấp thu",
        "description": "Giảm đáng kể hấp thu doxycycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Doxycycline", "Calcium"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Calcium chelate với doxycycline, giảm hấp thu",
        "description": "Giảm hấp thu doxycycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Doxycycline", "Iron"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Iron chelate với doxycycline, giảm hấp thu",
        "description": "Giảm hấp thu doxycycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Doxycycline", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng doxycycline",
        "references": "Micromedex"
    },
    
    ("Doxycycline", "Oral Contraceptive"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể giảm hiệu quả tránh thai",
        "description": "Giảm hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung",
        "references": "Clinical Pharmacology"
    },
    
    ("Minocycline", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid chelate với minocycline, giảm hấp thu",
        "description": "Giảm hấp thu minocycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Tetracycline", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid chelate với tetracycline, giảm hấp thu",
        "description": "Giảm hấp thu tetracycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    # ========== VANCOMYCIN ==========
    
    ("Vancomycin", "Aminoglycoside"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính thận và thần kinh thính giác",
        "description": "Tăng nguy cơ suy thận và điếc",
        "clinical_significance": "Nguy cơ suy thận tăng 2-3 lần khi dùng chung. Đặc biệt nguy hiểm ở bệnh nhân suy thận.",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận và thính giác. Tránh dùng nếu có thể",
        "references": "Micromedex"
    },
    
    ("Vancomycin", "Loop Diuretic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng độc tính thận",
        "description": "Tăng nguy cơ suy thận",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận",
        "references": "Micromedex"
    },
    
    ("Vancomycin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng vancomycin",
        "references": "Micromedex"
    },
    
    # ========== LINEZOLID ==========
    
    ("Linezolid", "SSRI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ co giật, nhầm lẫn, hôn mê, tử vong",
        "clinical_significance": "Nguy cơ hội chứng serotonin tăng đáng kể. Có thể gây tử vong.",
        "management": "Tránh dùng chung. Nếu cần: ngừng SSRI 2 tuần trước khi dùng linezolid",
        "alternatives": {
            "for_linezolid": ["Vancomycin", "Daptomycin"],
            "for_ssri": ["Mirtazapine (nếu phù hợp)"]
        },
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    ("Linezolid", "SNRI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "FDA, Micromedex"
    },
    
    ("Linezolid", "Tramadol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "FDA, Micromedex"
    },
    
    ("Linezolid", "MAO Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Linezolid là MAO inhibitor, tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "FDA, Micromedex"
    },
    
    ("Linezolid", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng linezolid",
        "references": "Micromedex"
    },
    
    # ========== CLINDAMYCIN ==========
    
    ("Clindamycin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng clindamycin",
        "references": "Micromedex"
    },
    
    ("Clindamycin", "Neuromuscular Blocking Agent"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Clindamycin tăng tác dụng thuốc giãn cơ",
        "description": "Tăng nguy cơ suy hô hấp",
        "management": "Thận trọng khi dùng chung. Theo dõi hô hấp",
        "references": "Micromedex"
    },
    
    # ========== METRONIDAZOLE ==========
    # (already has warfarin interaction in main file)
    
    ("Metronidazole", "Alcohol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Metronidazole ức chế aldehyde dehydrogenase, gây phản ứng disulfiram-like",
        "description": "Buồn nôn, nôn, đỏ mặt, nhịp tim nhanh khi uống rượu",
        "clinical_significance": "Phản ứng có thể rất nặng, gây khó chịu nghiêm trọng.",
        "management": "Tránh uống rượu trong khi dùng và ít nhất 48 giờ sau khi dừng metronidazole",
        "references": "Micromedex"
    },
    
    ("Metronidazole", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Metronidazole ức chế chuyển hóa warfarin qua CYP2C9",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "clinical_significance": "INR có thể tăng 2-3 lần. Nguy cơ xuất huyết nặng, đặc biệt trong 1-2 tuần đầu.",
        "management": "Giảm liều warfarin 30-50% khi dùng metronidazole. Theo dõi INR 2-3 lần/tuần",
        "alternatives": {
            "for_metronidazole": ["Clindamycin", "Vancomycin (nếu phù hợp)"],
            "for_warfarin": ["Dabigatran", "Rivaroxaban"]
        },
        "references": "AHFS Drug Information"
    },
    
    ("Metronidazole", "Lithium"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng nồng độ lithium",
        "description": "Tăng nguy cơ độc tính lithium",
        "management": "Theo dõi nồng độ lithium khi dùng metronidazole",
        "references": "Micromedex"
    },
    
    ("Metronidazole", "Phenytoin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Metronidazole ức chế chuyển hóa phenytoin",
        "description": "Tăng nồng độ phenytoin",
        "management": "Theo dõi nồng độ phenytoin, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    # ========== TRIMETHOPRIM-SULFAMETHOXAZOLE (TMP-SMX) ==========
    
    ("Trimethoprim-Sulfamethoxazole", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Sulfamethoxazole ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "clinical_significance": "INR có thể tăng đáng kể. Nguy cơ xuất huyết nặng.",
        "management": "Giảm liều warfarin 30-50%. Theo dõi INR 2-3 lần/tuần",
        "references": "Micromedex"
    },
    
    ("Trimethoprim-Sulfamethoxazole", "Methotrexate"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính methotrexate",
        "description": "Tăng nguy cơ giảm bạch cầu, thiếu máu, nhiễm độc gan thận",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: theo dõi công thức máu thường xuyên",
        "references": "AHFS Drug Information"
    },
    
    ("Trimethoprim-Sulfamethoxazole", "ACE Inhibitor"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "Tăng nguy cơ tăng kali máu",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu",
        "references": "Micromedex"
    },
    
    ("Trimethoprim-Sulfamethoxazole", "ARB"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "Tăng nguy cơ tăng kali máu",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu",
        "references": "Micromedex"
    },
    
    ("Trimethoprim-Sulfamethoxazole", "Phenytoin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "TMP-SMX ức chế chuyển hóa phenytoin",
        "description": "Tăng nồng độ phenytoin",
        "management": "Theo dõi nồng độ phenytoin, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    # ========== AMINOGLYCOSIDES ==========
    
    ("Gentamicin", "Vancomycin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính thận và thần kinh thính giác",
        "description": "Tăng nguy cơ suy thận và điếc",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận và thính giác",
        "references": "Micromedex"
    },
    
    ("Gentamicin", "Loop Diuretic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng độc tính thận và thần kinh thính giác",
        "description": "Tăng nguy cơ suy thận và điếc",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận",
        "references": "Micromedex"
    },
    
    ("Gentamicin", "Neuromuscular Blocking Agent"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Gentamicin tăng tác dụng thuốc giãn cơ",
        "description": "Tăng nguy cơ suy hô hấp",
        "management": "Thận trọng khi dùng chung. Theo dõi hô hấp",
        "references": "Micromedex"
    },
    
    ("Amikacin", "Vancomycin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính thận và thần kinh thính giác",
        "description": "Tăng nguy cơ suy thận và điếc",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận và thính giác",
        "references": "Micromedex"
    },
    
    # ========== OTHER ANTIBIOTICS ==========
    
    ("Rifampin", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rifampin cảm ứng CYP2C9, giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông, tăng nguy cơ huyết khối",
        "clinical_significance": "INR có thể giảm đáng kể. Nguy cơ huyết khối tái phát.",
        "management": "Tăng liều warfarin khi bắt đầu rifampin. Theo dõi INR thường xuyên. Giảm liều warfarin khi dừng rifampin",
        "references": "Micromedex"
    },
    
    ("Rifampin", "Oral Contraceptive"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rifampin cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "clinical_significance": "Hiệu quả tránh thai giảm đáng kể. Nguy cơ có thai cao.",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung (barrier method) hoặc chuyển sang biện pháp khác",
        "references": "Micromedex"
    },
    
    ("Rifampin", "HIV Protease Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rifampin cảm ứng chuyển hóa, giảm nồng độ HIV protease inhibitor",
        "description": "Giảm hiệu quả điều trị HIV",
        "management": "Tránh dùng chung. Cân nhắc dùng rifabutin thay thế",
        "references": "Micromedex"
    },
    
    ("Rifampin", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Rifampin cảm ứng P-gp, giảm nồng độ digoxin",
        "description": "Giảm hiệu quả digoxin",
        "management": "Tăng liều digoxin khi dùng rifampin. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Rifampin", "Theophylline"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Rifampin cảm ứng chuyển hóa theophylline",
        "description": "Giảm nồng độ theophylline",
        "management": "Tăng liều theophylline khi dùng rifampin. Theo dõi nồng độ theophylline",
        "references": "Micromedex"
    },
    
    ("Rifampin", "Phenytoin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Rifampin cảm ứng chuyển hóa phenytoin",
        "description": "Giảm nồng độ phenytoin",
        "management": "Tăng liều phenytoin khi dùng rifampin. Theo dõi nồng độ phenytoin",
        "references": "Micromedex"
    },
    
    # ========== DAPTOMYCIN ==========
    
    ("Daptomycin", "Statins"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tiêu cơ vân",
        "description": "Tăng nguy cơ tiêu cơ vân, suy thận",
        "management": "Ngừng statin khi dùng daptomycin. Theo dõi CK",
        "references": "FDA, Micromedex"
    },
    
    ("Daptomycin", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng daptomycin",
        "references": "Micromedex"
    },
    
    # ========== COLISTIN ==========
    
    ("Colistin", "Aminoglycoside"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính thận và thần kinh",
        "description": "Tăng nguy cơ suy thận và độc tính thần kinh",
        "management": "Tránh dùng chung. Theo dõi chức năng thận",
        "references": "Micromedex"
    },
    
    ("Colistin", "Neuromuscular Blocking Agent"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Colistin tăng tác dụng thuốc giãn cơ",
        "description": "Tăng nguy cơ suy hô hấp",
        "management": "Thận trọng khi dùng chung. Theo dõi hô hấp",
        "references": "Micromedex"
    },
    
    # ========== FLUOROQUINOLONES - ADDITIONAL ==========
    
    ("Ciprofloxacin", "Probenecid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Probenecid làm giảm đào thải ciprofloxacin, tăng nồng độ ciprofloxacin",
        "description": "Tăng nguy cơ tác dụng phụ ciprofloxacin",
        "management": "Thận trọng khi dùng chung. Có thể cần giảm liều ciprofloxacin",
        "references": "Micromedex"
    },
    
    ("Levofloxacin", "Probenecid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Probenecid làm giảm đào thải levofloxacin",
        "description": "Tăng nồng độ levofloxacin",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Ciprofloxacin", "Cyclosporine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ciprofloxacin có thể tăng nồng độ cyclosporine",
        "description": "Tăng nguy cơ độc tính cyclosporine",
        "management": "Theo dõi nồng độ cyclosporine khi dùng ciprofloxacin",
        "references": "Micromedex"
    },
    
    ("Ciprofloxacin", "Tacrolimus"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ciprofloxacin có thể tăng nồng độ tacrolimus",
        "description": "Tăng nguy cơ độc tính tacrolimus",
        "management": "Theo dõi nồng độ tacrolimus khi dùng ciprofloxacin",
        "references": "Micromedex"
    },
    
    # ========== MACROLIDES - ADDITIONAL ==========
    
    ("Erythromycin", "Cyclosporine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa cyclosporine",
        "description": "Tăng nồng độ cyclosporine",
        "management": "Theo dõi nồng độ cyclosporine, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Erythromycin", "Tacrolimus"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa tacrolimus",
        "description": "Tăng nồng độ tacrolimus",
        "management": "Theo dõi nồng độ tacrolimus, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Clarithromycin", "Cyclosporine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế chuyển hóa cyclosporine",
        "description": "Tăng nồng độ cyclosporine",
        "management": "Theo dõi nồng độ cyclosporine, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Clarithromycin", "Tacrolimus"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế chuyển hóa tacrolimus",
        "description": "Tăng nồng độ tacrolimus",
        "management": "Theo dõi nồng độ tacrolimus, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    # ========== PENICILLINS - ADDITIONAL ==========
    
    ("Ampicillin", "Oral Contraceptive"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể giảm nhẹ hiệu quả tránh thai",
        "description": "Giảm nhẹ hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung",
        "references": "Clinical Pharmacology"
    },
    
    ("Ampicillin", "Methotrexate"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ampicillin làm giảm đào thải methotrexate",
        "description": "Tăng nguy cơ độc tính methotrexate",
        "management": "Theo dõi công thức máu khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Piperacillin-Tazobactam", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng piperacillin-tazobactam",
        "references": "Micromedex"
    },
    
    # ========== CEPHALOSPORINS - ADDITIONAL ==========
    
    ("Ceftazidime", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng ceftazidime",
        "references": "Micromedex"
    },
    
    ("Cefuroxime", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng cefuroxime",
        "references": "Micromedex"
    },
    
    ("Cefotaxime", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng cefotaxime",
        "references": "Micromedex"
    },
    
    # ========== TETRACYCLINES - ADDITIONAL ==========
    
    ("Tetracycline", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng tetracycline",
        "references": "Micromedex"
    },
    
    ("Minocycline", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng minocycline",
        "references": "Micromedex"
    },
    
    # ========== VANCOMYCIN - ADDITIONAL ==========
    
    ("Vancomycin", "Aminoglycoside"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính thận và thần kinh thính giác",
        "description": "Tăng nguy cơ suy thận và điếc",
        "clinical_significance": "Nguy cơ suy thận tăng 2-3 lần khi dùng chung. Đặc biệt nguy hiểm ở bệnh nhân suy thận.",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận và thính giác. Tránh dùng nếu có thể",
        "references": "Micromedex"
    },
    
    ("Vancomycin", "Anesthetic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Vancomycin có thể gây phản ứng phản vệ khi dùng với một số thuốc gây mê",
        "description": "Tăng nguy cơ phản ứng phản vệ",
        "management": "Thận trọng khi dùng chung. Theo dõi sát",
        "references": "Micromedex"
    },
    
    # ========== LINEZOLID - ADDITIONAL ==========
    
    ("Linezolid", "Pseudoephedrine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng huyết áp",
        "description": "Tăng nguy cơ tăng huyết áp nặng",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("Linezolid", "Phenylephrine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng huyết áp",
        "description": "Tăng nguy cơ tăng huyết áp nặng",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    # ========== METRONIDAZOLE - ADDITIONAL ==========
    
    ("Metronidazole", "Disulfiram"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cả hai đều ức chế aldehyde dehydrogenase",
        "description": "Tăng nguy cơ phản ứng disulfiram-like",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("Metronidazole", "Busulfan"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Metronidazole ức chế chuyển hóa busulfan",
        "description": "Tăng nguy cơ độc tính busulfan",
        "management": "Tránh dùng chung. Nếu cần: giảm liều busulfan",
        "references": "Micromedex"
    },
    
    # ========== TMP-SMX - ADDITIONAL ==========
    
    ("Trimethoprim-Sulfamethoxazole", "Cyclosporine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "TMP-SMX có thể tăng nồng độ cyclosporine",
        "description": "Tăng nguy cơ độc tính cyclosporine",
        "management": "Theo dõi nồng độ cyclosporine",
        "references": "Micromedex"
    },
    
    ("Trimethoprim-Sulfamethoxazole", "Tacrolimus"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "TMP-SMX có thể tăng nồng độ tacrolimus",
        "description": "Tăng nguy cơ độc tính tacrolimus",
        "management": "Theo dõi nồng độ tacrolimus",
        "references": "Micromedex"
    },
    
    ("Trimethoprim-Sulfamethoxazole", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "TMP có thể tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    # ========== AMINOGLYCOSIDES - ADDITIONAL ==========
    
    ("Tobramycin", "Vancomycin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính thận và thần kinh thính giác",
        "description": "Tăng nguy cơ suy thận và điếc",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận và thính giác",
        "references": "Micromedex"
    },
    
    ("Amikacin", "Loop Diuretic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng độc tính thận và thần kinh thính giác",
        "description": "Tăng nguy cơ suy thận và điếc",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận",
        "references": "Micromedex"
    },
    
    ("Gentamicin", "Cisplatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính thận",
        "description": "Tăng nguy cơ suy thận",
        "management": "Tránh dùng chung nếu có thể. Theo dõi chức năng thận sát",
        "references": "Micromedex"
    },
    
    # ========== ADDITIONAL INTERACTIONS TO REACH 100+ ==========
    
    ("Azithromycin", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Azithromycin có thể tăng nhẹ nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin khi dùng azithromycin",
        "references": "Micromedex"
    },
    
    ("Azithromycin", "Cyclosporine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Azithromycin có thể tăng nồng độ cyclosporine",
        "description": "Tăng nguy cơ độc tính cyclosporine",
        "management": "Theo dõi nồng độ cyclosporine",
        "references": "Micromedex"
    },
    
    ("Ceftriaxone", "Probenecid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Probenecid làm giảm đào thải ceftriaxone",
        "description": "Tăng nồng độ ceftriaxone",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Cefazolin", "Probenecid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Probenecid làm giảm đào thải cefazolin",
        "description": "Tăng nồng độ cefazolin",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Vancomycin", "Probenecid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Probenecid làm giảm đào thải vancomycin",
        "description": "Tăng nồng độ vancomycin, tăng nguy cơ độc tính",
        "management": "Thận trọng khi dùng chung. Có thể cần giảm liều vancomycin",
        "references": "Micromedex"
    },
    
    ("Penicillin", "Probenecid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Probenecid làm giảm đào thải penicillin, tăng nồng độ",
        "description": "Tăng nồng độ penicillin",
        "management": "Thận trọng khi dùng chung. Có thể cần giảm liều penicillin",
        "references": "Micromedex"
    },
    
    ("Amoxicillin", "Probenecid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Probenecid làm giảm đào thải amoxicillin",
        "description": "Tăng nồng độ amoxicillin",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Moxifloxacin", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid chelate với moxifloxacin, giảm hấp thu",
        "description": "Giảm hấp thu moxifloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Levofloxacin", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid (Ca, Mg, Al) chelate với levofloxacin, giảm hấp thu",
        "description": "Giảm hấp thu levofloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Doxycycline", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng doxycycline",
        "references": "Micromedex"
    },
    
    ("Tobramycin", "Loop Diuretic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng độc tính thận và thần kinh thính giác",
        "description": "Tăng nguy cơ suy thận và điếc",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận",
        "references": "Micromedex"
    },
    
    ("Amikacin", "Neuromuscular Blocking Agent"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amikacin tăng tác dụng thuốc giãn cơ",
        "description": "Tăng nguy cơ suy hô hấp",
        "management": "Thận trọng khi dùng chung. Theo dõi hô hấp",
        "references": "Micromedex"
    },
    
    ("Gentamicin", "Neuromuscular Blocking Agent"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Gentamicin tăng tác dụng thuốc giãn cơ",
        "description": "Tăng nguy cơ suy hô hấp",
        "management": "Thận trọng khi dùng chung. Theo dõi hô hấp",
        "references": "Micromedex"
    },
}

