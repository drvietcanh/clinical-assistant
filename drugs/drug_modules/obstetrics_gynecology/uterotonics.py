"""
Obstetrics and Gynecology Medications
Uterotonic medications (Note: Should be in emergency module)
"""
from typing import Dict, Any

UTEROTONICS_DRUGS: Dict[str, Dict[str, Any]] = {
    "Methylergonovine":     {
        "group": "Obstetrics/Gynecology - Uterotonic (Ergot Alkaloid)",
        "vietnamese_name": "Methylergonovine, Methergine",
        "administration": [
            "IM",
            "IV",
            "PO"
    ],
        "indications": [
            "Xuất huyết sau sinh (postpartum hemorrhage) - do đờ tử cung",
            "Dự phòng xuất huyết sau sinh (sau khi sổ thai)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng methylergonovine",
                "Tăng huyết áp (hypertension) - NGUY HIỂM",
                "Tiền sản giật (preeclampsia) hoặc sản giật (eclampsia) - NGUY HIỂM",
                "Bệnh mạch vành, đau thắt ngực",
                "Đang mang thai (induction of labor) - CHỐNG CHỈ ĐỊNH (chỉ dùng sau khi sổ thai)",
                "Dùng với thuốc ức chế CYP3A4 mạnh"
    ],
            "tương_đối": [
                "Suy gan/thận nặng",
                "Hội chứng Raynaud",
                "Nhiễm trùng huyết (sepsis)"
    ],
        },
        "dosage": {
            "adult_pph_prevention_im": """0.2mg IM sau khi sổ thai vai trước hoặc sau khi sổ nhau. Có thể lặp lại mỗi 2-4 giờ nếu cần (tối đa 5 liều).""",
            "adult_pph_treatment_im": "0.2mg IM mỗi 2-4 giờ (tối đa 5 liều).",
            "adult_pph_treatment_iv": """0.2mg IV CHẬM (trên 60 giây) - CHỈ DÙNG TRONG CẤP CỨU NẾU KHÔNG THỂ TIÊM IM (nguy cơ tăng huyết áp nặng, đột quỵ).""",
            "adult_pph_maintenance_po": "0.2mg PO x 3-4 lần/ngày trong 2-7 ngày (sau khi ổn định bằng tiêm).",
            "notes": """Methylergonovine gây co thắt tử cung mạnh và kéo dài. Tác dụng nhanh (IM: 2-5 phút, IV: tức thì). IV chỉ dùng trong trường hợp cấp cứu đe dọa tính mạng vì nguy cơ tai biến cao (tăng huyết áp đột ngột).""",
        },
        "renal_adjustment": {
            "normal": "Thận trọng",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng (tích lũy thuốc)",
        },
        "side_effects": {
            "phổ_biến": [
                "Tăng huyết áp",
                "Buồn nôn, nôn",
                "Đau bụng (co thắt tử cung)",
                "Đau đầu"
    ],
            "nghiêm_trọng": [
                "Tăng huyết áp kịch phát (hypertensive crisis) - đặc biệt khi IV nhanh",
                "Đột quỵ (stroke)",
                "Nhồi máu cơ tim (MI) - co thắt mạch vành",
                "Co giật (seizures)"
    ],
        },
        "interactions": {
            "giảm_hiệu_quả": [],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 mạnh (clarithromycin, ritonavir...): tăng nồng độ gây ngộ độc ergot (ergotism).",
                "Thuốc vận mạch khác: tăng nguy cơ tăng huyết áp."
    ],
        },
        "pregnancy": "C - CHỐNG CHỈ ĐỊNH trong thai kỳ (chỉ dùng sau khi sổ thai)",
        "mechanism_of_action": """Ergot alkaloid tác động trực tiếp lên cơ trơn tử cung, tăng cường độ, tần số và trương lực co bóp. Làm giảm xuất huyết do đờ tử cung sau sinh.""",
        "monitoring": [
            "Huyết áp - TRƯỚC và SAU khi tiêm",
            "Mạch, nhịp tim",
            "Co hồi tử cung",
            "Lượng máu mất"
    ],
        "precautions": {
            "quan_trọng": [
                "KHÔNG tiêm IV nhanh - nguy cơ tử vong do tăng huyết áp/đột quỵ",
                "Kiểm tra huyết áp trước khi tiêm. Nếu HA >140/90, cân nhắc không dùng.",
                "Không dùng cho phụ nữ đang mang thai để gây chuyển dạ (induction)."
    ],
            "khác": [],
        },
        "pharmacokinetics": {
            "half_life": "0.5 - 2 giờ (giai đoạn đầu), 3.4 giờ (giai đoạn cuối)",
            "onset": "IM: 2-5 phút; IV: <1 phút; PO: 5-10 phút",
            "duration": "IM: 3 giờ; PO: 3 giờ",
            "protein_binding": "Không rõ",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Phân và nước tiểu",
        },
        "storage": "Bảo quản lạnh (2-8°C), tránh ánh sáng. Ổn định ở nhiệt độ phòng trong 14 ngày (Methergine).",
        "black_box_warnings": """Chống chỉ định dùng chung với các thuốc ức chế CYP3A4 mạnh (protease inhibitors, macrolides, azole antifungals) do nguy cơ co mạch ngoại vi nghiêm trọng và thiếu máu cục bộ (ergotism).""",
        "analysis": {
            "clinical_use": "Thuốc hàng thứ 2 (Second-line) sau Oxytocin để điều trị băng huyết sau sinh do đờ tử cung.",
            "safety_profile": "Nguy cơ cao nhất là tăng huyết áp. Thận trọng đặc biệt trên bệnh nhân tiền sản giật.",
        },
        "references": {
            "primary_sources": [
                "Methergine Package Insert",
                "ACOG Practice Bulletin No. 183: Postpartum Hemorrhage"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Cardiovascular effects (hypertension, vasospasm, stroke, MI)", "Uterine hyperstimulation"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Blood pressure - CRITICAL (before and after injection)", "Heart rate", "Uterine contractions", "Signs of hyperstimulation", "Signs of ergotism (vasospasm, ischemia) with CYP3A4 inhibitors"]
        },
        "guideline_tags": [
            "ACOG Practice Bulletin - Postpartum Hemorrhage",
            "WHO Guidelines - Uterotonics",
            "FDA Black Box Warning - CYP3A4 Inhibitors and Ergotism",
            "ISMP High Alert Medications"
        ],
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
        "administration_instructions": {
        },
    },
    "Carboprost":     {
        "group": "Obstetrics/Gynecology - Uterotonic (Prostaglandin)",
        "vietnamese_name": "Carboprost Tromethamine, Hemabate",
        "administration": [
            "IM",
            "Intramyometrial (off-label)"
    ],
        "indications": [
            "Xuất huyết sau sinh do đờ tử cung (refractory PPH) - không đáp ứng với oxytocin/ergot",
            "Chấm dứt thai kỳ (phá thai) ở tam cá nguyệt 2 (13-20 tuần)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng carboprost",
                "Hen suyễn (Asthma) đang hoạt động - gây co thắt phế quản nặng",
                "Bệnh tim, phổi, thận, gan nặng đang hoạt động",
                "Viêm vùng chậu cấp (PID)"
    ],
            "tương_đối": [
                "Tăng huyết áp, hạ huyết áp",
                "Tiền sử hen suyễn (cần thận trọng)",
                "Thiếu máu, vàng da, động kinh"
    ],
        },
        "dosage": {
            "adult_pph_treatment": "250 mcg (0.25 mg) IM sâu. Có thể lặp lại mỗi 15-90 phút nếu cần. Tối đa 2 mg (8 liều).",
            "notes": """KHÔNG TIÊM TĨNH MẠCH (IV). Tiêm bắp sâu. Có thể tiêm trực tiếp vào cơ tử cung (intramyometrial) trong phẫu thuật (off-label).""",
        },
        "side_effects": {
            "phổ_biến": [
                "Tiêu chảy (rất phổ biến >60%)",
                "Buồn nôn, nôn",
                "Sốt (transient fever)",
                "Đỏ bừng mặt (flushing)"
    ],
            "nghiêm_trọng": [
                "Co thắt phế quản (bronchospasm) - đặc biệt bệnh nhân hen",
                "Phù phổi",
                "Tăng huyết áp"
    ],
        },
        "pregnancy": "C - Dùng để chấm dứt thai kỳ hoặc sau sinh.",
        "mechanism_of_action": """Prostaglandin F2 alpha analogue. Gây co bóp myometrium mạnh (tử cung) để cầm máu. Cũng gây co cơ trơn đường tiêu hóa (tiêu chảy) và phế quản.""",
        "monitoring": [
            "Hô hấp (nghe phổi - bronchospasm)",
            "Mạch, Huyết áp, Nhiệt độ (sốt phổ biến)",
            "Lượng máu mất",
            "Tác dụng phụ đường tiêu hóa"
    ],
        "precautions": {
            "quan_trọng": [
                "Chống chỉ định tuyệt đối cho bệnh nhân HEN SUYỄN.",
                "Sẵn sàng thuốc chống nôn và chống tiêu chảy (Loperamide) vì tác dụng phụ tiêu hóa rất mạnh.",
                "Phân biệt sốt do thuốc với sốt do nhiễm trùng (sốt do thuốc thường tự hết sau vài giờ)."
    ],
        },
        "pharmacokinetics": {
            "onset": "IM: đỉnh nồng độ sau 20-30 phút",
            "duration": "Vài giờ",
            "metabolism": "Gan, phổi",
            "clearance": "Thận",
        },
        "storage": "Bảo quản lạnh (2-8°C).",
        "interaction": {
            "tăng_nguy_cơ": [
                "Oxytocin (tăng nguy cơ vỡ tử cung nếu dùng đồng thời liều cao gây cơn co cường tính - cần theo dõi sát)"
    ],
        },
        "analysis": {
            "clinical_use": """Thuốc hàng thứ 3 (Third-line) sau Oxytocin và Methylergonovine (hoặc thay thế Methergine ở BN tăng huyết áp).""",
            "safety_profile": "Rất hiệu quả nhưng tác dụng phụ tiêu hóa rất nhiều. Thận trọng tối đa với bệnh nhân có bệnh phổi.",
        },
        "references": {
            "primary_sources": [
                "Hemabate Package Insert",
                "ACOG Guidelines"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Bronchospasm (asthma contraindication)", "Pulmonary edema", "Cardiovascular effects (hypertension)", "Uterine hyperstimulation"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory status - CRITICAL (bronchospasm risk)", "Blood pressure", "Heart rate", "Temperature (fever is common)", "Uterine contractions", "Signs of hyperstimulation"]
        },
        "guideline_tags": [
            "ACOG Practice Bulletin - Postpartum Hemorrhage",
            "WHO Guidelines - Uterotonics",
            "FDA Black Box Warning - Asthma Contraindication",
            "ISMP High Alert Medications"
        ],
        "interactions": [],
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
        "administration_instructions": {
        },
    },
    "Dinoprostone":     {
        "group": "Obstetrics/Gynecology - Prostaglandin E2 (Cervical Ripening)",
        "vietnamese_name": "Dinoprostone, Cervidil (Insert), Prepidil (Gel)",
        "administration": [
            "Vaginal Insert",
            "Endocervical Gel"
    ],
        "indications": [
            "Làm chín muồi cổ tử cung (cervical ripening) ở thai phụ đủ tháng hoặc gần đủ tháng cần khởi phát chuyển dạ.",
            "Chấm dứt thai kỳ (phá thai) ở tam cá nguyệt 2."
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng dinoprostone/prostaglandins",
                "Tiền sử mổ lấy thai hoặc phẫu thuật tử cung (nguy cơ vỡ tử cung)",
                "Đang có cơn co tử cung cường tính",
                "Suy thai đang diễn tiến",
                "Rau tiền đạo, xuất huyết không rõ nguyên nhân",
                "Chống chỉ định sinh ngả âm đạo (vd: herpes sinh dục hoạt động, ngôi bất thường)"
    ],
            "tương_đối": [
                "Glaucoma",
                "Hen suyễn (ít ảnh hưởng hơn Carboprost nhưng vẫn thận trọng)"
    ],
        },
        "dosage": {
            "vaginal_insert": """Cervidil 10mg: Đặt 1 miếng vào túi cùng sau âm đạo. Để tối đa 12 giờ hoặc đến khi chuyển dạ tích cực. Rút dây để lấy ra.""",
            "cervical_gel": "Prepidil 0.5mg: Bơm vào kênh cổ tử cung. Có thể lặp lại mỗi 6 giờ, tối đa 1.5mg/24h.",
            "notes": "BN nằm nghỉ 30 phút - 2 giờ sau khi đặt. Theo dõi tim thai và cơn co liên tục (CTG).",
        },
        "side_effects": {
            "phổ_biến": [
                "Cơn co tử cung cường tính (tachysystole)",
                "Buồn nôn, nôn, tiêu chảy (ít hơn F2 alpha)",
                "Sốt"
    ],
            "nghiêm_trọng": [
                "Vỡ tử cung (Uterine rupture) - đặc biệt BN có sẹo mổ cũ",
                "Suy thai cấp do cơn co quá mạnh",
                "Thuyên tắc dịch ối (hiếm)"
    ],
        },
        "pregnancy": "C - Dùng để khởi phát chuyển dạ.",
        "interactions": {
            "quan_trọng": [
                "Oxytocin: Không dùng đồng thời. Chờ ít nhất 30 phút sau khi rút Cervidil hoặc 6-12 giờ sau khi dùng gel mới được bắt đầu truyền Oxytocin (nguy cơ vỡ tử cung do cộng hưởng tác dụng)."
    ],
        },
        "mechanism_of_action": "Prostaglandin E2 (PGE2). Làm mềm, xóa mở cổ tử cung (collagenase) và kích thích cơ tư cung co bóp.",
        "monitoring": [
            "Cơn co tử cung (tần số, cường độ)",
            "Tim thai (FHR)",
            "Tiến triển cổ tử cung (Bishop score)"
    ],
        "precautions": {
            "quan_trọng": [
                "Phải thực hiện tại bệnh viện có khả năng phẫu thuật cấp cứu (mổ lấy thai).",
                "Nguy cơ vỡ tử cung cao ở BN có sẹo mổ cũ -> Tốt nhất TRÁNH.",
                "Nếu xảy ra cơn co cường tính/suy thai: Rút ngay Cervidil (dễ dàng), Gel khó lấy ra hơn."
    ],
        },
        "storage": "Bảo quản đông lạnh (Cervidil) hoặc lạnh (Prepidil).",
        "references": {
            "primary_sources": [
                "Cervidil Package Insert",
                "ACOG Practice Bulletin 107: Induction of Labor"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Uterine rupture (especially with prior uterine surgery)", "Fetal distress (due to hyperstimulation)", "Uterine hyperstimulation (tachysystole)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Uterine contractions - CRITICAL (frequency, intensity, duration)", "Fetal heart rate (FHR) - CRITICAL", "Cervical dilation (Bishop score)", "Signs of hyperstimulation (tachysystole)", "Signs of uterine rupture"]
        },
        "guideline_tags": [
            "ACOG Practice Bulletin - Induction of Labor",
            "WHO Guidelines - Labor Induction",
            "FDA Black Box Warning - Uterine Rupture Risk",
            "ISMP High Alert Medications"
        ],
        "pharmacokinetics": {
        },
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
        "administration_instructions": {
        },
    },
}

__all__ = ['UTEROTONICS_DRUGS']
