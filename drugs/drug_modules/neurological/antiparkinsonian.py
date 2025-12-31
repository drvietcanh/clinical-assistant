"""
Antiparkinsonian Drugs
Drugs for Parkinson's disease and movement disorders
"""

ANTIPARKINSONIAN_DRUGS = {
    "Deutetrabenazine": {
        "group": "Neurology - Movement Disorders (VMAT2 Inhibitor)",
        "vietnamese_name": "Deutetrabenazine, Austedo",
        "administration": ["PO"],
        "indications": [
            "Rối loạn vận động do Huntington (Huntington's disease chorea)",
            "Rối loạn vận động do tardive dyskinesia"
        ],
        "contraindications": [
            "Dị ứng deutetrabenazine hoặc tetrabenazine",
            "Suy gan nặng",
            "Dùng với MAO inhibitors (trong 14 ngày)"
        ],
        "dosage": {
            "adult_huntington_initial": "6mg PO mỗi ngày, tăng dần mỗi tuần (6→12→18→24→30→36→42→48mg/ngày) đến liều hiệu quả",
            "adult_huntington_max": "48mg/ngày (chia 2 lần)",
            "adult_tardive_initial": "12mg PO mỗi ngày, tăng dần mỗi tuần (12→18→24→30→36mg/ngày) đến liều hiệu quả",
            "adult_tardive_max": "36mg/ngày (chia 2 lần)",
            "notes": "Chia 2 lần/ngày. Uống với thức ăn. Bắt đầu với liều thấp và tăng dần để giảm tác dụng phụ. Không ngừng đột ngột."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Buồn ngủ, mệt mỏi - phổ biến",
            "Trầm cảm - phổ biến, NGUY HIỂM",
            "Rối loạn giấc ngủ - phổ biến",
            "Lo âu - phổ biến",
            "Rối loạn nhịp tim (QT kéo dài) - NGUY HIỂM",
            "Parkinsonism - có thể xảy ra",
            "Buồn nôn",
            "Chóng mặt"
        ],
        "interactions": [
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH - tăng nguy cơ serotonin syndrome",
            "Thuốc kéo dài QT (amiodarone, sotalol): TĂNG nguy cơ QT kéo dài - TRÁNH",
            "CYP2D6 inhibitors (paroxetine, fluoxetine): tăng nồng độ - giảm liều",
            "Reserpine: tăng nguy cơ tác dụng phụ - TRÁNH"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Deutetrabenazine là chất ức chế VMAT2 (vesicular monoamine transporter 2) với deuterium substitution. VMAT2 là protein vận chuyển monoamine (dopamine, serotonin, norepinephrine) vào túi tiết (vesicles) trong tế bào thần kinh. Ức chế VMAT2 → giảm vận chuyển monoamine vào túi tiết → giảm giải phóng monoamine → giảm hoạt động dopamine trong não → giảm rối loạn vận động (chorea, tardive dyskinesia). Deutetrabenazine có deuterium substitution → chuyển hóa chậm hơn tetrabenazine → half-life dài hơn, liều thấp hơn, tác dụng phụ ít hơn. Dẫn đến: giảm rối loạn vận động trong bệnh Huntington và tardive dyskinesia. Deutetrabenazine được dùng để điều trị rối loạn vận động do Huntington và tardive dyskinesia.",
        "monitoring": [
            "Rối loạn vận động (chorea, tardive dyskinesia) - đánh giá hiệu quả điều trị",
            "Trầm cảm - QUAN TRỌNG: theo dõi chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều",
            "ECG (QT interval) - theo dõi trước và trong điều trị, đặc biệt khi dùng với thuốc kéo dài QT",
            "Parkinsonism - theo dõi triệu chứng",
            "Rối loạn giấc ngủ - theo dõi",
            "Chức năng gan (ALT, AST) - mỗi 3-6 tháng",
            "Dấu hiệu serotonin syndrome (nếu dùng với MAO inhibitors)"
        ],
        "precautions": [
            "THEO DÕI TRẦM CẢM CHẶT CHẼ - tăng nguy cơ, đặc biệt khi bắt đầu hoặc tăng liều, ngừng ngay nếu có ý tưởng tự tử",
            "THEO DÕI ECG (QT INTERVAL) - tăng nguy cơ QT kéo dài, đặc biệt khi dùng với thuốc kéo dài QT",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors (trong 14 ngày) - tăng nguy cơ serotonin syndrome",
            "TRÁNH dùng với reserpine - tăng nguy cơ tác dụng phụ",
            "Buồn ngủ, mệt mỏi - phổ biến, tránh lái xe hoặc vận hành máy móc",
            "Parkinsonism - có thể xảy ra, giảm liều nếu có",
            "Không ngừng đột ngột - giảm dần dần",
            "Giảm liều 50% ở bệnh nhân dùng CYP2D6 inhibitors mạnh"
        ],
        "pharmacokinetics": {
            "half_life": "9-10 giờ (dao động 6-15 giờ)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "12 giờ (chia 2 lần/ngày)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa ở gan qua CYP2D6 và CYP1A2",
            "clearance": "Chuyển hóa ở gan, thải trừ qua thận một phần. Half-life dài hơn tetrabenazine nhờ deuterium substitution."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "TRẦM CẢM VÀ Ý TƯỞNG TỰ TỬ - tăng nguy cơ trầm cảm và ý tưởng tự tử. Theo dõi chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều. Ngừng ngay nếu có ý tưởng tự tử. QT KÉO DÀI - tăng nguy cơ rối loạn nhịp tim. TRÁNH dùng với thuốc kéo dài QT.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa monoamine, tăng nguy cơ serotonin syndrome",
                    "effect": "Tăng nguy cơ serotonin syndrome (nguy hiểm)",
                    "management": "CHỐNG CHỈ ĐỊNH - không được dùng cùng. Ngừng MAO inhibitors ít nhất 14 ngày trước khi dùng deutetrabenazine."
                },
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, sotalol, haloperidol)",
                    "mechanism": "Tác dụng cộng dồn kéo dài QT",
                    "effect": "Tăng nguy cơ QT kéo dài, rối loạn nhịp tim (nguy hiểm)",
                    "management": "TRÁNH dùng cùng. Nếu bắt buộc, theo dõi ECG chặt chẽ."
                },
                {
                    "drug": "Reserpine",
                    "mechanism": "Tác dụng cộng dồn ức chế VMAT2",
                    "effect": "Tăng nguy cơ tác dụng phụ",
                    "management": "TRÁNH dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP2D6 inhibitors mạnh (paroxetine, fluoxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa deutetrabenazine, tăng nồng độ",
                    "effect": "Tăng tác dụng phụ",
                    "management": "Giảm liều deutetrabenazine 50%. Theo dõi tác dụng phụ chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng deutetrabenazine hoặc tetrabenazine",
                "Suy gan nặng",
                "Dùng với MAO inhibitors (trong 14 ngày)"
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng",
                "Trầm cảm hoặc tiền sử trầm cảm - tăng nguy cơ",
                "QT kéo dài - tăng nguy cơ",
                "Parkinsonism - có thể làm nặng",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Deutetrabenazine là FDA category C. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Caution",
                "details": "Deutetrabenazine bài tiết vào sữa mẹ. Chưa rõ an toàn cho trẻ sơ sinh.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi tác dụng phụ",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Deutetrabenazine chuyển hóa ở gan qua CYP2D6 và CYP1A2. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng, hôn mê",
                "Trầm cảm nặng, ý tưởng tự tử",
                "QT kéo dài, rối loạn nhịp tim",
                "Parkinsonism nặng",
                "Serotonin syndrome (nếu dùng với MAO inhibitors)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "ECG - theo dõi QT interval",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp",
                "Xử trí trầm cảm, ý tưởng tự tử - tư vấn tâm thần",
                "Xử trí rối loạn nhịp tim nếu có",
                "Xử trí serotonin syndrome nếu có (cyproheptadine, cooling)",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp, ECG (QT interval), dấu hiệu trầm cảm, ý tưởng tự tử"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu.",
                "timing": "Chia 2 lần/ngày, uống cùng thời điểm mỗi ngày. Bắt đầu với liều thấp và tăng dần mỗi tuần để giảm tác dụng phụ. Không ngừng đột ngột - giảm dần dần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Deutetrabenazine (Austedo)",
                "UpToDate - Deutetrabenazine: Drug information",
                "Lexicomp - Deutetrabenazine monograph",
                "AAN Guidelines - Huntington's Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, clinical trial data, widely used"
        }
    },
    
    "Istradefylline": {
        "group": "Neurology - Antiparkinsonian (Adenosine A2A Receptor Antagonist)",
        "vietnamese_name": "Istradefylline, Nourianz",
        "administration": ["PO"],
        "indications": [
            "Parkinson's disease - điều trị bổ sung với levodopa/carbidopa",
            "Giảm 'off' time (thời gian không đáp ứng với levodopa)",
            "Tăng 'on' time (thời gian đáp ứng với levodopa)"
        ],
        "contraindications": [
            "Dị ứng istradefylline",
            "Suy gan nặng - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_initial": "20mg PO x 1 lần/ngày",
            "adult_max": "40mg PO x 1 lần/ngày (tăng sau 2 tuần nếu cần)",
            "notes": "Istradefylline là adenosine A2A receptor antagonist. Dùng 1 lần/ngày. Bắt đầu với 20mg, có thể tăng đến 40mg sau 2 tuần nếu cần. Uống với hoặc không thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi (thải trừ qua gan)"
        },
        "side_effects": [
            "Dyskinesia (rối loạn vận động) - phổ biến",
            "Buồn nôn",
            "Chóng mặt",
            "Mất ngủ",
            "Ảo giác - hiếm",
            "Rối loạn hành vi (impulse control disorders) - hiếm",
            "Tăng transaminase (hiếm)"
        ],
        "interactions": [
            "CYP1A1 inhibitors: tăng nồng độ istradefylline",
            "CYP3A4 inhibitors: tăng nồng độ istradefylline",
            "CYP3A4 inducers: giảm nồng độ istradefylline"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Istradefylline là adenosine A2A receptor antagonist. Adenosine A2A receptors có mặt ở vùng striatum (basal ganglia), ức chế hoạt động của dopamine D2 receptors. Istradefylline ức chế adenosine A2A receptors → giảm ức chế dopamine D2 receptors → tăng hoạt động dopamine → tăng hiệu quả levodopa. Dẫn đến: giảm 'off' time và tăng 'on' time với levodopa. ĐẶC ĐIỂM: (1) Adenosine A2A receptor antagonist (cơ chế mới, khác với MAO-B inhibitor và COMT inhibitor), (2) Giảm 'off' time và tăng 'on' time với levodopa, (3) Dùng 1 lần/ngày, (4) Dyskinesia phổ biến (có thể cần giảm liều levodopa), (5) CHỐNG CHỈ ĐỊNH ở suy gan nặng.",
        "monitoring": [
            "Đáp ứng điều trị: giảm 'off' time, tăng 'on' time với levodopa",
            "Dyskinesia - phổ biến, có thể cần giảm liều levodopa",
            "Dấu hiệu ảo giác, lú lẫn - hiếm",
            "Dấu hiệu rối loạn hành vi (impulse control disorders) - hiếm",
            "Chức năng gan (ALT, AST) - hiếm, nhưng CHỐNG CHỈ ĐỊNH ở suy gan nặng"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở suy gan nặng",
            "Dyskinesia phổ biến - có thể cần giảm liều levodopa",
            "Dùng 1 lần/ngày, với hoặc không thức ăn",
            "Thận trọng khi dùng với CYP3A4 inhibitors mạnh - tăng nồng độ",
            "Thận trọng khi dùng với CYP3A4 inducers mạnh - giảm nồng độ",
            "Không ngừng đột ngột - giảm dần dần"
        ],
        "pharmacokinetics": {
            "half_life": "83 giờ (rất dài)",
            "onset": "Vài ngày đến 1 tuần",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "99.8%",
            "metabolism": "Chuyển hóa ở gan (CYP1A1, CYP3A4)",
            "clearance": "Thải trừ qua gan (90%) và thận (10%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở suy gan nặng. Istradefylline chuyển hóa ở gan, tích lũy ở suy gan nặng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ istradefylline",
                    "effect": "Tăng nồng độ istradefylline, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều istradefylline. Theo dõi dấu hiệu tác dụng phụ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ istradefylline",
                    "effect": "Giảm nồng độ istradefylline, giảm hiệu quả",
                    "management": "Thận trọng. Có thể cần tăng liều istradefylline. Theo dõi đáp ứng điều trị."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng istradefylline",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH (tích lũy, tăng nguy cơ tác dụng phụ)"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình - thận trọng, theo dõi chức năng gan",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Istradefylline là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Istradefylline bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ về dấu hiệu buồn nôn, chóng mặt."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, theo dõi chức năng gan chặt chẽ",
            "severe": "CHỐNG CHỈ ĐỊNH. Istradefylline chuyển hóa ở gan, tích lũy ở suy gan nặng.",
            "notes": "Istradefylline chuyển hóa ở gan (CYP1A1, CYP3A4) và thải trừ qua gan (90%). Suy gan nặng có thể làm tích lũy istradefylline, tăng nguy cơ tác dụng phụ. CHỐNG CHỈ ĐỊNH ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Dyskinesia nặng",
                "Ảo giác, lú lẫn nặng",
                "Buồn nôn, nôn nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay istradefylline",
                "Điều trị triệu chứng:",
                "  - Antiemetic cho buồn nôn, nôn",
                "  - Antipsychotic cho ảo giác (thận trọng, có thể làm nặng Parkinson)",
                "Theo dõi: Dấu hiệu sinh tồn, dấu hiệu ảo giác, dyskinesia"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu ảo giác, dyskinesia trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (do half-life dài - 83 giờ)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng bởi thức ăn.",
                "timing": "20mg PO x 1 lần/ngày. Có thể tăng đến 40mg sau 2 tuần nếu cần. Uống cùng thời điểm mỗi ngày. Không ngừng đột ngột - giảm dần dần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Istradefylline (Nourianz)",
                "UpToDate - Istradefylline: Drug Information",
                "Medscape - Istradefylline Drug Reference",
                "MDS Guidelines - Parkinson's Disease Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "reversal_agents": {
                  "available": False,
                  "agents": []
              },
},
    "Levodopa/Carbidopa": {
        "group": "Neurology - Antiparkinsonian (Dopamine Precursor + DOPA Decarboxylase Inhibitor)",
        "vietnamese_name": "Levodopa/Carbidopa, Sinemet",
        "administration": ["PO"],
        "indications": [
            "Parkinson's disease",
            "Parkinsonism (secondary)",
            "Restless legs syndrome - off-label"
        ],
        "contraindications": [
            "Dị ứng",
            "Glaucoma góc đóng",
            "Melanoma ác tính (hoặc tiền sử)",
            "Dùng với MAO inhibitors không chọn lọc (trong 14 ngày)",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_parkinson": "Bắt đầu: 25/100mg (levodopa/carbidopa) x 3 lần/ngày, tăng dần đến 25/250mg hoặc 50/200mg x 3-4 lần/ngày",
            "adult_max": "200/2000mg/ngày (levodopa/carbidopa)",
            "notes": "Levodopa là tiền chất dopamine, carbidopa ức chế DOPA decarboxylase ngoại biên. Dùng với thức ăn để giảm buồn nôn. Tránh protein cao (giảm hấp thu)."
        },
        "side_effects": [
            "Buồn nôn, nôn (phổ biến khi bắt đầu)",
            "Chóng mặt",
            "Rối loạn vận động (dyskinesia) - phổ biến với dùng dài ngày",
            "Tác dụng dao động (wearing-off, on-off) - phổ biến với dùng dài ngày",
            "Ảo giác (đặc biệt ở người cao tuổi)",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Hạ huyết áp tư thế",
            "Rối loạn giấc ngủ",
            "Rối loạn hành vi (impulse control disorders) - hiếm"
        ],
        "interactions": [
            "MAO inhibitors không chọn lọc: CHỐNG CHỈ ĐỊNH - tăng nguy cơ tăng huyết áp nặng",
            "Protein cao: giảm hấp thu levodopa",
            "Pyridoxine (vitamin B6): giảm hiệu quả (nếu không có carbidopa)",
            "Antipsychotics: giảm hiệu quả (đối kháng dopamine)",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "Iron supplements: giảm hấp thu levodopa"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Levodopa là tiền chất dopamine, được chuyển hóa thành dopamine trong não bởi DOPA decarboxylase. Dopamine không thể qua hàng rào máu-não (blood-brain barrier), nhưng levodopa có thể. Carbidopa là DOPA decarboxylase inhibitor ngoại biên, ức chế chuyển hóa levodopa thành dopamine ở ngoại biên (giảm tác dụng phụ ngoại biên như buồn nôn, nôn) và tăng lượng levodopa đến não (tăng hiệu quả). Tác dụng: điều trị Parkinson's disease và parkinsonism. Tác dụng phụ: buồn nôn, nôn (phổ biến khi bắt đầu), rối loạn vận động (dyskinesia) - phổ biến với dùng dài ngày, tác dụng dao động (wearing-off, on-off) - phổ biến với dùng dài ngày, ảo giác (đặc biệt ở người cao tuổi).",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng Parkinson (run, cứng, chậm vận động), cải thiện chức năng vận động",
            "Rối loạn vận động (dyskinesia) - phổ biến với dùng dài ngày, có thể cần giảm liều",
            "Tác dụng dao động (wearing-off, on-off) - phổ biến với dùng dài ngày, có thể cần điều chỉnh liều hoặc thêm thuốc khác",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục",
            "Tương tác với MAO inhibitors (CHỐNG CHỈ ĐỊNH), protein cao, antipsychotics"
        ],
        "precautions": [
            "Buồn nôn, nôn - phổ biến khi bắt đầu, dùng với thức ăn, có thể dùng domperidone nếu cần",
            "Rối loạn vận động (dyskinesia) - phổ biến với dùng dài ngày, có thể cần giảm liều",
            "Tác dụng dao động (wearing-off, on-off) - phổ biến với dùng dài ngày, có thể cần điều chỉnh liều, thêm thuốc khác (COMT inhibitors, MAO-B inhibitors), hoặc dùng dạng extended release",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều hoặc thêm quetiapine/clozapine (atypical antipsychotics)",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors không chọn lọc (trong 14 ngày) - tăng nguy cơ tăng huyết áp nặng",
            "Tránh protein cao - giảm hấp thu levodopa, dùng levodopa 30-60 phút trước hoặc sau bữa ăn",
            "Tránh antipsychotics - giảm hiệu quả (đối kháng dopamine)",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Thận trọng khi dùng với iron supplements - giảm hấp thu levodopa, dùng cách nhau 2 giờ",
            "Dạng extended release - dùng cho tác dụng dao động, uống 1-2 lần/ngày, hấp thu chậm hơn"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (levodopa)",
            "onset": "30-60 phút (PO)",
            "duration": "3-5 giờ (PO), 4-6 giờ (extended release)",
            "protein_binding": "Minimal",
            "clearance": "Gan: chuyển hóa levodopa qua DOPA decarboxylase (ngoại biên và trung ương), COMT, MAO. Carbidopa ức chế DOPA decarboxylase ngoại biên. Thận: bài tiết một phần nguyên dạng và metabolites."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release: bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ rối loạn vận động (dyskinesia) với dùng dài ngày. Nguy cơ ảo giác, lú lẫn, đặc biệt ở người cao tuổi. Nguy cơ rối loạn hành vi (impulse control disorders).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors không chọn lọc (Phenelzine, Tranylcypromine)",
                    "mechanism": "Ức chế chuyển hóa dopamine qua MAO, tăng nồng độ dopamine, tăng nguy cơ tăng huyết áp nặng",
                    "effect": "Tăng huyết áp nặng, đau đầu, đột quỵ (nguy hiểm)",
                    "management": "CHỐNG CHỈ ĐỊNH - không được dùng cùng. Ngừng MAO inhibitors ít nhất 14 ngày trước khi dùng levodopa/carbidopa."
                },
                {
                    "drug": "Antipsychotics (Haloperidol, Risperidone, Olanzapine)",
                    "mechanism": "Đối kháng thụ thể dopamine D2, giảm hiệu quả levodopa",
                    "effect": "Giảm hiệu quả levodopa, tăng triệu chứng Parkinson",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc (ảo giác), dùng quetiapine hoặc clozapine (atypical antipsychotics ít đối kháng D2 hơn)."
                }
            ],
            "moderate": [
                {
                    "drug": "Protein cao",
                    "mechanism": "Cạnh tranh hấp thu với levodopa ở ruột",
                    "effect": "Giảm hấp thu levodopa, giảm hiệu quả",
                    "management": "Dùng levodopa 30-60 phút trước hoặc sau bữa ăn. Tránh bữa ăn giàu protein."
                },
                {
                    "drug": "Iron supplements",
                    "mechanism": "Giảm hấp thu levodopa ở ruột",
                    "effect": "Giảm hấp thu levodopa, giảm hiệu quả",
                    "management": "Dùng cách nhau 2 giờ. Tránh dùng cùng lúc."
                },
                {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng levodopa, carbidopa hoặc các thành phần khác",
                "Glaucoma góc đóng - tăng nhãn áp",
                "Melanoma ác tính (hoặc tiền sử) - levodopa có thể kích thích tăng trưởng melanoma",
                "Dùng với MAO inhibitors không chọn lọc (trong 14 ngày) - tăng nguy cơ tăng huyết áp nặng",
                "Suy tim nặng - tăng nguy cơ rối loạn nhịp tim"
            ],
            "tương_đối": [
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh tâm thần (ảo giác, lú lẫn) - tăng nguy cơ ảo giác, lú lẫn",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, ảo giác, lú lẫn, giảm liều 25-50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với antipsychotics - giảm hiệu quả",
                "Dùng với protein cao - giảm hấp thu levodopa",
                "Dùng với iron supplements - giảm hấp thu levodopa"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Levodopa và carbidopa bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, theo dõi tác dụng phụ",
            "severe": "Thận trọng, giảm liều 25-50%, theo dõi tác dụng phụ chặt chẽ",
            "notes": "Levodopa và carbidopa chuyển hóa ở gan. Suy gan có thể ảnh hưởng đến chuyển hóa, nhưng ít tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: rối loạn vận động nặng (dyskinesia), ảo giác, lú lẫn, kích động",
                "Rối loạn tim mạch: tăng huyết áp (nếu dùng với MAO inhibitors), hạ huyết áp, rối loạn nhịp tim",
                "Rối loạn tiêu hóa: buồn nôn, nôn nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Có thể dùng pyridoxine (vitamin B6) để tăng chuyển hóa levodopa ngoại biên (giảm nồng độ levodopa đến não).",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Pyridoxine (vitamin B6): 50-100mg PO/IV để tăng chuyển hóa levodopa ngoại biên (giảm nồng độ levodopa đến não)",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp",
                "Xử trí tăng huyết áp: nếu dùng với MAO inhibitors, dùng phentolamine hoặc nitroprusside",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Xử trí rối loạn vận động: giảm liều hoặc ngừng levodopa tạm thời",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp, rối loạn vận động"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Dùng với thức ăn để giảm buồn nôn, nôn. Tránh bữa ăn giàu protein (giảm hấp thu levodopa). Dùng levodopa 30-60 phút trước hoặc sau bữa ăn.",
                "timing": "Chia 3-4 lần/ngày. Uống cùng thời điểm mỗi ngày. Dạng extended release: uống 1-2 lần/ngày, hấp thu chậm hơn. KHÔNG nghiền hoặc nhai viên extended release (phải uống nguyên viên)."
            },
            "im": {
                "reconstitution": "Không có dạng IM",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
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
                "Lexicomp - Levodopa/Carbidopa",
                "UpToDate - Levodopa/Carbidopa: Drug information",
                "FDA - Sinemet (levodopa/carbidopa) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },
    "Opicapone": {
        "group": "Neurology - Antiparkinsonian (COMT Inhibitor)",
        "vietnamese_name": "Opicapone, Ongentys",
        "administration": ["PO"],
        "indications": [
            "Parkinson's disease - điều trị bổ sung với levodopa/carbidopa",
            "Giảm 'off' time (thời gian không đáp ứng với levodopa)",
            "Tăng 'on' time (thời gian đáp ứng với levodopa)"
        ],
        "contraindications": [
            "Dị ứng opicapone",
            "Pheochromocytoma - CHỐNG CHỈ ĐỊNH",
            "Dùng với non-selective MAO inhibitors (trong 14 ngày) - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_standard": "50mg PO x 1 lần/ngày (buổi tối, trước khi đi ngủ)",
            "notes": "Opicapone là COMT inhibitor, ức chế catechol-O-methyltransferase. Dùng 1 lần/ngày, buổi tối, trước khi đi ngủ. Uống với hoặc không thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, giảm liều nếu cần"
        },
        "side_effects": [
            "Dyskinesia (rối loạn vận động) - phổ biến",
            "Tăng transaminase (ALT, AST) - phổ biến",
            "Buồn nôn",
            "Chóng mặt",
            "Mất ngủ",
            "Tăng creatine kinase (CK) - hiếm",
            "Rhabdomyolysis - hiếm nhưng nghiêm trọng",
            "Ảo giác - hiếm",
            "Rối loạn hành vi (impulse control disorders) - hiếm"
        ],
        "interactions": [
            "Non-selective MAO inhibitors: CHỐNG CHỈ ĐỊNH - tăng nguy cơ tăng huyết áp nặng",
            "Levodopa: tăng nồng độ levodopa (tác dụng mong muốn, nhưng có thể tăng dyskinesia)",
            "UDP-glucuronosyltransferase (UGT) inhibitors: tăng nồng độ opicapone"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Opicapone là COMT inhibitor (catechol-O-methyltransferase inhibitor), ức chế enzyme COMT ở ngoại biên và não. COMT chuyển hóa levodopa thành 3-O-methyldopa (không hoạt động) và dopamine thành 3-methoxytyramine. Ức chế COMT → giảm chuyển hóa levodopa và dopamine → tăng nồng độ levodopa và dopamine trong não → tăng hiệu quả levodopa. Dẫn đến: giảm 'off' time và tăng 'on' time với levodopa. ĐẶC ĐIỂM: (1) COMT inhibitor (tương tự entacapone, tolcapone), (2) Dùng 1 lần/ngày, buổi tối (ưu điểm so với entacapone - q8h), (3) Giảm 'off' time và tăng 'on' time với levodopa, (4) Dyskinesia phổ biến (có thể cần giảm liều levodopa), (5) Tăng transaminase phổ biến - theo dõi chức năng gan, (6) Nguy cơ rhabdomyolysis - hiếm nhưng nghiêm trọng.",
        "monitoring": [
            "Đáp ứng điều trị: giảm 'off' time, tăng 'on' time với levodopa",
            "Dyskinesia - phổ biến, có thể cần giảm liều levodopa",
            "Chức năng gan (ALT, AST) - QUAN TRỌNG: theo dõi định kỳ (tăng transaminase phổ biến)",
            "Creatine kinase (CK) - theo dõi nếu có dấu hiệu rhabdomyolysis (đau cơ, yếu cơ, nước tiểu sẫm màu)",
            "Dấu hiệu rhabdomyolysis - hiếm nhưng nghiêm trọng: đau cơ, yếu cơ, nước tiểu sẫm màu, tăng CK",
            "Dấu hiệu ảo giác, lú lẫn - hiếm",
            "Dấu hiệu rối loạn hành vi (impulse control disorders) - hiếm"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với non-selective MAO inhibitors (trong 14 ngày) - tăng nguy cơ tăng huyết áp nặng",
            "CHỐNG CHỈ ĐỊNH ở pheochromocytoma - tăng nguy cơ tăng huyết áp nặng",
            "Dyskinesia phổ biến - có thể cần giảm liều levodopa",
            "Tăng transaminase phổ biến - theo dõi chức năng gan định kỳ",
            "Nguy cơ rhabdomyolysis - hiếm nhưng nghiêm trọng, theo dõi CK nếu có dấu hiệu",
            "Dùng 1 lần/ngày, buổi tối, trước khi đi ngủ",
            "Uống với hoặc không thức ăn",
            "Không ngừng đột ngột - giảm dần dần"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (ngắn), nhưng tác dụng ức chế COMT kéo dài 24 giờ",
            "onset": "Vài ngày đến 1 tuần",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "99.9%",
            "metabolism": "Chuyển hóa ở gan (UGT1A9, UGT2B7)",
            "clearance": "Thải trừ qua thận (50%) và phân (50%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với non-selective MAO inhibitors trong 14 ngày. CHỐNG CHỈ ĐỊNH ở pheochromocytoma. Tăng transaminase phổ biến - theo dõi chức năng gan định kỳ. Nguy cơ rhabdomyolysis - hiếm nhưng nghiêm trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Non-selective MAO Inhibitors (Phenelzine, Tranylcypromine, Isocarboxazid)",
                    "mechanism": "Cả hai đều ức chế chuyển hóa catecholamine, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tăng huyết áp nặng, đe dọa tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng opicapone trong 14 ngày sau khi ngừng non-selective MAO inhibitor."
                }
            ],
            "moderate": [
                {
                    "drug": "UDP-glucuronosyltransferase (UGT) Inhibitors",
                    "mechanism": "Ức chế UGT, tăng nồng độ opicapone",
                    "effect": "Tăng nồng độ opicapone, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi dấu hiệu tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng opicapone",
                "Pheochromocytoma - CHỐNG CHỈ ĐỊNH (tăng nguy cơ tăng huyết áp nặng)",
                "Dùng với non-selective MAO inhibitors (trong 14 ngày) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ tăng huyết áp nặng)"
            ],
            "tương_đối": [
                "Suy gan nặng - thận trọng, tăng nguy cơ tăng transaminase",
                "Suy thận nặng - thận trọng, giảm liều nếu cần",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Opicapone là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Opicapone bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ về dấu hiệu buồn nôn, chóng mặt."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, theo dõi chức năng gan chặt chẽ",
            "severe": "Thận trọng, theo dõi chức năng gan chặt chẽ, có thể cần giảm liều",
            "notes": "Opicapone chuyển hóa ở gan (UGT1A9, UGT2B7). Suy gan có thể làm tích lũy opicapone, tăng nguy cơ tăng transaminase. Theo dõi chức năng gan chặt chẽ ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Dyskinesia nặng",
                "Tăng transaminase nặng",
                "Rhabdomyolysis - đau cơ, yếu cơ, nước tiểu sẫm màu, tăng CK",
                "Tăng huyết áp nặng (nếu dùng với MAO inhibitor)",
                "Ảo giác, lú lẫn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay opicapone",
                "Nếu rhabdomyolysis:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Theo dõi CK, creatinine, myoglobin",
                "  - Lọc máu nếu cần",
                "Nếu tăng huyết áp nặng:",
                "  - Phentolamine 5-10mg IV",
                "  - Nitroprusside IV nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng gan, CK, dấu hiệu rhabdomyolysis"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan (ALT, AST), CK, dấu hiệu rhabdomyolysis (đau cơ, yếu cơ, nước tiểu sẫm màu) trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có rhabdomyolysis."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng bởi thức ăn.",
                "timing": "50mg PO x 1 lần/ngày, buổi tối, trước khi đi ngủ. Uống cùng thời điểm mỗi ngày. Không ngừng đột ngột - giảm dần dần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Opicapone (Ongentys)",
                "UpToDate - Opicapone: Drug Information",
                "Medscape - Opicapone Drug Reference",
                "MDS Guidelines - Parkinson's Disease Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "reversal_agents": {
                  "available": False,
                  "agents": []
              },
},
    
    "Pimavanserin": {
        "group": "Neurology - Antiparkinsonian (5-HT2A Inverse Agonist)",
        "vietnamese_name": "Pimavanserin, Nuplazid",
        "administration": ["PO"],
        "indications": [
            "Ảo giác và hoang tưởng trong bệnh Parkinson (Parkinson's disease psychosis)",
            "Ảo giác và hoang tưởng trong bệnh Alzheimer (Alzheimer's disease psychosis) - off-label"
        ],
        "contraindications": [
            "Dị ứng pimavanserin hoặc bất kỳ thành phần nào",
            "Suy gan nặng (Child-Pugh class C)",
            "Suy thận nặng (eGFR <30 ml/min/1.73m²)"
        ],
        "dosage": {
            "adult": "34mg PO mỗi ngày (1 viên)",
            "notes": "Uống với thức ăn. Không nghiền hoặc nhai viên (phải uống nguyên viên). Bắt đầu với liều 34mg/ngày. Không cần điều chỉnh liều ở người cao tuổi."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều 50% (17mg/ngày)",
            "under_30": "CHỐNG CHỈ ĐỊNH"
        },
        "side_effects": [
            "Buồn nôn - phổ biến",
            "Phù ngoại biên - phổ biến",
            "Lú lẫn - phổ biến",
            "Ảo giác - có thể xảy ra (paradoxical)",
            "Rối loạn nhịp tim (QT kéo dài) - NGUY HIỂM",
            "Tử vong - tăng nguy cơ ở bệnh nhân sa sút trí tuệ",
            "Đau đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "CYP3A4 inhibitors mạnh (ketoconazole, clarithromycin): TĂNG nguy cơ QT kéo dài - TRÁNH",
            "CYP3A4 inducers (rifampin, carbamazepine): giảm hiệu quả - tăng liều",
            "Thuốc kéo dài QT (amiodarone, sotalol): TĂNG nguy cơ QT kéo dài - TRÁNH",
            "Thuốc chống đông (warfarin): có thể tăng INR - theo dõi"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Pimavanserin là chất đối vận nghịch (inverse agonist) chọn lọc thụ thể 5-HT2A (serotonin 2A receptor). Trong bệnh Parkinson, ảo giác và hoang tưởng thường do mất cân bằng dopamine và serotonin. Các thuốc chống loạn thần truyền thống (antipsychotics) ức chế thụ thể dopamine D2 → giảm ảo giác nhưng làm nặng triệu chứng Parkinson. Pimavanserin ức chế thụ thể 5-HT2A (không ảnh hưởng D2) → giảm ảo giác và hoang tưởng mà không làm nặng triệu chứng Parkinson. Dẫn đến: cải thiện ảo giác và hoang tưởng trong bệnh Parkinson mà không làm nặng triệu chứng vận động. Pimavanserin được dùng để điều trị ảo giác và hoang tưởng trong bệnh Parkinson.",
        "monitoring": [
            "Ảo giác và hoang tưởng - đánh giá hiệu quả điều trị",
            "Triệu chứng Parkinson - đảm bảo không làm nặng",
            "ECG (QT interval) - QUAN TRỌNG: theo dõi trước và trong điều trị, đặc biệt khi dùng với thuốc kéo dài QT",
            "Chức năng gan (ALT, AST) - mỗi 3-6 tháng",
            "Chức năng thận (creatinine, eGFR) - trước khi bắt đầu và định kỳ",
            "Dấu hiệu lú lẫn, ảo giác (paradoxical)",
            "Dấu hiệu phù ngoại biên"
        ],
        "precautions": [
            "THEO DÕI ECG (QT INTERVAL) - tăng nguy cơ QT kéo dài, đặc biệt khi dùng với thuốc kéo dài QT",
            "TRÁNH DÙNG VỚI CYP3A4 INHIBITORS MẠNH - tăng nguy cơ QT kéo dài",
            "TRÁNH DÙNG VỚI THUỐC KÉO DÀI QT - tăng nguy cơ rối loạn nhịp tim",
            "Tăng nguy cơ tử vong ở bệnh nhân sa sút trí tuệ - thận trọng",
            "Có thể gây ảo giác (paradoxical) - ngừng nếu xảy ra",
            "Lú lẫn - phổ biến, theo dõi",
            "Phù ngoại biên - phổ biến, theo dõi",
            "Giảm liều 50% ở suy thận vừa (eGFR 30-60)",
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (eGFR <30) và suy gan nặng"
        ],
        "pharmacokinetics": {
            "half_life": "57 giờ (dao động 40-80 giờ)",
            "onset": "Vài tuần",
            "duration": "24 giờ (liều mỗi ngày)",
            "protein_binding": ">95%",
            "metabolism": "Chuyển hóa ở gan qua CYP3A4 và CYP2J2",
            "clearance": "Chuyển hóa ở gan, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Không nghiền hoặc nhai viên (phải uống nguyên viên).",
        "black_box_warnings": "TĂNG NGUY CƠ TỬ VONG Ở BỆNH NHÂN SA SÚT TRÍ TUỆ - tăng nguy cơ tử vong ở bệnh nhân sa sút trí tuệ. QT KÉO DÀI - tăng nguy cơ rối loạn nhịp tim. TRÁNH dùng với CYP3A4 inhibitors mạnh và thuốc kéo dài QT.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 inhibitors mạnh (ketoconazole, clarithromycin, itraconazole)",
                    "mechanism": "Ức chế chuyển hóa pimavanserin, tăng nồng độ, tăng nguy cơ QT kéo dài",
                    "effect": "Tăng nguy cơ QT kéo dài, rối loạn nhịp tim (nguy hiểm)",
                    "management": "TRÁNH dùng cùng. Nếu bắt buộc, giảm liều pimavanserin 50% và theo dõi ECG chặt chẽ."
                },
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, sotalol, haloperidol, quetiapine)",
                    "mechanism": "Tác dụng cộng dồn kéo dài QT",
                    "effect": "Tăng nguy cơ QT kéo dài, rối loạn nhịp tim (nguy hiểm)",
                    "management": "TRÁNH dùng cùng. Nếu bắt buộc, theo dõi ECG chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa pimavanserin, giảm nồng độ",
                    "effect": "Giảm hiệu quả pimavanserin",
                    "management": "Có thể cần tăng liều pimavanserin. Theo dõi hiệu quả."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Pimavanserin có thể ảnh hưởng đến đông máu",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên khi bắt đầu pimavanserin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng pimavanserin hoặc bất kỳ thành phần nào",
                "Suy gan nặng (Child-Pugh class C)",
                "Suy thận nặng (eGFR <30 ml/min/1.73m²)"
            ],
            "tương_đối": [
                "Suy thận vừa (eGFR 30-60) - giảm liều 50%",
                "Suy gan vừa - thận trọng",
                "QT kéo dài - tăng nguy cơ",
                "Sa sút trí tuệ - tăng nguy cơ tử vong",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Pimavanserin là FDA category C. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Caution",
                "details": "Pimavanserin bài tiết vào sữa mẹ. Chưa rõ an toàn cho trẻ sơ sinh.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi tác dụng phụ",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Pimavanserin chuyển hóa ở gan qua CYP3A4. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Lú lẫn nặng",
                "Ảo giác",
                "QT kéo dài, rối loạn nhịp tim",
                "Buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "ECG - theo dõi QT interval",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp",
                "Xử trí rối loạn nhịp tim nếu có",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp, ECG (QT interval)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu.",
                "timing": "Uống 1 lần/ngày, cùng thời điểm mỗi ngày. KHÔNG nghiền hoặc nhai viên (phải uống nguyên viên)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pimavanserin (Nuplazid)",
                "UpToDate - Pimavanserin: Drug information",
                "Lexicomp - Pimavanserin monograph",
                "AAN Guidelines - Parkinson's Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, clinical trial data, widely used"
        }
    },
    
    "Pramipexole": {
        "group": "Neurology - Antiparkinsonian (Dopamine Agonist)",
        "vietnamese_name": "Pramipexole, Mirapex",
        "administration": ["PO"],
        "indications": [
            "Parkinson's disease",
            "Restless legs syndrome (RLS)"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_parkinson": "0.125mg x 3 lần/ngày, tăng dần mỗi 5-7 ngày đến 1.5mg x 3 lần/ngày (tối đa 4.5mg/ngày)",
            "adult_rls": "0.125mg trước khi ngủ, tăng dần đến 0.5mg trước khi ngủ (tối đa 0.5mg/ngày)",
            "adult_max": "4.5mg/ngày (Parkinson), 0.5mg/ngày (RLS)",
            "notes": "Dopamine agonist (D2, D3). Tác dụng dài. Tăng liều chậm để giảm tác dụng phụ. Dạng extended release: uống 1 lần/ngày."
        },
        "side_effects": [
            "Buồn nôn (phổ biến khi bắt đầu)",
            "Chóng mặt",
            "Buồn ngủ (phổ biến)",
            "Hạ huyết áp tư thế",
            "Ảo giác (đặc biệt ở người cao tuổi)",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Rối loạn hành vi (impulse control disorders) - hiếm: cờ bạc, mua sắm, tình dục",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm",
            "Rối loạn vận động (dyskinesia) - ít hơn levodopa"
        ],
        "interactions": [
            "Antipsychotics: giảm hiệu quả (đối kháng dopamine)",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "Cimetidine: tăng nồng độ pramipexole",
            "Quinidine: tăng nồng độ pramipexole"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Pramipexole là dopamine agonist, kích thích trực tiếp thụ thể dopamine D2 và D3 trong não. Khác với levodopa (tiền chất dopamine), pramipexole không cần chuyển hóa và có tác dụng dài hơn. Pramipexole ưu tiên kích thích thụ thể D3 (nhiều hơn D2), có thể giải thích tác dụng tốt hơn với các triệu chứng không vận động (non-motor symptoms) như trầm cảm, lo âu. Tác dụng: điều trị Parkinson's disease và restless legs syndrome (RLS). Có dạng immediate release (IR) và extended release (XR). Tác dụng phụ: buồn nôn (phổ biến khi bắt đầu), buồn ngủ (phổ biến), ảo giác (đặc biệt ở người cao tuổi), rối loạn hành vi (impulse control disorders) - hiếm, buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm.",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng Parkinson (run, cứng, chậm vận động), cải thiện chức năng vận động",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm, cảnh báo bệnh nhân",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục",
            "Tương tác với antipsychotics (giảm hiệu quả), antihypertensives, cimetidine, quinidine"
        ],
        "precautions": [
            "Buồn nôn - phổ biến khi bắt đầu, dùng với thức ăn, có thể dùng domperidone nếu cần",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm, cảnh báo bệnh nhân, tránh lái xe nếu có tiền sử",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều hoặc thêm quetiapine/clozapine (atypical antipsychotics)",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục, giảm liều hoặc ngừng nếu có",
            "Tránh antipsychotics - giảm hiệu quả (đối kháng dopamine)",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Thận trọng khi dùng với cimetidine hoặc quinidine - tăng nồng độ pramipexole, giảm liều pramipexole 25-50%",
            "Tăng liều chậm (mỗi 5-7 ngày) để giảm tác dụng phụ",
            "Dạng extended release (XR) - uống 1 lần/ngày, thuận tiện hơn, không nghiền hoặc nhai (phải uống nguyên viên)"
        ],
        "pharmacokinetics": {
            "half_life": "8-12 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "8-12 giờ (PO), 24 giờ (XR)",
            "protein_binding": "15%",
            "clearance": "Thận: bài tiết chủ yếu nguyên dạng (90%). Gan: chuyển hóa một phần. Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release (XR): bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ buồn ngủ đột ngột (sleep attacks) - có thể xảy ra mà không có dấu hiệu cảnh báo, nguy hiểm khi lái xe hoặc vận hành máy móc. Nguy cơ ảo giác, lú lẫn, đặc biệt ở người cao tuổi. Nguy cơ rối loạn hành vi (impulse control disorders).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antipsychotics (Haloperidol, Risperidone, Olanzapine)",
                    "mechanism": "Đối kháng thụ thể dopamine D2, giảm hiệu quả pramipexole",
                    "effect": "Giảm hiệu quả pramipexole, tăng triệu chứng Parkinson",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc (ảo giác), dùng quetiapine hoặc clozapine (atypical antipsychotics ít đối kháng D2 hơn)."
                }
            ],
            "moderate": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế thải trừ pramipexole qua thận, tăng nồng độ pramipexole",
                    "effect": "Tăng nồng độ pramipexole, tăng tác dụng phụ",
                    "management": "Giảm liều pramipexole 25-50% khi dùng với cimetidine. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Quinidine",
                    "mechanism": "Ức chế thải trừ pramipexole qua thận, tăng nồng độ pramipexole",
                    "effect": "Tăng nồng độ pramipexole, tăng tác dụng phụ",
                    "management": "Giảm liều pramipexole 25-50% khi dùng với quinidine. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng pramipexole hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Bệnh thận (CrCl <60) - giảm thải trừ, tăng nguy cơ tích lũy, giảm liều",
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh tâm thần (ảo giác, lú lẫn) - tăng nguy cơ ảo giác, lú lẫn",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, ảo giác, lú lẫn, giảm liều 25-50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với antipsychotics - giảm hiệu quả",
                "Dùng với cimetidine hoặc quinidine - giảm liều pramipexole"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Pramipexole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Thận trọng, theo dõi tác dụng phụ",
            "notes": "Pramipexole chuyển hóa một phần ở gan. Suy gan ít ảnh hưởng đến nồng độ pramipexole."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "under_30": "Giảm liều 50-75%, theo dõi tác dụng phụ chặt chẽ",
            "notes": "Pramipexole bài tiết chủ yếu qua thận (90% nguyên dạng). Suy thận làm giảm thải trừ, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, ảo giác, lú lẫn, kích động",
                "Rối loạn tim mạch: hạ huyết áp, nhịp chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Xử trí nhịp chậm: Atropine nếu cần",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": "Dạng immediate release (IR): chia 3 lần/ngày. Dạng extended release (XR): uống 1 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm (mỗi 5-7 ngày) để giảm tác dụng phụ. KHÔNG nghiền hoặc nhai viên XR (phải uống nguyên viên)."
            },
            "im": {
                "reconstitution": "Không có dạng IM",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
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
                "Lexicomp - Pramipexole",
                "UpToDate - Pramipexole: Drug information",
                "FDA - Mirapex (pramipexole) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },
    "Ropinirole": {
        "group": "Neurology - Antiparkinsonian (Dopamine Agonist)",
        "vietnamese_name": "Ropinirole, Requip",
        "administration": ["PO"],
        "indications": [
            "Parkinson's disease",
            "Restless legs syndrome (RLS)"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_parkinson": "0.25mg x 3 lần/ngày, tăng dần mỗi 7 ngày đến 1-3mg x 3 lần/ngày (tối đa 24mg/ngày)",
            "adult_rls": "0.25mg trước khi ngủ, tăng dần đến 4mg trước khi ngủ (tối đa 4mg/ngày)",
            "adult_max": "24mg/ngày (Parkinson), 4mg/ngày (RLS)",
            "notes": "Dopamine agonist (D2, D3). Tác dụng trung bình. Tăng liều chậm để giảm tác dụng phụ. Dạng extended release: uống 1 lần/ngày."
        },
        "side_effects": [
            "Buồn nôn (phổ biến khi bắt đầu)",
            "Chóng mặt",
            "Buồn ngủ (phổ biến)",
            "Hạ huyết áp tư thế",
            "Ảo giác (đặc biệt ở người cao tuổi)",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Rối loạn hành vi (impulse control disorders) - hiếm: cờ bạc, mua sắm, tình dục",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm",
            "Rối loạn vận động (dyskinesia) - ít hơn levodopa"
        ],
        "interactions": [
            "Antipsychotics: giảm hiệu quả (đối kháng dopamine)",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "CYP1A2 inhibitors: tăng nồng độ ropinirole",
            "CYP1A2 inducers: giảm nồng độ ropinirole",
            "Estrogens: tăng nồng độ ropinirole"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ropinirole là dopamine agonist, kích thích trực tiếp thụ thể dopamine D2 và D3 trong não. Khác với levodopa (tiền chất dopamine), ropinirole không cần chuyển hóa và có tác dụng trung bình. Ropinirole ưu tiên kích thích thụ thể D3 (nhiều hơn D2), có thể giải thích tác dụng tốt hơn với các triệu chứng không vận động (non-motor symptoms) như trầm cảm, lo âu. Tác dụng: điều trị Parkinson's disease và restless legs syndrome (RLS). Có dạng immediate release (IR) và extended release (XR). Tác dụng phụ: buồn nôn (phổ biến khi bắt đầu), buồn ngủ (phổ biến), ảo giác (đặc biệt ở người cao tuổi), rối loạn hành vi (impulse control disorders) - hiếm, buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm.",
        "monitoring": [
            "Đáp ứng điều trị: giảm triệu chứng Parkinson (run, cứng, chậm vận động), cải thiện chức năng vận động",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm, cảnh báo bệnh nhân",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều",
            "Huyết áp - hạ huyết áp tư thế, đặc biệt khi bắt đầu hoặc tăng liều",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục",
            "Tương tác với antipsychotics (giảm hiệu quả), antihypertensives, CYP1A2 inhibitors/inducers, estrogens"
        ],
        "precautions": [
            "Buồn nôn - phổ biến khi bắt đầu, dùng với thức ăn, có thể dùng domperidone nếu cần",
            "Buồn ngủ - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, tránh lái xe hoặc vận hành máy móc",
            "Buồn ngủ đột ngột (sleep attacks) - hiếm nhưng nguy hiểm, cảnh báo bệnh nhân, tránh lái xe nếu có tiền sử",
            "Ảo giác, lú lẫn - đặc biệt ở người cao tuổi, có thể cần giảm liều hoặc thêm quetiapine/clozapine (atypical antipsychotics)",
            "Hạ huyết áp tư thế - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Rối loạn hành vi (impulse control disorders) - hiếm, theo dõi: cờ bạc, mua sắm, tình dục, giảm liều hoặc ngừng nếu có",
            "Tránh antipsychotics - giảm hiệu quả (đối kháng dopamine)",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Thận trọng khi dùng với CYP1A2 inhibitors (fluvoxamine, ciprofloxacin) - tăng nồng độ ropinirole, giảm liều ropinirole 50%",
            "Thận trọng khi dùng với CYP1A2 inducers (carbamazepine, smoking) - giảm nồng độ ropinirole, có thể cần tăng liều",
            "Thận trọng khi dùng với estrogens - tăng nồng độ ropinirole, giảm liều ropinirole 25-50%",
            "Tăng liều chậm (mỗi 7 ngày) để giảm tác dụng phụ",
            "Dạng extended release (XR) - uống 1 lần/ngày, thuận tiện hơn, không nghiền hoặc nhai (phải uống nguyên viên)"
        ],
        "pharmacokinetics": {
            "half_life": "6 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "6-8 giờ (PO), 24 giờ (XR)",
            "protein_binding": "40%",
            "clearance": "Gan: chuyển hóa qua CYP1A2 (chính). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều khi dùng với CYP1A2 inhibitors/inducers và estrogens."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release (XR): bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ buồn ngủ đột ngột (sleep attacks) - có thể xảy ra mà không có dấu hiệu cảnh báo, nguy hiểm khi lái xe hoặc vận hành máy móc. Nguy cơ ảo giác, lú lẫn, đặc biệt ở người cao tuổi. Nguy cơ rối loạn hành vi (impulse control disorders).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antipsychotics (Haloperidol, Risperidone, Olanzapine)",
                    "mechanism": "Đối kháng thụ thể dopamine D2, giảm hiệu quả ropinirole",
                    "effect": "Giảm hiệu quả ropinirole, tăng triệu chứng Parkinson",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc (ảo giác), dùng quetiapine hoặc clozapine (atypical antipsychotics ít đối kháng D2 hơn)."
                },
                {
                    "drug": "CYP1A2 inhibitors (Fluvoxamine, Ciprofloxacin)",
                    "mechanism": "Ức chế chuyển hóa ropinirole qua CYP1A2, tăng nồng độ ropinirole",
                    "effect": "Tăng nồng độ ropinirole, tăng tác dụng phụ (buồn ngủ, ảo giác)",
                    "management": "Giảm liều ropinirole 50% khi dùng với CYP1A2 inhibitors. Theo dõi tác dụng phụ chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP1A2 inducers (Carbamazepine, Smoking)",
                    "mechanism": "Cảm ứng chuyển hóa ropinirole qua CYP1A2, giảm nồng độ ropinirole",
                    "effect": "Giảm nồng độ ropinirole, giảm hiệu quả",
                    "management": "Tăng liều ropinirole 50-100% khi dùng với carbamazepine hoặc ở người hút thuốc. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Estrogens",
                    "mechanism": "Ức chế chuyển hóa ropinirole, tăng nồng độ ropinirole",
                    "effect": "Tăng nồng độ ropinirole, tăng tác dụng phụ",
                    "management": "Giảm liều ropinirole 25-50% khi dùng với estrogens. Theo dõi tác dụng phụ."
                },
                {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ropinirole hoặc các thành phần khác"
            ],
            "tương_đối": [
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy",
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ rối loạn nhịp tim",
                "Bệnh tâm thần (ảo giác, lú lẫn) - tăng nguy cơ ảo giác, lú lẫn",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, ảo giác, lú lẫn, giảm liều 25-50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với antipsychotics - giảm hiệu quả",
                "Dùng với CYP1A2 inhibitors - giảm liều ropinirole",
                "Dùng với CYP1A2 inducers hoặc hút thuốc - tăng liều ropinirole",
                "Dùng với estrogens - giảm liều ropinirole"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Ropinirole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, theo dõi tác dụng phụ",
            "severe": "Giảm liều 25-50%, theo dõi tác dụng phụ chặt chẽ",
            "notes": "Ropinirole chuyển hóa ở gan qua CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, ảo giác, lú lẫn, kích động",
                "Rối loạn tim mạch: hạ huyết áp, nhịp chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Xử trí nhịp chậm: Atropine nếu cần",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": "Dạng immediate release (IR): chia 3 lần/ngày. Dạng extended release (XR): uống 1 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm (mỗi 7 ngày) để giảm tác dụng phụ. KHÔNG nghiền hoặc nhai viên XR (phải uống nguyên viên)."
            },
            "im": {
                "reconstitution": "Không có dạng IM",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
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
                "Lexicomp - Ropinirole",
                "UpToDate - Ropinirole: Drug information",
                "FDA - Requip (ropinirole) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },
    
    "Safinamide": {
        "group": "Neurology - Antiparkinsonian (MAO-B Inhibitor + Glutamate Release Inhibitor)",
        "vietnamese_name": "Safinamide, Xadago",
        "administration": ["PO"],
        "indications": [
            "Parkinson's disease - điều trị bổ sung với levodopa/carbidopa",
            "Giảm 'off' time (thời gian không đáp ứng với levodopa)",
            "Tăng 'on' time (thời gian đáp ứng với levodopa)"
        ],
        "contraindications": [
            "Dị ứng safinamide",
            "Dùng với MAO inhibitors không chọn lọc (trong 14 ngày) - CHỐNG CHỈ ĐỊNH",
            "Dùng với meperidine, tramadol, methadone, propoxyphene, dextromethorphan (trong 14 ngày) - CHỐNG CHỈ ĐỊNH",
            "Dùng với St. John's wort (trong 14 ngày) - CHỐNG CHỈ ĐỊNH",
            "Suy gan nặng - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_initial": "50mg PO x 1 lần/ngày",
            "adult_max": "100mg PO x 1 lần/ngày (tăng sau 2 tuần nếu cần)",
            "notes": "Safinamide là MAO-B inhibitor và glutamate release inhibitor. Dùng 1 lần/ngày. Bắt đầu với 50mg, có thể tăng đến 100mg sau 2 tuần nếu cần. Dùng với hoặc không thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, giảm liều nếu cần"
        },
        "side_effects": [
            "Dyskinesia (rối loạn vận động) - phổ biến",
            "Buồn nôn",
            "Mất ngủ",
            "Chóng mặt",
            "Lo lắng",
            "Tăng huyết áp - hiếm",
            "Ảo giác - hiếm",
            "Rối loạn hành vi (impulse control disorders) - hiếm"
        ],
        "interactions": [
            "MAO inhibitors không chọn lọc: CHỐNG CHỈ ĐỊNH - tăng nguy cơ tăng huyết áp nặng",
            "Meperidine, tramadol, methadone, propoxyphene, dextromethorphan: CHỐNG CHỈ ĐỊNH - tăng nguy cơ serotonin syndrome",
            "St. John's wort: CHỐNG CHỈ ĐỊNH - tăng nguy cơ serotonin syndrome",
            "SSRI/SNRI: tăng nguy cơ serotonin syndrome",
            "Tyramine: có thể tăng huyết áp (nhưng ít hơn MAO-A inhibitor)"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Safinamide là thuốc kép: (1) MAO-B inhibitor - ức chế monoamine oxidase B, giảm phân hủy dopamine, tăng nồng độ dopamine trong não, (2) Glutamate release inhibitor - ức chế giải phóng glutamate, giảm kích thích quá mức của glutamate receptors (NMDA, AMPA). Dẫn đến: tăng dopamine (giảm triệu chứng Parkinson) và giảm glutamate (giảm dyskinesia, tăng hiệu quả levodopa). ĐẶC ĐIỂM: (1) MAO-B inhibitor + glutamate release inhibitor (cơ chế kép), (2) Giảm 'off' time và tăng 'on' time với levodopa, (3) Dùng 1 lần/ngày, (4) CHỐNG CHỈ ĐỊNH với MAO inhibitors không chọn lọc và một số thuốc (meperidine, tramadol, methadone, propoxyphene, dextromethorphan), (5) Dyskinesia phổ biến, (6) CHỐNG CHỈ ĐỊNH ở suy gan nặng.",
        "monitoring": [
            "Đáp ứng điều trị: giảm 'off' time, tăng 'on' time với levodopa",
            "Dyskinesia - phổ biến, có thể cần giảm liều levodopa",
            "Huyết áp - hiếm tăng huyết áp",
            "Dấu hiệu serotonin syndrome (nếu dùng với SSRI/SNRI): kích động, tăng thân nhiệt, tăng phản xạ",
            "Dấu hiệu ảo giác, lú lẫn - hiếm",
            "Dấu hiệu rối loạn hành vi (impulse control disorders) - hiếm",
            "Chức năng gan (ALT, AST) - CHỐNG CHỈ ĐỊNH ở suy gan nặng"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors không chọn lọc (trong 14 ngày) - tăng nguy cơ tăng huyết áp nặng",
            "CHỐNG CHỈ ĐỊNH với meperidine, tramadol, methadone, propoxyphene, dextromethorphan (trong 14 ngày) - tăng nguy cơ serotonin syndrome",
            "CHỐNG CHỈ ĐỊNH với St. John's wort (trong 14 ngày) - tăng nguy cơ serotonin syndrome",
            "CHỐNG CHỈ ĐỊNH ở suy gan nặng",
            "Dyskinesia phổ biến - có thể cần giảm liều levodopa",
            "Thận trọng khi dùng với SSRI/SNRI - tăng nguy cơ serotonin syndrome",
            "Tránh tyramine cao (phô mai lên men, thịt chế biến) - có thể tăng huyết áp (nhưng ít hơn MAO-A inhibitor)",
            "Dùng 1 lần/ngày, với hoặc không thức ăn",
            "Không ngừng đột ngột - giảm dần dần"
        ],
        "pharmacokinetics": {
            "half_life": "20-26 giờ",
            "onset": "Vài ngày đến 1 tuần",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "90%",
            "metabolism": "Chuyển hóa ở gan (CYP3A4, MAO-B)",
            "clearance": "Thải trừ qua thận (50%) và phân (50%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với MAO inhibitors không chọn lọc và một số thuốc (meperidine, tramadol, methadone, propoxyphene, dextromethorphan) trong 14 ngày. CHỐNG CHỈ ĐỊNH ở suy gan nặng. Tăng nguy cơ serotonin syndrome khi dùng với SSRI/SNRI.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO Inhibitors không chọn lọc (Phenelzine, Tranylcypromine, Isocarboxazid)",
                    "mechanism": "Cả hai đều ức chế MAO, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tăng huyết áp nặng, đe dọa tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng safinamide trong 14 ngày sau khi ngừng MAO inhibitor không chọn lọc."
                },
                {
                    "drug": "Meperidine, Tramadol, Methadone, Propoxyphene, Dextromethorphan",
                    "mechanism": "Tăng giải phóng serotonin, tác dụng cộng dồn với MAO-B inhibition",
                    "effect": "Tăng nguy cơ serotonin syndrome, đe dọa tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng safinamide trong 14 ngày sau khi ngừng các thuốc này."
                },
                {
                    "drug": "St. John's Wort",
                    "mechanism": "Tăng giải phóng serotonin, tác dụng cộng dồn với MAO-B inhibition",
                    "effect": "Tăng nguy cơ serotonin syndrome",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng safinamide trong 14 ngày sau khi ngừng St. John's wort."
                }
            ],
            "moderate": [
                {
                    "drug": "SSRI/SNRI (Fluoxetine, Sertraline, Paroxetine, Venlafaxine, Duloxetine)",
                    "mechanism": "Tăng giải phóng serotonin, tác dụng cộng dồn với MAO-B inhibition",
                    "effect": "Tăng nguy cơ serotonin syndrome",
                    "management": "Thận trọng. Theo dõi dấu hiệu serotonin syndrome (kích động, tăng thân nhiệt, tăng phản xạ). Có thể cần giảm liều SSRI/SNRI hoặc tránh dùng cùng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng safinamide",
                "Dùng với MAO inhibitors không chọn lọc (trong 14 ngày) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ tăng huyết áp nặng)",
                "Dùng với meperidine, tramadol, methadone, propoxyphene, dextromethorphan (trong 14 ngày) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ serotonin syndrome)",
                "Dùng với St. John's wort (trong 14 ngày) - CHỐNG CHỈ ĐỊNH (tăng nguy cơ serotonin syndrome)",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Dùng với SSRI/SNRI - thận trọng, tăng nguy cơ serotonin syndrome",
                "Suy thận nặng - thận trọng, giảm liều nếu cần",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Safinamide là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt khi không có lựa chọn khác.",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": "Safinamide bài tiết vào sữa mẹ. Thận trọng khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Theo dõi trẻ về dấu hiệu buồn nôn, mất ngủ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng, giảm liều nếu cần",
            "severe": "CHỐNG CHỈ ĐỊNH. Safinamide chuyển hóa ở gan, tích lũy ở suy gan nặng.",
            "notes": "Safinamide chuyển hóa ở gan (CYP3A4, MAO-B). Suy gan nặng có thể làm tích lũy safinamide, tăng nguy cơ tác dụng phụ. CHỐNG CHỈ ĐỊNH ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng huyết áp nặng",
                "Serotonin syndrome (nếu dùng với SSRI/SNRI): kích động, tăng thân nhiệt, tăng phản xạ, co giật",
                "Dyskinesia nặng",
                "Ảo giác, lú lẫn"
            ],
            "antidote": "Phentolamine hoặc nitroprusside cho tăng huyết áp. Cyproheptadine cho serotonin syndrome.",
            "treatment": [
                "Ngừng ngay safinamide",
                "Nếu tăng huyết áp nặng:",
                "  - Phentolamine 5-10mg IV",
                "  - Nitroprusside IV nếu cần",
                "  - Theo dõi huyết áp chặt chẽ",
                "Nếu serotonin syndrome:",
                "  - Cyproheptadine 4-8mg PO/NG, lặp lại mỗi 4 giờ",
                "  - Hỗ trợ hô hấp nếu cần",
                "  - Điều trị co giật nếu có",
                "Theo dõi: Dấu hiệu sinh tồn, huyết áp, dấu hiệu serotonin syndrome"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, huyết áp, dấu hiệu serotonin syndrome trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Phentolamine",
                    "mechanism": "Alpha-blocker, đối kháng tác dụng tăng huyết áp",
                    "indication": "Tăng huyết áp nặng do safinamide",
                    "dose": "5-10mg IV, lặp lại nếu cần"
                },
                {
                    "agent": "Cyproheptadine",
                    "mechanism": "Serotonin antagonist, đối kháng serotonin syndrome",
                    "indication": "Serotonin syndrome do safinamide",
                    "dose": "4-8mg PO/NG, lặp lại mỗi 4 giờ"
                }
            ],
            "notes": "Phentolamine đối kháng tăng huyết áp. Cyproheptadine đối kháng serotonin syndrome."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Hấp thu không bị ảnh hưởng bởi thức ăn.",
                "timing": "50mg PO x 1 lần/ngày. Có thể tăng đến 100mg sau 2 tuần nếu cần. Uống cùng thời điểm mỗi ngày. Không ngừng đột ngột - giảm dần dần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Safinamide (Xadago)",
                "UpToDate - Safinamide: Drug Information",
                "Medscape - Safinamide Drug Reference",
                "MDS Guidelines - Parkinson's Disease Treatment"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, clinical guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Tetrabenazine": {
        "group": "Neurology - Movement Disorders (VMAT2 Inhibitor)",
        "vietnamese_name": "Tetrabenazine, Xenazine",
        "administration": ["PO"],
        "indications": [
            "Rối loạn vận động do Huntington (Huntington's disease chorea)"
        ],
        "contraindications": [
            "Dị ứng tetrabenazine",
            "Suy gan nặng",
            "Trầm cảm nặng hoặc ý tưởng tự tử",
            "Dùng với MAO inhibitors (trong 14 ngày)"
        ],
        "dosage": {
            "adult_initial": "12.5mg PO mỗi ngày, tăng dần mỗi 3-5 ngày (12.5→25→37.5→50→62.5→75→87.5→100mg/ngày) đến liều hiệu quả",
            "adult_max": "100mg/ngày (chia 3 lần)",
            "notes": "Chia 3 lần/ngày. Uống với thức ăn. Bắt đầu với liều thấp và tăng dần để giảm tác dụng phụ. Không ngừng đột ngột. Giảm liều 50% ở bệnh nhân dùng CYP2D6 inhibitors mạnh."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Buồn ngủ, mệt mỏi - phổ biến",
            "Trầm cảm - phổ biến, NGUY HIỂM",
            "Rối loạn giấc ngủ - phổ biến",
            "Lo âu - phổ biến",
            "Rối loạn nhịp tim (QT kéo dài) - NGUY HIỂM",
            "Parkinsonism - có thể xảy ra",
            "Buồn nôn",
            "Chóng mặt"
        ],
        "interactions": [
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH - tăng nguy cơ serotonin syndrome",
            "Thuốc kéo dài QT (amiodarone, sotalol): TĂNG nguy cơ QT kéo dài - TRÁNH",
            "CYP2D6 inhibitors (paroxetine, fluoxetine): tăng nồng độ - giảm liều 50%",
            "Reserpine: tăng nguy cơ tác dụng phụ - TRÁNH"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Tetrabenazine là chất ức chế VMAT2 (vesicular monoamine transporter 2). VMAT2 là protein vận chuyển monoamine (dopamine, serotonin, norepinephrine) vào túi tiết (vesicles) trong tế bào thần kinh. Ức chế VMAT2 → giảm vận chuyển monoamine vào túi tiết → giảm giải phóng monoamine → giảm hoạt động dopamine trong não → giảm rối loạn vận động (chorea). Dẫn đến: giảm rối loạn vận động trong bệnh Huntington. Tetrabenazine được dùng để điều trị rối loạn vận động do Huntington. Lưu ý: Deutetrabenazine là dạng cải tiến của tetrabenazine với deuterium substitution → half-life dài hơn, liều thấp hơn, tác dụng phụ ít hơn.",
        "monitoring": [
            "Rối loạn vận động (chorea) - đánh giá hiệu quả điều trị",
            "Trầm cảm - QUAN TRỌNG: theo dõi chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều",
            "ECG (QT interval) - theo dõi trước và trong điều trị, đặc biệt khi dùng với thuốc kéo dài QT",
            "Parkinsonism - theo dõi triệu chứng",
            "Rối loạn giấc ngủ - theo dõi",
            "Chức năng gan (ALT, AST) - mỗi 3-6 tháng",
            "Dấu hiệu serotonin syndrome (nếu dùng với MAO inhibitors)"
        ],
        "precautions": [
            "THEO DÕI TRẦM CẢM CHẶT CHẼ - tăng nguy cơ, đặc biệt khi bắt đầu hoặc tăng liều, ngừng ngay nếu có ý tưởng tự tử",
            "CHỐNG CHỈ ĐỊNH ở trầm cảm nặng hoặc ý tưởng tự tử",
            "THEO DÕI ECG (QT INTERVAL) - tăng nguy cơ QT kéo dài, đặc biệt khi dùng với thuốc kéo dài QT",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors (trong 14 ngày) - tăng nguy cơ serotonin syndrome",
            "TRÁNH dùng với reserpine - tăng nguy cơ tác dụng phụ",
            "Buồn ngủ, mệt mỏi - phổ biến, tránh lái xe hoặc vận hành máy móc",
            "Parkinsonism - có thể xảy ra, giảm liều nếu có",
            "Không ngừng đột ngột - giảm dần dần",
            "Giảm liều 50% ở bệnh nhân dùng CYP2D6 inhibitors mạnh"
        ],
        "pharmacokinetics": {
            "half_life": "5-8 giờ (dao động 3-12 giờ)",
            "onset": "Vài ngày đến vài tuần",
            "duration": "8 giờ (chia 3 lần/ngày)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa ở gan qua CYP2D6 và CYP1A2",
            "clearance": "Chuyển hóa ở gan, thải trừ qua thận một phần. Half-life ngắn hơn deutetrabenazine."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "TRẦM CẢM VÀ Ý TƯỞNG TỰ TỬ - tăng nguy cơ trầm cảm và ý tưởng tự tử. CHỐNG CHỈ ĐỊNH ở trầm cảm nặng hoặc ý tưởng tự tử. Theo dõi chặt chẽ, đặc biệt khi bắt đầu hoặc tăng liều. Ngừng ngay nếu có ý tưởng tự tử. QT KÉO DÀI - tăng nguy cơ rối loạn nhịp tim. TRÁNH dùng với thuốc kéo dài QT.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa monoamine, tăng nguy cơ serotonin syndrome",
                    "effect": "Tăng nguy cơ serotonin syndrome (nguy hiểm)",
                    "management": "CHỐNG CHỈ ĐỊNH - không được dùng cùng. Ngừng MAO inhibitors ít nhất 14 ngày trước khi dùng tetrabenazine."
                },
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, sotalol, haloperidol)",
                    "mechanism": "Tác dụng cộng dồn kéo dài QT",
                    "effect": "Tăng nguy cơ QT kéo dài, rối loạn nhịp tim (nguy hiểm)",
                    "management": "TRÁNH dùng cùng. Nếu bắt buộc, theo dõi ECG chặt chẽ."
                },
                {
                    "drug": "Reserpine",
                    "mechanism": "Tác dụng cộng dồn ức chế VMAT2",
                    "effect": "Tăng nguy cơ tác dụng phụ",
                    "management": "TRÁNH dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP2D6 inhibitors mạnh (paroxetine, fluoxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa tetrabenazine, tăng nồng độ",
                    "effect": "Tăng tác dụng phụ",
                    "management": "Giảm liều tetrabenazine 50%. Theo dõi tác dụng phụ chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tetrabenazine",
                "Suy gan nặng",
                "Trầm cảm nặng hoặc ý tưởng tự tử",
                "Dùng với MAO inhibitors (trong 14 ngày)"
            ],
            "tương_đối": [
                "Suy gan vừa - thận trọng",
                "Trầm cảm hoặc tiền sử trầm cảm - tăng nguy cơ",
                "QT kéo dài - tăng nguy cơ",
                "Parkinsonism - có thể làm nặng",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tetrabenazine là FDA category C. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Caution",
                "details": "Tetrabenazine bài tiết vào sữa mẹ. Chưa rõ an toàn cho trẻ sơ sinh.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi tác dụng phụ",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Tetrabenazine chuyển hóa ở gan qua CYP2D6 và CYP1A2. Suy gan nặng làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng, hôn mê",
                "Trầm cảm nặng, ý tưởng tự tử",
                "QT kéo dài, rối loạn nhịp tim",
                "Parkinsonism nặng",
                "Serotonin syndrome (nếu dùng với MAO inhibitors)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "ECG - theo dõi QT interval",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp",
                "Xử trí trầm cảm, ý tưởng tự tử - tư vấn tâm thần",
                "Xử trí rối loạn nhịp tim nếu có",
                "Xử trí serotonin syndrome nếu có (cyproheptadine, cooling)",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp, ECG (QT interval), dấu hiệu trầm cảm, ý tưởng tự tử"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để tăng hấp thu.",
                "timing": "Chia 3 lần/ngày, uống cùng thời điểm mỗi ngày. Bắt đầu với liều thấp và tăng dần mỗi 3-5 ngày để giảm tác dụng phụ. Không ngừng đột ngột - giảm dần dần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tetrabenazine (Xenazine)",
                "UpToDate - Tetrabenazine: Drug information",
                "Lexicomp - Tetrabenazine monograph",
                "AAN Guidelines - Huntington's Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, clinical trial data, widely used"
        }
    },
    
}

__all__ = ['ANTIPARKINSONIAN_DRUGS']





















