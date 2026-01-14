"""
Penicillin Antibiotics (Core)
Amoxicillin, Ampicillin, Amoxicillin-clavulanate, Ampicillin-sulbactam, Nafcillin, Oxacillin
"""

PENICILLIN_ANTIBIOTICS = {
    "Amoxicillin": {
        "group": "Antibiotic - Penicillin (Aminopenicillin)",
        "vietnamese_name": "Amoxicillin, Amoxil",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp trên (viêm amidan, viêm xoang, viêm tai giữa)",
            "Viêm phổi cộng đồng nhẹ",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu không biến chứng",
            "H. pylori (phác đồ 3 hoặc 4 thuốc)",
        ],
        "contraindications": [
            "Dị ứng penicillin hoặc beta-lactam",
            "Tiền sử phản vệ với penicillin",
        ],
        "dosage": {
            "adult_standard": "500mg PO mỗi 8 giờ hoặc 875mg PO mỗi 12 giờ",
            "adult_sinusitis": "875mg PO mỗi 12 giờ x 5-7 ngày",
            "pediatric": "45-90mg/kg/ngày PO chia 2-3 lần (tối đa 4g/ngày)",
            "notes": "Uống trước hoặc sau ăn đều được. Liều cao 80-90mg/kg/ngày cho viêm tai giữa/viêm phổi cộng đồng.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm còn mỗi 12 giờ",
            "under_30": "Giảm còn mỗi 24 giờ",
            "hemodialysis": "Liều sau mỗi lần lọc",
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Tăng men gan nhẹ (hiếm)",
        ],
        "interactions": [
            "Allopurinol: tăng nguy cơ phát ban",
            "Warfarin: có thể tăng INR",
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Aminopenicillin, ức chế tổng hợp thành tế bào vi khuẩn (PBPs). Phổ: Streptococcus, Enterococcus (một số), H. influenzae không sinh beta-lactamase, một số Enterobacteriaceae; bị phá bởi beta-lactamase.",
        "monitoring": [
            "Dấu hiệu dị ứng",
            "Dấu hiệu nhiễm C. difficile nếu tiêu chảy kéo dài",
            "Chức năng thận khi cần chỉnh liều",
        ],
        "precautions": [
            "Phản ứng chéo với cephalosporin ~5-10%",
            "Điều chỉnh liều ở suy thận nặng",
            "Theo dõi tiêu chảy kéo dài (C. difficile)",
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ",
            "onset": "1-2 giờ (PO)",
            "duration": "q8-12h",
            "protein_binding": "17%",
            "clearance": "Thận (chủ yếu), cần chỉnh liều ở suy thận",
        },
        "storage": "Bảo quản viên ở nhiệt độ phòng, tránh ẩm.",
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng penicillin hoặc beta-lactam",
                "Tiền sử phản vệ với penicillin",
            ],
            "tương_đối": []
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng."},
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Acute Bacterial Sinusitis",
            "IDSA Guidelines - Acute Otitis Media",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Amoxicillin-clavulanate": {
        "group": "Antibiotic - Penicillin/Beta-lactamase Inhibitor",
        "vietnamese_name": "Amoxicillin-clavulanate, Augmentin",
        "administration": ["PO"],
        "indications": [
            "Viêm xoang, viêm tai giữa, viêm phổi cộng đồng",
            "Nhiễm khuẩn da/mô mềm do cắn động vật/người",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm H. influenzae, Moraxella sinh beta-lactamase",
        ],
        "contraindications": [
            "Dị ứng penicillin/beta-lactam",
            "Tiền sử vàng da ứ mật do amoxicillin-clavulanate",
        ],
        "dosage": {
            "adult_standard": "875/125mg PO mỗi 12 giờ hoặc 500/125mg PO mỗi 8 giờ",
            "adult_high_dose": "2000/125mg PO mỗi 12 giờ (viêm xoang nặng, viêm phổi cộng đồng)",
            "pediatric": "45-90mg/kg/ngày (tính theo amoxicillin) chia 2 lần (tối đa 4g amoxicillin/ngày)",
            "notes": "Dùng khi cần ức chế beta-lactamase (H. influenzae, Moraxella, cắn động vật). Uống cùng thức ăn để giảm kích ứng tiêu hóa.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Mỗi 12 giờ",
            "under_30": "Tránh dạng 875mg; dùng 500/125mg mỗi 12 giờ",
            "hemodialysis": "500/125mg sau mỗi lần lọc",
        },
        "side_effects": [
            "Tiêu chảy (phổ biến do clavulanate)",
            "Buồn nôn",
            "Phát ban",
            "Tăng men gan, vàng da ứ mật (hiếm)",
        ],
        "interactions": [
            "Probenecid: tăng nồng độ amoxicillin",
            "Allopurinol: tăng nguy cơ phát ban",
            "Warfarin: có thể tăng INR",
            "Thuốc tránh thai: có thể giảm hiệu quả (hiếm)",
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Amoxicillin ức chế thành tế bào; clavulanate ức chế beta-lactamase, mở rộng phổ tới vi khuẩn sinh beta-lactamase (H. influenzae, Moraxella, một số Enterobacteriaceae, MSSA).",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban, phản vệ)",
            "Chức năng gan (men gan, bilirubin) - đặc biệt quan trọng do nguy cơ vàng da ứ mật",
            "Chức năng thận khi cần chỉnh liều",
            "Dấu hiệu nhiễm C. difficile nếu tiêu chảy kéo dài",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
        ],
        "precautions": [
            "Tiêu chảy do clavulanate - dùng liều clavulanate thấp hơn (875/125 hoặc 2000/125)",
            "Uống với thức ăn",
            "Điều chỉnh liều ở suy thận",
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ (amoxicillin), 1 giờ (clavulanate)",
            "onset": "1-2 giờ sau khi uống",
            "duration": "q8-12h",
            "protein_binding": "17-20% (amoxicillin), 25% (clavulanate)",
            "metabolism": "Amoxicillin: không chuyển hóa đáng kể. Clavulanate: chuyển hóa một phần ở gan.",
            "clearance": "Thận (cả hai thành phần), cần điều chỉnh thận"
        },
        "storage": "Bảo quản viên ở nhiệt độ phòng, tránh ẩm. Dung dịch pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết amoxicillin ở thận, làm tăng nồng độ amoxicillin",
                    "effect": "Tăng nồng độ amoxicillin, tăng thời gian bán thải",
                    "management": "Có thể dùng cùng để tăng nồng độ amoxicillin. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "Allopurinol",
                    "mechanism": "Tăng nguy cơ phát ban dị ứng (cơ chế không rõ ràng)",
                    "effect": "Tăng nguy cơ phát ban, đặc biệt ở bệnh nhân có tiền sử dị ứng",
                    "management": "Thận trọng khi dùng cùng. Theo dõi dấu hiệu phát ban. Ngừng ngay nếu có phát ban."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm sản xuất vitamin K",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc tránh thai",
                    "mechanism": "Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm hấp thu estrogen",
                    "effect": "Có thể giảm hiệu quả thuốc tránh thai (hiếm)",
                    "management": "Sử dụng biện pháp tránh thai bổ sung trong thời gian dùng amoxicillin-clavulanate và 7 ngày sau khi ngừng."
                }
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng penicillin/beta-lactam",
                "Tiền sử vàng da ứ mật do amoxicillin-clavulanate",
            ],
            "tương_đối": []
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng."},
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Amoxicillin-clavulanate là thuốc phân loại B. Amoxicillin và clavulanate đều được coi là an toàn trong thai kỳ. Đã được sử dụng rộng rãi trong thai kỳ. Không có bằng chứng về nguy cơ dị tật thai nhi. Nhiễm khuẩn nặng có thể gây nguy hiểm cho cả mẹ và thai nhi nếu không điều trị.",
            "lactation": {
                "safety": "Compatible",
                "details": "Amoxicillin và clavulanate bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ. Có thể gây tiêu chảy nhẹ ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu dị ứng hoặc tiêu chảy."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Clavulanate chuyển hóa một phần ở gan nhưng không đáng kể.",
            "moderate": "Thận trọng. Clavulanate chuyển hóa một phần ở gan, có thể tích lũy nhẹ ở suy gan trung bình. Theo dõi chức năng gan.",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng. Clavulanate chuyển hóa ở gan, có thể tích lũy ở suy gan nặng. Nguy cơ vàng da ứ mật tăng. Theo dõi chức năng gan chặt chẽ.",
            "notes": "Clavulanate chuyển hóa một phần ở gan. Suy gan có thể làm giảm chuyển hóa clavulanate, nhưng ảnh hưởng ít hơn so với suy thận (thải trừ chủ yếu qua thận). Nguy cơ vàng da ứ mật tăng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy nặng",
                "Triệu chứng thần kinh: Co giật (hiếm, thường ở suy thận nặng)",
                "Triệu chứng gan: Vàng da ứ mật, tăng men gan",
                "Triệu chứng thận: Suy thận cấp (hiếm)",
                "Triệu chứng dị ứng: Phát ban, sốc phản vệ"
            ],
            "antidote": "Không có antidote đặc hiệu cho quá liều amoxicillin-clavulanate. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay amoxicillin-clavulanate nếu đang dùng",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước do tiêu chảy",
                "  - Theo dõi điện giải",
                "Điều trị co giật nếu có:",
                "  - Benzodiazepine (diazepam, lorazepam) IV",
                "  - Phenytoin hoặc fosphenytoin IV nếu cần",
                "Điều trị vàng da ứ mật nếu có:",
                "  - Ngừng amoxicillin-clavulanate",
                "  - Theo dõi chức năng gan (ALT, AST, bilirubin)",
                "  - Thường tự hồi phục sau khi ngừng thuốc",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần",
                "Điều trị sốc phản vệ nếu có:",
                "  - Epinephrine",
                "  - Antihistamines",
                "  - Corticosteroids",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn (huyết áp, nhịp tim, nhịp thở, SpO2) trong ít nhất 24-48 giờ sau khi ngừng amoxicillin-clavulanate. Theo dõi chức năng gan, thận, và dấu hiệu dị ứng. Theo dõi lâu hơn nếu có biến chứng (vàng da ứ mật, suy thận)."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống cùng thức ăn để giảm kích ứng dạ dày và tăng hấp thu. Có thể uống trước hoặc sau ăn, nhưng uống cùng thức ăn được khuyến cáo.",
                "timing": "Uống mỗi 8-12 giờ tùy theo liều. Liều chuẩn: 875/125mg mỗi 12 giờ hoặc 500/125mg mỗi 8 giờ. Liều cao: 2000/125mg mỗi 12 giờ.",
                "notes": "QUAN TRỌNG: 1) Uống cùng thức ăn để giảm kích ứng dạ dày, 2) Tiêu chảy phổ biến do clavulanate - có thể cần điều trị hỗ trợ, 3) Theo dõi chức năng gan (nguy cơ vàng da ứ mật), 4) Điều chỉnh liều ở suy thận, 5) Dùng khi cần ức chế beta-lactamase (H. influenzae, Moraxella, cắn động vật)."
            },
            "iv": None,
            "im": None
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Amoxicillin-clavulanate (Augmentin)",
                "IDSA Guidelines - Community-Acquired Pneumonia",
                "IDSA Guidelines - Acute Bacterial Sinusitis",
                "UpToDate - Amoxicillin-clavulanate: Drug Information",
                "Medscape - Amoxicillin-clavulanate Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Moderate", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Community-Acquired Pneumonia",
            "IDSA Guidelines - Acute Bacterial Sinusitis",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Ampicillin": {
        "group": "Antibiotic - Penicillin (Aminopenicillin)",
        "vietnamese_name": "Ampicillin",
        "administration": ["IV", "IM", "PO"],
        "indications": [
            "Nhiễm Enterococcus faecalis (kết hợp gentamicin trong viêm nội tâm mạc)",
            "Listeria monocytogenes (viêm màng não, nhiễm khuẩn huyết)",
            "Nhiễm khuẩn đường tiết niệu, đường mật",
            "Nhiễm Streptococcus, Enterococcus nhạy cảm",
        ],
        "contraindications": [
            "Dị ứng penicillin/beta-lactam",
            "Tiền sử phản vệ với penicillin",
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 4-6 giờ",
            "adult_po": "500mg PO mỗi 6 giờ",
            "adult_listeria_meningitis": "2g IV mỗi 4 giờ",
            "pediatric": "100-200mg/kg/ngày IV chia 4-6 lần (tối đa 12g/ngày)",
            "notes": "Ưu tiên đường IV cho nhiễm nặng/Listeria. Thường phối hợp gentamicin trong viêm nội tâm mạc do Enterococcus.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Mỗi 8 giờ",
            "under_30": "Mỗi 12 giờ",
            "hemodialysis": "Liều sau mỗi lần lọc",
        },
        "side_effects": [
            "Phát ban (đặc biệt ở bệnh nhân EBV)",
            "Tiêu chảy",
            "Buồn nôn",
            "Tăng men gan nhẹ",
        ],
        "interactions": [
            "Probenecid: tăng nồng độ ampicillin (giảm bài tiết thận)",
            "Allopurinol: tăng nguy cơ phát ban",
            "Warfarin: có thể tăng INR",
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Aminopenicillin, ức chế tổng hợp thành tế bào. Phổ: Streptococcus, Enterococcus, Listeria, H. influenzae không sinh beta-lactamase, một số Gram âm đường ruột; bị phá bởi beta-lactamase.",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban, phản vệ)",
            "Chức năng thận khi cần chỉnh liều",
            "Dấu hiệu nhiễm C. difficile nếu tiêu chảy kéo dài",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
        ],
        "precautions": [
            "Phản ứng chéo với cephalosporin ~5-10%",
            "Điều chỉnh liều ở suy thận",
            "Phát ban giả dị ứng khi nhiễm EBV",
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ",
            "clearance": "Thận (chủ yếu)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng. Dung dịch pha IV: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày.",
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng penicillin/beta-lactam",
                "Tiền sử phản vệ với penicillin",
            ],
            "tương_đối": []
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng."},
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Infective Endocarditis (Enterococcus)",
            "IDSA Guidelines - Listeria monocytogenes Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Ampicillin-sulbactam": {
        "group": "Antibiotic - Penicillin/Beta-lactamase Inhibitor",
        "vietnamese_name": "Ampicillin-sulbactam, Unasyn",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn ổ bụng nhẹ-trung bình",
            "Nhiễm khuẩn do vi khuẩn sinh beta-lactamase (H. influenzae, Moraxella, MSSA)",
            "Nhiễm khuẩn do cắn động vật/người",
        ],
        "contraindications": [
            "Dị ứng penicillin/beta-lactam",
            "Tiền sử phản vệ với penicillin",
        ],
        "dosage": {
            "adult_standard": "1.5-3g IV mỗi 6 giờ (ampicillin:sulbactam = 2:1)",
            "adult_severe": "3g IV mỗi 6 giờ",
            "pediatric": "150-300mg/kg/ngày (tính tổng) IV chia 4 lần (tối đa 12g tổng/ngày)",
            "notes": "Phổ tương tự amoxicillin-clavulanate dạng IV. Dùng trong nhiễm da-mô mềm, ổ bụng, cắn động vật.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Mỗi 8 giờ",
            "under_30": "Mỗi 12 giờ",
            "hemodialysis": "Liều sau mỗi lần lọc",
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn",
            "Phát ban",
            "Tăng men gan nhẹ",
        ],
        "interactions": [
            "Probenecid: tăng nồng độ ampicillin",
            "Warfarin: có thể tăng INR",
            "Aminoglycosides: không pha chung (bất hoạt)",
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ampicillin ức chế thành tế bào; sulbactam ức chế beta-lactamase, mở rộng phổ tới vi khuẩn sinh beta-lactamase (H. influenzae, Moraxella, MSSA, một số Enterobacteriaceae).",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban, phản vệ)",
            "Chức năng thận khi cần chỉnh liều",
            "Dấu hiệu nhiễm C. difficile nếu tiêu chảy kéo dài",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
        ],
        "precautions": [
            "Điều chỉnh liều ở suy thận",
            "Không pha chung aminoglycoside",
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ",
            "clearance": "Thận",
        },
        "storage": "Bảo quản ở nhiệt độ phòng. Dung dịch pha IV: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng penicillin/beta-lactam",
                "Tiền sử phản vệ với penicillin",
            ],
            "tương_đối": []
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng."},
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Low", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "IDSA Guidelines - Intra-abdominal Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Nafcillin": {
        "group": "Antibiotic - Penicillin (Anti-staphylococcal)",
        "vietnamese_name": "Nafcillin",
        "administration": ["IV"],
        "indications": [
            "Nhiễm MSSA (viêm nội tâm mạc, nhiễm khuẩn huyết, viêm xương)",
            "Nhiễm khuẩn da và mô mềm do MSSA",
        ],
        "contraindications": [
            "Dị ứng penicillin/beta-lactam",
        ],
        "dosage": {
            "adult_standard": "2g IV mỗi 4 giờ",
            "adult_endocarditis": "2g IV mỗi 4 giờ",
            "notes": "Chọn ưu tiên cho MSSA nặng (nhiễm khuẩn huyết, nội tâm mạc).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "any": "Không cần chỉnh liều đáng kể (thải qua gan/cholestatic)",
        },
        "side_effects": [
            "Viêm tĩnh mạch tại chỗ tiêm",
            "Tăng men gan/ứ mật",
            "Giảm bạch cầu (hiếm)",
            "Phát ban",
        ],
        "interactions": [
            "Probenecid: tăng nồng độ nafcillin",
            "Warfarin: có thể tăng INR",
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Penicillin kháng penicillinase, bền với beta-lactamase của MSSA. Phổ: MSSA, Streptococcus; không hiệu quả với MRSA, Enterococcus, Gram âm.",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban, phản vệ)",
            "Chức năng gan (men gan, bilirubin) - đặc biệt quan trọng do nguy cơ ứ mật",
            "Dấu hiệu viêm tĩnh mạch tại chỗ tiêm",
            "Công thức máu (giảm bạch cầu)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
        ],
        "precautions": [
            "Theo dõi chức năng gan (có thể gây ứ mật)",
            "Theo dõi viêm tĩnh mạch, nên dùng đường truyền trung tâm nếu kéo dài",
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "clearance": "Chủ yếu gan (mật), không cần chỉnh thận",
        },
        "storage": "Bảo quản ở nhiệt độ phòng. Dung dịch pha IV: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": None,
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Moderate", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Infective Endocarditis (MSSA)",
            "IDSA Guidelines - Staphylococcus aureus Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Oxacillin": {
        "group": "Antibiotic - Penicillin (Anti-staphylococcal)",
        "vietnamese_name": "Oxacillin",
        "administration": ["IV"],
        "indications": [
            "Nhiễm MSSA (nội tâm mạc, nhiễm khuẩn huyết, viêm xương)",
            "Nhiễm khuẩn da và mô mềm do MSSA",
        ],
        "contraindications": [
            "Dị ứng penicillin/beta-lactam",
        ],
        "dosage": {
            "adult_standard": "2g IV mỗi 4 giờ",
            "notes": "Thay thế nafcillin cho MSSA. Dùng liều tương tự nafcillin.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "any": "Không cần chỉnh đáng kể (thải qua gan/cholestatic)",
        },
        "side_effects": [
            "Viêm tĩnh mạch tại chỗ tiêm",
            "Tăng men gan/ứ mật",
            "Giảm bạch cầu (hiếm)",
            "Phát ban",
        ],
        "interactions": [
            "Probenecid: tăng nồng độ oxacillin",
            "Warfarin: có thể tăng INR",
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Penicillin kháng penicillinase, bền với beta-lactamase của MSSA. Phổ: MSSA, Streptococcus; không hiệu quả với MRSA, Enterococcus, Gram âm.",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban, phản vệ)",
            "Chức năng gan (men gan, bilirubin) - đặc biệt quan trọng do nguy cơ ứ mật",
            "Dấu hiệu viêm tĩnh mạch tại chỗ tiêm",
            "Công thức máu (giảm bạch cầu)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
        ],
        "precautions": [
            "Theo dõi chức năng gan (ứ mật)",
            "Theo dõi viêm tĩnh mạch",
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "clearance": "Chủ yếu gan (mật)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng. Dung dịch pha IV: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": None,
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"hepatic": "Moderate", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Infective Endocarditis (MSSA)",
            "IDSA Guidelines - Staphylococcus aureus Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
}

__all__ = ["PENICILLIN_ANTIBIOTICS"]

