"""
Antidiuretic Hormone (ADH) Analogs (Thuốc tương tự hormone chống bài niệu)
Bao gồm: Desmopressin
"""

ANTIDIURETIC_HORMONE_DRUGS = {
    "Desmopressin": {
        "group": "Endocrinology - ADH Analog",
        "vietnamese_name": "Desmopressin, DDAVP",
        "brand_names": {
            "common": ["DDAVP", "Stimate", "Noctiva"],
            "vietnam": ["Desmopressin", "DDAVP"]
        },
        "administration": ["PO", "IV", "SC", "Intranasal"],
        "indications": [
            "Đái tháo nhạt trung ương (Central Diabetes Insipidus)",
            "Đái dầm ban đêm (Nocturnal Enuresis)",
            "Rối loạn đông máu (Hemophilia A, von Willebrand disease type 1)",
            "Hạ natri máu do SIADH (off-label - thận trọng)"
        ],
        "contraindications": [
            "Dị ứng desmopressin",
            "Hạ natri máu (Hyponatremia)",
            "Suy tim ứ huyết nặng",
            "Bệnh thận nặng (CrCl <50 ml/min) - thận trọng",
            "Polydipsia tâm thần (Psychogenic polydipsia)"
        ],
        "dosage": {
            "diabetes_insipidus_po": "0.1-0.2mg PO x 2-3 lần/ngày",
            "diabetes_insipidus_iv": "1-4mcg IV/SC x 1-2 lần/ngày",
            "diabetes_insipidus_intranasal": "10-40mcg intranasal x 1-2 lần/ngày",
            "nocturnal_enuresis": "0.2mg PO trước khi ngủ",
            "hemophilia_bleeding": "0.3mcg/kg IV trong 15-30 phút",
            "notes": "Điều chỉnh liều theo đáp ứng lâm sàng. Tránh uống quá nhiều nước (nguy cơ hạ natri máu)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Tránh dùng hoặc dùng liều thấp dưới sự giám sát chặt chẽ"
        },
        "side_effects": [
            "Hạ natri máu (Hyponatremia) - Nghiêm trọng, có thể gây co giật, hôn mê, tử vong",
            "Giữ nước (Fluid retention)",
            "Đau đầu",
            "Buồn nôn",
            "Đau bụng",
            "Tăng huyết áp (hiếm)",
            "Co giật (do hạ natri máu)",
            "Phản ứng tại chỗ (đỏ, sưng - với intranasal)"
        ],
        "interactions": [
            "Thuốc lợi tiểu: Tăng nguy cơ hạ natri máu",
            "Corticosteroid: Có thể ảnh hưởng tác dụng",
            "Lithium, Demeclocycline: Đối kháng tác dụng (dùng trong SIADH)"
        ],
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc lợi tiểu (Furosemide, Thiazide)",
                    "mechanism": "Cả hai đều ảnh hưởng đến cân bằng nước và điện giải",
                    "effect": "Tăng nguy cơ hạ natri máu nghiêm trọng",
                    "management": "Tránh dùng cùng. Nếu cần, theo dõi natri máu rất chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Corticosteroid",
                    "mechanism": "Có thể ảnh hưởng đến tác dụng của desmopressin",
                    "effect": "Giảm hiệu quả điều trị",
                    "management": "Theo dõi đáp ứng lâm sàng."
                },
                {
                    "drug": "Lithium, Demeclocycline",
                    "mechanism": "Đối kháng tác dụng của desmopressin",
                    "effect": "Giảm hiệu quả điều trị",
                    "management": "Tránh dùng cùng. Lithium và demeclocycline được dùng để điều trị SIADH."
                }
            ],
            "minor": []
        },
        "pregnancy": "B",
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Không có bằng chứng về nguy cơ ở người. Có thể dùng trong thai kỳ nếu cần. Theo dõi natri máu chặt chẽ.",
            "lactation_details": "Không rõ liệu có bài tiết vào sữa mẹ. Thận trọng khi cho con bú. Có thể dùng nếu lợi ích vượt trội nguy cơ."
        },
        "mechanism_of_action": "Desmopressin là chất tương tự tổng hợp của vasopressin (ADH), có tác dụng chống bài niệu mạnh hơn vasopressin tự nhiên nhưng ít tác dụng co mạch. Desmopressin gắn vào thụ thể V2 ở ống thận xa và ống góp, làm tăng tái hấp thu nước tự do, giảm bài tiết nước tiểu và tăng độ cô đặc nước tiểu. Trong rối loạn đông máu, desmopressin làm tăng giải phóng factor VIII và von Willebrand factor từ nội mô mạch máu.",
        "monitoring": [
            "Natri máu (Serum sodium) - CRITICAL, theo dõi thường xuyên để phát hiện hạ natri máu",
            "Lượng nước tiểu (Urine output)",
            "Độ cô đặc nước tiểu (Urine osmolality)",
            "Cân nặng (fluid retention)",
            "Huyết áp",
            "Dấu hiệu hạ natri máu (đau đầu, buồn nôn, lú lẫn, co giật, hôn mê)",
            "Factor VIII, von Willebrand factor (nếu dùng cho rối loạn đông máu)"
        ],
        "precautions": [
            "Hạ natri máu là tác dụng phụ NGHIÊM TRỌNG - Theo dõi natri máu thường xuyên",
            "Tránh uống quá nhiều nước (nguy cơ hạ natri máu)",
            "Giới hạn lượng nước uống khi dùng desmopressin",
            "Ngừng ngay nếu có dấu hiệu hạ natri máu (đau đầu, buồn nôn, lú lẫn, co giật)",
            "Thận trọng ở người cao tuổi (tăng nguy cơ hạ natri máu)",
            "Thận trọng ở bệnh nhân suy tim (giữ nước)",
            "Thận trọng ở bệnh nhân suy thận (CrCl <50 - giảm liều hoặc tránh dùng)",
            "Không dùng cho polydipsia tâm thần (nguy cơ hạ natri máu cao)",
            "Dạng intranasal: Có thể gây kích ứng tại chỗ"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-3 giờ (IV/SC), 1.5-2.5 giờ (PO)",
            "onset": "30-60 phút (IV/SC), 1-2 giờ (PO)",
            "duration": "6-12 giờ (tùy liều và đường dùng)",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận: bài tiết qua nước tiểu. Chuyển hóa ở gan một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng intranasal: bảo quản trong tủ lạnh (2-8°C) sau khi mở.",
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều. Desmopressin chuyển hóa một phần qua gan."
        },
        "overdose_management": {
            "symptoms": ["Hạ natri máu nghiêm trọng", "Co giật", "Hôn mê", "Giữ nước", "Tăng huyết áp", "Phù phổi"],
            "treatment": "Ngừng thuốc ngay. Điều trị hạ natri máu: hạn chế nước, có thể cần truyền natri chloride 3% nếu hạ natri máu nặng. Điều trị co giật nếu có. Hỗ trợ hô hấp nếu cần.",
            "antidote": None
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là ngừng thuốc và điều trị hạ natri máu. Có thể dùng demeclocycline hoặc lithium để đối kháng tác dụng trong trường hợp cần thiết."
        },
        "administration_instructions": {
            "preparation": "PO: Viên nén, uống nguyên viên với nước. IV/SC: Dung dịch tiêm. Intranasal: Dung dịch xịt mũi.",
            "administration": "PO: Uống với nước, điều chỉnh liều theo đáp ứng. IV/SC: Tiêm chậm, theo dõi natri máu. Intranasal: Xịt vào mũi theo hướng dẫn. QUAN TRỌNG: Giới hạn lượng nước uống để tránh hạ natri máu.",
            "monitoring": ["Natri máu (CRITICAL - thường xuyên)", "Lượng nước tiểu", "Cân nặng", "Dấu hiệu hạ natri máu"]
        },
        "black_box_warnings": "Hạ natri máu nghiêm trọng, có thể gây co giật, hôn mê, tử vong. Cần theo dõi natri máu thường xuyên. Tránh uống quá nhiều nước. Ngừng ngay nếu có dấu hiệu hạ natri máu.",
        "references": {
            "primary_sources": [
                "FDA Drug Label - Desmopressin (DDAVP, Stimate, Noctiva)",
                "UpToDate - Desmopressin: Drug information",
                "Endocrine Society Guidelines - Diabetes Insipidus",
                "ASH Guidelines - von Willebrand Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA approved, extensive clinical experience"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"metabolic": "Black Box Warning - Hyponatremia (may cause seizures, coma, death - CRITICAL)", "cardiovascular": "Fluid retention, hypertension (rare)", "neurological": "Seizures (due to hyponatremia)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Serum sodium (CRITICAL - monitor frequently for hyponatremia)", "Urine output (diuresis response)", "Urine osmolality (concentration)", "Weight (fluid retention)", "Blood pressure (hypertension risk)", "Signs of hyponatremia (headache, nausea, confusion, seizures, coma - CRITICAL)", "Water intake (limit to prevent hyponatremia)", "Factor VIII, von Willebrand factor (if used for bleeding disorders)"],
            "look_alike_sound_alike": ["Desmopressin", "Vasopressin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Hyponatremia (may cause seizures, coma, death)",
            "Endocrine Society Guidelines - Diabetes Insipidus",
            "ASH Guidelines - von Willebrand Disease",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    }
}

__all__ = ['ANTIDIURETIC_HORMONE_DRUGS']

