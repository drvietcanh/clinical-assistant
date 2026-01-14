"""
Glycopeptide and Lipopeptide Antibiotics
Vancomycin (Glycopeptide)
Daptomycin (Lipopeptide)
"""

GLYCOPEPTIDE_ANTIBIOTICS = {
    "Daptomycin":     {
        "group": "Antibiotic - Lipopeptide",
        "vietnamese_name": "Daptomycin, Cubicin",
        "administration": [
            "IV"
    ],
        "indications": [
            "Nhiễm khuẩn da và mô mềm phức tạp (cSSTI) do Gram-dương",
            "Nhiễm khuẩn huyết do S. aureus (kể cả MRSA)",
            "Viêm nội tâm mạc do S. aureus (kể cả MRSA)",
            "Nhiễm khuẩn do MRSA (Methicillin-resistant Staphylococcus aureus)",
            "Nhiễm khuẩn do VRE (Vancomycin-resistant Enterococcus)",
            "Nhiễm khuẩn do Enterococcus (kể cả VRE)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với daptomycin",
                "Viêm cơ (myositis) - CHỐNG CHỈ ĐỊNH"
    ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều",
                "Đang dùng statin hoặc fibrate - tăng nguy cơ viêm cơ"
    ],
        },
        "dosage": {
            "adult_standard": "4-6 mg/kg IV x 1 lần/ngày",
            "adult_ssti": "4 mg/kg IV x 1 lần/ngày",
            "adult_bacteremia": "6 mg/kg IV x 1 lần/ngày",
            "adult_endocarditis": "6-10 mg/kg IV x 1 lần/ngày",
            "adult_vre": "6-10 mg/kg IV x 1 lần/ngày",
            "notes": """Truyền IV trong 30 phút. Liều cao hơn (6-10 mg/kg) cho nhiễm khuẩn huyết, viêm nội tâm mạc, VRE. Cần theo dõi CPK (creatine phosphokinase) để phát hiện viêm cơ.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "4-6 mg/kg IV mỗi 48 giờ",
            "under_30": "4-6 mg/kg IV mỗi 48 giờ (bao gồm hemodialysis)",
            "hemodialysis": "4-6 mg/kg IV sau lọc máu (mỗi 48 giờ)",
        },
        "side_effects": [
            "Viêm cơ (myositis) - tăng CPK, đau cơ, yếu cơ, có thể dẫn đến rhabdomyolysis",
            "Độc thận (nephrotoxicity) - tăng creatinine, hiếm",
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Tăng CPK (creatine phosphokinase) - dấu hiệu viêm cơ",
            "Giảm bạch cầu (hiếm)"
    ],
        "interactions": [
            "Statins (Atorvastatin, Simvastatin, Rosuvastatin): tăng nguy cơ viêm cơ, rhabdomyolysis",
            "Fibrates (Gemfibrozil): tăng nguy cơ viêm cơ",
            "Aminoglycosides: có thể tăng độc thận",
            "Warfarin: có thể tăng INR"
    ],
        "pregnancy": "B - Sử dụng nếu lợi ích > nguy cơ",
        "mechanism_of_action": """Daptomycin là lipopeptide kháng sinh, gắn với màng tế bào vi khuẩn Gram-dương và tạo lỗ thủng trong màng, gây mất gradient ion và dẫn đến chết tế bào. Khác với vancomycin (ức chế tổng hợp thành tế bào), daptomycin tác động trực tiếp lên màng tế bào. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - kể cả MRSA, Staphylococcus epidermidis, Streptococcus, Enterococcus - kể cả VRE), không có hoạt tính với Gram-âm hoặc kỵ khí. Đặc điểm: phụ thuộc nồng độ (concentration-dependent killing), có hiệu ứng hậu kháng sinh, dùng 1 lần/ngày. CHỐNG CHỈ ĐỊNH trong viêm phổi (bị bất hoạt bởi surfactant phổi).""",
        "monitoring": [
            "CPK (Creatine Phosphokinase) - BẮT BUỘC: 1-2 lần/tuần, hoặc ngay khi có triệu chứng đau cơ, yếu cơ",
            "Mục tiêu: CPK <5x ULN (upper limit of normal). Nếu CPK >5x ULN hoặc có triệu chứng viêm cơ → DỪNG NGAY",
            "Chức năng thận (creatinine, eGFR) - hàng tuần, đặc biệt quan trọng vì độc thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Triệu chứng viêm cơ: đau cơ, yếu cơ, sưng cơ, nước tiểu sẫm màu (myoglobinuria)",
            "Công thức máu (CBC) - nếu dùng kéo dài",
            "PT/INR (nếu dùng với warfarin)"
    ],
        "precautions": [
            "CPK monitoring BẮT BUỘC - không dùng nếu không có khả năng theo dõi CPK",
            "Viêm cơ (myositis) - CHỐNG CHỈ ĐỊNH nếu có tiền sử viêm cơ, rhabdomyolysis",
            "DỪNG NGAY nếu CPK >5x ULN hoặc có triệu chứng viêm cơ (đau cơ, yếu cơ)",
            "Tránh dùng với statins hoặc fibrates - tăng nguy cơ viêm cơ, rhabdomyolysis",
            "CHỐNG CHỈ ĐỊNH trong viêm phổi - bị bất hoạt bởi surfactant phổi, không hiệu quả",
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Truyền IV trong 30 phút",
            "Thận trọng ở người cao tuổi, suy thận, có tiền sử bệnh cơ",
            "Theo dõi chức năng thận nếu dùng kéo dài",
            "Pha trong NS, truyền IV trong 30 phút"
    ],
        "pharmacokinetics": {
            "half_life": "8-9 giờ",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "24 giờ (liều 1 lần/ngày)",
            "protein_binding": "90-93% (rất cao)",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (78% bài tiết nguyên dạng), cần điều chỉnh thận",
            "volume_of_distribution": "0.1 L/kg (thấp, phân bố kém)",
        },
        "storage": """Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 12 giờ, hoặc trong tủ lạnh 48 giờ. Không đông lạnh.""",
        "black_box_warnings": """Viêm cơ (myositis) - có thể dẫn đến rhabdomyolysis. Cần theo dõi CPK thường xuyên. DỪNG NGAY nếu CPK >5x ULN hoặc có triệu chứng viêm cơ. CHỐNG CHỈ ĐỊNH trong viêm phổi (bị bất hoạt bởi surfactant phổi).""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Statins (Atorvastatin, Simvastatin, Rosuvastatin, Pravastatin)",
                    "mechanism": "Cả hai đều có thể gây viêm cơ, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ viêm cơ, rhabdomyolysis nặng",
                    "management": """Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi CPK sát (2-3 lần/tuần), dừng statin nếu CPK tăng. Dừng cả hai nếu CPK >5x ULN hoặc có triệu chứng viêm cơ.""",
                },
    {
                    "drug": "Fibrates (Gemfibrozil, Fenofibrate)",
                    "mechanism": "Cả hai đều có thể gây viêm cơ, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ viêm cơ, rhabdomyolysis",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi CPK sát, dừng fibrate nếu CPK tăng.",
                }
                ],
            "moderate": [
    {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cả hai đều có thể gây độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận",
                    "management": "Theo dõi chức năng thận sát nếu dùng đồng thời.",
                },
    {
                    "drug": "Warfarin",
                    "mechanism": "Daptomycin có thể ảnh hưởng đến đông máu",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần). Có thể cần giảm liều warfarin.",
                }
                ],
            "minor": [],
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Daptomycin (Cubicin)",
                "IDSA Guidelines - Antimicrobial Therapy, MRSA",
                "UpToDate - Daptomycin: Drug Information",
                "Medscape - Daptomycin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Daptomycin Monograph",
                "Micromedex - Daptomycin Drug Information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {
                "renal": "Moderate",
                "musculoskeletal": "High (myositis/rhabdomyolysis)",
            },
        },
        "guideline_tags": [
            "IDSA Guidelines - Methicillin-Resistant Staphylococcus aureus Infections",
            "IDSA Guidelines - Infective Endocarditis",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "IDSA Guidelines - Vancomycin-Resistant Enterococcus Infections",
            "WHO Essential Medicines List"
    ],
        "last_updated": "2025-02-18",
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": """Sử dụng nếu lợi ích vượt trội nguy cơ. Dữ liệu hạn chế nhưng được sử dụng rộng rãi. Theo dõi CPK và chức năng thận của mẹ.""",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ có bài tiết vào sữa mẹ hay không. Thận trọng khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho bú tạm thời hoặc đổi thuốc khác.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Daptomycin không chuyển hóa đáng kể qua gan, thải trừ chủ yếu qua thận.",
        },
        "overdose_management": {
            "symptoms": [
                "Viêm cơ (myositis) - tăng CPK, đau cơ, yếu cơ, rhabdomyolysis",
                "Độc thận (nephrotoxicity) - tăng creatinine"
    ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng daptomycin ngay",
                "Đo CPK ngay",
                "Nếu CPK >5x ULN hoặc có triệu chứng viêm cơ → DỪNG NGAY",
                "Đo chức năng thận",
                "Truyền dịch tích cực nếu rhabdomyolysis",
                "Theo dõi CPK và chức năng thận hàng ngày"
    ],
            "monitoring": "CPK (bắt buộc), creatinine, eGFR, triệu chứng viêm cơ (đau cơ, yếu cơ, nước tiểu sẫm màu).",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có thuốc giải độc đặc hiệu. Ngừng thuốc là biện pháp chính.",
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha trong NaCl 0.9%.",
                "infusion_rate": "Truyền IV trong 30 phút.",
                "notes": """CPK monitoring BẮT BUỘC. Điều chỉnh liều theo chức năng thận. DỪNG NGAY nếu CPK >5x ULN hoặc có triệu chứng viêm cơ. CHỐNG CHỈ ĐỊNH trong viêm phổi.""",
            },
        },
    },
    "Teicoplanin": {
        "group": "Antibiotic - Glycopeptide",
        "vietnamese_name": "Teicoplanin, Targocid",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do MRSA (Methicillin-resistant Staphylococcus aureus)",
            "Nhiễm khuẩn do Staphylococcus (kể cả MRSA)",
            "Nhiễm khuẩn do Enterococcus (kể cả một số VRE)",
            "Nhiễm khuẩn huyết",
            "Viêm nội tâm mạc",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn xương và khớp",
            "Nhiễm khuẩn đường tiết niệu phức tạp"
        ],
        "contraindications": [
            "Dị ứng teicoplanin",
            "Dị ứng vancomycin (có thể có phản ứng chéo)"
        ],
        "dosage": {
            "adult_loading": "400mg IV x 2 lần/ngày x 3 liều (ngày 1), sau đó 400mg IV x 1 lần/ngày",
            "adult_standard": "400mg IV x 1 lần/ngày (sau loading)",
            "adult_severe": "400mg IV x 2 lần/ngày (sau loading)",
            "adult_endocarditis": "12mg/kg IV x 2 lần/ngày x 3 liều (ngày 1), sau đó 12mg/kg IV x 1 lần/ngày",
            "adult_im": "400mg IM x 1 lần/ngày (sau loading IV)",
            "pediatric_loading": "10mg/kg IV x 2 lần/ngày x 3 liều (ngày 1), sau đó 10mg/kg IV x 1 lần/ngày",
            "notes": "Cần loading dose (3 liều trong ngày đầu). Sau đó dùng 1 lần/ngày (ưu điểm so với vancomycin). Có thể dùng IM (ưu điểm). Ít độc thận hơn vancomycin. Phổ biến ở Việt Nam."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 50-75% hoặc tăng khoảng cách đáng kể",
            "hemodialysis": "Liều sau lọc máu, cần TDM"
        },
        "side_effects": [
            "Độc thận (nephrotoxicity) - ít hơn vancomycin",
            "Độc thần kinh thính giác (ototoxicity) - hiếm, ít hơn vancomycin",
            "Phát ban (hiếm)",
            "Thrombophlebitis (viêm tĩnh mạch) tại vị trí tiêm",
            "Giảm bạch cầu (neutropenia) - hiếm",
            "Thrombocytopenia (giảm tiểu cầu) - hiếm",
            "Đau tại chỗ tiêm (IM)"
        ],
        "interactions": [
            "Aminoglycosides: có thể tăng độc thận (ít hơn vancomycin)",
            "Furosemide: có thể tăng độc thận",
            "Cisplatin: có thể tăng độc thận"
        ],
        "pregnancy": "C - Sử dụng nếu lợi ích > nguy cơ",
        "mechanism_of_action": "Teicoplanin là glycopeptide kháng sinh, tương tự vancomycin. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với D-alanyl-D-alanine của peptidoglycan, ngăn chặn quá trình transglycosylation và transpeptidation. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - kể cả MRSA, Staphylococcus epidermidis, Streptococcus pneumoniae, Enterococcus - kể cả một số VRE), không có hoạt tính với Gram-âm. ĐẶC ĐIỂM: (1) Thời gian bán thải dài (70-100 giờ) → dùng 1 lần/ngày sau loading (ưu điểm so với vancomycin), (2) Có thể dùng IM (ưu điểm), (3) Ít độc thận hơn vancomycin, (4) Ít gây red man syndrome hơn vancomycin, (5) Phổ biến ở Việt Nam. Cần loading dose (3 liều trong ngày đầu) để đạt nồng độ điều trị nhanh.",
        "monitoring": [
            "TDM (Therapeutic Drug Monitoring) - KHUYẾN CÁO: Trough (ngay trước liều tiếp theo)",
            "Mục tiêu: Trough 10-20 mg/L (nhiễm khuẩn thông thường), 20-30 mg/L (nhiễm khuẩn nặng như viêm nội tâm mạc)",
            "Chức năng thận (creatinine, eGFR) - hàng tuần (ít độc thận hơn vancomycin nhưng vẫn cần theo dõi)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Công thức máu (CBC) - nếu dùng kéo dài (>14 ngày)",
            "Dấu hiệu dị ứng (phát ban) - hiếm"
        ],
        "precautions": [
            "Cần loading dose (3 liều trong ngày đầu) để đạt nồng độ điều trị nhanh",
            "Sau loading: dùng 1 lần/ngày (ưu điểm so với vancomycin q8-12h)",
            "Có thể dùng IM (ưu điểm so với vancomycin chỉ dùng IV)",
            "Ít độc thận hơn vancomycin - nhưng vẫn cần theo dõi",
            "Ít gây red man syndrome hơn vancomycin - có thể truyền nhanh hơn",
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Tránh dùng với thuốc độc thận khác (aminoglycosides, furosemide, cisplatin)",
            "Thận trọng ở người cao tuổi, suy thận",
            "Theo dõi công thức máu nếu dùng kéo dài (>14 ngày)",
            "Pha trong NS hoặc D5W"
        ],
        "pharmacokinetics": {
            "half_life": "70-100 giờ (rất dài, cho phép dùng 1 lần/ngày)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "24 giờ (liều 1 lần/ngày sau loading)",
            "protein_binding": "90-95% (rất cao)",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (80-90% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": "Độc thận - ít hơn vancomycin nhưng vẫn có thể xảy ra, đặc biệt khi dùng với aminoglycoside. Cần TDM để tối ưu hiệu quả và giảm độc tính.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cả hai đều có thể độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận (ít hơn vancomycin nhưng vẫn có)",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Furosemide",
                    "mechanism": "Furosemide có thể tăng nồng độ teicoplanin trong thận",
                    "effect": "Tăng nguy cơ độc thận",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận sát."
                },
                {
                    "drug": "Cisplatin",
                    "mechanism": "Cả hai đều có thể độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận sát."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng teicoplanin"
            ],
            "tương_đối": [
                "Dị ứng vancomycin - có thể có phản ứng chéo (thận trọng)",
                "Suy thận nặng - giảm liều",
                "Bệnh nhân cao tuổi - tăng nhạy cảm"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Teicoplanin là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Teicoplanin có thể qua nhau thai. Nhiễm khuẩn nặng có thể gây nguy hiểm cho cả mẹ và thai nhi nếu không điều trị. Được sử dụng trong thai kỳ khi cần thiết.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết teicoplanin có bài tiết vào sữa mẹ hay không. Thời gian bán thải rất dài (70-100 giờ), protein binding rất cao (90-95%). Có thể bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ chủ yếu qua thận)",
            "notes": "Teicoplanin không chuyển hóa đáng kể, thải trừ chủ yếu qua thận. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Độc thận (tăng creatinine)",
                "Độc thần kinh thính giác (hiếm)",
                "Giảm bạch cầu, giảm tiểu cầu (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng teicoplanin",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Nếu độc thận:",
                "  - Bù dịch (NS, LR)",
                "  - Tránh thuốc độc thận khác",
                "  - Lọc máu (hemodialysis) nếu suy thận nặng",
                "Lọc máu (hemodialysis) - teicoplanin có thể được loại bỏ một phần",
                "Theo dõi: Chức năng thận, công thức máu, thính giác"
            ],
            "monitoring": "Theo dõi chức năng thận, công thức máu, thính giác liên tục cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Điều trị hỗ trợ. Lọc máu có thể giúp loại bỏ một phần teicoplanin."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha bột: 400mg trong 3ml NS = 133mg/ml, sau đó pha loãng trong 100-250ml NS hoặc D5W.",
                "infusion_rate": "Loading: 400mg IV x 2 lần/ngày x 3 liều (ngày 1), truyền trong 30 phút. Maintenance: 400mg IV x 1 lần/ngày, truyền trong 30 phút. Severe: 400mg IV x 2 lần/ngày.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."
                ],
                "notes": "QUAN TRỌNG: 1) Cần loading dose (3 liều trong ngày đầu), 2) Sau loading: dùng 1 lần/ngày (ưu điểm so với vancomycin), 3) Có thể truyền nhanh hơn vancomycin (30 phút), 4) Ít độc thận hơn vancomycin, 5) Có thể dùng IM (ưu điểm), 6) Phổ biến ở Việt Nam."
            },
            "im": {
                "reconstitution": "Pha bột: 400mg trong 3ml NS = 133mg/ml.",
                "injection_site": "Cơ lớn (đùi, cánh tay).",
                "notes": "IM: 400mg x 1 lần/ngày (sau loading IV). Tiêm sâu vào cơ, không tiêm vào mỡ dưới da. Có thể gây đau tại chỗ tiêm. Ưu điểm: có thể dùng ngoại trú sau khi đã loading IV."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Teicoplanin (Targocid)",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Teicoplanin: Drug Information",
                "European Guidelines - Teicoplanin",
                "Medscape - Teicoplanin Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, European guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate", "neurological": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Methicillin-Resistant Staphylococcus aureus Infections",
            "IDSA Guidelines - Infective Endocarditis",
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "European Guidelines - Antimicrobial Therapy",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
    "Vancomycin": {
        "group": "Antibiotic - Glycopeptide",
        "vietnamese_name": "Vancomycin, Vancocin",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do MRSA (Methicillin-resistant Staphylococcus aureus)",
            "Nhiễm khuẩn do Enterococcus (kể cả VRE - vancomycin-resistant enterococci với liều cao)",
            "Nhiễm khuẩn huyết",
            "Viêm nội tâm mạc",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn xương và khớp",
            "Viêm màng não do vi khuẩn (Gram-dương)",
            "Viêm đại tràng do C. difficile (uống)"
        ],
        "contraindications": [
            "Dị ứng vancomycin",
            "Suy thận nặng (CrCl <10) - thận trọng, cần điều chỉnh liều"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng vancomycin"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <10) - thận trọng, cần điều chỉnh liều"
            ]
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có độc tính thận hoặc phản ứng dị ứng nghiêm trọng (Red man syndrome)."},
        "dosage": {
            "adult_iv_standard": "15-20 mg/kg IV mỗi 8-12 giờ (dựa trên trọng lượng thực tế)",
            "adult_iv_severe": "15-20 mg/kg IV mỗi 8-12 giờ",
            "adult_iv_meningitis": "15-20 mg/kg IV mỗi 6-8 giờ",
            "adult_iv_endocarditis": "15-20 mg/kg IV mỗi 8-12 giờ",
            "adult_po_cdiff": "125-500mg PO x 4 lần/ngày x 10-14 ngày",
            "notes": "Cần TDM (therapeutic drug monitoring). Trough: 10-20 mg/L (nhiễm khuẩn thông thường), 15-20 mg/L (nhiễm khuẩn nặng). Truyền IV trong ít nhất 60 phút để tránh red man syndrome."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 50-75% hoặc tăng khoảng cách đáng kể",
            "hemodialysis": "Liều sau lọc máu, cần TDM"
        },
        "side_effects": [
            "Độc thận (nephrotoxicity) - tăng creatinine, đặc biệt khi dùng với aminoglycoside",
            "Độc thần kinh thính giác (ototoxicity) - hiếm, thường kết hợp với độc thận",
            "Red man syndrome (hội chứng người đỏ) - đỏ bừng mặt, cổ, ngực, hạ huyết áp (do truyền quá nhanh)",
            "Thrombophlebitis (viêm tĩnh mạch) tại vị trí tiêm",
            "Giảm bạch cầu (neutropenia) - hiếm, thường khi dùng kéo dài",
            "Thrombocytopenia (giảm tiểu cầu) - hiếm"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Furosemide: tăng độc thận",
            "Cisplatin: tăng độc thận",
            "Anesthesia: tăng nguy cơ red man syndrome"
        ],
        "pregnancy": "C - Sử dụng nếu lợi ích > nguy cơ",
        "mechanism_of_action": "Vancomycin là glycopeptide kháng sinh, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với D-alanyl-D-alanine của peptidoglycan, ngăn chặn quá trình transglycosylation và transpeptidation. Dẫn đến thành tế bào yếu và vỡ tế bào vi khuẩn. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus aureus - kể cả MRSA, Staphylococcus epidermidis, Streptococcus pneumoniae, Enterococcus - kể cả một số VRE với liều cao), không có hoạt tính với Gram-âm. Đặc điểm: phụ thuộc thời gian (time-dependent killing), cần duy trì nồng độ trên MIC, cần TDM để tối ưu hiệu quả và giảm độc tính.",
        "monitoring": [
            "TDM (Therapeutic Drug Monitoring) - BẮT BUỘC: Trough (ngay trước liều tiếp theo, ít nhất sau 1-2 liều)",
            "Mục tiêu: Trough 10-20 mg/L (nhiễm khuẩn thông thường), 15-20 mg/L (nhiễm khuẩn nặng như viêm nội tâm mạc, viêm màng não, viêm phổi)",
            "Chức năng thận (creatinine, eGFR) - hàng ngày, đặc biệt quan trọng vì độc thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Thính giác (audiometry) - nếu dùng kéo dài hoặc có dấu hiệu độc tính",
            "Công thức máu (CBC) - nếu dùng kéo dài (>14 ngày) để phát hiện giảm bạch cầu, giảm tiểu cầu",
            "Dấu hiệu red man syndrome (đỏ bừng, hạ huyết áp) - nếu truyền quá nhanh"
        ],
        "precautions": [
            "TDM BẮT BUỘC - không dùng nếu không có khả năng theo dõi nồng độ",
            "Độc thận - đặc biệt nguy hiểm khi dùng với aminoglycoside, furosemide, cisplatin",
            "Điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Truyền IV trong ít nhất 60 phút (liều chuẩn) để tránh red man syndrome",
            "Không truyền quá nhanh - nguy cơ red man syndrome (đỏ bừng, hạ huyết áp, có thể nguy hiểm)",
            "Tránh dùng với thuốc độc thận khác (aminoglycosides, furosemide, cisplatin)",
            "Thận trọng ở người cao tuổi, suy thận, mất nước",
            "Theo dõi công thức máu nếu dùng kéo dài (>14 ngày)",
            "Pha trong NS hoặc D5W, nồng độ không quá 5 mg/ml"
        ],
        "pharmacokinetics": {
            "half_life": "4-6 giờ (bình thường), 200-250 giờ (suy thận nặng)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều q8-12h (bình thường), q24-48h (suy thận)",
            "protein_binding": "30-55%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (80-90% bài tiết nguyên dạng), cần điều chỉnh thận",
            "volume_of_distribution": "0.4-1 L/kg"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 14 ngày. Không đông lạnh.",
        "black_box_warnings": "Độc thận - có thể không hồi phục, đặc biệt khi dùng với aminoglycoside. Cần TDM để tối ưu hiệu quả và giảm độc tính. Red man syndrome có thể xảy ra nếu truyền quá nhanh.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cả hai đều độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng, có thể không hồi phục",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận sát, TDM cho cả hai, giảm liều nếu cần."
                },
                {
                    "drug": "Furosemide",
                    "mechanism": "Furosemide tăng nồng độ vancomycin trong thận, tăng độc tính",
                    "effect": "Tăng nguy cơ độc thận",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận sát."
                },
                {
                    "drug": "Cisplatin",
                    "mechanism": "Cả hai đều độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu bắt buộc, theo dõi chức năng thận sát."
                }
            ]
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vancomycin",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Vancomycin: Drug Information",
                "Medscape - Vancomycin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Vancomycin Monograph",
                "Micromedex - Vancomycin Drug Information"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"renal": "Nephrotoxicity (Black Box Warning - may be irreversible, especially with aminoglycosides)", "neurological": "Ototoxicity (rare, may be irreversible)", "hematologic": "Neutropenia, thrombocytopenia (rare, with prolonged use)", "dermatologic": "Red Man Syndrome (infusion-related)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["TDM required (trough 10-20 mg/L) - Black Box Warning", "Renal function (creatinine, eGFR - daily, Black Box Warning for nephrotoxicity)", "Audiometry (ototoxicity risk with prolonged use)", "CBC (neutropenia, thrombocytopenia with prolonged use)", "Red Man Syndrome signs (infusion rate critical)", "Dose adjustment required for renal function"],
            "look_alike_sound_alike": ["Vancomycin", "Vincristine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Nephrotoxicity (may be irreversible)",
            "IDSA Guidelines - Methicillin-Resistant Staphylococcus aureus Infections",
            "IDSA Guidelines - Infective Endocarditis",
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "IDSA Guidelines - Clostridium difficile Infection",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation_details": ""
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },
        "overdose_management": {
            "symptoms": [],
            "treatment": "",
            "antidote": None
        },
        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": []
        },
    },
    
}

__all__ = ['GLYCOPEPTIDE_ANTIBIOTICS']

