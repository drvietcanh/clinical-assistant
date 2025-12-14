"""
Statins - HMG-CoA Reductase Inhibitors
"""

STATINS = {
    "Atorvastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Atorvastatin, Lipitor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch",
            "Sau nhồi máu cơ tim",
            "Bệnh động mạch vành"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú",
            "Tiêu cơ vân đang hoạt động"
        ],
        "dosage": {
            "adult_standard": "10-80mg x 1 lần/ngày",
            "adult_high_intensity": "40-80mg x 1 lần/ngày",
            "notes": "Uống bất kỳ lúc nào trong ngày, có thể uống với thức ăn"
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Tăng men gan",
            "Tăng đường huyết",
            "Suy giảm trí nhớ (hiếm)"
        ],
        "interactions": [
            "Clarithromycin/Erythromycin: tăng nguy cơ tiêu cơ vân",
            "Grapefruit juice: tăng nồng độ (với liều cao)",
            "Cyclosporine: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Ức chế HMG-CoA reductase, enzyme chính trong tổng hợp cholesterol, dẫn đến giảm LDL-cholesterol và tăng HDL-cholesterol",
        "monitoring": [
            "Lipid profile (LDL, HDL, TG) sau 6-8 tuần, sau đó mỗi 3-6 tháng",
            "AST/ALT trước điều trị, sau 12 tuần, sau đó mỗi 6-12 tháng",
            "CK nếu có đau cơ, yếu cơ",
            "HbA1c/đường huyết (statin có thể tăng đường huyết)"
        ],
        "precautions": [
            "Kiểm tra CK nếu đau cơ hoặc yếu cơ (ngừng nếu CK >10 lần ULN)",
            "Ngừng nếu ALT >3 lần ULN",
            "Thận trọng với bệnh nhân đái tháo đường (có thể tăng đường huyết)",
            "Tránh grapefruit juice với liều cao"
        ],
        "pharmacokinetics": {
            "half_life": "14 giờ",
            "onset": "1-2 tuần",
            "duration": "24 giờ",
            "protein_binding": ">98%",
            "clearance": "Gan (CYP3A4)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tiêu cơ vân - có thể gây suy thận cấp và tử vong. Nguy cơ tăng khi dùng chung với thuốc khác hoặc liều cao",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cyclosporine ức chế CYP3A4 và P-glycoprotein, tăng nồng độ atorvastatin đáng kể",
                    "effect": "Tăng nguy cơ tiêu cơ vân (rhabdomyolysis) nghiêm trọng, có thể gây suy thận cấp, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu cần: giảm liều atorvastatin tối đa 10mg/ngày, theo dõi CK và men gan thường xuyên. Cân nhắc dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4)."
                },
                {
                    "drug": "Clarithromycin, Erythromycin, Telithromycin",
                    "mechanism": "Macrolide ức chế CYP3A4, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân, đặc biệt ở liều cao atorvastatin",
                    "management": "Tránh dùng cùng nếu có thể. Nếu cần: giảm liều atorvastatin 50-75%, theo dõi CK và dấu hiệu đau cơ. Tạm ngừng atorvastatin nếu có đau cơ hoặc CK tăng."
                },
                {
                    "drug": "Itraconazole, Ketoconazole, Voriconazole, Posaconazole",
                    "mechanism": "Azole antifungals ức chế CYP3A4 mạnh, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Tạm ngừng atorvastatin trong thời gian dùng azole antifungal. Hoặc dùng pravastatin/rosuvastatin (ít chuyển hóa qua CYP3A4)."
                },
                {
                    "drug": "Grapefruit juice (lớn hơn 1.2L/ngày hoặc liều cao atorvastatin)",
                    "mechanism": "Grapefruit juice ức chế CYP3A4 ở ruột, tăng hấp thu atorvastatin",
                    "effect": "Tăng nồng độ atorvastatin, tăng nguy cơ tiêu cơ vân",
                    "management": "Tránh grapefruit juice khi dùng atorvastatin, đặc biệt ở liều cao (40-80mg). Nước ép cam, táo không có vấn đề."
                }
            ],
            "moderate": [
                {
                    "drug": "Amiodarone, Diltiazem, Verapamil",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều atorvastatin 50% hoặc tối đa 20mg/ngày. Theo dõi CK và dấu hiệu đau cơ. Cân nhắc dùng pravastatin/rosuvastatin."
                },
                {
                    "drug": "Ritonavir, Lopinavir, Saquinavir (HIV protease inhibitors)",
                    "mechanism": "Ức chế CYP3A4 mạnh, tăng nồng độ atorvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều atorvastatin. Theo dõi CK. Cân nhắc dùng pravastatin hoặc rosuvastatin."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Atorvastatin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên khi bắt đầu hoặc thay đổi liều atorvastatin. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Atorvastatin có thể tăng nhẹ nồng độ digoxin qua P-glycoprotein",
                    "effect": "Tăng nhẹ nồng độ digoxin",
                    "management": "Theo dõi nồng độ digoxin và dấu hiệu ngộ độc digoxin. Có thể cần giảm liều digoxin."
                },
                {
                    "drug": "Colchicine",
                    "mechanism": "Cả hai đều chuyển hóa qua CYP3A4, có thể tăng tác dụng phụ",
                    "effect": "Tăng nguy cơ độc cơ, đặc biệt ở bệnh nhân suy thận",
                    "management": "Thận trọng, đặc biệt ở bệnh nhân suy thận. Theo dõi CK và dấu hiệu đau cơ. Có thể cần giảm liều một trong hai thuốc."
                }
            ],
            "minor": [
                {
                    "drug": "Rifampin, Phenytoin",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa atorvastatin",
                    "effect": "Giảm hiệu quả atorvastatin",
                    "management": "Có thể cần tăng liều atorvastatin. Theo dõi lipid profile."
                },
                {
                    "drug": "Oral contraceptives",
                    "mechanism": "Atorvastatin có thể tăng nhẹ nồng độ estrogen",
                    "effect": "Tăng nhẹ tác dụng phụ của thuốc tránh thai",
                    "management": "Thường không cần điều chỉnh. Theo dõi tác dụng phụ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                "Dị ứng với atorvastatin hoặc bất kỳ thành phần nào",
                "Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, giảm liều nếu cần",
                "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                "Uống rượu nhiều - tăng nguy cơ viêm gan",
                "Bệnh nhân Châu Á - tăng nồng độ atorvastatin, có thể cần liều thấp hơn",
                "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                "Dùng cùng thuốc ức chế CYP3A4 - giảm liều atorvastatin"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Atorvastatin gây dị tật thai nhi, đặc biệt trong tam cá nguyệt đầu tiên. Statins ức chế tổng hợp cholesterol, cần thiết cho sự phát triển của thai nhi. Có thể gây dị tật bẩm sinh, chậm phát triển. Phải ngừng atorvastatin ít nhất 1-2 tháng trước khi có thai. Nếu có thai khi đang dùng, ngừng ngay lập tức.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Atorvastatin bài tiết vào sữa mẹ. Có thể gây tác dụng phụ trên trẻ bú mẹ. Chưa có dữ liệu đầy đủ về an toàn. Statins có thể ảnh hưởng đến sự phát triển của trẻ.",
                "recommendation": "CHỐNG CHỈ ĐỊNH khi cho con bú. Ngừng atorvastatin hoặc ngừng cho con bú. Cân nhắc thuốc thay thế nếu cần."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều. Theo dõi men gan thường xuyên.",
            "moderate": "Thận trọng. Giảm liều hoặc dùng liều thấp hơn. Theo dõi men gan mỗi 3-6 tháng. Ngừng nếu ALT >3 lần ULN.",
            "severe": "CHỐNG CHỈ ĐỊNH. Không dùng ở bệnh nhân suy gan nặng hoặc bệnh gan hoạt động.",
            "notes": "Atorvastatin chuyển hóa qua gan (CYP3A4). Suy gan có thể làm tăng nồng độ atorvastatin và tăng nguy cơ độc tính. Kiểm tra men gan trước điều trị. Ngừng nếu ALT >3 lần ULN hoặc có dấu hiệu viêm gan."
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
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng atorvastatin, truyền dịch tích cực để phòng suy thận, lọc máu nếu cần",
            "treatment": [
                "Ngừng atorvastatin ngay lập tức",
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
                "Theo dõi ít nhất 48-72 giờ do half-life 14 giờ"
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
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày (sáng, trưa, hoặc tối). Uống cùng một giờ mỗi ngày để nhớ. Có thể uống trước hoặc sau bữa ăn."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Atorvastatin chỉ có dạng uống (PO)."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <10 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <10 tuổi (dữ liệu hạn chế)",
            "children": "10-17 tuổi: 10mg x 1 lần/ngày, tăng dần đến 20mg/ngày nếu cần. Chỉ dùng cho tăng cholesterol máu gia đình (familial hypercholesterolemia). Theo dõi lipid panel, men gan, CK",
            "adolescents": "10-20mg x 1 lần/ngày, tăng dần đến 20-40mg/ngày nếu cần. Liều người lớn. Theo dõi lipid panel, men gan, CK",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng cholesterol máu gia đình ở trẻ ≥10 tuổi. Khởi đầu với liều thấp, tăng dần. Theo dõi lipid panel, men gan, CK. CHỐNG CHỈ ĐỊNH trong thai kỳ"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (đau cơ, tiêu cơ vân). Suy gan, suy thận phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (10mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo chức năng gan, thận",
            "monitoring": "Theo dõi men gan, CK thường xuyên hơn. Cảnh báo về triệu chứng đau cơ, yếu cơ (dấu hiệu tiêu cơ vân). Theo dõi lipid panel"
        },
        "brand_names": {
            "vietnam": ["Lipitor", "Atorvastatin Stada", "Atorvastatin", "Atorlip"],
            "common": ["Lipitor", "Atorvastatin"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "15,000 - 50,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Atorvastatin generic thường rẻ hơn (15,000-30,000 VND/viên 20mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lipitor (atorvastatin)",
                "UpToDate - Atorvastatin: Drug information",
                "ACC/AHA Guidelines - Cholesterol Management (2018)",
                "NLA Guidelines - Statin Safety (2014)",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics - Lipid-lowering drugs"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (ASCOT, CARDS, PROVE-IT) showing cardiovascular benefit"
        }
    },

    "Simvastatin": {
        "group": "Cardiovascular - Statin",
        "vietnamese_name": "Simvastatin, Zocor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú"
        ],
        "dosage": {
            "adult_standard": "10-40mg x 1 lần/ngày",
            "adult_max": "80mg x 1 lần/ngày (hiếm dùng)",
            "notes": "Uống buổi tối, tránh grapefruit juice"
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân",
            "Tăng men gan"
        ],
                  "interactions": [
              "Amiodarone: giảm liều simvastatin xuống tối đa 20mg/ngày",
              "Verapamil: giảm liều simvastatin",
              "Grapefruit juice: tăng nồng độ"
          ],
          "pregnancy": "X",
          "mechanism_of_action": "HMG-CoA reductase inhibitor (statin). Ức chế enzyme HMG-CoA reductase - enzyme quan trọng trong tổng hợp cholesterol ở gan. Giảm sản xuất cholesterol nội sinh, tăng biểu hiện LDL receptor ở gan, giảm LDL cholesterol. Cũng có tác dụng chống viêm, ổn định mảng xơ vữa (pleiotropic effects).",
          "monitoring": [
              "Lipid panel: Cholesterol toàn phần, LDL, HDL, triglycerides (sau 4-8 tuần, sau đó mỗi 3-6 tháng)",
              "Chức năng gan: ALT, AST (trước khi bắt đầu, sau 12 tuần, sau đó mỗi 6-12 tháng hoặc khi có triệu chứng)",
              "CK (creatine kinase) - nếu có đau cơ, yếu cơ (để phát hiện tiêu cơ vân)",
              "Glucose/HbA1c - statins có thể tăng đường huyết nhẹ",
              "Dấu hiệu đau cơ, yếu cơ, nước tiểu sẫm màu (dấu hiệu tiêu cơ vân)"
          ],
          "precautions": [
              "Uống buổi tối (cholesterol được tổng hợp nhiều vào ban đêm)",
              "TRÁNH grapefruit juice (ức chế CYP3A4, tăng nồng độ, tăng nguy cơ tác dụng phụ)",
              "Kiểm tra CK nếu có đau cơ/yếu cơ - ngừng ngay nếu CK >10x ULN hoặc có dấu hiệu tiêu cơ vân",
              "Thận trọng với liều cao (>40mg/ngày) - tăng nguy cơ tiêu cơ vân",
              "Giảm liều khi dùng với amiodarone, verapamil, diltiazem, macrolides, azole antifungals (tương tác CYP3A4)",
              "CHỐNG CHỈ ĐỊNH trong thai kỳ và cho con bú (category X)",
              "Thận trọng ở bệnh nhân có bệnh gan - kiểm tra ALT/AST trước khi bắt đầu",
              "Có thể tăng đường huyết nhẹ (đặc biệt ở bệnh nhân đái tháo đường)"
          ],
          "pharmacokinetics": {
              "half_life": "2-3 giờ (ngắn), nhưng tác dụng kéo dài do ức chế enzyme)",
              "onset": "1-2 tuần (giảm LDL)",
              "duration": "Kéo dài sau khi ngừng",
              "protein_binding": "95%",
              "clearance": "Gan (CYP3A4) - extensive first-pass metabolism"
          },
          "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
          "black_box_warnings": "CHỐNG CHỈ ĐỊNH trong thai kỳ - có thể gây dị tật thai nhi. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả. Tiêu cơ vân có thể gây suy thận cấp và tử vong - ngừng ngay nếu có đau cơ, yếu cơ, nước tiểu sẫm màu",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Cyclosporine, Tacrolimus",
                      "mechanism": "Cyclosporine ức chế CYP3A4 và P-glycoprotein, tăng nồng độ simvastatin đáng kể",
                      "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng, có thể gây suy thận cấp, tử vong",
                      "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu cần: giảm liều simvastatin tối đa 10mg/ngày, theo dõi CK và men gan thường xuyên. Cân nhắc dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4)."
                  },
                  {
                      "drug": "Itraconazole, Ketoconazole, Voriconazole, Posaconazole",
                      "mechanism": "Azole antifungals ức chế CYP3A4 mạnh, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
                      "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Tạm ngừng simvastatin trong thời gian dùng azole antifungal. Hoặc dùng pravastatin/rosuvastatin (ít chuyển hóa qua CYP3A4)."
                  },
                  {
                      "drug": "Clarithromycin, Erythromycin, Telithromycin",
                      "mechanism": "Macrolide ức chế CYP3A4, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân, đặc biệt ở liều cao simvastatin",
                      "management": "Tránh dùng cùng nếu có thể. Nếu cần: giảm liều simvastatin hoặc tạm ngừng. Theo dõi CK và dấu hiệu đau cơ. Tạm ngừng simvastatin nếu có đau cơ hoặc CK tăng."
                  },
                  {
                      "drug": "Grapefruit juice",
                      "mechanism": "Grapefruit juice ức chế CYP3A4 ở ruột, tăng hấp thu simvastatin",
                      "effect": "Tăng nồng độ simvastatin đáng kể, tăng nguy cơ tiêu cơ vân",
                      "management": "CHỐNG CHỈ ĐỊNH dùng grapefruit juice khi dùng simvastatin. Tránh hoàn toàn, kể cả lượng nhỏ. Nước ép cam, táo không có vấn đề."
                  },
                  {
                      "drug": "Amiodarone",
                      "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân, đặc biệt ở liều cao simvastatin",
                      "management": "Giảm liều simvastatin xuống TỐI ĐA 20mg/ngày. Theo dõi CK và dấu hiệu đau cơ. Cân nhắc dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4)."
                  }
              ],
              "moderate": [
                  {
                      "drug": "Diltiazem, Verapamil",
                      "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân",
                      "management": "Giảm liều simvastatin 50% hoặc tối đa 20mg/ngày. Theo dõi CK và dấu hiệu đau cơ. Cân nhắc dùng pravastatin/rosuvastatin."
                  },
                  {
                      "drug": "Ritonavir, Lopinavir, Saquinavir (HIV protease inhibitors)",
                      "mechanism": "Ức chế CYP3A4 mạnh, tăng nồng độ simvastatin",
                      "effect": "Tăng nguy cơ tiêu cơ vân",
                      "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Cân nhắc dùng pravastatin hoặc rosuvastatin."
                  },
                  {
                      "drug": "Warfarin",
                      "mechanism": "Simvastatin có thể tăng tác dụng chống đông của warfarin",
                      "effect": "Tăng INR, tăng nguy cơ chảy máu",
                      "management": "Theo dõi INR thường xuyên khi bắt đầu hoặc thay đổi liều simvastatin. Có thể cần giảm liều warfarin."
                  },
                  {
                      "drug": "Colchicine",
                      "mechanism": "Cả hai đều chuyển hóa qua CYP3A4, có thể tăng tác dụng phụ",
                      "effect": "Tăng nguy cơ độc cơ, đặc biệt ở bệnh nhân suy thận",
                      "management": "Thận trọng, đặc biệt ở bệnh nhân suy thận. Theo dõi CK và dấu hiệu đau cơ. Có thể cần giảm liều một trong hai thuốc."
                  }
              ],
              "minor": [
                  {
                      "drug": "Rifampin, Phenytoin",
                      "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa simvastatin",
                      "effect": "Giảm hiệu quả simvastatin",
                      "management": "Có thể cần tăng liều simvastatin. Theo dõi lipid profile."
                  }
              ]
          },
          "contraindications": {
              "tuyệt_đối": [
                  "Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan",
                  "Có thai (pregnancy) - FDA category X, gây dị tật thai nhi",
                  "Cho con bú (lactation) - bài tiết vào sữa mẹ",
                  "Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)",
                  "Dị ứng với simvastatin hoặc bất kỳ thành phần nào",
                  "Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)",
                  "Dùng grapefruit juice"
              ],
              "tương_đối": [
                  "Suy thận - thận trọng, giảm liều nếu cần",
                  "Suy gan - thận trọng, theo dõi men gan thường xuyên",
                  "Uống rượu nhiều - tăng nguy cơ viêm gan",
                  "Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân",
                  "Đái tháo đường - statins có thể tăng đường huyết nhẹ",
                  "Bệnh tuyến giáp - tăng nguy cơ đau cơ",
                  "Dùng cùng thuốc ức chế CYP3A4 - giảm liều simvastatin",
                  "Liều cao (>40mg/ngày) - tăng nguy cơ tiêu cơ vân"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "X",
              "pregnancy_details": "CHỐNG CHỈ ĐỊNH trong thai kỳ. Simvastatin gây dị tật thai nhi, đặc biệt trong tam cá nguyệt đầu tiên. Statins ức chế tổng hợp cholesterol, cần thiết cho sự phát triển của thai nhi. Có thể gây dị tật bẩm sinh, chậm phát triển. Phụ nữ trong độ tuổi sinh đẻ phải dùng biện pháp tránh thai hiệu quả. Phải ngừng simvastatin ít nhất 1-2 tháng trước khi có thai. Nếu có thai khi đang dùng, ngừng ngay lập tức.",
              "lactation": {
                  "safety": "Incompatible",
                  "details": "Simvastatin bài tiết vào sữa mẹ. Có thể gây tác dụng phụ trên trẻ bú mẹ. Chưa có dữ liệu đầy đủ về an toàn. Statins có thể ảnh hưởng đến sự phát triển của trẻ.",
                  "recommendation": "CHỐNG CHỈ ĐỊNH khi cho con bú. Ngừng simvastatin hoặc ngừng cho con bú. Cân nhắc thuốc thay thế nếu cần."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không đổi liều. Theo dõi men gan thường xuyên.",
              "moderate": "Thận trọng. Giảm liều hoặc dùng liều thấp hơn. Theo dõi men gan mỗi 3-6 tháng. Ngừng nếu ALT >3 lần ULN.",
              "severe": "CHỐNG CHỈ ĐỊNH. Không dùng ở bệnh nhân suy gan nặng hoặc bệnh gan hoạt động.",
              "notes": "Simvastatin chuyển hóa qua gan (CYP3A4) - extensive first-pass metabolism. Suy gan có thể làm tăng nồng độ simvastatin và tăng nguy cơ độc tính. Kiểm tra men gan trước điều trị. Ngừng nếu ALT >3 lần ULN hoặc có dấu hiệu viêm gan."
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
              "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: ngừng simvastatin, truyền dịch tích cực để phòng suy thận, lọc máu nếu cần",
              "treatment": [
                  "Ngừng simvastatin ngay lập tức",
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
                  "Theo dõi ít nhất 24-48 giờ do half-life 2-3 giờ (nhưng tác dụng kéo dài)"
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
                  "timing": "Uống 1 lần/ngày vào BUỔI TỐI (cholesterol được tổng hợp nhiều vào ban đêm). Uống cùng một giờ mỗi ngày để nhớ. TRÁNH grapefruit juice hoàn toàn."
              },
              "iv": {
                  "reconstitution": "Không có dạng IV",
                  "infusion_rate": "Không áp dụng",
                  "compatibility": [],
                  "incompatibility": [],
                  "notes": "Simvastatin chỉ có dạng uống (PO)."
              }
          },
          "pediatric_dosing": {
              "neonates": "Không khuyến cáo cho trẻ <10 tuổi (dữ liệu hạn chế)",
              "infants": "Không khuyến cáo cho trẻ <10 tuổi (dữ liệu hạn chế)",
              "children": "10-17 tuổi: 10mg x 1 lần/ngày vào buổi tối, tăng dần đến 20-40mg/ngày nếu cần. Chỉ dùng cho tăng cholesterol máu gia đình. Theo dõi lipid panel, men gan, CK. TRÁNH grapefruit juice",
              "adolescents": "10-20mg x 1 lần/ngày vào buổi tối, tăng dần đến 20-40mg/ngày nếu cần. Liều người lớn. Theo dõi lipid panel, men gan, CK",
              "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng cholesterol máu gia đình ở trẻ ≥10 tuổi. Uống buổi tối. Khởi đầu với liều thấp, tăng dần. Theo dõi lipid panel, men gan, CK. CHỐNG CHỈ ĐỊNH trong thai kỳ. TRÁNH grapefruit juice hoàn toàn"
          },
          "geriatric_dosing": {
              "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (đau cơ, tiêu cơ vân). Suy gan phổ biến hơn (extensive first-pass metabolism qua CYP3A4)",
              "dose_adjustment": "Khởi đầu với liều thấp hơn (10mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo chức năng gan. Giảm liều khi dùng với amiodarone, verapamil, diltiazem",
              "monitoring": "Theo dõi men gan, CK thường xuyên hơn. Cảnh báo về triệu chứng đau cơ, yếu cơ (dấu hiệu tiêu cơ vân). Theo dõi lipid panel. Cảnh báo về TRÁNH grapefruit juice"
          },
          "brand_names": {
              "vietnam": ["Zocor", "Simvastatin Stada", "Simvastatin", "Simva"],
              "common": ["Zocor", "Simvastatin"]
          },
          "cost_estimate": {
              "unit": "VND",
              "range": "10,000 - 40,000 VND/viên (tùy hàm lượng và thương hiệu)",
              "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Simvastatin generic thường rẻ hơn (10,000-25,000 VND/viên 20mg)."
          },
          "references": {
              "primary_sources": [
                  "FDA Drug Label - Zocor (simvastatin)",
                  "UpToDate - Simvastatin: Drug information",
                  "ACC/AHA Guidelines - Cholesterol Management (2018)",
                  "NLA Guidelines - Statin Safety (2014)",
                  "4S Study - Lancet (1994) - Simvastatin trong dự phòng biến cố tim mạch",
                  "Goodman & Gilman's Pharmacological Basis of Therapeutics - Lipid-lowering drugs"
              ],
              "last_updated": "2024-12-19",
              "evidence_level": "High - Multiple large RCTs (4S, HPS) showing cardiovascular benefit"
          }
      },
    
    "Simvastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Simvastatin, Zocor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch",
            "Sau nhồi máu cơ tim",
            "Bệnh động mạch vành"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú",
            "Tiêu cơ vân đang hoạt động"
        ],
        "dosage": {
            "adult_standard": "10-40mg x 1 lần/ngày (tối đa 40mg)",
            "adult_high_intensity": "40mg x 1 lần/ngày (tối đa 40mg)",
            "adult_with_amiodarone": "Tối đa 20mg/ngày",
            "adult_with_verapamil": "Tối đa 20mg/ngày",
            "adult_with_diltiazem": "Tối đa 20mg/ngày",
            "notes": "Uống buổi tối (cholesterol tổng hợp nhiều vào ban đêm). Tránh grapefruit juice."
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Tăng men gan",
            "Tăng đường huyết",
            "Suy giảm trí nhớ (hiếm)"
        ],
        "interactions": [
            "Clarithromycin/Erythromycin: TĂNG NGUY CƠ TIÊU CƠ VÂN - tránh dùng chung",
            "Amiodarone: tăng nguy cơ tiêu cơ vân - giảm liều simvastatin xuống tối đa 20mg/ngày",
            "Verapamil/Diltiazem: tăng nguy cơ tiêu cơ vân - giảm liều simvastatin xuống tối đa 20mg/ngày",
            "Grapefruit juice: tăng nồng độ - tránh",
            "Cyclosporine: tăng nguy cơ tiêu cơ vân - tránh dùng chung",
            "Gemfibrozil: tăng nguy cơ tiêu cơ vân - tránh dùng chung"
        ],
        "pregnancy": "X - Chống chỉ định trong thai kỳ",
        "mechanism_of_action": "Ức chế HMG-CoA reductase, enzyme chính trong tổng hợp cholesterol, dẫn đến giảm LDL-cholesterol và tăng HDL-cholesterol. Simvastatin là prodrug, chuyển hóa thành simvastatin acid (hoạt chất) trong gan.",
        "monitoring": [
            "Lipid profile (LDL, HDL, TG) sau 6-8 tuần, sau đó mỗi 3-6 tháng",
            "AST/ALT trước điều trị, sau 12 tuần, sau đó mỗi 6-12 tháng",
            "CK nếu có đau cơ, yếu cơ",
            "HbA1c/đường huyết (statin có thể tăng đường huyết)"
        ],
        "precautions": [
            "Kiểm tra CK nếu đau cơ hoặc yếu cơ (ngừng nếu CK >10 lần ULN)",
            "Ngừng nếu ALT >3 lần ULN",
            "Thận trọng với bệnh nhân đái tháo đường (có thể tăng đường huyết)",
            "TRÁNH grapefruit juice (ức chế CYP3A4, tăng nồng độ simvastatin)",
            "Giảm liều xuống tối đa 20mg/ngày khi dùng với amiodarone, verapamil, diltiazem",
            "TRÁNH dùng với clarithromycin, erythromycin, cyclosporine, gemfibrozil",
            "Uống buổi tối để tối ưu hiệu quả"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (simvastatin acid)",
            "onset": "1-2 tuần",
            "duration": "24 giờ",
            "protein_binding": "95%",
            "metabolism": "CYP3A4 (quan trọng - nhiều tương tác)",
            "clearance": "Chủ yếu qua gan (13% qua thận)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tiêu cơ vân - có thể gây suy thận cấp và tử vong. Đặc biệt nguy hiểm khi dùng với thuốc ức chế CYP3A4 (clarithromycin, erythromycin, amiodarone, verapamil, diltiazem) hoặc gemfibrozil, cyclosporine. Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Clarithromycin, Erythromycin",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG CHUNG. Nếu cần: ngừng simvastatin hoặc chuyển statin khác (pravastatin, rosuvastatin)."
                },
                {
                    "drug": "Amiodarone",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày hoặc chuyển statin khác."
                },
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày hoặc chuyển statin khác."
                },
                {
                    "drug": "Gemfibrozil",
                    "mechanism": "Tăng nồng độ simvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "TRÁNH DÙNG CHUNG."
                },
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Ức chế CYP3A4 và P-gp, tăng nồng độ simvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "TRÁNH DÙNG CHUNG."
                }
            ],
            "moderate": [
                {
                    "drug": "Grapefruit juice",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ simvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "TRÁNH uống grapefruit juice khi dùng simvastatin."
                }
            ]
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Simvastatin (Zocor)",
                "UpToDate - Simvastatin: Drug Information",
                "4S Study - The Lancet",
                "HPS Study - The Lancet"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Multiple large RCTs (4S, HPS) showing cardiovascular benefit"
        }
    },

    "Lovastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Lovastatin, Mevacor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch",
            "Bệnh động mạch vành"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú",
            "Tiêu cơ vân đang hoạt động"
        ],
        "dosage": {
            "adult_standard": "20-40mg x 1 lần/ngày (bữa tối)",
            "adult_high_intensity": "40-80mg x 1 lần/ngày (bữa tối) hoặc chia 2 lần",
            "adult_extended_release": "20-60mg x 1 lần/ngày (bữa tối)",
            "notes": "Uống với bữa tối để tăng hấp thu. Có thể chia 2 lần/ngày với liều cao."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, giảm liều nếu CrCl <30"
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Tăng men gan",
            "Tăng đường huyết",
            "Suy giảm trí nhớ (hiếm)"
        ],
        "interactions": [
            "Clarithromycin/Erythromycin: tăng nguy cơ tiêu cơ vân",
            "Grapefruit juice: tăng nồng độ (với liều cao)",
            "Cyclosporine: tăng nguy cơ tiêu cơ vân",
            "Gemfibrozil: tăng nguy cơ tiêu cơ vân"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Lovastatin là statin đầu tiên được phê duyệt, ức chế HMG-CoA reductase, enzyme chính trong tổng hợp cholesterol, dẫn đến giảm LDL-cholesterol và tăng HDL-cholesterol. Lovastatin chuyển hóa qua CYP3A4, nên có nhiều tương tác thuốc. Cần uống với thức ăn để tăng hấp thu (tăng sinh khả dụng 50%).",
        "monitoring": [
            "Lipid profile (LDL, HDL, TG) sau 6-8 tuần, sau đó mỗi 3-6 tháng",
            "AST/ALT trước điều trị, sau 12 tuần, sau đó mỗi 6-12 tháng",
            "CK nếu có đau cơ, yếu cơ",
            "HbA1c/đường huyết (statin có thể tăng đường huyết)"
        ],
        "precautions": [
            "Uống với bữa tối để tăng hấp thu (tăng sinh khả dụng 50%)",
            "Kiểm tra CK nếu đau cơ hoặc yếu cơ (ngừng nếu CK >10 lần ULN)",
            "Ngừng nếu ALT >3 lần ULN",
            "Thận trọng với bệnh nhân đái tháo đường (có thể tăng đường huyết)",
            "Tránh grapefruit juice với liều cao (ức chế CYP3A4)",
            "Nhiều tương tác với CYP3A4 inhibitors (clarithromycin, azole antifungals, cyclosporine)"
        ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ",
            "onset": "2 tuần",
            "duration": "24 giờ",
            "protein_binding": ">95%",
            "metabolism": "Gan (CYP3A4) - nhiều tương tác",
            "clearance": "Chủ yếu qua gan (metabolism), một phần qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tiêu cơ vân - có thể gây suy thận cấp và tử vong. Nguy cơ tăng khi dùng chung với thuốc khác hoặc liều cao. Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine, Tacrolimus",
                    "mechanism": "Cyclosporine ức chế CYP3A4 và P-glycoprotein, tăng nồng độ lovastatin đáng kể",
                    "effect": "Tăng nguy cơ tiêu cơ vân (rhabdomyolysis) nghiêm trọng, có thể gây suy thận cấp, tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Nếu cần: giảm liều lovastatin tối đa 20mg/ngày, theo dõi CK và men gan thường xuyên. Cân nhắc dùng pravastatin hoặc rosuvastatin (ít chuyển hóa qua CYP3A4)."
                },
                {
                    "drug": "Clarithromycin, Erythromycin, Telithromycin",
                    "mechanism": "Macrolide ức chế CYP3A4, tăng nồng độ lovastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân, đặc biệt ở liều cao lovastatin",
                    "management": "Tránh dùng cùng nếu có thể. Nếu cần: giảm liều lovastatin 50-75%, theo dõi CK và dấu hiệu đau cơ. Tạm ngừng lovastatin nếu có đau cơ hoặc CK tăng."
                },
                {
                    "drug": "Itraconazole, Ketoconazole, Voriconazole, Posaconazole",
                    "mechanism": "Azole antifungals ức chế CYP3A4 mạnh, tăng nồng độ lovastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Tạm ngừng lovastatin trong thời gian dùng azole antifungal. Hoặc dùng pravastatin/rosuvastatin (ít chuyển hóa qua CYP3A4)."
                },
                {
                    "drug": "Grapefruit juice (lớn hơn 1.2L/ngày hoặc liều cao lovastatin)",
                    "mechanism": "Grapefruit juice ức chế CYP3A4 ở ruột, tăng hấp thu lovastatin",
                    "effect": "Tăng nồng độ lovastatin, tăng nguy cơ tiêu cơ vân",
                    "management": "Tránh grapefruit juice khi dùng lovastatin, đặc biệt ở liều cao (40-80mg). Nước ép cam, táo không có vấn đề."
                },
                {
                    "drug": "Gemfibrozil",
                    "mechanism": "Tăng nồng độ lovastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "TRÁNH DÙNG CHUNG. Nếu cần: dùng liều lovastatin thấp nhất, theo dõi CK chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Amiodarone, Diltiazem, Verapamil",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ lovastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều lovastatin 50% hoặc tối đa 20mg/ngày. Theo dõi CK và dấu hiệu đau cơ. Cân nhắc dùng pravastatin/rosuvastatin."
                },
                {
                    "drug": "Ritonavir, Lopinavir, Saquinavir (HIV protease inhibitors)",
                    "mechanism": "Ức chế CYP3A4 mạnh, tăng nồng độ lovastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều lovastatin. Theo dõi CK. Cân nhắc dùng pravastatin hoặc rosuvastatin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động",
                "Có thai (category X)",
                "Cho con bú",
                "Tiêu cơ vân đang hoạt động",
                "Dùng với cyclosporine, azole antifungals, macrolides mạnh"
            ],
            "tương_đối": [
                "Suy thận (CrCl <30) - giảm liều",
                "Suy gan - thận trọng",
                "Bệnh nhân đái tháo đường - có thể tăng đường huyết",
                "Dùng với gemfibrozil - tránh dùng chung"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Lovastatin gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ. Ngừng thuốc ngay khi phát hiện có thai.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Lovastatin bài tiết vào sữa mẹ. Thuốc có thể gây độc tính cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng lovastatin. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Theo dõi men gan.",
            "moderate": "Thận trọng, theo dõi men gan. Có thể cần giảm liều.",
            "severe": "CHỐNG CHỈ ĐỊNH. Không dùng ở bệnh gan hoạt động.",
            "notes": "Lovastatin chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ, tăng nguy cơ tiêu cơ vân. Không dùng ở bệnh gan hoạt động."
        },
        "overdose_management": {
            "symptoms": [
                "Đau cơ, yếu cơ",
                "Tiêu cơ vân (rhabdomyolysis) - tăng CK, myoglobin niệu, suy thận cấp",
                "Tăng men gan",
                "Suy thận cấp (do tiêu cơ vân)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng lovastatin ngay lập tức",
                "Theo dõi CK, men gan, chức năng thận",
                "Truyền dịch nếu có tiêu cơ vân (để phòng suy thận cấp)",
                "Điều trị suy thận cấp nếu có",
                "Theo dõi tại bệnh viện nếu có tiêu cơ vân"
            ],
            "monitoring": "CK, men gan, chức năng thận, myoglobin niệu, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "NÊN uống với bữa tối (tăng hấp thu 50%). Có thể uống với thức ăn bất kỳ lúc nào.",
                "timing": "Uống 1 lần/ngày với bữa tối. Với liều cao (80mg), có thể chia 2 lần/ngày (40mg x 2 lần). Dạng extended release: 1 lần/ngày với bữa tối."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lovastatin (Mevacor)",
                "UpToDate - Lovastatin: Drug Information",
                "AFCAPS/TexCAPS Study - JAMA",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA approved, multiple large RCTs showing cardiovascular benefit"
        }
    },

    "Pravastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Pravastatin, Pravachol",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch",
            "Sau nhồi máu cơ tim",
            "Bệnh động mạch vành"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú",
            "Tiêu cơ vân đang hoạt động"
        ],
        "dosage": {
            "adult_standard": "10-40mg x 1 lần/ngày",
            "adult_high_intensity": "40-80mg x 1 lần/ngày",
            "notes": "Uống bất kỳ lúc nào trong ngày, có thể uống với thức ăn. Ít tương tác với CYP3A4."
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm, ít hơn statin chuyển hóa qua CYP3A4)",
            "Tăng men gan",
            "Tăng đường huyết (nhẹ)",
            "Suy giảm trí nhớ (hiếm)"
        ],
        "interactions": [
            "Ít tương tác với CYP3A4 inhibitors (an toàn hơn với clarithromycin, azole antifungals)",
            "Cyclosporine: vẫn tăng nguy cơ tiêu cơ vân (nhưng ít hơn statin khác)",
            "Gemfibrozil: tăng nguy cơ tiêu cơ vân - tránh dùng chung"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Ức chế HMG-CoA reductase, enzyme chính trong tổng hợp cholesterol, dẫn đến giảm LDL-cholesterol và tăng HDL-cholesterol. Pravastatin không chuyển hóa qua CYP3A4 (khác với atorvastatin, simvastatin) → ít tương tác thuốc hơn, an toàn hơn khi dùng với các thuốc ức chế CYP3A4.",
        "monitoring": [
            "Lipid profile (LDL, HDL, TG) sau 6-8 tuần, sau đó mỗi 3-6 tháng",
            "AST/ALT trước điều trị, sau 12 tuần, sau đó mỗi 6-12 tháng",
            "CK nếu có đau cơ, yếu cơ",
            "HbA1c/đường huyết (statin có thể tăng đường huyết)"
        ],
        "precautions": [
            "Kiểm tra CK nếu đau cơ hoặc yếu cơ (ngừng nếu CK >10 lần ULN)",
            "Ngừng nếu ALT >3 lần ULN",
            "Ưu điểm: ít tương tác với CYP3A4 inhibitors (an toàn hơn với clarithromycin, azole antifungals, amiodarone)",
            "Thận trọng với bệnh nhân đái tháo đường (có thể tăng đường huyết)",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ và cho con bú (category X)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "2 tuần",
            "duration": "24 giờ",
            "protein_binding": "50%",
            "metabolism": "Chuyển hóa qua gan (nhưng không qua CYP3A4) - ít tương tác",
            "clearance": "Chủ yếu qua thận (60%) và gan (40%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tiêu cơ vân - có thể gây suy thận cấp và tử vong. Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Gemfibrozil",
                    "mechanism": "Tăng nồng độ pravastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "TRÁNH DÙNG CHUNG. Nếu cần: dùng liều pravastatin thấp nhất, theo dõi CK chặt chẽ."
                },
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Tăng nồng độ pravastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều pravastatin xuống tối đa 20mg/ngày. Theo dõi CK chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng enzyme, giảm nồng độ pravastatin",
                    "effect": "Giảm hiệu quả",
                    "management": "Có thể cần tăng liều pravastatin."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động",
                "Có thai",
                "Cho con bú",
                "Tiêu cơ vân đang hoạt động"
            ],
            "tương_đối": [
                "Suy thận nặng - cần điều chỉnh liều",
                "Dùng với cyclosporine - giảm liều",
                "Dùng với gemfibrozil - tránh dùng chung"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định tuyệt đối trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Chống chỉ định khi cho con bú. Pravastatin bài tiết vào sữa mẹ và có thể gây hại cho trẻ sơ sinh.",
                "recommendation": "Không dùng khi cho con bú. Chọn phương pháp điều trị khác hoặc ngừng cho con bú nếu cần dùng pravastatin."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Nhưng theo dõi chức năng gan.",
            "moderate": "Thận trọng. Có thể cần giảm liều. Theo dõi chức năng gan chặt chẽ.",
            "severe": "Chống chỉ định nếu bệnh gan hoạt động.",
            "notes": "Pravastatin chuyển hóa một phần qua gan nhưng không phụ thuộc vào CYP3A4. Bệnh gan hoạt động là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Đau cơ nặng",
                "Yếu cơ",
                "Nước tiểu sẫm màu (myoglobinuria)",
                "Suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay pravastatin",
                "Bù dịch đầy đủ",
                "Lọc máu nếu suy thận cấp",
                "Theo dõi CK, creatinine"
            ],
            "monitoring": "Theo dõi CK, creatinine, chức năng thận, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Uống cùng một giờ mỗi ngày để nhớ."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Pravastatin chỉ có dạng uống (PO)."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <8 tuổi",
            "infants": "Không khuyến cáo cho trẻ <8 tuổi",
            "children": "8-13 tuổi: 10-20mg x 1 lần/ngày. 14-18 tuổi: 10-40mg x 1 lần/ngày. Chỉ dùng cho tăng cholesterol máu gia đình.",
            "adolescents": "10-40mg x 1 lần/ngày. Liều người lớn.",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng cholesterol máu gia đình ở trẻ ≥8 tuổi."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ. Suy gan, suy thận phổ biến hơn.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (10-20mg x 1 lần/ngày). Tăng dần chậm hơn.",
            "monitoring": "Theo dõi men gan, CK thường xuyên hơn. Cảnh báo về triệu chứng đau cơ, yếu cơ."
        },
        "brand_names": {
            "vietnam": ["Pravachol", "Pravastatin", "Pravastatin Stada"],
            "common": ["Pravachol", "Pravastatin"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "10,000 - 35,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Pravastatin generic thường rẻ hơn (10,000-25,000 VND/viên 20mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Pravachol (pravastatin)",
                "UpToDate - Pravastatin: Drug information",
                "ACC/AHA Guidelines - Cholesterol Management (2018)",
                "WOSCOPS Study - New England Journal of Medicine (1995)",
                "LIPID Study - New England Journal of Medicine (1998)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple large RCTs (WOSCOPS, LIPID) showing cardiovascular benefit"
        }
    },

    "Rosuvastatin": {
        "group": "Cardiovascular - Statin (HMG-CoA Reductase Inhibitor)",
        "vietnamese_name": "Rosuvastatin, Crestor",
        "administration": ["PO"],
        "indications": [
            "Tăng cholesterol máu",
            "Dự phòng biến cố tim mạch",
            "Sau nhồi máu cơ tim",
            "Bệnh động mạch vành",
            "Tăng cholesterol máu gia đình"
        ],
        "contraindications": [
            "Bệnh gan hoạt động",
            "Có thai",
            "Cho con bú",
            "Tiêu cơ vân đang hoạt động"
        ],
        "dosage": {
            "adult_standard": "5-20mg x 1 lần/ngày",
            "adult_high_intensity": "20-40mg x 1 lần/ngày",
            "adult_asian_or_creatinine_clearance": "Khởi đầu 5mg/ngày (tăng nguy cơ ở người châu Á, CrCl <60)",
            "notes": "Uống bất kỳ lúc nào trong ngày, có thể uống với thức ăn. Không chuyển hóa qua CYP3A4 → ít tương tác."
        },
        "side_effects": [
            "Đau cơ",
            "Tiêu cơ vân (hiếm nhưng nguy hiểm)",
            "Tăng men gan",
            "Protein niệu (với liều cao >40mg, thường nhẹ và không tiến triển)",
            "Tăng đường huyết (nhẹ)",
            "Suy giảm trí nhớ (hiếm)"
        ],
        "interactions": [
            "Cyclosporine: tăng nguy cơ tiêu cơ vân - giảm liều tối đa 5mg/ngày",
            "Gemfibrozil: tăng nguy cơ tiêu cơ vân - tránh dùng chung",
            "Warfarin: tăng INR - theo dõi INR",
            "Ít tương tác với CYP3A4 inhibitors (an toàn hơn với clarithromycin, azole antifungals)"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Ức chế HMG-CoA reductase, enzyme chính trong tổng hợp cholesterol, dẫn đến giảm LDL-cholesterol và tăng HDL-cholesterol. Rosuvastatin không chuyển hóa qua CYP3A4 (khác với atorvastatin, simvastatin) → ít tương tác thuốc hơn. Mạnh hơn atorvastatin (10mg rosuvastatin ≈ 20mg atorvastatin). Có thể gây protein niệu với liều cao.",
        "monitoring": [
            "Lipid profile (LDL, HDL, TG) sau 4-8 tuần, sau đó mỗi 3-6 tháng",
            "AST/ALT trước điều trị, sau 12 tuần, sau đó mỗi 6-12 tháng",
            "CK nếu có đau cơ, yếu cơ",
            "Protein niệu nếu dùng liều >40mg/ngày (thường nhẹ và không tiến triển)",
            "HbA1c/đường huyết (statin có thể tăng đường huyết)",
            "INR nếu dùng với warfarin"
        ],
        "precautions": [
            "Kiểm tra CK nếu đau cơ hoặc yếu cơ (ngừng nếu CK >10 lần ULN)",
            "Ngừng nếu ALT >3 lần ULN",
            "Protein niệu với liều cao (>40mg) - thường nhẹ và không tiến triển, không cần giảm liều",
            "Tăng nguy cơ ở người châu Á - khởi đầu với 5mg/ngày",
            "Ưu điểm: ít tương tác với CYP3A4 inhibitors (an toàn hơn với clarithromycin, azole antifungals)",
            "Thận trọng ở CrCl <60 - khởi đầu với 5mg/ngày",
            "CHỐNG CHỈ ĐỊNH trong thai kỳ và cho con bú (category X)"
        ],
        "pharmacokinetics": {
            "half_life": "19 giờ (dài nhất trong các statin)",
            "onset": "2 tuần",
            "duration": "24 giờ",
            "protein_binding": "88%",
            "metabolism": "Chuyển hóa ít qua gan (CYP2C9, không phải CYP3A4) - ít tương tác",
            "clearance": "Chủ yếu qua phân (90%) và thận (10%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Tiêu cơ vân - có thể gây suy thận cấp và tử vong. Đặc biệt nguy hiểm khi dùng với cyclosporine hoặc gemfibrozil. Chống chỉ định trong thai kỳ - có thể gây dị tật thai nhi.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Tăng nồng độ rosuvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "Giảm liều rosuvastatin xuống TỐI ĐA 5mg/ngày. Theo dõi CK chặt chẽ."
                },
                {
                    "drug": "Gemfibrozil",
                    "mechanism": "Tăng nồng độ rosuvastatin",
                    "effect": "Tăng nguy cơ tiêu cơ vân",
                    "management": "TRÁNH DÙNG CHUNG. Nếu cần: dùng liều rosuvastatin thấp nhất (5mg/ngày), theo dõi CK chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Rosuvastatin có thể tăng tác dụng warfarin",
                    "effect": "Tăng INR",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc thay đổi liều rosuvastatin. Điều chỉnh liều warfarin nếu cần."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Bệnh gan hoạt động",
                "Có thai",
                "Cho con bú",
                "Tiêu cơ vân đang hoạt động"
            ],
            "tương_đối": [
                "CrCl <60 - khởi đầu với 5mg/ngày",
                "Người châu Á - khởi đầu với 5mg/ngày",
                "Dùng với cyclosporine - giảm liều tối đa 5mg/ngày",
                "Dùng với gemfibrozil - tránh dùng chung"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Chống chỉ định tuyệt đối trong thai kỳ - có thể gây dị tật thai nhi và tử vong thai nhi.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Chống chỉ định khi cho con bú. Rosuvastatin bài tiết vào sữa mẹ và có thể gây hại cho trẻ sơ sinh.",
                "recommendation": "Không dùng khi cho con bú. Chọn phương pháp điều trị khác hoặc ngừng cho con bú nếu cần dùng rosuvastatin."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Nhưng theo dõi chức năng gan.",
            "moderate": "Thận trọng. Có thể cần giảm liều. Theo dõi chức năng gan chặt chẽ.",
            "severe": "Chống chỉ định nếu bệnh gan hoạt động.",
            "notes": "Rosuvastatin chuyển hóa ít qua gan (CYP2C9). Bệnh gan hoạt động là chống chỉ định."
        },
        "overdose_management": {
            "symptoms": [
                "Đau cơ nặng",
                "Yếu cơ",
                "Nước tiểu sẫm màu (myoglobinuria)",
                "Suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay rosuvastatin",
                "Bù dịch đầy đủ",
                "Lọc máu nếu suy thận cấp",
                "Theo dõi CK, creatinine"
            ],
            "monitoring": "Theo dõi CK, creatinine, chức năng thận, điện giải"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, bất kỳ lúc nào trong ngày. Uống cùng một giờ mỗi ngày để nhớ."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "Không áp dụng",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Rosuvastatin chỉ có dạng uống (PO)."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <10 tuổi",
            "infants": "Không khuyến cáo cho trẻ <10 tuổi",
            "children": "10-17 tuổi: 5-10mg x 1 lần/ngày. Chỉ dùng cho tăng cholesterol máu gia đình.",
            "adolescents": "5-20mg x 1 lần/ngày. Liều người lớn.",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho tăng cholesterol máu gia đình ở trẻ ≥10 tuổi."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ. Suy gan, suy thận phổ biến hơn.",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (5-10mg x 1 lần/ngày). Tăng dần chậm hơn.",
            "monitoring": "Theo dõi men gan, CK thường xuyên hơn. Cảnh báo về triệu chứng đau cơ, yếu cơ."
        },
        "brand_names": {
            "vietnam": ["Crestor", "Rosuvastatin", "Rosuvastatin Stada"],
            "common": ["Crestor", "Rosuvastatin"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "15,000 - 50,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Rosuvastatin generic thường rẻ hơn (15,000-30,000 VND/viên 10mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Crestor (rosuvastatin)",
                "UpToDate - Rosuvastatin: Drug information",
                "ACC/AHA Guidelines - Cholesterol Management (2018)",
                "JUPITER Study - New England Journal of Medicine (2008)",
                "HOPE-3 Study - New England Journal of Medicine (2016)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple large RCTs (JUPITER, HOPE-3) showing cardiovascular benefit"
        }
    }

}

__all__ = ['STATINS']
