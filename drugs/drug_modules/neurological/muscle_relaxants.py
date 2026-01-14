"""
Muscle Relaxants
Skeletal muscle relaxants for spasticity and muscle spasms
"""

MUSCLE_RELAXANTS_DRUGS = {
    "Baclofen":     {
        "group": "Neurology - Muscle Relaxant (GABA-B Agonist)",
        "vietnamese_name": "Baclofen, Lioresal",
        "administration": [
            "PO",
            "Intrathecal"
    ],
        "indications": [
            "Co cứng cơ (spasticity) - đa xơ cứng, chấn thương tủy sống",
            "Co cứng cơ do bại não",
            "Đau cơ xương (off-label)",
            "Hiccups kháng trị (off-label)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng baclofen hoặc các thành phần khác",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy"
    ],
            "tương_đối": [
                "Bệnh thận (CrCl 30-60) - giảm thải trừ, giảm liều 25-50%",
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy hô hấp - tăng nguy cơ suy hô hấp",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, lú lẫn, giảm liều 50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với alcohol hoặc opioids - tăng nguy cơ suy hô hấp",
                "Dùng với benzodiazepines - tăng tác dụng ức chế hệ thần kinh trung ương"
    ],
        },
        "dosage": {
            "adult_spasticity_po": "5mg x 3 lần/ngày, tăng dần mỗi 3-7 ngày đến 15-20mg x 3-4 lần/ngày (tối đa 80mg/ngày)",
            "adult_intrathecal": "Bắt đầu với test dose, sau đó truyền liên tục qua pump (50-200mcg/ngày)",
            "adult_max": "80mg/ngày PO",
            "notes": """GABA-B receptor agonist. Tăng liều chậm để giảm tác dụng phụ. Không ngừng đột ngột (có thể gây co giật, ảo giác).""",
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Yếu cơ (phổ biến)",
            "Mệt mỏi",
            "Buồn nôn",
            "Hạ huyết áp",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Suy hô hấp (hiếm, đặc biệt khi dùng intrathecal)",
            "Co giật khi ngừng đột ngột"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Opioids: tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Benzodiazepines: tăng tác dụng ức chế hệ thần kinh trung ương",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "MAO inhibitors: tăng nguy cơ tác dụng phụ"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Baclofen là GABA-B receptor agonist, kích thích thụ thể GABA-B ở tủy sống và não. GABA-B receptors là thụ thể G-protein coupled, khi được kích thích sẽ ức chế phóng thích chất dẫn truyền thần kinh kích thích (glutamate) và tăng phóng thích chất dẫn truyền thần kinh ức chế (GABA). Ở tủy sống, baclofen ức chế phản xạ kéo dãn (stretch reflex), giảm co cứng cơ (spasticity). Tác dụng: điều trị co cứng cơ (spasticity) trong đa xơ cứng, chấn thương tủy sống, và bại não. Có dạng uống (PO) và dạng intrathecal (tiêm vào khoang dưới nhện, qua pump). Tác dụng phụ: buồn ngủ, chóng mặt, yếu cơ (phổ biến), suy hô hấp (hiếm, đặc biệt khi dùng intrathecal), co giật khi ngừng đột ngột.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm co cứng cơ, cải thiện chức năng vận động",
            "Dấu hiệu suy hô hấp: thở chậm, thở nông, giảm SpO2 (đặc biệt khi dùng intrathecal)",
            "Dấu hiệu quá liều: buồn ngủ nặng, lú lẫn, hôn mê, suy hô hấp",
            "Yếu cơ - phổ biến, có thể ảnh hưởng đến khả năng đi lại",
            "Hạ huyết áp - đặc biệt khi bắt đầu hoặc tăng liều",
            "Dấu hiệu cai khi ngừng đột ngột: co giật, ảo giác, lo âu, mất ngủ",
            "Tương tác với alcohol, opioids, benzodiazepines, antihypertensives"
    ],
        "precautions": [
            "Suy hô hấp - hiếm nhưng nguy hiểm, đặc biệt khi dùng intrathecal, theo dõi hô hấp chặt chẽ",
            "Yếu cơ - phổ biến, có thể ảnh hưởng đến khả năng đi lại, cân nhắc giảm liều",
            "Hạ huyết áp - đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Lú lẫn - đặc biệt ở người cao tuổi, giảm liều",
            "Tăng liều chậm để giảm tác dụng phụ (đặc biệt buồn ngủ, yếu cơ)",
            "Tránh rượu - tăng tác dụng ức chế hệ thần kinh trung ương, suy hô hấp",
            "Tránh opioids - tăng nguy cơ suy hô hấp (nguy hiểm)",
            "Thận trọng khi dùng với benzodiazepines - tăng tác dụng ức chế hệ thần kinh trung ương",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Dạng intrathecal - dùng cho co cứng cơ nặng không đáp ứng với PO, cần pump và theo dõi chặt chẽ",
            "KHÔNG ngừng đột ngột (có thể gây co giật, ảo giác, lo âu, mất ngủ) - giảm liều dần (tapering)"
    ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "4-8 giờ (PO)",
            "protein_binding": "30%",
            "clearance": """Thận: bài tiết chủ yếu nguyên dạng (70-80%). Gan: chuyển hóa một phần. Cần điều chỉnh liều ở suy thận.""",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": """Nguy cơ suy hô hấp, đặc biệt khi dùng với opioids hoặc alcohol. Nguy cơ co giật khi ngừng đột ngột - phải giảm liều dần (tapering).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp (nguy hiểm)",
                    "management": "Tránh hoặc giảm rượu. Cảnh báo bệnh nhân về nguy cơ suy hô hấp.",
                },
    {
                    "drug": "Opioids (Morphine, Fentanyl, Oxycodone)",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ suy hô hấp (nguy hiểm, có thể tử vong)",
                    "management": "Tránh dùng cùng nếu có thể. Nếu bắt buộc, giảm liều cả hai thuốc, theo dõi hô hấp chặt chẽ.",
                }
                ],
            "moderate": [
    {
                    "drug": "Benzodiazepines (Diazepam, Lorazepam)",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng buồn ngủ, chóng mặt, suy hô hấp",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi hô hấp.",
                },
    {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở, co giật) nếu mẹ dùng baclofen trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.""",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": """Baclofen bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.""",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém).",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": """Baclofen chuyển hóa một phần ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "under_30": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": """Baclofen bài tiết chủ yếu qua thận (70-80% nguyên dạng). Suy thận làm giảm thải trừ, tăng nguy cơ tích lũy và tác dụng phụ.""",
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, lú lẫn, hôn mê",
                "Rối loạn hô hấp: suy hô hấp (nguy hiểm, có thể tử vong)",
                "Rối loạn tim mạch: hạ huyết áp, nhịp chậm",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần (quan trọng, có thể cần thở máy)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp (quan trọng), tim mạch, huyết áp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Theo dõi ít nhất 24 giờ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (quan trọng), tim mạch, huyết áp",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": """Chia 3-4 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm (mỗi 3-7 ngày) để giảm tác dụng phụ. KHÔNG ngừng đột ngột (có thể gây co giật, ảo giác, lo âu, mất ngủ) - giảm liều dần (tapering).""",
            },
            "intrathecal": {
                "reconstitution": "Dạng intrathecal: pha loãng trong sterile solution.",
                "infusion_rate": "Truyền liên tục qua pump. Bắt đầu với test dose, sau đó điều chỉnh liều.",
                "compatibility": [],
                "incompatibility": [],
                "notes": """Dạng intrathecal: dùng cho co cứng cơ nặng không đáp ứng với PO, cần pump và theo dõi chặt chẽ. Nguy cơ suy hô hấp cao hơn PO.""",
            },
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Baclofen",
                "UpToDate - Baclofen: Drug information",
                "FDA - Lioresal (baclofen) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
    ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews",
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với baclofen"
    ],
            "tương_đối": [
                "Suy thận nặng (tăng nguy cơ độc tính, cần giảm liều)",
                "Động kinh không kiểm soát",
                "Rối loạn tâm thần",
                "Loét dạ dày tá tràng"
    ],
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ],
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế)",
            "infants": "1 tháng - 2 tuổi: 2.5-5mg x 3 lần/ngày PO, tăng dần. Intrathecal: bắt đầu với test dose rất thấp. Theo dõi chặt chẽ suy hô hấp.",
            "children_2_12": "2.5-5mg x 3 lần/ngày PO, tăng dần đến 10-15mg x 3-4 lần/ngày (tối đa 40mg/ngày). Intrathecal: bắt đầu với test dose, sau đó truyền liên tục qua pump. Theo dõi chặt chẽ suy hô hấp.",
            "adolescents_12_18": "5mg x 3 lần/ngày PO, tăng dần đến 15-20mg x 3-4 lần/ngày (tối đa 80mg/ngày). Liều tương tự người lớn. Theo dõi chặt chẽ suy hô hấp.",
            "notes": "GABA-B receptor agonist. Tăng liều chậm để giảm tác dụng phụ. QUAN TRỌNG: KHÔNG ngừng đột ngột (có thể gây co giật, ảo giác, suy hô hấp). Điều chỉnh liều theo chức năng thận. Theo dõi chặt chẽ suy hô hấp, đặc biệt khi dùng intrathecal."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, lú lẫn, suy hô hấp). Tăng nguy cơ té ngã. Suy thận phổ biến hơn → cần điều chỉnh liều.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (5mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh liều theo chức năng thận (CrCl 30-60: giảm 25-50%, CrCl <30: giảm 50% hoặc tránh dùng). Theo dõi chặt chẽ tác dụng phụ.",
            "monitoring": "Theo dõi chặt chẽ suy hô hấp - QUAN TRỌNG. Theo dõi tác dụng phụ (buồn ngủ, lú lẫn, yếu cơ). Theo dõi nguy cơ té ngã. Theo dõi chức năng thận. KHÔNG ngừng đột ngột."
        },
        "brand_names": {
            "vietnam": ["Lioresal", "Baclofen", "Baclofen Stada"],
            "common": ["Lioresal", "Baclofen", "Gablofen (intrathecal)"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "3,000 - 20,000 VND/viên PO (tùy hàm lượng và thương hiệu). Intrathecal: giá rất cao.",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Baclofen generic thường rẻ hơn (3,000-10,000 VND/viên 10mg PO). Lioresal (brand) thường đắt hơn (10,000-20,000 VND/viên 10mg PO). Dạng intrathecal: giá rất cao, cần thiết bị đặc biệt."
        }
    },
    "Carisoprodol":     {
        "group": "Neurology - Muscle Relaxant (Skeletal)",
        "vietnamese_name": "Carisoprodol, Soma",
        "administration": [
            "PO"
    ],
        "indications": [
            "Co thắt cơ xương khớp (muscle spasm) - ngắn hạn",
            "Đau cơ xương (musculoskeletal pain)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng carisoprodol",
                "Porphyria",
                "Dị ứng với meprobamate"
    ],
            "tương_đối": [
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện",
                "Bệnh gan nặng - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "250-350mg x 3-4 lần/ngày",
            "adult_max": "1400mg/ngày",
            "notes": "CHỈ dùng ngắn hạn (2-3 tuần). Chuyển hóa thành meprobamate (controlled substance, nguy cơ nghiện).",
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Đau đầu",
            "Nguy cơ nghiện/lệ thuộc (do meprobamate)",
            "Hội chứng cai khi ngừng"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần, nguy cơ ức chế hô hấp",
            "CNS depressants: tăng tác dụng ức chế",
            "CYP2C19 inhibitors: tăng nồng độ carisoprodol"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Carisoprodol là thuốc giãn cơ xương khớp, được chuyển hóa thành meprobamate (controlled substance, có nguy cơ nghiện). Cơ chế chính xác chưa rõ. CHỈ dùng ngắn hạn (2-3 tuần). Có nguy cơ nghiện/lệ thuộc do meprobamate.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm co thắt cơ",
            "Dấu hiệu nghiện/lệ thuộc",
            "Dấu hiệu cai khi ngừng"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (2-3 tuần)",
            "NGUY CƠ NGHIỆN/LỆ THUỘC - do meprobamate (controlled substance)",
            "Không ngừng đột ngột - có thể gây hội chứng cai",
            "Tránh rượu - tăng tác dụng an thần, nguy cơ ức chế hô hấp",
            "Thận trọng ở bệnh nhân có tiền sử nghiện/lạm dụng chất"
    ],
        "pharmacokinetics": {
            "half_life": "2 giờ (carisoprodol), 10 giờ (meprobamate)",
            "onset": "30 phút",
            "duration": "4-6 giờ",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan (chuyển hóa thành meprobamate qua CYP2C19), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Controlled substance - cần bảo quản an toàn.",
        "black_box_warnings": """NGUY CƠ NGHIỆN, LẠM DỤNG, VÀ LỆ THUỘC - carisoprodol chuyển hóa thành meprobamate (controlled substance). Chỉ dùng ngắn hạn (2-3 tuần).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol, CNS depressants",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp",
                    "management": "Tránh rượu. Thận trọng với CNS depressants.",
                }
                ],
            "moderate": [
    {
                    "drug": "CYP2C19 inhibitors (Omeprazole, Fluoxetine)",
                    "mechanism": "Ức chế chuyển hóa carisoprodol",
                    "effect": "Tăng nồng độ carisoprodol",
                    "management": "Thận trọng. Có thể cần giảm liều carisoprodol.",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng carisoprodol",
                "Porphyria",
                "Dị ứng với meprobamate"
    ],
            "tương_đối": [
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện",
                "Bệnh gan nặng - thận trọng",
                "Suy thận nặng - thận trọng, giảm liều"
    ],
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Carisoprodol và meprobamate không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": """Carisoprodol chuyển hóa thành meprobamate ở gan, sau đó thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy meprobamate. Giảm liều và theo dõi chặt chẽ ở suy thận.""",
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Carisoprodol và meprobamate bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Carisoprodol chuyển hóa qua gan. Suy gan có thể ảnh hưởng đến chuyển hóa.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Ức chế hô hấp",
                "Hôn mê",
                "Hạ huyết áp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Hỗ trợ hô hấp",
                "Rửa dạ dày",
                "Than hoạt tính",
                "Theo dõi hỗ trợ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": "250-350mg x 3-4 lần/ngày. CHỈ dùng ngắn hạn (2-3 tuần).",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Carisoprodol (Soma)",
                "UpToDate - Carisoprodol: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, controlled substance",
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <16 tuổi (dữ liệu hạn chế, nguy cơ nghiện)",
            "children_2_12": "Không khuyến cáo cho trẻ <16 tuổi (dữ liệu hạn chế, nguy cơ nghiện)",
            "adolescents_12_18": "Không khuyến cáo cho trẻ <16 tuổi (dữ liệu hạn chế, nguy cơ nghiện). Nếu cần: 250-350mg x 3-4 lần/ngày PO. CHỈ dùng ngắn hạn (2-3 tuần).",
            "notes": "Chủ yếu dùng cho người lớn. QUAN TRỌNG: Nguy cơ nghiện, lạm dụng. CHỈ dùng ngắn hạn (2-3 tuần). Tránh dùng với alcohol hoặc opioids (tăng nguy cơ suy hô hấp)."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt, lú lẫn). Tăng nguy cơ té ngã. Nguy cơ nghiện.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (250mg x 2-3 lần/ngày). CHỈ dùng ngắn hạn (2-3 tuần). Theo dõi chặt chẽ tác dụng phụ và nguy cơ nghiện.",
            "monitoring": "Theo dõi tác dụng phụ (buồn ngủ, chóng mặt, lú lẫn). Theo dõi nguy cơ té ngã. Theo dõi dấu hiệu nghiện, lạm dụng. CHỈ dùng ngắn hạn."
        },
        "brand_names": {
            "vietnam": ["Soma", "Carisoprodol"],
            "common": ["Soma", "Carisoprodol"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "10,000 - 40,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Carisoprodol generic thường rẻ hơn (10,000-25,000 VND/viên 350mg). Soma (brand) thường đắt hơn (25,000-40,000 VND/viên 350mg)."
        }
    },
    "Cyclobenzaprine":     {
        "group": "Neurology - Muscle Relaxant (Skeletal)",
        "vietnamese_name": "Cyclobenzaprine, Flexeril",
        "administration": [
            "PO"
    ],
        "indications": [
            "Co thắt cơ xương khớp (muscle spasm) - ngắn hạn",
            "Đau cơ xương (musculoskeletal pain)",
            "Đau lưng cấp tính"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cyclobenzaprine",
                "Dùng MAO inhibitor trong vòng 14 ngày",
                "Giai đoạn cấp tính sau nhồi máu cơ tim",
                "Suy tim nặng",
                "Block nhĩ thất độ 2-3",
                "Cường giáp"
    ],
            "tương_đối": [
                "Dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                "Bệnh tim mạch - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "5mg x 3 lần/ngày, có thể tăng đến 10mg x 3 lần/ngày (tối đa 30mg/ngày)",
            "adult_extended": "15-30mg x 1 lần/ngày (dạng extended release)",
            "adult_max": "30mg/ngày",
            "notes": "CHỈ dùng ngắn hạn (2-3 tuần). Cấu trúc tương tự tricyclic antidepressants. Có tác dụng an thần.",
        },
        "side_effects": [
            "Buồn ngủ (rất phổ biến)",
            "Khô miệng (phổ biến)",
            "Chóng mặt",
            "Mệt mỏi",
            "Nhìn mờ",
            "Táo bón",
            "Hạ huyết áp tư thế"
    ],
        "interactions": [
            "MAO inhibitor: CHỐNG CHỈ ĐỊNH",
            "Thuốc ức chế tái hấp thu serotonin (SSRI, SNRI): tăng nguy cơ hội chứng serotonin",
            "Alcohol: tăng tác dụng an thần",
            "Thuốc chống trầm cảm tricyclic: tác dụng cộng dồn",
            "Thuốc chống loạn thần: tăng tác dụng an thần"
    ],
        "pregnancy": "B",
        "mechanism_of_action": """Cyclobenzaprine là thuốc giãn cơ xương khớp, có cấu trúc tương tự tricyclic antidepressants (TCA). Cơ chế chính xác chưa rõ, nhưng có thể tác động lên brainstem để giảm phản xạ cơ xương. Cyclobenzaprine KHÔNG tác động trực tiếp lên cơ xương như thuốc giãn cơ khác. Có tác dụng an thần mạnh (do cấu trúc tương tự TCA). CHỈ dùng ngắn hạn (2-3 tuần) cho co thắt cơ xương khớp.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm co thắt cơ, giảm đau",
            "Dấu hiệu an thần quá mức (buồn ngủ, mệt mỏi)",
            "Dấu hiệu hội chứng serotonin (khi dùng với SSRI/SNRI)",
            "Huyết áp (hạ huyết áp tư thế)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (2-3 tuần) - không hiệu quả trong dùng lâu dài",
            "Buồn ngủ rất phổ biến - tránh lái xe, vận hành máy móc",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitor",
            "Thận trọng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin",
            "Tránh rượu - tăng tác dụng an thần",
            "Cấu trúc tương tự TCA - có thể có tác dụng phụ tương tự TCA",
            "Không dùng cho trẻ em <15 tuổi"
    ],
        "pharmacokinetics": {
            "half_life": "1-3 ngày (dài, tích lũy)",
            "onset": "1 giờ",
            "duration": "12-24 giờ",
            "protein_binding": "93%",
            "clearance": "Gan (chuyển hóa qua CYP3A4, CYP1A2), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": """CHỐNG CHỈ ĐỊNH với MAO inhibitor. Nguy cơ hội chứng serotonin khi dùng với SSRI/SNRI. Buồn ngủ có thể ảnh hưởng đến khả năng lái xe và vận hành máy móc.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng nghiêm trọng",
                    "effect": "Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng cyclobenzaprine.",
                },
    {
                    "drug": "SSRI/SNRI (Fluoxetine, Sertraline, Venlafaxine)",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "Tránh dùng chung. Nếu bắt buộc, theo dõi dấu hiệu hội chứng serotonin.",
                }
                ],
            "moderate": [
    {
                    "drug": "Alcohol, Benzodiazepines",
                    "mechanism": "Tăng tác dụng an thần",
                    "effect": "Tăng buồn ngủ, chóng mặt",
                    "management": "Tránh rượu. Thận trọng với benzodiazepines.",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng cyclobenzaprine",
                "Dùng MAO inhibitor trong vòng 14 ngày",
                "Giai đoạn cấp tính sau nhồi máu cơ tim",
                "Suy tim nặng",
                "Block nhĩ thất độ 2-3",
                "Cường giáp"
    ],
            "tương_đối": [
                "Dùng với SSRI/SNRI - tăng nguy cơ hội chứng serotonin",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                "Bệnh tim mạch - thận trọng",
                "Suy thận nặng - thận trọng, giảm liều",
                "Suy gan nặng - thận trọng, giảm liều"
    ],
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Cyclobenzaprine không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": """Cyclobenzaprine thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy, đặc biệt với half-life dài (1-3 ngày). Giảm liều và theo dõi chặt chẽ ở suy thận.""",
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Cyclobenzaprine bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Cyclobenzaprine chuyển hóa qua gan. Suy gan có thể ảnh hưởng đến chuyển hóa.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Lú lẫn, hôn mê",
                "Nhịp tim nhanh",
                "Hạ huyết áp",
                "Co giật"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày",
                "Than hoạt tính",
                "Theo dõi hỗ trợ",
                "Điều trị co giật nếu có"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": "5mg x 3 lần/ngày, có thể tăng đến 10mg x 3 lần/ngày. CHỈ dùng ngắn hạn (2-3 tuần).",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cyclobenzaprine (Flexeril)",
                "UpToDate - Cyclobenzaprine: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <15 tuổi (dữ liệu hạn chế)",
            "children_2_12": "Không khuyến cáo cho trẻ <15 tuổi (dữ liệu hạn chế)",
            "adolescents_12_18": "Không khuyến cáo cho trẻ <15 tuổi (dữ liệu hạn chế). Nếu cần: 5mg x 3 lần/ngày PO. CHỈ dùng ngắn hạn (2-3 tuần).",
            "notes": "Chủ yếu dùng cho người lớn. CHỈ dùng ngắn hạn (2-3 tuần). Tránh dùng với MAO inhibitors (tăng nguy cơ serotonin syndrome)."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, khô miệng, chóng mặt). Tăng nguy cơ té ngã. Suy gan, suy thận phổ biến hơn.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (5mg x 2 lần/ngày). CHỈ dùng ngắn hạn (2-3 tuần). Điều chỉnh liều theo chức năng gan, thận. Theo dõi chặt chẽ tác dụng phụ.",
            "monitoring": "Theo dõi tác dụng phụ (buồn ngủ, khô miệng, chóng mặt). Theo dõi nguy cơ té ngã. CHỈ dùng ngắn hạn."
        },
        "brand_names": {
            "vietnam": ["Flexeril", "Cyclobenzaprine"],
            "common": ["Flexeril", "Cyclobenzaprine"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "5,000 - 25,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Cyclobenzaprine generic thường rẻ hơn (5,000-15,000 VND/viên 10mg). Flexeril (brand) thường đắt hơn (15,000-25,000 VND/viên 10mg)."
        }
    },
    "Metaxalone":     {
        "group": "Neurology - Muscle Relaxant (Skeletal)",
        "vietnamese_name": "Metaxalone, Skelaxin",
        "administration": [
            "PO"
    ],
        "indications": [
            "Co thắt cơ xương khớp (muscle spasm) - ngắn hạn",
            "Đau cơ xương (musculoskeletal pain)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng metaxalone",
                "Suy thận nặng",
                "Suy gan nặng",
                "Thiếu máu nặng"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng",
                "Suy gan trung bình - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "800mg x 3-4 lần/ngày",
            "adult_max": "3200mg/ngày",
            "notes": "CHỈ dùng ngắn hạn. Ít tác dụng an thần hơn cyclobenzaprine.",
        },
        "side_effects": [
            "Buồn ngủ (ít hơn cyclobenzaprine)",
            "Chóng mặt",
            "Mệt mỏi",
            "Buồn nôn",
            "Nôn",
            "Thiếu máu (hiếm)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần",
            "CNS depressants: tăng tác dụng ức chế"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Metaxalone là thuốc giãn cơ xương khớp. Cơ chế chính xác chưa rõ. CHỈ dùng ngắn hạn cho co thắt cơ xương khớp. Ít tác dụng an thần hơn cyclobenzaprine.""",
        "monitoring": [
            "Đáp ứng điều trị: giảm co thắt cơ",
            "Dấu hiệu an thần (buồn ngủ, mệt mỏi)",
            "Công thức máu (thiếu máu - hiếm)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn",
            "Tránh rượu - tăng tác dụng an thần",
            "Thiếu máu - hiếm nhưng có thể xảy ra, theo dõi công thức máu",
            "Thận trọng ở suy thận, suy gan"
    ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "1 giờ",
            "duration": "4-6 giờ",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "Alcohol, CNS depressants",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, chóng mặt",
                    "management": "Tránh rượu. Thận trọng với CNS depressants.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết metaxalone có bài tiết vào sữa mẹ hay không.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Metaxalone chuyển hóa qua gan. Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Lú lẫn",
                "Ức chế hô hấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Rửa dạ dày",
                "Than hoạt tính",
                "Theo dõi hỗ trợ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": "800mg x 3-4 lần/ngày. CHỈ dùng ngắn hạn.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Metaxalone (Skelaxin)",
                "UpToDate - Metaxalone: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <12 tuổi (dữ liệu hạn chế)",
            "children_2_12": "Không khuyến cáo cho trẻ <12 tuổi (dữ liệu hạn chế)",
            "adolescents_12_18": "Không khuyến cáo cho trẻ <12 tuổi (dữ liệu hạn chế). Nếu cần: 400-800mg x 3-4 lần/ngày PO. CHỈ dùng ngắn hạn.",
            "notes": "Chủ yếu dùng cho người lớn. CHỈ dùng ngắn hạn. CHỐNG CHỈ ĐỊNH ở suy gan nặng và suy thận nặng."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt, mệt mỏi). Suy gan, suy thận phổ biến hơn → CHỐNG CHỈ ĐỊNH nếu suy gan/thận nặng.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (400mg x 2-3 lần/ngày). CHỈ dùng ngắn hạn. CHỐNG CHỈ ĐỊNH nếu suy gan/thận nặng. Theo dõi chặt chẽ tác dụng phụ.",
            "monitoring": "Theo dõi tác dụng phụ (buồn ngủ, chóng mặt, mệt mỏi). Theo dõi chức năng gan, thận. CHỈ dùng ngắn hạn."
        },
        "brand_names": {
            "vietnam": ["Skelaxin", "Metaxalone"],
            "common": ["Skelaxin", "Metaxalone"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "8,000 - 30,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Metaxalone generic thường rẻ hơn (8,000-20,000 VND/viên 400mg). Skelaxin (brand) thường đắt hơn (20,000-30,000 VND/viên 400mg)."
        }
    },
    "Methocarbamol":     {
        "group": "Neurology - Muscle Relaxant (Skeletal)",
        "vietnamese_name": "Methocarbamol, Robaxin",
        "administration": [
            "PO",
            "IV",
            "IM"
    ],
        "indications": [
            "Co thắt cơ xương khớp (muscle spasm) - ngắn hạn",
            "Đau cơ xương (musculoskeletal pain)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng methocarbamol"
    ],
            "tương_đối": [
                "Bệnh gan nặng - thận trọng",
                "Bệnh thận nặng - thận trọng"
    ],
        },
        "dosage": {
            "adult_po": "1.5g x 4 lần/ngày trong 2-3 ngày, sau đó 1g x 4 lần/ngày hoặc 750mg mỗi 4 giờ",
            "adult_iv_im": "1-3g IV/IM, có thể lặp lại mỗi 8 giờ (tối đa 3g/ngày IV/IM)",
            "adult_max": "8g/ngày PO",
            "notes": "CHỈ dùng ngắn hạn. Liều khởi đầu cao, sau đó giảm. Có thể gây nước tiểu màu xanh/đen (vô hại).",
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Mệt mỏi",
            "Nhìn mờ",
            "Nước tiểu màu xanh/đen (vô hại)",
            "Phản ứng tại chỗ tiêm (IV/IM)"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần",
            "CNS depressants: tăng tác dụng ức chế"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Methocarbamol là thuốc giãn cơ xương khớp. Cơ chế chính xác chưa rõ, có thể tác động lên CNS để giảm phản xạ cơ xương. CHỈ dùng ngắn hạn cho co thắt cơ xương khớp. Có thể gây nước tiểu màu xanh/đen (vô hại).""",
        "monitoring": [
            "Đáp ứng điều trị: giảm co thắt cơ",
            "Dấu hiệu an thần (buồn ngủ, mệt mỏi)",
            "Màu nước tiểu (xanh/đen - vô hại, không cần điều trị)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn",
            "Nước tiểu màu xanh/đen - vô hại, không cần điều trị, giải thích cho bệnh nhân",
            "Tránh rượu - tăng tác dụng an thần",
            "IV/IM: có thể gây phản ứng tại chỗ tiêm, phù phổi (hiếm)"
    ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ",
            "onset": "30 phút (PO)",
            "duration": "4-6 giờ",
            "protein_binding": "46-50%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "Alcohol, CNS depressants",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, chóng mặt",
                    "management": "Tránh rượu. Thận trọng với CNS depressants.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết methocarbamol có bài tiết vào sữa mẹ hay không.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Methocarbamol chuyển hóa qua gan. Suy gan có thể ảnh hưởng đến chuyển hóa.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Lú lẫn",
                "Ức chế hô hấp"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn",
                "Hỗ trợ hô hấp",
                "Rửa dạ dày",
                "Than hoạt tính",
                "Theo dõi hỗ trợ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Khởi đầu: 1.5g x 4 lần/ngày trong 2-3 ngày, sau đó 1g x 4 lần/ngày hoặc 750mg mỗi 4 giờ. CHỈ dùng ngắn hạn.""",
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W",
                "infusion_rate": "Truyền chậm, không quá 3ml/phút",
                "compatibility": [
                    "NS",
                    "D5W"
    ],
                "incompatibility": [],
                "notes": """1-3g IV, có thể lặp lại mỗi 8 giờ. Truyền chậm để tránh phản ứng tại chỗ. Có thể gây phù phổi (hiếm).""",
            },
            "im": {
                "notes": "1-3g IM, có thể lặp lại mỗi 8 giờ. Có thể gây đau tại chỗ tiêm.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Methocarbamol (Robaxin)",
                "UpToDate - Methocarbamol: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <16 tuổi (dữ liệu hạn chế)",
            "children_2_12": "Không khuyến cáo cho trẻ <16 tuổi (dữ liệu hạn chế)",
            "adolescents_12_18": "Không khuyến cáo cho trẻ <16 tuổi (dữ liệu hạn chế). Nếu cần: 400-600mg x 3-4 lần/ngày PO. CHỈ dùng ngắn hạn.",
            "notes": "Chủ yếu dùng cho người lớn. CHỈ dùng ngắn hạn. Có dạng IV/IM cho trường hợp nặng. Tránh dùng với alcohol hoặc opioids (tăng nguy cơ suy hô hấp)."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt, mệt mỏi). Tăng nguy cơ té ngã. Suy gan, suy thận phổ biến hơn.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (400mg x 2-3 lần/ngày). CHỈ dùng ngắn hạn. Điều chỉnh liều theo chức năng gan, thận. Theo dõi chặt chẽ tác dụng phụ.",
            "monitoring": "Theo dõi tác dụng phụ (buồn ngủ, chóng mặt, mệt mỏi). Theo dõi nguy cơ té ngã. CHỈ dùng ngắn hạn."
        },
        "brand_names": {
            "vietnam": ["Robaxin", "Methocarbamol"],
            "common": ["Robaxin", "Methocarbamol"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "4,000 - 20,000 VND/viên PO (tùy hàm lượng và thương hiệu). Dạng IV/IM: 15,000 - 50,000 VND/ống.",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Methocarbamol generic thường rẻ hơn (4,000-12,000 VND/viên 500mg PO). Robaxin (brand) thường đắt hơn (12,000-20,000 VND/viên 500mg PO). Dạng IV/IM: 15,000-50,000 VND/ống 500mg."
        }
    },
    "Tizanidine":     {
        "group": "Neurology - Muscle Relaxant (Alpha-2 Adrenergic Agonist)",
        "vietnamese_name": "Tizanidine, Zanaflex",
        "administration": [
            "PO"
    ],
        "indications": [
            "Co cứng cơ (spasticity) - đa xơ cứng, chấn thương tủy sống",
            "Co cứng cơ do bại não",
            "Đau cơ xương (off-label)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tizanidine hoặc các thành phần khác",
                "Dùng với ciprofloxacin - CHỐNG CHỈ ĐỊNH",
                "Dùng với fluvoxamine - CHỐNG CHỈ ĐỊNH"
    ],
            "tương_đối": [
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy",
                "Bệnh tim mạch (suy tim, loạn nhịp) - tăng nguy cơ hạ huyết áp, nhịp chậm",
                "Người cao tuổi - tăng nguy cơ tác dụng phụ, lú lẫn, hạ huyết áp, giảm liều 50%",
                "Mang thai (nguy cơ dị tật bẩm sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Dùng với CYP1A2 inhibitors (trừ ciprofloxacin, fluvoxamine) - giảm liều tizanidine",
                "Dùng với CYP1A2 inducers hoặc hút thuốc - tăng liều tizanidine",
                "Dùng với oral contraceptives - giảm liều tizanidine 50%",
                "Dùng với antihypertensives - tăng nguy cơ hạ huyết áp"
    ],
        },
        "dosage": {
            "adult_spasticity": "2-4mg x 3 lần/ngày, tăng dần đến 8mg x 3 lần/ngày (tối đa 36mg/ngày)",
            "adult_max": "36mg/ngày",
            "notes": """Alpha-2 adrenergic agonist. Tác dụng ngắn (3-6 giờ). Tăng liều chậm để giảm tác dụng phụ. CHỐNG CHỈ ĐỊNH với ciprofloxacin hoặc fluvoxamine.""",
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Chóng mặt",
            "Khô miệng (phổ biến)",
            "Yếu cơ",
            "Mệt mỏi",
            "Hạ huyết áp (phổ biến)",
            "Nhịp chậm",
            "Lú lẫn (đặc biệt ở người cao tuổi)",
            "Tăng ALT/AST (hiếm)"
    ],
        "interactions": [
            "Ciprofloxacin: CHỐNG CHỈ ĐỊNH - tăng nồng độ tizanidine, tăng nguy cơ tác dụng phụ nặng",
            "Fluvoxamine: CHỐNG CHỈ ĐỊNH - tăng nồng độ tizanidine, tăng nguy cơ tác dụng phụ nặng",
            "CYP1A2 inhibitors: tăng nồng độ tizanidine",
            "CYP1A2 inducers: giảm nồng độ tizanidine",
            "Alcohol: tăng tác dụng ức chế hệ thần kinh trung ương",
            "Antihypertensives: tăng nguy cơ hạ huyết áp",
            "Oral contraceptives: tăng nồng độ tizanidine"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Tizanidine là alpha-2 adrenergic agonist, kích thích thụ thể alpha-2 adrenergic ở tủy sống và não. Alpha-2 receptors là thụ thể G-protein coupled, khi được kích thích sẽ ức chế phóng thích chất dẫn truyền thần kinh kích thích (norepinephrine) và tăng phóng thích chất dẫn truyền thần kinh ức chế (GABA). Ở tủy sống, tizanidine ức chế phản xạ kéo dãn (stretch reflex), giảm co cứng cơ (spasticity). Tác dụng: điều trị co cứng cơ (spasticity) trong đa xơ cứng, chấn thương tủy sống, và bại não. Có dạng uống (PO). Tác dụng ngắn (3-6 giờ), cần dùng nhiều lần/ngày. Tác dụng phụ: buồn ngủ, chóng mặt, khô miệng (phổ biến), hạ huyết áp (phổ biến), nhịp chậm, tăng ALT/AST (hiếm).""",
        "monitoring": [
            "Đáp ứng điều trị: giảm co cứng cơ, cải thiện chức năng vận động",
            "Huyết áp - hạ huyết áp phổ biến, đặc biệt khi bắt đầu hoặc tăng liều",
            "Nhịp tim - nhịp chậm, đặc biệt khi bắt đầu hoặc tăng liều",
            "Dấu hiệu quá liều: buồn ngủ nặng, lú lẫn, hạ huyết áp nặng, nhịp chậm",
            "ALT/AST - tăng ALT/AST hiếm, theo dõi định kỳ",
            "Tương tác với ciprofloxacin, fluvoxamine (CHỐNG CHỈ ĐỊNH), CYP1A2 inhibitors/inducers, oral contraceptives"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với ciprofloxacin hoặc fluvoxamine - tăng nồng độ tizanidine, tăng nguy cơ tác dụng phụ nặng (hạ huyết áp nặng, nhịp chậm, suy hô hấp)",
            "Hạ huyết áp - phổ biến, đặc biệt khi bắt đầu hoặc tăng liều, đứng dậy chậm, uống đủ nước",
            "Nhịp chậm - đặc biệt khi bắt đầu hoặc tăng liều, theo dõi nhịp tim",
            "Lú lẫn - đặc biệt ở người cao tuổi, giảm liều",
            "Tăng liều chậm để giảm tác dụng phụ (đặc biệt hạ huyết áp, buồn ngủ)",
            "Tránh rượu - tăng tác dụng ức chế hệ thần kinh trung ương",
            "Thận trọng khi dùng với CYP1A2 inhibitors (fluvoxamine, ciprofloxacin) - CHỐNG CHỈ ĐỊNH với fluvoxamine và ciprofloxacin",
            "Thận trọng khi dùng với CYP1A2 inducers (carbamazepine, smoking) - giảm nồng độ tizanidine, có thể cần tăng liều",
            "Thận trọng khi dùng với oral contraceptives - tăng nồng độ tizanidine, giảm liều tizanidine 50%",
            "Thận trọng khi dùng với antihypertensives - tăng nguy cơ hạ huyết áp",
            "Hút thuốc - giảm nồng độ tizanidine, có thể cần tăng liều ở người hút thuốc"
    ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "3-6 giờ (PO)",
            "protein_binding": "30%",
            "clearance": """Gan: chuyển hóa qua CYP1A2 (chính). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều khi dùng với CYP1A2 inhibitors/inducers và oral contraceptives.""",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": """CHỐNG CHỈ ĐỊNH với ciprofloxacin hoặc fluvoxamine - tăng nồng độ tizanidine, tăng nguy cơ tác dụng phụ nặng (hạ huyết áp nặng, nhịp chậm, suy hô hấp).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Ciprofloxacin",
                    "mechanism": "Ức chế chuyển hóa tizanidine qua CYP1A2, tăng nồng độ tizanidine",
                    "effect": """Tăng nồng độ tizanidine 10-33 lần, tăng nguy cơ tác dụng phụ nặng (hạ huyết áp nặng, nhịp chậm, suy hô hấp)""",
                    "management": """CHỐNG CHỈ ĐỊNH - không được dùng cùng. Nếu đang dùng tizanidine, ngừng tizanidine ít nhất 2 tuần trước khi dùng ciprofloxacin.""",
                },
    {
                    "drug": "Fluvoxamine",
                    "mechanism": "Ức chế chuyển hóa tizanidine qua CYP1A2, tăng nồng độ tizanidine",
                    "effect": """Tăng nồng độ tizanidine 10-33 lần, tăng nguy cơ tác dụng phụ nặng (hạ huyết áp nặng, nhịp chậm, suy hô hấp)""",
                    "management": """CHỐNG CHỈ ĐỊNH - không được dùng cùng. Nếu đang dùng tizanidine, ngừng tizanidine ít nhất 2 tuần trước khi dùng fluvoxamine.""",
                },
    {
                    "drug": "Other CYP1A2 inhibitors (Cimetidine, Acyclovir)",
                    "mechanism": "Ức chế chuyển hóa tizanidine qua CYP1A2, tăng nồng độ tizanidine",
                    "effect": "Tăng nồng độ tizanidine, tăng tác dụng phụ (hạ huyết áp, nhịp chậm)",
                    "management": """Tránh dùng cùng nếu có thể. Nếu bắt buộc, giảm liều tizanidine 50-75%. Theo dõi tác dụng phụ chặt chẽ.""",
                }
                ],
            "moderate": [
    {
                    "drug": "CYP1A2 inducers (Carbamazepine, Smoking)",
                    "mechanism": "Cảm ứng chuyển hóa tizanidine qua CYP1A2, giảm nồng độ tizanidine",
                    "effect": "Giảm nồng độ tizanidine, giảm hiệu quả",
                    "management": """Tăng liều tizanidine 50-100% khi dùng với carbamazepine hoặc ở người hút thuốc. Theo dõi đáp ứng điều trị.""",
                },
    {
                    "drug": "Oral contraceptives",
                    "mechanism": "Ức chế chuyển hóa tizanidine qua CYP1A2, tăng nồng độ tizanidine",
                    "effect": "Tăng nồng độ tizanidine, tăng tác dụng phụ",
                    "management": "Giảm liều tizanidine 50% khi dùng với oral contraceptives. Theo dõi tác dụng phụ.",
                },
    {
                    "drug": "Antihypertensives",
                    "mechanism": "Cả hai đều có thể gây hạ huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp tư thế, ngất",
                    "management": "Thận trọng. Có thể cần giảm liều một trong hai thuốc. Theo dõi huyết áp.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh, nhưng chứng cứ không rõ ràng. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ.""",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": """Tizanidine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ sơ sinh rất thấp. Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ.""",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém).",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": """Tizanidine chuyển hóa ở gan qua CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.""",
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ nặng, lú lẫn, hôn mê",
                "Rối loạn tim mạch: hạ huyết áp nặng, nhịp chậm",
                "Rối loạn hô hấp: suy hô hấp (hiếm)",
                "Rối loạn tiêu hóa: buồn nôn, nôn"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, huyết áp (quan trọng)",
                "Xử trí hạ huyết áp: IV fluids, vasopressors nếu cần",
                "Xử trí nhịp chậm: Atropine nếu cần",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi ít nhất 24 giờ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, huyết áp (quan trọng), nhịp tim",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn.",
                "timing": """Chia 3 lần/ngày. Uống cùng thời điểm mỗi ngày. Tăng liều chậm để giảm tác dụng phụ (đặc biệt hạ huyết áp, buồn ngủ).""",
            },
            "im": {
                "reconstitution": "Không có dạng IM",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống",
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống",
            },
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Tizanidine",
                "UpToDate - Tizanidine: Drug information",
                "FDA - Zanaflex (tizanidine) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
    ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews",
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với tizanidine hoặc bất kỳ thành phần nào"
    ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần giảm liều",
                "Suy gan vừa-nặng - cần giảm liều",
                "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ, giảm liều",
                "Hạ huyết áp - thận trọng",
                "Có thai - thận trọng",
                "Đang cho con bú - thận trọng"
    ],
        },
        "renal_adjustment": {
            "normal": "Không đổi liều",
            "30_60": "Không đổi liều",
            "under_30": "Giảm liều, thận trọng",
            "hemodialysis": "Không đổi liều",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ],
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế)",
            "infants": "1 tháng - 2 tuổi: 0.5-1mg x 2-3 lần/ngày PO, tăng dần. Theo dõi chặt chẽ hạ huyết áp và suy hô hấp.",
            "children_2_12": "0.5-1mg x 2-3 lần/ngày PO, tăng dần đến 2-4mg x 3-4 lần/ngày (tối đa 36mg/ngày). Theo dõi chặt chẽ hạ huyết áp và suy hô hấp.",
            "adolescents_12_18": "2mg x 2-3 lần/ngày PO, tăng dần đến 4-8mg x 3-4 lần/ngày (tối đa 36mg/ngày). Liều tương tự người lớn. Theo dõi chặt chẽ hạ huyết áp.",
            "notes": "Alpha-2 adrenergic agonist. Tăng liều chậm để giảm tác dụng phụ. QUAN TRỌNG: Theo dõi hạ huyết áp tư thế - phổ biến. Điều chỉnh liều theo chức năng gan, thận. Giảm liều 50% nếu dùng với oral contraceptives hoặc CYP1A2 inhibitors."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, hạ huyết áp, suy hô hấp). Tăng nguy cơ té ngã. Suy gan, suy thận phổ biến hơn → cần điều chỉnh liều.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (2mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh liều theo chức năng gan, thận (CrCl <30: giảm liều, suy gan: giảm liều). Giảm liều 50% nếu dùng với oral contraceptives. Theo dõi chặt chẽ tác dụng phụ.",
            "monitoring": "Theo dõi hạ huyết áp tư thế - QUAN TRỌNG. Theo dõi tác dụng phụ (buồn ngủ, suy hô hấp, mệt mỏi). Theo dõi nguy cơ té ngã. Theo dõi chức năng gan, thận."
        },
        "brand_names": {
            "vietnam": ["Zanaflex", "Tizanidine", "Tizanidine Stada"],
            "common": ["Zanaflex", "Tizanidine"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "8,000 - 35,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Tizanidine generic thường rẻ hơn (8,000-20,000 VND/viên 4mg). Zanaflex (brand) thường đắt hơn (20,000-35,000 VND/viên 4mg)."
        }
    },
}

__all__ = ['MUSCLE_RELAXANTS_DRUGS']





















