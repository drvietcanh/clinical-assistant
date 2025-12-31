"""
ADHD Medications and Anxiolytics
"""

ADHD_ANXIOLYTICS_DRUGS = {
    "Atomoxetine": {
        "group": "Psychiatry - ADHD Medication (Non-stimulant)",
        "vietnamese_name": "Atomoxetine, Strattera",
        "administration": ["PO"],
        "indications": [
            "ADHD (Attention Deficit Hyperactivity Disorder)"
        ],
        "contraindications": [
            "Glaucoma góc hẹp",
            "Dùng MAO inhibitor",
            "Bệnh tim nặng",
            "Dị ứng atomoxetine"
        ],
        "dosage": {
            "adult_initial": "40mg/ngày, tăng sau 3 ngày",
            "adult_maintenance": "80-100mg/ngày (chia 1-2 lần)",
            "adult_max": "100mg/ngày",
            "pediatric_initial": "0.5mg/kg/ngày, tăng sau 3 ngày",
            "pediatric_maintenance": "1.2-1.4mg/kg/ngày",
            "pediatric_max": "1.4mg/kg/ngày hoặc 100mg/ngày",
            "notes": "Non-stimulant, không gây nghiện. Tác dụng chậm (1-2 tuần). Dùng 1-2 lần/ngày."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "Buồn nôn (phổ biến khi bắt đầu)",
            "Giảm cảm giác thèm ăn",
            "Mệt mỏi",
            "Chóng mặt",
            "Nhức đầu",
            "Tăng huyết áp, nhịp tim nhanh (nhẹ)",
            "Tăng nguy cơ tự sát ở trẻ em (hiếm)",
            "Tổn thương gan (hiếm nhưng nguy hiểm)"
        ],
        "interactions": [
            "MAO inhibitors: chống chỉ định",
            "CYP2D6 inhibitors: tăng nồng độ atomoxetine",
            "Thuốc tăng huyết áp: tăng tác dụng"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Atomoxetine là non-stimulant, ức chế tái hấp thu norepinephrine ở synap thần kinh, tăng nồng độ norepinephrine. Tăng sự chú ý, giảm hiếu động, cải thiện hành vi ở ADHD. Đặc điểm: non-stimulant, không gây nghiện, không gây lệ thuộc, không gây mất ngủ. Tác dụng chậm (1-2 tuần) - khác với methylphenidate (tác dụng nhanh). Ít tác dụng phụ hơn stimulant, nhưng có nguy cơ tổn thương gan (hiếm).",
        "monitoring": [
            "Triệu chứng ADHD (sự chú ý, hiếu động)",
            "Huyết áp, nhịp tim (tăng nhẹ)",
            "Cân nặng (giảm cảm giác thèm ăn)",
            "Chức năng gan (ALT, AST) - quan trọng (nguy cơ tổn thương gan)",
            "Dấu hiệu tự sát ở trẻ em (hiếm)",
            "Buồn nôn (phổ biến khi bắt đầu)"
        ],
        "precautions": [
            "Tổn thương gan - hiếm nhưng nguy hiểm, theo dõi ALT/AST",
            "Ngừng ngay nếu có dấu hiệu tổn thương gan (vàng da, đau bụng, mệt mỏi)",
            "Tăng nguy cơ tự sát ở trẻ em - theo dõi sát",
            "Tác dụng chậm (1-2 tuần) - không dùng cho cấp cứu",
            "Không gây nghiện - ưu điểm so với stimulant",
            "Thận trọng với CYP2D6 inhibitors",
            "Không dùng với MAO inhibitors"
        ],
        "pharmacokinetics": {
            "half_life": "5 giờ (người bình thường), 24 giờ (người chuyển hóa chậm CYP2D6)",
            "onset": "1-2 tuần (chậm)",
            "duration": "12-24 giờ",
            "protein_binding": "98%",
            "clearance": "Gan: chuyển hóa qua CYP2D6. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tăng nguy cơ tự sát ở trẻ em và thanh thiếu niên. Tổn thương gan - hiếm nhưng nguy hiểm, ngừng ngay nếu có dấu hiệu. Chống chỉ định với MAO inhibitors.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine)",
                    "mechanism": "Tăng nồng độ norepinephrine",
                    "effect": "Tăng huyết áp nghiêm trọng, sốt cao, co giật, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu atomoxetine."
                },
                {
                    "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa atomoxetine",
                    "effect": "Tăng nồng độ atomoxetine đáng kể, tăng tác dụng phụ",
                    "management": "Giảm liều atomoxetine 50%. Theo dõi sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc tăng huyết áp (epinephrine, norepinephrine)",
                    "mechanism": "Tác dụng hiệp đồng",
                    "effect": "Tăng huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Glaucoma góc hẹp",
                "Dùng MAO inhibitor",
                "Bệnh tim nặng",
                "Dị ứng atomoxetine"
            ],
            "tương_đối": [
                "Bệnh tim nhẹ đến trung bình - thận trọng, theo dõi ECG",
                "Tăng huyết áp nhẹ đến trung bình - thận trọng, theo dõi huyết áp",
                "Suy gan - tăng nguy cơ tổn thương gan",
                "Dùng với CYP2D6 inhibitors - giảm liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Chỉ dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 50%",
            "severe": "CHỐNG CHỈ ĐỊNH (nguy cơ tổn thương gan)",
            "notes": "Chuyển hóa qua gan (CYP2D6). Suy gan làm giảm chuyển hóa và tăng nguy cơ tổn thương gan."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Kích động",
                "Tăng huyết áp",
                "Nhịp tim nhanh",
                "Co giật (hiếm)",
                "Hôn mê (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ECG liên tục",
                "Điều trị tăng huyết áp: Labetalol",
                "Điều trị co giật: Benzodiazepines",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Lọc máu KHÔNG hiệu quả do protein binding cao (98%)"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, nhịp tim, ý thức, chức năng gan"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Dùng 1-2 lần/ngày. Khởi đầu 40mg/ngày, tăng sau 3 ngày. Tác dụng chậm (1-2 tuần). QUAN TRỌNG: Theo dõi chức năng gan (ALT/AST)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Strattera (atomoxetine)",
                "UpToDate - Atomoxetine: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Buspirone": {
        "group": "Psychiatry - Anxiolytic (5-HT1A Partial Agonist)",
        "vietnamese_name": "Buspirone, Buspar",
        "administration": ["PO"],
        "indications": [
            "Rối loạn lo âu tổng quát (GAD)",
            "Rối loạn lo âu"
        ],
        "contraindications": [
            "Dị ứng buspirone",
            "Suy gan nặng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_initial": "7.5mg x 2 lần/ngày, tăng dần",
            "adult_maintenance": "15-30mg x 2 lần/ngày",
            "adult_max": "60mg/ngày",
            "notes": "Không gây nghiện, không gây an thần. Tác dụng chậm (2-4 tuần)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "Chóng mặt (phổ biến)",
            "Buồn nôn",
            "Nhức đầu",
            "Kích động (hiếm)",
            "Mất ngủ (hiếm)",
            "Ít tác dụng phụ hơn benzodiazepine"
        ],
        "interactions": [
            "MAO inhibitors: tăng nguy cơ huyết áp cao",
            "CYP3A4 inhibitors: tăng nồng độ buspirone",
            "Grapefruit juice: tăng nồng độ buspirone"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Buspirone là anxiolytic không phải benzodiazepine, tác dụng như partial agonist thụ thể serotonin 5-HT1A. Kích thích thụ thể 5-HT1A presynaptic (giảm giải phóng serotonin) và postsynaptic (tác dụng anxiolytic). Đặc điểm: không gây nghiện, không gây an thần, không gây lệ thuộc, không gây rối loạn nhận thức. Tác dụng chậm (2-4 tuần) - khác với benzodiazepine (tác dụng nhanh). Ít tác dụng phụ hơn benzodiazepine. Không hiệu quả cho panic disorder.",
        "monitoring": [
            "Triệu chứng lo âu",
            "Chóng mặt (phổ biến)",
            "Buồn nôn",
            "Chức năng gan (hiếm)"
        ],
        "precautions": [
            "Tác dụng chậm (2-4 tuần) - không dùng cho cấp cứu",
            "Không gây nghiện, không gây an thần - ưu điểm",
            "Tránh grapefruit juice (tăng nồng độ)",
            "Thận trọng với CYP3A4 inhibitors",
            "Không hiệu quả cho panic disorder"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (ngắn)",
            "onset": "2-4 tuần (chậm)",
            "duration": "6-8 giờ",
            "protein_binding": "95%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, không dùng với MAO inhibitors.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine)",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Tăng nguy cơ huyết áp cao, hội chứng serotonin",
                    "management": "TRÁNH dùng cùng."
                },
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa buspirone",
                    "effect": "Tăng nồng độ buspirone, tăng tác dụng phụ",
                    "management": "TRÁNH grapefruit juice."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa buspirone",
                    "effect": "Tăng nồng độ buspirone, tăng tác dụng phụ",
                    "management": "Giảm liều buspirone 50%."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng buspirone",
                "Dùng MAO inhibitors",
                "Suy gan nặng",
                "Suy thận nặng"
            ],
            "tương_đối": [
                "Suy gan nhẹ đến trung bình - thận trọng",
                "Suy thận nhẹ đến trung bình - thận trọng"
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
            "notes": "Chuyển hóa qua gan (CYP3A4). Suy gan làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Chóng mặt",
                "Buồn ngủ",
                "Hạ huyết áp (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ triệu chứng",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi dấu hiệu sinh tồn"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Dùng 2 lần/ngày. Khởi đầu 7.5mg x 2 lần/ngày, tăng dần. Tác dụng chậm (2-4 tuần)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Buspar (buspirone)",
                "UpToDate - Buspirone: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Dextroamphetamine": {
        "group": "Psychiatry - ADHD Medication (Stimulant)",
        "vietnamese_name": "Dextroamphetamine, Dexedrine, Adderall (dextroamphetamine + levoamphetamine)",
        "administration": ["PO"],
        "indications": [
            "ADHD (Attention Deficit Hyperactivity Disorder)",
            "Narcolepsy"
        ],
        "contraindications": [
            "Glaucoma",
            "Tics hoặc Tourette's syndrome",
            "Dùng MAO inhibitor",
            "Bệnh tim nặng",
            "Tăng huyết áp nặng",
            "Dị ứng amphetamine"
        ],
        "dosage": {
            "adult_adhd": "5-10mg x 1-2 lần/ngày, tăng đến 20-40mg/ngày",
            "adult_narcolepsy": "10-20mg x 1-2 lần/ngày",
            "pediatric_adhd": "2.5-5mg x 1-2 lần/ngày, tăng đến 20-30mg/ngày",
            "adult_max": "40mg/ngày",
            "notes": "Stimulant, tác dụng nhanh. Có dạng immediate release (IR) và extended release (ER). Dùng buổi sáng và trưa, tránh buổi tối (gây mất ngủ)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Mất ngủ (phổ biến)",
            "Giảm cảm giác thèm ăn",
            "Nhức đầu",
            "Đau bụng",
            "Tăng huyết áp",
            "Nhịp tim nhanh",
            "Kích động",
            "Tics (có thể làm nặng)",
            "Tăng nguy cơ lạm dụng (stimulant)"
        ],
        "interactions": [
            "MAO inhibitors: chống chỉ định (nguy hiểm)",
            "Thuốc tăng huyết áp: tăng tác dụng",
            "Antacids: tăng hấp thu dextroamphetamine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Dextroamphetamine là stimulant, ức chế tái hấp thu dopamine và norepinephrine ở synap thần kinh, và tăng giải phóng dopamine và norepinephrine từ presynaptic terminals. Tăng nồng độ các chất dẫn truyền thần kinh này. Tăng sự chú ý, giảm hiếu động, cải thiện hành vi ở ADHD. Tác dụng nhanh (30-60 phút). Có dạng immediate release (IR) và extended release (ER). Đặc điểm: tác dụng nhanh, hiệu quả cao với ADHD, nhưng có nguy cơ lạm dụng (stimulant).",
        "monitoring": [
            "Triệu chứng ADHD (sự chú ý, hiếu động)",
            "Huyết áp, nhịp tim (tăng huyết áp, nhịp tim nhanh)",
            "Cân nặng (giảm cảm giác thèm ăn)",
            "Giấc ngủ (mất ngủ)",
            "Tics (có thể làm nặng)",
            "Dấu hiệu lạm dụng",
            "Chức năng tim (nếu có bệnh tim)"
        ],
        "precautions": [
            "NGUY CƠ LẠM DỤNG - stimulant, cần theo dõi sát",
            "Tăng huyết áp, nhịp tim nhanh - theo dõi định kỳ",
            "Mất ngủ - tránh dùng buổi tối",
            "Giảm cảm giác thèm ăn - theo dõi cân nặng",
            "Tics - có thể làm nặng, thận trọng",
            "Không dùng với MAO inhibitors",
            "Thận trọng ở bệnh nhân có bệnh tim",
            "Dùng buổi sáng và trưa, tránh buổi tối"
        ],
        "pharmacokinetics": {
            "half_life": "10-12 giờ (IR), 10-13 giờ (ER)",
            "onset": "30-60 phút (IR), 1-2 giờ (ER)",
            "duration": "4-6 giờ (IR), 8-12 giờ (ER)",
            "protein_binding": "20%",
            "clearance": "Gan: chuyển hóa một phần. Thận: bài tiết một phần (pH-dependent)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Bảo quản an toàn (nguy cơ lạm dụng).",
        "black_box_warnings": "Nguy cơ lạm dụng và lệ thuộc. Chỉ dùng cho ADHD hoặc narcolepsy được chẩn đoán. Tăng huyết áp và nhịp tim. Tics. Chống chỉ định với MAO inhibitors.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine)",
                    "mechanism": "Tăng nồng độ catecholamines",
                    "effect": "Tăng huyết áp nghiêm trọng, sốt cao, co giật, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu dextroamphetamine."
                },
                {
                    "drug": "Thuốc tăng huyết áp (epinephrine, norepinephrine)",
                    "mechanism": "Tác dụng hiệp đồng",
                    "effect": "Tăng huyết áp nghiêm trọng",
                    "management": "Thận trọng. Theo dõi huyết áp sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacids",
                    "mechanism": "Tăng pH dạ dày, tăng hấp thu dextroamphetamine",
                    "effect": "Tăng nồng độ dextroamphetamine",
                    "management": "Cách thời gian ít nhất 1 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Glaucoma",
                "Tics hoặc Tourette's syndrome",
                "Dùng MAO inhibitor",
                "Bệnh tim nặng",
                "Tăng huyết áp nặng",
                "Dị ứng amphetamine"
            ],
            "tương_đối": [
                "Bệnh tim nhẹ đến trung bình - thận trọng, theo dõi ECG",
                "Tăng huyết áp nhẹ đến trung bình - thận trọng, theo dõi huyết áp",
                "Tiền sử lạm dụng chất - tăng nguy cơ lạm dụng",
                "Lo âu nặng - có thể làm nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Chỉ dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Dextroamphetamine bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Dextroamphetamine chuyển hóa một phần qua gan. Suy gan có thể làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Kích động, lo âu",
                "Tăng huyết áp nghiêm trọng",
                "Nhịp tim nhanh",
                "Sốt",
                "Co giật",
                "Hôn mê",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ECG liên tục",
                "Điều trị tăng huyết áp: Labetalol, phentolamine",
                "Điều trị co giật: Benzodiazepines",
                "Hạ nhiệt nếu sốt",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, nhịp tim, ý thức, nhiệt độ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Dùng buổi sáng và trưa, tránh buổi tối (gây mất ngủ). IR: 1-2 lần/ngày. ER: 1 lần/ngày buổi sáng. QUAN TRỌNG: Bảo quản an toàn (nguy cơ lạm dụng)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dexedrine (dextroamphetamine), Adderall (amphetamine salts)",
                "UpToDate - Dextroamphetamine: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
    "Lisdexamfetamine": {
        "group": "Psychiatry - ADHD Medication (Stimulant - Prodrug)",
        "vietnamese_name": "Lisdexamfetamine, Vyvanse",
        "administration": ["PO"],
        "indications": [
            "ADHD (Attention Deficit Hyperactivity Disorder)",
            "Binge eating disorder"
        ],
        "contraindications": [
            "Glaucoma",
            "Tics hoặc Tourette's syndrome",
            "Dùng MAO inhibitor",
            "Bệnh tim nặng",
            "Tăng huyết áp nặng",
            "Dị ứng amphetamine"
        ],
        "dosage": {
            "adult_adhd": "30mg/ngày, tăng đến 50-70mg/ngày",
            "adult_binge_eating": "30mg/ngày, tăng đến 50-70mg/ngày",
            "pediatric_adhd": "20-30mg/ngày, tăng đến 50-70mg/ngày",
            "adult_max": "70mg/ngày",
            "notes": "Prodrug của dextroamphetamine. Chuyển hóa thành dextroamphetamine trong cơ thể. Tác dụng kéo dài (10-12 giờ), dùng 1 lần/ngày. Ít nguy cơ lạm dụng hơn dextroamphetamine (do là prodrug)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, có thể giảm liều"
        },
        "side_effects": [
            "Mất ngủ (phổ biến)",
            "Giảm cảm giác thèm ăn",
            "Nhức đầu",
            "Đau bụng",
            "Tăng huyết áp",
            "Nhịp tim nhanh",
            "Kích động",
            "Tics (có thể làm nặng)",
            "Tăng nguy cơ lạm dụng (ít hơn dextroamphetamine)"
        ],
        "interactions": [
            "MAO inhibitors: chống chỉ định (nguy hiểm)",
            "Thuốc tăng huyết áp: tăng tác dụng",
            "Antacids: tăng hấp thu lisdexamfetamine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Lisdexamfetamine là prodrug của dextroamphetamine. Sau khi uống, lisdexamfetamine được chuyển hóa thành dextroamphetamine trong cơ thể (qua enzyme trong hồng cầu). Dextroamphetamine ức chế tái hấp thu dopamine và norepinephrine, và tăng giải phóng các chất dẫn truyền thần kinh này. Tăng sự chú ý, giảm hiếu động, cải thiện hành vi ở ADHD. Đặc điểm: prodrug, tác dụng kéo dài (10-12 giờ), dùng 1 lần/ngày, ít nguy cơ lạm dụng hơn dextroamphetamine (do là prodrug, không thể tiêm hoặc hít).",
        "monitoring": [
            "Triệu chứng ADHD (sự chú ý, hiếu động)",
            "Huyết áp, nhịp tim (tăng huyết áp, nhịp tim nhanh)",
            "Cân nặng (giảm cảm giác thèm ăn)",
            "Giấc ngủ (mất ngủ)",
            "Tics (có thể làm nặng)",
            "Dấu hiệu lạm dụng (ít hơn dextroamphetamine)",
            "Chức năng tim (nếu có bệnh tim)"
        ],
        "precautions": [
            "NGUY CƠ LẠM DỤNG - stimulant, nhưng ít hơn dextroamphetamine (do là prodrug)",
            "Tăng huyết áp, nhịp tim nhanh - theo dõi định kỳ",
            "Mất ngủ - tránh dùng buổi tối",
            "Giảm cảm giác thèm ăn - theo dõi cân nặng",
            "Tics - có thể làm nặng, thận trọng",
            "Không dùng với MAO inhibitors",
            "Thận trọng ở bệnh nhân có bệnh tim",
            "Dùng buổi sáng, tránh buổi tối (tác dụng kéo dài 10-12 giờ)"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (lisdexamfetamine), 10-12 giờ (dextroamphetamine sau chuyển hóa)",
            "onset": "1-2 giờ (chậm hơn dextroamphetamine do là prodrug)",
            "duration": "10-12 giờ (dài, dùng 1 lần/ngày)",
            "protein_binding": "20% (dextroamphetamine)",
            "clearance": "Chuyển hóa thành dextroamphetamine trong hồng cầu. Dextroamphetamine: gan (chuyển hóa một phần), thận (bài tiết một phần)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Bảo quản an toàn (nguy cơ lạm dụng).",
        "black_box_warnings": "Nguy cơ lạm dụng và lệ thuộc. Chỉ dùng cho ADHD hoặc binge eating disorder được chẩn đoán. Tăng huyết áp và nhịp tim. Tics. Chống chỉ định với MAO inhibitors.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine)",
                    "mechanism": "Tăng nồng độ catecholamines",
                    "effect": "Tăng huyết áp nghiêm trọng, sốt cao, co giật, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu lisdexamfetamine."
                },
                {
                    "drug": "Thuốc tăng huyết áp (epinephrine, norepinephrine)",
                    "mechanism": "Tác dụng hiệp đồng",
                    "effect": "Tăng huyết áp nghiêm trọng",
                    "management": "Thận trọng. Theo dõi huyết áp sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacids",
                    "mechanism": "Tăng pH dạ dày, tăng hấp thu lisdexamfetamine",
                    "effect": "Tăng nồng độ lisdexamfetamine",
                    "management": "Cách thời gian ít nhất 1 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Glaucoma",
                "Tics hoặc Tourette's syndrome",
                "Dùng MAO inhibitor",
                "Bệnh tim nặng",
                "Tăng huyết áp nặng",
                "Dị ứng amphetamine"
            ],
            "tương_đối": [
                "Bệnh tim nhẹ đến trung bình - thận trọng, theo dõi ECG",
                "Tăng huyết áp nhẹ đến trung bình - thận trọng, theo dõi huyết áp",
                "Tiền sử lạm dụng chất - tăng nguy cơ lạm dụng",
                "Lo âu nặng - có thể làm nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Chỉ dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Lisdexamfetamine (và dextroamphetamine sau chuyển hóa) bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Lisdexamfetamine chuyển hóa thành dextroamphetamine. Dextroamphetamine chuyển hóa một phần qua gan. Suy gan có thể làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Kích động, lo âu",
                "Tăng huyết áp nghiêm trọng",
                "Nhịp tim nhanh",
                "Sốt",
                "Co giật",
                "Hôn mê",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ECG liên tục",
                "Điều trị tăng huyết áp: Labetalol, phentolamine",
                "Điều trị co giật: Benzodiazepines",
                "Hạ nhiệt nếu sốt",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, nhịp tim, ý thức, nhiệt độ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Dùng 1 lần/ngày buổi sáng. Tác dụng kéo dài 10-12 giờ. Tránh buổi tối (gây mất ngủ). QUAN TRỌNG: Bảo quản an toàn (nguy cơ lạm dụng)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vyvanse (lisdexamfetamine)",
                "UpToDate - Lisdexamfetamine: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    "Methylphenidate": {
        "group": "Psychiatry - ADHD Medication (Stimulant)",
        "vietnamese_name": "Methylphenidate, Ritalin, Concerta",
        "administration": ["PO"],
        "indications": [
            "ADHD (Attention Deficit Hyperactivity Disorder)",
            "Narcolepsy"
        ],
        "contraindications": [
            "Glaucoma",
            "Tics hoặc Tourette's syndrome",
            "Dùng MAO inhibitor",
            "Bệnh tim nặng",
            "Tăng huyết áp nặng",
            "Dị ứng methylphenidate"
        ],
        "dosage": {
            "adult_adhd": "5-10mg x 2-3 lần/ngày, tăng đến 20-30mg x 2-3 lần/ngày",
            "adult_narcolepsy": "10-20mg x 2-3 lần/ngày",
            "pediatric_adhd": "5mg x 2 lần/ngày, tăng đến 20-30mg x 2-3 lần/ngày",
            "adult_max": "60mg/ngày",
            "notes": "Stimulant, tác dụng nhanh. Có dạng immediate release (IR) và extended release (ER). Dùng buổi sáng và trưa, tránh dùng buổi tối (gây mất ngủ)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Mất ngủ (phổ biến)",
            "Giảm cảm giác thèm ăn",
            "Nhức đầu",
            "Đau bụng",
            "Tăng huyết áp",
            "Nhịp tim nhanh",
            "Kích động",
            "Tics (có thể làm nặng)",
            "Tăng nguy cơ lạm dụng (stimulant)"
        ],
        "interactions": [
            "MAO inhibitors: chống chỉ định (nguy hiểm)",
            "Thuốc tăng huyết áp: tăng tác dụng",
            "Antacids: tăng hấp thu methylphenidate"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Methylphenidate là stimulant, ức chế tái hấp thu dopamine và norepinephrine ở synap thần kinh, tăng nồng độ các chất dẫn truyền thần kinh này. Tăng sự chú ý, giảm hiếu động, cải thiện hành vi ở ADHD. Tác dụng nhanh (30-60 phút). Có dạng immediate release (IR) và extended release (ER). Đặc điểm: tác dụng nhanh, hiệu quả cao với ADHD, nhưng có nguy cơ lạm dụng (stimulant).",
        "monitoring": [
            "Triệu chứng ADHD (sự chú ý, hiếu động)",
            "Huyết áp, nhịp tim (tăng huyết áp, nhịp tim nhanh)",
            "Cân nặng (giảm cảm giác thèm ăn)",
            "Giấc ngủ (mất ngủ)",
            "Tics (có thể làm nặng)",
            "Dấu hiệu lạm dụng",
            "Chức năng tim (nếu có bệnh tim)"
        ],
        "precautions": [
            "NGUY CƠ LẠM DỤNG - stimulant, cần theo dõi sát",
            "Tăng huyết áp, nhịp tim nhanh - theo dõi định kỳ",
            "Mất ngủ - tránh dùng buổi tối",
            "Giảm cảm giác thèm ăn - theo dõi cân nặng",
            "Tics - có thể làm nặng, thận trọng",
            "Không dùng với MAO inhibitors",
            "Thận trọng ở bệnh nhân có bệnh tim",
            "Dùng buổi sáng và trưa, tránh buổi tối"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (IR), 3-4 giờ (ER)",
            "onset": "30-60 phút (IR), 1-2 giờ (ER)",
            "duration": "3-4 giờ (IR), 8-12 giờ (ER)",
            "protein_binding": "15%",
            "clearance": "Gan: chuyển hóa qua esterase. Thận: bài tiết một phần."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Bảo quản an toàn (nguy cơ lạm dụng).",
        "black_box_warnings": "Nguy cơ lạm dụng và lệ thuộc. Chỉ dùng cho ADHD hoặc narcolepsy được chẩn đoán. Tăng huyết áp và nhịp tim. Tics. Chống chỉ định với MAO inhibitors.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine)",
                    "mechanism": "Tăng nồng độ catecholamines",
                    "effect": "Tăng huyết áp nghiêm trọng, sốt cao, co giật, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu methylphenidate."
                },
                {
                    "drug": "Thuốc tăng huyết áp (epinephrine, norepinephrine)",
                    "mechanism": "Tác dụng hiệp đồng",
                    "effect": "Tăng huyết áp nghiêm trọng",
                    "management": "Thận trọng. Theo dõi huyết áp sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Antacids",
                    "mechanism": "Tăng pH dạ dày, tăng hấp thu methylphenidate",
                    "effect": "Tăng nồng độ methylphenidate",
                    "management": "Cách thời gian ít nhất 1 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Glaucoma",
                "Tics hoặc Tourette's syndrome",
                "Dùng MAO inhibitor",
                "Bệnh tim nặng",
                "Tăng huyết áp nặng",
                "Dị ứng methylphenidate"
            ],
            "tương_đối": [
                "Bệnh tim nhẹ đến trung bình - thận trọng, theo dõi ECG",
                "Tăng huyết áp nhẹ đến trung bình - thận trọng, theo dõi huyết áp",
                "Tiền sử lạm dụng chất - tăng nguy cơ lạm dụng",
                "Lo âu nặng - có thể làm nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Chỉ dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Chuyển hóa qua gan (esterase). Suy gan có thể làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Kích động, lo âu",
                "Tăng huyết áp nghiêm trọng",
                "Nhịp tim nhanh",
                "Sốt",
                "Co giật",
                "Hôn mê",
                "Rối loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Hỗ trợ hô hấp nếu cần",
                "Theo dõi ECG liên tục",
                "Điều trị tăng huyết áp: Labetalol, phentolamine",
                "Điều trị co giật: Benzodiazepines",
                "Hạ nhiệt nếu sốt",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính"
            ],
            "monitoring": "Theo dõi liên tục ECG, huyết áp, nhịp tim, ý thức, nhiệt độ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn",
                "timing": "Dùng buổi sáng và trưa, tránh buổi tối (gây mất ngủ). IR: 2-3 lần/ngày. ER: 1 lần/ngày buổi sáng. QUAN TRỌNG: Bảo quản an toàn (nguy cơ lạm dụng)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ritalin (methylphenidate), Concerta (methylphenidate ER)",
                "UpToDate - Methylphenidate: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    },
    
}

__all__ = ['ADHD_ANXIOLYTICS_DRUGS']

