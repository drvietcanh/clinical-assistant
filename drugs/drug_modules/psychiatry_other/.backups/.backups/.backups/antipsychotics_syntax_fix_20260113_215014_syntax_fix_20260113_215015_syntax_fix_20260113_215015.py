"""
Antipsychotic Drugs
"""

ANTIPSYCHOTICS_DRUGS = {
    "Aripiprazole": {
        "group": "Psychiatry - Antipsychotic (Atypical, Partial Agonist)",
        "vietnamese_name": "Aripiprazole, Abilify",
        "administration": ["PO", "IM"],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (mania, depression)",
            "Rối loạn trầm cảm nặng (adjunct)",
            "Rối loạn tự kỷ (irritability)",
            "Rối loạn Tourette"
        ],
        "contraindications": [
            "Dị ứng aripiprazole",
            "Suy gan nặng",
            "Suy thận nặng (CrCl <30)"
        ],
        "dosage": {
            "adult_schizophrenia": "10-15mg x 1 lần/ngày, tăng đến 30mg/ngày nếu cần",
            "adult_bipolar": "15-30mg x 1 lần/ngày",
            "adult_depression_adjunct": "2-15mg x 1 lần/ngày",
            "adult_max": "30mg/ngày",
            "notes": "Partial agonist D2 và 5-HT1A, đối vận 5-HT2A. Ít gây tăng cân và rối loạn chuyển hóa hơn các atypical antipsychotics khác. Có dạng uống và tiêm bắp (depot)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "Kích động, mất ngủ (phổ biến khi bắt đầu)",
            "Buồn nôn",
            "Chóng mặt",
            "Nhức đầu",
            "Tăng cân (ít hơn các atypical antipsychotics khác)",
            "Rối loạn chuyển hóa (ít hơn các atypical khác)",
            "QT kéo dài (hiếm)",
            "Rối loạn vận động ngoại tháp (EPS) - ít hơn typical antipsychotics"
        ],
        "interactions": [
            "CYP2D6 inhibitors: tăng nồng độ aripiprazole",
            "CYP3A4 inhibitors: tăng nồng độ aripiprazole",
            "CYP3A4 inducers: giảm nồng độ aripiprazole",
            "Thuốc QT kéo dài: tăng nguy cơ rối loạn nhịp tim"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Atypical antipsychotic với cơ chế độc đáo: partial agonist (kích thích một phần) thụ thể dopamine D2 và serotonin 5-HT1A, đối vận (ức chế) thụ thể serotonin 5-HT2A. Khác với các atypical antipsychotics khác (đối vận D2), aripiprazole là partial agonist D2 - có thể kích thích D2 khi nồng độ dopamine thấp và ức chế khi nồng độ dopamine cao. Cơ chế này giúp aripiprazole ít gây rối loạn vận động ngoại tháp (EPS) và tăng prolactin hơn typical antipsychotics, đồng thời ít gây tăng cân và rối loạn chuyển hóa hơn các atypical antipsychotics khác. Được dùng để điều trị tâm thần phân liệt, rối loạn lưỡng cực, và trầm cảm kháng trị (adjunct).",
        "monitoring": [
            "Triệu chứng tâm thần (tâm thần phân liệt, rối loạn lưỡng cực)",
            "Kích động, mất ngủ (phổ biến khi bắt đầu)",
            "Cân nặng (ít tăng cân hơn các atypical khác)",
            "Đường huyết, lipid máu (ít rối loạn chuyển hóa hơn các atypical khác)",
            "ECG - hiếm QT kéo dài",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu rối loạn vận động ngoại tháp (EPS) - ít hơn typical antipsychotics"
        ],
        "precautions": [
            "Kích động, mất ngủ phổ biến khi bắt đầu - thường tự khỏi sau vài tuần",
            "Ít gây tăng cân và rối loạn chuyển hóa hơn các atypical antipsychotics khác - ưu điểm",
            "Thận trọng ở bệnh nhân có bệnh tim - nguy cơ QT kéo dài",
            "Tương tác với CYP2D6 và CYP3A4 inhibitors/inducers - cần điều chỉnh liều",
            "Thận trọng ở suy gan, suy thận (giảm liều)",
            "Có thể gây chóng mặt, nhức đầu - thận trọng khi lái xe"
        ],
        "pharmacokinetics": {
            "half_life": "75 giờ (rất dài, do chất chuyển hóa có hoạt tính)",
            "onset": "1-2 tuần",
            "duration": "Rất dài (do half-life rất dài, dùng 1 lần/ngày)",
            "protein_binding": "99% (rất cao)",
            "metabolism": "Gan (chuyển hóa qua CYP2D6 và CYP3A4 thành dehydro-aripiprazole - có hoạt tính)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ hành vi tự sát ở trẻ em, thanh thiếu niên, và thanh niên (18-24 tuổi) khi dùng cho rối loạn tâm thần. Nguy cơ tăng trong vài tháng đầu điều trị. Theo dõi sát các dấu hiệu tự sát, thay đổi hành vi, hoặc suy nghĩ tự sát.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa aripiprazole qua CYP2D6",
                    "effect": "Tăng nồng độ aripiprazole đáng kể, tăng tác dụng phụ",
                    "management": "Giảm liều aripiprazole 50% khi dùng với CYP2D6 inhibitors mạnh. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa aripiprazole qua CYP3A4",
                    "effect": "Tăng nồng độ aripiprazole đáng kể, tăng tác dụng phụ",
                    "management": "Giảm liều aripiprazole 50% khi dùng với CYP3A4 inhibitors mạnh. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "CYP3A4 inducers (carbamazepine, phenytoin, rifampin)",
                    "mechanism": "Cảm ứng enzyme CYP3A4, tăng chuyển hóa aripiprazole",
                    "effect": "Giảm nồng độ aripiprazole đáng kể, giảm hiệu quả",
                    "management": "Tăng liều aripiprazole gấp đôi khi dùng với CYP3A4 inducers mạnh. Khi ngừng inducer, giảm liều aripiprazole về liều ban đầu."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc QT kéo dài (amiodarone, sotalol, citalopram, escitalopram)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim",
                    "management": "Thận trọng. Theo dõi ECG. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng aripiprazole",
                "Suy gan nặng (Child-Pugh C)",
                "Suy thận nặng (CrCl <15)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, giảm liều",
                "Suy thận (CrCl 15-30) - thận trọng, có thể giảm liều",
                "Bệnh tim - tăng nguy cơ QT kéo dài",
                "Dùng với CYP2D6 hoặc CYP3A4 inhibitors - tăng nồng độ aripiprazole",
                "Dùng với CYP3A4 inducers - giảm nồng độ aripiprazole",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Aripiprazole là category C. Chứng cứ về an toàn trong thai kỳ còn hạn chế. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Aripiprazole bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, giảm liều 25-50%",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa chủ yếu qua gan)",
            "notes": "Aripiprazole chuyển hóa chủ yếu qua gan (CYP2D6, CYP3A4). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ, chóng mặt, nhức đầu",
                "Rối loạn tim mạch: QT kéo dài, rối loạn nhịp tim (hiếm)",
                "Rối loạn hô hấp: suy hô hấp (hiếm)",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục (quan trọng - nguy cơ QT kéo dài)",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Lọc máu: ít hiệu quả (protein binding 99%, chuyển hóa chủ yếu qua gan)"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, nhịp tim, ý thức, hô hấp trong ít nhất 24-48 giờ (do half-life rất dài 75 giờ)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Uống 1 lần/ngày (do half-life rất dài 75 giờ). Uống cùng thời điểm mỗi ngày để duy trì nồng độ ổn định. KHÔNG ngừng đột ngột - giảm liều dần dần."
            },
            "im": {
                "reconstitution": "Dạng depot: tiêm bắp sâu, mỗi 4 tuần",
                "injection_site": "Tiêm bắp sâu (gluteus maximus)",
                "notes": "Dạng depot: tiêm bắp sâu mỗi 4 tuần. Không tiêm IV."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Abilify (aripiprazole)",
                "UpToDate - Aripiprazole: Drug information",
                "Lexicomp - Aripiprazole"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"hepatic": "Rare (hepatitis)"},
            "qt_prolongation": True,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (QT prolongation)", "Weight", "Glucose", "Lipids"],
            "look_alike_sound_alike": ["Aripiprazole", "Risperidone"]
        },
        "guideline_tags": [
            "APA Guidelines - Schizophrenia",
            "APA Guidelines - Bipolar Disorder",
            "NICE Guidelines - Psychosis and Schizophrenia",
            "FDA Black Box Warning - Suicidal Behavior in Children/Adolescents"
        ],
        "last_updated": "2025-02-18",
    },
    
    "Chlorpromazine": {
        "group": "Psychiatry - Antipsychotic (Typical, Phenothiazine)",
        "vietnamese_name": "Chlorpromazine, Thorazine",
        "administration": ["PO", "IM", "IV"],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (mania)",
            "Loạn thần cấp",
            "Nôn mửa nặng",
            "Hội chứng Tourette",
            "Động kinh (hiếm)"
        ],
        "contraindications": [
            "Dị ứng chlorpromazine hoặc phenothiazine",
            "Coma do CNS depressants",
            "Suy gan nặng",
            "Bệnh tủy xương (giảm bạch cầu, giảm tiểu cầu)"
        ],
        "dosage": {
            "adult_psychosis_po": "25-100mg x 3-4 lần/ngày, tăng đến 400-800mg/ngày",
            "adult_psychosis_im": "25-50mg IM mỗi 6-8 giờ",
            "adult_nausea": "10-25mg PO/IM mỗi 4-6 giờ",
            "adult_max": "1000mg/ngày",
            "notes": "Typical antipsychotic đầu tiên. Tác dụng an thần mạnh. Nhiều tác dụng phụ: EPS, tăng prolactin, hạ huyết áp, an thần. Ít dùng hơn do tác dụng phụ nhiều."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "Rối loạn vận động ngoại tháp (EPS) - phổ biến (parkinsonism, dystonia, akathisia, tardive dyskinesia)",
            "Tăng prolactin (phổ biến)",
            "Hạ huyết áp tư thế (orthostatic hypotension) - phổ biến",
            "Buồn ngủ, an thần mạnh",
            "Khô miệng, mờ mắt, táo bón (anticholinergic)",
            "QT kéo dài (hiếm, nhưng quan trọng)",
            "Giảm bạch cầu (hiếm, nhưng nguy hiểm)",
            "Rối loạn gan (hiếm)",
            "Rối loạn da (nhạy cảm ánh sáng)"
        ],
        "interactions": [
            "CNS depressants: tăng tác dụng an thần",
            "Anticholinergics: tăng tác dụng phụ anticholinergic",
            "Thuốc QT kéo dài: tăng nguy cơ rối loạn nhịp tim",
            "CYP2D6 inhibitors: tăng nồng độ chlorpromazine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Typical antipsychotic (phenothiazine), đối vận mạnh thụ thể dopamine D2. Gắn chặt với D2 (tight binding), gây ức chế dopamine mạnh, dẫn đến nguy cơ cao rối loạn vận động ngoại tháp (EPS) và tăng prolactin. Chlorpromazine cũng đối kháng thụ thể alpha-1 adrenergic (gây hạ huyết áp), histamine H1 (gây an thần), và muscarinic (gây khô miệng, mờ mắt). Tác dụng: điều trị tâm thần phân liệt, rối loạn lưỡng cực (mania), loạn thần cấp, và nôn mửa nặng. Có dạng uống (PO), tiêm bắp (IM), và tiêm tĩnh mạch (IV). Tác dụng phụ nhiều: EPS, tăng prolactin, hạ huyết áp, an thần mạnh. Ít dùng hơn do tác dụng phụ nhiều so với atypical antipsychotics.",
        "monitoring": [
            "Triệu chứng tâm thần (tâm thần phân liệt, rối loạn lưỡng cực)",
            "Rối loạn vận động ngoại tháp (EPS): parkinsonism, dystonia, akathisia, tardive dyskinesia",
            "Huyết áp tư thế (orthostatic hypotension) - phổ biến",
            "Công thức máu (CBC) - hiếm giảm bạch cầu, nhưng nguy hiểm",
            "ECG - hiếm QT kéo dài",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Prolactin (nếu có triệu chứng tăng prolactin)",
            "Dấu hiệu nhiễm trùng (giảm bạch cầu)"
        ],
        "precautions": [
            "Nguy cơ rối loạn vận động ngoại tháp (EPS) cao - theo dõi sát, có thể cần dùng anticholinergics",
            "Nguy cơ hạ huyết áp tư thế - đứng dậy chậm, đặc biệt khi bắt đầu",
            "Tác dụng an thần mạnh - thận trọng khi lái xe, vận hành máy móc",
            "Nguy cơ giảm bạch cầu (hiếm, nhưng nguy hiểm) - theo dõi công thức máu",
            "Nguy cơ QT kéo dài - theo dõi ECG, tránh dùng với thuốc QT kéo dài khác",
            "Nhạy cảm ánh sáng - tránh ánh nắng trực tiếp, dùng kem chống nắng",
            "Thận trọng ở suy gan, suy thận (giảm liều)",
            "Tương tác với nhiều thuốc - thận trọng"
        ],
        "pharmacokinetics": {
            "half_life": "30 giờ (dài)",
            "onset": "30-60 phút (PO), 15-30 phút (IM), ngay lập tức (IV)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "90-95%",
            "metabolism": "Gan (chuyển hóa qua CYP2D6, CYP1A2, CYP3A4)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng IV: bảo quản ở nhiệt độ phòng, tránh đông lạnh.",
        "black_box_warnings": "Nguy cơ giảm bạch cầu (agranulocytosis) - rất hiếm nhưng có thể gây tử vong. Theo dõi công thức máu. Ngừng ngay nếu có dấu hiệu nhiễm trùng (sốt, đau họng, loét miệng). Nguy cơ QT kéo dài và rối loạn nhịp tim.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CNS depressants (benzodiazepine, rượu, opioid)",
                    "mechanism": "Tác dụng hiệp đồng ức chế thần kinh trung ương",
                    "effect": "Tăng tác dụng an thần, tăng nguy cơ suy hô hấp",
                    "management": "Thận trọng. Giảm liều một trong hai thuốc. Tránh rượu."
                },
                {
                    "drug": "Thuốc QT kéo dài (amiodarone, sotalol, citalopram, escitalopram)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim, torsades de pointes",
                    "management": "Thận trọng. Theo dõi ECG. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa chlorpromazine qua CYP2D6",
                    "effect": "Tăng nồng độ chlorpromazine, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều chlorpromazine. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "Anticholinergics (atropine, benztropine)",
                    "mechanism": "Tác dụng hiệp đồng anticholinergic",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng, mờ mắt, táo bón, bí tiểu)",
                    "management": "Thận trọng. Có thể dùng để điều trị EPS, nhưng theo dõi tác dụng phụ anticholinergic."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng chlorpromazine hoặc phenothiazine",
                "Coma do CNS depressants",
                "Suy gan nặng (Child-Pugh C)",
                "Bệnh tủy xương (giảm bạch cầu, giảm tiểu cầu)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, giảm liều",
                "Suy thận nặng - thận trọng",
                "Bệnh tim - tăng nguy cơ QT kéo dài",
                "Bệnh mạch máu ngoại biên - có thể làm nặng",
                "Động kinh - có thể làm tăng nguy cơ co giật",
                "Mang thai (category C) - thận trọng, chỉ dùng nếu lợi ích > nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chlorpromazine là category C. Có thể dùng khi cần thiết. Có thể gây nhịp tim chậm thai nhi, hạ huyết áp. Theo dõi sát thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Chlorpromazine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém).",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều, nhưng theo dõi chặt chẽ chức năng gan",
            "moderate": "Thận trọng, giảm liều 25-50%",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa chủ yếu qua gan)",
            "notes": "Chlorpromazine chuyển hóa chủ yếu qua gan (CYP2D6, CYP1A2, CYP3A4). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ sâu, hôn mê, co giật",
                "Rối loạn tim mạch: hạ huyết áp nặng, QT kéo dài, rối loạn nhịp tim",
                "Rối loạn hô hấp: suy hô hấp",
                "Rối loạn vận động: EPS nặng, dystonia",
                "Rối loạn tiêu hóa: khô miệng, táo bón, bí tiểu"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp ngay lập tức (quan trọng)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục (quan trọng - nguy cơ QT kéo dài, rối loạn nhịp tim)",
                "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, nếu cần: dopamine, norepinephrine",
                "Điều trị rối loạn nhịp tim nếu có",
                "Điều trị EPS nếu có: Anticholinergics (benztropine, diphenhydramine)",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Lọc máu: ít hiệu quả (protein binding 90-95%, chuyển hóa chủ yếu qua gan)"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, nhịp tim, ý thức, hô hấp trong ít nhất 24-48 giờ (do half-life dài 30 giờ)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày và buồn nôn.",
                "timing": "Chia 3-4 lần/ngày. Uống cùng thời điểm mỗi ngày. KHÔNG ngừng đột ngột - giảm liều dần dần."
            },
            "iv": {
                "reconstitution": "Pha trong 0.9% NaCl hoặc D5W. Nồng độ pha: 1mg/ml. Pha 25mg trong 25ml = 1mg/ml.",
                "infusion_rate": "Truyền IV chậm trong 30-60 phút. Tốc độ: 25ml/30 phút = ~0.83ml/phút. KHÔNG truyền nhanh hơn.",
                "compatibility": ["0.9% NaCl", "D5W"],
                "incompatibility": [],
                "notes": "QUAN TRỌNG: 1) Truyền IV chậm trong 30-60 phút, không truyền nhanh hơn (nguy cơ hạ huyết áp nặng), 2) Theo dõi huyết áp sát, 3) Theo dõi ECG (nguy cơ QT kéo dài)."
            },
            "im": {
                "reconstitution": "Dùng trực tiếp từ lọ, không cần pha.",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis).",
                "notes": "Tiêm sâu vào cơ. Có thể gây đau tại chỗ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Thorazine (chlorpromazine)",
                "UpToDate - Chlorpromazine: Drug information",
                "Lexicomp - Chlorpromazine"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"hematologic": "Rare but serious (agranulocytosis)", "hepatic": "Rare", "cardiovascular": "QT prolongation"},
            "qt_prolongation": True,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC (agranulocytosis)", "ECG (QT prolongation)", "Liver function", "Prolactin"],
            "look_alike_sound_alike": ["Chlorpromazine", "Chlorpropamide"]
        },
        "guideline_tags": [
            "APA Guidelines - Schizophrenia",
            "FDA Black Box Warning - Agranulocytosis",
            "FDA Black Box Warning - QT Prolongation",
            "NICE Guidelines - Psychosis and Schizophrenia"
        ],
        "last_updated": "2025-02-18",
    },

    "Clozapine": {
        "group": "Psychiatry - Antipsychotic (Atypical)",
        "vietnamese_name": "Clozapine, Clozaril",
        "administration": ["PO"],
        "indications": [
            "Tâm thần phân liệt kháng trị",
            "Giảm nguy cơ hành vi tự sát ở tâm thần phân liệt",
            "Parkinson's disease psychosis (off-label)"
        ],
        "contraindications": [
            "Giảm bạch cầu trước đó do clozapine",
            "Bệnh tủy xương",
            "Dị ứng clozapine",
            "Suy gan nặng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_initial": "12.5-25mg x 1-2 lần/ngày, tăng dần",
            "adult_maintenance": "300-450mg/ngày (chia 2-3 lần)",
            "adult_max": "900mg/ngày",
            "notes": "THUỐC ĐẶC BIỆT: Cần theo dõi bạch cầu hàng tuần (giảm bạch cầu có thể tử vong). Chỉ dùng cho tâm thần phân liệt kháng trị."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "Giảm bạch cầu (NGUY HIỂM - có thể tử vong, cần theo dõi hàng tuần)",
            "Tăng cân (phổ biến, nặng)",
            "Tăng lipid máu",
            "Tăng đường huyết (nguy cơ đái tháo đường)",
            "Buồn ngủ",
            "Chóng mặt",
            "Tăng tiết nước bọt (sialorrhea)",
            "Táo bón (có thể nặng, nguy hiểm)",
            "Hạ huyết áp tư thế",
            "Co giật (nguy cơ tăng theo liều)",
            "Viêm cơ tim (hiếm nhưng nguy hiểm)"
        ],
        "interactions": [
            "CYP1A2 inhibitors: tăng nồng độ clozapine",
            "CYP1A2 inducers: giảm nồng độ clozapine",
            "Benzodiazepine: tăng nguy cơ suy hô hấp",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Clozapine là atypical antipsychotic với cơ chế phức tạp: đối kháng thụ thể dopamine D1, D2, D4, serotonin 5-HT2A, 5-HT2C, 5-HT3, 5-HT6, 5-HT7, histamine H1, muscarinic M1-M5, và alpha-1, alpha-2 adrenergic. Đặc điểm: hiệu quả nhất với tâm thần phân liệt kháng trị, nhưng có nguy cơ giảm bạch cầu nghiêm trọng (cần theo dõi hàng tuần). Ít gây rối loạn vận động ngoại tháp (EPS) hơn các antipsychotic khác. Tác dụng phụ: giảm bạch cầu (nguy hiểm), tăng cân nặng, tăng lipid máu, tăng đường huyết, táo bón nặng, co giật.",
        "monitoring": [
            "BẠCH CẦU HÀNG TUẦN (QUAN TRỌNG NHẤT - giảm bạch cầu có thể tử vong)",
            "Triệu chứng tâm thần",
            "Cân nặng (tăng cân phổ biến, nặng)",
            "Lipid máu (cholesterol, triglyceride)",
            "Đường huyết (HbA1c nếu cần)",
            "Táo bón (có thể nặng, nguy hiểm)",
            "Dấu hiệu co giật (nguy cơ tăng theo liều)",
            "ECG (hiếm QT prolongation)",
            "Dấu hiệu viêm cơ tim (hiếm nhưng nguy hiểm)"
        ],
        "precautions": [
            "GIẢM BẠCH CẦU - cần theo dõi bạch cầu hàng tuần (có thể tử vong)",
            "Chỉ dùng cho tâm thần phân liệt kháng trị",
            "Ngừng ngay nếu bạch cầu <3000/mm3 hoặc giảm >50%",
            "Tăng cân nặng - theo dõi cân nặng định kỳ",
            "Táo bón có thể nặng, nguy hiểm - theo dõi sát",
            "Nguy cơ co giật tăng theo liều (>600mg/ngày)",
            "Thận trọng với CYP1A2 inhibitors/inducers",
            "Tránh dùng với benzodiazepine (tăng nguy cơ suy hô hấp)"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ",
            "onset": "1-2 tuần",
            "duration": "24 giờ",
            "protein_binding": "95%",
            "clearance": "Gan: chuyển hóa qua CYP1A2, CYP3A4. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "GIẢM BẠCH CẦU NGHIÊM TRỌNG - có thể tử vong. Cần theo dõi bạch cầu hàng tuần. Ngừng ngay nếu bạch cầu <3000/mm3 hoặc giảm >50%. Nguy cơ co giật. Nguy cơ viêm cơ tim. Nguy cơ suy hô hấp khi dùng với benzodiazepine.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP1A2 inhibitors (fluvoxamine, ciprofloxacin)",
                    "mechanism": "Ức chế chuyển hóa clozapine",
                    "effect": "Tăng nồng độ clozapine đáng kể, tăng tác dụng phụ",
                    "management": "Giảm liều clozapine 50%. Theo dõi sát."
                },
                {
                    "drug": "Benzodiazepines (lorazepam, clonazepam)",
                    "mechanism": "Tác dụng hiệp đồng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ suy hô hấp, hôn mê, tử vong",
                    "management": "TRÁNH dùng cùng. Nếu cần, dùng liều thấp và theo dõi sát."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP1A2 inducers (carbamazepine, phenytoin, smoking)",
                    "mechanism": "Tăng chuyển hóa clozapine",
                    "effect": "Giảm nồng độ clozapine, giảm hiệu quả",
                    "management": "Tăng liều clozapine. Lưu ý: ngừng hút thuốc có thể tăng nồng độ clozapine."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Giảm bạch cầu trước đó do clozapine",
                "Bệnh tủy xương",
                "Dị ứng clozapine",
                "Suy gan nặng",
                "Suy thận nặng"
            ],
            "tương_đối": [
                "Bệnh tim - tăng nguy cơ viêm cơ tim",
                "Tiền sử co giật - tăng nguy cơ",
                "Táo bón - có thể làm nặng",
                "Dùng với CYP1A2 inhibitors - giảm liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Có thể dùng khi cần thiết.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa qua gan)",
            "notes": "Chuyển hóa qua gan (CYP1A2, CYP3A4). Suy gan làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ sâu, hôn mê",
                "Suy hô hấp (đặc biệt nếu dùng với benzodiazepine)",
                "Hạ huyết áp",
                "Co giật",
                "Rối loạn nhịp tim",
                "Giảm bạch cầu (có thể chậm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ hô hấp ngay lập tức (quan trọng nhất)",
                "Theo dõi ECG liên tục",
                "Điều trị co giật: Benzodiazepines",
                "Điều trị hạ huyết áp: Truyền dịch, vận mạch",
                "Theo dõi bạch cầu (có thể giảm chậm)",
                "Lọc máu KHÔNG hiệu quả do protein binding cao"
            ],
            "monitoring": "Theo dõi liên tục hô hấp, ECG, huyết áp, ý thức, bạch cầu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Dùng 2-3 lần/ngày. Khởi đầu 12.5-25mg/ngày, tăng dần. QUAN TRỌNG: Cần theo dõi bạch cầu hàng tuần. KHÔNG ngừng đột ngột."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Clozaril (clozapine)",
                "UpToDate - Clozapine: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"hematologic": "Black Box Warning (agranulocytosis - fatal)", "cardiovascular": "Rare (myocarditis)", "neurological": "Seizures (dose-dependent)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["CBC weekly (agranulocytosis - Black Box Warning)", "Weight", "Glucose", "Lipids", "ECG (myocarditis)", "Constipation"],
            "look_alike_sound_alike": ["Clozapine", "Clonazepam", "Olanzapine"]
        },
        "guideline_tags": [
            "APA Guidelines - Treatment-Resistant Schizophrenia",
            "FDA Black Box Warning - Agranulocytosis",
            "FDA Black Box Warning - Myocarditis",
            "FDA Black Box Warning - Seizures",
            "NICE Guidelines - Psychosis and Schizophrenia"
        ],
        "last_updated": "2025-02-18",
    },
    
    "Fluphenazine": {
        "group": "Psychiatry - Antipsychotic (Typical)",
        "vietnamese_name": "Fluphenazine, Prolixin",
        "administration": ["PO", "IM", "SC"],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn tâm thần khác"
        ],
        "contraindications": [
            "Dị ứng phenothiazine",
            "Coma do CNS depressants",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_po": "2.5-10mg x 2-4 lần/ngày, tăng đến 20mg/ngày",
            "adult_im": "2.5-10mg mỗi 6-8 giờ",
            "adult_depot": "12.5-25mg IM mỗi 2-4 tuần",
            "adult_max": "40mg/ngày (PO)",
            "notes": "Typical antipsychotic, nguy cơ EPS cao. Có dạng depot (long-acting)."
        },
        "side_effects": [
            "Rối loạn vận động ngoại tháp (EPS) - phổ biến",
            "Dystonia",
            "Parkinsonism",
            "Akathisia",
            "Tardive dyskinesia",
            "Hạ huyết áp",
            "Sedation",
            "Tăng prolactin"
        ],
        "interactions": [
            "CNS depressants: tăng tác dụng an thần",
            "Anticholinergics: giảm EPS nhưng tăng tác dụng phụ anticholinergic",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp"
        ],
        ',
        "pregnancy": "C",
        ',
        "mechanism_of_action": "Fluphenazine là typical antipsychotic (phenothiazine), đối kháng mạnh thụ thể dopamine D2 ở não. Ức chế dopaminergic pathway dẫn đến giảm triệu chứng tâm thần nhưng tăng nguy cơ rối loạn vận động ngoại tháp (EPS). Có dạng depot (long-acting) cho phép tiêm mỗi 2-4 tuần, cải thiện compliance. Nguy cơ EPS cao hơn atypical antipsychotics.",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng tâm thần",
            "EPS: dystonia, parkinsonism, akathisia, tardive dyskinesia",
            "Huyết áp - hạ huyết áp có thể xảy ra",
            "ECG - QT prolongation",
            "Prolactin - tăng prolactin có thể gây vô kinh, galactorrhea"
        ],
        "precautions": [
            "Nguy cơ EPS cao - cần theo dõi chặt chẽ",
            "Tardive dyskinesia - có thể không hồi phục, cần đánh giá định kỳ",
            "Hạ huyết áp - đặc biệt khi bắt đầu điều trị",
            "Dạng depot - tiêm sâu vào cơ, không tiêm vào mạch máu",
            "Không ngừng đột ngột - giảm liều dần dần"
        ],
        "pharmacokinetics": {
            "half_life": "15-30 giờ (PO), 6.8-9.6 ngày (depot)",
            "onset": "1-2 giờ (PO), 24-72 giờ (depot)",
            "duration": "6-8 giờ (PO), 2-4 tuần (depot)",
            "protein_binding": ">90%",
            "clearance": "Gan: chuyển hóa qua CYP2D6. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dạng depot: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng.",
        "black_box_warnings": "Tardive dyskinesia có thể không hồi phục. Nguy cơ tăng ở người cao tuổi, phụ nữ, dùng lâu dài.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "QT prolonging drugs",
                    "mechanism": "Cả hai đều kéo dài QT",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim",
                    "management": "Tránh dùng chung nếu có thể. Theo dõi ECG."
                }
            ],
            "moderate": [
                {
                    "drug": "CNS depressants",
                    "mechanism": "Tác dụng hiệp đồng ức chế CNS",
                    "effect": "Tăng tác dụng an thần",
                    "management": "Thận trọng, giảm liều nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fluphenazine hoặc phenothiazine",
                "Coma do CNS depressants",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Bệnh tim - tăng nguy cơ QT prolongation",
                "Động kinh - có thể làm tăng nguy cơ co giật",
                "Mang thai (category C) - thận trọng"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng fluphenazine hoặc phenothiazine",
                "Coma do CNS depressants",
                "Suy gan nặng"
            ],
            "tương_đối": [
                "Bệnh tim - tăng nguy cơ QT prolongation",
                "Động kinh - có thể làm tăng nguy cơ co giật",
                "Mang thai (category C) - thận trọng",
                "Suy thận nặng (CrCl <30) - thận trọng, giảm liều"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Fluphenazine không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Fluphenazine thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy. Giảm liều và theo dõi chặt chẽ ở suy thận nặng."
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Thận trọng.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Chuyển hóa qua gan (CYP2D6). Suy gan nặng là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ sâu, hôn mê",
                "Hạ huyết áp nặng",
                "QT prolongation, rối loạn nhịp tim",
                "EPS nặng",
                "Suy hô hấp"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ hô hấp ngay lập tức",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục",
                "Điều trị hạ huyết áp",
                "Điều trị EPS nếu có"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, ý thức, hô hấp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "Chia 2-4 lần/ngày. Không ngừng đột ngột."
            },
            "im": {
                "reconstitution": "Dùng trực tiếp từ lọ.",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus).",
                "notes": "Tiêm sâu vào cơ. Dạng depot: tiêm mỗi 2-4 tuần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Prolixin (Fluphenazine)",
                "UpToDate - Fluphenazine: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "neurological": "Black Box Warning - Tardive dyskinesia (may be irreversible, increased risk in elderly, women, long-term use) - CRITICAL",
                "cardiovascular": "QT prolongation, arrhythmias",
                "endocrine": "Hyperprolactinemia (amenorrhea, galactorrhea)"
            },
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - Tardive dyskinesia signs (involuntary movements, especially face/tongue) - CRITICAL, assess periodically (AIMS scale)",
                "EPS signs (dystonia, parkinsonism, akathisia) - common",
                "ECG (QT prolongation risk)",
                "Blood pressure (hypotension, especially at initiation)",
                "Prolactin levels (hyperprolactinemia - amenorrhea, galactorrhea)",
                "CYP2D6 interactions (metabolized via CYP2D6)"
            ],
            "look_alike_sound_alike": ["Fluphenazine", "Prolixin", "Fluphenazine decanoate"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Tardive Dyskinesia",
            "APA Guidelines - Schizophrenia Treatment",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Haloperidol":     {
        "group": "Psychiatry - Antipsychotic (Typical)",
        "vietnamese_name": "Haloperidol, Haldol",
        "administration": [
            "PO",
            "IM",
            "IV"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (mania)",
            "Loạn thần cấp",
            "Delirium (ICU)",
            "Tourette syndrome",
            "Chứng nôn mửa nặng (refractory)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng haloperidol hoặc các thành phần khác",
                "Parkinson's disease - làm nặng triệu chứng",
                "Coma - ức chế hệ thần kinh trung ương nặng",
                "Ức chế hệ thần kinh trung ương nặng"
    ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ QT prolongation, hạ huyết áp",
                "QT prolongation - tăng nguy cơ rối loạn nhịp tim",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP2D6, CYP3A4 inhibitors - giảm liều haloperidol",
                "Dùng với CYP2D6, CYP3A4 inducers - tăng liều haloperidol",
                "Dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ, EPS, hạ huyết áp"
    ],
        },
        "dosage": {
            "adult_schizophrenia_po": "0.5-5mg x 2-3 lần/ngày, tăng đến 15-20mg/ngày (tối đa 100mg/ngày)",
            "adult_schizophrenia_im": "2-5mg IM, lặp mỗi 4-8 giờ nếu cần (tối đa 20mg/ngày)",
            "adult_delirium": "0.5-2mg PO/IM mỗi 4-6 giờ",
            "adult_max": "100mg/ngày PO, 20mg/ngày IM",
            "notes": """Typical antipsychotic, nguy cơ cao rối loạn vận động ngoại tháp (EPS). Dạng decanoate (depot): 50-200mg IM mỗi 4 tuần.""",
        },
        "side_effects": [
            "Rối loạn vận động ngoại tháp (EPS) - phổ biến: dystonia, akathisia, parkinsonism, tardive dyskinesia",
            "Tăng prolactin (phổ biến)",
            "QT prolongation (nguy hiểm)",
            "Neuroleptic malignant syndrome (NMS) - hiếm nhưng nguy hiểm",
            "Buồn ngủ, chóng mặt",
            "Khô miệng",
            "Táo bón",
            "Hạ huyết áp tư thế"
    ],
        "interactions": [
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "CYP2D6 inhibitors: tăng nồng độ haloperidol",
            "CYP3A4 inhibitors: tăng nồng độ haloperidol",
            "Anticholinergics: giảm EPS nhưng tăng tác dụng phụ anticholinergic",
            "Alcohol: tăng tác dụng ức chế hệ thần kinh trung ương"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Haloperidol là thuốc chống loạn thần điển hình (typical antipsychotic), đối kháng mạnh thụ thể dopamine D2. Khác với atypical antipsychotics, haloperidol gắn chặt với D2 (tight binding), gây ức chế dopamine mạnh, dẫn đến nguy cơ cao rối loạn vận động ngoại tháp (EPS) và tăng prolactin. Haloperidol cũng đối kháng thụ thể alpha-1 adrenergic (gây hạ huyết áp) và histamine H1 (gây buồn ngủ). Tác dụng: điều trị tâm thần phân liệt, rối loạn lưỡng cực (mania), loạn thần cấp, delirium (ICU), và Tourette syndrome. Có dạng uống (PO), tiêm bắp (IM), tiêm tĩnh mạch (IV), và dạng depot (decanoate). Tác dụng phụ: rối loạn vận động ngoại tháp (EPS) - phổ biến, tăng prolactin, QT prolongation, neuroleptic malignant syndrome (NMS) - hiếm nhưng nguy hiểm.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng tâm thần, ổn định tâm trạng (đánh giá sau 2-4 tuần)",
            "Rối loạn vận động ngoại tháp (EPS) - phổ biến, theo dõi: dystonia, akathisia, parkinsonism, tardive dyskinesia",
            "ECG - QT prolongation (nguy hiểm), đặc biệt ở liều cao",
            "Prolactin - tăng prolactin phổ biến (gây vô kinh, tiết sữa)",
            "Dấu hiệu neuroleptic malignant syndrome (NMS): sốt, cứng cơ, thay đổi ý thức, tăng CK, tăng nhịp tim",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Tương tác với CYP2D6, CYP3A4 inhibitors/inducers (ảnh hưởng nồng độ haloperidol)"
    ],
        "precautions": [
            "Rối loạn vận động ngoại tháp (EPS) - phổ biến, đặc biệt ở liều cao, có thể dùng anticholinergics (benztropine, trihexyphenidyl) để điều trị",
            "QT prolongation - nguy hiểm, đặc biệt ở liều cao, tránh dùng với thuốc kéo dài QT khác, theo dõi ECG",
            "Neuroleptic malignant syndrome (NMS) - hiếm nhưng nguy hiểm, ngừng ngay nếu nghi ngờ, điều trị hỗ trợ",
            "Tăng prolactin - phổ biến, gây vô kinh, tiết sữa, giảm ham muốn tình dục",
            "Tardive dyskinesia - rối loạn vận động muộn, có thể không hồi phục, giảm liều hoặc ngừng nếu có thể",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Thận trọng khi dùng với CYP2D6, CYP3A4 inhibitors - tăng nồng độ haloperidol, giảm liều",
            "Thận trọng khi dùng với CYP2D6, CYP3A4 inducers - giảm nồng độ haloperidol, có thể cần tăng liều",
            "Thận trọng khi dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
            "Tránh rượu - tăng tác dụng ức chế hệ thần kinh trung ương",
            "Dạng depot (decanoate) - tiêm bắp mỗi 4 tuần, thuận tiện cho bệnh nhân không tuân thủ điều trị",
            "Không ngừng đột ngột (có thể làm tăng triệu chứng)"
    ],
        "pharmacokinetics": {
            "half_life": "12-38 giờ (PO), 21 giờ (IM), 14-26 giờ (decanoate depot)",
            "onset": "30-60 phút (IM), vài ngày đến vài tuần (tác dụng chống loạn thần)",
            "duration": "12-24 giờ (PO), 4-8 giờ (IM), 4 tuần (decanoate depot)",
            "protein_binding": "92%",
            "clearance": """Gan: chuyển hóa qua CYP2D6 (chính), CYP3A4 (phụ). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều khi dùng với CYP2D6, CYP3A4 inhibitors/inducers.""",
        },
        "storage": """Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng tiêm: bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Dạng depot (decanoate): bảo quản ở nhiệt độ phòng, tránh ánh sáng.""",
        "black_box_warnings": """Nguy cơ tử vong tăng ở bệnh nhân lớn tuổi với rối loạn tâm thần do sa sút trí tuệ (dementia-related psychosis) - không được dùng cho chỉ định này. Nguy cơ QT prolongation, có thể gây rối loạn nhịp tim (torsades de pointes). Nguy cơ neuroleptic malignant syndrome (NMS). Nguy cơ rối loạn vận động ngoại tháp (EPS), đặc biệt tardive dyskinesia (có thể không hồi phục).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "QT prolonging drugs (Amiodarone, Sotalol, Citalopram, Escitalopram, Quetiapine)",
                    "mechanism": "Cả hai đều kéo dài QT, tăng nguy cơ rối loạn nhịp tim",
                    "effect": "QT prolongation, rối loạn nhịp tim (torsades de pointes)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi ECG. Giảm liều một trong hai thuốc.",
                },
    {
                    "drug": "CYP2D6 inhibitors (Paroxetine, Fluoxetine, Bupropion)",
                    "mechanism": "Ức chế chuyển hóa haloperidol qua CYP2D6, tăng nồng độ haloperidol",
                    "effect": "Tăng nồng độ haloperidol, tăng tác dụng phụ (EPS, QT prolongation)",
                    "management": "Giảm liều haloperidol 50% khi dùng với CYP2D6 inhibitors. Theo dõi tác dụng phụ chặt chẽ.",
                },
    {
                    "drug": "CYP3A4 inhibitors (Ketoconazole, Itraconazole, Erythromycin, Clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa haloperidol qua CYP3A4, tăng nồng độ haloperidol",
                    "effect": "Tăng nồng độ haloperidol, tăng tác dụng phụ",
                    "management": "Giảm liều haloperidol 25-50% khi dùng với CYP3A4 inhibitors. Theo dõi tác dụng phụ chặt chẽ.",
                }
                ],
            "moderate": [
    {
                    "drug": "Anticholinergics (Benztropine, Trihexyphenidyl)",
                    "mechanism": "Điều trị EPS nhưng tăng tác dụng phụ anticholinergic",
                    "effect": "Tăng khô miệng, táo bón, bí tiểu, lú lẫn (đặc biệt ở người cao tuổi)",
                    "management": "Dùng liều thấp nhất có hiệu quả. Theo dõi tác dụng phụ anticholinergic.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp",
                    "management": "Tránh hoặc giảm rượu. Cảnh báo bệnh nhân.",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng haloperidol hoặc các thành phần khác",
                "Parkinson's disease - làm nặng triệu chứng",
                "Coma - ức chế hệ thần kinh trung ương nặng",
                "Ức chế hệ thần kinh trung ương nặng"
    ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ QT prolongation, hạ huyết áp",
                "QT prolongation - tăng nguy cơ rối loạn nhịp tim",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP2D6, CYP3A4 inhibitors - giảm liều haloperidol",
                "Dùng với CYP2D6, CYP3A4 inducers - tăng liều haloperidol",
                "Dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ, EPS, hạ huyết áp"
    ],
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Haloperidol không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": """Haloperidol thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy. Giảm liều và theo dõi chặt chẽ ở suy thận nặng.""",
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở) nếu mẹ dùng haloperidol trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.""",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": """Haloperidol bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.""",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém).",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": """Haloperidol chuyển hóa ở gan qua CYP2D6, CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.""",
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, hôn mê, co giật",
                "Rối loạn vận động: dystonia nặng, akathisia, parkinsonism",
                "Rối loạn tim mạch: QT prolongation, rối loạn nhịp tim (torsades de pointes), hạ huyết áp",
                "Rối loạn hô hấp: suy hô hấp",
                "Neuroleptic malignant syndrome (NMS): sốt, cứng cơ, thay đổi ý thức, tăng CK",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Benztropine hoặc diphenhydramine cho EPS.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Xử trí EPS: Benztropine 1-2mg IM/IV hoặc diphenhydramine 25-50mg IM/IV",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ (QT prolongation)",
                "Xử trí QT prolongation: Magnesium sulfate (2g IV), isoproterenol nếu cần",
                "Xử trí torsades de pointes: Magnesium sulfate, overdrive pacing",
                "Xử trí NMS: Ngừng haloperidol ngay, điều trị hỗ trợ, dantrolene nếu cần",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi ít nhất 24-48 giờ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, điện tâm đồ (QT interval), huyết áp, CK (nếu nghi ngờ NMS)",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": """Chia 2-3 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm để giảm tác dụng phụ (đặc biệt EPS). Không ngừng đột ngột (có thể làm tăng triệu chứng).""",
            },
            "im": {
                "reconstitution": "Không cần pha loãng. Lắc kỹ trước khi dùng.",
                "infusion_rate": "Tiêm bắp sâu vào cơ lớn (gluteal, deltoid). Tránh tiêm vào mạch máu.",
                "compatibility": [],
                "incompatibility": [],
                "notes": """Dạng IM: dùng cho loạn thần cấp, delirium. Dạng depot (decanoate): tiêm bắp mỗi 4 tuần, thuận tiện cho bệnh nhân không tuân thủ điều trị.""",
            },
            "iv": {
                "reconstitution": "Pha loãng trong NS hoặc D5W. Nồng độ: 0.2-5mg/mL.",
                "infusion_rate": "Tiêm tĩnh mạch chậm (không quá 5mg/phút). Hoặc truyền tĩnh mạch liên tục.",
                "compatibility": [
                    "NS",
                    "D5W"
    ],
                "incompatibility": [],
                "notes": "Dạng IV: dùng cho loạn thần cấp, delirium (ICU). Theo dõi QT prolongation chặt chẽ.",
            },
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Haloperidol",
                "UpToDate - Haloperidol: Drug information",
                "FDA - Haldol (haloperidol) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
    ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"cardiovascular": "QT prolongation - Black Box Warning", "neurological": "NMS - rare but fatal", "neurological_extrapyramidal": "EPS, tardive dyskinesia"},
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (QT prolongation - Black Box Warning)", "EPS signs", "NMS signs", "Prolactin"],
            "look_alike_sound_alike": ["Haloperidol", "Halothane"]
        },
        "guideline_tags": [
            "APA Guidelines - Schizophrenia",
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "FDA Black Box Warning - QT Prolongation",
            "FDA Black Box Warning - Neuroleptic Malignant Syndrome",
            "FDA Black Box Warning - Tardive Dyskinesia",
            "NICE Guidelines - Psychosis and Schizophrenia"
        ],
        "last_updated": "2025-02-18",
    },
    "Lurasidone": {
        "group": "Psychiatry - Antipsychotic (Atypical)",
        "vietnamese_name": "Lurasidone, Latuda",
        "administration": ["PO"],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (depression)",
            "Trầm cảm kháng trị (adjunct)"
        ],
        "contraindications": [
            "Dị ứng",
            "QT prolongation nặng"
        ],
        "dosage": {
            "adult_schizophrenia": "40-80mg x 1 lần/ngày (tối đa 160mg/ngày)",
            "adult_bipolar_depression": "20-60mg x 1 lần/ngày",
            "adult_max": "160mg/ngày",
            "notes": "Uống với thức ăn (≥350 calo) để tăng hấp thu. Atypical antipsychotic, ít tăng cân hơn các atypical khác."
        },
        "side_effects": [
            "Buồn ngủ",
            "Buồn nôn",
            "Chóng mặt",
            "Akathisia",
            "QT prolongation (hiếm)",
            "Tăng prolactin (nhẹ)",
            "Ít tăng cân hơn các atypical khác"
        ],
        "interactions": [
            "CYP3A4 inhibitors: tăng nồng độ lurasidone",
            "CYP3A4 inducers: giảm nồng độ lurasidone",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Lurasidone là atypical antipsychotic, đối kháng thụ thể dopamine D2 và serotonin 5-HT2A. Khác với các atypical khác, lurasidone ít gây tăng cân và tăng lipid máu. Có tác dụng chống trầm cảm, được dùng cho rối loạn lưỡng cực depression. Ưu điểm: ít tăng cân, ít tác dụng phụ chuyển hóa. Phải uống với thức ăn để tăng hấp thu.",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng tâm thần, cải thiện trầm cảm",
            "ECG - QT prolongation (hiếm)",
            "Cân nặng - ít tăng cân hơn các atypical khác",
            "Prolactin - tăng nhẹ",
            "Akathisia - tác dụng phụ phổ biến"
        ],
        "precautions": [
            "PHẢI uống với thức ăn (≥350 calo) để tăng hấp thu - nếu không hấp thu giảm 50%",
            "Akathisia - tác dụng phụ phổ biến, có thể điều trị bằng propranolol",
            "QT prolongation - hiếm nhưng cần theo dõi ECG",
            "Ít tăng cân hơn các atypical khác - ưu điểm",
            "Thận trọng với CYP3A4 inhibitors/inducers"
        ],
        "pharmacokinetics": {
            "half_life": "18 giờ",
            "onset": "1-2 tuần",
            "duration": "24 giờ",
            "protein_binding": "99%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Nguy cơ tự sát ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa lurasidone",
                    "effect": "Tăng nồng độ lurasidone, tăng tác dụng phụ",
                    "management": "Giảm liều lurasidone 50%. Tránh dùng với ketoconazole liều cao."
                },
                {
                    "drug": "CYP3A4 inducers (carbamazepine, rifampin)",
                    "mechanism": "Tăng chuyển hóa lurasidone",
                    "effect": "Giảm nồng độ lurasidone, giảm hiệu quả",
                    "management": "Tăng liều lurasidone. Hoặc tránh dùng chung."
                }
            ],
            "moderate": [
                {
                    "drug": "QT prolonging drugs",
                    "mechanism": "Cả hai đều kéo dài QT",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim",
                    "management": "Thận trọng, theo dõi ECG."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng lurasidone",
                "QT prolongation nặng"
            ],
            "tương_đối": [
                "Bệnh tim - tăng nguy cơ QT prolongation",
                "Dùng với CYP3A4 inhibitors mạnh - giảm liều",
                "Dùng với CYP3A4 inducers mạnh - tăng liều"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng lurasidone",
                "QT prolongation nặng"
            ],
            "tương_đối": [
                "Bệnh tim - tăng nguy cơ QT prolongation",
                "Dùng với CYP3A4 inhibitors mạnh - giảm liều",
                "Dùng với CYP3A4 inducers mạnh - tăng liều",
                "Suy thận nặng (CrCl <30) - thận trọng, giảm liều"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Lurasidone không được lọc sạch hiệu quả qua thẩm phân máu do protein binding cao (99%).",
            "notes": "Lurasidone thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy. Giảm liều và theo dõi chặt chẽ ở suy thận nặng."
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Có thể dùng khi cần thiết.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 50%",
            "severe": "Giảm liều 50%",
            "notes": "Chuyển hóa qua gan (CYP3A4). Suy gan làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ sâu",
                "QT prolongation",
                "Hạ huyết áp",
                "Akathisia nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ECG liên tục",
                "Điều trị hạ huyết áp",
                "Điều trị akathisia nếu có"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống với thức ăn (≥350 calo) để tăng hấp thu - nếu không hấp thu giảm 50%",
                "timing": "Dùng 1 lần/ngày với bữa ăn. Không ngừng đột ngột."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Latuda (Lurasidone)",
                "UpToDate - Lurasidone: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA approved"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "cardiovascular": "QT prolongation (rare but serious)",
                "neurological": "Akathisia (common)"
            },
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - Suicidal thoughts/behaviors in children/adolescents/young adults (<25 years) - CRITICAL",
                "CRITICAL - Must take with food (≥350 calories) - absorption decreases 50% without food",
                "ECG (QT prolongation risk, especially with QT prolonging drugs)",
                "Akathisia signs (restlessness, inability to sit still) - common, may need propranolol",
                "Weight (less weight gain than other atypical antipsychotics - advantage)",
                "Prolactin levels (mild increase)",
                "CYP3A4 interactions (inhibitors increase levels, inducers decrease levels)"
            ],
            "look_alike_sound_alike": ["Lurasidone", "Latuda"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Suicidal Thoughts/Behaviors",
            "APA Guidelines - Schizophrenia Treatment",
            "APA Guidelines - Bipolar Disorder",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    
    "Olanzapine":     {
        "group": "Psychiatry - Antipsychotic (Atypical)",
        "vietnamese_name": "Olanzapine, Zyprexa",
        "administration": [
            "PO",
            "IM"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (mania, depression)",
            "Trầm cảm kháng trị (adjunct)",
            "Delirium (ICU) - off-label"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng olanzapine hoặc các thành phần khác",
                "QT prolongation nặng (QTc >500ms)"
    ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ QT prolongation, hạ huyết áp",
                "Đái tháo đường - tăng đường huyết, nguy cơ đái tháo đường",
                "Tăng lipid máu - tăng cholesterol, triglyceride",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP1A2 inhibitors - giảm liều olanzapine 50%",
                "Dùng với CYP1A2 inducers hoặc hút thuốc - tăng liều olanzapine 50-100%",
                "Dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ, hạ huyết áp"
    ],
        },
        "dosage": {
            "adult_schizophrenia_po": "5-10mg/ngày, tăng đến 10-20mg/ngày (tối đa 20mg/ngày)",
            "adult_bipolar_mania_po": "10-15mg/ngày, tăng đến 15-20mg/ngày",
            "adult_im": "5-10mg IM, lặp mỗi 2-4 giờ nếu cần (tối đa 30mg/ngày)",
            "adult_max": "20mg/ngày PO, 30mg/ngày IM",
            "notes": """Atypical antipsychotic, tăng cân nhiều nhất trong các atypical antipsychotics. Dạng depot (Relprevv): tiêm bắp mỗi 2-4 tuần.""",
        },
        "side_effects": [
            "Tăng cân (phổ biến, nhiều nhất trong các atypical)",
            "Tăng lipid máu (phổ biến)",
            "Tăng đường huyết (nguy cơ đái tháo đường) - phổ biến",
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Khô miệng",
            "Rối loạn vận động (hiếm hơn typical antipsychotics)",
            "QT prolongation (hiếm)",
            "Hạ huyết áp tư thế"
    ],
        "interactions": [
            "CYP1A2 inhibitors (fluvoxamine): tăng nồng độ olanzapine",
            "CYP1A2 inducers (carbamazepine, smoking): giảm nồng độ olanzapine",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "Alcohol: tăng tác dụng an thần"
    ],
        ',
        "pregnancy": "C",
        ',
        "mechanism_of_action": """Olanzapine là thuốc chống loạn thần không điển hình (atypical antipsychotic), đối kháng thụ thể dopamine D2 và serotonin 5-HT2A. Khác với typical antipsychotics, olanzapine có ái lực thấp hơn với D2 và gắn tạm thời (fast dissociation), giảm nguy cơ rối loạn vận động ngoại tháp (EPS) và tăng prolactin. Olanzapine đối kháng mạnh thụ thể histamine H1 (gây buồn ngủ, tăng cân - nhiều nhất trong các atypical), muscarinic (gây khô miệng), và alpha-1 adrenergic (gây hạ huyết áp). Tác dụng: điều trị tâm thần phân liệt, rối loạn lưỡng cực (mania và depression), và trầm cảm kháng trị (adjunct). Có dạng uống (PO), tiêm bắp (IM), và dạng depot (Relprevv). Tác dụng phụ: tăng cân (phổ biến, nhiều nhất trong các atypical), tăng lipid máu, tăng đường huyết (nguy cơ đái tháo đường) - phổ biến, buồn ngủ, QT prolongation (hiếm).""",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng tâm thần, ổn định tâm trạng (đánh giá sau 2-4 tuần)",
            "Cân nặng - tăng cân phổ biến, nhiều nhất trong các atypical, theo dõi định kỳ",
            "Lipid máu (cholesterol, triglyceride) - tăng lipid máu phổ biến",
            "Đường huyết (glucose, HbA1c) - tăng đường huyết, nguy cơ đái tháo đường (phổ biến)",
            "ECG - QT prolongation (hiếm nhưng nguy hiểm), đặc biệt ở liều cao",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Prolactin - ít tăng prolactin hơn typical antipsychotics",
            "Dấu hiệu rối loạn vận động ngoại tháp (EPS) - hiếm hơn typical antipsychotics",
            "Tương tác với CYP1A2 inhibitors/inducers (ảnh hưởng nồng độ olanzapine)"
    ],
        "precautions": [
            "Tăng cân - phổ biến, nhiều nhất trong các atypical, theo dõi cân nặng, khuyến khích chế độ ăn lành mạnh và tập thể dục",
            "Tăng lipid máu - phổ biến, theo dõi cholesterol, triglyceride, điều chỉnh chế độ ăn hoặc dùng statin nếu cần",
            "Tăng đường huyết, nguy cơ đái tháo đường - phổ biến, theo dõi glucose, HbA1c, đặc biệt ở bệnh nhân có nguy cơ đái tháo đường",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "QT prolongation - hiếm nhưng nguy hiểm, đặc biệt ở liều cao, tránh dùng với thuốc kéo dài QT khác",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Thận trọng khi dùng với CYP1A2 inhibitors (fluvoxamine) - tăng nồng độ olanzapine, giảm liều olanzapine 50%",
            "Thận trọng khi dùng với CYP1A2 inducers (carbamazepine, smoking) - giảm nồng độ olanzapine, có thể cần tăng liều",
            "Hút thuốc - giảm nồng độ olanzapine, có thể cần tăng liều ở người hút thuốc",
            "Thận trọng khi dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
            "Tránh rượu - tăng tác dụng an thần",
            "Dạng depot (Relprevv) - tiêm bắp mỗi 2-4 tuần, thuận tiện cho bệnh nhân không tuân thủ điều trị",
            "Không ngừng đột ngột (có thể làm tăng triệu chứng)"
    ],
        "pharmacokinetics": {
            "half_life": "30 giờ",
            "onset": "Vài ngày đến vài tuần (tác dụng chống loạn thần)",
            "duration": "24 giờ (PO), 2-4 tuần (depot)",
            "protein_binding": "93%",
            "clearance": """Gan: chuyển hóa qua CYP1A2 (chính), CYP2D6 (phụ). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều khi dùng với CYP1A2 inhibitors/inducers và khi hút thuốc.""",
        },
        "storage": """Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng depot (Relprevv): bảo quản ở nhiệt độ phòng, tránh ánh sáng, tránh đông lạnh.""",
        "black_box_warnings": """Nguy cơ tử vong tăng ở bệnh nhân lớn tuổi với rối loạn tâm thần do sa sút trí tuệ (dementia-related psychosis) - không được dùng cho chỉ định này. Nguy cơ QT prolongation, có thể gây rối loạn nhịp tim (torsades de pointes). Nguy cơ tăng đường huyết, đái tháo đường. Nguy cơ tăng lipid máu. Nguy cơ tăng cân.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "CYP1A2 inhibitors (Fluvoxamine)",
                    "mechanism": "Ức chế chuyển hóa olanzapine qua CYP1A2, tăng nồng độ olanzapine",
                    "effect": "Tăng nồng độ olanzapine, tăng tác dụng phụ (buồn ngủ, tăng cân, QT prolongation)",
                    "management": "Giảm liều olanzapine 50% khi dùng với fluvoxamine. Theo dõi tác dụng phụ chặt chẽ.",
                },
    {
                    "drug": "CYP1A2 inducers (Carbamazepine, Smoking)",
                    "mechanism": "Cảm ứng chuyển hóa olanzapine qua CYP1A2, giảm nồng độ olanzapine",
                    "effect": "Giảm nồng độ olanzapine, giảm hiệu quả",
                    "management": """Tăng liều olanzapine 50-100% khi dùng với carbamazepine hoặc ở người hút thuốc. Theo dõi đáp ứng điều trị.""",
                },
    {
                    "drug": "QT prolonging drugs (Amiodarone, Sotalol, Citalopram, Escitalopram, Haloperidol)",
                    "mechanism": "Cả hai đều kéo dài QT, tăng nguy cơ rối loạn nhịp tim",
                    "effect": "QT prolongation, rối loạn nhịp tim (torsades de pointes)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi ECG. Giảm liều một trong hai thuốc.",
                }
                ],
            "moderate": [
    {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp",
                    "management": "Tránh hoặc giảm rượu. Cảnh báo bệnh nhân.",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng olanzapine hoặc các thành phần khác",
                "QT prolongation nặng (QTc >500ms)"
    ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ QT prolongation, hạ huyết áp",
                "Đái tháo đường - tăng đường huyết, nguy cơ đái tháo đường",
                "Tăng lipid máu - tăng cholesterol, triglyceride",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP1A2 inhibitors - giảm liều olanzapine 50%",
                "Dùng với CYP1A2 inducers hoặc hút thuốc - tăng liều olanzapine 50-100%",
                "Dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ, hạ huyết áp"
    ],
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Olanzapine không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": """Olanzapine thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy. Giảm liều và theo dõi chặt chẽ ở suy thận nặng.""",
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở) nếu mẹ dùng olanzapine trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.""",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": """Olanzapine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.""",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém).",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": """Olanzapine chuyển hóa ở gan qua CYP1A2, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.""",
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, hôn mê",
                "Rối loạn tim mạch: QT prolongation, rối loạn nhịp tim (torsades de pointes), hạ huyết áp",
                "Rối loạn hô hấp: suy hô hấp",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ (QT prolongation)",
                "Xử trí QT prolongation: Magnesium sulfate (2g IV), isoproterenol nếu cần",
                "Xử trí torsades de pointes: Magnesium sulfate, overdrive pacing",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi ít nhất 24-48 giờ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, điện tâm đồ (QT interval), huyết áp",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": """Uống 1 lần/ngày vào buổi tối. Uống cùng thời điểm mỗi ngày. Tăng liều chậm để giảm tác dụng phụ (đặc biệt buồn ngủ, tăng cân). Không ngừng đột ngột (có thể làm tăng triệu chứng).""",
            },
            "im": {
                "reconstitution": "Không cần pha loãng. Lắc kỹ trước khi dùng.",
                "infusion_rate": "Tiêm bắp sâu vào cơ lớn (gluteal, deltoid). Tránh tiêm vào mạch máu.",
                "compatibility": [],
                "incompatibility": [],
                "notes": """Dạng IM: dùng cho loạn thần cấp, delirium. Dạng depot (Relprevv): tiêm bắp mỗi 2-4 tuần, thuận tiện cho bệnh nhân không tuân thủ điều trị.""",
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống và tiêm bắp (depot)",
            },
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Olanzapine",
                "UpToDate - Olanzapine: Drug information",
                "FDA - Zyprexa (olanzapine) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
    ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "metabolic": "Black Box Warning - Hyperglycemia, diabetes mellitus (common)",
                "metabolic_other": "Black Box Warning - Hyperlipidemia (common), weight gain (most among atypical antipsychotics - common)",
                "cardiovascular": "Black Box Warning - QT prolongation (rare but serious), hypotension",
                "neurological": "Black Box Warning - Increased mortality in elderly with dementia-related psychosis (contraindicated)"
            },
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Black Box Warning - Increased mortality in elderly with dementia-related psychosis - CONTRAINDICATED for this indication - CRITICAL",
                "Black Box Warning - Blood glucose, HbA1c (hyperglycemia, diabetes risk - common) - CRITICAL",
                "Black Box Warning - Lipid panel (cholesterol, triglycerides - hyperlipidemia common) - CRITICAL",
                "Black Box Warning - Weight (most weight gain among atypical antipsychotics - common) - CRITICAL",
                "Black Box Warning - ECG (QT prolongation risk, especially at high doses or with QT prolonging drugs) - CRITICAL",
                "Blood pressure (orthostatic hypotension, especially at initiation or dose increase)",
                "CYP1A2 interactions (inhibitors increase levels 50% - reduce dose, inducers/smoking decrease levels - may need dose increase)"
            ],
            "look_alike_sound_alike": ["Olanzapine", "Zyprexa", "Quetiapine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia-Related Psychosis",
            "FDA Black Box Warning - Hyperglycemia and Diabetes",
            "FDA Black Box Warning - Hyperlipidemia",
            "FDA Black Box Warning - QT Prolongation",
            "APA Guidelines - Schizophrenia Treatment",
            "APA Guidelines - Bipolar Disorder",
            "ISMP High Alert Medications",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
    "Pimozide": {
        "group": "Psychiatry - Antipsychotic (Typical)",
        "vietnamese_name": "Pimozide, Orap",
        "administration": ["PO"],
        "indications": [
            "Tourette's syndrome",
            "Tics nặng",
            "Tâm thần phân liệt (ít dùng)"
        ],
        "contraindications": [
            "QT prolongation nặng (QTc >500ms)",
            "Rối loạn nhịp tim",
            "Dùng với QT prolonging drugs",
            "Dùng với CYP3A4 inhibitors mạnh",
            "Dị ứng pimozide"
        ],
        "dosage": {
            "adult_tourette": "1-2mg/ngày, tăng dần đến 4-8mg/ngày",
            "adult_max": "10mg/ngày",
            "notes": "Typical antipsychotic, hiệu quả với Tourette's syndrome. QT prolongation - cần theo dõi ECG. Tương tác nhiều với CYP3A4 inhibitors."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "QT prolongation (QUAN TRỌNG - cần theo dõi ECG)",
            "Rối loạn vận động ngoại tháp (EPS) - phổ biến",
            "Buồn ngủ",
            "Chóng mặt",
            "Khô miệng",
            "Tăng prolactin",
            "Rối loạn nhịp tim (torsades de pointes)"
        ],
        "interactions": [
            "CYP3A4 inhibitors: tăng nồng độ pimozide đáng kể (nguy hiểm)",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "Macrolides, azoles: CHỐNG CHỈ ĐỊNH (tăng nồng độ pimozide)"
        ],
        ',
        "pregnancy": "C",
        ',
        "mechanism_of_action": "Pimozide là typical antipsychotic, đối kháng thụ thể dopamine D2 mạnh. Ức chế dopamine ở vùng nigrostriatal → giảm tics trong Tourette's syndrome. Đối kháng D2 ở vùng mesolimbic → tác dụng chống loạn thần. Đặc điểm: hiệu quả với Tourette's syndrome và tics nặng, nhưng có nguy cơ QT prolongation cao, rối loạn vận động ngoại tháp (EPS) phổ biến, tương tác nhiều với CYP3A4 inhibitors (tăng nồng độ đáng kể, nguy hiểm).",
        "monitoring": [
            "ECG trước khi bắt đầu và định kỳ (QT prolongation) - QUAN TRỌNG",
            "Triệu chứng Tourette's (tics)",
            "Dấu hiệu rối loạn vận động ngoại tháp (EPS): parkinsonism, dystonia, akathisia",
            "Dấu hiệu rối loạn nhịp tim (torsades de pointes)",
            "Prolactin (tăng prolactin phổ biến)"
        ],
        "precautions": [
            "QT PROLONGATION - cần theo dõi ECG trước và định kỳ",
            "Rối loạn vận động ngoại tháp (EPS) - phổ biến, có thể điều trị bằng anticholinergics",
            "Tương tác với CYP3A4 inhibitors - tăng nồng độ pimozide đáng kể, nguy hiểm",
            "CHỐNG CHỈ ĐỊNH với macrolides, azoles (tăng nồng độ pimozide)",
            "Tránh dùng với QT prolonging drugs",
            "Thận trọng ở bệnh nhân có bệnh tim",
            "Tăng prolactin - phổ biến"
        ],
        "pharmacokinetics": {
            "half_life": "55 giờ (rất dài)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "99%",
            "clearance": "Gan: chuyển hóa qua CYP3A4, CYP2D6. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "QT prolongation - có thể gây rối loạn nhịp tim nghiêm trọng (torsades de pointes), có thể tử vong. Cần theo dõi ECG. Chống chỉ định với CYP3A4 inhibitors mạnh (macrolides, azoles).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin)",
                    "mechanism": "Ức chế chuyển hóa pimozide",
                    "effect": "Tăng nồng độ pimozide đáng kể (10-20 lần), tăng nguy cơ QT prolongation, rối loạn nhịp tim, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Tránh dùng cùng."
                },
                {
                    "drug": "QT prolonging drugs (amiodarone, sotalol, haloperidol, thioridazine)",
                    "mechanism": "Cả hai đều kéo dài QT",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim nghiêm trọng (torsades de pointes)",
                    "management": "TRÁNH dùng cùng. Nếu cần, theo dõi ECG sát."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa pimozide",
                    "effect": "Tăng nồng độ pimozide, tăng tác dụng phụ",
                    "management": "Thận trọng. Giảm liều pimozide 50%."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "QT prolongation nặng (QTc >500ms)",
                "Rối loạn nhịp tim",
                "Dùng với CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, clarithromycin, erythromycin)",
                "Dùng với QT prolonging drugs",
                "Dị ứng pimozide"
            ],
            "tương_đối": [
                "Bệnh tim - tăng nguy cơ QT prolongation",
                "Dùng với CYP2D6 inhibitors - giảm liều",
                "Suy gan nặng - tăng nguy cơ tích lũy"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Có thể dùng khi lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Pimozide bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH (chuyển hóa qua gan)",
            "notes": "Pimozide chuyển hóa qua gan (CYP3A4, CYP2D6). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "QT prolongation nặng",
                "Rối loạn nhịp tim (torsades de pointes)",
                "Rối loạn vận động ngoại tháp nặng",
                "Buồn ngủ sâu, hôn mê",
                "Hạ huyết áp"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ECG liên tục (QT prolongation)",
                "Điều trị rối loạn nhịp tim: Magnesium sulfate, isoproterenol nếu cần",
                "Điều trị rối loạn vận động: Anticholinergics (benztropine, diphenhydramine)",
                "Điều trị hạ huyết áp: Truyền dịch, vận mạch",
                "Lọc máu KHÔNG hiệu quả do protein binding cao (99%)"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, ý thức, dấu hiệu rối loạn vận động"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Dùng 1 lần/ngày. Khởi đầu 1-2mg/ngày, tăng dần. QUAN TRỌNG: Theo dõi ECG trước và định kỳ. KHÔNG ngừng đột ngột."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Orap (pimozide)",
                "UpToDate - Pimozide: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"cardiovascular": "QT prolongation - Black Box Warning (torsades de pointes)", "neurological_extrapyramidal": "EPS"},
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (QT prolongation - Black Box Warning, before and periodically)", "EPS signs", "Prolactin"],
            "look_alike_sound_alike": ["Pimozide", "Pimobendan"]
        },
        "guideline_tags": [
            "APA Guidelines - Tourette's Syndrome",
            "FDA Black Box Warning - QT Prolongation",
            "FDA Black Box Warning - CYP3A4 Inhibitors Contraindicated",
            "NICE Guidelines - Tourette's Syndrome"
        ],
        "last_updated": "2025-02-18",
    },
    "Quetiapine": {
        "group": "Psychiatry - Antipsychotic (Atypical)",
        "vietnamese_name": "Quetiapine, Seroquel",
        "administration": ["PO"],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (mania, depression)",
            "Trầm cảm kháng trị (adjunct)",
            "Rối loạn lo âu tổng quát (GAD) - off-label"
        ],
        "contraindications": [
            "Dị ứng",
            "QT prolongation nặng"
        ],
        "dosage": {
            "adult_schizophrenia": "25mg x 2 lần/ngày, tăng đến 300-800mg/ngày (chia 2-3 lần)",
            "adult_bipolar_mania": "50mg x 2 lần/ngày, tăng đến 400-800mg/ngày",
            "adult_bipolar_depression": "50mg/ngày, tăng đến 300mg/ngày",
            "adult_max": "800mg/ngày",
            "notes": "Tăng liều chậm. Dạng extended release (XR): uống 1 lần/ngày"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Khô miệng",
            "Tăng cân (phổ biến)",
            "Tăng lipid máu",
            "Tăng đường huyết (nguy cơ đái tháo đường)",
            "QT prolongation (hiếm)",
            "Hạ huyết áp tư thế",
            "Rối loạn vận động (hiếm hơn typical antipsychotics)"
        ],
        "interactions": [
            "CYP3A4 inhibitors (ketoconazole, erythromycin): tăng nồng độ quetiapine",
            "CYP3A4 inducers (carbamazepine, phenytoin): giảm nồng độ quetiapine",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "Alcohol: tăng tác dụng an thần",
            "Antihypertensives: tăng nguy cơ hạ huyết áp"
        ],
        ',
        "pregnancy": "C",
        ',
        "mechanism_of_action": "Quetiapine là thuốc chống loạn thần không điển hình (atypical antipsychotic), đối kháng thụ thể dopamine D2 và serotonin 5-HT2A. Khác với typical antipsychotics, quetiapine có ái lực thấp hơn với D2 và gắn tạm thời (fast dissociation), giảm nguy cơ rối loạn vận động ngoại tháp (EPS) và tăng prolactin. Quetiapine cũng đối kháng thụ thể histamine H1 (gây buồn ngủ, tăng cân), alpha-1 adrenergic (gây hạ huyết áp), và muscarinic (gây khô miệng). Tác dụng: điều trị tâm thần phân liệt, rối loạn lưỡng cực (mania và depression), và trầm cảm kháng trị (adjunct). Có dạng immediate release (IR) và extended release (XR). Tác dụng phụ: buồn ngủ (phổ biến), tăng cân, tăng lipid máu, tăng đường huyết (nguy cơ đái tháo đường), QT prolongation (hiếm).",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng tâm thần, ổn định tâm trạng (đánh giá sau 2-4 tuần)",
            "Cân nặng - tăng cân phổ biến, theo dõi định kỳ",
            "Lipid máu (cholesterol, triglyceride) - tăng lipid máu phổ biến",
            "Đường huyết (glucose, HbA1c) - tăng đường huyết, nguy cơ đái tháo đường",
            "ECG - QT prolongation (hiếm nhưng nguy hiểm), đặc biệt ở liều cao",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Prolactin - ít tăng prolactin hơn typical antipsychotics",
            "Dấu hiệu rối loạn vận động ngoại tháp (EPS) - hiếm hơn typical antipsychotics",
            "Tương tác với CYP3A4 inhibitors/inducers (ảnh hưởng nồng độ quetiapine)"
        ],
        "precautions": [
            "Tăng liều chậm để giảm tác dụng phụ (đặc biệt hạ huyết áp, buồn ngủ)",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "Tăng cân - phổ biến, theo dõi cân nặng, khuyến khích chế độ ăn lành mạnh và tập thể dục",
            "Tăng lipid máu - phổ biến, theo dõi cholesterol, triglyceride, điều chỉnh chế độ ăn hoặc dùng statin nếu cần",
            "Tăng đường huyết, nguy cơ đái tháo đường - theo dõi glucose, HbA1c, đặc biệt ở bệnh nhân có nguy cơ đái tháo đường",
            "QT prolongation - hiếm nhưng nguy hiểm, đặc biệt ở liều cao, tránh dùng với thuốc kéo dài QT khác",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Thận trọng khi dùng với CYP3A4 inhibitors (ketoconazole, erythromycin) - tăng nồng độ quetiapine, giảm liều quetiapine 50-75%",
            "Thận trọng khi dùng với CYP3A4 inducers (carbamazepine, phenytoin) - giảm nồng độ quetiapine, có thể cần tăng liều",
            "Thận trọng khi dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
            "Tránh rượu - tăng tác dụng an thần",
            "Dạng extended release (XR) - uống 1 lần/ngày, thuận tiện hơn, không nghiền hoặc nhai (phải uống nguyên viên)",
            "Không ngừng đột ngột (có thể làm tăng triệu chứng)"
        ],
        "pharmacokinetics": {
            "half_life": "6 giờ (IR), 7 giờ (XR)",
            "onset": "Vài ngày đến vài tuần (tác dụng chống loạn thần)",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "83%",
            "clearance": "Gan: chuyển hóa qua CYP3A4 (chính), CYP2D6 (phụ). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều khi dùng với CYP3A4 inhibitors/inducers."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release (XR): bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ tử vong tăng ở bệnh nhân lớn tuổi với rối loạn tâm thần do sa sút trí tuệ (dementia-related psychosis) - không được dùng cho chỉ định này. Nguy cơ QT prolongation, có thể gây rối loạn nhịp tim (torsades de pointes). Nguy cơ tăng đường huyết, đái tháo đường. Nguy cơ tăng lipid máu. Nguy cơ tăng cân.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 inhibitors (Ketoconazole, Itraconazole, Erythromycin, Clarithromycin, Ritonavir)",
                    "mechanism": "Ức chế chuyển hóa quetiapine qua CYP3A4, tăng nồng độ quetiapine",
                    "effect": "Tăng nồng độ quetiapine, tăng tác dụng phụ (buồn ngủ, hạ huyết áp, QT prolongation)",
                    "management": "Giảm liều quetiapine 50-75% khi dùng với CYP3A4 inhibitors. Theo dõi tác dụng phụ chặt chẽ."
                },
                {
                    "drug": "CYP3A4 inducers (Carbamazepine, Phenytoin, Rifampin, St. John's wort)",
                    "mechanism": "Cảm ứng chuyển hóa quetiapine qua CYP3A4, giảm nồng độ quetiapine",
                    "effect": "Giảm nồng độ quetiapine, giảm hiệu quả",
                    "management": "Tăng liều quetiapine 2-5 lần khi dùng với CYP3A4 inducers. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "QT prolonging drugs (Amiodarone, Sotalol, Citalopram, Escitalopram, Haloperidol)",
                    "mechanism": "Cả hai đều kéo dài QT, tăng nguy cơ rối loạn nhịp tim",
                    "effect": "QT prolongation, rối loạn nhịp tim (torsades de pointes)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi ECG. Giảm liều một trong hai thuốc."
                }
            ],
            "moderate": [
                {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp."
                },
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp",
                    "management": "Tránh hoặc giảm rượu. Cảnh báo bệnh nhân."
                },
                {
                    "drug": "CYP2D6 inhibitors (Paroxetine, Fluoxetine)",
                    "mechanism": "Ức chế chuyển hóa quetiapine qua CYP2D6 (phụ)",
                    "effect": "Tăng nhẹ nồng độ quetiapine",
                    "management": "Thận trọng. Có thể cần giảm liều quetiapine nhẹ."
                }
            ],
            "minor": [
                {
                    "drug": "Lithium",
                    "mechanism": "Có thể tăng tác dụng an thần nhẹ",
                    "effect": "Tăng nhẹ buồn ngủ, chóng mặt",
                    "management": "Thận trọng. Thường không cần điều chỉnh liều."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng quetiapine hoặc các thành phần khác",
                "QT prolongation nặng (QTc >500ms)"
            ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ QT prolongation, hạ huyết áp",
                "Đái tháo đường - tăng đường huyết, nguy cơ đái tháo đường",
                "Tăng lipid máu - tăng cholesterol, triglyceride",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP3A4 inhibitors - giảm liều quetiapine 50-75%",
                "Dùng với CYP3A4 inducers - tăng liều quetiapine 2-5 lần",
                "Dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ, hạ huyết áp"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng quetiapine hoặc các thành phần khác",
                "QT prolongation nặng (QTc >500ms)"
            ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ QT prolongation, hạ huyết áp",
                "Đái tháo đường - tăng đường huyết, nguy cơ đái tháo đường",
                "Tăng lipid máu - tăng cholesterol, triglyceride",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP3A4 inhibitors - giảm liều quetiapine 50-75%",
                "Dùng với CYP3A4 inducers - tăng liều quetiapine 2-5 lần",
                "Dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ, hạ huyết áp"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Quetiapine không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": "Quetiapine thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy. Giảm liều và theo dõi chặt chẽ ở suy thận nặng."
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở) nếu mẹ dùng quetiapine trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Quetiapine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Quetiapine chuyển hóa ở gan qua CYP3A4, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, hôn mê",
                "Rối loạn tim mạch: QT prolongation, rối loạn nhịp tim (torsades de pointes), hạ huyết áp",
                "Rối loạn hô hấp: suy hô hấp",
                "Rối loạn tiêu hóa: buồn nôn, nôn",
                "Triệu chứng khác: giãn đồng tử"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ (QT prolongation)",
                "Xử trí QT prolongation: Magnesium sulfate (2g IV), isoproterenol nếu cần",
                "Xử trí torsades de pointes: Magnesium sulfate, overdrive pacing",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, điện tâm đồ (QT interval), huyết áp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dạng immediate release (IR): chia 2-3 lần/ngày. Dạng extended release (XR): uống 1 lần/ngày vào buổi tối. Uống cùng thời điểm mỗi ngày. KHÔNG nghiền hoặc nhai viên XR (phải uống nguyên viên). Tăng liều chậm để giảm tác dụng phụ. Không ngừng đột ngột."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Quetiapine",
                "UpToDate - Quetiapine: Drug information",
                "FDA - Seroquel (quetiapine) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"metabolic": "Black Box Warning (diabetes, hyperlipidemia, weight gain)", "cardiovascular": "QT prolongation"},
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Weight", "Glucose/HbA1c (Black Box Warning)", "Lipids (Black Box Warning)", "ECG (QT prolongation)", "CYP3A4 interactions"],
            "look_alike_sound_alike": ["Quetiapine", "Quinidine"]
        },
        "guideline_tags": [
            "APA Guidelines - Schizophrenia",
            "APA Guidelines - Bipolar Disorder",
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "FDA Black Box Warning - QT Prolongation",
            "FDA Black Box Warning - Diabetes/Hyperglycemia",
            "FDA Black Box Warning - Hyperlipidemia",
            "NICE Guidelines - Psychosis and Schizophrenia"
        ],
        "last_updated": "2025-02-18",
    },
    "Risperidone":     {
        "group": "Psychiatry - Antipsychotic (Atypical)",
        "vietnamese_name": "Risperidone, Risperdal",
        "administration": [
            "PO",
            "IM"
    ],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (mania)",
            "Rối loạn phổ tự kỷ (irritability)",
            "Delirium (ICU) - off-label"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng risperidone hoặc các thành phần khác",
                "QT prolongation nặng (QTc >500ms)"
    ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ QT prolongation, hạ huyết áp",
                "Đái tháo đường - tăng đường huyết, nguy cơ đái tháo đường",
                "Tăng lipid máu - tăng cholesterol, triglyceride",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP2D6 inhibitors - giảm liều risperidone 50%",
                "Dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ, hạ huyết áp"
    ],
        },
        "dosage": {
            "adult_schizophrenia_po": "1mg x 2 lần/ngày, tăng đến 4-6mg/ngày (tối đa 16mg/ngày)",
            "adult_bipolar_mania_po": "2-3mg/ngày, tăng đến 6mg/ngày",
            "adult_im": "25mg IM mỗi 2 tuần, tăng đến 37.5-50mg mỗi 2 tuần (tối đa 50mg mỗi 2 tuần)",
            "adult_max": "16mg/ngày PO, 50mg mỗi 2 tuần IM",
            "notes": """Atypical antipsychotic, ít EPS hơn typical antipsychotics nhưng vẫn có nguy cơ. Dạng depot (Consta): tiêm bắp mỗi 2 tuần.""",
        },
        "side_effects": [
            "Rối loạn vận động ngoại tháp (EPS) - ít hơn typical antipsychotics nhưng vẫn có",
            "Tăng prolactin (phổ biến, nhiều hơn các atypical khác)",
            "Tăng cân (phổ biến)",
            "Tăng lipid máu",
            "Tăng đường huyết (nguy cơ đái tháo đường)",
            "QT prolongation (hiếm)",
            "Hạ huyết áp tư thế",
            "Buồn ngủ, chóng mặt"
    ],
        "interactions": [
            "CYP2D6 inhibitors: tăng nồng độ risperidone",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "Alcohol: tăng tác dụng an thần"
    ],
        ',
        "pregnancy": "C",
        ',
        "mechanism_of_action": """Risperidone là thuốc chống loạn thần không điển hình (atypical antipsychotic), đối kháng thụ thể dopamine D2 và serotonin 5-HT2A. Khác với typical antipsychotics, risperidone có ái lực cân bằng với D2 và 5-HT2A, giảm nguy cơ rối loạn vận động ngoại tháp (EPS) so với typical antipsychotics, nhưng vẫn có nguy cơ (đặc biệt ở liều cao >6mg/ngày). Risperidone tăng prolactin nhiều hơn các atypical antipsychotics khác (do ức chế D2 mạnh hơn). Tác dụng: điều trị tâm thần phân liệt, rối loạn lưỡng cực (mania), và rối loạn phổ tự kỷ (irritability). Có dạng uống (PO) và dạng depot (Consta - tiêm bắp mỗi 2 tuần). Tác dụng phụ: rối loạn vận động ngoại tháp (EPS) - ít hơn typical nhưng vẫn có, tăng prolactin (phổ biến), tăng cân, tăng lipid máu, tăng đường huyết, QT prolongation (hiếm).""",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng tâm thần, ổn định tâm trạng (đánh giá sau 2-4 tuần)",
            "Rối loạn vận động ngoại tháp (EPS) - ít hơn typical nhưng vẫn có, đặc biệt ở liều cao >6mg/ngày",
            "Prolactin - tăng prolactin phổ biến (gây vô kinh, tiết sữa), nhiều hơn các atypical khác",
            "Cân nặng - tăng cân phổ biến, theo dõi định kỳ",
            "Lipid máu (cholesterol, triglyceride) - tăng lipid máu phổ biến",
            "Đường huyết (glucose, HbA1c) - tăng đường huyết, nguy cơ đái tháo đường",
            "ECG - QT prolongation (hiếm nhưng nguy hiểm), đặc biệt ở liều cao",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Tương tác với CYP2D6 inhibitors (ảnh hưởng nồng độ risperidone)"
    ],
        "precautions": [
            "Rối loạn vận động ngoại tháp (EPS) - ít hơn typical nhưng vẫn có, đặc biệt ở liều cao >6mg/ngày, có thể dùng anticholinergics nếu cần",
            "Tăng prolactin - phổ biến, nhiều hơn các atypical khác, gây vô kinh, tiết sữa, giảm ham muốn tình dục",
            "Tăng cân - phổ biến, theo dõi cân nặng, khuyến khích chế độ ăn lành mạnh và tập thể dục",
            "Tăng lipid máu - phổ biến, theo dõi cholesterol, triglyceride, điều chỉnh chế độ ăn hoặc dùng statin nếu cần",
            "Tăng đường huyết, nguy cơ đái tháo đường - theo dõi glucose, HbA1c, đặc biệt ở bệnh nhân có nguy cơ đái tháo đường",
            "QT prolongation - hiếm nhưng nguy hiểm, đặc biệt ở liều cao, tránh dùng với thuốc kéo dài QT khác",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Thận trọng khi dùng với CYP2D6 inhibitors (paroxetine, fluoxetine) - tăng nồng độ risperidone, giảm liều risperidone 50%",
            "Thận trọng khi dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
            "Tránh rượu - tăng tác dụng an thần",
            "Dạng depot (Consta) - tiêm bắp mỗi 2 tuần, thuận tiện cho bệnh nhân không tuân thủ điều trị",
            "Không ngừng đột ngột (có thể làm tăng triệu chứng)"
    ],
        "pharmacokinetics": {
            "half_life": "3 giờ (PO), 3-6 ngày (depot)",
            "onset": "Vài ngày đến vài tuần (tác dụng chống loạn thần)",
            "duration": "12-24 giờ (PO), 2 tuần (depot)",
            "protein_binding": "90%",
            "clearance": """Gan: chuyển hóa qua CYP2D6 (chính). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều khi dùng với CYP2D6 inhibitors.""",
        },
        "storage": """Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng depot (Consta): bảo quản ở nhiệt độ phòng, tránh ánh sáng, tránh đông lạnh.""",
        "black_box_warnings": """Nguy cơ tử vong tăng ở bệnh nhân lớn tuổi với rối loạn tâm thần do sa sút trí tuệ (dementia-related psychosis) - không được dùng cho chỉ định này. Nguy cơ QT prolongation, có thể gây rối loạn nhịp tim (torsades de pointes). Nguy cơ tăng đường huyết, đái tháo đường. Nguy cơ tăng lipid máu. Nguy cơ tăng cân.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "CYP2D6 inhibitors (Paroxetine, Fluoxetine, Bupropion)",
                    "mechanism": "Ức chế chuyển hóa risperidone qua CYP2D6, tăng nồng độ risperidone",
                    "effect": "Tăng nồng độ risperidone, tăng tác dụng phụ (EPS, tăng prolactin, QT prolongation)",
                    "management": "Giảm liều risperidone 50% khi dùng với CYP2D6 inhibitors. Theo dõi tác dụng phụ chặt chẽ.",
                },
    {
                    "drug": "QT prolonging drugs (Amiodarone, Sotalol, Citalopram, Escitalopram, Haloperidol)",
                    "mechanism": "Cả hai đều kéo dài QT, tăng nguy cơ rối loạn nhịp tim",
                    "effect": "QT prolongation, rối loạn nhịp tim (torsades de pointes)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, theo dõi ECG. Giảm liều một trong hai thuốc.",
                }
                ],
            "moderate": [
    {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp.",
                },
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp",
                    "management": "Tránh hoặc giảm rượu. Cảnh báo bệnh nhân.",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng risperidone hoặc các thành phần khác",
                "QT prolongation nặng (QTc >500ms)"
    ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ QT prolongation, hạ huyết áp",
                "Đái tháo đường - tăng đường huyết, nguy cơ đái tháo đường",
                "Tăng lipid máu - tăng cholesterol, triglyceride",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP2D6 inhibitors - giảm liều risperidone 50%",
                "Dùng với QT prolonging drugs - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ, hạ huyết áp"
    ],
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Risperidone không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": """Risperidone thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy. Giảm liều và theo dõi chặt chẽ ở suy thận nặng.""",
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở) nếu mẹ dùng risperidone trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.""",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": """Risperidone bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.""",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém).",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": """Risperidone chuyển hóa ở gan qua CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.""",
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, hôn mê",
                "Rối loạn vận động: EPS (dystonia, akathisia, parkinsonism)",
                "Rối loạn tim mạch: QT prolongation, rối loạn nhịp tim (torsades de pointes), hạ huyết áp",
                "Rối loạn hô hấp: suy hô hấp",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Benztropine hoặc diphenhydramine cho EPS.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Xử trí EPS: Benztropine 1-2mg IM/IV hoặc diphenhydramine 25-50mg IM/IV",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ (QT prolongation)",
                "Xử trí QT prolongation: Magnesium sulfate (2g IV), isoproterenol nếu cần",
                "Xử trí torsades de pointes: Magnesium sulfate, overdrive pacing",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi ít nhất 24-48 giờ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, điện tâm đồ (QT interval), huyết áp",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": """Chia 2 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm để giảm tác dụng phụ. Không ngừng đột ngột (có thể làm tăng triệu chứng).""",
            },
            "im": {
                "reconstitution": "Dạng depot (Consta): pha loãng với diluent đi kèm. Lắc kỹ trước khi dùng.",
                "infusion_rate": "Tiêm bắp sâu vào cơ lớn (gluteal, deltoid). Tránh tiêm vào mạch máu.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Dạng depot (Consta): tiêm bắp mỗi 2 tuần, thuận tiện cho bệnh nhân không tuân thủ điều trị.",
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống và tiêm bắp (depot)",
            },
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Risperidone",
                "UpToDate - Risperidone: Drug information",
                "FDA - Risperdal (risperidone) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
    ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"metabolic": "Black Box Warning (diabetes, hyperlipidemia, weight gain)", "endocrine": "High prolactin (more than other atypicals)", "cardiovascular": "QT prolongation"},
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Prolactin (higher than other atypicals)", "Weight", "Glucose/HbA1c (Black Box Warning)", "Lipids (Black Box Warning)", "ECG (QT prolongation)", "EPS signs (especially at doses >6mg/day)"],
            "look_alike_sound_alike": ["Risperidone", "Aripiprazole"]
        },
        "guideline_tags": [
            "APA Guidelines - Schizophrenia",
            "APA Guidelines - Bipolar Disorder",
            "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
            "FDA Black Box Warning - QT Prolongation",
            "FDA Black Box Warning - Diabetes/Hyperglycemia",
            "FDA Black Box Warning - Hyperlipidemia",
            "NICE Guidelines - Psychosis and Schizophrenia"
        ],
        "last_updated": "2025-02-18",
    },
    "Ziprasidone": {
        "group": "Psychiatry - Antipsychotic (Atypical)",
        "vietnamese_name": "Ziprasidone, Geodon",
        "administration": ["PO", "IM"],
        "indications": [
            "Tâm thần phân liệt",
            "Rối loạn lưỡng cực (mania, mixed episodes)",
            "Agitation cấp tính (IM)"
        ],
        "contraindications": [
            "QT prolongation nặng (QTc >500ms)",
            "Nhồi máu cơ tim gần đây",
            "Suy tim nặng",
            "Dị ứng ziprasidone"
        ],
        "dosage": {
            "adult_po": "20mg x 2 lần/ngày với thức ăn, tăng đến 40-80mg x 2 lần/ngày",
            "adult_im": "10-20mg IM, có thể lặp lại sau 2-4 giờ (tối đa 40mg/ngày)",
            "adult_max": "160mg/ngày (PO)",
            "notes": "PHẢI uống với thức ăn (≥500 calo) để tăng hấp thu. QT prolongation - cần theo dõi ECG."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "QT prolongation (quan trọng - cần theo dõi ECG)",
            "Buồn ngủ",
            "Chóng mặt",
            "Buồn nôn",
            "Tăng cân (ít hơn các atypical khác)",
            "Hạ huyết áp tư thế",
            "Rối loạn vận động (hiếm)"
        ],
        "interactions": [
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "CYP3A4 inhibitors: tăng nồng độ ziprasidone",
            "CYP3A4 inducers: giảm nồng độ ziprasidone"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ziprasidone là atypical antipsychotic, đối kháng thụ thể dopamine D2 và serotonin 5-HT2A. Cũng đối kháng 5-HT1A, 5-HT1D, 5-HT2C, và ức chế tái hấp thu serotonin và norepinephrine. Đặc điểm: ít tăng cân hơn các atypical khác, nhưng có nguy cơ QT prolongation (cần theo dõi ECG). PHẢI uống với thức ăn (≥500 calo) để tăng hấp thu. Có dạng IM cho agitation cấp tính.",
        "monitoring": [
            "ECG trước khi bắt đầu và định kỳ (QT prolongation)",
            "Triệu chứng tâm thần",
            "Cân nặng (ít tăng cân hơn các atypical khác)",
            "Huyết áp (hạ huyết áp tư thế)",
            "Chức năng gan (hiếm)"
        ],
        "precautions": [
            "QT PROLONGATION - cần theo dõi ECG trước và định kỳ",
            "PHẢI uống với thức ăn (≥500 calo) để tăng hấp thu - nếu không hấp thu giảm 50%",
            "Tránh dùng với QT prolonging drugs",
            "Thận trọng ở bệnh nhân có bệnh tim",
            "Ít tăng cân hơn các atypical khác - ưu điểm",
            "Thận trọng với CYP3A4 inhibitors/inducers"
        ],
        "pharmacokinetics": {
            "half_life": "7 giờ",
            "onset": "1-2 tuần (PO), 30-60 phút (IM)",
            "duration": "12 giờ (PO), 4-6 giờ (IM)",
            "protein_binding": "99%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ tự sát ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi). QT prolongation - cần theo dõi ECG.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "QT prolonging drugs (amiodarone, sotalol, haloperidol, thioridazine)",
                    "mechanism": "Cả hai đều kéo dài QT",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim nghiêm trọng (torsades de pointes)",
                    "management": "TRÁNH dùng cùng. Nếu cần, theo dõi ECG sát."
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa ziprasidone",
                    "effect": "Tăng nồng độ ziprasidone, tăng tác dụng phụ",
                    "management": "Giảm liều ziprasidone 50%."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (carbamazepine, rifampin)",
                    "mechanism": "Tăng chuyển hóa ziprasidone",
                    "effect": "Giảm nồng độ ziprasidone, giảm hiệu quả",
                    "management": "Tăng liều ziprasidone."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "QT prolongation nặng (QTc >500ms)",
                "Nhồi máu cơ tim gần đây",
                "Suy tim nặng",
                "Dị ứng ziprasidone"
            ],
            "tương_đối": [
                "Bệnh tim - tăng nguy cơ QT prolongation",
                "Dùng với QT prolonging drugs - tránh",
                "Dùng với CYP3A4 inhibitors mạnh - giảm liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Có nguy cơ dị tật thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 50%",
            "severe": "Giảm liều 50%",
            "notes": "Chuyển hóa qua gan (CYP3A4). Suy gan làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ sâu",
                "QT prolongation nặng",
                "Hạ huyết áp",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ECG liên tục (QT prolongation)",
                "Điều trị rối loạn nhịp tim nếu có",
                "Điều trị hạ huyết áp"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "PHẢI uống với thức ăn (≥500 calo) để tăng hấp thu - nếu không hấp thu giảm 50%",
                "timing": "Dùng 2 lần/ngày với bữa ăn. Không ngừng đột ngột."
            },
            "im": {
                "reconstitution": "Dùng trực tiếp dung dịch đã pha sẵn",
                "injection_site": "Cơ lớn (đùi, cánh tay)",
                "notes": "IM: 10-20mg, có thể lặp lại sau 2-4 giờ (tối đa 40mg/ngày). Dùng cho agitation cấp tính."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Geodon (ziprasidone)",
                "UpToDate - Ziprasidone: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"cardiovascular": "QT prolongation - Black Box Warning", "metabolic": "Less weight gain than other atypicals"},
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (QT prolongation - Black Box Warning, before and periodically)", "Weight (less gain than other atypicals)", "Must take with food ≥500 cal"],
            "look_alike_sound_alike": ["Ziprasidone", "Zonisamide"]
        },
        "guideline_tags": [
            "APA Guidelines - Schizophrenia",
            "APA Guidelines - Bipolar Disorder",
            "FDA Black Box Warning - Suicidal Behavior in Children/Adolescents",
            "FDA Black Box Warning - QT Prolongation",
            "NICE Guidelines - Psychosis and Schizophrenia"
        ],
        "last_updated": "2025-02-18",
    },
    
}

__all__ = ['ANTIPSYCHOTICS_DRUGS']







