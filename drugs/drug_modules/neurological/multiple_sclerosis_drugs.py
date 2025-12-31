"""Neurological Medications - Multiple Sclerosis (MS) Drugs
Active module - contains disease-modifying therapies for multiple sclerosis"""

# Multiple Sclerosis Disease-Modifying Therapies

MULTIPLE_SCLEROSIS_DRUGS = {
    "Dimethyl fumarate": {
        "group": "Neurology - Fumaric Acid Ester for MS",
        "vietnamese_name": "Dimethyl fumarate, Tecfidera",
        "administration": ["PO"],
        "indications": [
            "Đa xơ cứng (MS) - relapsing-remitting (RRMS)",
            "Đa xơ cứng (MS) - active secondary progressive (SPMS)"
        ],
        "contraindications": [
            "Dị ứng dimethyl fumarate hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_loading": "120mg PO x 2 lần/ngày x 7 ngày",
            "adult_maintenance": "240mg PO x 2 lần/ngày",
            "notes": "Uống với thức ăn để giảm tác dụng phụ tiêu hóa. Có thể tăng liều từ 120mg x 2 lần/ngày lên 240mg x 2 lần/ngày sau 7 ngày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Đỏ bừng mặt (flushing) - phổ biến, thường tự khỏi sau vài tuần",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Đau bụng - phổ biến",
            "Giảm bạch cầu lympho (lymphopenia) - phổ biến, có thể nghiêm trọng",
            "Giảm bạch cầu trung tính (neutropenia) - hiếm",
            "Giảm bạch cầu (leukopenia) - hiếm",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Protein niệu - hiếm",
            "Tăng nguy cơ nhiễm trùng (do giảm lympho)"
        ],
        "interactions": [
            "Aspirin: có thể giảm đỏ bừng mặt (flushing)",
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Dimethyl fumarate là fumaric acid ester, được chuyển hóa thành monomethyl fumarate (MMF) trong ruột. "
            "Cơ chế chính xác chưa hoàn toàn rõ ràng, nhưng dimethyl fumarate/MMF có nhiều tác dụng: "
            "(1) Kích hoạt Nrf2 (nuclear factor erythroid 2-related factor 2) pathway → "
            "tăng sản xuất các chất chống oxy hóa (antioxidants) và giảm stress oxy hóa → "
            "bảo vệ tế bào thần kinh khỏi tổn thương. "
            "(2) Ức chế NF-κB (nuclear factor kappa B) pathway → "
            "giảm sản xuất các cytokine gây viêm (TNF-α, IL-1β, IL-6) → giảm viêm. "
            "(3) Ức chế sự di chuyển của tế bào T vào hệ thần kinh trung ương (CNS) → "
            "giảm viêm trong MS. "
            "(4) Gây apoptosis (chết tế bào) của tế bào T kích hoạt → "
            "giảm số lượng tế bào T gây viêm. "
            "Dẫn đến: giảm viêm trong MS, giảm tần suất tái phát, và làm chậm tiến triển bệnh. "
            "Dimethyl fumarate được dùng để điều trị RRMS và active SPMS, "
            "là thuốc đường uống, tiện lợi hơn các thuốc tiêm. "
            "Tác dụng phụ chính là đỏ bừng mặt (flushing) và các triệu chứng tiêu hóa, "
            "thường tự khỏi sau vài tuần."
        ),
        "monitoring": [
            "Số lượng bạch cầu lympho - theo dõi lymphopenia (quan trọng, có thể nghiêm trọng)",
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Tổng số bạch cầu - theo dõi leukopenia",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Protein niệu - theo dõi định kỳ",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.) - do giảm lympho",
            "Đáp ứng điều trị: tần suất tái phát, MRI não"
        ],
        "precautions": [
            "GIẢM BẠCH CẦU LYMPHO - phổ biến và có thể nghiêm trọng, cần theo dõi số lượng lympho định kỳ",
            "Ngừng dimethyl fumarate nếu số lượng lympho <500/μL kéo dài (>6 tháng)",
            "ĐỎ BỪNG MẶT (flushing) - phổ biến nhưng thường tự khỏi sau vài tuần, có thể giảm bằng aspirin",
            "Tác dụng phụ tiêu hóa (buồn nôn, tiêu chảy, đau bụng) - phổ biến, thường tự khỏi sau vài tuần",
            "Uống với thức ăn để giảm tác dụng phụ tiêu hóa",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm lympho",
            "Ngừng dimethyl fumarate nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân có tiền sử nhiễm trùng tái phát",
            "Theo dõi chức năng gan định kỳ - tăng men gan có thể nghiêm trọng"
        ],
        "pharmacokinetics": {
            "half_life": "~1 giờ (dimethyl fumarate), ~1 giờ (MMF)",
            "onset": "Giảm tế bào lympho trong vòng vài tuần",
            "duration": "Trung bình (do half-life ngắn, cần dùng 2 lần/ngày)",
            "protein_binding": "MMF: ~27-45%",
            "metabolism": "Ruột: chuyển hóa thành MMF (esterase), gan: chuyển hóa MMF qua TCA cycle",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Không cần điều chỉnh liều ở suy gan hoặc suy thận nhẹ-trung bình."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nang: bảo quản trong bao bì kín.",
        "black_box_warnings": (
            "GIẢM BẠCH CẦU LYMPHO - có thể nghiêm trọng. "
            "Cần theo dõi số lượng lympho định kỳ (trước điều trị, sau 6 tháng, sau đó mỗi 6-12 tháng). "
            "Ngừng dimethyl fumarate nếu số lượng lympho <500/μL kéo dài (>6 tháng). "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội, do giảm lympho. "
            "Ngừng dimethyl fumarate nếu có nhiễm trùng nặng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc ức chế miễn dịch khác (corticosteroid liều cao, methotrexate, azathioprine)",
                    "mechanism": "Tăng ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng nặng",
                    "management": "Thận trọng. Theo dõi chặt chẽ dấu hiệu nhiễm trùng và số lượng lympho."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin",
                    "mechanism": "Có thể giảm đỏ bừng mặt (flushing)",
                    "effect": "Giảm tác dụng phụ flushing",
                    "management": "Có thể dùng aspirin 325mg trước mỗi liều để giảm flushing."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng dimethyl fumarate hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tiền sử nhiễm trùng tái phát",
                "Giảm lympho nặng (<500/μL) - tăng nguy cơ nhiễm trùng",
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi cần thiết (MS nặng). Một số nghiên cứu cho thấy không tăng nguy cơ dị tật bẩm sinh, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng, có thể cần giảm liều",
            "notes": "Dimethyl fumarate chuyển hóa một phần ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ giảm lympho nặng",
                "Tăng tác dụng phụ tiêu hóa (buồn nôn, tiêu chảy, đau bụng)",
                "Tăng đỏ bừng mặt (flushing)",
                "Tăng men gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Theo dõi số lượng lympho chặt chẽ",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị hỗ trợ triệu chứng tiêu hóa",
                "Theo dõi chức năng gan"
            ],
            "monitoring": "Số lượng lympho, dấu hiệu nhiễm trùng, chức năng gan, triệu chứng tiêu hóa"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm tác dụng phụ tiêu hóa (quan trọng)",
                "timing": "Uống 2 lần/ngày (sáng, tối) với thức ăn. Liều tăng dần: 120mg x 2 lần/ngày x 7 ngày, sau đó 240mg x 2 lần/ngày.",
                "notes": "Uống với thức ăn để giảm tác dụng phụ tiêu hóa. Có thể dùng aspirin 325mg trước mỗi liều để giảm đỏ bừng mặt (flushing)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dimethyl fumarate (Tecfidera)",
                "UpToDate - Dimethyl fumarate: Drug information",
                "Lexicomp - Dimethyl fumarate monograph",
                "AAN Guidelines - Multiple Sclerosis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in RRMS and active SPMS"
        }
    },
    "Fingolimod": {
        "group": "Neurology - S1P Receptor Modulator for MS",
        "vietnamese_name": "Fingolimod, Gilenya",
        "administration": ["PO"],
        "indications": [
            "Đa xơ cứng (MS) - relapsing-remitting (RRMS)",
            "Đa xơ cứng (MS) - active secondary progressive (SPMS)"
        ],
        "contraindications": [
            "Dị ứng fingolimod hoặc bất kỳ thành phần nào",
            "Nhồi máu cơ tim, đột quỵ, TIA trong 6 tháng qua",
            "Block nhĩ thất độ II-III hoặc sick sinus syndrome (trừ khi có pacemaker)",
            "QTc kéo dài (≥500ms) hoặc nguy cơ kéo dài QTc",
            "Suy tim nặng (NYHA class III-IV)",
            "Nhiễm trùng nặng đang hoạt động"
        ],
        "dosage": {
            "adult_standard": "0.5mg PO mỗi ngày",
            "notes": "Uống với hoặc không có thức ăn. Cần theo dõi tim mạch trong 6 giờ đầu sau liều đầu tiên (nguy cơ chậm nhịp tim)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Chậm nhịp tim (bradycardia) - phổ biến, đặc biệt sau liều đầu",
            "Block nhĩ thất - phổ biến, đặc biệt sau liều đầu",
            "Nhiễm trùng (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu, herpes zoster) - phổ biến",
            "Tăng men gan (ALT) - phổ biến",
            "Tăng huyết áp",
            "Nhức đầu",
            "Ho",
            "Tiêu chảy",
            "Đau lưng",
            "Giảm bạch cầu lympho (lymphopenia)",
            "Macular edema (phù hoàng điểm) - hiếm nhưng nghiêm trọng",
            "Tăng nguy cơ nhiễm trùng nặng (bao gồm PML - progressive multifocal leukoencephalopathy)"
        ],
        "interactions": [
            "Thuốc chậm nhịp tim (beta-blockers, calcium channel blockers, digoxin): tăng nguy cơ chậm nhịp tim",
            "Thuốc kéo dài QTc (quinidine, procainamide, amiodarone): tăng nguy cơ rối loạn nhịp tim",
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Vaccine sống: chống chỉ định trong và sau điều trị",
            "Ketoconazole, itraconazole: tăng nồng độ fingolimod"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Fingolimod là thuốc điều biến thụ thể sphingosine-1-phosphate (S1P receptor modulator). "
            "S1P là một lipid signaling molecule quan trọng trong quá trình di chuyển tế bào lympho từ hạch bạch huyết vào máu. "
            "Tế bào lympho (đặc biệt tế bào T) cần S1P để rời khỏi hạch bạch huyết và vào máu, sau đó di chuyển vào hệ thần kinh trung ương (CNS) và gây viêm trong MS. "
            "Fingolimod (sau khi được phosphoryl hóa thành fingolimod-phosphate) gắn với thụ thể S1P1 trên tế bào lympho → "
            "gây internalization và degradation của thụ thể S1P1 → tế bào lympho không thể rời khỏi hạch bạch huyết → "
            "giảm số lượng tế bào lympho trong máu và giảm di chuyển vào CNS → giảm viêm trong MS. "
            "Dẫn đến: giảm tần suất tái phát và làm chậm tiến triển bệnh trong MS. "
            "Fingolimod cũng có tác dụng trên tim mạch (gây chậm nhịp tim, block nhĩ thất) do tác dụng trên thụ thể S1P trong tim. "
            "Fingolimod được dùng để điều trị RRMS và active SPMS, là thuốc S1P modulator đầu tiên được FDA phê duyệt cho MS."
        ),
        "monitoring": [
            "THEO DÕI TIM MẠCH TRONG 6 GIỜ ĐẦU SAU LIỀU ĐẦU TIÊN - ECG, huyết áp, nhịp tim (quan trọng)",
            "Số lượng bạch cầu lympho - theo dõi lymphopenia",
            "Chức năng gan (ALT, AST, bilirubin) - theo dõi tăng men gan",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Khám mắt định kỳ (3-4 tháng sau khi bắt đầu) để phát hiện macular edema",
            "Dấu hiệu PML (progressive multifocal leukoencephalopathy): thay đổi thần kinh, lú lẫn, yếu liệt",
            "MRI não định kỳ để đánh giá hoạt động bệnh MS",
            "Huyết áp - theo dõi tăng huyết áp"
        ],
        "precautions": [
            "NGUY CƠ CHẬM NHỊP TIM VÀ BLOCK NHĨ THẤT - đặc biệt sau liều đầu tiên, cần theo dõi tim mạch trong 6 giờ đầu",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có block nhĩ thất độ II-III, sick sinus syndrome (trừ khi có pacemaker)",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có QTc ≥500ms hoặc nguy cơ kéo dài QTc",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có suy tim nặng (NYHA class III-IV)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm tế bào lympho",
            "NGUY CƠ PML (progressive multifocal leukoencephalopathy) - nhiễm trùng não do JC virus, có thể gây tử vong",
            "NGUY CƠ MACULAR EDEMA (phù hoàng điểm) - hiếm nhưng nghiêm trọng, có thể gây mất thị lực",
            "Cần hoàn thành tất cả vaccine trước khi bắt đầu điều trị (ít nhất 4-6 tuần trước)",
            "CHỐNG CHỈ ĐỊNH vaccine sống trong và sau điều trị (ít nhất 2 tháng sau liều cuối)",
            "Ngừng fingolimod nếu có nhiễm trùng nặng",
            "Thận trọng khi dùng với thuốc chậm nhịp tim (beta-blockers, calcium channel blockers)",
            "Thận trọng ở bệnh nhân có tiền sử nhiễm trùng tái phát hoặc herpes zoster"
        ],
        "pharmacokinetics": {
            "half_life": "~6-9 ngày (dài)",
            "onset": "Giảm tế bào lympho trong vòng vài ngày",
            "duration": "Tác dụng kéo dài sau liều cuối (tế bào lympho tái tạo chậm, có thể mất vài tháng)",
            "protein_binding": ">99%",
            "metabolism": "Gan (chuyển hóa qua CYP4F2 và các enzyme khác)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nang: bảo quản trong bao bì kín.",
        "black_box_warnings": (
            "NGUY CƠ CHẬM NHỊP TIM VÀ BLOCK NHĨ THẤT - đặc biệt sau liều đầu tiên. "
            "Cần theo dõi tim mạch (ECG, huyết áp, nhịp tim) trong 6 giờ đầu sau liều đầu tiên. "
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có block nhĩ thất độ II-III, sick sinus syndrome (trừ khi có pacemaker), "
            "QTc ≥500ms, hoặc suy tim nặng (NYHA class III-IV). "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội và PML (progressive multifocal leukoencephalopathy). "
            "PML là nhiễm trùng não do JC virus, có thể gây tử vong hoặc tàn tật nặng. "
            "NGUY CƠ MACULAR EDEMA (phù hoàng điểm) - có thể gây mất thị lực, cần khám mắt định kỳ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc chậm nhịp tim (beta-blockers, non-dihydropyridine calcium channel blockers, digoxin)",
                    "mechanism": "Cả hai đều có thể gây chậm nhịp tim",
                    "effect": "Tăng nguy cơ chậm nhịp tim nghiêm trọng, block nhĩ thất, ngất",
                    "management": "Thận trọng. Có thể cần ngừng thuốc chậm nhịp tim trước khi bắt đầu fingolimod. Theo dõi tim mạch chặt chẽ."
                },
                {
                    "drug": "Thuốc kéo dài QTc (quinidine, procainamide, amiodarone, sotalol)",
                    "mechanism": "Cả hai đều có thể kéo dài QTc",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim nghiêm trọng (torsades de pointes)",
                    "management": "CHỐNG CHỈ ĐỊNH dùng đồng thời. Nếu cần dùng, theo dõi ECG chặt chẽ."
                },
                {
                    "drug": "Vaccine sống (MMR, varicella, zoster, yellow fever, BCG)",
                    "mechanism": "Fingolimod làm giảm đáp ứng miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "CHỐNG CHỈ ĐỊNH dùng vaccine sống trong và sau điều trị. Hoãn vaccine sống ít nhất 2 tháng sau liều cuối."
                }
            ],
            "moderate": [
                {
                    "drug": "Ketoconazole, itraconazole (CYP4F2 inhibitors)",
                    "mechanism": "Ức chế chuyển hóa fingolimod",
                    "effect": "Tăng nồng độ fingolimod, tăng tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều fingolimod."
                },
                {
                    "drug": "Thuốc ức chế miễn dịch khác (corticosteroid liều cao, methotrexate, azathioprine)",
                    "mechanism": "Tăng ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng nặng, bao gồm PML",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu phải dùng, theo dõi chặt chẽ dấu hiệu nhiễm trùng."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng fingolimod hoặc bất kỳ thành phần nào",
                "Block nhĩ thất độ II-III hoặc sick sinus syndrome (trừ khi có pacemaker)",
                "QTc ≥500ms hoặc nguy cơ kéo dài QTc",
                "Suy tim nặng (NYHA class III-IV)",
                "Nhồi máu cơ tim, đột quỵ, TIA trong 6 tháng qua",
                "Nhiễm trùng nặng đang hoạt động"
            ],
            "tương_đối": [
                "Tiền sử nhiễm trùng tái phát",
                "Tiền sử PML hoặc các nhiễm trùng cơ hội khác",
                "Tiền sử dùng thuốc ức chế miễn dịch khác (tăng nguy cơ PML)",
                "Tiền sử herpes zoster",
                "Bệnh tim mạch (suy tim nhẹ, block nhĩ thất độ I) - tăng nguy cơ chậm nhịp tim",
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi cần thiết (MS nặng). Một số nghiên cứu cho thấy tăng nguy cơ dị tật bẩm sinh, nhưng cần cân nhắc lợi ích/rủi ro. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Fingolimod bài tiết vào sữa mẹ. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu phải dùng, ngừng cho bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "notes": "Fingolimod chuyển hóa ở gan qua CYP4F2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Chậm nhịp tim nghiêm trọng, block nhĩ thất",
                "Tăng nguy cơ nhiễm trùng",
                "Giảm bạch cầu lympho nặng",
                "Tăng men gan nặng",
                "Macular edema"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "THEO DÕI TIM MẠCH CHẶT CHẼ - ECG, huyết áp, nhịp tim",
                "Xử trí chậm nhịp tim: atropine, pacemaker nếu cần",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chức năng gan",
                "Khám mắt để phát hiện macular edema"
            ],
            "monitoring": "Tim mạch (ECG, huyết áp, nhịp tim), dấu hiệu nhiễm trùng, số lượng lympho, chức năng gan, khám mắt"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn",
                "timing": "Uống 1 lần/ngày. Cần theo dõi tim mạch trong 6 giờ đầu sau liều đầu tiên (quan trọng).",
                "notes": "Uống với hoặc không có thức ăn. Cần được theo dõi tim mạch (ECG, huyết áp, nhịp tim) trong 6 giờ đầu sau liều đầu tiên do nguy cơ chậm nhịp tim và block nhĩ thất."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fingolimod (Gilenya)",
                "UpToDate - Fingolimod: Drug information",
                "Lexicomp - Fingolimod monograph",
                "AAN Guidelines - Multiple Sclerosis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in RRMS and active SPMS"
        }
    },

    "Ofatumumab": {
        "group": "Neurology - Anti-CD20 Monoclonal Antibody for MS",
        "vietnamese_name": "Ofatumumab, Kesimpta",
        "administration": ["SC"],
        "indications": [
            "Đa xơ cứng (MS) - relapsing-remitting (RRMS)",
            "Đa xơ cứng (MS) - active secondary progressive (SPMS)"
        ],
        "contraindications": [
            "Dị ứng ofatumumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng đang hoạt động",
            "Suy giảm miễn dịch nặng"
        ],
        "dosage": {
            "adult_loading": "20mg SC ngày 1, 20mg SC ngày 7, 20mg SC ngày 14",
            "adult_maintenance": "20mg SC mỗi tháng bắt đầu từ tuần 4",
            "notes": "Tiêm dưới da (SC) ở vùng bụng, đùi, hoặc cánh tay. Có thể tự tiêm sau khi được hướng dẫn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, ngứa) - phổ biến",
            "Nhiễm trùng (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu) - phổ biến",
            "Giảm immunoglobulin (hypogammaglobulinemia)",
            "Giảm bạch cầu lympho (lymphopenia)",
            "Dị ứng (hiếm)",
            "Tăng nguy cơ nhiễm trùng nặng (bao gồm PML - progressive multifocal leukoencephalopathy)"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Vaccine sống: chống chỉ định trong và sau điều trị"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Ofatumumab là kháng thể đơn dòng kháng CD20 (human monoclonal antibody). "
            "CD20 là kháng nguyên bề mặt trên tế bào B trưởng thành (pre-B cells đến memory B cells, nhưng không có trên plasma cells và stem cells). "
            "Trong MS, tế bào B đóng vai trò quan trọng trong quá trình viêm và tổn thương myelin. "
            "Ofatumumab gắn với CD20 → kích hoạt complement-dependent cytotoxicity (CDC) và antibody-dependent cell-mediated cytotoxicity (ADCC) → tiêu diệt tế bào B. "
            "Dẫn đến: giảm số lượng tế bào B trong máu và mô, giảm sản xuất autoantibodies, và giảm viêm trong MS. "
            "Ofatumumab được dùng để điều trị RRMS và active SPMS, là thuốc anti-CD20 đầu tiên được dùng qua đường tiêm dưới da (SC) cho MS, "
            "cho phép bệnh nhân tự tiêm tại nhà. "
            "Hiệu quả tương tự ocrelizumab nhưng tiện lợi hơn do có thể tự tiêm."
        ),
        "monitoring": [
            "Số lượng tế bào B (CD19+ hoặc CD20+) - giảm đáng kể sau điều trị",
            "Số lượng bạch cầu lympho - theo dõi lymphopenia",
            "Immunoglobulin (IgG, IgA, IgM) - theo dõi hypogammaglobulinemia",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Dấu hiệu PML (progressive multifocal leukoencephalopathy): thay đổi thần kinh, lú lẫn, yếu liệt, thay đổi thị giác",
            "MRI não định kỳ để đánh giá hoạt động bệnh MS",
            "Chức năng gan (ALT, AST) - theo dõi viêm gan"
        ],
        "precautions": [
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm tế bào B và immunoglobulin",
            "NGUY CƠ PML (progressive multifocal leukoencephalopathy) - nhiễm trùng não do JC virus, có thể gây tử vong",
            "Cần hoàn thành tất cả vaccine trước khi bắt đầu điều trị (ít nhất 4-6 tuần trước)",
            "CHỐNG CHỈ ĐỊNH vaccine sống trong và sau điều trị (ít nhất 6-12 tháng sau liều cuối)",
            "Ngừng ofatumumab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân có tiền sử nhiễm trùng tái phát",
            "Theo dõi immunoglobulin định kỳ - có thể cần IVIG nếu giảm nặng",
            "Có thể tự tiêm sau khi được hướng dẫn đúng cách"
        ],
        "pharmacokinetics": {
            "half_life": "~16 ngày (dài, cho phép dùng 1 lần/tháng)",
            "onset": "Giảm tế bào B trong vòng vài tuần",
            "duration": "Tác dụng kéo dài sau liều cuối (tế bào B tái tạo chậm)",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 7 ngày. Không làm nóng hoặc lắc mạnh.",
        "black_box_warnings": (
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội và PML (progressive multifocal leukoencephalopathy). "
            "PML là nhiễm trùng não do JC virus, có thể gây tử vong hoặc tàn tật nặng. "
            "Nguy cơ PML tăng ở bệnh nhân có tiền sử dùng thuốc ức chế miễn dịch khác hoặc có anti-JC virus antibodies. "
            "Cần theo dõi chặt chẽ dấu hiệu PML (thay đổi thần kinh, lú lẫn, yếu liệt). "
            "Ngừng ofatumumab ngay nếu nghi ngờ PML."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc ức chế miễn dịch khác (corticosteroid liều cao, methotrexate, azathioprine)",
                    "mechanism": "Tăng ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng nặng, bao gồm PML",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu phải dùng, theo dõi chặt chẽ dấu hiệu nhiễm trùng."
                },
                {
                    "drug": "Vaccine sống (MMR, varicella, zoster, yellow fever, BCG)",
                    "mechanism": "Ofatumumab làm giảm đáp ứng miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "CHỐNG CHỈ ĐỊNH dùng vaccine sống trong và sau điều trị. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                }
            ],
            "moderate": [
                {
                    "drug": "Vaccine không sống (inactivated vaccines)",
                    "mechanism": "Ofatumumab có thể làm giảm đáp ứng vaccine",
                    "effect": "Giảm hiệu quả vaccine",
                    "management": "Hoàn thành vaccine trước khi bắt đầu điều trị (ít nhất 4-6 tuần). Nếu cần tiêm trong điều trị, theo dõi đáp ứng."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng ofatumumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng đang hoạt động",
                "Suy giảm miễn dịch nặng"
            ],
            "tương_đối": [
                "Tiền sử nhiễm trùng tái phát",
                "Tiền sử PML hoặc các nhiễm trùng cơ hội khác",
                "Tiền sử dùng thuốc ức chế miễn dịch khác (tăng nguy cơ PML)",
                "Giảm immunoglobulin nặng",
                "Viêm gan B hoặc C đang hoạt động (nguy cơ reactivation)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi cần thiết (MS nặng). Một số nghiên cứu cho thấy tăng nguy cơ giảm tế bào B ở trẻ sơ sinh, nhưng không tăng nguy cơ dị tật bẩm sinh. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Ofatumumab bài tiết vào sữa mẹ ở nồng độ thấp. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi trẻ, nhưng cân nhắc ngừng cho bú nếu có thể."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Ofatumumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần thận trọng ở bệnh nhân viêm gan B hoặc C (nguy cơ reactivation)."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ nhiễm trùng",
                "Giảm bạch cầu lympho nặng",
                "Giảm immunoglobulin nặng",
                "Phản ứng tại chỗ tiêm nặng",
                "Dị ứng (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Có thể cần IVIG nếu giảm immunoglobulin nặng",
                "Xử trí phản ứng dị ứng nếu có (antihistamine, corticosteroid, epinephrine nếu cần)",
                "Theo dõi số lượng tế bào B và lympho"
            ],
            "monitoring": "Dấu hiệu nhiễm trùng, số lượng tế bào B và lympho, immunoglobulin, dấu hiệu PML"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dùng trực tiếp từ bút tiêm hoặc ống tiêm đã pha sẵn.",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                "notes": "Có thể tự tiêm sau khi được hướng dẫn. Lưu trữ trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm. Liều đầu: 20mg ngày 1, 7, 14; sau đó 20mg/tháng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ofatumumab (Kesimpta)",
                "UpToDate - Ofatumumab: Drug information",
                "Lexicomp - Ofatumumab monograph",
                "AAN Guidelines - Multiple Sclerosis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in RRMS and active SPMS"
        }
    },

}

__all__ = ['MULTIPLE_SCLEROSIS_DRUGS']

