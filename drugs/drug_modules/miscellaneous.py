"""
Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology
"""

MISCELLANEOUS_DRUGS = {
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
          "black_box_warnings": "Có thể gây phản ứng da nghiêm trọng (ban da, SJS, TEN) đe dọa tính mạng. Ngừng ngay nếu có ban da. Nguy cơ tăng ở bệnh nhân suy thận, dùng đồng thời với ampicillin/amoxicillin, hoặc có tiền sử dị ứng allopurinol",
          "drug_interactions": {
              "major": [
                  {
                      "drug": "Azathioprine, 6-Mercaptopurine",
                      "mechanism": "Allopurinol ức chế xanthine oxidase, enzyme chuyển hóa azathioprine và 6-mercaptopurine thành các chất không hoạt động. Ức chế enzyme này làm tăng nồng độ azathioprine/6-mercaptopurine trong máu.",
                      "effect": "Tăng nồng độ azathioprine/6-mercaptopurine đáng kể, tăng độc tính (giảm bạch cầu, độc gan, độc tủy xương)",
                      "management": "Giảm liều azathioprine/6-mercaptopurine 75% khi dùng với allopurinol. Theo dõi công thức máu và chức năng gan chặt chẽ. Hoặc tránh dùng đồng thời nếu có thể."
                  },
                  {
                      "drug": "Ampicillin, Amoxicillin",
                      "mechanism": "Cơ chế chưa rõ ràng, nhưng ampicillin/amoxicillin làm tăng nguy cơ phản ứng da nghiêm trọng với allopurinol.",
                      "effect": "Tăng nguy cơ ban da nghiêm trọng, SJS, TEN (đe dọa tính mạng)",
                      "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi sát dấu hiệu ban da. Ngừng ngay nếu có ban da."
                  },
                  {
                      "drug": "Warfarin",
                      "mechanism": "Allopurinol có thể ức chế chuyển hóa warfarin, làm tăng nồng độ warfarin.",
                      "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                      "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc điều chỉnh liều allopurinol. Điều chỉnh liều warfarin nếu cần."
                  }
              ],
              "moderate": [
                  {
                      "drug": "Theophylline",
                      "mechanism": "Allopurinol có thể ức chế chuyển hóa theophylline, làm tăng nồng độ theophylline.",
                      "effect": "Tăng nồng độ theophylline, tăng độc tính (nhịp tim nhanh, co giật)",
                      "management": "Theo dõi nồng độ theophylline và điều chỉnh liều nếu cần."
                  },
                  {
                      "drug": "Cyclophosphamide",
                      "mechanism": "Allopurinol có thể ức chế chuyển hóa cyclophosphamide, làm tăng độc tính.",
                      "effect": "Tăng độc tính cyclophosphamide",
                      "management": "Thận trọng khi dùng đồng thời. Theo dõi công thức máu và chức năng gan, thận."
                  }
              ],
              "minor": []
          },
          "contraindications": {
              "tuyệt_đối": [
                  "Dị ứng allopurinol",
                  "Có thai (category C)",
                  "Đang cho con bú",
                  "Phản ứng da nghiêm trọng trước đây với allopurinol (SJS, TEN)"
              ],
              "tương_đối": [
                  "Suy thận (giảm liều theo CrCl)",
                  "Suy gan (thận trọng, theo dõi chức năng gan)",
                  "Đang dùng azathioprine/6-mercaptopurine (cần giảm liều 75%)",
                  "Đang dùng ampicillin/amoxicillin (tăng nguy cơ ban da)"
              ]
          },
          "pregnancy_lactation": {
              "fda_category": "C",
              "pregnancy_details": "Allopurinol là category C. Không có dữ liệu đầy đủ về an toàn trong thai kỳ. Chỉ dùng nếu lợi ích > nguy cơ. Cân nhắc dùng liều thấp nhất hiệu quả.",
              "lactation": {
                  "safety": "Incompatible",
                  "details": "Allopurinol và oxypurinol bài tiết vào sữa mẹ. Không nên dùng khi cho con bú do thiếu dữ liệu về an toàn cho trẻ bú mẹ.",
                  "recommendation": "KHÔNG dùng khi cho con bú. Ngừng cho con bú hoặc ngừng allopurinol."
              }
          },
          "hepatic_adjustment": {
              "mild": "Không cần điều chỉnh liều. Theo dõi chức năng gan.",
              "moderate": "Thận trọng, theo dõi chức năng gan. Có thể cần giảm liều nhẹ.",
              "severe": "Thận trọng, theo dõi chức năng gan chặt chẽ. Có thể cần giảm liều hoặc tránh dùng.",
              "notes": "Allopurinol chuyển hóa một phần qua gan. Suy gan có thể làm tăng nồng độ và độc tính. Theo dõi ALT, AST định kỳ."
          },
          "overdose_management": {
              "symptoms": [
                  "Ban da (có thể tiến triển thành SJS/TEN nếu nặng)",
                  "Buồn nôn, nôn",
                  "Đau đầu",
                  "Tăng men gan",
                  "Suy thận (hiếm)",
                  "Phản ứng dị ứng nặng"
              ],
              "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
              "treatment": [
                  "Ngừng allopurinol ngay lập tức",
                  "Nếu có ban da: đánh giá mức độ nghiêm trọng, nếu SJS/TEN: điều trị như bỏng nặng (ICU, chăm sóc vết thương, điều trị nhiễm trùng)",
                  "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                  "Than hoạt tính nếu uống trong vòng 1-2 giờ",
                  "Theo dõi chức năng gan, thận",
                  "Điều trị hỗ trợ: truyền dịch nếu cần",
                  "Nếu SJS/TEN: điều trị tại ICU, có thể cần corticosteroid, IVIG"
              ],
              "monitoring": "Dấu hiệu ban da, chức năng gan, thận, dấu hiệu dị ứng. Nếu SJS/TEN: theo dõi tại ICU."
          },
          "reversal_agents": {
              "available": False,
              "agents": []
          },
          "administration_instructions": {
              "oral": {
                  "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                  "timing": "Uống 1 lần/ngày sau bữa ăn. Uống với nhiều nước (2-3L/ngày) để tránh sỏi thận. Uống cùng thời điểm mỗi ngày."
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
                  "FDA Drug Label - Allopurinol (Zyloric, Aloprim)",
                  "American College of Rheumatology Guidelines - Gout Management",
                  "UpToDate - Allopurinol drug information",
                  "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                  "Lexicomp Online - Allopurinol Monograph"
              ],
              "last_updated": "2024-12-19",
              "evidence_level": "A - Dựa trên FDA drug labels, ACR guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
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
        "black_box_warnings": None,
        "drug_interactions": {
            "moderate": [
                {
                    "drug": "Methotrexate",
                    "mechanism": "Folic acid giảm hiệu quả methotrexate (methotrexate ức chế dihydrofolate reductase, folic acid bổ sung folate)",
                    "effect": "Giảm hiệu quả methotrexate (nhưng dùng để giảm độc tính methotrexate)",
                    "management": "Dùng folic acid 24 giờ sau methotrexate (không dùng cùng lúc). Theo dõi đáp ứng điều trị methotrexate"
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Folic acid giảm nồng độ phenytoin (cơ chế chưa rõ)",
                    "effect": "Giảm nồng độ phenytoin, giảm hiệu quả chống co giật",
                    "management": "Theo dõi nồng độ phenytoin, có thể cần tăng liều phenytoin"
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng folic acid"
            ],
            "tương_đối": [
                "Ung thư - thận trọng (folic acid có thể kích thích tế bào ung thư)",
                "Thiếu vitamin B12 chưa được điều trị - thận trọng (folic acid có thể che dấu thiếu B12, dẫn đến tổn thương thần kinh)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Khuyến nghị dùng trong thai kỳ. Folic acid rất quan trọng cho sự phát triển bình thường của ống thần kinh trong thai kỳ (tuần 3-4), giúp ngăn ngừa dị tật ống thần kinh (spina bifida, anencephaly). Nên bắt đầu trước khi có thai 1 tháng và tiếp tục trong 3 tháng đầu thai kỳ. Liều dự phòng: 0.4-0.8mg/ngày. Liều điều trị thiếu máu: 1-5mg/ngày.",
            "lactation": {
                "safety": "Compatible",
                "details": "Folic acid bài tiết vào sữa mẹ ở nồng độ thấp. An toàn cho trẻ bú mẹ. Folic acid trong sữa mẹ có lợi cho trẻ.",
                "recommendation": "Có thể dùng an toàn khi cho con bú. Liều thường dùng (0.4-5mg/ngày) an toàn cho trẻ bú mẹ"
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi liều",
            "moderate": "Không đổi liều",
            "severe": "Không đổi liều",
            "notes": "Folic acid là vitamin, không chuyển hóa ở gan. Suy gan không ảnh hưởng đến folic acid"
        },
        "overdose_management": {
            "symptoms": [
                "Hiếm khi có triệu chứng (folic acid ít độc)",
                "Phản ứng dị ứng (hiếm)",
                "Có thể che dấu thiếu B12 nếu dùng liều cao (>1mg/ngày)"
            ],
            "antidote": "Không có thuốc giải độc đặc hiệu",
            "treatment": [
                "Ngừng thuốc nếu có phản ứng dị ứng",
                "Điều trị hỗ trợ: Truyền dịch nếu cần",
                "Kiểm tra nồng độ vitamin B12 nếu dùng liều cao lâu dài",
                "Điều trị dị ứng nếu có (antihistamine, corticosteroid)"
            ],
            "monitoring": "Triệu chứng lâm sàng, dấu hiệu dị ứng, nồng độ vitamin B12 (nếu dùng liều cao lâu dài)"
        },
        "reversal_agents": {
            "available": False,
            "agents": None,
            "notes": "Không có thuốc giải độc đặc hiệu. Folic acid ít độc, hiếm khi cần điều trị đặc biệt"
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không. Uống với thức ăn có thể giảm kích ứng dạ dày nhẹ (nếu có)",
                "timing": "Với thiếu máu: 1-5mg x 1 lần/ngày. Với dự phòng dị tật ống thần kinh: 0.4-0.8mg x 1 lần/ngày (bắt đầu trước khi có thai 1 tháng, tiếp tục trong 3 tháng đầu). Với methotrexate: 5-10mg/tuần (dùng 24 giờ sau methotrexate, không dùng cùng lúc)",
                "notes": "Dùng kèm vitamin B12 khi thiếu máu (folic acid có thể che dấu thiếu B12). Với thiếu máu: luôn kiểm tra B12 trước khi dùng folic acid. Với methotrexate: dùng 24 giờ sau methotrexate (không dùng cùng lúc)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Folic Acid",
                "UpToDate - Folic acid drug information",
                "CDC Guidelines for folic acid supplementation in pregnancy",
                "WHO Guidelines for folic acid supplementation",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "High - Guidelines dựa trên chứng cứ từ CDC, WHO và FDA"
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
            "tuyệt_đối": [
                "Suy gan nặng (Child-Pugh C)",
                "Dị ứng paracetamol",
                "Quá liều paracetamol (đang trong quá trình điều trị)"
            ],
            "tương_đối": [
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
            "tuyệt_đối": [
                "Dị ứng NSAID hoặc aspirin (quá mẫn cảm, phản ứng dị ứng nghiêm trọng)",
                "Loét dạ dày tá tràng hoạt động",
                "Xuất huyết tiêu hóa đang hoạt động",
                "Suy thận nặng (CrCl <30 ml/min) hoặc đang lọc máu",
                "Suy gan nặng (Child-Pugh C)",
                "Suy tim nặng (NYHA class IV)",
                "Có thai (3 tháng cuối) - đóng ống động mạch sớm",
                "Trẻ em <6 tháng tuổi"
            ],
            "tương_đối": [
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
            "tuyệt_đối": [
                "Dị ứng salbutamol hoặc các thành phần trong chế phẩm",
                "Nhịp tim nhanh nặng không kiểm soát (>120 bpm ở người lớn, >150 bpm ở trẻ em)",
                "Rối loạn nhịp tim nặng (rung nhĩ, rung thất không kiểm soát)",
                "Cường giáp không điều trị (tăng nhạy cảm với catecholamine)"
            ],
            "tương_đối": [
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
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ritonavir (HIV protease inhibitor)",
                    "mechanism": "Ritonavir ức chế CYP3A4 mạnh, làm giảm chuyển hóa budesonide, tăng nồng độ budesonide đáng kể.",
                    "effect": "Tăng nồng độ budesonide đáng kể, tăng nguy cơ ức chế trục HPA, tác dụng phụ toàn thân (Cushing, tăng đường huyết, ức chế miễn dịch)",
                    "management": "TRÁNH DÙNG cùng. Nếu bắt buộc, giảm liều budesonide đáng kể hoặc dùng corticosteroid hít khác (fluticasone ít bị ảnh hưởng hơn). Theo dõi dấu hiệu ức chế HPA."
                }
            ],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole, Voriconazole (Azole antifungals)",
                    "mechanism": "Azole antifungals ức chế CYP3A4, làm giảm chuyển hóa budesonide.",
                    "effect": "Tăng nồng độ budesonide, tăng nguy cơ tác dụng phụ toàn thân",
                    "management": "Thận trọng. Có thể cần giảm liều budesonide. Theo dõi dấu hiệu ức chế HPA."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng budesonide",
                "Nhiễm trùng đường hô hấp không điều trị (lao phổi, nhiễm nấm) - corticosteroid có thể làm nặng nhiễm trùng"
            ],
            "tương_đối": [
                "Lao phổi - cần điều trị lao trước, thận trọng",
                "Nhiễm nấm đường hô hấp - cần điều trị trước",
                "Có thai - category C, thận trọng",
                "Đang dùng ritonavir - tăng nguy cơ ức chế HPA"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Budesonide là category C. Có thể dùng trong thai kỳ nếu lợi ích > nguy cơ. Corticosteroid hít có ít tác dụng toàn thân hơn corticosteroid uống, nhưng vẫn có thể ảnh hưởng đến thai nhi ở liều cao. Dùng liều thấp nhất hiệu quả.",
            "lactation": {
                "safety": "Compatible",
                "details": "Budesonide bài tiết vào sữa mẹ ở nồng độ rất thấp do chuyển hóa nhanh ở gan. An toàn cho trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Budesonide chuyển hóa ở gan nhưng suy gan nhẹ không ảnh hưởng đáng kể.",
            "moderate": "Thận trọng, có thể tăng nồng độ nhẹ. Theo dõi dấu hiệu tác dụng phụ toàn thân.",
            "severe": "Thận trọng, có thể tăng nồng độ. Giảm liều nếu có dấu hiệu tác dụng phụ toàn thân.",
            "notes": "Budesonide chuyển hóa nhanh ở gan qua CYP3A4 (first-pass metabolism cao). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ toàn thân."
        },
        "overdose_management": {
            "symptoms": [
                "Tác dụng toàn thân: ức chế trục HPA, Cushing, tăng đường huyết, tăng huyết áp",
                "Nấm miệng nặng (nếu không súc miệng)",
                "Khàn tiếng, ho nặng",
                "Ức chế miễn dịch (tăng nguy cơ nhiễm trùng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng budesonide hoặc giảm liều đáng kể",
                "Nếu ức chế HPA: điều trị hỗ trợ, có thể cần corticosteroid thay thế tạm thời",
                "Nếu nấm miệng: điều trị nấm (nystatin, fluconazole)",
                "Theo dõi đường huyết, huyết áp, dấu hiệu nhiễm trùng",
                "Theo dõi chức năng thượng thận nếu có dấu hiệu ức chế HPA"
            ],
            "monitoring": "Đường huyết, huyết áp, dấu hiệu ức chế HPA, dấu hiệu nhiễm trùng, nấm miệng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - dạng hít",
                "timing": "N/A - dạng hít"
            },
            "iv": {
                "reconstitution": "N/A - chỉ có dạng hít",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng hít (MDI/DPI) và nebulizer"
            },
            "inhaled": {
                "technique": "MDI: Lắc kỹ, thở ra hoàn toàn, đặt ống ngậm vào miệng, bấm và hít sâu chậm, giữ hơi 10 giây. DPI: Thở ra hoàn toàn, đặt ống ngậm vào miệng, hít mạnh và sâu, giữ hơi 10 giây.",
                "after_use": "Súc miệng và súc họng sau mỗi lần dùng để tránh nấm miệng - QUAN TRỌNG",
                "frequency": "2 lần/ngày (sáng và tối), cách đều"
            },
            "nebulizer": {
                "preparation": "Lắc kỹ suspension trước khi dùng. Đổ vào buồng nebulizer. Dùng trong vòng 2 giờ sau khi mở gói.",
                "administration": "Thở bình thường qua ống ngậm hoặc mặt nạ cho đến khi hết thuốc (thường 5-15 phút).",
                "after_use": "Súc miệng và súc họng sau khi dùng. Rửa sạch thiết bị nebulizer."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Budesonide (Pulmicort)",
                "UpToDate - Budesonide: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-04",
            "evidence_level": "A - Dựa trên FDA drug labels và dữ liệu lâm sàng"
        }
    },

}

__all__ = ['MISCELLANEOUS_DRUGS']
