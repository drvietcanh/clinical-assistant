"""Gastrointestinal Drugs - JAK Inhibitors
Active module - contains JAK inhibitors for IBD and autoimmune conditions"""

# JAK Inhibitors for IBD and Autoimmune Conditions

JAK_INHIBITORS_DRUGS = {
    "Upadacitinib": {
        "group": "Gastrointestinal - JAK Inhibitor",
        "vietnamese_name": "Upadacitinib, Rinvoq",
        "administration": ["PO"],
        "indications": [
            "Viêm loét đại tràng (UC) - moderate to severe",
            "Bệnh Crohn (Crohn's disease) - moderate to severe",
            "Viêm khớp dạng thấp (RA) - moderate to severe",
            "Viêm khớp vảy nến (PsA)",
            "Viêm cột sống dính khớp (AS)",
            "Viêm da cơ địa (atopic dermatitis) - moderate to severe"
        ],
        "contraindications": [
            "Dị ứng upadacitinib hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng đang hoạt động",
            "Suy giảm miễn dịch nặng",
            "Bệnh gan nặng"
        ],
        "dosage": {
            "adult_uc": "45mg PO mỗi ngày x 8 tuần (induction), sau đó 15mg PO mỗi ngày (maintenance)",
            "adult_crohn": "45mg PO mỗi ngày x 12 tuần (induction), sau đó 15mg hoặc 30mg PO mỗi ngày (maintenance)",
            "adult_ra": "15mg PO mỗi ngày",
            "adult_psa_as": "15mg PO mỗi ngày",
            "adult_dermatitis": "15mg hoặc 30mg PO mỗi ngày",
            "notes": "Uống với hoặc không có thức ăn. Điều chỉnh liều theo chỉ định và đáp ứng."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Nhiễm trùng (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu, herpes zoster) - phổ biến",
            "Tăng cholesterol (LDL, HDL, triglycerides) - phổ biến",
            "Tăng creatine kinase (CK) - phổ biến",
            "Giảm bạch cầu trung tính (neutropenia)",
            "Giảm bạch cầu lympho (lymphopenia)",
            "Giảm hemoglobin (anemia)",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Nhức đầu",
            "Buồn nôn",
            "Tăng nguy cơ huyết khối (thrombosis) - đặc biệt ở bệnh nhân có yếu tố nguy cơ",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da không phải melanoma)",
            "Tăng nguy cơ nhiễm trùng nặng (bao gồm lao, nhiễm trùng cơ hội)"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Thuốc chống đông/kháng tiểu cầu: tăng nguy cơ huyết khối",
            "Vaccine sống: chống chỉ định trong và sau điều trị",
            "Strong CYP3A4 inhibitors: tăng nồng độ upadacitinib"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Upadacitinib là chất ức chế Janus kinase (JAK inhibitor) chọn lọc, ức chế chủ yếu JAK1. "
            "JAK (Janus kinase) là một nhóm enzyme tyrosine kinase quan trọng trong quá trình truyền tín hiệu cytokine. "
            "Các cytokine (như IL-6, IL-12, IL-23, IFN-γ) gắn với thụ thể trên tế bào → kích hoạt JAK → "
            "phosphoryl hóa STAT (signal transducer and activator of transcription) → STAT di chuyển vào nhân → "
            "kích hoạt biểu hiện gen → tăng viêm và đáp ứng miễn dịch. "
            "Trong IBD (UC, Crohn), RA, và các bệnh tự miễn khác, có sự kích hoạt quá mức của JAK-STAT pathway, "
            "dẫn đến viêm mạn tính. "
            "Upadacitinib ức chế JAK1 (và một phần JAK2) → ức chế JAK-STAT pathway → "
            "giảm sản xuất các cytokine gây viêm → giảm viêm và triệu chứng bệnh. "
            "Dẫn đến: cải thiện triệu chứng, giảm viêm, và làm chậm tiến triển bệnh trong UC, Crohn, RA, và các bệnh tự miễn khác. "
            "Upadacitinib có tính chọn lọc cao với JAK1 (so với JAK2, JAK3), giảm một số tác dụng phụ so với các JAK inhibitor không chọn lọc."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng bạch cầu lympho - theo dõi lymphopenia",
            "Hemoglobin - theo dõi anemia",
            "Cholesterol (LDL, HDL, triglycerides) - theo dõi tăng cholesterol",
            "Creatine kinase (CK) - theo dõi tăng CK",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Dấu hiệu huyết khối (đau ngực, khó thở, đau chân, sưng chân)",
            "Dấu hiệu ung thư (hạch to, sụt cân, v.v.)",
            "Tuberculosis (TB) screening trước khi bắt đầu điều trị"
        ],
        "precautions": [
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do ức chế miễn dịch",
            "Cần hoàn thành tất cả vaccine trước khi bắt đầu điều trị (ít nhất 4-6 tuần trước)",
            "CHỐNG CHỈ ĐỊNH vaccine sống trong và sau điều trị (ít nhất 4-6 tuần sau liều cuối)",
            "NGUY CƠ HUYẾT KHỐI - đặc biệt ở bệnh nhân có yếu tố nguy cơ (tuổi >50, hút thuốc, béo phì, tiền sử huyết khối)",
            "NGUY CƠ UNG THƯ - tăng nguy cơ lymphoma và ung thư da không phải melanoma",
            "NGUY CƠ LAO - cần screening TB trước khi bắt đầu điều trị",
            "Ngừng upadacitinib nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân có tiền sử nhiễm trùng tái phát",
            "Theo dõi chức năng gan định kỳ - tăng men gan có thể nghiêm trọng"
        ],
        "pharmacokinetics": {
            "half_life": "~8-14 giờ (trung bình)",
            "onset": "Vài tuần (tác dụng chậm)",
            "duration": "Dài (do half-life trung bình)",
            "protein_binding": "~50%",
            "metabolism": "Gan (chuyển hóa qua CYP3A4 chủ yếu, một phần CYP2D6)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Cần điều chỉnh liều ở suy gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": (
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội và lao. "
            "Cần screening TB trước khi bắt đầu điều trị. "
            "Ngừng upadacitinib nếu có nhiễm trùng nặng. "
            "NGUY CƠ HUYẾT KHỐI - đặc biệt ở bệnh nhân có yếu tố nguy cơ. "
            "Có báo cáo huyết khối tĩnh mạch sâu (DVT) và thuyên tắc phổi (PE). "
            "NGUY CƠ UNG THƯ - tăng nguy cơ lymphoma và ung thư da không phải melanoma. "
            "NGUY CƠ TỬ VONG - tăng nguy cơ tử vong ở bệnh nhân RA ≥50 tuổi có ≥1 yếu tố nguy cơ tim mạch."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc ức chế miễn dịch khác (corticosteroid liều cao, methotrexate, azathioprine, TNF inhibitors)",
                    "mechanism": "Tăng ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng nặng, bao gồm lao và nhiễm trùng cơ hội",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu phải dùng, theo dõi chặt chẽ dấu hiệu nhiễm trùng."
                },
                {
                    "drug": "Vaccine sống (MMR, varicella, zoster, yellow fever, BCG)",
                    "mechanism": "Upadacitinib làm giảm đáp ứng miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "CHỐNG CHỈ ĐỊNH dùng vaccine sống trong và sau điều trị. Hoãn vaccine sống ít nhất 4-6 tuần sau liều cuối."
                }
            ],
            "moderate": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa upadacitinib",
                    "effect": "Tăng nồng độ upadacitinib, tăng tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều upadacitinib."
                },
                {
                    "drug": "Thuốc chống đông/kháng tiểu cầu (warfarin, aspirin, clopidogrel)",
                    "mechanism": "Tăng nguy cơ huyết khối",
                    "effect": "Tăng nguy cơ huyết khối",
                    "management": "Thận trọng. Theo dõi dấu hiệu huyết khối."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng upadacitinib hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng đang hoạt động",
                "Suy giảm miễn dịch nặng"
            ],
            "tương_đối": [
                "Tiền sử nhiễm trùng tái phát",
                "Tiền sử lao hoặc tiếp xúc với lao - cần screening và điều trị dự phòng nếu cần",
                "Tiền sử huyết khối - tăng nguy cơ huyết khối",
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng - giảm thải trừ, tăng nguy cơ tích lũy",
                "Tuổi >50 với yếu tố nguy cơ tim mạch - tăng nguy cơ tử vong"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH (bệnh gan nặng)",
            "notes": "Upadacitinib chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ nhiễm trùng",
                "Giảm bạch cầu trung tính/lympho nặng",
                "Tăng men gan nặng",
                "Tăng nguy cơ huyết khối"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi số lượng bạch cầu và hemoglobin",
                "Theo dõi chức năng gan",
                "Xử trí huyết khối nếu có (anticoagulation nếu cần)"
            ],
            "monitoring": "Dấu hiệu nhiễm trùng, số lượng bạch cầu, chức năng gan, dấu hiệu huyết khối"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn",
                "timing": "Uống 1 lần/ngày. Điều chỉnh liều theo chỉ định (UC: 45mg induction → 15mg maintenance; Crohn: 45mg induction → 15-30mg maintenance; RA: 15mg).",
                "notes": "Uống với hoặc không có thức ăn. Điều chỉnh liều theo chỉ định và đáp ứng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Upadacitinib (Rinvoq)",
                "UpToDate - Upadacitinib: Drug information",
                "Lexicomp - Upadacitinib monograph",
                "ACG Guidelines - IBD"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in UC, Crohn, RA"
        }
    },

    "Tofacitinib": {
        "group": "Gastrointestinal - JAK Inhibitor",
        "vietnamese_name": "Tofacitinib, Xeljanz",
        "administration": ["PO"],
        "indications": [
            "Viêm loét đại tràng (UC) - moderate to severe",
            "Viêm khớp dạng thấp (RA) - moderate to severe",
            "Viêm khớp vảy nến (PsA)",
            "Viêm cột sống dính khớp (AS)"
        ],
        "contraindications": [
            "Dị ứng tofacitinib hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng đang hoạt động",
            "Suy giảm miễn dịch nặng",
            "Bệnh gan nặng"
        ],
        "dosage": {
            "adult_uc": "10mg PO x 2 lần/ngày x 8 tuần (induction), sau đó 5mg PO x 2 lần/ngày (maintenance)",
            "adult_ra": "5mg PO x 2 lần/ngày (có thể tăng đến 10mg x 2 lần/ngày nếu cần)",
            "adult_psa_as": "5mg PO x 2 lần/ngày",
            "notes": "Uống với hoặc không có thức ăn. Điều chỉnh liều theo chỉ định và đáp ứng."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 50% hoặc tránh dùng"
        },
        "side_effects": [
            "Nhiễm trùng (nhiễm trùng đường hô hấp trên, nhiễm trùng đường tiết niệu, herpes zoster) - phổ biến",
            "Tăng cholesterol (LDL, HDL, triglycerides) - phổ biến",
            "Tăng creatine kinase (CK) - phổ biến",
            "Giảm bạch cầu trung tính (neutropenia)",
            "Giảm bạch cầu lympho (lymphopenia)",
            "Giảm hemoglobin (anemia)",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Nhức đầu",
            "Buồn nôn",
            "Tiêu chảy",
            "Tăng nguy cơ huyết khối (thrombosis) - đặc biệt ở bệnh nhân có yếu tố nguy cơ",
            "Tăng nguy cơ ung thư (lymphoma, ung thư da không phải melanoma)",
            "Tăng nguy cơ nhiễm trùng nặng (bao gồm lao, nhiễm trùng cơ hội)"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Thuốc chống đông/kháng tiểu cầu: tăng nguy cơ huyết khối",
            "Vaccine sống: chống chỉ định trong và sau điều trị",
            "Strong CYP3A4 inhibitors: tăng nồng độ tofacitinib",
            "Strong CYP3A4 inducers: giảm nồng độ tofacitinib"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Tofacitinib là chất ức chế Janus kinase (JAK inhibitor) không chọn lọc, ức chế JAK1, JAK2, và JAK3. "
            "JAK (Janus kinase) là một nhóm enzyme tyrosine kinase quan trọng trong quá trình truyền tín hiệu cytokine. "
            "Các cytokine (như IL-6, IL-12, IL-23, IFN-γ) gắn với thụ thể trên tế bào → kích hoạt JAK → "
            "phosphoryl hóa STAT (signal transducer and activator of transcription) → STAT di chuyển vào nhân → "
            "kích hoạt biểu hiện gen → tăng viêm và đáp ứng miễn dịch. "
            "Trong UC, RA, và các bệnh tự miễn khác, có sự kích hoạt quá mức của JAK-STAT pathway, "
            "dẫn đến viêm mạn tính. "
            "Tofacitinib ức chế JAK1, JAK2, và JAK3 → ức chế JAK-STAT pathway → "
            "giảm sản xuất các cytokine gây viêm → giảm viêm và triệu chứng bệnh. "
            "Dẫn đến: cải thiện triệu chứng, giảm viêm, và làm chậm tiến triển bệnh trong UC, RA, và các bệnh tự miễn khác. "
            "Tofacitinib là JAK inhibitor đầu tiên được FDA phê duyệt cho UC và RA, "
            "nhưng có nhiều tác dụng phụ hơn upadacitinib do không chọn lọc (ức chế cả JAK2, có thể gây giảm bạch cầu và thiếu máu)."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng bạch cầu lympho - theo dõi lymphopenia",
            "Hemoglobin - theo dõi anemia",
            "Cholesterol (LDL, HDL, triglycerides) - theo dõi tăng cholesterol",
            "Creatine kinase (CK) - theo dõi tăng CK",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều ở suy thận",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Dấu hiệu huyết khối (đau ngực, khó thở, đau chân, sưng chân)",
            "Dấu hiệu ung thư (hạch to, sụt cân, v.v.)",
            "Tuberculosis (TB) screening trước khi bắt đầu điều trị"
        ],
        "precautions": [
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do ức chế miễn dịch",
            "Cần hoàn thành tất cả vaccine trước khi bắt đầu điều trị (ít nhất 4-6 tuần trước)",
            "CHỐNG CHỈ ĐỊNH vaccine sống trong và sau điều trị (ít nhất 4-6 tuần sau liều cuối)",
            "NGUY CƠ HUYẾT KHỐI - đặc biệt ở bệnh nhân có yếu tố nguy cơ (tuổi >50, hút thuốc, béo phì, tiền sử huyết khối)",
            "NGUY CƠ UNG THƯ - tăng nguy cơ lymphoma và ung thư da không phải melanoma",
            "NGUY CƠ LAO - cần screening TB trước khi bắt đầu điều trị",
            "Ngừng tofacitinib nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân có tiền sử nhiễm trùng tái phát",
            "Theo dõi chức năng gan định kỳ - tăng men gan có thể nghiêm trọng",
            "Điều chỉnh liều ở suy thận - giảm liều 50% ở CrCl 30-60, tránh dùng ở CrCl <30"
        ],
        "pharmacokinetics": {
            "half_life": "~3 giờ (ngắn, cần dùng 2 lần/ngày)",
            "onset": "Vài tuần (tác dụng chậm)",
            "duration": "Trung bình (do half-life ngắn)",
            "protein_binding": "~40%",
            "metabolism": "Gan (chuyển hóa qua CYP3A4 chủ yếu, một phần CYP2C19)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ một phần). Cần điều chỉnh liều ở suy gan và suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": (
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội và lao. "
            "Cần screening TB trước khi bắt đầu điều trị. "
            "Ngừng tofacitinib nếu có nhiễm trùng nặng. "
            "NGUY CƠ HUYẾT KHỐI - đặc biệt ở bệnh nhân có yếu tố nguy cơ. "
            "Có báo cáo huyết khối tĩnh mạch sâu (DVT) và thuyên tắc phổi (PE). "
            "NGUY CƠ UNG THƯ - tăng nguy cơ lymphoma và ung thư da không phải melanoma. "
            "NGUY CƠ TỬ VONG - tăng nguy cơ tử vong ở bệnh nhân RA ≥50 tuổi có ≥1 yếu tố nguy cơ tim mạch."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc ức chế miễn dịch khác (corticosteroid liều cao, methotrexate, azathioprine, TNF inhibitors)",
                    "mechanism": "Tăng ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng nặng, bao gồm lao và nhiễm trùng cơ hội",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu phải dùng, theo dõi chặt chẽ dấu hiệu nhiễm trùng."
                },
                {
                    "drug": "Vaccine sống (MMR, varicella, zoster, yellow fever, BCG)",
                    "mechanism": "Tofacitinib làm giảm đáp ứng miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "CHỐNG CHỈ ĐỊNH dùng vaccine sống trong và sau điều trị. Hoãn vaccine sống ít nhất 4-6 tuần sau liều cuối."
                }
            ],
            "moderate": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa tofacitinib",
                    "effect": "Tăng nồng độ tofacitinib, tăng tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều tofacitinib 50%."
                },
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa tofacitinib",
                    "effect": "Giảm nồng độ tofacitinib, giảm hiệu quả",
                    "management": "Thận trọng. Có thể cần tăng liều tofacitinib."
                },
                {
                    "drug": "Thuốc chống đông/kháng tiểu cầu (warfarin, aspirin, clopidogrel)",
                    "mechanism": "Tăng nguy cơ huyết khối",
                    "effect": "Tăng nguy cơ huyết khối",
                    "management": "Thận trọng. Theo dõi dấu hiệu huyết khối."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng tofacitinib hoặc bất kỳ thành phần nào",
                "Nhiễm trùng nặng đang hoạt động",
                "Suy giảm miễn dịch nặng"
            ],
            "tương_đối": [
                "Tiền sử nhiễm trùng tái phát",
                "Tiền sử lao hoặc tiếp xúc với lao - cần screening và điều trị dự phòng nếu cần",
                "Tiền sử huyết khối - tăng nguy cơ huyết khối",
                "Bệnh gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Bệnh thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy, tránh dùng",
                "Tuổi >50 với yếu tố nguy cơ tim mạch - tăng nguy cơ tử vong"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Thận trọng khi dùng khi cho con bú.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH (bệnh gan nặng)",
            "notes": "Tofacitinib chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ nhiễm trùng",
                "Giảm bạch cầu trung tính/lympho nặng",
                "Tăng men gan nặng",
                "Tăng nguy cơ huyết khối"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi số lượng bạch cầu và hemoglobin",
                "Theo dõi chức năng gan",
                "Xử trí huyết khối nếu có (anticoagulation nếu cần)"
            ],
            "monitoring": "Dấu hiệu nhiễm trùng, số lượng bạch cầu, chức năng gan, dấu hiệu huyết khối"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn",
                "timing": "Uống 2 lần/ngày (sáng, tối). Điều chỉnh liều theo chỉ định (UC: 10mg x 2 lần/ngày induction → 5mg x 2 lần/ngày maintenance; RA: 5mg x 2 lần/ngày).",
                "notes": "Uống với hoặc không có thức ăn. Điều chỉnh liều theo chỉ định và đáp ứng. Điều chỉnh liều ở suy thận (giảm 50% ở CrCl 30-60)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tofacitinib (Xeljanz)",
                "UpToDate - Tofacitinib: Drug information",
                "Lexicomp - Tofacitinib monograph",
                "ACG Guidelines - IBD"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in UC and RA"
        }
    },

    "Baricitinib": {
        "group": "Rheumatology/Gastrointestinal - JAK Inhibitor (JAK1/JAK2)",
        "vietnamese_name": "Baricitinib, Olumiant",
        "administration": ["PO"],
        "indications": [
            "Viêm khớp dạng thấp (RA) – moderate đến severe sau thất bại DMARD khác",
            "Viêm da cơ địa (atopic dermatitis) – moderate đến severe",
            "Alopecia areata (rụng tóc từng mảng, patchy/bắc cầu)",
        ],
        "contraindications": [
            "Dị ứng với baricitinib hoặc bất kỳ thành phần nào",
            "Nhiễm trùng nặng đang hoạt động (lao, nhiễm nấm xâm lấn, nhiễm trùng cơ hội)",
            "Suy giảm miễn dịch nặng",
            "Suy thận nặng (eGFR <15 ml/phút/1.73m²) hoặc đang lọc máu",
        ],
        "dosage": {
            "adult_ra": "2mg PO 1 lần/ngày; có thể 4mg/ngày ở một số bệnh nhân nguy cơ thấp (tùy guideline và cảnh báo an toàn)",
            "adult_atopic_dermatitis": "2–4mg PO 1 lần/ngày (tùy mức độ bệnh và yếu tố nguy cơ)",
            "adult_alopecia": "2–4mg PO 1 lần/ngày (tùy phác đồ từng nước)",
            "notes": "Uống cùng hoặc không cùng thức ăn; không nên dùng đồng thời nhiều JAK inhibitor hoặc biologic DMARD khác trừ khi chuyên khoa chỉ định.",
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Giảm còn 1mg/ngày hoặc 50% liều (tùy chỉ định cụ thể)",
            "under_30": "Không khuyến cáo/Tránh dùng (trừ khi có phác đồ chuyên khoa rõ ràng)",
        },
        "side_effects": [
            "Nhiễm trùng (đường hô hấp trên, herpes zoster) – tương tự các JAK khác",
            "Tăng lipid máu (LDL, HDL)",
            "Tăng men gan (ALT, AST)",
            "Giảm bạch cầu lympho, giảm hemoglobin",
            "Huyết khối tĩnh mạch (DVT, PE) – hiếm nhưng nghiêm trọng",
            "Nguy cơ ung thư (lymphoma, ung thư da không melanoma – hiếm)",
        ],
        "interactions": [
            "Các thuốc ức chế miễn dịch mạnh khác (biologic DMARD, azathioprine, cyclosporine): tăng nguy cơ nhiễm trùng",
            "Vaccine sống: chống chỉ định trong khi dùng và một thời gian sau khi ngừng",
            "Strong OAT3 inhibitors (probenecid): tăng nồng độ baricitinib",
        ],
        "pregnancy": "C – nhìn chung tránh dùng; cân nhắc thay thế an toàn hơn",
        "mechanism_of_action": (
            "Baricitinib là chất ức chế chọn lọc Janus kinase 1 và 2 (JAK1/JAK2). "
            "Bằng cách ức chế JAK1/JAK2, thuốc làm giảm truyền tín hiệu của nhiều cytokine tiền viêm (như IL-6, IFN, GM-CSF), "
            "giảm hoạt hóa tế bào miễn dịch và quá trình viêm trong RA, viêm da cơ địa và alopecia areata."
        ),
        "monitoring": [
            "CBC (bạch cầu, hemoglobin, tiểu cầu) trước và định kỳ",
            "Lipid máu (cholesterol, triglycerides) sau 3 tháng và định kỳ",
            "Men gan (ALT, AST)",
            "Creatinin, eGFR để điều chỉnh liều",
            "Sàng lọc lao (TB test) trước khi bắt đầu; sàng lọc HBV/HCV khi có yếu tố nguy cơ",
            "Dấu hiệu nhiễm trùng, huyết khối, ung thư",
        ],
        "precautions": [
            "NGUY CƠ NHIỄM TRÙNG: tăng nguy cơ nhiễm trùng nặng và cơ hội, bao gồm lao; cần sàng lọc và điều trị dự phòng khi cần.",
            "NGUY CƠ HUYẾT KHỐI: thận trọng ở bệnh nhân có tiền sử DVT/PE hoặc nhiều yếu tố nguy cơ tim mạch.",
            "Không phối hợp với JAK inhibitor khác hoặc biologic DMARD trừ khi có chỉ định rất rõ.",
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 12 giờ",
            "onset": "Vài tuần cho cải thiện triệu chứng RA/viêm da cơ địa",
            "duration": "Cho phép dùng 1 lần/ngày",
            "protein_binding": "~50%",
            "metabolism": "Ít chuyển hóa qua CYP; chủ yếu thải trừ qua thận dưới dạng không đổi",
            "clearance": "Thận (OAT3-mediated); suy thận làm tăng nồng độ thuốc.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng, tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": (
            "Tương tự các JAK inhibitor khác: tăng nguy cơ nhiễm trùng nặng, huyết khối, ung thư và biến cố tim mạch lớn "
            "ở một số nhóm nguy cơ cao; cần cân nhắc so với anti-TNF và các lựa chọn khác."
        ),
        "drug_interactions_detail": {
            "major": [
                {
                    "drug": "Vaccine sống (MMR, varicella, zoster sống, yellow fever, BCG)",
                    "mechanism": "Ức chế miễn dịch làm tăng nguy cơ nhiễm trùng do vaccine sống",
                    "effect": "Nhiễm trùng từ vaccine, có thể nặng",
                    "management": "CHỐNG CHỈ ĐỊNH. Hoàn tất vaccine sống ≥4 tuần trước khi bắt đầu baricitinib.",
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid và các OAT3 inhibitors mạnh",
                    "mechanism": "Giảm thải trừ baricitinib qua thận",
                    "effect": "Tăng nồng độ và nguy cơ tác dụng phụ",
                    "management": "Cân nhắc giảm liều baricitinib.",
                }
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng baricitinib",
                "Nhiễm trùng nặng đang hoạt động",
                "eGFR <15 ml/phút/1.73m² hoặc đang lọc máu",
            ],
            "tương_đối": [
                "Tiền sử DVT/PE hoặc nhiều yếu tố nguy cơ huyết khối",
                "Nhiễm trùng mạn tính hoặc tiền sử nhiễm trùng tái phát",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu người hạn chế; nhìn chung tránh dùng trong thai kỳ, đặc biệt tam cá nguyệt đầu.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết qua sữa; thận trọng.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc dùng thuốc thay thế an toàn hơn.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, theo dõi men gan",
            "severe": "Dữ liệu hạn chế; tránh dùng nếu có thể",
            "notes": "Không chuyển hóa mạnh qua gan nhưng bệnh gan nặng vẫn có thể tăng nguy cơ biến cố.",
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ nhiễm trùng, rối loạn huyết học và huyết khối (tương tự JAK khác) nếu dùng liều cao kéo dài",
            ],
            "antidote": "Không có antidote đặc hiệu.",
            "treatment": [
                "Ngừng thuốc, theo dõi dấu hiệu nhiễm trùng và huyết khối",
                "Điều trị hỗ trợ và điều trị biến chứng nếu xuất hiện",
            ],
            "monitoring": "CBC, lipid, men gan, creatinin/eGFR, dấu hiệu nhiễm trùng và huyết khối.",
        },
        "reversal_agents": {"available": False, "agents": []},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không với thức ăn.",
                "timing": "Uống 1 lần/ngày, cùng thời điểm mỗi ngày.",
            }
        },
        "references": {
            "primary_sources": [
                "ACR Guidelines – Rheumatoid arthritis and JAK inhibitors",
                "FDA Drug Label – Baricitinib (Olumiant)",
                "UpToDate – Baricitinib: Drug information",
            ],
            "last_updated": "2025-02-23",
            "evidence_level": "A – RA; B – viêm da cơ địa, alopecia (tùy quốc gia/phê duyệt)",
        },
    },
}

__all__ = ["JAK_INHIBITORS_DRUGS"]


