"""
Selective Beta-blockers
Beta-1 selective adrenergic blocking agents
"""
SELECTIVE_BETA_BLOCKERS = {
    "Metoprolol": {
        "group": "Cardiovascular - Beta-blocker",
        "vietnamese_name": "Metoprolol, Betaloc",
        "administration": ["PO", "IV"],
        "indications": [
            "Tăng huyết áp",
            "Suy tim",
            "Rối loạn nhịp tim",
            "Sau nhồi máu cơ tim",
            "Đau thắt ngực"
        ],
        "contraindications": [
            "Hen phế quản nặng",
            "Block nhĩ thất độ 2-3",
            "Suy tim cấp không bù",
            "Nhịp tim chậm nặng"
        ],
        "dosage": {
            "adult_po": "25-200mg x 2 lần/ngày (tartrate) hoặc 50-200mg x 1 lần/ngày (succinate)",
            "adult_iv": "2.5-5mg IV mỗi 5 phút x 3 lần (tối đa 15mg)",
            "heart_failure": "12.5-25mg x 2 lần/ngày, tăng dần đến 200mg x 2 lần/ngày",
            "notes": "Tartrate: ngắn tác dụng, Succinate: dài tác dụng"
        },
        "side_effects": [
            "Mệt mỏi",
            "Lạnh tay chân",
            "Nhịp tim chậm",
            "Rối loạn giấc ngủ",
            "Khó thở ở bệnh nhân hen/COPD"
        ],
        "interactions": [
            "Verapamil/Diltiazem: tăng nguy cơ block nhĩ thất",
            "Insulin: che dấu triệu chứng hạ đường huyết",
            "NSAID: giảm hiệu quả"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ức chế thụ thể beta-1 chọn lọc, giảm nhịp tim, lực co bóp cơ tim, và dẫn truyền nhĩ thất",
        "monitoring": [
            "Huyết áp, nhịp tim mỗi lần khám",
            "ECG nếu có triệu chứng block nhĩ thất",
            "Đường huyết ở bệnh nhân đái tháo đường (che dấu triệu chứng hạ đường huyết)",
            "Chức năng gan, thận định kỳ"
        ],
        "precautions": [
            "Không ngừng đột ngột (có thể gây cơn tăng huyết áp phản hồi)",
            "Giảm liều từ từ khi ngừng",
            "Thận trọng với bệnh nhân hen/COPD (có thể gây co thắt phế quản)",
            "Theo dõi suy tim mới xuất hiện"
        ],
        "pharmacokinetics": {
            "half_life": "3-7 giờ (tartrate), 3-4 giờ (succinate)",
            "onset": "1-2 giờ (PO), 15 phút (IV)",
            "duration": "6-12 giờ (tartrate), 24 giờ (succinate)",
            "protein_binding": "12%",
            "clearance": "Gan (CYP2D6)"
                },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Không ngừng đột ngột - có thể gây tăng huyết áp phản hồi, đau thắt ngực, nhồi máu cơ tim. Giảm liều từ từ trong 1-2 tuần. Suy tim cấp có thể xảy ra nếu dùng ở bệnh nhân suy tim không bù trừ",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Verapamil, Diltiazem",
                    "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất và co bóp tim",
                    "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, nhịp tim chậm nặng, suy tim",
                    "management": "Thận trọng. Tránh dùng cùng nếu có thể. Nếu cần, dùng liều thấp và theo dõi ECG sát."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, các thuốc hạ đường huyết",
                    "mechanism": "Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run rẩy)",
                    "effect": "Tăng nguy cơ hạ đường huyết không được phát hiện, nguy hiểm",
                    "management": "Theo dõi đường huyết thường xuyên. Bệnh nhân đái tháo đường nên biết các triệu chứng khác của hạ đường huyết."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "Giảm tác dụng hạ huyết áp",
                    "effect": "Giảm hiệu quả điều trị tăng huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp. Tránh dùng lâu dài cùng."
                },
                {
                    "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                    "mechanism": "Ức chế chuyển hóa metoprolol",
                    "effect": "Tăng nồng độ metoprolol, tăng tác dụng phụ",
                    "management": "Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều metoprolol."
                }
            ],
            "minor": [
                {
                    "drug": "Diphenhydramine",
                    "mechanism": "Tăng nguy cơ an thần",
                    "effect": "Tăng tác dụng an thần",
                    "management": "Thận trọng. Tránh lái xe hoặc vận hành máy móc."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Hen phế quản nặng",
                "Block nhĩ thất độ 2-3",
                "Suy tim cấp không bù",
                "Nhịp tim chậm nặng (<50 bpm)",
                "Sốc tim",
                "Hội chứng sick sinus (trừ khi có máy tạo nhịp)"
            ],
            "tương_đối": [
                "COPD (thận trọng, có thể dùng liều thấp)",
                "Đái tháo đường (che dấu triệu chứng hạ đường huyết)",
                "Bệnh mạch máu ngoại biên (có thể làm nặng)",
                "Suy gan (giảm chuyển hóa)",
                "Dùng với verapamil/diltiazem (tăng nguy cơ block AV)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Có thể dùng khi cần thiết. Có thể gây nhịp tim chậm thai nhi, hạ đường huyết, giảm thông khí. Theo dõi sát thai nhi. Ưu tiên dùng trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Metoprolol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu nhịp tim chậm hoặc hạ đường huyết."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều (chuyển hóa qua gan)",
            "severe": "Giảm liều 50% (chuyển hóa qua gan CYP2D6)",
            "notes": "Metoprolol chuyển hóa qua gan (CYP2D6). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim chậm nặng (<40 bpm)",
                "Block nhĩ thất độ 2-3",
                "Hạ huyết áp nặng",
                "Suy tim cấp",
                "Co thắt phế quản",
                "Hạ đường huyết",
                "Ngất"
            ],
            "antidote": "Atropine (cho nhịp tim chậm), Glucagon (cho suy tim), Epinephrine (cho hạ huyết áp nặng)",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại",
                "Nếu atropine không hiệu quả: Glucagon 1-5mg IV (kích thích tim qua cơ chế không phụ thuộc beta-receptor)",
                "Điều trị hạ huyết áp: Truyền dịch, nâng chân, nếu cần: dopamine, norepinephrine",
                "Điều trị block AV: Atropine, nếu cần: máy tạo nhịp tạm thời",
                "Điều trị co thắt phế quản: Albuterol, ipratropium",
                "Điều trị hạ đường huyết: Glucose IV",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi ít nhất 12-24 giờ (do half-life 3-7 giờ)"
            ],
            "monitoring": "Nhịp tim, huyết áp, ECG (block AV, rối loạn nhịp), đường huyết, chức năng hô hấp, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Glucagon",
                    "mechanism": "Kích thích tim qua cơ chế không phụ thuộc beta-receptor (tăng cAMP)",
                    "indication": "Suy tim, nhịp tim chậm nặng do beta-blocker",
                    "dose": "1-5mg IV, có thể lặp lại"
                },
                {
                    "name": "Atropine",
                    "mechanism": "Ức chế phó giao cảm, tăng nhịp tim",
                    "indication": "Nhịp tim chậm, block nhĩ thất",
                    "dose": "0.5-1mg IV, có thể lặp lại"
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm tác dụng phụ đầu tiên.",
                "timing": "Tartrate: 2 lần/ngày. Succinate: 1 lần/ngày. Uống cùng giờ mỗi ngày. KHÔNG ngừng đột ngột - giảm liều dần dần trong 1-2 tuần."
            },
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ. Không pha loãng.",
                "infusion_rate": "Tiêm trực tiếp 2.5-5mg mỗi 5 phút, tối đa 15mg. Theo dõi ECG và huyết áp sát.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": [],
                "notes": "Dùng cho cấp cứu. Theo dõi ECG và huyết áp liên tục. Chuyển sang PO càng sớm càng tốt."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
            "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế). Nếu cần, 1-2mg/kg/ngày chia 2 lần, tối đa 200mg/ngày",
            "adolescents": "25-50mg x 2 lần/ngày (tartrate) hoặc 50-100mg x 1 lần/ngày (succinate), tăng dần. Liều người lớn",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng khi thực sự cần thiết. Theo dõi nhịp tim, huyết áp, chức năng gan chặt chẽ"
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (nhịp tim chậm, hạ huyết áp, mệt mỏi). Suy gan phổ biến hơn",
            "dose_adjustment": "Khởi đầu với liều thấp hơn (12.5-25mg x 2 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo chức năng gan",
            "monitoring": "Theo dõi nhịp tim, huyết áp sát hơn. Theo dõi chức năng gan. Cảnh báo về không ngừng đột ngột"
        },
        "brand_names": {
            "vietnam": ["Betaloc", "Metoprolol Stada", "Metoprolol", "Lopressor", "Toprol-XL"],
            "common": ["Lopressor", "Toprol-XL", "Metoprolol", "Betaloc"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "8,000 - 25,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Metoprolol generic thường rẻ hơn (8,000-15,000 VND/viên 50mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lopressor (metoprolol tartrate), Toprol-XL (metoprolol succinate)",
                "UpToDate - Metoprolol: Drug information",
                "MERIT-HF Study - The Lancet",
                "Goteborg Metoprolol Trial - The Lancet",
                "American Heart Association/American College of Cardiology guidelines"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (MERIT-HF, Goteborg) and extensive clinical experience"
        }
    },

    "Atenolol": {
    "group": "Cardiovascular - Beta-blocker (Selective)",
    "vietnamese_name": "Atenolol, Tenormin",
    "administration": ["PO"],
    "indications": [
        "Tăng huyết áp",
        "Đau thắt ngực",
        "Sau nhồi máu cơ tim",
        "Rối loạn nhịp tim"
    ],
    "contraindications": [
        "Hen phế quản nặng",
        "Block nhĩ thất độ 2-3",
        "Suy tim cấp không bù",
        "Nhịp tim chậm nặng"
    ],
    "dosage": {
        "adult_htn": "25-100mg x 1 lần/ngày",
        "adult_angina": "50-100mg x 1 lần/ngày",
        "adult_post_mi": "50-100mg x 1 lần/ngày",
        "notes": "Uống 1 lần/ngày. Chọn lọc beta-1"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "Giảm liều 75%, hoặc dùng mỗi 2 ngày"
    },
    "side_effects": [
        "Mệt mỏi",
        "Lạnh tay chân",
        "Nhịp tim chậm",
        "Rối loạn giấc ngủ",
        "Khó thở ở bệnh nhân hen/COPD"
    ],
          "interactions": [
          "Verapamil/Diltiazem: tăng nguy cơ block nhĩ thất",
          "Insulin: che dấu triệu chứng hạ đường huyết"
      ],
      "pregnancy": "D",
      "mechanism_of_action": "Selective beta-1 adrenergic receptor blocker. Ức chế tác dụng của catecholamines (epinephrine, norepinephrine) trên beta-1 receptors ở tim, giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp, giảm nhu cầu oxy cơ tim. Chọn lọc beta-1 hơn metoprolol, ít tác dụng trên beta-2 (ít gây co thắt phế quản hơn propranolol). Thải chủ yếu qua thận (khác với metoprolol - thải qua gan).",
      "monitoring": [
          "Nhịp tim và huyết áp (trước và sau khi bắt đầu)",
          "Chức năng thận: creatinine, BUN (thải chủ yếu qua thận - cần điều chỉnh liều)",
          "Dấu hiệu suy tim (khó thở, phù, tăng cân)",
          "Đường huyết (ở bệnh nhân đái tháo đường - che dấu triệu chứng hạ đường huyết)",
          "Triệu chứng mệt mỏi, lạnh tay chân"
      ],
      "precautions": [
          "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng). Phải giảm liều dần trong 1-2 tuần",
          "Thải chủ yếu qua thận - cần giảm liều ở bệnh nhân suy thận (CrCl <30: giảm 75% hoặc dùng mỗi 2 ngày)",
          "Thận trọng ở bệnh nhân hen phế quản/COPD (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản ở liều cao)",
          "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <50 bpm",
          "Thận trọng ở bệnh nhân đái tháo đường (che dấu triệu chứng hạ đường huyết)",
          "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)"
      ],
      "pharmacokinetics": {
          "half_life": "6-7 giờ (dài hơn metoprolol)",
          "onset": "1 giờ (PO)",
          "duration": "24 giờ (uống 1 lần/ngày)",
          "protein_binding": "5-15% (thấp, ít protein binding)",
          "clearance": "Thận (chủ yếu, 85-100% thải nguyên dạng qua nước tiểu). Không chuyển hóa qua gan"
      },
      "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
      "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực hoặc sau nhồi máu cơ tim - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, rối loạn nhịp tim nặng. Phải giảm liều dần dần trong 1-2 tuần",
      "drug_interactions": {
          "major": [
              {
                  "drug": "Verapamil, Diltiazem",
                  "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                  "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, suy tim, nhịp tim chậm nặng",
                  "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp. Tránh dùng cùng nếu có thể."
              },
              {
                  "drug": "Clonidine (khi ngừng đột ngột)",
                  "mechanism": "Cả hai đều ức chế giao cảm, ngừng clonidine đột ngột gây rebound hypertension",
                  "effect": "Tăng huyết áp nghiêm trọng, có thể gây đột quỵ",
                  "management": "Không ngừng clonidine đột ngột khi đang dùng atenolol. Giảm liều clonidine dần."
              }
          ],
          "moderate": [
              {
                  "drug": "Insulin, Sulfonylureas (thuốc điều trị đái tháo đường)",
                  "mechanism": "Che dấu triệu chứng hạ đường huyết (nhịp tim nhanh, run), tăng nguy cơ hạ đường huyết kéo dài",
                  "effect": "Hạ đường huyết nặng, khó nhận biết triệu chứng",
                  "management": "Theo dõi đường huyết thường xuyên. Bệnh nhân đái tháo đường nên biết triệu chứng hạ đường huyết khác (đổ mồ hôi, lú lẫn)."
              },
              {
                  "drug": "Digoxin",
                  "mechanism": "Tăng nguy cơ block nhĩ thất",
                  "effect": "Nhịp tim chậm nặng, block AV",
                  "management": "Theo dõi nhịp tim, ECG. Có thể cần giảm liều digoxin."
              },
              {
                  "drug": "NSAIDs (ibuprofen, naproxen)",
                  "mechanism": "NSAID làm giảm tác dụng hạ huyết áp của beta-blocker",
                  "effect": "Giảm hiệu quả hạ huyết áp",
                  "management": "Thận trọng. Theo dõi huyết áp. Tránh dùng lâu dài cùng."
              }
          ],
          "minor": [
              {
                  "drug": "Rifampin",
                  "mechanism": "Có thể tăng chuyển hóa atenolol (mặc dù thải chủ yếu qua thận)",
                  "effect": "Giảm hiệu quả atenolol",
                  "management": "Theo dõi huyết áp, nhịp tim. Có thể cần tăng liều atenolol."
              }
          ]
      },
      "contraindications": {
          "tuyệt_đối": [
              "Hen phế quản nặng",
              "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
              "Suy tim cấp không bù",
              "Nhịp tim chậm nặng (<50 bpm)",
              "Sốc tim"
          ],
          "tương_đối": [
              "COPD - thận trọng (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản)",
              "Suy thận nặng (CrCl <30) - giảm liều 75% hoặc dùng mỗi 2 ngày",
              "Suy thận trung bình (CrCl 30-60) - giảm liều 50%",
              "Đái tháo đường - thận trọng (che dấu triệu chứng hạ đường huyết)",
              "Bệnh mạch máu ngoại vi (Raynaud) - có thể làm nặng thêm",
              "Dùng với verapamil/diltiazem - tăng nguy cơ block AV"
          ]
      },
      "pregnancy_lactation": {
          "fda_category": "D",
          "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm, suy hô hấp ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm, hạ đường huyết ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được nếu lợi ích vượt trội nguy cơ.",
          "lactation": {
              "safety": "Compatible",
              "details": "Atenolol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Có thể gây nhịp tim chậm nhẹ ở trẻ bú mẹ nhưng hiếm.",
              "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi, tăng cân kém."
          }
      },
      "hepatic_adjustment": {
          "mild": "Không đổi",
          "moderate": "Không đổi (thải chủ yếu qua thận)",
          "severe": "Không đổi (thải chủ yếu qua thận)",
          "notes": "Atenolol thải chủ yếu qua thận (85-100% thải nguyên dạng qua nước tiểu), không chuyển hóa qua gan. Suy gan không ảnh hưởng đến dược động học của atenolol."
      },
      "overdose_management": {
          "symptoms": [
              "Nhịp tim chậm nặng (<40 bpm)",
              "Block nhĩ thất độ 2-3",
              "Hạ huyết áp nặng",
              "Suy tim cấp",
              "Co giật",
              "Hôn mê",
              "Suy hô hấp"
          ],
          "antidote": "Glucagon (có thể đảo ngược tác dụng beta-blocker), Atropine (cho nhịp tim chậm), Epinephrine (cho hạ huyết áp nặng)",
          "treatment": [
              "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
              "Than hoạt tính",
              "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Glucagon 1-5mg IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
              "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Glucagon 1-5mg IV, Epinephrine (thận trọng - có thể gây tăng huyết áp quá mức)",
              "Theo dõi ECG liên tục",
              "Theo dõi huyết áp, nhịp tim, ý thức",
              "Hỗ trợ hô hấp nếu cần",
              "Theo dõi ít nhất 12-24 giờ (do half-life 6-7 giờ)"
          ],
          "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu suy hô hấp"
      },
      "reversal_agents": {
          "available": True,
          "agents": [
              {
                  "name": "Glucagon",
                  "mechanism": "Kích thích cAMP, đảo ngược tác dụng beta-blocker",
                  "dose": "1-5mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, hạ huyết áp do quá liều beta-blocker"
              },
              {
                  "name": "Atropine",
                  "mechanism": "Chẹn muscarinic, tăng nhịp tim",
                  "dose": "0.5-1mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, block AV"
              },
              {
                  "name": "Epinephrine",
                  "mechanism": "Agonist alpha và beta, tăng nhịp tim và huyết áp",
                  "dose": "Theo protocol ACLS",
                  "indication": "Hạ huyết áp nặng không đáp ứng với glucagon"
              }
          ]
      },
      "administration_instructions": {
          "oral": {
              "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
              "timing": "Uống 1 lần/ngày vào cùng một giờ mỗi ngày. Không ngừng đột ngột - phải giảm liều dần trong 1-2 tuần."
          },
          "iv": {
              "reconstitution": "Không có dạng IV",
              "infusion_rate": "Không áp dụng",
              "compatibility": [],
              "incompatibility": [],
              "notes": "Atenolol chỉ có dạng uống (PO)."
          }
      },
      "pediatric_dosing": {
          "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
          "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
          "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế). Nếu cần, 0.5-1mg/kg/ngày x 1 lần, tối đa 100mg/ngày",
          "adolescents": "25-50mg x 1 lần/ngày, tăng dần đến 100mg/ngày nếu cần. Liều người lớn",
          "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng khi thực sự cần thiết. Theo dõi nhịp tim, huyết áp, chức năng thận chặt chẽ"
      },
      "geriatric_dosing": {
          "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (nhịp tim chậm, hạ huyết áp, mệt mỏi). Suy thận phổ biến hơn",
          "dose_adjustment": "Khởi đầu với liều thấp hơn (12.5-25mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo CrCl (giảm liều 50-75% nếu CrCl <60)",
          "monitoring": "Theo dõi nhịp tim, huyết áp sát hơn. Theo dõi chức năng thận. Cảnh báo về không ngừng đột ngột"
      },
      "brand_names": {
          "vietnam": ["Tenormin", "Atenolol Stada", "Atenolol"],
          "common": ["Tenormin", "Atenolol"]
      },
      "cost_estimate": {
          "unit": "VND",
          "range": "5,000 - 20,000 VND/viên (tùy hàm lượng và thương hiệu)",
          "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Atenolol generic thường rẻ hơn (5,000-12,000 VND/viên 50mg)."
      },
      "references": {
          "primary_sources": [
              "FDA Drug Label - Tenormin (atenolol)",
              "UpToDate - Atenolol: Drug information",
              "ISIS-1 Study - Lancet (1986) - Beta-blocker sau nhồi máu cơ tim",
              "American Heart Association/American College of Cardiology guidelines - Beta-blockers in hypertension and heart failure"
          ],
          "last_updated": "2024-12-19",
          "evidence_level": "High - Multiple large RCTs (ISIS-1) and extensive clinical experience"
      }
    },

    "Bisoprolol": {
    "group": "Cardiovascular - Beta-blocker (Selective)",
    "vietnamese_name": "Bisoprolol, Concor",
    "administration": ["PO"],
    "indications": [
        "Tăng huyết áp",
        "Suy tim (NYHA class II-IV)",
        "Đau thắt ngực"
    ],
    "contraindications": [
        "Hen phế quản nặng",
        "Block nhĩ thất độ 2-3",
        "Suy tim cấp không bù",
        "Nhịp tim chậm nặng (<60 bpm)"
    ],
    "dosage": {
        "adult_htn": "2.5-10mg x 1 lần/ngày",
        "adult_heart_failure": "1.25mg x 1 lần/ngày, tăng dần đến 10mg x 1 lần/ngày",
        "adult_angina": "5-10mg x 1 lần/ngày",
        "notes": "Uống 1 lần/ngày. Có bằng chứng giảm tỷ lệ tử vong trong suy tim"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Thận trọng, có thể giảm liều",
        "under_30": "Thận trọng, giảm liều"
    },
    "side_effects": [
        "Mệt mỏi",
        "Lạnh tay chân",
        "Nhịp tim chậm",
        "Chóng mặt",
        "Khó thở ở bệnh nhân hen/COPD"
    ],
          "interactions": [
          "Verapamil/Diltiazem: tăng nguy cơ block nhĩ thất",
          "Insulin: che dấu triệu chứng hạ đường huyết"
      ],
      "pregnancy": "C",
      "mechanism_of_action": "Selective beta-1 adrenergic receptor blocker. Ức chế tác dụng của catecholamines trên beta-1 receptors ở tim, giảm nhịp tim, giảm co bóp cơ tim, giảm huyết áp. Có bằng chứng mạnh làm giảm tỷ lệ tử vong và nhập viện trong suy tim mạn tính (NYHA class II-IV). Thải qua cả thận và gan (50-50%).",
      "monitoring": [
          "Nhịp tim và huyết áp (trước và sau khi bắt đầu, đặc biệt ở bệnh nhân suy tim)",
          "Dấu hiệu suy tim: khó thở, phù, tăng cân, giảm khả năng gắng sức",
          "Chức năng thận và gan (thải qua cả hai)",
          "Đường huyết (ở bệnh nhân đái tháo đường)",
          "Triệu chứng mệt mỏi, chóng mặt, lạnh tay chân"
      ],
      "precautions": [
          "KHÔNG được ngừng đột ngột (có thể gây rebound hypertension, đau thắt ngực nặng, suy tim nặng). Phải giảm liều dần trong 1-2 tuần",
          "Khởi đầu với liều thấp (1.25mg/ngày) ở bệnh nhân suy tim, tăng dần mỗi 2-4 tuần",
          "Thận trọng ở bệnh nhân hen phế quản/COPD (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản)",
          "Tránh dùng trong suy tim cấp không bù, block AV độ 2-3, nhịp tim chậm <60 bpm",
          "Thận trọng ở bệnh nhân suy thận hoặc suy gan nặng",
          "Thận trọng khi dùng với verapamil/diltiazem (tăng nguy cơ block AV, suy tim)"
      ],
      "pharmacokinetics": {
          "half_life": "9-12 giờ (dài, cho phép uống 1 lần/ngày)",
          "onset": "1-2 giờ (PO)",
          "duration": "24 giờ",
          "protein_binding": "30%",
          "clearance": "Thận (50%) và gan (50%) - chuyển hóa qua CYP3A4 và CYP2D6"
      },
      "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
      "black_box_warnings": "KHÔNG được ngừng đột ngột ở bệnh nhân đau thắt ngực hoặc suy tim - có thể gây đau thắt ngực nặng, nhồi máu cơ tim, suy tim nặng. Phải giảm liều dần dần trong 1-2 tuần",
      "drug_interactions": {
          "major": [
              {
                  "drug": "Verapamil, Diltiazem",
                  "mechanism": "Tác dụng hiệp đồng ức chế dẫn truyền nhĩ thất",
                  "effect": "Tăng nguy cơ block nhĩ thất độ 2-3, suy tim, nhịp tim chậm nặng",
                  "management": "Thận trọng. Theo dõi ECG, nhịp tim, huyết áp. Tránh dùng cùng nếu có thể."
              },
              {
                  "drug": "Clonidine (khi ngừng đột ngột)",
                  "mechanism": "Cả hai đều ức chế giao cảm, ngừng clonidine đột ngột gây rebound hypertension",
                  "effect": "Tăng huyết áp nghiêm trọng, có thể gây đột quỵ",
                  "management": "Không ngừng clonidine đột ngột khi đang dùng bisoprolol. Giảm liều clonidine dần."
              }
          ],
          "moderate": [
              {
                  "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, erythromycin)",
                  "mechanism": "Ức chế chuyển hóa bisoprolol qua CYP3A4",
                  "effect": "Tăng nồng độ bisoprolol, tăng tác dụng phụ",
                  "management": "Thận trọng. Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều bisoprolol."
              },
              {
                  "drug": "CYP2D6 inhibitors (fluoxetine, paroxetine, quinidine)",
                  "mechanism": "Ức chế chuyển hóa bisoprolol qua CYP2D6",
                  "effect": "Tăng nồng độ bisoprolol, tăng tác dụng phụ",
                  "management": "Thận trọng. Theo dõi nhịp tim, huyết áp. Có thể cần giảm liều bisoprolol."
              },
              {
                  "drug": "Insulin, Sulfonylureas",
                  "mechanism": "Che dấu triệu chứng hạ đường huyết",
                  "effect": "Hạ đường huyết nặng, khó nhận biết triệu chứng",
                  "management": "Theo dõi đường huyết thường xuyên."
              },
              {
                  "drug": "Digoxin",
                  "mechanism": "Tăng nguy cơ block nhĩ thất",
                  "effect": "Nhịp tim chậm nặng, block AV",
                  "management": "Theo dõi nhịp tim, ECG. Có thể cần giảm liều digoxin."
              }
          ],
          "minor": [
              {
                  "drug": "NSAIDs",
                  "mechanism": "Giảm tác dụng hạ huyết áp",
                  "effect": "Giảm hiệu quả hạ huyết áp",
                  "management": "Theo dõi huyết áp."
              }
          ]
      },
      "contraindications": {
          "tuyệt_đối": [
              "Hen phế quản nặng",
              "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
              "Suy tim cấp không bù",
              "Nhịp tim chậm nặng (<60 bpm)",
              "Sốc tim"
          ],
          "tương_đối": [
              "COPD - thận trọng (mặc dù chọn lọc beta-1, vẫn có thể gây co thắt phế quản)",
              "Suy thận nặng (CrCl <30) - giảm liều, thận trọng",
              "Suy gan nặng - giảm liều, thận trọng (thải qua cả thận và gan)",
              "Đái tháo đường - thận trọng (che dấu triệu chứng hạ đường huyết)",
              "Dùng với verapamil/diltiazem - tăng nguy cơ block AV",
              "Dùng với CYP3A4 hoặc CYP2D6 inhibitors - tăng nồng độ bisoprolol"
          ]
      },
      "pregnancy_lactation": {
          "fda_category": "C",
          "pregnancy_details": "Có thể gây hạ huyết áp, nhịp tim chậm ở thai nhi. Có thể gây chậm phát triển thai nhi, nhịp tim chậm ở trẻ sơ sinh. Cân nhắc lợi ích/nguy cơ. Thường dùng được nếu lợi ích vượt trội nguy cơ, đặc biệt trong suy tim.",
          "lactation": {
              "safety": "Compatible",
              "details": "Bisoprolol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Có thể gây nhịp tim chậm nhẹ ở trẻ bú mẹ nhưng hiếm.",
              "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có nhịp tim chậm, mệt mỏi, tăng cân kém."
          }
      },
      "hepatic_adjustment": {
          "mild": "Không đổi",
          "moderate": "Thận trọng, giảm liều (thải 50% qua gan)",
          "severe": "Thận trọng, giảm liều (thải 50% qua gan)",
          "notes": "Bisoprolol thải qua cả thận (50%) và gan (50%, chuyển hóa qua CYP3A4 và CYP2D6). Suy gan có thể làm tăng nồng độ bisoprolol."
      },
      "overdose_management": {
          "symptoms": [
              "Nhịp tim chậm nặng (<40 bpm)",
              "Block nhĩ thất độ 2-3",
              "Hạ huyết áp nặng",
              "Suy tim cấp",
              "Co giật",
              "Hôn mê",
              "Suy hô hấp"
          ],
          "antidote": "Glucagon (có thể đảo ngược tác dụng beta-blocker), Atropine (cho nhịp tim chậm), Epinephrine (cho hạ huyết áp nặng)",
          "treatment": [
              "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
              "Than hoạt tính",
              "Điều trị nhịp tim chậm: Atropine 0.5-1mg IV, có thể lặp lại. Nếu không hiệu quả: Glucagon 1-5mg IV, Isoproterenol, hoặc máy tạo nhịp tạm thời",
              "Điều trị hạ huyết áp: Truyền dịch (normal saline), nâng chân, Glucagon 1-5mg IV, Epinephrine (thận trọng)",
              "Theo dõi ECG liên tục",
              "Theo dõi huyết áp, nhịp tim, ý thức",
              "Hỗ trợ hô hấp nếu cần",
              "Theo dõi ít nhất 24-48 giờ (do half-life 9-12 giờ)"
          ],
          "monitoring": "ECG liên tục, huyết áp, nhịp tim, ý thức, dấu hiệu suy tim, dấu hiệu suy hô hấp"
      },
      "reversal_agents": {
          "available": True,
          "agents": [
              {
                  "name": "Glucagon",
                  "mechanism": "Kích thích cAMP, đảo ngược tác dụng beta-blocker",
                  "dose": "1-5mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, hạ huyết áp do quá liều beta-blocker"
              },
              {
                  "name": "Atropine",
                  "mechanism": "Chẹn muscarinic, tăng nhịp tim",
                  "dose": "0.5-1mg IV, có thể lặp lại",
                  "indication": "Nhịp tim chậm, block AV"
              },
              {
                  "name": "Epinephrine",
                  "mechanism": "Agonist alpha và beta, tăng nhịp tim và huyết áp",
                  "dose": "Theo protocol ACLS",
                  "indication": "Hạ huyết áp nặng không đáp ứng với glucagon"
              }
          ]
      },
      "administration_instructions": {
          "oral": {
              "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
              "timing": "Uống 1 lần/ngày vào cùng một giờ mỗi ngày. Ở bệnh nhân suy tim: khởi đầu với liều thấp (1.25mg/ngày), tăng dần mỗi 2-4 tuần. KHÔNG ngừng đột ngột - phải giảm liều dần trong 1-2 tuần."
          },
          "iv": {
              "reconstitution": "Không có dạng IV",
              "infusion_rate": "Không áp dụng",
              "compatibility": [],
              "incompatibility": [],
              "notes": "Bisoprolol chỉ có dạng uống (PO)."
          }
      },
      "pediatric_dosing": {
          "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
          "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế)",
          "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế). Nếu cần, 0.1-0.2mg/kg/ngày x 1 lần, tối đa 10mg/ngày",
          "adolescents": "1.25-2.5mg x 1 lần/ngày, tăng dần đến 5-10mg/ngày nếu cần. Liều người lớn",
          "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng khi thực sự cần thiết. Theo dõi nhịp tim, huyết áp, chức năng thận và gan chặt chẽ"
      },
      "geriatric_dosing": {
          "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (nhịp tim chậm, hạ huyết áp, mệt mỏi). Suy thận và suy gan phổ biến hơn",
          "dose_adjustment": "Khởi đầu với liều thấp hơn (1.25mg x 1 lần/ngày). Tăng dần chậm hơn. Điều chỉnh theo chức năng thận và gan",
          "monitoring": "Theo dõi nhịp tim, huyết áp sát hơn. Theo dõi chức năng thận và gan. Cảnh báo về không ngừng đột ngột"
      },
      "brand_names": {
          "vietnam": ["Concor", "Bisoprolol Stada", "Bisoprolol", "Zebeta"],
          "common": ["Zebeta", "Concor", "Bisoprolol"]
      },
      "cost_estimate": {
          "unit": "VND",
          "range": "10,000 - 30,000 VND/viên (tùy hàm lượng và thương hiệu)",
          "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Bisoprolol generic thường rẻ hơn (10,000-20,000 VND/viên 5mg)."
      },
      "references": {
          "primary_sources": [
              "FDA Drug Label - Zebeta (bisoprolol)",
              "UpToDate - Bisoprolol: Drug information",
              "CIBIS-II Study - Lancet (1999) - Bisoprolol trong suy tim",
              "American Heart Association/American College of Cardiology guidelines - Beta-blockers in heart failure"
          ],
          "last_updated": "2024-12-19",
          "evidence_level": "High - Large RCT (CIBIS-II) showing mortality benefit in heart failure and extensive clinical experience"
      }
    }
}

__all__ = ['SELECTIVE_BETA_BLOCKERS']
