"""Respiratory Medications - PDE-4 Inhibitors
PDE-4 inhibitors for COPD treatment"""

# PDE-4 Inhibitors

PDE4_INHIBITORS_DRUGS = {
    "Roflumilast": {
        "group": "Respiratory - PDE-4 Inhibitor (Anti-inflammatory)",
        "vietnamese_name": "Roflumilast, Daxas, Daliresp",
        "administration": ["PO"],
        "indications": [
            "COPD (chronic obstructive pulmonary disease) - nặng, có tiền sử đợt cấp",
            "COPD với viêm mạn tính nặng"
        ],
        "contraindications": [
            "Dị ứng roflumilast hoặc bất kỳ thành phần nào",
            "Suy gan nặng (Child-Pugh C) - CHỐNG CHỈ ĐỊNH",
            "Có thai - CHỐNG CHỈ ĐỊNH",
            "Đang cho con bú - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_standard": "500mcg PO x 1 lần/ngày",
            "notes": "Uống với hoặc không thức ăn. Roflumilast là PDE-4 inhibitor, ức chế viêm trong COPD. CHỈ dùng cho COPD nặng có tiền sử đợt cấp. KHÔNG dùng để điều trị cấp cứu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Tiêu chảy - phổ biến",
            "Buồn nôn - phổ biến",
            "Đau đầu - phổ biến",
            "Mất ngủ - phổ biến",
            "Giảm cân - phổ biến",
            "Đau bụng - phổ biến",
            "Trầm cảm - phổ biến",
            "Lo âu - phổ biến",
            "Tự tử, ý tưởng tự tử - hiếm nhưng NGUY HIỂM",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Giảm bạch cầu - hiếm"
        ],
        "interactions": [
            "CYP3A4 inhibitors mạnh (ketoconazole, itraconazole, ritonavir): tăng nồng độ roflumilast",
            "CYP3A4 inducers mạnh (rifampin, carbamazepine, phenytoin): giảm nồng độ roflumilast",
            "Cimetidine: tăng nồng độ roflumilast"
        ],
        "pregnancy": "X - Chống chỉ định",
        "mechanism_of_action": "Roflumilast là phosphodiesterase-4 (PDE-4) inhibitor. PDE-4 là enzyme phân hủy cAMP trong tế bào viêm (neutrophils, macrophages, T cells). PDE-4 phân hủy cAMP → giảm cAMP → tăng hoạt động viêm → tăng sản xuất các cytokine viêm (TNF-α, IL-8) → gây viêm đường hô hấp và COPD. Roflumilast ức chế PDE-4 → tăng cAMP trong tế bào viêm → ức chế hoạt động viêm → giảm sản xuất cytokine viêm → giảm viêm đường hô hấp. Dẫn đến: giảm đợt cấp COPD và cải thiện chức năng hô hấp. Roflumilast được dùng để điều trị COPD nặng có tiền sử đợt cấp. ĐẶC ĐIỂM: (1) PDE-4 inhibitor, ức chế viêm, (2) CHỈ dùng cho COPD nặng có tiền sử đợt cấp, (3) KHÔNG dùng để điều trị cấp cứu, (4) Tác dụng phụ: tiêu chảy, buồn nôn, trầm cảm, tự tử, (5) CHỐNG CHỈ ĐỊNH ở suy gan nặng, (6) Tương tác với CYP3A4 inhibitors/inducers.",
        "monitoring": [
            "Dấu hiệu trầm cảm, lo âu, ý tưởng tự tử - QUAN TRỌNG (hiếm nhưng NGUY HIỂM), theo dõi thường xuyên",
            "Cân nặng - giảm cân phổ biến, theo dõi mỗi tháng",
            "Chức năng gan (ALT, AST) - tăng men gan phổ biến, theo dõi trước điều trị và mỗi 3 tháng",
            "Công thức máu (CBC) - giảm bạch cầu hiếm, theo dõi định kỳ",
            "Chức năng hô hấp (FEV1) - đánh giá hiệu quả điều trị",
            "Tần suất đợt cấp COPD - giảm đợt cấp",
            "Triệu chứng lâm sàng (khó thở, ho, đờm)"
        ],
        "precautions": [
            "TỰ TỬ, Ý TƯỞNG TỰ TỬ - hiếm nhưng NGUY HIỂM - theo dõi dấu hiệu trầm cảm, lo âu, ý tưởng tự tử thường xuyên, ngừng ngay nếu có",
            "TRẦM CẢM, LO ÂU - phổ biến - theo dõi thường xuyên",
            "CHỈ DÙNG CHO COPD NẶNG CÓ TIỀN SỬ ĐỢT CẤP - không dùng cho COPD nhẹ hoặc không có tiền sử đợt cấp",
            "KHÔNG DÙNG ĐỂ ĐIỀU TRỊ CẤP CỨU - không có tác dụng giãn phế quản nhanh",
            "Giảm cân - phổ biến, theo dõi cân nặng",
            "Tăng men gan - phổ biến, theo dõi chức năng gan",
            "CHỐNG CHỈ ĐỊNH ở suy gan nặng (Child-Pugh C)",
            "Tương tác với CYP3A4 inhibitors/inducers (ảnh hưởng nồng độ roflumilast)",
            "Ngừng ngay nếu có dấu hiệu trầm cảm, lo âu, ý tưởng tự tử"
        ],
        "pharmacokinetics": {
            "half_life": "17 giờ (roflumilast), 30 giờ (roflumilast N-oxide - chất chuyển hóa hoạt động)",
            "onset": "Vài tuần đến vài tháng (tác dụng lâm sàng)",
            "duration": "Dài (dùng hàng ngày)",
            "protein_binding": "99%",
            "metabolism": "Gan (CYP3A4, CYP1A2 → roflumilast N-oxide - chất chuyển hóa hoạt động)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "TỰ TỬ, Ý TƯỞNG TỰ TỬ - hiếm nhưng NGUY HIỂM. Theo dõi dấu hiệu trầm cảm, lo âu, ý tưởng tự tử thường xuyên. Ngừng ngay roflumilast nếu có dấu hiệu trầm cảm, lo âu, ý tưởng tự tử. CHỐNG CHỈ ĐỊNH ở suy gan nặng (Child-Pugh C).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ roflumilast",
                    "effect": "Tăng nồng độ roflumilast, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều roflumilast. Theo dõi tác dụng phụ, đặc biệt trầm cảm và tự tử."
                },
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế CYP450, tăng nồng độ roflumilast",
                    "effect": "Tăng nồng độ roflumilast, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều roflumilast. Cân nhắc dùng ranitidine hoặc famotidine thay thế."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 Inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ roflumilast",
                    "effect": "Giảm nồng độ roflumilast, giảm hiệu quả điều trị",
                    "management": "Thận trọng. Có thể cần tăng liều roflumilast. Theo dõi đáp ứng điều trị."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng roflumilast hoặc bất kỳ thành phần nào",
                "Suy gan nặng (Child-Pugh C) - CHỐNG CHỈ ĐỊNH",
                "Có thai - CHỐNG CHỈ ĐỊNH (category X)",
                "Đang cho con bú - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Tiền sử trầm cảm, lo âu, tự tử - tăng nguy cơ",
                "Suy gan trung bình (Child-Pugh B) - tăng nguy cơ tăng men gan",
                "Giảm cân nền - tăng nguy cơ giảm cân thêm"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Roflumilast phân loại X - chống chỉ định tuyệt đối trong thai kỳ. Roflumilast gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ. Phụ nữ trong độ tuổi sinh đẻ PHẢI dùng biện pháp tránh thai hiệu quả trong và sau điều trị.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Roflumilast bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng roflumilast. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH - roflumilast chuyển hóa qua gan, suy gan nặng tăng độc tính nghiêm trọng",
            "notes": "Roflumilast chuyển hóa qua gan (CYP3A4, CYP1A2). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính nghiêm trọng. CHỐNG CHỈ ĐỊNH ở suy gan nặng (Child-Pugh C)."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng",
                "Buồn nôn, nôn nặng",
                "Trầm cảm nặng",
                "Ý tưởng tự tử",
                "Tăng men gan nặng",
                "Giảm bạch cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay roflumilast",
                "Rửa dạ dày nếu mới uống <1 giờ",
                "Than hoạt tính",
                "Nếu trầm cảm, ý tưởng tự tử: đánh giá tâm thần ngay, điều trị trầm cảm, theo dõi chặt chẽ",
                "Điều trị tiêu chảy: loperamide, bù dịch nếu cần",
                "Điều trị buồn nôn, nôn: ondansetron, metoclopramide",
                "Theo dõi chức năng gan, CBC",
                "Supportive care: bù dịch, điều trị nhiễm trùng"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu trầm cảm, ý tưởng tự tử, chức năng gan, CBC, cân nặng trong ít nhất 24-48 giờ"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có dấu hiệu trầm cảm hoặc ý tưởng tự tử."
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống với thức ăn để giảm kích ứng dạ dày.",
                "timing": "500mcg PO x 1 lần/ngày. Uống đều đặn cùng một thời điểm mỗi ngày.",
                "notes": "QUAN TRỌNG: 1) CHỈ dùng cho COPD nặng có tiền sử đợt cấp, 2) KHÔNG dùng để điều trị cấp cứu, 3) Tự tử, ý tưởng tự tử - hiếm nhưng NGUY HIỂM, 4) Trầm cảm, lo âu - phổ biến, 5) CHỐNG CHỈ ĐỊNH ở suy gan nặng, 6) Theo dõi dấu hiệu trầm cảm, lo âu, ý tưởng tự tử thường xuyên."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Roflumilast (Daliresp)",
                "UpToDate - Roflumilast: Drug Information",
                "GOLD Guidelines - COPD",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, effective for severe COPD with exacerbation history, extensive clinical data"
        }
    }
}

__all__ = ['PDE4_INHIBITORS_DRUGS']

