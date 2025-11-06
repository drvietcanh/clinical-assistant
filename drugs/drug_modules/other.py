"""
Other Common Medications
Active module - contains all other common drug data
"""

OTHER_DRUGS = {
"Allopurinol": {
        "group": "Metabolism - Xanthine Oxidase Inhibitor",
        "vietnamese_name": "Allopurinol, Zyloric",
        "administration": ["PO"],
        "indications": [
            "Gout",
            "Tăng acid uric máu",
            "Phòng ngừa sỏi thận uric acid",
            "Hóa trị (phòng ngừa tăng acid uric)"
        ],
        "contraindications": [
            "Dị ứng",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "adult_standard": "100-300mg x 1 lần/ngày",
            "adult_severe": "400-600mg/ngày chia 2-3 lần",
            "notes": "Khởi đầu với liều thấp (100mg), tăng dần. Dùng kèm colchicine khi bắt đầu để tránh cơn gout cấp"
        },
        "side_effects": [
            "Ban da (nặng có thể SJS/TEN - nguy hiểm)",
            "Buồn nôn",
            "Đau đầu",
            "Tăng men gan"
        ],
                  "interactions": [
              "Azathioprine/6-mercaptopurine: tăng độc tính (giảm liều azathioprine 75%)",
              "Ampicillin/Amoxicillin: tăng nguy cơ ban da",
              "Warfarin: tăng tác dụng chống đông"
          ],
          "pregnancy": "C",
          "mechanism_of_action": "Xanthine oxidase inhibitor. Ức chế enzyme xanthine oxidase, enzyme chuyển hypoxanthine thành xanthine và xanthine thành acid uric. Giảm sản xuất acid uric, giảm nồng độ acid uric trong máu và nước tiểu. Được dùng để điều trị gout mạn tính và phòng ngừa tăng acid uric máu (ví dụ trong hóa trị).",
          "monitoring": [
              "Nồng độ acid uric máu (mục tiêu <6 mg/dL)",
              "Chức năng thận: creatinine, BUN (thải qua thận)",
              "Chức năng gan: ALT, AST (có thể gây tăng men gan)",
              "Dấu hiệu ban da (QUAN TRỌNG - có thể tiến triển thành SJS/TEN nếu nặng)",
              "Triệu chứng gout cấp (có thể xảy ra khi bắt đầu điều trị - cần dùng colchicine dự phòng)"
          ],
          "precautions": [
              "KHỞI ĐẦU với liều thấp (100mg/ngày), tăng dần mỗi 1-2 tuần để tránh cơn gout cấp",
              "Dùng kèm colchicine hoặc NSAID khi bắt đầu để dự phòng cơn gout cấp (1-2 tháng đầu)",
              "NGỪNG NGAY nếu có ban da - có thể tiến triển thành SJS/TEN (đe dọa tính mạng)",
              "Tránh dùng với ampicillin/amoxicillin (tăng nguy cơ ban da nặng)",
              "Thận trọng khi dùng với azathioprine/6-mercaptopurine (tăng độc tính - cần giảm liều 75%)",
              "Thận trọng khi dùng với warfarin (tăng tác dụng chống đông - theo dõi INR)",
              "Thận trọng ở bệnh nhân suy thận (giảm liều)",
              "Uống với nhiều nước để tránh sỏi thận"
          ],
          "pharmacokinetics": {
              "half_life": "1-2 giờ (allopurinol), 15-18 giờ (metabolite oxypurinol - hoạt chất)",
              "onset": "1-2 tuần (giảm acid uric máu)",
              "duration": "24 giờ (uống 1 lần/ngày)",
              "protein_binding": "Rất ít",
              "clearance": "Thận (chủ yếu, allopurinol và oxypurinol thải qua nước tiểu). Cần giảm liều ở suy thận"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "Có thể gây phản ứng da nghiêm trọng (ban da, SJS, TEN) đe dọa tính mạng. Ngừng ngay nếu có ban da. Nguy cơ tăng ở bệnh nhân suy thận, dùng đồng thời với ampicillin/amoxicillin, hoặc có tiền sử dị ứng allopurinol"
      },
      "Prednisolone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Prednisolone",
        "administration": ["PO"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản",
            "Bệnh tự miễn",
            "Suy thượng thận",
            "Dị ứng nặng"
        ],
        "contraindications": [
            "Nhiễm khuẩn hệ thống không điều trị",
            "Loét dạ dày tá tràng đang hoạt động",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "5-60mg/ngày tùy chỉ định",
            "adult_high": "1-2mg/kg/ngày cho bệnh nặng",
            "notes": "Giảm dần liều khi ngừng, không ngừng đột ngột. Uống buổi sáng với thức ăn"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Ức chế miễn dịch",
            "Tăng cân",
            "Loét dạ dày",
            "Rối loạn tâm thần",
            "Ức chế trục HPA (khi ngừng)"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày",
            "Insulin/OAD: tăng đường huyết",
            "Vaccines: giảm hiệu quả vaccine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Glucocorticoid tổng hợp, tác dụng trung bình. Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm, ức chế phospholipase A2 → giảm prostaglandin và leukotriene. Có tác dụng mineralocorticoid nhẹ (ít hơn hydrocortisone). Ức chế miễn dịch. Được dùng trong nhiều tình trạng viêm và tự miễn. Tác dụng tương tự prednisone nhưng prednisolone là dạng hoạt động (không cần chuyển hóa ở gan).",
        "monitoring": [
            "Đường huyết (tăng đường huyết, đặc biệt ở bệnh nhân đái tháo đường)",
            "Huyết áp (tăng huyết áp)",
            "Điện giải (natri, kali)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Dạ dày (dấu hiệu loét, xuất huyết)",
            "Tâm thần (rối loạn tâm thần, mất ngủ, kích động)",
            "Xương (loãng xương nếu dùng kéo dài)",
            "Mắt (tăng nhãn áp, đục thủy tinh thể)",
            "Chức năng thượng thận (ức chế trục HPA nếu dùng kéo dài)"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột nếu dùng > 1 tuần (có thể gây suy thượng thận cấp - nguy hiểm tính mạng)",
            "Phải giảm liều dần dần (tapering) nếu dùng > 1 tuần",
            "Ức chế miễn dịch - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm nấm, lao",
            "Không dùng trong nhiễm nấm hệ thống không điều trị",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Thận trọng ở bệnh nhân loét dạ dày (tăng nguy cơ)",
            "Thận trọng ở bệnh nhân tăng huyết áp",
            "Dùng với thức ăn để giảm kích ứng dạ dày",
            "Dự phòng loãng xương nếu dùng kéo dài (bổ sung calcium, vitamin D)",
            "Theo dõi dấu hiệu nhiễm trùng (ức chế miễn dịch có thể che dấu triệu chứng)",
            "Liều thay thế: 5-7.5mg/ngày, liều chống viêm: 20-60mg/ngày"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (ngắn, nhưng tác dụng kéo dài hơn do tác động gen)",
            "onset": "1-2 giờ (PO)",
            "duration": "18-36 giờ",
            "protein_binding": "90-95%",
            "metabolism": "Gan (CYP3A4) - prednisolone là dạng hoạt động (khác prednisone)",
            "clearance": "Gan, không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ngừng đột ngột sau khi dùng kéo dài có thể gây suy thượng thận cấp, có thể tử vong. Ức chế miễn dịch mạnh có thể làm nặng nhiễm trùng hoặc gây nhiễm trùng cơ hội.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ketoconazole, Itraconazole (Azole antifungals)",
                    "mechanism": "Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa prednisolone, tăng nồng độ và tác dụng.",
                    "effect": "Tăng nồng độ prednisolone, tăng tác dụng và tác dụng phụ (Cushing, tăng đường huyết, ức chế miễn dịch)",
                    "management": "Giảm liều prednisolone 25-50% khi dùng với azole antifungals. Theo dõi đường huyết, dấu hiệu Cushing."
                },
                {
                    "drug": "Rifampin, Rifabutin",
                    "mechanism": "Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa prednisolone, giảm nồng độ và hiệu quả.",
                    "effect": "Giảm nồng độ prednisolone, giảm hiệu quả điều trị",
                    "management": "Tăng liều prednisolone 25-50% khi dùng với rifampin. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Corticosteroid có thể thay đổi chuyển hóa warfarin và ảnh hưởng đến đông máu.",
                    "effect": "Thay đổi INR (có thể tăng hoặc giảm), tăng nguy cơ chảy máu hoặc huyết khối",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng prednisolone. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAID (Ibuprofen, Naproxen, Diclofenac)",
                    "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.",
                    "effect": "Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa nghiêm trọng",
                    "management": "Cân nhắc dùng PPI hoặc misoprostol. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu chảy máu dạ dày."
                },
                {
                    "drug": "Phenytoin, Phenobarbital, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa, tăng chuyển hóa prednisolone.",
                    "effect": "Giảm nồng độ prednisolone, giảm hiệu quả",
                    "management": "Tăng liều prednisolone. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cả hai đều ức chế miễn dịch, tác dụng cộng dồn. Có thể ảnh hưởng đến chuyển hóa.",
                    "effect": "Tăng ức chế miễn dịch, tăng nguy cơ nhiễm trùng, tăng nguy cơ độc tính",
                    "management": "Giảm liều cả hai thuốc. Theo dõi chức năng thận, dấu hiệu nhiễm trùng."
                }
            ],
            "minor": [
                {
                    "drug": "Diuretics (Thiazide, Furosemide)",
                    "mechanism": "Corticosteroid gây giữ natri, có thể đối kháng tác dụng lợi tiểu.",
                    "effect": "Giảm hiệu quả lợi tiểu, có thể gây giữ nước",
                    "management": "Theo dõi cân nặng, dấu hiệu giữ nước. Có thể cần điều chỉnh liều lợi tiểu."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Nhiễm nấm hệ thống không điều trị (cryptococcosis, histoplasmosis, coccidioidomycosis) - corticosteroid làm nặng nhiễm nấm",
                "Dị ứng prednisolone hoặc các corticosteroid khác",
                "Nhiễm virus hoạt động (herpes simplex keratitis, varicella zoster lan tỏa) - trừ khi chỉ định đặc biệt"
            ],
            "relative": [
                "Nhiễm trùng đang hoạt động - có thể làm nặng, che dấu triệu chứng",
                "Đái tháo đường - tăng đường huyết, cần theo dõi và điều chỉnh",
                "Tăng huyết áp - có thể tăng huyết áp, giữ nước",
                "Suy tim - giữ nước, có thể làm nặng",
                "Loãng xương - tăng nguy cơ gãy xương",
                "Loét dạ dày tá tràng - tăng nguy cơ loét",
                "Rối loạn tâm thần - có thể làm nặng",
                "Glaucoma - có thể tăng nhãn áp",
                "Có thai - có thể ảnh hưởng đến thai nhi",
                "Suy gan - prednisolone là dạng hoạt động, không cần chuyển hóa nhưng thận trọng",
                "Suy thận - không cần điều chỉnh liều nhưng thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Prednisolone là thuốc phân loại C. Corticosteroid có thể đi qua nhau thai và có thể ảnh hưởng đến thai nhi. Dùng lâu dài hoặc liều cao trong thai kỳ có thể gây ức chế thượng thận ở trẻ sơ sinh, chậm phát triển, tăng nguy cơ sứt môi/vòm miệng (khi dùng trong tam cá nguyệt đầu), và các tác dụng phụ khác. Tuy nhiên, prednisolone được sử dụng trong thai kỳ để điều trị một số bệnh tự miễn và hen phế quản. Nên dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Tránh dùng liều cao kéo dài trong thai kỳ nếu có thể.",
            "lactation": {
                "safety": "Compatible (với dùng ngắn hạn)",
                "details": "Prednisolone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ với liều thường dùng. Với liều cao hoặc kéo dài, có thể ảnh hưởng đến trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với liều điều trị tiêu chuẩn. Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Prednisolone là dạng hoạt động, không cần chuyển hóa ở gan (khác với prednisone).",
            "moderate": "Không cần điều chỉnh liều. Prednisolone là dạng hoạt động, không phụ thuộc vào chức năng gan.",
            "severe": "Không cần điều chỉnh liều. Prednisolone là dạng hoạt động, không phụ thuộc vào chức năng gan. Tuy nhiên, thận trọng ở bệnh nhân suy gan nặng.",
            "notes": "Prednisolone là dạng hoạt động của prednisone, không cần chuyển hóa ở gan. Đây là ưu điểm so với prednisone ở bệnh nhân suy gan - có thể dùng prednisolone thay vì prednisone ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng Cushing: Tăng cân, mặt tròn, tích mỡ, bướu trâu, vết rạn da, tăng huyết áp",
                "Triệu chứng chuyển hóa: Tăng đường huyết nghiêm trọng, toan chuyển hóa, hạ kali máu",
                "Triệu chứng tiêu hóa: Loét dạ dày, xuất huyết tiêu hóa, thủng dạ dày",
                "Triệu chứng thần kinh: Kích động, loạn thần, trầm cảm, co giật, hôn mê",
                "Triệu chứng miễn dịch: Nhiễm trùng nghiêm trọng (do ức chế miễn dịch), che dấu triệu chứng nhiễm trùng",
                "Triệu chứng tim mạch: Suy tim, phù, giữ nước, tăng huyết áp nặng",
                "Triệu chứng nghiêm trọng: Suy thượng thận cấp (khi ngừng đột ngột sau dùng lâu dài), sốc, tử vong"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay prednisolone nếu có thể (nhưng KHÔNG ngừng đột ngột nếu đã dùng >2 tuần - phải giảm dần)",
                "Nếu ngừng đột ngột sau dùng lâu dài:",
                "  - Bắt đầu lại corticosteroid ngay (hydrocortisone 100mg IV mỗi 6-8 giờ)",
                "  - Giảm dần liều theo thời gian",
                "Điều trị tăng đường huyết:",
                "  - Theo dõi đường huyết thường xuyên",
                "  - Insulin nếu cần",
                "  - Điều chỉnh liều đái tháo đường",
                "Điều trị loét dạ dày/xuất huyết tiêu hóa:",
                "  - PPI (omeprazole, pantoprazole)",
                "  - Truyền máu nếu cần",
                "  - Nội soi dạ dày nếu nghi ngờ thủng",
                "Điều trị rối loạn tâm thần:",
                "  - An thần nếu kích động, loạn thần",
                "  - Antipsychotic nếu cần",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị nhiễm trùng:",
                "  - Kháng sinh nếu có nhiễm trùng",
                "  - Theo dõi dấu hiệu nhiễm trùng (có thể che dấu)",
                "Điều chỉnh điện giải:",
                "  - Bổ sung kali nếu hạ kali máu",
                "  - Điều chỉnh natri nếu cần",
                "Hỗ trợ huyết động:",
                "  - Truyền dịch nếu cần",
                "  - Thuốc vận mạch nếu sốc",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, đường huyết"
            ],
            "monitoring": "Theo dõi đường huyết, điện giải, dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu loét dạ dày, tâm thần trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng. Nếu ngừng đột ngột sau dùng lâu dài, theo dõi dấu hiệu suy thượng thận cấp trong ít nhất 1-2 tuần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.",
                "timing": "Uống 1-4 lần/ngày tùy chỉ định. Có thể uống buổi sáng (để giảm ảnh hưởng đến giấc ngủ) hoặc chia đều trong ngày. Với liều cao, chia nhiều lần. Với liều thấp, có thể uống 1 lần buổi sáng."
            },
            "iv": {
                "reconstitution": "Prednisolone chủ yếu dùng đường uống. Nếu cần IV, có thể dùng methylprednisolone thay thế.",
                "infusion_rate": "N/A - chủ yếu dùng đường uống",
                "compatibility": ["N/A"],
                "incompatibility": ["N/A"],
                "notes": "Prednisolone chủ yếu dùng đường uống. Nếu cần dùng IV, cân nhắc dùng methylprednisolone hoặc hydrocortisone thay thế."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Prednisolone",
                "UpToDate - Prednisolone: Drug Information",
                "Medscape - Prednisolone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Prednisolone Monograph",
                "Micromedex - Prednisolone Drug Information",
                "Endocrine Society Guidelines - Corticosteroid Use"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Folic Acid": {
        "group": "Hematology - Vitamin",
        "vietnamese_name": "Acid Folic",
        "administration": ["PO"],
        "indications": [
            "Thiếu máu do thiếu folate",
            "Dự phòng dị tật ống thần kinh trong thai kỳ",
            "Bệnh hồng cầu hình liềm",
            "Đang dùng methotrexate"
        ],
        "contraindications": [
            "Dị ứng"
        ],
        "dosage": {
            "adult_deficiency": "1-5mg x 1 lần/ngày",
            "pregnancy": "0.4-0.8mg x 1 lần/ngày",
            "methotrexate": "5-10mg/tuần (24h sau methotrexate)",
            "notes": "Dùng kèm vitamin B12 khi thiếu máu"
        },
        "side_effects": [
            "Hiếm khi có tác dụng phụ",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Methotrexate: giảm hiệu quả methotrexate (nhưng dùng để giảm độc tính)",
            "Phenytoin: giảm nồng độ phenytoin"
        ],
        "pregnancy": "A - Khuyến nghị dùng trong thai kỳ",
        "mechanism_of_action": "Folic acid (folate, vitamin B9) là coenzyme cần thiết cho tổng hợp DNA và RNA, đặc biệt quan trọng trong quá trình phân chia tế bào. Folic acid được chuyển đổi thành tetrahydrofolate (THF), tham gia vào các phản ứng methyl transfer, tổng hợp purine và pyrimidine (các nucleotide của DNA/RNA). Folic acid cần thiết cho sự phát triển bình thường của ống thần kinh trong thai kỳ (tuần 3-4), giúp ngăn ngừa dị tật ống thần kinh (spina bifida, anencephaly). Thiếu folic acid gây thiếu máu hồng cầu to do giảm tổng hợp DNA, dẫn đến tế bào hồng cầu chưa trưởng thành. Folic acid cũng được dùng để giảm độc tính của methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate).",
        "monitoring": [
            "Hemoglobin, MCV (mean corpuscular volume) - theo dõi đáp ứng điều trị thiếu máu",
            "Nồng độ folate trong máu (nếu cần)",
            "Nồng độ vitamin B12 (thiếu B12 có thể che dấu bởi folic acid)",
            "Đáp ứng điều trị (giảm triệu chứng thiếu máu)",
            "Dấu hiệu dị ứng (hiếm)"
        ],
        "precautions": [
            "Dùng kèm vitamin B12 khi thiếu máu (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)",
            "Với thiếu máu: luôn kiểm tra B12 trước khi dùng folic acid",
            "Dự phòng dị tật ống thần kinh: bắt đầu trước khi có thai 1 tháng, tiếp tục trong 3 tháng đầu",
            "Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)",
            "Liều cao (>1mg/ngày) có thể che dấu thiếu B12",
            "An toàn trong thai kỳ và cho con bú",
            "Hiếm khi có tác dụng phụ",
            "Thận trọng ở bệnh nhân ung thư (folic acid có thể kích thích tế bào ung thư)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (vitamin)",
            "onset": "Vài ngày đến vài tuần (tác dụng tích tụ)",
            "duration": "Phụ thuộc vào dự trữ trong cơ thể",
            "protein_binding": "Không đáng kể",
            "clearance": "Thận (thải trừ qua nước tiểu), một phần dự trữ trong gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None
    },
"Ticagrelor": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Ticagrelor, Brilinta",
        "administration": ["PO"],
        "indications": [
            "Hội chứng mạch vành cấp",
            "Sau đặt stent",
            "Sau nhồi máu cơ tim",
            "Phòng ngừa đột quỵ/TIA"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Xuất huyết nội sọ",
            "Suy gan nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_loading": "180mg x 1 lần",
            "adult_maintenance": "90mg x 2 lần/ngày",
            "notes": "Dùng kèm aspirin 75-100mg/ngày (dual antiplatelet therapy). Dùng với thức ăn để giảm dyspnea"
        },
        "side_effects": [
            "Chảy máu",
            "Khó thở (dyspnea) - phổ biến nhưng thường nhẹ",
            "Chóng mặt",
            "Nhức đầu"
        ],
        "interactions": [
            "Aspirin: dùng kèm (nhưng liều aspirin >100mg/ngày có thể giảm hiệu quả)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Strong CYP3A4 inhibitors: tăng nồng độ (tránh dùng)"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ticagrelor là chất ức chế P2Y12 receptor chọn lọc, đối kháng có thể đảo ngược (reversible) với P2Y12 receptor trên tiểu cầu. P2Y12 receptor là một thụ thể adenosine diphosphate (ADP) quan trọng trong quá trình hoạt hóa và kết tập tiểu cầu. Khác với clopidogrel và prasugrel (irreversible inhibitors), ticagrelor gắn trực tiếp với P2Y12 receptor mà không cần chuyển hóa thành metabolite hoạt động, và có thể đảo ngược (reversible). Ticagrelor ức chế kết tập tiểu cầu do ADP, giảm nguy cơ huyết khối trong hội chứng mạch vành cấp và sau can thiệp mạch vành. Ticagrelor cũng ức chế tái hấp thu adenosine (adenosine reuptake inhibitor), làm tăng nồng độ adenosine ngoại bào, có thể gây khó thở (dyspnea) và bradycardia. Tác dụng khởi phát nhanh hơn clopidogrel và hiệu quả hơn trong một số nghiên cứu.",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu tại vị trí tiêm)",
            "Chảy máu lớn (xuất huyết tiêu hóa, xuất huyết nội sọ, chảy máu sau phẫu thuật)",
            "Khó thở (dyspnea) - phổ biến (10-20%) nhưng thường nhẹ, có thể do ức chế tái hấp thu adenosine",
            "Nhịp tim chậm (bradycardia) - do tăng adenosine",
            "Chức năng gan nếu có triệu chứng (hiếm)",
            "Tương tác với strong CYP3A4 inhibitors (ketoconazole, clarithromycin) - tăng nồng độ"
        ],
        "precautions": [
            "Dùng kèm với aspirin 75-100mg/ngày (dual antiplatelet therapy - DAPT) - không dùng aspirin >100mg/ngày (có thể giảm hiệu quả)",
            "Không ngừng đột ngột (tăng nguy cơ huyết khối)",
            "Khó thở (dyspnea) - phổ biến nhưng thường nhẹ, có thể giảm khi dùng với thức ăn, thường tự khỏi",
            "Nguy cơ chảy máu cao - không dùng nếu có chảy máu đang hoạt động, xuất huyết nội sọ",
            "Tránh dùng với strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir) - tăng nồng độ",
            "Tránh dùng với strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin) - giảm nồng độ",
            "Dùng với thức ăn để giảm dyspnea và tăng hấp thu",
            "Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình",
            "Thận trọng ở bệnh nhân có tiền sử nhịp tim chậm hoặc block nhĩ thất",
            "Thời gian DAPT thường 12 tháng sau ACS hoặc đặt stent, có thể kéo dài ở một số bệnh nhân nguy cơ cao"
        ],
        "pharmacokinetics": {
            "half_life": "7-9 giờ (ticagrelor), 8-12 giờ (metabolite hoạt động)",
            "onset": "30 phút - 2 giờ (nhanh hơn clopidogrel)",
            "duration": "12 giờ (cần dùng 2 lần/ngày do reversible binding)",
            "protein_binding": ">99%",
            "clearance": "Gan: chuyển hóa qua CYP3A4 thành metabolite hoạt động. Thận: bài tiết một phần. Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Không dùng ở bệnh nhân có xuất huyết nội sọ đang hoạt động, chảy máu đang hoạt động. Không dùng aspirin >100mg/ngày vì có thể giảm hiệu quả của ticagrelor.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa ticagrelor, tăng nồng độ",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "CHỐNG CHỈ ĐỊNH. Tránh dùng cùng strong CYP3A4 inhibitors."
                },
                {
                    "drug": "Aspirin >100mg/ngày",
                    "mechanism": "Có thể giảm hiệu quả của ticagrelor",
                    "effect": "Giảm hiệu quả chống kết tập tiểu cầu",
                    "management": "Dùng aspirin 75-100mg/ngày. Không dùng aspirin >100mg/ngày."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi INR, dấu hiệu chảy máu. Thường tránh dùng cùng."
                },
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa ticagrelor, giảm nồng độ",
                    "effect": "Giảm hiệu quả ticagrelor",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể."
                }
            ],
            "minor": [
                {
                    "drug": "Moderate CYP3A4 inhibitors (diltiazem, verapamil)",
                    "mechanism": "Có thể tăng nhẹ nồng độ ticagrelor",
                    "effect": "Tăng nhẹ nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Chảy máu đang hoạt động",
                "Xuất huyết nội sọ đang hoạt động",
                "Dị ứng ticagrelor",
                "Dùng strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)"
            ],
            "relative": [
                "Suy gan nặng - chống chỉ định",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Tiền sử nhịp tim chậm hoặc block nhĩ thất - tăng nguy cơ bradycardia",
                "Suy thận nặng - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Nguy cơ chảy máu ở mẹ và thai nhi. Cân nhắc nguy cơ huyết khối vs nguy cơ chảy máu. Theo dõi chặt chẽ dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Caution",
                "details": "Ticagrelor và metabolite có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ về dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Ticagrelor chuyển hóa ở gan qua CYP3A4. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Chống chỉ định ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Khó thở (dyspnea) - do tăng adenosine",
                "Nhịp tim chậm (bradycardia)",
                "Chảy máu có thể nghiêm trọng và đe dọa tính mạng"
            ],
            "antidote": "Không có antidote đặc hiệu. Truyền tiểu cầu nếu cần",
            "treatment": [
                "Ngừng ticagrelor ngay lập tức",
                "Truyền tiểu cầu nếu chảy máu nghiêm trọng (hiệu quả hạn chế do ticagrelor reversible)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi ít nhất 24-48 giờ (do half-life metabolite 8-12 giờ)",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, ECG (bradycardia)"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên dùng với thức ăn để giảm dyspnea và tăng hấp thu",
                "timing": "Uống 2 lần/ngày (sáng và tối), cách nhau 12 giờ. Loading dose: 180mg x 1 lần. Maintenance: 90mg x 2 lần/ngày. Dùng kèm aspirin 75-100mg/ngày."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Brilinta (ticagrelor)",
                "PLATO Study - New England Journal of Medicine",
                "UpToDate - Ticagrelor: Drug information",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Large RCT (PLATO study)"
        }
    },
    "Prasugrel": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Prasugrel, Effient",
        "administration": ["PO"],
        "indications": [
            "Hội chứng mạch vành cấp cần PCI",
            "Sau đặt stent"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Tiền sử TIA/đột quỵ",
            "Tuổi ≥75 (trừ nguy cơ cao)",
            "Cân nặng <60kg (trừ nguy cơ cao)"
        ],
        "dosage": {
            "adult_loading": "60mg x 1 lần",
            "adult_maintenance": "10mg x 1 lần/ngày (5mg nếu <60kg hoặc ≥75 tuổi)",
            "notes": "Mạnh hơn clopidogrel, nguy cơ chảy máu cao hơn"
        },
        "side_effects": [
            "Chảy máu (nhiều hơn clopidogrel)",
            "Chảy máu lớn (hiếm nhưng nguy hiểm)",
            "Thrombotic thrombocytopenic purpura (TTP) - hiếm"
        ],
        "interactions": [
            "Aspirin: dùng kèm (dual antiplatelet therapy)",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Prasugrel là chất ức chế P2Y12 receptor, đối kháng không thể đảo ngược (irreversible) với P2Y12 receptor trên tiểu cầu. P2Y12 receptor là một thụ thể adenosine diphosphate (ADP) quan trọng trong quá trình hoạt hóa và kết tập tiểu cầu. Prasugrel là một prodrug, được chuyển hóa nhanh chóng qua CYP3A4 và CYP2B6 thành metabolite hoạt động. Metabolite hoạt động gắn không thể đảo ngược với P2Y12 receptor, ức chế kết tập tiểu cầu do ADP. Prasugrel mạnh hơn và có tác dụng nhanh hơn clopidogrel, với ít biến thể di truyền (genetic variation) hơn. Prasugrel giảm nguy cơ huyết khối trong hội chứng mạch vành cấp cần can thiệp mạch vành (PCI), nhưng tăng nguy cơ chảy máu lớn so với clopidogrel, đặc biệt ở bệnh nhân có tiền sử TIA/đột quỵ hoặc tuổi ≥75.",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu tại vị trí tiêm)",
            "Chảy máu lớn (xuất huyết tiêu hóa, xuất huyết nội sọ, chảy máu sau phẫu thuật) - nguy cơ cao hơn clopidogrel",
            "Thrombotic thrombocytopenic purpura (TTP) - hiếm nhưng nguy hiểm (sốt, thiếu máu, giảm tiểu cầu, rối loạn thần kinh)",
            "Chức năng gan nếu có triệu chứng (hiếm)",
            "Công thức máu (tiểu cầu) nếu có dấu hiệu chảy máu"
        ],
        "precautions": [
            "Dùng kèm với aspirin 75-100mg/ngày (dual antiplatelet therapy - DAPT)",
            "Không dùng ở bệnh nhân có tiền sử TIA hoặc đột quỵ - tăng nguy cơ chảy máu nội sọ",
            "Thận trọng ở bệnh nhân ≥75 tuổi - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
            "Thận trọng ở bệnh nhân <60kg - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
            "Nguy cơ chảy máu cao hơn clopidogrel - không dùng nếu có chảy máu đang hoạt động",
            "Không ngừng đột ngột (tăng nguy cơ huyết khối)",
            "Không dùng ở bệnh nhân có nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây)",
            "Thời gian DAPT thường 12 tháng sau ACS với PCI, có thể kéo dài ở một số bệnh nhân nguy cơ cao",
            "Mạnh hơn clopidogrel - giảm nguy cơ huyết khối nhưng tăng nguy cơ chảy máu",
            "Liều khởi đầu: 60mg loading dose, sau đó 10mg/ngày (5mg nếu <60kg hoặc ≥75 tuổi)"
        ],
        "pharmacokinetics": {
            "half_life": "7 giờ",
            "onset": "30 phút - 1 giờ (nhanh hơn clopidogrel)",
            "duration": "7-10 ngày (do irreversible binding - tiểu cầu mới không bị ảnh hưởng)",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan: chuyển hóa nhanh qua CYP3A4 và CYP2B6 thành metabolite hoạt động (không cần chuyển hóa qua CYP2C19 như clopidogrel). Thận: bài tiết một phần. Không cần điều chỉnh liều ở suy thận hoặc suy gan nhẹ-trung bình."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Nguy cơ chảy máu nghiêm trọng, có thể gây tử vong. Không dùng ở bệnh nhân có tiền sử TIA hoặc đột quỵ - tăng nguy cơ chảy máu nội sọ. Không dùng ở bệnh nhân có chảy máu đang hoạt động. Thận trọng ở bệnh nhân ≥75 tuổi, <60kg, hoặc có nguy cơ chảy máu cao.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng chống đông",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi INR, dấu hiệu chảy máu. Thường tránh dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin",
                    "mechanism": "Dùng kèm trong dual antiplatelet therapy",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Dùng kèm aspirin 75-100mg/ngày. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "Tác dụng hiệp đồng chống kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Tránh dùng nếu có thể."
                }
            ],
            "minor": [
                {
                    "drug": "CYP inducers/inhibitors",
                    "mechanism": "Prasugrel chuyển hóa qua CYP3A4, CYP2B6, nhưng ít bị ảnh hưởng bởi CYP inhibitors/inducers hơn clopidogrel",
                    "effect": "Tương tác tối thiểu",
                    "management": "Không cần điều chỉnh liều"
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Chảy máu đang hoạt động",
                "Tiền sử TIA hoặc đột quỵ",
                "Dị ứng prasugrel"
            ],
            "relative": [
                "Tuổi ≥75 (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
                "Cân nặng <60kg (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày",
                "Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng",
                "Phẫu thuật lớn - cần ngừng trước phẫu thuật",
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Không có bằng chứng về nguy cơ gây dị tật thai nhi ở động vật. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Nguy cơ chảy máu ở mẹ và thai nhi. Cân nhắc nguy cơ huyết khối vs nguy cơ chảy máu. Theo dõi chặt chẽ dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Caution",
                "details": "Prasugrel và metabolite có thể bài tiết vào sữa mẹ. Không có dữ liệu đầy đủ về an toàn ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc nếu có thể. Nếu cần dùng, theo dõi trẻ chặt chẽ về dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng",
            "notes": "Prasugrel chuyển hóa ở gan qua CYP3A4 và CYP2B6. Không cần điều chỉnh liều ở suy gan nhẹ đến trung bình. Thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu: chảy máu mũi, chảy máu nướu, phân đen, nôn ra máu, chảy máu nội sọ",
                "Chảy máu lớn có thể nghiêm trọng và đe dọa tính mạng",
                "Thrombotic thrombocytopenic purpura (TTP) - hiếm nhưng nguy hiểm"
            ],
            "antidote": "Không có antidote đặc hiệu. Truyền tiểu cầu nếu cần (hiệu quả hạn chế do irreversible binding)",
            "treatment": [
                "Ngừng prasugrel ngay lập tức",
                "Truyền tiểu cầu nếu chảy máu nghiêm trọng (hiệu quả hạn chế do irreversible binding - cần tiểu cầu mới)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi dấu hiệu sống, công thức máu, dấu hiệu chảy máu",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Theo dõi ít nhất 7-10 ngày (do irreversible binding - tiểu cầu mới không bị ảnh hưởng)",
                "Điều trị chảy máu: truyền máu, tiểu cầu, huyết tương tươi đông lạnh nếu cần",
                "Nếu có TTP: điều trị với plasma exchange"
            ],
            "monitoring": "Dấu hiệu sống, công thức máu (tiểu cầu, hemoglobin), dấu hiệu chảy máu, dấu hiệu TTP"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Không ảnh hưởng đến hấp thu.",
                "timing": "Uống 1 lần/ngày. Loading dose: 60mg x 1 lần. Maintenance: 10mg x 1 lần/ngày (5mg nếu <60kg hoặc ≥75 tuổi). Dùng kèm aspirin 75-100mg/ngày."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Effient (prasugrel)",
                "TRITON-TIMI 38 Study - New England Journal of Medicine",
                "UpToDate - Prasugrel: Drug information",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Large RCT (TRITON-TIMI 38 study)"
        }
    },
    "Ticlopidine": {
        "group": "Cardiovascular - Antiplatelet",
        "vietnamese_name": "Ticlopidine, Ticlid",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ sau TIA",
            "Phòng ngừa huyết khối sau stent (ít dùng, thay bằng clopidogrel)"
        ],
        "contraindications": [
            "Giảm bạch cầu/giảm tiểu cầu",
            "Chảy máu đang hoạt động",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "250mg x 2 lần/ngày",
            "notes": "Ít dùng do nguy cơ giảm bạch cầu/tiểu cầu. Clopidogrel thay thế tốt hơn"
        },
        "side_effects": [
            "Giảm bạch cầu (nguy hiểm - cần theo dõi)",
            "Giảm tiểu cầu",
            "Ban xuất huyết giảm tiểu cầu huyết khối (TTP)",
            "Chảy máu",
            "Rối loạn tiêu hóa"
        ],
        "interactions": [
            "Aspirin: tăng nguy cơ chảy máu",
            "Warfarin: tăng nguy cơ chảy máu",
            "Antacids: giảm hấp thu"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ticlopidine là thienopyridine, ức chế P2Y12 receptor trên tiểu cầu, ngăn chặn kích hoạt tiểu cầu bởi ADP. Thuốc ức chế aggregation tiểu cầu và giải phóng các chất tiểu cầu, làm giảm hình thành huyết khối. Ticlopidine là prodrug, chuyển hóa trong gan thành chất hoạt động. Thuốc ức chế mạnh hơn clopidogrel nhưng có nhiều tác dụng phụ nghiêm trọng, đặc biệt giảm bạch cầu và giảm tiểu cầu, nên ít dùng, thay bằng clopidogrel. Thường dùng để phòng ngừa đột quỵ sau TIA, nhưng hiện tại clopidogrel là lựa chọn ưu tiên.",
        "monitoring": [
            "Công thức máu (CBC) - mỗi 2 tuần trong 3 tháng đầu (nguy cơ giảm bạch cầu cao nhất)",
            "Bạch cầu (WBC) - nếu <3500/μL: ngừng ngay",
            "Tiểu cầu - nếu <100,000/μL: ngừng ngay",
            "Dấu hiệu nhiễm trùng (sốt, đau họng) - dấu hiệu giảm bạch cầu",
            "Dấu hiệu chảy máu (xuất huyết, chảy máu chân răng)",
            "Dấu hiệu TTP (sốt, thiếu máu, giảm tiểu cầu, rối loạn thần kinh) - cấp cứu"
        ],
        "precautions": [
            "Ít dùng do nguy cơ giảm bạch cầu/tiểu cầu cao - clopidogrel thay thế tốt hơn",
            "Theo dõi sát công thức máu mỗi 2 tuần trong 3 tháng đầu (nguy cơ cao nhất)",
            "Ngừng ngay nếu giảm bạch cầu <3500/μL hoặc giảm tiểu cầu <100,000/μL",
            "Nguy cơ TTP (thrombotic thrombocytopenic purpura) - cấp cứu, có thể tử vong",
            "Thận trọng ở bệnh nhân suy gan (giảm chuyển hóa)",
            "Tránh dùng với aspirin và warfarin (tăng nguy cơ chảy máu)",
            "Có thể gây rối loạn tiêu hóa (buồn nôn, tiêu chảy)",
            "Ngừng 10-14 ngày trước phẫu thuật lớn"
        ],
        "pharmacokinetics": {
            "half_life": "4-5 ngày (rất dài)",
            "onset": "3-5 ngày (tác dụng tích tụ)",
            "duration": "7-10 ngày sau khi ngừng (do half-life dài)",
            "protein_binding": "98%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Nguy cơ giảm bạch cầu và giảm tiểu cầu nghiêm trọng, đe dọa tính mạng. Nguy cơ TTP (thrombotic thrombocytopenic purpura) có thể tử vong. Cần theo dõi công thức máu thường xuyên"
    },
    "Dipyridamole": {
        "group": "Cardiovascular - Antiplatelet",
        "vietnamese_name": "Dipyridamole, Persantine",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ/TIA (kết hợp với aspirin)",
            "Phòng ngừa huyết khối sau phẫu thuật van tim"
        ],
        "contraindications": [
            "Nhồi máu cơ tim cấp",
            "Co thắt mạch vành (vasospasm)"
        ],
        "dosage": {
            "adult_standard": "200mg x 2 lần/ngày (với aspirin)",
            "adult_modified_release": "200mg x 2 lần/ngày",
            "notes": "Thường dùng kết hợp với aspirin 25mg x 2 lần/ngày"
        },
        "side_effects": [
            "Nhức đầu (phổ biến)",
            "Chóng mặt",
            "Đau bụng",
            "Chảy máu",
            "Tim đập nhanh"
        ],
        "interactions": [
            "Aspirin: dùng kèm để tăng hiệu quả",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Dipyridamole ức chế phosphodiesterase và adenosine deaminase, làm tăng nồng độ cAMP và adenosine trong tiểu cầu, ức chế aggregation tiểu cầu. Thuốc cũng ức chế tái hấp thu adenosine, làm giãn mạch vành. Dipyridamole thường dùng kết hợp với aspirin để phòng ngừa đột quỵ/TIA sau stroke hoặc TIA. Thuốc có tác dụng chống đông và giãn mạch, nhưng có thể gây nhức đầu do giãn mạch. Thường dùng dạng modified-release để giảm tác dụng phụ.",
        "monitoring": [
            "Dấu hiệu chảy máu (xuất huyết, chảy máu chân răng, chảy máu cam)",
            "Nhức đầu (tác dụng phụ phổ biến, có thể giảm khi dùng liều thấp hơn)",
            "Huyết áp (có thể giảm nhẹ do giãn mạch)",
            "Nhịp tim (có thể tăng nhẹ)",
            "Đáp ứng điều trị (giảm nguy cơ đột quỵ/TIA)"
        ],
        "precautions": [
            "Thường dùng kết hợp với aspirin 25mg x 2 lần/ngày để tăng hiệu quả",
            "Nhức đầu là tác dụng phụ phổ biến (có thể giảm khi dùng liều thấp hơn hoặc dạng modified-release)",
            "Tránh dùng trong nhồi máu cơ tim cấp (có thể làm nặng thêm)",
            "Thận trọng ở bệnh nhân co thắt mạch vành (vasospasm)",
            "Tránh dùng với warfarin (tăng nguy cơ chảy máu)",
            "Có thể gây chóng mặt, đau bụng",
            "Ngừng 5-7 ngày trước phẫu thuật lớn",
            "Thận trọng ở bệnh nhân hạ huyết áp"
        ],
        "pharmacokinetics": {
            "half_life": "10-12 giờ",
            "onset": "2-4 giờ",
            "duration": "12-24 giờ",
            "protein_binding": "91-99%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None
    },
"Sertraline": {
        "group": "Psychiatry - SSRI (Selective Serotonin Reuptake Inhibitor)",
        "vietnamese_name": "Sertraline, Zoloft",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu",
            "Rối loạn ám ảnh cưỡng chế (OCD)",
            "Rối loạn stress sau sang chấn (PTSD)",
            "Rối loạn hoảng sợ"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng"
        ],
        "dosage": {
            "adult_depression": "50mg x 1 lần/ngày, tăng đến 50-200mg/ngày",
            "adult_ocd": "50-200mg/ngày",
            "adult_max": "200mg/ngày",
            "notes": "Khởi đầu 25-50mg/ngày, tăng dần. Uống buổi sáng hoặc tối"
        },
        "side_effects": [
            "Buồn nôn",
            "Tiêu chảy",
            "Mất ngủ",
            "Giảm ham muốn tình dục",
            "Nhức đầu",
            "Khô miệng",
            "Hội chứng serotonin (với thuốc khác)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng chống đông",
            "Tramadol: tăng nguy cơ co giật",
            "Triptans: tăng nguy cơ hội chứng serotonin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Sertraline là SSRI ức chế tái hấp thu serotonin ở synap thần kinh, tăng nồng độ serotonin và dẫn đến tác dụng chống trầm cảm, chống lo âu. Có tính chọn lọc cao với serotonin. Cũng có tác dụng ức chế nhẹ tái hấp thu dopamine ở liều cao. Tác dụng trên nhiều chỉ định: trầm cảm, lo âu, OCD, PTSD, hoảng sợ. Ưu điểm: half-life trung bình, ít tương tác thuốc hơn fluoxetine, dùng 1 lần/ngày",
        "monitoring": [
            "Tâm trạng và triệu chứng trầm cảm, lo âu (đánh giá định kỳ)",
            "Dấu hiệu tự tử (tăng nguy cơ trong vài tuần đầu, đặc biệt ở <24 tuổi)",
            "Dấu hiệu hội chứng serotonin (nếu dùng với thuốc khác)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Triệu chứng tiêu hóa: buồn nôn, tiêu chảy (phổ biến)",
            "Dấu hiệu rút thuốc khi ngừng (chóng mặt, buồn nôn)"
        ],
        "precautions": [
            "KHÔNG dùng với MAO inhibitor (chống chỉ định tuyệt đối)",
            "Ngừng sertraline ít nhất 2 tuần trước khi bắt đầu MAO inhibitor",
            "Theo dõi sát dấu hiệu tự tử trong vài tuần đầu (tăng nguy cơ ở <24 tuổi)",
            "Giảm liều dần khi ngừng (tránh hội chứng rút thuốc)",
            "Thận trọng khi dùng với tramadol, triptans (tăng nguy cơ hội chứng serotonin)",
            "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu)",
            "Có thể gây tiêu chảy (phổ biến) - thường tự hết sau vài tuần",
            "Khởi đầu với liều thấp (25-50mg), tăng dần"
        ],
        "pharmacokinetics": {
            "half_life": "26 giờ (trung bình)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "Dài (do half-life trung bình)",
            "protein_binding": "98% (rất cao)",
            "clearance": "Gan (chuyển hóa qua CYP2C9, CYP2C19, CYP2D6, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng sertraline ít nhất 2 tuần trước khi bắt đầu MAO inhibitor."
                },
                {
                    "drug": "Tramadol",
                    "mechanism": "Tăng nồng độ serotonin, tăng nguy cơ co giật",
                    "effect": "Hội chứng serotonin, tăng nguy cơ co giật",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giảm liều tramadol và theo dõi sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Triptans",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin",
                    "management": "Thận trọng. Dùng cách xa ít nhất 24 giờ."
                }
            ],
            "minor": [
                {
                    "drug": "CYP2D6 substrates",
                    "mechanism": "Ức chế CYP2D6 nhẹ",
                    "effect": "Tăng nhẹ nồng độ các thuốc chuyển hóa qua CYP2D6",
                    "management": "Thận trọng. Điều chỉnh liều nếu cần."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Dị ứng sertraline"
            ],
            "relative": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Có ý định tự tử - chỉ kê đơn số lượng ít",
                "Dùng với tramadol, triptans - tăng nguy cơ hội chứng serotonin"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Một số nghiên cứu gợi ý tăng nguy cơ dị tật thai nhi (dị tật tim) khi dùng trong 3 tháng đầu, nhưng chứng cứ không rõ ràng. Có thể gây tăng huyết áp phổi ở trẻ sơ sinh (PPHN) - nguy cơ thấp. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh.",
            "lactation": {
                "safety": "Compatible",
                "details": "Sertraline bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường <1% nồng độ mẹ. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú. Sertraline là SSRI được lựa chọn khi cho con bú do nồng độ trong sữa mẹ thấp. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Sertraline chuyển hóa ở gan qua CYP2C9, CYP2C19, CYP2D6, CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Kích động, lú lẫn",
                "Nhịp tim nhanh",
                "Co giật",
                "Hôn mê",
                "Hội chứng serotonin (nếu dùng với thuốc khác)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG, huyết áp, nhịp tim",
                "Điều trị hội chứng serotonin: Cyproheptadine, benzodiazepines",
                "Điều trị co giật: Benzodiazepines",
                "Truyền dịch",
                "Theo dõi ít nhất 24 giờ"
            ],
            "monitoring": "ECG, huyết áp, nhịp tim, ý thức, dấu hiệu co giật"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dùng 1 lần/ngày (buổi sáng hoặc tối). Có thể dùng cùng bữa ăn để giảm tiêu chảy."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zoloft (sertraline)",
                "UpToDate - Sertraline: Drug information",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Citalopram": {
        "group": "Psychiatry - SSRI",
        "vietnamese_name": "Citalopram, Celexa",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "QT prolongation",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "20mg x 1 lần/ngày, tăng đến 20-40mg/ngày",
            "adult_max": "40mg/ngày (20mg nếu >60 tuổi)",
            "notes": "Giới hạn 40mg/ngày do nguy cơ QT prolongation. Người già: max 20mg/ngày"
        },
        "side_effects": [
            "Buồn nôn",
            "Mất ngủ",
            "Nhức đầu",
            "QT prolongation (liều cao)",
            "Giảm ham muốn tình dục"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "QT prolonging drugs: tăng nguy cơ rối loạn nhịp",
            "Warfarin: có thể tăng tác dụng"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Citalopram là SSRI ức chế tái hấp thu serotonin ở synap thần kinh, tăng nồng độ serotonin và dẫn đến tác dụng chống trầm cảm, chống lo âu. Có tính chọn lọc cao với serotonin. Citalopram là racemic mixture (R- và S-enantiomer). S-enantiomer (escitalopram) là chất hoạt động chính. Tác dụng: trầm cảm, lo âu. CẢNH BÁO: Có thể gây QT kéo dài ở liều >40mg/ngày, đặc biệt ở người già",
        "monitoring": [
            "Tâm trạng và triệu chứng trầm cảm, lo âu (đánh giá định kỳ)",
            "Dấu hiệu tự tử (tăng nguy cơ trong vài tuần đầu, đặc biệt ở <24 tuổi)",
            "ECG nếu dùng liều cao >40mg/ngày hoặc ở người già (QT kéo dài)",
            "Dấu hiệu hội chứng serotonin (nếu dùng với thuốc khác)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Dấu hiệu rút thuốc khi ngừng"
        ],
        "precautions": [
            "KHÔNG dùng với MAO inhibitor (chống chỉ định tuyệt đối)",
            "GIỚI HẠN LIỀU 40mg/ngày (nguy cơ QT kéo dài, rối loạn nhịp)",
            "Người già >60 tuổi: GIỚI HẠN 20mg/ngày (tăng nguy cơ QT kéo dài)",
            "Theo dõi ECG nếu dùng liều cao hoặc ở người già",
            "Tránh dùng với các thuốc kéo dài QT khác",
            "Theo dõi sát dấu hiệu tự tử trong vài tuần đầu",
            "Giảm liều dần khi ngừng (tránh hội chứng rút thuốc)",
            "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu)",
            "Khởi đầu với liều thấp (20mg), tăng dần"
        ],
        "pharmacokinetics": {
            "half_life": "35 giờ (dài)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "80%",
            "clearance": "Gan (chuyển hóa qua CYP2C19, CYP3A4, CYP2D6), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. QT kéo dài có thể xảy ra ở liều >40mg/ngày, đặc biệt ở người già - giới hạn liều 40mg/ngày (20mg ở người già). Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng citalopram ít nhất 2 tuần trước khi bắt đầu MAO inhibitor."
                },
                {
                    "drug": "QT prolonging drugs (amiodarone, sotalol, quetiapine)",
                    "mechanism": "Tăng nguy cơ QT prolongation",
                    "effect": "QT kéo dài, rối loạn nhịp tim (torsades de pointes)",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giới hạn liều citalopram 20mg/ngày và theo dõi ECG."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Triptans, Tramadol",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin",
                    "management": "Thận trọng. Dùng cách xa ít nhất 24 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "QT prolongation",
                "Dị ứng citalopram",
                "Liều >40mg/ngày (chống chỉ định do QT prolongation)"
            ],
            "relative": [
                "Người già >60 tuổi - giới hạn 20mg/ngày",
                "Bệnh tim - tăng nguy cơ QT prolongation",
                "Rối loạn điện giải (hạ kali, hạ magne) - tăng nguy cơ QT prolongation",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Một số nghiên cứu gợi ý tăng nguy cơ dị tật thai nhi (dị tật tim) khi dùng trong 3 tháng đầu, nhưng chứng cứ không rõ ràng. Có thể gây tăng huyết áp phổi ở trẻ sơ sinh (PPHN) - nguy cơ thấp. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh.",
            "lactation": {
                "safety": "Compatible",
                "details": "Citalopram bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ bú mẹ thường <10% nồng độ mẹ. Có thể gây buồn ngủ, bú kém ở trẻ. Ít báo cáo về tác dụng phụ nghiêm trọng.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc chuyển sang SSRI khác (sertraline)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Citalopram chuyển hóa ở gan qua CYP2C19, CYP3A4, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ít gây độc gan trực tiếp."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Kích động, lú lẫn",
                "QT prolongation, rối loạn nhịp tim (torsades de pointes)",
                "Nhịp tim nhanh",
                "Co giật",
                "Hôn mê",
                "Hội chứng serotonin (nếu dùng với thuốc khác)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục - QT prolongation là nguy hiểm nhất",
                "Điều trị QT prolongation: Magnesium sulfate (2g IV), isoproterenol nếu cần",
                "Điều trị torsades de pointes: Magnesium sulfate, overdrive pacing",
                "Điều trị hội chứng serotonin: Cyproheptadine, benzodiazepines",
                "Điều trị co giật: Benzodiazepines",
                "Truyền dịch",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "ECG liên tục (QT interval), huyết áp, nhịp tim, ý thức, dấu hiệu co giật, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dùng 1 lần/ngày (buổi sáng hoặc tối). GIỚI HẠN 40mg/ngày (20mg ở người già >60 tuổi) do nguy cơ QT prolongation."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Celexa (citalopram)",
                "UpToDate - Citalopram: Drug information",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Escitalopram": {
        "group": "Psychiatry - SSRI",
        "vietnamese_name": "Escitalopram, Lexapro",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu tổng quát (GAD)",
            "Rối loạn hoảng sợ"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "10mg x 1 lần/ngày, tăng đến 10-20mg/ngày",
            "adult_max": "20mg/ngày",
            "notes": "Là S-enantiomer của citalopram, ít tác dụng phụ hơn"
        },
        "side_effects": [
            "Buồn nôn",
            "Mất ngủ",
            "Nhức đầu",
            "Giảm ham muốn tình dục",
            "Ít tác dụng phụ hơn citalopram"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng",
            "Tramadol: tăng nguy cơ co giật"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Escitalopram là S-enantiomer (chất hoạt động) của citalopram, SSRI ức chế tái hấp thu serotonin ở synap thần kinh. Tăng nồng độ serotonin dẫn đến tác dụng chống trầm cảm, chống lo âu. Là chất hoạt động chính của citalopram, nên hiệu quả tương đương với citalopram nhưng liều thấp hơn (10mg escitalopram ≈ 20mg citalopram). Ưu điểm: ít tác dụng phụ hơn citalopram, không có R-enantiomer (ít gây QT kéo dài hơn), dùng 1 lần/ngày",
        "monitoring": [
            "Tâm trạng và triệu chứng trầm cảm, lo âu (đánh giá định kỳ)",
            "Dấu hiệu tự tử (tăng nguy cơ trong vài tuần đầu, đặc biệt ở <24 tuổi)",
            "Dấu hiệu hội chứng serotonin (nếu dùng với thuốc khác)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Triệu chứng tiêu hóa: buồn nôn (phổ biến)",
            "Dấu hiệu rút thuốc khi ngừng"
        ],
        "precautions": [
            "KHÔNG dùng với MAO inhibitor (chống chỉ định tuyệt đối)",
            "Ngừng escitalopram ít nhất 2 tuần trước khi bắt đầu MAO inhibitor",
            "Theo dõi sát dấu hiệu tự tử trong vài tuần đầu (tăng nguy cơ ở <24 tuổi)",
            "Giảm liều dần khi ngừng (tránh hội chứng rút thuốc)",
            "Thận trọng khi dùng với tramadol, triptans (tăng nguy cơ hội chứng serotonin)",
            "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu)",
            "Khởi đầu với liều thấp (10mg), tăng dần",
            "Ưu điểm: ít tác dụng phụ hơn citalopram, ít nguy cơ QT kéo dài hơn"
        ],
        "pharmacokinetics": {
            "half_life": "27-32 giờ (dài)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "56% (thấp hơn citalopram)",
            "clearance": "Gan (chuyển hóa qua CYP2C19, CYP3A4, CYP2D6), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng escitalopram ít nhất 2 tuần trước khi bắt đầu MAO inhibitor."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Tramadol, Triptans",
                    "mechanism": "Tăng nồng độ serotonin",
                    "effect": "Hội chứng serotonin",
                    "management": "Thận trọng. Dùng cách xa ít nhất 24 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "absolute": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Dị ứng escitalopram"
            ],
            "relative": [
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Dùng với tramadol, triptans - tăng nguy cơ hội chứng serotonin"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Một số nghiên cứu gợi ý tăng nguy cơ dị tật thai nhi (dị tật tim) khi dùng trong 3 tháng đầu, nhưng chứng cứ không rõ ràng. Có thể gây tăng huyết áp phổi ở trẻ sơ sinh (PPHN) - nguy cơ thấp. Có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh.",
            "lactation": {
                "safety": "Compatible",
                "details": "Escitalopram bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường <5% nồng độ mẹ. An toàn cho trẻ bú mẹ. Ít báo cáo về tác dụng phụ ở trẻ.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém ở trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Escitalopram chuyển hóa ở gan qua CYP2C19, CYP3A4, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy. Tuy nhiên, ít gây độc gan trực tiếp."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Kích động, lú lẫn",
                "Nhịp tim nhanh",
                "Co giật",
                "Hôn mê",
                "Hội chứng serotonin (nếu dùng với thuốc khác)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG, huyết áp, nhịp tim",
                "Điều trị hội chứng serotonin: Cyproheptadine, benzodiazepines",
                "Điều trị co giật: Benzodiazepines",
                "Truyền dịch",
                "Theo dõi ít nhất 24-48 giờ"
            ],
            "monitoring": "ECG, huyết áp, nhịp tim, ý thức, dấu hiệu co giật"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm buồn nôn",
                "timing": "Dùng 1 lần/ngày (buổi sáng hoặc tối). Ưu điểm: ít tác dụng phụ hơn citalopram, ít nguy cơ QT kéo dài hơn."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lexapro (escitalopram)",
                "UpToDate - Escitalopram: Drug information",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Venlafaxine": {
        "group": "Psychiatry - SNRI (Serotonin-Norepinephrine Reuptake Inhibitor)",
        "vietnamese_name": "Venlafaxine, Effexor",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Rối loạn lo âu tổng quát (GAD)",
            "Rối loạn hoảng sợ",
            "Rối loạn lo âu xã hội"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Tăng huyết áp không kiểm soát",
            "Dị ứng"
        ],
        "dosage": {
            "adult_standard": "37.5-75mg x 2 lần/ngày (immediate) hoặc 75-150mg x 1 lần/ngày (extended release)",
            "adult_max": "225mg/ngày (immediate) hoặc 225mg/ngày (extended release)",
            "notes": "Extended release: uống 1 lần/ngày, thuận tiện hơn"
        },
        "side_effects": [
            "Buồn nôn",
            "Tăng huyết áp (liều cao)",
            "Mất ngủ",
            "Chóng mặt",
            "Giảm ham muốn tình dục",
            "Tăng nhịp tim",
            "Khó chịu khi ngừng (withdrawal)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định",
            "Warfarin: có thể tăng tác dụng",
            "Tramadol: tăng nguy cơ co giật và hội chứng serotonin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Venlafaxine là thuốc chống trầm cảm thuộc nhóm SNRI (serotonin-norepinephrine reuptake inhibitor), ức chế tái hấp thu serotonin và norepinephrine ở synap thần kinh. Ở liều thấp (<75mg/ngày), venlafaxine chủ yếu ức chế tái hấp thu serotonin (giống SSRI). Ở liều trung bình (75-225mg/ngày), venlafaxine ức chế cả serotonin và norepinephrine. Ở liều cao (>225mg/ngày), venlafaxine cũng có thể ức chế tái hấp thu dopamine nhẹ. Bằng cách ức chế tái hấp thu, venlafaxine làm tăng nồng độ serotonin và norepinephrine trong synap, dẫn đến tăng hoạt động của các chất dẫn truyền thần kinh này và cải thiện triệu chứng trầm cảm và lo âu. Venlafaxine có tác dụng mạnh hơn SSRI trong một số trường hợp, đặc biệt trầm cảm nặng và kháng trị. Tác dụng phụ chính: tăng huyết áp ở liều cao do ức chế norepinephrine. Venlafaxine có dạng extended release (ER) cho phép dùng 1 lần/ngày.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng trầm cảm, lo âu) - đánh giá sau 2-4 tuần",
            "Huyết áp - tăng huyết áp ở liều cao (>150mg/ngày), đặc biệt ở bệnh nhân có tăng huyết áp",
            "Nhịp tim - tăng nhịp tim có thể xảy ra",
            "Dấu hiệu hội chứng serotonin (sốt, kích động, run, nhịp tim nhanh, co giật) - đặc biệt khi dùng với tramadol, MAO inhibitor",
            "Dấu hiệu withdrawal (khó chịu, buồn nôn, chóng mặt, lo âu, mất ngủ) - khi ngừng đột ngột",
            "Tác dụng phụ (buồn nôn, mất ngủ, chóng mặt, giảm ham muốn tình dục)",
            "Tương tác với MAO inhibitor (chống chỉ định), warfarin (tăng INR), tramadol (tăng nguy cơ co giật và hội chứng serotonin)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với MAO inhibitor - phải ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu venlafaxine (nguy cơ hội chứng serotonin nghiêm trọng)",
            "Không ngừng đột ngột - giảm liều dần dần trong ít nhất 2 tuần (nguy cơ withdrawal syndrome: khó chịu, buồn nôn, chóng mặt, lo âu, mất ngủ)",
            "Tăng huyết áp - nguy cơ tăng ở liều cao (>150mg/ngày), đặc biệt ở bệnh nhân có tăng huyết áp, cần theo dõi huyết áp",
            "Tăng nhịp tim - có thể xảy ra, thận trọng ở bệnh nhân có bệnh tim",
            "Nguy cơ hội chứng serotonin - đặc biệt khi dùng với tramadol, triptans, MAO inhibitor, SSRI",
            "Tăng nguy cơ tự sát - đặc biệt ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi) trong vài tuần đầu",
            "Buồn nôn - tác dụng phụ phổ biến nhất, thường tự khỏi sau vài tuần, có thể giảm bằng cách uống với thức ăn",
            "Mất ngủ - có thể xảy ra, cân nhắc dùng vào buổi sáng",
            "Giảm ham muốn tình dục - tác dụng phụ phổ biến, có thể kéo dài",
            "Dạng extended release (ER) - uống 1 lần/ngày, thuận tiện hơn, ít tác dụng phụ hơn",
            "Dùng với thức ăn để giảm buồn nôn",
            "Thận trọng ở bệnh nhân có bệnh gan, suy thận (có thể cần giảm liều)"
        ],
        "pharmacokinetics": {
            "half_life": "5 giờ (venlafaxine), 11 giờ (desvenlafaxine - metabolite hoạt động)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm)",
            "duration": "12-24 giờ (dùng 1-2 lần/ngày)",
            "protein_binding": "27-30%",
            "clearance": "Gan: chuyển hóa qua CYP2D6 thành desvenlafaxine (metabolite hoạt động, mạnh hơn venlafaxine). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều ở suy thận và suy gan nặng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng extended release: bảo quản tương tự, không nghiền hoặc nhai (phải uống nguyên viên).",
        "black_box_warnings": "Nguy cơ tự sát và hành vi tự sát ở trẻ em, thanh thiếu niên, và người trẻ tuổi (<25 tuổi) với các thuốc chống trầm cảm. Nguy cơ tăng trong vài tháng đầu điều trị và khi tăng liều. Theo dõi chặt chẽ dấu hiệu tự sát, thay đổi hành vi, lo âu, kích động, mất ngủ, hoặc các triệu chứng mới hoặc nặng hơn. Nguy cơ hội chứng serotonin khi dùng với MAO inhibitor, tramadol, triptans.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa serotonin, tăng nồng độ serotonin",
                    "effect": "Nguy cơ hội chứng serotonin nghiêm trọng, có thể tử vong (sốt, kích động, run, nhịp tim nhanh, co giật, hôn mê)",
                    "management": "CHỐNG CHỈ ĐỊNH. Phải ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu venlafaxine. Phải ngừng venlafaxine ít nhất 7 ngày trước khi bắt đầu MAO inhibitor."
                },
                {
                    "drug": "Tramadol",
                    "mechanism": "Cả hai đều tăng serotonin, tăng nguy cơ hội chứng serotonin",
                    "effect": "Nguy cơ hội chứng serotonin và co giật",
                    "management": "Tránh dùng chung nếu có thể. Nếu phải dùng, theo dõi chặt chẽ dấu hiệu hội chứng serotonin. Giảm liều tramadol."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Venlafaxine có thể ức chế CYP2C9 nhẹ, tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Triptans (sumatriptan, rizatriptan)",
                    "mechanism": "Cả hai đều tăng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "Thận trọng, theo dõi dấu hiệu hội chứng serotonin. Có thể cần giảm liều triptan hoặc tăng khoảng cách giữa các liều."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Tăng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin",
                    "management": "Theo dõi dấu hiệu hội chứng serotonin. Có thể cần giảm liều lithium."
                },
                {
                    "drug": "Cimetidine",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa venlafaxine",
                    "effect": "Tăng nồng độ venlafaxine",
                    "management": "Giảm liều venlafaxine 25-50%. Theo dõi tác dụng phụ."
                }
            ],
            "minor": [
                {
                    "drug": "Metoclopramide",
                    "mechanism": "Cả hai đều tăng serotonin nhẹ",
                    "effect": "Tăng nhẹ nguy cơ hội chứng serotonin",
                    "management": "Theo dõi dấu hiệu hội chứng serotonin. Thường không cần điều chỉnh liều."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dùng MAO inhibitor (trong vòng 14 ngày)",
                "Dị ứng venlafaxine hoặc các thành phần khác"
            ],
            "relative": [
                "Tăng huyết áp không kiểm soát - nguy cơ tăng huyết áp ở liều cao",
                "Bệnh tim mạch (loạn nhịp, suy tim) - tăng nhịp tim, tăng huyết áp",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tích lũy",
                "Suy thận nặng (CrCl <30) - giảm thải trừ, tăng nguy cơ tích lũy",
                "Mang thai (nguy cơ dị tật bẩm sinh, withdrawal ở trẻ sơ sinh) - chỉ dùng nếu lợi ích > nguy cơ",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Glaucoma góc hẹp - tăng nguy cơ tăng nhãn áp",
                "Bệnh nhân lớn tuổi - tăng nguy cơ tác dụng phụ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chứng cứ về an toàn trong thai kỳ còn hạn chế. Một số nghiên cứu gợi ý tăng nhẹ nguy cơ dị tật bẩm sinh (tim, sứt môi/hà ếch), nhưng chứng cứ không rõ ràng. Trẻ sơ sinh có thể có withdrawal syndrome (khó chịu, run, khó thở, co giật) nếu mẹ dùng venlafaxine trong thai kỳ, đặc biệt gần cuối thai kỳ. Chỉ dùng nếu lợi ích điều trị vượt trội nguy cơ. Nếu dùng trong thai kỳ, cần tư vấn di truyền và theo dõi chặt chẽ. Theo dõi trẻ sơ sinh về dấu hiệu withdrawal.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Venlafaxine và desvenlafaxine bài tiết vào sữa mẹ ở nồng độ thấp đến trung bình. Nồng độ trong máu trẻ sơ sinh rất thấp (<5% nồng độ trong máu mẹ). Tác dụng phụ ở trẻ rất hiếm nhưng có thể có buồn ngủ nhẹ, kích động nhẹ.",
                "recommendation": "Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, kích động, bú kém)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%, theo dõi tác dụng phụ",
            "severe": "Giảm liều 50%, theo dõi tác dụng phụ chặt chẽ. Hoặc tránh dùng nếu có thể.",
            "notes": "Venlafaxine chuyển hóa ở gan qua CYP2D6 thành desvenlafaxine. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy venlafaxine và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: buồn ngủ, chóng mặt, lú lẫn, co giật, hôn mê",
                "Hội chứng serotonin: sốt, kích động, run, nhịp tim nhanh, tăng huyết áp, co giật",
                "Rối loạn tim mạch: nhịp nhanh, tăng huyết áp, rối loạn nhịp, QT kéo dài",
                "Rối loạn hô hấp: suy hô hấp",
                "Rối loạn tiêu hóa: buồn nôn, nôn",
                "Triệu chứng khác: giãn đồng tử, sốt"
            ],
            "antidote": "Không có antidote đặc hiệu. Cyproheptadine có thể được dùng để điều trị hội chứng serotonin (không được FDA chấp thuận).",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ sau uống (nếu bệnh nhân tỉnh táo)",
                "Than hoạt tính: 1g/kg (tối đa 50-100g) nếu trong vòng 1-2 giờ",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch, điện tâm đồ (QT kéo dài)",
                "Xử trí hội chứng serotonin: cyproheptadine (antagonist serotonin), hạ nhiệt, benzodiazepine cho kích động, co giật",
                "Xử trí co giật: benzodiazepine (diazepam, lorazepam)",
                "Xử trí tăng huyết áp: labetalol, esmolol (beta-blocker)",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Theo dõi điện tâm đồ: QT kéo dài, rối loạn nhịp"
            ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch, điện tâm đồ (QT, nhịp tim), dấu hiệu hội chứng serotonin, nhiệt độ cơ thể"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm buồn nôn (tác dụng phụ phổ biến nhất)",
                "timing": "Dạng immediate release: chia 2-3 lần/ngày. Dạng extended release (ER): uống 1 lần/ngày vào buổi sáng hoặc tối. Uống cùng thời điểm mỗi ngày. KHÔNG nghiền hoặc nhai viên ER (phải uống nguyên viên). Không ngừng đột ngột - giảm liều dần dần trong ít nhất 2 tuần."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "Lexicomp - Venlafaxine",
                "UpToDate - Venlafaxine: Drug information",
                "FDA - Effexor (venlafaxine) prescribing information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 13th ed."
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Evidence from well-designed randomized controlled trials and systematic reviews"
        }
    },
    "Amitriptyline": {
        "group": "Psychiatry - Tricyclic Antidepressant (TCA)",
        "vietnamese_name": "Amitriptyline, Elavil",
        "administration": ["PO"],
        "indications": [
            "Trầm cảm",
            "Đau thần kinh (neuropathic pain)",
            "Migraine phòng ngừa",
            "Rối loạn giấc ngủ",
            "Đau cơ xơ hóa"
        ],
        "contraindications": [
            "Dùng MAO inhibitor",
            "Nhồi máu cơ tim gần đây",
            "Block nhĩ thất độ 2-3",
            "Rối loạn nhịp tim",
            "Suy tim nặng"
        ],
        "dosage": {
            "adult_depression": "25-75mg x 1 lần/ngày buổi tối, tăng đến 50-150mg/ngày",
            "adult_neuropathic": "10-25mg buổi tối, tăng đến 25-100mg/ngày",
            "adult_max": "150-300mg/ngày",
            "notes": "Dùng buổi tối để tránh buồn ngủ ban ngày. Nguy cơ quá liều cao"
        },
        "side_effects": [
            "Buồn ngủ (phổ biến)",
            "Khô miệng",
            "Táo bón",
            "Rối loạn nhịp tim",
            "Hạ huyết áp tư thế",
            "Nhìn mờ",
            "Tăng cân",
            "Nguy cơ quá liều (cardiotoxic)"
        ],
        "interactions": [
            "MAO inhibitor: chống chỉ định (nguy hiểm)",
            "Quinidine: tăng nồng độ amitriptyline",
            "Cimetidine: tăng nồng độ",
            "Alcohol: tăng tác dụng an thần",
            "Sympathomimetics: tăng nguy cơ tăng huyết áp"
        ],
        "pregnancy": "C - D trong 3 tháng đầu",
        "mechanism_of_action": "Amitriptyline là tricyclic antidepressant (TCA) ức chế tái hấp thu norepinephrine và serotonin ở synap thần kinh, tăng nồng độ các chất dẫn truyền thần kinh này. Cũng có tác dụng chẹn muscarinic (kháng cholinergic), histamine H1 (an thần), và alpha-1 adrenergic (hạ huyết áp). Tác dụng chống trầm cảm, giảm đau thần kinh (cơ chế chưa rõ hoàn toàn), phòng ngừa migraine. Có tác dụng an thần mạnh do chẹn histamine H1",
        "monitoring": [
            "ECG trước khi bắt đầu và định kỳ (đặc biệt ở bệnh nhân có bệnh tim, cao tuổi) - QT kéo dài, block nhĩ thất",
            "Nhịp tim, huyết áp (hạ huyết áp tư thế, rối loạn nhịp)",
            "Dấu hiệu quá liều: nhịp tim nhanh, loạn nhịp, co giật, hôn mê (cấp cứu)",
            "Triệu chứng kháng cholinergic: khô miệng, táo bón, nhìn mờ, bí tiểu",
            "Tâm trạng và triệu chứng trầm cảm",
            "Chức năng gan nếu có triệu chứng (hiếm)"
        ],
        "precautions": [
            "NGUY CƠ QUÁ LIỀU CAO - cardiotoxic (rối loạn nhịp, block nhĩ thất), có thể tử vong",
            "Chỉ kê đơn số lượng ít, theo dõi sát bệnh nhân có ý định tự tử",
            "Không dùng với MAO inhibitor (chống chỉ định tuyệt đối - nguy cơ cao huyết áp, sốt, co giật, tử vong)",
            "Thận trọng ở bệnh nhân có bệnh tim, block nhĩ thất (chống chỉ định block độ 2-3)",
            "Dùng buổi tối để tránh buồn ngủ ban ngày (tác dụng an thần mạnh)",
            "Khởi đầu với liều thấp (10-25mg), tăng dần",
            "Giảm liều dần khi ngừng (tránh hội chứng cai)",
            "Tránh rượu (tăng tác dụng an thần, nguy cơ quá liều)",
            "Thận trọng khi lái xe hoặc vận hành máy móc (buồn ngủ, nhìn mờ)",
            "Theo dõi sát bệnh nhân có ý định tự tử (tăng nguy cơ trong vài tuần đầu)"
        ],
        "pharmacokinetics": {
            "half_life": "10-28 giờ (dài)",
            "onset": "2-4 tuần (tác dụng chống trầm cảm), nhanh hơn (giảm đau, an thần)",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "82-96% (cao)",
            "clearance": "Gan (chuyển hóa qua CYP2D6, CYP2C19, CYP1A2), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tăng nguy cơ tự tử ở trẻ em, thanh thiếu niên, và thanh niên <24 tuổi trong vài tháng đầu điều trị. Quá liều có thể gây rối loạn nhịp tim nghiêm trọng, block nhĩ thất, co giật, hôn mê, tử vong. Chống chỉ định với MAO inhibitor",
        "drug_interactions": {
            "major": [
                {
                    "drug": "MAO inhibitors (phenelzine, tranylcypromine, selegiline)",
                    "mechanism": "Ức chế chuyển hóa catecholamines, tăng nồng độ serotonin và norepinephrine",
                    "effect": "Hội chứng serotonin, tăng huyết áp nghiêm trọng, sốt cao, co giật, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAO inhibitor ít nhất 14 ngày trước khi bắt đầu amitriptyline."
                },
                {
                    "drug": "Quinidine, Cimetidine",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa amitriptyline",
                    "effect": "Tăng nồng độ amitriptyline, tăng nguy cơ độc tính (rối loạn nhịp, block nhĩ thất)",
                    "management": "Giảm liều amitriptyline 50%. Theo dõi ECG. Thận trọng."
                },
                {
                    "drug": "Sympathomimetics (epinephrine, norepinephrine)",
                    "mechanism": "Tăng tác dụng alpha-adrenergic",
                    "effect": "Tăng huyết áp nghiêm trọng, rối loạn nhịp tim",
                    "management": "Tránh dùng. Nếu cần, dùng liều thấp và theo dõi huyết áp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng an thần, suy hô hấp, nguy cơ quá liều",
                    "management": "Tránh rượu. Cảnh báo bệnh nhân về nguy cơ."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Anticholinergics (atropine, benztropine)",
                    "mechanism": "Tăng tác dụng kháng cholinergic",
                    "effect": "Tăng khô miệng, táo bón, bí tiểu, nhìn mờ, lú lẫn",
                    "management": "Thận trọng. Giảm liều hoặc tránh dùng cùng."
                }
            ],
            "minor": [
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa",
                    "effect": "Giảm nồng độ amitriptyline",
                    "management": "Tăng liều amitriptyline nếu cần"
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dùng MAO inhibitor (chống chỉ định tuyệt đối)",
                "Nhồi máu cơ tim gần đây (<6 tháng)",
                "Block nhĩ thất độ 2-3",
                "Rối loạn nhịp tim nặng",
                "Suy tim nặng (NYHA class IV)",
                "Dị ứng amitriptyline hoặc TCA"
            ],
            "relative": [
                "Bệnh tim (thiếu máu cơ tim, suy tim nhẹ-trung bình) - thận trọng, theo dõi ECG",
                "Block nhĩ thất độ 1 - thận trọng",
                "Tăng nhãn áp (glaucoma) - tăng nguy cơ",
                "Bí tiểu - tăng nguy cơ",
                "Suy gan nặng - giảm liều",
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Trẻ em <18 tuổi - tăng nguy cơ tự tử",
                "Có ý định tự tử - chỉ kê đơn số lượng ít"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dùng được trong thai kỳ nếu lợi ích > nguy cơ. Có nguy cơ dị tật thai nhi (dị tật tim, dị tật chi) khi dùng trong 3 tháng đầu, đặc biệt liều cao. Có thể gây hội chứng cai ở trẻ sơ sinh (kích động, khó thở, run, co giật) nếu dùng gần ngày sinh. Theo dõi trẻ sơ sinh sau sinh. Nguy cơ rối loạn phát triển thần kinh thấp.",
            "lactation": {
                "safety": "Compatible with caution",
                "details": "Amitriptyline bài tiết vào sữa mẹ ở nồng độ thấp (<5% liều mẹ). Nồng độ trong máu trẻ bú mẹ thường rất thấp. Có thể gây buồn ngủ, bú kém ở trẻ. Ít báo cáo về tác dụng phụ nghiêm trọng.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi chặt chẽ trẻ. Theo dõi dấu hiệu buồn ngủ, bú kém, táo bón ở trẻ. Nếu trẻ có dấu hiệu bất thường, cân nhắc ngừng cho con bú hoặc giảm liều."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi hoặc giảm liều nhẹ",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Amitriptyline chuyển hóa ở gan qua CYP2D6, CYP2C19, CYP1A2. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính. Tuy nhiên, ít gây độc gan trực tiếp."
        },
        "overdose_management": {
            "symptoms": [
                "Giai đoạn sớm: Buồn ngủ, lú lẫn, chóng mặt, nhìn mờ",
                "Giai đoạn nặng: Rối loạn nhịp tim (nhịp nhanh, rung nhĩ, block nhĩ thất), hạ huyết áp hoặc tăng huyết áp",
                "Co giật, hôn mê",
                "Suy hô hấp",
                "Triệu chứng kháng cholinergic: khô miệng, bí tiểu, nhịp tim nhanh, sốt",
                "Tử vong do rối loạn nhịp tim hoặc suy hô hấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Có thể dùng sodium bicarbonate cho rối loạn nhịp",
            "treatment": [
                "Hỗ trợ hô hấp và tuần hoàn ngay lập tức (quan trọng nhất)",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ (thận trọng nếu đã hôn mê)",
                "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                "Theo dõi ECG liên tục - rối loạn nhịp là nguy hiểm nhất",
                "Điều trị rối loạn nhịp: Sodium bicarbonate (1-2 mEq/kg IV bolus) để điều chỉnh QT kéo dài và block nhĩ thất",
                "Điều trị co giật: Benzodiazepines (lorazepam, diazepam)",
                "Điều trị hạ huyết áp: Truyền dịch, vận mạch nếu cần",
                "Theo dõi điện giải, đường huyết",
                "Lọc máu (hemodialysis) KHÔNG hiệu quả do protein binding cao",
                "Theo dõi ít nhất 24-48 giờ (do half-life dài)"
            ],
            "monitoring": "ECG liên tục (rối loạn nhịp), huyết áp, nhịp tim, ý thức, hô hấp, điện giải, đường huyết, nhiệt độ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm kích ứng dạ dày",
                "timing": "Dùng buổi tối (1 lần/ngày) để tránh buồn ngủ ban ngày. Có thể chia 2-3 lần nếu liều cao hoặc tác dụng phụ nhiều"
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Elavil (amitriptyline)",
                "UpToDate - Amitriptyline: Drug information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "American Psychiatric Association guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
"Dexamethasone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Dexamethasone, Decadron",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản",
            "Phù não",
            "Nôn do hóa trị",
            "Chấn thương tủy sống",
            "Viêm màng não do vi khuẩn (kết hợp kháng sinh)",
            "COVID-19 (nặng)"
        ],
        "contraindications": [
            "Nhiễm nấm hệ thống không điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_antiinflammatory": "0.75-9mg/ngày chia 2-4 lần",
            "adult_edema": "10mg IV x 1 lần, sau đó 4mg IV mỗi 6 giờ",
            "adult_chemotherapy_nausea": "8-20mg x 1 lần trước hóa trị",
            "adult_covid19": "6mg x 1 lần/ngày (IV hoặc PO) x 10 ngày",
            "notes": "Tác dụng dài, ức chế mạnh. Không dùng cho nhiễm nấm không điều trị"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Ức chế miễn dịch",
            "Tăng cân",
            "Loét dạ dày",
            "Rối loạn tâm thần",
            "Phù",
            "Khó ngủ"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày",
            "Insulin/OAD: tăng đường huyết",
            "Vaccines: giảm hiệu quả vaccine"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Glucocorticoid tổng hợp tác dụng dài và mạnh (tương đương 25-30mg hydrocortisone). Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm, ức chế phospholipase A2 → giảm prostaglandin và leukotriene. Ức chế miễn dịch mạnh. Tác dụng chống viêm và ức chế miễn dịch mạnh hơn hydrocortisone. Thời gian bán thải dài (36-72 giờ) do ít gắn với protein hơn hydrocortisone.",
        "monitoring": [
            "Đường huyết (tăng đường huyết, đặc biệt ở bệnh nhân đái tháo đường)",
            "Huyết áp (tăng huyết áp)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Điện giải (hạ kali, giữ natri)",
            "Tâm thần (rối loạn tâm thần, mất ngủ, kích động)",
            "Dạ dày (dấu hiệu loét, xuất huyết)",
            "Xương (loãng xương nếu dùng kéo dài)",
            "Mắt (tăng nhãn áp, đục thủy tinh thể)",
            "Chức năng thượng thận (ức chế trục HPA nếu dùng kéo dài)"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột nếu dùng > 1 tuần (có thể gây suy thượng thận cấp - nguy hiểm tính mạng)",
            "Phải giảm liều dần dần (tapering) nếu dùng > 1 tuần",
            "Ức chế miễn dịch mạnh - tăng nguy cơ nhiễm trùng, đặc biệt nhiễm nấm, lao",
            "Không dùng trong nhiễm nấm hệ thống không điều trị (có thể làm nặng)",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Thận trọng ở bệnh nhân loét dạ dày (tăng nguy cơ)",
            "Thận trọng ở bệnh nhân tăng huyết áp (có thể tăng huyết áp)",
            "Dùng với thức ăn để giảm kích ứng dạ dày",
            "Dự phòng loãng xương nếu dùng kéo dài (bổ sung calcium, vitamin D)",
            "Theo dõi dấu hiệu nhiễm trùng (ức chế miễn dịch có thể che dấu triệu chứng)",
            "Thời gian bán thải dài → ức chế trục HPA lâu hơn hydrocortisone"
        ],
        "pharmacokinetics": {
            "half_life": "36-72 giờ (rất dài)",
            "onset": "1-2 giờ (PO/IV)",
            "duration": "36-72 giờ",
            "protein_binding": "77% (thấp hơn hydrocortisone)",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ngừng đột ngột sau khi dùng kéo dài có thể gây suy thượng thận cấp, có thể tử vong. Ức chế miễn dịch mạnh có thể làm nặng nhiễm trùng hoặc gây nhiễm trùng cơ hội.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ketoconazole, Itraconazole (Azole antifungals)",
                    "mechanism": "Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa dexamethasone, tăng nồng độ và tác dụng.",
                    "effect": "Tăng nồng độ dexamethasone, tăng tác dụng và tác dụng phụ (Cushing, tăng đường huyết, ức chế miễn dịch)",
                    "management": "Giảm liều dexamethasone 25-50% khi dùng với azole antifungals. Theo dõi đường huyết, dấu hiệu Cushing."
                },
                {
                    "drug": "Rifampin, Rifabutin",
                    "mechanism": "Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa dexamethasone, giảm nồng độ và hiệu quả.",
                    "effect": "Giảm nồng độ dexamethasone, giảm hiệu quả điều trị",
                    "management": "Tăng liều dexamethasone 25-50% khi dùng với rifampin. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Corticosteroid có thể thay đổi chuyển hóa warfarin và ảnh hưởng đến đông máu.",
                    "effect": "Thay đổi INR (có thể tăng hoặc giảm), tăng nguy cơ chảy máu hoặc huyết khối",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng dexamethasone. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAID (Ibuprofen, Naproxen, Diclofenac)",
                    "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.",
                    "effect": "Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa nghiêm trọng",
                    "management": "Cân nhắc dùng PPI hoặc misoprostol. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu chảy máu dạ dày."
                },
                {
                    "drug": "Phenytoin, Phenobarbital, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa, tăng chuyển hóa dexamethasone.",
                    "effect": "Giảm nồng độ dexamethasone, giảm hiệu quả",
                    "management": "Tăng liều dexamethasone. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cả hai đều ức chế miễn dịch, tác dụng cộng dồn. Có thể ảnh hưởng đến chuyển hóa.",
                    "effect": "Tăng ức chế miễn dịch, tăng nguy cơ nhiễm trùng, tăng nguy cơ độc tính",
                    "management": "Giảm liều cả hai thuốc. Theo dõi chức năng thận, dấu hiệu nhiễm trùng."
                }
            ],
            "minor": [
                {
                    "drug": "Diuretics (Thiazide, Furosemide)",
                    "mechanism": "Corticosteroid gây giữ natri, có thể đối kháng tác dụng lợi tiểu.",
                    "effect": "Giảm hiệu quả lợi tiểu, có thể gây giữ nước",
                    "management": "Theo dõi cân nặng, dấu hiệu giữ nước. Có thể cần điều chỉnh liều lợi tiểu."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Nhiễm nấm hệ thống không điều trị (cryptococcosis, histoplasmosis, coccidioidomycosis) - corticosteroid làm nặng nhiễm nấm",
                "Dị ứng dexamethasone hoặc các corticosteroid khác",
                "Nhiễm virus hoạt động (herpes simplex keratitis, varicella zoster lan tỏa) - trừ khi chỉ định đặc biệt"
            ],
            "relative": [
                "Nhiễm trùng đang hoạt động - có thể làm nặng, che dấu triệu chứng",
                "Đái tháo đường - tăng đường huyết, cần theo dõi và điều chỉnh",
                "Tăng huyết áp - có thể tăng huyết áp, giữ nước",
                "Suy tim - giữ nước, có thể làm nặng",
                "Loãng xương - tăng nguy cơ gãy xương",
                "Loét dạ dày tá tràng - tăng nguy cơ loét",
                "Rối loạn tâm thần - có thể làm nặng",
                "Glaucoma - có thể tăng nhãn áp",
                "Có thai - có thể ảnh hưởng đến thai nhi",
                "Suy gan - có thể giảm chuyển hóa",
                "Suy thận - không cần điều chỉnh liều nhưng thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dexamethasone là thuốc phân loại C. Corticosteroid có thể đi qua nhau thai và có thể ảnh hưởng đến thai nhi. Dùng lâu dài hoặc liều cao trong thai kỳ có thể gây ức chế thượng thận ở trẻ sơ sinh, chậm phát triển, tăng nguy cơ sứt môi/vòm miệng (khi dùng trong tam cá nguyệt đầu), và các tác dụng phụ khác. Tuy nhiên, dexamethasone được sử dụng trong thai kỳ để điều trị một số bệnh tự miễn và hen phế quản. Nên dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Tránh dùng liều cao kéo dài trong thai kỳ nếu có thể.",
            "lactation": {
                "safety": "Compatible (với dùng ngắn hạn)",
                "details": "Dexamethasone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ với liều thường dùng. Với liều cao hoặc kéo dài, có thể ảnh hưởng đến trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với liều điều trị tiêu chuẩn. Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Dexamethasone chuyển hóa qua gan nhưng không phụ thuộc nhiều vào chức năng gan.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng thời gian bán thải.",
            "notes": "Dexamethasone chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng có thể làm giảm chuyển hóa, tăng thời gian bán thải, tăng nồng độ và tác dụng. Theo dõi tác dụng phụ chặt chẽ ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng Cushing: Tăng cân, mặt tròn, tích mỡ, bướu trâu, vết rạn da, tăng huyết áp",
                "Triệu chứng chuyển hóa: Tăng đường huyết nghiêm trọng, toan chuyển hóa, hạ kali máu",
                "Triệu chứng tiêu hóa: Loét dạ dày, xuất huyết tiêu hóa, thủng dạ dày",
                "Triệu chứng thần kinh: Kích động, loạn thần, trầm cảm, co giật, hôn mê",
                "Triệu chứng miễn dịch: Nhiễm trùng nghiêm trọng (do ức chế miễn dịch), che dấu triệu chứng nhiễm trùng",
                "Triệu chứng tim mạch: Suy tim, phù, giữ nước, tăng huyết áp nặng",
                "Triệu chứng nghiêm trọng: Suy thượng thận cấp (khi ngừng đột ngột sau dùng lâu dài), sốc, tử vong"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay dexamethasone nếu có thể (nhưng KHÔNG ngừng đột ngột nếu đã dùng >2 tuần - phải giảm dần)",
                "Nếu ngừng đột ngột sau dùng lâu dài:",
                "  - Bắt đầu lại corticosteroid ngay (hydrocortisone 100mg IV mỗi 6-8 giờ)",
                "  - Giảm dần liều theo thời gian",
                "Điều trị tăng đường huyết:",
                "  - Theo dõi đường huyết thường xuyên",
                "  - Insulin nếu cần",
                "  - Điều chỉnh liều đái tháo đường",
                "Điều trị loét dạ dày/xuất huyết tiêu hóa:",
                "  - PPI (omeprazole, pantoprazole)",
                "  - Truyền máu nếu cần",
                "  - Nội soi dạ dày nếu nghi ngờ thủng",
                "Điều trị rối loạn tâm thần:",
                "  - An thần nếu kích động, loạn thần",
                "  - Antipsychotic nếu cần",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị nhiễm trùng:",
                "  - Kháng sinh nếu có nhiễm trùng",
                "  - Theo dõi dấu hiệu nhiễm trùng (có thể che dấu)",
                "Điều chỉnh điện giải:",
                "  - Bổ sung kali nếu hạ kali máu",
                "  - Điều chỉnh natri nếu cần",
                "Hỗ trợ huyết động:",
                "  - Truyền dịch nếu cần",
                "  - Thuốc vận mạch nếu sốc",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, đường huyết"
            ],
            "monitoring": "Theo dõi đường huyết, điện giải, dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu loét dạ dày, tâm thần trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng. Nếu ngừng đột ngột sau dùng lâu dài, theo dõi dấu hiệu suy thượng thận cấp trong ít nhất 1-2 tuần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.",
                "timing": "Uống 1-4 lần/ngày tùy chỉ định. Có thể uống buổi sáng (để giảm ảnh hưởng đến giấc ngủ) hoặc chia đều trong ngày. Với liều cao, chia nhiều lần. Với liều thấp, có thể uống 1 lần buổi sáng."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1-5mg/ml. Pha 4mg trong 50ml dịch = 0.08mg/ml. Pha 10mg trong 50ml dịch = 0.2mg/ml.",
                "infusion_rate": "Truyền trong 15-30 phút. Không truyền quá nhanh. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với thuốc có tính kiềm hoặc axit."],
                "notes": "Theo dõi đường huyết, huyết áp, điện giải trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Dexamethasone (Decadron)",
                "UpToDate - Dexamethasone: Drug Information",
                "Medscape - Dexamethasone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Dexamethasone Monograph",
                "Micromedex - Dexamethasone Drug Information",
                "Endocrine Society Guidelines - Corticosteroid Use"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Methylprednisolone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Methylprednisolone, Medrol",
        "administration": ["PO", "IV", "IM"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản",
            "Bệnh tự miễn",
            "Sốc phản vệ (kết hợp)",
            "Chấn thương tủy sống",
            "Đợt cấp bệnh đa xơ cứng"
        ],
        "contraindications": [
            "Nhiễm nấm hệ thống không điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "4-48mg/ngày chia 1-4 lần",
            "adult_iv_pulse": "250-1000mg IV x 1 lần/ngày x 3-5 ngày",
            "adult_iv_standard": "40-125mg IV mỗi 6-12 giờ",
            "spinal_cord_injury": "30mg/kg IV x 1 lần, sau đó 5.4mg/kg/giờ x 23 giờ",
            "notes": "IV pulse therapy cho bệnh nặng. Giảm dần liều khi ngừng"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Ức chế miễn dịch",
            "Tăng cân",
            "Loét dạ dày",
            "Rối loạn tâm thần"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày",
            "Ketoconazole: tăng nồng độ methylprednisolone"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Methylprednisolone là một corticosteroid tổng hợp, tương tự cortisol tự nhiên nhưng có hoạt tính mạnh hơn. Tác dụng qua thụ thể glucocorticoid (GR) trong tế bào, điều hòa biểu hiện gen (gen activation và repression). Ức chế tổng hợp và giải phóng các chất trung gian gây viêm (prostaglandin, leukotriene, cytokine), ức chế di cư bạch cầu và hoạt động miễn dịch. Tác dụng chống viêm, chống dị ứng, ức chế miễn dịch mạnh. Có tác dụng mineralocorticoid nhẹ hơn hydrocortisone",
        "monitoring": [
            "Đường huyết (glucose) khi dùng liều cao hoặc kéo dài",
            "Huyết áp (corticosteroid có thể tăng huyết áp)",
            "Điện giải (natri, kali) khi dùng liều cao",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch, có thể che dấu triệu chứng)",
            "Dấu hiệu loét dạ dày (đau bụng, phân đen, nôn ra máu)",
            "Tâm thần (kích động, trầm cảm, loạn thần - đặc biệt liều cao)",
            "Dấu hiệu Cushing (tăng cân, mặt tròn, tích mỡ)",
            "Mật độ xương nếu dùng lâu dài"
        ],
        "precautions": [
            "GIẢM DẦN liều khi ngừng (tránh suy thượng thận cấp)",
            "Không ngừng đột ngột nếu dùng >2 tuần",
            "Dùng liều thấp nhất hiệu quả, thời gian ngắn nhất có thể",
            "Cân nhắc bổ sung canxi, vitamin D, bisphosphonate nếu dùng lâu dài",
            "Theo dõi sát dấu hiệu nhiễm trùng (có thể che dấu triệu chứng)",
            "Cân nhắc dùng PPI khi dùng liều cao hoặc kéo dài (giảm nguy cơ loét)",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Thận trọng ở bệnh nhân tăng huyết áp, suy tim (giữ nước)",
            "IV pulse therapy (250-1000mg) chỉ dùng cho bệnh nặng, cần theo dõi sát"
        ],
        "pharmacokinetics": {
            "half_life": "18-36 giờ (dài)",
            "onset": "Vài giờ (PO), nhanh (IV)",
            "duration": "24-36 giờ",
            "protein_binding": "77% (gắn với transcortin và albumin)",
            "clearance": "Gan (chuyển hóa qua CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản theo hướng dẫn nhà sản xuất",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ketoconazole, Itraconazole (Azole antifungals)",
                    "mechanism": "Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa methylprednisolone, tăng nồng độ và tác dụng.",
                    "effect": "Tăng nồng độ methylprednisolone, tăng tác dụng và tác dụng phụ (Cushing, tăng đường huyết, ức chế miễn dịch)",
                    "management": "Giảm liều methylprednisolone 25-50% khi dùng với azole antifungals. Theo dõi đường huyết, dấu hiệu Cushing."
                },
                {
                    "drug": "Rifampin, Rifabutin",
                    "mechanism": "Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa methylprednisolone, giảm nồng độ và hiệu quả.",
                    "effect": "Giảm nồng độ methylprednisolone, giảm hiệu quả điều trị",
                    "management": "Tăng liều methylprednisolone 25-50% khi dùng với rifampin. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Corticosteroid có thể thay đổi chuyển hóa warfarin và ảnh hưởng đến đông máu.",
                    "effect": "Thay đổi INR (có thể tăng hoặc giảm), tăng nguy cơ chảy máu hoặc huyết khối",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng methylprednisolone. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAID (Ibuprofen, Naproxen, Diclofenac)",
                    "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.",
                    "effect": "Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa nghiêm trọng",
                    "management": "Cân nhắc dùng PPI hoặc misoprostol. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu chảy máu dạ dày."
                },
                {
                    "drug": "Phenytoin, Phenobarbital, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa, tăng chuyển hóa methylprednisolone.",
                    "effect": "Giảm nồng độ methylprednisolone, giảm hiệu quả",
                    "management": "Tăng liều methylprednisolone. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cả hai đều ức chế miễn dịch, tác dụng cộng dồn. Có thể ảnh hưởng đến chuyển hóa.",
                    "effect": "Tăng ức chế miễn dịch, tăng nguy cơ nhiễm trùng, tăng nguy cơ độc tính",
                    "management": "Giảm liều cả hai thuốc. Theo dõi chức năng thận, dấu hiệu nhiễm trùng."
                }
            ],
            "minor": [
                {
                    "drug": "Diuretics (Thiazide, Furosemide)",
                    "mechanism": "Corticosteroid gây giữ natri, có thể đối kháng tác dụng lợi tiểu.",
                    "effect": "Giảm hiệu quả lợi tiểu, có thể gây giữ nước",
                    "management": "Theo dõi cân nặng, dấu hiệu giữ nước. Có thể cần điều chỉnh liều lợi tiểu."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Nhiễm nấm hệ thống không điều trị (cryptococcosis, histoplasmosis, coccidioidomycosis) - corticosteroid làm nặng nhiễm nấm",
                "Dị ứng methylprednisolone hoặc các corticosteroid khác",
                "Nhiễm virus hoạt động (herpes simplex keratitis, varicella zoster lan tỏa) - trừ khi chỉ định đặc biệt"
            ],
            "relative": [
                "Nhiễm trùng đang hoạt động - có thể làm nặng, che dấu triệu chứng",
                "Đái tháo đường - tăng đường huyết, cần theo dõi và điều chỉnh",
                "Tăng huyết áp - có thể tăng huyết áp, giữ nước",
                "Suy tim - giữ nước, có thể làm nặng",
                "Loãng xương - tăng nguy cơ gãy xương",
                "Loét dạ dày tá tràng - tăng nguy cơ loét",
                "Rối loạn tâm thần - có thể làm nặng",
                "Glaucoma - có thể tăng nhãn áp",
                "Có thai - có thể ảnh hưởng đến thai nhi",
                "Suy gan - có thể giảm chuyển hóa",
                "Suy thận - không cần điều chỉnh liều nhưng thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Methylprednisolone là thuốc phân loại C. Corticosteroid có thể đi qua nhau thai và có thể ảnh hưởng đến thai nhi. Dùng lâu dài hoặc liều cao trong thai kỳ có thể gây ức chế thượng thận ở trẻ sơ sinh, chậm phát triển, tăng nguy cơ sứt môi/vòm miệng (khi dùng trong tam cá nguyệt đầu), và các tác dụng phụ khác. Tuy nhiên, corticosteroid được sử dụng trong thai kỳ để điều trị một số bệnh tự miễn và hen phế quản. Nên dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Tránh dùng liều cao kéo dài trong thai kỳ nếu có thể.",
            "lactation": {
                "safety": "Compatible (với dùng ngắn hạn)",
                "details": "Methylprednisolone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ với liều thường dùng. Với liều cao hoặc kéo dài, có thể ảnh hưởng đến trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với liều điều trị tiêu chuẩn. Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Methylprednisolone chuyển hóa qua gan nhưng không phụ thuộc nhiều vào chức năng gan.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng thời gian bán thải.",
            "notes": "Methylprednisolone chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng có thể làm giảm chuyển hóa, tăng thời gian bán thải, tăng nồng độ và tác dụng. Theo dõi tác dụng phụ chặt chẽ ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng Cushing: Tăng cân, mặt tròn, tích mỡ, bướu trâu, vết rạn da, tăng huyết áp",
                "Triệu chứng chuyển hóa: Tăng đường huyết nghiêm trọng, toan chuyển hóa, hạ kali máu",
                "Triệu chứng tiêu hóa: Loét dạ dày, xuất huyết tiêu hóa, thủng dạ dày",
                "Triệu chứng thần kinh: Kích động, loạn thần, trầm cảm, co giật, hôn mê",
                "Triệu chứng miễn dịch: Nhiễm trùng nghiêm trọng (do ức chế miễn dịch), che dấu triệu chứng nhiễm trùng",
                "Triệu chứng tim mạch: Suy tim, phù, giữ nước, tăng huyết áp nặng",
                "Triệu chứng nghiêm trọng: Suy thượng thận cấp (khi ngừng đột ngột sau dùng lâu dài), sốc, tử vong"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay methylprednisolone nếu có thể (nhưng KHÔNG ngừng đột ngột nếu đã dùng >2 tuần - phải giảm dần)",
                "Nếu ngừng đột ngột sau dùng lâu dài:",
                "  - Bắt đầu lại corticosteroid ngay (hydrocortisone 100mg IV mỗi 6-8 giờ)",
                "  - Giảm dần liều theo thời gian",
                "Điều trị tăng đường huyết:",
                "  - Theo dõi đường huyết thường xuyên",
                "  - Insulin nếu cần",
                "  - Điều chỉnh liều đái tháo đường",
                "Điều trị loét dạ dày/xuất huyết tiêu hóa:",
                "  - PPI (omeprazole, pantoprazole)",
                "  - Truyền máu nếu cần",
                "  - Nội soi dạ dày nếu nghi ngờ thủng",
                "Điều trị rối loạn tâm thần:",
                "  - An thần nếu kích động, loạn thần",
                "  - Antipsychotic nếu cần",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị nhiễm trùng:",
                "  - Kháng sinh nếu có nhiễm trùng",
                "  - Theo dõi dấu hiệu nhiễm trùng (có thể che dấu)",
                "Điều chỉnh điện giải:",
                "  - Bổ sung kali nếu hạ kali máu",
                "  - Điều chỉnh natri nếu cần",
                "Hỗ trợ huyết động:",
                "  - Truyền dịch nếu cần",
                "  - Thuốc vận mạch nếu sốc",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, đường huyết"
            ],
            "monitoring": "Theo dõi đường huyết, điện giải, dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu loét dạ dày, tâm thần trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng. Nếu ngừng đột ngột sau dùng lâu dài, theo dõi dấu hiệu suy thượng thận cấp trong ít nhất 1-2 tuần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.",
                "timing": "Uống 1-4 lần/ngày tùy chỉ định. Có thể uống buổi sáng (để giảm ảnh hưởng đến giấc ngủ) hoặc chia đều trong ngày. Với liều cao, chia nhiều lần. Với liều thấp, có thể uống 1 lần buổi sáng."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1-5mg/ml. Pha 125mg trong 50ml dịch = 2.5mg/ml. Pha 500mg trong 100ml dịch = 5mg/ml. Pha 1g trong 250ml dịch = 4mg/ml.",
                "infusion_rate": "Truyền trong 15-60 phút tùy liều. Liều thấp (40-125mg): truyền trong 15-30 phút. Liều cao (250-1000mg): truyền trong 30-60 phút. Không truyền quá nhanh. Tốc độ: 50ml/30 phút = ~1.7ml/phút. 100ml/60 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với thuốc có tính kiềm hoặc axit."],
                "notes": "IV pulse therapy (250-1000mg) chỉ dùng cho bệnh nặng, cần theo dõi sát. Theo dõi đường huyết, huyết áp, điện giải trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Methylprednisolone (Medrol)",
                "UpToDate - Methylprednisolone: Drug Information",
                "Medscape - Methylprednisolone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Methylprednisolone Monograph",
                "Micromedex - Methylprednisolone Drug Information",
                "Endocrine Society Guidelines - Corticosteroid Use"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Hydrocortisone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Hydrocortisone, Cortef",
        "administration": ["PO", "IV", "IM", "Topical"],
        "indications": [
            "Suy thượng thận",
            "Phản ứng dị ứng nặng",
            "Sốc phản vệ (kết hợp)",
            "Viêm khớp",
            "Bệnh Addison",
            "Phù não"
        ],
        "contraindications": [
            "Nhiễm nấm hệ thống không điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_replacement": "15-25mg/ngày (20mg buổi sáng, 10mg buổi tối)",
            "adult_stress": "50-100mg IV mỗi 6-8 giờ",
            "adult_shock": "100mg IV x 1 lần, sau đó 50-100mg mỗi 6 giờ",
            "adult_antiinflammatory": "20-240mg/ngày",
            "notes": "Glucocorticoid tự nhiên, tác dụng ngắn"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Giữ natri, phù",
            "Loét dạ dày",
            "Ức chế miễn dịch"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Glucocorticoid tự nhiên (cortisol), tác dụng ngắn. Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm, ức chế phospholipase A2. Có tác dụng mineralocorticoid (giữ natri, thải kali) - mạnh hơn dexamethasone. Được dùng trong suy thượng thận để thay thế cortisol thiếu hụt. Tác dụng chống viêm và ức chế miễn dịch yếu hơn dexamethasone nhưng có tác dụng mineralocorticoid.",
        "monitoring": [
            "Đường huyết (tăng đường huyết)",
            "Huyết áp (tăng huyết áp, đặc biệt do giữ natri)",
            "Điện giải (natri, kali - giữ natri, thải kali)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Dạ dày (dấu hiệu loét, xuất huyết)",
            "Dấu hiệu suy thượng thận nếu ngừng đột ngột (mệt mỏi, hạ huyết áp, hạ natri máu)",
            "Dấu hiệu Cushing nếu dùng liều cao kéo dài",
            "Xương (loãng xương nếu dùng kéo dài)"
        ],
        "precautions": [
            "Trong suy thượng thận: KHÔNG được quên liều hoặc ngừng đột ngột (có thể gây suy thượng thận cấp - nguy hiểm tính mạng)",
            "Tăng liều trong stress (phẫu thuật, nhiễm trùng nặng) - cần tăng gấp 2-3 lần liều thay thế",
            "Giữ natri mạnh hơn dexamethasone → cần theo dõi natri, kali",
            "Không dùng trong nhiễm nấm hệ thống không điều trị",
            "Thận trọng ở bệnh nhân suy tim (giữ natri → phù)",
            "Thận trọng ở bệnh nhân tăng huyết áp (giữ natri → tăng huyết áp)",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Dùng với thức ăn để giảm kích ứng dạ dày",
            "Thời gian bán thải ngắn → cần chia liều trong ngày (2-3 lần/ngày) cho thay thế",
            "Trong stress dosing: dùng liều cao IV mỗi 6-8 giờ"
        ],
        "pharmacokinetics": {
            "half_life": "8-12 giờ",
            "onset": "IV: 1 giờ; PO: 1-2 giờ",
            "duration": "8-12 giờ",
            "protein_binding": "90-95% (cao)",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng bột pha tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, trong suy thượng thận, quên liều hoặc ngừng đột ngột có thể gây suy thượng thận cấp, có thể tử vong. Trong stress, không tăng liều có thể dẫn đến suy thượng thận cấp.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ketoconazole, Itraconazole (Azole antifungals)",
                    "mechanism": "Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa hydrocortisone, tăng nồng độ và tác dụng.",
                    "effect": "Tăng nồng độ hydrocortisone, tăng tác dụng và tác dụng phụ (Cushing, tăng đường huyết, ức chế miễn dịch)",
                    "management": "Giảm liều hydrocortisone 25-50% khi dùng với azole antifungals. Theo dõi đường huyết, dấu hiệu Cushing."
                },
                {
                    "drug": "Rifampin, Rifabutin",
                    "mechanism": "Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa hydrocortisone, giảm nồng độ và hiệu quả.",
                    "effect": "Giảm nồng độ hydrocortisone, giảm hiệu quả điều trị - đặc biệt nguy hiểm trong suy thượng thận",
                    "management": "Tăng liều hydrocortisone 25-50% khi dùng với rifampin. Trong suy thượng thận, cần tăng liều thay thế. Theo dõi dấu hiệu suy thượng thận."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Corticosteroid có thể thay đổi chuyển hóa warfarin và ảnh hưởng đến đông máu.",
                    "effect": "Thay đổi INR (có thể tăng hoặc giảm), tăng nguy cơ chảy máu hoặc huyết khối",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng hydrocortisone. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAID (Ibuprofen, Naproxen, Diclofenac)",
                    "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.",
                    "effect": "Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa nghiêm trọng",
                    "management": "Cân nhắc dùng PPI hoặc misoprostol. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu chảy máu dạ dày."
                },
                {
                    "drug": "Phenytoin, Phenobarbital, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa, tăng chuyển hóa hydrocortisone.",
                    "effect": "Giảm nồng độ hydrocortisone, giảm hiệu quả - đặc biệt nguy hiểm trong suy thượng thận",
                    "management": "Tăng liều hydrocortisone. Trong suy thượng thận, cần tăng liều thay thế. Theo dõi dấu hiệu suy thượng thận."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cả hai đều ức chế miễn dịch, tác dụng cộng dồn. Có thể ảnh hưởng đến chuyển hóa.",
                    "effect": "Tăng ức chế miễn dịch, tăng nguy cơ nhiễm trùng, tăng nguy cơ độc tính",
                    "management": "Giảm liều cả hai thuốc. Theo dõi chức năng thận, dấu hiệu nhiễm trùng."
                }
            ],
            "minor": [
                {
                    "drug": "Diuretics (Thiazide, Furosemide)",
                    "mechanism": "Hydrocortisone có tác dụng mineralocorticoid mạnh (giữ natri), có thể đối kháng tác dụng lợi tiểu.",
                    "effect": "Giảm hiệu quả lợi tiểu, có thể gây giữ nước, tăng mất kali",
                    "management": "Theo dõi cân nặng, dấu hiệu giữ nước, kali máu. Có thể cần điều chỉnh liều lợi tiểu, bổ sung kali."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Nhiễm nấm hệ thống không điều trị (cryptococcosis, histoplasmosis, coccidioidomycosis) - corticosteroid làm nặng nhiễm nấm",
                "Dị ứng hydrocortisone hoặc các corticosteroid khác",
                "Nhiễm virus hoạt động (herpes simplex keratitis, varicella zoster lan tỏa) - trừ khi chỉ định đặc biệt"
            ],
            "relative": [
                "Nhiễm trùng đang hoạt động - có thể làm nặng, che dấu triệu chứng",
                "Đái tháo đường - tăng đường huyết, cần theo dõi và điều chỉnh",
                "Tăng huyết áp - có thể tăng huyết áp, giữ nước (do tác dụng mineralocorticoid)",
                "Suy tim - giữ nước, có thể làm nặng (đặc biệt do tác dụng mineralocorticoid)",
                "Loãng xương - tăng nguy cơ gãy xương",
                "Loét dạ dày tá tràng - tăng nguy cơ loét",
                "Rối loạn tâm thần - có thể làm nặng",
                "Glaucoma - có thể tăng nhãn áp",
                "Có thai - có thể ảnh hưởng đến thai nhi",
                "Suy gan - có thể giảm chuyển hóa",
                "Suy thận - không cần điều chỉnh liều nhưng thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Hydrocortisone là thuốc phân loại C. Corticosteroid có thể đi qua nhau thai và có thể ảnh hưởng đến thai nhi. Dùng lâu dài hoặc liều cao trong thai kỳ có thể gây ức chế thượng thận ở trẻ sơ sinh, chậm phát triển, tăng nguy cơ sứt môi/vòm miệng (khi dùng trong tam cá nguyệt đầu), và các tác dụng phụ khác. Tuy nhiên, hydrocortisone được sử dụng trong thai kỳ để điều trị suy thượng thận và một số bệnh tự miễn. Nên dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Trong suy thượng thận, cần tiếp tục điều trị nhưng với liều thấp nhất hiệu quả.",
            "lactation": {
                "safety": "Compatible (với dùng ngắn hạn)",
                "details": "Hydrocortisone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ với liều thay thế thông thường. Với liều cao hoặc kéo dài, có thể ảnh hưởng đến trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với liều thay thế tiêu chuẩn (15-25mg/ngày). Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Hydrocortisone chuyển hóa qua gan nhưng không phụ thuộc nhiều vào chức năng gan.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình. Trong suy thượng thận, cần theo dõi dấu hiệu suy thượng thận.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng thời gian bán thải. Trong suy thượng thận, cần theo dõi dấu hiệu suy thượng thận chặt chẽ.",
            "notes": "Hydrocortisone chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng có thể làm giảm chuyển hóa, tăng thời gian bán thải, tăng nồng độ và tác dụng. Theo dõi tác dụng phụ chặt chẽ ở bệnh nhân suy gan. Trong suy thượng thận, không được giảm liều quá mức - cần cân bằng giữa điều chỉnh liều và đảm bảo đủ liều thay thế."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng Cushing: Tăng cân, mặt tròn, tích mỡ, bướu trâu, vết rạn da, tăng huyết áp",
                "Triệu chứng chuyển hóa: Tăng đường huyết nghiêm trọng, toan chuyển hóa, hạ kali máu (do tác dụng mineralocorticoid)",
                "Triệu chứng tiêu hóa: Loét dạ dày, xuất huyết tiêu hóa, thủng dạ dày",
                "Triệu chứng thần kinh: Kích động, loạn thần, trầm cảm, co giật, hôn mê",
                "Triệu chứng miễn dịch: Nhiễm trùng nghiêm trọng (do ức chế miễn dịch), che dấu triệu chứng nhiễm trùng",
                "Triệu chứng tim mạch: Suy tim, phù, giữ nước, tăng huyết áp nặng (đặc biệt do tác dụng mineralocorticoid)",
                "Triệu chứng nghiêm trọng: Suy thượng thận cấp (khi ngừng đột ngột sau dùng lâu dài hoặc quên liều trong suy thượng thận), sốc, tử vong"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay hydrocortisone nếu có thể (nhưng KHÔNG ngừng đột ngột nếu đã dùng >2 tuần hoặc trong suy thượng thận - phải giảm dần)",
                "Nếu ngừng đột ngột sau dùng lâu dài hoặc quên liều trong suy thượng thận:",
                "  - Bắt đầu lại corticosteroid ngay (hydrocortisone 100mg IV mỗi 6-8 giờ)",
                "  - Giảm dần liều theo thời gian",
                "Điều trị tăng đường huyết:",
                "  - Theo dõi đường huyết thường xuyên",
                "  - Insulin nếu cần",
                "  - Điều chỉnh liều đái tháo đường",
                "Điều trị loét dạ dày/xuất huyết tiêu hóa:",
                "  - PPI (omeprazole, pantoprazole)",
                "  - Truyền máu nếu cần",
                "  - Nội soi dạ dày nếu nghi ngờ thủng",
                "Điều trị rối loạn tâm thần:",
                "  - An thần nếu kích động, loạn thần",
                "  - Antipsychotic nếu cần",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị nhiễm trùng:",
                "  - Kháng sinh nếu có nhiễm trùng",
                "  - Theo dõi dấu hiệu nhiễm trùng (có thể che dấu)",
                "Điều chỉnh điện giải (đặc biệt quan trọng với hydrocortisone do tác dụng mineralocorticoid):",
                "  - Bổ sung kali nếu hạ kali máu",
                "  - Điều chỉnh natri nếu cần (có thể giữ natri)",
                "  - Theo dõi cân nặng, dấu hiệu giữ nước",
                "Hỗ trợ huyết động:",
                "  - Truyền dịch nếu cần",
                "  - Thuốc vận mạch nếu sốc",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, đường huyết"
            ],
            "monitoring": "Theo dõi đường huyết, điện giải (đặc biệt natri, kali), dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu loét dạ dày, tâm thần trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng. Nếu ngừng đột ngột sau dùng lâu dài hoặc quên liều trong suy thượng thận, theo dõi dấu hiệu suy thượng thận cấp trong ít nhất 1-2 tuần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.",
                "timing": "Với liều thay thế: uống 2-3 lần/ngày (ví dụ: 20mg buổi sáng, 10mg buổi tối). Với liều chống viêm: uống 1-4 lần/ngày tùy chỉ định. Có thể uống buổi sáng (để giảm ảnh hưởng đến giấc ngủ) hoặc chia đều trong ngày."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1-5mg/ml. Pha 100mg trong 50ml dịch = 2mg/ml. Pha 250mg trong 100ml dịch = 2.5mg/ml.",
                "infusion_rate": "Truyền trong 15-30 phút. Không truyền quá nhanh. Tốc độ: 50ml/30 phút = ~1.7ml/phút. 100ml/30 phút = ~3.3ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với thuốc có tính kiềm hoặc axit."],
                "notes": "Trong stress dosing (phẫu thuật, nhiễm trùng nặng): dùng 50-100mg IV mỗi 6-8 giờ. Trong sốc: 100mg IV x 1 lần, sau đó 50-100mg mỗi 6 giờ. Theo dõi đường huyết, huyết áp, điện giải trong quá trình truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Hydrocortisone (Cortef)",
                "UpToDate - Hydrocortisone: Drug Information",
                "Medscape - Hydrocortisone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Hydrocortisone Monograph",
                "Micromedex - Hydrocortisone Drug Information",
                "Endocrine Society Guidelines - Adrenal Insufficiency Management"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Betamethasone": {
        "group": "Endocrinology - Corticosteroid",
        "vietnamese_name": "Betamethasone, Celestone",
        "administration": ["PO", "IV", "IM", "Topical"],
        "indications": [
            "Viêm khớp dạng thấp",
            "Hen phế quản",
            "Bệnh tự miễn",
            "Viêm da",
            "Thúc đẩy trưởng thành phổi thai nhi (IM)"
        ],
        "contraindications": [
            "Nhiễm nấm hệ thống không điều trị",
            "Dị ứng"
        ],
        "dosage": {
            "adult_po": "0.6-7.2mg/ngày chia 1-4 lần",
            "adult_im": "0.5-9mg IM",
            "fetal_lung_maturation": "12mg IM x 2 lần cách 24 giờ (cho mẹ)",
            "notes": "Tác dụng dài, ức chế mạnh"
        },
        "side_effects": [
            "Tăng đường huyết",
            "Tăng huyết áp",
            "Loãng xương",
            "Ức chế miễn dịch",
            "Tăng cân",
            "Loét dạ dày"
        ],
        "interactions": [
            "Warfarin: thay đổi tác dụng chống đông",
            "NSAID: tăng nguy cơ loét dạ dày"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Glucocorticoid tổng hợp tác dụng dài và mạnh (tương đương 25-30mg hydrocortisone, mạnh hơn dexamethasone một chút). Gắn với glucocorticoid receptor trong tế bào, điều hòa biểu hiện gen, ức chế tổng hợp các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm di chuyển bạch cầu đến vị trí viêm. Ức chế miễn dịch mạnh. Có tác dụng mineralocorticoid tối thiểu (ít hơn hydrocortisone và dexamethasone). Được dùng trong nhiều tình trạng viêm và tự miễn. Thường dùng để thúc đẩy trưởng thành phổi ở thai nhi (khi có nguy cơ sinh non).",
        "monitoring": [
            "Đường huyết (tăng đường huyết)",
            "Huyết áp (tăng huyết áp)",
            "Điện giải (natri, kali)",
            "Dấu hiệu nhiễm trùng (ức chế miễn dịch)",
            "Dạ dày (dấu hiệu loét)",
            "Tâm thần (rối loạn tâm thần)",
            "Xương (loãng xương nếu dùng kéo dài)",
            "Mắt (tăng nhãn áp, đục thủy tinh thể)",
            "Trong thai kỳ: theo dõi thai nhi nếu dùng để thúc đẩy trưởng thành phổi"
        ],
        "precautions": [
            "KHÔNG được ngừng đột ngột nếu dùng > 1 tuần (có thể gây suy thượng thận cấp)",
            "Phải giảm liều dần dần (tapering) nếu dùng > 1 tuần",
            "Ức chế miễn dịch mạnh - tăng nguy cơ nhiễm trùng",
            "Không dùng trong nhiễm nấm hệ thống không điều trị",
            "Thận trọng ở bệnh nhân đái tháo đường (tăng đường huyết)",
            "Thận trọng ở bệnh nhân loét dạ dày",
            "Dùng với thức ăn để giảm kích ứng dạ dày",
            "Dự phòng loãng xương nếu dùng kéo dài",
            "Trong thai kỳ: có thể dùng để thúc đẩy trưởng thành phổi (24-34 tuần) nhưng thận trọng",
            "Theo dõi dấu hiệu nhiễm trùng"
        ],
        "pharmacokinetics": {
            "half_life": "36-54 giờ (rất dài)",
            "onset": "1-2 giờ (PO/IM)",
            "duration": "36-54 giờ",
            "protein_binding": "64% (thấp hơn hydrocortisone)",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan, không cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ngừng đột ngột sau khi dùng kéo dài có thể gây suy thượng thận cấp, có thể tử vong. Ức chế miễn dịch mạnh có thể làm nặng nhiễm trùng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ketoconazole, Itraconazole (Azole antifungals)",
                    "mechanism": "Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa betamethasone, tăng nồng độ và tác dụng.",
                    "effect": "Tăng nồng độ betamethasone, tăng tác dụng và tác dụng phụ (Cushing, tăng đường huyết, ức chế miễn dịch)",
                    "management": "Giảm liều betamethasone 25-50% khi dùng với azole antifungals. Theo dõi đường huyết, dấu hiệu Cushing."
                },
                {
                    "drug": "Rifampin, Rifabutin",
                    "mechanism": "Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa betamethasone, giảm nồng độ và hiệu quả.",
                    "effect": "Giảm nồng độ betamethasone, giảm hiệu quả điều trị",
                    "management": "Tăng liều betamethasone 25-50% khi dùng với rifampin. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Corticosteroid có thể thay đổi chuyển hóa warfarin và ảnh hưởng đến đông máu.",
                    "effect": "Thay đổi INR (có thể tăng hoặc giảm), tăng nguy cơ chảy máu hoặc huyết khối",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng betamethasone. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "NSAID (Ibuprofen, Naproxen, Diclofenac)",
                    "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.",
                    "effect": "Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa nghiêm trọng",
                    "management": "Cân nhắc dùng PPI hoặc misoprostol. Tránh dùng đồng thời nếu có thể. Theo dõi dấu hiệu chảy máu dạ dày."
                },
                {
                    "drug": "Phenytoin, Phenobarbital, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa, tăng chuyển hóa betamethasone.",
                    "effect": "Giảm nồng độ betamethasone, giảm hiệu quả",
                    "management": "Tăng liều betamethasone. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cả hai đều ức chế miễn dịch, tác dụng cộng dồn. Có thể ảnh hưởng đến chuyển hóa.",
                    "effect": "Tăng ức chế miễn dịch, tăng nguy cơ nhiễm trùng, tăng nguy cơ độc tính",
                    "management": "Giảm liều cả hai thuốc. Theo dõi chức năng thận, dấu hiệu nhiễm trùng."
                }
            ],
            "minor": [
                {
                    "drug": "Diuretics (Thiazide, Furosemide)",
                    "mechanism": "Corticosteroid gây giữ natri, có thể đối kháng tác dụng lợi tiểu.",
                    "effect": "Giảm hiệu quả lợi tiểu, có thể gây giữ nước",
                    "management": "Theo dõi cân nặng, dấu hiệu giữ nước. Có thể cần điều chỉnh liều lợi tiểu."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Nhiễm nấm hệ thống không điều trị (cryptococcosis, histoplasmosis, coccidioidomycosis) - corticosteroid làm nặng nhiễm nấm",
                "Dị ứng betamethasone hoặc các corticosteroid khác",
                "Nhiễm virus hoạt động (herpes simplex keratitis, varicella zoster lan tỏa) - trừ khi chỉ định đặc biệt"
            ],
            "relative": [
                "Nhiễm trùng đang hoạt động - có thể làm nặng, che dấu triệu chứng",
                "Đái tháo đường - tăng đường huyết, cần theo dõi và điều chỉnh",
                "Tăng huyết áp - có thể tăng huyết áp, giữ nước",
                "Suy tim - giữ nước, có thể làm nặng",
                "Loãng xương - tăng nguy cơ gãy xương",
                "Loét dạ dày tá tràng - tăng nguy cơ loét",
                "Rối loạn tâm thần - có thể làm nặng",
                "Glaucoma - có thể tăng nhãn áp",
                "Có thai - có thể ảnh hưởng đến thai nhi (nhưng có thể dùng để thúc đẩy trưởng thành phổi)",
                "Suy gan - có thể giảm chuyển hóa",
                "Suy thận - không cần điều chỉnh liều nhưng thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Betamethasone là thuốc phân loại C. Corticosteroid có thể đi qua nhau thai và có thể ảnh hưởng đến thai nhi. Dùng lâu dài hoặc liều cao trong thai kỳ có thể gây ức chế thượng thận ở trẻ sơ sinh, chậm phát triển, tăng nguy cơ sứt môi/vòm miệng (khi dùng trong tam cá nguyệt đầu), và các tác dụng phụ khác. Tuy nhiên, betamethasone được sử dụng trong thai kỳ để thúc đẩy trưởng thành phổi ở thai nhi (khi có nguy cơ sinh non, 24-34 tuần). Liều thường dùng: 12mg IM x 2 lần cách 24 giờ cho mẹ. Nên dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Tránh dùng liều cao kéo dài trong thai kỳ nếu không cần thiết.",
            "lactation": {
                "safety": "Compatible (với dùng ngắn hạn)",
                "details": "Betamethasone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ với liều thường dùng. Với liều cao hoặc kéo dài, có thể ảnh hưởng đến trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với liều điều trị tiêu chuẩn. Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Betamethasone chuyển hóa qua gan nhưng không phụ thuộc nhiều vào chức năng gan.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng thời gian bán thải.",
            "notes": "Betamethasone chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan nặng có thể làm giảm chuyển hóa, tăng thời gian bán thải, tăng nồng độ và tác dụng. Theo dõi tác dụng phụ chặt chẽ ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng Cushing: Tăng cân, mặt tròn, tích mỡ, bướu trâu, vết rạn da, tăng huyết áp",
                "Triệu chứng chuyển hóa: Tăng đường huyết nghiêm trọng, toan chuyển hóa, hạ kali máu",
                "Triệu chứng tiêu hóa: Loét dạ dày, xuất huyết tiêu hóa, thủng dạ dày",
                "Triệu chứng thần kinh: Kích động, loạn thần, trầm cảm, co giật, hôn mê",
                "Triệu chứng miễn dịch: Nhiễm trùng nghiêm trọng (do ức chế miễn dịch), che dấu triệu chứng nhiễm trùng",
                "Triệu chứng tim mạch: Suy tim, phù, giữ nước, tăng huyết áp nặng",
                "Triệu chứng nghiêm trọng: Suy thượng thận cấp (khi ngừng đột ngột sau dùng lâu dài), sốc, tử vong"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay betamethasone nếu có thể (nhưng KHÔNG ngừng đột ngột nếu đã dùng >2 tuần - phải giảm dần)",
                "Nếu ngừng đột ngột sau dùng lâu dài:",
                "  - Bắt đầu lại corticosteroid ngay (hydrocortisone 100mg IV mỗi 6-8 giờ)",
                "  - Giảm dần liều theo thời gian",
                "Điều trị tăng đường huyết:",
                "  - Theo dõi đường huyết thường xuyên",
                "  - Insulin nếu cần",
                "  - Điều chỉnh liều đái tháo đường",
                "Điều trị loét dạ dày/xuất huyết tiêu hóa:",
                "  - PPI (omeprazole, pantoprazole)",
                "  - Truyền máu nếu cần",
                "  - Nội soi dạ dày nếu nghi ngờ thủng",
                "Điều trị rối loạn tâm thần:",
                "  - An thần nếu kích động, loạn thần",
                "  - Antipsychotic nếu cần",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị nhiễm trùng:",
                "  - Kháng sinh nếu có nhiễm trùng",
                "  - Theo dõi dấu hiệu nhiễm trùng (có thể che dấu)",
                "Điều chỉnh điện giải:",
                "  - Bổ sung kali nếu hạ kali máu",
                "  - Điều chỉnh natri nếu cần",
                "Hỗ trợ huyết động:",
                "  - Truyền dịch nếu cần",
                "  - Thuốc vận mạch nếu sốc",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, đường huyết"
            ],
            "monitoring": "Theo dõi đường huyết, điện giải, dấu hiệu sinh tồn, dấu hiệu nhiễm trùng, dấu hiệu loét dạ dày, tâm thần trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng. Nếu ngừng đột ngột sau dùng lâu dài, theo dõi dấu hiệu suy thượng thận cấp trong ít nhất 1-2 tuần."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.",
                "timing": "Uống 1-4 lần/ngày tùy chỉ định. Có thể uống buổi sáng (để giảm ảnh hưởng đến giấc ngủ) hoặc chia đều trong ngày. Với liều cao, chia nhiều lần. Với liều thấp, có thể uống 1 lần buổi sáng."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1-5mg/ml. Pha 4mg trong 50ml dịch = 0.08mg/ml.",
                "infusion_rate": "Truyền trong 15-30 phút. Không truyền quá nhanh. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với thuốc có tính kiềm hoặc axit."],
                "notes": "Theo dõi đường huyết, huyết áp, điện giải trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần."
            },
            "im": {
                "notes": "Betamethasone có thể dùng IM. Liều thúc đẩy trưởng thành phổi: 12mg IM x 2 lần cách 24 giờ (cho mẹ, 24-34 tuần thai). Tiêm vào cơ delta hoặc cơ mông. Theo dõi phản ứng tại chỗ tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Betamethasone (Celestone)",
                "UpToDate - Betamethasone: Drug Information",
                "Medscape - Betamethasone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Betamethasone Monograph",
                "Micromedex - Betamethasone Drug Information",
                "ACOG Guidelines - Antenatal Corticosteroid Therapy for Fetal Maturation",
                "Endocrine Society Guidelines - Corticosteroid Use"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
"Azithromycin": {
        "group": "Infectious Disease - Macrolide Antibiotic",
        "vietnamese_name": "Azithromycin, Zithromax",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường hô hấp trên (viêm họng, viêm xoang)",
            "Nhiễm trùng đường hô hấp dưới (viêm phổi, viêm phế quản)",
            "Nhiễm trùng da và mô mềm",
            "Chlamydia",
            "Nhiễm trùng đường tiết niệu không biến chứng"
        ],
        "contraindications": [
            "Dị ứng azithromycin/macrolide",
            "QT kéo dài",
            "Rối loạn nhịp tim"
        ],
        "dosage": {
            "adult_respiratory": "500mg x 1 lần/ngày x 3 ngày hoặc 500mg ngày đầu, sau đó 250mg x 1 lần/ngày x 4 ngày",
            "adult_chlamydia": "1g x 1 lần (đơn liều)",
            "adult_iv": "500mg x 1 lần/ngày IV",
            "notes": "Tác dụng kéo dài, uống ít lần hơn erythromycin"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn nôn, nôn, tiêu chảy",
            "Đau bụng",
            "QT kéo dài",
            "Loạn nhịp tim (torsades de pointes)",
            "Rối loạn thính giác (hiếm)"
        ],
                  "interactions": [
              "Warfarin: tăng nguy cơ chảy máu",
              "Digoxin: tăng nồng độ digoxin",
              "Cyclosporine: tăng nồng độ cyclosporine",
              "Thuốc QT kéo dài: tăng nguy cơ loạn nhịp"
          ],
          "pregnancy": "B",
          "mechanism_of_action": "Macrolide antibiotic. Ức chế tổng hợp protein vi khuẩn bằng cách gắn vào 50S ribosomal subunit, ức chế peptide chain elongation. Phổ tác dụng: Gram-positive (Streptococcus, Staphylococcus), một số Gram-negative (Haemophilus influenzae), atypical pathogens (Mycoplasma, Chlamydia, Legionella). Có tác dụng kéo dài do thời gian bán hủy dài (68 giờ), cho phép phác đồ ngắn (3-5 ngày).",
          "monitoring": [
              "ECG: QT interval (có thể gây QT kéo dài, đặc biệt ở bệnh nhân có yếu tố nguy cơ)",
              "Triệu chứng rối loạn nhịp tim (torsades de pointes - hiếm nhưng nguy hiểm)",
              "Chức năng gan: ALT, AST (hiếm gây độc gan)",
              "Triệu chứng tiêu hóa: buồn nôn, nôn, tiêu chảy (phổ biến)",
              "Rối loạn thính giác (hiếm, thường ở liều cao hoặc dùng lâu dài)"
          ],
          "precautions": [
              "Tránh dùng ở bệnh nhân QT kéo dài hoặc có yếu tố nguy cơ (suy tim, hạ kali máu, hạ magie máu, dùng thuốc QT kéo dài khác)",
              "Thận trọng khi dùng với warfarin (tăng nguy cơ chảy máu - theo dõi INR)",
              "Thận trọng khi dùng với digoxin (tăng nồng độ digoxin - theo dõi nồng độ)",
              "Thận trọng khi dùng với cyclosporine (tăng nồng độ cyclosporine)",
              "Có thể gây tiêu chảy (phổ biến) - có thể dẫn đến C. difficile colitis nếu nặng",
              "Thận trọng ở bệnh nhân suy gan nặng"
          ],
          "pharmacokinetics": {
              "half_life": "68 giờ (RẤT DÀI - cho phép phác đồ ngắn 3-5 ngày)",
              "onset": "2-3 giờ (PO), 1 giờ (IV)",
              "duration": "5-7 ngày sau liều cuối (do half-life dài)",
              "protein_binding": "7-50% (thay đổi theo nồng độ)",
              "clearance": "Chủ yếu qua phân (không đổi), một phần qua gan. Không phụ thuộc vào chức năng thận (không cần điều chỉnh liều ở suy thận)"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Bảo quản suspension trong tủ lạnh sau khi pha",
          "black_box_warnings": "Có thể gây QT kéo dài và torsades de pointes, đặc biệt ở bệnh nhân có yếu tố nguy cơ (suy tim, hạ kali máu, hạ magie máu, nhịp tim chậm, dùng thuốc QT kéo dài khác). Tránh dùng ở bệnh nhân QT kéo dài",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Warfarin",
                      "mechanism": "Azithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin. Cũng có thể ức chế nhẹ CYP450.",
                      "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                      "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng azithromycin. Điều chỉnh liều warfarin nếu cần."
                  },
                  {
                      "drug": "Digoxin",
                      "mechanism": "Azithromycin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm chuyển hóa digoxin, tăng hấp thu digoxin.",
                      "effect": "Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim, block AV)",
                      "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin nếu cần. Theo dõi ECG."
                  }
              ],
              "moderate": [
                  {
                      "drug": "Cyclosporine, Tacrolimus",
                      "mechanism": "Azithromycin có thể ức chế nhẹ CYP3A4, làm giảm chuyển hóa cyclosporine và tacrolimus.",
                      "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng độc tính (độc thận, tăng huyết áp, độc thần kinh)",
                      "management": "Theo dõi nồng độ cyclosporine/tacrolimus, chức năng thận. Điều chỉnh liều nếu cần."
                  },
                  {
                      "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Antipsychotics)",
                      "mechanism": "Cả hai đều kéo dài QT interval, tác dụng cộng dồn.",
                      "effect": "Tăng nguy cơ QT kéo dài, torsades de pointes, rối loạn nhịp tim nghiêm trọng",
                      "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi ECG chặt chẽ. Đảm bảo kali, magie bình thường. Ngừng ngay nếu QT >500ms hoặc có triệu chứng."
                  }
              ],
              "minor": [
                  {
                      "drug": "Antacids (Aluminum, Magnesium)",
                      "mechanism": "Antacids có thể giảm nhẹ hấp thu azithromycin.",
                      "effect": "Giảm nhẹ hấp thu azithromycin",
                      "management": "Cách 2 giờ nếu có thể. Không ảnh hưởng đáng kể ở liều điều trị thông thường."
                  }
              ]
          },
          "contraindications": {
              "absolute": [
                  "Dị ứng azithromycin hoặc các macrolide khác (erythromycin, clarithromycin)",
                  "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ torsades de pointes",
                  "Dùng với pimozide, terfenadine, astemizole - tăng nguy cơ loạn nhịp tim nghiêm trọng"
              ],
              "relative": [
                  "Suy tim - tăng nguy cơ QT kéo dài, torsades de pointes",
                  "Hạ kali máu, hạ magie máu - tăng nguy cơ QT kéo dài, torsades de pointes",
                  "Nhịp tim chậm - tăng nguy cơ QT kéo dài",
                  "Dùng với thuốc kéo dài QT khác - tác dụng cộng dồn",
                  "Suy gan nặng - thận trọng, có thể giảm chuyển hóa",
                  "Suy thận nặng - thận trọng, mặc dù không cần điều chỉnh liều thường quy"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "B",
              "pregnancy_details": "Azithromycin phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Macrolide là một trong những kháng sinh an toàn nhất trong thai kỳ (sau penicillin). Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng, đặc biệt Chlamydia. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.",
              "lactation": {
                  "safety": "Compatible",
                  "details": "Azithromycin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Macrolide là một trong những kháng sinh an toàn nhất khi cho con bú.",
                  "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban)."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không cần điều chỉnh liều. Azithromycin chuyển hóa một phần qua gan nhưng không đáng kể.",
              "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, nhưng thải trừ chủ yếu qua phân nên ít ảnh hưởng.",
              "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua phân nên ít ảnh hưởng. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần theo dõi chặt chẽ.",
              "notes": "Azithromycin chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua phân (không đổi), một phần qua gan. Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể do thải trừ chủ yếu qua phân. Không cần điều chỉnh liều thường quy ở suy gan."
          },
          "overdose_management": {
              "symptoms": [
                  "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
                  "Triệu chứng tim mạch: QT kéo dài, torsades de pointes, rối loạn nhịp tim (hiếm nhưng nguy hiểm)",
                  "Triệu chứng thần kinh: Đau đầu, chóng mặt, mệt mỏi",
                  "Triệu chứng thính giác: Giảm thính lực, ù tai (hiếm, thường ở liều cao hoặc dùng lâu dài)",
                  "Triệu chứng nghiêm trọng: Torsades de pointes, rối loạn nhịp tim nghiêm trọng, mất thính lực"
              ],
              "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
              "treatment": [
                  "Ngừng ngay azithromycin",
                  "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                  "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
                  "Điều trị triệu chứng tiêu hóa:",
                  "  - Chống nôn nếu cần",
                  "  - Truyền dịch nếu mất nước",
                  "  - Theo dõi điện giải",
                  "Điều trị QT kéo dài/torsades de pointes nếu có:",
                  "  - Theo dõi ECG liên tục",
                  "  - Đảm bảo kali, magie bình thường",
                  "  - Điều trị torsades de pointes: Magnesium sulfate IV, pacing nếu cần",
                  "  - Tránh các thuốc kéo dài QT khác",
                  "Điều trị rối loạn thính giác nếu có:",
                  "  - Ngừng ngay azithromycin",
                  "  - Điều trị hỗ trợ",
                  "  - Có thể không hồi phục",
                  "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG"
              ],
              "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG (QT interval), điện giải (kali, magie), dấu hiệu thính giác trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (QT kéo dài, torsades de pointes, rối loạn thính giác)."
          },
          "reversal_agents": None,
          "administration_instructions": {
              "oral": {
                  "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày và buồn nôn. Có thể uống không thức ăn nếu cần.",
                  "timing": "Uống 1 lần/ngày (phác đồ 3-5 ngày) hoặc theo chỉ định. Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều. Có thể uống trước hoặc sau bữa ăn."
              },
              "iv": {
                  "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.",
                  "infusion_rate": "Truyền IV trong 60 phút (không truyền nhanh hơn). Có thể truyền trong 30 phút nếu cần nhưng không khuyến nghị.",
                  "compatibility": [
                      "NaCl 0.9%",
                      "D5W (Dextrose 5%)",
                      "Nước cất vô trùng"
                  ],
                  "incompatibility": [
                      "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                      "Lactated Ringer's (LR) - không tương thích",
                      "Các dung dịch có cation (Al3+, Mg2+) - có thể tạo phức hợp"
                  ],
                  "notes": "Truyền IV trong 60 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
              }
          },
          "references": {
              "primary_sources": [
                  "FDA Label: Zithromax (azithromycin)",
                  "UpToDate: Azithromycin drug information",
                  "Lexicomp: Azithromycin monograph",
                  "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                  "Sanford Guide to Antimicrobial Therapy"
              ],
              "last_updated": "2025-02-03",
              "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
          }
      },
      "Clarithromycin": {
        "group": "Infectious Disease - Macrolide Antibiotic",
        "vietnamese_name": "Clarithromycin, Klacid",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường hô hấp (viêm phổi, viêm phế quản)",
            "Nhiễm trùng da và mô mềm",
            "Tiệt trừ H. pylori (kết hợp)",
            "Mycobacterium avium complex (MAC)"
        ],
        "contraindications": [
            "Dị ứng clarithromycin/macrolide",
            "QT kéo dài",
            "Dùng pimozide, terfenadine, astemizole"
        ],
        "dosage": {
            "adult_respiratory": "250-500mg x 2 lần/ngày x 7-14 ngày",
            "adult_h_pylori": "500mg x 2 lần/ngày (với amoxicillin + PPI)",
            "adult_mac": "500mg x 2 lần/ngày",
            "notes": "Mạnh hơn azithromycin nhưng nhiều tương tác hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Vị kim loại trong miệng",
            "QT kéo dài",
            "Rối loạn thính giác (hiếm)"
        ],
        "interactions": [
            "CYP3A4 substrates: tăng đáng kể nồng độ (simvastatin, lovastatin, midazolam)",
            "Warfarin: tăng tác dụng chống đông",
            "Digoxin: tăng nồng độ digoxin",
            "Theophylline: tăng nồng độ theophylline"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Clarithromycin là kháng sinh macrolide bán tổng hợp, thuộc nhóm azalide. Ức chế tổng hợp protein của vi khuẩn bằng cách gắn vào tiểu đơn vị 50S của ribosome vi khuẩn, ngăn chặn quá trình dịch mã (translocation) và kéo dài chuỗi peptide. Dẫn đến ngừng tổng hợp protein và ức chế sự phát triển của vi khuẩn. Clarithromycin có phổ kháng khuẩn rộng: Gram-dương (Streptococcus pneumoniae, Staphylococcus aureus - không phải MRSA), một số Gram-âm (H. influenzae, Moraxella catarrhalis), và vi khuẩn không điển hình (Mycoplasma pneumoniae, Chlamydia pneumoniae, Legionella pneumophila). Clarithromycin cũng có tác dụng với Helicobacter pylori và một số vi khuẩn không điển hình khác. Mạnh hơn azithromycin nhưng có nhiều tương tác thuốc hơn do ức chế CYP3A4.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
            "ECG - QT kéo dài (đặc biệt ở bệnh nhân có nguy cơ, dùng với thuốc kéo dài QT khác)",
            "Rối loạn thính giác (giảm thính lực, ù tai) - hiếm nhưng có thể không hồi phục",
            "Chức năng gan (ALT, AST) nếu dùng lâu dài hoặc có triệu chứng",
            "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
            "Tương tác với CYP3A4 substrates (simvastatin, lovastatin, midazolam, warfarin, digoxin, theophylline) - theo dõi tác dụng phụ và nồng độ nếu có"
        ],
        "precautions": [
            "QT kéo dài - không dùng với các thuốc kéo dài QT khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp",
            "Không dùng với pimozide, terfenadine, astemizole (tăng nguy cơ loạn nhịp nghiêm trọng)",
            "Nhiều tương tác thuốc do ức chế CYP3A4 - tăng nồng độ simvastatin, lovastatin (nguy cơ tiêu cơ vân), midazolam, warfarin (tăng INR), digoxin (tăng nồng độ), theophylline (tăng nồng độ)",
            "Giảm liều ở suy thận (CrCl <30: giảm 50-75%)",
            "Uống với thức ăn để giảm buồn nôn, nôn",
            "Rối loạn thính giác - ngừng ngay nếu có giảm thính lực, ù tai (có thể không hồi phục)",
            "Vị kim loại trong miệng - tác dụng phụ phổ biến, thường tự khỏi",
            "Thận trọng ở bệnh nhân có bệnh gan (metabolite qua gan)",
            "Dùng đủ liều và đủ thời gian để tránh kháng thuốc"
        ],
        "pharmacokinetics": {
            "half_life": "3-7 giờ (tăng ở suy thận)",
            "onset": "2-4 giờ",
            "duration": "q12h (dùng 2 lần/ngày)",
            "protein_binding": "70%",
            "clearance": "Gan: chuyển hóa qua CYP3A4 thành 14-hydroxyclarithromycin (metabolite hoạt động, mạnh hơn với H. influenzae). Thận: bài tiết một phần nguyên dạng và metabolites. Cần điều chỉnh liều ở suy thận (CrCl <30)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 14 ngày sau khi pha. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha.",
        "black_box_warnings": "Tăng nguy cơ tử vong do tim mạch ở bệnh nhân có bệnh tim mạch. Không dùng ở bệnh nhân có QT kéo dài, loạn nhịp tim, hoặc dùng với các thuốc kéo dài QT. Tăng nguy cơ tiêu cơ vân khi dùng với simvastatin, lovastatin.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Simvastatin, Lovastatin",
                    "mechanism": "Clarithromycin ức chế mạnh CYP3A4, làm giảm chuyển hóa simvastatin và lovastatin.",
                    "effect": "Tăng nồng độ statin, tăng nguy cơ tiêu cơ vân (myopathy, rhabdomyolysis), suy thận cấp",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều statin hoặc tạm ngừng. Dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4) nếu có thể. Theo dõi CK, dấu hiệu đau cơ."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Clarithromycin ức chế CYP2C9 và CYP3A4, làm giảm chuyển hóa warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng clarithromycin. Giảm liều warfarin 25-50% khi bắt đầu clarithromycin. Điều chỉnh liều warfarin theo INR."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Clarithromycin ức chế P-glycoprotein và ảnh hưởng đến hệ vi khuẩn đường ruột, làm tăng hấp thu và giảm thải trừ digoxin.",
                    "effect": "Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim, block AV)",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin 25-50% khi bắt đầu clarithromycin. Theo dõi ECG."
                },
                {
                    "drug": "Pimozide, Terfenadine, Astemizole",
                    "mechanism": "Clarithromycin ức chế CYP3A4, làm giảm chuyển hóa pimozide, terfenadine, astemizole. Cả hai đều kéo dài QT interval.",
                    "effect": "Tăng nồng độ thuốc, tăng nguy cơ QT kéo dài, torsades de pointes, rối loạn nhịp tim nghiêm trọng, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không dùng đồng thời."
                }
            ],
            "moderate": [
                {
                    "drug": "Midazolam, Triazolam",
                    "mechanism": "Clarithromycin ức chế CYP3A4, làm giảm chuyển hóa benzodiazepine.",
                    "effect": "Tăng nồng độ benzodiazepine, tăng tác dụng an thần, kéo dài thời gian tác dụng",
                    "management": "Giảm liều benzodiazepine 50-75%. Theo dõi dấu hiệu an thần quá mức, suy hô hấp."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Clarithromycin có thể ảnh hưởng đến chuyển hóa theophylline.",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính (buồn nôn, nôn, co giật, rối loạn nhịp tim)",
                    "management": "Theo dõi nồng độ theophylline. Giảm liều theophylline nếu cần. Theo dõi dấu hiệu độc tính."
                },
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Clarithromycin ức chế CYP3A4, làm giảm chuyển hóa cyclosporine và tacrolimus.",
                    "effect": "Tăng nồng độ cyclosporine/tacrolimus, tăng độc tính (độc thận, tăng huyết áp, độc thần kinh)",
                    "management": "Giảm liều cyclosporine/tacrolimus 25-50% khi bắt đầu clarithromycin. Theo dõi nồng độ, chức năng thận. Điều chỉnh liều theo nồng độ."
                },
                {
                    "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Antipsychotics)",
                    "mechanism": "Cả hai đều kéo dài QT interval, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ QT kéo dài, torsades de pointes, rối loạn nhịp tim nghiêm trọng",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi ECG chặt chẽ. Đảm bảo kali, magie bình thường. Ngừng ngay nếu QT >500ms hoặc có triệu chứng."
                }
            ],
            "minor": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Rifampin cảm ứng CYP3A4, làm tăng chuyển hóa clarithromycin.",
                    "effect": "Giảm nồng độ clarithromycin, giảm hiệu quả điều trị",
                    "management": "Tăng liều clarithromycin nếu cần. Theo dõi đáp ứng điều trị."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng clarithromycin hoặc các macrolide khác (erythromycin, azithromycin)",
                "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ tử vong do tim mạch",
                "Dùng với pimozide, terfenadine, astemizole - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI, tăng nguy cơ loạn nhịp tim nghiêm trọng, tử vong",
                "Bệnh tim mạch nặng - tăng nguy cơ tử vong do tim mạch"
            ],
            "relative": [
                "Suy tim - tăng nguy cơ QT kéo dài, tử vong do tim mạch",
                "Hạ kali máu, hạ magie máu - tăng nguy cơ QT kéo dài, torsades de pointes",
                "Dùng với thuốc kéo dài QT khác - tác dụng cộng dồn",
                "Dùng với simvastatin, lovastatin - tăng nguy cơ tiêu cơ vân",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với digoxin - tăng độc tính digoxin",
                "Suy thận nặng (CrCl <30) - cần giảm liều 50-75%",
                "Suy gan - thận trọng, có thể giảm chuyển hóa"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Clarithromycin phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ (giảm cân, chậm phát triển xương). Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh rõ ràng, nhưng dữ liệu còn hạn chế. Macrolide nói chung an toàn hơn nhiều kháng sinh khác trong thai kỳ. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị H. pylori hoặc nhiễm trùng nặng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết. Azithromycin có thể là lựa chọn an toàn hơn trong thai kỳ (phân loại B).",
            "lactation": {
                "safety": "Compatible",
                "details": "Clarithromycin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Macrolide là một trong những kháng sinh an toàn nhất khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Clarithromycin chuyển hóa qua gan nhưng không đáng kể ở suy gan nhẹ.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng nồng độ clarithromycin và nguy cơ tác dụng phụ.",
            "notes": "Clarithromycin chuyển hóa qua CYP3A4 thành 14-hydroxyclarithromycin (metabolite hoạt động). Suy gan có thể giảm chuyển hóa, tăng nồng độ clarithromycin. Tuy nhiên, thải trừ một phần qua thận nên cần điều chỉnh liều theo cả chức năng gan và thận. Theo dõi chặt chẽ tác dụng phụ ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng, vị kim loại trong miệng",
                "Triệu chứng tim mạch: QT kéo dài, torsades de pointes, rối loạn nhịp tim, tử vong do tim mạch (hiếm nhưng nguy hiểm)",
                "Triệu chứng thần kinh: Đau đầu, chóng mặt, mệt mỏi",
                "Triệu chứng thính giác: Giảm thính lực, ù tai (hiếm, có thể không hồi phục)",
                "Triệu chứng nghiêm trọng: Torsades de pointes, rối loạn nhịp tim nghiêm trọng, tử vong do tim mạch, mất thính lực"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay clarithromycin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "  - Theo dõi điện giải",
                "Điều trị QT kéo dài/torsades de pointes nếu có:",
                "  - Theo dõi ECG liên tục",
                "  - Đảm bảo kali, magie bình thường",
                "  - Điều trị torsades de pointes: Magnesium sulfate IV, pacing nếu cần",
                "  - Tránh các thuốc kéo dài QT khác",
                "Điều trị rối loạn thính giác nếu có:",
                "  - Ngừng ngay clarithromycin",
                "  - Điều trị hỗ trợ",
                "  - Có thể không hồi phục",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG (QT interval), điện giải (kali, magie), dấu hiệu thính giác trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (QT kéo dài, torsades de pointes, rối loạn thính giác)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày, giảm buồn nôn, nôn. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.",
                "timing": "Uống 2 lần/ngày (q12h), thường 250-500mg x 2 lần/ngày. Uống đều đặn, cách đều nhau trong ngày (12 giờ). Không bỏ liều."
            },
            "iv": {
                "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 60 phút (không truyền nhanh hơn). Có thể truyền trong 30 phút nếu cần nhưng không khuyến nghị.",
                "compatibility": [
                    "NaCl 0.9%",
                    "D5W (Dextrose 5%)",
                    "Nước cất vô trùng"
                ],
                "incompatibility": [
                    "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                    "Lactated Ringer's (LR) - không tương thích",
                    "Các dung dịch có cation (Al3+, Mg2+) - có thể tạo phức hợp"
                ],
                "notes": "Truyền IV trong 60 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Klacid (clarithromycin)",
                "UpToDate: Clarithromycin drug information",
                "Lexicomp: Clarithromycin monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Sanford Guide to Antimicrobial Therapy"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
        }
    },
    "Ciprofloxacin": {
        "group": "Infectious Disease - Fluoroquinolone Antibiotic",
        "vietnamese_name": "Ciprofloxacin, Cipro",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường tiết niệu (UTI)",
            "Nhiễm trùng đường hô hấp",
            "Nhiễm trùng da và mô mềm",
            "Nhiễm trùng xương và khớp",
            "Nhiễm trùng ổ bụng",
            "Tiêu chảy do vi khuẩn"
        ],
        "contraindications": [
            "Dị ứng ciprofloxacin/quinolone",
            "Có thai",
            "Trẻ em <18 tuổi (trừ chỉ định đặc biệt)",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_uti": "250-500mg x 2 lần/ngày x 3-7 ngày",
            "adult_respiratory": "500-750mg x 2 lần/ngày",
            "adult_complicated": "400mg IV x 2 lần/ngày",
            "notes": "Tránh dùng với antacid, sắt, sucralfate (cách 2 giờ)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Đứt gân Achilles (hiếm nhưng nguy hiểm)",
            "QT kéo dài",
            "Rối loạn thần kinh (co giật, lú lẫn)",
            "Phản ứng quang hóa",
            "Viêm khớp (trẻ em)"
        ],
        "interactions": [
            "Antacid/Sắt/Sucralfate: giảm hấp thu - cách 2 giờ",
            "Warfarin: tăng tác dụng chống đông",
            "Theophylline: tăng nồng độ theophylline",
            "Cyclosporine: tăng nồng độ cyclosporine"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Fluoroquinolone kháng sinh phổ rộng. Ức chế DNA gyrase (ở vi khuẩn Gram-âm) và topoisomerase IV (ở vi khuẩn Gram-dương), enzyme cần thiết cho sao chép và sửa chữa DNA. Dẫn đến tổn thương DNA và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, H. influenzae, Neisseria), một số Gram-dương (không phải MRSA), và một số vi khuẩn không điển hình (Legionella, Mycoplasma). Kháng thuốc phát triển nhanh nếu dùng không đúng.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles)",
            "Thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm)",
            "Tim mạch (QT kéo dài, rối loạn nhịp tim)",
            "Đường huyết (tăng hoặc hạ đường huyết - đặc biệt với sulfonylurea)",
            "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
            "Chức năng gan (ALT, AST) - hiếm viêm gan nặng"
        ],
        "precautions": [
            "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc",
            "Nguy cơ tăng ở: > 60 tuổi, dùng corticosteroid, ghép thận, ghép tim, phổi, hoạt động thể lực",
            "NGỪNG NGAY nếu có đau, sưng gân",
            "QT kéo dài → không dùng với các thuốc kéo dài QT khác, bệnh nhân có tiền sử rối loạn nhịp",
            "Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng",
            "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm (cách 2 giờ)",
            "Hạ đường huyết → thận trọng với sulfonylurea",
            "Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn",
            "Tránh dùng với sữa, sản phẩm sữa (giảm hấp thu)",
            "Uống nhiều nước để tránh kết tinh trong nước tiểu"
        ],
        "pharmacokinetics": {
            "half_life": "4 giờ (bình thường), 5-7 giờ (suy thận)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q12h (PO/IV), q8h cho Pseudomonas",
            "protein_binding": "20-40%",
            "metabolism": "Gan (CYP1A2) - một phần",
            "clearance": "Chủ yếu qua thận (40-60% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Tăng nguy cơ viêm gân và đứt gân ở mọi lứa tuổi. Nguy cơ tăng ở bệnh nhân > 60 tuổi, dùng corticosteroid, ghép cơ quan. Nguy cơ tổn thương thần kinh ngoại biên không hồi phục. Nguy cơ tác dụng phụ nghiêm trọng về gân, cơ, khớp, và thần kinh có thể xảy ra cùng lúc. Nguy cơ làm nặng bệnh nhược cơ. Tăng nguy cơ rối loạn tâm thần và hành vi tự sát."
    },
    "Doxycycline": {
        "group": "Infectious Disease - Tetracycline Antibiotic",
        "vietnamese_name": "Doxycycline, Vibramycin",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm trùng đường hô hấp",
            "Nhiễm trùng da (mụn trứng cá)",
            "Chlamydia",
            "Lyme disease",
            "Sốt rét phòng ngừa",
            "Rickettsia",
            "Mycoplasma"
        ],
        "contraindications": [
            "Dị ứng doxycycline/tetracycline",
            "Có thai (3 tháng cuối)",
            "Trẻ em <8 tuổi (gây vàng răng)"
        ],
        "dosage": {
            "adult_respiratory": "100mg x 2 lần/ngày x 7-14 ngày",
            "adult_chlamydia": "100mg x 2 lần/ngày x 7 ngày",
            "adult_acne": "50-100mg x 1-2 lần/ngày",
            "adult_malaria_prophylaxis": "100mg x 1 lần/ngày",
            "notes": "Uống với nhiều nước, tránh nằm ngay sau khi uống. Tránh nắng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Loét thực quản (nếu không uống đủ nước)",
            "Phản ứng quang hóa (nhạy cảm ánh sáng)",
            "Vàng răng (trẻ em, có thai)",
            "Tăng áp lực nội sọ (hiếm)",
            "Độc gan (liều cao)"
        ],
        "interactions": [
            "Antacid/Sắt/Calcium: giảm hấp thu - cách 2 giờ",
            "Warfarin: tăng tác dụng chống đông",
            "Digoxin: tăng nồng độ digoxin",
            "Phenytoin/Carbamazepine: giảm nồng độ doxycycline"
        ],
        "pregnancy": "D - Chống chỉ định trong 3 tháng cuối",
        "mechanism_of_action": "Tetracycline kháng sinh phổ rộng. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 30S của ribosome, ngăn cản gắn aminoacyl-tRNA. Phổ kháng khuẩn: Gram-dương, Gram-âm, vi khuẩn không điển hình (Chlamydia, Mycoplasma, Rickettsia, Borrelia), và một số ký sinh trùng (Plasmodium). Không hiệu quả với Pseudomonas hoặc Proteus. Đặc biệt hiệu quả với vi khuẩn không điển hình và được dùng trong nhiễm trùng đường hô hấp, Lyme disease, và sốt rét.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dạ dày-ruột (buồn nôn, nôn, tiêu chảy, viêm thực quản)",
            "Da (tăng độ nhạy cảm với ánh sáng, phát ban)",
            "Răng và xương (ở trẻ em < 8 tuổi: ố vàng răng vĩnh viễn, chậm phát triển xương)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan, tăng áp lực nội sọ giả (ở phụ nữ)",
            "Thận (không tích lũy ở suy thận, nhưng theo dõi)"
        ],
        "precautions": [
            "KHÔNG dùng cho trẻ em < 8 tuổi (trừ trường hợp đe dọa tính mạng) - gây ố vàng răng vĩnh viễn, chậm phát triển xương",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng, mặc quần áo che phủ",
            "Uống với nhiều nước (ít nhất 200ml) và ở tư thế đứng để tránh viêm thực quản (đau khi nuốt, khó nuốt)",
            "KHÔNG uống nằm ngửa hoặc trước khi ngủ",
            "Tương tác với nhiều thuốc và thực phẩm: giảm hấp thu với antacid, sắt, canxi, magie, kẽm, sữa (cách 2 giờ)",
            "Tương tác với warfarin → tăng nguy cơ chảy máu (theo dõi INR)",
            "Tương tác với thuốc tránh thai → giảm hiệu quả (dùng biện pháp tránh thai khác)",
            "Tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị) - đặc biệt ở phụ nữ, ngừng nếu có",
            "Không dùng trong 3 tháng cuối thai kỳ (nguy cơ ố vàng răng, chậm phát triển xương ở trẻ)",
            "Uống với thức ăn để giảm kích ứng dạ dày (nhưng giảm hấp thu một phần)"
        ],
        "pharmacokinetics": {
            "half_life": "18-22 giờ (dài)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q12h hoặc q24h (PO/IV)",
            "protein_binding": "80-90%",
            "metabolism": "Gan (một phần), bài tiết một phần nguyên dạng",
            "clearance": "Gan và thận, KHÔNG tích lũy ở suy thận (khác với tetracycline cũ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nang: tránh ẩm. Bảo quản tốt hơn các tetracycline cũ (ít bị hỏng).",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, ố vàng răng vĩnh viễn ở trẻ em < 8 tuổi là không hồi phục. Tăng áp lực nội sọ giả có thể gây mù. Viêm thực quản có thể nghiêm trọng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antacid, Sắt, Calcium, Magnesium, Kẽm, Bismuth",
                    "mechanism": "Các cation hóa trị 2+ (Ca²⁺, Mg²⁺, Fe²⁺, Zn²⁺) tạo phức hợp không hòa tan với doxycycline, làm giảm hấp thu doxycycline.",
                    "effect": "Giảm hấp thu doxycycline đáng kể (50-90%), giảm hiệu quả kháng khuẩn",
                    "management": "Cách ít nhất 2 giờ giữa doxycycline và các thuốc/thực phẩm chứa cation (antacid, sắt, canxi, magie, kẽm, sữa, bismuth). Uống doxycycline trước bữa ăn hoặc 2 giờ sau bữa ăn nếu bữa ăn chứa nhiều sữa hoặc thực phẩm giàu canxi."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Doxycycline có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể đẩy warfarin khỏi albumin (protein binding cao).",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng doxycycline). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân dùng kéo dài (>7 ngày)."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Doxycycline có thể làm tăng hấp thu digoxin bằng cách thay đổi hệ vi khuẩn đường ruột, làm tăng nồng độ digoxin.",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính digoxin (buồn nôn, rối loạn nhịp tim)",
                    "management": "Theo dõi nồng độ digoxin. Có thể cần giảm liều digoxin. Theo dõi dấu hiệu độc tính digoxin."
                },
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Phenytoin và carbamazepine cảm ứng enzyme chuyển hóa doxycycline, làm giảm nồng độ doxycycline.",
                    "effect": "Giảm nồng độ doxycycline, giảm hiệu quả kháng khuẩn",
                    "management": "Có thể cần tăng liều doxycycline. Theo dõi đáp ứng điều trị."
                },
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột. Ngoài ra, doxycycline có thể cảm ứng enzyme chuyển hóa estrogen.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng."
                }
            ],
            "minor": [
                {
                    "drug": "Penicillin",
                    "mechanism": "Doxycycline có thể đối kháng với penicillin trong một số trường hợp (ức chế tổng hợp protein vs ức chế tổng hợp thành tế bào).",
                    "effect": "Giảm hiệu quả kháng khuẩn của penicillin (hiếm)",
                    "management": "Tránh dùng đồng thời nếu có thể. Chọn một trong hai thuốc tùy theo chỉ định."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng doxycycline hoặc tetracycline",
                "Có thai (3 tháng cuối) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (nguy cơ ố vàng răng, chậm phát triển xương ở trẻ)",
                "Trẻ em < 8 tuổi - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (trừ trường hợp đe dọa tính mạng như sốt rét, rickettsia) - nguy cơ ố vàng răng vĩnh viễn, chậm phát triển xương"
            ],
            "relative": [
                "Có thai (3 tháng đầu và giữa) - nguy cơ ố vàng răng, chậm phát triển xương ở trẻ, chỉ dùng khi thực sự cần thiết",
                "Suy gan nặng - tăng nguy cơ độc gan",
                "Tăng áp lực nội sọ giả - có thể làm nặng thêm",
                "Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu",
                "Bệnh nhân đang dùng digoxin - tăng nguy cơ độc tính digoxin",
                "Nhạy cảm với ánh sáng - tăng nguy cơ phản ứng quang hóa"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Doxycycline là thuốc phân loại D. Các nghiên cứu trên động vật và người cho thấy nguy cơ ố vàng răng vĩnh viễn và chậm phát triển xương ở trẻ khi dùng trong thai kỳ, đặc biệt trong tam cá nguyệt thứ hai và thứ ba. Chống chỉ định trong tam cá nguyệt thứ hai và thứ ba. Tránh dùng trong tam cá nguyệt đầu tiên nếu có thể. Chỉ dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong các trường hợp đe dọa tính mạng như sốt rét, rickettsia.",
            "lactation": {
                "safety": "Compatible",
                "details": "Doxycycline bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, có thể gây ố vàng răng ở trẻ sơ sinh nếu dùng kéo dài.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Tránh dùng kéo dài. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Doxycycline chuyển hóa một phần qua gan, nhưng không tích lũy đáng kể ở suy gan nhẹ.",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan và dấu hiệu độc gan.",
            "severe": "Giảm liều 25-50% hoặc tăng khoảng cách giữa các liều. Theo dõi chức năng gan chặt chẽ. Có thể cần tránh dùng nếu suy gan rất nặng.",
            "notes": "Doxycycline chuyển hóa một phần qua gan, nhưng thải trừ chủ yếu qua gan và thận. Không tích lũy đáng kể ở suy gan nhẹ, nhưng có thể tích lũy ở suy gan nặng. Cần điều chỉnh liều ở suy gan nặng. Khác với tetracycline cũ, doxycycline không tích lũy ở suy thận."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, viêm thực quản (đau khi nuốt, khó nuốt)",
                "Triệu chứng gan: Tăng men gan, viêm gan (đặc biệt ở liều cao, suy gan)",
                "Triệu chứng thần kinh: Tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị) - đặc biệt ở phụ nữ, có thể gây mù",
                "Triệu chứng da: Phản ứng quang hóa nặng (phát ban, bỏng da khi tiếp xúc với ánh sáng)",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay doxycycline",
                "Điều trị viêm thực quản nếu có:",
                "  - Uống nhiều nước",
                "  - Tránh nằm ngửa",
                "  - Điều trị giảm đau nếu cần",
                "  - Có thể cần nội soi nếu nghiêm trọng",
                "Điều trị tăng áp lực nội sọ giả nếu có:",
                "  - Ngừng ngay doxycycline",
                "  - Điều trị bằng acetazolamide hoặc mannitol nếu cần",
                "  - Theo dõi thị lực và dấu hiệu thần kinh",
                "  - Có thể cần chọc dò tủy sống để giảm áp lực",
                "Điều trị phản ứng quang hóa nếu có:",
                "  - Tránh ánh nắng trực tiếp",
                "  - Dùng kem chống nắng",
                "  - Điều trị phát ban/bỏng da",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị độc gan nếu có:",
                "  - Ngừng ngay doxycycline",
                "  - Điều trị hỗ trợ gan",
                "  - Theo dõi chức năng gan",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis không hiệu quả do protein binding cao (80-90%)"
            ],
            "monitoring": "Theo dõi dấu hiệu tiêu hóa (buồn nôn, nôn, viêm thực quản), dấu hiệu tăng áp lực nội sọ giả (đau đầu, nhìn mờ, phù gai thị), dấu hiệu phản ứng quang hóa (phát ban, bỏng da), chức năng gan (ALT, AST), PT/INR (nếu dùng với warfarin), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có tăng áp lực nội sọ giả hoặc độc gan."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhưng giảm hấp thu một phần. Tránh uống với sữa hoặc thực phẩm giàu canxi (giảm hấp thu đáng kể).",
                "timing": "Uống 1-2 lần/ngày tùy chỉ định (respiratory: 2 lần/ngày, chlamydia: 2 lần/ngày, acne: 1-2 lần/ngày, malaria prophylaxis: 1 lần/ngày). Cách đều trong ngày. Uống với nhiều nước (ít nhất 200ml) và ở tư thế đứng để tránh viêm thực quản. KHÔNG uống nằm ngửa hoặc trước khi ngủ. Cách ít nhất 2 giờ với antacid, sắt, canxi, magie, kẽm, sữa."
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 0.1-1mg/ml. Pha 100mg trong 100ml = 1mg/ml. Pha 200mg trong 200ml = 1mg/ml. Lắc kỹ để hòa tan hoàn toàn. Bảo quản tránh ánh sáng.",
                "infusion_rate": "Truyền IV trong 1-4 giờ. Tốc độ: 100ml/1 giờ = ~1.7ml/phút, 200ml/4 giờ = ~0.83ml/phút. KHÔNG truyền nhanh (bolus) - tăng nguy cơ tác dụng phụ.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Ringer's Lactate - có thể tạo kết tủa với canxi",
                    "Các dung dịch chứa canxi, magie, sắt - tạo kết tủa",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Uống với nhiều nước và ở tư thế đứng để tránh viêm thực quản, 2) Tránh ánh nắng trực tiếp, dùng kem chống nắng, 3) Cách ít nhất 2 giờ với antacid, sắt, canxi, magie, kẽm, sữa, 4) KHÔNG dùng cho trẻ em < 8 tuổi (trừ trường hợp đe dọa tính mạng), 5) KHÔNG dùng trong 3 tháng cuối thai kỳ, 6) Theo dõi dấu hiệu tăng áp lực nội sọ giả."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Doxycycline (Vibramycin)",
                "UpToDate - Doxycycline: Drug Information",
                "Medscape - Doxycycline Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Doxycycline Monograph",
                "Micromedex - Doxycycline Drug Information",
                "IDSA Guidelines - Community-Acquired Pneumonia, Tick-Borne Infections"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Metronidazole": {
        "group": "Infectious Disease - Nitroimidazole Antibiotic",
        "vietnamese_name": "Metronidazole, Flagyl",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn kỵ khí",
            "Giardia",
            "Trichomonas",
            "Amebiasis",
            "Bacterial vaginosis",
            "H. pylori (kết hợp)",
            "C. difficile colitis"
        ],
        "contraindications": [
            "Dị ứng metronidazole",
            "Có thai (3 tháng đầu)",
            "Dùng disulfiram trong 14 ngày"
        ],
        "dosage": {
            "adult_anaerobic": "500mg x 3 lần/ngày PO hoặc 500mg mỗi 6-8 giờ IV",
            "adult_giardia": "250mg x 3 lần/ngày x 7 ngày",
            "adult_trichomonas": "2g x 1 lần hoặc 500mg x 2 lần/ngày x 7 ngày",
            "adult_c_diff": "500mg x 3 lần/ngày x 10-14 ngày",
            "adult_h_pylori": "500mg x 2 lần/ngày (với amoxicillin + PPI)",
            "notes": "TRÁNH RƯỢU (phản ứng disulfiram-like). Uống với thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Giảm liều 50%"
        },
        "side_effects": [
            "Vị kim loại trong miệng",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Phản ứng với rượu (nôn, đỏ mặt, nhịp tim nhanh)",
            "Co giật (liều cao)",
            "Bệnh thần kinh ngoại biên (dùng lâu dài)",
            "Ban da"
        ],
        "interactions": [
            "Rượu: phản ứng disulfiram-like (nôn, đỏ mặt) - TRÁNH",
            "Warfarin: tăng tác dụng chống đông",
            "Lithium: tăng nồng độ lithium",
            "Phenytoin: tăng nồng độ phenytoin",
            "Disulfiram: chống chỉ định"
        ],
        "pregnancy": "B - D trong 3 tháng đầu",
        "mechanism_of_action": "Nitroimidazole kháng sinh/kháng ký sinh trùng. Sau khi vào tế bào vi khuẩn/ký sinh trùng, bị khử bởi ferredoxin (có trong vi khuẩn kỵ khí và ký sinh trùng) → tạo ra các gốc tự do độc hại phá hủy DNA. Chỉ hoạt động với vi khuẩn kỵ khí (Bacteroides, Clostridium, giardia) và ký sinh trùng (Trichomonas, Giardia, Entamoeba). KHÔNG hoạt động với vi khuẩn hiếu khí. Đặc biệt hiệu quả với kỵ khí và được dùng trong nhiễm trùng bụng, nhiễm trùng phụ khoa, và nhiễm C. difficile.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Thần kinh (dị cảm, co giật, viêm dây thần kinh ngoại biên, chóng mặt, mất điều hòa)",
            "Dạ dày-ruột (buồn nôn, nôn, tiêu chảy, vị kim loại)",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Số lượng bạch cầu (hiếm giảm bạch cầu)",
            "Phản ứng Disulfiram-like nếu uống rượu (buồn nôn, nôn, đỏ bừng, nhịp tim nhanh)"
        ],
        "precautions": [
            "TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng thuốc - gây phản ứng Disulfiram-like nặng (buồn nôn, nôn, đỏ bừng, nhịp tim nhanh, hạ huyết áp)",
            "Nguy cơ tổn thương thần kinh ngoại biên và trung ương (dị cảm, co giật, viêm dây thần kinh) - tăng ở dùng kéo dài, liều cao, suy gan",
            "Ngừng nếu có dấu hiệu tổn thương thần kinh",
            "Không dùng cho nhiễm trùng do vi khuẩn hiếu khí (không hiệu quả)",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Vị kim loại rất thường gặp - không phải tác dụng phụ nghiêm trọng nhưng khó chịu",
            "Có thể làm nước tiểu sẫm màu (vô hại)",
            "Thận trọng ở suy gan (giảm chuyển hóa → tăng nguy cơ tác dụng phụ thần kinh)",
            "Không dùng trong 3 tháng đầu thai kỳ (nguy cơ dị tật) - chỉ dùng khi thực sự cần thiết",
            "Pha trong NS, D5W, hoặc LR, truyền IV trong 30-60 phút"
        ],
        "pharmacokinetics": {
            "half_life": "6-8 giờ (bình thường), 9-15 giờ (suy gan)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q8h (PO/IV), q12h cho C. difficile (PO)",
            "protein_binding": "< 20%",
            "metabolism": "Gan (CYP450) - chuyển hóa mạnh",
            "clearance": "Chủ yếu qua gan (60-80%), cần điều chỉnh ở suy gan nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng. Viên nén: tránh ẩm. Dung dịch pha tiêm: sau khi pha, bảo quản ở nhiệt độ phòng 24 giờ, tránh ánh sáng.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, phản ứng Disulfiram-like với rượu có thể nặng. Tổn thương thần kinh có thể không hồi phục. Nguy cơ dị tật thai nhi nếu dùng trong 3 tháng đầu thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Rượu (Ethanol)",
                    "mechanism": "Metronidazole ức chế aldehyde dehydrogenase, enzyme chuyển hóa acetaldehyde (sản phẩm chuyển hóa của ethanol) thành acetate. Kết quả là tích lũy acetaldehyde, gây phản ứng Disulfiram-like.",
                    "effect": "Phản ứng Disulfiram-like nặng: buồn nôn, nôn, đỏ bừng mặt, nhịp tim nhanh, hạ huyết áp, khó thở, có thể đe dọa tính mạng",
                    "management": "TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng metronidazole. Tránh tất cả các sản phẩm chứa rượu (thuốc ho, nước súc miệng, thực phẩm có rượu). Nếu uống rượu, ngừng ngay metronidazole và điều trị hỗ trợ."
                },
                {
                    "drug": "Disulfiram",
                    "mechanism": "Cả hai đều ức chế aldehyde dehydrogenase, tác dụng cộng dồn làm tăng nguy cơ phản ứng Disulfiram-like và tổn thương thần kinh.",
                    "effect": "Tăng nguy cơ phản ứng Disulfiram-like nặng, tăng nguy cơ tổn thương thần kinh",
                    "management": "CHỐNG CHỈ ĐỊNH: Không dùng metronidazole trong vòng 14 ngày sau khi ngừng disulfiram. Nếu đang dùng disulfiram, không dùng metronidazole."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Metronidazole ức chế chuyển hóa warfarin qua CYP2C9, làm tăng nồng độ warfarin và tăng tác dụng chống đông.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng metronidazole). Giảm liều warfarin 30-50%. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày)."
                }
            ],
            "moderate": [
                {
                    "drug": "Lithium",
                    "mechanism": "Metronidazole có thể làm giảm thải trừ lithium, làm tăng nồng độ lithium trong máu.",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính lithium (buồn nôn, run, lú lẫn, suy thận)",
                    "management": "Theo dõi nồng độ lithium thường xuyên. Có thể cần giảm liều lithium. Theo dõi dấu hiệu độc tính lithium."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Metronidazole ức chế chuyển hóa phenytoin qua CYP2C9, làm tăng nồng độ phenytoin.",
                    "effect": "Tăng nồng độ phenytoin, tăng nguy cơ độc tính (chóng mặt, rung giật nhãn cầu, lú lẫn, co giật)",
                    "management": "Theo dõi nồng độ phenytoin. Có thể cần giảm liều phenytoin. Theo dõi dấu hiệu độc tính phenytoin."
                },
                {
                    "drug": "Phenobarbital",
                    "mechanism": "Phenobarbital có thể cảm ứng enzyme chuyển hóa metronidazole, làm giảm nồng độ metronidazole.",
                    "effect": "Giảm nồng độ metronidazole, giảm hiệu quả kháng khuẩn",
                    "management": "Có thể cần tăng liều metronidazole. Theo dõi đáp ứng điều trị."
                }
            ],
            "minor": [
                {
                    "drug": "Cimetidine",
                    "mechanism": "Cimetidine có thể ức chế chuyển hóa metronidazole, làm tăng nhẹ nồng độ metronidazole.",
                    "effect": "Tăng nhẹ nồng độ metronidazole",
                    "management": "Theo dõi dấu hiệu tác dụng phụ. Thường không cần điều chỉnh liều."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng metronidazole hoặc nitroimidazole",
                "Đang dùng disulfiram hoặc đã dùng disulfiram trong vòng 14 ngày - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI"
            ],
            "relative": [
                "Có thai (3 tháng đầu) - nguy cơ dị tật thai nhi, chỉ dùng khi thực sự cần thiết",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tác dụng phụ thần kinh",
                "Bệnh thần kinh ngoại biên - tăng nguy cơ tổn thương thần kinh",
                "Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu",
                "Bệnh nhân đang dùng lithium - tăng nguy cơ độc tính lithium",
                "Nhiễm trùng do vi khuẩn hiếu khí - không hiệu quả"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B (D trong 3 tháng đầu)",
            "pregnancy_details": "Metronidazole là thuốc phân loại B trong tam cá nguyệt thứ hai và thứ ba, nhưng phân loại D trong tam cá nguyệt đầu tiên. Các nghiên cứu trên động vật cho thấy nguy cơ dị tật bẩm sinh khi dùng trong tam cá nguyệt đầu tiên. Các nghiên cứu trên người cho thấy nguy cơ dị tật tăng nhẹ khi dùng trong tam cá nguyệt đầu tiên. Tránh dùng trong tam cá nguyệt đầu tiên nếu có thể. Nếu cần thiết, chỉ dùng khi lợi ích vượt quá nguy cơ. Có thể dùng trong tam cá nguyệt thứ hai và thứ ba khi cần thiết.",
            "lactation": {
                "safety": "Compatible",
                "details": "Metronidazole bài tiết vào sữa mẹ ở nồng độ tương đương nồng độ trong máu mẹ. Nồng độ trong sữa mẹ cao và có thể gây vị đắng cho trẻ sơ sinh. Tuy nhiên, không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ khi dùng liều thông thường.",
                "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng. Có thể gây vị đắng cho trẻ sơ sinh. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả. Có thể cân nhắc ngừng cho con bú trong thời gian ngắn nếu dùng liều cao."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Metronidazole chuyển hóa qua gan (CYP450), nhưng không tích lũy đáng kể ở suy gan nhẹ.",
            "moderate": "Thận trọng, có thể cần giảm liều 25-50%. Theo dõi chức năng gan và dấu hiệu tác dụng phụ thần kinh.",
            "severe": "Giảm liều 50% hoặc tăng khoảng cách giữa các liều (q12h thay vì q8h). Theo dõi chức năng gan chặt chẽ. Theo dõi dấu hiệu tác dụng phụ thần kinh (dị cảm, co giật). Có thể cần tránh dùng nếu suy gan rất nặng.",
            "notes": "Metronidazole chuyển hóa mạnh qua gan (CYP450), thải trừ chủ yếu qua gan (60-80%). Half-life tăng từ 6-8 giờ (bình thường) lên 9-15 giờ (suy gan). Tích lũy ở suy gan nặng, làm tăng nguy cơ tác dụng phụ thần kinh. Cần điều chỉnh liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức, dị cảm, viêm dây thần kinh ngoại biên, chóng mặt, mất điều hòa (đặc biệt ở suy gan, liều cao)",
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, vị kim loại",
                "Triệu chứng Disulfiram-like: Buồn nôn, nôn, đỏ bừng mặt, nhịp tim nhanh, hạ huyết áp, khó thở (nếu uống rượu)",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)",
                "Triệu chứng gan: Tăng men gan, viêm gan (hiếm)",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay metronidazole",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều trị phản ứng Disulfiram-like nếu có (nếu uống rượu):",
                "  - Ngừng ngay metronidazole",
                "  - Bù dịch đầy đủ",
                "  - Hỗ trợ hô hấp nếu cần",
                "  - Điều trị hạ huyết áp nếu cần",
                "  - Theo dõi dấu hiệu sinh tồn",
                "Điều trị tổn thương thần kinh ngoại biên:",
                "  - Ngừng ngay metronidazole",
                "  - Điều trị hỗ trợ (vật lý trị liệu)",
                "  - Tổn thương có thể không hồi phục hoàn toàn",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ metronidazole một phần (protein binding <20%), nhưng không hiệu quả lắm do chuyển hóa chủ yếu qua gan."
            ],
            "monitoring": "Theo dõi dấu hiệu thần kinh (co giật, ý thức, dị cảm, viêm dây thần kinh), dấu hiệu Disulfiram-like (nếu uống rượu), PT/INR (nếu dùng với warfarin), chức năng gan (ALT, AST), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có tổn thương thần kinh hoặc suy gan."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày và vị kim loại. Uống với thức ăn không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 2-3 lần/ngày tùy chỉ định (anaerobic: 3 lần/ngày, C. difficile: 3 lần/ngày, H. pylori: 2 lần/ngày). Cách đều trong ngày. TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng."
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl), D5W (5% Dextrose), hoặc Ringer's Lactate. Nồng độ pha: 5mg/ml (tối đa). Pha 500mg trong 100ml = 5mg/ml. Pha 1g trong 200ml = 5mg/ml. Lắc kỹ để hòa tan hoàn toàn. Bảo quản tránh ánh sáng.",
                "infusion_rate": "Truyền IV trong 30-60 phút. Tốc độ: 100ml/30 phút = ~3.3ml/phút, 100ml/60 phút = ~1.7ml/phút. KHÔNG truyền nhanh (bolus) - tăng nguy cơ tác dụng phụ.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Aminophylline - tạo kết tủa, không pha chung",
                    "Phenytoin - có thể tạo kết tủa, không pha chung",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) TUYỆT ĐỐI KHÔNG uống rượu trong và ít nhất 3 ngày sau khi ngừng, 2) Truyền chậm (30-60 phút) để giảm tác dụng phụ, 3) Bảo quản tránh ánh sáng, 4) Theo dõi dấu hiệu tổn thương thần kinh, 5) Điều chỉnh liều ở suy gan nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Metronidazole (Flagyl)",
                "UpToDate - Metronidazole: Drug Information",
                "Medscape - Metronidazole Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Metronidazole Monograph",
                "Micromedex - Metronidazole Drug Information",
                "IDSA Guidelines - Anaerobic Infections, C. difficile Infection"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
