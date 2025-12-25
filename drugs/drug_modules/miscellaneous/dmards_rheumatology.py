"""Disease-Modifying Antirheumatic Drugs (DMARDs) for Rheumatologic Diseases

Bao gồm: Methotrexate, Leflunomide, Hydroxychloroquine dùng trong viêm khớp dạng thấp,
viêm cột sống dính khớp, lupus và các bệnh tự miễn khác liên quan khớp."""

DMARDS_RHEUMATOLOGY_DRUGS = {
    "Methotrexate": {
        "group": "Rheumatology - Conventional DMARD (Antimetabolite, Folic Acid Antagonist)",
        "vietnamese_name": "Methotrexate, MTX",
        "administration": ["PO", "SC", "IM", "IV"],
        "indications": [
            "Viêm khớp dạng thấp (Rheumatoid Arthritis) - DMARD nền tảng (first-line)",
            "Viêm khớp vảy nến (Psoriatic arthritis)",
            "Vảy nến thể mảng trung bình–nặng",
            "Một số bệnh tự miễn khác (viêm mạch, lupus – off-label, tùy phác đồ chuyên khoa)",
        ],
        "contraindications": [
            "Có thai hoặc dự định có thai (CẤM – gây quái thai)",
            "Cho con bú",
            "Suy gan nặng (xơ gan, men gan rất cao)",
            "Suy thận nặng (CrCl <30 ml/phút) nếu không thể hiệu chỉnh liều và theo dõi sát",
            "Nghiện rượu, bệnh gan do rượu tiến triển",
            "Giảm bạch cầu, tiểu cầu nặng trước điều trị",
            "Nhiễm trùng nặng đang tiến triển",
        ],
        "dosage": {
            "adult_ra_po_weekly": "7.5–15mg uống 1 lần/tuần, có thể tăng tối đa 25–30mg/tuần theo đáp ứng và dung nạp",
            "adult_ra_sc_im_weekly": "7.5–25mg tiêm dưới da hoặc bắp 1 lần/tuần (sinh khả dụng tốt hơn PO ở liều cao)",
            "folic_acid_supplement": "Acid folic 5–10mg uống mỗi tuần (24 giờ sau methotrexate) hoặc 1mg/ngày (trừ ngày dùng MTX) để giảm độc tính",
            "notes": (
                "TUYỆT ĐỐI dùng methotrexate theo LIỀU TUẦN (ONCE WEEKLY), KHÔNG dùng hàng ngày. "
                "Khởi đầu liều thấp, tăng dần mỗi 2–4 tuần. Luôn bổ sung acid folic."
            ),
        },
        "renal_adjustment": {
            "normal": "Không đổi nhưng thận trọng với liều >20mg/tuần",
            "30_60": "Giảm liều 25–50% và kéo dài khoảng cách theo dõi",
            "under_30": "Tránh dùng hoặc giảm liều mạnh dưới giám sát chuyên khoa; cân nhắc DMARD khác",
        },
        "side_effects": [
            "Buồn nôn, nôn, chán ăn",
            "Viêm miệng, loét miệng",
            "Mệt mỏi",
            "Tăng men gan, viêm gan, xơ gan (dùng lâu dài, đặc biệt có uống rượu/béo phì)",
            "Ức chế tủy xương: giảm bạch cầu, tiểu cầu, thiếu máu",
            "Bệnh phổi kẽ do thuốc (ho khan, khó thở, tổn thương kẽ phổi)",
            "Rụng tóc nhẹ",
            "Nhiễm trùng cơ hội (nếu dùng phối hợp thuốc ức chế miễn dịch khác)",
        ],
        "interactions": [
            "NSAIDs (đặc biệt liều cao, suy thận): giảm thải trừ MTX, tăng độc tính",
            "Trimethoprim-sulfamethoxazole: tăng độc tủy xương (hiệp đồng ức chế folate)",
            "Penicillins, probenecid: giảm bài tiết MTX qua thận",
            "Folic acid / folinic acid: giảm độc tính MTX nhưng có thể giảm hiệu quả (cần dùng theo phác đồ)",
            "Rượu: tăng nguy cơ độc gan",
        ],
        "pregnancy": "X – CHỐNG CHỈ ĐỊNH tuyệt đối trong thai kỳ",
        "mechanism_of_action": (
            "Methotrexate ức chế dihydrofolate reductase và các enzyme liên quan tổng hợp purine, pyrimidine, "
            "làm giảm tổng hợp DNA/RNA, ức chế tăng sinh tế bào, đặc biệt là tế bào miễn dịch. "
            "Ở liều thấp dùng trong thấp khớp, MTX còn tăng adenosine ngoại bào (chống viêm mạnh) "
            "và điều hòa miễn dịch (giảm hoạt động tế bào T, B, đại thực bào)."
        ),
        "monitoring": [
            "Công thức máu (CBC) trước điều trị, mỗi 2–4 tuần giai đoạn đầu, sau đó mỗi 1–3 tháng",
            "Chức năng gan (ALT, AST), albumin, siêu âm/xơ gan nếu dùng lâu dài",
            "Chức năng thận (creatinin, eGFR)",
            "X-quang/CT ngực nền nếu nguy cơ bệnh phổi kẽ; thăm khám nếu ho/khó thở mới xuất hiện",
            "Test HBsAg, anti-HCV, HBsAb trước điều trị nếu có yếu tố nguy cơ",
            "Tình trạng thai nghén, biện pháp tránh thai (nam và nữ)",
        ],
        "precautions": [
            "Chỉ dùng 1 lần/tuần. Nhầm dùng hàng ngày có thể gây tử vong.",
            "Luôn bổ sung acid folic để giảm viêm miệng, độc tủy xương và gan.",
            "Ngừng MTX nếu men gan tăng >2–3 lần giới hạn trên, hoặc có giảm bạch cầu/tiểu cầu nặng.",
            "Tránh rượu. Hạn chế thuốc ảnh hưởng thận (NSAID liều cao, aminoglycoside).",
            "Thận trọng ở bệnh nhân béo phì, đái tháo đường, gan nhiễm mỡ, tiền sử bệnh gan.",
        ],
        "pharmacokinetics": {
            "half_life": "3–10 giờ (liều thấp), kéo dài ở suy thận",
            "onset": "4–6 tuần cho đáp ứng lâm sàng RA, tối đa 3–6 tháng",
            "duration": "Dùng 1 lần/tuần, tác dụng duy trì nhiều ngày",
            "protein_binding": "~50%",
            "clearance": "Thải trừ chủ yếu qua thận (lọc cầu thận và bài tiết ống thận); tích lũy trong dịch cơ thể và mô.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ánh sáng. Dung dịch tiêm theo hướng dẫn nhà sản xuất.",
        "black_box_warnings": (
            "Độc tủy xương, độc gan, bệnh phổi kẽ, độc tính trên thai nhi và gây quái thai, "
            "nhiễm trùng nặng, tổn thương thận, và tử vong nếu dùng sai liều (hàng ngày thay vì hàng tuần)."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Trimethoprim-sulfamethoxazole",
                    "mechanism": "Ức chế folate hiệp đồng và giảm thải trừ MTX",
                    "effect": "Tăng mạnh nguy cơ giảm bạch cầu, giảm tiểu cầu, viêm miệng, độc gan",
                    "management": "Tránh phối hợp; nếu bắt buộc, dùng liều rất thấp và theo dõi CBC sát.",
                },
                {
                    "drug": "NSAIDs liều cao, suy thận",
                    "mechanism": "Giảm thải trừ MTX qua thận, tăng nồng độ",
                    "effect": "Tăng độc tính MTX (tủy xương, gan, thận)",
                    "management": "Dùng NSAID liều thấp theo dõi sát; tránh NSAID liều cao/đợt dài.",
                },
            ],
            "moderate": [
                {
                    "drug": "Penicillins, probenecid",
                    "mechanism": "Cạnh tranh bài tiết ống thận",
                    "effect": "Tăng nồng độ MTX",
                    "management": "Theo dõi chức năng thận và CBC; điều chỉnh liều MTX nếu cần.",
                },
                {
                    "drug": "Folic acid / folinic acid",
                    "mechanism": "Bổ sung folate, đối kháng một phần tác dụng MTX",
                    "effect": "Giảm độc tính (có lợi), nhưng có thể giảm chút hiệu quả",
                    "management": "Bắt buộc dùng để giảm độc; chỉnh liều MTX để vẫn đạt hiệu quả.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Mang thai hoặc dự định mang thai trong vài tháng tới",
                "Cho con bú",
                "Suy gan nặng, xơ gan",
                "Suy thận nặng không kiểm soát",
                "Giảm bạch cầu, tiểu cầu nặng",
                "Nghiện rượu hoạt động",
            ],
            "tương_đối": [
                "Tiền sử bệnh gan do rượu, gan nhiễm mỡ",
                "Nhiễm trùng mạn tính (HBV, HCV, lao tiềm ẩn) – cần điều trị/phòng ngừa trước",
                "Béo phì, đái tháo đường (tăng nguy cơ gan nhiễm mỡ)",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": (
                "CHỐNG CHỈ ĐỊNH. Gây quái thai và sẩy thai. Ngừng MTX ít nhất 3 tháng "
                "trước khi thụ thai (nam và nữ, tùy khuyến cáo)."
            ),
            "lactation": {
                "safety": "Incompatible",
                "details": "MTX bài tiết vào sữa mẹ; nguy cơ độc tủy xương, ức chế tăng trưởng ở trẻ.",
                "recommendation": "Không dùng khi cho con bú hoặc ngừng cho bú nếu bắt buộc dùng MTX.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi men gan; cân nhắc liều thấp hơn",
            "moderate": "Tránh nếu có lựa chọn khác; nếu dùng phải theo dõi rất sát",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "MTX có nguy cơ gây xơ gan, đặc biệt ở bệnh nhân có yếu tố nguy cơ.",
        },
        "overdose_management": {
            "symptoms": [
                "Loét miệng lan tỏa, viêm niêm mạc",
                "Giảm bạch cầu, tiểu cầu nặng",
                "Viêm gan, suy gan",
                "Suy thận cấp do kết tủa MTX",
                "Bệnh phổi kẽ cấp, khó thở",
            ],
            "antidote": "Leucovorin (calcium folinate) – 'rescue' folate, đặc biệt trong ngộ độc/ dùng nhầm liều cao.",
            "treatment": [
                "Ngừng MTX ngay lập tức",
                "Dùng leucovorin cứu vãn theo phác đồ (liều và thời gian tùy mức độ)",
                "Bù dịch tích cực, kiềm hóa nước tiểu để tăng thải trừ MTX",
                "Có thể dùng glucarpidase ở ngộ độc rất nặng (nếu sẵn có)",
                "Theo dõi sát CBC, chức năng gan, thận, triệu chứng phổi",
            ],
            "monitoring": "Nồng độ MTX (nếu có), CBC, AST/ALT, creatinin, X-quang/CT ngực.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Leucovorin (calcium folinate)",
                    "dose": "Theo phác đồ cứu vãn MTX (ví dụ 10–15mg/m2 mỗi 6 giờ, điều chỉnh theo nồng độ MTX)",
                    "mechanism": "Cung cấp folate khử, vượt qua ức chế dihydrofolate reductase.",
                    "notes": "Cần dùng càng sớm càng tốt sau phát hiện ngộ độc.",
                }
            ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không kèm thức ăn; uống buổi tối sau ăn có thể giảm buồn nôn.",
                "timing": "LUÔN theo liều tuần (1 ngày cố định/tuần). Không chia liều hàng ngày.",
            },
            "sc": {
                "notes": "Tiêm dưới da giúp tăng sinh khả dụng và giảm tác dụng phụ tiêu hóa ở liều trung–cao.",
            },
        },
        "references": {
            "primary_sources": [
                "ACR 2021 Guidelines for the Treatment of Rheumatoid Arthritis",
                "EULAR 2019 recommendations for the management of RA",
                "UpToDate – Methotrexate: Drug information (rheumatology)",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "A – guideline-recommended first-line DMARD",
        },
    },

    "Leflunomide": {
        "group": "Rheumatology - Conventional DMARD (Pyrimidine Synthesis Inhibitor)",
        "vietnamese_name": "Leflunomide, Arava",
        "administration": ["PO"],
        "indications": [
            "Viêm khớp dạng thấp (Rheumatoid Arthritis)",
            "Viêm khớp vảy nến (Psoriatic arthritis)",
        ],
        "contraindications": [
            "Có thai hoặc dự định có thai (gây quái thai, rất kéo dài do t1/2 dài)",
            "Cho con bú",
            "Bệnh gan mạn tính hoặc men gan tăng cao",
            "Giảm bạch cầu, tiểu cầu nặng",
            "Nhiễm trùng nặng đang tiến triển",
        ],
        "dosage": {
            "adult_ra": "Liều duy trì thường 10–20mg PO 1 lần/ngày; có thể dùng liều nạp 100mg/ngày x 3 ngày nhưng hay gây độc tiêu hóa",
            "notes": "Nhiều guideline hiện nay bỏ liều nạp để giảm tác dụng phụ. Bắt đầu 10–20mg/ngày tùy bệnh nhân.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, theo dõi tác dụng phụ",
            "under_30": "Tránh dùng hoặc giảm liều, vì chất chuyển hóa thải chủ yếu qua mật nhưng có phần qua thận",
        },
        "side_effects": [
            "Tiêu chảy, buồn nôn, đau bụng",
            "Tăng men gan, hiếm khi suy gan nặng",
            "Rụng tóc nhẹ",
            "Tăng huyết áp nhẹ",
            "Giảm bạch cầu, tiểu cầu",
            "Tăng nguy cơ nhiễm trùng",
        ],
        "interactions": [
            "Hepatotoxic drugs khác (MTX, isoniazid, rượu): tăng nguy cơ độc gan",
            "Warfarin: có thể tăng INR",
            "Cholestyramine: tăng thanh thải leflunomide (dùng để 'rửa thuốc')",
        ],
        "pregnancy": "X – CHỐNG CHỈ ĐỊNH trong thai kỳ",
        "mechanism_of_action": (
            "Leflunomide là tiền chất, chuyển hóa thành A77 1726 (teriflunomide), "
            "ức chế dihydroorotate dehydrogenase, enzym then chốt trong tổng hợp de novo pyrimidine. "
            "Điều này làm giảm tăng sinh tế bào lympho T/N kích hoạt và điều hòa đáp ứng miễn dịch trong RA."
        ),
        "monitoring": [
            "Men gan (ALT, AST) trước và định kỳ (mỗi 1–2 tháng trong 6 tháng đầu, sau đó 3–6 tháng)",
            "Công thức máu (CBC) định kỳ",
            "Huyết áp",
            "Dấu hiệu nhiễm trùng (sốt, ho, tiểu đau)",
        ],
        "precautions": [
            "Thời gian bán thải dài (1–2 tuần) và tích lũy trong cơ thể; cần dùng cholestyramine để rửa thuốc nếu có thai/ngộ độc.",
            "Tránh dùng cùng các thuốc độc gan khác; nếu phối hợp MTX phải theo dõi men gan sát.",
            "Ngừng thuốc và rửa thuốc nếu men gan tăng kéo dài hoặc >2–3 lần giới hạn trên.",
        ],
        "pharmacokinetics": {
            "half_life": "Dài, khoảng 14–18 ngày (do chu trình ruột–gan)",
            "onset": "4–6 tuần, tối đa 3–6 tháng",
            "duration": "Tác dụng kéo dài hàng tuần sau khi ngừng nếu không rửa thuốc",
            "protein_binding": ">99%",
            "clearance": "Chuyển hóa ở gan; thải qua mật (phân) và ít qua thận; chu trình ruột–gan mạnh.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Gây độc gan nặng, có thể tử vong; cần theo dõi men gan thường xuyên. "
            "Gây quái thai; phụ nữ trong độ tuổi sinh sản phải tránh thai hiệu quả và rửa thuốc khi muốn mang thai."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Methotrexate và thuốc độc gan khác",
                    "mechanism": "Cộng hưởng độc gan",
                    "effect": "Tăng nguy cơ viêm gan, suy gan",
                    "management": "Chỉ phối hợp dưới giám sát chuyên khoa; theo dõi men gan mỗi 2–4 tuần.",
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tương tác chuyển hóa qua CYP2C9 và gắn protein",
                    "effect": "Có thể tăng INR, nguy cơ chảy máu",
                    "management": "Theo dõi INR sát khi bắt đầu/ngừng leflunomide.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Có thai hoặc dự định có thai (cả nam và nữ cần rửa thuốc trước khi có thai)",
                "Bệnh gan mạn tính tiến triển hoặc men gan tăng cao",
                "Giảm bạch cầu/tiểu cầu nặng không giải thích được",
            ],
            "tương_đối": [
                "Tiền sử bệnh gan, uống rượu nhiều",
                "Suy thận trung bình–nặng",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": (
                "CHỐNG CHỈ ĐỊNH. Cần rửa thuốc bằng cholestyramine (8g x 3 lần/ngày x 11 ngày) "
                "và đo nồng độ <0.02 mg/L trước khi mang thai."
            ),
            "lactation": {
                "safety": "Incompatible",
                "details": "Chưa rõ nồng độ trong sữa nhưng nguy cơ lý thuyết cao.",
                "recommendation": "Không dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi men gan sát",
            "moderate": "Tránh dùng nếu có lựa chọn khác",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Do nguy cơ độc gan, không khuyến cáo ở bệnh gan trung bình–nặng.",
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng",
                "Tăng men gan mạnh",
                "Giảm bạch cầu, tiểu cầu",
            ],
            "antidote": "Không có antidote đặc hiệu; dùng cholestyramine để tăng thải trừ (rửa thuốc).",
            "treatment": [
                "Ngừng leflunomide",
                "Dùng cholestyramine 8g uống 3 lần/ngày trong 11 ngày (không nhất thiết liên tiếp nếu không dung nạp)",
                "Theo dõi men gan, CBC, huyết áp",
            ],
            "monitoring": "Men gan, CBC, huyết áp mỗi vài ngày đến khi ổn định.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Cholestyramine",
                    "dose": "8g uống 3 lần/ngày x 11 ngày (hoặc phác đồ tương đương)",
                    "mechanism": "Gắn chất chuyển hóa leflunomide trong ruột, cắt chu trình ruột–gan, tăng thải trừ.",
                    "notes": "Dùng khi ngộ độc, men gan tăng nặng, hoặc chuẩn bị mang thai.",
                }
            ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không với thức ăn.",
                "timing": "Uống 1 lần/ngày, vào cùng thời điểm mỗi ngày.",
            }
        },
        "references": {
            "primary_sources": [
                "ACR 2021 Guidelines for RA",
                "UpToDate – Leflunomide: Drug information",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "A – guideline-supported DMARD",
        },
    },

    "Hydroxychloroquine": {
        "group": "Rheumatology - Conventional DMARD (Antimalarial)",
        "vietnamese_name": "Hydroxychloroquine, Plaquenil",
        "administration": ["PO"],
        "indications": [
            "Viêm khớp dạng thấp thể nhẹ đến trung bình (thường phối hợp DMARD khác)",
            "Lupus ban đỏ hệ thống (SLE) – thuốc nền tảng",
            "Viêm khớp vảy nến thể nhẹ (ít dùng đơn độc)",
        ],
        "contraindications": [
            "Dị ứng hydroxychloroquine hoặc chloroquine",
            "Bệnh võng mạc do 4-aminoquinoline hiện có",
        ],
        "dosage": {
            "adult_ra_sle": "200–400mg/ngày PO, chia 1–2 lần",
            "max_by_weight": "Không vượt quá 5mg/kg/ngày theo cân nặng thật (hoặc 6.5mg/kg/ngày theo cân nặng lý tưởng) để giảm nguy cơ độc võng mạc",
            "notes": "Tác dụng xuất hiện chậm (6–12 tuần), tối đa 6 tháng. Thường dùng phối hợp MTX/sulfasalazine trong RA.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Cân nhắc giảm liều nhẹ nếu dùng lâu dài",
            "under_30": "Giảm liều hoặc kéo dài khoảng cách dùng, theo dõi độc võng mạc",
        },
        "side_effects": [
            "Buồn nôn, đau bụng, tiêu chảy nhẹ",
            "Ban da, ngứa",
            "Tăng sắc tố da/móng (dùng lâu dài)",
            "Độc võng mạc (hiếm, liên quan liều tích lũy và thời gian dùng)",
            "Bệnh cơ/ bệnh thần kinh cơ rất hiếm",
        ],
        "interactions": [
            "Thuốc hạ đường huyết (insulin, sulfonylurea): tăng nguy cơ hạ đường huyết",
            "Thuốc kéo dài QT (amiodarone, một số kháng loạn nhịp, kháng sinh): tăng nguy cơ rối loạn nhịp",
        ],
        "pregnancy": "C – nhưng thường được xem là an toàn và khuyến cáo duy trì ở SLE",
        "mechanism_of_action": (
            "Hydroxychloroquine tích tụ trong lysosome tế bào miễn dịch, tăng pH nội lysosome, "
            "ức chế xử lý kháng nguyên và trình diện qua MHC class II, giảm hoạt hóa tế bào T. "
            "Nó cũng ức chế Toll-like receptors (TLR7/9), giảm sản xuất interferon và cytokine tiền viêm; "
            "tác dụng điều hòa miễn dịch nhẹ nhưng an toàn, hữu ích trong SLE và RA nhẹ."
        ),
        "monitoring": [
            "Khám mắt (võng mạc) nền trong 1 năm đầu dùng, sau đó định kỳ (thường mỗi năm sau 5 năm điều trị hoặc sớm hơn nếu có nguy cơ)",
            "Thị lực tự báo cáo (nhìn mờ, ám điểm hình bò – bull’s-eye maculopathy)",
            "Công thức máu (hiếm khi gây giảm bạch cầu)",
            "Men gan, creatinin định kỳ nếu dùng lâu dài",
        ],
        "precautions": [
            "Độc võng mạc phụ thuộc liều tích lũy và thời gian dùng (>5 năm, liều cao); giới hạn liều theo cân nặng.",
            "Thận trọng ở bệnh nhân có bệnh thận mạn, béo phì (cân nhắc liều theo cân nặng lý tưởng).",
            "Thận trọng khi phối hợp thuốc kéo dài QT; tránh ở bệnh nhân tiền sử loạn nhịp thất nặng.",
        ],
        "pharmacokinetics": {
            "half_life": "Dài, khoảng 40–50 ngày (tích lũy mô, đặc biệt mô mắt)",
            "onset": "6–12 tuần",
            "duration": "Hiệu quả duy trì nhiều tuần–tháng sau ngừng thuốc",
            "protein_binding": "~50%",
            "clearance": "Chuyển hóa ở gan, thải qua thận và phân; tích lũy trong mô (mắt, da).",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc kéo dài QT (amiodarone, sotalol, một số macrolide, fluoroquinolone)",
                    "mechanism": "Cộng hưởng kéo dài QT",
                    "effect": "Tăng nguy cơ xoắn đỉnh và loạn nhịp thất",
                    "management": "Thận trọng; tránh phối hợp nếu bệnh nhân có yếu tố nguy cơ QT kéo dài.",
                },
                {
                    "drug": "Insulin, sulfonylurea",
                    "mechanism": "Tăng nhạy cảm insulin và/hoặc tác dụng hạ đường huyết",
                    "effect": "Nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết, giảm liều thuốc hạ đường nếu cần.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng hydroxychloroquine hoặc chloroquine",
                "Bệnh võng mạc đặc hiệu do 4-aminoquinoline trước đó",
            ],
            "tương_đối": [
                "Bệnh thận mạn (tăng nguy cơ độc võng mạc)",
                "Tiền sử loạn nhịp thất, QT kéo dài",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": (
                "Trong SLE và RA, đa số guideline khuyến cáo TIẾP TỤC hydroxychloroquine trong thai kỳ "
                "do giảm đợt bùng phát và an toàn tương đối cho thai."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Nồng độ trong sữa thấp; không thấy tác dụng phụ nghiêm trọng ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú; theo dõi trẻ nếu dùng liều cao kéo dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều nhưng thận trọng",
            "moderate": "Cân nhắc giảm liều và theo dõi chức năng gan",
            "severe": "Thận trọng cao hoặc tránh dùng nếu có lựa chọn khác",
            "notes": "Chuyển hóa qua gan; suy gan có thể tăng phơi nhiễm.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, hạ huyết áp",
                "Loạn nhịp thất, ngừng tim (quá liều cấp nặng, thường do chloroquine hơn)",
            ],
            "antidote": "Không có antidote đặc hiệu; điều trị cấp cứu nâng đỡ.",
            "treatment": [
                "Hồi sức tim phổi tích cực, theo dõi ECG liên tục",
                "Bicarbonate natri, magnesium sulfate cho loạn nhịp, tùy phác đồ",
            ],
            "monitoring": "ECG, huyết áp, dấu hiệu thần kinh, đường huyết.",
        },
        "reversal_agents": {"available": False, "agents": []},
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống cùng thức ăn hoặc sữa để giảm kích ứng tiêu hóa.",
                "timing": "Chia 1–2 lần/ngày; nên dùng đều đặn, không tự ý ngừng đột ngột nếu đang kiểm soát tốt bệnh.",
            }
        },
        "references": {
            "primary_sources": [
                "ACR Guidelines for SLE and RA",
                "UpToDate – Hydroxychloroquine: Drug information",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "A – lâu năm, guideline-recommended background therapy",
        },
    },
}

__all__ = ["DMARDS_RHEUMATOLOGY_DRUGS"]


