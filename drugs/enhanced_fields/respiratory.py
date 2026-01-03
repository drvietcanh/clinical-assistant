"""
Enhanced fields overrides - Respiratory
"""
from typing import Any, Dict


RESPIRATORY_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
        # ======================== SESSION 1: SABAs, LABAs, ICS, METHYLXANTHINES, LEUKOTRIENE ANTAGONISTS ========================
        "Salbutamol": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"cardiovascular": "Moderate (tachycardia, arrhythmias - especially with IV or high doses)", "metabolic": "Moderate (hypokalemia - especially with high doses)", "respiratory": "Low (paradoxical bronchospasm - rare but serious)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Heart rate and blood pressure - CRITICAL (especially with IV or high doses)",
                    "Serum potassium - CRITICAL (hypokalemia risk, especially with high doses)",
                    "Bronchodilator response (peak flow, FEV1)",
                    "Signs of paradoxical bronchospasm (worsening wheezing) - CRITICAL (rare but serious)",
                    "Signs of overdose (tachycardia >120 bpm, severe tremor, arrhythmias)",
                    "Frequency of use - CRITICAL (if >4 times/day, need to reassess treatment and increase ICS)"
                ],
                "look_alike_sound_alike": ["Salbutamol", "Ventolin", "Albuterol", "Terbutaline"]
            },
            "guideline_tags": [
                "GINA Guidelines - Asthma Management",
                "GOLD Guidelines - COPD Management",
                "FDA Black Box Warning - Not for Chronic Use Without ICS",
                "FDA Drug Label - Salbutamol (paradoxical bronchospasm and excessive use warnings)"
            ]
        },

        "Terbutaline": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"cardiovascular": "Moderate (tachycardia, arrhythmias - especially with SC or high doses)", "metabolic": "Moderate (hypokalemia - especially with high doses)", "respiratory": "Low (paradoxical bronchospasm - rare but serious)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Heart rate and blood pressure - CRITICAL (especially with SC or high doses)",
                    "Serum potassium - CRITICAL (hypokalemia risk, especially with high doses)",
                    "Bronchodilator response (peak flow, FEV1)",
                    "Signs of paradoxical bronchospasm (worsening wheezing) - CRITICAL (rare but serious)",
                    "Signs of overdose (tachycardia >120 bpm, severe tremor, arrhythmias)",
                    "Frequency of use - CRITICAL (if >4 times/day, need to reassess treatment and increase ICS)"
                ],
                "look_alike_sound_alike": ["Terbutaline", "Bricanyl", "Salbutamol"]
            },
            "guideline_tags": [
                "GINA Guidelines - Asthma Management",
                "GOLD Guidelines - COPD Management",
                "FDA Black Box Warning - Not for Chronic Use Without ICS",
                "FDA Drug Label - Terbutaline (paradoxical bronchospasm and excessive use warnings)"
            ]
        },

        "Formoterol": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"cardiovascular": "Moderate (tachycardia, arrhythmias)", "metabolic": "Moderate (hypokalemia)", "respiratory": "Low (paradoxical bronchospasm - rare but serious)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Heart rate and blood pressure (especially when starting treatment)",
                    "Bronchodilator response (peak flow, FEV1)",
                    "Signs of paradoxical bronchospasm (worsening wheezing) - CRITICAL (rare but serious)",
                    "Signs of overdose (tachycardia >120 bpm, severe tremor, arrhythmias)",
                    "Frequency of SABA use (if increasing, need to reassess treatment)",
                    "Drug interactions (beta-blockers - CONTRAINDICATED, theophylline, digoxin) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Formoterol", "Foradil", "Oxeze", "Salmeterol"]
            },
            "guideline_tags": [
                "GINA Guidelines - Asthma Management",
                "GOLD Guidelines - COPD Management",
                "FDA Black Box Warning - Never Use Alone for Asthma (Must Combine with ICS)",
                "FDA Drug Label - Formoterol (asthma-related death warning)"
            ]
        },

        "Salmeterol": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"cardiovascular": "Moderate (tachycardia, arrhythmias)", "metabolic": "Moderate (hypokalemia)", "respiratory": "Low (paradoxical bronchospasm - rare but serious)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Heart rate and blood pressure (especially when starting treatment)",
                    "Bronchodilator response (peak flow, FEV1)",
                    "Signs of paradoxical bronchospasm (worsening wheezing) - CRITICAL (rare but serious)",
                    "Signs of overdose (tachycardia >120 bpm, severe tremor, arrhythmias)",
                    "Frequency of SABA use (if increasing, need to reassess treatment)",
                    "Drug interactions (beta-blockers - CONTRAINDICATED, theophylline, digoxin) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Salmeterol", "Serevent", "Formoterol"]
            },
            "guideline_tags": [
                "GINA Guidelines - Asthma Management",
                "GOLD Guidelines - COPD Management",
                "FDA Black Box Warning - Never Use Alone for Asthma (Must Combine with ICS)",
                "FDA Black Box Warning - Asthma-Related Death",
                "FDA Drug Label - Salmeterol (asthma-related death warning)"
            ]
        },

        "Beclomethasone inhaled": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"infectious": "Moderate (oral candidiasis - common)", "endocrine": "Low (HPA axis suppression - rare, only with high doses)", "ophthalmic": "Low (cataracts, glaucoma - rare, only with high doses)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Asthma/COPD response (symptoms, exacerbation frequency, SABA use)",
                    "Oral candidiasis - CRITICAL (check tongue, mouth, especially if not rinsing after use)",
                    "Hoarseness, cough, throat irritation (common local side effects)",
                    "HPA axis function (cortisol, ACTH) - only with high doses (>1600mcg/day)",
                    "Growth in children (only with high doses)",
                    "Drug interactions (ritonavir - CONTRAINDICATED, ketoconazole/itraconazole - increased levels) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Beclomethasone", "Beclovent", "Qvar", "Budesonide", "Fluticasone"]
            },
            "guideline_tags": [
                "GINA Guidelines - Asthma Management",
                "GOLD Guidelines - COPD Management",
                "FDA Drug Label - Beclomethasone (ritonavir interaction and oral candidiasis warnings)"
            ]
        },

        "Theophylline": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neurologic": "High (seizures - at levels >30 mcg/ml, can be fatal)", "cardiovascular": "High (arrhythmias, tachycardia - at levels >20 mcg/ml)", "gastrointestinal": "Moderate (nausea, vomiting - common at levels >20 mcg/ml)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Theophylline blood level - CRITICAL (TDM required, therapeutic range: 10-20 mcg/ml, Black Box Warning)",
                    "Signs of toxicity (nausea, vomiting, tremor, tachycardia, seizures) - CRITICAL",
                    "Heart rate, blood pressure, ECG (arrhythmias risk)",
                    "Blood glucose (may increase)",
                    "Hepatic function (ALT, AST) - CRITICAL (metabolized in liver)",
                    "Renal function (CrCl, eGFR) - CRITICAL (dose adjustment required)",
                    "Drug interactions (ciprofloxacin/enoxacin - AVOID, erythromycin/clarithromycin, cimetidine, rifampin) - CRITICAL",
                    "Smoking status (increases clearance 50-100%, need higher dose)"
                ],
                "look_alike_sound_alike": ["Theophylline", "Theolair", "Uniphyl", "Aminophylline"]
            },
            "guideline_tags": [
                "GINA Guidelines - Asthma Management",
                "GOLD Guidelines - COPD Management",
                "FDA Black Box Warning - Narrow Therapeutic Window (TDM Required)",
                "FDA Black Box Warning - Seizures and Death at High Levels",
                "FDA Drug Label - Theophylline (TDM and toxicity warnings)"
            ]
        },

        "Aminophylline": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neurologic": "High (seizures - at theophylline levels >30 mcg/ml, can be fatal)", "cardiovascular": "High (arrhythmias, tachycardia - at theophylline levels >20 mcg/ml)", "gastrointestinal": "Moderate (nausea, vomiting - common at theophylline levels >20 mcg/ml)", "allergic": "Low (ethylenediamine hypersensitivity - rare)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Theophylline blood level - CRITICAL (TDM required, therapeutic range: 10-20 mcg/ml, Black Box Warning)",
                    "Signs of toxicity (nausea, vomiting, tremor, tachycardia, seizures) - CRITICAL",
                    "Heart rate, blood pressure, ECG (arrhythmias risk)",
                    "Hepatic function (ALT, AST) - CRITICAL (metabolized in liver)",
                    "Renal function (CrCl, eGFR) - CRITICAL (dose adjustment required)",
                    "Signs of ethylenediamine hypersensitivity (rare)",
                    "Drug interactions (ciprofloxacin/enoxacin - AVOID, erythromycin/clarithromycin, cimetidine, rifampin) - CRITICAL",
                    "Dose calculation - CRITICAL (aminophylline = theophylline × 1.25, calculate dose based on theophylline)"
                ],
                "look_alike_sound_alike": ["Aminophylline", "Theophylline ethylenediamine", "Theophylline"]
            },
            "guideline_tags": [
                "GINA Guidelines - Asthma Management",
                "GOLD Guidelines - COPD Management",
                "FDA Black Box Warning - Narrow Therapeutic Window (TDM Required)",
                "FDA Black Box Warning - Seizures and Death at High Levels",
                "FDA Drug Label - Aminophylline (TDM and toxicity warnings)"
            ]
        },

        "Montelukast": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neuropsychiatric": "High (mood changes, depression, suicidal ideation and behavior - Black Box Warning, especially in children and adolescents)", "neurologic": "Moderate (sleep disturbances, nightmares)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Asthma response (symptoms, exacerbation frequency, SABA use)",
                    "Neuropsychiatric symptoms - CRITICAL (mood changes, depression, suicidal ideation and behavior - Black Box Warning, especially in children and adolescents)",
                    "Sleep disturbances (insomnia, nightmares)",
                    "Drug interactions (phenobarbital, rifampin - decreased levels)"
                ],
                "look_alike_sound_alike": ["Montelukast", "Singulair", "Zafirlukast"]
            },
            "guideline_tags": [
                "GINA Guidelines - Asthma Management",
                "FDA Black Box Warning - Neuropsychiatric Events (Mood Changes, Depression, Suicidal Ideation)",
                "FDA Drug Label - Montelukast (neuropsychiatric events warning)"
            ]
        },

        # ======================== RESPIRATORY – THEOPHYLLINE (OLD DATA - TO BE REMOVED) ========================
        "Amikacin": {
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Chưa cập nhật chi tiết; tham khảo guideline và tài liệu nhà sản xuất trước khi dùng cho phụ nữ mang thai.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Chưa rõ mức độ bài tiết vào sữa mẹ; cân nhắc lợi ích và nguy cơ.",
                    "recommendation": "Tham khảo chuyên gia nhi/INF trước khi dùng kéo dài khi cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh đáng kể; chủ yếu thải trừ qua thận.",
                "moderate": "Không cần điều chỉnh đáng kể; theo dõi chức năng gan nếu dùng kéo dài.",
                "severe": "Thận trọng; ưu tiên điều chỉnh theo chức năng thận.",
                "notes": "Aminoglycoside chủ yếu thải qua thận; điều chỉnh liều dựa trên eGFR.",
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
                "treatment": [],
                "monitoring": "Theo dõi chức năng thận, thính lực và nồng độ thuốc (nếu có) trong trường hợp nghi ngờ quá liều hoặc tích luỹ.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "",
                    "timing": "",
                },
                "iv": {
                    "reconstitution": "Pha theo hướng dẫn nhà sản xuất; thường pha trong NaCl 0,9% hoặc D5W.",
                    "infusion_rate": "Truyền chậm theo phác đồ; tránh bolus nhanh.",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Theo dõi chức năng thận, nồng độ thuốc (nếu có điều kiện) để tránh độc tính.",
                },
            },
        },

        "Gentamicin": {
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Chưa cập nhật chi tiết; cân nhắc lợi ích/nguy cơ và tham khảo guideline khi dùng cho phụ nữ mang thai.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Chưa rõ mức độ bài tiết vào sữa mẹ; nguy cơ toàn thân cho trẻ thường thấp do hấp thu kém qua đường tiêu hoá.",
                    "recommendation": "Có thể dùng ngắn hạn với theo dõi thích hợp; tham khảo chuyên gia nếu dùng kéo dài.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh đáng kể; chủ yếu thải trừ qua thận.",
                "moderate": "Không cần điều chỉnh đáng kể.",
                "severe": "Thận trọng; ưu tiên đánh giá và chỉnh liều theo chức năng thận.",
                "notes": "Điều chỉnh liều chủ yếu theo eGFR/CrCl; monitor nồng độ thuốc nếu có.",
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
                "treatment": [],
                "monitoring": "Theo dõi chức năng thận, thính lực, tiền đình và nồng độ thuốc trong trường hợp dùng liều cao/kéo dài.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "",
                    "timing": "",
                },
                "iv": {
                    "reconstitution": "Pha loãng trong NaCl 0,9% hoặc D5W theo khuyến cáo.",
                    "infusion_rate": "Truyền chậm trong 30–60 phút (tuỳ phác đồ).",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Không trộn chung cùng bơm tiêm với penicillin/beta-lactam khác; theo dõi chức năng thận.",
                },
            },
        },

        "Tobramycin": {
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Chưa cập nhật chi tiết; sử dụng khi lợi ích vượt trội nguy cơ và theo dõi sát.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Hấp thu toàn thân thấp khi dùng dạng hít; cân nhắc nguy cơ/lợi ích.",
                    "recommendation": "Tham khảo chuyên gia nếu dùng kéo dài ở phụ nữ đang cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh đáng kể.",
                "moderate": "Không cần điều chỉnh đáng kể.",
                "severe": "Thận trọng; ưu tiên điều chỉnh theo chức năng thận.",
                "notes": "Chủ yếu thải trừ qua thận; điều chỉnh theo eGFR.",
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
                "treatment": [],
                "monitoring": "Theo dõi chức năng thận, thính lực và nồng độ thuốc (nếu có) khi nghi ngờ tích luỹ/quá liều.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "",
                    "timing": "",
                },
                "iv": {
                    "reconstitution": "Pha loãng trong dung dịch truyền phù hợp (NaCl 0,9% hoặc D5W).",
                    "infusion_rate": "Truyền chậm theo phác đồ; tránh bolus nhanh.",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Có thể dùng dạng hít cho bệnh lý hô hấp mạn, tuỳ phác đồ từng cơ sở.",
                },
            },
        },

        "Dopamine": {
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Chưa cập nhật chi tiết; dùng trong bối cảnh cấp cứu khi lợi ích vượt trội nguy cơ.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Thường dùng ngắn hạn trong ICU; dữ liệu cho con bú hạn chế.",
                    "recommendation": "Không phải chỉ định điều trị kéo dài; tham khảo chuyên gia khi cần.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều.",
                "moderate": "Không cần điều chỉnh liều.",
                "severe": "Thận trọng; ưu tiên chỉnh theo đáp ứng huyết động và chức năng cơ quan.",
                "notes": "Chủ yếu được chuyển hoá tại gan và thần kinh; dùng chủ yếu trong ICU với monitor liên tục.",
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
                "treatment": [],
                "monitoring": "Theo dõi huyết áp, nhịp tim, tưới máu ngoại vi, dấu hiệu thiếu máu cơ quan đích.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "",
                    "timing": "",
                },
                "iv": {
                    "reconstitution": "Pha trong NaCl 0,9% hoặc D5W; truyền qua bơm tiêm điện hoặc bơm truyền.",
                    "infusion_rate": "Titration theo đáp ứng huyết áp và cung lượng tim.",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Ưu tiên truyền qua đường tĩnh mạch trung tâm nếu dùng kéo dài; tránh thoát mạch.",
                },
            },
        },

        "Dobutamine": {
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Chưa cập nhật chi tiết; dùng trong bối cảnh cấp cứu tim mạch khi cần thiết.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dùng ngắn hạn trong ICU; dữ liệu an toàn khi cho con bú hạn chế.",
                    "recommendation": "Không dùng kéo dài; đánh giá lợi ích/nguy cơ từng trường hợp.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều.",
                "moderate": "Không cần điều chỉnh liều.",
                "severe": "Thận trọng; chỉnh liều theo đáp ứng lâm sàng.",
                "notes": "Chủ yếu dùng ngắn hạn trong ICU với monitor huyết động liên tục.",
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
                "treatment": [],
                "monitoring": "Theo dõi huyết áp, nhịp tim, dấu hiệu thiếu máu cơ tim hoặc loạn nhịp.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "",
                    "timing": "",
                },
                "iv": {
                    "reconstitution": "Pha trong dung dịch truyền thích hợp (NaCl 0,9%, D5W).",
                    "infusion_rate": "Truyền liên tục với bơm tiêm điện; chỉnh liều theo cung lượng tim và huyết áp.",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Theo dõi liên tục ECG, huyết áp và dấu hiệu suy tim.",
                },
            },
        },

        "Norepinephrine": {
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Dùng chủ yếu trong cấp cứu; cân nhắc lợi ích/nguy cơ cho mẹ và thai.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dùng ngắn hạn trong ICU; dữ liệu cho con bú rất hạn chế.",
                    "recommendation": "Không dùng kéo dài; tham khảo chuyên gia khi cần.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều.",
                "moderate": "Không cần điều chỉnh liều.",
                "severe": "Thận trọng; chỉnh liều theo đáp ứng huyết động.",
                "notes": "Truyền qua bơm tiêm điện với monitor liên tục; ưu tiên đường trung tâm.",
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
                "treatment": [],
                "monitoring": "Theo dõi huyết áp, tưới máu ngoại vi, tổn thương đầu chi và cơ quan đích khi dùng liều cao/kéo dài.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "",
                    "timing": "",
                },
                "iv": {
                    "reconstitution": "Pha trong NaCl 0,9% hoặc dung dịch thích hợp; truyền qua bơm tiêm điện.",
                    "infusion_rate": "Titration theo MAP mục tiêu; thường truyền qua đường trung tâm.",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Theo dõi chặt ECG, huyết áp xâm lấn (nếu có) và tưới máu ngoại vi.",
                },
            },
        },

        "Vasopressin": {
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "Chưa cập nhật chi tiết; sử dụng chủ yếu trong bối cảnh cấp cứu sốc kháng catecholamine.",
                "lactation": {
                    "safety": "Caution",
                    "details": "Dữ liệu hạn chế; cân nhắc lợi ích/nguy cơ.",
                    "recommendation": "Chỉ dùng trong ICU với thời gian ngắn.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều riêng.",
                "moderate": "Không cần điều chỉnh liều riêng.",
                "severe": "Thận trọng; đánh giá toàn trạng huyết động và cơ quan đích.",
                "notes": "Thường dùng liều cố định nhỏ; monitor huyết áp và tưới máu.",
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
                "treatment": [],
                "monitoring": "Theo dõi huyết áp, natri máu, tưới máu chi và dấu hiệu thiếu máu ruột/cơ quan.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "",
                    "timing": "",
                },
                "iv": {
                    "reconstitution": "Pha trong dung dịch truyền phù hợp; truyền liên tục liều thấp.",
                    "infusion_rate": "Tốc độ cố định hoặc titration nhỏ tuỳ phác đồ; thường dùng kèm norepinephrine.",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Chỉ dùng tại ICU/HSTC với monitor huyết động chặt chẽ.",
                },
            },
        },

        "Valsartan": {
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "pregnancy_lactation": {
                "fda_category": "D",
                "pregnancy_details": "Chống chỉ định trong thai kỳ do nguy cơ gây độc cho thai (giảm sản thận, thiểu ối, tử vong thai).",
                "lactation": {
                    "safety": "Caution",
                    "details": "Chưa có nhiều dữ liệu; nồng độ trong sữa mẹ có thể thấp nhưng cần thận trọng.",
                    "recommendation": "Ưu tiên thuốc khác an toàn hơn khi cho con bú, đặc biệt với trẻ sơ sinh/nhũ nhi.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Có thể không cần chỉnh liều.",
                "moderate": "Thận trọng, cân nhắc liều khởi đầu thấp hơn.",
                "severe": "Tránh dùng hoặc dùng rất thận trọng; tham khảo guideline chuyên khoa.",
                "notes": "Một phần chuyển hoá qua gan; cần lưu ý ở bệnh nhân suy gan rõ.",
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
                "treatment": [],
                "monitoring": "Theo dõi huyết áp, chức năng thận và kali máu trong trường hợp dùng liều cao/quá liều.",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống cùng hoặc không cùng thức ăn.",
                    "timing": "Uống 1–2 lần/ngày, cố định thời điểm trong ngày.",
                },
                "iv": {
                    "reconstitution": "",
                    "infusion_rate": "",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Không có dạng tiêm tĩnh mạch thường quy.",
                },
            },
        },

        "Vancomycin": {
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": "Dữ liệu hạn chế; thường được xem là có thể chấp nhận khi cần thiết trong nhiễm trùng nặng.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Hấp thu qua đường tiêu hoá của trẻ kém; nồng độ toàn thân thấp.",
                    "recommendation": "Thường chấp nhận được khi cho con bú, đặc biệt khi dùng đường IV; theo dõi nếu dùng kéo dài.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần điều chỉnh liều riêng.",
                "moderate": "Không cần điều chỉnh liều riêng.",
                "severe": "Thận trọng; điều chỉnh chủ yếu theo chức năng thận.",
                "notes": "Thải trừ chủ yếu qua thận; cần điều chỉnh liều theo eGFR và monitor nồng độ thuốc nếu có.",
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
                "treatment": [],
                "monitoring": "Theo dõi chức năng thận, nồng độ thuốc và dấu hiệu độc tính (ví dụ hội chứng đỏ da, độc tai).",
            },
            "reversal_agents": None,
            "administration_instructions": {
                "oral": {
                    "with_food": "Có thể uống cùng hoặc không cùng thức ăn khi dùng điều trị C. difficile.",
                    "timing": "Chia đều trong ngày theo phác đồ.",
                },
                "iv": {
                    "reconstitution": "Pha theo hướng dẫn nhà sản xuất; truyền chậm để tránh phản ứng đỏ da.",
                    "infusion_rate": "Thường truyền trong ≥60 phút (liều lớn có thể cần lâu hơn).",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Monitor nồng độ đáy (trough) ở bệnh nhân nguy cơ cao hoặc dùng kéo dài.",
                },
            },
        },

}