"Chloroquine": {
        "group": "Infectious Disease - Antimalarial",
        "vietnamese_name": "Chloroquine, Aralen",
        "administration": ["PO"],
        "indications": [
            "Sốt rét (phòng ngừa và điều trị)",
            "Amebiasis ngoài gan",
            "Lupus ban đỏ hệ thống",
            "Viêm khớp dạng thấp"
        ],
        "contraindications": [
            "Dị ứng chloroquine/4-aminoquinoline",
            "Bệnh võng mạc",
            "Bệnh gan nặng",
            "Bệnh thận nặng",
            "Rối loạn tạo máu"
        ],
        "dosage": {
            "adult_malaria_treatment": "600mg base (1g phosphate) ngày đầu, sau đó 300mg base (500mg phosphate) sau 6-8 giờ, sau đó 300mg base/ngày x 2 ngày",
            "adult_malaria_prophylaxis": "300mg base (500mg phosphate) x 1 lần/tuần, bắt đầu 1-2 tuần trước khi đi, tiếp tục trong khi ở và 4 tuần sau khi về",
            "adult_lupus": "200-400mg base/ngày",
            "notes": "Rất độc cho võng mạc nếu dùng lâu dài. Theo dõi mắt định kỳ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "under_30": "Tránh dùng"
        },
        "side_effects": [
            "Độc võng mạc (dùng lâu dài, không hồi phục)",
            "Rối loạn thị giác",
            "Ban da, rụng tóc",
            "Rối loạn tạo máu",
            "Rối loạn tim mạc (liều cao)",
            "Co giật (quá liều)",
            "Độc gan"
        ],
        "interactions": [
            "Digoxin: tăng nồng độ digoxin",
            "Cimetidine: tăng nồng độ chloroquine",
            "Ampicillin: giảm hấp thu ampicillin",
            "Kaolin: giảm hấp thu chloroquine"
        ],
        "pregnancy": "C - Thận trọng, nhưng có thể dùng cho sốt rét",
        "mechanism_of_action": "Chloroquine là 4-aminoquinoline, ức chế polymerase của ký sinh trùng sốt rét, ngăn cản tổng hợp DNA và RNA. Thuốc tích lũy trong lysosome của ký sinh trùng, tăng pH và ức chế tiêu hóa hemoglobin. Đối với sốt rét, chloroquine diệt thể vô tính trong hồng cầu. Đối với bệnh tự miễn (lupus, RA), chloroquine ức chế hoạt động của tế bào miễn dịch và giảm sản xuất cytokine viêm",
        "monitoring": [
            "Khám mắt định kỳ mỗi 6-12 tháng nếu dùng lâu dài (theo dõi độc võng mạc)",
            "Thị trường (visual field) mỗi 6-12 tháng nếu dùng lâu dài",
            "Chức năng gan (ALT, AST) định kỳ",
            "Công thức máu toàn phần (CBC) định kỳ",
            "Điện tâm đồ nếu dùng liều cao (theo dõi rối loạn nhịp)",
            "Dấu hiệu rối loạn thị giác (nhìn mờ, ám điểm)",
            "Dấu hiệu độc võng mạc (không hồi phục nếu phát hiện muộn)"
        ],
        "precautions": [
            "Rất độc cho võng mạc nếu dùng lâu dài - cần khám mắt định kỳ",
            "Ngừng ngay nếu có dấu hiệu độc võng mạc (nhìn mờ, ám điểm)",
            "Giảm liều 50% nếu suy thận (CrCl 30-60)",
            "Tránh dùng nếu suy thận nặng (CrCl <30)",
            "Có thể dùng trong thai kỳ cho sốt rét (category C)",
            "Tránh dùng với kaolin (giảm hấp thu)",
            "Tương tác với digoxin (tăng nồng độ digoxin)",
            "Có thể gây rối loạn nhịp tim nếu dùng liều cao (cần theo dõi ECG)"
        ],
        "pharmacokinetics": {
            "half_life": "20-60 ngày (rất dài, tích lũy)",
            "onset": "2-3 giờ (sốt rét), 4-8 tuần (lupus/RA)",
            "duration": "7-14 ngày (sốt rét), kéo dài (lupus/RA)",
            "protein_binding": "55%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ - chậm)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Có thể gây độc võng mạc nặng và không hồi phục nếu dùng lâu dài. Cần khám mắt định kỳ mỗi 6-12 tháng khi dùng lâu dài. Ngừng ngay nếu có dấu hiệu độc võng mạc"
    },
    "Artesunate": {
        "group": "Infectious Disease - Antimalarial (Artemisinin)",
        "vietnamese_name": "Artesunate",
        "administration": ["PO", "IV", "IM", "Rectal"],
        "indications": [
            "Sốt rét nặng (severe malaria)",
            "Sốt rét kháng chloroquine",
            "Sốt rét sốt rét P. falciparum",
            "Điều trị kết hợp sốt rét (ACT)"
        ],
        "contraindications": [
            "Dị ứng artesunate/artemisinin",
            "3 tháng đầu thai kỳ (trừ sốt rét nặng)",
            "Dùng đơn độc (phải dùng kết hợp)"
        ],
        "dosage": {
            "adult_severe_iv": "2.4mg/kg IV ngay, sau đó 1.2mg/kg sau 12 và 24 giờ, sau đó mỗi ngày",
            "adult_po": "200mg ngày đầu, sau đó 100mg x 1 lần/ngày x 5 ngày (với artemether-lumefantrine)",
            "adult_act": "Theo phác đồ ACT (artesunate + amodiaquine/ mefloquine/piperaquine)",
            "notes": "PHẢI dùng kết hợp với thuốc sốt rét khác (ACT). Không dùng đơn độc"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Nhức đầu",
            "Chóng mặt",
            "Buồn nôn",
            "Rối loạn tiêu hóa",
            "Nhịp tim chậm (hiếm)",
            "Độc tính thần kinh (dùng lâu dài, liều cao - hiếm)"
        ],
        "interactions": [
            "Thuốc sốt rét khác: dùng kết hợp (ACT protocol)",
            "Warfarin: có thể tăng tác dụng chống đông",
            "CYP2A6 substrates: có thể tăng nồng độ"
        ],
        "pregnancy": "D - Tránh trong 3 tháng đầu (trừ sốt rét nặng)",
        "mechanism_of_action": "Artesunate là dẫn xuất artemisinin (sesquiterpene lactone), chuyển hóa thành dihydroartemisinin (hoạt chất). Tác động nhanh và mạnh lên ký sinh trùng sốt rét bằng cách tạo ra các gốc tự do (free radicals) trong hồng cầu bị nhiễm, gây stress oxy hóa và phá vỡ màng tế bào ký sinh trùng. Artesunate diệt cả thể vô tính và thể giao tử (gametocyte), đặc biệt hiệu quả với P. falciparum kháng chloroquine. Thuốc có tác dụng nhanh (fast-acting), giảm số lượng ký sinh trùng trong 24-48 giờ",
        "monitoring": [
            "Theo dõi sốt và triệu chứng sốt rét (giảm nhanh trong 24-48 giờ)",
            "Ký sinh trùng trong máu (parasitemia) mỗi 6-12 giờ trong sốt rét nặng",
            "Chức năng gan (ALT, AST) nếu dùng lâu dài",
            "Dấu hiệu rối loạn nhịp tim (nhịp chậm - hiếm)",
            "Dấu hiệu độc tính thần kinh nếu dùng lâu dài, liều cao (hiếm)",
            "Đường huyết nếu dùng IV (có thể gây hạ đường huyết)"
        ],
        "precautions": [
            "PHẢI dùng kết hợp với thuốc sốt rét khác (ACT protocol) - không dùng đơn độc",
            "Tránh dùng trong 3 tháng đầu thai kỳ (trừ sốt rét nặng - cân nhắc lợi ích/nguy cơ)",
            "Dùng đúng phác đồ ACT để tránh kháng thuốc",
            "Không dùng đơn độc (dễ gây kháng thuốc)",
            "Có thể gây hạ đường huyết nếu dùng IV (theo dõi)",
            "Có thể gây nhịp tim chậm (hiếm - theo dõi ECG nếu có triệu chứng)",
            "Có thể tương tác với warfarin (tăng tác dụng chống đông)",
            "Dùng kết hợp với amodiaquine, mefloquine, hoặc piperaquine theo phác đồ ACT"
        ],
        "pharmacokinetics": {
            "half_life": "45 phút (artesunate), 1-2 giờ (dihydroartemisinin)",
            "onset": "1-2 giờ (giảm sốt, triệu chứng)",
            "duration": "4-6 giờ (ngắn)",
            "protein_binding": "Moderate",
            "clearance": "Gan (chuyển hóa nhanh qua CYP2A6, esterase), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để tủ lạnh (2-8°C) nếu yêu cầu",
        "black_box_warnings": "KHÔNG được dùng đơn độc - phải dùng kết hợp với thuốc sốt rét khác theo phác đồ ACT để tránh kháng thuốc. Tránh dùng trong 3 tháng đầu thai kỳ trừ sốt rét nặng (cân nhắc lợi ích/nguy cơ)"
    },
    "Albendazole": {
        "group": "Infectious Disease - Anthelmintic",
        "vietnamese_name": "Albendazole, Albenza",
        "administration": ["PO"],
        "indications": [
            "Giun sán (giun đũa, giun móc, giun tóc, giun kim)",
            "Sán dây",
            "Sán lá gan",
            "Hydatid disease (Echinococcus)",
            "Neurocysticercosis"
        ],
        "contraindications": [
            "Dị ứng albendazole/benzimidazole",
            "Có thai",
            "Suy gan nặng",
            "Giảm bạch cầu"
        ],
        "dosage": {
            "adult_intestinal_worms": "400mg x 1 lần (đơn liều) hoặc 400mg x 2 lần/ngày x 3 ngày",
            "adult_echinococcus": "400mg x 2 lần/ngày x 28 ngày (có thể lặp lại)",
            "adult_neurocysticercosis": "400mg x 2 lần/ngày x 8-30 ngày",
            "adult_hydatid": "10-15mg/kg/ngày x 28 ngày",
            "notes": "Uống với thức ăn béo để tăng hấp thu. Uống kèm corticosteroid cho neurocysticercosis"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Đau đầu",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Tiêu chảy",
            "Giảm bạch cầu",
            "Tăng men gan",
            "Ban da",
            "Rụng tóc (dùng lâu dài)"
        ],
        "interactions": [
            "Dexamethasone: tăng nồng độ albendazole",
            "Praziquantel: tăng nồng độ albendazole",
            "Cimetidine: tăng nồng độ albendazole",
            "Phenytoin/Carbamazepine: giảm nồng độ albendazole"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Albendazole là benzimidazole carbamate, ức chế tubulin polymerization trong tế bào ký sinh trùng, gây mất microtubule, phá vỡ cấu trúc tế bào và chức năng của ký sinh trùng. Thuốc ngăn chặn vận chuyển glucose và các chất dinh dưỡng khác trong tế bào ký sinh trùng, dẫn đến mất năng lượng và chết. Albendazole có tác dụng phổ rộng trên nhiều loại giun sán, bao gồm giun đũa, giun móc, giun tóc, giun kim, sán dây, và sán lá gan. Đặc biệt hiệu quả trong điều trị hydatid disease và neurocysticercosis do tác dụng hệ thống tốt hơn mebendazole.",
        "monitoring": [
            "Công thức máu (CBC) - theo dõi giảm bạch cầu, đặc biệt khi dùng lâu dài",
            "Chức năng gan (ALT, AST, bilirubin) - theo dõi độc tính gan",
            "Triệu chứng lâm sàng (đau đầu, buồn nôn, đau bụng)",
            "Đáp ứng điều trị (xét nghiệm phân sau điều trị)",
            "Dấu hiệu nhiễm độc (rụng tóc, ban da) khi dùng lâu dài"
        ],
        "precautions": [
            "Uống với thức ăn béo để tăng hấp thu (tăng nồng độ trong máu 5 lần)",
            "Dùng kèm corticosteroid (dexamethasone) cho neurocysticercosis để giảm phản ứng viêm",
            "Theo dõi chức năng gan thường xuyên khi dùng lâu dài (hydatid disease, neurocysticercosis)",
            "Tránh dùng trong thai kỳ (gây dị tật thai nhi)",
            "Kiểm tra thai trước khi bắt đầu điều trị",
            "Dùng biện pháp tránh thai hiệu quả trong và sau điều trị",
            "Thận trọng ở bệnh nhân suy gan",
            "Theo dõi công thức máu khi dùng lâu dài (nguy cơ giảm bạch cầu)"
        ],
        "pharmacokinetics": {
            "half_life": "8-12 giờ (albendazole sulfoxide - chất chuyển hóa hoạt động)",
            "onset": "2-4 giờ",
            "duration": "24-48 giờ",
            "protein_binding": "70%",
            "clearance": "Gan (chuyển hóa thành albendazole sulfoxide), thải trừ qua mật và nước tiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi. Cần kiểm tra thai trước khi bắt đầu điều trị"
    },
    "Mebendazole": {
        "group": "Infectious Disease - Anthelmintic",
        "vietnamese_name": "Mebendazole, Vermox",
        "administration": ["PO"],
        "indications": [
            "Giun sán (giun đũa, giun móc, giun tóc, giun kim)",
            "Sán dây",
            "Trichinosis"
        ],
        "contraindications": [
            "Dị ứng mebendazole/benzimidazole",
            "Có thai",
            "Trẻ em <1 tuổi"
        ],
        "dosage": {
            "adult_intestinal_worms": "100mg x 2 lần/ngày x 3 ngày",
            "adult_pinworm": "100mg x 1 lần (đơn liều), lặp lại sau 2-3 tuần",
            "adult_whipworm": "100mg x 2 lần/ngày x 3 ngày",
            "adult_tapeworm": "100mg x 2 lần/ngày x 3 ngày",
            "notes": "Uống với thức ăn hoặc không đều được. Không hấp thu tốt nên ít tác dụng phụ hệ thống"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau bụng",
            "Tiêu chảy",
            "Buồn nôn",
            "Ban da",
            "Giảm bạch cầu (dùng lâu dài, liều cao)",
            "Độc gan (hiếm)"
        ],
        "interactions": [
            "Cimetidine: có thể tăng nồng độ mebendazole",
            "Carbamazepine/Phenytoin: có thể giảm nồng độ mebendazole"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Mebendazole là benzimidazole carbamate, ức chế tubulin polymerization trong tế bào ký sinh trùng, gây mất microtubule và phá vỡ cấu trúc tế bào. Thuốc ngăn chặn vận chuyển glucose và các chất dinh dưỡng trong tế bào ký sinh trùng, dẫn đến mất năng lượng và chết. Khác với albendazole, mebendazole hấp thu kém qua đường tiêu hóa (<5%), nên chủ yếu tác dụng tại chỗ trong ruột, ít tác dụng phụ hệ thống. Thuốc hiệu quả trên giun đũa, giun móc, giun tóc, giun kim, và sán dây. Thường dùng cho nhiễm giun đường ruột đơn giản, ít dùng cho nhiễm nấm hệ thống.",
        "monitoring": [
            "Triệu chứng lâm sàng (đau bụng, tiêu chảy, buồn nôn)",
            "Đáp ứng điều trị (xét nghiệm phân sau 2-3 tuần)",
            "Công thức máu (nếu dùng lâu dài, liều cao) - theo dõi giảm bạch cầu",
            "Chức năng gan (nếu dùng lâu dài, liều cao)",
            "Dấu hiệu dị ứng (ban da)"
        ],
        "precautions": [
            "Có thể uống với thức ăn hoặc không (không ảnh hưởng nhiều do hấp thu kém)",
            "Không hấp thu tốt nên ít tác dụng phụ hệ thống (ưu điểm so với albendazole)",
            "Phù hợp cho nhiễm giun đường ruột đơn giản",
            "Lặp lại liều sau 2-3 tuần cho giun kim (để diệt ấu trùng mới nở)",
            "Tránh dùng trong thai kỳ (gây dị tật thai nhi)",
            "Không dùng cho trẻ em <1 tuổi",
            "Thận trọng ở bệnh nhân suy gan nặng",
            "Theo dõi công thức máu nếu dùng lâu dài hoặc liều cao"
        ],
        "pharmacokinetics": {
            "half_life": "2-9 giờ (rất thay đổi do hấp thu kém)",
            "onset": "2-4 giờ",
            "duration": "24-48 giờ",
            "protein_binding": "90-95%",
            "clearance": "Hấp thu kém (<5%), chủ yếu thải trừ qua phân, một phần qua nước tiểu"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi"
    },
"Amoxicillin-clavulanate": {
        "group": "Antibiotic - Beta-lactam (Penicillin + Beta-lactamase inhibitor)",
        "vietnamese_name": "Amoxicillin-clavulanate, Augmentin, Amoclav",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp trên/dưới",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da mô mềm",
            "Nhiễm khuẩn răng miệng",
            "Nhiễm khuẩn tai mũi họng (trẻ em)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Viêm gan do amoxicillin-clavulanate trước đây",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "adult_po": "875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày",
            "pediatric_po_suspension": "20-40mg amoxicillin/kg/ngày chia 2-3 lần (tối đa 875mg/125mg)",
            "pediatric_po_tablet": "25-45mg amoxicillin/kg/ngày chia 2 lần (trên 40kg: dùng liều người lớn)",
            "adult_iv": "1000/200mg IV mỗi 8 giờ",
            "pediatric_iv": "90mg amoxicillin/kg/ngày chia 3 lần (tối đa 1000/200mg mỗi 8 giờ)",
            "notes": "Có dạng suspension cho trẻ em. Uống với thức ăn để giảm tiêu chảy"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều hoặc tăng khoảng cách",
            "under_30": "Liều thấp hơn, khoảng cách dài hơn"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Buồn nôn",
            "Phát ban",
            "Viêm gan (hiếm nhưng nguy hiểm)",
            "Nhiễm trùng nấm Candida"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Methotrexate: tăng độc tính methotrexate",
            "Allopurinol: tăng nguy cơ phát ban",
            "Thuốc tránh thai: có thể giảm hiệu quả"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Amoxicillin: aminopenicillin phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Clavulanate: beta-lactamase inhibitor, bảo vệ amoxicillin khỏi bị phân hủy bởi beta-lactamase. Kết hợp này mở rộng phổ kháng khuẩn, đặc biệt hiệu quả với H. influenzae, E. coli, và một số kỵ khí. Clavulanate không có hoạt tính kháng khuẩn riêng. Được dùng rộng rãi trong nhiễm trùng đường hô hấp, tiết niệu, da và mô mềm.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - tăng men gan (thường nhất thời), hiếm viêm gan (đặc biệt với clavulanate)",
            "Dấu hiệu nhiễm C. difficile",
            "Phát ban (đặc biệt ở bệnh nhân nhiễm virus như EBV)",
            "Chức năng thận (creatinine) - hiếm viêm thận kẽ"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Nguy cơ viêm gan (đặc biệt do clavulanate) - thường nhất thời, hiếm nặng, tăng ở nam giới, dùng kéo dài",
            "Theo dõi men gan, ngừng nếu tăng nặng",
            "Phát ban thường gặp, đặc biệt ở bệnh nhân nhiễm virus (EBV, CMV) - không phải dị ứng thật",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Uống với thức ăn để giảm kích ứng dạ dày và tăng hấp thu",
            "Dùng đúng liều và đủ thời gian để tránh kháng thuốc",
            "Không dùng cho nhiễm trùng do Pseudomonas hoặc Enterococcus kháng"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (amoxicillin và clavulanate)",
            "onset": "1-2 giờ (PO)",
            "duration": "q8h hoặc q12h tùy công thức",
            "protein_binding": "17-20% (amoxicillin), 22-30% (clavulanate)",
            "metabolism": "Một phần trong gan",
            "clearance": "Chủ yếu qua thận, cần điều chỉnh thận ở suy thận nặng"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm. Sau khi pha (suspension): bảo quản trong tủ lạnh 10 ngày, sau đó vứt bỏ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ viêm gan (đặc biệt do clavulanate) có thể nặng, đặc biệt ở nam giới và dùng kéo dài. Phát ban thường gặp và có thể nhầm với dị ứng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tổng hợp vitamin K, tăng tác dụng warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng amoxicillin-clavulanate. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Amoxicillin-clavulanate ức chế bài tiết methotrexate ở ống thận, làm giảm thải trừ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính (giảm bạch cầu, thiếu máu, độc gan, độc thận)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate, theo dõi chặt chẽ công thức máu, chức năng gan, thận. Ngừng methotrexate nếu có dấu hiệu độc tính."
                }
            ],
            "moderate": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Cơ chế chưa rõ ràng, có thể liên quan đến phản ứng miễn dịch.",
                    "effect": "Tăng nguy cơ phát ban, phản ứng dị ứng (đặc biệt phát ban maculopapular)",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi dấu hiệu phát ban. Ngừng ngay nếu có phát ban nặng hoặc phản ứng dị ứng."
                },
                {
                    "drug": "Thuốc tránh thai nội tiết",
                    "mechanism": "Amoxicillin-clavulanate có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen, giảm nồng độ estrogen.",
                    "effect": "Có thể giảm hiệu quả thuốc tránh thai, tăng nguy cơ mang thai",
                    "management": "Khuyến nghị sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng amoxicillin-clavulanate và 7 ngày sau khi ngừng thuốc."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết amoxicillin ở ống thận, làm tăng nồng độ amoxicillin.",
                    "effect": "Tăng nồng độ amoxicillin, tăng tác dụng phụ",
                    "management": "Có thể dùng để tăng nồng độ amoxicillin nếu cần. Theo dõi tác dụng phụ. Giảm liều amoxicillin nếu cần."
                }
            ],
            "minor": [
                {
                    "drug": "Antacids",
                    "mechanism": "Antacids có thể giảm nhẹ hấp thu amoxicillin.",
                    "effect": "Giảm nhẹ hấp thu amoxicillin",
                    "management": "Cách 2 giờ nếu có thể. Không ảnh hưởng đáng kể ở liều điều trị thông thường."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng amoxicillin, clavulanate, hoặc các penicillin khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Viêm gan do amoxicillin-clavulanate trước đây - nguy cơ tái phát cao, có thể nặng hơn"
            ],
            "relative": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều, tăng khoảng cách",
                "Suy gan - thận trọng, có thể giảm chuyển hóa",
                "Nhiễm virus (EBV, CMV) - tăng nguy cơ phát ban (không phải dị ứng thật)",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Dùng với methotrexate - tăng độc tính methotrexate",
                "Dùng với allopurinol - tăng nguy cơ phát ban"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Amoxicillin-clavulanate phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Penicillin là một trong những kháng sinh an toàn nhất trong thai kỳ. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.",
            "lactation": {
                "safety": "Compatible",
                "details": "Amoxicillin và clavulanate bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Penicillin là một trong những kháng sinh an toàn nhất khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (tiêu chảy, phát ban)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Amoxicillin và clavulanate chuyển hóa một phần qua gan nhưng không đáng kể.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận.",
            "notes": "Amoxicillin và clavulanate chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua thận (60-70% bài tiết nguyên dạng qua nước tiểu). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, nguy cơ viêm gan do clavulanate tăng ở bệnh nhân có bệnh gan, đặc biệt nam giới và dùng kéo dài. Theo dõi chặt chẽ chức năng gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
                "Triệu chứng thần kinh: Kích động, co giật (hiếm, thường ở liều rất cao)",
                "Triệu chứng thận: Tăng creatinine, suy thận cấp (hiếm)",
                "Triệu chứng da: Phát ban, mày đay",
                "Triệu chứng gan: Tăng men gan, viêm gan (đặc biệt với clavulanate)",
                "Triệu chứng nghiêm trọng: Co giật, suy thận cấp, viêm gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay amoxicillin-clavulanate",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "  - Theo dõi điện giải",
                "Điều trị co giật nếu có:",
                "  - Benzodiazepine (diazepam, lorazepam)",
                "  - Theo dõi hô hấp",
                "Điều trị tăng men gan/viêm gan nếu có:",
                "  - Theo dõi ALT, AST, bilirubin",
                "  - Điều trị hỗ trợ gan",
                "  - Nếu viêm gan nặng: điều trị suy gan",
                "Điều trị suy thận cấp nếu có:",
                "  - Theo dõi creatinine, BUN, lượng nước tiểu",
                "  - Điều trị suy thận cấp",
                "Lọc máu (hemodialysis) có thể loại bỏ một phần amoxicillin nhưng không được khuyến nghị thường quy",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng gan (ALT, AST, bilirubin), chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu da trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (suy gan, suy thận, co giật)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm kích ứng dạ dày, giảm tiêu chảy, và tăng hấp thu. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.",
                "timing": "Uống 2-3 lần/ngày tùy công thức (875/125mg x 2 lần/ngày hoặc 500/125mg x 3 lần/ngày). Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều."
            },
            "iv": {
                "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với nước cất vô trùng hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30 phút (không truyền nhanh hơn). Có thể truyền trong 15-20 phút nếu cần nhưng không khuyến nghị.",
                "compatibility": [
                    "NaCl 0.9%",
                    "D5W (Dextrose 5%)",
                    "Lactated Ringer's (LR) - thận trọng, kiểm tra tương thích",
                    "Nước cất vô trùng"
                ],
                "incompatibility": [
                    "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                    "Aminoglycosides (mất hoạt tính nếu trộn trực tiếp)",
                    "Probenecid (không trộn, dùng riêng)"
                ],
                "notes": "Truyền IV trong 30 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Label: Augmentin (amoxicillin-clavulanate)",
                "UpToDate: Amoxicillin-clavulanate drug information",
                "Lexicomp: Amoxicillin-clavulanate monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
                "Sanford Guide to Antimicrobial Therapy"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
        }
    },
    "Paracetamol": {
        "group": "Analgesic/Antipyretic",
        "vietnamese_name": "Paracetamol, Acetaminophen, Tylenol, Efferalgan",
        "administration": ["PO", "IV", "PR"],
        "indications": [
            "Sốt",
            "Đau nhẹ đến trung bình",
            "Đau đầu",
            "Đau cơ",
            "Đau răng"
        ],
        "contraindications": [
            "Dị ứng paracetamol",
            "Suy gan nặng",
            "Bệnh gan tiến triển"
        ],
        "dosage": {
            "adult_po": "500-1000mg x 3-4 lần/ngày (tối đa 4g/ngày)",
            "adult_iv": "1000mg IV mỗi 6 giờ (tối đa 4g/ngày)",
            "pediatric_po": "10-15mg/kg x 3-4 lần/ngày (tối đa 60mg/kg/ngày)",
            "pediatric_iv": "15mg/kg IV mỗi 6 giờ (tối đa 60mg/kg/ngày)",
            "pediatric_pr": "15-20mg/kg PR mỗi 6 giờ (khi không uống được)",
            "notes": "Liều tối đa: Người lớn 4g/ngày, Trẻ em 60mg/kg/ngày. Quá liều gây độc gan nghiêm trọng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Khoảng cách 6-8 giờ"
        },
        "side_effects": [
            "Hiếm khi có tác dụng phụ ở liều điều trị",
            "Độc gan (với liều quá cao - >150mg/kg)",
            "Phát ban (hiếm)",
            "Giảm bạch cầu (rất hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu (với liều cao kéo dài)",
            "Isoniazid: tăng nguy cơ độc gan",
            "Alcohol: tăng nguy cơ độc gan",
            "Phenytoin/Carbamazepine: tăng nguy cơ độc gan"
        ],
        "pregnancy": "C - An toàn (dùng được trong thai kỳ)",
        "mechanism_of_action": "Paracetamol ức chế cyclooxygenase (COX) chủ yếu ở hệ thần kinh trung ương, làm giảm tổng hợp prostaglandin E2 trong vùng dưới đồi, từ đó giảm đau và hạ sốt. Khác với NSAID, paracetamol ít tác dụng kháng viêm ở ngoại biên vì không ức chế COX hiệu quả ở mô ngoại biên. Cơ chế chính xác vẫn chưa hoàn toàn rõ ràng, nhưng có thể liên quan đến ức chế COX-2 ở hệ thần kinh trung ương hoặc tác dụng qua con đường cannabinoid. Quan trọng: Ở liều quá cao, chuyển hóa qua CYP2E1 tạo NAPQI (N-acetyl-p-benzoquinone imine) - chất độc gây tổn thương gan nặng.",
        "monitoring": [
            "ALT/AST nếu nghi ngờ quá liều hoặc bệnh nhân có nguy cơ (suy gan, uống rượu, dùng isoniazid)",
            "INR nếu dùng với warfarin liều cao kéo dài (tăng nguy cơ chảy máu)",
            "Dấu hiệu độc tính gan: buồn nôn, nôn, đau bụng, vàng da (xuất hiện sau 24-48h sau quá liều)",
            "Nồng độ paracetamol trong máu nếu quá liều (đồ thị Rumack-Matthew để quyết định điều trị N-acetylcysteine)",
            "Đường huyết (hạ đường huyết có thể xảy ra trong quá liều)"
        ],
        "precautions": [
            "Không vượt quá 4g/ngày ở người lớn, 60mg/kg/ngày ở trẻ em để tránh độc tính gan",
            "Giảm liều ở bệnh nhân suy gan, suy thận nặng (khoảng cách liều 6-8 giờ)",
            "Tránh rượu khi dùng (rượu tăng CYP2E1 → tăng sản xuất NAPQI độc)",
            "Kiểm tra các thuốc kết hợp có chứa paracetamol (tránh quá liều không chủ ý)",
            "Thận trọng với bệnh nhân suy dinh dưỡng, nhịn ăn (giảm glutathione → tăng nguy cơ độc tính)",
            "Nếu quá liều, điều trị ngay với N-acetylcysteine (hiệu quả nhất trong vòng 8 giờ đầu)",
            "Thận trọng với bệnh nhân dùng isoniazid, phenytoin, carbamazepine (tăng nguy cơ độc gan)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (bình thường), 4-8 giờ (quá liều)",
            "onset": "30-60 phút (PO), 15-30 phút (IV), 60 phút (PR)",
            "duration": "4-6 giờ",
            "protein_binding": "10-25%",
            "clearance": "Gan: chủ yếu qua glucuronidation (40-60%) và sulfation (20-40%), một phần nhỏ qua CYP2E1 tạo NAPQI (chất độc). Thận: <5% bài tiết nguyên dạng. Ở quá liều, con đường CYP2E1 tăng → tăng NAPQI → vượt quá glutathione → độc gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dung dịch: tránh đông lạnh. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi dùng.",
        "black_box_warnings": "Quá liều có thể gây độc tính gan nghiêm trọng, suy gan cấp, tử vong. Liều >150mg/kg ở trẻ em hoặc >10g ở người lớn có thể gây độc tính gan. Triệu chứng ban đầu có thể nhẹ (buồn nôn, nôn) nhưng tổn thương gan xảy ra sau 24-48 giờ. Điều trị ngay với N-acetylcysteine nếu quá liều (hiệu quả nhất trong vòng 8 giờ đầu). Không dùng quá 4g/ngày ở người lớn.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Paracetamol liều cao kéo dài có thể ức chế CYP2C9, tăng nồng độ warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên nếu dùng paracetamol liều cao (>2g/ngày) kéo dài. Điều chỉnh liều warfarin nếu cần."
                },
                {
                    "drug": "Rượu (Ethanol)",
                    "mechanism": "Rượu kích hoạt CYP2E1, tăng chuyển hóa paracetamol thành NAPQI (chất độc)",
                    "effect": "Tăng nguy cơ độc tính gan nghiêm trọng, đặc biệt ở liều paracetamol >4g/ngày",
                    "management": "Tránh rượu hoặc giảm liều paracetamol khi uống rượu. Thận trọng ở bệnh nhân nghiện rượu."
                }
            ],
            "moderate": [
                {
                    "drug": "Isoniazid",
                    "mechanism": "Tăng chuyển hóa qua CYP2E1",
                    "effect": "Tăng nguy cơ độc tính gan",
                    "management": "Thận trọng, giảm liều paracetamol, theo dõi ALT/AST"
                },
                {
                    "drug": "Phenytoin, Carbamazepine",
                    "mechanism": "Cảm ứng enzyme chuyển hóa",
                    "effect": "Tăng nguy cơ độc tính gan",
                    "management": "Thận trọng, giảm liều paracetamol"
                }
            ],
            "minor": [
                {
                    "drug": "Metoclopramide",
                    "mechanism": "Tăng nhu động dạ dày",
                    "effect": "Tăng hấp thu paracetamol (nhẹ)",
                    "management": "Không cần điều chỉnh liều"
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Suy gan nặng (Child-Pugh C)",
                "Dị ứng paracetamol",
                "Quá liều paracetamol (đang trong quá trình điều trị)"
            ],
            "relative": [
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - giảm liều",
                "Nghiện rượu - giảm liều tối đa 2g/ngày",
                "Suy thận nặng (CrCl <30) - giảm liều hoặc tăng khoảng cách",
                "Thiếu hụt G6PD (hiếm gây thiếu máu tan máu)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "An toàn trong thai kỳ. Paracetamol là thuốc giảm đau/hạ sốt được lựa chọn đầu tiên trong thai kỳ. Không có bằng chứng về dị tật bẩm sinh. Có thể dùng ở tất cả các tam cá nguyệt. Tuy nhiên, một số nghiên cứu quan sát gợi ý mối liên hệ có thể có với ADHD và tự kỷ ở trẻ khi dùng lâu dài trong thai kỳ, nhưng chứng cứ chưa rõ ràng.",
            "lactation": {
                "safety": "Compatible",
                "details": "Paracetamol bài tiết vào sữa mẹ ở nồng độ thấp (<1% liều mẹ). An toàn cho trẻ bú mẹ. Nồng độ trong sữa mẹ rất thấp, không có tác dụng phụ đáng kể ở trẻ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú. Dùng liều thường dùng (500-1000mg mỗi 4-6 giờ)."
            }
        },
        "hepatic_adjustment": {
            "mild": "Giảm liều tối đa 2-3g/ngày, chia 3-4 lần",
            "moderate": "Giảm liều tối đa 2g/ngày, chia 3-4 lần. Theo dõi ALT/AST",
            "severe": "Tránh dùng hoặc dùng liều rất thấp (1-1.5g/ngày) dưới sự giám sát chặt chẽ. Theo dõi ALT/AST thường xuyên",
            "notes": "Paracetamol chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và độc tính. Đặc biệt thận trọng ở bệnh nhân nghiện rượu."
        },
        "overdose_management": {
            "symptoms": [
                "Giai đoạn 1 (0-24h): Buồn nôn, nôn, đau bụng, chán ăn, mệt mỏi. Bệnh nhân có thể không có triệu chứng rõ ràng",
                "Giai đoạn 2 (24-48h): Giảm triệu chứng (giai đoạn 'yên lặng'), nhưng ALT/AST bắt đầu tăng",
                "Giai đoạn 3 (48-72h): Tăng ALT/AST đỉnh, vàng da, suy gan, rối loạn đông máu, bệnh não gan, có thể tử vong",
                "Giai đoạn 4 (4-14 ngày): Hồi phục (nếu sống sót) hoặc tử vong"
            ],
            "antidote": "N-acetylcysteine (NAC) - hiệu quả nếu dùng trong vòng 8-10 giờ sau quá liều, tốt nhất trong 4-6 giờ",
            "treatment": [
                "Đánh giá nguy cơ: Liều >150mg/kg (trẻ em) hoặc >10g (người lớn) hoặc >200mg/kg (người lớn có nguy cơ) = nguy cơ cao",
                "Đo nồng độ paracetamol trong máu 4 giờ sau khi uống (hoặc ngay khi đến viện nếu >4 giờ)",
                "Sử dụng đồ thị Rumack-Matthew để quyết định điều trị: Nếu nồng độ trên đường 'điều trị' → dùng NAC",
                "NAC protocol: IV hoặc PO. IV: 150mg/kg trong 15 phút, sau đó 50mg/kg trong 4 giờ, sau đó 100mg/kg trong 16 giờ. PO: 140mg/kg, sau đó 70mg/kg mỗi 4 giờ x 17 liều",
                "Theo dõi ALT/AST, INR, bilirubin, glucose, lactate, creatinine thường xuyên",
                "Điều trị hỗ trợ: Truyền dịch, điều chỉnh đường huyết, điều chỉnh rối loạn đông máu, xem xét ghép gan nếu suy gan nặng"
            ],
            "monitoring": "Nồng độ paracetamol trong máu, ALT/AST mỗi 12-24 giờ, INR, bilirubin, glucose, lactate, creatinine, dấu hiệu bệnh não gan, tiên lượng (King's College Criteria cho ghép gan)"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "N-acetylcysteine (NAC)",
                    "indication": "Quá liều paracetamol",
                    "dose": "IV: 150mg/kg trong 15 phút, sau đó 50mg/kg trong 4 giờ, sau đó 100mg/kg trong 16 giờ. PO: 140mg/kg, sau đó 70mg/kg mỗi 4 giờ x 17 liều",
                    "mechanism": "Bổ sung glutathione, liên kết với NAPQI (chất độc), giải độc gan",
                    "notes": "Hiệu quả nhất nếu dùng trong vòng 8-10 giờ sau quá liều, tốt nhất trong 4-6 giờ. Vẫn có thể có lợi sau 24 giờ nếu có suy gan."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ",
                "timing": "Mỗi 4-6 giờ khi cần. Không quá 4g/ngày (người lớn) hoặc 60mg/kg/ngày (trẻ em). Có thể dùng trước khi đi ngủ nếu cần giảm đau/giảm sốt ban đêm."
            },
            "iv": {
                "reconstitution": "Pha trong D5W hoặc NS. Nồng độ cuối: 1mg/ml (tối đa 10mg/ml). Dùng ngay sau khi pha.",
                "infusion_rate": "Truyền trong 15 phút",
                "compatibility": ["D5W", "NS", "LR"],
                "incompatibility": ["Không pha trộn với các thuốc khác"],
                "notes": "Dùng cho bệnh nhân không uống được hoặc cần tác dụng nhanh. Liều tương đương PO."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Acetaminophen",
                "UpToDate - Acetaminophen poisoning",
                "Rumack-Matthew nomogram",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics",
                "King's College Criteria for liver transplantation in acute liver failure"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - RCTs và guidelines dựa trên chứng cứ"
        }
    },
    "Ibuprofen": {
        "group": "Analgesic/Antipyretic/NSAID",
        "vietnamese_name": "Ibuprofen, Brufen, Advil",
        "administration": ["PO", "IV"],
        "indications": [
            "Sốt",
            "Đau nhẹ đến trung bình",
            "Viêm khớp",
            "Đau bụng kinh",
            "Đau đầu"
        ],
        "contraindications": [
            "Dị ứng NSAID",
            "Loét dạ dày tá tràng hoạt động",
            "Suy thận nặng",
            "Suy tim nặng",
            "Có thai (3 tháng cuối)",
            "Trẻ em <6 tháng"
        ],
        "dosage": {
            "adult_po": "200-400mg x 3-4 lần/ngày (tối đa 2.4g/ngày)",
            "adult_iv": "400-800mg IV mỗi 6 giờ",
            "pediatric_po": "5-10mg/kg x 3-4 lần/ngày (tối đa 40mg/kg/ngày)",
            "pediatric_suspension": "Có dạng suspension 100mg/5ml cho trẻ em",
            "notes": "Uống với thức ăn để giảm kích ứng dạ dày. Không dùng quá 10 ngày không có chỉ định"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Không dùng hoặc giảm liều đáng kể"
        },
        "side_effects": [
            "Kích ứng dạ dày",
            "Đau đầu",
            "Chóng mặt",
            "Tăng nguy cơ tim mạch (với dùng lâu dài)",
            "Suy thận cấp (hiếm)",
            "Phát ban"
        ],
        "interactions": [
            "Aspirin: có thể giảm hiệu quả aspirin",
            "Warfarin: tăng nguy cơ chảy máu",
            "Lithium: tăng nồng độ lithium",
            "Methotrexate: tăng độc tính",
            "ACE inhibitors: giảm hiệu quả"
        ],
        "pregnancy": "C - Tránh dùng trong 3 tháng cuối (D)",
        "mechanism_of_action": "Ibuprofen ức chế không chọn lọc enzyme cyclooxygenase (COX-1 và COX-2), làm giảm tổng hợp prostaglandin, thromboxane A2, và prostacyclin từ acid arachidonic. Prostaglandin tham gia vào quá trình viêm, đau, sốt, và điều hòa thận. Thromboxane A2 gây kết tập tiểu cầu và co mạch. Ức chế COX-1 làm giảm prostaglandin bảo vệ niêm mạc dạ dày và ảnh hưởng đến chức năng thận. Ức chế COX-2 chủ yếu giảm viêm và đau. Ibuprofen là NSAID không chọn lọc, có tác dụng kháng viêm, giảm đau, và hạ sốt. Tác dụng kháng viêm mạnh hơn paracetamol nhưng có nhiều tác dụng phụ hơn, đặc biệt là kích ứng dạ dày và ảnh hưởng đến thận.",
        "monitoring": [
            "Dấu hiệu chảy máu dạ dày (phân đen, nôn ra máu, đau bụng, thiếu máu)",
            "Creatinine, BUN nếu dùng lâu dài hoặc bệnh nhân có nguy cơ suy thận (tuổi cao, tiểu đường, tăng huyết áp)",
            "Huyết áp (NSAID có thể tăng huyết áp, đặc biệt ở bệnh nhân tăng huyết áp đang điều trị)",
            "Chức năng gan (ALT, AST) nếu dùng lâu dài hoặc có triệu chứng",
            "Dấu hiệu suy tim (giữ nước, phù, khó thở) - NSAID có thể làm nặng suy tim",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)",
            "Triệu chứng tim mạch (đau ngực, khó thở) - tăng nguy cơ tim mạch với dùng lâu dài"
        ],
        "precautions": [
            "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày",
            "Cân nhắc dùng PPI (omeprazole, pantoprazole) hoặc misoprostol nếu có nguy cơ loét dạ dày (tuổi >65, tiền sử loét, dùng corticosteroid, dùng aspirin)",
            "Tránh dùng lâu dài ở bệnh nhân suy thận, suy tim, tăng huyết áp (làm nặng bệnh)",
            "Tránh dùng với ACE inhibitor/ARB (giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp)",
            "Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm, tăng nguy cơ chảy máu ở mẹ và con)",
            "Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể",
            "Thận trọng ở bệnh nhân >65 tuổi (tăng nguy cơ tác dụng phụ)",
            "Tránh dùng với aspirin liều thấp (có thể giảm hiệu quả bảo vệ tim mạch của aspirin)",
            "Thận trọng với bệnh nhân hen suyễn (có thể gây co thắt phế quản)",
            "Không dùng quá 10 ngày cho đau hoặc sốt mà không có chỉ định rõ ràng"
        ],
        "pharmacokinetics": {
            "half_life": "2-4 giờ",
            "onset": "30-60 phút (PO), 15-30 phút (IV)",
            "duration": "4-6 giờ",
            "protein_binding": ">99% (gắn chặt với albumin)",
            "clearance": "Gan: chuyển hóa qua CYP2C9 và CYP2C8 thành hydroxy và carboxy metabolites (không hoạt động). Thận: bài tiết <1% nguyên dạng, chủ yếu là metabolites. Thời gian bán thải tăng ở suy thận và suy gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha.",
        "black_box_warnings": "Tăng nguy cơ biến cố tim mạch nghiêm trọng (nhồi máu cơ tim, đột quỵ) có thể xảy ra sớm và tăng nguy cơ tử vong. Nguy cơ tăng ở bệnh nhân có bệnh tim mạch hoặc các yếu tố nguy cơ tim mạch. NSAID tăng nguy cơ xuất huyết tiêu hóa, loét, thủng dạ dày có thể gây tử vong. Nguy cơ tăng ở người cao tuổi, tiền sử loét, dùng corticosteroid, aspirin, rượu, hút thuốc. Không dùng trong 3 tháng cuối thai kỳ (đóng ống động mạch sớm).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Ibuprofen ức chế kết tập tiểu cầu và có thể tăng nguy cơ chảy máu. Có thể ảnh hưởng đến chuyển hóa warfarin.",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng, tăng INR",
                    "management": "Theo dõi INR chặt chẽ. Tránh dùng đồng thời nếu có thể. Nếu cần dùng, giảm liều ibuprofen và theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "ACE Inhibitors, ARB",
                    "mechanism": "NSAID giảm tổng hợp prostaglandin, làm giảm tác dụng giãn mạch của ACE inhibitor/ARB. Có thể gây giữ natri và nước.",
                    "effect": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp, tăng kali máu",
                    "management": "Tránh dùng đồng thời nếu có thể. Nếu cần, theo dõi creatinine, BUN, kali máu. Cân nhắc dùng liều thấp NSAID và thời gian ngắn."
                },
                {
                    "drug": "Aspirin (liều thấp tim mạch)",
                    "mechanism": "Ibuprofen có thể cạnh tranh với aspirin tại vị trí gắn COX-1, làm giảm tác dụng ức chế kết tập tiểu cầu của aspirin.",
                    "effect": "Giảm hiệu quả bảo vệ tim mạch của aspirin",
                    "management": "Nếu dùng aspirin liều thấp để bảo vệ tim mạch, dùng ibuprofen ít nhất 30 phút sau aspirin hoặc 8 giờ trước aspirin. Hoặc cân nhắc dùng NSAID khác không ức chế COX-1."
                }
            ],
            "moderate": [
                {
                    "drug": "Methotrexate",
                    "mechanism": "NSAID giảm thải trừ methotrexate qua thận, tăng nồng độ methotrexate trong máu.",
                    "effect": "Tăng độc tính methotrexate (giảm bạch cầu, suy tủy xương, độc gan)",
                    "management": "Tránh dùng với liều cao methotrexate. Nếu dùng liều thấp, theo dõi công thức máu, chức năng gan. Có thể cần giảm liều methotrexate."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "NSAID giảm thải trừ lithium qua thận, tăng nồng độ lithium.",
                    "effect": "Tăng nồng độ lithium, tăng nguy cơ độc tính lithium",
                    "management": "Theo dõi nồng độ lithium trong máu. Có thể cần giảm liều lithium khi bắt đầu dùng ibuprofen."
                },
                {
                    "drug": "Corticosteroid",
                    "mechanism": "Cả hai đều tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa.",
                    "effect": "Tăng nguy cơ xuất huyết tiêu hóa, loét dạ dày",
                    "management": "Cân nhắc dùng PPI hoặc misoprostol. Theo dõi dấu hiệu chảy máu dạ dày."
                }
            ],
            "minor": [
                {
                    "drug": "Furosemide, Thiazide",
                    "mechanism": "NSAID giảm tác dụng lợi tiểu, có thể gây giữ natri và nước.",
                    "effect": "Giảm hiệu quả lợi tiểu, có thể gây phù",
                    "management": "Theo dõi cân nặng, dấu hiệu giữ nước. Có thể cần điều chỉnh liều lợi tiểu."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng NSAID hoặc aspirin (quá mẫn cảm, phản ứng dị ứng nghiêm trọng)",
                "Loét dạ dày tá tràng hoạt động",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Suy thận nặng (CrCl <30 ml/min) hoặc đang lọc máu",
                "Suy gan nặng (Child-Pugh C)",
                "Suy tim nặng (NYHA class IV)",
                "Có thai (3 tháng cuối) - đóng ống động mạch sớm",
                "Trẻ em <6 tháng tuổi"
            ],
            "relative": [
                "Suy thận nhẹ đến trung bình (CrCl 30-60) - thận trọng, giảm liều",
                "Suy gan nhẹ đến trung bình (Child-Pugh A-B) - thận trọng, giảm liều",
                "Suy tim nhẹ đến trung bình (NYHA class II-III) - có thể làm nặng",
                "Tăng huyết áp không kiểm soát - có thể tăng huyết áp",
                "Tiền sử loét dạ dày - tăng nguy cơ loét",
                "Bệnh tim mạch hoặc yếu tố nguy cơ tim mạch - tăng nguy cơ biến cố tim mạch",
                "Hen suyễn - có thể gây co thắt phế quản (đặc biệt ở bệnh nhân nhạy cảm với aspirin)",
                "Người cao tuổi (>65) - tăng nguy cơ tác dụng phụ",
                "Có thai (1-2 tam cá nguyệt đầu) - thận trọng, chỉ dùng khi thực sự cần thiết"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C (1-2 tam cá nguyệt), D (3 tam cá nguyệt cuối)",
            "pregnancy_details": "Tam cá nguyệt 1-2: Thuốc phân loại C. Có thể dùng khi lợi ích vượt quá nguy cơ, nhưng nên tránh nếu không cần thiết. Một số nghiên cứu gợi ý tăng nguy cơ dị tật tim và thành bụng khi dùng trong tam cá nguyệt đầu. Tam cá nguyệt 3: Thuốc phân loại D - CHỐNG CHỈ ĐỊNH. NSAID ức chế tổng hợp prostaglandin, có thể gây đóng ống động mạch sớm ở thai nhi, thiểu ối, suy thận thai nhi, tăng nguy cơ chảy máu ở mẹ và con. Không dùng từ tuần 30 trở đi.",
            "lactation": {
                "safety": "Compatible (với dùng ngắn hạn)",
                "details": "Ibuprofen bài tiết vào sữa mẹ ở nồng độ rất thấp (<0.6% liều mẹ). Nồng độ trong sữa mẹ thấp và thời gian bán thải ngắn (2-4 giờ). Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú với liều điều trị tiêu chuẩn. Dùng liều thấp nhất hiệu quả và thời gian ngắn nhất có thể. Theo dõi trẻ sơ sinh nếu dùng lâu dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan nếu dùng lâu dài.",
            "moderate": "Thận trọng, giảm liều 25-50%. Tối đa 1.2g/ngày. Theo dõi ALT, AST thường xuyên.",
            "severe": "Tránh dùng hoặc dùng liều rất thấp (600-800mg/ngày) dưới sự giám sát chặt chẽ. Theo dõi ALT, AST, bilirubin thường xuyên. Chuyển hóa qua gan có thể giảm ở suy gan nặng.",
            "notes": "Ibuprofen chuyển hóa chủ yếu qua gan (CYP2C9, CYP2C8). Suy gan có thể làm giảm chuyển hóa, tăng thời gian bán thải. Thận trọng ở bệnh nhân nghiện rượu hoặc viêm gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng sớm (1-4 giờ): Buồn nôn, nôn, đau bụng, chóng mặt, buồn ngủ, đau đầu",
                "Triệu chứng muộn (4-24 giờ): Chảy máu dạ dày, suy thận cấp, rối loạn điện giải, toan chuyển hóa",
                "Triệu chứng nghiêm trọng: Hạ huyết áp, sốc, suy hô hấp, co giật, hôn mê (hiếm)",
                "Triệu chứng tim mạch: Rối loạn nhịp tim, suy tim cấp (với liều rất cao)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Đánh giá nguy cơ: Liều >100mg/kg (trẻ em) hoặc >7.5g (người lớn) = nguy cơ cao",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Điều trị hỗ trợ: Truyền dịch, điều chỉnh điện giải, điều trị toan chuyển hóa nếu có",
                "Theo dõi chức năng thận: Creatinine, BUN, nước tiểu",
                "Theo dõi chức năng gan: ALT, AST, bilirubin",
                "Theo dõi dấu hiệu chảy máu: Công thức máu, INR, PTT nếu có",
                "Điều trị xuất huyết tiêu hóa nếu có: PPI, truyền máu nếu cần",
                "Điều trị suy thận cấp nếu có: Điều chỉnh dịch, lọc máu nếu cần",
                "Hỗ trợ hô hấp nếu có suy hô hấp",
                "Điều trị co giật nếu có: Benzodiazepine"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận, chức năng gan, công thức máu, dấu hiệu chảy máu trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn hoặc sữa để giảm kích ứng dạ dày. Có thể uống với nước đầy đủ.",
                "timing": "Uống 3-4 lần/ngày, cách đều. Có thể uống với hoặc sau bữa ăn. Không uống khi đói."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 4mg/ml (tối đa). Pha 800mg trong 200ml dịch = 4mg/ml. Pha 400mg trong 100ml dịch = 4mg/ml.",
                "infusion_rate": "Truyền trong 30 phút. Không truyền quá nhanh. Tốc độ: 400mg/100ml = 200ml/30 phút = ~6.7ml/phút. 800mg/200ml = 200ml/30 phút = ~6.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Lactated Ringer"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha."],
                "notes": "Không dùng cho trẻ em <12 tuổi qua đường IV. Theo dõi dấu hiệu phản ứng dị ứng và tác dụng phụ trong quá trình truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ibuprofen (Advil, Motrin)",
                "UpToDate - Ibuprofen: Drug Information",
                "Medscape - Ibuprofen Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Ibuprofen Monograph",
                "Micromedex - Ibuprofen Drug Information"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Salbutamol": {
        "group": "Respiratory - Beta-2 Agonist (Short-acting)",
        "vietnamese_name": "Salbutamol, Albuterol, Ventolin, Salbutamol",
        "administration": ["INH", "IV", "PO", "NEB"],
        "indications": [
            "Hen phế quản",
            "COPD",
            "Co thắt phế quản",
            "Phòng co thắt phế quản do gắng sức",
            "Cấp cứu hen (nebulizer/IV)"
        ],
        "contraindications": [
            "Dị ứng salbutamol",
            "Nhịp tim nhanh nặng",
            "Rối loạn nhịp tim nặng",
            "Cường giáp"
        ],
        "dosage": {
            "adult_inh": "1-2 puff (100-200mcg) x 4 lần/ngày hoặc khi cần (tối đa 8-12 puff/ngày)",
            "adult_neb": "2.5-5mg nebulizer mỗi 4-6 giờ",
            "adult_iv": "5mcg/kg IV bolus, sau đó 0.5-5mcg/kg/phút",
            "pediatric_inh": "1-2 puff (100-200mcg) x 4 lần/ngày (trên 4 tuổi)",
            "pediatric_neb": "0.15mg/kg (tối thiểu 1.25mg) nebulizer mỗi 4-6 giờ",
            "pediatric_po_syrup": "0.1-0.15mg/kg x 3 lần/ngày (tối đa 2-4mg x 3 lần/ngày)",
            "notes": "Có dạng syrup và nebulizer cho trẻ em. Dùng khi cần cho cơn cấp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Run tay (phổ biến)",
            "Tim đập nhanh",
            "Đánh trống ngực",
            "Đau đầu",
            "Chóng mặt",
            "Hạ kali máu (với liều cao)",
            "Kích động"
        ],
        "interactions": [
            "Beta-blockers: đối kháng tác dụng",
            "Digoxin: có thể tăng nguy cơ loạn nhịp",
            "Diuretics: tăng nguy cơ hạ kali máu",
            "MAOIs: thận trọng"
        ],
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Salbutamol (albuterol) là chất chủ vận beta-2 adrenergic receptors chọn lọc, kích thích beta-2 receptors ở cơ trơn phế quản. Khi gắn vào beta-2 receptor, kích hoạt adenylate cyclase → tăng cAMP trong tế bào → hoạt hóa protein kinase A → phosphoryl hóa các protein → giãn cơ trơn phế quản. Salbutamol chọn lọc beta-2 hơn beta-1 (tỷ lệ ~10:1), nhưng vẫn có tác dụng tim mạch ở liều cao do kích thích beta-1 receptors. Ngoài ra, salbutamol ức chế phóng thích các chất trung gian gây viêm từ mast cells và giảm phù nề niêm mạc phế quản. Tác dụng nhanh (5-15 phút với dạng hít), ngắn (4-6 giờ), phù hợp cho cắt cơn hen cấp tính.",
        "monitoring": [
            "Nhịp tim, huyết áp (đặc biệt khi dùng IV hoặc liều cao) - có thể gây nhịp tim nhanh, tăng huyết áp",
            "Kali máu nếu dùng liều cao hoặc kéo dài (hạ kali máu do kích thích beta-2 → tăng kali vào tế bào)",
            "Đáp ứng phế quản (peak flow, FEV1, triệu chứng lâm sàng) để đánh giá hiệu quả",
            "Dấu hiệu quá liều: nhịp tim nhanh >120 bpm, run cơ nặng, loạn nhịp, đau ngực, khó thở nặng hơn",
            "Dấu hiệu nghịch lý: co thắt phế quản nặng hơn (hiếm nhưng nguy hiểm - cần ngừng ngay)",
            "Đường huyết nếu dùng liều cao (có thể tăng đường huyết do kích thích beta-2)",
            "Tần suất sử dụng (nếu cần dùng >4 lần/ngày → cần đánh giá lại điều trị và tăng ICS)"
        ],
        "precautions": [
            "Chỉ dùng khi cần (PRN) cho cắt cơn - không dùng thường xuyên như thuốc duy trì",
            "Nếu cần dùng >4 lần/ngày hoặc >8-12 puff/ngày → cần đánh giá lại điều trị và tăng liều ICS (inhaled corticosteroid)",
            "Tránh dùng với beta-blocker không chọn lọc (propranolol) - đối kháng tác dụng, có thể gây co thắt phế quản nặng",
            "Thận trọng ở bệnh nhân tim mạch, tăng huyết áp, loạn nhịp (tăng nguy cơ tác dụng tim mạch)",
            "Dùng liều thấp nhất hiệu quả để giảm tác dụng phụ (run, tim đập nhanh)",
            "Rửa miệng sau khi dùng dạng hít để giảm kích ứng và tránh nấm miệng (nếu dùng với ICS)",
            "Nếu không đáp ứng hoặc cần dùng thường xuyên → cần đánh giá lại chẩn đoán và điều trị",
            "Thận trọng với bệnh nhân cường giáp (tăng nhạy cảm với catecholamine)",
            "Thận trọng với bệnh nhân dùng digoxin (tăng nguy cơ loạn nhịp)",
            "Dùng liều cao có thể gây hạ kali máu - thận trọng với diuretics"
        ],
        "pharmacokinetics": {
            "half_life": "2-7 giờ (dạng hít), 2-4 giờ (IV), 3.8 giờ (PO)",
            "onset": "5-15 phút (dạng hít), 2-5 phút (IV), 30 phút (PO)",
            "duration": "4-6 giờ (dạng hít), 4-6 giờ (IV), 4-6 giờ (PO)",
            "protein_binding": "Không đáng kể",
            "clearance": "Gan: chuyển hóa qua sulfation và glucuronidation. Thận: bài tiết một phần nguyên dạng và metabolites. Dạng hít: tác dụng tại chỗ, hấp thu toàn thân ít. PO: hấp thu tốt nhưng tác dụng chậm hơn và nhiều tác dụng phụ hơn."
        },
        "storage": "Dạng hít (MDI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh đông lạnh. Kiểm tra xem có còn thuốc (lắc, nghe tiếng). Nebulizer solution: bảo quản ở nhiệt độ phòng, tránh ánh sáng, dùng trong vòng 1 tháng sau khi mở. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha. Syrup: bảo quản ở nhiệt độ phòng, đậy kín sau khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Beta-blockers (không chọn lọc: Propranolol, Nadolol)",
                    "mechanism": "Beta-blockers đối kháng tác dụng beta-2 của salbutamol, có thể gây co thắt phế quản nặng và làm giảm hiệu quả điều trị hen.",
                    "effect": "Đối kháng tác dụng giãn phế quản, có thể gây co thắt phế quản nặng, suy hô hấp",
                    "management": "TRÁNH DÙNG với beta-blocker không chọn lọc. Nếu bệnh nhân cần beta-blocker, dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng. Theo dõi chặt chẽ đáp ứng phế quản."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Salbutamol có thể gây hạ kali máu và tăng nhịp tim, tăng nguy cơ độc tính digoxin và loạn nhịp tim.",
                    "effect": "Tăng nguy cơ loạn nhịp tim, tăng độc tính digoxin (đặc biệt khi hạ kali máu)",
                    "management": "Theo dõi nồng độ digoxin và kali máu. Theo dõi ECG nếu có triệu chứng. Có thể cần điều chỉnh liều digoxin."
                },
                {
                    "drug": "Diuretics (Furosemide, Thiazide)",
                    "mechanism": "Cả hai đều có thể gây hạ kali máu, tăng nguy cơ hạ kali máu nghiêm trọng.",
                    "effect": "Tăng nguy cơ hạ kali máu nghiêm trọng, loạn nhịp tim, yếu cơ",
                    "management": "Theo dõi kali máu thường xuyên, đặc biệt khi dùng liều cao salbutamol. Bổ sung kali nếu cần."
                },
                {
                    "drug": "MAOIs (Phenelzine, Tranylcypromine)",
                    "mechanism": "MAOIs ức chế chuyển hóa catecholamine, có thể tăng tác dụng và tác dụng phụ của salbutamol.",
                    "effect": "Tăng tác dụng tim mạch, tăng huyết áp, tăng nguy cơ loạn nhịp",
                    "management": "Thận trọng, dùng liều thấp salbutamol. Theo dõi huyết áp và nhịp tim chặt chẽ."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Cả hai đều kích thích beta-adrenergic, có thể tăng tác dụng phụ và độc tính.",
                    "effect": "Tăng tác dụng phụ (run, tim đập nhanh, loạn nhịp), tăng nguy cơ độc tính theophylline",
                    "management": "Theo dõi nồng độ theophylline. Theo dõi nhịp tim và triệu chứng. Có thể cần giảm liều theophylline."
                }
            ],
            "minor": [
                {
                    "drug": "Tricyclic Antidepressants (TCA)",
                    "mechanism": "TCA tăng nhạy cảm với catecholamine, có thể tăng tác dụng tim mạch.",
                    "effect": "Tăng nhịp tim, tăng huyết áp (nhẹ)",
                    "management": "Theo dõi nhịp tim và huyết áp. Không cần điều chỉnh liều thường quy."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng salbutamol hoặc các thành phần trong chế phẩm",
                "Nhịp tim nhanh nặng không kiểm soát (>120 bpm ở người lớn, >150 bpm ở trẻ em)",
                "Rối loạn nhịp tim nặng (rung nhĩ, rung thất không kiểm soát)",
                "Cường giáp không điều trị (tăng nhạy cảm với catecholamine)"
            ],
            "relative": [
                "Bệnh tim mạch (suy tim, bệnh mạch vành) - thận trọng, theo dõi chặt chẽ",
                "Tăng huyết áp không kiểm soát - có thể tăng huyết áp",
                "Loạn nhịp tim nhẹ - có thể làm nặng",
                "Đái tháo đường - có thể tăng đường huyết",
                "Hạ kali máu - có thể làm nặng",
                "Cường giáp đang điều trị - thận trọng",
                "Dùng với digoxin - tăng nguy cơ loạn nhịp",
                "Dùng với MAOIs - tăng tác dụng tim mạch"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Salbutamol là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể có tác dụng phụ trên thai nhi, nhưng không có nghiên cứu đầy đủ trên người. Salbutamol được sử dụng rộng rãi trong thai kỳ để điều trị hen và có vẻ an toàn. Hen phế quản không kiểm soát có thể gây nguy hiểm cho cả mẹ và thai nhi (thiếu oxy, suy thai). Salbutamol có thể được dùng khi lợi ích vượt quá nguy cơ. Dạng hít được ưu tiên hơn dạng uống hoặc IV để giảm tác dụng toàn thân. Tránh dùng liều cao kéo dài trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Salbutamol bài tiết vào sữa mẹ ở nồng độ rất thấp. Dạng hít có hấp thu toàn thân tối thiểu, nồng độ trong sữa mẹ rất thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Dạng uống và IV có hấp thu toàn thân nhiều hơn nhưng vẫn an toàn.",
                "recommendation": "Có thể dùng khi cho con bú. Dạng hít được ưu tiên. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Salbutamol chuyển hóa qua gan nhưng không phụ thuộc nhiều vào chức năng gan.",
            "moderate": "Không cần điều chỉnh liều. Theo dõi tác dụng phụ nếu có.",
            "severe": "Thận trọng, có thể cần giảm liều. Theo dõi tác dụng phụ chặt chẽ. Chuyển hóa có thể giảm ở suy gan nặng.",
            "notes": "Salbutamol chuyển hóa chủ yếu qua gan (sulfation, glucuronidation). Suy gan nặng có thể làm giảm chuyển hóa, tăng thời gian bán thải, nhưng ít khi cần điều chỉnh liều vì dạng hít có tác dụng tại chỗ."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tim mạch: Nhịp tim nhanh (>120-150 bpm), đánh trống ngực, loạn nhịp tim, đau ngực, tăng huyết áp",
                "Triệu chứng thần kinh: Run cơ nặng, kích động, lo âu, mất ngủ, đau đầu, chóng mặt",
                "Triệu chứng chuyển hóa: Hạ kali máu (do kích thích beta-2 → tăng kali vào tế bào), tăng đường huyết, toan chuyển hóa (hiếm)",
                "Triệu chứng hô hấp: Co thắt phế quản nghịch lý (hiếm nhưng nguy hiểm - khó thở nặng hơn), suy hô hấp",
                "Triệu chứng nghiêm trọng: Rung nhĩ, rung thất, sốc, suy tim cấp (với liều rất cao)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blocker chọn lọc có thể đối kháng tác dụng nhưng thận trọng vì có thể gây co thắt phế quản.",
            "treatment": [
                "Ngừng ngay salbutamol",
                "Theo dõi dấu hiệu sinh tồn: Nhịp tim, huyết áp, nhịp thở, SpO2, ECG",
                "Điều trị hỗ trợ: Nghỉ ngơi, trấn an, hỗ trợ hô hấp nếu cần",
                "Điều chỉnh điện giải: Bổ sung kali nếu hạ kali máu (theo dõi kali máu)",
                "Điều trị loạn nhịp: Nếu có rối loạn nhịp tim nghiêm trọng, cân nhắc dùng beta-blocker chọn lọc beta-1 (atenolol, metoprolol) với thận trọng (có thể gây co thắt phế quản)",
                "Điều trị hạ huyết áp nếu có: Truyền dịch, nếu cần dùng thuốc vận mạch (thận trọng với thuốc kích thích beta)",
                "Theo dõi đường huyết: Điều chỉnh nếu tăng đường huyết",
                "Điều trị co thắt phế quản nghịch lý: Ngừng salbutamol, dùng ipratropium hoặc corticosteroid",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG, kali máu, đường huyết trong ít nhất 4-6 giờ. Theo dõi lâu hơn nếu có biến chứng tim mạch hoặc loạn nhịp."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ.",
                "timing": "Uống 3-4 lần/ngày, cách đều. Có thể uống trước hoặc sau bữa ăn. Lưu ý: Dạng uống có nhiều tác dụng phụ hơn dạng hít, nên ưu tiên dạng hít khi có thể."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1-5mcg/ml. Pha 1mg (1ml) trong 100ml dịch = 10mcg/ml. Pha 5mg (5ml) trong 500ml dịch = 10mcg/ml.",
                "infusion_rate": "Bolus: 5mcg/kg IV trong 1-2 phút. Truyền liên tục: 0.5-5mcg/kg/phút. Bắt đầu với liều thấp, tăng dần theo đáp ứng. Tốc độ: Ví dụ 70kg, 1mcg/kg/phút = 70mcg/phút = 4.2mg/giờ. Pha 5mg trong 500ml = 10mcg/ml → 70mcg/phút = 7ml/phút = 420ml/giờ.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với thuốc có tính kiềm."],
                "notes": "Chỉ dùng IV trong cấp cứu hen nặng. Theo dõi chặt chẽ nhịp tim, huyết áp, ECG. Dùng liều thấp nhất hiệu quả. Có thể gây hạ kali máu với liều cao - theo dõi kali máu."
            },
            "inhalation": {
                "technique": "MDI: Lắc kỹ, thở ra hết, đặt ống ngậm vào miệng, bắt đầu hít vào chậm và sâu, bấm thuốc, tiếp tục hít vào đến khi đầy phổi, giữ hơi 10 giây, thở ra chậm. Đợi 30-60 giây trước khi bấm lần thứ 2. Spacer: Dùng với MDI để tăng hiệu quả và giảm tác dụng phụ (đặc biệt ở trẻ em và người cao tuổi).",
                "nebulizer": "Pha 2.5-5mg trong 2-4ml NS hoặc nước cất. Thở bình thường qua mask hoặc ống ngậm. Thời gian: 5-15 phút. Rửa miệng sau khi dùng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Albuterol (Salbutamol)",
                "GINA 2023 Guidelines - Global Initiative for Asthma",
                "UpToDate - Albuterol: Drug Information",
                "Medscape - Albuterol Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Albuterol Monograph",
                "Micromedex - Albuterol Drug Information"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, GINA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Budesonide": {
        "group": "Respiratory - Corticosteroid (Inhaled)",
        "vietnamese_name": "Budesonide inhaled, Pulmicort",
        "administration": ["INH", "NEB"],
        "indications": [
            "Hen phế quản (duy trì)",
            "COPD",
            "Viêm mũi dị ứng",
            "Hen phế quản (trẻ em)"
        ],
        "contraindications": [
            "Dị ứng budesonide",
            "Nhiễm trùng đường hô hấp không điều trị"
        ],
        "dosage": {
            "adult_inh": "200-800mcg x 2 lần/ngày",
            "adult_neb": "0.5-1mg nebulizer x 2 lần/ngày",
            "pediatric_inh": "100-400mcg x 2 lần/ngày (theo tuổi)",
            "pediatric_neb": "0.25-0.5mg nebulizer x 2 lần/ngày",
            "notes": "Súc miệng sau khi dùng để tránh nấm miệng. Có dạng nebulizer cho trẻ em"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Nấm miệng (candida - phổ biến nếu không súc miệng)",
            "Khàn tiếng",
            "Ho",
            "Kích ứng họng",
            "Tác dụng toàn thân (hiếm với liều thường)"
        ],
        "interactions": [
            "Ketoconazole/Itraconazole: tăng nồng độ budesonide",
            "Ritonavir: tăng nồng độ budesonide"
        ],
        "pregnancy": "C - An toàn",
        "mechanism_of_action": "Budesonide là corticosteroid hít (inhaled corticosteroid, ICS) có tác dụng kháng viêm mạnh tại chỗ. Budesonide gắn vào glucocorticoid receptor trong tế bào, sau đó di chuyển vào nhân và gắn vào glucocorticoid response elements (GRE) trên DNA, kích hoạt hoặc ức chế biểu hiện gen. Dẫn đến: ức chế tổng hợp các cytokine gây viêm (IL-1, IL-2, IL-4, IL-5, TNF-α), giảm phóng thích các chất trung gian gây viêm từ mast cells và eosinophils, giảm thâm nhập tế bào viêm, giảm phù nề niêm mạc phế quản, và tăng số lượng beta-2 receptors. Budesonide có tác dụng chủ yếu tại chỗ (phế quản), ít hấp thu toàn thân nên ít tác dụng phụ toàn thân. Tuy nhiên, một phần nhỏ vẫn được hấp thu và có thể gây tác dụng toàn thân ở liều cao. Budesonide được chuyển hóa nhanh ở gan (first-pass metabolism cao) nên tác dụng toàn thân ít hơn so với corticosteroid uống.",
        "monitoring": [
            "Đáp ứng điều trị (giảm triệu chứng hen, tần suất cơn cấp, nhu cầu dùng SABA)",
            "Nấm miệng (candidiasis) - kiểm tra lưỡi, miệng, đặc biệt nếu không súc miệng sau khi dùng",
            "Khàn tiếng, ho, kích ứng họng - tác dụng phụ tại chỗ phổ biến",
            "Tác dụng toàn thân (chỉ ở liều cao): ức chế trục HPA, chậm phát triển ở trẻ em, loãng xương, tăng huyết áp",
            "Chức năng gan nếu có triệu chứng (hiếm)",
            "Tương tác với ritonavir, ketoconazole, itraconazole (tăng nồng độ budesonide)"
        ],
        "precautions": [
            "Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng (candidiasis) - QUAN TRỌNG",
            "Không dùng cho cắt cơn cấp - cần SABA (salbutamol) cho cơn cấp, budesonide là thuốc duy trì",
            "Tác dụng phát huy sau vài ngày đến vài tuần - không mong đợi tác dụng tức thì",
            "Không ngừng đột ngột - giảm liều dần dần",
            "Tác dụng toàn thân hiếm với liều thường nhưng có thể xảy ra ở liều cao (>1600mcg/ngày)",
            "Thận trọng với bệnh nhân lao phổi, nhiễm trùng đường hô hấp - cần điều trị nhiễm trùng trước",
            "Tránh dùng với ritonavir (tăng đáng kể nồng độ budesonide, tăng nguy cơ ức chế HPA)",
            "Thận trọng với ketoconazole, itraconazole (tăng nồng độ budesonide)",
            "Theo dõi chậm phát triển ở trẻ em nếu dùng liều cao",
            "Có thể dùng cho trẻ em (có dạng nebulizer)",
            "Dùng đều đặn hàng ngày, không phải khi cần"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (trong phổi), 4-6 giờ (toàn thân sau hấp thu)",
            "onset": "Vài giờ đến vài ngày (tác dụng kháng viêm)",
            "duration": "12-24 giờ (dùng 2 lần/ngày)",
            "protein_binding": "88-90%",
            "clearance": "Gan: chuyển hóa nhanh qua CYP3A4 (first-pass metabolism cao, ~85-90% bị chuyển hóa). Thận: bài tiết một phần metabolites. Hấp thu toàn thân ít do chuyển hóa nhanh ở gan. Phần lớn tác dụng tại chỗ (phế quản)."
        },
        "storage": "Dạng hít (MDI/DPI): bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng trực tiếp. Không đông lạnh. Nebulizer suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng, dùng trong vòng 2 giờ sau khi mở gói. Bảo quản trong tủ lạnh nếu không dùng ngay (2-8°C), để nhiệt độ phòng trước khi dùng.",
        "black_box_warnings": None
    },
    "Amoxicillin suspension": {
        "group": "Antibiotic - Beta-lactam (Penicillin)",
        "vietnamese_name": "Amoxicillin suspension, Amoxicillin sirô",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn tai mũi họng",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da mô mềm",
            "Helicobacter pylori (phối hợp)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "pediatric_otitis": "80-90mg/kg/ngày chia 2 lần (10 ngày)",
            "pediatric_pneumonia": "80-100mg/kg/ngày chia 3-4 lần",
            "pediatric_uti": "25-50mg/kg/ngày chia 3 lần",
            "pediatric_suspension_common": "20-40mg/kg/ngày chia 2-3 lần",
            "notes": "Có dạng suspension 125mg/5ml, 250mg/5ml cho trẻ em. Uống với hoặc không thức ăn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều hoặc tăng khoảng cách",
            "under_30": "Liều thấp hơn, khoảng cách dài hơn"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn",
            "Phát ban",
            "Nhiễm trùng nấm Candida",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Methotrexate: tăng độc tính",
            "Allopurinol: tăng nguy cơ phát ban",
            "Thuốc tránh thai: có thể giảm hiệu quả"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Amoxicillin là aminopenicillin (beta-lactam antibiotic), ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs) trên màng tế bào vi khuẩn. Amoxicillin là chất tương tự penicillin nhưng có nhóm amin, giúp tăng khả năng xuyên qua màng ngoài của vi khuẩn Gram-âm và tăng phổ kháng khuẩn. Amoxicillin ức chế enzyme transpeptidase, ngăn chặn liên kết chéo giữa các chuỗi peptidoglycan trong thành tế bào vi khuẩn, dẫn đến làm suy yếu và vỡ thành tế bào khi vi khuẩn phân chia. Amoxicillin có phổ kháng khuẩn rộng: Gram-dương (Streptococcus, Enterococcus, một số Staphylococcus không kháng penicillinase), Gram-âm (H. influenzae, E. coli, Proteus mirabilis, Salmonella, Shigella), và một số kỵ khí. Không hiệu quả với vi khuẩn tiết beta-lactamase (cần kết hợp với clavulanate). Dạng suspension phù hợp cho trẻ em, dễ uống và hấp thu tốt.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng: sốt, WBC, CRP (theo dõi đáp ứng điều trị)",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để đánh giá hiệu quả",
            "Dấu hiệu dị ứng: phát ban, mề đay, khó thở, sốc phản vệ (đặc biệt ở lần đầu tiên dùng)",
            "Tiêu chảy (phổ biến, có thể là nhiễm C. difficile nếu nặng)",
            "Chức năng thận (creatinine) nếu dùng liều cao hoặc suy thận",
            "Dấu hiệu nhiễm C. difficile: tiêu chảy nặng, đau bụng, sốt (cần ngừng và điều trị)",
            "Chức năng gan (ALT, AST) nếu có triệu chứng (hiếm)",
            "Công thức máu (giảm bạch cầu, thiếu máu hiếm)",
            "INR nếu dùng với warfarin (tăng nguy cơ chảy máu)"
        ],
        "precautions": [
            "Không dùng ở bệnh nhân dị ứng penicillin hoặc beta-lactam (phản ứng chéo với cephalosporin ~5-10%)",
            "Lắc kỹ suspension trước khi dùng (thuốc lắng xuống đáy)",
            "Có thể uống với hoặc không thức ăn (hấp thu tốt)",
            "Dùng đủ liều và đủ thời gian (thường 7-10 ngày) để tránh kháng thuốc",
            "Thận trọng ở bệnh nhân suy thận (giảm liều hoặc tăng khoảng cách)",
            "Thận trọng ở bệnh nhân có tiền sử nhiễm C. difficile (tăng nguy cơ tái phát)",
            "Thận trọng với allopurinol (tăng nguy cơ phát ban)",
            "Thận trọng với methotrexate (amoxicillin làm giảm thải trừ methotrexate, tăng độc tính)",
            "Có thể giảm hiệu quả thuốc tránh thai (dùng biện pháp dự phòng)",
            "Theo dõi tiêu chảy - nếu nặng hoặc kéo dài, có thể là nhiễm C. difficile",
            "Dùng đúng liều theo cân nặng ở trẻ em (tính theo mg/kg)"
        ],
        "pharmacokinetics": {
            "half_life": "1-1.5 giờ",
            "onset": "1-2 giờ (đạt nồng độ đỉnh trong máu)",
            "duration": "6-8 giờ (dùng 2-3 lần/ngày)",
            "protein_binding": "20%",
            "clearance": "Thận: bài tiết chủ yếu qua nước tiểu (không thay đổi, 60-70% trong 6-8 giờ). Một phần nhỏ qua mật. Hấp thu tốt qua đường uống (75-90%), không bị ảnh hưởng bởi thức ăn. Dạng suspension hấp thu tương tự viên nén."
        },
        "storage": "Bảo quản suspension ở nhiệt độ phòng (15-30°C) hoặc trong tủ lạnh (2-8°C) - theo hướng dẫn trên nhãn. Lắc kỹ trước khi dùng. Sau khi pha (nếu là bột pha nước): bảo quản trong tủ lạnh (2-8°C), dùng trong vòng 7-14 ngày (theo hướng dẫn). Tránh đông lạnh. Để nơi khô ráo, tránh ánh sáng trực tiếp, tránh xa tầm tay trẻ em.",
        "black_box_warnings": None
    },
"Rosuvastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Rosuvastatin, Crestor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Phòng ngừa biến cố tim mạch",
            "Hội chứng chuyển hóa"
        ],
        "contraindications": [
            "Dị ứng rosuvastatin",
            "Bệnh gan hoạt động",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_start": "5-10mg x 1 lần/ngày (tối)",
            "adult_usual": "10-20mg x 1 lần/ngày",
            "adult_max": "40mg x 1 lần/ngày",
            "notes": "Uống với hoặc không thức ăn. Mạnh hơn atorvastatin ở liều tương đương"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Bắt đầu với 5mg/ngày"
        },
        "side_effects": [
            "Đau cơ, yếu cơ",
            "Tăng transaminase",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Đau đầu",
            "Táo bón",
            "Đái tháo đường (nguy cơ tăng nhẹ)"
        ],
        "interactions": [
            "Cyclosporine: tăng nguy cơ độc tính",
            "Gemfibrozil: tăng nguy cơ độc cơ",
            "Warfarin: tăng INR",
            "Rifampin: giảm nồng độ rosuvastatin"
        ],
        "pregnancy": "X - Chống chỉ định",
        "mechanism_of_action": "Statin (HMG-CoA reductase inhibitor). Ức chế không chọn lọc enzyme HMG-CoA reductase trong gan, enzyme chính trong tổng hợp cholesterol. Giảm tổng hợp cholesterol nội sinh → tăng số lượng LDL receptors trên bề mặt tế bào gan → tăng thanh thải LDL từ máu. Giảm LDL cholesterol, giảm triglyceride, tăng nhẹ HDL cholesterol. Có tác dụng chống viêm và ổn định mảng xơ vữa (pleiotropic effects). Được dùng trong tăng cholesterol máu, dự phòng biến cố tim mạch (nhồi máu cơ tim, đột quỵ).",
        "monitoring": [
            "Lipid profile (LDL, HDL, triglyceride, total cholesterol) - kiểm tra 4-12 tuần sau khi bắt đầu, sau đó định kỳ",
            "Chức năng gan (ALT, AST) - tăng men gan (thường nhất thời), hiếm viêm gan",
            "CK (creatine kinase) - tăng CK, dấu hiệu tiêu cơ vân (myopathy, rhabdomyolysis)",
            "Dấu hiệu tiêu cơ vân (đau cơ, yếu cơ, nước tiểu sẫm màu) - nguy hiểm",
            "Đường huyết (có thể tăng nhẹ đường huyết)",
            "HbA1c (tăng nguy cơ đái tháo đường type 2)"
        ],
        "precautions": [
            "Nguy cơ tiêu cơ vân (myopathy, rhabdomyolysis) - nguy hiểm, có thể gây suy thận cấp",
            "Nguy cơ tăng ở: liều cao, suy thận, suy gan, người cao tuổi, dùng với fibrate, niacin, cyclosporine, diltiazem, verapamil",
            "NGỪNG NGAY nếu có đau cơ, yếu cơ, CK tăng > 10 lần ULN, hoặc dấu hiệu tiêu cơ vân",
            "Nguy cơ tăng men gan - kiểm tra ALT/AST trước khi bắt đầu, sau 12 tuần, và định kỳ",
            "Tăng nguy cơ đái tháo đường type 2 (nhẹ)",
            "Không dùng trong thai kỳ (gây dị tật thai nhi) - dùng biện pháp tránh thai",
            "Không dùng ở suy gan hoạt động",
            "Tương tác với nhiều thuốc: cyclosporine, gemfibrozil, diltiazem, verapamil → tăng nguy cơ tiêu cơ vân",
            "Liều khởi đầu thường: 10-20mg/ngày, liều tối đa: 40mg/ngày",
            "Uống với hoặc không có thức ăn"
        ],
        "pharmacokinetics": {
            "half_life": "19 giờ (dài)",
            "onset": "1-2 tuần (giảm LDL)",
            "duration": "Dài (nhiều ngày)",
            "protein_binding": "88%",
            "metabolism": "Gan (CYP2C9, CYP2C19) - chuyển hóa yếu, ít tương tác hơn các statin khác",
            "clearance": "Chủ yếu qua gan (90%), một phần qua thận (10%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Viên nén: tránh ẩm.",
        "black_box_warnings": "Nguy cơ tiêu cơ vân (rhabdomyolysis), có thể gây suy thận cấp và tử vong. Nguy cơ tăng ở liều cao, suy thận, và dùng với một số thuốc. Ngừng ngay nếu có đau cơ, yếu cơ, hoặc dấu hiệu tiêu cơ vân. Không dùng trong thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cyclosporine ức chế OATP1B1 transporter và P-glycoprotein, tăng nồng độ rosuvastatin đáng kể",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng, có thể gây suy thận cấp, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu cần: giảm liều rosuvastatin tối đa 5mg/ngày, theo dõi CK và men gan thường xuyên. Cân nhắc dùng pravastatin (ít tương tác hơn)."
                },
                {
                    "drug": "Gemfibrozil, Fenofibrate (fibrates)",
                    "mechanism": "Fibrates và rosuvastatin đều có thể gây độc cơ, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể. Nếu cần: dùng liều thấp cả hai, theo dõi CK và dấu hiệu đau cơ thường xuyên. KHÔNG dùng gemfibrozil với rosuvastatin (tăng nguy cơ cao). Có thể cân nhắc fenofibrate (ít tương tác hơn gemfibrozil)."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Rosuvastatin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên khi bắt đầu hoặc thay đổi liều rosuvastatin. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Diltiazem, Verapamil",
                    "mechanism": "Có thể tăng nhẹ nồng độ rosuvastatin qua OATP1B1",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Giảm liều rosuvastatin 50% hoặc tối đa 10mg/ngày. Theo dõi CK và dấu hiệu đau cơ."
                },
                {
                    "drug": "Niacin (liều cao)",
                    "mechanism": "Cả hai đều có thể gây độc cơ, tác dụng hiệp đồng",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Theo dõi CK và dấu hiệu đau cơ thường xuyên. Có thể cần giảm liều một trong hai thuốc."
                },
                {
                    "drug": "Colchicine",
                    "mechanism": "Có thể tăng tác dụng phụ độc cơ",
                    "effect": "Tăng nguy cơ độc cơ, đặc biệt ở bệnh nhân suy thận",
                    "management": "Thận trọng, đặc biệt ở bệnh nhân suy thận. Theo dõi CK và dấu hiệu đau cơ. Có thể cần giảm liều một trong hai thuốc."
                }
            ],
            "minor": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng OATP1B1, giảm hấp thu rosuvastatin",
                    "effect": "Giảm hiệu quả rosuvastatin",
                    "management": "Có thể cần tăng liều rosuvastatin. Theo dõi lipid profile."
                },
                {
                    "drug": "Oral contraceptives",
                    "mechanism": "Rosuvastatin có thể tăng nhẹ nồng độ estrogen",
                    "effect": "Tăng nhẹ tác dụng phụ của thuốc tránh thai",
                    "management": "Thường không cần điều chỉnh. Theo dõi tác dụng phụ."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                "Dị ứng với rosuvastatin hoặc bất kỳ thành phần nào",
                "Dùng cùng cyclosporine (tăng nguy cơ tiêu cơ vân nghiêm trọng)"
            ],
            "relative": [
                "Suy thận nặng (CrCl <30) - bắt đầu với liều thấp (5mg/ngày)",
                "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                "Uống rượu nhiều - tăng nguy cơ viêm gan",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                "Dùng với fibrate, niacin liều cao - tăng nguy cơ tiêu cơ vân",
                "Bệnh nhân Châu Á - tăng nồng độ rosuvastatin, có thể cần liều thấp hơn"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Rosuvastatin gây dị tật thai nhi, đặc biệt trong tam cá nguyệt đầu tiên. Statins ức chế tổng hợp cholesterol, cần thiết cho sự phát triển của thai nhi. Có thể gây dị tật bẩm sinh, chậm phát triển. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả. Phải ngừng rosuvastatin ít nhất 1-2 tháng trước khi có thai. Nếu có thai khi đang dùng, ngừng ngay lập tức.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Rosuvastatin bài tiết vào sữa mẹ. Có thể gây tác dụng phụ trên trẻ bú mẹ. Chưa có dữ liệu đầy đủ về an toàn. Statins có thể ảnh hưởng đến sự phát triển của trẻ.",
                "recommendation": "CHỐNG CHỈ ĐỊNH khi cho con bú. Ngừng rosuvastatin hoặc ngừng cho con bú. Cân nhắc thuốc thay thế nếu cần."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều. Theo dõi men gan thường xuyên.",
            "moderate": "Thận trọng. Giảm liều hoặc dùng liều thấp hơn. Theo dõi men gan mỗi 3-6 tháng. Ngừng nếu ALT >3 lần ULN.",
            "severe": "CHỐNG CHỈ ĐỊNH. Không dùng ở bệnh nhân suy gan nặng hoặc bệnh gan hoạt động.",
            "notes": "Rosuvastatin chuyển hóa qua gan (CYP2C9, CYP2C19) - chuyển hóa yếu hơn atorvastatin/simvastatin, ít tương tác hơn. Tuy nhiên, suy gan vẫn có thể làm tăng nồng độ và tăng nguy cơ độc tính. Kiểm tra men gan trước điều trị. Ngừng nếu ALT >3 lần ULN hoặc có dấu hiệu viêm gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu cơ vân (rhabdomyolysis) - triệu chứng chính và nguy hiểm nhất",
                "Đau cơ dữ dội, yếu cơ",
                "Nước tiểu sẫm màu (myoglobinuria)",
                "Suy thận cấp (do myoglobin)",
                "Tăng men gan (ALT, AST)",
                "Tăng CK (creatine kinase)",
                "Mệt mỏi, buồn nôn",
                "Rối loạn tiêu hóa"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng rosuvastatin, truyền dịch tích cực để phòng suy thận, lọc máu nếu cần",
            "treatment": [
                "Ngừng rosuvastatin ngay lập tức",
                "Đo CK, men gan, chức năng thận ngay",
                "Nếu có tiêu cơ vân:",
                "  - Truyền dịch tích cực (normal saline 1-2L/giờ) để duy trì lượng nước tiểu >100-200ml/giờ",
                "  - Kiềm hóa nước tiểu (sodium bicarbonate) để giảm độc tính myoglobin trên thận",
                "  - Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu)",
                "  - Hemodialysis nếu suy thận cấp, tăng kali máu, hoặc quá tải dịch",
                "  - Theo dõi điện giải (natri, kali, canxi, phosphate)",
                "Điều trị hỗ trợ:",
                "  - Điều chỉnh rối loạn điện giải",
                "  - Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "  - Giảm đau (opioids) nếu đau cơ nặng",
                "Theo dõi CK, men gan, chức năng thận hàng ngày cho đến khi ổn định",
                "Theo dõi ít nhất 48-72 giờ do half-life 19 giờ (dài)"
            ],
            "monitoring": "CK, ALT, AST, creatinine, BUN, kali, canxi, phosphate, lượng nước tiểu, ECG (nếu có rối loạn điện giải), dấu hiệu suy thận"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, có thể uống vào buổi sáng hoặc buổi tối. Uống cùng một giờ mỗi ngày để nhớ. Không cần thiết phải uống buổi tối như simvastatin (rosuvastatin có half-life dài 19 giờ)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Rosuvastatin chỉ có dạng uống (PO)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Crestor (rosuvastatin)",
                "UpToDate - Rosuvastatin: Drug information",
                "ACC/AHA Guidelines - Cholesterol Management (2018)",
                "NLA Guidelines - Statin Safety (2014)",
                "JUPITER Study - New England Journal of Medicine (2008) - Rosuvastatin trong dự phòng biến cố tim mạch",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics - Lipid-lowering drugs"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (JUPITER, CORONA) showing cardiovascular benefit"
        }
    },
    "Enalaprilat": {
        "group": "Cardiovascular - ACE Inhibitor (IV)",
        "vietnamese_name": "Enalaprilat, Enalapril IV",
        "administration": ["IV"],
        "indications": [
            "Tăng huyết áp cấp cứu",
            "Suy tim cấp",
            "Khi không uống được"
        ],
        "contraindications": [
            "Dị ứng ACE inhibitor",
            "Có thai",
            "Hẹp động mạch thận 2 bên"
        ],
        "dosage": {
            "adult_htn": "0.625-1.25mg IV mỗi 6 giờ",
            "adult_heart_failure": "0.625mg IV mỗi 6 giờ, tăng dần đến 1.25mg mỗi 6 giờ",
            "notes": "Khởi đầu với liều thấp, theo dõi huyết áp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "under_30": "Thận trọng, giảm liều 50%"
        },
        "side_effects": [
            "Hạ huyết áp (phổ biến)",
            "Ho khan",
            "Tăng kali máu",
            "Phù mạch",
            "Suy thận cấp"
        ],
        "interactions": [
            "Kali: tăng kali máu",
            "Diuretics: tăng nguy cơ hạ huyết áp",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Enalaprilat là dạng hoạt chất của enalapril (enalapril là prodrug, chuyển hóa thành enalaprilat trong gan). Enalaprilat ức chế angiotensin converting enzyme (ACE), enzyme chuyển angiotensin I thành angiotensin II. Angiotensin II là chất co mạch mạnh và kích thích tiết aldosterone. Bằng cách ức chế ACE, enalaprilat giảm nồng độ angiotensin II, dẫn đến: giãn mạch (giảm sức cản mạch máu ngoại biên), giảm aldosterone (giảm tái hấp thu natri và nước ở thận, tăng bài tiết kali), giảm tiền gánh và hậu gánh tim, và giảm huyết áp. Enalaprilat cũng ức chế phân hủy bradykinin (chất giãn mạch), có thể góp phần vào tác dụng hạ huyết áp nhưng cũng gây ho khan (tác dụng phụ). Dạng IV tác dụng nhanh hơn enalapril uống, phù hợp cho cấp cứu tăng huyết áp và suy tim cấp.",
        "monitoring": [
            "Huyết áp liên tục (đặc biệt trong 30-60 phút đầu sau liều đầu tiên) - nguy cơ hạ huyết áp đột ngột",
            "Kali máu (tăng kali máu do giảm aldosterone) - theo dõi định kỳ",
            "Creatinine và eGFR (suy thận cấp có thể xảy ra, đặc biệt ở bệnh nhân hẹp động mạch thận)",
            "Dấu hiệu phù mạch (angioedema): sưng mặt, môi, lưỡi, họng - cấp cứu, cần ngừng ngay",
            "Dấu hiệu ho khan (tác dụng phụ phổ biến, có thể dai dẳng)",
            "Nhịp tim và ECG (đặc biệt nếu có tiền sử rối loạn nhịp)",
            "Dấu hiệu suy tim: khó thở, phù, tăng cân"
        ],
        "precautions": [
            "Khởi đầu với liều thấp (0.625mg) và theo dõi huyết áp sát trong 30-60 phút đầu",
            "Nguy cơ hạ huyết áp đột ngột cao hơn so với enalapril uống (tác dụng nhanh hơn)",
            "Thận trọng ở bệnh nhân đang dùng diuretics (tăng nguy cơ hạ huyết áp) - có thể tạm ngừng diuretic trước khi bắt đầu",
            "Thận trọng ở bệnh nhân hẹp động mạch thận (có thể gây suy thận cấp)",
            "Thận trọng ở bệnh nhân suy thận (giảm liều, theo dõi creatinine)",
            "Thận trọng ở bệnh nhân đang dùng kali hoặc kali-sparing diuretics (tăng nguy cơ tăng kali máu)",
            "Tránh dùng với NSAID (giảm hiệu quả, tăng nguy cơ suy thận)",
            "Theo dõi phù mạch (angioedema) - có thể xảy ra ngay sau liều đầu tiên hoặc sau vài giờ",
            "Chuyển sang enalapril uống khi bệnh nhân có thể uống được",
            "Không dùng trong thai kỳ (chống chỉ định tuyệt đối - gây dị tật thai nhi)",
            "Thận trọng ở bệnh nhân có tiền sử phù mạch với ACE inhibitor khác"
        ],
        "pharmacokinetics": {
            "half_life": "11 giờ (enalaprilat, dài hơn enalapril)",
            "onset": "15 phút (IV, nhanh hơn enalapril uống)",
            "duration": "6 giờ (tiêm mỗi 6 giờ)",
            "protein_binding": "50-60%",
            "clearance": "Thận: bài tiết chủ yếu qua nước tiểu (không cần chuyển hóa như enalapril). Thời gian bán thải dài (11 giờ) so với enalapril (1 giờ) vì enalaprilat là chất chuyển hóa cuối cùng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Sau khi pha: dùng ngay, không bảo quản lâu. Theo hướng dẫn của nhà sản xuất về thời gian sử dụng sau khi pha.",
        "black_box_warnings": "Chống chỉ định trong thai kỳ - có thể gây tổn thương thai nhi và tử vong khi dùng trong tam cá nguyệt thứ hai và thứ ba. Phù mạch (angioedema) có thể xảy ra bất cứ lúc nào, có thể đe dọa tính mạng, cần ngừng ngay và điều trị cấp cứu."
    },
    "Ceftriaxone": {
        "group": "Antibiotic - Cephalosporin (3rd Generation)",
        "vietnamese_name": "Ceftriaxone, Rocephin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn nặng",
            "Viêm màng não",
            "Nhiễm khuẩn bệnh viện",
            "Nhiễm khuẩn đường tiết niệu",
            "Viêm phổi"
        ],
        "contraindications": [
            "Dị ứng cephalosporin hoặc penicillin (thận trọng)",
            "Trẻ sơ sinh <28 ngày với Ca IV"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM mỗi 24 giờ",
            "adult_severe": "2-4g IV mỗi 24 giờ",
            "adult_meningitis": "2g IV mỗi 12 giờ",
            "pediatric_standard": "50-75mg/kg IV/IM mỗi 24 giờ (tối đa 2g)",
            "pediatric_meningitis": "80-100mg/kg IV mỗi 12-24 giờ (tối đa 4g/ngày)",
            "notes": "Thời gian bán hủy dài, dùng 1 lần/ngày. Có thể gây kết tủa với Ca ở trẻ sơ sinh"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua mật)",
            "under_30": "Giảm liều nếu CrCl <10 và suy gan"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Tăng transaminase",
            "Viêm túi mật (hiếm)",
            "Giảm bạch cầu (hiếm)",
            "Sỏi mật (với liều cao dài ngày)"
        ],
        "interactions": [
            "Warfarin: tăng INR",
            "Calcium IV: kết tủa (trẻ sơ sinh)",
            "Probenecid: tăng nồng độ ceftriaxone"
        ],
        "pregnancy": "B - An toàn",
        "mechanism_of_action": "Cephalosporin thế hệ 3, phổ rộng. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (một số), Gram-âm mạnh (Enterobacteriaceae, Neisseria, H. influenzae), và một số kỵ khí. Kháng được nhiều beta-lactamase do có cấu trúc vòng beta-lactam bền vững. Không hiệu quả với Pseudomonas aeruginosa, Enterococcus, hoặc MRSA. Thời gian bán thải dài (6-9 giờ) → chỉ cần tiêm 1 lần/ngày.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST, bilirubin) - có thể tăng, hiếm sỏi mật",
            "Sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao",
            "Chức năng thận (creatinine) - không cần điều chỉnh thận nhưng theo dõi",
            "Dấu hiệu nhiễm C. difficile",
            "Co giật (hiếm, nhưng có thể ở suy thận nặng)",
            "Phản ứng tại chỗ tiêm (đau, viêm tĩnh mạch)"
        ],
        "precautions": [
            "KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV (nguy cơ kết tủa ceftriaxone-calcium trong phổi, thận) - có thể tử vong",
            "Nguy cơ sỏi mật (ceftriaxone-calcium complex) - đặc biệt ở trẻ em, dùng liều cao, dùng kéo dài",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~5-10%)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Có thể gây tăng bilirubin (nhất thời, do đẩy bilirubin khỏi albumin)",
            "Pha trong NS, D5W, hoặc LR, tiêm IV hoặc IM",
            "Tiêm IM: pha với lidocaine 1% để giảm đau",
            "Không pha trộn với các thuốc khác (tương kỵ với nhiều thuốc, đặc biệt vancomycin, calcium)",
            "Thời gian bán thải dài → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h)"
        ],
        "pharmacokinetics": {
            "half_life": "6-9 giờ (rất dài cho cephalosporin)",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "24 giờ (liều 1-2g q24h), 12 giờ (viêm màng não: 2g q12h)",
            "protein_binding": "85-95% (rất cao)",
            "metabolism": "Không chuyển hóa, bài tiết nguyên dạng",
            "clearance": "40% qua thận, 60% qua mật (độc nhất trong cephalosporin) → không cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 10 ngày. Không đông lạnh.",
        "black_box_warnings": "KHÔNG dùng ở trẻ sơ sinh < 28 ngày tuổi nếu đang dùng calci IV - có thể gây kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong. Tránh dùng calci IV trong 48 giờ sau liều ceftriaxone cuối cùng ở trẻ sơ sinh.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium IV (đặc biệt ở trẻ sơ sinh < 28 ngày)",
                    "mechanism": "Ceftriaxone tạo phức hợp không hòa tan với calci, gây kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong.",
                    "effect": "Kết tủa ceftriaxone-calcium trong phổi, thận, có thể tử vong (đặc biệt ở trẻ sơ sinh)",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI: Không dùng ceftriaxone ở trẻ sơ sinh < 28 ngày nếu đang dùng calci IV. Tránh dùng calci IV trong 48 giờ sau liều ceftriaxone cuối cùng ở trẻ sơ sinh. Ở người lớn, tránh pha chung trong cùng một ống truyền, truyền riêng biệt."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Ceftriaxone có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể đẩy warfarin khỏi albumin (protein binding cao).",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng ceftriaxone). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân suy gan, dùng kéo dài (>7 ngày)."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của ceftriaxone, làm giảm thải trừ và tăng nồng độ ceftriaxone.",
                    "effect": "Tăng nồng độ ceftriaxone, tăng thời gian bán thải",
                    "management": "Có thể cần giảm liều ceftriaxone. Theo dõi chức năng thận. Thường không cần điều chỉnh liều thường quy do ceftriaxone thải trừ chủ yếu qua mật."
                },
                {
                    "drug": "Vancomycin",
                    "mechanism": "Có thể tạo kết tủa khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.",
                    "effect": "Kết tủa khi pha chung, tăng nguy cơ độc thận",
                    "management": "Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ. Theo dõi nồng độ vancomycin nếu có thể."
                },
                {
                    "drug": "Aminoglycosides (Gentamicin, Tobramycin, Amikacin)",
                    "mechanism": "Có thể tạo kết tủa khi pha chung. Cả hai đều có thể gây độc thận, tác dụng cộng dồn.",
                    "effect": "Kết tủa khi pha chung, tăng nguy cơ độc thận",
                    "management": "Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng cephalosporin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)",
                "Trẻ sơ sinh < 28 ngày tuổi đang dùng calci IV - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (nguy cơ kết tủa tử vong)"
            ],
            "relative": [
                "Dị ứng penicillin (phản ứng chéo ~5-10%) - thận trọng, có thể dùng nếu phản ứng nhẹ",
                "Suy gan nặng kèm suy thận (CrCl <10) - cần giảm liều",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Rối loạn đông máu - tăng nguy cơ chảy máu khi dùng với warfarin",
                "Sỏi mật - tăng nguy cơ sỏi mật (ceftriaxone-calcium complex), đặc biệt ở trẻ em, dùng liều cao"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ceftriaxone là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Cephalosporins nói chung được coi là an toàn trong thai kỳ và được sử dụng rộng rãi. Ceftriaxone có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm khuẩn nặng như viêm màng não. Tuy nhiên, cần thận trọng với nguy cơ sỏi mật và tương tác với calci. Nên tránh dùng kéo dài nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ceftriaxone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Cephalosporins nói chung được coi là an toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ceftriaxone thải trừ 40% qua thận, 60% qua mật, không chuyển hóa qua gan.",
            "moderate": "Không cần điều chỉnh liều. Tuy nhiên, cần thận trọng với nguy cơ tăng bilirubin (nhất thời, do đẩy bilirubin khỏi albumin).",
            "severe": "Không cần điều chỉnh liều. Tuy nhiên, nếu kèm theo suy thận nặng (CrCl <10), có thể cần giảm liều. Theo dõi bilirubin và chức năng gan.",
            "notes": "Ceftriaxone không chuyển hóa qua gan, thải trừ 40% qua thận và 60% qua mật (độc nhất trong cephalosporin). Không cần điều chỉnh liều ở bệnh nhân suy gan. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận nếu CrCl <10. Ngoài ra, ceftriaxone có protein binding cao (85-95%), có thể đẩy bilirubin khỏi albumin, gây tăng bilirubin nhất thời."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, thường chỉ với liều rất cao hoặc suy thận nặng)",
                "Triệu chứng gan: Tăng bilirubin, tăng transaminase (nhất thời)",
                "Triệu chứng sỏi mật: Đau bụng, buồn nôn, nôn (do kết tủa ceftriaxone-calcium)",
                "Triệu chứng thận: Suy thận cấp (hiếm với liều thông thường)",
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay ceftriaxone",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều trị sỏi mật nếu có:",
                "  - Giảm đau: NSAID hoặc opioid",
                "  - Bù dịch đầy đủ",
                "  - Theo dõi siêu âm bụng",
                "  - Có thể cần can thiệp nếu tắc nghẽn",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ ceftriaxone một phần)",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ ceftriaxone một phần (40% thải qua thận), nhưng không hiệu quả bằng các cephalosporin khác do thải trừ chủ yếu qua mật."
            ],
            "monitoring": "Theo dõi dấu hiệu thần kinh (co giật, ý thức), chức năng gan (bilirubin, ALT, AST), dấu hiệu sỏi mật (đau bụng), chức năng thận (creatinine, BUN, lượng nước tiểu), PT/INR (nếu dùng với warfarin), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có suy thận cấp hoặc sỏi mật."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng - chỉ có dạng IV và IM",
                "timing": "Không áp dụng - chỉ có dạng IV và IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl), D5W (5% Dextrose), hoặc Ringer's Lactate. Nồng độ pha: 10-40mg/ml. Pha 1g trong 10ml = 100mg/ml (quá đậm, không dùng). Pha 1g trong 50ml = 20mg/ml. Pha 2g trong 50ml = 40mg/ml. Lắc kỹ để hòa tan hoàn toàn. KHÔNG pha với calci IV.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút. Có thể truyền nhanh hơn (bolus) nếu cần, nhưng thường truyền trong 30 phút để giảm đau tại chỗ.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Calcium IV - KHÔNG pha chung, nguy cơ kết tủa tử vong (đặc biệt ở trẻ sơ sinh)",
                    "Vancomycin - tạo kết tủa, không pha chung",
                    "Aminoglycosides - có thể tạo kết tủa, truyền riêng biệt",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) KHÔNG pha chung với calci IV (nguy cơ kết tủa tử vong ở trẻ sơ sinh), 2) Không pha chung với vancomycin hoặc aminoglycosides, 3) Thời gian bán thải dài (6-9 giờ) → chỉ cần 1 lần/ngày (trừ viêm màng não: q12h), 4) Tiêm IM: pha với lidocaine 1% để giảm đau, 5) Theo dõi sỏi mật ở trẻ em, dùng liều cao, dùng kéo dài."
            },
            "im": {
                "reconstitution": "Pha với lidocaine 1% (không có epinephrine) để giảm đau. Nồng độ pha: 250mg/ml (1g trong 3.5ml lidocaine 1%). Pha 1g trong 3.5ml lidocaine 1% = 250mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis). Tránh tiêm vào mạch máu.",
                "notes": "Pha với lidocaine 1% để giảm đau tại chỗ. Tiêm sâu vào cơ. Có thể gây đau tại chỗ, nhưng thường nhẹ khi pha với lidocaine."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ceftriaxone (Rocephin)",
                "UpToDate - Ceftriaxone: Drug Information",
                "Medscape - Ceftriaxone Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Ceftriaxone Monograph",
                "Micromedex - Ceftriaxone Drug Information",
                "IDSA Guidelines - Community-Acquired Pneumonia, Meningitis"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Ciprofloxacin": {
        "group": "Antibiotic - Fluoroquinolone",
        "vietnamese_name": "Ciprofloxacin, Cipro",
        "administration": ["PO", "IV"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường tiêu hóa",
            "Nhiễm khuẩn da mô mềm",
            "Nhiễm khuẩn xương khớp",
            "Viêm phổi (một số loại)"
        ],
        "contraindications": [
            "Dị ứng fluoroquinolone",
            "Có thai",
            "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
            "QT kéo dài"
        ],
        "dosage": {
            "adult_uti": "250-500mg PO x 2 lần/ngày",
            "adult_uti_complicated": "500-750mg PO x 2 lần/ngày",
            "adult_iv": "200-400mg IV mỗi 12 giờ",
            "adult_severe": "400mg IV mỗi 8 giờ",
            "notes": "Uống cách xa antacid 2 giờ. Không dùng với sữa"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%"
        },
        "side_effects": [
            "Rối loạn tiêu hóa",
            "Đau gân, viêm gân (có thể đứt gân)",
            "QT kéo dài",
            "Co giật (hiếm)",
            "Nhạy cảm ánh sáng",
            "Rối loạn tâm thần (hiếm)"
        ],
        "interactions": [
            "Antacid: giảm hấp thu",
            "Warfarin: tăng INR",
            "Theophylline: tăng nồng độ theophylline",
            "Probenecid: tăng nồng độ ciprofloxacin"
        ],
        "pregnancy": "C - Tránh dùng",
        "mechanism_of_action": "Ciprofloxacin là fluoroquinolone kháng sinh phổ rộng thuộc thế hệ thứ hai. Ức chế DNA gyrase (topoisomerase II) ở vi khuẩn Gram-âm và topoisomerase IV ở vi khuẩn Gram-dương, các enzyme cần thiết cho quá trình sao chép, phiên mã, sửa chữa, và tái tổ hợp DNA. Dẫn đến tổn thương DNA không thể sửa chữa và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, Pseudomonas aeruginosa, H. influenzae, Neisseria, Moraxella), một số Gram-dương (không phải MRSA), và một số vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Kháng thuốc phát triển nhanh nếu dùng không đúng hoặc không đủ liều.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
            "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
            "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc",
            "Thần kinh trung ương (co giật, kích động, mất ngủ, lo âu, trầm cảm, rối loạn tâm thần)",
            "Tim mạch (ECG - QT kéo dài, rối loạn nhịp tim) - đặc biệt ở bệnh nhân có nguy cơ",
            "Đường huyết (tăng hoặc hạ đường huyết - đặc biệt với sulfonylurea)",
            "Chức năng thận (creatinine, BUN) - điều chỉnh liều ở suy thận",
            "Chức năng gan (ALT, AST) - hiếm viêm gan nặng"
        ],
        "precautions": [
            "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc",
            "Nguy cơ tăng ở: > 60 tuổi, dùng corticosteroid, ghép thận, ghép tim, ghép phổi, hoạt động thể lực",
            "NGỪNG NGAY nếu có đau, sưng gân - nghỉ ngơi, không vận động",
            "QT kéo dài → không dùng với các thuốc kéo dài QT khác (amiodarone, sotalol, antipsychotics), bệnh nhân có tiền sử rối loạn nhịp",
            "Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID (tăng nguy cơ)",
            "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng, mặc quần áo che",
            "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm, canxi (cách ít nhất 2 giờ)",
            "Hạ đường huyết → thận trọng với sulfonylurea (glibenclamide, gliclazide)",
            "Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn, viêm khớp",
            "Tránh dùng với sữa, sản phẩm sữa (giảm hấp thu)",
            "Uống nhiều nước để tránh kết tinh trong nước tiểu",
            "Không dùng trong thai kỳ (nguy cơ tổn thương sụn thai nhi)"
        ],
        "pharmacokinetics": {
            "half_life": "4 giờ (bình thường), 5-7 giờ (suy thận nặng)",
            "onset": "1-2 giờ (PO), ngay lập tức (IV)",
            "duration": "q12h (PO/IV), q8h cho Pseudomonas hoặc nhiễm trùng nặng",
            "protein_binding": "20-40%",
            "clearance": "Chủ yếu qua thận (40-60% bài tiết nguyên dạng), một phần qua gan (CYP1A2). Cần điều chỉnh liều ở suy thận (CrCl <30)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín, tránh ẩm. IV: bảo quản trong tủ lạnh (2-8°C), để nhiệt độ phòng trước khi pha. Dung dịch đã pha: bảo quản ở nhiệt độ phòng, dùng trong vòng 24 giờ.",
        "black_box_warnings": "Tăng nguy cơ viêm gân và đứt gân ở mọi lứa tuổi. Nguy cơ tăng ở bệnh nhân > 60 tuổi, dùng corticosteroid, ghép cơ quan. Nguy cơ tổn thương thần kinh ngoại biên không hồi phục. Nguy cơ tác dụng phụ nghiêm trọng về gân, cơ, khớp, và thần kinh có thể xảy ra cùng lúc. Nguy cơ làm nặng bệnh nhược cơ. Tăng nguy cơ rối loạn tâm thần và hành vi tự sát. Chỉ dùng khi không có lựa chọn khác.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Antacids (Aluminum, Magnesium), Sucralfate, Sắt, Kẽm, Canxi",
                    "mechanism": "Cation (Al3+, Mg2+, Fe2+, Zn2+, Ca2+) tạo phức hợp không hòa tan với ciprofloxacin, giảm hấp thu.",
                    "effect": "Giảm hấp thu ciprofloxacin, giảm nồng độ trong máu, giảm hiệu quả điều trị",
                    "management": "Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống ciprofloxacin. Không uống cùng lúc."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Ciprofloxacin ức chế CYP2C9, làm giảm chuyển hóa warfarin, tăng nồng độ warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng ciprofloxacin. Giảm liều warfarin khi bắt đầu ciprofloxacin. Điều chỉnh liều warfarin theo INR."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Ciprofloxacin ức chế CYP1A2, làm giảm chuyển hóa theophylline, tăng nồng độ theophylline.",
                    "effect": "Tăng nồng độ theophylline, tăng độc tính theophylline (buồn nôn, nôn, co giật, rối loạn nhịp tim)",
                    "management": "Giảm liều theophylline 25-50% khi bắt đầu ciprofloxacin. Theo dõi nồng độ theophylline. Theo dõi dấu hiệu độc tính."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của ciprofloxacin, tăng nồng độ.",
                    "effect": "Tăng nồng độ ciprofloxacin, tăng tác dụng phụ",
                    "management": "Theo dõi tác dụng phụ. Có thể cần giảm liều ciprofloxacin."
                },
                {
                    "drug": "NSAID (Ibuprofen, Naproxen)",
                    "mechanism": "Cả hai đều có thể gây co giật, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ co giật",
                    "management": "Tránh dùng đồng thời nếu có thể. Thận trọng ở bệnh nhân có tiền sử co giật."
                },
                {
                    "drug": "Corticosteroid",
                    "mechanism": "Cả hai đều tăng nguy cơ đứt gân, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ viêm gân, đứt gân",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ dấu hiệu đau, sưng gân. Ngừng ngay nếu có đau gân."
                }
            ],
            "minor": [
                {
                    "drug": "Sulfonylurea (Glibenclamide, Gliclazide)",
                    "mechanism": "Ciprofloxacin có thể gây hạ đường huyết.",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Theo dõi đường huyết. Điều chỉnh liều sulfonylurea nếu cần."
                }
            ]
        },
        "contraindications": {
            "absolute": [
                "Dị ứng ciprofloxacin hoặc các fluoroquinolone khác",
                "Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi",
                "Trẻ em < 18 tuổi (trừ trường hợp đặc biệt như nhiễm trùng nặng không có lựa chọn khác) - nguy cơ tổn thương sụn, viêm khớp",
                "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng",
                "Bệnh nhược cơ nặng - có thể làm nặng bệnh"
            ],
            "relative": [
                "Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân",
                "Dùng corticosteroid - tăng nguy cơ đứt gân",
                "Ghép cơ quan - tăng nguy cơ đứt gân",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Suy thận nặng (CrCl <30) - giảm liều đáng kể",
                "Suy gan - thận trọng, có thể giảm chuyển hóa",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với theophylline - tăng độc tính theophylline",
                "Hoạt động thể lực nặng - tăng nguy cơ đứt gân"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ciprofloxacin là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể gây tổn thương sụn ở khớp ở thai nhi. Có báo cáo về tổn thương sụn ở trẻ em khi dùng trong thai kỳ. CHỐNG CHỈ ĐỊNH trong thai kỳ trừ khi lợi ích vượt quá nguy cơ rõ ràng và không có lựa chọn khác. Nhiễm trùng nặng có thể gây nguy hiểm cho thai nhi, nhưng nên dùng kháng sinh khác nếu có thể.",
            "lactation": {
                "safety": "Compatible (với thận trọng)",
                "details": "Ciprofloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, fluoroquinolone có thể gây tổn thương sụn ở trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với thận trọng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh. Tránh dùng nếu có lựa chọn khác."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ciprofloxacin chuyển hóa một phần qua gan nhưng không phụ thuộc nhiều vào chức năng gan.",
            "moderate": "Không cần điều chỉnh liều. Thận trọng nếu có suy thận kèm theo.",
            "severe": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
            "notes": "Ciprofloxacin chuyển hóa một phần qua gan (CYP1A2), thải trừ chủ yếu qua thận (40-60% nguyên dạng). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
                "Triệu chứng thần kinh: Co giật, kích động, lo âu, mất ngủ, trầm cảm, rối loạn tâm thần, hành vi tự sát",
                "Triệu chứng gân: Đau gân, viêm gân, đứt gân (đặc biệt gân Achilles)",
                "Triệu chứng tim mạch: QT kéo dài, rối loạn nhịp tim, có thể gây tử vong",
                "Triệu chứng chuyển hóa: Hạ hoặc tăng đường huyết",
                "Triệu chứng nghiêm trọng: Tổn thương thần kinh ngoại biên không hồi phục, rối loạn nhịp tim nghiêm trọng, đứt gân"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay ciprofloxacin",
                "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
                "Điều trị co giật nếu có:",
                "  - Benzodiazepine (diazepam, lorazepam)",
                "  - Theo dõi thần kinh chặt chẽ",
                "Điều trị rối loạn nhịp tim nếu có:",
                "  - Theo dõi ECG liên tục",
                "  - Điều trị loạn nhịp nếu cần",
                "Điều trị đau gân nếu có:",
                "  - Ngừng ngay ciprofloxacin",
                "  - Nghỉ ngơi, không vận động",
                "  - Chườm lạnh",
                "  - Thuốc giảm đau nếu cần",
                "Điều trị hạ đường huyết nếu có:",
                "  - Truyền glucose",
                "  - Theo dõi đường huyết",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG, dấu hiệu thần kinh, dấu hiệu gân, đường huyết trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (loạn nhịp, co giật, đứt gân)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để tránh kết tinh trong nước tiểu. KHÔNG uống với sữa hoặc sản phẩm sữa (giảm hấp thu).",
                "timing": "Uống 2 lần/ngày (q12h), cách đều 12 giờ. Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống antacid, sucralfate, sắt, kẽm, canxi. Không uống cùng lúc với các cation này."
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 1-2mg/ml (tối đa). Pha 200mg trong 100ml dịch = 2mg/ml. Pha 400mg trong 200ml dịch = 2mg/ml.",
                "infusion_rate": "Truyền trong 60 phút (ít nhất 60 phút). Không truyền quá nhanh. Tốc độ: 100ml/60 phút = ~1.7ml/phút. 200ml/60 phút = ~3.3ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với cation (Al3+, Mg2+, Ca2+)."],
                "notes": "Theo dõi chức năng thận, dấu hiệu gân, thần kinh trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần. Liều: 200-400mg mỗi 12 giờ (q12h), hoặc 400mg mỗi 8 giờ (q8h) cho Pseudomonas hoặc nhiễm trùng nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ciprofloxacin (Cipro)",
                "UpToDate - Ciprofloxacin: Drug Information",
                "Medscape - Ciprofloxacin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Ciprofloxacin Monograph",
                "Micromedex - Ciprofloxacin Drug Information",
                "IDSA Guidelines - Antimicrobial Therapy"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    }
}

__all__ = ['OTHER_DRUGS']
