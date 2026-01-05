"""
Benzodiazepines (Thuốc Benzodiazepine)
Thuốc an thần, chống lo âu, chống co giật.
"""

BENZODIAZEPINES_DRUGS = {
    "Diazepam":     {
        "group": "Psychiatry - Benzodiazepine",
        "vietnamese_name": "Diazepam, Valium",
        "brand_names": {
            "common": [
                "Valium"
    ],
            "vietnam": [
                "Diazepam 5mg/10mg",
                "Seduxen"
    ],
        },
        "administration": [
            "PO",
            "IV",
            "IM"
    ],
        "indications": [
            "Lo âu (Anxiety)",
            "Co giật (Status epilepticus) - IV",
            "Cai rượu (Alcohol withdrawal)",
            "Co cứng cơ (Muscle spasm)",
            "Tiền mê (Premedication)"
    ],
        "dosage": {
            "anxiety": "2-10mg PO x 2-4 lần/ngày.",
            "status_epilepticus": "5-10mg IV, lặp lại sau 10-15 phút nếu cần (tối đa 30mg).",
            "alcohol_withdrawal": "10mg PO x 3-4 lần/ngày ngày 1, sau đó giảm dần.",
            "notes": "Tác dụng kéo dài (half-life 20-100h). Nguy cơ nghiện cao.",
        },
        "side_effects": [
            "Buồn ngủ, chóng mặt",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Nghiện, lệ thuộc (nếu dùng lâu dài)",
            "Ức chế hô hấp (liều cao, IV)",
            "Ngã (ở người cao tuổi)"
    ],
        "contraindications": [
            "Suy hô hấp nặng",
            "Ngưng thở khi ngủ (Sleep apnea) nặng",
            "Suy gan nặng",
            "Myasthenia gravis"
    ],
        "mechanism_of_action": """Tăng cường tác dụng GABA (chất ức chế thần kinh) tại thụ thể GABA-A → An thần, chống lo âu, chống co giật, giãn cơ.""",
        "monitoring": [
            "Mức độ an thần",
            "Hô hấp (đặc biệt khi dùng IV)",
            "Dấu hiệu lệ thuộc, nghiện"
    ],
        "precautions": [
            "Nguy cơ NGHIỆN CAO - Chỉ dùng ngắn hạn (2-4 tuần)",
            "KHÔNG NGỪNG ĐỘT NGỘT sau dùng lâu dài (nguy cơ co giật cai thuốc)",
            "Giảm liều từ từ khi ngừng",
            "Thận trọng ở người cao tuổi (nguy cơ ngã, lú lẫn)",
            "Tránh rượu (tăng ức chế hô hấp)",
            "Không lái xe khi dùng"
    ],
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, lệ thuộc. Dùng chung với opioid tăng nguy cơ ức chế hô hấp, tử vong.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["neurological"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory function", "Sedation level", "Dependence signs"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Abuse, Dependence, Withdrawal",
            "FDA Black Box Warning - Opioid Interaction (Respiratory Depression)",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
        ],
        "interactions": [],
        "pregnancy": "",
        "pharmacokinetics": {
        },
        "storage": "",
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
    "Lorazepam":     {
        "group": "Psychiatry - Benzodiazepine",
        "vietnamese_name": "Lorazepam, Ativan",
        "brand_names": {
            "common": [
                "Ativan"
    ],
            "vietnam": [
                "Lorazepam 1mg/2mg"
    ],
        },
        "administration": [
            "PO",
            "IV",
            "IM"
    ],
        "indications": [
            "Lo âu",
            "Co giật (Status epilepticus)",
            "An thần trước thủ thuật",
            "Kích động cấp (Agitation)"
    ],
        "dosage": {
            "anxiety": "0.5-2mg PO x 2-3 lần/ngày.",
            "status_epilepticus": "4mg IV, lặp lại sau 10-15 phút nếu cần.",
            "premedication": "2-4mg PO/IV/IM.",
            "notes": "Tác dụng trung bình (half-life 10-20h). An toàn hơn Diazepam ở suy gan.",
        },
        "side_effects": [
            "Buồn ngủ",
            "Lú lẫn",
            "Nghiện, lệ thuộc",
            "Ức chế hô hấp (IV)"
    ],
        "mechanism_of_action": "Tương tự Diazepam. An toàn hơn ở suy gan (không chuyển hóa qua CYP450).",
        "precautions": [
            "Tương tự Diazepam",
            "An toàn hơn ở suy gan"
    ],
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, lệ thuộc. Dùng chung với opioid tăng nguy cơ tử vong.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["neurological"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory function", "Sedation level", "Dependence signs"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Abuse, Dependence, Withdrawal",
            "FDA Black Box Warning - Opioid Interaction (Respiratory Depression)",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
        ],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "monitoring": [],
        "pharmacokinetics": {
        },
        "storage": "",
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
    "Midazolam":     {
        "group": "Anesthesia - Benzodiazepine (Sedative)",
        "vietnamese_name": "Midazolam, Dormicum",
        "brand_names": {
            "common": [
                "Versed",
                "Dormicum"
    ],
            "vietnam": [
                "Dormicum 5mg/ml"
    ],
        },
        "administration": [
            "IV",
            "IM",
            "Intranasal"
    ],
        "indications": [
            "An thần cho thủ thuật (Procedural sedation)",
            "Tiền mê",
            "Co giật (trẻ em - Intranasal)",
            "An thần ICU"
    ],
        "dosage": {
            "procedural_sedation": "0.5-2mg IV từ từ, lặp lại nếu cần (tối đa 5mg).",
            "premedication": "0.07-0.08mg/kg IM.",
            "seizure_pediatric": "0.2mg/kg Intranasal (tối đa 10mg).",
            "notes": "Tác dụng NHANH (2-5 phút IV), ngắn (half-life 1.5-2.5h). Dùng cho thủ thuật.",
        },
        "side_effects": [
            "Ức chế hô hấp (nguy hiểm nhất)",
            "Hạ huyết áp",
            "Buồn ngủ",
            "Quên ngược (Anterograde amnesia) - Tác dụng mong muốn"
    ],
        "mechanism_of_action": "Benzodiazepine tác dụng nhanh, ngắn. Dùng cho an thần thủ thuật, tiền mê.",
        "monitoring": [
            "Hô hấp, SpO2 (QUAN TRỌNG)",
            "Huyết áp, mạch",
            "Mức độ an thần"
    ],
        "precautions": [
            "PHẢI có thiết bị hồi sức (Oxy, Ambu, Flumazenil)",
            "Nguy cơ ức chế hô hấp cao - Theo dõi sát",
            "Tiêm IV CHẬM để tránh ức chế hô hấp đột ngột",
            "Có antidote: Flumazenil"
    ],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": "Nguy cơ ức chế hô hấp nghiêm trọng. Phải có thiết bị hồi sức.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["respiratory"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory function (CRITICAL)", "SpO2", "Blood pressure", "Sedation level"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Respiratory Depression",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
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
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
    "Alprazolam":     {
        "group": "Psychiatry - Benzodiazepine",
        "vietnamese_name": "Alprazolam, Xanax",
        "brand_names": {
            "common": [
                "Xanax"
    ],
            "vietnam": [
                "Xanax 0.25/0.5mg",
                "Alprazolam"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Rối loạn lo âu (Anxiety disorder)",
            "Rối loạn hoảng sợ (Panic disorder)"
    ],
        "dosage": {
            "anxiety": "0.25-0.5mg PO x 3 lần/ngày. Tối đa 4mg/ngày.",
            "panic": "0.5mg PO x 3 lần/ngày, tăng dần nếu cần.",
            "notes": "Tác dụng nhanh (1-2h), ngắn (half-life 11h). Nguy cơ nghiện RẤT CAO.",
        },
        "side_effects": [
            "Buồn ngủ",
            "Nghiện, lệ thuộc (RẤT CAO)",
            "Lú lẫn",
            "Rối loạn trí nhớ"
    ],
        "mechanism_of_action": "Benzodiazepine tác dụng nhanh. Nguy cơ nghiện cao nhất trong nhóm.",
        "precautions": [
            "Nguy cơ NGHIỆN RẤT CAO - Tránh dùng lâu dài",
            "Chỉ dùng ngắn hạn (2-4 tuần)",
            "Giảm liều từ từ khi ngừng",
            "Tránh rượu"
    ],
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, lệ thuộc RẤT CAO. Dùng chung với opioid tăng nguy cơ tử vong.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["neurological"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Dependence signs (HIGH RISK)", "Respiratory function", "Sedation level"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Abuse, Dependence, Withdrawal (HIGH RISK)",
            "FDA Black Box Warning - Opioid Interaction (Respiratory Depression)",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
        ],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "monitoring": [],
        "pharmacokinetics": {
        },
        "storage": "",
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
    "Clonazepam":     {
        "group": "Psychiatry/Neurology - Benzodiazepine",
        "vietnamese_name": "Clonazepam, Rivotril",
        "brand_names": {
            "common": [
                "Klonopin",
                "Rivotril"
    ],
            "vietnam": [
                "Rivotril 0.5/2mg"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Rối loạn hoảng sợ (Panic disorder)",
            "Co giật (Epilepsy) - Phụ trợ",
            "Rối loạn lo âu"
    ],
        "dosage": {
            "panic": "0.25mg PO x 2 lần/ngày, tăng dần đến 1mg/ngày.",
            "seizure": "0.5mg PO x 3 lần/ngày, tăng dần nếu cần.",
            "notes": "Tác dụng kéo dài (half-life 30-40h). Dùng cho co giật và lo âu.",
        },
        "side_effects": [
            "Buồn ngủ",
            "Nghiện, lệ thuộc",
            "Lú lẫn",
            "Rối loạn phối hợp vận động"
    ],
        "mechanism_of_action": "Benzodiazepine tác dụng kéo dài. Dùng cho co giật và rối loạn hoảng sợ.",
        "precautions": [
            "Tương tự các benzodiazepine khác",
            "Nguy cơ nghiện cao",
            "Giảm liều từ từ khi ngừng"
    ],
        "contraindications": [],
        "interactions": [],
        "pregnancy": "",
        "monitoring": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, lệ thuộc. Dùng chung với opioid tăng nguy cơ tử vong.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["neurological"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Dependence signs", "Respiratory function", "Sedation level"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Abuse, Dependence, Withdrawal",
            "FDA Black Box Warning - Opioid Interaction (Respiratory Depression)",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
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
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
}
