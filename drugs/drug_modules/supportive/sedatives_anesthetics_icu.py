"""
Sedatives and Anesthetics commonly used in ICU and procedural sedation
"""

SEDATIVES_ANESTHETICS_ICU_DRUGS = {
    "Propofol": {
        "group": "Supportive - Sedative/Anesthetic (ICU)",
        "vietnamese_name": "Propofol (Diprivan)",
        "administration": ["IV"],
        "indications": [
            "Gây mê khởi đầu và duy trì trong phẫu thuật.",
            "An thần cho bệnh nhân thở máy trong ICU.",
            "An thần ngắn hạn trong các thủ thuật (nội soi, can thiệp).",
        ],
        "contraindications": [
            "Dị ứng với propofol hoặc bất kỳ thành phần nào của thuốc (bao gồm lecithin trứng, dầu đậu nành tùy chế phẩm).",
            "Huyết áp rất thấp hoặc sốc không kiểm soát được.",
        ],
        "dosage": {
            "induction_of_anesthesia": "1–2.5mg/kg IV bolus chậm (người lớn khỏe).",
            "maintenance_of_anesthesia": "4–12mg/kg/giờ truyền tĩnh mạch, chỉnh liều theo đáp ứng.",
            "icu_sedation": "5–50mcg/kg/phút (0.3–3mg/kg/giờ), chỉnh theo mức an thần mong muốn.",
            "procedural_sedation": "0.5–1mg/kg IV bolus, sau đó truyền 25–75mcg/kg/phút nếu cần.",
            "notes": "Người cao tuổi, suy tim, giảm thể tích: dùng liều thấp hơn và tăng từ từ.",
        },
        "renal_adjustment": {
            "normal": "Không cần điều chỉnh.",
            "30_60": "Không cần điều chỉnh đáng kể; chỉnh liều theo huyết động và đáp ứng lâm sàng.",
            "under_30": "Không cần chỉnh liều riêng; vẫn theo dõi tác dụng kéo dài nếu có suy đa cơ quan.",
        },
        "side_effects": [
            "Hạ huyết áp, tụt huyết áp khi bolus nhanh hoặc liều cao.",
            "Ức chế hô hấp, ngừng thở nếu tiêm nhanh/ liều cao.",
            "Đau tại chỗ tiêm.",
            "Propofol infusion syndrome (hiếm, thường khi truyền liều cao kéo dài): toan chuyển hóa, tăng CK, suy tim, suy thận.",
        ],
        "interactions": [
            "Thuốc an thần khác (benzodiazepine, opioid): tăng tác dụng ức chế TKTW và ức chế hô hấp.",
            "Thuốc hạ huyết áp, thuốc lợi tiểu: tăng nguy cơ tụt huyết áp.",
        ],
        "pregnancy": "B–C: thường dùng trong gây mê ngắn hạn; tránh trong an thần kéo dài thai kỳ nếu có lựa chọn khác.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiac": True, "metabolic": True},
            "icu_critical_care_only": True,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "SCCM ICU Sedation Guidelines",
            "ASA Practice Guidelines for Sedation and Analgesia",
            "PADIS Guidelines"
        ],
        # === 6 ENHANCED FIELDS CƠ BẢN ===
        "mechanism_of_action": (
            "Propofol là thuốc gây mê đường tĩnh mạch, tăng cường hoạt tính của GABA tại thụ thể GABA_A, "
            "làm tăng dòng chloride vào tế bào thần kinh, gây ưu phân cực màng và ức chế dẫn truyền thần kinh. "
            "Thuốc có khởi phát nhanh và hồi phục nhanh nhờ phân bố và chuyển hóa nhanh tại gan và mô ngoài gan."
        ),
        "monitoring": [
            "Huyết áp, nhịp tim, SpO2, tần số thở liên tục trong khi dùng.",
            "Mức độ an thần (RASS, Ramsay hoặc công cụ tương tự).",
            "Dấu hiệu propofol infusion syndrome nếu truyền liều cao kéo dài: toan chuyển hóa, tăng CK, suy tim, suy thận, tiêu cơ vân.",
        ],
        "precautions": [
            "Chỉ sử dụng khi có khả năng hỗ trợ hô hấp và hồi sức tim phổi đầy đủ.",
            "Giảm liều và titrate chậm ở bệnh nhân giảm thể tích, suy tim, người cao tuổi.",
            "Hạn chế truyền liều cao kéo dài (>4mg/kg/giờ >48 giờ) để giảm nguy cơ propofol infusion syndrome.",
        ],
        "pharmacokinetics": {
            "half_life": "Phân bố nhanh (2–4 phút), thải trừ pha cuối 3–12 giờ nhưng hồi phục lâm sàng nhanh.",
            "onset": "30–60 giây sau tiêm tĩnh mạch.",
            "duration": "5–10 phút sau một liều bolus; hồi phục nhanh khi ngừng truyền.",
            "protein_binding": "Khoảng 95–99%.",
            "clearance": "Chủ yếu chuyển hóa ở gan và mô ngoài gan thành chất không hoạt tính, thải qua thận.",
        },
        "storage": "Nhũ dịch propofol cần bảo quản ở 2–25°C, lắc nhẹ trước khi dùng; hủy bỏ phần còn lại sau 6–12 giờ tùy quy định để tránh nhiễm khuẩn.",
        "black_box_warnings": (
            "Chỉ dùng bởi bác sĩ có kinh nghiệm về gây mê/an thần và quản lý đường thở. "
            "Nguy cơ suy hô hấp, tụt huyết áp nặng, và hội chứng truyền propofol khi dùng liều cao kéo dài."
        ),
        # === 8 ENHANCED FIELDS TÙY CHỌN ===
        "drug_interactions": {
            "major": [
                {
                    "drug": "Các thuốc an thần khác (benzodiazepine, opioid mạnh)",
                    "mechanism": "Tác dụng hiệp đồng trên GABA và ức chế TKTW.",
                    "effect": "Tăng nguy cơ suy hô hấp và tụt huyết áp.",
                    "management": "Giảm liều từng thuốc, theo dõi sát hô hấp và huyết áp; chuẩn bị phương tiện hỗ trợ hô hấp.",
                }
            ],
            "moderate": [],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với propofol hoặc các thành phần trong tá dược.",
            ],
            "tương_đối": [
                "Suy tim nặng, giảm thể tích tuần hoàn chưa bù.",
                "Rối loạn chuyển hóa acid béo, thiếu hụt carnitine (nguy cơ propofol infusion syndrome).",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "Chưa phân loại rõ (thường xếp C)",
            "pregnancy_details": (
                "Thường dùng trong gây mê ngắn hạn ở thai phụ khi cần phẫu thuật; tránh an thần kéo dài nếu có lựa chọn khác."
            ),
            "lactation": {
                "safety": "Compatible/Caution",
                "details": "Propofol vào sữa rất ít; có thể cho bú lại vài giờ sau khi tỉnh hoàn toàn.",
                "recommendation": "Thường không cần ngừng cho bú sau gây mê ngắn bằng propofol.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thường không cần chỉnh liều rõ; chỉnh theo đáp ứng lâm sàng.",
            "moderate": "Thận trọng, có thể kéo dài thời gian tác dụng.",
            "severe": "Theo dõi sát thời gian hồi tỉnh và huyết động; cân nhắc liều thấp hơn.",
            "notes": "Propofol chuyển hóa chủ yếu qua gan nhưng còn chuyển hóa ngoài gan; suy gan không nhất thiết làm tích lũy quá mức.",
        },
        "overdose_management": {
            "symptoms": [
                "Suy hô hấp, ngừng thở.",
                "Tụt huyết áp sâu, trụy mạch.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng truyền thuốc ngay lập tức.",
                "Hỗ trợ hô hấp (mask, đặt nội khí quản, thở máy nếu cần).",
                "Truyền dịch, thuốc vận mạch để nâng huyết áp.",
            ],
            "monitoring": "Theo dõi huyết động, hô hấp và toan kiềm.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": "Thuốc có dạng nhũ dịch sẵn dùng, không pha loãng quá mức; tuân thủ hướng dẫn vô khuẩn.",
                "infusion_rate": "Bolus chậm 20–40mg mỗi 10 giây đến khi đạt hiệu quả; truyền duy trì bằng bơm tiêm điện.",
                "compatibility": [],
                "incompatibility": [
                    "Không trộn chung trong cùng đường truyền với máu hoặc nhũ dịch khác.",
                ],
                "notes": "Thay dây truyền và lọ thuốc theo khuyến cáo (thường không quá 12 giờ) để tránh nhiễm khuẩn.",
            },
        },
        "references": {
            "primary_sources": [
                "Society of Critical Care Medicine (SCCM) guidelines for ICU sedation and analgesia",
                "ASA Practice Guidelines for Sedation and Anesthesia",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
             "reversal_agents": {
             "available": False,
             "agents": []
         },
},

    "Midazolam (IV/ICU)": {
        "group": "Supportive - Benzodiazepine (IV Sedation/ICU)",
        "vietnamese_name": "Midazolam tiêm tĩnh mạch",
        "administration": ["IV"],
        "indications": [
            "An thần cho bệnh nhân thở máy trong ICU.",
            "Tiền mê và an thần trước thủ thuật/phẫu thuật.",
            "Kiểm soát cơn co giật trong một số trường hợp (khi không có đường khác).",
        ],
        "contraindications": [
            "Dị ứng với midazolam hoặc các benzodiazepine khác.",
            "Suy hô hấp nặng không được hỗ trợ.",
            "Sốc, tụt huyết áp nặng chưa kiểm soát.",
        ],
        "dosage": {
            "icu_sedation_loading": "0.01–0.05mg/kg IV bolus chậm, lặp lại nếu cần.",
            "icu_sedation_maintenance": "0.02–0.1mg/kg/giờ truyền tĩnh mạch, chỉnh theo thang điểm an thần.",
            "procedural_sedation": "0.02–0.07mg/kg IV chậm (thường 1–2mg), tiêm nhắc lại theo đáp ứng.",
            "notes": "Người cao tuổi, suy gan, suy hô hấp: dùng liều thấp hơn và tiêm thật chậm.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều ban đầu.",
            "30_60": "Có thể kéo dài thời gian tác dụng; chỉnh tốc độ truyền thấp hơn.",
            "under_30": "Thận trọng, giảm liều duy trì; theo dõi tích lũy chất chuyển hóa gây an thần kéo dài.",
        },
        "side_effects": [
            "Ức chế hô hấp, ngừng thở (đặc biệt khi dùng nhanh hoặc phối hợp opioid).",
            "Tụt huyết áp, đặc biệt ở bệnh nhân giảm thể tích hoặc dùng liều cao.",
            "Lú lẫn, mê sảng, đặc biệt khi dùng kéo dài trong ICU.",
            "Phản ứng nghịch đảo (kích động, bứt rứt) hiếm gặp.",
        ],
        "interactions": [
            "Opioid (fentanyl, morphine): tăng tác dụng ức chế TKTW và ức chế hô hấp.",
            "Thuốc ức chế CYP3A4 (azole, macrolid): tăng nồng độ midazolam, kéo dài an thần.",
            "Thuốc cảm ứng CYP3A4 (rifampin, phenytoin): giảm hiệu quả an thần.",
        ],
        "pregnancy": "D khi dùng kéo dài; có thể dùng liều đơn trong tiền mê khi cần thiết.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"respiratory": True, "neurologic": True},
            "icu_critical_care_only": True,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "SCCM ICU Sedation Guidelines",
            "ASA Practice Guidelines for Sedation and Analgesia",
            "PADIS Guidelines"
        ],
        "mechanism_of_action": (
            "Midazolam là benzodiazepine, gắn vào vị trí đặc hiệu trên thụ thể GABA_A, "
            "tăng tần suất mở kênh chloride khi GABA gắn, làm tăng ức chế sau synap. "
            "Tác dụng: an thần, giải lo âu, gây ngủ, chống co giật, giãn cơ trung ương."
        ),
        "monitoring": [
            "Huyết áp, nhịp tim, SpO2, tần số thở liên tục.",
            "Mức độ an thần (RASS, Ramsay).",
            "Dấu hiệu mê sảng, đặc biệt khi dùng kéo dài.",
        ],
        "precautions": [
            "Luôn chuẩn bị sẵn phương tiện hỗ trợ hô hấp và thuốc đảo ngược (flumazenil) trong môi trường thủ thuật.",
            "Giảm liều ở người cao tuổi, suy gan, suy hô hấp, suy thận.",
            "Hạn chế dùng kéo dài liều cao trong ICU do nguy cơ mê sảng và tích lũy.",
        ],
        "pharmacokinetics": {
            "half_life": "2–6 giờ (kéo dài ở người cao tuổi, suy gan, suy thận).",
            "onset": "1–5 phút sau tiêm IV.",
            "duration": "15–60 phút sau liều đơn; có thể kéo dài khi truyền liên tục.",
            "protein_binding": "Khoảng 95%.",
            "clearance": "Chuyển hóa qua CYP3A4 ở gan thành chất chuyển hóa có hoạt tính, thải qua thận.",
        },
        "storage": "Bảo quản ở 20–25°C, tránh ánh sáng; không trộn chung với dung dịch kiềm mạnh.",
        "black_box_warnings": (
            "Nguy cơ ức chế hô hấp, tụt huyết áp, đặc biệt khi phối hợp với opioid và các thuốc an thần khác; "
            "chỉ dùng ở nơi có sẵn phương tiện hồi sức."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Opioid mạnh (fentanyl, morphine, hydromorphone)",
                    "mechanism": "Hiệp đồng ức chế TKTW và trung tâm hô hấp.",
                    "effect": "Tăng nguy cơ suy hô hấp, ngừng thở.",
                    "management": "Dùng liều thấp từng thuốc, tăng dần; theo dõi sát và chuẩn bị hỗ trợ hô hấp.",
                },
                {
                    "drug": "Azole (fluconazole, voriconazole), macrolid (erythromycin, clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, làm giảm chuyển hóa midazolam.",
                    "effect": "Kéo dài và tăng mức độ an thần.",
                    "management": "Giảm liều midazolam và theo dõi tác dụng kéo dài.",
                },
            ],
            "moderate": [
                {
                    "drug": "Rifampin, phenytoin, carbamazepine",
                    "mechanism": "Cảm ứng CYP3A4.",
                    "effect": "Giảm hiệu lực an thần của midazolam.",
                    "management": "Có thể cần liều cao hơn; theo dõi đáp ứng.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn với benzodiazepine.",
            ],
            "tương_đối": [
                "Suy hô hấp mạn (COPD nặng) khi không có hỗ trợ hô hấp.",
                "Suy gan, suy thận nặng.",
                "Người cao tuổi, nguy cơ mê sảng cao.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "D (khi dùng kéo dài); C cho liều đơn.",
            "pregnancy_details": (
                "Có thể sử dụng liều đơn trong tiền mê khi lợi ích vượt trội nguy cơ; tránh dùng kéo dài trong thai kỳ."
            ),
            "lactation": {
                "safety": "Compatible/Caution",
                "details": "Midazolam bài tiết vào sữa ở lượng nhỏ; có thể cho bú lại sau vài giờ khi mẹ tỉnh táo.",
                "recommendation": "Thường không cần ngừng cho bú sau liều đơn; thận trọng nếu dùng kéo dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Giảm liều và tăng khoảng cách; theo dõi thời gian tỉnh.",
            "moderate": "Thận trọng, có thể tích lũy; ưu tiên thuốc khác nếu được.",
            "severe": "Tránh dùng kéo dài; nếu bắt buộc, dùng liều rất thấp và theo dõi sát.",
            "notes": "Suy gan làm giảm chuyển hóa midazolam và kéo dài an thần.",
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp, ngừng thở.",
                "Hạ huyết áp, ngủ gà sâu.",
            ],
            "antidote": "Flumazenil – thuốc đối kháng benzodiazepine đặc hiệu.",
            "treatment": [
                "Đảm bảo đường thở, hỗ trợ hô hấp.",
                "Dùng flumazenil liều khởi đầu 0.2mg IV trong 15 giây, có thể nhắc lại 0.2mg mỗi phút (tối đa 1mg) tùy đáp ứng.",
                "Theo dõi tái an thần do thời gian bán thải midazolam dài hơn flumazenil.",
            ],
            "monitoring": "Theo dõi nhịp thở, SpO2, huyết áp, ý thức.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Flumazenil",
                    "indication": "Đảo ngược tác dụng benzodiazepine quá mức (bao gồm midazolam).",
                    "dose": "0.2mg IV trong 15 giây, nhắc lại 0.2mg mỗi phút đến tối đa 1mg; có thể truyền duy trì nếu cần.",
                    "mechanism": "Đối kháng cạnh tranh tại vị trí gắn benzodiazepine trên thụ thể GABA_A.",
                    "notes": "Thận trọng ở bệnh nhân lệ thuộc benzodiazepine mạn tính (nguy cơ co giật).",
                }
            ],
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Dung dịch tiêm sẵn dùng hoặc pha loãng trong NaCl 0.9%/D5W theo hướng dẫn.",
                "infusion_rate": "Truyền bằng bơm tiêm điện; tăng giảm tốc độ theo thang điểm an thần.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Tiêm bolus chậm trong ít nhất 2 phút để giảm nguy cơ tụt huyết áp và ức chế hô hấp.",
            },
        },
        "references": {
            "primary_sources": [
                "SCCM guidelines for ICU sedation and analgesia",
                "ASA Practice Guidelines for Sedation and Anesthesia",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
    },

    "Ketamine": {
        "group": "Supportive - Dissociative anesthetic/analgesic (ICU/Procedural)",
        "vietnamese_name": "Ketamine",
        "administration": ["IV", "IM"],
        "indications": [
            "Khởi mê nhanh trong gây mê/tình huống cấp cứu (RSI) khi cần duy trì huyết động.",
            "An thần/giảm đau liều thấp cho thủ thuật ngắn hoặc giảm đau trong ICU.",
            "Hỗ trợ giảm đau khi đau khó kiểm soát hoặc giảm opioid, đặc biệt trong đau thần kinh.",
            "Khởi mê hoặc an thần ở bệnh nhân hen co thắt/phản vệ do tác dụng giãn phế quản.",
        ],
        "contraindications": [
            "Dị ứng với ketamine.",
            "Tăng huyết áp nặng, phình tách động mạch chủ hoặc bệnh mạch vành không ổn định.",
            "Tăng áp lực nội sọ/nhãn cầu rõ rệt (thận trọng, không phải chống chỉ định tuyệt đối).",
        ],
        "dosage": {
            "induction_iv": "1–2mg/kg IV bolus chậm trong 30–60 giây (người lớn).",
            "induction_im": "4–10mg/kg IM khi không có đường IV.",
            "procedural_sedation_analgesia_iv": "0.25–0.5mg/kg IV bolus, có thể nhắc lại; truyền duy trì 0.1–0.5mg/kg/giờ nếu cần.",
            "analgesia_low_dose": "Bolus 0.1–0.3mg/kg IV, sau đó truyền 0.1–0.3mg/kg/giờ để giảm đau/tiết giảm opioid.",
            "status_asthmaticus_adjunct": "0.5–1mg/kg IV bolus, có thể truyền 0.5–2mcg/kg/phút (0.03–0.12mg/kg/giờ) nếu cần.",
            "notes": "Tiêm bolus chậm để hạn chế nhịp tim/huyết áp tăng mạnh; cân nhắc phối hợp benzodiazepine liều thấp để giảm ảo giác.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Thường không cần chỉnh liều đáng kể; theo dõi kéo dài tác dụng.",
            "under_30": "Không cần chỉnh liều riêng; theo dõi tích lũy nếu suy đa cơ quan.",
        },
        "side_effects": [
            "Tăng huyết áp, nhịp tim nhanh.",
            "Tăng tiết nước bọt, tăng trương lực cơ/giật rung cơ nhẹ.",
            "Ảo giác, mê sảng khi hồi tỉnh (emergence reactions).",
            "Buồn nôn/nôn, chóng mặt.",
        ],
        "interactions": [
            "Thuốc cường giao cảm (epinephrine, ephedrine): tăng tác dụng tim mạch.",
            "Benzodiazepine/propofol/opioid: có thể giảm ảo giác và cải thiện an thần nhưng tăng nguy cơ ức chế hô hấp.",
        ],
        "pregnancy": "B–C: có thể dùng khi lợi ích vượt trội, tránh lạm dụng; thận trọng ở quý 1.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiac": True, "neurologic": True},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "SCCM ICU Sedation Guidelines",
            "ASA Practice Guidelines for Sedation and Anesthesia",
            "ACEP Clinical Policy for Procedural Sedation"
        ],
        "mechanism_of_action": (
            "Ketamine là thuốc gây mê phân ly, đối kháng thụ thể NMDA, giảm dẫn truyền glutamate "
            "và hoạt hóa nhẹ thụ thể opioid/monoamine, tạo tác dụng gây mê, giảm đau và amnestic. "
            "Bảo tồn phản xạ đường thở và thường duy trì huyết áp/nhịp tim do kích thích giao cảm."
        ),
        "monitoring": [
            "Huyết áp, nhịp tim, SpO2, nhịp thở trong quá trình dùng.",
            "Mức độ an thần và dấu hiệu ảo giác/agitation khi hồi tỉnh.",
            "Tiết dịch đường hô hấp; chuẩn bị hút đờm nếu cần.",
        ],
        "precautions": [
            "Thận trọng ở bệnh nhân bệnh mạch vành, tăng huyết áp nặng, tăng ICP/IOP.",
            "Dùng thêm benzodiazepine liều thấp có thể giảm phản ứng mê sảng khi hồi tỉnh.",
            "Chuẩn bị chống tăng tiết (atropine/glycopyrrolate) nếu tiết nhiều.",
        ],
        "pharmacokinetics": {
            "half_life": "2–3 giờ; tác dụng lâm sàng ngắn do tái phân bố nhanh.",
            "onset": "30–60 giây IV; 3–5 phút IM.",
            "duration": "5–15 phút sau bolus IV; lâu hơn với IM hoặc truyền.",
            "protein_binding": "Khoảng 20–50%.",
            "clearance": "Chuyển hóa ở gan qua CYP2B6/3A4/2C9 thành norketamine, thải qua thận.",
        },
        "storage": "Bảo quản ở 20–25°C, tránh ánh sáng; dung dịch dùng trực tiếp không cần bảo quản lạnh.",
        "black_box_warnings": (
            "Nguy cơ tăng huyết áp/nhịp tim và phản ứng mê sảng khi hồi tỉnh; "
            "chỉ dùng ở nơi có khả năng hồi sức và giám sát thích hợp."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc cường giao cảm (epinephrine, ephedrine)",
                    "mechanism": "Hiệp đồng kích thích giao cảm.",
                    "effect": "Tăng huyết áp/nhịp tim quá mức.",
                    "management": "Theo dõi huyết động; giảm liều hoặc tránh phối hợp liều cao.",
                }
            ],
            "moderate": [
                {
                    "drug": "Benzodiazepine hoặc propofol",
                    "mechanism": "Tăng an thần/ức chế TKTW; có thể giảm ảo giác.",
                    "effect": "Có thể ức chế hô hấp khi phối hợp; giảm nhu cầu ketamine.",
                    "management": "Giảm liều từng thuốc, theo dõi hô hấp/huyết động.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn với ketamine.",
            ],
            "tương_đối": [
                "Tăng huyết áp nặng hoặc bệnh mạch vành không ổn định.",
                "Tăng áp lực nội sọ/nhãn cầu.",
                "Tiền sử phản ứng mê sảng nặng.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B–C",
            "pregnancy_details": (
                "Có thể cân nhắc khi cần gây mê nhanh, ưu tiên tránh lạm dụng trong thai kỳ sớm."
            ),
            "lactation": {
                "safety": "Compatible/Caution",
                "details": "Dữ liệu hạn chế, bài tiết vào sữa ít; có thể cho bú lại khi mẹ tỉnh táo.",
                "recommendation": "Theo dõi trẻ nếu dùng liều cao/lặp lại.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thường không cần chỉnh liều đáng kể.",
            "moderate": "Thận trọng, có thể kéo dài tác dụng; giảm liều truyền.",
            "severe": "Giảm liều và theo dõi sát do nguy cơ tích lũy.",
            "notes": "Chuyển hóa ở gan; suy gan có thể kéo dài thời gian bán thải.",
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp (hiếm, thường khi phối hợp thuốc khác).",
                "Tăng huyết áp/nhịp tim quá mức hoặc loạn nhịp.",
                "Kích động, ảo giác mạnh.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Đảm bảo đường thở, hỗ trợ hô hấp nếu cần.",
                "Kiểm soát huyết áp/tim mạch; dùng benzodiazepine nếu kích động/ảo giác.",
                "Theo dõi ECG, huyết áp liên tục.",
            ],
            "monitoring": "Giám sát huyết động và hô hấp cho đến khi hồi phục.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": "Dung dịch có sẵn; có thể pha loãng trong NaCl 0.9%/D5W để truyền.",
                "infusion_rate": "Truyền bằng bơm tiêm điện 0.1–0.5mg/kg/giờ cho giảm đau/an thần nhẹ.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Tiêm bolus chậm; hút đờm/anticholinergic nếu tăng tiết nhiều.",
            },
            "im": {
                "reconstitution": "Dung dịch sẵn dùng; tiêm bắp sâu.",
                "notes": "Khởi phát chậm hơn IV; phù hợp khi khó thiết lập đường IV.",
            },
        },
        "references": {
            "primary_sources": [
                "SCCM guidelines for ICU sedation and analgesia",
                "ACEP clinical policy for procedural sedation",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
              "reversal_agents": {
              "available": False,
              "agents": []
          },
},

    "Dexmedetomidine": {
        "group": "Supportive - Alpha-2 agonist sedative (ICU/Procedural)",
        "vietnamese_name": "Dexmedetomidine",
        "administration": ["IV"],
        "indications": [
            "An thần cho bệnh nhân thở máy trong ICU (tỉnh táo, hợp tác).",
            "An thần cho thủ thuật không đặt nội khí quản (awake sedation).",
            "Giảm liều opioid/benzodiazepine, hỗ trợ kiểm soát mê sảng.",
        ],
        "contraindications": [
            "Dị ứng với dexmedetomidine.",
            "Block tim độ 2–3 hoặc rối loạn dẫn truyền nặng chưa đặt máy tạo nhịp.",
            "Huyết áp thấp, nhịp chậm triệu chứng nặng.",
        ],
        "dosage": {
            "loading_optional": "1mcg/kg truyền IV trong 10 phút (có thể bỏ qua nếu huyết động không ổn).",
            "maintenance": "0.2–1.4mcg/kg/giờ truyền liên tục, chỉnh theo thang điểm an thần.",
            "procedural_sedation": "0.5–1mcg/kg bolus 10 phút, sau đó truyền 0.2–1mcg/kg/giờ.",
            "notes": "Bỏ liều bolus nếu nguy cơ tụt huyết áp/nhịp chậm; tăng giảm tốc độ mỗi 30–60 phút.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; theo dõi huyết động.",
            "under_30": "Không cần chỉnh liều; tác dụng không thay đổi đáng kể.",
        },
        "side_effects": [
            "Nhịp chậm, block tim, ngừng xoang thoáng qua.",
            "Hạ huyết áp (đặc biệt khi bolus).",
            "Tăng huyết áp thoáng qua khi bắt đầu bolus.",
            "Khô miệng, buồn nôn.",
        ],
        "interactions": [
            "Thuốc chẹn beta hoặc chẹn kênh calcium: tăng nguy cơ nhịp chậm/hạ huyết áp.",
            "Thuốc an thần khác (opioid, propofol, benzo): hiệp đồng an thần, có thể giảm nhu cầu opioid.",
        ],
        "pregnancy": "C: thận trọng, chỉ dùng khi lợi ích vượt trội.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"cardiac": True},
            "icu_critical_care_only": True,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "SCCM ICU Sedation Guidelines",
            "ASA Practice Guidelines for Sedation and Analgesia",
            "PADIS Guidelines"
        ],
        "mechanism_of_action": (
            "Dexmedetomidine là chất chủ vận chọn lọc alpha-2 adrenergic trung ương, "
            "giảm phóng thích norepinephrine, gây an thần kiểu ngủ sinh lý, giảm lo âu và giảm đau nhẹ, "
            "với ít ức chế hô hấp."
        ),
        "monitoring": [
            "Huyết áp, nhịp tim liên tục khi titrate.",
            "Mức độ an thần (RASS).",
            "Dấu hiệu giảm lưu lượng tim ở bệnh nhân suy tim hoặc giảm thể tích.",
        ],
        "precautions": [
            "Tránh bolus nhanh; ưu tiên khởi đầu truyền thấp để hạn chế hạ huyết áp/nhịp chậm.",
            "Thận trọng ở bệnh nhân block tim, suy nút xoang, suy thất phải hoặc giảm thể tích tuần hoàn.",
            "Ngừng truyền từ từ nếu dùng kéo dài để hạn chế rebound tăng huyết áp/nhịp nhanh.",
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 2 giờ (kéo dài hơn khi truyền dài ngày).",
            "onset": "5–10 phút sau bolus/khởi truyền.",
            "duration": "Tác dụng hết trong 1–2 giờ sau ngừng truyền, có thể lâu hơn nếu truyền kéo dài.",
            "protein_binding": "Khoảng 94%.",
            "clearance": "Chuyển hóa ở gan (UGT, CYP2A6) thành chất không hoạt tính, thải qua thận.",
        },
        "storage": "Dung dịch/ống truyền sẵn dùng bảo quản 20–25°C, tránh ánh sáng; pha loãng trong NaCl 0.9% trước khi truyền.",
        "black_box_warnings": (
            "Nguy cơ nhịp chậm và hạ huyết áp đáng kể, đặc biệt khi bolus hoặc ở bệnh nhân giảm thể tích; "
            "cần giám sát huyết động liên tục."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Chẹn beta hoặc chẹn kênh calcium (ví dụ metoprolol, diltiazem)",
                    "mechanism": "Hiệp đồng giảm nhịp tim và co bóp.",
                    "effect": "Tăng nguy cơ nhịp chậm/hạ huyết áp.",
                    "management": "Giảm liều, theo dõi huyết động chặt chẽ; ngừng bolus.",
                }
            ],
            "moderate": [
                {
                    "drug": "Opioid/propofol/benzodiazepine",
                    "mechanism": "Hiệp đồng an thần/giảm đau.",
                    "effect": "Có thể ức chế hô hấp nhẹ và tụt huyết áp.",
                    "management": "Giảm liều từng thuốc, titrate theo đáp ứng.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn với dexmedetomidine.",
            ],
            "tương_đối": [
                "Block tim độ 2–3 không có máy tạo nhịp.",
                "Nhịp chậm có triệu chứng, huyết áp thấp.",
                "Giảm thể tích tuần hoàn chưa bù.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế; chỉ dùng khi lợi ích vượt trội.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa; theo dõi trẻ nếu mẹ dùng kéo dài.",
                "recommendation": "Cân nhắc ngừng/hoãn cho bú trong thời gian truyền dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Có thể không cần chỉnh, nhưng nên bắt đầu liều thấp.",
            "moderate": "Giảm liều duy trì; tăng khoảng điều chỉnh.",
            "severe": "Giảm đáng kể tốc độ truyền và theo dõi sát huyết động.",
            "notes": "Giảm thanh thải đáng kể ở suy gan; dễ tích lũy khi truyền dài.",
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp chậm sâu, block tim.",
                "Hạ huyết áp hoặc tăng huyết áp thoáng qua (do alpha-2 ngoại biên).",
                "Buồn ngủ sâu, hiếm khi ức chế hô hấp đáng kể.",
            ],
            "antidote": "Không có antidote đặc hiệu cho người (atipamezole dùng cho thú y).",
            "treatment": [
                "Ngừng truyền ngay lập tức.",
                "Hồi sức dịch, thuốc vận mạch nếu hạ huyết áp; atropine/glycopyrrolate nếu nhịp chậm có triệu chứng.",
                "Theo dõi ECG, huyết áp liên tục.",
            ],
            "monitoring": "Giám sát huyết động cho đến khi thuốc thải trừ.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng nồng độ chuẩn 4mcg/mL trong NaCl 0.9% trước khi truyền.",
                "infusion_rate": "Khởi đầu 0.2–0.4mcg/kg/giờ, tăng dần tối đa 1.4mcg/kg/giờ theo đáp ứng.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Tránh bolus nhanh; chỉnh tốc độ mỗi 30–60 phút.",
            },
        },
        "references": {
            "primary_sources": [
                "SCCM guidelines for ICU sedation and analgesia",
                "FDA/label recommendations for dexmedetomidine (Precedex)",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
              "reversal_agents": {
              "available": False,
              "agents": []
          },
},

    "Etomidate": {
        "group": "Supportive - IV anesthetic for induction (hemodynamic stability)",
        "vietnamese_name": "Etomidate",
        "administration": ["IV"],
        "indications": [
            "Khởi mê nhanh (RSI) hoặc khởi mê ở bệnh nhân huyết động không ổn định.",
            "Khởi mê ngắn cho thủ thuật cần gây mê tĩnh mạch nhanh.",
        ],
        "contraindications": [
            "Dị ứng với etomidate hoặc propylene glycol.",
            "Tiền sử suy thượng thận nặng hoặc đang dùng ức chế tổng hợp steroid (thận trọng).",
        ],
        "dosage": {
            "induction_rsi": "0.2–0.3mg/kg IV bolus trong 30–60 giây.",
            "procedural_sedation_short": "0.1–0.2mg/kg IV bolus (khởi mê ngắn), có thể nhắc lại liều nhỏ 0.05mg/kg nếu cần.",
            "infusion_rare": "5–20mcg/kg/phút (0.3–1.2mg/kg/giờ) hiếm dùng do nguy cơ ức chế thượng thận.",
            "notes": "Tiêm cùng lidocain 0.5–1mL 1% có thể giảm đau tại chỗ tiêm và giảm myoclonus.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều; theo dõi kéo dài tác dụng.",
            "under_30": "Không cần chỉnh liều riêng; theo dõi huyết động.",
        },
        "side_effects": [
            "Myoclonus thoáng qua.",
            "Buồn nôn/nôn.",
            "Đau tại chỗ tiêm (do propylene glycol).",
            "Ức chế tổng hợp cortisol tạm thời (6–24 giờ) sau liều bolus.",
        ],
        "interactions": [
            "Thuốc an thần khác: hiệp đồng ức chế TKTW.",
            "Thuốc ức chế tổng hợp steroid (ketoconazole): có thể tăng ức chế thượng thận.",
        ],
        "pregnancy": "C: cân nhắc khi lợi ích vượt trội; thường tránh truyền kéo dài.",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"endocrine": True},
            "icu_critical_care_only": True,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "SCCM ICU Sedation Guidelines",
            "ASA Practice Guidelines for Sedation and Analgesia",
            "Difficult Airway Guidelines"
        ],
        "mechanism_of_action": (
            "Etomidate tăng cường dẫn truyền GABA tại thụ thể GABA_A, gây gây mê nhanh với tối thiểu ảnh hưởng đến huyết động; "
            "không có tác dụng giảm đau đáng kể."
        ),
        "monitoring": [
            "Huyết áp, nhịp tim, SpO2 trong quá trình khởi mê.",
            "Đánh giá dấu hiệu suy thượng thận (hiếm khi cần sau liều đơn).",
        ],
        "precautions": [
            "Tránh truyền kéo dài hoặc liều lặp lại nhiều lần do nguy cơ ức chế thượng thận.",
            "Thận trọng ở bệnh nhân sepsis nặng hoặc phụ thuộc steroid.",
            "Có thể gây myoclonus; premedication bằng opioid/benzodiazepine hoặc lidocain tĩnh mạch giúp giảm.",
        ],
        "pharmacokinetics": {
            "half_life": "2–5 giờ; tác dụng lâm sàng ngắn do tái phân bố nhanh.",
            "onset": "30–60 giây sau tiêm IV.",
            "duration": "3–10 phút sau bolus.",
            "protein_binding": "Khoảng 75%.",
            "clearance": "Thủy phân bởi esterase ở gan và huyết tương, thải qua thận/bile.",
        },
        "storage": "Bảo quản ở 20–25°C; dung dịch chứa propylene glycol có thể kết tinh ở nhiệt độ thấp, lắc nhẹ trước khi dùng.",
        "black_box_warnings": (
            "Không dùng truyền kéo dài do ức chế tổng hợp cortisol; chỉ dùng bolus/ngắn hạn và theo dõi huyết động."
        ),
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Ketoconazole hoặc thuốc ức chế steroidogenesis",
                    "mechanism": "Hiệp đồng ức chế tổng hợp cortisol.",
                    "effect": "Tăng nguy cơ suy thượng thận.",
                    "management": "Tránh phối hợp nếu có lựa chọn khác; theo dõi huyết áp/điện giải.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Quá mẫn với etomidate hoặc tá dược propylene glycol.",
            ],
            "tương_đối": [
                "Sepsis nặng hoặc suy thượng thận đang điều trị steroid.",
                "Bệnh nhân phụ thuộc steroid lâu dài.",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế; có thể dùng khởi mê ngắn khi cần thiết.",
            "lactation": {
                "safety": "Compatible/Caution",
                "details": "Lượng vào sữa thấp; có thể cho bú lại khi mẹ tỉnh táo.",
                "recommendation": "Theo dõi trẻ nếu mẹ dùng lặp lại hoặc truyền (hiếm).",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều rõ rệt.",
            "moderate": "Thận trọng; có thể kéo dài tác dụng.",
            "severe": "Theo dõi hồi phục; điều chỉnh liều nếu cần.",
            "notes": "Etomidate chuyển hóa qua esterase; suy gan nặng có thể giảm thanh thải.",
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp, tụt huyết áp (hiếm, nhẹ hơn propofol).",
                "Kéo dài hôn mê, myoclonus.",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Hỗ trợ đường thở và thông khí.",
                "Hồi sức dịch/thuốc vận mạch nếu tụt huyết áp.",
                "Theo dõi điện giải và cortisol nếu dùng lặp lại.",
            ],
            "monitoring": "Theo dõi hô hấp và huyết động cho đến khi tỉnh hoàn toàn.",
        },
        "reversal_agents": None,
        "administration_instructions": {
            "iv": {
                "reconstitution": "Dung dịch sẵn dùng, tiêm tĩnh mạch chậm trong 30–60 giây.",
                "infusion_rate": "Không khuyến cáo truyền kéo dài; nếu phải dùng, ≤20mcg/kg/phút với giám sát chặt.",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Có thể phối hợp lidocain IV để giảm đau tiêm và myoclonus.",
            },
        },
        "references": {
            "primary_sources": [
                "SCCM guidelines for ICU sedation and analgesia",
                "Advanced airway/RSI references for etomidate dosing",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High – guideline-based",
        },
              "reversal_agents": {
              "available": False,
              "agents": []
          },
},
    
    "Thiopental": {
        "group": "Supportive - Barbiturate Anesthetic (ICU)",
        "vietnamese_name": "Thiopental, Thiopentone, Pentothal",
        "administration": ["IV"],
        "indications": [
            "Gây mê khởi đầu (induction of anesthesia)",
            "Barbiturate coma trong tăng áp lực nội sọ (intracranial hypertension)",
            "Status epilepticus kháng trị",
            "Bảo vệ não trong phẫu thuật tim (cerebral protection)"
        ],
        "contraindications": [
            "Dị ứng thiopental hoặc barbiturates",
            "Porphyria (bệnh porphyria) - chống chỉ định tuyệt đối",
            "Suy hô hấp nặng không có hỗ trợ thông khí",
            "Sốc nặng (shock)"
        ],
        "dosage": {
            "adult_induction": "3-5 mg/kg IV bolus (thường 4 mg/kg)",
            "adult_barbiturate_coma_loading": "10-20 mg/kg IV (truyền trong 30-60 phút)",
            "adult_barbiturate_coma_maintenance": "1-3 mg/kg/giờ IV infusion",
            "adult_status_epilepticus": "10-20 mg/kg IV bolus, sau đó 1-3 mg/kg/giờ",
            "pediatric_induction": "3-5 mg/kg IV bolus",
            "notes": "Tác dụng nhanh (30-60 giây), ngắn (5-10 phút sau liều đơn). Barbiturate coma: chỉ dùng khi các biện pháp khác thất bại, cần theo dõi ICP, EEG."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng (có thể tích lũy)",
            "under_30": "Thận trọng, giảm liều (tích lũy, tác dụng kéo dài)"
        },
        "side_effects": [
            "Ức chế hô hấp nặng (phải hỗ trợ thông khí)",
            "Hạ huyết áp (do giãn mạch, ức chế tim)",
            "Ức chế tim (giảm cung lượng tim)",
            "Co thắt phế quản (hiếm)",
            "Phản ứng dị ứng (hiếm nhưng nguy hiểm)",
            "Tích lũy ở mô mỡ (tác dụng kéo dài khi dùng liều cao, kéo dài)"
        ],
        "interactions": [
            "Thuốc ức chế TKTW: tăng tác dụng",
            "Thuốc hạ huyết áp: tăng nguy cơ hạ huyết áp",
            "Warfarin: tăng tác dụng (ức chế chuyển hóa)"
        ],
        "pregnancy": "C - Thận trọng trong thai kỳ",
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {"respiratory": True, "cardiac": True, "neurologic": True},
            "icu_critical_care_only": True,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "SCCM ICU Sedation Guidelines",
            "ASA Practice Guidelines for Sedation and Analgesia",
            "Brain Trauma Foundation Guidelines (ICP management)"
        ],
        "mechanism_of_action": "Thiopental là barbiturate tác dụng ngắn. Tăng cường hoạt tính của GABA tại thụ thể GABA_A, làm tăng dòng chloride vào tế bào thần kinh, gây ưu phân cực màng và ức chế dẫn truyền thần kinh. Thiopental có khởi phát rất nhanh (30-60 giây) do phân bố nhanh vào não, nhưng tác dụng ngắn (5-10 phút) do phân bố lại vào mô mỡ. Khi dùng liều cao, kéo dài (barbiturate coma), thuốc tích lũy ở mô mỡ và có thể có tác dụng kéo dài. Thiopental làm giảm chuyển hóa não, giảm lưu lượng máu não, giảm áp lực nội sọ (ICP) - có lợi trong tăng áp lực nội sọ.",
        "monitoring": [
            "Huyết áp liên tục (arterial line nếu có thể)",
            "Nhịp tim và ECG",
            "Hô hấp (phải hỗ trợ thông khí)",
            "Áp lực nội sọ (ICP) - nếu dùng cho barbiturate coma",
            "EEG (nếu dùng cho barbiturate coma - mục tiêu burst suppression)",
            "Nồng độ thiopental trong máu (nếu có thể)",
            "Chức năng gan, thận"
        ],
        "precautions": [
            "PHẢI hỗ trợ thông khí (bệnh nhân không thể thở tự nhiên)",
            "TUYỆT ĐỐI KHÔNG dùng ở bệnh nhân porphyria (có thể gây cơn porphyria nặng, tử vong)",
            "Thận trọng ở sốc (hạ huyết áp nặng)",
            "Thận trọng ở suy tim (ức chế tim)",
            "Thận trọng ở suy gan, suy thận (tích lũy, tác dụng kéo dài)",
            "Barbiturate coma: chỉ dùng khi các biện pháp khác thất bại, cần theo dõi ICP, EEG",
            "Mục tiêu barbiturate coma: burst suppression trên EEG",
            "Có thể gây phản ứng dị ứng nặng (hiếm)"
        ],
        "pharmacokinetics": {
            "half_life": "10-12 giờ (sau phân bố lại), có thể dài hơn khi dùng liều cao, kéo dài",
            "onset": "30-60 giây (rất nhanh)",
            "duration": "5-10 phút (liều đơn), kéo dài khi dùng liều cao, kéo dài",
            "protein_binding": "80-85%",
            "clearance": "Gan (chuyển hóa chậm), tích lũy ở mô mỡ"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch đã pha: ổn định trong 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": "TUYỆT ĐỐI KHÔNG dùng ở bệnh nhân porphyria - có thể gây cơn porphyria nặng, tử vong. Ức chế hô hấp nặng - PHẢI hỗ trợ thông khí.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Thiopental ức chế CYP2C9, giảm chuyển hóa warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Giảm liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế TKTW (benzodiazepines, opioids, propofol)",
                    "mechanism": "Tác dụng hiệp đồng ức chế TKTW",
                    "effect": "Tăng ức chế hô hấp, hạ huyết áp",
                    "management": "Thận trọng. Giảm liều các thuốc. Theo dõi hô hấp, huyết áp chặt chẽ."
                },
                {
                    "drug": "Thuốc hạ huyết áp",
                    "mechanism": "Tác dụng hiệp đồng giãn mạch",
                    "effect": "Tăng nguy cơ hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng thiopental hoặc barbiturates",
                "Porphyria (bệnh porphyria) - chống chỉ định tuyệt đối, có thể gây cơn porphyria nặng, tử vong",
                "Suy hô hấp nặng không có hỗ trợ thông khí"
            ],
            "tương_đối": [
                "Sốc nặng - tăng nguy cơ hạ huyết áp",
                "Suy tim - ức chế tim",
                "Suy gan nặng - tích lũy, tác dụng kéo dài",
                "Suy thận nặng - tích lũy, tác dụng kéo dài",
                "Bệnh nhân cao tuổi - tăng nhạy cảm, tác dụng kéo dài"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Thiopental là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Thiopental có thể qua nhau thai. Được sử dụng trong gây mê sản khoa và có vẻ an toàn. Trong cấp cứu, lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết thiopental có bài tiết vào sữa mẹ hay không. Thời gian bán thải 10-12 giờ, protein binding 80-85%. Có thể bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (chuyển hóa ở gan)",
            "severe": "Thận trọng, giảm liều (tích lũy, tác dụng kéo dài)",
            "notes": "Thiopental chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nồng độ và kéo dài tác dụng. Giảm liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (ngừng thở)",
                "Hạ huyết áp nặng",
                "Ức chế tim (giảm cung lượng tim)",
                "Hôn mê sâu",
                "Tích lũy ở mô mỡ (tác dụng kéo dài)"
            ],
            "antidote": "Không có antidote đặc hiệu. Hỗ trợ thông khí và huyết động.",
            "treatment": [
                "Hỗ trợ thông khí: Đặt nội khí quản, thở máy cho đến khi hồi phục",
                "Hỗ trợ huyết động:",
                "  - Bù dịch (NS, LR) nếu chưa đủ",
                "  - Vasopressor (norepinephrine, epinephrine) nếu hạ huyết áp nặng",
                "  - Inotrope (dobutamine, milrinone) nếu ức chế tim",
                "Theo dõi: Huyết áp, nhịp tim, ECG, hô hấp liên tục",
                "Nếu tích lũy (dùng liều cao, kéo dài):",
                "  - Hỗ trợ thông khí và huyết động cho đến khi hồi phục (có thể >24 giờ)",
                "  - Có thể cần lọc máu (hemodialysis) nếu tích lũy nặng"
            ],
            "monitoring": "Theo dõi huyết áp, nhịp tim, ECG, hô hấp liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có tích lũy (dùng liều cao, kéo dài)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Hỗ trợ thông khí và huyết động cho đến khi hồi phục."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha bột: 500mg-1g trong 20-40ml NS = 25mg/ml. Hoặc dùng dung dịch đã pha sẵn.",
                "infusion_rate": "Induction: 3-5 mg/kg IV bolus chậm (30-60 giây). Barbiturate coma: Loading 10-20 mg/kg IV truyền trong 30-60 phút, sau đó 1-3 mg/kg/giờ IV infusion. Status epilepticus: 10-20 mg/kg IV bolus, sau đó 1-3 mg/kg/giờ.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."
                ],
                "notes": "QUAN TRỌNG: 1) PHẢI hỗ trợ thông khí (bệnh nhân không thể thở tự nhiên), 2) TUYỆT ĐỐI KHÔNG dùng ở bệnh nhân porphyria, 3) Thận trọng ở sốc (hạ huyết áp nặng), 4) Barbiturate coma: chỉ dùng khi các biện pháp khác thất bại, theo dõi ICP, EEG, 5) Mục tiêu barbiturate coma: burst suppression trên EEG."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Thiopental (Pentothal)",
                "ACLS Guidelines 2020 - American Heart Association",
                "Intracranial Hypertension Guidelines",
                "UpToDate - Thiopental: Drug Information",
                "Anesthesia Guidelines - Barbiturate Anesthetics",
                "Medscape - Thiopental Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACLS guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
}

__all__ = ["SEDATIVES_ANESTHETICS_ICU_DRUGS"]


