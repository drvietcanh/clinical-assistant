"""
Migraine Triptans (Serotonin 5-HT1B/1D Agonists)
"""

MIGRAINE_TRIPTANS = {
    "Sumatriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Sumatriptan, Imigran",
        "brand_names": {
            "common": [
                "Imitrex",
                "Imigran"
    ],
            "vietnam": [
                "Sumatriptan",
                "Imigran",
                "Sumagran"
    ],
        },
        "administration": [
            "PO",
            "SC",
            "Nasal Spray"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính (có hoặc không có aura)",
            "Điều trị Cluster Headache (Dạng tiêm SC)"
    ],
        "contraindications": {
            "absolute": [
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Suy gan nặng",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)"
    ],
        },
        "dosage": {
            "adult_oral": "25, 50, hoặc 100 mg. Có thể lặp lại sau 2 giờ. Tối đa 200 mg/24h.",
            "adult_sc": "6 mg SC. Có thể lặp lại sau 1 giờ. Tối đa 12 mg/24h. (Hiệu quả nhanh nhất).",
            "adult_nasal": "5-20 mg/lần. Lặp lại sau 2 giờ. Tối đa 40 mg/24h.",
            "notes": "Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
        },
        "side_effects": [
            "Cảm giác nặng/thắt ngực, cổ họng (Chest tightness) - thường lành tính nhưng cần phân biệt với tim mạch",
            "Chóng mặt, buồn ngủ",
            "Nóng bừng mặt",
            "Phản ứng tại chỗ tiêm (SC)"
    ],
        "interactions": [
            "MAO Inhibitors: Tăng nồng độ Sumatriptan -> Ngộ độc Serotonin/Tác dụng phụ tim mạch.",
            "Ergotamine (trong vòng 24h): Co mạch quá mức -> Chống chỉ định.",
            "SSRI/SNRI: Về lý thuyết tăng nguy cơ Serotonin Syndrome (hiếm gặp trên lâm sàng)."
    ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Nhiều dữ liệu (Sumatriptan Registry) cho thấy tương đối an toàn, không tăng nguy cơ dị tật lớn. Ưu tiên dùng nếu cần thiết.""",
            "lactation": {
                "safety": "Compatible",
                "details": """Bài tiết thấp. Có thể bỏ bú 8-12h sau dùng thuốc để an toàn tuyệt đối, nhưng thường được xem là an toàn.""",
                "recommendation": "",
            },
        },
        "mechanism_of_action": """Kích thích thụ thể 5-HT1B/1D gây co mạch máu não (đang bị giãn trong cơn Migraine) và ức chế giải phóng neuropeptide viêm.""",
        "monitoring": [
            "Huyết áp",
            "Dấu hiệu thiếu máu cơ tim (nếu có nguy cơ cao)"
    ],
        "pregnancy": "",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
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
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
    "Rizatriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Rizatriptan, Maxalt",
        "brand_names": {
            "common": [
                "Maxalt",
                "Maxalt-MLT"
    ],
            "vietnam": [
                "Rizatriptan",
                "Maxalt"
    ],
        },
        "administration": [
            "PO",
            "ODT (Viên phân tán)"
    ],
        "indications": [
            "Migraine cấp tính"
    ],
        "dosage": {
            "adult": "5-10 mg. Lặp lại sau 2 giờ. Tối đa 30 mg/24h.",
            "with_propranolol": "Propranolol làm tăng nồng độ Rizatriptan -> Dùng tối đa 5 mg/lần, tối đa 15 mg/24h.",
            "notes": "Khởi phát tác dụng nhanh (hơn Sumatriptan uống).",
        },
        "interactions": [
            "Propranolol: Tăng nồng độ Rizatriptan 70%. Cần giảm liều Rizatriptan."
    ],
        "side_effects": [
            "Buồn ngủ, chóng mặt",
            "Khô miệng"
    ],
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "Kém an toàn hơn Sumatriptan (ít dữ liệu hơn).",
            "lactation": {
                "safety": "Caution",
                "details": "Thận trọng.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "contraindications": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
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
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
    "Zolmitriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Zolmitriptan, Zomig",
        "brand_names": {
            "common": [
                "Zomig"
    ],
            "vietnam": [
                "Zolmitriptan",
                "Zomig"
    ],
        },
        "administration": [
            "PO",
            "Nasal Spray"
    ],
        "indications": [
            "Migraine cấp tính",
            "Cluster Headache (Nasal Spray - ít dùng hơn Sumatriptan SC)"
    ],
        "dosage": {
            "adult_oral": "2.5 mg. Lặp lại sau 2 giờ. Tối đa 10 mg/24h.",
            "adult_nasal": "5 mg. Tối đa 10 mg/24h.",
        },
        "interactions": [
            "Cimetidine: Ức chế chuyển hóa Zolmitriptan."
    ],
        "side_effects": [],
        "contraindications": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
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
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
}
