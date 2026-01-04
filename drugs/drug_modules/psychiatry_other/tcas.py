"""
TCA (Tricyclic Antidepressant) Drugs
"""

TCA_DRUGS = {
    "Amitriptyline": {
        "group": "Psychiatry - Tricyclic Antidepressant (TCA)",
        "vietnamese_name": "Amitriptyline, Elavil",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Đau thần kinh (neuropathic pain)",
            "Migraine phòng ngừa",
            "Rối loạn giấc ngủ",
            "Đau cơ xơ hóa"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Nhồi máu cơ tim gần đây",
            "Block nhĩ thất độ 2-3",
            "Rối loạn nhịp tim",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_depression": "25-75mg x 1 lần/ngày buổi tối, tăng đến 50-150mg/ngày",
            "adult_neuropathic": "10-25mg buổi tối, tăng đến 25-100mg/ngày",
            "adult_max": "150-300mg/ngày",
            "notes": "Dùng buổi tối để tránh buồn ngủ ban ngày. Nguy cơ quá liều cao"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Khô miệng",
            "Táo bón",
            "Rối loạn nhịp tim",
            "Hạ huyết áp tư thế",
            "Nhìn mờ",
            "Tăng cân",
            "Nguy cơ quá liều (cardiotoxic)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định (nguy hiểm)",
            "Quinidine: tăng nồng độ amitriptyline",
            "Cimetidine: tăng nồng độ",
            "Alcohol: tăng tác dụng an thần",
            "Sympathomimetics: tăng nguy cơ tăng huyết áp"
        ],
        "pregnancy": "C - D trong 3 tháng đầu",
        "mechanism_of_action": "Amitriptyline là tricyclic antidepressant (TCA) ức chế tái hấp thu norepinephrine và serotonin ở synap thần kinh, tăng nồng độ các chất dẫn truyền thần kinh này. Cũng có tác dụng chẹn muscarinic (kháng cholinergic), histamine H1 (an thần), và alpha-1 adrenergic (hạ huyết áp). Tác dụng chống trầm cảm, giảm đau thần kinh (cơ chế chưa rõ hoàn toàn), phòng ngừa migraine. Có tác dụng an thần mạnh do chẹn histamine H1",
        "monitoring": [
            "ECG trước khi bắt đầu và định kỳ (đặc biệt ở bệnh nhân có bệnh tim, cao tuổi) - QT kéo dài, block nhĩ thất",
            "Nhịp tim, huyết áp (hạ huyết áp tư thế, rối loạn nhịp)",
            "Dấu hiệu quá liều: nhịp tim nhanh, loạn nhịp, co giật, hôn mê (cấp cứu)",
            "Triệu chứng kháng cholinergic: khô miệng, táo bón, nhìn mờ, bí tiểu",
            "Tâm trạng và triệu chứng trầm cảm",
            "Chức năng gan nếu có triệu chứng (hiếm)"
        ],
        "precautions": [
            "NGUY CƠ QUÁ LIỀU CAO - cardiotoxic (rối loạn nhịp, block nhĩ thất), có thể tử vong",
            "Chỉ kê đơn số lượng ít, theo dõi sát bệnh nhân có ý định tự tử",
            "Không dùng với MAO inhibitor (chống chỉ định tuyệt đối - nguy cơ cao huyết áp, sốt, co giật, tử vong)",
            "Thận trọng ở bệnh nhân có bệnh tim, block nhĩ thất (chống chỉ định block độ 2-3)",
            "Dùng buổi tối để tránh buồn ngủ ban ngày (tác dụng an thần mạnh)",
            "Khởi đầu với liều thấp (10-25mg), tăng dần",
            "Giảm liều dần khi ngừng (tránh hội chứng cai)",
            "Tránh rượu (tăng tác dụng an thần, nguy cơ quá liều)",
            "Thận trọng khi lái xe hoặc vận hành máy móc (buồn ngủ, nhìn mờ)",
            "Theo dõi sát bệnh nhân có ý định tự tử (tăng nguy cơ trong vài tuần đầu)"
        ],
        "pharmacokinetics": {
            "half_life": "10-28 giờ (dài)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm), nhanh hơn (giảm đau, an thần)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "82-96% (cao)",
            "clearance": "Gan (chuyển hóa qua CYP2D6, CYP2C19, CYP1A2), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Quá liều có thể gây rối loạn nhịp tim nghiêm trọng, block nhĩ thất, co giật, hôn mê, tử vong. Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa catecholamines, tăng nồng độ serotonin và norepinephrine",
                    "effect": "Hội chứng serotonin, tăng huyết áp nghiêm trọng, sốt cao, co giật, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu amitriptyline."
                },
                {
                    "drug": "Quinidine, Cimetidine",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa amitriptyline",
                    "effect": "Tăng nồng độ amitriptyline, tăng nguy cơ độc tính (rối loạn nhịp, block nhĩ thất)",
                    "management": "Giảm liều amitriptyline 50%. Theo dõi ECG. Thận trọng."
                },
                {
                    "drug": "Sympathomimetics (epinephrine, norepinephrine)",
                    "mechanism": "Tăng tác dụng alpha-adrenergic",
                    "effect": "Tăng huyết áp nghiêm trọng, rối loạn nhịp tim",
                    "management": "Tránh dùng. Nếu cần, dùng liều thấp và theo dõi huyết áp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng an thần, suy hô hấp, nguy cơ quá liều",
                    "management": "Tránh rượu. Cảnh báo bệnh nhân về nguy cơ."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Anticholinergics (atropine, benztropine)",
                    "mechanism": "Tăng tác dụng kháng cholinergic",
                    "effect": "Tăng khô miệng, táo bón, bí tiểu, nhìn mờ, lú lẫn",
                    "management": "Thận trọng. Giảm liều hoặc tránh dùng cùng."
                }
            ],
            "minor": [
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa",
                    "effect": "Giảm nồng độ amitriptyline",
                    "management": "Tăng liều amitriptyline nếu cần"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Nhồi máu cơ tim gần đây (<6 tháng)",
                "Block nhĩ thất độ 2-3",
                "Rối loạn nhịp tim nặng",
                "Suy tim nặng (NYHA class IV)",
                "Dị ứng amitriptyline hoặc TCA"
            ],
            "tương_đối": [
                "Bệnh tim (thiếu máu cơ tim, suy tim nhẹ-trung bình) - thận trọng, theo dõi ECG",
                "Block nhĩ thất độ 1 - thận trọng",
                "Tăng nhãn áp (glaucoma) - tăng nguy cơ",
                "Bí tiểu - tăng nguy cơ",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Có ý định tự tử - chỉ kê đơn số lượng ít"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Nhồi máu cơ tim gần đây (<6 tháng)",
                "Block nhĩ thất độ 2-3",
                "Rối loạn nhịp tim nặng",
                "Suy tim nặng (NYHA class IV)",
                "Dị ứng amitriptyline hoặc TCA"
            ],
            "tương_đối": [
                "Bệnh tim (thiếu máu cơ tim, suy tim nhẹ-trung bình) - thận trọng, theo dõi ECG",
                "Block nhĩ thất độ 1 - thận trọng",
                "Tăng nhãn áp (glaucoma) - tăng nguy cơ",
                "Bí tiểu - tăng nguy cơ",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Có ý định tự tử - chỉ kê đơn số lượng ít"
            ]
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Amitriptyline không được lọc sạch hiệu quả qua thẩm phân máu do protein binding cao.",
            "notes": "Amitriptyline thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy, đặc biệt với half-life dài (10-28 giờ). Giảm liều và theo dõi chặt chẽ ở suy thận nặng."
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Có nguy cơ dị tật thai nhi (dị tật tim, dị tật chi) khi dùng trong 3 tháng đầu, đặc biệt liều cao. Có thể gây hội chứng cai ở trẻ sơ sinh (kích động, khó thở, run, co giật) nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh. Nguy cơ rối loạn phát triển thần kinh thấp.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Amitriptyline bài tiết vào sữa mẹ ở nồng độ thấp (<5% liều mẹ). Nồng độ trong máu trẻ bú mẹ thường rất thấp. Có thể gây buồn ngủ, bú kém ở trẻ. Ít báo cáo về tác dụng phụ nghiêm trọng.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém, táo bón ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Amitriptyline chuyển hóa ở gan qua CYP2D6, CYP2C19, CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính. Tuy nhiên, ít gây độc gan trực tiếp."
        },
        "overdose_management": {
            "symptoms": [
                "Giai đoạn sớm: Buồn ngủ, lú lẫn, chóng mặt, nhìn mờ",
                "Giai đoạn nặng: Rối loạn nhịp tim (nhịp nhanh, rung nhĩ, block nhĩ thất), hạ huyết áp hoặc tăng huyết áp",
                "Co giật, hôn mê",
                "Suy hô hấp",
                "Triệu chứng kháng cholinergic: khô miệng, bí tiểu, nhịp tim nhanh, sốt",
                "Tử vong do rối loạn nhịp tim hoặc suy hô hấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Có thể dùng sodium bicarbonate cho rối loạn nhịp",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn ngay lập tức (quan trọng nhất)",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ (thận trọng nếu đã hôn mê)",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục - rối loạn nhịp là nguy hiểm nhất",
                "Điều trị rối loạn nhịp: Sodium bicarbonate (1-2 mEq/kg IV bolus) để điều chỉnh QT kéo dài và block nhĩ thất",
                "Điều trị co giật: Benzodiazepines (lorazepam, diazepam)",
                "Điều trị hạ huyết áp: Truyền dịch, vận mạch nếu cần",
                "Theo dõi điện giải, đường huyết",
                "Lọc máu (hemodialysis) KHÔNG hiệu quả do protein binding cao",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài)"
            ],
            "monitoring": "ECG liên tục (rối loạn nhịp), huyết áp, nhịp tim, ý thức, hô hấp, điện giải, đường huyết, nhiệt độ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm kích ứng dạ dày",
                "timing": "Dùng buổi tối (1 lần/ngày) để tránh buồn ngủ ban ngày. Có thể chia 2-3 lần nếu liều cao hoặc tác dụng phụ nhiều"
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
                "FDA Drug Label - Elavil (amitriptyline)",
                "UpToDate - Amitriptyline: Drug information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "neurological"],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (QT prolongation, AV block - Black Box Warning)", "Blood pressure (orthostatic hypotension)", "Suicidal ideation (Black Box Warning - children/adolescents)", "Overdose risk (cardiotoxic - Black Box Warning)", "Anticholinergic symptoms"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Suicidal Behavior (Children/Adolescents)",
            "FDA Black Box Warning - Overdose Risk (Cardiotoxic - can be fatal)",
            "ISMP High Alert Medications",
            "APA Guidelines - Depression"
        ]
    },
    
    "Clomipramine": {
        "group": "Psychiatry - Tricyclic Antidepressant (TCA)",
        "vietnamese_name": "Clomipramine, Anafranil",
        "administration": ["PO"],
        "indications": [
            "Rối loạn ám ảnh cưỡng chế (OCD)",
            "Trầm cảm",
            "Panic disorder",
            "Đau thần kinh (neuropathic pain)"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Nhồi máu cơ tim gần đây",
            "Block nhĩ thất độ 2-3",
            "Rối loạn nhịp tim",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_ocd": "25mg/ngày, tăng dần đến 100-250mg/ngày (chia 2-3 lần)",
            "adult_depression": "25-75mg/ngày, tăng đến 100-250mg/ngày",
            "adult_max": "250mg/ngày",
            "notes": "TCA mạnh nhất về ức chế tái hấp thu serotonin. Dùng cho OCD là chỉ định chính. Tăng liều chậm."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Thận trọng, giảm liều"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Khô miệng",
            "Táo bón",
            "Rối loạn nhịp tim",
            "Hạ huyết áp tư thế",
            "Nhìn mờ",
            "Tăng cân",
            "Nguy cơ quá liều (cardiotoxic)",
            "Tác dụng phụ serotonin (nếu dùng với SSRI/MAOI)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định (nguy hiểm)",
            "SSRIs: tăng nguy cơ serotonin syndrome",
            "Quinidine, Cimetidine: tăng nồng độ",
            "Alcohol: tăng tác dụng an thần"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Clomipramine là tricyclic antidepressant (TCA) với tác dụng ức chế tái hấp thu serotonin mạnh nhất trong các TCA. Ức chế tái hấp thu norepinephrine và serotonin ở synap thần kinh, tăng nồng độ các chất dẫn truyền thần kinh này. Cũng có tác dụng chẹn muscarinic (kháng cholinergic), histamine H1 (an thần), và alpha-1 adrenergic (hạ huyết áp). Đặc điểm: TCA mạnh nhất về ức chế tái hấp thu serotonin, do đó hiệu quả đặc biệt với rối loạn ám ảnh cưỡng chế (OCD) - chỉ định chính. Cũng dùng cho trầm cảm và panic disorder.",
        "monitoring": [
            "ECG trước khi bắt đầu và định kỳ (đặc biệt ở bệnh nhân có bệnh tim, cao tuổi) - QT kéo dài, block nhĩ thất",
            "Triệu chứng OCD (Y-BOCS score nếu có)",
            "Nhịp tim, huyết áp (hạ huyết áp tư thế, rối loạn nhịp)",
            "Dấu hiệu quá liều: nhịp tim nhanh, loạn nhịp, co giật, hôn mê",
            "Triệu chứng kháng cholinergic: khô miệng, táo bón, nhìn mờ, bí tiểu",
            "Dấu hiệu serotonin syndrome (nếu dùng với SSRI/MAOI): sốt, kích động, co giật"
        ],
        "precautions": [
            "NGUY CƠ QUÁ LIỀU CAO - cardiotoxic (rối loạn nhịp, block nhĩ thất), có thể tử vong",
            "Chỉ kê đơn số lượng ít, theo dõi sát bệnh nhân có ý định tự tử",
            "Không dùng với MAO inhibitor (chống chỉ định tuyệt đối)",
            "Thận trọng khi dùng với SSRIs (tăng nguy cơ serotonin syndrome)",
            "Thận trọng ở bệnh nhân có bệnh tim, block nhĩ thất",
            "Dùng buổi tối để tránh buồn ngủ ban ngày",
            "Khởi đầu với liều thấp (25mg), tăng dần",
            "Giảm liều dần khi ngừng"
        ],
        "pharmacokinetics": {
            "half_life": "19-37 giờ (dài)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm, OCD)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "97% (rất cao)",
            "clearance": "Gan (chuyển hóa qua CYP2D6, CYP2C19), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Quá liều có thể gây rối loạn nhịp tim nghiêm trọng, block nhĩ thất, co giật, hôn mê, tử vong. Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa catecholamines, tăng nồng độ serotonin và norepinephrine",
                    "effect": "Hội chứng serotonin nghiêm trọng, tăng huyết áp, sốt cao, co giật, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu clomipramine."
                },
                {
                    "drug": "SSRIs (fluoxetine, sertraline, paroxetine, citalopram, escitalopram)",
                    "mechanism": "Cả hai đều ức chế tái hấp thu serotonin, tác dụng cộng dồn",
                    "effect": "Hội chứng serotonin: sốt, kích động, co giật, rối loạn ý thức, có thể tử vong",
                    "management": "TRÁNH dùng cùng. Ngừng SSRI ít nhất 5 tuần (fluoxetine) hoặc 2 tuần (các SSRI khác) trước khi bắt đầu clomipramine."
                }
            ],
            "moderate": [
                {
                    "drug": "Quinidine, Cimetidine",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa clomipramine",
                    "effect": "Tăng nồng độ clomipramine, tăng nguy cơ độc tính",
                    "management": "Giảm liều clomipramine 50%. Theo dõi ECG."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dùng MAO inhibitor",
                "Dùng SSRI (tăng nguy cơ serotonin syndrome)",
                "Nhồi máu cơ tim gần đây (<6 tháng)",
                "Block nhĩ thất độ 2-3",
                "Rối loạn nhịp tim nặng",
                "Suy tim nặng (NYHA class IV)"
            ],
            "tương_đối": [
                "Bệnh tim - thận trọng, theo dõi ECG",
                "Block nhĩ thất độ 1 - thận trọng",
                "Tăng nhãn áp (glaucoma) - tăng nguy cơ",
                "Bí tiểu - tăng nguy cơ",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Có nguy cơ dị tật thai nhi khi dùng trong 3 tháng đầu. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng gần ngày sinh.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Clomipramine bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây buồn ngủ, bú kém ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp",
            "notes": "Clomipramine chuyển hóa ở gan qua CYP2D6, CYP2C19. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Rối loạn nhịp tim (nhịp nhanh, rung nhĩ, block nhĩ thất)",
                "Hạ huyết áp hoặc tăng huyết áp",
                "Co giật, hôn mê",
                "Suy hô hấp",
                "Triệu chứng kháng cholinergic: khô miệng, bí tiểu, nhịp tim nhanh, sốt",
                "Hội chứng serotonin (nếu dùng với SSRI/MAOI)"
            ],
            "antidote": "Không có antidote đặc hiệu. Có thể dùng sodium bicarbonate cho rối loạn nhịp",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn ngay lập tức",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi ECG liên tục",
                "Điều trị rối loạn nhịp: Sodium bicarbonate (1-2 mEq/kg IV bolus)",
                "Điều trị co giật: Benzodiazepines",
                "Điều trị hạ huyết áp: Truyền dịch, vận mạch",
                "Lọc máu KHÔNG hiệu quả do protein binding cao (97%)",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, hô hấp, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn",
                "timing": "Dùng buổi tối hoặc chia 2-3 lần/ngày. Khởi đầu 25mg/ngày, tăng dần. KHÔNG ngừng đột ngột."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Anafranil (clomipramine)",
                "UpToDate - Clomipramine: Drug information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "neurological"],
            "qt_prolongation": True,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG (QT prolongation, AV block - Black Box Warning)", "Blood pressure (orthostatic hypotension)", "Suicidal ideation (Black Box Warning - children/adolescents)", "Overdose risk (cardiotoxic - Black Box Warning)", "Seizures (higher risk than other TCAs)", "Anticholinergic symptoms"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Suicidal Behavior (Children/Adolescents)",
            "FDA Black Box Warning - Overdose Risk (Cardiotoxic - can be fatal)",
            "FDA Black Box Warning - Seizures (higher risk than other TCAs)",
            "ISMP High Alert Medications",
            "APA Guidelines - OCD"
        ]
    },
}

__all__ = ['TCA_DRUGS']
