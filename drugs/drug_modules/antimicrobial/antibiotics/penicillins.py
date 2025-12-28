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
        "pregnancy": "B",
        "mechanism_of_action": "Aminopenicillin, ức chế tổng hợp thành tế bào. Phổ: Streptococcus, Enterococcus, Listeria, H. influenzae không sinh beta-lactamase, một số Gram âm đường ruột; bị phá bởi beta-lactamase.",
        "precautions": [
            "Phản ứng chéo với cephalosporin ~5-10%",
            "Điều chỉnh liều ở suy thận",
            "Phát ban giả dị ứng khi nhiễm EBV",
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ",
            "clearance": "Thận (chủ yếu)",
        },
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
        "pregnancy": "B",
        "mechanism_of_action": "Amoxicillin ức chế thành tế bào; clavulanate ức chế beta-lactamase, mở rộng phổ tới vi khuẩn sinh beta-lactamase (H. influenzae, Moraxella, một số Enterobacteriaceae, MSSA).",
        "precautions": [
            "Tiêu chảy do clavulanate - dùng liều clavulanate thấp hơn (875/125 hoặc 2000/125)",
            "Uống với thức ăn",
            "Điều chỉnh liều ở suy thận",
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ",
            "clearance": "Thận (cả hai thành phần)",
        },
        "black_box_warnings": None,
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng penicillin/beta-lactam",
                "Tiền sử vàng da ứ mật do amoxicillin-clavulanate",
            ],
            "tương_đối": []
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng."},
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
        "pregnancy": "B",
        "mechanism_of_action": "Ampicillin ức chế thành tế bào; sulbactam ức chế beta-lactamase, mở rộng phổ tới vi khuẩn sinh beta-lactamase (H. influenzae, Moraxella, MSSA, một số Enterobacteriaceae).",
        "precautions": [
            "Điều chỉnh liều ở suy thận",
            "Không pha chung aminoglycoside",
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ",
            "clearance": "Thận",
        },
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
        "pregnancy": "B",
        "mechanism_of_action": "Penicillin kháng penicillinase, bền với beta-lactamase của MSSA. Phổ: MSSA, Streptococcus; không hiệu quả với MRSA, Enterococcus, Gram âm.",
        "precautions": [
            "Theo dõi chức năng gan (có thể gây ứ mật)",
            "Theo dõi viêm tĩnh mạch, nên dùng đường truyền trung tâm nếu kéo dài",
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "clearance": "Chủ yếu gan (mật), không cần chỉnh thận",
        },
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
        "pregnancy": "B",
        "mechanism_of_action": "Penicillin kháng penicillinase, bền với beta-lactamase của MSSA. Phổ: MSSA, Streptococcus; không hiệu quả với MRSA, Enterococcus, Gram âm.",
        "precautions": [
            "Theo dõi chức năng gan (ứ mật)",
            "Theo dõi viêm tĩnh mạch",
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ",
            "clearance": "Chủ yếu gan (mật)",
        },
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

