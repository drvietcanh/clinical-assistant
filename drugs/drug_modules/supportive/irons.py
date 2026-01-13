"""Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data"""

# Irons

IRONS_DRUGS = {
    "Iron": {
        "group": "Vitamins/Supplements - Iron",
        "vietnamese_name": "Iron, Ferrous sulfate, Ferrous fumarate, Ferrous gluconate",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Thiếu máu thiếu sắt",
            "Dự phòng thiếu sắt",
            "Có thai (dự phòng)",
            "Chảy máu mạn tính",
            "Sau phẫu thuật",
        ],
        "contraindications": [
            "Thừa sắt (hemochromatosis)",
            "Thiếu máu không do thiếu sắt",
            "Viêm loét dạ dày tá tràng nặng",
            "Viêm ruột",
        ],
        "dosage": {
            "adult_po_ferrous_sulfate": "325mg (65mg sắt nguyên tố) x 1-3 lần/ngày",
            "adult_po_ferrous_fumarate": "200mg (66mg sắt nguyên tố) x 2-3 lần/ngày",
            "adult_po_ferrous_gluconate": "300mg (35mg sắt nguyên tố) x 3 lần/ngày",
            "adult_pregnancy": "30-60mg sắt nguyên tố/ngày",
            "adult_iv": "100-200mg IV mỗi ngày hoặc theo phác đồ",
            "notes": "Uống khi bụng đói (1 giờ trước bữa ăn) để tăng hấp thu. Uống với vitamin C",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng (tăng nguy cơ tích tụ sắt)",
        },
        "side_effects": [
            "Táo bón",
            "Phân đen (không nguy hiểm)",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Kích ứng dạ dày",
            "Phản ứng dị ứng (IV)",
            "Quá tải sắt (dùng lâu dài, liều cao)",
        ],
        "interactions": [
            "Antacid/PPI/H2 blocker: giảm hấp thu sắt",
            "Tetracycline/Quinolone: giảm hấp thu cả hai",
            "Thyroxine: giảm hấp thu thyroxine",
            "Chloramphenicol: giảm đáp ứng với sắt",
            "Vitamin C: tăng hấp thu sắt",
        ],
        "pregnancy": "A - An toàn, cần thiết",
        "mechanism_of_action": "Sắt (iron) là nguyên tố vi lượng cần thiết cho tổng hợp hemoglobin, myoglobin, và các enzyme chứa sắt. Sắt được hấp thu ở tá tràng và phần trên ruột non, chuyển hóa thành ferritin (dự trữ) và transferrin (vận chuyển). Sắt tham gia vào chuỗi hô hấp tế bào, tổng hợp DNA, và nhiều phản ứng enzyme. Thiếu sắt gây thiếu máu thiếu sắt (iron deficiency anemia), đặc trưng bởi hồng cầu nhỏ, nhược sắc (microcytic, hypochromic). Sắt có nhiều dạng: ferrous sulfate (65mg sắt nguyên tố/325mg), ferrous fumarate (66mg sắt nguyên tố/200mg), ferrous gluconate (35mg sắt nguyên tố/300mg). Hấp thu sắt tăng khi bụng đói và khi dùng với vitamin C.",
        "monitoring": [
            "Hemoglobin (Hb) - mục tiêu: tăng 1-2g/dL mỗi tháng",
            "Ferritin - dự trữ sắt (mục tiêu: >50 ng/mL)",
            "TIBC (total iron binding capacity), transferrin saturation",
            "MCV (mean corpuscular volume) - tăng khi điều trị thành công",
            "Đáp ứng điều trị (giảm mệt mỏi, tăng năng lượng)",
            "Dấu hiệu quá tải sắt (nếu dùng lâu dài, liều cao)",
        ],
        "precautions": [
            "Uống khi bụng đói (1 giờ trước bữa ăn) để tăng hấp thu (có thể gây kích ứng dạ dày)",
            "Nếu kích ứng dạ dày: uống với thức ăn (giảm hấp thu 50%)",
            "Uống với vitamin C (tăng hấp thu sắt)",
            "Tránh uống với antacid, PPI, H2 blocker (giảm hấp thu)",
            "Cách xa tetracycline, quinolone ít nhất 2 giờ (giảm hấp thu cả hai)",
            "Phân đen là bình thường (không phải chảy máu)",
            "Táo bón là tác dụng phụ phổ biến (uống nhiều nước, ăn nhiều chất xơ)",
            "Thận trọng ở bệnh nhân hemochromatosis (thừa sắt)",
            "IV cho thiếu máu nặng hoặc không dung nạp PO (có thể gây phản ứng dị ứng nặng)",
            "Tiếp tục điều trị 3-6 tháng sau khi hemoglobin bình thường (để bổ sung dự trữ)",
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (sắt được dự trữ trong cơ thể)",
            "onset": "Vài ngày đến vài tuần (tác dụng tích tụ)",
            "duration": "Phụ thuộc vào dự trữ trong cơ thể",
            "protein_binding": "Gắn với transferrin (vận chuyển) và ferritin (dự trữ)",
            "clearance": "Dự trữ trong gan, lách, tủy xương; thải trừ qua phân, mồ hôi, nước tiểu (ít)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Quá tải sắt có thể gây tổn thương gan, tim, và các cơ quan khác. Tránh dùng ở bệnh nhân hemochromatosis",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Tetracycline, Doxycycline, Minocycline",
                    "mechanism": "Sắt gắn với tetracycline trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu cả hai.",
                    "effect": "Giảm hấp thu cả sắt và tetracycline, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 2-3 giờ giữa sắt và tetracycline. Uống sắt trước, tetracycline sau.",
                },
                {
                    "drug": "Quinolone (Ciprofloxacin, Levofloxacin, Moxifloxacin)",
                    "mechanism": "Sắt gắn với quinolone trong ruột, tạo phức hợp không hấp thu được, giảm hấp thu cả hai.",
                    "effect": "Giảm hấp thu cả sắt và quinolone, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 2-3 giờ giữa sắt và quinolone. Uống sắt trước, quinolone sau.",
                },
            ],
            "moderate": [
                {
                    "drug": "Levothyroxine",
                    "mechanism": "Sắt gắn với levothyroxine trong ruột, giảm hấp thu levothyroxine.",
                    "effect": "Giảm hấp thu levothyroxine, giảm hiệu quả điều trị suy giáp",
                    "management": "Cách ít nhất 4 giờ giữa sắt và levothyroxine. Uống levothyroxine sáng đói, sắt sau bữa ăn.",
                },
                {
                    "drug": "Antacid, PPI (Omeprazole, Pantoprazole), H2 blockers (Ranitidine)",
                    "mechanism": "Giảm acid dạ dày, giảm hấp thu sắt (sắt cần acid để hấp thu tốt).",
                    "effect": "Giảm hấp thu sắt, giảm hiệu quả điều trị thiếu máu",
                    "management": "Cách ít nhất 2 giờ giữa sắt và antacid/PPI/H2 blocker. Uống sắt khi bụng đói (nếu dung nạp), antacid sau bữa ăn.",
                },
            ],
            "minor": [
                {
                    "drug": "Vitamin C",
                    "mechanism": "Vitamin C tăng hấp thu sắt bằng cách khử Fe3+ thành Fe2+ (dạng hấp thu tốt hơn).",
                    "effect": "Tăng hấp thu sắt (tác dụng mong muốn)",
                    "management": "Kết hợp sắt và vitamin C là phổ biến và có lợi. Uống cùng lúc hoặc gần nhau.",
                },
                {
                    "drug": "Chloramphenicol",
                    "mechanism": "Chloramphenicol có thể giảm đáp ứng với sắt trong điều trị thiếu máu.",
                    "effect": "Giảm đáp ứng với sắt",
                    "management": "Thận trọng. Theo dõi đáp ứng điều trị thiếu máu.",
                },
            ],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Hemochromatosis (thừa sắt di truyền) - sắt làm nặng thêm",
                "Thiếu máu không do thiếu sắt - không hiệu quả và có thể gây quá tải sắt",
                "Dị ứng sắt",
            ],
            "tương_đối": [
                "Viêm loét dạ dày tá tràng nặng - sắt có thể gây kích ứng",
                "Viêm ruột (Crohn, viêm loét đại tràng) - sắt có thể gây kích ứng",
                "Suy thận nặng - tăng nguy cơ tích tụ sắt",
                "Đang truyền máu thường xuyên - tăng nguy cơ quá tải sắt",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Sắt an toàn và cần thiết trong thai kỳ. Thiếu sắt trong thai kỳ có thể gây thiếu máu ở mẹ, sinh non, nhẹ cân, và các biến chứng khác. Nhu cầu sắt tăng trong thai kỳ. Khuyến cáo: 30-60 mg sắt nguyên tố/ngày trong thai kỳ. Phụ nữ thiếu máu thiếu sắt cần liều cao hơn. Theo dõi hemoglobin và ferritin trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Sắt bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ sắt trong sữa mẹ tương đối ổn định và không phụ thuộc nhiều vào nồng độ sắt của mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Khuyến cáo: 15-30 mg sắt nguyên tố/ngày khi cho con bú. Phụ nữ thiếu máu thiếu sắt cần liều cao hơn.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Sắt được dự trữ trong gan, nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Thận trọng, theo dõi ferritin. Sắt được dự trữ trong gan, suy gan trung bình có thể ảnh hưởng đến dự trữ.",
            "severe": "Thận trọng, theo dõi ferritin chặt chẽ. Suy gan nặng có thể ảnh hưởng đến dự trữ sắt và tăng nguy cơ quá tải sắt.",
            "notes": "Sắt được dự trữ trong gan dưới dạng ferritin. Suy gan có thể ảnh hưởng đến dự trữ sắt. Theo dõi ferritin để tránh quá tải sắt.",
        },
        "overdose_management": {
            "symptoms": [
                "Quá liều cấp tính (thường ở trẻ em):",
                "  - Buồn nôn, nôn (có thể có máu)",
                "  - Đau bụng, tiêu chảy (có thể có máu)",
                "  - Mệt mỏi, yếu cơ",
                "  - Sốc, hạ huyết áp",
                "  - Tổn thương gan (tăng ALT/AST, vàng da)",
                "  - Tổn thương thận (suy thận cấp)",
                "  - Rối loạn đông máu",
                "  - Hôn mê, tử vong (với liều rất cao)",
                "Quá tải sắt mạn tính (hemosiderosis, hemochromatosis):",
                "  - Tổn thương gan (xơ gan, suy gan)",
                "  - Tổn thương tim (suy tim, loạn nhịp)",
                "  - Tổn thương tụy (đái tháo đường)",
                "  - Tổn thương khớp (viêm khớp)",
                "  - Tăng sắc tố da (da xám, đồng)",
            ],
            "antidote": "Deferoxamine (Desferal) - chelate sắt, tăng bài tiết qua nước tiểu. Deferasirox (Exjade) - chelate sắt đường uống.",
            "treatment": [
                "Quá liều cấp tính:",
                "  - Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "  - Than hoạt tính KHÔNG hiệu quả với sắt (không dùng)",
                "  - Deferoxamine IV: 15 mg/kg/giờ (tối đa 6g/24h) nếu nồng độ sắt >350 mcg/dL hoặc có triệu chứng nặng",
                "  - Deferoxamine IM: 1g mỗi 4-6 giờ (nếu không thể IV)",
                "  - Theo dõi nồng độ sắt trong máu, ferritin",
                "  - Điều trị hỗ trợ: truyền dịch, điều chỉnh điện giải, hỗ trợ gan/thận",
                "  - Theo dõi dấu hiệu sinh tồn, chức năng gan/thận",
                "Quá tải sắt mạn tính:",
                "  - Ngừng bổ sung sắt",
                "  - Deferoxamine hoặc deferasirox để giảm dự trữ sắt",
                "  - Phlebotomy (lấy máu) nếu hemochromatosis",
                "  - Điều trị tổn thương cơ quan (gan, tim, tụy)",
            ],
            "monitoring": "Nồng độ sắt trong máu, ferritin, TIBC, transferrin saturation, chức năng gan (ALT/AST, bilirubin), chức năng thận (creatinine, eGFR), dấu hiệu sinh tồn, ECG (nếu quá tải sắt nặng).",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Deferoxamine (Desferal)",
                    "mechanism": "Chelate sắt, tạo phức hợp sắt-deferoxamine, tăng bài tiết qua nước tiểu.",
                    "indication": "Quá liều sắt cấp tính hoặc quá tải sắt mạn tính",
                    "dose": "IV: 15 mg/kg/giờ (tối đa 6g/24h). IM: 1g mỗi 4-6 giờ.",
                    "notes": "Deferoxamine là antidote chính cho quá liều sắt. Bắt đầu sớm nếu có triệu chứng nặng hoặc nồng độ sắt cao.",
                },
                {
                    "name": "Deferasirox (Exjade)",
                    "mechanism": "Chelate sắt đường uống, tăng bài tiết qua phân.",
                    "indication": "Quá tải sắt mạn tính",
                    "dose": "Theo chỉ định, thường 20-30 mg/kg/ngày",
                    "notes": "Dùng cho quá tải sắt mạn tính, không dùng cho quá liều cấp tính.",
                },
            ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống khi bụng đói (1 giờ trước bữa ăn) để tăng hấp thu. Nếu kích ứng dạ dày, có thể uống với thức ăn (giảm hấp thu 50%). Uống với vitamin C (nước cam, viên vitamin C) để tăng hấp thu.",
                "timing": "Uống 1-3 lần/ngày tùy liều. Uống khi bụng đói (1 giờ trước bữa ăn) để tăng hấp thu. Cách xa các thuốc khác ít nhất 2-4 giờ: tetracycline, quinolone (2-3 giờ), levothyroxine (4 giờ), antacid/PPI/H2 blocker (2 giờ).",
            },
            "iv": {
                "reconstitution": "Pha với nước muối đẳng trương (0.9% NaCl). Không pha với các dung dịch khác.",
                "infusion_rate": "Truyền chậm trong ít nhất 1 giờ. Không truyền nhanh (tăng nguy cơ phản ứng dị ứng).",
                "compatibility": ["Normal saline (0.9% NaCl)"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "IV cho thiếu máu nặng hoặc không dung nạp PO. Có thể gây phản ứng dị ứng nặng (sốc phản vệ). Theo dõi chặt chẽ trong 30 phút đầu. Test dose trước khi truyền đầy đủ.",
            },
            "im": {
                "reconstitution": "Sắt IM thường có sẵn dạng tiêm sẵn. Không cần pha.",
                "injection_site": "Tiêm bắp sâu (gluteal). Xoay vị trí tiêm.",
                "injection_rate": "Tiêm chậm, đều",
                "notes": "IM ít dùng hơn IV. Tiêm bắp sâu, xoay vị trí tiêm. Có thể gây đau và đổi màu da tại chỗ tiêm.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Iron (Ferrous sulfate, Ferrous fumarate, Ferrous gluconate)",
                "American Society of Hematology Guidelines - Iron Deficiency Anemia",
                "WHO Guidelines - Iron Supplementation in Pregnancy",
                "UpToDate - Iron deficiency anemia treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
            ],
            "evidence_level": "A - Dựa trên FDA drug labels, ASH/WHO guidelines, và dữ liệu lâm sàng",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [
                "Iron overload (with long-term, high-dose use)",
                "GI irritation (constipation, nausea, abdominal pain)",
            ],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Hemoglobin (target: increase 1-2 g/dL per month)",
                "Ferritin (target: >50 ng/mL)",
                "TIBC, transferrin saturation",
                "MCV (increases with successful treatment)",
                "Clinical response",
                "Signs of iron overload (if used long-term, high-dose)",
            ],
        },
        "guideline_tags": [
            "ASH Guidelines - Iron Deficiency Anemia",
            "WHO Guidelines - Iron Supplementation in Pregnancy",
            "ACOG Guidelines - Iron Supplementation in Pregnancy",
            "FDA Drug Information - Iron",
        ],
    }
}

__all__ = ["IRONS_DRUGS"]
