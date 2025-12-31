"""Biological Drugs - Monoclonal Antibodies, Fusion Proteins, and Biologics
Includes both classic and newer biological medications"""

BIOLOGICAL_DRUGS = {
    "Adalimumab": {
        "group": "Biological - Monoclonal Antibody (anti-TNF-α)",
        "vietnamese_name": "Adalimumab, Humira",
        "administration": ["SC"],
        "indications": [
            "Viêm khớp dạng thấp (RA)",
            "Viêm cột sống dính khớp (AS)",
            "Bệnh Crohn (Crohn's disease)",
            "Viêm loét đại tràng (UC)",
            "Vảy nến (psoriasis)",
            "Viêm khớp vảy nến (PsA)",
            "Viêm khớp vị thành niên (JIA)",
            "Uveitis",
            "Hidradenitis suppurativa"
        ],
        "contraindications": [
            "Dị ứng adalimumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Suy tim nặng (NYHA class III-IV)",
            "Bệnh lao đang hoạt động"
        ],
        "dosage": {
            "adult_ra": "40mg SC mỗi 2 tuần (có thể tăng lên mỗi tuần nếu cần)",
            "adult_crohn": "160mg SC ngày 1 (hoặc 80mg x 2), sau đó 80mg SC ngày 15, sau đó 40mg SC mỗi 2 tuần",
            "adult_uc": "160mg SC ngày 1, sau đó 80mg SC ngày 15, sau đó 40mg SC mỗi 2 tuần",
            "adult_psoriasis": "80mg SC ngày 1, sau đó 40mg SC mỗi 2 tuần bắt đầu từ ngày 15",
            "adult_as": "40mg SC mỗi 2 tuần",
            "pediatric_jia": "20mg SC mỗi 2 tuần (nếu <30kg) hoặc 40mg SC mỗi 2 tuần (nếu ≥30kg)",
            "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng cơ hội, lao)",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Phản ứng dị ứng (rash, urticaria)",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
            "Suy tim - có thể làm nặng",
            "Bệnh lý thần kinh (demyelinating disease) - hiếm",
            "Giảm bạch cầu, tiểu cầu - hiếm",
            "Tăng men gan",
            "Buồn nôn, đau đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Adalimumab là kháng thể đơn dòng kháng TNF-α (tumor necrosis factor-alpha, fully human monoclonal antibody). TNF-α là cytokine tiền viêm quan trọng, được sản xuất bởi đại thực bào và tế bào T, đóng vai trò trong quá trình viêm. Trong các bệnh tự miễn (RA, Crohn, UC, psoriasis), TNF-α tăng cao → gây viêm mạn tính → tổn thương mô. Adalimumab gắn với TNF-α (cả dạng hòa tan và dạng màng) → ngăn chặn TNF-α gắn với thụ thể → ức chế tín hiệu viêm → giảm viêm và tổn thương mô. Dẫn đến: giảm triệu chứng và làm chậm tiến triển bệnh. Adalimumab được dùng để điều trị nhiều bệnh tự miễn qua trung gian TNF-α.",
        "monitoring": [
            "Nhiễm trùng - QUAN TRỌNG: theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Phản ứng tại chỗ tiêm",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng",
            "Dấu hiệu suy tim (nếu có tiền sử)",
            "Dấu hiệu bệnh lý thần kinh (nếu có triệu chứng)"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt và nghiêm trọng",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
            "Ngừng adalimumab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân suy tim - có thể làm nặng",
            "Thận trọng ở bệnh nhân có tiền sử ung thư - tăng nguy cơ ung thư",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh lý thần kinh demyelinating",
            "Theo dõi chức năng gan - có thể tăng men gan"
        ],
        "pharmacokinetics": {
            "half_life": "14 ngày (dao động 10-20 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "2 tuần (liều mỗi 2 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 15-30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng, đặc biệt lao và nhiễm trùng cơ hội. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ ung thư (lymphoma, ung thư da). Suy tim - có thể làm nặng, ngừng nếu suy tim mới hoặc nặng hơn.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (methotrexate, azathioprine, 6-mercaptopurine)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Adalimumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị adalimumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng adalimumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Bệnh lao đang hoạt động",
                "Suy tim nặng (NYHA class III-IV)"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Suy tim nhẹ đến trung bình (NYHA class I-II) - có thể làm nặng",
                "Tiền sử lao - cần điều trị dự phòng",
                "Tiền sử ung thư - tăng nguy cơ",
                "Bệnh lý thần kinh demyelinating - có thể làm nặng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Adalimumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ. Có thể truyền qua nhau thai trong tam cá nguyệt thứ ba, có thể ảnh hưởng đến đáp ứng vaccine ở trẻ sơ sinh.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Adalimumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Adalimumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chức năng gan (có thể tăng men gan)."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng",
                "Giảm bạch cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng adalimumab",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi công thức máu",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, công thức máu trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 40mg/0.8ml hoặc 80mg/0.8ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 15-30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Adalimumab (Humira)",
                "UpToDate - Adalimumab: Drug information",
                "Lexicomp - Adalimumab monograph",
                "ACR Guidelines - Rheumatoid Arthritis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections (opportunistic infections, TB)", "Hepatotoxicity", "Heart failure exacerbation", "Malignancy (lymphoma, skin cancer)", "Demyelinating disease"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL", "TB screening (PPD/IGRA) before treatment", "Hepatic function (ALT, AST)", "CBC", "Signs of heart failure", "Signs of malignancy"]
        },
        "guideline_tags": [
            "ACR Guidelines - Rheumatoid Arthritis",
            "ACR Guidelines - Psoriatic Arthritis",
            "FDA Black Box Warning - TNF-α Blockers and Serious Infections/TB",
            "FDA Black Box Warning - TNF-α Blockers and Malignancy",
            "ECCO Guidelines - Inflammatory Bowel Disease"
        ]
    },
    
    "Alemtuzumab": {
        "group": "Biological - Monoclonal Antibody (anti-CD52)",
        "vietnamese_name": "Alemtuzumab, Campath, Lemtrada",
        "administration": ["IV"],
        "indications": [
            "Đa xơ cứng (MS) - relapsing-remitting",
            "Bệnh bạch cầu lympho mạn (CLL) - đã điều trị trước đó"
        ],
        "contraindications": [
            "Dị ứng alemtuzumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "HIV dương tính",
            "Bệnh tự miễn đang hoạt động nặng"
        ],
        "dosage": {
            "adult_ms": "12mg IV/ngày x 5 ngày (chu kỳ 1), sau đó 12mg IV/ngày x 3 ngày sau 12 tháng (chu kỳ 2), có thể lặp lại sau 12 tháng nếu cần",
            "adult_cll": "30mg IV/ngày x 3 lần/tuần, tối đa 12 tuần",
            "notes": "Truyền trong 4 giờ. Premedication với corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền. Test lao, viêm gan B, HIV trước khi dùng. BLACK BOX WARNING về nhiều tác dụng phụ nghiêm trọng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion reaction) - phổ biến, có thể nghiêm trọng: sốt, ớn lạnh, đau đầu, buồn nôn, phát ban, khó thở",
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng cơ hội)",
            "Bệnh tự miễn thứ phát - phổ biến, có thể nghiêm trọng: ITP, thyroid disorders, nephropathies, cytopenias",
            "Giảm bạch cầu, tiểu cầu - phổ biến, có thể nghiêm trọng",
            "Tăng nguy cơ ung thư (thyroid cancer, melanoma, lymphoma)",
            "Viêm gan B tái hoạt (HBV reactivation) - NGUY HIỂM",
            "PML (progressive multifocal leukoencephalopathy) - hiếm nhưng nghiêm trọng",
            "Đau đầu",
            "Mệt mỏi",
            "Rash"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng và bệnh tự miễn khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Alemtuzumab là kháng thể đơn dòng kháng CD52 (humanized monoclonal antibody). CD52 là kháng nguyên bề mặt trên nhiều loại tế bào miễn dịch: tế bào T, tế bào B, NK cells, monocytes, macrophages. Trong MS, các tế bào miễn dịch này đóng vai trò quan trọng trong quá trình viêm và tổn thương myelin. Alemtuzumab gắn với CD52 → kích hoạt CDC và ADCC → tiêu diệt các tế bào miễn dịch. Dẫn đến: giảm số lượng tế bào T và B trong máu và mô, giảm viêm trong MS. Tuy nhiên, sau khi tế bào miễn dịch được tái tạo, hệ miễn dịch có thể tự điều chỉnh và giảm hoạt động gây bệnh. Alemtuzumab được dùng để điều trị MS relapsing-remitting, đặc biệt hiệu quả nhưng có nhiều tác dụng phụ nghiêm trọng.",
        "monitoring": [
            "Phản ứng truyền (infusion reaction) - QUAN TRỌNG: theo dõi trong và sau truyền",
            "Công thức máu (CBC) - QUAN TRỌNG: giảm bạch cầu, tiểu cầu phổ biến, theo dõi hàng tháng trong ít nhất 48 tháng sau liều cuối",
            "Bệnh tự miễn thứ phát - QUAN TRỌNG: theo dõi ITP (platelet), thyroid disorders (TSH, T4), nephropathies (creatinine, protein niệu), cytopenias hàng tháng trong ít nhất 48 tháng sau liều cuối",
            "Nhiễm trùng - tăng nguy cơ, đặc biệt nhiễm trùng cơ hội, theo dõi hàng tháng",
            "Viêm gan B (HBsAg, anti-HBc) - test trước khi dùng, theo dõi HBV reactivation",
            "HIV - test trước khi dùng",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Dấu hiệu PML (thay đổi thần kinh)",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Chức năng thận: creatinine, eGFR, protein niệu - mỗi 3-6 tháng",
            "Thyroid function: TSH, T4 - mỗi 3 tháng trong 48 tháng sau liều cuối",
            "Dấu hiệu ung thư - tăng nguy cơ"
        ],
        "precautions": [
            "BLACK BOX WARNING: nhiều tác dụng phụ nghiêm trọng",
            "THEO DÕI BỆNH TỰ MIỄN THỨ PHÁT CHẶT CHẼ - phổ biến và có thể nghiêm trọng, theo dõi hàng tháng trong ít nhất 48 tháng sau liều cuối",
            "Theo dõi ITP (platelet), thyroid disorders (TSH, T4), nephropathies (creatinine, protein niệu), cytopenias hàng tháng",
            "TEST VIÊM GAN B, HIV, LAO TRƯỚC KHI DÙNG",
            "Điều trị dự phòng HBV nếu có tiền sử viêm gan B",
            "Premedication với corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền",
            "Truyền chậm trong 4 giờ",
            "Theo dõi phản ứng truyền chặt chẽ - phổ biến và có thể nghiêm trọng",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng alemtuzumab nếu có nhiễm trùng nặng hoặc bệnh tự miễn nghiêm trọng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh tự miễn đang hoạt động",
            "Giảm bạch cầu có thể kéo dài vài tháng sau điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ chính xác, khoảng 1-2 tuần",
            "onset": "Vài tuần đến vài tháng",
            "duration": "12 tháng (chu kỳ mỗi 12 tháng)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life trung bình."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 8 giờ.",
        "black_box_warnings": "NHIỀU TÁC DỤNG PHỤ NGHIÊM TRỌNG: Bệnh tự miễn thứ phát (ITP, thyroid disorders, nephropathies, cytopenias) - phổ biến và có thể nghiêm trọng, theo dõi hàng tháng trong ít nhất 48 tháng sau liều cuối. VIÊM GAN B TÁI HOẠT (HBV reactivation) - có thể gây suy gan cấp và tử vong. Test HBsAg và anti-HBc trước khi dùng. Điều trị dự phòng HBV nếu có tiền sử. PML (progressive multifocal leukoencephalopathy) - hiếm nhưng nghiêm trọng. Phản ứng truyền nặng có thể gây tử vong. Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội. Tăng nguy cơ ung thư (thyroid cancer, melanoma, lymphoma).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Alemtuzumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị alemtuzumab. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                },
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng và bệnh tự miễn",
                    "management": "Tránh dùng đồng thời. Thận trọng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng alemtuzumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "HIV dương tính",
                "Bệnh tự miễn đang hoạt động nặng"
            ],
            "tương_đối": [
                "Viêm gan B (HBsAg dương tính) - cần điều trị dự phòng HBV",
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Giảm bạch cầu nặng - tăng nguy cơ nhiễm trùng",
                "Bệnh tự miễn từ trước - tăng nguy cơ bệnh tự miễn thứ phát",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Alemtuzumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (MS nặng). Một số nghiên cứu cho thấy tăng nguy cơ dị tật bẩm sinh, nhưng cần cân nhắc lợi ích/rủi ro. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Alemtuzumab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Alemtuzumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần thận trọng ở bệnh nhân viêm gan B (nguy cơ reactivation)."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở, phù, sốc)",
                "Nhiễm trùng nặng",
                "Bệnh tự miễn thứ phát nghiêm trọng (ITP nặng, suy thận)",
                "Viêm gan B tái hoạt",
                "Giảm bạch cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị sốc: dịch, vận mạch nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị bệnh tự miễn thứ phát: corticosteroid, IVIG cho ITP, điều trị suy thận nếu cần",
                "Điều trị HBV reactivation nếu có",
                "Theo dõi công thức máu, chức năng thận, chức năng gan",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, phản ứng truyền, công thức máu, chức năng thận, chức năng gan, dấu hiệu nhiễm trùng, dấu hiệu bệnh tự miễn trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 0.03-0.3mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 4 giờ.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Premedication: methylprednisolone 1000mg IV (hoặc tương đương), diphenhydramine 50mg IV/PO, acetaminophen 650-1000mg PO, 30-60 phút trước truyền. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Alemtuzumab (Lemtrada)",
                "UpToDate - Alemtuzumab: Drug information",
                "Lexicomp - Alemtuzumab monograph",
                "AAN Guidelines - Multiple Sclerosis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Autoimmune disorders (ITP, thyroid disorders, nephropathies, cytopenias) - common and serious", "HBV reactivation (life-threatening)", "PML (progressive multifocal leukoencephalopathy) - rare but serious", "Malignancy (thyroid cancer, melanoma, lymphoma)", "Serious infections (opportunistic infections)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["Autoimmune disorders - CRITICAL (monthly monitoring for at least 48 months after last dose)", "CBC (platelet, WBC) - CRITICAL (monthly for at least 48 months)", "Thyroid function (TSH, T4) - monthly for at least 48 months", "Renal function (creatinine, proteinuria) - monthly for at least 48 months", "HBV screening (HBsAg, anti-HBc) before treatment - CRITICAL", "HIV, TB screening before treatment", "Signs of infection - CRITICAL", "Signs of PML"]
        },
        "guideline_tags": [
            "AAN Guidelines - Multiple Sclerosis",
            "FDA Black Box Warning - Alemtuzumab and Autoimmune Disorders",
            "FDA Black Box Warning - Alemtuzumab and HBV Reactivation",
            "FDA Black Box Warning - Alemtuzumab and PML",
            "EAN Guidelines - Multiple Sclerosis"
        ]
    },
    
    "Anifrolumab": {
        "group": "Biological - Monoclonal Antibody (anti-IFN-α receptor)",
        "vietnamese_name": "Anifrolumab, Saphnelo",
        "administration": ["IV"],
        "indications": [
            "Lupus ban đỏ hệ thống (SLE) - trung bình đến nặng, tự kháng thể dương tính"
        ],
        "contraindications": [
            "Dị ứng anifrolumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult": "300mg IV mỗi 4 tuần",
            "notes": "Truyền trong 30 phút. Premedication với corticosteroid, antihistamine và acetaminophen để giảm phản ứng truyền."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu, herpes zoster)",
            "Phản ứng truyền (infusion reaction) - phổ biến lần đầu: sốt, ớn lạnh, đau đầu, buồn nôn",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Ung thư - tăng nguy cơ nhẹ",
            "Đau đầu",
            "Buồn nôn"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Anifrolumab là kháng thể đơn dòng kháng IFN-α receptor type I (interferon-alpha receptor type I, fully human monoclonal antibody). IFN-α là cytokine quan trọng trong quá trình viêm và tự miễn. IFN-α tăng cao trong SLE → kích hoạt các tế bào miễn dịch → tăng sản xuất autoantibodies và cytokines khác → gây viêm mạn tính → tổn thương mô. Anifrolumab gắn với IFN-α receptor type I → ngăn chặn IFN-α gắn với receptor → ức chế signaling → giảm viêm và tổn thương mô. Dẫn đến: giảm hoạt động bệnh và cải thiện triệu chứng trong SLE. Anifrolumab được dùng để điều trị SLE trung bình đến nặng, tự kháng thể dương tính.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị, đặc biệt herpes zoster",
            "Phản ứng truyền - QUAN TRỌNG: theo dõi trong và sau truyền, đặc biệt lần đầu",
            "Hoạt động bệnh SLE (SLEDAI, BILAG) - đánh giá hiệu quả điều trị",
            "Tự kháng thể (anti-dsDNA, complement) - có thể cải thiện",
            "Chức năng thận (creatinine, protein niệu) - trong SLE",
            "Công thức máu: CBC - mỗi 3-6 tháng"
        ],
        "precautions": [
            "THEO DÕI NHIỄM TRÙNG CHẶT CHẼ - tăng nguy cơ nhiễm trùng, đặc biệt herpes zoster",
            "Ngừng anifrolumab nếu có nhiễm trùng nặng",
            "Premedication với corticosteroid, antihistamine và acetaminophen để giảm phản ứng truyền",
            "Truyền chậm lần đầu - theo dõi chặt chẽ",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động",
            "Thận trọng ở bệnh nhân có tiền sử ung thư"
        ],
        "pharmacokinetics": {
            "half_life": "17 ngày (dao động 12-22 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "4 tuần",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng, đặc biệt herpes zoster. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ ung thư.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Anifrolumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị anifrolumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng anifrolumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử herpes zoster - tăng nguy cơ tái phát",
                "Tiền sử ung thư - tăng nguy cơ",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Anifrolumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (SLE nặng). Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Anifrolumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Anifrolumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu phản ứng truyền trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 0.5-1.5mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 30 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Premedication: methylprednisolone 100mg IV (hoặc tương đương), diphenhydramine 50mg IV/PO, acetaminophen 650-1000mg PO, 30-60 phút trước truyền. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Anifrolumab (Saphnelo)",
                "UpToDate - Anifrolumab: Drug information",
                "Lexicomp - Anifrolumab monograph",
                "ACR Guidelines - Systemic Lupus Erythematosus"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections (especially herpes zoster)", "Malignancy (slight increase)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL (especially herpes zoster)", "Infusion reactions (IV) - especially first dose", "SLE disease activity (SLEDAI, BILAG)", "CBC"]
        },
        "guideline_tags": [
            "ACR Guidelines - Systemic Lupus Erythematosus",
            "EULAR Guidelines - Systemic Lupus Erythematosus",
            "FDA Black Box Warning - Anifrolumab and Serious Infections",
            "FDA Black Box Warning - Anifrolumab and Malignancy"
        ]
    },
    
    "Atezolizumab": {
        "group": "Biological - Monoclonal Antibody (anti-PD-L1)",
        "vietnamese_name": "Atezolizumab, Tecentriq",
        "administration": ["IV"],
        "indications": [
            "Ung thư phổi không tế bào nhỏ (NSCLC) - kết hợp với chemotherapy hoặc đơn trị",
            "Ung thư phổi tế bào nhỏ (SCLC)",
            "Ung thư bàng quang (urothelial carcinoma)",
            "Ung thư vú triple-negative (PD-L1 dương tính)",
            "Ung thư gan (HCC)",
            "Ung thư hắc tố (melanoma)"
        ],
        "contraindications": [
            "Dị ứng atezolizumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Bệnh tự miễn đang hoạt động nặng"
        ],
        "dosage": {
            "adult_standard": "840mg IV mỗi 2 tuần, hoặc 1200mg IV mỗi 3 tuần, hoặc 1680mg IV mỗi 4 tuần",
            "adult_combination": "1200mg IV mỗi 3 tuần (kết hợp với chemotherapy)",
            "notes": "Truyền trong 60 phút (lần đầu) hoặc 30 phút (lần sau nếu dung nạp tốt). Có thể dùng đơn trị hoặc kết hợp với chemotherapy. Điều trị đến khi bệnh tiến triển hoặc độc tính không chấp nhận được."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng miễn dịch (immune-related adverse events, irAEs) - NGUY HIỂM, phổ biến",
            "Viêm phổi do miễn dịch (pneumonitis) - có thể tử vong",
            "Viêm đại tràng (colitis) - có thể tử vong",
            "Viêm gan (hepatitis) - có thể tử vong",
            "Viêm nội tiết (endocrinopathies): viêm tuyến giáp, viêm tuyến yên, viêm tuyến thượng thận - có thể vĩnh viễn",
            "Viêm da (dermatitis, rash)",
            "Viêm cơ tim (myocarditis) - hiếm nhưng nghiêm trọng",
            "Viêm thần kinh (neuropathy)",
            "Phản ứng truyền (infusion reaction) - hiếm",
            "Mệt mỏi",
            "Ngứa, phát ban",
            "Buồn nôn, tiêu chảy",
            "Giảm bạch cầu, tiểu cầu (khi kết hợp với chemotherapy)"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ phản ứng miễn dịch khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Atezolizumab là kháng thể đơn dòng kháng PD-L1 (programmed death-ligand 1, humanized monoclonal antibody). PD-L1 là ligand trên tế bào ung thư và tế bào miễn dịch, khi gắn với PD-1 trên tế bào T → ức chế hoạt động tế bào T → tế bào T không thể tiêu diệt tế bào ung thư (immune evasion). Atezolizumab gắn với PD-L1 → ngăn chặn PD-L1 gắn với PD-1 → giải phóng ức chế tế bào T → tế bào T hoạt động trở lại → tiêu diệt tế bào ung thư. Dẫn đến: tăng đáp ứng miễn dịch chống ung thư. Atezolizumab được dùng để điều trị nhiều loại ung thư có PD-L1 dương tính, có thể dùng đơn trị hoặc kết hợp với chemotherapy.",
        "monitoring": [
            "Phản ứng miễn dịch (irAEs) - QUAN TRỌNG: theo dõi chặt chẽ trong và sau điều trị",
            "Viêm phổi: khó thở, ho, đau ngực - chụp X-quang ngực nếu có triệu chứng",
            "Viêm đại tràng: tiêu chảy, đau bụng, phân có máu - nội soi nếu cần",
            "Viêm gan: vàng da, mệt mỏi, đau bụng - ALT, AST, bilirubin mỗi chu kỳ",
            "Viêm nội tiết: TSH, T4 (tuyến giáp), cortisol (tuyến thượng thận), glucose - mỗi chu kỳ",
            "Viêm cơ tim: đau ngực, khó thở, nhịp tim nhanh - troponin, ECG, echo nếu có triệu chứng",
            "Chức năng thận: creatinine, eGFR - mỗi chu kỳ",
            "Công thức máu: CBC - mỗi chu kỳ",
            "Dấu hiệu phản ứng truyền"
        ],
        "precautions": [
            "THEO DÕI PHẢN ỨNG MIỄN DỊCH (irAEs) CHẶT CHẼ - có thể nghiêm trọng và tử vong",
            "Ngừng atezolizumab và điều trị ngay nếu có irAE độ 3-4 (corticosteroid, immunosuppressant)",
            "Viêm phổi: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid liều cao",
            "Viêm đại tràng: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid, infliximab nếu cần",
            "Viêm gan: ngừng nếu ALT/AST >5x ULN, điều trị với corticosteroid",
            "Viêm nội tiết: có thể vĩnh viễn, cần điều trị thay thế hormone",
            "Viêm cơ tim: ngừng ngay, điều trị với corticosteroid liều cao",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh tự miễn đang hoạt động",
            "Thận trọng ở bệnh nhân đã cấy ghép tạng - tăng nguy cơ thải ghép"
        ],
        "pharmacokinetics": {
            "half_life": "27 ngày (dao động 18-38 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "2-4 tuần (liều mỗi 2-4 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "PHẢN ỨNG MIỄN DỊCH (immune-related adverse events, irAEs) - có thể nghiêm trọng và tử vong. Viêm phổi, viêm đại tràng, viêm gan, viêm nội tiết, viêm cơ tim có thể xảy ra. Ngừng và điều trị ngay nếu có irAE độ 3-4. Có thể gây tử vong thai nhi (category D).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Corticosteroid (liều cao, kéo dài)",
                    "mechanism": "Corticosteroid ức chế miễn dịch, có thể làm giảm hiệu quả atezolizumab",
                    "effect": "Có thể làm giảm đáp ứng điều trị",
                    "management": "Tránh dùng corticosteroid liều cao kéo dài trước điều trị. Có thể dùng để điều trị irAEs."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Atezolizumab làm thay đổi đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị atezolizumab. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng atezolizumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Bệnh tự miễn đang hoạt động nặng - tăng nguy cơ irAEs",
                "Đã cấy ghép tạng - tăng nguy cơ thải ghép",
                "Viêm phổi đang hoạt động - tăng nguy cơ viêm phổi do miễn dịch",
                "Viêm đại tràng đang hoạt động - tăng nguy cơ viêm đại tràng do miễn dịch",
                "Có thai (category D) - có thể gây tử vong thai nhi"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Atezolizumab là FDA category D - có thể gây tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rủi ro. Có thể gây dị tật bẩm sinh và tử vong thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Atezolizumab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Atezolizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chặt chẽ viêm gan do miễn dịch."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng miễn dịch nặng (irAEs độ 3-4)",
                "Phản ứng truyền nặng",
                "Viêm phổi nặng",
                "Viêm đại tràng nặng",
                "Viêm gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị irAEs.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị irAEs: corticosteroid liều cao (methylprednisolone 1-2mg/kg/ngày), immunosuppressant (infliximab cho viêm đại tràng) nếu cần",
                "Điều trị viêm phổi: corticosteroid liều cao, hỗ trợ hô hấp nếu cần",
                "Điều trị viêm đại tràng: corticosteroid, infliximab nếu không đáp ứng",
                "Điều trị viêm gan: corticosteroid, hỗ trợ gan nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu irAEs, chức năng gan, thận, nội tiết trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 0.3-12mg/ml. Không lọc.",
                "infusion_rate": "Lần đầu: truyền trong 60 phút. Lần sau: có thể truyền trong 30 phút nếu dung nạp tốt.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Không cần premedication thường quy. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi phản ứng miễn dịch."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Atezolizumab (Tecentriq)",
                "UpToDate - Atezolizumab: Drug information",
                "Lexicomp - Atezolizumab monograph",
                "NCCN Guidelines - Multiple cancer types"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Immune-related adverse events (irAEs) - life-threatening", "Pneumonitis (can be fatal)", "Colitis (can be fatal)", "Hepatitis (can be fatal)", "Myocarditis (rare but serious)", "Endocrinopathies (may be permanent)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of irAEs - CRITICAL (pneumonitis, colitis, hepatitis, endocrinopathies)", "Hepatic function (ALT, AST, bilirubin) - each cycle", "Thyroid function (TSH, T4) - each cycle", "Cortisol, glucose - each cycle", "Chest X-ray if respiratory symptoms", "ECG, troponin if cardiac symptoms"]
        },
        "guideline_tags": [
            "NCCN Guidelines - Multiple Cancer Types",
            "ASCO Guidelines - Immune Checkpoint Inhibitors",
            "FDA Black Box Warning - Immune Checkpoint Inhibitors and irAEs",
            "ESMO Guidelines - Immunotherapy"
        ]
    },
    
    "Belimumab": {
        "group": "Biological - Monoclonal Antibody (anti-BAFF)",
        "vietnamese_name": "Belimumab, Benlysta",
        "administration": ["IV", "SC"],
        "indications": [
            "Lupus ban đỏ hệ thống (SLE) - hoạt động, tự kháng thể dương tính",
            "Lupus ban đỏ hệ thống (SLE) - trẻ em ≥5 tuổi"
        ],
        "contraindications": [
            "Dị ứng belimumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult_iv": "10mg/kg IV ngày 0, 14, 28, sau đó mỗi 4 tuần",
            "adult_sc": "200mg SC mỗi tuần (sau loading 200mg SC x 2 lần cách nhau 1 tuần)",
            "pediatric_iv_5_17": "10mg/kg IV ngày 0, 14, 28, sau đó mỗi 4 tuần",
            "notes": "IV: truyền trong 1 giờ. SC: tiêm dưới da. Premedication với antihistamine và acetaminophen để giảm phản ứng truyền."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)",
            "Phản ứng truyền (infusion reaction) - phổ biến lần đầu: sốt, ớn lạnh, đau đầu, buồn nôn",
            "Phản ứng tại chỗ tiêm (SC) - đau, đỏ, sưng",
            "Buồn nôn, tiêu chảy",
            "Mất ngủ",
            "Trầm cảm",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Ung thư - tăng nguy cơ nhẹ"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Belimumab là kháng thể đơn dòng kháng BAFF (B-cell activating factor, fully human monoclonal antibody). BAFF là cytokine quan trọng cho sự sống và hoạt động của tế bào B. BAFF tăng cao trong SLE → tăng số lượng và hoạt động tế bào B → tăng sản xuất autoantibodies → gây bệnh tự miễn. Belimumab gắn với BAFF → ngăn chặn BAFF gắn với receptor trên tế bào B → giảm số lượng và hoạt động tế bào B → giảm sản xuất autoantibodies → giảm viêm và tổn thương mô. Dẫn đến: giảm hoạt động bệnh và cải thiện triệu chứng trong SLE. Belimumab được dùng để điều trị SLE hoạt động, tự kháng thể dương tính.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Phản ứng truyền (IV) - QUAN TRỌNG: theo dõi trong và sau truyền, đặc biệt lần đầu",
            "Phản ứng tại chỗ tiêm (SC)",
            "Hoạt động bệnh SLE (SLEDAI, BILAG) - đánh giá hiệu quả điều trị",
            "Tự kháng thể (anti-dsDNA, complement) - có thể cải thiện",
            "Chức năng thận (creatinine, protein niệu) - trong SLE",
            "Công thức máu: CBC - mỗi 3-6 tháng"
        ],
        "precautions": [
            "THEO DÕI NHIỄM TRÙNG CHẶT CHẼ - tăng nguy cơ nhiễm trùng",
            "Ngừng belimumab nếu có nhiễm trùng nặng",
            "Premedication với antihistamine và acetaminophen để giảm phản ứng truyền (IV)",
            "Truyền chậm lần đầu (IV) - theo dõi chặt chẽ",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động",
            "Theo dõi dấu hiệu trầm cảm - tăng nguy cơ",
            "Thận trọng ở bệnh nhân có tiền sử ung thư"
        ],
        "pharmacokinetics": {
            "half_life": "19 ngày (dao động 15-25 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "4 tuần (IV) hoặc 1 tuần (SC)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "IV: Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ. SC: Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ ung thư. Tăng nguy cơ trầm cảm và tự tử.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Belimumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị belimumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng belimumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử ung thư - tăng nguy cơ",
                "Trầm cảm hoặc tiền sử trầm cảm - tăng nguy cơ",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Belimumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (SLE nặng). Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Belimumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Belimumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền/tiêm ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu phản ứng truyền trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 0.8-1.2mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 1 giờ.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Premedication: diphenhydramine 50mg IV/PO, acetaminophen 650-1000mg PO, 30-60 phút trước truyền. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu."
            },
            "sc": {
                "reconstitution": "Dạng SC: 200mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Belimumab (Benlysta)",
                "UpToDate - Belimumab: Drug information",
                "Lexicomp - Belimumab monograph",
                "ACR Guidelines - Systemic Lupus Erythematosus"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections", "Malignancy (slight increase)", "Depression/suicide risk"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL", "Infusion reactions (IV) - especially first dose", "SLE disease activity (SLEDAI, BILAG)", "Signs of depression/suicide", "CBC"]
        },
        "guideline_tags": [
            "ACR Guidelines - Systemic Lupus Erythematosus",
            "EULAR Guidelines - Systemic Lupus Erythematosus",
            "FDA Black Box Warning - Belimumab and Serious Infections",
            "FDA Black Box Warning - Belimumab and Depression/Suicide"
        ]
    },
    
    "Bevacizumab": {
        "group": "Biological - Monoclonal Antibody (anti-VEGF)",
        "vietnamese_name": "Bevacizumab, Avastin",
        "administration": ["IV"],
        "indications": [
            "Ung thư đại trực tràng (metastatic) - kết hợp với chemotherapy",
            "Ung thư phổi không tế bào nhỏ (NSCLC) - kết hợp với chemotherapy",
            "Ung thư thận (RCC) - kết hợp với interferon",
            "Ung thư buồng trứng (recurrent) - kết hợp với chemotherapy",
            "Ung thư cổ tử cung (recurrent) - kết hợp với chemotherapy",
            "Glioblastoma (recurrent)",
            "Thoái hóa điểm vàng do tuổi (AMD) - dạng mắt"
        ],
        "contraindications": [
            "Dị ứng bevacizumab",
            "Chảy máu nặng hoặc đang chảy máu",
            "Phẫu thuật gần đây (trong vòng 28 ngày) hoặc dự kiến phẫu thuật",
            "Thủng đường tiêu hóa",
            "Có thai (category C)"
        ],
        "dosage": {
            "adult_colorectal": "5-10mg/kg IV mỗi 2 tuần, hoặc 7.5-15mg/kg IV mỗi 3 tuần (kết hợp với chemotherapy)",
            "adult_nsclc": "15mg/kg IV mỗi 3 tuần (kết hợp với chemotherapy)",
            "adult_rcc": "10mg/kg IV mỗi 2 tuần (kết hợp với interferon)",
            "adult_ovarian": "15mg/kg IV mỗi 3 tuần (kết hợp với chemotherapy)",
            "adult_glioblastoma": "10mg/kg IV mỗi 2 tuần",
            "notes": "Ngừng ít nhất 28 ngày trước phẫu thuật lớn. Không dùng trong vòng 28 ngày sau phẫu thuật."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Chảy máu (bleeding) - phổ biến, có thể nghiêm trọng",
            "Thủng đường tiêu hóa (GI perforation) - NGUY HIỂM",
            "Tăng huyết áp - phổ biến",
            "Protein niệu - phổ biến, có thể nặng (nephrotic syndrome)",
            "Huyết khối tĩnh mạch (VTE) - tăng nguy cơ",
            "Huyết khối động mạch (ATE) - tăng nguy cơ",
            "Chậm lành vết thương - tăng nguy cơ",
            "Suy tim - hiếm",
            "Phản ứng truyền (infusion reaction) - hiếm",
            "Giảm bạch cầu, tiểu cầu (khi kết hợp với chemotherapy)"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Tăng nguy cơ chảy máu khi dùng với thuốc chống đông, kháng tiểu cầu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Bevacizumab là kháng thể đơn dòng kháng VEGF (vascular endothelial growth factor, humanized monoclonal antibody). VEGF là cytokine quan trọng trong quá trình tạo mạch (angiogenesis). VEGF gắn với VEGFR (VEGF receptor) trên tế bào nội mô → kích hoạt signaling → tăng sinh tế bào nội mô, tạo mạch mới. Tạo mạch cần thiết cho sự phát triển của khối u (ung thư cần mạch máu để cung cấp oxy và chất dinh dưỡng). Bevacizumab gắn với VEGF → ngăn chặn VEGF gắn với VEGFR → ức chế tạo mạch → giảm cung cấp máu cho khối u → ức chế tăng trưởng khối u. Dẫn đến: giảm tăng trưởng và di căn của khối u. Bevacizumab được dùng để điều trị nhiều loại ung thư (đại trực tràng, phổi, thận, buồng trứng, v.v.) kết hợp với chemotherapy.",
        "monitoring": [
            "Huyết áp - tăng huyết áp phổ biến, theo dõi mỗi 2-3 tuần",
            "Protein niệu (urine protein/creatinine ratio hoặc 24h urine protein) - phổ biến, có thể nặng",
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, ho ra máu) - phổ biến",
            "Dấu hiệu thủng đường tiêu hóa (đau bụng dữ dội, sốt, buồn nôn, nôn) - NGUY HIỂM",
            "Dấu hiệu huyết khối (VTE, ATE) - tăng nguy cơ",
            "Dấu hiệu chậm lành vết thương",
            "Công thức máu (khi kết hợp với chemotherapy)",
            "Chức năng thận (creatinine, eGFR)"
        ],
        "precautions": [
            "NGỪNG ÍT NHẤT 28 NGÀY TRƯỚC PHẪU THUẬT LỚN - tăng nguy cơ chậm lành vết thương và chảy máu",
            "Không dùng trong vòng 28 ngày sau phẫu thuật",
            "Theo dõi huyết áp chặt chẽ - tăng huyết áp phổ biến, điều trị nếu cần",
            "Theo dõi protein niệu - có thể tiến triển thành nephrotic syndrome",
            "Ngừng nếu protein niệu >3.5g/24h hoặc nephrotic syndrome",
            "Thận trọng ở bệnh nhân có nguy cơ chảy máu cao",
            "Thận trọng ở bệnh nhân có tiền sử thủng đường tiêu hóa",
            "Thận trọng với thuốc chống đông, kháng tiểu cầu - tăng nguy cơ chảy máu",
            "Theo dõi dấu hiệu thủng đường tiêu hóa - ngừng ngay nếu nghi ngờ"
        ],
        "pharmacokinetics": {
            "half_life": "20 ngày (dao động 11-50 ngày)",
            "onset": "Vài tuần",
            "duration": "2-3 tuần (liều mỗi 2-3 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "THỦNG ĐƯỜNG TIÊU HÓA (GI perforation) - có thể gây tử vong. Ngừng ngay nếu nghi ngờ. Chảy máu nặng (pulmonary hemorrhage, GI bleeding, CNS bleeding) - có thể gây tử vong. Tăng nguy cơ huyết khối động mạch (ATE). Chậm lành vết thương - ngừng ít nhất 28 ngày trước phẫu thuật lớn.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc chống đông (warfarin, heparin, LMWH, DOAC)",
                    "mechanism": "Cả hai đều tăng nguy cơ chảy máu, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ. Cân nhắc giảm liều hoặc ngừng một trong hai thuốc."
                },
                {
                    "drug": "Thuốc kháng tiểu cầu (aspirin, clopidogrel, ticagrelor)",
                    "mechanism": "Cả hai đều tăng nguy cơ chảy máu, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng bevacizumab",
                "Chảy máu nặng hoặc đang chảy máu",
                "Phẫu thuật gần đây (trong vòng 28 ngày) hoặc dự kiến phẫu thuật",
                "Thủng đường tiêu hóa"
            ],
            "tương_đối": [
                "Tăng huyết áp không kiểm soát - có thể làm nặng",
                "Protein niệu nặng (>2g/24h) - có thể tiến triển thành nephrotic syndrome",
                "Tiền sử thủng đường tiêu hóa - tăng nguy cơ",
                "Tiền sử huyết khối động mạch - tăng nguy cơ",
                "Suy tim - có thể làm nặng",
                "Dùng với thuốc chống đông, kháng tiểu cầu - tăng nguy cơ chảy máu",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Bevacizumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (ung thư nặng). Một số nghiên cứu trên động vật cho thấy tăng nguy cơ dị tật bẩm sinh và sảy thai. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Bevacizumab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Bevacizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu nặng",
                "Thủng đường tiêu hóa",
                "Tăng huyết áp nặng",
                "Protein niệu nặng (nephrotic syndrome)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng bevacizumab",
                "Điều trị chảy máu: truyền máu, huyết tương, tiểu cầu nếu cần",
                "Điều trị thủng đường tiêu hóa: phẫu thuật nếu cần",
                "Điều trị tăng huyết áp: thuốc hạ huyết áp",
                "Điều trị protein niệu: ACE inhibitor hoặc ARB nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu chảy máu, dấu hiệu thủng đường tiêu hóa, huyết áp, protein niệu trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 1.4-16.5mg/ml. Không lọc.",
                "infusion_rate": "Truyền trong 90 phút lần đầu. Nếu dung nạp tốt, có thể truyền trong 60 phút lần sau, sau đó 30 phút nếu vẫn dung nạp tốt.",
                "compatibility": ["NS"],
                "incompatibility": ["D5W (không ổn định)", "Không pha với các thuốc khác"],
                "notes": "Không cần premedication thường quy. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Bevacizumab (Avastin)",
                "UpToDate - Bevacizumab: Drug information",
                "Lexicomp - Bevacizumab monograph",
                "NCCN Guidelines - Colorectal Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": True,
            "organ_toxicity": ["GI perforation (life-threatening)", "Wound healing complications", "Hypertension", "Proteinuria (may progress to nephrotic syndrome)", "Arterial/venous thromboembolism", "Heart failure"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Blood pressure - CRITICAL (hypertension common)", "Proteinuria (urine protein/creatinine ratio or 24h urine protein) - CRITICAL", "Signs of bleeding - CRITICAL", "Signs of GI perforation - CRITICAL (life-threatening)", "Signs of thromboembolism", "Wound healing (stop 28 days before/after major surgery)"]
        },
        "guideline_tags": [
            "NCCN Guidelines - Multiple Cancer Types",
            "ASCO Guidelines - Anti-VEGF Therapy",
            "FDA Black Box Warning - Bevacizumab and GI Perforation",
            "FDA Black Box Warning - Bevacizumab and Wound Healing"
        ]
    },
    
    "Brodalumab": {
        "group": "Biological - Monoclonal Antibody (anti-IL-17RA)",
        "vietnamese_name": "Brodalumab, Siliq",
        "administration": ["SC"],
        "indications": [
            "Vảy nến (psoriasis) - trung bình đến nặng"
        ],
        "contraindications": [
            "Dị ứng brodalumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Bệnh viêm ruột (IBD) đang hoạt động",
            "Tiền sử tự tử hoặc ý tưởng tự tử"
        ],
        "dosage": {
            "adult_psoriasis": "210mg SC ngày 1, sau đó 210mg SC ngày 8, sau đó 210mg SC mỗi 2 tuần",
            "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn. Test lao trước khi dùng. Có black box warning về tự tử."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên)",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhiễm trùng nấm Candida - tăng nguy cơ",
            "Bệnh viêm ruột (IBD) - tăng nguy cơ, đặc biệt Crohn",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Tự tử, ý tưởng tự tử - NGUY HIỂM, black box warning",
            "Đau đầu",
            "Mệt mỏi",
            "Buồn nôn"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Brodalumab là kháng thể đơn dòng kháng IL-17RA (interleukin-17 receptor A, fully human monoclonal antibody). IL-17RA là thụ thể của IL-17A, IL-17F, và các cytokine IL-17 khác. IL-17A/IL-17F gắn với IL-17RA → kích hoạt signaling → tăng sản xuất các cytokine và chemokine → gây viêm mạn tính → tổn thương mô. Trong vảy nến, IL-17A tăng cao → gây viêm da. Brodalumab gắn với IL-17RA → ngăn chặn IL-17A/IL-17F gắn với receptor → ức chế signaling → giảm viêm. Dẫn đến: giảm triệu chứng trong vảy nến. Brodalumab được dùng để điều trị vảy nến trung bình đến nặng.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Nhiễm trùng nấm Candida - tăng nguy cơ, theo dõi triệu chứng",
            "Bệnh viêm ruột (IBD) - theo dõi triệu chứng tiêu hóa, đặc biệt Crohn",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Tự tử, ý tưởng tự tử - QUAN TRỌNG: theo dõi tâm trạng, hành vi tự tử",
            "Phản ứng tại chỗ tiêm",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng"
        ],
        "precautions": [
            "BLACK BOX WARNING: TỰ TỬ VÀ Ý TƯỞNG TỰ TỬ - theo dõi chặt chẽ tâm trạng và hành vi tự tử",
            "Ngừng brodalumab nếu có ý tưởng tự tử hoặc hành vi tự tử",
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng brodalumab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân có tiền sử IBD - tăng nguy cơ, đặc biệt Crohn",
            "Thận trọng ở bệnh nhân có tiền sử tự tử hoặc trầm cảm",
            "Không dùng vaccine sống trong và sau điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ chính xác, khoảng 2-3 tuần",
            "onset": "Vài tuần",
            "duration": "2 tuần (liều mỗi 2 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
        "black_box_warnings": "TỰ TỬ VÀ Ý TƯỞNG TỰ TỬ - tăng nguy cơ tự tử và ý tưởng tự tử. Theo dõi chặt chẽ tâm trạng và hành vi tự tử. Ngừng ngay nếu có ý tưởng tự tử hoặc hành vi tự tử. NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ bệnh viêm ruột (IBD), đặc biệt Crohn.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Brodalumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị brodalumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng brodalumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Bệnh viêm ruột (IBD) đang hoạt động",
                "Tiền sử tự tử hoặc ý tưởng tự tử"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử lao - cần điều trị dự phòng",
                "Tiền sử IBD - tăng nguy cơ, đặc biệt Crohn",
                "Tiền sử trầm cảm hoặc rối loạn tâm thần - tăng nguy cơ tự tử",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Brodalumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Brodalumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Brodalumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng",
                "Tự tử, ý tưởng tự tử"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng brodalumab",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Đánh giá và điều trị ngay nếu có ý tưởng tự tử hoặc hành vi tự tử",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu phản ứng dị ứng, tâm trạng và hành vi tự tử trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 210mg/1.5ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Brodalumab (Siliq)",
                "UpToDate - Brodalumab: Drug information",
                "Lexicomp - Brodalumab monograph",
                "AAD Guidelines - Psoriasis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Caplacizumab": {
        "group": "Biological - Nanobody (anti-vWF)",
        "vietnamese_name": "Caplacizumab, Cablivi",
        "administration": ["SC"],
        "indications": [
            "TTP (thrombotic thrombocytopenic purpura) - acquired, kết hợp với plasma exchange và immunosuppression"
        ],
        "contraindications": [
            "Dị ứng caplacizumab hoặc bất kỳ thành phần nào",
            "Chảy máu nặng đang hoạt động"
        ],
        "dosage": {
            "adult_loading": "11mg SC ngày 1 (trước plasma exchange đầu tiên), sau đó 11mg SC mỗi ngày",
            "adult_maintenance": "11mg SC mỗi ngày trong ít nhất 30 ngày sau plasma exchange cuối cùng",
            "notes": "Tiêm dưới da. Dùng kết hợp với plasma exchange và immunosuppression (corticosteroid, rituximab). Tiếp tục ít nhất 30 ngày sau plasma exchange cuối cùng hoặc cho đến khi ADAMTS13 activity bình thường."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Chảy máu - phổ biến (chảy máu mũi, chảy máu nướu, chảy máu đường tiêu hóa)",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Đau đầu",
            "Mệt mỏi",
            "Chảy máu nặng - có thể nghiêm trọng",
            "Thiếu máu"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Thuốc chống đông (warfarin, heparin): tăng nguy cơ chảy máu - TRÁNH hoặc thận trọng",
            "Thuốc chống kết tập tiểu cầu (aspirin, clopidogrel): tăng nguy cơ chảy máu - TRÁNH hoặc thận trọng"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Caplacizumab là nanobody (single-domain antibody) kháng vWF (von Willebrand factor). vWF là protein quan trọng cho quá trình kết tập tiểu cầu và đông máu. Trong TTP, thiếu ADAMTS13 (enzyme phân hủy vWF) → vWF không được phân hủy → tăng vWF → tăng kết tập tiểu cầu → hình thành huyết khối → tổn thương vi mạch → TTP. Caplacizumab gắn với vWF → ngăn chặn vWF gắn với platelet receptor (GPIb) → ức chế kết tập tiểu cầu → giảm hình thành huyết khối. Dẫn đến: giảm tổn thương vi mạch và cải thiện triệu chứng trong TTP. Caplacizumab được dùng để điều trị TTP kết hợp với plasma exchange và immunosuppression.",
        "monitoring": [
            "Chảy máu - QUAN TRỌNG: theo dõi chặt chẽ, đặc biệt chảy máu nặng",
            "Platelet - đánh giá hiệu quả điều trị, tăng platelet cho thấy đáp ứng",
            "LDH - giảm LDH cho thấy đáp ứng",
            "Creatinine - cải thiện chức năng thận",
            "ADAMTS13 activity - đánh giá đáp ứng, tiếp tục điều trị cho đến khi bình thường",
            "Hemoglobin - thiếu máu do chảy máu",
            "Phản ứng tại chỗ tiêm"
        ],
        "precautions": [
            "THEO DÕI CHẢY MÁU CHẶT CHẼ - tăng nguy cơ chảy máu, đặc biệt chảy máu nặng",
            "TRÁNH dùng với thuốc chống đông và thuốc chống kết tập tiểu cầu - tăng nguy cơ chảy máu",
            "Ngừng caplacizumab nếu có chảy máu nặng",
            "Dùng kết hợp với plasma exchange và immunosuppression - không dùng đơn độc",
            "Tiếp tục ít nhất 30 ngày sau plasma exchange cuối cùng hoặc cho đến khi ADAMTS13 activity bình thường",
            "Theo dõi platelet, LDH, creatinine để đánh giá đáp ứng",
            "Theo dõi ADAMTS13 activity - tiếp tục cho đến khi bình thường"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ chính xác, khoảng vài giờ",
            "onset": "Nhanh (vài giờ)",
            "duration": "24 giờ (liều mỗi ngày)",
            "protein_binding": "Gắn với vWF",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life ngắn."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
        "black_box_warnings": "CHẢY MÁU NẶNG - tăng nguy cơ chảy máu nghiêm trọng. Theo dõi chặt chẽ. Ngừng ngay nếu có chảy máu nặng. TRÁNH dùng với thuốc chống đông và thuốc chống kết tập tiểu cầu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc chống đông (warfarin, heparin, DOACs)",
                    "mechanism": "Tác dụng cộng dồn chống đông",
                    "effect": "Tăng nguy cơ chảy máu nặng (nguy hiểm)",
                    "management": "TRÁNH dùng cùng. Nếu bắt buộc, theo dõi chặt chẽ và giảm liều thuốc chống đông."
                },
                {
                    "drug": "Thuốc chống kết tập tiểu cầu (aspirin, clopidogrel, ticagrelor)",
                    "mechanism": "Tác dụng cộng dồn ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nặng (nguy hiểm)",
                    "management": "TRÁNH dùng cùng. Nếu bắt buộc, theo dõi chặt chẽ và cân nhắc ngừng thuốc chống kết tập tiểu cầu."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng caplacizumab hoặc bất kỳ thành phần nào",
                "Chảy máu nặng đang hoạt động"
            ],
            "tương_đối": [
                "Chảy máu nhẹ - tăng nguy cơ",
                "Tiền sử chảy máu nặng - tăng nguy cơ",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Caplacizumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (TTP nặng). Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Caplacizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Caplacizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu nặng",
                "Thiếu máu do chảy máu"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng caplacizumab ngay",
                "Điều trị chảy máu: truyền máu, huyết tương, tiểu cầu nếu cần",
                "Theo dõi hemoglobin, platelet",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu chảy máu, hemoglobin, platelet trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 11mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Tiêm trước plasma exchange đầu tiên. Tiếp tục ít nhất 30 ngày sau plasma exchange cuối cùng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Caplacizumab (Cablivi)",
                "UpToDate - Caplacizumab: Drug information",
                "Lexicomp - Caplacizumab monograph",
                "ASH Guidelines - Thrombotic Thrombocytopenic Purpura"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, clinical trial data, widely used"
        }
    },
    
    "Cemiplimab": {
        "group": "Biological - Monoclonal Antibody (anti-PD-1)",
        "vietnamese_name": "Cemiplimab, Libtayo",
        "administration": ["IV"],
        "indications": [
            "Ung thư da tế bào vảy (cutaneous squamous cell carcinoma, cSCC) - locally advanced hoặc metastatic",
            "Ung thư da tế bào đáy (basal cell carcinoma, BCC) - locally advanced hoặc metastatic",
            "Ung thư phổi không tế bào nhỏ (NSCLC) - PD-L1 ≥50%",
            "Ung thư cổ tử cung (recurrent hoặc metastatic)"
        ],
        "contraindications": [
            "Dị ứng cemiplimab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Bệnh tự miễn đang hoạt động nặng"
        ],
        "dosage": {
            "adult_standard": "350mg IV mỗi 3 tuần",
            "notes": "Truyền trong 30 phút. Điều trị đến khi bệnh tiến triển hoặc độc tính không chấp nhận được."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng miễn dịch (immune-related adverse events, irAEs) - NGUY HIỂM, phổ biến",
            "Viêm phổi do miễn dịch (pneumonitis) - có thể tử vong",
            "Viêm đại tràng (colitis) - có thể tử vong",
            "Viêm gan (hepatitis) - có thể tử vong",
            "Viêm nội tiết (endocrinopathies): viêm tuyến giáp, viêm tuyến yên, viêm tuyến thượng thận - có thể vĩnh viễn",
            "Viêm da (dermatitis, rash)",
            "Viêm cơ tim (myocarditis) - hiếm nhưng nghiêm trọng",
            "Viêm thần kinh (neuropathy)",
            "Phản ứng truyền (infusion reaction) - hiếm",
            "Mệt mỏi",
            "Ngứa, phát ban",
            "Buồn nôn, tiêu chảy"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ phản ứng miễn dịch khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Cemiplimab là kháng thể đơn dòng kháng PD-1 (programmed death-1, fully human monoclonal antibody). PD-1 là thụ thể ức chế trên tế bào T, khi gắn với PD-L1/PD-L2 (ligands trên tế bào ung thư và tế bào miễn dịch) → ức chế hoạt động tế bào T → tế bào T không thể tiêu diệt tế bào ung thư (immune evasion). Cemiplimab gắn với PD-1 → ngăn chặn PD-1 gắn với PD-L1/PD-L2 → giải phóng ức chế tế bào T → tế bào T hoạt động trở lại → tiêu diệt tế bào ung thư. Dẫn đến: tăng đáp ứng miễn dịch chống ung thư. Cemiplimab được dùng để điều trị ung thư da tế bào vảy và các loại ung thư khác có PD-L1 dương tính.",
        "monitoring": [
            "Phản ứng miễn dịch (irAEs) - QUAN TRỌNG: theo dõi chặt chẽ trong và sau điều trị",
            "Viêm phổi: khó thở, ho, đau ngực - chụp X-quang ngực nếu có triệu chứng",
            "Viêm đại tràng: tiêu chảy, đau bụng, phân có máu - nội soi nếu cần",
            "Viêm gan: vàng da, mệt mỏi, đau bụng - ALT, AST, bilirubin mỗi chu kỳ",
            "Viêm nội tiết: TSH, T4 (tuyến giáp), cortisol (tuyến thượng thận), glucose - mỗi chu kỳ",
            "Viêm cơ tim: đau ngực, khó thở, nhịp tim nhanh - troponin, ECG, echo nếu có triệu chứng",
            "Chức năng thận: creatinine, eGFR - mỗi chu kỳ",
            "Công thức máu: CBC - mỗi chu kỳ",
            "Dấu hiệu phản ứng truyền"
        ],
        "precautions": [
            "THEO DÕI PHẢN ỨNG MIỄN DỊCH (irAEs) CHẶT CHẼ - có thể nghiêm trọng và tử vong",
            "Ngừng cemiplimab và điều trị ngay nếu có irAE độ 3-4 (corticosteroid, immunosuppressant)",
            "Viêm phổi: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid liều cao",
            "Viêm đại tràng: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid, infliximab nếu cần",
            "Viêm gan: ngừng nếu ALT/AST >5x ULN, điều trị với corticosteroid",
            "Viêm nội tiết: có thể vĩnh viễn, cần điều trị thay thế hormone",
            "Viêm cơ tim: ngừng ngay, điều trị với corticosteroid liều cao",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh tự miễn đang hoạt động",
            "Thận trọng ở bệnh nhân đã cấy ghép tạng - tăng nguy cơ thải ghép"
        ],
        "pharmacokinetics": {
            "half_life": "19 ngày (dao động 12-25 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "3 tuần (liều mỗi 3 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "PHẢN ỨNG MIỄN DỊCH (immune-related adverse events, irAEs) - có thể nghiêm trọng và tử vong. Viêm phổi, viêm đại tràng, viêm gan, viêm nội tiết, viêm cơ tim có thể xảy ra. Ngừng và điều trị ngay nếu có irAE độ 3-4. Có thể gây tử vong thai nhi (category D).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Corticosteroid (liều cao, kéo dài)",
                    "mechanism": "Corticosteroid ức chế miễn dịch, có thể làm giảm hiệu quả cemiplimab",
                    "effect": "Có thể làm giảm đáp ứng điều trị",
                    "management": "Tránh dùng corticosteroid liều cao kéo dài trước điều trị. Có thể dùng để điều trị irAEs."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Cemiplimab làm thay đổi đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị cemiplimab. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cemiplimab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Bệnh tự miễn đang hoạt động nặng - tăng nguy cơ irAEs",
                "Đã cấy ghép tạng - tăng nguy cơ thải ghép",
                "Viêm phổi đang hoạt động - tăng nguy cơ viêm phổi do miễn dịch",
                "Viêm đại tràng đang hoạt động - tăng nguy cơ viêm đại tràng do miễn dịch",
                "Có thai (category D) - có thể gây tử vong thai nhi"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Cemiplimab là FDA category D - có thể gây tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rủi ro. Có thể gây dị tật bẩm sinh và tử vong thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Cemiplimab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Cemiplimab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chặt chẽ viêm gan do miễn dịch."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng miễn dịch nặng (irAEs độ 3-4)",
                "Phản ứng truyền nặng",
                "Viêm phổi nặng",
                "Viêm đại tràng nặng",
                "Viêm gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị irAEs.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị irAEs: corticosteroid liều cao (methylprednisolone 1-2mg/kg/ngày), immunosuppressant (infliximab cho viêm đại tràng) nếu cần",
                "Điều trị viêm phổi: corticosteroid liều cao, hỗ trợ hô hấp nếu cần",
                "Điều trị viêm đại tràng: corticosteroid, infliximab nếu không đáp ứng",
                "Điều trị viêm gan: corticosteroid, hỗ trợ gan nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu irAEs, chức năng gan, thận, nội tiết trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 1-10mg/ml. Không lọc.",
                "infusion_rate": "Truyền trong 30 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Không cần premedication thường quy. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi phản ứng miễn dịch."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cemiplimab (Libtayo)",
                "UpToDate - Cemiplimab: Drug information",
                "Lexicomp - Cemiplimab monograph",
                "NCCN Guidelines - Cutaneous Squamous Cell Carcinoma"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Certolizumab pegol": {
        "group": "Biological - Monoclonal Antibody (anti-TNF-α, pegylated)",
        "vietnamese_name": "Certolizumab pegol, Cimzia",
        "administration": ["SC"],
        "indications": [
            "Viêm khớp dạng thấp (RA)",
            "Bệnh Crohn (Crohn's disease)",
            "Viêm khớp vảy nến (PsA)",
            "Viêm cột sống dính khớp (AS)",
            "Vảy nến (psoriasis)"
        ],
        "contraindications": [
            "Dị ứng certolizumab pegol hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Suy tim nặng (NYHA class III-IV)",
            "Bệnh lao đang hoạt động"
        ],
        "dosage": {
            "adult_ra": "400mg SC ngày 0, 2, 4 tuần, sau đó 200mg SC mỗi 2 tuần (hoặc 400mg SC mỗi 4 tuần)",
            "adult_crohn": "400mg SC ngày 0, 2, 4 tuần, sau đó 400mg SC mỗi 4 tuần",
            "adult_psa": "400mg SC ngày 0, 2, 4 tuần, sau đó 200mg SC mỗi 2 tuần",
            "adult_as": "400mg SC ngày 0, 2, 4 tuần, sau đó 200mg SC mỗi 2 tuần",
            "notes": "Tiêm dưới da. Test lao trước khi dùng. Certolizumab pegol là anti-TNF-α được pegylated, không có Fc region nên không qua nhau thai."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng cơ hội, lao)",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
            "Suy tim - có thể làm nặng",
            "Bệnh lý thần kinh (demyelinating disease) - hiếm",
            "Giảm bạch cầu, tiểu cầu - hiếm",
            "Tăng men gan",
            "Buồn nôn, đau đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Certolizumab pegol là kháng thể đơn dòng kháng TNF-α được pegylated (Fab fragment của anti-TNF-α gắn với polyethylene glycol, không có Fc region). TNF-α là cytokine tiền viêm quan trọng, được sản xuất bởi đại thực bào và tế bào T, đóng vai trò trong quá trình viêm. Trong các bệnh tự miễn (RA, Crohn, PsA, AS), TNF-α tăng cao → gây viêm mạn tính → tổn thương mô. Certolizumab pegol gắn với TNF-α → ngăn chặn TNF-α gắn với thụ thể → ức chế tín hiệu viêm → giảm viêm và tổn thương mô. Pegylation làm tăng half-life. Không có Fc region nên không qua nhau thai, an toàn hơn trong thai kỳ. Dẫn đến: giảm triệu chứng và làm chậm tiến triển bệnh.",
        "monitoring": [
            "Phản ứng tại chỗ tiêm",
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng",
            "Dấu hiệu suy tim (nếu có tiền sử)",
            "Dấu hiệu bệnh lý thần kinh (nếu có triệu chứng)"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt và nghiêm trọng",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
            "Ngừng certolizumab pegol nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân suy tim - có thể làm nặng",
            "Thận trọng ở bệnh nhân có tiền sử ung thư - tăng nguy cơ ung thư",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh lý thần kinh demyelinating",
            "An toàn hơn trong thai kỳ do không có Fc region (không qua nhau thai)"
        ],
        "pharmacokinetics": {
            "half_life": "14 ngày (dao động 10-20 ngày)",
            "onset": "Vài tuần",
            "duration": "2-4 tuần (liều mỗi 2-4 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác. Pegylation làm tăng half-life.",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài do pegylation."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 15-30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng, đặc biệt lao và nhiễm trùng cơ hội. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ ung thư (lymphoma, ung thư da). Suy tim - có thể làm nặng, ngừng nếu suy tim mới hoặc nặng hơn.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (methotrexate, azathioprine, 6-mercaptopurine)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Certolizumab pegol làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị certolizumab pegol. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng certolizumab pegol hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Bệnh lao đang hoạt động",
                "Suy tim nặng (NYHA class III-IV)"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Suy tim nhẹ đến trung bình (NYHA class I-II) - có thể làm nặng",
                "Tiền sử lao - cần điều trị dự phòng",
                "Tiền sử ung thư - tăng nguy cơ",
                "Bệnh lý thần kinh demyelinating - có thể làm nặng",
                "Có thai (category B) - thận trọng, nhưng an toàn hơn do không qua nhau thai"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Certolizumab pegol là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Không có Fc region nên không qua nhau thai, an toàn hơn các anti-TNF khác trong thai kỳ. Một số nghiên cứu cho thấy an toàn trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Certolizumab pegol bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Certolizumab pegol không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chức năng gan (có thể tăng men gan)."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng",
                "Giảm bạch cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng certolizumab pegol",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi công thức máu",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, công thức máu trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 200mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 15-30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Certolizumab pegol (Cimzia)",
                "UpToDate - Certolizumab pegol: Drug information",
                "Lexicomp - Certolizumab pegol monograph",
                "ACR Guidelines - Rheumatoid Arthritis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Dostarlimab": {
        "group": "Biological - Monoclonal Antibody (anti-PD-1)",
        "vietnamese_name": "Dostarlimab, Jemperli",
        "administration": ["IV"],
        "indications": [
            "Ung thư nội mạc tử cung (endometrial cancer) - dMMR/MSI-H, recurrent hoặc advanced",
            "Ung thư nội mạc tử cung (endometrial cancer) - dMMR/MSI-H, first-line treatment",
            "Ung thư đại trực tràng (colorectal cancer) - dMMR/MSI-H, recurrent hoặc advanced",
            "Các loại ung thư solid tumors - dMMR/MSI-H (tumor-agnostic indication)"
        ],
        "contraindications": [
            "Dị ứng dostarlimab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Bệnh tự miễn đang hoạt động nặng"
        ],
        "dosage": {
            "adult_loading": "500mg IV mỗi 3 tuần x 4 liều",
            "adult_maintenance": "1000mg IV mỗi 6 tuần",
            "notes": "Truyền trong 30 phút. Loading dose: 4 liều đầu tiên mỗi 3 tuần, sau đó chuyển sang maintenance mỗi 6 tuần. Điều trị đến khi bệnh tiến triển hoặc độc tính không chấp nhận được."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng miễn dịch (immune-related adverse events, irAEs) - NGUY HIỂM, phổ biến",
            "Viêm phổi do miễn dịch (pneumonitis) - có thể tử vong",
            "Viêm đại tràng (colitis) - có thể tử vong",
            "Viêm gan (hepatitis) - có thể tử vong",
            "Viêm nội tiết (endocrinopathies): viêm tuyến giáp, viêm tuyến yên, viêm tuyến thượng thận - có thể vĩnh viễn",
            "Viêm da (dermatitis, rash)",
            "Viêm cơ tim (myocarditis) - hiếm nhưng nghiêm trọng",
            "Viêm thần kinh (neuropathy)",
            "Phản ứng truyền (infusion reaction) - hiếm",
            "Mệt mỏi",
            "Ngứa, phát ban",
            "Buồn nôn, tiêu chảy",
            "Thiếu máu"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ phản ứng miễn dịch khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Dostarlimab là kháng thể đơn dòng kháng PD-1 (programmed death-1, humanized monoclonal antibody). PD-1 là thụ thể ức chế trên tế bào T, khi gắn với PD-L1/PD-L2 (ligands trên tế bào ung thư và tế bào miễn dịch) → ức chế hoạt động tế bào T → tế bào T không thể tiêu diệt tế bào ung thư (immune evasion). Dostarlimab gắn với PD-1 → ngăn chặn PD-1 gắn với PD-L1/PD-L2 → giải phóng ức chế tế bào T → tế bào T hoạt động trở lại → tiêu diệt tế bào ung thư. Dẫn đến: tăng đáp ứng miễn dịch chống ung thư. Dostarlimab được FDA phê duyệt đặc biệt cho ung thư có dMMR/MSI-H (deficient mismatch repair/microsatellite instability-high), một biomarker cho thấy đáp ứng tốt với immunotherapy. ĐẶC ĐIỂM: (1) FDA phê duyệt 2021, (2) Chỉ định đặc biệt cho dMMR/MSI-H tumors (tumor-agnostic), (3) Loading dose: 4 liều đầu mỗi 3 tuần, sau đó maintenance mỗi 6 tuần, (4) Hiệu quả cao ở ung thư nội mạc tử cung dMMR/MSI-H.",
        "monitoring": [
            "Phản ứng miễn dịch (irAEs) - QUAN TRỌNG: theo dõi chặt chẽ trong và sau điều trị",
            "Viêm phổi: khó thở, ho, đau ngực - chụp X-quang ngực nếu có triệu chứng",
            "Viêm đại tràng: tiêu chảy, đau bụng, phân có máu - nội soi nếu cần",
            "Viêm gan: vàng da, mệt mỏi, đau bụng - ALT, AST, bilirubin mỗi chu kỳ",
            "Viêm nội tiết: TSH, T4 (tuyến giáp), cortisol (tuyến thượng thận), glucose - mỗi chu kỳ",
            "Viêm cơ tim: đau ngực, khó thở, nhịp tim nhanh - troponin, ECG, echo nếu có triệu chứng",
            "Chức năng thận: creatinine, eGFR - mỗi chu kỳ",
            "Công thức máu: CBC - mỗi chu kỳ (theo dõi thiếu máu)",
            "Dấu hiệu phản ứng truyền",
            "Đáp ứng điều trị: CT scan, MRI mỗi 2-3 chu kỳ"
        ],
        "precautions": [
            "THEO DÕI PHẢN ỨNG MIỄN DỊCH (irAEs) CHẶT CHẼ - có thể nghiêm trọng và tử vong",
            "Ngừng dostarlimab và điều trị ngay nếu có irAE độ 3-4 (corticosteroid, immunosuppressant)",
            "Viêm phổi: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid liều cao",
            "Viêm đại tràng: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid, infliximab nếu cần",
            "Viêm gan: ngừng nếu ALT/AST >5x ULN, điều trị với corticosteroid",
            "Viêm nội tiết: có thể vĩnh viễn, cần điều trị thay thế hormone",
            "Viêm cơ tim: ngừng ngay, điều trị với corticosteroid liều cao",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh tự miễn đang hoạt động",
            "Thận trọng ở bệnh nhân đã cấy ghép tạng - tăng nguy cơ thải ghép",
            "Chỉ định đặc biệt cho dMMR/MSI-H tumors - cần test biomarker trước điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "~20 ngày (dao động 15-25 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "3 tuần (loading), 6 tuần (maintenance)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES), tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "PHẢN ỨNG MIỄN DỊCH (immune-related adverse events, irAEs) - có thể nghiêm trọng và tử vong. Viêm phổi, viêm đại tràng, viêm gan, viêm nội tiết, viêm cơ tim có thể xảy ra. Ngừng và điều trị ngay nếu có irAE độ 3-4. Có thể gây tử vong thai nhi (category D).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Corticosteroid (liều cao, kéo dài)",
                    "mechanism": "Corticosteroid ức chế miễn dịch, có thể làm giảm hiệu quả dostarlimab",
                    "effect": "Có thể làm giảm đáp ứng điều trị",
                    "management": "Tránh dùng corticosteroid liều cao kéo dài trước điều trị. Có thể dùng để điều trị irAEs."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Dostarlimab làm thay đổi đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị dostarlimab. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng dostarlimab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Bệnh tự miễn đang hoạt động nặng - tăng nguy cơ irAEs",
                "Đã cấy ghép tạng - tăng nguy cơ thải ghép",
                "Viêm phổi đang hoạt động - tăng nguy cơ viêm phổi do miễn dịch",
                "Viêm đại tràng đang hoạt động - tăng nguy cơ viêm đại tràng do miễn dịch",
                "Có thai (category D) - có thể gây tử vong thai nhi"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Dostarlimab là FDA category D - có thể gây tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rủi ro. Có thể gây dị tật bẩm sinh và tử vong thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Dostarlimab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Dostarlimab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chặt chẽ viêm gan do miễn dịch."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng miễn dịch nặng (irAEs độ 3-4)",
                "Phản ứng truyền nặng",
                "Viêm phổi nặng",
                "Viêm đại tràng nặng",
                "Viêm gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị irAEs.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị irAEs: corticosteroid liều cao (methylprednisolone 1-2mg/kg/ngày), immunosuppressant (infliximab cho viêm đại tràng) nếu cần",
                "Điều trị viêm phổi: corticosteroid liều cao, hỗ trợ hô hấp nếu cần",
                "Điều trị viêm đại tràng: corticosteroid, infliximab nếu không đáp ứng",
                "Điều trị viêm gan: corticosteroid, hỗ trợ gan nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu irAEs, chức năng gan, thận, nội tiết trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 1-10mg/ml. Không lọc.",
                "infusion_rate": "Truyền trong 30 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Không cần premedication thường quy. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi phản ứng miễn dịch. Loading dose: 4 liều đầu mỗi 3 tuần, sau đó maintenance mỗi 6 tuần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dostarlimab (Jemperli)",
                "UpToDate - Dostarlimab: Drug information",
                "Lexicomp - Dostarlimab monograph",
                "NCCN Guidelines - Endometrial Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved (2021), clinical trial data, tumor-agnostic indication for dMMR/MSI-H"
        }
    },
    
    "Durvalumab": {
        "group": "Biological - Monoclonal Antibody (anti-PD-L1)",
        "vietnamese_name": "Durvalumab, Imfinzi",
        "administration": ["IV"],
        "indications": [
            "Ung thư phổi không tế bào nhỏ (NSCLC) giai đoạn III - sau hóa xạ trị",
            "Ung thư phổi không tế bào nhỏ (NSCLC) giai đoạn IV",
            "Ung thư phổi tế bào nhỏ (SCLC)",
            "Ung thư bàng quang (urothelial carcinoma)",
            "Ung thư gan (HCC)",
            "Ung thư đường mật (biliary tract cancer)"
        ],
        "contraindications": [
            "Dị ứng durvalumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Bệnh tự miễn đang hoạt động nặng"
        ],
        "dosage": {
            "adult_standard": "10mg/kg IV mỗi 2 tuần, hoặc 1500mg IV mỗi 4 tuần",
            "adult_combination": "1500mg IV mỗi 3 tuần (kết hợp với chemotherapy)",
            "notes": "Truyền trong 60 phút. Có thể dùng đơn trị hoặc kết hợp với chemotherapy. Điều trị đến khi bệnh tiến triển hoặc độc tính không chấp nhận được. Đối với NSCLC giai đoạn III: điều trị đến 12 tháng sau hóa xạ trị."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng miễn dịch (immune-related adverse events, irAEs) - NGUY HIỂM, phổ biến",
            "Viêm phổi do miễn dịch (pneumonitis) - có thể tử vong, đặc biệt sau hóa xạ trị",
            "Viêm đại tràng (colitis) - có thể tử vong",
            "Viêm gan (hepatitis) - có thể tử vong",
            "Viêm nội tiết (endocrinopathies): viêm tuyến giáp, viêm tuyến yên, viêm tuyến thượng thận - có thể vĩnh viễn",
            "Viêm da (dermatitis, rash)",
            "Viêm cơ tim (myocarditis) - hiếm nhưng nghiêm trọng",
            "Viêm thần kinh (neuropathy)",
            "Phản ứng truyền (infusion reaction) - hiếm",
            "Mệt mỏi",
            "Ngứa, phát ban",
            "Buồn nôn, tiêu chảy",
            "Ho, khó thở (đặc biệt sau hóa xạ trị)",
            "Giảm bạch cầu, tiểu cầu (khi kết hợp với chemotherapy)"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ viêm phổi khi dùng sau hóa xạ trị"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Durvalumab là kháng thể đơn dòng kháng PD-L1 (programmed death-ligand 1, human monoclonal antibody). PD-L1 là ligand trên tế bào ung thư và tế bào miễn dịch, khi gắn với PD-1 trên tế bào T → ức chế hoạt động tế bào T → tế bào T không thể tiêu diệt tế bào ung thư (immune evasion). Durvalumab gắn với PD-L1 → ngăn chặn PD-L1 gắn với PD-1 → giải phóng ức chế tế bào T → tế bào T hoạt động trở lại → tiêu diệt tế bào ung thư. Dẫn đến: tăng đáp ứng miễn dịch chống ung thư. Durvalumab được dùng để điều trị ung thư phổi giai đoạn III sau hóa xạ trị (consolidation therapy) và nhiều loại ung thư khác có PD-L1 dương tính.",
        "monitoring": [
            "Phản ứng miễn dịch (irAEs) - QUAN TRỌNG: theo dõi chặt chẽ trong và sau điều trị",
            "Viêm phổi: khó thở, ho, đau ngực - CHẶT CHẼ sau hóa xạ trị, chụp X-quang ngực nếu có triệu chứng",
            "Viêm đại tràng: tiêu chảy, đau bụng, phân có máu - nội soi nếu cần",
            "Viêm gan: vàng da, mệt mỏi, đau bụng - ALT, AST, bilirubin mỗi chu kỳ",
            "Viêm nội tiết: TSH, T4 (tuyến giáp), cortisol (tuyến thượng thận), glucose - mỗi chu kỳ",
            "Viêm cơ tim: đau ngực, khó thở, nhịp tim nhanh - troponin, ECG, echo nếu có triệu chứng",
            "Chức năng thận: creatinine, eGFR - mỗi chu kỳ",
            "Công thức máu: CBC - mỗi chu kỳ",
            "Dấu hiệu phản ứng truyền"
        ],
        "precautions": [
            "THEO DÕI PHẢN ỨNG MIỄN DỊCH (irAEs) CHẶT CHẼ - có thể nghiêm trọng và tử vong",
            "THEO DÕI VIÊM PHỔI CHẶT CHẼ SAU HÓA XẠ TRỊ - tăng nguy cơ viêm phổi do miễn dịch",
            "Ngừng durvalumab và điều trị ngay nếu có irAE độ 3-4 (corticosteroid, immunosuppressant)",
            "Viêm phổi: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid liều cao",
            "Viêm đại tràng: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid, infliximab nếu cần",
            "Viêm gan: ngừng nếu ALT/AST >5x ULN, điều trị với corticosteroid",
            "Viêm nội tiết: có thể vĩnh viễn, cần điều trị thay thế hormone",
            "Viêm cơ tim: ngừng ngay, điều trị với corticosteroid liều cao",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh tự miễn đang hoạt động",
            "Thận trọng ở bệnh nhân đã cấy ghép tạng - tăng nguy cơ thải ghép"
        ],
        "pharmacokinetics": {
            "half_life": "17 ngày (dao động 10-25 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "2-4 tuần (liều mỗi 2-4 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "PHẢN ỨNG MIỄN DỊCH (immune-related adverse events, irAEs) - có thể nghiêm trọng và tử vong. Viêm phổi, viêm đại tràng, viêm gan, viêm nội tiết, viêm cơ tim có thể xảy ra. Tăng nguy cơ viêm phổi sau hóa xạ trị. Ngừng và điều trị ngay nếu có irAE độ 3-4. Có thể gây tử vong thai nhi (category D).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Hóa xạ trị (chemoradiation)",
                    "mechanism": "Cả hai đều có thể gây viêm phổi, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ viêm phổi do miễn dịch nghiêm trọng",
                    "management": "Theo dõi chặt chẽ viêm phổi sau hóa xạ trị. Ngừng durvalumab nếu có viêm phổi độ 3-4."
                },
                {
                    "drug": "Corticosteroid (liều cao, kéo dài)",
                    "mechanism": "Corticosteroid ức chế miễn dịch, có thể làm giảm hiệu quả durvalumab",
                    "effect": "Có thể làm giảm đáp ứng điều trị",
                    "management": "Tránh dùng corticosteroid liều cao kéo dài trước điều trị. Có thể dùng để điều trị irAEs."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Durvalumab làm thay đổi đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị durvalumab. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng durvalumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Bệnh tự miễn đang hoạt động nặng - tăng nguy cơ irAEs",
                "Đã cấy ghép tạng - tăng nguy cơ thải ghép",
                "Viêm phổi đang hoạt động - tăng nguy cơ viêm phổi do miễn dịch",
                "Viêm đại tràng đang hoạt động - tăng nguy cơ viêm đại tràng do miễn dịch",
                "Sau hóa xạ trị - tăng nguy cơ viêm phổi",
                "Có thai (category D) - có thể gây tử vong thai nhi"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Durvalumab là FDA category D - có thể gây tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rủi ro. Có thể gây dị tật bẩm sinh và tử vong thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Durvalumab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Durvalumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chặt chẽ viêm gan do miễn dịch."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng miễn dịch nặng (irAEs độ 3-4)",
                "Phản ứng truyền nặng",
                "Viêm phổi nặng",
                "Viêm đại tràng nặng",
                "Viêm gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị irAEs.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị irAEs: corticosteroid liều cao (methylprednisolone 1-2mg/kg/ngày), immunosuppressant (infliximab cho viêm đại tràng) nếu cần",
                "Điều trị viêm phổi: corticosteroid liều cao, hỗ trợ hô hấp nếu cần",
                "Điều trị viêm đại tràng: corticosteroid, infliximab nếu không đáp ứng",
                "Điều trị viêm gan: corticosteroid, hỗ trợ gan nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu irAEs, chức năng gan, thận, nội tiết trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 1-15mg/ml. Không lọc.",
                "infusion_rate": "Truyền trong 60 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Không cần premedication thường quy. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi phản ứng miễn dịch, đặc biệt viêm phổi sau hóa xạ trị."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Durvalumab (Imfinzi)",
                "UpToDate - Durvalumab: Drug information",
                "Lexicomp - Durvalumab monograph",
                "NCCN Guidelines - Lung Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Eculizumab": {
        "group": "Biological - Monoclonal Antibody (anti-C5)",
        "vietnamese_name": "Eculizumab, Soliris",
        "administration": ["IV"],
        "indications": [
            "Paroxysmal nocturnal hemoglobinuria (PNH)",
            "Atypical hemolytic uremic syndrome (aHUS)",
            "Myasthenia gravis (MG) - anti-AChR dương tính",
            "Neuromyelitis optica spectrum disorder (NMOSD) - anti-AQP4 dương tính"
        ],
        "contraindications": [
            "Dị ứng eculizumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng Neisseria meningitidis chưa điều trị",
            "Chưa được tiêm vaccine meningococcal"
        ],
        "dosage": {
            "adult_pnh": "600mg IV mỗi tuần x 4 tuần, sau đó 900mg IV tuần thứ 5, sau đó 900mg IV mỗi 2 tuần",
            "adult_ahus": "900mg IV mỗi tuần x 4 tuần, sau đó 1200mg IV tuần thứ 5, sau đó 1200mg IV mỗi 2 tuần",
            "adult_mg": "900mg IV mỗi tuần x 4 tuần, sau đó 1200mg IV tuần thứ 5, sau đó 1200mg IV mỗi 2 tuần",
            "adult_nmosd": "900mg IV mỗi tuần x 4 tuần, sau đó 1200mg IV tuần thứ 5, sau đó 1200mg IV mỗi 2 tuần",
            "pediatric_ahus": "Weight-based IV: 600mg nếu 40-60kg, 900mg nếu >60kg, mỗi tuần x 4 tuần, sau đó maintenance",
            "notes": "Truyền trong 25-45 phút. TIÊM VACCINE MENINGOCOCCAL TRƯỚC KHI BẮT ĐẦU. Điều trị dự phòng kháng sinh nếu cần."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng Neisseria meningitidis - NGUY HIỂM, có thể tử vong",
            "Nhiễm trùng nặng khác - tăng nguy cơ",
            "Phản ứng truyền (infusion reaction) - phổ biến",
            "Đau đầu",
            "Buồn nôn",
            "Mệt mỏi",
            "Đau cơ, đau khớp",
            "Phản ứng dị ứng - hiếm"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Eculizumab là kháng thể đơn dòng kháng C5 (complement component 5, humanized monoclonal antibody). Complement system là một phần quan trọng của hệ miễn dịch bẩm sinh, giúp tiêu diệt vi khuẩn và tế bào lạ. C5 là thành phần quan trọng trong complement cascade, khi được kích hoạt → tạo thành C5a (anaphylatoxin) và C5b (bắt đầu hình thành MAC - membrane attack complex) → MAC tạo lỗ trên màng tế bào → tiêu diệt tế bào. Trong PNH, aHUS, MG, và NMOSD, complement system hoạt động quá mức → gây tổn thương tế bào. Eculizumab gắn với C5 → ngăn chặn C5 được chia cắt thành C5a và C5b → ức chế hình thành MAC → giảm tổn thương tế bào. Dẫn đến: giảm tan máu trong PNH, giảm tổn thương thận trong aHUS, giảm tổn thương thần kinh trong MG và NMOSD.",
        "monitoring": [
            "Nhiễm trùng Neisseria meningitidis - QUAN TRỌNG: theo dõi dấu hiệu viêm màng não (sốt, đau đầu, cứng cổ, phát ban)",
            "Nhiễm trùng nặng khác - theo dõi dấu hiệu nhiễm trùng",
            "Công thức máu (CBC) - trong PNH, theo dõi tan máu",
            "Chức năng thận (creatinine, eGFR) - trong aHUS, theo dõi tổn thương thận",
            "Chức năng gan (ALT, AST) - trong aHUS",
            "LDH - trong PNH, tăng LDH cho thấy tan máu",
            "Phản ứng truyền",
            "Dấu hiệu viêm màng não - ngay lập tức nếu có triệu chứng"
        ],
        "precautions": [
            "BLACK BOX WARNING: NHIỄM TRÙNG NEISSERIA MENINGITIDIS - có thể tử vong",
            "TIÊM VACCINE MENINGOCOCCAL TRƯỚC KHI BẮT ĐẦU (ít nhất 2 tuần trước)",
            "Điều trị dự phòng kháng sinh (penicillin hoặc tương đương) nếu chưa tiêm vaccine hoặc vaccine chưa có hiệu lực",
            "Theo dõi dấu hiệu viêm màng não chặt chẽ - điều trị ngay nếu nghi ngờ",
            "Giáo dục bệnh nhân về dấu hiệu viêm màng não",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng eculizumab nếu có nhiễm trùng nặng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động"
        ],
        "pharmacokinetics": {
            "half_life": "272 giờ (khoảng 11 ngày)",
            "onset": "Vài tuần",
            "duration": "1-2 tuần (liều mỗi 1-2 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "NHIỄM TRÙNG NEISSERIA MENINGITIDIS - có thể tử vong. Eculizumab làm tăng nguy cơ nhiễm trùng Neisseria meningitidis nghiêm trọng và đe dọa tính mạng. Tiêm vaccine meningococcal trước khi bắt đầu (ít nhất 2 tuần trước). Điều trị dự phòng kháng sinh nếu cần. Theo dõi dấu hiệu viêm màng não chặt chẽ. Điều trị ngay nếu nghi ngờ viêm màng não.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Eculizumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị eculizumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                },
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng eculizumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng Neisseria meningitidis chưa điều trị",
                "Chưa được tiêm vaccine meningococcal (trừ trường hợp khẩn cấp với điều trị dự phòng kháng sinh)"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Chưa tiêm vaccine meningococcal đủ 2 tuần - cần điều trị dự phòng kháng sinh",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Eculizumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (PNH, aHUS nặng). Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Eculizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Eculizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng Neisseria meningitidis",
                "Nhiễm trùng nặng khác",
                "Phản ứng truyền nặng",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị nhiễm trùng Neisseria meningitidis ngay nếu nghi ngờ: ceftriaxone IV + điều trị hỗ trợ",
                "Điều trị nhiễm trùng nặng khác nếu có",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine, epinephrine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu viêm màng não, dấu hiệu nhiễm trùng, phản ứng truyền, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 5mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 25-45 phút.",
                "compatibility": ["NS"],
                "incompatibility": ["D5W", "Không pha với các thuốc khác"],
                "notes": "Không cần premedication thường quy. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi dấu hiệu viêm màng não."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Eculizumab (Soliris)",
                "UpToDate - Eculizumab: Drug information",
                "Lexicomp - Eculizumab monograph",
                "ASH Guidelines - PNH"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Efgartigimod": {
        "group": "Biological - FcRn Blocker (anti-FcRn)",
        "vietnamese_name": "Efgartigimod, Vyvgart",
        "administration": ["IV"],
        "indications": [
            "Nhược cơ (myasthenia gravis) - kháng acetylcholine receptor (AChR) dương tính, generalized"
        ],
        "contraindications": [
            "Dị ứng efgartigimod hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult": "10mg/kg IV mỗi tuần x 4 tuần, sau đó điều chỉnh theo đáp ứng",
            "notes": "Truyền trong 1 giờ. Có thể lặp lại đợt điều trị nếu triệu chứng tái phát."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)",
            "Phản ứng truyền (infusion reaction) - phổ biến lần đầu: sốt, ớn lạnh, đau đầu, buồn nôn",
            "Đau đầu",
            "Buồn nôn",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Giảm IgG - có thể xảy ra do cơ chế tác dụng"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Có thể làm giảm hiệu quả immunoglobulin therapy"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Efgartigimod là kháng thể đơn dòng kháng FcRn (neonatal Fc receptor, humanized monoclonal antibody). FcRn là receptor quan trọng cho sự sống của IgG trong cơ thể. FcRn bảo vệ IgG khỏi bị phân hủy → kéo dài half-life của IgG. Trong myasthenia gravis, autoantibodies (IgG) tấn công acetylcholine receptor → gây yếu cơ. Efgartigimod gắn với FcRn → ngăn chặn FcRn bảo vệ IgG → tăng phân hủy IgG (bao gồm cả autoantibodies) → giảm nồng độ autoantibodies → giảm tấn công acetylcholine receptor → cải thiện yếu cơ. Dẫn đến: giảm triệu chứng và cải thiện chức năng trong myasthenia gravis. Efgartigimod được dùng để điều trị myasthenia gravis generalized, kháng AChR dương tính.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Phản ứng truyền - QUAN TRỌNG: theo dõi trong và sau truyền, đặc biệt lần đầu",
            "Triệu chứng myasthenia gravis (yếu cơ, mệt mỏi) - đánh giá hiệu quả điều trị",
            "IgG máu - có thể giảm do cơ chế tác dụng",
            "Tự kháng thể AChR - có thể giảm",
            "Dấu hiệu nhiễm trùng nặng"
        ],
        "precautions": [
            "THEO DÕI NHIỄM TRÙNG CHẶT CHẼ - tăng nguy cơ nhiễm trùng do giảm IgG",
            "Ngừng efgartigimod nếu có nhiễm trùng nặng",
            "Theo dõi phản ứng truyền chặt chẽ, đặc biệt lần đầu",
            "IgG có thể giảm - theo dõi, có thể cần bổ sung immunoglobulin nếu giảm quá mức",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động",
            "Có thể cần lặp lại đợt điều trị nếu triệu chứng tái phát"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ chính xác, khoảng vài ngày",
            "onset": "Vài tuần",
            "duration": "1 tuần (liều mỗi tuần), tác dụng có thể kéo dài vài tuần sau đợt điều trị",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng do giảm IgG. Ngừng nếu có nhiễm trùng nặng. Giảm IgG có thể làm tăng nguy cơ nhiễm trùng.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Efgartigimod làm giảm IgG, giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị efgartigimod. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                },
                {
                    "drug": "Immunoglobulin therapy (IVIG)",
                    "mechanism": "Efgartigimod làm giảm IgG, có thể làm giảm hiệu quả IVIG",
                    "effect": "Giảm hiệu quả IVIG",
                    "management": "Thận trọng. Có thể cần điều chỉnh liều IVIG hoặc thời gian dùng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng efgartigimod hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Giảm IgG nặng - tăng nguy cơ nhiễm trùng",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Efgartigimod là FDA category C. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Efgartigimod bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Efgartigimod không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở)",
                "Giảm IgG nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Bổ sung immunoglobulin (IVIG) nếu giảm IgG nặng",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, phản ứng truyền, IgG máu trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 0.5-2mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 1 giờ.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Ngừng ngay nếu có phản ứng nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Efgartigimod (Vyvgart)",
                "UpToDate - Efgartigimod: Drug information",
                "Lexicomp - Efgartigimod monograph",
                "AAN Guidelines - Myasthenia Gravis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, clinical trial data, widely used"
        }
    },
    
    "Etanercept": {
        "group": "Biological - Fusion Protein (TNF receptor)",
        "vietnamese_name": "Etanercept, Enbrel",
        "administration": ["SC"],
        "indications": [
            "Viêm khớp dạng thấp (RA)",
            "Viêm cột sống dính khớp (AS)",
            "Vảy nến (psoriasis)",
            "Viêm khớp vảy nến (PsA)",
            "Viêm khớp vị thành niên (JIA)"
        ],
        "contraindications": [
            "Dị ứng etanercept hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Suy tim nặng (NYHA class III-IV)",
            "Bệnh lao đang hoạt động"
        ],
        "dosage": {
            "adult_ra": "50mg SC mỗi tuần (hoặc 25mg SC 2 lần/tuần)",
            "adult_psoriasis": "50mg SC 2 lần/tuần x 3 tháng, sau đó 50mg SC mỗi tuần",
            "adult_as": "50mg SC mỗi tuần",
            "adult_psa": "50mg SC mỗi tuần",
            "pediatric_jia": "0.8mg/kg SC mỗi tuần (tối đa 50mg/tuần)",
            "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng cơ hội, lao)",
            "Phản ứng dị ứng (rash, urticaria)",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
            "Suy tim - có thể làm nặng",
            "Bệnh lý thần kinh (demyelinating disease) - hiếm",
            "Giảm bạch cầu, tiểu cầu - hiếm",
            "Tăng men gan",
            "Buồn nôn, đau đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Etanercept là fusion protein gồm thụ thể TNF-α (p75) gắn với Fc của IgG1. TNF-α là cytokine tiền viêm quan trọng, được sản xuất bởi đại thực bào và tế bào T, đóng vai trò trong quá trình viêm. Trong các bệnh tự miễn (RA, AS, psoriasis), TNF-α tăng cao → gây viêm mạn tính → tổn thương mô. Etanercept gắn với TNF-α (cả TNF-α và lymphotoxin-α) → ngăn chặn TNF-α gắn với thụ thể trên tế bào → ức chế tín hiệu viêm → giảm viêm và tổn thương mô. Dẫn đến: giảm triệu chứng và làm chậm tiến triển bệnh. Etanercept được dùng để điều trị nhiều bệnh tự miễn qua trung gian TNF-α, đặc biệt hiệu quả trong RA và AS.",
        "monitoring": [
            "Phản ứng tại chỗ tiêm",
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng",
            "Dấu hiệu suy tim (nếu có tiền sử)",
            "Dấu hiệu bệnh lý thần kinh (nếu có triệu chứng)"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt và nghiêm trọng",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
            "Ngừng etanercept nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân suy tim - có thể làm nặng",
            "Thận trọng ở bệnh nhân có tiền sử ung thư - tăng nguy cơ ung thư",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh lý thần kinh demyelinating",
            "Theo dõi chức năng gan - có thể tăng men gan"
        ],
        "pharmacokinetics": {
            "half_life": "102 giờ (khoảng 4 ngày)",
            "onset": "Vài tuần",
            "duration": "1 tuần (liều mỗi tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life trung bình."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 15-30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng, đặc biệt lao và nhiễm trùng cơ hội. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ ung thư (lymphoma, ung thư da). Suy tim - có thể làm nặng, ngừng nếu suy tim mới hoặc nặng hơn.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (methotrexate, azathioprine, 6-mercaptopurine)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Etanercept làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị etanercept. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng etanercept hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Bệnh lao đang hoạt động",
                "Suy tim nặng (NYHA class III-IV)"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Suy tim nhẹ đến trung bình (NYHA class I-II) - có thể làm nặng",
                "Tiền sử lao - cần điều trị dự phòng",
                "Tiền sử ung thư - tăng nguy cơ",
                "Bệnh lý thần kinh demyelinating - có thể làm nặng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Etanercept là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Etanercept bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Etanercept không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chức năng gan (có thể tăng men gan)."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng",
                "Giảm bạch cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng etanercept",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi công thức máu",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, công thức máu trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 25mg/0.5ml hoặc 50mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 15-30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Etanercept (Enbrel)",
                "UpToDate - Etanercept: Drug information",
                "Lexicomp - Etanercept monograph",
                "ACR Guidelines - Rheumatoid Arthritis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections (especially TB and opportunistic infections)", "Malignancy (lymphoma, skin cancer)", "Heart failure exacerbation", "Demyelinating disease"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL", "TB screening (PPD or IGRA) before treatment - CRITICAL", "CBC", "Hepatic function (ALT, AST)", "Symptoms of heart failure", "Neurological symptoms"]
        },
        "guideline_tags": [
            "ACR Guidelines - Rheumatoid Arthritis",
            "ACR Guidelines - Psoriatic Arthritis",
            "AAD Guidelines - Psoriasis",
            "FDA Black Box Warning - Etanercept and Serious Infections",
            "FDA Black Box Warning - Etanercept and TB",
            "FDA Black Box Warning - Etanercept and Malignancy"
        ]
    },
    
    "Golimumab": {
        "group": "Biological - Monoclonal Antibody (anti-TNF-α)",
        "vietnamese_name": "Golimumab, Simponi",
        "administration": ["SC", "IV"],
        "indications": [
            "Viêm khớp dạng thấp (RA)",
            "Viêm cột sống dính khớp (AS)",
            "Viêm loét đại tràng (UC)",
            "Viêm khớp vảy nến (PsA)"
        ],
        "contraindications": [
            "Dị ứng golimumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Suy tim nặng (NYHA class III-IV)",
            "Bệnh lao đang hoạt động"
        ],
        "dosage": {
            "adult_ra_sc": "50mg SC mỗi tháng",
            "adult_ra_iv": "2mg/kg IV ngày 0, 4 tuần, sau đó mỗi 8 tuần",
            "adult_as": "50mg SC mỗi tháng",
            "adult_uc": "200mg SC ngày 1, sau đó 100mg SC ngày 15, sau đó 100mg SC mỗi tháng",
            "adult_psa": "50mg SC mỗi tháng",
            "notes": "Tiêm dưới da hoặc truyền tĩnh mạch. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Phản ứng truyền (infusion reaction) - khi dùng IV",
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng cơ hội, lao)",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
            "Suy tim - có thể làm nặng",
            "Bệnh lý thần kinh (demyelinating disease) - hiếm",
            "Giảm bạch cầu, tiểu cầu - hiếm",
            "Tăng men gan",
            "Buồn nôn, đau đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Golimumab là kháng thể đơn dòng kháng TNF-α (tumor necrosis factor-alpha, fully human monoclonal antibody). TNF-α là cytokine tiền viêm quan trọng, được sản xuất bởi đại thực bào và tế bào T, đóng vai trò trong quá trình viêm. Trong các bệnh tự miễn (RA, AS, UC, PsA), TNF-α tăng cao → gây viêm mạn tính → tổn thương mô. Golimumab gắn với TNF-α (cả dạng hòa tan và dạng màng) → ngăn chặn TNF-α gắn với thụ thể → ức chế tín hiệu viêm → giảm viêm và tổn thương mô. Dẫn đến: giảm triệu chứng và làm chậm tiến triển bệnh. Golimumab được dùng để điều trị nhiều bệnh tự miễn qua trung gian TNF-α.",
        "monitoring": [
            "Phản ứng tại chỗ tiêm hoặc phản ứng truyền",
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng",
            "Dấu hiệu suy tim (nếu có tiền sử)",
            "Dấu hiệu bệnh lý thần kinh (nếu có triệu chứng)"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt và nghiêm trọng",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
            "Ngừng golimumab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân suy tim - có thể làm nặng",
            "Thận trọng ở bệnh nhân có tiền sử ung thư - tăng nguy cơ ung thư",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh lý thần kinh demyelinating"
        ],
        "pharmacokinetics": {
            "half_life": "14 ngày (dao động 10-20 ngày)",
            "onset": "Vài tuần",
            "duration": "1 tháng (liều SC mỗi tháng) hoặc 8 tuần (liều IV mỗi 8 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 15-30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng, đặc biệt lao và nhiễm trùng cơ hội. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ ung thư (lymphoma, ung thư da). Suy tim - có thể làm nặng, ngừng nếu suy tim mới hoặc nặng hơn.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (methotrexate, azathioprine, 6-mercaptopurine)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Golimumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị golimumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng golimumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Bệnh lao đang hoạt động",
                "Suy tim nặng (NYHA class III-IV)"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Suy tim nhẹ đến trung bình (NYHA class I-II) - có thể làm nặng",
                "Tiền sử lao - cần điều trị dự phòng",
                "Tiền sử ung thư - tăng nguy cơ",
                "Bệnh lý thần kinh demyelinating - có thể làm nặng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Golimumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Golimumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Golimumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chức năng gan (có thể tăng men gan)."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng",
                "Giảm bạch cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng golimumab",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi công thức máu",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, công thức máu trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 50mg/0.5ml hoặc 100mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 15-30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần."
            },
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 0.4-4mg/ml.",
                "infusion_rate": "Truyền trong 2 giờ.",
                "compatibility": ["NS"],
                "incompatibility": ["D5W", "Không pha với các thuốc khác"],
                "notes": "Premedication: corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền. Theo dõi chặt chẽ trong và sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Golimumab (Simponi)",
                "UpToDate - Golimumab: Drug information",
                "Lexicomp - Golimumab monograph",
                "ACR Guidelines - Rheumatoid Arthritis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections (especially TB and opportunistic infections)", "Malignancy (lymphoma, skin cancer)", "Heart failure exacerbation", "Demyelinating disease"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL", "TB screening (PPD or IGRA) before treatment - CRITICAL", "CBC", "Hepatic function (ALT, AST)", "Symptoms of heart failure", "Neurological symptoms"]
        },
        "guideline_tags": [
            "ACR Guidelines - Rheumatoid Arthritis",
            "ACR Guidelines - Psoriatic Arthritis",
            "ECCO Guidelines - Inflammatory Bowel Disease",
            "FDA Black Box Warning - Golimumab and Serious Infections",
            "FDA Black Box Warning - Golimumab and TB",
            "FDA Black Box Warning - Golimumab and Malignancy"
        ]
    },
    
    "Guselkumab": {
        "group": "Biological - Monoclonal Antibody (anti-IL-23)",
        "vietnamese_name": "Guselkumab, Tremfya",
        "administration": ["SC"],
        "indications": [
            "Vảy nến (psoriasis) - trung bình đến nặng",
            "Viêm khớp vảy nến (PsA)"
        ],
        "contraindications": [
            "Dị ứng guselkumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult_psoriasis": "100mg SC ngày 1, sau đó 100mg SC ngày 28, sau đó 100mg SC mỗi 8 tuần",
            "adult_psa": "100mg SC ngày 1, sau đó 100mg SC ngày 28, sau đó 100mg SC mỗi 8 tuần",
            "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên)",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Đau đầu",
            "Tiêu chảy",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Guselkumab là kháng thể đơn dòng kháng IL-23 (interleukin-23, fully human monoclonal antibody). IL-23 là cytokine quan trọng trong quá trình viêm qua trung gian Th17 cells. IL-23 kích hoạt Th17 cells → sản xuất IL-17A và các cytokine khác → gây viêm mạn tính → tổn thương mô. Trong vảy nến và viêm khớp vảy nến, IL-23 tăng cao → gây viêm da và khớp. Guselkumab gắn với p19 subunit của IL-23 → ngăn chặn IL-23 gắn với receptor → ức chế signaling → giảm viêm. Dẫn đến: giảm triệu chứng và cải thiện chức năng trong vảy nến và viêm khớp vảy nến. Guselkumab được dùng để điều trị vảy nến và viêm khớp vảy nến.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Phản ứng tại chỗ tiêm",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng guselkumab nếu có nhiễm trùng nặng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động"
        ],
        "pharmacokinetics": {
            "half_life": "15-18 ngày",
            "onset": "Vài tuần",
            "duration": "8 tuần (liều mỗi 8 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Guselkumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị guselkumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng guselkumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử lao - cần điều trị dự phòng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Guselkumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Guselkumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Guselkumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng guselkumab",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 100mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Guselkumab (Tremfya)",
                "UpToDate - Guselkumab: Drug information",
                "Lexicomp - Guselkumab monograph",
                "AAD Guidelines - Psoriasis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL", "TB screening (PPD or IGRA) before treatment - CRITICAL", "CBC", "Hepatic function (ALT, AST)", "Injection site reactions"]
        },
        "guideline_tags": [
            "AAD Guidelines - Psoriasis",
            "ACR Guidelines - Psoriatic Arthritis",
            "FDA Black Box Warning - Guselkumab and Serious Infections",
            "FDA Black Box Warning - Guselkumab and TB"
        ]
    },
    
    "Infliximab": {
        "group": "Biological - Monoclonal Antibody (anti-TNF-α)",
        "vietnamese_name": "Infliximab, Remicade",
        "administration": ["IV"],
        "indications": [
            "Viêm khớp dạng thấp (RA)",
            "Bệnh Crohn (Crohn's disease)",
            "Viêm loét đại tràng (UC)",
            "Vảy nến (psoriasis)",
            "Viêm khớp vảy nến (PsA)",
            "Viêm cột sống dính khớp (AS)",
            "Viêm khớp vị thành niên (JIA)"
        ],
        "contraindications": [
            "Dị ứng infliximab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Suy tim nặng (NYHA class III-IV)",
            "Bệnh lao đang hoạt động"
        ],
        "dosage": {
            "adult_ra": "3mg/kg IV ngày 0, 2, 6 tuần, sau đó mỗi 8 tuần (có thể tăng lên 10mg/kg hoặc mỗi 4 tuần nếu cần)",
            "adult_crohn": "5mg/kg IV ngày 0, 2, 6 tuần, sau đó mỗi 8 tuần (có thể tăng lên 10mg/kg hoặc mỗi 4 tuần nếu cần)",
            "adult_uc": "5mg/kg IV ngày 0, 2, 6 tuần, sau đó mỗi 8 tuần",
            "adult_psoriasis": "5mg/kg IV ngày 0, 2, 6 tuần, sau đó mỗi 8 tuần",
            "adult_as": "5mg/kg IV ngày 0, 2, 6 tuần, sau đó mỗi 6-8 tuần",
            "pediatric_crohn": "5mg/kg IV ngày 0, 2, 6 tuần, sau đó mỗi 8 tuần",
            "notes": "Truyền trong 2 giờ. Premedication với corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion reaction) - phổ biến: sốt, ớn lạnh, đau đầu, phát ban, khó thở",
            "Phản ứng dị ứng muộn (delayed hypersensitivity) - 3-12 ngày sau truyền",
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng cơ hội, lao)",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
            "Suy tim - có thể làm nặng",
            "Bệnh lý thần kinh (demyelinating disease) - hiếm",
            "Giảm bạch cầu, tiểu cầu - hiếm",
            "Tăng men gan",
            "Buồn nôn, đau đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Infliximab là kháng thể đơn dòng kháng TNF-α (tumor necrosis factor-alpha, chimeric mouse-human monoclonal antibody). TNF-α là cytokine tiền viêm quan trọng, được sản xuất bởi đại thực bào và tế bào T, đóng vai trò trong quá trình viêm. Trong các bệnh tự miễn (RA, Crohn, UC, psoriasis), TNF-α tăng cao → gây viêm mạn tính → tổn thương mô. Infliximab gắn với TNF-α (cả dạng hòa tan và dạng màng) → ngăn chặn TNF-α gắn với thụ thể → ức chế tín hiệu viêm → giảm viêm và tổn thương mô. Dẫn đến: giảm triệu chứng và làm chậm tiến triển bệnh. Infliximab được dùng để điều trị nhiều bệnh tự miễn qua trung gian TNF-α, đặc biệt hiệu quả trong Crohn và UC.",
        "monitoring": [
            "Phản ứng truyền (infusion reaction) - QUAN TRỌNG: theo dõi trong và sau truyền",
            "Phản ứng dị ứng muộn - theo dõi 3-12 ngày sau truyền",
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng",
            "Dấu hiệu suy tim (nếu có tiền sử)",
            "Dấu hiệu bệnh lý thần kinh (nếu có triệu chứng)"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt và nghiêm trọng",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Premedication với corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền",
            "Truyền chậm trong 2 giờ",
            "Theo dõi phản ứng truyền chặt chẽ - phổ biến, có thể nghiêm trọng",
            "Theo dõi phản ứng dị ứng muộn - 3-12 ngày sau truyền",
            "Ngừng infliximab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân suy tim - có thể làm nặng",
            "Thận trọng ở bệnh nhân có tiền sử ung thư - tăng nguy cơ ung thư",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh lý thần kinh demyelinating"
        ],
        "pharmacokinetics": {
            "half_life": "8-10 ngày (dao động 7-12 ngày)",
            "onset": "Vài tuần",
            "duration": "6-8 tuần (liều mỗi 6-8 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life trung bình."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng, đặc biệt lao và nhiễm trùng cơ hội. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Phản ứng truyền nặng có thể gây tử vong. Tăng nguy cơ ung thư (lymphoma, ung thư da). Suy tim - có thể làm nặng, ngừng nếu suy tim mới hoặc nặng hơn.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (methotrexate, azathioprine, 6-mercaptopurine)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Infliximab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị infliximab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng infliximab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Bệnh lao đang hoạt động",
                "Suy tim nặng (NYHA class III-IV)"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Suy tim nhẹ đến trung bình (NYHA class I-II) - có thể làm nặng",
                "Tiền sử lao - cần điều trị dự phòng",
                "Tiền sử ung thư - tăng nguy cơ",
                "Bệnh lý thần kinh demyelinating - có thể làm nặng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Infliximab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ. Có thể truyền qua nhau thai trong tam cá nguyệt thứ ba, có thể ảnh hưởng đến đáp ứng vaccine ở trẻ sơ sinh.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Infliximab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Infliximab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chức năng gan (có thể tăng men gan)."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở, phù, sốc)",
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng",
                "Giảm bạch cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị sốc: dịch, vận mạch nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi công thức máu",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, phản ứng truyền, công thức máu, dấu hiệu nhiễm trùng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 0.4-4mg/ml. Lọc qua filter 1.2 micron.",
                "infusion_rate": "Truyền trong 2 giờ (ít nhất 2 giờ).",
                "compatibility": ["NS"],
                "incompatibility": ["D5W (không ổn định)", "Không pha với các thuốc khác"],
                "notes": "Premedication: methylprednisolone 125mg IV (hoặc tương đương), diphenhydramine 50mg IV/PO, acetaminophen 650-1000mg PO, 30-60 phút trước truyền. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi phản ứng dị ứng muộn 3-12 ngày sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Infliximab (Remicade)",
                "UpToDate - Infliximab: Drug information",
                "Lexicomp - Infliximab monograph",
                "ACR Guidelines - Rheumatoid Arthritis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections (especially TB and opportunistic infections)", "Malignancy (lymphoma, skin cancer)", "Heart failure exacerbation", "Demyelinating disease", "Infusion reactions (can be severe)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Infusion reactions - CRITICAL (during and after infusion)", "Signs of infection - CRITICAL", "TB screening (PPD or IGRA) before treatment - CRITICAL", "Delayed hypersensitivity reactions (3-12 days after infusion)", "CBC", "Hepatic function (ALT, AST)", "Symptoms of heart failure", "Neurological symptoms"]
        },
        "guideline_tags": [
            "ACR Guidelines - Rheumatoid Arthritis",
            "ECCO Guidelines - Inflammatory Bowel Disease",
            "AAD Guidelines - Psoriasis",
            "FDA Black Box Warning - Infliximab and Serious Infections",
            "FDA Black Box Warning - Infliximab and TB",
            "FDA Black Box Warning - Infliximab and Infusion Reactions",
            "FDA Black Box Warning - Infliximab and Malignancy"
        ]
    },
    
    "Ixekizumab": {
        "group": "Biological - Monoclonal Antibody (anti-IL-17A)",
        "vietnamese_name": "Ixekizumab, Taltz",
        "administration": ["SC"],
        "indications": [
            "Vảy nến (psoriasis) - trung bình đến nặng",
            "Viêm khớp vảy nến (PsA)",
            "Viêm cột sống dính khớp (AS)",
            "Viêm cột sống dính khớp không X-quang (nr-axSpA)"
        ],
        "contraindications": [
            "Dị ứng ixekizumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult_psoriasis": "160mg SC ngày 1 (2 lần tiêm 80mg), sau đó 80mg SC mỗi 2 tuần",
            "adult_psa": "160mg SC ngày 1, sau đó 80mg SC mỗi 4 tuần",
            "adult_as": "80mg SC mỗi 4 tuần",
            "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên)",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhiễm trùng nấm Candida - tăng nguy cơ",
            "Bệnh viêm ruột (IBD) - tăng nguy cơ, đặc biệt Crohn",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Đau đầu",
            "Tiêu chảy",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ixekizumab là kháng thể đơn dòng kháng IL-17A (interleukin-17A, humanized monoclonal antibody). IL-17A là cytokine quan trọng trong quá trình viêm qua trung gian Th17 cells. IL-17A kích hoạt các tế bào viêm → tăng sản xuất các cytokine và chemokine khác → gây viêm mạn tính → tổn thương mô. Trong vảy nến và viêm khớp, IL-17A tăng cao → gây viêm da và khớp. Ixekizumab gắn với IL-17A → ngăn chặn IL-17A gắn với receptor → ức chế signaling → giảm viêm. Dẫn đến: giảm triệu chứng và cải thiện chức năng trong vảy nến và viêm khớp. Ixekizumab được dùng để điều trị vảy nến, viêm khớp vảy nến, và viêm cột sống dính khớp.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Nhiễm trùng nấm Candida - tăng nguy cơ, theo dõi triệu chứng",
            "Bệnh viêm ruột (IBD) - theo dõi triệu chứng tiêu hóa, đặc biệt Crohn",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Phản ứng tại chỗ tiêm",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng ixekizumab nếu có nhiễm trùng nặng",
            "Theo dõi nhiễm trùng nấm Candida - điều trị nếu có",
            "Thận trọng ở bệnh nhân có tiền sử IBD - tăng nguy cơ, đặc biệt Crohn",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động"
        ],
        "pharmacokinetics": {
            "half_life": "13 ngày (dao động 10-18 ngày)",
            "onset": "Vài tuần",
            "duration": "2-4 tuần (liều mỗi 2-4 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life trung bình."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ bệnh viêm ruột (IBD), đặc biệt Crohn.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Ixekizumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị ixekizumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ixekizumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử lao - cần điều trị dự phòng",
                "Tiền sử IBD - tăng nguy cơ, đặc biệt Crohn",
                "Nhiễm trùng nấm Candida đang hoạt động - có thể làm nặng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ixekizumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Ixekizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Ixekizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ixekizumab",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 80mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ixekizumab (Taltz)",
                "UpToDate - Ixekizumab: Drug information",
                "Lexicomp - Ixekizumab monograph",
                "AAD Guidelines - Psoriasis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections", "Inflammatory bowel disease (IBD, especially Crohn) - increased risk", "Candida infections - increased risk"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL", "TB screening (PPD or IGRA) before treatment - CRITICAL", "Candida infections", "IBD symptoms (especially Crohn) - CRITICAL", "CBC", "Hepatic function (ALT, AST)", "Injection site reactions"]
        },
        "guideline_tags": [
            "AAD Guidelines - Psoriasis",
            "ACR Guidelines - Psoriatic Arthritis",
            "ACR Guidelines - Ankylosing Spondylitis",
            "FDA Black Box Warning - Ixekizumab and Serious Infections",
            "FDA Black Box Warning - Ixekizumab and IBD"
        ]
    },
    
    "Lanadelumab": {
        "group": "Biological - Monoclonal Antibody (anti-plasma kallikrein)",
        "vietnamese_name": "Lanadelumab, Takhzyro",
        "administration": ["SC"],
        "indications": [
            "Phù mạch di truyền (hereditary angioedema, HAE) - type I và II, dự phòng cơn"
        ],
        "contraindications": [
            "Dị ứng lanadelumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_loading": "300mg SC ngày 1, sau đó 300mg SC mỗi 2 tuần",
            "adult_maintenance": "300mg SC mỗi 2 tuần (có thể tăng lên 300mg SC mỗi tuần nếu cần)",
            "pediatric_12_17": "300mg SC ngày 1, sau đó 300mg SC mỗi 2 tuần",
            "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn. Dùng để dự phòng cơn HAE, không dùng để điều trị cơn cấp."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Đau đầu",
            "Đau bụng",
            "Buồn nôn",
            "Chóng mặt",
            "Phản ứng dị ứng - hiếm"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Lanadelumab là kháng thể đơn dòng kháng plasma kallikrein (fully human monoclonal antibody). Plasma kallikrein là enzyme quan trọng trong hệ thống contact system. Kích hoạt contact system → tạo plasma kallikrein → chuyển đổi kininogen thành bradykinin → bradykinin tăng tính thấm mạch máu → phù mạch. Trong HAE, thiếu hoặc rối loạn C1 esterase inhibitor (C1-INH) → không ức chế plasma kallikrein → tăng bradykinin → phù mạch. Lanadelumab gắn với plasma kallikrein → ngăn chặn plasma kallikrein chuyển đổi kininogen thành bradykinin → giảm bradykinin → giảm phù mạch. Dẫn đến: giảm tần suất và mức độ cơn HAE. Lanadelumab được dùng để dự phòng cơn HAE type I và II.",
        "monitoring": [
            "Phản ứng tại chỗ tiêm",
            "Tần suất và mức độ cơn HAE - đánh giá hiệu quả điều trị",
            "Sử dụng thuốc điều trị cơn cấp - giảm sử dụng cho thấy đáp ứng",
            "Dấu hiệu phản ứng dị ứng"
        ],
        "precautions": [
            "DÙNG ĐỂ DỰ PHÒNG CƠN HAE - không dùng để điều trị cơn cấp",
            "Bệnh nhân vẫn cần có thuốc điều trị cơn cấp (C1-INH, icatibant, ecallantide)",
            "Có thể tăng liều lên 300mg SC mỗi tuần nếu vẫn có cơn thường xuyên",
            "Theo dõi tần suất và mức độ cơn HAE",
            "Theo dõi phản ứng tại chỗ tiêm"
        ],
        "pharmacokinetics": {
            "half_life": "14 ngày (dao động 10-18 ngày)",
            "onset": "Vài tuần",
            "duration": "2 tuần (liều mỗi 2 tuần) hoặc 1 tuần (liều mỗi tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần lưu ý rằng lanadelumab dùng để dự phòng, không dùng để điều trị cơn cấp.",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng lanadelumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Lanadelumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Lanadelumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu phản ứng dị ứng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Lanadelumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng lanadelumab",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine, epinephrine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 300mg/2ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn. Dùng để dự phòng, không dùng để điều trị cơn cấp."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lanadelumab (Takhzyro)",
                "UpToDate - Lanadelumab: Drug information",
                "Lexicomp - Lanadelumab monograph",
                "WAO Guidelines - Hereditary Angioedema"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, clinical trial data, widely used"
        }
    },
    "Natalizumab": {
        "group": "Biological - Monoclonal Antibody (anti-integrin α4)",
        "vietnamese_name": "Natalizumab, Tysabri",
        "administration": ["IV"],
        "indications": [
            "Đa xơ cứng (MS) - relapsing-remitting",
            "Bệnh Crohn (Crohn's disease) - trung bình đến nặng"
        ],
        "contraindications": [
            "Dị ứng natalizumab hoặc bất kỳ thành phần nào",
            "PML (progressive multifocal leukoencephalopathy) - đang hoạt động hoặc tiền sử",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult_ms": "300mg IV mỗi 4 tuần",
            "adult_crohn": "300mg IV ngày 0, 4, 8 tuần, sau đó 300mg IV mỗi 4 tuần",
            "notes": "Truyền trong 1 giờ. BLACK BOX WARNING về PML. Test JCV antibody trước khi dùng. Chỉ dùng trong chương trình đặc biệt (TOUCH Prescribing Program)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "PML (progressive multifocal leukoencephalopathy) - NGUY HIỂM, có thể tử vong, black box warning",
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng",
            "Phản ứng truyền (infusion reaction) - phổ biến",
            "Phản ứng dị ứng muộn (delayed hypersensitivity) - 3-12 ngày sau truyền",
            "Đau đầu",
            "Mệt mỏi",
            "Buồn nôn",
            "Đau khớp"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ PML khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Natalizumab là kháng thể đơn dòng kháng integrin α4 (humanized monoclonal antibody). Integrin α4 là phân tử kết dính trên tế bào T và B, giúp các tế bào này di chuyển từ máu vào mô thần kinh trung ương (CNS) và ruột. Tế bào T/B gắn với VCAM-1 (vascular cell adhesion molecule-1) trên tế bào nội mô qua integrin α4 → di chuyển vào mô CNS và ruột → gây viêm trong MS và Crohn. Natalizumab gắn với integrin α4 → ngăn chặn integrin α4 gắn với VCAM-1 → ức chế di chuyển tế bào T/B vào mô CNS và ruột → giảm viêm. Dẫn đến: giảm tái phát và làm chậm tiến triển bệnh trong MS và Crohn. Tuy nhiên, ức chế di chuyển tế bào T vào CNS cũng làm giảm khả năng chống lại JC virus → tăng nguy cơ PML.",
        "monitoring": [
            "PML (progressive multifocal leukoencephalopathy) - QUAN TRỌNG: theo dõi dấu hiệu thần kinh (thay đổi nhận thức, yếu, mất thị lực, mất điều hòa)",
            "Test JCV antibody - trước khi bắt đầu và định kỳ trong điều trị",
            "MRI não - trước khi bắt đầu và định kỳ (mỗi 6-12 tháng) để phát hiện PML sớm",
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng",
            "Phản ứng truyền",
            "Phản ứng dị ứng muộn - 3-12 ngày sau truyền",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng"
        ],
        "precautions": [
            "BLACK BOX WARNING: PML (progressive multifocal leukoencephalopathy) - có thể tử vong",
            "TEST JCV ANTIBODY TRƯỚC KHI BẮT ĐẦU - tăng nguy cơ PML nếu JCV dương tính",
            "Nguy cơ PML tăng theo thời gian điều trị và JCV antibody status",
            "Ngừng natalizumab ngay nếu nghi ngờ PML",
            "MRI não trước khi bắt đầu và định kỳ (mỗi 6-12 tháng) để phát hiện PML sớm",
            "Chỉ dùng trong chương trình đặc biệt (TOUCH Prescribing Program)",
            "Theo dõi dấu hiệu thần kinh chặt chẽ - ngừng ngay nếu có triệu chứng PML",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân JCV dương tính - tăng nguy cơ PML",
            "Thận trọng ở bệnh nhân đã dùng các thuốc ức chế miễn dịch khác - tăng nguy cơ PML"
        ],
        "pharmacokinetics": {
            "half_life": "11 ngày (dao động 7-15 ngày)",
            "onset": "Vài tuần",
            "duration": "4 tuần (liều mỗi 4 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life trung bình."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 8 giờ.",
        "black_box_warnings": "PML (progressive multifocal leukoencephalopathy) - có thể tử vong. PML là nhiễm trùng não do JC virus, thường gây tử vong hoặc tàn tật nghiêm trọng. Tăng nguy cơ PML ở bệnh nhân JCV dương tính, đã điều trị lâu dài, và đã dùng các thuốc ức chế miễn dịch khác. Test JCV antibody trước khi bắt đầu. MRI não định kỳ. Ngừng ngay nếu nghi ngờ PML. Chỉ dùng trong chương trình đặc biệt (TOUCH Prescribing Program).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (corticosteroid liều cao, azathioprine, methotrexate)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ PML nghiêm trọng",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, theo dõi chặt chẽ PML."
                }
            ],
            "moderate": [
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Natalizumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị natalizumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng natalizumab hoặc bất kỳ thành phần nào",
                "PML (progressive multifocal leukoencephalopathy) - đang hoạt động hoặc tiền sử",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "JCV antibody dương tính - tăng nguy cơ PML",
                "Đã điều trị lâu dài (>2 năm) - tăng nguy cơ PML",
                "Đã dùng các thuốc ức chế miễn dịch khác - tăng nguy cơ PML",
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Natalizumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (MS, Crohn nặng). Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Natalizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Natalizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "PML (progressive multifocal leukoencephalopathy)",
                "Nhiễm trùng nặng",
                "Phản ứng truyền nặng",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị PML ngay nếu nghi ngờ: ngừng natalizumab, điều trị hỗ trợ, plasmapheresis để loại bỏ natalizumab",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu PML (thần kinh), dấu hiệu nhiễm trùng, phản ứng truyền, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": ["Plasmapheresis có thể giúp loại bỏ natalizumab nếu cần"]
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 0.3-3mg/ml. Lọc qua filter 1.2 micron.",
                "infusion_rate": "Truyền trong 1 giờ.",
                "compatibility": ["NS"],
                "incompatibility": ["D5W", "Không pha với các thuốc khác"],
                "notes": "Premedication: corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền (nếu cần). Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi phản ứng dị ứng muộn 3-12 ngày sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Natalizumab (Tysabri)",
                "UpToDate - Natalizumab: Drug information",
                "Lexicomp - Natalizumab monograph",
                "AAN Guidelines - Multiple Sclerosis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Nivolumab": {
        "group": "Biological - Monoclonal Antibody (anti-PD-1)",
        "vietnamese_name": "Nivolumab, Opdivo",
        "administration": ["IV"],
        "indications": [
            "Ung thư phổi không tế bào nhỏ (NSCLC)",
            "Ung thư phổi tế bào nhỏ (SCLC)",
            "Ung thư hắc tố (melanoma)",
            "Ung thư thận (RCC)",
            "Ung thư đầu cổ (HNSCC)",
            "Ung thư bàng quang (urothelial carcinoma)",
            "Ung thư gan (HCC)",
            "Ung thư đại trực tràng (MSI-H/dMMR)",
            "Ung thư dạ dày, thực quản, GEJ",
            "Ung thư hạch Hodgkin (cHL)",
            "Ung thư hạch không Hodgkin (PMBCL)",
            "Ung thư tế bào Merkel",
            "Mesothelioma màng phổi"
        ],
        "contraindications": [
            "Dị ứng nivolumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Bệnh tự miễn đang hoạt động nặng"
        ],
        "dosage": {
            "adult_standard": "240mg IV mỗi 2 tuần, hoặc 480mg IV mỗi 4 tuần",
            "adult_weight_based": "3mg/kg IV mỗi 2 tuần (không khuyến cáo)",
            "adult_combination": "360mg IV mỗi 3 tuần (kết hợp với ipilimumab)",
            "notes": "Truyền trong 30 phút. Có thể dùng đơn trị hoặc kết hợp với ipilimumab hoặc chemotherapy. Điều trị đến khi bệnh tiến triển hoặc độc tính không chấp nhận được."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng miễn dịch (immune-related adverse events, irAEs) - NGUY HIỂM, phổ biến",
            "Viêm phổi do miễn dịch (pneumonitis) - có thể tử vong",
            "Viêm đại tràng (colitis) - có thể tử vong",
            "Viêm gan (hepatitis) - có thể tử vong",
            "Viêm nội tiết (endocrinopathies): viêm tuyến giáp, viêm tuyến yên, viêm tuyến thượng thận - có thể vĩnh viễn",
            "Viêm da (dermatitis, rash)",
            "Viêm cơ tim (myocarditis) - hiếm nhưng nghiêm trọng",
            "Viêm thần kinh (neuropathy)",
            "Viêm khớp (arthritis)",
            "Viêm thận (nephritis) - hiếm",
            "Phản ứng truyền (infusion reaction) - hiếm",
            "Mệt mỏi",
            "Ngứa, phát ban",
            "Buồn nôn, tiêu chảy"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ phản ứng miễn dịch khi dùng với ipilimumab"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Nivolumab là kháng thể đơn dòng kháng PD-1 (programmed death-1, fully human monoclonal antibody). PD-1 là thụ thể ức chế trên tế bào T, khi gắn với PD-L1/PD-L2 (ligands trên tế bào ung thư và tế bào miễn dịch) → ức chế hoạt động tế bào T → tế bào T không thể tiêu diệt tế bào ung thư (immune evasion). Nivolumab gắn với PD-1 → ngăn chặn PD-1 gắn với PD-L1/PD-L2 → giải phóng ức chế tế bào T → tế bào T hoạt động trở lại → tiêu diệt tế bào ung thư. Dẫn đến: tăng đáp ứng miễn dịch chống ung thư. Nivolumab được dùng để điều trị nhiều loại ung thư, có thể dùng đơn trị hoặc kết hợp với ipilimumab (anti-CTLA-4) để tăng hiệu quả.",
        "monitoring": [
            "Phản ứng miễn dịch (irAEs) - QUAN TRỌNG: theo dõi chặt chẽ trong và sau điều trị",
            "Viêm phổi: khó thở, ho, đau ngực - chụp X-quang ngực nếu có triệu chứng",
            "Viêm đại tràng: tiêu chảy, đau bụng, phân có máu - nội soi nếu cần",
            "Viêm gan: vàng da, mệt mỏi, đau bụng - ALT, AST, bilirubin mỗi chu kỳ",
            "Viêm nội tiết: TSH, T4 (tuyến giáp), cortisol (tuyến thượng thận), glucose - mỗi chu kỳ",
            "Viêm cơ tim: đau ngực, khó thở, nhịp tim nhanh - troponin, ECG, echo nếu có triệu chứng",
            "Viêm thận: creatinine, eGFR, protein niệu - mỗi chu kỳ",
            "Chức năng thận: creatinine, eGFR - mỗi chu kỳ",
            "Công thức máu: CBC - mỗi chu kỳ",
            "Dấu hiệu phản ứng truyền"
        ],
        "precautions": [
            "THEO DÕI PHẢN ỨNG MIỄN DỊCH (irAEs) CHẶT CHẼ - có thể nghiêm trọng và tử vong",
            "Ngừng nivolumab và điều trị ngay nếu có irAE độ 3-4 (corticosteroid, immunosuppressant)",
            "Viêm phổi: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid liều cao",
            "Viêm đại tràng: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid, infliximab nếu cần",
            "Viêm gan: ngừng nếu ALT/AST >5x ULN, điều trị với corticosteroid",
            "Viêm nội tiết: có thể vĩnh viễn, cần điều trị thay thế hormone",
            "Viêm cơ tim: ngừng ngay, điều trị với corticosteroid liều cao",
            "Viêm thận: ngừng nếu creatinine tăng, điều trị với corticosteroid",
            "Kết hợp với ipilimumab: tăng nguy cơ irAEs nghiêm trọng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh tự miễn đang hoạt động",
            "Thận trọng ở bệnh nhân đã cấy ghép tạng - tăng nguy cơ thải ghép"
        ],
        "pharmacokinetics": {
            "half_life": "25 ngày (dao động 12-20 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "2-4 tuần (liều mỗi 2-4 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "PHẢN ỨNG MIỄN DỊCH (immune-related adverse events, irAEs) - có thể nghiêm trọng và tử vong. Viêm phổi, viêm đại tràng, viêm gan, viêm nội tiết, viêm cơ tim, viêm thận có thể xảy ra. Ngừng và điều trị ngay nếu có irAE độ 3-4. Kết hợp với ipilimumab tăng nguy cơ irAEs. Có thể gây tử vong thai nhi (category D).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ipilimumab",
                    "mechanism": "Cả hai đều là checkpoint inhibitors, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ phản ứng miễn dịch nghiêm trọng (irAEs độ 3-4)",
                    "management": "Theo dõi chặt chẽ irAEs. Điều trị ngay nếu có irAE độ 3-4."
                }
            ],
            "moderate": [
                {
                    "drug": "Corticosteroid (liều cao, kéo dài)",
                    "mechanism": "Corticosteroid ức chế miễn dịch, có thể làm giảm hiệu quả nivolumab",
                    "effect": "Có thể làm giảm đáp ứng điều trị",
                    "management": "Tránh dùng corticosteroid liều cao kéo dài trước điều trị. Có thể dùng để điều trị irAEs."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Nivolumab làm thay đổi đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị nivolumab. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng nivolumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Bệnh tự miễn đang hoạt động nặng - tăng nguy cơ irAEs",
                "Đã cấy ghép tạng - tăng nguy cơ thải ghép",
                "Viêm phổi đang hoạt động - tăng nguy cơ viêm phổi do miễn dịch",
                "Viêm đại tràng đang hoạt động - tăng nguy cơ viêm đại tràng do miễn dịch",
                "Kết hợp với ipilimumab - tăng nguy cơ irAEs nghiêm trọng",
                "Có thai (category D) - có thể gây tử vong thai nhi"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Nivolumab là FDA category D - có thể gây tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rủi ro. Có thể gây dị tật bẩm sinh và tử vong thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Nivolumab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Nivolumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chặt chẽ viêm gan do miễn dịch."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng miễn dịch nặng (irAEs độ 3-4)",
                "Phản ứng truyền nặng",
                "Viêm phổi nặng",
                "Viêm đại tràng nặng",
                "Viêm gan nặng",
                "Viêm thận nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị irAEs.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị irAEs: corticosteroid liều cao (methylprednisolone 1-2mg/kg/ngày), immunosuppressant (infliximab cho viêm đại tràng) nếu cần",
                "Điều trị viêm phổi: corticosteroid liều cao, hỗ trợ hô hấp nếu cần",
                "Điều trị viêm đại tràng: corticosteroid, infliximab nếu không đáp ứng",
                "Điều trị viêm gan: corticosteroid, hỗ trợ gan nếu cần",
                "Điều trị viêm thận: corticosteroid, hỗ trợ thận nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu irAEs, chức năng gan, thận, nội tiết trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 1-10mg/ml. Không lọc.",
                "infusion_rate": "Truyền trong 30 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Không cần premedication thường quy. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi phản ứng miễn dịch."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Nivolumab (Opdivo)",
                "UpToDate - Nivolumab: Drug information",
                "Lexicomp - Nivolumab monograph",
                "NCCN Guidelines - Multiple cancer types"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Ocrelizumab": {
        "group": "Biological - Monoclonal Antibody (anti-CD20)",
        "vietnamese_name": "Ocrelizumab, Ocrevus",
        "administration": ["IV"],
        "indications": [
            "Đa xơ cứng (MS) - relapsing-remitting (RRMS)",
            "Đa xơ cứng (MS) - primary progressive (PPMS)"
        ],
        "contraindications": [
            "Dị ứng ocrelizumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Viêm gan B đang hoạt động"
        ],
        "dosage": {
            "adult_ms": "300mg IV ngày 1, sau đó 300mg IV ngày 15, sau đó 600mg IV mỗi 6 tháng",
            "notes": "Truyền trong 2.5-4 giờ (lần đầu) hoặc 2 giờ (lần sau nếu dung nạp tốt). Premedication với corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền. Test lao và viêm gan B trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion reaction) - phổ biến lần đầu: sốt, ớn lạnh, đau đầu, buồn nôn, phát ban, khó thở",
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)",
            "Viêm gan B tái hoạt (HBV reactivation) - NGUY HIỂM",
            "Giảm bạch cầu, tiểu cầu - hiếm",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Đau đầu",
            "Mệt mỏi",
            "Buồn nôn"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ocrelizumab là kháng thể đơn dòng kháng CD20 (humanized monoclonal antibody). CD20 là kháng nguyên bề mặt trên tế bào B trưởng thành (pre-B cells đến memory B cells, nhưng không có trên plasma cells và stem cells). Trong MS, tế bào B đóng vai trò quan trọng trong quá trình viêm và tổn thương myelin. Ocrelizumab gắn với CD20 → kích hoạt complement-dependent cytotoxicity (CDC) và antibody-dependent cell-mediated cytotoxicity (ADCC) → tiêu diệt tế bào B. Dẫn đến: giảm số lượng tế bào B trong máu và mô, giảm sản xuất autoantibodies, và giảm viêm trong MS. Ocrelizumab được dùng để điều trị cả RRMS và PPMS, là thuốc đầu tiên được FDA phê duyệt cho PPMS.",
        "monitoring": [
            "Phản ứng truyền (infusion reaction) - QUAN TRỌNG: theo dõi trong và sau truyền, đặc biệt lần đầu",
            "Công thức máu (WBC, lymphocyte, platelet) - giảm bạch cầu, giảm tiểu cầu",
            "Nhiễm trùng - tăng nguy cơ, đặc biệt nhiễm trùng cơ hội",
            "Viêm gan B (HBsAg, anti-HBc) - test trước khi dùng, theo dõi HBV reactivation",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Chức năng thận: creatinine, eGFR - mỗi 3-6 tháng"
        ],
        "precautions": [
            "TEST VIÊM GAN B TRƯỚC KHI DÙNG (HBsAg, anti-HBc) - HBV reactivation có thể gây tử vong",
            "Điều trị dự phòng HBV nếu có tiền sử viêm gan B (entecavir, tenofovir)",
            "Premedication với corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền",
            "Truyền chậm lần đầu (2.5-4 giờ), có thể rút ngắn lần sau nếu dung nạp tốt",
            "Theo dõi phản ứng truyền chặt chẽ - phổ biến lần đầu",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng ocrelizumab nếu có nhiễm trùng nặng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động",
            "Giảm bạch cầu có thể kéo dài vài tháng sau điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "26 ngày (dao động 20-32 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "6 tháng (liều mỗi 6 tháng)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "VIÊM GAN B TÁI HOẠT (HBV reactivation) - có thể gây suy gan cấp và tử vong. Test HBsAg và anti-HBc trước khi dùng. Điều trị dự phòng HBV nếu có tiền sử. Phản ứng truyền nặng có thể gây tử vong. Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Ocrelizumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị ocrelizumab. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                },
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ocrelizumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Viêm gan B đang hoạt động"
            ],
            "tương_đối": [
                "Viêm gan B (HBsAg dương tính) - cần điều trị dự phòng HBV",
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Giảm bạch cầu nặng - tăng nguy cơ nhiễm trùng",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ocrelizumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (MS nặng). Một số nghiên cứu cho thấy tăng nguy cơ giảm tế bào B ở trẻ sơ sinh, nhưng không tăng nguy cơ dị tật bẩm sinh. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Ocrelizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Ocrelizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần thận trọng ở bệnh nhân viêm gan B (nguy cơ reactivation)."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở, phù, sốc)",
                "Nhiễm trùng nặng",
                "Viêm gan B tái hoạt",
                "Giảm bạch cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị sốc: dịch, vận mạch nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị HBV reactivation nếu có",
                "Theo dõi công thức máu",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, phản ứng truyền, công thức máu, dấu hiệu nhiễm trùng, chức năng gan trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 1-10mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Lần đầu: bắt đầu 30mg/giờ, tăng dần mỗi 30 phút (30→60→120→180→240mg/giờ) nếu dung nạp tốt. Lần sau: có thể bắt đầu 120mg/giờ, tăng dần đến 240mg/giờ. Tổng thời gian truyền: 2.5-4 giờ lần đầu, 2 giờ lần sau.",
                "compatibility": ["NS"],
                "incompatibility": ["D5W", "Không pha với các thuốc khác"],
                "notes": "Premedication: methylprednisolone 100mg IV (hoặc tương đương), diphenhydramine 50mg IV/PO, acetaminophen 650-1000mg PO, 30-60 phút trước truyền. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ocrelizumab (Ocrevus)",
                "UpToDate - Ocrelizumab: Drug information",
                "Lexicomp - Ocrelizumab monograph",
                "AAN Guidelines - Multiple Sclerosis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Pembrolizumab": {
        "group": "Biological - Monoclonal Antibody (anti-PD-1)",
        "vietnamese_name": "Pembrolizumab, Keytruda",
        "administration": ["IV"],
        "indications": [
            "Ung thư phổi không tế bào nhỏ (NSCLC) - PD-L1 ≥1%",
            "Ung thư phổi tế bào nhỏ (SCLC)",
            "Ung thư vú triple-negative (PD-L1 dương tính)",
            "Ung thư đại trực tràng (MSI-H/dMMR)",
            "Ung thư dạ dày (PD-L1 dương tính)",
            "Ung thư thực quản",
            "Ung thư đầu cổ (HNSCC)",
            "Ung thư thận (RCC)",
            "Ung thư bàng quang (urothelial carcinoma)",
            "Ung thư hắc tố (melanoma)",
            "Ung thư gan (HCC)",
            "Ung thư cổ tử cung",
            "Ung thư nội mạc tử cung",
            "Ung thư hạch Hodgkin (cHL)",
            "Ung thư hạch không Hodgkin (PMBCL)",
            "Ung thư Merkel cell carcinoma"
        ],
        "contraindications": [
            "Dị ứng pembrolizumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Bệnh tự miễn đang hoạt động nặng"
        ],
        "dosage": {
            "adult_standard": "200mg IV mỗi 3 tuần, hoặc 400mg IV mỗi 6 tuần",
            "adult_weight_based": "2mg/kg IV mỗi 3 tuần (không khuyến cáo)",
            "notes": "Truyền trong 30 phút. Có thể dùng đơn trị hoặc kết hợp với chemotherapy. Điều trị đến khi bệnh tiến triển hoặc độc tính không chấp nhận được."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng miễn dịch (immune-related adverse events, irAEs) - NGUY HIỂM, phổ biến",
            "Viêm phổi do miễn dịch (pneumonitis) - có thể tử vong",
            "Viêm đại tràng (colitis) - có thể tử vong",
            "Viêm gan (hepatitis) - có thể tử vong",
            "Viêm nội tiết (endocrinopathies): viêm tuyến giáp, viêm tuyến yên, viêm tuyến thượng thận - có thể vĩnh viễn",
            "Viêm da (dermatitis, rash)",
            "Viêm cơ tim (myocarditis) - hiếm nhưng nghiêm trọng",
            "Viêm thần kinh (neuropathy)",
            "Viêm khớp (arthritis)",
            "Phản ứng truyền (infusion reaction) - hiếm",
            "Mệt mỏi",
            "Ngứa, phát ban",
            "Buồn nôn, tiêu chảy",
            "Giảm cảm giác ngon miệng"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ phản ứng miễn dịch khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Pembrolizumab là kháng thể đơn dòng kháng PD-1 (programmed death-1, humanized monoclonal antibody). PD-1 là thụ thể ức chế trên tế bào T, khi gắn với PD-L1/PD-L2 (ligands trên tế bào ung thư và tế bào miễn dịch) → ức chế hoạt động tế bào T → tế bào T không thể tiêu diệt tế bào ung thư (immune evasion). Pembrolizumab gắn với PD-1 → ngăn chặn PD-1 gắn với PD-L1/PD-L2 → giải phóng ức chế tế bào T → tế bào T hoạt động trở lại → tiêu diệt tế bào ung thư. Dẫn đến: tăng đáp ứng miễn dịch chống ung thư. Pembrolizumab được dùng để điều trị nhiều loại ung thư có PD-L1 dương tính hoặc MSI-H/dMMR.",
        "monitoring": [
            "Phản ứng miễn dịch (irAEs) - QUAN TRỌNG: theo dõi chặt chẽ trong và sau điều trị",
            "Viêm phổi: khó thở, ho, đau ngực - chụp X-quang ngực nếu có triệu chứng",
            "Viêm đại tràng: tiêu chảy, đau bụng, phân có máu - nội soi nếu cần",
            "Viêm gan: vàng da, mệt mỏi, đau bụng - ALT, AST, bilirubin mỗi chu kỳ",
            "Viêm nội tiết: TSH, T4 (tuyến giáp), cortisol (tuyến thượng thận), glucose - mỗi chu kỳ",
            "Viêm cơ tim: đau ngực, khó thở, nhịp tim nhanh - troponin, ECG, echo nếu có triệu chứng",
            "Chức năng thận: creatinine, eGFR - mỗi chu kỳ",
            "Công thức máu: CBC - mỗi chu kỳ",
            "Dấu hiệu phản ứng truyền"
        ],
        "precautions": [
            "THEO DÕI PHẢN ỨNG MIỄN DỊCH (irAEs) CHẶT CHẼ - có thể nghiêm trọng và tử vong",
            "Ngừng pembrolizumab và điều trị ngay nếu có irAE độ 3-4 (corticosteroid, immunosuppressant)",
            "Viêm phổi: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid liều cao",
            "Viêm đại tràng: ngừng ngay nếu nghi ngờ, điều trị với corticosteroid, infliximab nếu cần",
            "Viêm gan: ngừng nếu ALT/AST >5x ULN, điều trị với corticosteroid",
            "Viêm nội tiết: có thể vĩnh viễn, cần điều trị thay thế hormone",
            "Viêm cơ tim: ngừng ngay, điều trị với corticosteroid liều cao",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có bệnh tự miễn đang hoạt động",
            "Thận trọng ở bệnh nhân đã cấy ghép tạng - tăng nguy cơ thải ghép"
        ],
        "pharmacokinetics": {
            "half_life": "26 ngày (dao động 15-32 ngày)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "3-6 tuần (liều mỗi 3-6 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "PHẢN ỨNG MIỄN DỊCH (immune-related adverse events, irAEs) - có thể nghiêm trọng và tử vong. Viêm phổi, viêm đại tràng, viêm gan, viêm nội tiết, viêm cơ tim có thể xảy ra. Ngừng và điều trị ngay nếu có irAE độ 3-4. Có thể gây tử vong thai nhi (category D).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Corticosteroid (liều cao, kéo dài)",
                    "mechanism": "Corticosteroid ức chế miễn dịch, có thể làm giảm hiệu quả pembrolizumab",
                    "effect": "Có thể làm giảm đáp ứng điều trị",
                    "management": "Tránh dùng corticosteroid liều cao kéo dài trước điều trị. Có thể dùng để điều trị irAEs."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Pembrolizumab làm thay đổi đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị pembrolizumab. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng pembrolizumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Bệnh tự miễn đang hoạt động nặng - tăng nguy cơ irAEs",
                "Đã cấy ghép tạng - tăng nguy cơ thải ghép",
                "Viêm phổi đang hoạt động - tăng nguy cơ viêm phổi do miễn dịch",
                "Viêm đại tràng đang hoạt động - tăng nguy cơ viêm đại tràng do miễn dịch",
                "Có thai (category D) - có thể gây tử vong thai nhi"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Pembrolizumab là FDA category D - có thể gây tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rủi ro. Có thể gây dị tật bẩm sinh và tử vong thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Pembrolizumab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Pembrolizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chặt chẽ viêm gan do miễn dịch."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng miễn dịch nặng (irAEs độ 3-4)",
                "Phản ứng truyền nặng",
                "Viêm phổi nặng",
                "Viêm đại tràng nặng",
                "Viêm gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị irAEs.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị irAEs: corticosteroid liều cao (methylprednisolone 1-2mg/kg/ngày), immunosuppressant (infliximab cho viêm đại tràng) nếu cần",
                "Điều trị viêm phổi: corticosteroid liều cao, hỗ trợ hô hấp nếu cần",
                "Điều trị viêm đại tràng: corticosteroid, infliximab nếu không đáp ứng",
                "Điều trị viêm gan: corticosteroid, hỗ trợ gan nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu irAEs, chức năng gan, thận, nội tiết trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 1-10mg/ml. Không lọc.",
                "infusion_rate": "Truyền trong 30 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Không cần premedication thường quy. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Theo dõi phản ứng miễn dịch."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pembrolizumab (Keytruda)",
                "UpToDate - Pembrolizumab: Drug information",
                "Lexicomp - Pembrolizumab monograph",
                "NCCN Guidelines - Multiple cancer types"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Ravulizumab": {
        "group": "Biological - Monoclonal Antibody (anti-C5 Complement)",
        "vietnamese_name": "Ravulizumab, Ultomiris",
        "administration": ["IV"],
        "indications": [
            "Paroxysmal nocturnal hemoglobinuria (PNH)",
            "Atypical hemolytic uremic syndrome (aHUS)",
            "Myasthenia gravis - generalized (off-label)"
        ],
        "contraindications": [
            "Dị ứng ravulizumab hoặc eculizumab",
            "Nhiễm trùng nặng chưa điều trị, đặc biệt Neisseria meningitidis",
            "Chưa tiêm vaccine meningococcal"
        ],
        "dosage": {
            "adult_pnh_loading": "2400mg IV ngày 1, sau đó 3000mg IV ngày 15, sau đó 3000mg IV mỗi 8 tuần",
            "adult_pnh_maintenance": "3000mg IV mỗi 8 tuần",
            "adult_ahus_loading": "2400mg IV ngày 1, sau đó 3000mg IV ngày 15, sau đó 3000mg IV mỗi 8 tuần",
            "adult_ahus_maintenance": "3000mg IV mỗi 8 tuần",
            "pediatric_pnh_ahus": "Liều theo cân nặng, tính toán dựa trên body weight",
            "notes": "Truyền trong 4 giờ. PHẢI tiêm vaccine meningococcal trước khi bắt đầu. Điều trị dự phòng kháng sinh meningococcal nếu cần."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)",
            "Phản ứng truyền (infusion reaction) - phổ biến lần đầu: sốt, ớn lạnh, đau đầu, buồn nôn",
            "Nhiễm trùng nặng - có thể nghiêm trọng, đặc biệt Neisseria meningitidis",
            "Đau đầu",
            "Buồn nôn",
            "Tiêu chảy"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ravulizumab là kháng thể đơn dòng kháng C5 (complement component 5, humanized monoclonal antibody). C5 là thành phần quan trọng của hệ thống bổ thể (complement system). Kích hoạt bổ thể → tạo C5a và C5b → C5b tạo membrane attack complex (MAC) → phá hủy tế bào. Trong PNH và aHUS, kích hoạt bổ thể bất thường → phá hủy tế bào hồng cầu và tế bào nội mô → thiếu máu tan máu và tổn thương thận. Ravulizumab gắn với C5 → ngăn chặn C5 tạo C5a và C5b → ức chế MAC → giảm phá hủy tế bào. Dẫn đến: giảm thiếu máu tan máu và tổn thương thận trong PNH và aHUS. Ravulizumab được dùng để điều trị PNH và aHUS. Lưu ý: Ravulizumab là dạng cải tiến của eculizumab với half-life dài hơn (8 tuần so với 2 tuần).",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị, ĐẶC BIỆT Neisseria meningitidis",
            "Phản ứng truyền - QUAN TRỌNG: theo dõi trong và sau truyền, đặc biệt lần đầu",
            "PNH: LDH, hemoglobin, haptoglobin, reticulocyte - đánh giá hiệu quả điều trị",
            "aHUS: Creatinine, eGFR, LDH, platelet, hemoglobin - đánh giá hiệu quả điều trị",
            "Dấu hiệu nhiễm trùng meningococcal (sốt, đau đầu, cứng cổ, phát ban) - NGUY HIỂM",
            "Vaccine meningococcal - đảm bảo đã tiêm trước khi bắt đầu"
        ],
        "precautions": [
            "PHẢI TIÊM VACCINE MENINGOCOCCAL TRƯỚC KHI BẮT ĐẦU - nhiễm trùng meningococcal có thể tử vong",
            "Điều trị dự phòng kháng sinh meningococcal nếu cần (penicillin, ciprofloxacin)",
            "THEO DÕI NHIỄM TRÙNG MENINGOCOCCAL CHẶT CHẼ - dấu hiệu: sốt, đau đầu, cứng cổ, phát ban, điều trị ngay",
            "Ngừng ravulizumab nếu có nhiễm trùng nặng",
            "Theo dõi phản ứng truyền chặt chẽ, đặc biệt lần đầu",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động",
            "Theo dõi LDH, hemoglobin trong PNH",
            "Theo dõi creatinine, eGFR trong aHUS"
        ],
        "pharmacokinetics": {
            "half_life": "49 ngày (dao động 40-60 ngày)",
            "onset": "Vài tuần",
            "duration": "8 tuần (liều mỗi 8 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài hơn eculizumab (8 tuần so với 2 tuần)."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "NHIỄM TRÙNG MENINGOCOCCAL - tăng nguy cơ nhiễm trùng meningococcal nghiêm trọng, có thể tử vong. PHẢI tiêm vaccine meningococcal trước khi bắt đầu. Điều trị dự phòng kháng sinh meningococcal nếu cần. Theo dõi dấu hiệu nhiễm trùng meningococcal (sốt, đau đầu, cứng cổ, phát ban) - điều trị ngay.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Ravulizumab làm thay đổi đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị ravulizumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ravulizumab hoặc eculizumab",
                "Nhiễm trùng nặng chưa điều trị, đặc biệt Neisseria meningitidis",
                "Chưa tiêm vaccine meningococcal"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ravulizumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Ravulizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Ravulizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng, đặc biệt meningococcal",
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị nhiễm trùng meningococcal ngay nếu có (ceftriaxone, penicillin)",
                "Điều trị nhiễm trùng khác nếu có",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng (đặc biệt meningococcal), phản ứng truyền trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 0.5-5mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 4 giờ.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "PHẢI tiêm vaccine meningococcal trước khi bắt đầu. Điều trị dự phòng kháng sinh meningococcal nếu cần. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Ngừng ngay nếu có phản ứng nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ravulizumab (Ultomiris)",
                "UpToDate - Ravulizumab: Drug information",
                "Lexicomp - Ravulizumab monograph",
                "ASH Guidelines - PNH and aHUS"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Meningococcal infections (life-threatening) - CRITICAL", "Serious infections"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Meningococcal infection signs (fever, headache, neck stiffness, rash) - CRITICAL", "Infusion reactions - CRITICAL (during and after infusion, especially first time)", "PNH: LDH, hemoglobin, haptoglobin, reticulocyte", "aHUS: Creatinine, eGFR, LDH, platelet, hemoglobin", "Meningococcal vaccination status - CRITICAL (must be vaccinated before starting)"]
        },
        "guideline_tags": [
            "ASH Guidelines - Paroxysmal Nocturnal Hemoglobinuria",
            "ASH Guidelines - Atypical Hemolytic Uremic Syndrome",
            "FDA Black Box Warning - Ravulizumab and Meningococcal Infections",
            "FDA Black Box Warning - Ravulizumab and Vaccination Requirement"
        ]
    },
    
    "Reslizumab": {
        "group": "Biological - Monoclonal Antibody (anti-IL-5)",
        "vietnamese_name": "Reslizumab, Cinqair",
        "administration": ["IV"],
        "indications": [
            "Hen suyễn eosinophilic nặng (severe eosinophilic asthma) - kiểm soát kém"
        ],
        "contraindications": [
            "Dị ứng reslizumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult": "3mg/kg IV mỗi 4 tuần",
            "notes": "Truyền trong 20-50 phút. Chỉ dùng cho hen suyễn eosinophilic (eosinophil ≥400 cells/μL)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion reaction) - phổ biến lần đầu: sốt, ớn lạnh, đau đầu, buồn nôn",
            "Nhiễm trùng đường hô hấp trên",
            "Đau đầu",
            "Nhiễm trùng nặng - hiếm",
            "Phản ứng dị ứng nặng - hiếm",
            "Tăng creatine kinase (CK) - hiếm"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Reslizumab là kháng thể đơn dòng kháng IL-5 (interleukin-5, humanized monoclonal antibody). IL-5 là cytokine quan trọng cho sự sống và hoạt động của eosinophil. IL-5 được giải phóng từ Th2 cells và mast cells → gắn với IL-5R trên eosinophil → kích hoạt eosinophil → tăng số lượng và hoạt động eosinophil → gây viêm đường hô hấp và hen suyễn eosinophilic. Reslizumab gắn với IL-5 → ngăn chặn IL-5 gắn với receptor → ức chế signaling → giảm số lượng và hoạt động eosinophil. Dẫn đến: giảm eosinophil trong máu và mô, giảm cơn hen và cải thiện chức năng hô hấp trong hen suyễn eosinophilic. Reslizumab được dùng để điều trị hen suyễn eosinophilic nặng.",
        "monitoring": [
            "Phản ứng truyền - QUAN TRỌNG: theo dõi trong và sau truyền, đặc biệt lần đầu",
            "Chức năng hô hấp (FEV1) - đánh giá hiệu quả điều trị",
            "Eosinophil máu - giảm đáng kể (thường giảm 50-80%)",
            "Tần suất cơn hen - giảm cơn hen",
            "Sử dụng corticosteroid (ICS) - có thể giảm liều",
            "Dấu hiệu nhiễm trùng đường hô hấp",
            "Dấu hiệu phản ứng dị ứng",
            "Creatine kinase (CK) - nếu có triệu chứng đau cơ"
        ],
        "precautions": [
            "CHỈ DÙNG CHO HEN SUYỄN EOSINOPHILIC - eosinophil ≥400 cells/μL",
            "THEO DÕI PHẢN ỨNG TRUYỀN CHẶT CHẼ - phổ biến lần đầu",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động",
            "Không ngừng đột ngột các thuốc hen khác (ICS, LABA) - giảm dần dần",
            "Theo dõi chức năng hô hấp thường xuyên"
        ],
        "pharmacokinetics": {
            "half_life": "24 ngày (dao động 18-30 ngày)",
            "onset": "Vài tuần",
            "duration": "4 tuần",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "PHẢN ỨNG TRUYỀN NẶNG - có thể gây tử vong. Theo dõi chặt chẽ trong và sau truyền. Ngừng ngay nếu có phản ứng nặng. Tăng nguy cơ nhiễm trùng.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Reslizumab làm thay đổi đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị reslizumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng reslizumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - thận trọng",
                "Hen suyễn không eosinophilic - không hiệu quả",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Reslizumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Reslizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Reslizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở, phù, sốc)",
                "Phản ứng dị ứng nặng",
                "Nhiễm trùng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị sốc: dịch, vận mạch nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, phản ứng truyền, dấu hiệu nhiễm trùng, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 0.1-1mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 20-50 phút.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu. Ngừng ngay nếu có phản ứng nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Reslizumab (Cinqair)",
                "UpToDate - Reslizumab: Drug information",
                "Lexicomp - Reslizumab monograph",
                "GINA Guidelines - Asthma"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Infusion reactions (can be severe, fatal) - CRITICAL", "Serious infections"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Infusion reactions - CRITICAL (during and after infusion, especially first time)", "Respiratory function (FEV1) - assess treatment response", "Blood eosinophil count - significant decrease (usually 50-80% reduction)", "Asthma exacerbation frequency - reduction in asthma attacks", "ICS use - may reduce dose", "Signs of respiratory infection", "Signs of allergic reactions", "Creatine kinase (CK) - if muscle pain symptoms"]
        },
        "guideline_tags": [
            "GINA Guidelines - Severe Asthma",
            "FDA Black Box Warning - Reslizumab and Infusion Reactions",
            "FDA Drug Information - Reslizumab"
        ]
    },
    
    "Risankizumab": {
        "group": "Biological - Monoclonal Antibody (anti-IL-23)",
        "vietnamese_name": "Risankizumab, Skyrizi",
        "administration": ["SC", "IV"],
        "indications": [
            "Vảy nến (psoriasis) - trung bình đến nặng",
            "Bệnh Crohn (Crohn's disease)",
            "Viêm khớp vảy nến (PsA)"
        ],
        "contraindications": [
            "Dị ứng risankizumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult_psoriasis_sc": "150mg SC ngày 1, sau đó 150mg SC ngày 28, sau đó 150mg SC mỗi 12 tuần",
            "adult_crohn_iv": "600mg IV ngày 1, sau đó 600mg IV ngày 28, sau đó 360mg SC mỗi 8 tuần",
            "adult_psa_sc": "150mg SC ngày 1, sau đó 150mg SC ngày 28, sau đó 150mg SC mỗi 12 tuần",
            "notes": "Tiêm dưới da hoặc truyền tĩnh mạch. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên)",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Phản ứng truyền (infusion reaction) - khi dùng IV",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Đau đầu",
            "Tiêu chảy",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Risankizumab là kháng thể đơn dòng kháng IL-23 (interleukin-23, humanized monoclonal antibody). IL-23 là cytokine quan trọng trong quá trình viêm qua trung gian Th17 cells. IL-23 kích hoạt Th17 cells → sản xuất IL-17A và các cytokine khác → gây viêm mạn tính → tổn thương mô. Trong vảy nến, viêm khớp vảy nến, và Crohn, IL-23 tăng cao → gây viêm da, khớp, và ruột. Risankizumab gắn với p19 subunit của IL-23 → ngăn chặn IL-23 gắn với receptor → ức chế signaling → giảm viêm. Dẫn đến: giảm triệu chứng và cải thiện chức năng trong vảy nến, viêm khớp vảy nến, và Crohn. Risankizumab được dùng để điều trị vảy nến, viêm khớp vảy nến, và Crohn.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Phản ứng tại chỗ tiêm hoặc phản ứng truyền",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng risankizumab nếu có nhiễm trùng nặng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ chính xác, khoảng 3-4 tuần",
            "onset": "Vài tuần",
            "duration": "8-12 tuần (liều mỗi 8-12 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Risankizumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị risankizumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng risankizumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử lao - cần điều trị dự phòng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Risankizumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Risankizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Risankizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng",
                "Phản ứng truyền nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng risankizumab",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, phản ứng truyền, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 150mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            },
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 0.6-6mg/ml.",
                "infusion_rate": "Truyền trong ít nhất 1 giờ.",
                "compatibility": ["NS"],
                "incompatibility": ["D5W", "Không pha với các thuốc khác"],
                "notes": "Premedication: corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền. Theo dõi chặt chẽ trong và sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Risankizumab (Skyrizi)",
                "UpToDate - Risankizumab: Drug information",
                "Lexicomp - Risankizumab monograph",
                "AAD Guidelines - Psoriasis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL", "TB screening (PPD or IGRA) before treatment - CRITICAL", "CBC", "Hepatic function (ALT, AST)", "Injection site reactions or infusion reactions"]
        },
        "guideline_tags": [
            "AAD Guidelines - Psoriasis",
            "ACR Guidelines - Psoriatic Arthritis",
            "ECCO Guidelines - Inflammatory Bowel Disease",
            "FDA Black Box Warning - Risankizumab and Serious Infections",
            "FDA Black Box Warning - Risankizumab and TB"
        ]
    },
    
    "Rituximab": {
        "group": "Biological - Monoclonal Antibody (anti-CD20)",
        "vietnamese_name": "Rituximab, Rituxan, MabThera",
        "administration": ["IV"],
        "indications": [
            "U lympho không Hodgkin (NHL) - B-cell lymphoma",
            "Bệnh bạch cầu lympho mạn (CLL)",
            "Viêm khớp dạng thấp (RA) - kháng TNF",
            "Granulomatosis với polyangiitis (GPA)",
            "Microscopic polyangiitis (MPA)",
            "Hội chứng thận hư do bệnh màng đáy (membranous nephropathy)"
        ],
        "contraindications": [
            "Dị ứng rituximab hoặc murine proteins",
            "Nhiễm trùng nặng chưa điều trị",
            "Suy tim nặng (NYHA class IV)",
            "Phụ nữ có thai (category C)"
        ],
        "dosage": {
            "adult_nhl": "375mg/m² IV mỗi tuần x 4-8 tuần, hoặc 375mg/m² IV ngày 1, 8, 15, 22 (chu kỳ 28 ngày)",
            "adult_cll": "375mg/m² IV ngày 1 chu kỳ 1, sau đó 500mg/m² IV ngày 1 chu kỳ 2-6 (chu kỳ 28 ngày)",
            "adult_ra": "1000mg IV x 2 lần cách nhau 2 tuần, lặp lại mỗi 6-12 tháng",
            "adult_vasculitis": "375mg/m² IV mỗi tuần x 4 tuần",
            "notes": "Premedication với corticosteroid, antihistamine, và acetaminophen để giảm phản ứng truyền. Truyền chậm lần đầu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion reaction) - phổ biến lần đầu: sốt, ớn lạnh, đau đầu, buồn nôn, phát ban, khó thở",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Nhiễm trùng (tăng nguy cơ, đặc biệt nhiễm trùng cơ hội)",
            "Viêm gan B tái hoạt (HBV reactivation) - NGUY HIỂM",
            "PML (progressive multifocal leukoencephalopathy) - hiếm nhưng nghiêm trọng",
            "Tổn thương tim (suy tim, rối loạn nhịp) - hiếm",
            "Phản ứng da nặng (Stevens-Johnson, TEN) - hiếm",
            "Hội chứng giải phóng cytokine (cytokine release syndrome) - hiếm"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Rituximab là kháng thể đơn dòng kháng CD20 (chimeric mouse-human monoclonal antibody). CD20 là kháng nguyên bề mặt trên tế bào B trưởng thành (pre-B cells đến memory B cells, nhưng không có trên plasma cells và stem cells). Rituximab gắn với CD20 → kích hoạt complement-dependent cytotoxicity (CDC) và antibody-dependent cell-mediated cytotoxicity (ADCC) → tiêu diệt tế bào B. Dẫn đến: giảm số lượng tế bào B trong máu và mô, giảm sản xuất autoantibodies (trong bệnh tự miễn), và tiêu diệt tế bào B ác tính (trong lymphoma). Rituximab được dùng để điều trị B-cell lymphoma, CLL, và các bệnh tự miễn qua trung gian tế bào B (RA, vasculitis).",
        "monitoring": [
            "Phản ứng truyền (infusion reaction) - QUAN TRỌNG: theo dõi trong và sau truyền, đặc biệt lần đầu",
            "Công thức máu (WBC, lymphocyte, platelet) - giảm bạch cầu, giảm tiểu cầu",
            "Nhiễm trùng - tăng nguy cơ, đặc biệt nhiễm trùng cơ hội",
            "Viêm gan B (HBsAg, anti-HBc) - test trước khi dùng, theo dõi HBV reactivation",
            "Dấu hiệu PML (thay đổi thần kinh, suy giảm nhận thức) - hiếm nhưng nghiêm trọng",
            "Chức năng tim (ECG, echo nếu có triệu chứng) - tổn thương tim hiếm",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)"
        ],
        "precautions": [
            "TEST VIÊM GAN B TRƯỚC KHI DÙNG (HBsAg, anti-HBc) - HBV reactivation có thể gây tử vong",
            "Điều trị dự phòng HBV nếu có tiền sử viêm gan B (entecavir, tenofovir)",
            "Premedication với corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền",
            "Truyền chậm lần đầu (50mg/giờ, tăng dần nếu dung nạp tốt)",
            "Tăng nguy cơ nhiễm trùng - cần phòng ngừa nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
            "Không dùng vaccine sống trong và sau điều trị",
            "Theo dõi dấu hiệu PML (thay đổi thần kinh) - ngừng ngay nếu nghi ngờ",
            "Thận trọng ở bệnh nhân suy tim (có thể làm nặng)",
            "Giảm bạch cầu có thể kéo dài vài tháng sau điều trị"
        ],
        "pharmacokinetics": {
            "half_life": "18-32 ngày (dao động rộng)",
            "onset": "Giảm tế bào B trong vài ngày đến vài tuần",
            "duration": "Tế bào B có thể giảm trong 6-12 tháng",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống retículoendothelial (RES), tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài, tích lũy với liều lặp lại."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "VIÊM GAN B TÁI HOẠT (HBV reactivation) - có thể gây suy gan cấp và tử vong. Test HBsAg và anti-HBc trước khi dùng. Điều trị dự phòng HBV nếu có tiền sử. PML (progressive multifocal leukoencephalopathy) - hiếm nhưng nghiêm trọng, có thể tử vong. Phản ứng truyền nặng có thể gây tử vong. Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Rituximab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị rituximab. Hoãn vaccine sống ít nhất 6-12 tháng sau liều cuối."
                },
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (corticosteroid, methotrexate, cyclophosphamide)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng rituximab hoặc murine proteins",
                "Nhiễm trùng nặng chưa điều trị",
                "Suy tim nặng (NYHA class IV)"
            ],
            "tương_đối": [
                "Viêm gan B (HBsAg dương tính) - cần điều trị dự phòng HBV",
                "Suy tim (NYHA class II-III) - có thể làm nặng",
                "Giảm bạch cầu nặng - tăng nguy cơ nhiễm trùng",
                "Nhiễm trùng cơ hội đang hoạt động - tăng nguy cơ",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Rituximab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (lymphoma, bệnh tự miễn nặng). Một số nghiên cứu cho thấy tăng nguy cơ giảm tế bào B ở trẻ sơ sinh, nhưng không tăng nguy cơ dị tật bẩm sinh. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Rituximab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Rituximab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần thận trọng ở bệnh nhân viêm gan B (nguy cơ reactivation)."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở, phù, sốc)",
                "Hội chứng giải phóng cytokine nặng",
                "Giảm bạch cầu nặng",
                "Nhiễm trùng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị sốc: dịch, vận mạch nếu cần",
                "Theo dõi công thức máu",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, phản ứng truyền, công thức máu, dấu hiệu nhiễm trùng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Pha loãng đến nồng độ 1-4mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Lần đầu: bắt đầu 50mg/giờ, tăng dần mỗi 30 phút (50→100→150→200mg/giờ) nếu dung nạp tốt. Lần sau: có thể bắt đầu 100mg/giờ, tăng dần đến 400mg/giờ. Tổng thời gian truyền: 4-6 giờ lần đầu, 3-4 giờ lần sau.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "Premedication: methylprednisolone 100mg IV (hoặc tương đương), diphenhydramine 50mg IV/PO, acetaminophen 650-1000mg PO, 30-60 phút trước truyền. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Rituximab (Rituxan)",
                "UpToDate - Rituximab: Drug information",
                "Lexicomp - Rituximab monograph",
                "NCCN Guidelines - Non-Hodgkin Lymphoma"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["HBV reactivation (can cause fatal liver failure) - CRITICAL", "PML (progressive multifocal leukoencephalopathy) - rare but serious", "Serious infections (especially opportunistic infections)", "Cardiac toxicity (heart failure, arrhythmias)", "Infusion reactions (can be fatal)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["HBV screening (HBsAg, anti-HBc) before treatment - CRITICAL", "Infusion reactions - CRITICAL (during and after infusion, especially first time)", "CBC (WBC, lymphocyte, platelet) - myelosuppression", "Signs of infection - increased risk, especially opportunistic", "PML symptoms (neurological changes, cognitive decline) - CRITICAL", "Cardiac function (ECG, echo if symptoms) - cardiac toxicity rare", "Signs of opportunistic infections (PCP, CMV, herpes, fungal)"]
        },
        "guideline_tags": [
            "NCCN Guidelines - Non-Hodgkin Lymphoma",
            "ACR Guidelines - Rheumatoid Arthritis",
            "FDA Black Box Warning - Rituximab and HBV Reactivation",
            "FDA Black Box Warning - Rituximab and PML",
            "FDA Black Box Warning - Rituximab and Infusion Reactions"
        ]
    },
    
    "Sarilumab": {
        "group": "Biological - Monoclonal Antibody (anti-IL-6R)",
        "vietnamese_name": "Sarilumab, Kevzara",
        "administration": ["SC"],
        "indications": [
            "Viêm khớp dạng thấp (RA) - trung bình đến nặng"
        ],
        "contraindications": [
            "Dị ứng sarilumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Giảm bạch cầu nặng (ANC <500/mm³)",
            "Giảm tiểu cầu nặng (<50,000/mm³)"
        ],
        "dosage": {
            "adult_ra": "200mg SC mỗi 2 tuần (có thể giảm xuống 150mg SC mỗi 2 tuần nếu có giảm bạch cầu, tiểu cầu, hoặc tăng men gan)",
            "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn. Test lao trước khi dùng. Theo dõi công thức máu chặt chẽ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng cơ hội, lao)",
            "Giảm bạch cầu, tiểu cầu - phổ biến, có thể nghiêm trọng",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Tăng cholesterol, triglyceride - phổ biến",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Rối loạn tiêu hóa (buồn nôn, tiêu chảy)",
            "Đau đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Sarilumab là kháng thể đơn dòng kháng IL-6R (interleukin-6 receptor, fully human monoclonal antibody). IL-6 là cytokine quan trọng trong quá trình viêm, được sản xuất bởi đại thực bào, tế bào T, và các tế bào khác. IL-6 gắn với IL-6R (có thể là membrane-bound hoặc soluble) → kích hoạt signaling (JAK/STAT pathway) → tăng sản xuất các cytokine và chemokine khác → gây viêm mạn tính → tổn thương mô. Trong RA, IL-6 tăng cao → gây viêm khớp nặng. Sarilumab gắn với cả membrane-bound và soluble IL-6R → ngăn chặn IL-6 gắn với receptor → ức chế signaling → giảm viêm. Dẫn đến: giảm triệu chứng và làm chậm tiến triển bệnh. Sarilumab được dùng để điều trị RA trung bình đến nặng.",
        "monitoring": [
            "Công thức máu (CBC) - QUAN TRỌNG: giảm bạch cầu, tiểu cầu phổ biến, theo dõi mỗi 4-8 tuần",
            "Chức năng gan (ALT, AST) - tăng men gan phổ biến, theo dõi mỗi 4-8 tuần",
            "Lipid panel (cholesterol, triglyceride) - tăng lipid phổ biến, theo dõi mỗi 4-8 tuần",
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Phản ứng tại chỗ tiêm"
        ],
        "precautions": [
            "THEO DÕI CÔNG THỨC MÁU CHẶT CHẼ - giảm bạch cầu, tiểu cầu phổ biến và có thể nghiêm trọng",
            "Ngừng sarilumab nếu ANC <500/mm³ hoặc platelet <50,000/mm³",
            "Giảm liều xuống 150mg SC mỗi 2 tuần nếu có giảm bạch cầu, tiểu cầu, hoặc tăng men gan",
            "THEO DÕI CHỨC NĂNG GAN CHẶT CHẼ - tăng men gan phổ biến",
            "Ngừng sarilumab nếu ALT/AST >5x ULN",
            "THEO DÕI LIPID - tăng cholesterol, triglyceride phổ biến, điều trị nếu cần",
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng sarilumab nếu có nhiễm trùng nặng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có giảm bạch cầu, tiểu cầu từ trước"
        ],
        "pharmacokinetics": {
            "half_life": "8-10 ngày",
            "onset": "Vài tuần",
            "duration": "2 tuần (liều mỗi 2 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life trung bình."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng, đặc biệt lao và nhiễm trùng cơ hội. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. GIẢM BẠCH CẦU, TIỂU CẦU - phổ biến và có thể nghiêm trọng. Theo dõi công thức máu chặt chẽ. Ngừng nếu ANC <500/mm³ hoặc platelet <50,000/mm³. TĂNG MEN GAN - phổ biến. Theo dõi chức năng gan chặt chẽ. Ngừng nếu ALT/AST >5x ULN.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (methotrexate, corticosteroid)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Sarilumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị sarilumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng sarilumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Giảm bạch cầu nặng (ANC <500/mm³)",
                "Giảm tiểu cầu nặng (<50,000/mm³)"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử lao - cần điều trị dự phòng",
                "Giảm bạch cầu, tiểu cầu từ trước - có thể làm nặng",
                "Tăng men gan từ trước - có thể làm nặng",
                "Tăng lipid từ trước - có thể làm nặng",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Sarilumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (RA nặng). Một số nghiên cứu cho thấy tăng nguy cơ dị tật bẩm sinh, nhưng cần cân nhắc lợi ích/rủi ro. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Sarilumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Sarilumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chặt chẽ chức năng gan (có thể tăng men gan)."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Giảm bạch cầu nặng (ANC <500/mm³)",
                "Giảm tiểu cầu nặng (<50,000/mm³)",
                "Tăng men gan nặng (ALT/AST >5x ULN)",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng sarilumab",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi và hỗ trợ giảm bạch cầu, tiểu cầu (truyền tiểu cầu nếu cần)",
                "Theo dõi chức năng gan",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, công thức máu, chức năng gan, dấu hiệu nhiễm trùng, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 150mg/1.14ml hoặc 200mg/1.14ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sarilumab (Kevzara)",
                "UpToDate - Sarilumab: Drug information",
                "Lexicomp - Sarilumab monograph",
                "ACR Guidelines - Rheumatoid Arthritis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections", "Neutropenia (ANC <500/mm³) - CRITICAL", "Thrombocytopenia (<50,000/mm³) - CRITICAL", "Hepatotoxicity (ALT/AST elevation - common)"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL", "TB screening (PPD or IGRA) before treatment - CRITICAL", "CBC (ANC, platelet) - CRITICAL (neutropenia, thrombocytopenia common)", "Hepatic function (ALT, AST) - CRITICAL (common elevation, stop if >5x ULN)", "Injection site reactions"]
        },
        "guideline_tags": [
            "ACR Guidelines - Rheumatoid Arthritis",
            "FDA Black Box Warning - Sarilumab and Serious Infections",
            "FDA Black Box Warning - Sarilumab and Neutropenia/Thrombocytopenia",
            "FDA Black Box Warning - Sarilumab and Hepatotoxicity"
        ]
    },
    
    "Secukinumab": {
        "group": "Biological - Monoclonal Antibody (anti-IL-17A)",
        "vietnamese_name": "Secukinumab, Cosentyx",
        "administration": ["SC"],
        "indications": [
            "Vảy nến (psoriasis) - trung bình đến nặng",
            "Viêm khớp vảy nến (PsA)",
            "Viêm cột sống dính khớp (AS)",
            "Viêm cột sống dính khớp không X-quang (nr-axSpA)"
        ],
        "contraindications": [
            "Dị ứng secukinumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult_psoriasis": "300mg SC ngày 0, 1, 2, 3, 4 tuần, sau đó 300mg SC mỗi tháng",
            "adult_psa": "150mg SC ngày 0, 1, 2, 3, 4 tuần, sau đó 150mg SC mỗi tháng (có thể tăng lên 300mg nếu cần)",
            "adult_as": "150mg SC ngày 0, 1, 2, 3, 4 tuần, sau đó 150mg SC mỗi tháng",
            "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhiễm trùng nấm Candida - tăng nguy cơ",
            "Bệnh viêm ruột (IBD) - tăng nguy cơ, đặc biệt Crohn",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Đau đầu",
            "Tiêu chảy",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Secukinumab là kháng thể đơn dòng kháng IL-17A (interleukin-17A, fully human monoclonal antibody). IL-17A là cytokine quan trọng trong quá trình viêm qua trung gian Th17 cells. IL-17A kích hoạt các tế bào viêm → tăng sản xuất các cytokine và chemokine khác → gây viêm mạn tính → tổn thương mô. Trong vảy nến và viêm khớp, IL-17A tăng cao → gây viêm da và khớp. Secukinumab gắn với IL-17A → ngăn chặn IL-17A gắn với receptor → ức chế signaling → giảm viêm. Dẫn đến: giảm triệu chứng và cải thiện chức năng trong vảy nến và viêm khớp. Secukinumab được dùng để điều trị vảy nến, viêm khớp vảy nến, và viêm cột sống dính khớp.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Nhiễm trùng nấm Candida - tăng nguy cơ, theo dõi triệu chứng",
            "Bệnh viêm ruột (IBD) - theo dõi triệu chứng tiêu hóa, đặc biệt Crohn",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Phản ứng tại chỗ tiêm",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng secukinumab nếu có nhiễm trùng nặng",
            "Theo dõi nhiễm trùng nấm Candida - điều trị nếu có",
            "Thận trọng ở bệnh nhân có tiền sử IBD - tăng nguy cơ, đặc biệt Crohn",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động"
        ],
        "pharmacokinetics": {
            "half_life": "27 ngày (dao động 20-35 ngày)",
            "onset": "Vài tuần",
            "duration": "1 tháng (liều mỗi tháng)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 15-30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ bệnh viêm ruột (IBD), đặc biệt Crohn.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Secukinumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị secukinumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng secukinumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử lao - cần điều trị dự phòng",
                "Tiền sử IBD - tăng nguy cơ, đặc biệt Crohn",
                "Nhiễm trùng nấm Candida đang hoạt động - có thể làm nặng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Secukinumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Secukinumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Secukinumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng secukinumab",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 150mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 15-30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Secukinumab (Cosentyx)",
                "UpToDate - Secukinumab: Drug information",
                "Lexicomp - Secukinumab monograph",
                "AAD Guidelines - Psoriasis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections", "Inflammatory bowel disease (IBD, especially Crohn) - increased risk", "Candida infections - increased risk"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Signs of infection - CRITICAL", "TB screening (PPD or IGRA) before treatment - CRITICAL", "Candida infections", "IBD symptoms (especially Crohn) - CRITICAL", "CBC", "Hepatic function (ALT, AST)", "Injection site reactions"]
        },
        "guideline_tags": [
            "AAD Guidelines - Psoriasis",
            "ACR Guidelines - Psoriatic Arthritis",
            "ACR Guidelines - Ankylosing Spondylitis",
            "FDA Black Box Warning - Secukinumab and Serious Infections",
            "FDA Black Box Warning - Secukinumab and IBD"
        ]
    },
    
    "Tezepelumab": {
        "group": "Biological - Monoclonal Antibody (anti-TSLP)",
        "vietnamese_name": "Tezepelumab, Tezspire",
        "administration": ["SC"],
        "indications": [
            "Hen suyễn nặng (severe asthma) - kiểm soát kém, không phụ thuộc vào phenotype"
        ],
        "contraindications": [
            "Dị ứng tezepelumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult": "210mg SC mỗi 4 tuần",
            "pediatric_12_17": "210mg SC mỗi 4 tuần",
            "notes": "Tiêm dưới da. Có thể tự tiêm sau khi được hướng dẫn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhiễm trùng đường hô hấp trên",
            "Đau đầu",
            "Viêm họng",
            "Nhiễm trùng nặng - hiếm"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Tezepelumab là kháng thể đơn dòng kháng TSLP (thymic stromal lymphopoietin, fully human monoclonal antibody). TSLP là cytokine quan trọng trong quá trình viêm dị ứng và hen suyễn. TSLP được giải phóng từ tế bào biểu mô đường hô hấp khi có kích thích (dị ứng, nhiễm trùng, ô nhiễm) → kích hoạt các tế bào miễn dịch (dendritic cells, Th2 cells) → tăng sản xuất các cytokine viêm (IL-4, IL-5, IL-13) → gây viêm đường hô hấp và hen suyễn. Tezepelumab gắn với TSLP → ngăn chặn TSLP gắn với receptor → ức chế signaling → giảm viêm đường hô hấp. Dẫn đến: giảm cơn hen và cải thiện chức năng hô hấp trong hen suyễn nặng. Tezepelumab được dùng để điều trị hen suyễn nặng, không phụ thuộc vào phenotype (eosinophilic hoặc non-eosinophilic).",
        "monitoring": [
            "Phản ứng tại chỗ tiêm",
            "Chức năng hô hấp (FEV1) - đánh giá hiệu quả điều trị",
            "Tần suất cơn hen - giảm cơn hen",
            "Sử dụng corticosteroid (ICS) - có thể giảm liều",
            "Dấu hiệu nhiễm trùng đường hô hấp",
            "Dấu hiệu phản ứng dị ứng"
        ],
        "precautions": [
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động",
            "Không ngừng đột ngột các thuốc hen khác (ICS, LABA) - giảm dần dần",
            "Theo dõi chức năng hô hấp thường xuyên"
        ],
        "pharmacokinetics": {
            "half_life": "26 ngày (dao động 20-32 ngày)",
            "onset": "Vài tuần",
            "duration": "4 tuần",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần theo dõi nhiễm trùng và không ngừng đột ngột các thuốc hen khác.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Tezepelumab làm thay đổi đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị tezepelumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tezepelumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - thận trọng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Tezepelumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Tezepelumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Tezepelumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng dị ứng nặng",
                "Nhiễm trùng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng tezepelumab",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine, epinephrine nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 210mg/1.91ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần. Có thể tự tiêm sau khi được hướng dẫn."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tezepelumab (Tezspire)",
                "UpToDate - Tezepelumab: Drug information",
                "Lexicomp - Tezepelumab monograph",
                "GINA Guidelines - Asthma"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Serious infections (rare)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Injection site reactions (pain, redness, swelling)", "Respiratory function (FEV1) - assess treatment response", "Asthma exacerbation frequency - reduction in asthma attacks", "ICS use - may reduce dose", "Signs of respiratory infection", "Signs of serious infection"]
        },
        "guideline_tags": [
            "GINA Guidelines - Severe Asthma",
            "FDA Drug Information - Tezepelumab"
        ]
    },
    
    "Tocilizumab": {
        "group": "Biological - Monoclonal Antibody (anti-IL-6R)",
        "vietnamese_name": "Tocilizumab, Actemra",
        "administration": ["IV", "SC"],
        "indications": [
            "Viêm khớp dạng thấp (RA) - trung bình đến nặng",
            "Viêm khớp vị thành niên (JIA) - polyarticular và systemic",
            "Giant cell arteritis (GCA)",
            "COVID-19 - viêm nặng (hospitalized, requiring oxygen)"
        ],
        "contraindications": [
            "Dị ứng tocilizumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị",
            "Giảm bạch cầu nặng (ANC <500/mm³)",
            "Giảm tiểu cầu nặng (<50,000/mm³)"
        ],
        "dosage": {
            "adult_ra_iv": "4mg/kg IV mỗi 4 tuần (có thể tăng lên 8mg/kg nếu cần)",
            "adult_ra_sc": "162mg SC mỗi tuần (nếu <100kg) hoặc 162mg SC mỗi 2 tuần (nếu ≥100kg)",
            "adult_gca_sc": "162mg SC mỗi tuần (kết hợp với corticosteroid)",
            "adult_covid19_iv": "8mg/kg IV một lần (tối đa 800mg), có thể lặp lại sau 8-24 giờ nếu không cải thiện",
            "pediatric_jia_iv": "Weight-based IV: 8mg/kg nếu <30kg, 12mg/kg nếu ≥30kg, mỗi 2-4 tuần",
            "notes": "Truyền tĩnh mạch hoặc tiêm dưới da. Test lao trước khi dùng. Theo dõi công thức máu chặt chẽ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng cơ hội, lao)",
            "Giảm bạch cầu, tiểu cầu - phổ biến, có thể nghiêm trọng",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Tăng cholesterol, triglyceride - phổ biến",
            "Phản ứng truyền (infusion reaction) - khi dùng IV",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - khi dùng SC",
            "Rối loạn tiêu hóa (buồn nôn, tiêu chảy)",
            "Đau đầu",
            "Mệt mỏi"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Tocilizumab là kháng thể đơn dòng kháng IL-6R (interleukin-6 receptor, humanized monoclonal antibody). IL-6 là cytokine quan trọng trong quá trình viêm, được sản xuất bởi đại thực bào, tế bào T, và các tế bào khác. IL-6 gắn với IL-6R (có thể là membrane-bound hoặc soluble) → kích hoạt signaling (JAK/STAT pathway) → tăng sản xuất các cytokine và chemokine khác → gây viêm mạn tính → tổn thương mô. Trong RA, GCA, và COVID-19, IL-6 tăng cao → gây viêm nặng. Tocilizumab gắn với cả membrane-bound và soluble IL-6R → ngăn chặn IL-6 gắn với receptor → ức chế signaling → giảm viêm. Dẫn đến: giảm triệu chứng và làm chậm tiến triển bệnh. Tocilizumab được dùng để điều trị RA, JIA, GCA, và COVID-19 nặng.",
        "monitoring": [
            "Công thức máu (CBC) - QUAN TRỌNG: giảm bạch cầu, tiểu cầu phổ biến, theo dõi mỗi 4-8 tuần",
            "Chức năng gan (ALT, AST) - tăng men gan phổ biến, theo dõi mỗi 4-8 tuần",
            "Lipid panel (cholesterol, triglyceride) - tăng lipid phổ biến, theo dõi mỗi 4-8 tuần",
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Phản ứng truyền hoặc phản ứng tại chỗ tiêm"
        ],
        "precautions": [
            "THEO DÕI CÔNG THỨC MÁU CHẶT CHẼ - giảm bạch cầu, tiểu cầu phổ biến và có thể nghiêm trọng",
            "Ngừng tocilizumab nếu ANC <500/mm³ hoặc platelet <50,000/mm³",
            "THEO DÕI CHỨC NĂNG GAN CHẶT CHẼ - tăng men gan phổ biến",
            "Ngừng tocilizumab nếu ALT/AST >5x ULN",
            "THEO DÕI LIPID - tăng cholesterol, triglyceride phổ biến, điều trị nếu cần",
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng tocilizumab nếu có nhiễm trùng nặng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có giảm bạch cầu, tiểu cầu từ trước"
        ],
        "pharmacokinetics": {
            "half_life": "8-14 ngày (dao động rộng)",
            "onset": "Vài tuần",
            "duration": "1-4 tuần (liều mỗi 1-4 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life trung bình."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ. Dạng SC: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi dùng.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng, đặc biệt lao và nhiễm trùng cơ hội. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. GIẢM BẠCH CẦU, TIỂU CẦU - phổ biến và có thể nghiêm trọng. Theo dõi công thức máu chặt chẽ. Ngừng nếu ANC <500/mm³ hoặc platelet <50,000/mm³. TĂNG MEN GAN - phổ biến. Theo dõi chức năng gan chặt chẽ. Ngừng nếu ALT/AST >5x ULN.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (methotrexate, corticosteroid)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Tocilizumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị tocilizumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tocilizumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị",
                "Giảm bạch cầu nặng (ANC <500/mm³)",
                "Giảm tiểu cầu nặng (<50,000/mm³)"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử lao - cần điều trị dự phòng",
                "Giảm bạch cầu, tiểu cầu từ trước - có thể làm nặng",
                "Tăng men gan từ trước - có thể làm nặng",
                "Tăng lipid từ trước - có thể làm nặng",
                "Có thai (category C) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tocilizumab là FDA category C. Có thể dùng trong thai kỳ khi cần thiết (RA, COVID-19 nặng). Một số nghiên cứu cho thấy tăng nguy cơ dị tật bẩm sinh, nhưng cần cân nhắc lợi ích/rủi ro. Cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Tocilizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Tocilizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, cần theo dõi chặt chẽ chức năng gan (có thể tăng men gan)."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Giảm bạch cầu nặng (ANC <500/mm³)",
                "Giảm tiểu cầu nặng (<50,000/mm³)",
                "Tăng men gan nặng (ALT/AST >5x ULN)",
                "Phản ứng truyền nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng tocilizumab",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi và hỗ trợ giảm bạch cầu, tiểu cầu (truyền tiểu cầu nếu cần)",
                "Theo dõi chức năng gan",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, công thức máu, chức năng gan, dấu hiệu nhiễm trùng, phản ứng truyền trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 0.4-4mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 1 giờ.",
                "compatibility": ["NS"],
                "incompatibility": ["D5W", "Không pha với các thuốc khác"],
                "notes": "Premedication: corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền (nếu cần). Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu."
            },
            "sc": {
                "reconstitution": "Dạng SC: 162mg/0.9ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tocilizumab (Actemra)",
                "UpToDate - Tocilizumab: Drug information",
                "Lexicomp - Tocilizumab monograph",
                "ACR Guidelines - Rheumatoid Arthritis",
                "WHO Guidelines - COVID-19"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Trastuzumab": {
        "group": "Biological - Monoclonal Antibody (anti-HER2)",
        "vietnamese_name": "Trastuzumab, Herceptin",
        "administration": ["IV", "SC"],
        "indications": [
            "Ung thư vú HER2 dương tính (early và metastatic)",
            "Ung thư dạ dày HER2 dương tính (metastatic)",
            "Ung thư thực quản HER2 dương tính (metastatic)"
        ],
        "contraindications": [
            "Dị ứng trastuzumab",
            "Suy tim nặng (LVEF <50% hoặc NYHA class III-IV)",
            "Có thai (category D)"
        ],
        "dosage": {
            "adult_breast_iv": "Loading: 8mg/kg IV, sau đó 6mg/kg IV mỗi 3 tuần. Hoặc 4mg/kg IV, sau đó 2mg/kg IV mỗi tuần.",
            "adult_breast_sc": "600mg SC mỗi 3 tuần (sau loading 8mg/kg IV)",
            "adult_gastric": "8mg/kg IV loading, sau đó 6mg/kg IV mỗi 3 tuần (kết hợp với chemotherapy)",
            "notes": "Theo dõi LVEF trước và trong điều trị. Ngừng nếu LVEF giảm đáng kể."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Tổn thương tim (suy tim, giảm LVEF) - NGUY HIỂM, phổ biến",
            "Phản ứng truyền (infusion reaction) - phổ biến lần đầu",
            "Giảm bạch cầu, tiểu cầu (khi kết hợp với chemotherapy)",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Mệt mỏi",
            "Đau cơ, đau khớp",
            "Phản ứng tại chỗ tiêm (SC)"
        ],
        "interactions": [
            "Anthracyclines (doxorubicin, epirubicin) - tăng nguy cơ tổn thương tim",
            "Cyclophosphamide - tăng nguy cơ tổn thương tim"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Trastuzumab là kháng thể đơn dòng kháng HER2 (humanized monoclonal antibody). HER2 (human epidermal growth factor receptor 2, còn gọi là ErbB2) là thụ thể tyrosine kinase, thường overexpressed trong 15-20% ung thư vú. HER2 overactivation → tăng tín hiệu tăng trưởng → tăng sinh tế bào ung thư. Trastuzumab gắn với domain ngoại bào của HER2 → ức chế dimerization và signaling → giảm tăng sinh tế bào ung thư. Ngoài ra, trastuzumab kích hoạt ADCC → tiêu diệt tế bào ung thư. Dẫn đến: ức chế tăng trưởng và tiêu diệt tế bào ung thư HER2 dương tính. Trastuzumab được dùng để điều trị ung thư vú, dạ dày, thực quản HER2 dương tính.",
        "monitoring": [
            "LVEF (echocardiogram hoặc MUGA scan) - QUAN TRỌNG: trước điều trị, mỗi 3 tháng trong năm đầu, sau đó mỗi 6 tháng",
            "Dấu hiệu suy tim (khó thở, phù, mệt mỏi) - tổn thương tim phổ biến",
            "Phản ứng truyền (infusion reaction) - phổ biến lần đầu",
            "Công thức máu (khi kết hợp với chemotherapy)",
            "Chức năng gan (khi kết hợp với chemotherapy)"
        ],
        "precautions": [
            "THEO DÕI LVEF TRƯỚC VÀ TRONG ĐIỀU TRỊ - tổn thương tim phổ biến và có thể vĩnh viễn",
            "Ngừng trastuzumab nếu LVEF giảm >16% từ baseline hoặc LVEF <50%",
            "Tránh dùng với anthracyclines (doxorubicin, epirubicin) - tăng nguy cơ tổn thương tim nghiêm trọng",
            "Thận trọng với cyclophosphamide - tăng nguy cơ tổn thương tim",
            "Premedication với corticosteroid, antihistamine để giảm phản ứng truyền (nếu cần)",
            "Theo dõi dấu hiệu suy tim chặt chẽ",
            "Điều trị suy tim nếu xảy ra (ACE inhibitor, beta blocker, diuretic)"
        ],
        "pharmacokinetics": {
            "half_life": "28 ngày (dao động 1-32 ngày)",
            "onset": "Vài tuần",
            "duration": "3-4 tuần (liều mỗi 3 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ. Dạng SC: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi dùng.",
        "black_box_warnings": "TỔN THƯƠNG TIM (suy tim, giảm LVEF) - phổ biến và có thể vĩnh viễn. Tăng nguy cơ khi dùng với anthracyclines. Theo dõi LVEF trước và trong điều trị. Ngừng nếu LVEF giảm đáng kể. Phản ứng truyền nặng có thể gây tử vong. Có thể gây tử vong thai nhi (category D).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Anthracyclines (doxorubicin, epirubicin, daunorubicin)",
                    "mechanism": "Cả hai đều có thể gây tổn thương tim, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tổn thương tim nghiêm trọng, suy tim, có thể tử vong",
                    "management": "Tránh dùng đồng thời. Nếu phải dùng, theo dõi LVEF chặt chẽ. Cân nhắc dùng anthracyclines trước, sau đó trastuzumab."
                },
                {
                    "drug": "Cyclophosphamide",
                    "mechanism": "Cả hai đều có thể gây tổn thương tim, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ tổn thương tim",
                    "management": "Thận trọng. Theo dõi LVEF chặt chẽ."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng trastuzumab",
                "Suy tim nặng (LVEF <50% hoặc NYHA class III-IV)",
                "Có thai (category D) - có thể gây tử vong thai nhi"
            ],
            "tương_đối": [
                "Suy tim nhẹ đến trung bình (LVEF 50-55%) - theo dõi chặt chẽ",
                "Tiền sử bệnh tim - tăng nguy cơ tổn thương tim",
                "Dùng với anthracyclines - tăng nguy cơ tổn thương tim nghiêm trọng",
                "Dùng với cyclophosphamide - tăng nguy cơ tổn thương tim"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Trastuzumab là FDA category D - có thể gây tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rủi ro. Có thể gây oligohydramnios, suy thận ở thai nhi, và tử vong thai nhi. Tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Trastuzumab bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Trastuzumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở, phù, sốc)",
                "Tổn thương tim nặng (suy tim cấp)",
                "Giảm bạch cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị suy tim: ACE inhibitor, beta blocker, diuretic, vận mạch nếu cần",
                "Theo dõi LVEF",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, LVEF, dấu hiệu suy tim, phản ứng truyền trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 21mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Loading: truyền trong 90 phút. Maintenance: truyền trong 30 phút nếu dung nạp tốt (có thể truyền trong 90 phút nếu có phản ứng).",
                "compatibility": ["NS"],
                "incompatibility": ["D5W (không ổn định)", "Không pha với các thuốc khác"],
                "notes": "Premedication: có thể dùng corticosteroid, antihistamine nếu có tiền sử phản ứng truyền. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu."
            },
            "sc": {
                "reconstitution": "Dạng SC: 600mg/5ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm)",
                "notes": "Chỉ dùng SC sau khi đã dùng loading dose IV. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Trastuzumab (Herceptin)",
                "UpToDate - Trastuzumab: Drug information",
                "Lexicomp - Trastuzumab monograph",
                "NCCN Guidelines - Breast Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Ustekinumab": {
        "group": "Biological - Monoclonal Antibody (anti-IL-12/23)",
        "vietnamese_name": "Ustekinumab, Stelara",
        "administration": ["SC", "IV"],
        "indications": [
            "Vảy nến (psoriasis) - trung bình đến nặng",
            "Viêm khớp vảy nến (PsA)",
            "Bệnh Crohn (Crohn's disease)",
            "Viêm loét đại tràng (UC)"
        ],
        "contraindications": [
            "Dị ứng ustekinumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult_psoriasis_sc": "45mg SC ngày 1, sau đó 45mg SC ngày 28, sau đó 45mg SC mỗi 12 tuần (nếu <100kg) hoặc 90mg SC mỗi 12 tuần (nếu ≥100kg)",
            "adult_psa_sc": "45mg SC ngày 1, sau đó 45mg SC ngày 28, sau đó 45mg SC mỗi 12 tuần",
            "adult_crohn_iv": "Weight-based IV loading: 260-390mg (tùy cân nặng), sau đó 90mg SC mỗi 8 tuần",
            "adult_uc_iv": "Weight-based IV loading: 260-390mg (tùy cân nặng), sau đó 90mg SC mỗi 8 tuần",
            "notes": "Tiêm dưới da hoặc truyền tĩnh mạch. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)",
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Phản ứng truyền (infusion reaction) - khi dùng IV",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da)",
            "Đau đầu",
            "Mệt mỏi",
            "Buồn nôn"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ustekinumab là kháng thể đơn dòng kháng IL-12 và IL-23 (interleukin-12/23, fully human monoclonal antibody). IL-12 và IL-23 là cytokines quan trọng trong quá trình viêm qua trung gian Th1 và Th17 cells. IL-12 kích hoạt Th1 cells → sản xuất IFN-γ → gây viêm. IL-23 kích hoạt Th17 cells → sản xuất IL-17A → gây viêm. Trong vảy nến và IBD, IL-12/IL-23 tăng cao → gây viêm mạn tính → tổn thương mô. Ustekinumab gắn với p40 subunit chung của IL-12 và IL-23 → ngăn chặn cả IL-12 và IL-23 gắn với receptor → ức chế signaling → giảm viêm. Dẫn đến: giảm triệu chứng và cải thiện chức năng trong vảy nến và IBD. Ustekinumab được dùng để điều trị vảy nến, viêm khớp vảy nến, Crohn, và UC.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Phản ứng tại chỗ tiêm hoặc phản ứng truyền",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng",
            "Dấu hiệu ung thư - tăng nguy cơ"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng ustekinumab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân có tiền sử ung thư - tăng nguy cơ",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động"
        ],
        "pharmacokinetics": {
            "half_life": "15-32 ngày (dao động rộng)",
            "onset": "Vài tuần",
            "duration": "8-12 tuần (liều mỗi 8-12 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Không để ở nhiệt độ phòng quá 14 ngày. Để nhiệt độ phòng 30 phút trước khi tiêm.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Tăng nguy cơ ung thư (lymphoma, ung thư da).",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Ustekinumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị ustekinumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ustekinumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử lao - cần điều trị dự phòng",
                "Tiền sử ung thư - tăng nguy cơ",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ustekinumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết. Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Ustekinumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Ustekinumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng dị ứng nặng",
                "Phản ứng truyền nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ustekinumab",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, phản ứng truyền, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng SC: 45mg/0.5ml hoặc 90mg/ml, tiêm dưới da",
                "injection_site": "Vùng đùi, bụng (tránh vùng quanh rốn 5cm), cánh tay",
                "notes": "Để nhiệt độ phòng 30 phút trước khi tiêm. Tiêm dưới da, không tiêm vào cơ hoặc mạch máu. Thay đổi vị trí tiêm mỗi lần."
            },
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 0.5-5mg/ml.",
                "infusion_rate": "Truyền trong ít nhất 1 giờ.",
                "compatibility": ["NS"],
                "incompatibility": ["D5W", "Không pha với các thuốc khác"],
                "notes": "Premedication: corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền. Theo dõi chặt chẽ trong và sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ustekinumab (Stelara)",
                "UpToDate - Ustekinumab: Drug information",
                "Lexicomp - Ustekinumab monograph",
                "AAD Guidelines - Psoriasis"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
    "Vedolizumab": {
        "group": "Biological - Monoclonal Antibody (anti-integrin α4β7)",
        "vietnamese_name": "Vedolizumab, Entyvio",
        "administration": ["IV"],
        "indications": [
            "Bệnh Crohn (Crohn's disease) - trung bình đến nặng",
            "Viêm loét đại tràng (UC) - trung bình đến nặng"
        ],
        "contraindications": [
            "Dị ứng vedolizumab hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng chưa điều trị"
        ],
        "dosage": {
            "adult_crohn": "300mg IV ngày 0, 2, 6 tuần, sau đó 300mg IV mỗi 8 tuần",
            "adult_uc": "300mg IV ngày 0, 2, 6 tuần, sau đó 300mg IV mỗi 8 tuần",
            "notes": "Truyền trong 30 phút. Premedication với corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền. Test lao trước khi dùng."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Nhiễm trùng - phổ biến, có thể nghiêm trọng (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu)",
            "Phản ứng truyền (infusion reaction) - phổ biến",
            "Nhiễm trùng nặng - có thể nghiêm trọng",
            "Đau đầu",
            "Buồn nôn",
            "Tiêu chảy",
            "Mệt mỏi",
            "Đau khớp"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể làm giảm đáp ứng vaccine (sống)",
            "Tăng nguy cơ nhiễm trùng khi dùng với các thuốc ức chế miễn dịch khác"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Vedolizumab là kháng thể đơn dòng kháng integrin α4β7 (humanized monoclonal antibody). Integrin α4β7 là phân tử kết dính trên tế bào T và B, giúp các tế bào này di chuyển từ máu vào mô ruột. Tế bào T/B gắn với MAdCAM-1 (mucosal addressin cell adhesion molecule-1) trên tế bào nội mô ruột qua integrin α4β7 → di chuyển vào mô ruột → gây viêm trong IBD. Vedolizumab gắn với integrin α4β7 → ngăn chặn integrin α4β7 gắn với MAdCAM-1 → ức chế di chuyển tế bào T/B vào mô ruột → giảm viêm ruột. Dẫn đến: giảm triệu chứng và làm chậm tiến triển bệnh trong Crohn và UC. Vedolizumab được dùng để điều trị Crohn và UC trung bình đến nặng, đặc biệt hiệu quả khi các thuốc khác không đáp ứng.",
        "monitoring": [
            "Nhiễm trùng - theo dõi dấu hiệu nhiễm trùng trong và sau điều trị",
            "Lao (tuberculosis) - test PPD hoặc IGRA trước khi dùng, theo dõi trong điều trị",
            "Dấu hiệu nhiễm trùng cơ hội (PCP, CMV, herpes, fungal)",
            "Phản ứng truyền",
            "Chức năng gan: ALT, AST - mỗi 3-6 tháng",
            "Công thức máu: CBC - mỗi 3-6 tháng",
            "Dấu hiệu bệnh tiến triển (Crohn, UC)"
        ],
        "precautions": [
            "TEST LAO TRƯỚC KHI DÙNG (PPD hoặc IGRA) - lao có thể tái hoạt",
            "Điều trị dự phòng lao nếu có tiền sử lao hoặc test dương tính",
            "Premedication với corticosteroid, antihistamine, acetaminophen để giảm phản ứng truyền",
            "Truyền chậm trong 30 phút",
            "Theo dõi phản ứng truyền chặt chẽ - phổ biến",
            "Theo dõi dấu hiệu nhiễm trùng chặt chẽ - tăng nguy cơ nhiễm trùng",
            "Ngừng vedolizumab nếu có nhiễm trùng nặng",
            "Không dùng vaccine sống trong và sau điều trị",
            "Thận trọng ở bệnh nhân có nhiễm trùng đang hoạt động"
        ],
        "pharmacokinetics": {
            "half_life": "25 ngày (dao động 15-22 ngày)",
            "onset": "Vài tuần",
            "duration": "8 tuần (liều mỗi 8 tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua hệ thống RES, tương tự các immunoglobulin khác",
            "clearance": "Chuyển hóa qua RES, thải trừ qua thận một phần. Half-life dài."
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng (15-30°C) hoặc tủ lạnh (2-8°C), dùng trong 24 giờ.",
        "black_box_warnings": "NHIỄM TRÙNG NẶNG - tăng nguy cơ nhiễm trùng nghiêm trọng. Test lao trước khi dùng. Điều trị dự phòng lao nếu cần. Ngừng nếu có nhiễm trùng nặng. Phản ứng truyền nặng có thể gây tử vong.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Các thuốc ức chế miễn dịch khác (methotrexate, azathioprine, 6-mercaptopurine)",
                    "mechanism": "Tác dụng cộng dồn ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng, đặc biệt nhiễm trùng cơ hội",
                    "management": "Thận trọng. Cần phòng ngừa nhiễm trùng chặt chẽ (PCP prophylaxis, v.v.)."
                },
                {
                    "drug": "Vaccines (sống)",
                    "mechanism": "Vedolizumab làm giảm đáp ứng miễn dịch",
                    "effect": "Giảm hiệu quả vaccine, tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "Không dùng vaccine sống trong và sau điều trị vedolizumab. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng vedolizumab hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng chưa điều trị"
            ],
            "tương_đối": [
                "Nhiễm trùng đang hoạt động - tăng nguy cơ",
                "Tiền sử lao - cần điều trị dự phòng",
                "Có thai (category B) - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Vedolizumab là FDA category B. Có thể dùng trong thai kỳ khi cần thiết (Crohn, UC nặng). Một số nghiên cứu cho thấy an toàn trong thai kỳ, nhưng cần theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Vedolizumab bài tiết vào sữa mẹ ở nồng độ thấp. Có thể dùng khi cho con bú với theo dõi trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Theo dõi trẻ về dấu hiệu nhiễm trùng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, không cần điều chỉnh liều",
            "notes": "Vedolizumab không chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Nhiễm trùng nặng",
                "Phản ứng truyền nặng (sốt cao, ớn lạnh, khó thở, phù, sốc)",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị phản ứng truyền: corticosteroid IV, antihistamine, epinephrine nếu cần",
                "Điều trị sốc: dịch, vận mạch nếu cần",
                "Điều trị nhiễm trùng nếu có",
                "Điều trị phản ứng dị ứng: corticosteroid, antihistamine nếu cần",
                "Theo dõi chặt chẽ trong ít nhất 24-48 giờ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, phản ứng truyền, dấu hiệu nhiễm trùng, dấu hiệu phản ứng dị ứng trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS. Pha loãng đến nồng độ 0.6-6mg/ml. Lọc qua filter 0.2-0.22 micron.",
                "infusion_rate": "Truyền trong 30 phút.",
                "compatibility": ["NS"],
                "incompatibility": ["D5W", "Không pha với các thuốc khác"],
                "notes": "Premedication: methylprednisolone 125mg IV (hoặc tương đương), diphenhydramine 50mg IV/PO, acetaminophen 650-1000mg PO, 30-60 phút trước truyền. Theo dõi chặt chẽ trong và sau truyền, đặc biệt lần đầu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vedolizumab (Entyvio)",
                "UpToDate - Vedolizumab: Drug information",
                "Lexicomp - Vedolizumab monograph",
                "ACG Guidelines - Inflammatory Bowel Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, extensive clinical data, widely used"
        }
    },
    
}

__all__ = ['BIOLOGICAL_DRUGS']

