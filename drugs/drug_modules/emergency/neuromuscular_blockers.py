"""
Neuromuscular Blocking Agents (NMBAs)
Thuốc giãn cơ dùng trong ICU, gây mê, và cấp cứu
"""

NEUROMUSCULAR_BLOCKERS_DRUGS = {
    "Succinylcholine": {
        "group": "Emergency - Depolarizing Neuromuscular Blocker",
        "vietnamese_name": "Succinylcholine, Suxamethonium",
        "administration": ["IV", "IM"],
        "indications": [
            "Đặt nội khí quản nhanh (rapid sequence intubation - RSI)",
            "Gây mê khởi đầu (induction of anesthesia)",
            "Thủ thuật ngắn cần giãn cơ (short procedures)",
            "Co giật kéo dài (status epilepticus) - khi cần giãn cơ để đặt nội khí quản"
        ],
        "contraindications": [
            "Dị ứng succinylcholine",
            "Tăng kali máu nặng hoặc nguy cơ tăng kali máu (bỏng, chấn thương lớn, liệt tủy sống, bệnh thần kinh-cơ)",
            "Bệnh nhược cơ (myasthenia gravis) - có thể gây block kéo dài",
            "Tiền sử sốt ác tính do gây mê (malignant hyperthermia)",
            "Bệnh cơ di truyền (muscular dystrophy, Duchenne) - nguy cơ tăng kali máu, rhabdomyolysis"
        ],
        "dosage": {
            "adult_iv_rsi": "1-1.5 mg/kg IV bolus (thường 1 mg/kg)",
            "adult_iv_anesthesia": "0.6-1.1 mg/kg IV bolus",
            "adult_im": "3-4 mg/kg IM (khi không có đường IV)",
            "pediatric_iv": "1-2 mg/kg IV bolus",
            "pediatric_im": "4-5 mg/kg IM",
            "notes": "Tác dụng nhanh (30-60 giây), ngắn (5-10 phút). Liều cao hơn ở trẻ em. Dùng với sedative/anesthetic trước khi đặt nội khí quản."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (nhưng thận trọng nếu có tăng kali máu)",
            "under_30": "Thận trọng (tăng nguy cơ tăng kali máu)"
        },
        "side_effects": [
            "Tăng kali máu (0.5-1 mEq/L bình thường, có thể tăng nặng ở bệnh nhân có nguy cơ)",
            "Nhịp chậm (bradycardia) - đặc biệt ở trẻ em, liều lặp lại",
            "Co cơ (fasciculations) trước khi giãn cơ",
            "Đau cơ sau phẫu thuật (myalgia)",
            "Tăng áp lực nội nhãn (intraocular pressure)",
            "Tăng áp lực nội sọ (intracranial pressure)",
            "Sốt ác tính do gây mê (malignant hyperthermia) - hiếm nhưng nguy hiểm",
            "Rhabdomyolysis (ở bệnh nhân có bệnh cơ di truyền)"
        ],
        "interactions": [
            "Thuốc ức chế cholinesterase (neostigmine, pyridostigmine): kéo dài tác dụng",
            "Magnesium: tăng tác dụng, kéo dài thời gian giãn cơ",
            "Aminoglycosides: tăng tác dụng, kéo dài thời gian giãn cơ",
            "Lidocaine: tăng tác dụng nhẹ"
        ],
        "pregnancy": "C - An toàn trong cấp cứu và gây mê",
        "mechanism_of_action": "Succinylcholine là chất chủ vận (agonist) của nicotinic acetylcholine receptors tại junction thần kinh-cơ. Khác với non-depolarizing blockers (ức chế receptor), succinylcholine kích thích receptor và gây khử cực màng tế bào cơ (depolarization). Khử cực ban đầu gây co cơ (fasciculations), sau đó receptor bị desensitize và không đáp ứng với acetylcholine → giãn cơ. Succinylcholine bị phân hủy bởi pseudocholinesterase trong huyết tương (thời gian bán thải 2-3 phút), nên tác dụng ngắn (5-10 phút). Ở bệnh nhân thiếu pseudocholinesterase (di truyền hoặc mắc phải), tác dụng kéo dài (có thể >1 giờ).",
        "monitoring": [
            "ECG liên tục (theo dõi nhịp chậm, rối loạn nhịp do tăng kali máu)",
            "Kali máu (trước và sau dùng, đặc biệt ở bệnh nhân có nguy cơ)",
            "TOF (train-of-four) monitoring nếu có thể",
            "Dấu hiệu sốt ác tính do gây mê (tăng nhiệt độ, tăng CO2, tăng CK)",
            "Áp lực nội nhãn (nếu có bệnh mắt)",
            "Áp lực nội sọ (nếu có chấn thương sọ não)"
        ],
        "precautions": [
            "TUYỆT ĐỐI KHÔNG dùng ở bệnh nhân có nguy cơ tăng kali máu (bỏng >24h, chấn thương lớn, liệt tủy sống, bệnh thần kinh-cơ)",
            "Dùng với sedative/anesthetic trước khi đặt nội khí quản (bệnh nhân phải được an thần)",
            "Theo dõi kali máu ở bệnh nhân có nguy cơ",
            "Có thể dùng atropine để phòng ngừa nhịp chậm (đặc biệt ở trẻ em, liều lặp lại)",
            "Thận trọng ở bệnh nhân có bệnh cơ di truyền (nguy cơ rhabdomyolysis, tăng kali máu)",
            "Thận trọng ở bệnh nhân có bệnh nhược cơ (có thể gây block kéo dài)",
            "Chuẩn bị sẵn dantrolene nếu nghi ngờ sốt ác tính do gây mê",
            "Không dùng liều lặp lại (tăng nguy cơ tăng kali máu, nhịp chậm)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 phút (rất ngắn)",
            "onset": "30-60 giây (rất nhanh)",
            "duration": "5-10 phút (ngắn)",
            "protein_binding": "Không đáng kể",
            "clearance": "Phân hủy bởi pseudocholinesterase trong huyết tương (90%), một phần bởi cholinesterase ở mô"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Dung dịch đã pha: ổn định trong 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "Nguy cơ tăng kali máu nặng có thể gây rối loạn nhịp tim, ngừng tim, tử vong ở bệnh nhân có nguy cơ (bỏng, chấn thương lớn, liệt tủy sống, bệnh thần kinh-cơ). TUYỆT ĐỐI KHÔNG dùng ở những bệnh nhân này. Nguy cơ sốt ác tính do gây mê (malignant hyperthermia) - hiếm nhưng nguy hiểm, có thể tử vong.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc ức chế cholinesterase (neostigmine, pyridostigmine, physostigmine)",
                    "mechanism": "Ức chế pseudocholinesterase, làm giảm phân hủy succinylcholine",
                    "effect": "Kéo dài tác dụng giãn cơ (có thể >1 giờ)",
                    "management": "TRÁNH dùng succinylcholine với thuốc ức chế cholinesterase. Nếu đã dùng: theo dõi TOF, hỗ trợ thông khí cho đến khi hồi phục."
                },
                {
                    "drug": "Magnesium (IV)",
                    "mechanism": "Magnesium ức chế giải phóng acetylcholine và tăng tác dụng của succinylcholine",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều succinylcholine. Theo dõi TOF. Có thể cần giảm liều magnesium."
                }
            ],
            "moderate": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Aminoglycosides ức chế giải phóng acetylcholine",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều succinylcholine. Theo dõi TOF."
                },
                {
                    "drug": "Lidocaine",
                    "mechanism": "Lidocaine có thể tăng tác dụng của succinylcholine",
                    "effect": "Tăng tác dụng nhẹ",
                    "management": "Thận trọng. Theo dõi TOF."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng succinylcholine",
                "Tăng kali máu nặng hoặc nguy cơ tăng kali máu:",
                "  - Bỏng >24 giờ",
                "  - Chấn thương lớn (đặc biệt chấn thương tủy sống)",
                "  - Liệt tủy sống",
                "  - Bệnh thần kinh-cơ (myasthenia gravis, ALS, Guillain-Barré)",
                "  - Bệnh cơ di truyền (muscular dystrophy, Duchenne)",
                "Tiền sử sốt ác tính do gây mê (malignant hyperthermia)",
                "Bệnh nhược cơ (myasthenia gravis) - có thể gây block kéo dài"
            ],
            "tương_đối": [
                "Suy thận nặng - tăng nguy cơ tăng kali máu",
                "Bệnh cơ di truyền - nguy cơ rhabdomyolysis, tăng kali máu",
                "Tăng áp lực nội nhãn - có thể tăng áp lực",
                "Tăng áp lực nội sọ - có thể tăng áp lực",
                "Thiếu pseudocholinesterase - tác dụng kéo dài (>1 giờ)",
                "Trẻ em - tăng nguy cơ nhịp chậm, cần atropine"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Succinylcholine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Succinylcholine có thể qua nhau thai nhưng nồng độ thấp. Được sử dụng rộng rãi trong gây mê sản khoa (đặt nội khí quản trong mổ lấy thai) và có vẻ an toàn. Trong cấp cứu (RSI), lợi ích cứu sống mẹ vượt quá nguy cơ cho thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Succinylcholine có thời gian bán thải rất ngắn (2-3 phút) và bị phân hủy nhanh. Không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Succinylcholine có tác dụng cực ngắn và không bài tiết vào sữa mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (nhưng thận trọng nếu có giảm pseudocholinesterase)",
            "notes": "Succinylcholine chủ yếu phân hủy bởi pseudocholinesterase trong huyết tương, không phụ thuộc chức năng gan. Tuy nhiên, suy gan có thể làm giảm pseudocholinesterase, kéo dài tác dụng. Thường không cần điều chỉnh liều."
        },
        "overdose_management": {
            "symptoms": [
                "Giãn cơ kéo dài (>10 phút)",
                "Tăng kali máu nặng (có thể >6-7 mEq/L)",
                "Rối loạn nhịp tim (nhịp chậm, rung thất) do tăng kali máu",
                "Ngừng tim do tăng kali máu",
                "Suy hô hấp (do giãn cơ kéo dài)",
                "Rhabdomyolysis (ở bệnh nhân có bệnh cơ di truyền)"
            ],
            "antidote": "Không có antidote đặc hiệu. Hỗ trợ thông khí cho đến khi hồi phục. Điều trị tăng kali máu nếu có.",
            "treatment": [
                "Hỗ trợ thông khí: Đặt nội khí quản, thở máy cho đến khi hồi phục",
                "Theo dõi TOF để đánh giá hồi phục",
                "Nếu tăng kali máu nặng:",
                "  - Calcium gluconate 1g IV (bảo vệ tim)",
                "  - Insulin + Dextrose (chuyển kali vào tế bào)",
                "  - Sodium bicarbonate (nếu toan chuyển hóa)",
                "  - Albuterol nebulizer (chuyển kali vào tế bào)",
                "  - Hemodialysis nếu cần (thải trừ kali)",
                "Nếu rối loạn nhịp tim:",
                "  - Điều trị theo protocol rối loạn nhịp",
                "  - Nếu ngừng tim: CPR, defibrillation",
                "Nếu giãn cơ kéo dài do thiếu pseudocholinesterase:",
                "  - Hỗ trợ thông khí cho đến khi hồi phục (có thể >1 giờ)",
                "  - KHÔNG dùng neostigmine (có thể làm nặng)",
                "Nếu rhabdomyolysis:",
                "  - Bù dịch tích cực",
                "  - Theo dõi CK, myoglobin, chức năng thận",
                "  - Điều trị suy thận cấp nếu có",
                "Theo dõi: ECG, kali máu, CK, chức năng thận"
            ],
            "monitoring": "Theo dõi ECG, kali máu, TOF, hô hấp liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng (tăng kali máu, rhabdomyolysis)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Succinylcholine tự phân hủy nhanh (2-3 phút). Nếu tác dụng kéo dài do thiếu pseudocholinesterase: hỗ trợ thông khí cho đến khi hồi phục (có thể >1 giờ). KHÔNG dùng neostigmine (có thể làm nặng block)."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp dung dịch đã pha sẵn (20mg/ml). Hoặc pha bột: 500mg trong 5ml nước = 100mg/ml, sau đó pha loãng.",
                "infusion_rate": "RSI: 1-1.5 mg/kg IV bolus nhanh. Gây mê: 0.6-1.1 mg/kg IV bolus. Không truyền liên tục (chỉ dùng bolus).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Tiêm bolus riêng biệt."
                ],
                "notes": "QUAN TRỌNG: 1) Dùng với sedative/anesthetic trước (bệnh nhân phải được an thần), 2) Liều RSI: 1-1.5 mg/kg IV bolus nhanh, 3) TUYỆT ĐỐI KHÔNG dùng ở bệnh nhân có nguy cơ tăng kali máu, 4) Theo dõi kali máu và ECG, 5) Chuẩn bị sẵn dantrolene nếu nghi ngờ sốt ác tính do gây mê, 6) Có thể dùng atropine để phòng ngừa nhịp chậm (đặc biệt ở trẻ em)."
            },
            "im": {
                "reconstitution": "Dùng trực tiếp dung dịch đã pha sẵn (20mg/ml).",
                "injection_site": "Cơ lớn (đùi, cánh tay).",
                "notes": "IM: 3-4 mg/kg (người lớn), 4-5 mg/kg (trẻ em). Tác dụng chậm hơn IV (2-3 phút). Chỉ dùng khi không có đường IV."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Succinylcholine",
                "ACLS Guidelines 2020 - American Heart Association",
                "Rapid Sequence Intubation (RSI) Guidelines",
                "UpToDate - Succinylcholine: Drug Information",
                "Anesthesia Guidelines - Neuromuscular Blocking Agents",
                "Medscape - Succinylcholine Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, RSI guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Rocuronium": {
        "group": "Emergency - Non-depolarizing Neuromuscular Blocker (Aminosteroid)",
        "vietnamese_name": "Rocuronium, Esmeron",
        "administration": ["IV"],
        "indications": [
            "Đặt nội khí quản (intubation)",
            "Duy trì giãn cơ trong phẫu thuật",
            "Giãn cơ trong ICU (ARDS, status asthmaticus)",
            "RSI (rapid sequence intubation) - thay thế succinylcholine khi chống chỉ định"
        ],
        "contraindications": [
            "Dị ứng rocuronium",
            "Bệnh nhược cơ (myasthenia gravis) - có thể cần liều cao hơn hoặc tác dụng kéo dài"
        ],
        "dosage": {
            "adult_intubation": "0.6-1.2 mg/kg IV bolus (thường 0.6 mg/kg)",
            "adult_rsi": "1-1.2 mg/kg IV bolus (liều cao để đạt tác dụng nhanh)",
            "adult_maintenance": "0.1-0.2 mg/kg mỗi 20-45 phút hoặc 5-12 mcg/kg/phút IV infusion",
            "adult_icu": "5-12 mcg/kg/phút IV infusion (điều chỉnh theo TOF)",
            "pediatric_intubation": "0.6-1.2 mg/kg IV bolus",
            "notes": "Tác dụng nhanh (60-90 giây với liều 1.2 mg/kg), trung bình (30-60 phút). Có thể dùng cho RSI khi succinylcholine chống chỉ định."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (nhưng thận trọng, có thể kéo dài)",
            "under_30": "Thận trọng (có thể kéo dài, giảm liều maintenance)"
        },
        "side_effects": [
            "Giãn cơ kéo dài (đặc biệt ở suy gan, suy thận)",
            "Ức chế hô hấp (suy hô hấp nếu không hỗ trợ thông khí)",
            "Phản ứng dị ứng (hiếm)",
            "Tăng nhịp tim nhẹ (do giải phóng histamine nhẹ)"
        ],
        "interactions": [
            "Aminoglycosides: tăng tác dụng, kéo dài thời gian giãn cơ",
            "Magnesium: tăng tác dụng, kéo dài thời gian giãn cơ",
            "Volatile anesthetics: tăng tác dụng",
            "Corticosteroids: có thể giảm tác dụng nhẹ"
        ],
        "pregnancy": "C - An toàn trong cấp cứu và gây mê",
        "mechanism_of_action": "Rocuronium là non-depolarizing neuromuscular blocker (aminosteroid). Ức chế cạnh tranh nicotinic acetylcholine receptors tại junction thần kinh-cơ, ngăn chặn acetylcholine gắn với receptor. Kết quả: giãn cơ xương. Khác với succinylcholine (depolarizing), rocuronium không gây khử cực và không gây fasciculations. Rocuronium có tác dụng nhanh (60-90 giây với liều cao 1.2 mg/kg), phù hợp cho RSI. Thời gian tác dụng trung bình (30-60 phút). Thải trừ chủ yếu qua gan (70%), một phần qua thận (30%).",
        "monitoring": [
            "TOF (train-of-four) monitoring liên tục (quan trọng)",
            "Hô hấp (phải hỗ trợ thông khí cho đến khi hồi phục)",
            "ECG (theo dõi nhịp tim)",
            "Dấu hiệu hồi phục (cử động tự nhiên, phản xạ)"
        ],
        "precautions": [
            "PHẢI hỗ trợ thông khí cho đến khi hồi phục (bệnh nhân không thể thở tự nhiên)",
            "Theo dõi TOF để đánh giá mức độ block và hồi phục",
            "Dùng với sedative/anesthetic (bệnh nhân phải được an thần)",
            "Thận trọng ở suy gan (thải trừ chủ yếu qua gan, tác dụng kéo dài)",
            "Thận trọng ở suy thận (thải trừ một phần qua thận, có thể kéo dài)",
            "Có thể dùng cho RSI khi succinylcholine chống chỉ định",
            "Có reversal agent (sugammadex) - ưu điểm so với vecuronium"
        ],
        "pharmacokinetics": {
            "half_life": "60-90 phút",
            "onset": "60-90 giây (với liều 1.2 mg/kg), 90-120 giây (với liều 0.6 mg/kg)",
            "duration": "30-60 phút (phụ thuộc liều)",
            "protein_binding": "30%",
            "clearance": "Gan (70% - chuyển hóa), thận (30% - thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Dung dịch đã pha: ổn định trong 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "PHẢI hỗ trợ thông khí cho đến khi hồi phục. Bệnh nhân không thể thở tự nhiên khi đang dùng rocuronium.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Aminoglycosides ức chế giải phóng acetylcholine",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều rocuronium. Theo dõi TOF chặt chẽ."
                },
                {
                    "drug": "Magnesium (IV)",
                    "mechanism": "Magnesium ức chế giải phóng acetylcholine và tăng tác dụng của rocuronium",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều rocuronium. Theo dõi TOF. Có thể cần giảm liều magnesium."
                }
            ],
            "moderate": [
                {
                    "drug": "Volatile anesthetics (sevoflurane, isoflurane, desflurane)",
                    "mechanism": "Tăng nhạy cảm với neuromuscular blockers",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều rocuronium. Theo dõi TOF."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng rocuronium"
            ],
            "tương_đối": [
                "Bệnh nhược cơ (myasthenia gravis) - có thể cần liều cao hơn hoặc tác dụng kéo dài",
                "Suy gan nặng - tác dụng kéo dài (thải trừ chủ yếu qua gan)",
                "Suy thận nặng - tác dụng kéo dài (thải trừ một phần qua thận)",
                "Bệnh nhân cao tuổi - tăng nhạy cảm, tác dụng kéo dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Rocuronium là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Rocuronium có thể qua nhau thai nhưng nồng độ thấp. Được sử dụng rộng rãi trong gây mê sản khoa và có vẻ an toàn. Trong cấp cứu, lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết rocuronium có bài tiết vào sữa mẹ hay không. Thời gian bán thải 60-90 phút, protein binding 30%. Có thể bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (thải trừ chủ yếu qua gan)",
            "severe": "Thận trọng, giảm liều maintenance (tác dụng kéo dài)",
            "notes": "Rocuronium thải trừ chủ yếu qua gan (70%). Suy gan làm giảm thải trừ, tăng nồng độ và kéo dài tác dụng. Giảm liều maintenance ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Giãn cơ kéo dài (>60 phút)",
                "Suy hô hấp (bệnh nhân không thể thở tự nhiên)",
                "Không thể đảo ngược bằng neostigmine (nếu dùng liều cao)"
            ],
            "antidote": "Sugammadex (Bridion) - reversal agent đặc hiệu cho rocuronium và vecuronium. Hoặc neostigmine + glycopyrrolate (nếu liều thấp).",
            "treatment": [
                "Hỗ trợ thông khí: Đặt nội khí quản, thở máy cho đến khi hồi phục",
                "Theo dõi TOF để đánh giá hồi phục",
                "Nếu cần đảo ngược nhanh:",
                "  - Sugammadex (Bridion): 2-16 mg/kg IV (tùy mức độ block)",
                "  - Hoặc Neostigmine 0.04-0.07 mg/kg IV + Glycopyrrolate 0.01 mg/kg IV (nếu liều rocuronium thấp)",
                "Nếu không có reversal agent:",
                "  - Hỗ trợ thông khí cho đến khi hồi phục (có thể >1 giờ)",
                "Theo dõi: TOF, hô hấp, dấu hiệu hồi phục"
            ],
            "monitoring": "Theo dõi TOF, hô hấp liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Sugammadex (Bridion)",
                    "mechanism": "Cyclodextrin, bao bọc rocuronium và vecuronium, đảo ngược block nhanh chóng",
                    "indication": "Đảo ngược rocuronium/vecuronium (đặc biệt liều cao)",
                    "dose": "2-16 mg/kg IV (tùy mức độ block: 2mg/kg cho block nhẹ, 4mg/kg cho block vừa, 16mg/kg cho block sâu)",
                    "caution": "Sugammadex là reversal agent đặc hiệu, an toàn và hiệu quả. Ưu điểm so với neostigmine."
                },
                {
                    "agent": "Neostigmine + Glycopyrrolate",
                    "mechanism": "Neostigmine ức chế cholinesterase, tăng acetylcholine. Glycopyrrolate chống nhịp chậm.",
                    "indication": "Đảo ngược rocuronium (chỉ khi liều thấp, block nhẹ)",
                    "dose": "Neostigmine 0.04-0.07 mg/kg IV + Glycopyrrolate 0.01 mg/kg IV",
                    "caution": "Chỉ hiệu quả khi block nhẹ. Không hiệu quả khi block sâu hoặc liều cao."
                }
            ],
            "notes": "Sugammadex là reversal agent đặc hiệu và ưu tiên cho rocuronium. Neostigmine chỉ hiệu quả khi block nhẹ."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp dung dịch đã pha sẵn (10mg/ml).",
                "infusion_rate": "Intubation: 0.6-1.2 mg/kg IV bolus. Maintenance: 0.1-0.2 mg/kg mỗi 20-45 phút hoặc 5-12 mcg/kg/phút IV infusion. ICU: 5-12 mcg/kg/phút IV infusion (điều chỉnh theo TOF).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."
                ],
                "notes": "QUAN TRỌNG: 1) PHẢI hỗ trợ thông khí cho đến khi hồi phục, 2) Theo dõi TOF liên tục, 3) Dùng với sedative/anesthetic (bệnh nhân phải được an thần), 4) Liều RSI: 1-1.2 mg/kg để đạt tác dụng nhanh, 5) Thận trọng ở suy gan (tác dụng kéo dài), 6) Có reversal agent (sugammadex) - ưu điểm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Rocuronium (Esmeron)",
                "ACLS Guidelines 2020 - American Heart Association",
                "Rapid Sequence Intubation (RSI) Guidelines",
                "UpToDate - Rocuronium: Drug Information",
                "Anesthesia Guidelines - Neuromuscular Blocking Agents",
                "Medscape - Rocuronium Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, RSI guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Vecuronium": {
        "group": "Emergency - Non-depolarizing Neuromuscular Blocker (Aminosteroid)",
        "vietnamese_name": "Vecuronium, Norcuron",
        "administration": ["IV"],
        "indications": [
            "Đặt nội khí quản (intubation)",
            "Duy trì giãn cơ trong phẫu thuật",
            "Giãn cơ trong ICU (ARDS, status asthmaticus)",
            "Tăng áp lực nội sọ (intracranial hypertension)"
        ],
        "contraindications": [
            "Dị ứng vecuronium",
            "Bệnh nhược cơ (myasthenia gravis) - có thể cần liều cao hơn hoặc tác dụng kéo dài"
        ],
        "dosage": {
            "adult_intubation": "0.08-0.1 mg/kg IV bolus",
            "adult_maintenance": "0.01-0.015 mg/kg mỗi 25-40 phút hoặc 1-2 mcg/kg/phút IV infusion",
            "adult_icu": "1-2 mcg/kg/phút IV infusion (điều chỉnh theo TOF)",
            "pediatric_intubation": "0.08-0.1 mg/kg IV bolus",
            "notes": "Tác dụng trung bình (90-120 giây), thời gian tác dụng 30-45 phút. Không giải phóng histamine (ưu điểm so với atracurium)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (nhưng thận trọng, có thể kéo dài)",
            "under_30": "Thận trọng (có thể kéo dài, giảm liều maintenance)"
        },
        "side_effects": [
            "Giãn cơ kéo dài (đặc biệt ở suy gan, suy thận)",
            "Ức chế hô hấp (suy hô hấp nếu không hỗ trợ thông khí)",
            "Phản ứng dị ứng (hiếm)",
            "Không giải phóng histamine (ưu điểm)"
        ],
        "interactions": [
            "Aminoglycosides: tăng tác dụng, kéo dài thời gian giãn cơ",
            "Magnesium: tăng tác dụng, kéo dài thời gian giãn cơ",
            "Volatile anesthetics: tăng tác dụng",
            "Corticosteroids: có thể giảm tác dụng nhẹ"
        ],
        "pregnancy": "C - An toàn trong cấp cứu và gây mê",
        "mechanism_of_action": "Vecuronium là non-depolarizing neuromuscular blocker (aminosteroid). Ức chế cạnh tranh nicotinic acetylcholine receptors tại junction thần kinh-cơ, ngăn chặn acetylcholine gắn với receptor. Kết quả: giãn cơ xương. Vecuronium không giải phóng histamine (ưu điểm so với atracurium). Thời gian tác dụng trung bình (30-45 phút). Thải trừ chủ yếu qua gan (70-80%), một phần qua thận (20-30%).",
        "monitoring": [
            "TOF (train-of-four) monitoring liên tục (quan trọng)",
            "Hô hấp (phải hỗ trợ thông khí cho đến khi hồi phục)",
            "ECG (theo dõi nhịp tim)",
            "Dấu hiệu hồi phục (cử động tự nhiên, phản xạ)"
        ],
        "precautions": [
            "PHẢI hỗ trợ thông khí cho đến khi hồi phục (bệnh nhân không thể thở tự nhiên)",
            "Theo dõi TOF để đánh giá mức độ block và hồi phục",
            "Dùng với sedative/anesthetic (bệnh nhân phải được an thần)",
            "Thận trọng ở suy gan (thải trừ chủ yếu qua gan, tác dụng kéo dài)",
            "Thận trọng ở suy thận (thải trừ một phần qua thận, có thể kéo dài)",
            "Có reversal agent (sugammadex) - ưu điểm",
            "Không giải phóng histamine (ưu điểm so với atracurium)"
        ],
        "pharmacokinetics": {
            "half_life": "50-80 phút",
            "onset": "90-120 giây",
            "duration": "30-45 phút (phụ thuộc liều)",
            "protein_binding": "30-50%",
            "clearance": "Gan (70-80% - chuyển hóa), thận (20-30% - thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Dung dịch đã pha: ổn định trong 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "PHẢI hỗ trợ thông khí cho đến khi hồi phục. Bệnh nhân không thể thở tự nhiên khi đang dùng vecuronium.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Aminoglycosides ức chế giải phóng acetylcholine",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều vecuronium. Theo dõi TOF chặt chẽ."
                },
                {
                    "drug": "Magnesium (IV)",
                    "mechanism": "Magnesium ức chế giải phóng acetylcholine và tăng tác dụng của vecuronium",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều vecuronium. Theo dõi TOF. Có thể cần giảm liều magnesium."
                }
            ],
            "moderate": [
                {
                    "drug": "Volatile anesthetics (sevoflurane, isoflurane, desflurane)",
                    "mechanism": "Tăng nhạy cảm với neuromuscular blockers",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều vecuronium. Theo dõi TOF."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng vecuronium"
            ],
            "tương_đối": [
                "Bệnh nhược cơ (myasthenia gravis) - có thể cần liều cao hơn hoặc tác dụng kéo dài",
                "Suy gan nặng - tác dụng kéo dài (thải trừ chủ yếu qua gan)",
                "Suy thận nặng - tác dụng kéo dài (thải trừ một phần qua thận)",
                "Bệnh nhân cao tuổi - tăng nhạy cảm, tác dụng kéo dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Vecuronium là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Vecuronium có thể qua nhau thai nhưng nồng độ thấp. Được sử dụng rộng rãi trong gây mê sản khoa và có vẻ an toàn. Trong cấp cứu, lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết vecuronium có bài tiết vào sữa mẹ hay không. Thời gian bán thải 50-80 phút, protein binding 30-50%. Có thể bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (thải trừ chủ yếu qua gan)",
            "severe": "Thận trọng, giảm liều maintenance (tác dụng kéo dài)",
            "notes": "Vecuronium thải trừ chủ yếu qua gan (70-80%). Suy gan làm giảm thải trừ, tăng nồng độ và kéo dài tác dụng. Giảm liều maintenance ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Giãn cơ kéo dài (>45 phút)",
                "Suy hô hấp (bệnh nhân không thể thở tự nhiên)",
                "Không thể đảo ngược bằng neostigmine (nếu dùng liều cao)"
            ],
            "antidote": "Sugammadex (Bridion) - reversal agent đặc hiệu cho vecuronium và rocuronium. Hoặc neostigmine + glycopyrrolate (nếu liều thấp).",
            "treatment": [
                "Hỗ trợ thông khí: Đặt nội khí quản, thở máy cho đến khi hồi phục",
                "Theo dõi TOF để đánh giá hồi phục",
                "Nếu cần đảo ngược nhanh:",
                "  - Sugammadex (Bridion): 2-16 mg/kg IV (tùy mức độ block)",
                "  - Hoặc Neostigmine 0.04-0.07 mg/kg IV + Glycopyrrolate 0.01 mg/kg IV (nếu liều vecuronium thấp)",
                "Nếu không có reversal agent:",
                "  - Hỗ trợ thông khí cho đến khi hồi phục (có thể >1 giờ)",
                "Theo dõi: TOF, hô hấp, dấu hiệu hồi phục"
            ],
            "monitoring": "Theo dõi TOF, hô hấp liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Sugammadex (Bridion)",
                    "mechanism": "Cyclodextrin, bao bọc vecuronium và rocuronium, đảo ngược block nhanh chóng",
                    "indication": "Đảo ngược vecuronium/rocuronium (đặc biệt liều cao)",
                    "dose": "2-16 mg/kg IV (tùy mức độ block: 2mg/kg cho block nhẹ, 4mg/kg cho block vừa, 16mg/kg cho block sâu)",
                    "caution": "Sugammadex là reversal agent đặc hiệu, an toàn và hiệu quả. Ưu điểm so với neostigmine."
                },
                {
                    "agent": "Neostigmine + Glycopyrrolate",
                    "mechanism": "Neostigmine ức chế cholinesterase, tăng acetylcholine. Glycopyrrolate chống nhịp chậm.",
                    "indication": "Đảo ngược vecuronium (chỉ khi liều thấp, block nhẹ)",
                    "dose": "Neostigmine 0.04-0.07 mg/kg IV + Glycopyrrolate 0.01 mg/kg IV",
                    "caution": "Chỉ hiệu quả khi block nhẹ. Không hiệu quả khi block sâu hoặc liều cao."
                }
            ],
            "notes": "Sugammadex là reversal agent đặc hiệu và ưu tiên cho vecuronium. Neostigmine chỉ hiệu quả khi block nhẹ."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp dung dịch đã pha sẵn (1mg/ml).",
                "infusion_rate": "Intubation: 0.08-0.1 mg/kg IV bolus. Maintenance: 0.01-0.015 mg/kg mỗi 25-40 phút hoặc 1-2 mcg/kg/phút IV infusion. ICU: 1-2 mcg/kg/phút IV infusion (điều chỉnh theo TOF).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."
                ],
                "notes": "QUAN TRỌNG: 1) PHẢI hỗ trợ thông khí cho đến khi hồi phục, 2) Theo dõi TOF liên tục, 3) Dùng với sedative/anesthetic (bệnh nhân phải được an thần), 4) Thận trọng ở suy gan (tác dụng kéo dài), 5) Có reversal agent (sugammadex) - ưu điểm, 6) Không giải phóng histamine (ưu điểm)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vecuronium (Norcuron)",
                "ACLS Guidelines 2020 - American Heart Association",
                "UpToDate - Vecuronium: Drug Information",
                "Anesthesia Guidelines - Neuromuscular Blocking Agents",
                "Medscape - Vecuronium Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    
    "Cisatracurium": {
        "group": "Emergency - Non-depolarizing Neuromuscular Blocker (Benzylisoquinolinium)",
        "vietnamese_name": "Cisatracurium, Nimbex",
        "administration": ["IV"],
        "indications": [
            "Đặt nội khí quản (intubation)",
            "Duy trì giãn cơ trong phẫu thuật",
            "Giãn cơ trong ICU (ARDS, status asthmaticus) - THUỐC ƯU TIÊN",
            "Tăng áp lực nội sọ (intracranial hypertension)"
        ],
        "contraindications": [
            "Dị ứng cisatracurium",
            "Bệnh nhược cơ (myasthenia gravis) - có thể cần liều cao hơn hoặc tác dụng kéo dài"
        ],
        "dosage": {
            "adult_intubation": "0.15-0.2 mg/kg IV bolus",
            "adult_maintenance": "0.03 mg/kg mỗi 40-60 phút hoặc 1-3 mcg/kg/phút IV infusion",
            "adult_icu": "1-3 mcg/kg/phút IV infusion (điều chỉnh theo TOF)",
            "pediatric_intubation": "0.1-0.15 mg/kg IV bolus",
            "notes": "Tác dụng trung bình (2-3 phút), thời gian tác dụng 40-60 phút. Hofmann elimination - không phụ thuộc gan/thận (ưu điểm lớn). Thuốc ưu tiên cho ICU."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (Hofmann elimination)",
            "under_30": "Không đổi (Hofmann elimination - không phụ thuộc thận)"
        },
        "side_effects": [
            "Giãn cơ kéo dài (ít hơn so với vecuronium/rocuronium ở suy gan/thận)",
            "Ức chế hô hấp (suy hô hấp nếu không hỗ trợ thông khí)",
            "Phản ứng dị ứng (hiếm)",
            "Giải phóng histamine nhẹ (ít hơn atracurium)"
        ],
        "interactions": [
            "Aminoglycosides: tăng tác dụng, kéo dài thời gian giãn cơ",
            "Magnesium: tăng tác dụng, kéo dài thời gian giãn cơ",
            "Volatile anesthetics: tăng tác dụng"
        ],
        "pregnancy": "C - An toàn trong cấp cứu và gây mê",
        "mechanism_of_action": "Cisatracurium là non-depolarizing neuromuscular blocker (benzylisoquinolinium). Ức chế cạnh tranh nicotinic acetylcholine receptors tại junction thần kinh-cơ, ngăn chặn acetylcholine gắn với receptor. Kết quả: giãn cơ xương. Cisatracurium là đồng phân của atracurium, nhưng mạnh hơn 3 lần và ít giải phóng histamine hơn. ĐẶC ĐIỂM QUAN TRỌNG: Cisatracurium bị phân hủy bởi Hofmann elimination (phản ứng hóa học tự phát ở nhiệt độ và pH cơ thể), KHÔNG phụ thuộc gan/thận. Đây là ưu điểm lớn so với vecuronium/rocuronium. Thời gian tác dụng trung bình (40-60 phút).",
        "monitoring": [
            "TOF (train-of-four) monitoring liên tục (quan trọng)",
            "Hô hấp (phải hỗ trợ thông khí cho đến khi hồi phục)",
            "ECG (theo dõi nhịp tim)",
            "Dấu hiệu hồi phục (cử động tự nhiên, phản xạ)"
        ],
        "precautions": [
            "PHẢI hỗ trợ thông khí cho đến khi hồi phục (bệnh nhân không thể thở tự nhiên)",
            "Theo dõi TOF để đánh giá mức độ block và hồi phục",
            "Dùng với sedative/anesthetic (bệnh nhân phải được an thần)",
            "Ưu điểm: Không phụ thuộc gan/thận (Hofmann elimination) - an toàn ở suy gan/thận",
            "Thuốc ưu tiên cho ICU (đặc biệt ARDS) - không tích lũy ở suy gan/thận",
            "Ít giải phóng histamine hơn atracurium (ưu điểm)",
            "Không có reversal agent đặc hiệu (sugammadex không hiệu quả) - phải chờ tự hồi phục"
        ],
        "pharmacokinetics": {
            "half_life": "22-29 phút",
            "onset": "2-3 phút",
            "duration": "40-60 phút (phụ thuộc liều)",
            "protein_binding": "Không đáng kể",
            "clearance": "Hofmann elimination (phản ứng hóa học tự phát, không phụ thuộc gan/thận) - 77%, một phần qua thận (16%) và gan (7%)"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Dung dịch đã pha: ổn định trong 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "PHẢI hỗ trợ thông khí cho đến khi hồi phục. Bệnh nhân không thể thở tự nhiên khi đang dùng cisatracurium.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Aminoglycosides ức chế giải phóng acetylcholine",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều cisatracurium. Theo dõi TOF chặt chẽ."
                },
                {
                    "drug": "Magnesium (IV)",
                    "mechanism": "Magnesium ức chế giải phóng acetylcholine và tăng tác dụng của cisatracurium",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều cisatracurium. Theo dõi TOF. Có thể cần giảm liều magnesium."
                }
            ],
            "moderate": [
                {
                    "drug": "Volatile anesthetics (sevoflurane, isoflurane, desflurane)",
                    "mechanism": "Tăng nhạy cảm với neuromuscular blockers",
                    "effect": "Tăng tác dụng và kéo dài thời gian giãn cơ",
                    "management": "Thận trọng. Giảm liều cisatracurium. Theo dõi TOF."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cisatracurium"
            ],
            "tương_đối": [
                "Bệnh nhược cơ (myasthenia gravis) - có thể cần liều cao hơn hoặc tác dụng kéo dài",
                "Bệnh nhân cao tuổi - tăng nhạy cảm, tác dụng kéo dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Cisatracurium là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Cisatracurium có thể qua nhau thai nhưng nồng độ thấp. Được sử dụng rộng rãi trong gây mê sản khoa và có vẻ an toàn. Trong cấp cứu, lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết cisatracurium có bài tiết vào sữa mẹ hay không. Thời gian bán thải 22-29 phút. Có thể bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều (Hofmann elimination)",
            "moderate": "Không cần điều chỉnh liều (Hofmann elimination)",
            "severe": "Không cần điều chỉnh liều (Hofmann elimination - không phụ thuộc gan)",
            "notes": "Cisatracurium bị phân hủy chủ yếu bởi Hofmann elimination (77%), không phụ thuộc chức năng gan. Đây là ưu điểm lớn so với vecuronium/rocuronium. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Giãn cơ kéo dài (>60 phút)",
                "Suy hô hấp (bệnh nhân không thể thở tự nhiên)"
            ],
            "antidote": "Neostigmine + Glycopyrrolate (chỉ khi block nhẹ). Không có reversal agent đặc hiệu (sugammadex không hiệu quả với cisatracurium).",
            "treatment": [
                "Hỗ trợ thông khí: Đặt nội khí quản, thở máy cho đến khi hồi phục",
                "Theo dõi TOF để đánh giá hồi phục",
                "Nếu block nhẹ:",
                "  - Neostigmine 0.04-0.07 mg/kg IV + Glycopyrrolate 0.01 mg/kg IV",
                "Nếu block sâu:",
                "  - Hỗ trợ thông khí cho đến khi hồi phục (có thể >1 giờ)",
                "  - Cisatracurium tự phân hủy bởi Hofmann elimination",
                "Theo dõi: TOF, hô hấp, dấu hiệu hồi phục"
            ],
            "monitoring": "Theo dõi TOF, hô hấp liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Neostigmine + Glycopyrrolate",
                    "mechanism": "Neostigmine ức chế cholinesterase, tăng acetylcholine. Glycopyrrolate chống nhịp chậm.",
                    "indication": "Đảo ngược cisatracurium (chỉ khi liều thấp, block nhẹ)",
                    "dose": "Neostigmine 0.04-0.07 mg/kg IV + Glycopyrrolate 0.01 mg/kg IV",
                    "caution": "Chỉ hiệu quả khi block nhẹ. Không hiệu quả khi block sâu. Sugammadex KHÔNG hiệu quả với cisatracurium."
                }
            ],
            "notes": "Không có reversal agent đặc hiệu cho cisatracurium (sugammadex chỉ hiệu quả với rocuronium/vecuronium). Neostigmine chỉ hiệu quả khi block nhẹ. Cisatracurium tự phân hủy bởi Hofmann elimination."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp dung dịch đã pha sẵn (2mg/ml hoặc 10mg/ml).",
                "infusion_rate": "Intubation: 0.15-0.2 mg/kg IV bolus. Maintenance: 0.03 mg/kg mỗi 40-60 phút hoặc 1-3 mcg/kg/phút IV infusion. ICU: 1-3 mcg/kg/phút IV infusion (điều chỉnh theo TOF).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."
                ],
                "notes": "QUAN TRỌNG: 1) PHẢI hỗ trợ thông khí cho đến khi hồi phục, 2) Theo dõi TOF liên tục, 3) Dùng với sedative/anesthetic (bệnh nhân phải được an thần), 4) ƯU ĐIỂM: Không phụ thuộc gan/thận (Hofmann elimination) - an toàn ở suy gan/thận, 5) Thuốc ưu tiên cho ICU (đặc biệt ARDS), 6) Không có reversal agent đặc hiệu (sugammadex không hiệu quả)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cisatracurium (Nimbex)",
                "ACLS Guidelines 2020 - American Heart Association",
                "ARDS Guidelines - Neuromuscular Blockade",
                "UpToDate - Cisatracurium: Drug Information",
                "Anesthesia Guidelines - Neuromuscular Blocking Agents",
                "ROSE Trial - NEJM (2019) - Cisatracurium trong ARDS",
                "Medscape - Cisatracurium Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, ROSE trial (ARDS), và dữ liệu lâm sàng từ nhiều nguồn"
        }
    }
}

__all__ = ['NEUROMUSCULAR_BLOCKERS_DRUGS']


