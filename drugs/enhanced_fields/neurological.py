"""
Enhanced fields overrides - Neurological
"""
from typing import Any, Dict


NEUROLOGICAL_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
    # ======================== BATCH 4: GI & NEUROLOGICAL DRUGS ========================
        "Omeprazole": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với omeprazole hoặc PPI",
                ],
                "tương_đối": [
                    "Suy gan nặng - giảm liều",
                    "Suy thận nặng - không cần giảm liều nhưng thận trọng",
                    "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                    "Thiếu vitamin B12 - giảm hấp thu khi dùng lâu dài",
                    "Nhiễm Clostridium difficile - tăng nguy cơ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Pantoprazole": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với pantoprazole hoặc PPI",
                ],
                "tương_đối": [
                    "Suy gan nặng - giảm liều",
                    "Suy thận nặng - không cần giảm liều nhưng thận trọng",
                    "Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài",
                    "Thiếu vitamin B12 - giảm hấp thu khi dùng lâu dài",
                    "Nhiễm Clostridium difficile - tăng nguy cơ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Ranitidine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ranitidine hoặc H2 blocker",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <50) - giảm liều",
                    "Suy gan nặng - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Famotidine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với famotidine hoặc H2 blocker",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <50) - giảm liều",
                    "Suy gan nặng - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Paracetamol": {
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": (
                    "Được xem là an toàn để hạ sốt và giảm đau trong tất cả các giai đoạn của thai kỳ khi dùng ở liều điều trị. "
                    "Tuy nhiên, nên dùng liều thấp nhất có hiệu quả trong thời gian ngắn nhất."
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ với lượng nhỏ. Được Viện Nhi khoa Hoa Kỳ (AAP) xếp vào nhóm thuốc an toàn khi cho con bú.",
                    "recommendation": "Có thể sử dụng. Không cần ngừng cho con bú.",
                },
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với paracetamol",
                    "Suy gan nặng",
                    "Nghiện rượu nặng",
                ],
                "tương_đối": [
                    "Suy gan vừa - giảm liều tối đa",
                    "Suy thận nặng - thận trọng",
                    "Thiếu G6PD - thận trọng",
                    "Suy dinh dưỡng - tăng nguy cơ độc tính",
                ],
            },
        },

        "Ibuprofen": {
            "pregnancy_lactation": {
                "fda_category": "C (D trong 3 tháng cuối)",
                "pregnancy_details": (
                    "FDA Category C trong 6 tháng đầu; Category D trong 3 tháng cuối (nguy cơ đóng ống động mạch sớm, thiểu niệu thai nhi, "
                    "kéo dài thời gian chuyển dạ). KHÔNG DÙNG trong 3 tháng cuối thai kỳ."
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết rất ít vào sữa mẹ (liều tương đối cho trẻ < 0.6%). AAP xếp vào nhóm an toàn.",
                    "recommendation": "Có thể sử dụng. Là lựa chọn NSAID ưu tiên cho phụ nữ cho con bú.",
                },
            },
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ibuprofen hoặc NSAID",
                    "Tiền sử hen suyễn do aspirin/NSAID",
                    "Loét dạ dày tá tràng đang hoạt động",
                    "Xuất huyết tiêu hóa đang hoạt động",
                    "Suy tim nặng (NYHA III-IV)",
                    "Có thai (3 tháng cuối)",
                ],
                "tương_đối": [
                    "Tiền sử loét dạ dày tá tràng",
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Suy gan nặng - thận trọng",
                    "Suy tim vừa - thận trọng",
                    "Tăng huyết áp không kiểm soát",
                    "Đang dùng thuốc chống đông",
                    "Có thai (1-2 tháng đầu) - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                ],
            },
        },

        "Diclofenac": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với diclofenac hoặc NSAID",
                    "Tiền sử hen suyễn do aspirin/NSAID",
                    "Loét dạ dày tá tràng đang hoạt động",
                    "Xuất huyết tiêu hóa đang hoạt động",
                    "Suy tim nặng (NYHA III-IV)",
                    "Suy gan nặng",
                    "Suy thận nặng (CrCl <30)",
                    "Có thai (3 tháng cuối) - nguy cơ đóng ống động mạch sớm",
                ],
                "tương_đối": [
                    "Tiền sử loét dạ dày tá tràng",
                    "Suy thận vừa (CrCl 30-60) - thận trọng",
                    "Suy gan vừa - thận trọng",
                    "Suy tim vừa - thận trọng",
                    "Tăng huyết áp không kiểm soát",
                    "Đang dùng thuốc chống đông",
                    "Có thai (1-2 tháng đầu và giữa) - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                ],
            },
        },

        "Carbamazepine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với carbamazepine",
                    "Block nhĩ thất độ 2-3",
                    "Suy gan nặng",
                    "Tiền sử tủy xương bị ức chế",
                    "Đang dùng MAO inhibitor",
                ],
                "tương_đối": [
                    "Suy gan vừa - thận trọng, theo dõi chức năng gan",
                    "Suy thận nặng - thận trọng",
                    "Bệnh tim mạch - tăng nguy cơ block AV",
                    "Bệnh nhân có tiền sử rối loạn tâm thần",
                    "Glaucoma góc đóng",
                    "Có thai - thận trọng, có thể gây dị tật",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nhạy cảm",
                ],
            },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hematologic": "High (aplastic anemia, agranulocytosis, thrombocytopenia)", "dermatologic": "High (Stevens-Johnson syndrome, toxic epidermal necrolysis)", "hepatic": "Moderate (hepatitis)", "metabolic": "Moderate (hyponatremia)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Carbamazepine blood level - CRITICAL (therapeutic range: 4-12 mcg/ml)",
                    "Complete blood count - CRITICAL (aplastic anemia, agranulocytosis, thrombocytopenia risk)",
                    "Signs of Stevens-Johnson syndrome/toxic epidermal necrolysis (severe rash) - CRITICAL",
                    "Hepatic function (ALT, AST) - CRITICAL",
                    "Serum sodium (hyponatremia risk)",
                    "Signs of toxicity (dizziness, ataxia, confusion, nausea)",
                    "Seizure frequency and severity",
                    "Drug interactions (strong CYP450 inducer) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Carbamazepine", "Tegretol", "Oxcarbazepine"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "ILAE Treatment Guidelines - Focal Seizures",
                "AAN Trigeminal Neuralgia Treatment Guidelines",
                "FDA Black Box Warning - Aplastic Anemia and Agranulocytosis",
                "FDA Black Box Warning - Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis",
                "FDA Black Box Warning - Suicidal Behavior and Ideation",
                "FDA Drug Label - Carbamazepine"
            ]
        },

        # ======================== SESSION 1: ANTICONVULSANTS & ANTIPARKINSONIAN ========================
        "Phenytoin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"dermatologic": "High (Stevens-Johnson syndrome, toxic epidermal necrolysis, DRESS)", "hepatic": "Moderate (hepatitis)", "hematologic": "Moderate (agranulocytosis, thrombocytopenia)", "neurologic": "Moderate (cerebellar atrophy with chronic use)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Phenytoin blood level - CRITICAL (therapeutic range: 10-20 mcg/ml)",
                    "Signs of Stevens-Johnson syndrome/toxic epidermal necrolysis (severe rash) - CRITICAL",
                    "Signs of DRESS (drug reaction with eosinophilia and systemic symptoms) - CRITICAL",
                    "Hepatic function (ALT, AST) - CRITICAL",
                    "Complete blood count (agranulocytosis, thrombocytopenia risk)",
                    "Signs of toxicity (nystagmus, ataxia, dysarthria, confusion)",
                    "Seizure frequency and severity",
                    "Drug interactions (strong CYP450 inducer/inhibitor) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Phenytoin", "Dilantin", "Fosphenytoin"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "ILAE Treatment Guidelines - Generalized Tonic-Clonic Seizures",
                "AAN Status Epilepticus Treatment Guidelines",
                "FDA Black Box Warning - Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis",
                "FDA Black Box Warning - Suicidal Behavior and Ideation",
                "FDA Drug Label - Phenytoin"
            ]
        },

        "Valproic acid": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "High (hepatotoxicity, especially in children <2 years)", "hematologic": "Moderate (thrombocytopenia, bleeding risk)", "pancreatic": "Moderate (pancreatitis)", "metabolic": "Moderate (hyperammonemia, especially with carnitine deficiency)", "teratogenic": "High (neural tube defects, craniofacial defects)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Valproic acid blood level - CRITICAL (therapeutic range: 50-100 mcg/ml)",
                    "Hepatic function (ALT, AST, bilirubin) - CRITICAL (especially in first 6 months)",
                    "Complete blood count (thrombocytopenia, bleeding risk)",
                    "Ammonia level (hyperammonemia risk, especially with carnitine deficiency)",
                    "Signs of pancreatitis (severe abdominal pain, nausea, vomiting) - CRITICAL",
                    "Signs of hepatotoxicity (jaundice, fatigue, nausea) - CRITICAL",
                    "Seizure frequency and severity",
                    "Pregnancy test (if woman of childbearing age) - CRITICAL (teratogenic)"
                ],
                "look_alike_sound_alike": ["Valproic acid", "Depakote", "Depakene", "Divalproex"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "ILAE Treatment Guidelines - Generalized Seizures",
                "AAN Bipolar Disorder Treatment Guidelines",
                "FDA Black Box Warning - Hepatotoxicity (especially in children <2 years)",
                "FDA Black Box Warning - Teratogenicity (neural tube defects)",
                "FDA Black Box Warning - Pancreatitis",
                "FDA Black Box Warning - Suicidal Behavior and Ideation",
                "FDA Drug Label - Valproic acid"
            ]
        },

        "Levetiracetam": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neuropsychiatric": "Moderate (agitation, aggression, depression, psychosis)", "hematologic": "Low (thrombocytopenia, leukopenia)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Seizure frequency and severity",
                    "Neuropsychiatric symptoms (agitation, aggression, depression, psychosis) - CRITICAL",
                    "Complete blood count (thrombocytopenia, leukopenia risk)",
                    "Renal function (CrCl) - adjust dose if CrCl <50"
                ],
                "look_alike_sound_alike": ["Levetiracetam", "Keppra", "Briviact"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "ILAE Treatment Guidelines - Focal and Generalized Seizures",
                "AAN Status Epilepticus Treatment Guidelines",
                "FDA Black Box Warning - Neuropsychiatric Adverse Reactions",
                "FDA Black Box Warning - Suicidal Behavior and Ideation",
                "FDA Drug Label - Levetiracetam"
            ]
        },

        "Lamotrigine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"dermatologic": "High (Stevens-Johnson syndrome, toxic epidermal necrolysis - especially with rapid titration or valproate co-administration)", "hematologic": "Low (blood dyscrasias)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of Stevens-Johnson syndrome/toxic epidermal necrolysis (severe rash) - CRITICAL (especially during first 8 weeks or with rapid titration)",
                    "Rash (any rash - may progress to SJS/TEN)",
                    "Seizure frequency and severity",
                    "Complete blood count (blood dyscrasias risk)",
                    "Drug interactions (valproate increases lamotrigine levels - requires slower titration)"
                ],
                "look_alike_sound_alike": ["Lamotrigine", "Lamictal", "Lamotrigine"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "ILAE Treatment Guidelines - Focal and Generalized Seizures",
                "AAN Bipolar Disorder Treatment Guidelines",
                "FDA Black Box Warning - Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis",
                "FDA Black Box Warning - Suicidal Behavior and Ideation",
                "FDA Drug Label - Lamotrigine (rash and SJS/TEN warnings)"
            ]
        },

        "Levodopa/Carbidopa": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neuropsychiatric": "High (hallucinations, psychosis, impulse control disorders)", "cardiovascular": "Moderate (orthostatic hypotension, arrhythmias)", "gastrointestinal": "Moderate (nausea, vomiting)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Parkinson's disease symptoms (motor fluctuations, dyskinesias)",
                    "Neuropsychiatric symptoms (hallucinations, psychosis, impulse control disorders) - CRITICAL",
                    "Blood pressure (orthostatic hypotension)",
                    "ECG (arrhythmias risk)",
                    "Gastrointestinal symptoms (nausea, vomiting)",
                    "Motor complications (wearing-off, on-off fluctuations, dyskinesias)"
                ],
                "look_alike_sound_alike": ["Levodopa/Carbidopa", "Sinemet", "Duopa", "Rytary"]
            },
            "guideline_tags": [
                "MDS Evidence-Based Medicine Review - Parkinson's Disease",
                "AAN Parkinson's Disease Treatment Guidelines",
                "NICE Parkinson's Disease Guidelines",
                "FDA Drug Label - Levodopa/Carbidopa (hallucinations and impulse control disorders warnings)"
            ]
        },

        "Clonazepam": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "High (respiratory depression, especially with opioids or alcohol)", "neurologic": "Moderate (dependence, withdrawal, falls, ataxia)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Seizure frequency and severity",
                    "Respiratory function (respiratory depression risk, especially with opioids/alcohol) - CRITICAL",
                    "Signs of dependence and withdrawal",
                    "Falls risk (especially in elderly)",
                    "Ataxia (loss of coordination)",
                    "Cognitive function (confusion, especially in elderly)",
                    "Drug interactions (CYP3A4 inhibitors/inducers, opioids, alcohol) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Clonazepam", "Klonopin", "Diazepam", "Lorazepam"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "ILAE Treatment Guidelines - Status Epilepticus",
                "AAN Panic Disorder Treatment Guidelines",
                "FDA Black Box Warning - Respiratory Depression (especially with opioids)",
                "FDA Black Box Warning - Abuse, Dependence, and Withdrawal",
                "FDA Drug Label - Clonazepam"
            ]
        },

        "Sumatriptan": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"cardiovascular": "High (coronary vasospasm, MI, stroke, arrhythmias - contraindicated in CAD)", "cerebrovascular": "High (stroke, TIA risk)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood pressure",
                    "Signs of coronary vasospasm (chest pain, tightness) - CRITICAL (may be benign but must rule out cardiac)",
                    "ECG (if cardiac risk factors present)",
                    "Signs of stroke (focal neurological deficits)",
                    "Drug interactions (MAO inhibitors, ergotamine, SSRI/SNRI - serotonin syndrome risk)"
                ],
                "look_alike_sound_alike": ["Sumatriptan", "Imitrex", "Imigran", "Rizatriptan", "Zolmitriptan"]
            },
            "guideline_tags": [
                "AHS Migraine Treatment Guidelines",
                "EFNS Migraine Treatment Guidelines",
                "FDA Drug Label - Sumatriptan (cardiovascular and cerebrovascular warnings)"
            ]
        },

        # ======================== SESSION 2: ADDITIONAL ANTICONVULSANTS, MUSCLE RELAXANTS, ALZHEIMER DRUGS ========================
        "Gabapentin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "High (respiratory depression, especially with opioids or benzodiazepines)", "neurologic": "Moderate (drowsiness, dizziness, ataxia, cognitive impairment)", "metabolic": "Moderate (peripheral edema, weight gain)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Seizure frequency and severity (if used for epilepsy)",
                    "Pain control (if used for neuropathic pain)",
                    "Respiratory function (respiratory depression risk, especially with opioids/benzodiazepines) - CRITICAL",
                    "Neurologic symptoms (drowsiness, dizziness, ataxia, cognitive impairment)",
                    "Peripheral edema (may be significant)",
                    "Weight (weight gain risk)",
                    "Renal function (CrCl, eGFR) - CRITICAL (adjust dose if CrCl <60)",
                    "Signs of dependence/abuse (rare but possible)"
                ],
                "look_alike_sound_alike": ["Gabapentin", "Neurontin", "Pregabalin", "Gralise"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "AAN Neuropathic Pain Treatment Guidelines",
                "ILAE Treatment Guidelines - Focal Seizures",
                "FDA Black Box Warning - Respiratory Depression (especially with opioids)",
                "FDA Drug Label - Gabapentin"
            ]
        },

        "Pregabalin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "High (respiratory depression, especially with opioids or benzodiazepines)", "neurologic": "Moderate (drowsiness, dizziness, ataxia, cognitive impairment)", "metabolic": "Moderate (peripheral edema, weight gain)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Seizure frequency and severity (if used for epilepsy)",
                    "Pain control (if used for neuropathic pain)",
                    "Respiratory function (respiratory depression risk, especially with opioids/benzodiazepines) - CRITICAL",
                    "Neurologic symptoms (drowsiness, dizziness, ataxia, cognitive impairment)",
                    "Peripheral edema (may be significant)",
                    "Weight (weight gain risk)",
                    "Renal function (CrCl, eGFR) - CRITICAL (adjust dose if CrCl <60)",
                    "Signs of dependence/abuse (rare but possible)"
                ],
                "look_alike_sound_alike": ["Pregabalin", "Lyrica", "Gabapentin"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "AAN Neuropathic Pain Treatment Guidelines",
                "ILAE Treatment Guidelines - Focal Seizures",
                "FDA Black Box Warning - Respiratory Depression (especially with opioids)",
                "FDA Black Box Warning - Abuse and Dependence",
                "FDA Drug Label - Pregabalin"
            ]
        },

        "Topiramate": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"ophthalmic": "High (acute angle-closure glaucoma, myopia, visual field defects)", "metabolic": "Moderate (metabolic acidosis, kidney stones)", "neurologic": "Moderate (cognitive impairment, word-finding difficulties)", "teratogenic": "High (cleft lip/palate, oral clefts)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Seizure frequency and severity",
                    "Visual function (acute angle-closure glaucoma, myopia, visual field defects) - CRITICAL",
                    "Serum bicarbonate (metabolic acidosis risk)",
                    "Kidney stones (nephrolithiasis risk)",
                    "Cognitive function (word-finding difficulties, memory problems)",
                    "Pregnancy test (if woman of childbearing age) - CRITICAL (teratogenic)",
                    "Weight (weight loss is common)"
                ],
                "look_alike_sound_alike": ["Topiramate", "Topamax", "Trokendi XR", "Qudexy XR"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "ILAE Treatment Guidelines - Focal and Generalized Seizures",
                "AAN Migraine Prevention Guidelines",
                "FDA Black Box Warning - Acute Angle-Closure Glaucoma",
                "FDA Black Box Warning - Teratogenicity (Cleft Lip/Palate)",
                "FDA Black Box Warning - Suicidal Behavior and Ideation",
                "FDA Drug Label - Topiramate"
            ]
        },

        "Oxcarbazepine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"dermatologic": "Moderate (Stevens-Johnson syndrome, toxic epidermal necrolysis - lower risk than carbamazepine)", "metabolic": "Moderate (hyponatremia)", "hematologic": "Low (agranulocytosis, aplastic anemia - rare)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Seizure frequency and severity",
                    "Signs of Stevens-Johnson syndrome/toxic epidermal necrolysis (severe rash) - CRITICAL",
                    "Serum sodium (hyponatremia risk)",
                    "Complete blood count (agranulocytosis, aplastic anemia risk - rare)",
                    "Signs of toxicity (dizziness, ataxia, confusion, nausea)"
                ],
                "look_alike_sound_alike": ["Oxcarbazepine", "Trileptal", "Carbamazepine"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "ILAE Treatment Guidelines - Focal Seizures",
                "FDA Black Box Warning - Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis",
                "FDA Black Box Warning - Suicidal Behavior and Ideation",
                "FDA Drug Label - Oxcarbazepine"
            ]
        },

        "Baclofen": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "High (respiratory depression, especially with opioids or alcohol, or intrathecal use)", "neurologic": "Moderate (drowsiness, dizziness, weakness, confusion, withdrawal seizures if stopped abruptly)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Spasticity response",
                    "Respiratory function (respiratory depression risk, especially with opioids/alcohol or intrathecal) - CRITICAL",
                    "Muscle weakness (may affect ambulation)",
                    "Blood pressure (hypotension risk)",
                    "Cognitive function (confusion, especially in elderly)",
                    "Renal function (CrCl) - adjust dose if CrCl <30",
                    "Signs of withdrawal (seizures, hallucinations, anxiety, insomnia) if stopped abruptly - CRITICAL"
                ],
                "look_alike_sound_alike": ["Baclofen", "Lioresal", "Gablofen"]
            },
            "guideline_tags": [
                "AAN Spasticity Treatment Guidelines",
                "AAN Multiple Sclerosis Treatment Guidelines",
                "FDA Black Box Warning - Respiratory Depression (especially with opioids)",
                "FDA Black Box Warning - Withdrawal Seizures (if stopped abruptly)",
                "FDA Drug Label - Baclofen"
            ]
        },

        "Donepezil": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"gastrointestinal": "High (nausea, vomiting, diarrhea - very common)", "cardiovascular": "Moderate (bradycardia, syncope, especially in patients with cardiac conduction abnormalities)", "neurologic": "Moderate (insomnia, nightmares, muscle cramps)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Cognitive function (Alzheimer's disease progression)",
                    "Gastrointestinal symptoms (nausea, vomiting, diarrhea) - very common, usually improves over time",
                    "Heart rate and ECG (bradycardia risk, especially in patients with cardiac conduction abnormalities) - CRITICAL",
                    "Blood pressure (syncope risk)",
                    "Sleep patterns (insomnia, nightmares)",
                    "Muscle cramps"
                ],
                "look_alike_sound_alike": ["Donepezil", "Aricept", "Adlarity"]
            },
            "guideline_tags": [
                "AAN Dementia Treatment Guidelines",
                "AAIC Alzheimer's Disease Treatment Guidelines",
                "NICE Dementia Treatment Guidelines",
                "FDA Drug Label - Donepezil (bradycardia and syncope warnings)"
            ]
        },

        "Memantine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"neurologic": "Moderate (dizziness, confusion, headache)", "gastrointestinal": "Low (constipation, diarrhea)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Cognitive function (Alzheimer's disease progression)",
                    "Neurologic symptoms (dizziness, confusion, headache)",
                    "Renal function (CrCl) - adjust dose if CrCl <30",
                    "Gastrointestinal symptoms (constipation, diarrhea)"
                ],
                "look_alike_sound_alike": ["Memantine", "Namenda", "Namenda XR"]
            },
            "guideline_tags": [
                "AAN Dementia Treatment Guidelines",
                "AAIC Alzheimer's Disease Treatment Guidelines",
                "NICE Dementia Treatment Guidelines",
                "FDA Drug Label - Memantine"
            ]
        },

        "Ethosuximide": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hematologic": "High (bone marrow suppression, aplastic anemia - rare but serious)", "dermatologic": "Moderate (Stevens-Johnson syndrome, toxic epidermal necrolysis)", "hepatic": "Low (hepatitis - rare)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Ethosuximide blood level - CRITICAL (therapeutic range: 40-100 mcg/ml)",
                    "Complete blood count - CRITICAL (bone marrow suppression, aplastic anemia risk)",
                    "Signs of Stevens-Johnson syndrome/toxic epidermal necrolysis (severe rash) - CRITICAL",
                    "Hepatic function (ALT, AST) - hepatitis risk (rare)",
                    "Absence seizure frequency and severity",
                    "Signs of toxicity (nausea, vomiting, dizziness, drowsiness)"
                ],
                "look_alike_sound_alike": ["Ethosuximide", "Zarontin"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "ILAE Treatment Guidelines - Absence Seizures",
                "FDA Black Box Warning - Bone Marrow Suppression (Aplastic Anemia)",
                "FDA Black Box Warning - Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis",
                "FDA Drug Label - Ethosuximide"
            ]
        },

        "Fosphenytoin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"dermatologic": "High (Stevens-Johnson syndrome, toxic epidermal necrolysis, DRESS)", "hepatic": "Moderate (hepatitis)", "hematologic": "Moderate (agranulocytosis, thrombocytopenia)", "cardiovascular": "Moderate (hypotension, arrhythmias - less than phenytoin IV)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Phenytoin blood level (after conversion from fosphenytoin) - CRITICAL (therapeutic range: 10-20 mcg/ml)",
                    "Signs of Stevens-Johnson syndrome/toxic epidermal necrolysis (severe rash) - CRITICAL",
                    "Signs of DRESS (drug reaction with eosinophilia and systemic symptoms) - CRITICAL",
                    "Hepatic function (ALT, AST) - CRITICAL",
                    "Complete blood count (agranulocytosis, thrombocytopenia risk)",
                    "Blood pressure and ECG (hypotension, arrhythmias risk - less than phenytoin IV)",
                    "Signs of toxicity (nystagmus, ataxia, dysarthria, confusion)",
                    "Seizure frequency and severity",
                    "Infusion site (pruritus, burning sensation - especially in groin area due to phosphate)"
                ],
                "look_alike_sound_alike": ["Fosphenytoin", "Cerebyx", "Phenytoin"]
            },
            "guideline_tags": [
                "AAN Epilepsy Treatment Guidelines",
                "AAN Status Epilepticus Treatment Guidelines",
                "ILAE Treatment Guidelines - Status Epilepticus",
                "FDA Black Box Warning - Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis",
                "FDA Black Box Warning - Suicidal Behavior and Ideation",
                "FDA Drug Label - Fosphenytoin"
            ]
        },

}

__all__ = ["NEUROLOGICAL_ENHANCED_FIELDS"]
