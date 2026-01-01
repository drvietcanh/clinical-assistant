"""
Immunosuppressants (Thuốc ức chế miễn dịch)
"""

IMMUNOSUPPRESSANTS_DRUGS = {
    "Tacrolimus": {
        "group": "Immunology - Calcineurin Inhibitor",
        "vietnamese_name": "Tacrolimus, FK506",
        "brand_names": {
            "common": ["Prograf", "Advagraf"],
            "vietnam": ["Prograf", "Tacrolimus", "Advagraf (tác dụng kéo dài)"]
        },
        "administration": ["PO", "IV", "Topical"],
        "indications": [
            "Dự phòng thải ghép (gan, thận, tim, phổi)",
            "Viêm da cơ địa (Topical - Protopic)",
            "Bệnh tự miễn kháng trị (Lupus, Viêm khớp dạng thấp - off-label)"
        ],
        "dosage": {
            "transplant_maintenance": "0.03-0.05 mg/kg/ngày chia 2 lần (Prograf) hoặc 1 lần (Advagraf). Điều chỉnh theo nồng độ đáy (Trough level).",
            "atopic_dermatitis": "Bôi 0.03-0.1% x 1-2 lần/ngày.",
            "notes": "Khoảng điều trị hẹp (Narrow therapeutic index). Cần theo dõi nồng độ thuốc trong máu (TDM) nghiêm ngặt."
        },
        "side_effects": [
            "Độc tính thận (Nephrotoxicity) - Phổ biến, phụ thuộc liều",
            "Độc tính thần kinh (Run tay, co giật, đau đầu)",
            "Tăng đường huyết (Đái tháo đường sau ghép - NODAT)",
            "Tăng huyết áp",
            "Tăng Kali máu"
        ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Macrolides, Azole antifungals, Nước bưởi) -> Tăng nồng độ Tacrolimus mạnh -> Ngộ độc.",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin) -> Giảm nồng độ Tacrolimus -> Thải ghép."
        ],
        "monitoring": ["Nồng độ Tacrolimus máu (Trough)", "Chức năng thận", "Đường huyết", "Kali máu"]
    },

    "Cyclosporine": {
        "group": "Immunology - Calcineurin Inhibitor",
        "vietnamese_name": "Cyclosporine, Cyclosporin A",
        "brand_names": {
            "common": ["Neoral", "Sandimmune"],
            "vietnam": ["Neoral (vi nhũ tương)", "Sandimmun"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Dự phòng thải ghép tạng",
            "Viêm khớp dạng thấp",
            "Vảy nến nặng",
            "Hội chứng thận hư"
        ],
        "dosage": {
            "transplant": "Khởi đầu 8-12 mg/kg/ngày, giảm dần. Điều chỉnh theo nồng độ đáy.",
            "ra_psoriasis": "2.5-4 mg/kg/ngày chia 2 lần.",
            "notes": "Dạng Neoral (Modified) và Sandimmune (Non-modified) KHÔNG tương đương nhau."
        },
        "side_effects": [
            "Độc tính thận (Nephrotoxicity)",
            "Tăng huyết áp",
            "Phì đại lợi (Gingival hyperplasia)",
            "Rậm lông (Hirsutism)",
            "Tăng lipid máu"
        ],
        "features": {
             "comparison_tacrolimus": "Cyclosporine gây phì đại lợi và rậm lông, Tacrolimus gây rụng tóc và đái tháo đường nhiều hơn."
        },
        "monitoring": ["Nồng độ Cyclosporine máu", "Chức năng thận", "Huyết áp"]
    },

    "Mycophenolate": {
        "group": "Immunology - Antimetabolite",
        "vietnamese_name": "Mycophenolate Mofetil (MMF), CellCept",
        "brand_names": {
            "common": ["CellCept", "Myfortic"],
            "vietnam": ["CellCept 250/500mg", "Myfortic (Mycophenolate Sodium)"]
        },
        "administration": ["PO", "IV"],
        "indications": [
            "Dự phòng thải ghép (kết hợp Tacrolimus/Cyclosporine + Corticoid)",
            "Viêm thận Lupus (Lupus Nephritis)"
        ],
        "contraindications": [
            "Phụ nữ mang thai (Gây quái thai nghiêm trọng - REMS program)"
        ],
        "dosage": {
            "transplant_adult": "1000 mg (CellCept) hoặc 720 mg (Myfortic) x 2 lần/ngày.",
            "lupus_nephritis": "500-1500 mg x 2 lần/ngày.",
            "notes": "Myfortic là dạng bao tan trong ruột, giảm kích ứng dạ dày hơn CellCept."
        },
        "side_effects": [
            "Rối loạn tiêu hóa (Tiêu chảy, nôn) - Rất phổ biến, giới hạn liều dùng",
            "Suy tủy (Giảm bạch cầu, thiếu máu)",
            "Tăng nguy cơ nhiễm trùng (CMV, BK virus)"
        ],
        "mechanism_of_action": "Ức chế IMPDH, ức chế tổng hợp Purine de novo, ức chế chọn lọc tăng sinh tế bào Lympho T và B.",
        "monitoring": ["Công thức máu (CBC)", "Dấu hiệu nhiễm trùng"]
    }
}
