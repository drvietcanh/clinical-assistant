"""
Vestibular Disorders and Dizziness Medications
Thuốc điều trị rối loạn tiền đình và chóng mặt
Betahistine, Dimenhydrinate, Meclizine
"""

VESTIBULAR_DRUGS = {
    "Betahistine":     {
        "group": "Neurology - Vestibular Disorder (Histamine H1 agonist, H3 antagonist)",
        "vietnamese_name": "Betahistine, Betaserc, Serc",
        "brand_names": {
            "common": ["Serc", "Betaserc", "Vertigo-Heel"],
            "vietnam": ["Betahistine STADA", "Serc", "Betaserc", "Betahistine"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Bệnh Meniere (Meniere's disease)",
            "Chóng mặt do rối loạn tiền đình",
            "Rối loạn tiền đình",
            "Ù tai",
            "Điếc đột ngột (off-label)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng betahistine",
                "Pheochromocytoma",
                "Loét dạ dày tá tràng đang hoạt động"
    ],
            "tương_đối": [
                "Hen phế quản - thận trọng",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng"
    ],
        },
        "dosage": {
            "adult_meniere": "8-16mg x 3 lần/ngày",
            "adult_vertigo": "8-16mg x 3 lần/ngày",
            "notes": "Betahistine là histamine H1 receptor agonist và H3 receptor antagonist. Tăng lưu lượng máu trong tai trong, giảm áp lực nội dịch, cải thiện chức năng tiền đình. Hiệu quả trong điều trị bệnh Meniere và chóng mặt do rối loạn tiền đình. Uống với thức ăn để giảm kích ứng dạ dày.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Đau đầu",
            "Buồn nôn",
            "Rối loạn tiêu hóa",
            "Chóng mặt (paradoxical - hiếm)",
            "Phản ứng dị ứng (hiếm)"
    ],
        "interactions": [
            "Thuốc kháng histamine H1 -> Có thể giảm hiệu quả betahistine",
            "MAO inhibitors -> Tăng nguy cơ tác dụng phụ"
    ],
        "pregnancy": "B",
        "mechanism_of_action": """Betahistine là histamine H1 receptor agonist và H3 receptor antagonist. Tác dụng: (1) Kích thích H1 receptors ở mạch máu tai trong → giãn mạch → tăng lưu lượng máu trong tai trong, (2) Đối kháng H3 receptors → tăng giải phóng histamine và các chất dẫn truyền thần kinh khác → cải thiện chức năng tiền đình, (3) Giảm áp lực nội dịch trong tai trong. Betahistine hiệu quả trong điều trị bệnh Meniere (tăng áp lực nội dịch) và chóng mặt do rối loạn tiền đình. Cơ chế chính xác chưa được hiểu đầy đủ, nhưng có liên quan đến cải thiện tuần hoàn và chức năng tiền đình.""",
        "monitoring": [
            "Triệu chứng chóng mặt, rối loạn tiền đình",
            "Triệu chứng bệnh Meniere (chóng mặt, ù tai, điếc)",
            "Dấu hiệu kích ứng dạ dày"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở pheochromocytoma",
            "CHỐNG CHỈ ĐỊNH ở loét dạ dày tá tràng đang hoạt động",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Thận trọng ở hen phế quản",
            "Thận trọng ở suy gan, suy thận"
    ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ",
            "onset": "Vài giờ",
            "duration": "6-8 giờ",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở pheochromocytoma và loét dạ dày tá tràng đang hoạt động.",
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ với histamine",
                    "effect": "Tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Dữ liệu hạn chế. Có thể bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Betahistine chuyển hóa ở gan. Thận trọng ở suy gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Đau đầu nặng",
                "Buồn nôn nặng",
                "Chóng mặt",
                "Rối loạn tiêu hóa"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hỗ trợ",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi triệu chứng lâm sàng",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "8-16mg x 3 lần/ngày, uống với thức ăn.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Betaserc (Betahistine)",
                "UpToDate - Betahistine: Drug information",
                "AAO-HNS Guidelines - Meniere's Disease"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["GI"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["GI symptoms"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AAO-HNS Guidelines - Meniere's Disease",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế). Betahistine chưa được nghiên cứu đầy đủ ở trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ tiêu hóa (buồn nôn, rối loạn tiêu hóa).",
                "dose_adjustment": "Liều tương tự người trẻ (8-16mg x 3 lần/ngày) nhưng thận trọng hơn. Có thể bắt đầu liều thấp hơn nếu cần.",
                "monitoring": "Theo dõi sát tác dụng phụ tiêu hóa, triệu chứng chóng mặt.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "2,000 - 10,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Serc (brand) thường đắt hơn (5,000-10,000 VND/viên 16mg). Betahistine generic thường rẻ hơn (2,000-5,000 VND/viên 16mg).",
            }
    },
    "Dimenhydrinate":     {
        "group": "Neurology - Vestibular Disorder (Antihistamine H1 + Stimulant)",
        "vietnamese_name": "Dimenhydrinate, Dramamine",
        "brand_names": {
            "common": ["Dramamine", "Gravol"],
            "vietnam": ["Dimenhydrinate", "Dramamine", "Gravol"],
        },
        "administration": [
            "PO",
            "IM",
            "IV"
    ],
        "indications": [
            "Say tàu xe (motion sickness)",
            "Chóng mặt do rối loạn tiền đình",
            "Chóng mặt do các nguyên nhân khác",
            "Buồn nôn, nôn"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng dimenhydrinate",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt",
                "Tắc ruột cơ học",
                "Trẻ sơ sinh <2 tuổi"
    ],
            "tương_đối": [
                "Người cao tuổi - tăng nhạy cảm với anticholinergic",
                "Bệnh tim mạch - thận trọng",
                "Hen phế quản - thận trọng"
    ],
        },
        "dosage": {
            "adult_motion_sickness": "50-100mg x 1 lần, uống 30-60 phút trước khi đi",
            "adult_vertigo": "50mg x 3-4 lần/ngày",
            "adult_im": "50mg IM mỗi 4 giờ nếu cần",
            "adult_iv": "50mg IV mỗi 4 giờ nếu cần",
            "notes": "Dimenhydrinate là kết hợp diphenhydramine (antihistamine H1) và 8-chlorotheophylline (stimulant). Tác dụng chống nôn và chống chóng mặt. Dùng 30-60 phút trước khi đi để phòng say tàu xe. Tác dụng an thần do diphenhydramine.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Khô miệng (do anticholinergic)",
            "Nhìn mờ",
            "Bí tiểu (đặc biệt ở nam giới có phì đại tuyến tiền liệt)",
            "Chóng mặt",
            "Rối loạn tiêu hóa"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần",
            "CNS depressants (Benzodiazepines, Opioids) -> Tăng tác dụng ức chế",
            "Thuốc kháng cholinergic khác -> Tăng tác dụng phụ anticholinergic",
            "MAO inhibitors -> Tăng nguy cơ tác dụng phụ"
    ],
        "pregnancy": "B",
        "mechanism_of_action": """Dimenhydrinate là kết hợp diphenhydramine (antihistamine H1, anticholinergic) và 8-chlorotheophylline (stimulant, tương tự caffeine). Diphenhydramine: (1) Ức chế histamine H1 receptors → giảm kích thích tiền đình, (2) Anticholinergic → giảm kích thích tiền đình và chống nôn, (3) Tác dụng an thần. 8-chlorotheophylline: (1) Stimulant → giảm buồn ngủ do diphenhydramine, (2) Tăng hiệu quả chống say tàu xe. Tác dụng hiệp đồng: chống say tàu xe, chống chóng mặt, chống nôn. Tuy nhiên, vẫn có tác dụng an thần do diphenhydramine.""",
        "monitoring": [
            "Triệu chứng say tàu xe, chóng mặt",
            "Buồn ngủ",
            "Dấu hiệu tác dụng phụ anticholinergic (khô miệng, nhìn mờ, bí tiểu)"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học",
            "Buồn ngủ - không lái xe sau khi uống",
            "Tác dụng phụ anticholinergic - khô miệng, nhìn mờ, bí tiểu",
            "Dùng 30-60 phút trước khi đi để phòng say tàu xe",
            "Thận trọng ở người cao tuổi - tăng nhạy cảm với anticholinergic",
            "Thận trọng ở bệnh nhân có bệnh tim mạch"
    ],
        "pharmacokinetics": {
            "half_life": "3-8 giờ",
            "onset": "30-60 phút",
            "duration": "4-6 giờ",
            "protein_binding": "98-99% (diphenhydramine)",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học. Buồn ngủ - không lái xe sau khi uống.",
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "Alcohol, CNS depressants",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp",
                    "management": "Thận trọng. Tránh rượu.",
                },
    {
                    "drug": "Thuốc kháng cholinergic khác",
                    "mechanism": "Tác dụng cộng dồn anticholinergic",
                    "effect": "Tăng tác dụng phụ anticholinergic",
                    "management": "Tránh dùng chung nếu có thể.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây buồn ngủ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Dimenhydrinate chuyển hóa ở gan. Thận trọng ở suy gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Khô miệng nặng",
                "Nhìn mờ",
                "Bí tiểu",
                "Ảo giác",
                "Co giật"
    ],
            "antidote": "Physostigmine (cho anticholinergic quá liều nặng)",
            "treatment": [
                "Điều trị hỗ trợ",
                "Nếu anticholinergic quá liều nặng (ảo giác, co giật): Physostigmine 0.5-2mg IV",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Physostigmine",
                    "mechanism": "Chất ức chế cholinesterase, đảo ngược tác dụng anticholinergic",
                    "indication": "Dimenhydrinate quá liều nặng (ảo giác, co giật, rối loạn ý thức)",
                    "dose": "0.5-2mg IV, có thể lặp lại",
                    "caution": "Chỉ dùng khi quá liều nặng, cần theo dõi chặt chẽ",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "50-100mg x 1 lần, uống 30-60 phút trước khi đi (để phòng say tàu xe). Hoặc 50mg x 3-4 lần/ngày (để điều trị chóng mặt).",
            },
            "im": {
                "reconstitution": "Không cần pha",
                "injection_site": "Tiêm bắp",
                "notes": "50mg IM mỗi 4 giờ nếu cần",
            },
            "iv": {
                "reconstitution": "Pha trong Normal saline hoặc D5W",
                "infusion_rate": "Tiêm chậm hoặc truyền trong 15-30 phút",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [],
                "notes": "50mg IV mỗi 4 giờ nếu cần",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dramamine (Dimenhydrinate)",
                "UpToDate - Dimenhydrinate: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CNS status", "Anticholinergic signs"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ],
            "pediatric_dosing": {
                "children_2_6": "12.5-25mg PO mỗi 6-8 giờ khi cần. Tối đa 75mg/ngày.",
                "children_6_12": "25-50mg PO mỗi 6-8 giờ khi cần. Tối đa 150mg/ngày.",
                "adolescents_12_18": "50-100mg PO mỗi 4-6 giờ khi cần. Tối đa 400mg/ngày.",
                "notes": "Không dùng cho trẻ sơ sinh. Thận trọng ở trẻ nhỏ (nguy cơ kích thích hoặc ức chế TKTW).",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ kháng cholinergic (khô miệng, bí tiểu, lú lẫn, té ngã).",
                "dose_adjustment": "Bắt đầu liều thấp (25-50mg) và theo dõi sát. Tối đa 200mg/ngày.",
                "monitoring": "Theo dõi sát tác dụng phụ kháng cholinergic, nguy cơ té ngã.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "1,000 - 5,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Dramamine (brand) thường đắt hơn (3,000-5,000 VND/viên 50mg). Dimenhydrinate generic thường rẻ hơn (1,000-3,000 VND/viên 50mg).",
            }
    },
    "Meclizine":     {
        "group": "Neurology - Vestibular Disorder (Antihistamine H1)",
        "vietnamese_name": "Meclizine, Antivert, Bonine",
        "brand_names": {
            "common": ["Antivert", "Bonine", "Dramamine Less Drowsy"],
            "vietnam": ["Meclizine", "Antivert", "Bonine"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Say tàu xe (motion sickness)",
            "Chóng mặt do rối loạn tiền đình",
            "Chóng mặt do các nguyên nhân khác",
            "Buồn nôn, nôn"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng meclizine",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt",
                "Tắc ruột cơ học"
    ],
            "tương_đối": [
                "Người cao tuổi - tăng nhạy cảm với anticholinergic",
                "Bệnh tim mạch - thận trọng",
                "Hen phế quản - thận trọng"
    ],
        },
        "dosage": {
            "adult_motion_sickness": "25-50mg x 1 lần, uống 1 giờ trước khi đi",
            "adult_vertigo": "25-50mg x 1-3 lần/ngày",
            "notes": "Meclizine là antihistamine H1, anticholinergic. Tác dụng chống say tàu xe và chống chóng mặt. Dùng 1 giờ trước khi đi để phòng say tàu xe. Tác dụng an thần ít hơn diphenhydramine. T1/2 dài (6-24 giờ) cho phép dùng 1 lần/ngày.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn ngủ (ít hơn diphenhydramine)",
            "Khô miệng (do anticholinergic)",
            "Nhìn mờ",
            "Bí tiểu (đặc biệt ở nam giới có phì đại tuyến tiền liệt)",
            "Chóng mặt",
            "Rối loạn tiêu hóa"
    ],
        "interactions": [
            "Alcohol: tăng tác dụng an thần",
            "CNS depressants (Benzodiazepines, Opioids) -> Tăng tác dụng ức chế",
            "Thuốc kháng cholinergic khác -> Tăng tác dụng phụ anticholinergic",
            "MAO inhibitors -> Tăng nguy cơ tác dụng phụ"
    ],
        "pregnancy": "B",
        "mechanism_of_action": """Meclizine là antihistamine H1, anticholinergic. Tác dụng: (1) Ức chế histamine H1 receptors → giảm kích thích tiền đình, (2) Anticholinergic → giảm kích thích tiền đình và chống nôn, (3) Tác dụng an thần (ít hơn diphenhydramine). Meclizine có t1/2 dài (6-24 giờ) cho phép dùng 1 lần/ngày. Hiệu quả trong điều trị say tàu xe và chóng mặt do rối loạn tiền đình. Tác dụng an thần ít hơn diphenhydramine, phù hợp cho bệnh nhân cần tỉnh táo.""",
        "monitoring": [
            "Triệu chứng say tàu xe, chóng mặt",
            "Buồn ngủ",
            "Dấu hiệu tác dụng phụ anticholinergic (khô miệng, nhìn mờ, bí tiểu)"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học",
            "Buồn ngủ - không lái xe sau khi uống (ít hơn diphenhydramine)",
            "Tác dụng phụ anticholinergic - khô miệng, nhìn mờ, bí tiểu",
            "Dùng 1 giờ trước khi đi để phòng say tàu xe",
            "Thận trọng ở người cao tuổi - tăng nhạy cảm với anticholinergic",
            "Thận trọng ở bệnh nhân có bệnh tim mạch",
            "T1/2 dài - có thể tích lũy nếu dùng nhiều lần"
    ],
        "pharmacokinetics": {
            "half_life": "6-24 giờ (dài)",
            "onset": "1 giờ",
            "duration": "12-24 giờ",
            "protein_binding": "Không rõ",
            "clearance": "Gan: chuyển hóa. Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở glaucoma góc đóng, phì đại tuyến tiền liệt, tắc ruột cơ học. Buồn ngủ - không lái xe sau khi uống.",
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "Alcohol, CNS depressants",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp",
                    "management": "Thận trọng. Tránh rượu.",
                },
    {
                    "drug": "Thuốc kháng cholinergic khác",
                    "mechanism": "Tác dụng cộng dồn anticholinergic",
                    "effect": "Tăng tác dụng phụ anticholinergic",
                    "management": "Tránh dùng chung nếu có thể.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây buồn ngủ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Meclizine chuyển hóa ở gan. Thận trọng ở suy gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Khô miệng nặng",
                "Nhìn mờ",
                "Bí tiểu",
                "Ảo giác",
                "Co giật"
    ],
            "antidote": "Physostigmine (cho anticholinergic quá liều nặng)",
            "treatment": [
                "Điều trị hỗ trợ",
                "Nếu anticholinergic quá liều nặng (ảo giác, co giật): Physostigmine 0.5-2mg IV",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Physostigmine",
                    "mechanism": "Chất ức chế cholinesterase, đảo ngược tác dụng anticholinergic",
                    "indication": "Meclizine quá liều nặng (ảo giác, co giật, rối loạn ý thức)",
                    "dose": "0.5-2mg IV, có thể lặp lại",
                    "caution": "Chỉ dùng khi quá liều nặng, cần theo dõi chặt chẽ",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "25-50mg x 1 lần, uống 1 giờ trước khi đi (để phòng say tàu xe). Hoặc 25-50mg x 1-3 lần/ngày (để điều trị chóng mặt).",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Antivert (Meclizine)",
                "UpToDate - Meclizine: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CNS status", "Anticholinergic signs"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 12 tuổi (dữ liệu hạn chế). Meclizine chưa được nghiên cứu đầy đủ ở trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ kháng cholinergic (khô miệng, bí tiểu, lú lẫn, té ngã).",
                "dose_adjustment": "Bắt đầu liều thấp (25mg) và theo dõi sát. Tối đa 50mg/ngày.",
                "monitoring": "Theo dõi sát tác dụng phụ kháng cholinergic, nguy cơ té ngã.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "2,000 - 15,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Antivert (brand) thường đắt hơn (5,000-15,000 VND/viên 25mg). Meclizine generic thường rẻ hơn (2,000-5,000 VND/viên 25mg).",
            }
    },
}

__all__ = ["VESTIBULAR_DRUGS"]
