"""
Enhanced fields overrides - Emergency
"""
from typing import Any, Dict


EMERGENCY_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
        # ======================== EMERGENCY: VASOPRESSORS ==========================
        "Norepinephrine": {
            "contraindications": {
                "tuyệt_đối": [],
                "tương_đối": [
                    "Thiếu máu cục bộ mô (nếu có thể tránh)",
                    "Rối loạn nhịp tim nặng",
                    "Pheochromocytoma",
                ],
            },
            "drug_interactions": {
                "major": [
                    {
                        "drug": "MAO inhibitors (MAOIs)",
                        "mechanism": "MAOIs ức chế chuyển hóa norepinephrine, tăng nồng độ",
                        "effect": "Tăng tác dụng mạnh, tăng huyết áp nặng, nguy cơ cơn tăng huyết áp",
                        "management": "Giảm liều norepinephrine xuống 50-75% khi dùng với MAOI. Theo dõi huyết áp sát.",
                    },
                    {
                        "drug": "Tricyclic antidepressants (TCA)",
                        "mechanism": "TCA ức chế tái hấp thu norepinephrine, tăng tác dụng",
                        "effect": "Tăng tác dụng mạnh, tăng huyết áp",
                        "management": "Giảm liều norepinephrine. Theo dõi huyết áp sát.",
                    },
                ],
                "moderate": [
                    {
                        "drug": "Beta-blockers",
                        "mechanism": "Block beta-receptors, tăng tác dụng alpha (co mạch)",
                        "effect": "Tăng huyết áp nặng, giảm nhịp tim",
                        "management": "Thận trọng. Theo dõi huyết áp và nhịp tim sát.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "An toàn trong cấp cứu. Dữ liệu hạn chế nhưng được sử dụng rộng rãi trong sốc thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Half-life rất ngắn (1-2 phút), không bài tiết vào sữa đáng kể.",
                    "recommendation": "Có thể dùng khi cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Norepinephrine bị bất hoạt nhanh bởi MAO và COMT, không phụ thuộc chức năng gan.",
            },
            "overdose_management": {
                "symptoms": [
                    "Tăng huyết áp nặng",
                    "Co mạch ngoại vi mạnh",
                    "Hoại tử mô (nếu rò rỉ ngoài mạch)",
                    "Rối loạn nhịp tim",
                    "Giảm tưới máu thận, suy thận cấp",
                ],
                "antidote": "Phentolamine (alpha-blocker) để đối kháng tác dụng alpha.",
                "treatment": [
                    "Ngừng truyền norepinephrine ngay lập tức",
                    "Nếu rò rỉ ngoài mạch: tiêm phentolamine 5-10mg pha loãng quanh vị trí rò rỉ để giảm co mạch",
                    "Phentolamine IV nếu tăng huyết áp nặng",
                    "Theo dõi huyết áp, nhịp tim, tưới máu mô liên tục",
                    "Truyền dịch nếu cần",
                ],
                "monitoring": "Huyết áp, nhịp tim, ECG, lactate máu, chức năng thận, tưới máu mô (da, thận, chi).",
            },
            "reversal_agents": {
                "available": True,
                "agents": ["Phentolamine (alpha-blocker)"],
                "notes": "Phentolamine có thể đối kháng tác dụng alpha của norepinephrine. Ngừng truyền là biện pháp chính.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha 4mg trong 250ml D5W = 16 mcg/ml. Hoặc pha theo hướng dẫn nhà sản xuất.",
                    "infusion_rate": "Truyền liên tục qua bơm tiêm điện, điều chỉnh theo huyết áp. Khởi đầu 0.05-0.1 mcg/kg/phút.",
                    "notes": "TUYỆT ĐỐI phải truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử nếu rò rỉ). Theo dõi huyết áp liên tục (arterial line nếu có thể).",
                },
            },
        },

        "Dopamine": {
            "contraindications": {
                "tuyệt_đối": [
                    "Pheochromocytoma",
                ],
                "tương_đối": [
                    "Rối loạn nhịp tim nặng",
                    "Thiếu máu cục bộ mô",
                ],
            },

            "drug_interactions": {
                "major": [
                    {
                        "drug": "MAO inhibitors (MAOIs)",
                        "mechanism": "MAOIs ức chế chuyển hóa dopamine, tăng nồng độ",
                        "effect": "Tăng tác dụng mạnh, tăng huyết áp nặng",
                        "management": "Giảm liều dopamine xuống 50-75% khi dùng với MAOI. Theo dõi huyết áp sát.",
                    },
                ],
                "moderate": [
                    {
                        "drug": "Beta-blockers",
                        "mechanism": "Block beta-receptors, tăng tác dụng alpha (ở liều cao)",
                        "effect": "Tăng huyết áp nặng",
                        "management": "Thận trọng. Theo dõi huyết áp và nhịp tim sát.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "An toàn trong cấp cứu. Dữ liệu hạn chế nhưng được sử dụng rộng rãi.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Half-life rất ngắn (1-2 phút), không bài tiết vào sữa đáng kể.",
                    "recommendation": "Có thể dùng khi cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Dopamine bị bất hoạt nhanh bởi MAO và COMT, không phụ thuộc chức năng gan.",
            },
            "overdose_management": {
                "symptoms": [
                    "Rối loạn nhịp tim nặng",
                    "Tăng huyết áp nặng (liều cao)",
                    "Co mạch ngoại vi (liều cao)",
                    "Hoại tử mô (nếu rò rỉ ngoài mạch)",
                ],
                "antidote": "Không có antidote đặc hiệu. Ngừng truyền là biện pháp chính.",
                "treatment": [
                    "Ngừng truyền dopamine ngay lập tức",
                    "Nếu rò rỉ ngoài mạch: tiêm phentolamine 5-10mg pha loãng quanh vị trí rò rỉ",
                    "Theo dõi huyết áp, nhịp tim, ECG liên tục",
                    "Điều trị rối loạn nhịp tim nếu cần",
                ],
                "monitoring": "Huyết áp, nhịp tim, ECG, tưới máu mô, dấu hiệu hoại tử.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Ngừng truyền là biện pháp chính.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha 400mg trong 250ml D5W = 1600 mcg/ml. Hoặc pha theo hướng dẫn nhà sản xuất.",
                    "infusion_rate": "Truyền liên tục qua bơm tiêm điện, điều chỉnh theo huyết áp và tác dụng mong muốn. Tác dụng phụ thuộc liều.",
                    "notes": "Truyền qua đường tĩnh mạch trung tâm (nguy cơ hoại tử nếu rò rỉ). Theo dõi huyết áp, nhịp tim liên tục. Không dùng liều thấp cho suy thận (không có bằng chứng).",
                },
            },
        },

        "Dobutamine": {
            "contraindications": {
                "tuyệt_đối": [
                    "Hẹp động mạch chủ nặng",
                ],
                "tương_đối": [
                    "Rối loạn nhịp tim nặng",
                    "Sốc giảm thể tích (chưa bù dịch)",
                    "Bệnh mạch vành không ổn định",
                ],
            },
            "drug_interactions": {
                "major": [],
                "moderate": [
                    {
                        "drug": "Beta-blockers",
                        "mechanism": "Đối kháng tác dụng beta của dobutamine",
                        "effect": "Giảm hiệu quả dobutamine",
                        "management": "Có thể cần tăng liều dobutamine. Theo dõi cung lượng tim sát.",
                    },
                    {
                        "drug": "MAO inhibitors",
                        "mechanism": "MAOIs ức chế chuyển hóa catecholamine",
                        "effect": "Tăng tác dụng dobutamine",
                        "management": "Giảm liều dobutamine. Theo dõi nhịp tim, huyết áp sát.",
                    },
                ],
                "minor": [],
            },
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": "An toàn trong cấp cứu. Dữ liệu hạn chế nhưng được sử dụng rộng rãi.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Half-life rất ngắn (2 phút), không bài tiết vào sữa đáng kể.",
                    "recommendation": "Có thể dùng khi cho con bú.",
                },
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Không cần chỉnh liều.",
                "severe": "Không cần chỉnh liều.",
                "notes": "Dobutamine bị bất hoạt nhanh bởi MAO và COMT, không phụ thuộc chức năng gan.",
            },
            "overdose_management": {
                "symptoms": [
                    "Tăng nhịp tim nặng",
                    "Rối loạn nhịp tim",
                    "Hạ huyết áp (do giãn mạch)",
                    "Đau ngực",
                    "Thiếu máu cục bộ cơ tim",
                ],
                "antidote": "Không có antidote đặc hiệu. Beta-blocker có thể đối kháng một phần.",
                "treatment": [
                    "Ngừng truyền dobutamine ngay lập tức",
                    "Theo dõi huyết áp, nhịp tim, ECG liên tục",
                    "Điều trị rối loạn nhịp tim nếu cần",
                    "Beta-blocker nếu nhịp tim quá nhanh (thận trọng)",
                    "Truyền dịch nếu hạ huyết áp",
                ],
                "monitoring": "Huyết áp, nhịp tim, ECG, cung lượng tim, dấu hiệu thiếu máu cục bộ.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Beta-blocker có thể đối kháng một phần nhưng không khuyến cáo thường quy.",
            },
            "administration_instructions": {
                "iv": {
                    "reconstitution": "Pha 250mg trong 250ml D5W = 1000 mcg/ml. Hoặc pha theo hướng dẫn nhà sản xuất.",
                    "infusion_rate": "Truyền liên tục qua bơm tiêm điện, điều chỉnh theo cung lượng tim. Khởi đầu 2.5-5 mcg/kg/phút.",
                    "notes": "Bù dịch đầy đủ trước khi dùng (tránh hạ huyết áp). Theo dõi nhịp tim, ECG liên tục. Giảm liều khi cung lượng tim đã cải thiện.",
                },
            },
        },

    # ======================== BATCH 1: ICU/EMERGENCY DRUGS ========================
        "Alteplase": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với alteplase hoặc bất kỳ thành phần nào",
                    "Xuất huyết nội sọ đang hoạt động",
                    "Tiền sử đột quỵ xuất huyết",
                    "Chấn thương đầu hoặc phẫu thuật đầu gần đây (3 tháng)",
                    "Xuất huyết tiêu hóa hoặc tiết niệu trong 21 ngày",
                    "Rối loạn đông máu",
                    "Huyết áp tâm thu >185 mmHg hoặc tâm trương >110 mmHg không kiểm soát được",
                ],
                "tương_đối": [
                    "Tuổi >80 tuổi - tăng nguy cơ xuất huyết",
                    "Điểm NIHSS >25 - nguy cơ cao",
                    "Điều trị kháng đông trong 48 giờ",
                    "Tiểu cầu <100,000/mm³",
                    "INR >1.7 hoặc PT >15 giây",
                    "Đường huyết <50 mg/dL hoặc >400 mg/dL",
                    "Đột quỵ nhẹ hoặc TIA trong 3 tháng",
                ],
            },
        },

        "Aspirin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với aspirin hoặc NSAID",
                    "Tiền sử hen suyễn do aspirin",
                    "Xuất huyết tiêu hóa đang hoạt động",
                    "Loét dạ dày tá tràng đang hoạt động",
                    "Rối loạn đông máu (hemophilia, von Willebrand)",
                    "Suy gan nặng",
                    "Suy thận nặng (CrCl <30)",
                    "Trẻ em <16 tuổi (nguy cơ hội chứng Reye)",
                ],
                "tương_đối": [
                    "Tiền sử loét dạ dày tá tràng",
                    "Đang dùng thuốc chống đông",
                    "Suy thận vừa (CrCl 30-60)",
                    "Suy gan vừa",
                    "Có thai (3 tháng cuối)",
                    "Đang cho con bú",
                    "Gout - có thể làm tăng acid uric",
                ],
            },
        },

        "Epinephrine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với epinephrine hoặc bất kỳ thành phần nào",
                    "Rối loạn nhịp tim nặng không kiểm soát được",
                    "Phẫu thuật tim gần đây",
                ],
                "tương_đối": [
                    "Bệnh tim mạch nặng",
                    "Tăng huyết áp nặng",
                    "Đái tháo đường",
                    "Cường giáp",
                    "Glaucoma góc đóng",
                    "Bệnh mạch máu ngoại biên",
                    "Người cao tuổi - tăng nhạy cảm",
                ],
            },
        },

        "Morphine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với morphine hoặc opioid",
                    "Suy hô hấp nặng không có hỗ trợ thở máy",
                    "Hen suyễn nặng không kiểm soát",
                    "Tắc ruột cơ học",
                    "Tăng áp lực nội sọ",
                    "Ức chế hô hấp nặng",
                ],
                "tương_đối": [
                    "Suy hô hấp vừa",
                    "Suy gan nặng",
                    "Suy thận nặng (CrCl <30)",
                    "Người cao tuổi - giảm liều",
                    "Có thai - nguy cơ ức chế hô hấp ở trẻ sơ sinh",
                    "Đang cho con bú",
                    "Tiền sử lạm dụng chất",
                    "Bệnh động kinh",
                ],
            },
        },

        "Metformin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với metformin",
                    "Suy thận nặng (CrCl <30 mL/min)",
                    "Nhiễm toan lactic",
                    "Suy gan nặng",
                    "Suy tim nặng cần điều trị bằng thuốc",
                    "Nhiễm trùng nặng hoặc mất nước nặng",
                ],
                "tương_đối": [
                    "Suy thận vừa (CrCl 30-45) - giảm liều",
                    "Suy gan vừa - thận trọng",
                    "Người cao tuổi >80 tuổi - giảm liều",
                    "Nghiện rượu",
                    "Phẫu thuật lớn hoặc thủ thuật có cản quang - tạm ngừng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Naloxone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với naloxone hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Bệnh nhân phụ thuộc opioid - có thể gây hội chứng cai nghiện nặng",
                    "Bệnh tim mạch - có thể gây rối loạn nhịp tim",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (monitor for re-overdose)",
                    "Level of consciousness (GCS)",
                    "Blood pressure and heart rate",
                    "Signs of opioid withdrawal syndrome",
                    "Signs of re-overdose (respiratory depression returns)"
                ],
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "AHA ACLS Guidelines - Opioid Overdose Management",
                "CDC Opioid Overdose Guidelines",
                "WHO Guidelines - Opioid Overdose Response",
                "SAMHSA Opioid Overdose Prevention Toolkit",
                "FDA Drug Label - Naloxone (Narcan)"
            ]
        },

        "Flumazenil": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với flumazenil hoặc benzodiazepine",
                    "Bệnh nhân phụ thuộc benzodiazepine - nguy cơ co giật",
                    "Đang dùng thuốc gây co giật (TCA, bupropion)",
                ],
                "tương_đối": [
                    "Bệnh nhân có tiền sử co giật",
                    "Tổn thương não",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Suy gan nặng - thời gian tác dụng kéo dài",
                ],
            },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Level of consciousness (GCS) - CRITICAL (monitor for re-sedation)",
                    "Respiratory rate and SpO2 - CRITICAL (monitor for re-respiratory depression)",
                    "Blood pressure and heart rate",
                    "Signs of benzodiazepine withdrawal syndrome",
                    "Seizure activity (especially in patients with seizure history)",
                    "Signs of re-sedation (benzodiazepine effects return)"
                ],
                "look_alike_sound_alike": []
            },
            "guideline_tags": [
                "AHA ACLS Guidelines - Benzodiazepine Overdose Management",
                "FDA Drug Label - Flumazenil (Anexate)",
                "Benzodiazepine Overdose Guidelines",
                "UpToDate - Flumazenil: Drug Information",
                "ISMP High Alert Medications - Reversal Agents"
            ]
        },

        # ======================== SESSION 1: EMERGENCY/ICU DRUGS - REMAINING ========================
        "Adenosine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (AV block - can be severe, bradycardia - can be severe, Black Box Warning)",
                    "respiratory": "Moderate (bronchospasm - can be severe in asthma/COPD, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (continuous monitoring, AV block can be severe, Black Box Warning)",
                    "Heart rate - CRITICAL (bradycardia can be severe, Black Box Warning)",
                    "Blood pressure - CRITICAL (hypotension can occur)",
                    "Respiratory rate and SpO2 - CRITICAL (bronchospasm can be severe in asthma/COPD, Black Box Warning)",
                    "Administration technique - CRITICAL (must inject IV bolus RAPIDLY in 1-2 seconds into large vein, then flush immediately with 10-20ml NS)",
                    "Drug interactions (dipyridamole - reduce dose 50-75%, theophylline/caffeine - may need higher dose) - CRITICAL",
                    "Half-life - CRITICAL (<10 seconds, very short, effects usually resolve within seconds to minutes)"
                ],
                "look_alike_sound_alike": ["Adenosine", "Adenocard", "Adenosine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - AV Block (Can Be Severe)",
                "FDA Black Box Warning - Bradycardia (Can Be Severe)",
                "FDA Black Box Warning - Bronchospasm (Can Be Severe in Asthma/COPD)",
                "FDA Drug Label - Adenosine (Adenocard)",
                "ACC/AHA/ESC Guidelines - Supraventricular Tachycardia",
                "AHA ACLS Guidelines - SVT Management",
                "ISMP High Alert Medications"
            ]
        },

        "Amiodarone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "pulmonary": "High (interstitial pneumonitis - can be fatal, Black Box Warning)",
                    "hepatic": "High (hepatotoxicity - can be fatal, Black Box Warning)",
                    "cardiac": "High (arrhythmias - can be fatal, Black Box Warning, QT prolongation, torsades de pointes)",
                    "endocrine": "High (thyroid dysfunction - hyperthyroidism or hypothyroidism, very common)",
                    "ophthalmic": "Moderate (corneal deposits, cataracts, very common)",
                    "dermatologic": "Moderate (photosensitivity, blue-gray skin discoloration, very common)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Pulmonary function (chest X-ray, PFT) - CRITICAL (every 6 months, interstitial pneumonitis can be fatal, Black Box Warning)",
                    "Hepatic function (ALT, AST, bilirubin) - CRITICAL (every 3-6 months, hepatotoxicity can be fatal, Black Box Warning)",
                    "ECG (QT interval) - CRITICAL (QT prolongation is normal but QTc >500ms or increase >60ms is dangerous, Black Box Warning)",
                    "Thyroid function (TSH, FT4, FT3) - CRITICAL (every 6 months, hyperthyroidism or hypothyroidism very common)",
                    "Ophthalmologic exam - CRITICAL (every 6-12 months, corneal deposits, cataracts very common)",
                    "Electrolytes (K+, Mg2+) - CRITICAL (must be normal before use, hypokalemia/hypomagnesemia increase torsades risk)",
                    "Drug interactions (digoxin - reduce dose 50%, warfarin - reduce dose 30-50%, statins - reduce dose 50%, QT-prolonging drugs - CONTRAINDICATED) - CRITICAL",
                    "Half-life - CRITICAL (50-60 days, very long, effects persist after discontinuation)"
                ],
                "look_alike_sound_alike": ["Amiodarone", "Cordarone", "Dronedarone", "Sotalol"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Pulmonary Toxicity (Interstitial Pneumonitis, Can Be Fatal)",
                "FDA Black Box Warning - Hepatotoxicity (Can Be Fatal)",
                "FDA Black Box Warning - Arrhythmias (Can Be Fatal, QT Prolongation)",
                "FDA Black Box Warning - Only for Life-Threatening Arrhythmias",
                "FDA Drug Label - Amiodarone (Cordarone)",
                "ACC/AHA Guidelines - Arrhythmias",
                "ESC Guidelines - Arrhythmias",
                "AHA ACLS Guidelines - Ventricular Arrhythmias",
                "ISMP High Alert Medications"
            ]
        },

        "Atropine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "ophthalmic": "High (glaucoma angle-closure - can cause blindness, contraindicated)",
                    "urinary": "Moderate (urinary retention - can be severe, contraindicated in obstruction)",
                    "neurologic": "Moderate (confusion, delirium - especially in elderly)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Heart rate and ECG - CRITICAL (monitor for paradoxical bradycardia with doses <0.5mg in adults)",
                    "Blood pressure",
                    "Intraocular pressure - CRITICAL (contraindicated in angle-closure glaucoma)",
                    "Urinary output - CRITICAL (contraindicated in urinary obstruction)",
                    "Mental status - CRITICAL (confusion, delirium especially in elderly)",
                    "Body temperature - CRITICAL (can increase temperature due to decreased sweating, contraindicated in fever)",
                    "Minimum dose - CRITICAL (adults: minimum 0.5mg to avoid paradoxical bradycardia)"
                ],
                "look_alike_sound_alike": ["Atropine", "Atrovent", "Ipratropium"]
            },
            "guideline_tags": [
                "FDA Drug Label - Atropine",
                "AHA ACLS Guidelines - Bradycardia Management",
                "AHA ACLS Guidelines - Cardiac Arrest (Asystole/PEA)",
                "WHO Guidelines - Organophosphate Poisoning",
                "ISMP High Alert Medications"
            ]
        },

        "Calcium chloride": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (arrhythmias - can be severe, especially with digoxin)",
                    "renal": "Moderate (hypercalcemia, kidney stones with prolonged use)",
                    "vascular": "High (tissue necrosis if extravasation, vascular irritation)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (continuous monitoring, arrhythmias can be severe, especially with digoxin)",
                    "Ionized calcium levels - CRITICAL (monitor for hypercalcemia)",
                    "Injection site - CRITICAL (tissue necrosis if extravasation, must use large vein)",
                    "Infusion rate - CRITICAL (must infuse SLOWLY over 5-10 minutes, rapid infusion can cause arrhythmias)",
                    "Drug interactions (digoxin - CONTRAINDICATED, sodium bicarbonate - CONTRAINDICATED - precipitation)",
                    "Compatibility - CRITICAL (DO NOT mix with sodium bicarbonate, phosphate, ceftriaxone - precipitation)"
                ],
                "look_alike_sound_alike": ["Calcium chloride", "Calcium gluconate"]
            },
            "guideline_tags": [
                "FDA Drug Label - Calcium Chloride Injection",
                "AHA ACLS Guidelines - Hyperkalemia Management",
                "AHA ACLS Guidelines - Hypocalcemia Management",
                "AHA ACLS Guidelines - Calcium Channel Blocker Overdose",
                "ISMP High Alert Medications - High Alert Drug"
            ]
        },

        "Calcium gluconate": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "Moderate (arrhythmias - can occur, especially with digoxin)",
                    "renal": "Moderate (hypercalcemia, kidney stones with prolonged use)",
                    "vascular": "Moderate (tissue irritation if extravasation, less than calcium chloride)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (monitor for arrhythmias, especially with digoxin)",
                    "Ionized calcium levels - CRITICAL (monitor for hypercalcemia)",
                    "Injection site - CRITICAL (tissue irritation if extravasation)",
                    "Infusion rate - CRITICAL (must infuse SLOWLY over 5-10 minutes)",
                    "Drug interactions (digoxin - use with caution, sodium bicarbonate - CONTRAINDICATED - precipitation)",
                    "Compatibility - CRITICAL (DO NOT mix with sodium bicarbonate, phosphate, ceftriaxone - precipitation)"
                ],
                "look_alike_sound_alike": ["Calcium gluconate", "Calcium chloride"]
            },
            "guideline_tags": [
                "FDA Drug Label - Calcium Gluconate Injection",
                "AHA ACLS Guidelines - Hyperkalemia Management",
                "AHA ACLS Guidelines - Hypocalcemia Management",
                "AHA ACLS Guidelines - Calcium Channel Blocker Overdose"
            ]
        },

        "Lidocaine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neurologic": "High (CNS toxicity - seizures, respiratory arrest, can be fatal, early warning signs: dizziness, tinnitus, perioral numbness)",
                    "cardiac": "High (arrhythmias, AV block, asystole - can be fatal, occurs after CNS toxicity)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "CNS toxicity signs - CRITICAL (dizziness, tinnitus, perioral numbness, confusion - EARLY WARNING SIGNS, stop immediately if present)",
                    "Seizures - CRITICAL (can occur with overdose, prepare benzodiazepines)",
                    "ECG - CRITICAL (continuous monitoring, arrhythmias, AV block can occur after CNS toxicity)",
                    "Respiratory rate - CRITICAL (respiratory arrest can occur with overdose)",
                    "Hepatic function - CRITICAL (reduce dose in hepatic impairment, lidocaine metabolized by liver)",
                    "Lidocaine levels - CRITICAL (if using prolonged infusion or high doses, therapeutic range 1.5-5 mcg/ml)",
                    "Infusion rate - CRITICAL (do not exceed 25-50mg/min IV push, slow infusion for maintenance)"
                ],
                "look_alike_sound_alike": ["Lidocaine", "Xylocaine", "Bupivacaine", "Ropivacaine"]
            },
            "guideline_tags": [
                "FDA Drug Label - Lidocaine (Xylocaine)",
                "AHA ACLS Guidelines - Ventricular Arrhythmias",
                "AHA ACLS Guidelines - Cardiac Arrest (Ventricular Fibrillation/Pulseless VT)",
                "ISMP High Alert Medications",
                "FDA Warning - CNS Toxicity (Seizures, Respiratory Arrest)"
            ]
        },

        "Magnesium sulfate": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neurologic": "High (respiratory depression, muscle weakness, paralysis - can be fatal with hypermagnesemia)",
                    "cardiac": "High (hypotension, bradycardia, heart block, cardiac arrest - can be fatal with hypermagnesemia)",
                    "respiratory": "High (respiratory depression, respiratory arrest - can be fatal with hypermagnesemia)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Magnesium levels - CRITICAL (monitor for hypermagnesemia, especially in renal impairment)",
                    "Deep tendon reflexes - CRITICAL (loss of reflexes is early sign of hypermagnesemia, stop infusion if absent)",
                    "Respiratory rate and SpO2 - CRITICAL (respiratory depression can occur with hypermagnesemia)",
                    "ECG - CRITICAL (monitor for bradycardia, heart block, cardiac arrest)",
                    "Blood pressure - CRITICAL (hypotension can occur)",
                    "Renal function - CRITICAL (reduce dose in renal impairment, magnesium excreted by kidneys)",
                    "Calcium levels - CRITICAL (hypocalcemia can occur, especially with rapid infusion)"
                ],
                "look_alike_sound_alike": ["Magnesium sulfate", "MgSO4"]
            },
            "guideline_tags": [
                "FDA Drug Label - Magnesium Sulfate Injection",
                "AHA ACLS Guidelines - Torsades de Pointes",
                "AHA ACLS Guidelines - Hypomagnesemia Management",
                "ACOG Guidelines - Eclampsia/Preeclampsia",
                "ISMP High Alert Medications",
                "FDA Warning - Hypermagnesemia (Respiratory Depression, Cardiac Arrest)"
            ]
        },

        "Sodium bicarbonate": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "metabolic": "High (metabolic alkalosis - can be severe, hypernatremia, hypokalemia, hypocalcemia)",
                    "cardiac": "Moderate (paradoxical intracellular acidosis, decreased oxygen delivery)",
                    "respiratory": "Moderate (respiratory depression due to alkalosis)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Arterial blood gas (pH, HCO3-, pCO2) - CRITICAL (monitor for metabolic alkalosis, target pH 7.30-7.50)",
                    "Serum sodium - CRITICAL (monitor for hypernatremia, especially with rapid infusion)",
                    "Serum potassium - CRITICAL (monitor for hypokalemia, can cause arrhythmias)",
                    "Serum calcium - CRITICAL (monitor for hypocalcemia, can cause tetany, seizures)",
                    "ECG - CRITICAL (monitor for arrhythmias, especially with hypokalemia/hypocalcemia)",
                    "Infusion rate - CRITICAL (must infuse SLOWLY, rapid infusion can cause severe complications)",
                    "Compatibility - CRITICAL (DO NOT mix with calcium salts - precipitation, DO NOT mix with catecholamines - inactivation)",
                    "Indications - CRITICAL (only use in severe metabolic acidosis with pH <7.1, hyperkalemia with ECG changes, certain poisonings)"
                ],
                "look_alike_sound_alike": ["Sodium bicarbonate", "NaHCO3", "Baking soda"]
            },
            "guideline_tags": [
                "FDA Drug Label - Sodium Bicarbonate Injection",
                "AHA ACLS Guidelines - Metabolic Acidosis Management",
                "AHA ACLS Guidelines - Hyperkalemia Management (with ECG changes)",
                "AHA ACLS Guidelines - Tricyclic Antidepressant Overdose",
                "ISMP High Alert Medications",
                "FDA Warning - Metabolic Alkalosis, Hypernatremia, Hypokalemia"
            ]
        },

}
