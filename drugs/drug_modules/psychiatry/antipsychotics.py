"""
Antipsychotic Drugs
"""

ANTIPSYCHOTICS_DRUGS = {
    "Haloperidol":     {
        "group": "Psychiatry - Antipsychotic (Typical/First Generation)",
        "vietnamese_name": "Haloperidol, Haldol",
        "brand_names": {
            "common": [
                "Haldol"
    ],
            "vietnam": [
                "Haloperidol",
                "Halofar"
    ],
        },
        "administration": [
            "PO",
            "IM",
            "IV (off-label)"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Trạng thái loạn thần cấp",
            "Kích động tâm thần vận động (cấp cứu)",
            "Hội chứng Tourette",
            "Nấc cụt khó trị (off-label)"
    ],
        "contraindications": {
            "absolute": [
                "Hôn mê",
                "Quá mẫn với haloperidol",
                "Ức chế thần kinh trung ương nặng",
                "Bệnh Parkinson"
    ],
            "relative": [
                "Kéo dài khoảng QT (nguy cơ Torsades de Pointes)",
                "Sa sút trí tuệ (tăng nguy cơ tử vong ở người già)",
                "Tiền sử hội chứng ác tính do thuốc an thần (NMS)"
    ],
        },
        "dosage": {
            "adult_psychosis_oral": "0.5-5 mg/lần x 2-3 lần/ngày. Tối đa 100 mg/ngày (hiếm khi cần >30 mg).",
            "adult_agitation_im": "2-5 mg IM. Có thể lặp lại mỗi 4-8 giờ. (Phối hợp Lorazepam thường dùng).",
            "adult_delirium_iv_offlabel": "0.5-2 mg IV chậm mỗi 2-4 giờ? Thận trọng QT.",
            "notes": "Liều người già: 0.5-2 mg/ngày. Dùng liều thấp nhất có hiệu quả.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "adjustment": "Thận trọng, bắt đầu liều thấp. Không có hướng dẫn chỉnh liều cụ thể theo CrCl.",
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "Thận trọng. Haloperidol chuyển hóa qua gan. Giảm liều ở suy gan nặng.",
        },
        "side_effects": [
            "Hội chứng ngoại tháp (EPS) - Rất thường gặp (cứng cơ, run, loạn trương lực)",
            "Loạn vận động muộn (Tardive Dyskinesia)",
            "Hội chứng ác tính do thuốc an thần (NMS) - Hiếm nhưng tử vong cao",
            "Kéo dài khoảng QT - Nguy cơ xoắn đỉnh",
            "Buồn ngủ, hạ huyết áp tư thế"
    ],
        "interactions": [
            "Thuốc kéo dài QT (Amiodarone, Macrolides, Ondansetron) -> Tăng nguy cơ loạn nhịp.",
            "Levodopa/Dopamine agonists -> Mất tác dụng điều trị Parkinson.",
            "Thuốc ức chế TKTW khác (Rượu, Benzodiazepines) -> Tăng ức chế hô hấp/thần kinh."
    ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Sử dụng khi lợi ích > nguy cơ. Có nguy cơ triệu chứng ngoại tháp ở trẻ sơ sinh nếu dùng 3 tháng cuối.""",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể ảnh hưởng phát triển thần kinh trẻ.",
                "recommendation": "",
            },
        },
        "pharmacokinetics": {
            "half_life": "14-26 giờ (PO)",
            "onset": "30-60 phút (IM), 1-3 giờ (PO)",
            "metabolism": "Gan (CYP3A4, CYP2D6)",
        },
        "monitoring": [
            "ECG (Khoảng QT) trước và trong khi điều trị (đặc biệt IV)",
            "Dấu hiệu ngoại tháp (EPS)",
            "Dấu hiệu sốt/cứng cơ (NMS)",
            "Công thức máu (hiếm gặp giảm bạch cầu)"
    ],
        "black_box_warnings": """Người cao tuổi mắc chứng sa sút trí tuệ (Dementia) dùng thuốc chống loạn thần có TĂNG nguy cơ tử vong.""",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "neurological"],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "EPS signs", "NMS signs"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "ISMP High Alert Medications",
            "APA Guidelines - Schizophrenia Treatment",
            "WHO Essential Medicines List"
        ],
    },
    "Risperidone":     {
        "group": "Psychiatry - Antipsychotic (Atypical/Second Generation)",
        "vietnamese_name": "Risperidone, Risperdal",
        "brand_names": {
            "common": [
                "Risperdal"
    ],
            "vietnam": [
                "Risperidone",
                "Rileptid",
                "Residon"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (Cơn mania)",
            "Rối loạn hành vi ở trẻ tự kỷ (kích động)"
    ],
        "contraindications": {
            "absolute": [
                "Quá mẫn với risperidone"
    ],
            "relative": [
                "Hội chứng QT kéo dài",
                "Sa sút trí tuệ (Black Box)"
    ],
        },
        "dosage": {
            "adult_schizophrenia": "Khởi đầu 2 mg/ngày -> tăng lên 4-6 mg/ngày. Uống 1-2 lần/ngày. Max 16 mg.",
            "adult_bipolar": "2-3 mg/ngày. Chỉnh liều sau 24h. Dải liều 1-6 mg.",
            "elderly": "Khởi đầu 0.5 mg x 2 lần/ngày. Tăng chậm.",
        },
        "renal_adjustment": {
            "crcl_30": "Liều khởi đầu 0.5 mg x 2 lần/ngày. Tăng liều cần chậm.",
            "severe": "Như trên. Thận trọng.",
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "Khởi đầu 0.5 mg x 2 lần/ngày. Chuẩn độ chậm.",
        },
        "side_effects": [
            "EPS (ít hơn Haloperidol nhưng nhiều nhất trong nhóm Atypical)",
            "Tăng Prolactin máu (Vú to nam giới, tiết sữa, rối loạn kinh nguyệt)",
            "Tăng cân, Rối loạn chuyển hóa (Đường, Mỡ)",
            "Hạ huyết áp tư thế"
    ],
        "interactions": [
            "Clopidogrel/SSRI (Fluoxetine, Paroxetine): Ức chế CYP2D6 làm tăng nồng độ Risperidone.",
            "Levodopa: Đối kháng tác dụng."
    ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Nguy cơ EPS ở trẻ sơ sinh.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa. Cân nhắc lợi ích/nguy cơ.",
                "recommendation": "",
            },
        },
        "pharmacokinetics": {
            "half_life": "20 giờ (Risperidone + chất chuyển hóa hoạt tính)",
            "metabolism": "Gan (CYP2D6)",
        },
        "monitoring": [
            "Cân nặng, Vòng eo, Glucose, Lipid (nguy cơ hội chứng chuyển hóa)",
            "Prolactin (nếu có triệu chứng lâm sàng)",
            "Huyết áp tư thế"
    ],
        "black_box_warnings": "Tăng nguy cơ tử vong ở người cao tuổi sa sút trí tuệ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["metabolic", "endocrine"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Weight", "Glucose", "Lipid", "Prolactin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "APA Guidelines - Schizophrenia Treatment",
            "APA Guidelines - Bipolar Disorder"
        ],
    },
    "Olanzapine":     {
        "group": "Psychiatry - Antipsychotic (Atypical)",
        "vietnamese_name": "Olanzapine, Zyprexa",
        "brand_names": {
            "common": [
                "Zyprexa"
    ],
            "vietnam": [
                "Olanzapine",
                "Olanxol",
                "SaVi Olanzapine"
    ],
        },
        "administration": [
            "PO",
            "IM (Cấp cứu)"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (Cơn mania/Hỗn hợp)",
            "Trầm cảm kháng trị (phối hợp Fluoxetine)"
    ],
        "dosage": {
            "adult_oral": "5-10 mg/ngày. Tăng 5mg mỗi tuần. Liều đích 10-20 mg/ngày.",
            "acute_agitation_im": "10 mg IM (Adult), 2.5-5 mg (Elderly). Tối đa 3 liều/24h.",
            "notes": "Uống buổi tối do gây buồn ngủ mạnh.",
        },
        "renal_adjustment": {
            "normal": "Không đổi. Khởi đầu liều thấp 5mg nếu suy thận nặng.",
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "E.g. Khởi đầu 5mg. Thận trọng.",
        },
        "side_effects": [
            "Tăng cân NHIỀU NHẤT, Rối loạn chuyển hóa (Tiểu đường, Tăng mỡ máu)",
            "Buồn ngủ (Sedation)",
            "Táo bón, khô miệng (Anticholinergic)",
            "EPS (ít gặp)"
    ],
        "interactions": [
            "Benzodiazepines (khi tiềm IM): Nguy cơ ức chế hô hấp/tử vong -> Không nên tiêm cùng lúc (cách nhau >1h).",
            "Thuốc lá: Hút thuốc làm giảm nồng độ Olanzapine (CYP1A2 induction)."
    ],
        "monitoring": [
            "BMI, Gluose, Hba1c, Lipid profile (Bắt buộc theo dõi sát)",
            "Huyết áp"
    ],
        "black_box_warnings": """Tử vong người già sa sút trí tuệ. Hội chứng sau tiêm (Delirium/Sedation syndrome) với dạng tiêm tác dụng kéo dài.""",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["metabolic", "cardiovascular"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["BMI", "Glucose", "HbA1c", "Lipid", "Blood pressure"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "FDA Black Box Warning - Post-Injection Delirium/Sedation Syndrome",
            "APA Guidelines - Schizophrenia Treatment",
            "APA Guidelines - Bipolar Disorder"
        ],
    },
    "Quetiapine":     {
        "group": "Psychiatry - Antipsychotic (Atypical)",
        "vietnamese_name": "Quetiapine, Seroquel",
        "administration": [
            "PO"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực",
            "Hỗ trợ điều trị trầm cảm lớn"
    ],
        "dosage": {
            "schizophrenia": "Liều tăng dần. Đích 400-800 mg/ngày (chia 2 lần hoặc XR 1 lần).",
            "bipolar_depression": "300 mg/ngày (buổi tối).",
            "notes": "Phải chỉnh liều từ từ (25 -> 50 -> 100...) để tránh tụt HA và an thần quá mức.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "Khởi đầu 25mg/ngày. Tăng 25-50mg/ngày.",
        },
        "side_effects": [
            "Buồn ngủ (Rất thường gặp)",
            "Tăng cân, Rối loạn chuyển hóa",
            "Hạ huyết áp tư thế",
            "QT kéo dài (nhẹ)"
    ],
        "interactions": [
            "CYP3A4 Inhibitors (Ketoconazole, Erythromycin) -> Tăng nồng độ Quetiapine -> Giảm liều.",
            "CYP3A4 Inducers (Phenytoin, Carbamazepine) -> Giảm nồng độ -> Tăng liều."
    ],
        "monitoring": [
            "Tuyến giáp (có thể gây giảm hormone tuyến giáp)",
            "Glucose, Lipid, BMI",
            "Khám mắt (đục thủy tinh thể - hiếm)"
    ],
        "black_box_warnings": """Tăng ý nghĩ tự sát ở trẻ em/thanh thiếu niên (khi dùng trị trầm cảm). Tử vong người già sa sút trí tuệ.""",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["metabolic", "endocrine"],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Thyroid function", "Glucose", "Lipid", "BMI", "Eye exam"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Suicidal Behavior in Children/Adolescents",
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "APA Guidelines - Schizophrenia Treatment",
            "APA Guidelines - Bipolar Disorder"
        ],
    },
    "Aripiprazole": {
        "group": "Psychiatry - Antipsychotic (Atypical/Third Gen)",
        "vietnamese_name": "Aripiprazole, Abilify",
        "administration": ["PO"],
        "indications": [
             "Tâm thần phân liệt",
             "Rối loạn lưỡng cực (Mania)",
             "Hỗ trợ trầm cảm"
        ],
        "dosage": {
             "adult": "10-15 mg/ngày. Max 30 mg. Uống sáng (do có thể gây mất ngủ)."
        },
        "renal_adjustment": {
             "normal": "Không đổi"
        },
        "side_effects": [
             "Bồn chồn (Akathisia) - Rất đặc trưng",
             "Ít gây tăng cân và rối loạn chuyển hóa nhất",
             "Ít gây an thần"
        ],
        "interactions": [
             "CYP3A4/2D6 Inhibitors -> Giảm 50% liều.",
        ],
        "monitoring": [
             "Dấu hiệu Akathisia (bệnh nhân báo cáo cảm giác không thể ngồi yên)"
        ],
        "black_box_warnings": "Tự sát & Tử vong người già sa sút trí tuệ.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["neurological"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Akathisia signs"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Suicidal Behavior",
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "APA Guidelines - Schizophrenia Treatment",
            "APA Guidelines - Bipolar Disorder"
        ],
    },

    "Clozapine": {
         "group": "Psychiatry - Antipsychotic (Atypical) - LAST LINE",
         "vietnamese_name": "Clozapine, Leponex",
         "administration": ["PO"],
         "indications": ["Tâm thần phân liệt KHÁNG TRỊ", "Giảm nguy cơ tự sát"],
         "contraindications": {
             "absolute": ["Tiền sử giảm bạch cầu hạt do Clozapine", "Động kinh không kiểm soát"]
         },
         "dosage": {
             "adult": "Khởi đầu 12.5 mg x 1-2 lần. Tăng rất chậm. Đích 300-450 mg/ngày."
         },
         "side_effects": [
             "GIẢM BẠCH CẦU HẠT (Agranulocytosis) - Nguy hiểm chết người (1-2%)",
             "Viêm cơ tim",
             "Co giật (phụ thuộc liều)",
             "Tiết nhiều nước bọt (Sialorrhea)",
             "Táo bón nặng (Giảm nhu động ruột)"
         ],
         "monitoring": [
             "Công thức máu (WBC/ANC): Hàng tuần trong 6 tháng đầu, sau đó 2 tuần/lần -> 4 tuần/lần. BẮT BUỘC.",
             "Troponin/CRP (nguy cơ viêm cơ tim)"
         ],
         "black_box_warnings": "Agranulocytosis nghiêm trọng; Co giật; Viêm cơ tim; Tử vong người già.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hematologic", "cardiac", "neurological"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (WBC/ANC) - weekly for 6 months", "Troponin/CRP", "Seizure monitoring"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Agranulocytosis",
            "FDA Black Box Warning - Seizures",
            "FDA Black Box Warning - Myocarditis",
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "APA Guidelines - Treatment-Resistant Schizophrenia"
        ],
    },
    "Brexpiprazole":     {
        "group": "Psychiatry - Antipsychotic (Atypical/Third Generation)",
        "vietnamese_name": "Brexpiprazole, Rexulti",
        "brand_names": {
            "common": [
                "Rexulti"
    ],
            "vietnam": [
                "Brexpiprazole",
                "Rexulti"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn trầm cảm nặng (MDD) - điều trị phụ trợ",
            "Kích động liên quan đến chứng mất trí nhớ (off-label)"
    ],
        "contraindications": {
            "absolute": [
                "Dị ứng brexpiprazole",
                "Trẻ em <13 tuổi"
    ],
            "relative": [
                "Sa sút trí tuệ (tăng nguy cơ tử vong ở người già)",
                "Kéo dài khoảng QT",
                "Tiền sử hội chứng ác tính do thuốc an thần (NMS)"
    ],
        },
        "dosage": {
            "adult_schizophrenia": "Khởi đầu 1mg x 1 lần/ngày. Tăng dần đến 2-4mg/ngày. Tối đa 4mg/ngày.",
            "adult_mdd_adjunct": "Khởi đầu 0.5-1mg x 1 lần/ngày. Tăng dần đến 2-3mg/ngày. Tối đa 3mg/ngày.",
            "notes": "Brexpiprazole là partial agonist tại D2 và 5-HT1A receptors, và antagonist tại 5-HT2A receptors. Tương tự aripiprazole nhưng có tỷ lệ 5-HT1A/D2 cao hơn, ít tác dụng phụ akathisia hơn.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "adjustment": "Không cần chỉnh liều ở suy thận nhẹ đến trung bình. Thận trọng ở suy thận nặng.",
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 50%",
            "severe": "Giảm liều 75%",
            "notes": "Brexpiprazole chuyển hóa qua gan (CYP3A4, CYP2D6). Giảm liều ở suy gan.",
        },
        "side_effects": [
            "Tăng cân (ít hơn olanzapine)",
            "Akathisia (ít hơn aripiprazole)",
            "Buồn ngủ",
            "Rối loạn vận động ngoại tháp (EPS) - ít hơn typical antipsychotics",
            "Kéo dài khoảng QT - ít hơn một số antipsychotics khác",
            "Tăng đường huyết, rối loạn lipid máu (ít hơn olanzapine)"
    ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ brexpiprazole, giảm liều 50%",
            "Thuốc ức chế CYP2D6 (Fluoxetine, Paroxetine) -> Tăng nồng độ brexpiprazole, giảm liều 50%",
            "Thuốc cảm ứng CYP3A4 (Carbamazepine, Rifampin) -> Giảm nồng độ brexpiprazole, tăng liều",
            "Thuốc kéo dài QT -> Tăng nguy cơ loạn nhịp"
    ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Sử dụng khi lợi ích > nguy cơ. Có nguy cơ triệu chứng ngoại tháp ở trẻ sơ sinh nếu dùng 3 tháng cuối.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể ảnh hưởng phát triển thần kinh trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "pharmacokinetics": {
            "half_life": "91 giờ (rất dài)",
            "onset": "1-2 tuần",
            "metabolism": "Gan (CYP3A4, CYP2D6)",
        },
        "monitoring": [
            "Cân nặng, BMI",
            "Đường huyết, lipid máu",
            "ECG (Khoảng QT) nếu có nguy cơ",
            "Dấu hiệu akathisia",
            "Dấu hiệu ngoại tháp (EPS)"
    ],
        "black_box_warnings": """Người cao tuổi mắc chứng sa sút trí tuệ (Dementia) dùng thuốc chống loạn thần có TĂNG nguy cơ tử vong. Tăng nguy cơ tự sát ở trẻ em, thanh thiếu niên và thanh niên.""",
        "mechanism_of_action": """Brexpiprazole là partial agonist tại dopamine D2 receptors và serotonin 5-HT1A receptors, và antagonist tại 5-HT2A receptors. Cơ chế tương tự aripiprazole nhưng có tỷ lệ 5-HT1A/D2 cao hơn, dẫn đến ít tác dụng phụ akathisia hơn. Brexpiprazole có ái lực cao với 5-HT1A và 5-HT2A receptors. Tác dụng điều chỉnh dopamine và serotonin, giảm triệu chứng dương tính và cải thiện triệu chứng âm tính của tâm thần phân liệt, đồng thời có tác dụng chống trầm cảm khi dùng phụ trợ với antidepressants.""",
        "precautions": [
            "Tăng cân - theo dõi cân nặng, BMI",
            "Akathisia - ít hơn aripiprazole nhưng vẫn có thể xảy ra",
            "Tăng đường huyết, rối loạn lipid máu - theo dõi định kỳ",
            "Kéo dài khoảng QT - thận trọng ở bệnh nhân có nguy cơ",
            "Sa sút trí tuệ - tăng nguy cơ tử vong",
            "Tăng nguy cơ tự sát ở trẻ em, thanh thiếu niên"
    ],
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa brexpiprazole",
                    "effect": "Tăng nồng độ brexpiprazole, tăng tác dụng phụ",
                    "management": "Giảm liều brexpiprazole 50%.",
                },
    {
                    "drug": "Thuốc ức chế CYP2D6 mạnh (Fluoxetine, Paroxetine, Bupropion)",
                    "mechanism": "Ức chế chuyển hóa brexpiprazole",
                    "effect": "Tăng nồng độ brexpiprazole, tăng tác dụng phụ",
                    "management": "Giảm liều brexpiprazole 50%.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc cảm ứng CYP3A4 (Carbamazepine, Rifampin, St. John's Wort)",
                    "mechanism": "Tăng chuyển hóa brexpiprazole",
                    "effect": "Giảm nồng độ brexpiprazole, giảm hiệu quả",
                    "management": "Tăng liều brexpiprazole nếu cần.",
                }
                ],
            "minor": [],
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ",
                "Kích động",
                "Rối loạn vận động ngoại tháp",
                "Hạ huyết áp",
                "Tăng nhịp tim"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hỗ trợ",
                "Theo dõi huyết áp, nhịp tim",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi ý thức, huyết áp, nhịp tim, ECG",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "1 lần/ngày, cùng thời điểm mỗi ngày",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Rexulti (Brexpiprazole)",
                "UpToDate - Brexpiprazole: Drug information",
                "APA Guidelines - Schizophrenia Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["metabolic", "cardiac"],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Weight", "Glucose", "Lipids", "ECG", "Akathisia signs"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "FDA Black Box Warning - Suicidal Behavior",
            "APA Guidelines - Schizophrenia Treatment",
            "APA Guidelines - Major Depressive Disorder"
        ],
        "pediatric_dosing": {
            "adolescents_13_17": "Khởi đầu 0.5mg x 1 lần/ngày. Tăng dần đến 2-4mg/ngày. Tối đa 4mg/ngày (tâm thần phân liệt). MDD: Khởi đầu 0.5mg x 1 lần/ngày, tăng dần đến 2mg/ngày.",
            "children_under_13": "CHỐNG CHỈ ĐỊNH ở trẻ em <13 tuổi. Chưa được nghiên cứu về an toàn và hiệu quả.",
            "notes": "FDA-approved cho trẻ em ≥13 tuổi với tâm thần phân liệt. Theo dõi chặt chẽ dấu hiệu tự sát, tăng cân, akathisia ở trẻ em và thanh thiếu niên."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ. Tăng nguy cơ tử vong ở bệnh nhân cao tuổi mắc chứng sa sút trí tuệ (dementia). Thận trọng với tác dụng phụ chuyển hóa và tim mạch.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (0.5-1mg/ngày). Tăng dần từ từ. Điều chỉnh liều theo chức năng gan (giảm 50% ở suy gan trung bình, 75% ở suy gan nặng).",
            "monitoring": "Theo dõi chặt chẽ: Cân nặng, BMI, đường huyết, lipid máu, ECG (QT interval), dấu hiệu akathisia, dấu hiệu ngoại tháp (EPS), dấu hiệu tự sát. Tăng nguy cơ tử vong ở bệnh nhân cao tuổi mắc chứng sa sút trí tuệ."
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "150,000 - 300,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Brexpiprazole là thuốc mới, giá cao. Rexulti (brand) thường đắt (200,000-300,000 VND/viên 2-4mg). Generic có thể rẻ hơn (150,000-200,000 VND/viên). Chi phí ước tính: ~$1,160/tháng (quốc tế), tương đương khoảng 27,000,000-30,000,000 VND/tháng tại Việt Nam."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng trực tiếp và độ ẩm. Giữ trong bao bì gốc, đậy kín. Không bảo quản trong phòng tắm hoặc nơi ẩm ướt. Để xa tầm tay trẻ em và thú cưng."
    },
    "Cariprazine":     {
        "group": "Psychiatry - Antipsychotic (Atypical/Third Generation)",
        "vietnamese_name": "Cariprazine, Vraylar",
        "brand_names": {
            "common": [
                "Vraylar"
    ],
            "vietnam": [
                "Cariprazine",
                "Vraylar"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực I (manic, mixed, depressive episodes)",
            "Rối loạn trầm cảm nặng (MDD) - điều trị phụ trợ (off-label)"
    ],
        "contraindications": {
            "absolute": [
                "Dị ứng cariprazine",
                "Trẻ em <18 tuổi (chưa được phê duyệt)"
    ],
            "relative": [
                "Sa sút trí tuệ (tăng nguy cơ tử vong ở người già)",
                "Kéo dài khoảng QT",
                "Tiền sử hội chứng ác tính do thuốc an thần (NMS)"
    ],
        },
        "dosage": {
            "adult_schizophrenia": "Khởi đầu 1.5mg x 1 lần/ngày. Tăng dần đến 3-6mg/ngày. Tối đa 6mg/ngày.",
            "adult_bipolar_manic": "Khởi đầu 1.5mg x 1 lần/ngày. Tăng dần đến 3-6mg/ngày. Tối đa 6mg/ngày.",
            "adult_bipolar_depressive": "Khởi đầu 1.5mg x 1 lần/ngày. Tăng dần đến 1.5-3mg/ngày. Tối đa 3mg/ngày.",
            "notes": "Cariprazine là partial agonist tại D2 và D3 receptors, và antagonist tại 5-HT2A receptors. Có ái lực cao với D3 receptors. T1/2 rất dài (2-3 ngày) do active metabolites.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "adjustment": "Không cần chỉnh liều ở suy thận nhẹ đến trung bình. Thận trọng ở suy thận nặng.",
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 50%",
            "severe": "Giảm liều 75%",
            "notes": "Cariprazine chuyển hóa qua gan (CYP3A4). Giảm liều ở suy gan.",
        },
        "side_effects": [
            "Akathisia (phổ biến, đặc biệt ở liều cao)",
            "Tăng cân (ít hơn olanzapine)",
            "Buồn ngủ",
            "Rối loạn vận động ngoại tháp (EPS) - ít hơn typical antipsychotics",
            "Kéo dài khoảng QT - ít hơn một số antipsychotics khác",
            "Tăng đường huyết, rối loạn lipid máu (ít hơn olanzapine)",
            "Rối loạn giấc ngủ"
    ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ cariprazine, giảm liều 50%",
            "Thuốc cảm ứng CYP3A4 (Carbamazepine, Rifampin) -> Giảm nồng độ cariprazine, tăng liều",
            "Thuốc kéo dài QT -> Tăng nguy cơ loạn nhịp"
    ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Sử dụng khi lợi ích > nguy cơ. Có nguy cơ triệu chứng ngoại tháp ở trẻ sơ sinh nếu dùng 3 tháng cuối.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể ảnh hưởng phát triển thần kinh trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "pharmacokinetics": {
            "half_life": "2-3 ngày (rất dài, do active metabolites)",
            "onset": "1-2 tuần",
            "metabolism": "Gan (CYP3A4)",
        },
        "monitoring": [
            "Cân nặng, BMI",
            "Đường huyết, lipid máu",
            "ECG (Khoảng QT) nếu có nguy cơ",
            "Dấu hiệu akathisia (QUAN TRỌNG - phổ biến)",
            "Dấu hiệu ngoại tháp (EPS)"
    ],
        "black_box_warnings": """Người cao tuổi mắc chứng sa sút trí tuệ (Dementia) dùng thuốc chống loạn thần có TĂNG nguy cơ tử vong. Tăng nguy cơ tự sát ở trẻ em, thanh thiếu niên và thanh niên.""",
        "mechanism_of_action": """Cariprazine là partial agonist tại dopamine D2 và D3 receptors, và antagonist tại 5-HT2A receptors. Cariprazine có ái lực cao với D3 receptors (cao hơn D2), có thể có lợi ích trong điều trị triệu chứng âm tính và nhận thức của tâm thần phân liệt. Tác dụng điều chỉnh dopamine và serotonin, giảm triệu chứng dương tính và cải thiện triệu chứng âm tính của tâm thần phân liệt, đồng thời có tác dụng điều trị rối loạn lưỡng cực. T1/2 rất dài (2-3 ngày) do active metabolites (desmethyl-cariprazine, didesmethyl-cariprazine).""",
        "precautions": [
            "Akathisia - PHỔ BIẾN, đặc biệt ở liều cao, cần theo dõi chặt chẽ",
            "Tăng cân - theo dõi cân nặng, BMI",
            "Tăng đường huyết, rối loạn lipid máu - theo dõi định kỳ",
            "Kéo dài khoảng QT - thận trọng ở bệnh nhân có nguy cơ",
            "Sa sút trí tuệ - tăng nguy cơ tử vong",
            "T1/2 rất dài - cần thời gian để đạt nồng độ ổn định và để thuốc thải trừ hoàn toàn",
            "Tăng nguy cơ tự sát ở trẻ em, thanh thiếu niên"
    ],
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa cariprazine",
                    "effect": "Tăng nồng độ cariprazine, tăng tác dụng phụ",
                    "management": "Giảm liều cariprazine 50%.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc cảm ứng CYP3A4 (Carbamazepine, Rifampin, St. John's Wort)",
                    "mechanism": "Tăng chuyển hóa cariprazine",
                    "effect": "Giảm nồng độ cariprazine, giảm hiệu quả",
                    "management": "Tăng liều cariprazine nếu cần.",
                }
                ],
            "minor": [],
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ",
                "Kích động",
                "Akathisia",
                "Rối loạn vận động ngoại tháp",
                "Hạ huyết áp",
                "Tăng nhịp tim"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hỗ trợ",
                "Theo dõi huyết áp, nhịp tim",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi ý thức, huyết áp, nhịp tim, ECG",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "1 lần/ngày, cùng thời điểm mỗi ngày",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vraylar (Cariprazine)",
                "UpToDate - Cariprazine: Drug information",
                "APA Guidelines - Schizophrenia Treatment",
                "APA Guidelines - Bipolar Disorder"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["metabolic", "cardiac"],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Weight", "Glucose", "Lipids", "ECG", "Akathisia signs"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "FDA Black Box Warning - Suicidal Behavior",
            "APA Guidelines - Schizophrenia Treatment",
            "APA Guidelines - Bipolar Disorder"
        ],
        "pediatric_dosing": {
            "adolescents_18plus": "CHỐNG CHỈ ĐỊNH ở trẻ em <18 tuổi. Chưa được FDA phê duyệt cho trẻ em. Chỉ dùng cho người lớn ≥18 tuổi.",
            "children_under_18": "CHỐNG CHỈ ĐỊNH ở trẻ em <18 tuổi. Chưa được nghiên cứu về an toàn và hiệu quả ở trẻ em.",
            "notes": "Cariprazine chỉ được FDA phê duyệt cho người lớn ≥18 tuổi. Không có dữ liệu an toàn và hiệu quả ở trẻ em."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ. Tăng nguy cơ tử vong ở bệnh nhân cao tuổi mắc chứng sa sút trí tuệ (dementia). Thận trọng với tác dụng phụ chuyển hóa, tim mạch, và akathisia. T1/2 rất dài (2-3 ngày) do active metabolites, tích lũy ở người cao tuổi.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (1.5mg/ngày). Tăng dần từ từ. Điều chỉnh liều theo chức năng gan (giảm 50% ở suy gan trung bình, tránh dùng ở suy gan nặng). Do T1/2 dài, cần thời gian lâu hơn để đạt nồng độ ổn định.",
            "monitoring": "Theo dõi chặt chẽ: Cân nặng, BMI, đường huyết, lipid máu, ECG (QT interval), dấu hiệu akathisia, dấu hiệu ngoại tháp (EPS), dấu hiệu tự sát. Tăng nguy cơ tử vong ở bệnh nhân cao tuổi mắc chứng sa sút trí tuệ. Theo dõi lâu hơn do T1/2 dài."
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "200,000 - 400,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Cariprazine là thuốc mới, giá cao. Vraylar (brand) thường đắt (250,000-400,000 VND/viên 1.5-6mg). Generic có thể rẻ hơn (200,000-300,000 VND/viên). Chi phí ước tính: ~$1,225/tháng (quốc tế), tương đương khoảng 28,000,000-32,000,000 VND/tháng tại Việt Nam."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng trực tiếp và độ ẩm. Giữ trong bao bì gốc, đậy kín. Không bảo quản trong phòng tắm hoặc nơi ẩm ướt. Để xa tầm tay trẻ em và thú cưng."
    },
    "Lumateperone":     {
        "group": "Psychiatry - Antipsychotic (Atypical/Third Generation)",
        "vietnamese_name": "Lumateperone, Caplyta",
        "brand_names": {
            "common": [
                "Caplyta"
    ],
            "vietnam": [
                "Lumateperone",
                "Caplyta"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực I và II (depressive episodes)"
    ],
        "contraindications": {
            "absolute": [
                "Dị ứng lumateperone",
                "Trẻ em <18 tuổi (chưa được phê duyệt)"
    ],
            "relative": [
                "Sa sút trí tuệ (tăng nguy cơ tử vong ở người già)",
                "Kéo dài khoảng QT",
                "Tiền sử hội chứng ác tính do thuốc an thần (NMS)"
    ],
        },
        "dosage": {
            "adult_schizophrenia": "42mg x 1 lần/ngày, uống với thức ăn",
            "adult_bipolar_depressive": "42mg x 1 lần/ngày, uống với thức ăn",
            "notes": "Lumateperone có cơ chế tác dụng đa thụ thể phức tạp. Uống với thức ăn để tăng hấp thu. Liều cố định 42mg/ngày, không cần điều chỉnh liều.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "adjustment": "Không cần chỉnh liều ở suy thận nhẹ đến trung bình. Thận trọng ở suy thận nặng.",
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Tránh dùng",
            "notes": "Lumateperone chuyển hóa qua gan (CYP3A4). Tránh dùng ở suy gan nặng.",
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Tăng cân (ít hơn olanzapine)",
            "Rối loạn vận động ngoại tháp (EPS) - ít hơn typical antipsychotics",
            "Kéo dài khoảng QT - ít hơn một số antipsychotics khác",
            "Tăng đường huyết, rối loạn lipid máu (ít hơn olanzapine)",
            "Buồn nôn"
    ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ lumateperone, giảm liều 50%",
            "Thuốc cảm ứng CYP3A4 (Carbamazepine, Rifampin) -> Giảm nồng độ lumateperone, tăng liều",
            "Thuốc kéo dài QT -> Tăng nguy cơ loạn nhịp"
    ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Sử dụng khi lợi ích > nguy cơ. Có nguy cơ triệu chứng ngoại tháp ở trẻ sơ sinh nếu dùng 3 tháng cuối.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể ảnh hưởng phát triển thần kinh trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "pharmacokinetics": {
            "half_life": "13-54 giờ",
            "onset": "1-2 tuần",
            "metabolism": "Gan (CYP3A4)",
        },
        "monitoring": [
            "Cân nặng, BMI",
            "Đường huyết, lipid máu",
            "ECG (Khoảng QT) nếu có nguy cơ",
            "Dấu hiệu ngoại tháp (EPS)",
            "Buồn ngủ"
    ],
        "black_box_warnings": """Người cao tuổi mắc chứng sa sút trí tuệ (Dementia) dùng thuốc chống loạn thần có TĂNG nguy cơ tử vong. Tăng nguy cơ tự sát ở trẻ em, thanh thiếu niên và thanh niên.""",
        "mechanism_of_action": """Lumateperone có cơ chế tác dụng đa thụ thể phức tạp: (1) Antagonist tại dopamine D2 receptors, (2) Antagonist tại serotonin 5-HT2A receptors, (3) Partial agonist tại serotonin 5-HT1A receptors, (4) Ức chế tái hấp thu serotonin (SERT), và (5) Tác động lên glutamate receptors. Cơ chế đa thụ thể này có thể giải thích hiệu quả trong điều trị cả triệu chứng dương tính và âm tính của tâm thần phân liệt, cũng như tác dụng chống trầm cảm trong rối loạn lưỡng cực. Ít tác dụng phụ chuyển hóa và vận động hơn một số antipsychotics khác.""",
        "precautions": [
            "Buồn ngủ - phổ biến, không lái xe sau khi uống",
            "Tăng cân - theo dõi cân nặng, BMI",
            "Tăng đường huyết, rối loạn lipid máu - theo dõi định kỳ",
            "Kéo dài khoảng QT - thận trọng ở bệnh nhân có nguy cơ",
            "Sa sút trí tuệ - tăng nguy cơ tử vong",
            "Uống với thức ăn - tăng hấp thu",
            "Tăng nguy cơ tự sát ở trẻ em, thanh thiếu niên"
    ],
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa lumateperone",
                    "effect": "Tăng nồng độ lumateperone, tăng tác dụng phụ",
                    "management": "Giảm liều lumateperone 50%.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc cảm ứng CYP3A4 (Carbamazepine, Rifampin, St. John's Wort)",
                    "mechanism": "Tăng chuyển hóa lumateperone",
                    "effect": "Giảm nồng độ lumateperone, giảm hiệu quả",
                    "management": "Tăng liều lumateperone nếu cần.",
                }
                ],
            "minor": [],
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Kích động",
                "Rối loạn vận động ngoại tháp",
                "Hạ huyết áp",
                "Tăng nhịp tim"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hỗ trợ",
                "Theo dõi huyết áp, nhịp tim",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi ý thức, huyết áp, nhịp tim, ECG",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn (tăng hấp thu)",
                "timing": "42mg x 1 lần/ngày, cùng thời điểm mỗi ngày, uống với thức ăn",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Caplyta (Lumateperone)",
                "UpToDate - Lumateperone: Drug information",
                "APA Guidelines - Schizophrenia Treatment",
                "APA Guidelines - Bipolar Disorder"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["metabolic", "cardiac"],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Weight", "Glucose", "Lipids", "ECG", "Sedation"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "FDA Black Box Warning - Suicidal Behavior",
            "APA Guidelines - Schizophrenia Treatment",
            "APA Guidelines - Bipolar Disorder"
        ],
        "pediatric_dosing": {
            "adolescents_18plus": "CHỐNG CHỈ ĐỊNH ở trẻ em <18 tuổi. Chưa được FDA phê duyệt cho trẻ em. Chỉ dùng cho người lớn ≥18 tuổi.",
            "children_under_18": "CHỐNG CHỈ ĐỊNH ở trẻ em <18 tuổi. Chưa được nghiên cứu về an toàn và hiệu quả ở trẻ em.",
            "notes": "Lumateperone chỉ được FDA phê duyệt cho người lớn ≥18 tuổi. Không có dữ liệu an toàn và hiệu quả ở trẻ em."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ. Tăng nguy cơ tử vong ở bệnh nhân cao tuổi mắc chứng sa sút trí tuệ (dementia). Thận trọng với tác dụng phụ chuyển hóa và buồn ngủ. Ít tác dụng phụ chuyển hóa hơn một số antipsychotics khác (ưu điểm).",
            "dose_adjustment": "Liều cố định 42mg/ngày, không cần điều chỉnh liều ở suy thận nhẹ đến trung bình. Tránh dùng ở suy gan nặng. Có thể cần giảm liều nếu có tác dụng phụ buồn ngủ nặng.",
            "monitoring": "Theo dõi chặt chẽ: Cân nặng, BMI, đường huyết, lipid máu, ECG (QT interval), dấu hiệu buồn ngủ, dấu hiệu tự sát. Tăng nguy cơ tử vong ở bệnh nhân cao tuổi mắc chứng sa sút trí tuệ. Ít tác dụng phụ chuyển hóa hơn (ưu điểm)."
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "250,000 - 500,000 VND/viên (tùy thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Lumateperone là thuốc mới nhất, giá rất cao. Caplyta (brand) thường đắt (300,000-500,000 VND/viên 42mg). Generic chưa có sẵn. Chi phí ước tính: ~$1,320/tháng (quốc tế), tương đương khoảng 30,000,000-35,000,000 VND/tháng tại Việt Nam."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng trực tiếp và độ ẩm. Giữ trong bao bì gốc, đậy kín. Không bảo quản trong phòng tắm hoặc nơi ẩm ướt. Để xa tầm tay trẻ em và thú cưng."
    },
    "Pimavanserin":     {
        "group": "Psychiatry - Antipsychotic (Atypical/Selective Serotonin Inverse Agonist)",
        "vietnamese_name": "Pimavanserin, Nuplazid",
        "brand_names": {
            "common": [
                "Nuplazid"
    ],
            "vietnam": [
                "Pimavanserin",
                "Nuplazid"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Ảo giác và hoang tưởng liên quan đến bệnh Parkinson (Parkinson's disease psychosis)",
            "Ảo giác và hoang tưởng liên quan đến chứng mất trí nhớ với thể Lewy (Dementia with Lewy bodies) - off-label"
    ],
        "contraindications": {
            "absolute": [
                "Dị ứng pimavanserin",
                "Trẻ em <18 tuổi (chưa được phê duyệt)"
    ],
            "relative": [
                "Kéo dài khoảng QT",
                "Rối loạn nhịp tim",
                "Suy gan nặng",
                "Suy thận nặng"
    ],
        },
        "dosage": {
            "adult_parkinson_psychosis": "34mg x 1 lần/ngày, uống với thức ăn",
            "notes": "Pimavanserin là selective serotonin inverse agonist tại 5-HT2A receptors, KHÔNG tác động lên dopamine receptors. Do đó, không làm nặng thêm các triệu chứng vận động của bệnh Parkinson (không gây parkinsonism). Liều cố định 34mg/ngày. Uống với thức ăn để tăng hấp thu.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "adjustment": "Không cần chỉnh liều ở suy thận nhẹ đến trung bình. Thận trọng ở suy thận nặng.",
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Tránh dùng",
            "notes": "Pimavanserin chuyển hóa qua gan (CYP3A4, CYP2J2). Tránh dùng ở suy gan nặng.",
        },
        "side_effects": [
            "Kéo dài khoảng QT (QUAN TRỌNG - nguy cơ cao)",
            "Buồn ngủ",
            "Phù ngoại vi",
            "Buồn nôn",
            "Rối loạn nhận thức",
            "Ảo giác (paradoxical - hiếm)"
    ],
        "interactions": [
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ pimavanserin, giảm liều 50%",
            "Thuốc cảm ứng CYP3A4 (Carbamazepine, Rifampin) -> Giảm nồng độ pimavanserin, tăng liều",
            "Thuốc kéo dài QT -> Tăng nguy cơ loạn nhịp (QUAN TRỌNG)",
            "Thuốc chống loạn nhịp (Amiodarone, Sotalol) -> Tránh dùng chung"
    ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Sử dụng khi lợi ích > nguy cơ. Dữ liệu hạn chế.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể ảnh hưởng phát triển thần kinh trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "pharmacokinetics": {
            "half_life": "57 giờ (dài)",
            "onset": "1-2 tuần",
            "metabolism": "Gan (CYP3A4, CYP2J2)",
        },
        "monitoring": [
            "ECG (Khoảng QT) - QUAN TRỌNG, trước và trong khi điều trị",
            "Triệu chứng vận động Parkinson (theo dõi không nặng thêm)",
            "Triệu chứng tâm thần (ảo giác, hoang tưởng)",
            "Nhịp tim"
    ],
        "black_box_warnings": """NGUY CƠ KÉO DÀI KHOẢNG QT VÀ LOẠN NHỊP TIM. Theo dõi ECG trước và trong khi điều trị. Người cao tuổi mắc chứng sa sút trí tuệ (Dementia) dùng thuốc chống loạn thần có TĂNG nguy cơ tử vong.""",
        "mechanism_of_action": """Pimavanserin là selective serotonin inverse agonist tại 5-HT2A receptors. KHÔNG tác động lên dopamine receptors (không phải dopamine antagonist). Do đó, pimavanserin không gây parkinsonism và không làm nặng thêm các triệu chứng vận động của bệnh Parkinson, khác với các antipsychotics điển hình. Pimavanserin điều trị ảo giác và hoang tưởng thông qua tác động lên hệ thống serotonin, đặc biệt phù hợp cho bệnh nhân Parkinson và Dementia with Lewy bodies.""",
        "precautions": [
            "NGUY CƠ KÉO DÀI KHOẢNG QT CAO - theo dõi ECG trước và trong khi điều trị",
            "Tránh dùng với thuốc kéo dài QT khác",
            "Tránh dùng với thuốc chống loạn nhịp",
            "Uống với thức ăn - tăng hấp thu",
            "Sa sút trí tuệ - tăng nguy cơ tử vong",
            "Theo dõi triệu chứng vận động Parkinson (không nên nặng thêm)"
    ],
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Macrolides, Quinolones)",
                    "mechanism": "Tác dụng cộng dồn kéo dài QT",
                    "effect": "Tăng nguy cơ loạn nhịp tim nghiêm trọng (Torsades de Pointes)",
                    "management": "TRÁNH DÙNG CHUNG. Nếu phải dùng, theo dõi ECG chặt chẽ.",
                },
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa pimavanserin",
                    "effect": "Tăng nồng độ pimavanserin, tăng nguy cơ kéo dài QT",
                    "management": "Giảm liều pimavanserin 50%.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc cảm ứng CYP3A4 (Carbamazepine, Rifampin, St. John's Wort)",
                    "mechanism": "Tăng chuyển hóa pimavanserin",
                    "effect": "Giảm nồng độ pimavanserin, giảm hiệu quả",
                    "management": "Tăng liều pimavanserin nếu cần.",
                }
                ],
            "minor": [],
        },
        "overdose_management": {
            "symptoms": [
                "Kéo dài khoảng QT nặng",
                "Loạn nhịp tim (Torsades de Pointes)",
                "Buồn ngủ",
                "Hạ huyết áp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Theo dõi ECG liên tục - QUAN TRỌNG",
                "Điều trị loạn nhịp tim nếu có",
                "Điều trị hỗ trợ",
                "Theo dõi huyết áp, nhịp tim",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi ECG liên tục (QUAN TRỌNG), huyết áp, nhịp tim",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn (tăng hấp thu)",
                "timing": "34mg x 1 lần/ngày, cùng thời điểm mỗi ngày, uống với thức ăn",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nuplazid (Pimavanserin)",
                "UpToDate - Pimavanserin: Drug information",
                "APA Guidelines - Parkinson's Disease Psychosis"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac"],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (QT interval) - CRITICAL", "Heart rate"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - QT Prolongation",
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "APA Guidelines - Parkinson's Disease Psychosis"
        ],
        "pediatric_dosing": {
            "adolescents_18plus": "CHỐNG CHỈ ĐỊNH ở trẻ em <18 tuổi. Chưa được FDA phê duyệt cho trẻ em. Chỉ dùng cho người lớn ≥18 tuổi.",
            "children_under_18": "CHỐNG CHỈ ĐỊNH ở trẻ em <18 tuổi. Chưa được nghiên cứu về an toàn và hiệu quả ở trẻ em.",
            "notes": "Pimavanserin chỉ được FDA phê duyệt cho người lớn ≥18 tuổi với ảo giác và hoang tưởng liên quan đến bệnh Parkinson. Không có dữ liệu an toàn và hiệu quả ở trẻ em."
        },
        "geriatric_dosing": {
            "considerations": "Pimavanserin chủ yếu dùng cho bệnh nhân cao tuổi mắc bệnh Parkinson. Tăng nguy cơ tử vong ở bệnh nhân cao tuổi mắc chứng sa sút trí tuệ (dementia). Thận trọng với QT prolongation và rối loạn nhịp tim. Ưu điểm: không làm nặng thêm triệu chứng vận động của Parkinson (không gây parkinsonism).",
            "dose_adjustment": "Liều cố định 34mg/ngày, không cần điều chỉnh liều ở suy thận nhẹ đến trung bình. Tránh dùng ở suy gan nặng. Có thể cần giảm liều hoặc tránh dùng nếu có QT prolongation hoặc rối loạn nhịp tim.",
            "monitoring": "Theo dõi chặt chẽ: ECG (QT interval) - BẮT BUỘC, nhịp tim, dấu hiệu rối loạn nhịp tim, triệu chứng Parkinson (đảm bảo không làm nặng thêm), dấu hiệu tự sát. Tăng nguy cơ tử vong ở bệnh nhân cao tuổi mắc chứng sa sút trí tuệ. QT prolongation là black box warning."
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "200,000 - 500,000 VND/viên (tùy thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Pimavanserin là thuốc mới, giá rất cao. Nuplazid (brand) thường đắt (250,000-500,000 VND/viên 34mg). Generic chưa có sẵn. Chi phí ước tính: ~$1,200-1,500/tháng (quốc tế), tương đương khoảng 28,000,000-35,000,000 VND/tháng tại Việt Nam."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng trực tiếp và độ ẩm. Giữ trong bao bì gốc, đậy kín. Không bảo quản trong phòng tắm hoặc nơi ẩm ướt. Để xa tầm tay trẻ em và thú cưng."
    }
}
