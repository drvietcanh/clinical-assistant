"""
Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data
"""

EMERGENCY_DRUGS = {
"Epinephrine": {
        "group": "Emergency - Catecholamine (Alpha & Beta Agonist)",
        "vietnamese_name": "Epinephrine, Adrenaline",
        "administration": ["IV", "IM", "SC", "INH", "IT"],
        "indications": [
            "Ngừng tim (cardiac arrest)",
            "Sốc phản vệ (anaphylaxis)",
            "Sốc (shock)",
            "Cơn hen nặng (IV/nebulizer)",
            "Co thắt thanh quản"
        ],
        "contraindications": [
            "Không có trong cấp cứu ngừng tim",
            "Sốc phản vệ: không có chống chỉ định tuyệt đối"
        ],
        "dosage": {
            "adult_cardiac_arrest_iv": "1mg IV mỗi 3-5 phút (hoặc 0.1mg/kg)",
            "adult_cardiac_arrest_it": "2-2.5mg IT",
            "adult_anaphylaxis_im": "0.3-0.5mg IM (0.3-0.5ml 1:1000) ở đùi ngoài",
            "adult_anaphylaxis_iv": "0.1-0.25mg IV bolus (pha 1mg trong 10ml = 0.1mg/ml)",
            "adult_shock": "0.1-2mcg/kg/phút IV infusion",
            "pediatric_cardiac_arrest": "0.01mg/kg (0.1ml/kg 1:10000) IV/IT mỗi 3-5 phút",
            "pediatric_anaphylaxis_im": "0.01mg/kg IM (0.01ml/kg 1:1000) ở đùi ngoài (tối đa 0.5mg)",
            "notes": "1:1000 = 1mg/ml (dùng IM/SC), 1:10000 = 0.1mg/ml (dùng IV). Đùi ngoài cho anaphylaxis"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Tim đập nhanh",
            "Tăng huyết áp",
            "Lo lắng, run tay",
            "Đau đầu",
            "Nhồi máu cơ tim (với liều cao)",
            "Rối loạn nhịp tim",
            "Hoại tử (nếu tiêm ngoài mạch)"
        ],
        "interactions": [
            "Beta-blockers: đối kháng tác dụng",
            "MAOIs: tăng tác dụng",
            "Tricyclic antidepressants: tăng tác dụng",
            "Digoxin: tăng nguy cơ loạn nhịp"
        ],
        "pregnancy": "C - An toàn trong cấp cứu",
        "mechanism_of_action": "Non-selective alpha và beta-adrenergic receptor agonist. Kích thích alpha-1 receptors → co mạch ngoại vi, tăng huyết áp. Kích thích beta-1 receptors → tăng nhịp tim, tăng co bóp cơ tim, tăng cung lượng tim. Kích thích beta-2 receptors → giãn phế quản, giãn mạch cơ xương. Trong ngừng tim: tăng áp lực tưới máu vành, tăng khả năng khử rung thành công.",
        "monitoring": [
            "Nhịp tim và huyết áp liên tục",
            "Điện tâm đồ (ECG) - theo dõi rối loạn nhịp",
            "Lactate máu (trong shock)",
            "Đường huyết (tăng đường huyết)",
            "Dấu hiệu thiếu máu cục bộ (đau ngực, thay đổi ST)",
            "Tổn thương mô tại chỗ tiêm (hoại tử nếu tiêm ngoài mạch)"
        ],
        "precautions": [
            "TUYỆT ĐỐI KHÔNG tiêm ngoài mạch (có thể gây hoại tử)",
            "Pha loãng đúng nồng độ: 1:1000 (1mg/ml) cho IM/SC, 1:10000 (0.1mg/ml) cho IV",
            "Trong anaphylaxis: tiêm IM ở đùi ngoài (hấp thu nhanh hơn cánh tay)",
            "Theo dõi sát trong 20 phút đầu (nguy cơ rối loạn nhịp, tăng huyết áp)",
            "Thận trọng ở bệnh nhân bệnh mạch vành (có thể gây nhồi máu cơ tim)",
            "Tránh dùng với thuốc chẹn beta (có thể gây tăng huyết áp nặng do không đối kháng alpha)",
            "Tiêm IV chậm, pha loãng để tránh tăng huyết áp đột ngột"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 phút (rất ngắn)",
            "onset": "IV: ngay lập tức; IM: 5-10 phút",
            "duration": "3-10 phút (IV), 10-30 phút (IM)",
            "protein_binding": "Không đáng kể (catecholamine)",
            "clearance": "Rất nhanh, bị bất hoạt bởi enzyme (MAO và COMT trong gan và mô)"
        },
        "storage": "Bảo quản ở nhiệt độ 2-8°C, tránh ánh sáng, tránh đông lạnh. Kiểm tra màu sắc trước dùng (hóa nâu = hỏng).",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, tiêm ngoài mạch có thể gây hoại tử mô. Liều cao có thể gây nhồi máu cơ tim, đột quỵ, hoặc tử vong.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (non-selective)",
                    "mechanism": "Beta-blockers đối kháng tác dụng beta của epinephrine, nhưng không đối kháng tác dụng alpha. Kết quả: tăng huyết áp nặng do chỉ còn tác dụng co mạch alpha, không có tác dụng giãn mạch beta-2.",
                    "effect": "Tăng huyết áp nặng, nguy cơ đột quỵ, nhồi máu cơ tim, phù phổi cấp",
                    "management": "TRÁNH dùng epinephrine với beta-blockers non-selective. Nếu cần trong cấp cứu: dùng liều thấp, theo dõi huyết áp chặt chẽ. Có thể cần thuốc giãn mạch (phentolamine) nếu tăng huyết áp nặng."
                },
                {
                    "drug": "MAOIs (Monoamine Oxidase Inhibitors)",
                    "mechanism": "MAOIs ức chế enzyme MAO chuyển hóa epinephrine, làm tăng nồng độ và thời gian tác dụng của epinephrine.",
                    "effect": "Tăng tác dụng và thời gian tác dụng của epinephrine, tăng nguy cơ tăng huyết áp nặng, nhồi máu cơ tim, đột quỵ",
                    "management": "GIẢM LIỀU epinephrine xuống 10-25% liều thông thường. Theo dõi huyết áp chặt chẽ. Trong cấp cứu: dùng liều thấp nhất có hiệu quả."
                },
                {
                    "drug": "Tricyclic Antidepressants (TCAs)",
                    "mechanism": "TCAs ức chế tái hấp thu norepinephrine, tăng nồng độ catecholamine, tăng tác dụng của epinephrine.",
                    "effect": "Tăng tác dụng của epinephrine, tăng nguy cơ tăng huyết áp nặng, rối loạn nhịp tim",
                    "management": "Thận trọng, giảm liều epinephrine. Theo dõi huyết áp và ECG chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Digoxin làm tăng nhạy cảm của cơ tim với catecholamine, tăng nguy cơ rối loạn nhịp tim.",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim (nhịp nhanh thất, rung thất), đặc biệt ở bệnh nhân digoxin độc tính",
                    "management": "Thận trọng, theo dõi ECG chặt chẽ. Kiểm tra nồng độ digoxin nếu có thể. Tránh dùng epinephrine nếu có dấu hiệu digoxin độc tính."
                },
                {
                    "drug": "Alpha-blockers",
                    "mechanism": "Alpha-blockers đối kháng tác dụng alpha của epinephrine, có thể làm giảm hiệu quả điều trị sốc.",
                    "effect": "Giảm hiệu quả điều trị sốc, có thể cần liều cao hơn",
                    "management": "Có thể cần tăng liều epinephrine. Theo dõi đáp ứng điều trị."
                }
            ],
            "minor": [
                {
                    "drug": "Beta-2 agonists (Salbutamol, Salmeterol)",
                    "mechanism": "Cùng tác dụng beta-2, có thể tăng tác dụng giãn phế quản và tăng nhịp tim.",
                    "effect": "Tăng nhịp tim, run tay (nhẹ)",
                    "management": "Theo dõi nhịp tim. Không cần điều chỉnh liều thường quy."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Không có chống chỉ định tuyệt đối trong cấp cứu ngừng tim",
                "Dị ứng epinephrine (hiếm nhưng nguy hiểm)"
            ],
            "relative": [
                "Bệnh mạch vành - tăng nguy cơ nhồi máu cơ tim, đau thắt ngực",
                "Tăng huyết áp nặng không kiểm soát - có thể làm tăng huyết áp hơn nữa",
                "Rối loạn nhịp tim nặng - có thể làm nặng rối loạn nhịp",
                "Đột quỵ gần đây - tăng nguy cơ tái phát",
                "Pheochromocytoma - tăng nguy cơ tăng huyết áp nặng, cơn tăng huyết áp",
                "Dùng với beta-blockers non-selective - tăng huyết áp nặng",
                "Dùng với MAOIs - tăng tác dụng, cần giảm liều",
                "Dùng với TCAs - tăng tác dụng, cần thận trọng",
                "Bệnh nhân cao tuổi - tăng nhạy cảm với tác dụng phụ",
                "Bệnh nhân có bệnh mạch máu ngoại biên - tăng nguy cơ thiếu máu cục bộ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Epinephrine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Epinephrine có thể qua nhau thai và có thể gây co mạch, giảm tưới máu nhau thai. Tuy nhiên, trong cấp cứu (sốc phản vệ, ngừng tim), lợi ích cứu sống mẹ vượt quá nguy cơ cho thai nhi. Sốc phản vệ và ngừng tim có thể gây tử vong cho cả mẹ và thai nhi nếu không điều trị. Epinephrine được sử dụng trong cấp cứu ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Epinephrine có thời gian bán thải rất ngắn (2-3 phút) và bị chuyển hóa nhanh. Không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Epinephrine có thời gian bán thải rất ngắn và không bài tiết vào sữa mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Epinephrine chuyển hóa nhanh bởi MAO và COMT, nhưng không phụ thuộc vào chức năng gan.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Không cần điều chỉnh liều. Epinephrine chuyển hóa nhanh, không tích lũy ở suy gan.",
            "notes": "Epinephrine bị chuyển hóa nhanh bởi enzyme MAO và COMT trong gan và mô, nhưng không phụ thuộc vào chức năng gan. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng huyết áp nặng (có thể >200/120 mmHg)",
                "Nhịp tim nhanh nặng (>150-200 bpm)",
                "Nhồi máu cơ tim",
                "Đột quỵ",
                "Phù phổi cấp",
                "Rối loạn nhịp tim (rung nhĩ, rung thất)",
                "Co giật",
                "Hoại tử mô (nếu tiêm ngoài mạch)"
            ],
            "antidote": "Không có antidote đặc hiệu. Có thể dùng thuốc giãn mạch (phentolamine, nitroglycerin) để đối kháng tác dụng alpha. Beta-blockers có thể đối kháng tác dụng beta nhưng nguy hiểm (tăng huyết áp nặng).",
            "treatment": [
                "Ngừng ngay epinephrine nếu đang truyền",
                "Theo dõi ECG và huyết áp liên tục",
                "Nếu tăng huyết áp nặng:",
                "  - Phentolamine 5-10mg IV (đối kháng alpha, giảm huyết áp)",
                "  - Hoặc Nitroglycerin IV (giãn mạch, giảm huyết áp)",
                "  - Hoặc Labetalol (alpha + beta blocker) - thận trọng",
                "Nếu nhịp tim nhanh nặng:",
                "  - Beta-blocker (metoprolol, esmolol) - THẬN TRỌNG, chỉ dùng nếu không có tăng huyết áp nặng",
                "  - Nếu có tăng huyết áp + nhịp nhanh: Labetalol",
                "Nếu nhồi máu cơ tim: Điều trị theo protocol nhồi máu cơ tim (aspirin, clopidogrel, statin, có thể cần can thiệp)",
                "Nếu đột quỵ: Điều trị theo protocol đột quỵ",
                "Nếu phù phổi cấp: Furosemide, nitroglycerin, hỗ trợ hô hấp",
                "Nếu rối loạn nhịp: Điều trị theo protocol rối loạn nhịp",
                "Nếu hoại tử mô (tiêm ngoài mạch):",
                "  - Phentolamine 5-10mg pha trong 10-15ml NS tiêm quanh vùng hoại tử (trong vòng 12 giờ)",
                "  - Chườm ấm",
                "  - Có thể cần phẫu thuật nếu hoại tử nặng",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG trong ít nhất 2-4 giờ"
            ],
            "monitoring": "Theo dõi ECG, huyết áp, nhịp tim liên tục trong ít nhất 2-4 giờ sau khi dùng. Theo dõi lâu hơn nếu có biến chứng (nhồi máu cơ tim, đột quỵ, rối loạn nhịp)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Phentolamine",
                    "mechanism": "Alpha-blocker, đối kháng tác dụng alpha của epinephrine (co mạch, tăng huyết áp)",
                    "indication": "Tăng huyết áp nặng do quá liều epinephrine, hoại tử mô do tiêm ngoài mạch",
                    "dose": "5-10mg IV cho tăng huyết áp, 5-10mg pha trong 10-15ml NS tiêm quanh vùng hoại tử (trong vòng 12 giờ)"
                },
                {
                    "agent": "Nitroglycerin",
                    "mechanism": "Giãn mạch, giảm huyết áp",
                    "indication": "Tăng huyết áp nặng do quá liều epinephrine",
                    "dose": "5-10mcg/phút IV, tăng dần đến khi đạt huyết áp mục tiêu"
                },
                {
                    "agent": "Beta-blockers (thận trọng)",
                    "mechanism": "Đối kháng tác dụng beta của epinephrine (nhịp tim nhanh)",
                    "indication": "Nhịp tim nhanh nặng do quá liều epinephrine (CHỈ dùng nếu không có tăng huyết áp nặng)",
                    "dose": "Metoprolol 5mg IV hoặc Esmolol 0.5mg/kg IV bolus, sau đó 50-200mcg/kg/phút IV infusion"
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha loãng: 1mg epinephrine (1ml 1:1000) trong 9ml NS = 0.1mg/ml (1:10000). Hoặc dùng trực tiếp dung dịch 1:10000 nếu có.",
                "infusion_rate": "Cardiac arrest: 1mg IV bolus mỗi 3-5 phút. Anaphylaxis: 0.1-0.25mg IV bolus (pha loãng). Shock: 0.1-2mcg/kg/phút IV infusion (pha 1mg trong 250ml D5W = 4mcg/ml).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."],
                "notes": "QUAN TRỌNG: 1) Pha đúng nồng độ: 1:1000 (1mg/ml) cho IM/SC, 1:10000 (0.1mg/ml) cho IV, 2) TUYỆT ĐỐI KHÔNG tiêm ngoài mạch (hoại tử), 3) Trong anaphylaxis: tiêm IM ở đùi ngoài (hấp thu nhanh hơn), 4) Theo dõi huyết áp và ECG chặt chẽ, 5) Kiểm tra màu sắc trước dùng (hóa nâu = hỏng)."
            },
            "im": {
                "reconstitution": "Dùng trực tiếp dung dịch 1:1000 (1mg/ml).",
                "injection_site": "Đùi ngoài (vastus lateralis) - hấp thu nhanh nhất. Có thể dùng cánh tay nhưng hấp thu chậm hơn.",
                "notes": "Anaphylaxis: 0.3-0.5mg IM ở đùi ngoài. Trẻ em: 0.01mg/kg IM ở đùi ngoài (tối đa 0.5mg). Tiêm sâu vào cơ, không tiêm vào mỡ dưới da."
            },
            "inhaled": {
                "reconstitution": "Dùng dung dịch 1:1000 (1mg/ml) pha trong 3-5ml NS cho nebulizer.",
                "dose": "0.5-1mg (0.5-1ml 1:1000) pha trong 3-5ml NS, khí dung mỗi 15-20 phút nếu cần.",
                "notes": "Dùng trong cơn hen nặng. Theo dõi nhịp tim và huyết áp."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Epinephrine",
                "ACLS Guidelines 2020 - American Heart Association",
                "Anaphylaxis Guidelines - World Allergy Organization",
                "UpToDate - Epinephrine: Drug Information",
                "Medscape - Epinephrine Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Epinephrine Monograph",
                "Micromedex - Epinephrine Drug Information"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, anaphylaxis guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Atropine": {
        "group": "Emergency - Anticholinergic",
        "vietnamese_name": "Atropine",
        "administration": ["IV", "IM", "IO", "IT"],
        "indications": [
            "Nhịp tim chậm có triệu chứng",
            "Block nhĩ thất",
            "Quá liều organophosphate",
            "Chuẩn bị phẫu thuật (giảm tiết)",
            "Ngừng tim với nhịp chậm/PEA"
        ],
        "contraindications": [
            "Glaucoma góc đóng",
            "Tắc nghẽn đường tiểu",
            "Nhịp tim nhanh",
            "Sốt"
        ],
        "dosage": {
            "adult_bradycardia": "0.5-1mg IV mỗi 3-5 phút (tối đa 3mg)",
            "adult_cardiac_arrest": "1mg IV/IT, lặp lại mỗi 3-5 phút",
            "adult_organophosphate": "2-5mg IV, lặp lại đến khi đạt tác dụng",
            "pediatric_bradycardia": "0.02mg/kg IV (tối thiểu 0.1mg, tối đa 0.5mg)",
            "pediatric_cardiac_arrest": "0.02mg/kg IV/IT (tối thiểu 0.1mg)",
            "notes": "Liều tối thiểu người lớn 0.5mg để tránh nhịp tim chậm nghịch lý"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nhịp tim nhanh",
            "Khô miệng",
            "Giãn đồng tử",
            "Táo bón",
            "Bí tiểu",
            "Lú lẫn (người già)",
            "Tăng nhãn áp"
        ],
        "interactions": [
            "Các anticholinergics khác: tăng tác dụng",
            "Digoxin: có thể tăng nồng độ digoxin"
        ],
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Anticholinergic (antimuscarinic). Kháng chọn lọc thụ thể muscarinic acetylcholine (M1-M5), ức chế tác dụng của acetylcholine. Tăng nhịp tim (ức chế vagal tone), giảm tiết (nước bọt, mồ hôi, dịch tiêu hóa, phế quản), giãn đồng tử và giảm co thắt cơ trơn (phế quản, ruột, bàng quang). Được dùng trong emergency để điều trị nhịp tim chậm có triệu chứng, block nhĩ thất, và như một chất giải độc trong quá liều organophosphate.",
        "monitoring": [
            "Nhịp tim (ECG monitoring - mục tiêu tăng nhịp tim)",
            "Dấu hiệu kháng cholinergic quá mức: khô miệng nặng, giãn đồng tử, bí tiểu, lú lẫn",
            "Nhãn áp (nếu có nguy cơ glaucoma)",
            "Triệu chứng nhịp tim chậm nghịch lý (paradoxical bradycardia) - có thể xảy ra với liều <0.5mg ở người lớn",
            "Phản ứng quá mức (nhịp tim nhanh, đánh trống ngực)"
        ],
        "precautions": [
            "QUAN TRỌNG: Liều tối thiểu người lớn 0.5mg để tránh nhịp tim chậm nghịch lý (liều thấp có thể kích thích trung tâm vagal)",
            "CHỐNG CHỈ ĐỊNH tuyệt đối: Glaucoma góc đóng (có thể gây tăng nhãn áp đe dọa thị giác)",
            "CHỐNG CHỈ ĐỊNH: Tắc nghẽn đường tiểu (có thể làm nặng thêm bí tiểu)",
            "CHỐNG CHỈ ĐỊNH: Nhịp tim nhanh (có thể làm tăng nhịp tim hơn nữa)",
            "Thận trọng ở người già (tăng nguy cơ lú lẫn, bí tiểu)",
            "Thận trọng ở bệnh nhân sốt (có thể làm tăng nhiệt độ do giảm tiết mồ hôi)",
            "Thận trọng khi dùng với các anticholinergics khác (tăng tác dụng phụ)",
            "Trong quá liều organophosphate: dùng liều cao hơn nhiều (2-5mg), có thể cần lặp lại nhiều lần cho đến khi đạt tác dụng (đồng tử co lại, giảm tiết)"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ (người lớn), 10-20 giờ (trẻ em)",
            "onset": "Vài phút (IV), 15-30 phút (IM)",
            "duration": "4-6 giờ (tác dụng lâm sàng)",
            "protein_binding": "50%",
            "clearance": "Thận (50-90% thải qua nước tiểu dưới dạng không đổi), gan (metabolite). Thời gian bán hủy dài hơn ở trẻ em"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch tiêm: bảo quản trong tủ mát (2-8°C) nếu có chỉ định, nhưng thường ổn định ở nhiệt độ phòng",
        "black_box_warnings": None
    },
    "Lidocaine": {
        "group": "Emergency - Local Anesthetic / Antiarrhythmic (Class IB)",
        "vietnamese_name": "Lidocaine, Xylocaine",
        "administration": ["IV", "IO", "IT"],
        "indications": [
            "Rung thất / Nhịp nhanh thất không có mạch (khi không có amiodarone)",
            "Rối loạn nhịp thất",
            "Gây tê tại chỗ",
            "Gây tê vùng"
        ],
        "contraindications": [
            "Dị ứng lidocaine",
            "Block nhĩ thất độ 2-3 (không có máy tạo nhịp)",
            "Hội chứng Adams-Stokes",
            "Rối loạn nhịp nặng"
        ],
        "dosage": {
            "adult_cardiac_arrest": "1-1.5mg/kg IV bolus, lặp lại 0.5-0.75mg/kg mỗi 5-10 phút (tối đa 3mg/kg)",
            "adult_vt_with_pulse": "1-1.5mg/kg IV bolus, sau đó 1-4mg/phút IV infusion",
            "pediatric_arrest": "1mg/kg IV/IO bolus",
            "pediatric_infusion": "20-50mcg/kg/phút IV",
            "notes": "Giảm liều ở suy tim, suy gan, người già. Theo dõi co giật, độc thần kinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Độc thần kinh trung ương (co giật, lú lẫn, ngừng thở - với liều cao)",
            "Rối loạn nhịp tim",
            "Hạ huyết áp",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Beta-blockers: giảm chuyển hóa lidocaine",
            "Cimetidine: tăng nồng độ lidocaine",
            "Phenytoin: tăng độc tính"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Thuốc gây tê tại chỗ nhóm amide và thuốc chống loạn nhịp class IB. Ức chế kênh natri voltage-gated trong màng tế bào thần kinh và tế bào cơ tim, ngăn cản khử cực và dẫn truyền xung động thần kinh. Ở tim: ức chế dẫn truyền trong các tế bào có thời gian khử cực dài (tâm thất), giảm tự động tính, giảm nguy cơ rối loạn nhịp thất. Tác dụng nhanh, thời gian bán thải ngắn. Được dùng trong gây tê tại chỗ, giảm đau tại chỗ, và điều trị rối loạn nhịp thất.",
        "monitoring": [
            "ECG liên tục (theo dõi rối loạn nhịp)",
            "Huyết áp và nhịp tim",
            "Dấu hiệu độc tính thần kinh trung ương (chóng mặt, ù tai, co giật, mất ý thức) - dấu hiệu đầu tiên của quá liều",
            "Dấu hiệu độc tính tim mạch (block nhĩ thất, nhịp tim chậm, rung thất) - dấu hiệu muộn, nguy hiểm",
            "Nồng độ lidocaine trong máu (nếu dùng kéo dài hoặc liều cao)",
            "Chức năng gan (lidocaine chuyển hóa mạnh ở gan)",
            "Dấu hiệu phản ứng dị ứng (hiếm)"
        ],
        "precautions": [
            "Độc tính thần kinh trung ương là dấu hiệu CẢNH BÁO SỚM - ngừng ngay nếu có chóng mặt, ù tai, co giật",
            "Độc tính tim mạch có thể xảy ra sau độc tính thần kinh - nguy hiểm tính mạng",
            "PHẢI điều chỉnh liều ở suy gan (giảm chuyển hóa → tích lũy → độc tính)",
            "Thận trọng ở suy tim (giảm phân bố → tăng nồng độ)",
            "Không dùng ở block nhĩ thất độ 2-3 hoặc block nhánh nếu không có máy tạo nhịp",
            "Liều gây tê tại chỗ: tuân thủ liều tối đa (không quá 4.5mg/kg không có epinephrine, 7mg/kg có epinephrine)",
            "Tiêm IV chậm (không quá 25-50mg/phút) để tránh độc tính",
            "Cần có sẵn thuốc chống co giật (benzodiazepine) và thiết bị hồi sức",
            "Giảm liều ở người cao tuổi (giảm chuyển hóa)"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ (bình thường), 3-5 giờ (suy gan)",
            "onset": "Ngay lập tức (IV), 2-5 phút (gây tê tại chỗ)",
            "duration": "10-20 phút (IV), 1-3 giờ (gây tê tại chỗ)",
            "protein_binding": "60-80%",
            "metabolism": "Gan (CYP3A4, CYP1A2) - chuyển hóa mạnh thành active metabolites",
            "clearance": "Chủ yếu qua gan, cần điều chỉnh ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch: tránh đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, độc tính tim mạch có thể gây block nhĩ thất, rung thất, và tử vong, đặc biệt ở suy gan hoặc quá liều. Độc tính thần kinh trung ương (co giật) là dấu hiệu cảnh báo sớm.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (Propranolol, Metoprolol, etc.)",
                    "mechanism": "Beta-blockers ức chế enzyme CYP3A4 và CYP1A2 chuyển hóa lidocaine, làm giảm chuyển hóa và tăng nồng độ lidocaine trong máu.",
                    "effect": "Tăng nồng độ lidocaine, tăng nguy cơ độc tính thần kinh trung ương (co giật, lú lẫn) và độc tính tim mạch (block AV, rung thất)",
                    "management": "GIẢM LIỀU lidocaine xuống 30-50% khi dùng với beta-blockers. Theo dõi chặt chẽ dấu hiệu độc tính. Kiểm tra nồng độ lidocaine trong máu nếu có thể."
                },
                {
                    "drug": "Cimetidine",
                    "mechanism": "Cimetidine ức chế enzyme CYP3A4 và CYP1A2 chuyển hóa lidocaine, làm giảm chuyển hóa và tăng nồng độ lidocaine trong máu.",
                    "effect": "Tăng nồng độ lidocaine, tăng nguy cơ độc tính thần kinh trung ương và độc tính tim mạch",
                    "management": "GIẢM LIỀU lidocaine xuống 30-50% khi dùng với cimetidine. Theo dõi chặt chẽ dấu hiệu độc tính. Có thể dùng ranitidine hoặc famotidine thay thế cimetidine."
                }
            ],
            "moderate": [
                {
                    "drug": "Phenytoin",
                    "mechanism": "Phenytoin có thể tăng độc tính của lidocaine (cơ chế không rõ ràng, có thể liên quan đến tác dụng trên hệ thần kinh trung ương).",
                    "effect": "Tăng nguy cơ độc tính thần kinh trung ương (co giật, lú lẫn)",
                    "management": "Thận trọng, theo dõi chặt chẽ dấu hiệu độc tính. Có thể cần giảm liều lidocaine."
                },
                {
                    "drug": "Amiodarone",
                    "mechanism": "Amiodarone có thể tăng độc tính tim mạch của lidocaine (cả hai đều là thuốc chống loạn nhịp, có thể tăng tác dụng phụ).",
                    "effect": "Tăng nguy cơ độc tính tim mạch (block AV, rung thất)",
                    "management": "Thận trọng, theo dõi ECG chặt chẽ. Có thể cần giảm liều lidocaine."
                }
            ],
            "minor": [
                {
                    "drug": "Quinidine, Procainamide",
                    "mechanism": "Các thuốc chống loạn nhịp khác có thể tăng tác dụng phụ tim mạch.",
                    "effect": "Tăng nguy cơ độc tính tim mạch (nhẹ)",
                    "management": "Theo dõi ECG. Không cần điều chỉnh liều thường quy."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng lidocaine hoặc thuốc gây tê nhóm amide",
                "Block nhĩ thất độ 2-3 không có máy tạo nhịp - có thể làm nặng block, gây nhịp chậm nặng",
                "Hội chứng Adams-Stokes - nguy cơ nhịp chậm nặng, ngừng tim"
            ],
            "relative": [
                "Suy gan nặng - giảm chuyển hóa, tích lũy, tăng nguy cơ độc tính",
                "Suy tim nặng - giảm phân bố, tăng nồng độ, tăng nguy cơ độc tính",
                "Người cao tuổi - giảm chuyển hóa, tăng nhạy cảm với độc tính",
                "Block nhĩ thất độ 1 - có thể làm nặng block",
                "Block nhánh - có thể làm nặng block",
                "Rối loạn nhịp nặng - có thể làm nặng rối loạn nhịp",
                "Dùng với beta-blockers hoặc cimetidine - tăng nồng độ, cần giảm liều",
                "Bệnh nhân có tiền sử co giật - tăng nguy cơ co giật"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Lidocaine là thuốc phân loại B. Có một số nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Lidocaine có thể qua nhau thai, nhưng nồng độ trong máu thai nhi thấp. Được sử dụng trong gây tê sản khoa (epidural, spinal) và được coi là an toàn. Trong cấp cứu (rối loạn nhịp thất), lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Lidocaine bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ khi dùng liều điều trị. Khi dùng liều cao hoặc kéo dài, có thể cần thận trọng.",
                "recommendation": "Có thể dùng khi cho con bú. Lidocaine bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Giảm liều 20-30%. Lidocaine chuyển hóa mạnh ở gan (CYP3A4, CYP1A2), suy gan nhẹ có thể làm giảm chuyển hóa.",
            "moderate": "Giảm liều 30-50%. Theo dõi chặt chẽ dấu hiệu độc tính.",
            "severe": "Giảm liều 50-70% hoặc tránh dùng. Suy gan nặng làm giảm chuyển hóa mạnh, tích lũy, tăng nguy cơ độc tính. Nếu cần dùng: dùng liều thấp, theo dõi chặt chẽ, kiểm tra nồng độ lidocaine trong máu.",
            "notes": "Lidocaine chuyển hóa mạnh ở gan (CYP3A4, CYP1A2). Suy gan làm giảm chuyển hóa, tích lũy, tăng nguy cơ độc tính. PHẢI điều chỉnh liều ở suy gan. Theo dõi chặt chẽ dấu hiệu độc tính (co giật, lú lẫn, block AV)."
        },
        "overdose_management": {
            "symptoms": [
                "Độc tính thần kinh trung ương (dấu hiệu sớm):",
                "  - Chóng mặt, ù tai, nhìn mờ",
                "  - Lú lẫn, kích động",
                "  - Co giật",
                "  - Mất ý thức, ngừng thở",
                "Độc tính tim mạch (dấu hiệu muộn, nguy hiểm):",
                "  - Block nhĩ thất độ 2-3",
                "  - Nhịp tim chậm nặng",
                "  - Rung thất",
                "  - Ngừng tim",
                "Hạ huyết áp",
                "Phản ứng dị ứng (hiếm): phát ban, sốc phản vệ"
            ],
            "antidote": "Không có antidote đặc hiệu cho quá liều lidocaine. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay lidocaine nếu đang truyền",
                "Theo dõi ECG và dấu hiệu sinh tồn liên tục",
                "Nếu độc tính thần kinh trung ương (co giật):",
                "  - Benzodiazepine (diazepam 5-10mg IV, lorazepam 2-4mg IV) - điều trị chính",
                "  - Nếu không đáp ứng: Phenytoin, phenobarbital",
                "  - Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Nếu độc tính tim mạch (block AV, nhịp chậm, rung thất):",
                "  - Nếu block AV độ 2-3 hoặc nhịp chậm nặng:",
                "    - Atropine 0.5-1mg IV (nếu không có block AV)",
                "    - Epinephrine 1mg IV (nếu ngừng tim)",
                "    - Máy tạo nhịp tạm thời nếu cần",
                "  - Nếu rung thất: Defibrillation",
                "  - Nếu ngừng tim: CPR, ACLS protocol",
                "Nếu hạ huyết áp:",
                "  - Truyền dịch (NS, LR)",
                "  - Thuốc vận mạch nếu cần (epinephrine, norepinephrine)",
                "Nếu phản ứng dị ứng:",
                "  - Epinephrine 0.3-0.5mg IM",
                "  - Diphenhydramine 25-50mg IV",
                "  - Corticosteroid (methylprednisolone 125mg IV)",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, ECG, nhịp thở, SpO2 trong ít nhất 2-4 giờ",
                "Kiểm tra nồng độ lidocaine trong máu nếu có thể (nồng độ điều trị: 1.5-5mcg/ml, độc tính: >5-6mcg/ml)"
            ],
            "monitoring": "Theo dõi ECG, huyết áp, nhịp tim, nhịp thở, SpO2 liên tục trong ít nhất 2-4 giờ sau khi dùng. Theo dõi lâu hơn nếu có biến chứng (độc tính thần kinh, độc tính tim mạch). Kiểm tra nồng độ lidocaine trong máu nếu có thể."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu cho lidocaine. Điều trị hỗ trợ và điều trị triệu chứng (benzodiazepine cho co giật, atropine/epinephrine cho block AV/nhịp chậm)."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ (1% = 10mg/ml, 2% = 20mg/ml). Không cần pha loãng cho bolus. Cho infusion: pha 1g (50ml 2%) trong 450ml D5W = 2mg/ml.",
                "infusion_rate": "Cardiac arrest: 1-1.5mg/kg IV bolus, lặp lại 0.5-0.75mg/kg mỗi 5-10 phút (tối đa 3mg/kg). VT with pulse: 1-1.5mg/kg IV bolus, sau đó 1-4mg/phút IV infusion. Trẻ em: 1mg/kg IV/IO bolus, sau đó 20-50mcg/kg/phút IV infusion.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "LR (Lactated Ringer's)"],
                "incompatibility": ["Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."],
                "notes": "QUAN TRỌNG: 1) PHẢI điều chỉnh liều ở suy gan (giảm 30-70%), 2) PHẢI điều chỉnh liều ở suy tim (giảm 20-30%), 3) PHẢI điều chỉnh liều khi dùng với beta-blockers hoặc cimetidine (giảm 30-50%), 4) Độc tính thần kinh trung ương là dấu hiệu CẢNH BÁO SỚM - ngừng ngay nếu có, 5) Tiêm IV chậm (không quá 25-50mg/phút) để tránh độc tính, 6) Theo dõi ECG chặt chẽ, 7) Giảm liều ở người cao tuổi."
            },
            "local_anesthesia": {
                "reconstitution": "Dùng trực tiếp từ lọ (1% = 10mg/ml, 2% = 20mg/ml). Có thể pha với epinephrine để kéo dài tác dụng và giảm hấp thu.",
                "max_dose": "Không có epinephrine: 4.5mg/kg (tối đa 300mg). Có epinephrine: 7mg/kg (tối đa 500mg).",
                "notes": "Tuân thủ liều tối đa để tránh độc tính. Không tiêm vào mạch máu. Theo dõi dấu hiệu độc tính (chóng mặt, ù tai, co giật)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lidocaine",
                "ACLS Guidelines 2020 - American Heart Association",
                "UpToDate - Lidocaine: Drug Information",
                "Medscape - Lidocaine Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Lidocaine Monograph",
                "Micromedex - Lidocaine Drug Information"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Adenosine": {
        "group": "Emergency - Antiarrhythmic",
        "vietnamese_name": "Adenosine",
        "administration": ["IV", "IO"],
        "indications": [
            "Nhịp nhanh trên thất (SVT) - cấp cứu",
            "Chẩn đoán rối loạn nhịp",
            "Cuồng nhĩ"
        ],
        "contraindications": [
            "Block nhĩ thất độ 2-3 (không có máy tạo nhịp)",
            "Hội chứng sick sinus",
            "Hen phế quản nặng",
            "Dị ứng adenosine"
        ],
        "dosage": {
            "adult_svt_first": "6mg IV bolus nhanh (1-2 giây) + flush nhanh 20ml NS",
            "adult_svt_second": "12mg IV nếu không đáp ứng (có thể lặp lại 1 lần)",
            "adult_max": "12mg (tối đa)",
            "pediatric_svt_first": "0.1mg/kg IV (tối đa 6mg)",
            "pediatric_svt_second": "0.2mg/kg IV nếu không đáp ứng (tối đa 12mg)",
            "notes": "Phải tiêm bolus nhanh (1-2 giây) và flush ngay 20ml. Có thể gây ngừng tim tạm thời"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Ngừng tim tạm thời (thường <10 giây - bình thường)",
            "Cảm giác khó chịu ở ngực",
            "Khó thở",
            "Đỏ mặt",
            "Chóng mặt",
            "Loạn nhịp (thoáng qua)"
        ],
        "interactions": [
            "Theophylline/Caffeine: đối kháng tác dụng",
            "Dipyridamole: tăng tác dụng",
            "Carbamazepine: tăng tác dụng"
        ],
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Adenosine là một nucleoside nội sinh kích hoạt các thụ thể A1 adenosine ở nút nhĩ-thất (AV node), làm tăng thời gian dẫn truyền và kéo dài thời gian refrac của nút AV. Tác dụng này chặn tạm thời dẫn truyền qua nút AV, phá vỡ vòng re-entry trong SVT và chuyển nhịp về xoang. Có thời gian bán thải cực ngắn (<10 giây) do bị bắt giữ nhanh bởi tế bào hồng cầu và nội mô, nên tác dụng thoáng qua và an toàn",
        "monitoring": [
            "ECG liên tục trong và sau khi tiêm (ngừng tim tạm thời có thể xảy ra)",
            "Nhịp tim, huyết áp trong và sau khi tiêm (1-2 phút)",
            "Dấu hiệu sốc phản vệ (hiếm nhưng nguy hiểm)",
            "Dấu hiệu co thắt phế quản (đặc biệt ở bệnh nhân hen)",
            "Đáp ứng điều trị (chuyển về nhịp xoang)"
        ],
        "precautions": [
            "PHẢI tiêm bolus nhanh (1-2 giây) và flush ngay 20ml NS để đảm bảo thuốc vào tim trước khi bị bắt giữ",
            "Nếu tiêm chậm → thuốc bị bắt giữ bởi tế bào máu → không hiệu quả",
            "Chuẩn bị sẵn thiết bị hồi sức tim phổi (CPR, defibrillator) vì có thể gây ngừng tim tạm thời",
            "Tránh dùng ở bệnh nhân hen phế quản nặng (có thể gây co thắt phế quản)",
            "Tránh dùng ở block AV độ 2-3 hoặc sick sinus syndrome (trừ khi có máy tạo nhịp)",
            "Có thể gây ngừng tim tạm thời <10 giây (bình thường, không cần điều trị)",
            "Nếu không đáp ứng với 6mg, có thể tăng lên 12mg (tối đa)",
            "Tránh dùng với theophylline hoặc caffeine (đối kháng tác dụng)"
        ],
        "pharmacokinetics": {
            "half_life": "<10 giây (cực ngắn)",
            "onset": "Ngay lập tức (vài giây)",
            "duration": "10-30 giây (tạm thời)",
            "protein_binding": "Không đáng kể",
            "clearance": "Bắt giữ nhanh bởi tế bào hồng cầu và nội mô, chuyển hóa thành inosine và adenosine monophosphate"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Bảo vệ khỏi ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Theophylline, Caffeine",
                    "mechanism": "Theophylline và caffeine là chất đối kháng adenosine receptor, ức chế tác dụng của adenosine.",
                    "effect": "Giảm hoặc mất hiệu quả điều trị SVT, có thể cần liều cao hơn hoặc không đáp ứng",
                    "management": "Tránh dùng adenosine nếu bệnh nhân đang dùng theophylline hoặc uống caffeine gần đây. Nếu cần, có thể cần liều cao hơn (12mg) hoặc dùng phương pháp khác (adenosine không hiệu quả)."
                },
                {
                    "drug": "Dipyridamole",
                    "mechanism": "Dipyridamole ức chế bắt giữ adenosine bởi tế bào, tăng nồng độ và thời gian tác dụng của adenosine.",
                    "effect": "Tăng tác dụng và thời gian tác dụng của adenosine, tăng nguy cơ tác dụng phụ (ngừng tim kéo dài, block AV)",
                    "management": "GIẢM LIỀU adenosine xuống 50-75% (1.5-3mg thay vì 6mg). Theo dõi chặt chẽ ECG. Chuẩn bị sẵn thiết bị hồi sức."
                }
            ],
            "moderate": [
                {
                    "drug": "Carbamazepine",
                    "mechanism": "Carbamazepine có thể tăng tác dụng của adenosine (cơ chế không rõ ràng, có thể liên quan đến bắt giữ adenosine).",
                    "effect": "Tăng tác dụng và thời gian tác dụng của adenosine, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng, có thể cần giảm liều adenosine. Theo dõi chặt chẽ ECG."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Digoxin có thể tăng độ nhạy cảm của nút AV với adenosine.",
                    "effect": "Tăng nguy cơ block AV, ngừng tim kéo dài",
                    "management": "Thận trọng, theo dõi ECG chặt chẽ. Có thể cần giảm liều adenosine."
                }
            ],
            "minor": [
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Beta-blockers có thể tăng độ nhạy cảm của nút AV với adenosine.",
                    "effect": "Tăng nguy cơ block AV (nhẹ)",
                    "management": "Theo dõi ECG. Không cần điều chỉnh liều thường quy."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Block nhĩ thất độ 2-3 (AV block) không có máy tạo nhịp",
                "Hội chứng sick sinus (sick sinus syndrome) không có máy tạo nhịp",
                "Hen phế quản nặng hoặc co thắt phế quản nặng",
                "Dị ứng adenosine",
                "Rung nhĩ/rung thất (không phải chỉ định)"
            ],
            "relative": [
                "Block AV độ 1 - thận trọng, có thể làm nặng",
                "Hen phế quản nhẹ đến trung bình - thận trọng, có thể gây co thắt phế quản",
                "Suy tim - thận trọng, có thể gây ngừng tim kéo dài",
                "Suy thận nặng - không cần điều chỉnh liều nhưng thận trọng",
                "Dùng với dipyridamole - giảm liều 50-75%",
                "Dùng với theophylline/caffeine - có thể không hiệu quả",
                "Nhịp tim chậm (<50 bpm) - thận trọng, có thể gây ngừng tim"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Adenosine là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Adenosine có thời gian bán thải cực ngắn (<10 giây) và tác dụng thoáng qua, nên ít có khả năng ảnh hưởng đến thai nhi. Được sử dụng trong cấp cứu để điều trị SVT ở phụ nữ có thai và có vẻ an toàn. SVT có thể gây nguy hiểm cho cả mẹ và thai nhi (giảm tưới máu, thiếu oxy). Adenosine có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong cấp cứu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Adenosine có thời gian bán thải cực ngắn (<10 giây), nên không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Tác dụng thoáng qua và bị bắt giữ nhanh bởi tế bào. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Adenosine có tác dụng cực ngắn và không bài tiết vào sữa mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Adenosine không chuyển hóa qua gan, bị bắt giữ bởi tế bào máu.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Không cần điều chỉnh liều. Adenosine không chuyển hóa qua gan.",
            "notes": "Adenosine không chuyển hóa qua gan, bị bắt giữ nhanh bởi tế bào hồng cầu và nội mô, chuyển hóa thành inosine. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Ngừng tim tạm thời kéo dài (>10-30 giây) - có thể tiến triển thành ngừng tim thực sự",
                "Block AV độ 2-3 kéo dài - có thể gây nhịp chậm nặng, suy tim",
                "Rung nhĩ/rung thất - hiếm nhưng nguy hiểm",
                "Co thắt phế quản nặng - khó thở, suy hô hấp",
                "Sốc phản vệ - phát ban, phù mạch, sốc (hiếm)",
                "Tụt huyết áp nặng",
                "Nhịp chậm nặng (<30-40 bpm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Theophylline hoặc aminophylline có thể đối kháng tác dụng adenosine (nếu có block AV kéo dài).",
            "treatment": [
                "Ngừng ngay adenosine nếu đang truyền (nếu có)",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi ECG liên tục: Nhịp tim, block AV, loạn nhịp",
                "Nếu ngừng tim tạm thời <10 giây: Quan sát, thường tự hồi phục",
                "Nếu ngừng tim kéo dài >10-30 giây hoặc block AV độ 2-3:",
                "  - Hỗ trợ hô hấp, thở oxy",
                "  - Nếu nhịp chậm nặng: Atropine 0.5-1mg IV (nếu không có block AV)",
                "  - Nếu block AV kéo dài: Theophylline 100-200mg IV hoặc aminophylline (đối kháng adenosine)",
                "  - Nếu ngừng tim thực sự: CPR, defibrillation nếu cần",
                "Nếu co thắt phế quản: Salbutamol dạng hít hoặc IV, corticosteroid nếu cần",
                "Nếu sốc phản vệ: Epinephrine, diphenhydramine, corticosteroid",
                "Hỗ trợ huyết động: Truyền dịch, thuốc vận mạch nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2 trong ít nhất 30-60 phút"
            ],
            "monitoring": "Theo dõi ECG liên tục, dấu hiệu sinh tồn trong ít nhất 30-60 phút sau khi dùng. Theo dõi lâu hơn nếu có biến chứng (block AV, ngừng tim, co thắt phế quản)."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Theophylline / Aminophylline",
                    "mechanism": "Đối kháng adenosine receptors, đảo ngược tác dụng block AV của adenosine",
                    "indication": "Block AV kéo dài sau khi dùng adenosine",
                    "dose": "Theophylline 100-200mg IV hoặc Aminophylline 5-6mg/kg IV"
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ, không cần pha. Có thể pha trong NS nếu cần nhưng thường dùng trực tiếp.",
                "infusion_rate": "BOLUS NHANH: Tiêm trực tiếp vào tĩnh mạch lớn (tĩnh mạch ngoại biên lớn hoặc tĩnh mạch trung tâm) trong 1-2 giây. SAU ĐÓ NGAY LẬP TỨC flush 20ml NS nhanh để đẩy thuốc vào tim trước khi bị bắt giữ bởi tế bào máu. KHÔNG được tiêm chậm hoặc truyền - sẽ không hiệu quả.",
                "compatibility": ["NS (0.9% NaCl) - để flush"],
                "incompatibility": ["Không trộn với các thuốc khác. Tiêm bolus riêng biệt."],
                "notes": "QUAN TRỌNG: 1) Tiêm bolus NHANH (1-2 giây) vào tĩnh mạch lớn, 2) Flush NGAY 20ml NS nhanh, 3) Theo dõi ECG liên tục, 4) Chuẩn bị sẵn thiết bị hồi sức. Nếu tiêm chậm → thuốc bị bắt giữ → không hiệu quả. Liều đầu: 6mg, nếu không đáp ứng: 12mg (tối đa)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Adenosine",
                "ACLS Guidelines 2020 - American Heart Association",
                "UpToDate - Adenosine: Drug Information",
                "Medscape - Adenosine Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Adenosine Monograph",
                "Micromedex - Adenosine Drug Information"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Naloxone": {
        "group": "Emergency - Opioid Antagonist",
        "vietnamese_name": "Naloxone, Narcan",
        "administration": ["IV", "IM", "SC", "INH", "IO"],
        "indications": [
            "Quá liều opioid (nghiện)",
            "Ngộ độc opioid",
            "Đảo ngược tác dụng opioid sau phẫu thuật",
            "Đảo ngược tác dụng opioid trong ICU"
        ],
        "contraindications": [
            "Dị ứng naloxone"
        ],
        "dosage": {
            "adult_overdose": "0.4-2mg IV/IM/SC, lặp lại mỗi 2-3 phút đến khi đáp ứng",
            "adult_reversal": "0.04-0.4mg IV titrate đến khi đáp ứng",
            "adult_infusion": "0.25-6.25mcg/kg/giờ IV (nếu cần duy trì)",
            "pediatric_overdose": "0.01mg/kg IV/IM/IO, lặp lại đến khi đáp ứng",
            "pediatric_infusion": "2.5-10mcg/kg/giờ IV",
            "notes": "Tác dụng ngắn (20-90 phút), có thể cần lặp lại hoặc infusion. Theo dõi hội chứng cai"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Hội chứng cai opioid (nếu bệnh nhân nghiện)",
            "Hạ huyết áp",
            "Rối loạn nhịp tim",
            "Co giật (hiếm)",
            "Phù phổi (hiếm)"
        ],
        "interactions": [
            "Opioids: đảo ngược tác dụng"
        ],
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Opioid receptor antagonist cạnh tranh. Gắn với ái lực cao vào mu-opioid receptor (và kappa, delta receptors), đẩy opioid ra khỏi receptor, đảo ngược hoàn toàn tác dụng của opioid (ức chế hô hấp, an thần, giảm đau, miosis). Tác dụng rất nhanh (1-2 phút IV), nhưng thời gian tác dụng ngắn (30-90 phút) do bị chuyển hóa nhanh, trong khi nhiều opioid có thời gian tác dụng dài hơn → cần lặp lại liều hoặc dùng infusion.",
        "monitoring": [
            "Độ bão hòa oxy (SpO2) và nhịp thở liên tục",
            "Mức độ ý thức (GCS)",
            "Dấu hiệu hội chứng cai opioid (kích động, vã mồ hôi, tăng huyết áp, nhịp tim nhanh)",
            "Huyết áp và nhịp tim",
            "Dấu hiệu tái ngộ độc opioid (thở chậm lại, giảm ý thức) - đặc biệt quan trọng nếu opioid có thời gian tác dụng dài hơn naloxone",
            "Co giật (hiếm nhưng nguy hiểm)"
        ],
        "precautions": [
            "Thời gian tác dụng NGẮN (30-90 phút) - opioid có thể tác dụng trở lại sau khi naloxone hết tác dụng",
            "Theo dõi sát ít nhất 2-4 giờ sau khi dùng naloxone (nguy cơ tái ngộ độc)",
            "Ở bệnh nhân nghiện opioid: naloxone có thể gây hội chứng cai nặng (kích động, nôn, tăng huyết áp) - cần chuẩn bị xử trí",
            "Không dùng quá liều (tăng nguy cơ hội chứng cai nặng, không tăng hiệu quả)",
            "Nếu cần duy trì: dùng infusion thay vì bolus lặp lại",
            "Thận trọng ở bệnh nhân có tiền sử co giật (có thể gây co giật)",
            "Dùng liều thấp (0.04-0.4mg) khi đảo ngược tác dụng opioid sau phẫu thuật để tránh đảo ngược hoàn toàn giảm đau"
        ],
        "pharmacokinetics": {
            "half_life": "30-90 phút (ngắn)",
            "onset": "1-2 phút (IV), 2-5 phút (IM)",
            "duration": "30-90 phút (tùy liều)",
            "protein_binding": "45%",
            "clearance": "Gan (glucuronidation), thời gian bán thải ngắn hơn nhiều so với hầu hết opioid"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Có thể bảo quản ở nhiệt độ 2-8°C.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, thời gian tác dụng ngắn có thể dẫn đến tái ngộ độc opioid nếu không theo dõi đúng. Hội chứng cai opioid có thể nguy hiểm ở bệnh nhân nghiện.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Opioids (Morphine, Fentanyl, Heroin, Methadone, etc.)",
                    "mechanism": "Naloxone là opioid receptor antagonist cạnh tranh, đẩy opioid ra khỏi receptor, đảo ngược hoàn toàn tác dụng của opioid.",
                    "effect": "Đảo ngược tác dụng opioid (ức chế hô hấp, an thần, giảm đau, miosis). Nếu opioid có thời gian tác dụng dài hơn naloxone → tái ngộ độc sau khi naloxone hết tác dụng.",
                    "management": "Đây là tác dụng điều trị mong muốn. Tuy nhiên, cần theo dõi sát ít nhất 2-4 giờ sau khi dùng naloxone vì nguy cơ tái ngộ độc. Nếu opioid có thời gian tác dụng dài (methadone, buprenorphine), có thể cần infusion naloxone."
                }
            ],
            "moderate": [
                {
                    "drug": "Buprenorphine",
                    "mechanism": "Buprenorphine có ái lực rất cao với opioid receptor, khó bị đẩy ra bởi naloxone. Có thể cần liều cao hơn hoặc không đáp ứng.",
                    "effect": "Có thể không đảo ngược hoàn toàn tác dụng của buprenorphine, hoặc cần liều naloxone cao hơn",
                    "management": "Có thể cần liều naloxone cao hơn (2-4mg) hoặc infusion. Theo dõi sát, có thể cần hỗ trợ hô hấp nếu không đáp ứng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng naloxone (hiếm)"
            ],
            "relative": [
                "Bệnh nhân nghiện opioid - có thể gây hội chứng cai nặng (kích động, nôn, tăng huyết áp, nhịp tim nhanh)",
                "Bệnh nhân dùng opioid để giảm đau mãn tính - có thể đảo ngược hoàn toàn giảm đau, gây đau nặng",
                "Bệnh nhân có tiền sử co giật - có thể gây co giật",
                "Bệnh nhân có bệnh tim mạch - hội chứng cai có thể gây tăng huyết áp, nhịp tim nhanh, nguy cơ biến cố tim mạch"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Naloxone là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Naloxone có thể qua nhau thai. Tuy nhiên, trong quá liều opioid, lợi ích cứu sống mẹ (và thai nhi) vượt quá nguy cơ. Quá liều opioid có thể gây tử vong cho cả mẹ và thai nhi (ức chế hô hấp, thiếu oxy). Naloxone được sử dụng trong cấp cứu ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Naloxone có thời gian bán thải ngắn (30-90 phút) và bị chuyển hóa nhanh. Không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Naloxone có thời gian bán thải ngắn và không bài tiết vào sữa mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Naloxone chuyển hóa qua gan nhưng không tích lũy ở suy gan nhẹ.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Không cần điều chỉnh liều. Naloxone chuyển hóa qua gan nhưng không tích lũy ở suy gan nặng.",
            "notes": "Naloxone chuyển hóa qua gan (glucuronidation), nhưng không tích lũy ở suy gan. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hội chứng cai opioid nặng (kích động, nôn, tăng huyết áp, nhịp tim nhanh, run, đau cơ)",
                "Co giật (hiếm)",
                "Phù phổi cấp (hiếm)",
                "Rối loạn nhịp tim (hiếm)",
                "Tăng huyết áp nặng",
                "Tái ngộ độc opioid (sau khi naloxone hết tác dụng)"
            ],
            "antidote": "Không có antidote đặc hiệu cho quá liều naloxone. Có thể dùng opioid (morphine, fentanyl) để đối kháng tác dụng nếu hội chứng cai quá nặng, nhưng THẬN TRỌNG (có thể gây ức chế hô hấp trở lại).",
            "treatment": [
                "Ngừng ngay naloxone nếu đang truyền",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Nếu hội chứng cai nặng:",
                "  - Hỗ trợ tâm lý, an ủi bệnh nhân",
                "  - Nếu tăng huyết áp nặng: Thuốc hạ huyết áp (labetalol, clonidine)",
                "  - Nếu nôn: Thuốc chống nôn (ondansetron, metoclopramide)",
                "  - Nếu đau: Thuốc giảm đau không opioid (paracetamol, ibuprofen)",
                "  - THẬN TRỌNG: Không dùng opioid để điều trị hội chứng cai (có thể gây ức chế hô hấp trở lại)",
                "Nếu co giật:",
                "  - Benzodiazepine (diazepam, lorazepam) IV",
                "  - Theo dõi hô hấp (benzodiazepine có thể ức chế hô hấp)",
                "Nếu phù phổi cấp:",
                "  - Hỗ trợ hô hấp: Thở oxy, CPAP/BiPAP nếu cần",
                "  - Furosemide nếu có suy tim",
                "  - Nitroglycerin nếu có tăng huyết áp",
                "Nếu tái ngộ độc opioid:",
                "  - Dùng lại naloxone (0.4-2mg IV/IM)",
                "  - Hoặc dùng infusion naloxone (0.25-6.25mcg/kg/giờ IV)",
                "  - Theo dõi sát nhịp thở và SpO2",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2 trong ít nhất 2-4 giờ"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn (huyết áp, nhịp tim, nhịp thở, SpO2) liên tục trong ít nhất 2-4 giờ sau khi dùng naloxone. Theo dõi lâu hơn nếu có biến chứng (hội chứng cai nặng, co giật, phù phổi, tái ngộ độc opioid)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent cho naloxone. Nếu hội chứng cai quá nặng, có thể dùng opioid (morphine, fentanyl) để đối kháng, nhưng THẬN TRỌNG vì có thể gây ức chế hô hấp trở lại."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ (0.4mg/ml hoặc 1mg/ml). Không cần pha loãng cho bolus. Cho infusion: pha 2mg trong 500ml D5W hoặc NS = 4mcg/ml.",
                "infusion_rate": "Overdose: 0.4-2mg IV bolus, lặp lại mỗi 2-3 phút đến khi đáp ứng. Reversal: 0.04-0.4mg IV titrate đến khi đáp ứng. Infusion: 0.25-6.25mcg/kg/giờ IV (pha 2mg trong 500ml = 4mcg/ml).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."],
                "notes": "QUAN TRỌNG: 1) Tác dụng ngắn (30-90 phút) - opioid có thể tác dụng trở lại, 2) Theo dõi sát ít nhất 2-4 giờ sau khi dùng, 3) Nếu opioid có thời gian tác dụng dài (methadone, buprenorphine), có thể cần infusion, 4) Ở bệnh nhân nghiện: có thể gây hội chứng cai nặng, 5) Dùng liều thấp (0.04-0.4mg) khi đảo ngược tác dụng opioid sau phẫu thuật."
            },
            "im": {
                "reconstitution": "Dùng trực tiếp từ lọ (0.4mg/ml hoặc 1mg/ml).",
                "injection_site": "Cánh tay hoặc đùi ngoài.",
                "notes": "Overdose: 0.4-2mg IM, lặp lại mỗi 2-3 phút đến khi đáp ứng. Trẻ em: 0.01mg/kg IM, lặp lại đến khi đáp ứng. Tác dụng chậm hơn IV (2-5 phút so với 1-2 phút)."
            },
            "inhaled": {
                "reconstitution": "Dùng dạng xịt mũi (Narcan Nasal Spray) - 4mg/0.1ml.",
                "dose": "4mg (1 lần xịt) vào một bên mũi. Lặp lại sau 2-3 phút nếu không đáp ứng (có thể đổi bên mũi).",
                "notes": "Dùng trong quá liều opioid ngoài bệnh viện. Tác dụng tương tự IM. Theo dõi sát sau khi dùng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Naloxone",
                "ACLS Guidelines 2020 - American Heart Association",
                "Opioid Overdose Guidelines - CDC",
                "UpToDate - Naloxone: Drug Information",
                "Medscape - Naloxone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Naloxone Monograph",
                "Micromedex - Naloxone Drug Information"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, opioid overdose guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Flumazenil": {
        "group": "Emergency - Benzodiazepine Antagonist",
        "vietnamese_name": "Flumazenil, Anexate",
        "administration": ["IV"],
        "indications": [
            "Quá liều benzodiazepine",
            "Đảo ngược tác dụng benzodiazepine sau phẫu thuật",
            "Quá liều zolpidem/zopiclone"
        ],
        "contraindications": [
            "Dị ứng flumazenil",
            "Động kinh (đang điều trị với benzodiazepine)",
            "Quá liều tricyclic antidepressants",
            "Phụ thuộc benzodiazepine lâu dài"
        ],
        "dosage": {
            "adult_overdose": "0.2mg IV, lặp lại 0.2mg mỗi 1 phút đến khi đáp ứng (tối đa 1mg)",
            "adult_reversal": "0.1-0.2mg IV titrate đến khi đáp ứng",
            "pediatric": "0.01mg/kg IV (tối đa 0.2mg), lặp lại đến khi đáp ứng",
            "notes": "Tác dụng ngắn (30-60 phút), có thể cần lặp lại. Nguy cơ co giật ở bệnh nhân động kinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Co giật (nguy hiểm ở bệnh nhân động kinh)",
            "Hội chứng cai benzodiazepine",
            "Buồn nôn, nôn",
            "Chóng mặt",
            "Lo lắng",
            "Rối loạn nhịp tim"
        ],
        "interactions": [
            "Benzodiazepines: đảo ngược tác dụng",
            "Tricyclic antidepressants: tăng nguy cơ co giật"
        ],
        "pregnancy": "C - Thận trọng",
        "mechanism_of_action": "Benzodiazepine receptor antagonist cạnh tranh. Gắn với ái lực cao vào benzodiazepine receptor (một phần của GABA-A receptor complex), đẩy benzodiazepine ra khỏi receptor, đảo ngược tác dụng của benzodiazepine (an thần, ức chế hô hấp, giảm trương lực cơ, mất trí nhớ). Tác dụng rất nhanh (1-2 phút IV), nhưng thời gian tác dụng ngắn (45-90 phút) do bị chuyển hóa nhanh, trong khi nhiều benzodiazepine có thời gian tác dụng dài hơn → cần theo dõi sát, có thể cần lặp lại liều.",
        "monitoring": [
            "Mức độ ý thức (GCS) liên tục",
            "Nhịp thở và độ bão hòa oxy (SpO2)",
            "Dấu hiệu tái an thần/tái ức chế hô hấp (quan trọng - flumazenil hết tác dụng trước benzodiazepine)",
            "Dấu hiệu hội chứng cai benzodiazepine (kích động, run, co giật) - đặc biệt ở bệnh nhân nghiện",
            "Huyết áp và nhịp tim",
            "Co giật (nguy cơ ở bệnh nhân có tiền sử co giật, dùng benzodiazepine để chống co giật)",
            "Rối loạn nhịp tim (hiếm)"
        ],
        "precautions": [
            "Thời gian tác dụng NGẮN (45-90 phút) - benzodiazepine có thể tác dụng trở lại sau khi flumazenil hết",
            "Theo dõi sát ít nhất 2-4 giờ sau khi dùng (nguy cơ tái an thần, tái ức chế hô hấp)",
            "Ở bệnh nhân nghiện benzodiazepine: có thể gây hội chứng cai nặng (kích động, run, co giật) - cần chuẩn bị xử trí",
            "KHÔNG dùng ở bệnh nhân dùng benzodiazepine để chống co giật (có thể gây co giật nặng)",
            "KHÔNG dùng ở ngộ độc tricyclic antidepressant (có thể gây co giật, rối loạn nhịp)",
            "Khởi đầu với liều thấp (0.2mg), tăng dần nếu cần",
            "Không dùng quá liều (không tăng hiệu quả, tăng nguy cơ tác dụng phụ)",
            "Nếu cần duy trì: có thể dùng infusion, nhưng thường không khuyến cáo",
            "Thận trọng ở bệnh nhân có tiền sử co giật"
        ],
        "pharmacokinetics": {
            "half_life": "41-79 phút (ngắn)",
            "onset": "1-2 phút (IV)",
            "duration": "45-90 phút (tùy liều)",
            "protein_binding": "50%",
            "metabolism": "Gan (glucuronidation)",
            "clearance": "Gan, thời gian bán thải ngắn hơn nhiều so với hầu hết benzodiazepine"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, thời gian tác dụng ngắn có thể dẫn đến tái an thần và tái ức chế hô hấp nếu không theo dõi đúng. Hội chứng cai benzodiazepine có thể nguy hiểm ở bệnh nhân nghiện. Nguy cơ co giật ở bệnh nhân có tiền sử co giật hoặc ngộ độc tricyclic antidepressant.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepines (Diazepam, Midazolam, Lorazepam, etc.)",
                    "mechanism": "Flumazenil là benzodiazepine receptor antagonist cạnh tranh, đẩy benzodiazepine ra khỏi receptor, đảo ngược hoàn toàn tác dụng của benzodiazepine.",
                    "effect": "Đảo ngược tác dụng benzodiazepine (an thần, ức chế hô hấp, giảm trương lực cơ, mất trí nhớ). Nếu benzodiazepine có thời gian tác dụng dài hơn flumazenil → tái an thần sau khi flumazenil hết tác dụng.",
                    "management": "Đây là tác dụng điều trị mong muốn. Tuy nhiên, cần theo dõi sát ít nhất 2-4 giờ sau khi dùng flumazenil vì nguy cơ tái an thần. Nếu benzodiazepine có thời gian tác dụng dài (diazepam, clonazepam), có thể cần lặp lại liều flumazenil."
                },
                {
                    "drug": "Tricyclic Antidepressants (TCAs)",
                    "mechanism": "Flumazenil có thể làm giảm ngưỡng co giật, và TCAs cũng làm giảm ngưỡng co giật. Kết hợp: tăng nguy cơ co giật nặng.",
                    "effect": "Tăng nguy cơ co giật nặng, rối loạn nhịp tim, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH dùng flumazenil ở ngộ độc tricyclic antidepressant. Nếu không chắc chắn, không dùng flumazenil."
                }
            ],
            "moderate": [
                {
                    "drug": "Zolpidem, Zopiclone (Non-benzodiazepine hypnotics)",
                    "mechanism": "Zolpidem và zopiclone tác dụng trên benzodiazepine receptor, có thể bị đảo ngược bởi flumazenil.",
                    "effect": "Có thể đảo ngược tác dụng của zolpidem/zopiclone, nhưng có thể không hoàn toàn",
                    "management": "Có thể dùng flumazenil để đảo ngược quá liều zolpidem/zopiclone. Theo dõi sát."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dị ứng flumazenil (hiếm)",
                "Động kinh đang điều trị với benzodiazepine - có thể gây co giật nặng",
                "Quá liều tricyclic antidepressant - tăng nguy cơ co giật, rối loạn nhịp tim",
                "Phụ thuộc benzodiazepine lâu dài - có thể gây hội chứng cai nặng, co giật"
            ],
            "relative": [
                "Bệnh nhân nghiện benzodiazepine - có thể gây hội chứng cai nặng (kích động, run, co giật)",
                "Bệnh nhân có tiền sử co giật - tăng nguy cơ co giật",
                "Bệnh nhân dùng benzodiazepine để chống co giật - có thể gây co giật nặng",
                "Bệnh nhân có bệnh tim mạch - hội chứng cai có thể gây tăng huyết áp, nhịp tim nhanh",
                "Ngộ độc hỗn hợp (nhiều thuốc) - không chắc chắn thành phần → không dùng flumazenil"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Flumazenil là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Flumazenil có thể qua nhau thai. Tuy nhiên, trong quá liều benzodiazepine, lợi ích cứu sống mẹ (và thai nhi) vượt quá nguy cơ. Quá liều benzodiazepine có thể gây tử vong cho cả mẹ và thai nhi (ức chế hô hấp, thiếu oxy). Flumazenil được sử dụng trong cấp cứu ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Flumazenil có thời gian bán thải ngắn (41-79 phút) và bị chuyển hóa nhanh. Không có khả năng bài tiết vào sữa mẹ ở nồng độ đáng kể. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Flumazenil có thời gian bán thải ngắn và không bài tiết vào sữa mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Flumazenil chuyển hóa qua gan nhưng không tích lũy ở suy gan nhẹ.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Không cần điều chỉnh liều. Flumazenil chuyển hóa qua gan nhưng không tích lũy ở suy gan nặng.",
            "notes": "Flumazenil chuyển hóa qua gan (glucuronidation), nhưng không tích lũy ở suy gan. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hội chứng cai benzodiazepine nặng (kích động, run, co giật, lo lắng)",
                "Co giật nặng (đặc biệt nguy hiểm ở bệnh nhân có tiền sử co giật hoặc ngộ độc TCA)",
                "Rối loạn nhịp tim (hiếm, thường liên quan đến ngộ độc TCA)",
                "Tăng huyết áp",
                "Tái an thần/tái ức chế hô hấp (sau khi flumazenil hết tác dụng)"
            ],
            "antidote": "Không có antidote đặc hiệu cho quá liều flumazenil. Có thể dùng benzodiazepine (diazepam, midazolam) để đối kháng tác dụng nếu hội chứng cai quá nặng hoặc co giật, nhưng THẬN TRỌNG (có thể gây ức chế hô hấp trở lại).",
            "treatment": [
                "Ngừng ngay flumazenil nếu đang truyền",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, mức độ ý thức",
                "Nếu co giật:",
                "  - Benzodiazepine (diazepam 5-10mg IV, lorazepam 2-4mg IV) - đây là điều trị chính",
                "  - Nếu không đáp ứng: Phenytoin, phenobarbital",
                "  - Theo dõi hô hấp (benzodiazepine có thể ức chế hô hấp)",
                "Nếu hội chứng cai nặng:",
                "  - Hỗ trợ tâm lý, an ủi bệnh nhân",
                "  - Nếu tăng huyết áp nặng: Thuốc hạ huyết áp (labetalol, clonidine)",
                "  - Nếu lo lắng nặng: Benzodiazepine (diazepam, lorazepam) - THẬN TRỌNG",
                "Nếu rối loạn nhịp tim:",
                "  - Điều trị theo protocol rối loạn nhịp",
                "  - Nếu liên quan đến ngộ độc TCA: Điều trị theo protocol ngộ độc TCA",
                "Nếu tái an thần/tái ức chế hô hấp:",
                "  - Dùng lại flumazenil (0.2mg IV, lặp lại đến khi đáp ứng)",
                "  - Hoặc dùng benzodiazepine nếu cần an thần (THẬN TRỌNG)",
                "  - Theo dõi sát nhịp thở và SpO2",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, mức độ ý thức trong ít nhất 2-4 giờ"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn (huyết áp, nhịp tim, nhịp thở, SpO2, mức độ ý thức) liên tục trong ít nhất 2-4 giờ sau khi dùng flumazenil. Theo dõi lâu hơn nếu có biến chứng (hội chứng cai nặng, co giật, tái an thần)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent cho flumazenil. Nếu hội chứng cai quá nặng hoặc co giật, có thể dùng benzodiazepine (diazepam, midazolam, lorazepam) để đối kháng, nhưng THẬN TRỌNG vì có thể gây ức chế hô hấp trở lại."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ (0.1mg/ml). Không cần pha loãng.",
                "infusion_rate": "Overdose: 0.2mg IV, lặp lại 0.2mg mỗi 1 phút đến khi đáp ứng (tối đa 1mg). Reversal: 0.1-0.2mg IV titrate đến khi đáp ứng. Trẻ em: 0.01mg/kg IV (tối đa 0.2mg), lặp lại đến khi đáp ứng.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác. Tiêm bolus riêng biệt."],
                "notes": "QUAN TRỌNG: 1) Tác dụng ngắn (45-90 phút) - benzodiazepine có thể tác dụng trở lại, 2) Theo dõi sát ít nhất 2-4 giờ sau khi dùng, 3) CHỐNG CHỈ ĐỊNH ở ngộ độc TCA hoặc động kinh đang điều trị với benzodiazepine, 4) Ở bệnh nhân nghiện: có thể gây hội chứng cai nặng, 5) Khởi đầu với liều thấp (0.2mg), tăng dần nếu cần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Flumazenil",
                "ACLS Guidelines 2020 - American Heart Association",
                "Benzodiazepine Overdose Guidelines",
                "UpToDate - Flumazenil: Drug Information",
                "Medscape - Flumazenil Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Flumazenil Monograph",
                "Micromedex - Flumazenil Drug Information"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, benzodiazepine overdose guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
}

__all__ = ['EMERGENCY_DRUGS']
