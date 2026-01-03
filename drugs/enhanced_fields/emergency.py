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

}
