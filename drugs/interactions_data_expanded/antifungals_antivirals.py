"""
Antifungals and Antivirals Drug Interactions
Expanded database for antifungals (Azoles) and antivirals (HIV PIs, Paxlovid)
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

ANTIFUNGALS_ANTIVIRALS_INTERACTIONS = {
    # ========== ANTIFUNGALS (AZOLES) ==========
    
    # Ketoconazole
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

    ("Ketoconazole", "Antacid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Antacid làm tăng pH dạ dày, giảm hấp thu ketoconazole (cần môi trường acid)",
        "description": "Giảm hiệu quả ketoconazole",
        "management": "Uống antacid ít nhất 2 giờ sau ketoconazole",
        "references": "Micromedex"
    },
    
    # Fluconazole
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

    ("Fluconazole", "Simvastatin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Fluconazole ức chế CYP3A4 (yếu hơn itra/keto), tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Thận trọng, theo dõi đau cơ",
        "references": "Micromedex"
    },
    
    # Itraconazole
    ("Itraconazole", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Itraconazole ức chế CYP3A4, có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },

    ("Itraconazole", "Simvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Itraconazole ức chế mạnh CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Chống chỉ định dùng chung",
        "references": "Micromedex"
    },

    ("Voriconazole", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Voriconazole ức chế CYP2C9, tăng mạnh INR",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR sát sao, giảm liều warfarin",
        "references": "Micromedex"
    },

    ("Azole Antifungal", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Azoles ức chế chuyển hóa thuốc kéo dài QT và bản thân cũng có thể kéo dài QT",
        "description": "Tăng nguy cơ xoắn đỉnh",
        "management": "Tránh dùng chung với thuốc chống loạn nhịp nhóm IA, III, cisapride, pimozide...",
        "references": "CredibleMeds"
    },
    
    # ========== ANTIVIRALS ==========
    
    # Paxlovid (Nirmatrelvir/Ritonavir) - CRITICAL INTERACTIONS
    ("Paxlovid", "Simvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ritonavir ức chế mạnh CYP3A4, tăng nồng độ simvastatin",
        "description": "Nguy cơ tiêu cơ vân nghiêm trọng",
        "management": "CHỐNG CHỈ ĐỊNH. Ngừng simvastatin 12h trước khi dùng Paxlovid và trong thời gian điều trị cộng thêm 5 ngày.",
        "references": "FDA EUA Fact Sheet"
    },

    ("Paxlovid", "Atorvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ritonavir ức chế mạnh CYP3A4, tăng nồng độ atorvastatin",
        "description": "Nguy cơ tiêu cơ vân",
        "management": "Ngừng atorvastatin khi dùng Paxlovid là an toàn nhất. Hoặc giảm liều tối đa.",
        "references": "FDA EUA Fact Sheet"
    },

    ("Paxlovid", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ritonavir có thể cảm ứng CYP2C9 hoặc ức chế (phức tạp), thường làm giảm INR nhưng có thể biến đổi",
        "description": "Dao động INR",
        "management": "Theo dõi INR thường xuyên trong và sau khi dùng Paxlovid",
        "references": "FDA EUA Fact Sheet"
    },

    ("Paxlovid", "Rivaroxaban"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ritonavir ức chế CYP3A4 và P-gp, tăng nồng độ rivaroxaban",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Tránh dùng chung. Cân nhắc đổi sang LMWH hoặc aspirin tùy nguy cơ",
        "references": "FDA EUA Fact Sheet"
    },

    ("Paxlovid", "Salmeterol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nồng độ salmeterol",
        "description": "Nguy cơ tim mạch (nhịp nhanh, kéo dài QT)",
        "management": "CHỐNG CHỈ ĐỊNH",
        "references": "FDA EUA Fact Sheet"
    },

    ("Paxlovid", "Amiodarone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nồng độ amiodarone",
        "description": "Nguy cơ loạn nhịp tim đe dọa tính mạng",
        "management": "CHỐNG CHỈ ĐỊNH",
        "references": "FDA EUA Fact Sheet"
    },

    # Ritonavir (General)
    ("Ritonavir", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ritonavir cảm ứng CYP2C9, thường làm giảm INR",
        "description": "Giảm hiệu quả chống đông hoặc biến đổi khó lường",
        "management": "Theo dõi INR khi dùng ritonavir",
        "references": "Micromedex"
    },
    
    ("Ritonavir", "Simvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ritonavir ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "CHỐNG CHỈ ĐỊNH",
        "references": "FDA, Micromedex"
    },
    
    ("Ritonavir", "Atorvastatin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ritonavir ức chế CYP3A4, tăng nồng độ atorvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều atorvastatin. Theo dõi CK",
        "references": "Micromedex"
    },

    # Acyclovir / Valacyclovir
    ("Acyclovir", "Nephrotoxic Agents"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tác dụng cộng hợp gây độc thận",
        "description": "Tăng nguy cơ suy thận cấp do kết tủa tinh thể",
        "management": "Đảm bảo bù đủ dịch. Theo dõi chức năng thận khi dùng liều cao hoặc tiêm truyền.",
        "references": "Micromedex"
    },

    ("Valacyclovir", "Nephrotoxic Agents"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tác dụng cộng hợp gây độc thận",
        "description": "Tăng nguy cơ suy thận",
        "management": "Đảm bảo bù đủ dịch.",
        "references": "Micromedex"
    }
}
