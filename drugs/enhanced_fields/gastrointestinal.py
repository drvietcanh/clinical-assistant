"""
Enhanced fields overrides - Gastrointestinal
"""
from typing import Any, Dict


GASTROINTESTINAL_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
        # ======================== GASTROINTESTINAL: H2 ANTAGONISTS ==================
        "Cimetidine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hepatic": "Moderate (hepatotoxicity - elevated transaminases, rare)",
                    "neurologic": "Moderate (confusion - especially in elderly and high doses)",
                    "endocrine": "Low (decreased testosterone, increased prolactin - rare, high doses)",
                    "cardiac": "Low (arrhythmias - rare, high IV doses)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Drug interactions - CRITICAL (strong CYP450 inhibitor - CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP3A4, many serious interactions)",
                    "INR - CRITICAL (if used with warfarin - significant increase in INR, bleeding risk, Black Box Warning)",
                    "Theophylline levels - CRITICAL (if used with theophylline - 30-50% increase, toxicity risk, Black Box Warning)",
                    "Phenytoin levels - CRITICAL (if used with phenytoin - increased levels, toxicity risk, Black Box Warning)",
                    "Lidocaine levels - CRITICAL (if used with lidocaine - increased levels, toxicity risk, Black Box Warning)",
                    "Metformin levels - CRITICAL (if used with metformin - increased levels, lactic acidosis risk)",
                    "Renal function (CrCl) - CRITICAL (dose adjustment required: reduce 50% if CrCl 30-60, reduce 75% if CrCl <30)",
                    "Mental status (confusion risk, especially in elderly and high doses)",
                    "Hepatic function (ALT, AST) - CRITICAL (hepatotoxicity rare but monitor)",
                    "Signs of endocrine effects (decreased libido, gynecomastia - rare, high doses)"
                ],
                "look_alike_sound_alike": ["Cimetidine", "Tagamet", "Ranitidine", "Famotidine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Strong CYP450 Inhibition (Many Serious Drug Interactions)",
                "ACG GERD Treatment Guidelines",
                "FDA Drug Label - Cimetidine (Tagamet)",
                "ISMP High Alert Medications - Drug Interactions"
            ]
        },

        "Famotidine": {
            "contraindications": {
                "tuyệt_đối": [
                    "Dị ứng với famotidine hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng - cần giảm liều 50%",
                    "Suy gan nặng - thận trọng",
                ],
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neurologic": "Moderate (confusion, especially in elderly and renal impairment)", "hematologic": "Low (thrombocytopenia, agranulocytosis - rare)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Renal function (CrCl) - CRITICAL (dose adjustment required if CrCl <50)",
                    "Mental status (confusion risk, especially in elderly and renal impairment)",
                    "Complete blood count (thrombocytopenia, agranulocytosis - rare)"
                ],
                "look_alike_sound_alike": ["Famotidine", "Pepcid", "Ranitidine", "Cimetidine"]
            },
            "guideline_tags": [
                "ACG GERD Treatment Guidelines",
                "FDA Drug Label - Famotidine"
            ],
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Ketoconazole, Itraconazole",
                        "mechanism": "Famotidine giảm acid dạ dày, giảm hấp thu azole antifungals",
                        "effect": "Giảm hấp thu azole, giảm hiệu quả",
                        "management": "Dùng cách nhau ít nhất 2 giờ. Hoặc dùng PPI thay thế.",
                    },
                ],
                "minor": [
                    {
                        "drug": "Warfarin",
                        "mechanism": "Tương tác tối thiểu với warfarin",
                        "effect": "Tăng nhẹ nguy cơ xuất huyết",
                        "management": "Theo dõi INR khi dùng famotidine.",
                    },
                ],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ. Dữ liệu lâm sàng tốt, không có bằng chứng về dị tật thai nhi.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết lượng nhỏ vào sữa; thường an toàn cho trẻ bú mẹ.",
                    "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ về các triệu chứng bất thường (hiếm).",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, theo dõi men gan.",
                "severe": "Thận trọng, có thể cần giảm liều.",
                "notes": "Famotidine chuyển hóa ít qua gan, thải trừ chủ yếu qua thận.",
            },
            "overdose_management": {
                "symptoms": [
                    "Nhức đầu",
                    "Chóng mặt",
                    "Rối loạn tiêu hóa",
                    "Rối loạn nhịp tim (hiếm)",
                ],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": [
                    "Điều trị hỗ trợ triệu chứng",
                    "Theo dõi huyết áp, nhịp tim",
                    "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                ],
                "monitoring": "Huyết áp, nhịp tim, dấu hiệu sốc (hiếm).",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Điều trị hỗ trợ là chính.",
            },
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                    "timing": "Uống 1-2 lần/ngày, có thể trước bữa ăn hoặc trước khi đi ngủ.",
                    "notes": "Điều chỉnh liều theo chức năng thận. Tránh dùng cùng với thuốc cần acid để hấp thu (cách 2 giờ).",
                },
                "iv": {
                    "reconstitution": "Pha trong NaCl 0.9% hoặc D5W, dùng ngay sau pha.",
                    "infusion_rate": "Tiêm/truyền chậm trong ít nhất 2 phút.",
                    "notes": "Theo dõi huyết áp, nhịp tim trong và sau khi truyền.",
                },
            },
        },

        # ======================== GASTROINTESTINAL: PPIs ===========================
        "Rabeprazole": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng rabeprazole hoặc PPI", "Dùng cùng atazanavir"],
                "tương_đối": ["Suy gan nặng", "Loãng xương", "Nhiễm C. difficile"],
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "Moderate (interstitial nephritis - rare but serious)", "metabolic": "Moderate (hypomagnesemia, vitamin B12 deficiency with long-term use)", "skeletal": "Moderate (osteoporosis, fractures with long-term use)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - CRITICAL (interstitial nephritis risk, rare but serious)",
                    "Magnesium levels (hypomagnesemia risk with long-term use)",
                    "Vitamin B12 levels (deficiency risk with long-term use >3 years)",
                    "Bone density (osteoporosis risk with long-term use)",
                    "Drug interactions (atazanavir - CONTRAINDICATED, clopidogrel - may reduce efficacy, warfarin - increased INR) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Rabeprazole", "Aciphex", "Omeprazole", "Esomeprazole"]
            },
            "guideline_tags": [
                "ACG GERD Treatment Guidelines",
                "FDA Drug Safety Communication - Clopidogrel Interaction",
                "FDA Drug Label - Rabeprazole (interstitial nephritis and hypomagnesemia warnings)"
            ],
            "drug_interactions": {
                "major": [
                    {
                        "drug": "Atazanavir",
                        "mechanism": "Giảm hấp thu atazanavir",
                        "effect": "Giảm hiệu quả điều trị HIV",
                        "management": "CHỐNG CHỈ ĐỊNH dùng cùng.",
                    },
                ],
                "moderate": [
                    {"drug": "Warfarin", "mechanism": "Có thể tăng INR", "effect": "Tăng INR", "management": "Theo dõi INR."},
                    {"drug": "Ketoconazole, Itraconazole", "mechanism": "Giảm hấp thu", "effect": "Giảm hiệu quả", "management": "Cách 2 giờ."},
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "An toàn trong thai kỳ.",
                "lactation": {"safety": "Compatible", "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.", "recommendation": "Có thể dùng khi cho con bú."},
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng.",
                "severe": "Thận trọng, có thể giảm liều.",
                "notes": "Rabeprazole chuyển hóa qua gan (CYP2C19, CYP3A4).",
            },
            "overdose_management": {
                "symptoms": ["Nhức đầu", "Buồn nôn", "Tiêu chảy"],
                "antidote": "Không có antidote đặc hiệu.",
                "treatment": ["Điều trị hỗ trợ triệu chứng"],
                "monitoring": "Dấu hiệu sinh tồn.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Uống 30-60 phút TRƯỚC bữa ăn.",
                    "timing": "Uống vào buổi sáng trước bữa sáng.",
                    "notes": "KHÔNG được nhai hoặc nghiền viên bao tan trong ruột.",
                },
            },
        },

        "Tegoprazan": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng tegoprazan hoặc PCAB"],
                "tương_đối": ["Suy gan nặng", "Loãng xương"],
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"metabolic": "Moderate (hypomagnesemia, vitamin B12 deficiency with long-term use)", "skeletal": "Moderate (osteoporosis, fractures with long-term use)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Magnesium levels (hypomagnesemia risk with long-term use)",
                    "Vitamin B12 levels (deficiency risk with long-term use)",
                    "Bone density (osteoporosis risk with long-term use)",
                    "Hepatic function (ALT, AST) - CRITICAL (metabolized via liver)"
                ],
                "look_alike_sound_alike": ["Tegoprazan", "K-CAB", "Vonoprazan", "Omeprazole"]
            },
            "guideline_tags": [
                "ACG GERD Treatment Guidelines",
                "FDA Drug Label - Tegoprazan (PCAB - Potassium-Competitive Acid Blocker)"
            ],
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "Không có dữ liệu",
                "pregnancy_details": "Thiếu dữ liệu. Thận trọng trong thai kỳ.",
                "lactation": {"safety": "Unknown", "details": "Thiếu dữ liệu.", "recommendation": "Thận trọng khi cho con bú."},
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng.",
                "severe": "Thận trọng, có thể giảm liều.",
                "notes": "Tegoprazan chuyển hóa qua gan.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn.",
                    "timing": "Uống 1 lần/ngày.",
                    "notes": "PCAB (Potassium-Competitive Acid Blocker), tác dụng nhanh hơn PPI.",
                },
            },
        },

        "Vonoprazan": {
            "contraindications": {
                "tuyệt_đối": ["Dị ứng vonoprazan hoặc PCAB"],
                "tương_đối": ["Suy gan nặng", "Loãng xương"],
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"metabolic": "Moderate (hypomagnesemia, vitamin B12 deficiency with long-term use)", "skeletal": "Moderate (osteoporosis, fractures with long-term use)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Magnesium levels (hypomagnesemia risk with long-term use)",
                    "Vitamin B12 levels (deficiency risk with long-term use)",
                    "Bone density (osteoporosis risk with long-term use)",
                    "Hepatic function (ALT, AST) - CRITICAL (metabolized via liver)"
                ],
                "look_alike_sound_alike": ["Vonoprazan", "Takecab", "Tegoprazan", "Omeprazole"]
            },
            "guideline_tags": [
                "ACG GERD Treatment Guidelines",
                "FDA Drug Label - Vonoprazan (PCAB - Potassium-Competitive Acid Blocker)"
            ],
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "Không có dữ liệu",
                "pregnancy_details": "Thiếu dữ liệu. Thận trọng trong thai kỳ.",
                "lactation": {"safety": "Unknown", "details": "Thiếu dữ liệu.", "recommendation": "Thận trọng khi cho con bú."},
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng.",
                "severe": "Thận trọng, có thể giảm liều.",
                "notes": "Vonoprazan chuyển hóa qua gan.",
            },
            "reversal_agents": {"available": False, "agents": [], "notes": "Không có thuốc giải độc đặc hiệu."},
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống với hoặc không có thức ăn.",
                    "timing": "Uống 1 lần/ngày.",
                    "notes": "PCAB (Potassium-Competitive Acid Blocker), tác dụng nhanh hơn PPI.",
                },
            },
        },

        # ======================== GASTROINTESTINAL: ADDITIONAL PPIs ==================
        "Esomeprazole": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "Moderate (interstitial nephritis - rare but serious)", "metabolic": "Moderate (hypomagnesemia, vitamin B12 deficiency with long-term use)", "skeletal": "Moderate (osteoporosis, fractures with long-term use)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - CRITICAL (interstitial nephritis risk, rare but serious)",
                    "Magnesium levels (hypomagnesemia risk with long-term use)",
                    "Vitamin B12 levels (deficiency risk with long-term use >3 years)",
                    "Bone density (osteoporosis risk with long-term use)",
                    "Drug interactions (clopidogrel - may reduce efficacy, atazanavir - reduced absorption, warfarin - increased INR) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Esomeprazole", "Nexium", "Omeprazole", "Lansoprazole"]
            },
            "guideline_tags": [
                "ACG GERD Treatment Guidelines",
                "FDA Drug Safety Communication - Clopidogrel Interaction",
                "FDA Drug Label - Esomeprazole (interstitial nephritis and hypomagnesemia warnings)"
            ]
        },

        "Lansoprazole": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"renal": "Moderate (interstitial nephritis - rare but serious)", "metabolic": "Moderate (hypomagnesemia, vitamin B12 deficiency with long-term use)", "skeletal": "Moderate (osteoporosis, fractures with long-term use)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - CRITICAL (interstitial nephritis risk, rare but serious)",
                    "Magnesium levels (hypomagnesemia risk with long-term use)",
                    "Vitamin B12 levels (deficiency risk with long-term use >3 years)",
                    "Bone density (osteoporosis risk with long-term use)",
                    "Drug interactions (atazanavir - reduced absorption, warfarin - increased INR, theophylline - increased levels) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Lansoprazole", "Prevacid", "Omeprazole", "Esomeprazole"]
            },
            "guideline_tags": [
                "ACG GERD Treatment Guidelines",
                "FDA Drug Label - Lansoprazole (interstitial nephritis and hypomagnesemia warnings)"
            ]
        },

        # ======================== GASTROINTESTINAL: ANTIEMETICS (5-HT3) ==================
        "Ondansetron": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (QT prolongation - can cause torsades de pointes, can be fatal, Black Box Warning)",
                    "gastrointestinal": "Low (constipation - common)",
                    "neurologic": "Low (headache, dizziness - common)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT interval) - CRITICAL (before and during treatment, especially at high doses, Black Box Warning)",
                    "Electrolytes (potassium, magnesium) - CRITICAL (hypokalemia, hypomagnesemia increase QT prolongation risk, Black Box Warning)",
                    "Hepatic function (ALT, AST) - CRITICAL (hepatic impairment increases QT prolongation risk, reduce dose 50% if severe, Black Box Warning)",
                    "Signs of arrhythmias (palpitations, dizziness, syncope) - CRITICAL (torsades de pointes risk, Black Box Warning)",
                    "Drug interactions (apomorphine - CONTRAINDICATED, other QT-prolonging drugs - avoid or monitor closely, CYP2D6 inhibitors - increase ondansetron levels) - CRITICAL",
                    "Dose limits - CRITICAL (max 32mg/day to reduce QT prolongation risk, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Ondansetron", "Zofran", "Granisetron", "Palonosetron"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - QT Prolongation (Can Cause Torsades de Pointes, Can Be Fatal)",
                "ISMP High Alert Medications",
                "ASCO Guidelines - Antiemetic Therapy for Chemotherapy-Induced Nausea and Vomiting",
                "FDA Drug Label - Ondansetron (Zofran)"
            ]
        },

        # ======================== GASTROINTESTINAL: PROKINETICS ==================
        "Metoclopramide": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neurologic": "High (tardive dyskinesia - can be permanent, Black Box Warning, risk increases with duration and dose)",
                    "neurologic_extrapyramidal": "High (extrapyramidal symptoms - dystonia, parkinsonism, akathisia, common, especially in young patients)",
                    "serotonin": "Moderate (serotonin syndrome - when used with SSRI/SNRI, can be serious)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Tardive dyskinesia (involuntary movements of face, tongue, limbs) - CRITICAL (can be permanent, Black Box Warning, stop immediately if signs appear)",
                    "Extrapyramidal symptoms (dystonia, parkinsonism, akathisia) - CRITICAL (common, especially in young patients, treat with diphenhydramine or benztropine)",
                    "Duration of treatment - CRITICAL (do not use >12 weeks, Black Box Warning, risk increases with duration)",
                    "Serotonin syndrome (agitation, hyperthermia, hyperreflexia) - CRITICAL (when used with SSRI/SNRI, can be serious)",
                    "Renal function (CrCl) - CRITICAL (dose adjustment required: reduce 25-50% if CrCl 30-60, reduce 50-75% if CrCl <30)",
                    "Hepatic function (ALT, AST) - CRITICAL (metabolized via CYP2D6, caution in hepatic impairment)",
                    "Drug interactions (SSRI/SNRI - serotonin syndrome risk, antipsychotics - increased extrapyramidal symptoms, anticholinergics - antagonize prokinetic effect) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Metoclopramide", "Primperan", "Domperidone", "Prochlorperazine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Tardive Dyskinesia (Can Be Permanent, Do Not Use >12 Weeks)",
                "ISMP High Alert Medications",
                "FDA Drug Label - Metoclopramide (Primperan)",
                "ACG Guidelines - Gastroparesis Treatment"
            ]
        },

        # ======================== GASTROINTESTINAL: ANTIDIARRHEALS ==================
        "Loperamide": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (cardiac events - serious arrhythmias including torsades de pointes, QT prolongation, can be fatal, Black Box Warning, especially with high doses or abuse)",
                    "respiratory": "High (respiratory depression - can be fatal, especially with high doses or abuse, Black Box Warning)",
                    "neurologic": "High (CNS depression - can be fatal, especially with high doses or abuse, Black Box Warning)",
                    "gastrointestinal": "Moderate (constipation, ileus - common)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT interval) - CRITICAL (cardiac events risk, serious arrhythmias including torsades de pointes, Black Box Warning)",
                    "Signs of cardiac events (palpitations, dizziness, syncope, arrhythmias) - CRITICAL (serious arrhythmias including torsades de pointes, can be fatal, Black Box Warning)",
                    "Respiratory depression (decreased respiratory rate, decreased SpO2) - CRITICAL (can be fatal, especially with high doses or abuse, Black Box Warning)",
                    "CNS depression (decreased consciousness, sedation) - CRITICAL (can be fatal, especially with high doses or abuse, Black Box Warning)",
                    "Dose limits - CRITICAL (max 16mg/day, do not exceed recommended dose, Black Box Warning)",
                    "Signs of abuse - CRITICAL (high doses, seeking multiple prescriptions, Black Box Warning)",
                    "Hepatic function (ALT, AST) - CRITICAL (metabolized via CYP3A4 and CYP2C8, caution in hepatic impairment, reduce dose 50% if moderate/severe)",
                    "Renal function (CrCl) - CRITICAL (caution in renal impairment, reduce dose or avoid if severe)",
                    "Drug interactions (CYP3A4 inhibitors - ketoconazole, itraconazole, ritonavir, clarithromycin - CONTRAINDICATED with high doses, increase loperamide levels and cardiac/respiratory depression risk, opioids - increased respiratory depression risk) - CRITICAL",
                    "Naloxone availability - CRITICAL (opioid antagonist, can reverse respiratory depression, use 0.4-2mg IV/IM/SC, repeat every 2-3 min if needed, max 10mg)"
                ],
                "look_alike_sound_alike": ["Loperamide", "Imodium", "Diphenoxylate", "Codeine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Cardiac Events (Serious Arrhythmias Including Torsades de Pointes, Can Be Fatal)",
                "FDA Black Box Warning - Respiratory Depression (Can Be Fatal, Especially with High Doses or Abuse)",
                "FDA Black Box Warning - CNS Depression (Can Be Fatal, Especially with High Doses or Abuse)",
                "FDA Drug Label - Loperamide (Imodium)",
                "FDA Safety Communication - Loperamide Abuse and Overdose (2016)"
            ]
        },

        # ======================== GASTROINTESTINAL: LAXATIVES ==================
        "Bisacodyl": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "gastrointestinal": "Moderate (abdominal cramps, diarrhea - common)",
                    "metabolic": "Moderate (electrolyte imbalance - hypokalemia, hyponatremia, with prolonged use or abuse)",
                    "gastrointestinal_dependency": "Moderate (laxative dependency - with prolonged use)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Electrolytes (potassium, sodium) - CRITICAL (hypokalemia, hyponatremia risk with prolonged use or abuse)",
                    "Duration of use - CRITICAL (short-term use only, avoid prolonged use to prevent dependency and electrolyte imbalance)",
                    "Signs of laxative dependency - CRITICAL (with prolonged use)",
                    "Drug interactions (milk, antacids, PPIs - dissolve enteric coating early, causing gastric irritation, take separately) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Bisacodyl", "Dulcolax", "Senna", "Phenolphthalein"]
            },
            "guideline_tags": [
                "ACG Guidelines - Constipation Treatment",
                "FDA Drug Label - Bisacodyl (Dulcolax)"
            ]
        },

        "Lactulose": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "gastrointestinal": "Moderate (bloating, flatulence, abdominal cramps - very common, especially at initiation or rapid dose increase)",
                    "metabolic": "Moderate (electrolyte imbalance - hypokalemia, hyponatremia, with severe diarrhea)",
                    "gastrointestinal_diarrhea": "Moderate (diarrhea - common, especially with high doses)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Electrolytes (potassium, sodium) - CRITICAL (hypokalemia, hyponatremia risk with severe diarrhea)",
                    "Stool frequency and consistency - CRITICAL (target 2-3 soft stools/day for hepatic encephalopathy, adjust dose accordingly)",
                    "Ammonia levels - CRITICAL (for hepatic encephalopathy, monitor response)",
                    "Mental status - CRITICAL (for hepatic encephalopathy, monitor improvement)",
                    "Drug interactions (antacids, antibiotics - may reduce effectiveness in hepatic encephalopathy) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Lactulose", "Duphalac", "Sorbitol", "Polyethylene glycol"]
            },
            "guideline_tags": [
                "ACG Guidelines - Constipation Treatment",
                "AASLD Guidelines - Hepatic Encephalopathy Treatment",
                "FDA Drug Label - Lactulose (Duphalac)"
            ]
        },

        # ======================== GASTROINTESTINAL: IBD/5-ASA ==================
        "Mesalazine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "renal": "High (interstitial nephritis - rare but serious, can be permanent, requires monitoring)",
                    "hematologic": "Low (blood dyscrasias - leukopenia, hemolytic anemia, rare)",
                    "hepatic": "Low (hepatotoxicity - elevated transaminases, rare)",
                    "gastrointestinal": "Moderate (nausea, abdominal pain, diarrhea - common)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - CRITICAL (before treatment, after 3 months, then every 6-12 months, interstitial nephritis risk, rare but serious)",
                    "CBC (blood dyscrasias - leukopenia, hemolytic anemia, rare)",
                    "Hepatic function (ALT, AST) - CRITICAL (periodically, hepatotoxicity rare)",
                    "Drug interactions (azathioprine/6-MP - increased myelosuppression risk, NSAIDs - increased nephrotoxicity risk) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Mesalazine", "Mesalamine", "Salofalk", "Pentasa", "Asacol", "Sulfasalazine"]
            },
            "guideline_tags": [
                "ACG Guidelines - Ulcerative Colitis Treatment",
                "FDA Drug Label - Mesalazine (Mesalamine)",
                "ECCO Guidelines - Inflammatory Bowel Disease Treatment"
            ]
        },

        "Sulfasalazine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "hematologic": "High (blood dyscrasias - hemolytic anemia especially in G6PD deficiency, leukopenia, thrombocytopenia, rare but serious)",
                    "hepatic": "Moderate (hepatotoxicity - elevated transaminases, rare)",
                    "renal": "Moderate (nephrotoxicity - rare)",
                    "gastrointestinal": "High (nausea, vomiting, abdominal pain, diarrhea - very common, especially at initiation)",
                    "dermatologic": "Moderate (rash, urticaria - sulfonamide allergy, common)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "CBC (blood dyscrasias) - CRITICAL (before treatment, after 2-4 weeks, then every 3 months first year, then every 6-12 months, hemolytic anemia especially in G6PD deficiency, leukopenia, thrombocytopenia)",
                    "G6PD testing - CRITICAL (if possible, especially in high-risk populations, G6PD deficiency increases hemolytic anemia risk)",
                    "Hepatic function (ALT, AST) - CRITICAL (periodically, hepatotoxicity rare)",
                    "Renal function (creatinine, eGFR) - CRITICAL (periodically, nephrotoxicity rare)",
                    "Folate levels - CRITICAL (sulfasalazine reduces folate absorption, supplement with folic acid 1mg/day)",
                    "Signs of hypersensitivity (rash, fever, sore throat) - CRITICAL (sulfonamide allergy, stop immediately if severe)",
                    "Drug interactions (warfarin - may increase INR, folate - need supplementation) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Sulfasalazine", "Salazopyrin", "Mesalazine", "Mesalamine"]
            },
            "guideline_tags": [
                "ACG Guidelines - Ulcerative Colitis Treatment",
                "FDA Drug Label - Sulfasalazine (Salazopyrin)",
                "ECCO Guidelines - Inflammatory Bowel Disease Treatment"
            ]
        },

        # ======================== GASTROINTESTINAL: MUCOSAL PROTECTANTS ==================
        "Misoprostol": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "reproductive": "High (abortion, birth defects - Black Box Warning, CONTRAINDICATED in pregnancy)",
                    "gastrointestinal": "High (diarrhea - very common, especially at initiation, abdominal cramps - common)",
                    "bleeding": "Moderate (increased bleeding risk - when used with anticoagulants)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Pregnancy test - CRITICAL (before treatment, Black Box Warning, CONTRAINDICATED in pregnancy)",
                    "Contraception - CRITICAL (effective contraception required in women of childbearing age, Black Box Warning)",
                    "Signs of pregnancy (vaginal bleeding, uterine contractions) - CRITICAL (Black Box Warning, stop immediately if pregnant)",
                    "Diarrhea - CRITICAL (very common, especially at initiation, usually self-limiting)",
                    "INR - CRITICAL (if used with warfarin, increased bleeding risk)",
                    "Drug interactions (magnesium antacid - increased GI side effects, anticoagulants - increased bleeding risk) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Misoprostol", "Cytotec", "Dinoprostone", "Carboprost"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Pregnancy (CONTRAINDICATED - Causes Abortion, Birth Defects)",
                "ACG Guidelines - NSAID-Induced Ulcer Prevention",
                "FDA Drug Label - Misoprostol (Cytotec)"
            ]
        },

        "Sucralfate": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "renal": "High (aluminum accumulation - in severe renal impairment, can cause neurotoxicity, bone toxicity, Black Box Warning)",
                    "gastrointestinal": "Moderate (constipation - common)",
                    "drug_absorption": "High (reduces absorption of many drugs - significant drug interactions)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - CRITICAL (before and during treatment, especially if long-term use, Black Box Warning, contraindicated if CrCl <30)",
                    "Signs of aluminum toxicity (neurological symptoms, bone weakness) - CRITICAL (in severe renal impairment, Black Box Warning)",
                    "Drug interactions - CRITICAL (separate by 2 hours: PPI/H2 blockers/antacids - reduce effectiveness, warfarin - may increase INR, phenytoin/digoxin/quinolones/thyroxine - reduce absorption) - CRITICAL",
                    "INR - CRITICAL (if used with warfarin, may increase INR)"
                ],
                "look_alike_sound_alike": ["Sucralfate", "Carafate", "Aluminum hydroxide", "Magnesium hydroxide"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Aluminum Accumulation (In Severe Renal Impairment, Can Cause Neurotoxicity, Bone Toxicity)",
                "ACG Guidelines - Peptic Ulcer Treatment",
                "FDA Drug Label - Sucralfate (Carafate)"
            ]
        },

        "Domperidone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (QT prolongation, torsades de pointes, fatal arrhythmias - with high doses, Black Box Warning)",
                    "endocrine": "Moderate (hyperprolactinemia - common, galactorrhea, menstrual disorders)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT interval) - CRITICAL (especially with high doses >80mg/day, renal/hepatic impairment, or with QT-prolonging drugs, Black Box Warning)",
                    "Electrolytes (potassium, magnesium) - CRITICAL (correct abnormalities before use, hypokalemia/hypomagnesemia increase QT prolongation risk)",
                    "Signs of arrhythmia (palpitations, dizziness, syncope, irregular heartbeat) - CRITICAL (Black Box Warning)",
                    "Signs of hyperprolactinemia (galactorrhea, menstrual disorders, breast pain) - CRITICAL (common)",
                    "Renal function (CrCl) - CRITICAL (dose adjustment needed if CrCl <60, reduce 50% if CrCl <30)",
                    "Hepatic function - CRITICAL (dose adjustment needed in severe hepatic impairment, increased QT prolongation risk)",
                    "Drug interactions (CYP3A4 inhibitors - ketoconazole, itraconazole, ritonavir, clarithromycin, erythromycin - increase domperidone levels, increase QT prolongation risk) - CRITICAL",
                    "Do NOT exceed 80mg/day - CRITICAL (Black Box Warning, increased QT prolongation risk)"
                ],
                "look_alike_sound_alike": ["Domperidone", "Motilium", "Metoclopramide", "Prochlorperazine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - QT Prolongation (Torsades de Pointes, Fatal Arrhythmias with High Doses)",
                "ISMP High Alert Medications",
                "ACG Guidelines - Gastroparesis Management",
                "FDA Drug Label - Domperidone (Motilium)"
            ]
        },

        "Granisetron": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "Low (QT prolongation - rare)",
                    "hepatic": "Low (elevated transaminases - rare)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT interval) - CRITICAL (if high doses or risk factors for QT prolongation)",
                    "Hepatic function (ALT, AST) - CRITICAL (if long-term use, rare elevated transaminases)",
                    "Signs of constipation - CRITICAL (common side effect)",
                    "Drug interactions (apomorphine - CONTRAINDICATED, other 5-HT3 antagonists - avoid concurrent use) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Granisetron", "Kytril", "Ondansetron", "Palonosetron"]
            },
            "guideline_tags": [
                "ASCO Guidelines - Antiemetic Therapy for Chemotherapy-Induced Nausea and Vomiting",
                "FDA Drug Label - Granisetron (Kytril)"
            ]
        },

        "Palonosetron": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "Low (QT prolongation - rare)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT interval) - CRITICAL (if risk factors for QT prolongation)",
                    "Hepatic function (ALT, AST) - CRITICAL (if long-term use, dose adjustment may be needed in severe hepatic impairment)",
                    "Signs of constipation - CRITICAL (common side effect)",
                    "Drug interactions (apomorphine - CONTRAINDICATED) - CRITICAL",
                    "Note: Long half-life (40 hours) - single dose provides 48-72 hours of protection"
                ],
                "look_alike_sound_alike": ["Palonosetron", "Aloxi", "Ondansetron", "Granisetron"]
            },
            "guideline_tags": [
                "ASCO Guidelines - Antiemetic Therapy for Chemotherapy-Induced Nausea and Vomiting",
                "FDA Drug Label - Palonosetron (Aloxi)"
            ]
        },

        "Tofacitinib": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "infectious": "High (serious infections including opportunistic infections, TB - Black Box Warning)",
                    "hematologic": "High (thrombosis - DVT, PE, arterial thrombosis, Black Box Warning; malignancy - lymphoma, non-melanoma skin cancer, Black Box Warning)",
                    "hepatic": "Moderate (hepatotoxicity - elevated ALT/AST, can be serious)",
                    "metabolic": "Moderate (increased cholesterol - LDL, HDL, triglycerides)",
                    "cardiovascular": "High (major adverse cardiovascular events - MACE, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of infection (fever, chills, cough, dyspnea, dysuria) - CRITICAL (serious infections common, Black Box Warning)",
                    "Tuberculosis (TB) screening - CRITICAL (before starting, Black Box Warning)",
                    "Complete blood count (CBC) - CRITICAL (neutropenia, lymphopenia, anemia - monitor before and periodically)",
                    "Liver function tests (ALT, AST) - CRITICAL (before, periodically, hepatotoxicity risk)",
                    "Lipid panel (LDL, HDL, triglycerides) - CRITICAL (before, 3 months after, then periodically)",
                    "Signs of thrombosis (chest pain, dyspnea, leg pain/swelling) - CRITICAL (DVT/PE risk, Black Box Warning)",
                    "Signs of malignancy (lymphadenopathy, skin lesions) - CRITICAL (lymphoma, non-melanoma skin cancer risk, Black Box Warning)",
                    "Renal function (creatinine, eGFR) - CRITICAL (dose adjustment needed if CrCl 30-60: reduce 50%, avoid if CrCl <30)",
                    "Vaccine status - CRITICAL (complete all vaccines before starting, avoid live vaccines during and after treatment)",
                    "Drug interactions (strong CYP3A4 inhibitors/inducers, immunosuppressants) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Tofacitinib", "Xeljanz", "Baricitinib", "Upadacitinib"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Serious Infections (Opportunistic Infections, TB)",
                "FDA Black Box Warning - Thrombosis (DVT, PE, Arterial Thrombosis)",
                "FDA Black Box Warning - Malignancy (Lymphoma, Non-Melanoma Skin Cancer)",
                "FDA Black Box Warning - Major Adverse Cardiovascular Events (MACE)",
                "ACG Guidelines - Ulcerative Colitis Management",
                "ECCO Guidelines - Crohn's Disease and Ulcerative Colitis",
                "FDA Drug Label - Tofacitinib (Xeljanz)"
            ]
        }

}
